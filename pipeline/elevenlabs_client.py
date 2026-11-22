"""Клиент ElevenLabs: TTS, звуковые эффекты (SFX), музыка.

База: https://api.elevenlabs.io, заголовок xi-api-key.
    TTS:   POST /v1/text-to-speech/{voice_id}?output_format=mp3_44100_128
    SFX:   POST /v1/sound-generation
    Music: POST /v1/music                         (TODO проверить по docs)
    Info:  GET  /v1/user/subscription, GET /v1/voices (бесплатно)

Форматы: "mp3" (mp3_44100_128) или "wav" — запрашивается pcm_44100 и
оборачивается в WAV-заголовок локально (TODO проверить по docs: pcm_44100
может требовать тариф Pro; иначе используйте mp3).

Стоимость оценивается в кредитах (см. costs.PRICES, ELEVENLABS_USD_PER_CREDIT).
"""
from __future__ import annotations

import argparse
import wave
from pathlib import Path

from . import config, costs
from .net import request

API_BASE = "https://api.elevenlabs.io"

DEFAULT_TTS_MODEL = "eleven_multilingual_v2"
# Модели с половинной ценой за символ. TODO проверить по docs/pricing.
HALF_PRICE_MODELS = {"eleven_flash_v2_5", "eleven_flash_v2", "eleven_turbo_v2_5", "eleven_turbo_v2"}
SFX_CREDITS_PER_SECOND = 40  # TODO проверить по docs (оценка)
SFX_DEFAULT_SECONDS = 5      # если длительность не задана — для оценки

FORMATS = {
    "mp3": "mp3_44100_128",
    "wav": "pcm_44100",
}


def _headers(accept: str = "audio/mpeg") -> dict[str, str]:
    return {"xi-api-key": config.get("ELEVENLABS_API_KEY"), "Content-Type": "application/json",
            "Accept": accept}


