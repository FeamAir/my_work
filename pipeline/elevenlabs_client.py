"""Клиент ElevenLabs: TTS, звуковые эффекты (SFX), музыка.

База: https://api.elevenlabs.io, заголовок xi-api-key.
    TTS:   POST /v1/text-to-speech/{voice_id}?output_format=mp3_44100_128
    SFX:   POST /v1/sound-generation   (model_id: eleven_text_to_sound_v3 по умолчанию;
                                         v2 — вывод из эксплуатации 2027-03-01, по данным звукорежиссёра)
    Music: POST /v1/music   (model_id music_v2_5, fallback music_v2; music_v1 не используем;
                             seed — только с composition_plan)
    Info:  GET  /v1/user/subscription, GET /v1/voices (бесплатно)

Форматы: "mp3" (mp3_44100_128) или "wav" — запрашивается pcm_44100 и
оборачивается в WAV-заголовок локально (TODO проверить по docs: pcm_44100
может требовать тариф Pro; иначе используйте mp3).

Стоимость оценивается в кредитах (см. costs.PRICES, ELEVENLABS_USD_PER_CREDIT).
"""
from __future__ import annotations

import argparse
import json
import warnings
import wave
from pathlib import Path

from . import config, costs
from .net import ApiError, request

API_BASE = "https://api.elevenlabs.io"

DEFAULT_TTS_MODEL = "eleven_multilingual_v2"
# Модели с половинной ценой за символ. TODO проверить по docs/pricing.
HALF_PRICE_MODELS = {"eleven_flash_v2_5", "eleven_flash_v2", "eleven_turbo_v2_5", "eleven_turbo_v2"}
SFX_CREDITS_PER_SECOND = 40  # TODO проверить по docs (оценка; для v3 цена может отличаться)
SFX_DEFAULT_SECONDS = 5      # если длительность не задана — для оценки
SFX_MIN_SECONDS, SFX_MAX_SECONDS = 0.5, 30.0
DEFAULT_SFX_MODEL = "eleven_text_to_sound_v3"
# Известные модели SFX и дата вывода из эксплуатации (None — не объявлена).
# Источник: studio/sound/sfx_music_workflow.md §3. TODO проверить по docs ElevenLabs.
SFX_MODELS = {"eleven_text_to_sound_v3": None, "eleven_text_to_sound_v2": "2027-03-01"}
# Музыка: модель передаётся явно (решение директора 2026-11-22 по данным звукорежиссёра).
DEFAULT_MUSIC_MODEL = "music_v2_5"
MUSIC_FALLBACK_MODEL = "music_v2"
MUSIC_MODELS = (DEFAULT_MUSIC_MODEL, MUSIC_FALLBACK_MODEL)
BANNED_MUSIC_MODELS = {"music_v1"}

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


def sfx_body(prompt: str, *, duration_seconds: float | None = None, prompt_influence: float = 0.3,
             loop: bool = False, model_id: str = DEFAULT_SFX_MODEL) -> dict:
    """Тело запроса /v1/sound-generation с проверкой параметров (без сети)."""
    if not prompt or not prompt.strip():
        raise ValueError("пустой промпт SFX")
    if duration_seconds is not None and not (SFX_MIN_SECONDS <= duration_seconds <= SFX_MAX_SECONDS):
        raise ValueError(f"duration_seconds={duration_seconds}: допустимо {SFX_MIN_SECONDS}–{SFX_MAX_SECONDS} с")
    if not 0.0 <= prompt_influence <= 1.0:
        raise ValueError(f"prompt_influence={prompt_influence}: допустимо 0–1")
    if model_id not in SFX_MODELS:
        warnings.warn(f"SFX-модель {model_id!r} не из списка {list(SFX_MODELS)} — отправляю как есть",
                      stacklevel=3)
    elif SFX_MODELS[model_id]:
        warnings.warn(f"{model_id}: объявлен вывод из эксплуатации {SFX_MODELS[model_id]}; "
                      f"используйте {DEFAULT_SFX_MODEL}", DeprecationWarning, stacklevel=3)
    body: dict = {"text": prompt, "model_id": model_id, "prompt_influence": prompt_influence}
    if duration_seconds is not None:
        body["duration_seconds"] = duration_seconds
    if loop:
        body["loop"] = True  # TODO проверить по docs: поддержка loop моделью v3
    return body


def sfx(prompt: str, out_path: str | Path, *, duration_seconds: float | None = None,
        prompt_influence: float = 0.3, loop: bool = False, fmt: str | None = None,
        model_id: str = DEFAULT_SFX_MODEL) -> Path:
    """Звуковой эффект по описанию. duration_seconds: 0.5–30 (None = авто), модель — v3 по умолчанию."""
    fmt = _fmt_from_path(out_path, fmt)
    body = sfx_body(prompt, duration_seconds=duration_seconds, prompt_influence=prompt_influence,
                    loop=loop, model_id=model_id)
    secs = duration_seconds or SFX_DEFAULT_SECONDS
    credits = secs * SFX_CREDITS_PER_SECOND
    costs.guard("elevenlabs-sfx", credits)
    endpoint = "/v1/sound-generation"
    try:
        resp = request("POST", API_BASE + endpoint, service="elevenlabs.sfx", retries=1,
                       headers=_headers(), params={"output_format": FORMATS[fmt]}, json=body)
    except Exception as e:
        costs.log("elevenlabs-sfx", credits, provider="elevenlabs", endpoint=endpoint,
                  status=f"error: {type(e).__name__}")
        raise
    costs.log("elevenlabs-sfx", credits, provider="elevenlabs", endpoint=endpoint,
              request_id=resp.headers.get("request-id"),
              extra={"prompt": prompt[:200], "model_id": model_id, "seconds": duration_seconds,
                     "loop": loop, "prompt_influence": prompt_influence})
    return _save(resp.content, out_path, fmt)


def music_body(prompt: str | None = None, *, length_seconds: float | None = 30,
               composition_plan: dict | None = None, model_id: str = DEFAULT_MUSIC_MODEL,
               force_instrumental: bool = True, seed: int | None = None) -> dict:
    """Тело запроса /v1/music с проверкой параметров (без сети).

    Правила (документация ElevenLabs, по данным звукорежиссёра 2026-11-22):
      * model_id передаётся явно: music_v2_5 (по умолчанию) или music_v2; music_v1 запрещён;
      * либо prompt (+ music_length_ms), либо composition_plan (секции со своими длительностями);
      * seed работает только вместе с composition_plan.
    """
    if model_id in BANNED_MUSIC_MODELS:
        raise ValueError(f"{model_id}: не используется в студии; берите {DEFAULT_MUSIC_MODEL} или {MUSIC_FALLBACK_MODEL}")
    if model_id not in MUSIC_MODELS:
        raise ValueError(f"неизвестная модель музыки {model_id!r}; есть {MUSIC_MODELS}")
    if (prompt is None) == (composition_plan is None):
        raise ValueError("нужно ровно одно из: prompt или composition_plan")
    if seed is not None and composition_plan is None:
        raise ValueError("seed в Music работает только вместе с composition_plan")
    body: dict = {"model_id": model_id}
    if composition_plan is not None:
        body["composition_plan"] = composition_plan
        if seed is not None:
            body["seed"] = seed
    else:
        if not prompt.strip():
            raise ValueError("пустой промпт музыки")
        body["prompt"] = prompt
        if length_seconds is not None:
            body["music_length_ms"] = int(length_seconds * 1000)
        body["force_instrumental"] = force_instrumental   # TODO проверить по docs: с composition_plan не нужен
    return body


def _plan_seconds(plan: dict) -> float | None:
    """Длина composition_plan по секциям (duration_ms) — для оценки стоимости. TODO сверить схему с docs."""
    try:
        return sum(float(sec.get("duration_ms", 0)) for sec in plan.get("sections", [])) / 1000 or None
    except (AttributeError, TypeError, ValueError):
        return None