def _save(content: bytes, out_path: str | Path, fmt: str, sample_rate: int = 44100) -> Path:
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    if fmt == "wav":
        # pcm_44100 = сырой 16-bit little-endian mono
        with wave.open(str(out), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(sample_rate)
            w.writeframes(content)
    else:
        out.write_bytes(content)
    return out


def _fmt_from_path(out_path: str | Path, fmt: str | None) -> str:
    if fmt:
        if fmt not in FORMATS:
            raise ValueError(f"формат {fmt!r} не поддерживается; есть {list(FORMATS)}")
        return fmt
    return "wav" if str(out_path).lower().endswith(".wav") else "mp3"


def tts_credits(text: str, model_id: str) -> float:
    return len(text) * (0.5 if model_id in HALF_PRICE_MODELS else 1.0)


def tts(text: str, voice_id: str, out_path: str | Path, *, model_id: str = DEFAULT_TTS_MODEL,
        fmt: str | None = None, stability: float = 0.5, similarity_boost: float = 0.75,
        style: float = 0.0, speed: float | None = None, language_code: str | None = None,
        previous_text: str | None = None, next_text: str | None = None, seed: int | None = None) -> Path:
    """Озвучить реплику. previous_text/next_text улучшают интонацию в диалоге."""
    fmt = _fmt_from_path(out_path, fmt)
    credits = tts_credits(text, model_id)
    costs.guard("elevenlabs-tts", credits)
    voice_settings = {"stability": stability, "similarity_boost": similarity_boost,
                      "style": style, "use_speaker_boost": True}
    if speed is not None:
        voice_settings["speed"] = speed  # TODO проверить по docs: диапазон 0.7–1.2
    body: dict = {"text": text, "model_id": model_id, "voice_settings": voice_settings}
    for k, v in (("language_code", language_code), ("previous_text", previous_text),
                 ("next_text", next_text), ("seed", seed)):
        if v is not None:
            body[k] = v
    endpoint = f"/v1/text-to-speech/{voice_id}"
    try:
        resp = request("POST", API_BASE + endpoint, service="elevenlabs.tts", retries=1,
                       headers=_headers(), params={"output_format": FORMATS[fmt]}, json=body)
    except Exception as e:
        costs.log("elevenlabs-tts", credits, provider="elevenlabs", endpoint=endpoint,
                  status=f"error: {type(e).__name__}")
        raise
    costs.log("elevenlabs-tts", credits, provider="elevenlabs", endpoint=endpoint,
              request_id=resp.headers.get("request-id"),
              extra={"voice_id": voice_id, "model_id": model_id, "chars": len(text)})
    return _save(resp.content, out_path, fmt)


def sfx(prompt: str, out_path: str | Path, *, duration_seconds: float | None = None,
        prompt_influence: float = 0.3, loop: bool = False, fmt: str | None = None) -> Path:
    """Звуковой эффект по описанию. duration_seconds: 0.5–30 (None = авто)."""
    fmt = _fmt_from_path(out_path, fmt)
    secs = duration_seconds or SFX_DEFAULT_SECONDS
    credits = secs * SFX_CREDITS_PER_SECOND
    costs.guard("elevenlabs-sfx", credits)
    body: dict = {"text": prompt, "prompt_influence": prompt_influence}
    if duration_seconds is not None:
        body["duration_seconds"] = duration_seconds
    if loop:
        body["loop"] = True  # TODO проверить по docs: поддерживается моделью eleven_text_to_sound_v2
    endpoint = "/v1/sound-generation"
    try:
        resp = request("POST", API_BASE + endpoint, service="elevenlabs.sfx", retries=1,
                       headers=_headers(), params={"output_format": FORMATS[fmt]}, json=body)
    except Exception as e:
        costs.log("elevenlabs-sfx", credits, provider="elevenlabs", endpoint=endpoint,
                  status=f"error: {type(e).__name__}")
        raise
    costs.log("elevenlabs-sfx", credits, provider="elevenlabs", endpoint=endpoint,
              request_id=resp.headers.get("request-id"), extra={"prompt": prompt[:200]})
    return _save(resp.content, out_path, fmt)


def music(prompt: str, out_path: str | Path, *, length_seconds: float = 30,
          fmt: str | None = None, force_instrumental: bool = True) -> Path:
    """Музыкальный трек по описанию.

    TODO проверить по docs: эндпоинт /v1/music, поля prompt / music_length_ms /
    model_id="music_v1" / force_instrumental, допустимая длительность, тариф.
    """
    fmt = _fmt_from_path(out_path, fmt)
    minutes = length_seconds / 60
    costs.guard("elevenlabs-music", minutes)
    body = {"prompt": prompt, "music_length_ms": int(length_seconds * 1000), "model_id": "music_v1",
            "force_instrumental": force_instrumental}
    endpoint = "/v1/music"
    try:
        resp = request("POST", API_BASE + endpoint, service="elevenlabs.music", retries=1,
                       headers=_headers(), params={"output_format": FORMATS[fmt]}, json=body,
                       timeout=(10, 600))
    except Exception as e:
        costs.log("elevenlabs-music", minutes, provider="elevenlabs", endpoint=endpoint,
                  status=f"error: {type(e).__name__}")
        raise
    costs.log("elevenlabs-music", minutes, provider="elevenlabs", endpoint=endpoint,
              request_id=resp.headers.get("request-id"), extra={"prompt": prompt[:200]})
    return _save(resp.content, out_path, fmt)


# ------------------------------------------------------------ бесплатные ---

def subscription() -> dict:
    """Тариф и остаток символов/кредитов (бесплатный вызов)."""
    return request("GET", API_BASE + "/v1/user/subscription", service="elevenlabs.subscription",
                   headers=_headers("application/json")).json()


def list_voices() -> list[dict]:
    data = request("GET", API_BASE + "/v1/voices", service="elevenlabs.voices",
                   headers=_headers("application/json")).json()
    return [{"voice_id": v.get("voice_id"), "name": v.get("name"), "labels": v.get("labels")}
            for v in data.get("voices", [])]


def _cli() -> None:
    ap = argparse.ArgumentParser(description="ElevenLabs: TTS / SFX / музыка (ПЛАТНО); voices (бесплатно)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("tts")
    t.add_argument("voice_id")
    t.add_argument("text")
    t.add_argument("out")
    t.add_argument("--model", default=DEFAULT_TTS_MODEL)
    s = sub.add_parser("sfx")
    s.add_argument("prompt")
    s.add_argument("out")
    s.add_argument("--seconds", type=float)
    m = sub.add_parser("music")
    m.add_argument("prompt")
    m.add_argument("out")
    m.add_argument("--seconds", type=float, default=30)
    sub.add_parser("voices")
    args = ap.parse_args()
    if args.cmd == "tts":
        print(tts(args.text, args.voice_id, args.out, model_id=args.model))
    elif args.cmd == "sfx":
        print(sfx(args.prompt, args.out, duration_seconds=args.seconds))
    elif args.cmd == "music":
        print(music(args.prompt, args.out, length_seconds=args.seconds))
    else:
        for v in list_voices():
            print(v["voice_id"], v["name"], v["labels"])


if __name__ == "__main__":
    _cli()