def _is_model_rejected(e: Exception) -> bool:
    """Ошибка «модель недоступна» (4xx, кроме 401/402/429) — за такой запрос денег не берут."""
    return isinstance(e, ApiError) and getattr(e, "status", None) in (400, 404, 422) and \
        "model" in str(e).lower()


def music(prompt: str | None, out_path: str | Path, *, length_seconds: float = 30,
          fmt: str | None = None, force_instrumental: bool = True,
          composition_plan: dict | None = None, seed: int | None = None,
          model_id: str = DEFAULT_MUSIC_MODEL, fallback: bool = True) -> Path:
    """Музыкальный трек: по prompt (length_seconds) или по composition_plan (+ seed).

    Модель music_v2_5; если API отклонит её как недоступную (400/404/422 с упоминанием model),
    один раз повторяем с music_v2 (fallback=False — не повторять). TODO проверить по docs
    формат ошибки и тарификацию.
    """
    fmt = _fmt_from_path(out_path, fmt)
    body = music_body(prompt, length_seconds=None if composition_plan else length_seconds,
                      composition_plan=composition_plan, model_id=model_id,
                      force_instrumental=force_instrumental, seed=seed)
    secs = (_plan_seconds(composition_plan) if composition_plan else length_seconds) or length_seconds
    minutes = secs / 60
    costs.guard("elevenlabs-music", minutes)
    endpoint = "/v1/music"
    models = [model_id] + ([MUSIC_FALLBACK_MODEL] if fallback and model_id != MUSIC_FALLBACK_MODEL else [])
    for i, mid in enumerate(models):
        body["model_id"] = mid
        try:
            resp = request("POST", API_BASE + endpoint, service="elevenlabs.music", retries=1,
                           headers=_headers(), params={"output_format": FORMATS[fmt]}, json=body,
                           timeout=(10, 600))
        except Exception as e:
            costs.log("elevenlabs-music", minutes, provider="elevenlabs", endpoint=endpoint,
                      status=f"error: {type(e).__name__}", extra={"model_id": mid})
            if i + 1 < len(models) and _is_model_rejected(e):
                continue
            raise
        costs.log("elevenlabs-music", minutes, provider="elevenlabs", endpoint=endpoint,
                  request_id=resp.headers.get("request-id"),
                  extra={"prompt": (prompt or "composition_plan")[:200], "model_id": mid, "seed": seed,
                         "seconds": secs})
        return _save(resp.content, out_path, fmt)
    raise RuntimeError("unreachable")


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
    s.add_argument("--model", default=DEFAULT_SFX_MODEL, help=f"по умолчанию {DEFAULT_SFX_MODEL}")
    s.add_argument("--influence", type=float, default=0.3, help="prompt_influence 0–1")
    s.add_argument("--loop", action="store_true", help="бесшовная петля (эмбиент)")
    m = sub.add_parser("music")
    m.add_argument("prompt")
    m.add_argument("out")
    m.add_argument("--seconds", type=float, default=30)
    m.add_argument("--model", default=DEFAULT_MUSIC_MODEL, choices=MUSIC_MODELS)
    m.add_argument("--plan", type=Path, help="JSON с composition_plan (вместо prompt; prompt = '-')")
    m.add_argument("--seed", type=int, help="только вместе с --plan")
    sub.add_parser("voices")
    args = ap.parse_args()
    if args.cmd == "tts":
        print(tts(args.text, args.voice_id, args.out, model_id=args.model))
    elif args.cmd == "sfx":
        print(sfx(args.prompt, args.out, duration_seconds=args.seconds, model_id=args.model,
                  prompt_influence=args.influence, loop=args.loop))
    elif args.cmd == "music":
        plan = json.loads(args.plan.read_text(encoding="utf-8")) if args.plan else None
        print(music(None if plan else args.prompt, args.out, length_seconds=args.seconds,
                    composition_plan=plan, seed=args.seed, model_id=args.model))
    else:
        for v in list_voices():
            print(v["voice_id"], v["name"], v["labels"])


if __name__ == "__main__":
    _cli()
