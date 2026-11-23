"""Клиент fal.ai через очередь (queue.fal.run): submit -> status -> result.

    POST https://queue.fal.run/{endpoint}                 -> {request_id, status_url, response_url, ...}
    GET  {status_url}  (…/requests/{id}/status)           -> {status: IN_QUEUE|IN_PROGRESS|COMPLETED, ...}
    GET  {response_url} (…/requests/{id})                 -> выход модели (images[] / video)
    Заголовок: Authorization: Key $FAL_KEY

Использование:
    from pipeline import fal_client
    img = fal_client.generate_image("anime girl on a rooftop at dusk", "output/shot01.png")
    vid = fal_client.image_to_video("output/shot01.png", "she turns her head", "output/shot01.mp4",
                                    model="kling-2.5-turbo-pro", duration=5)

Каждый вызов проходит costs.guard (разрешение + бюджет) и пишется в output/costs.jsonl.
"""
from __future__ import annotations

import argparse
import base64
import mimetypes
import time
from pathlib import Path
from typing import Any

from . import config, costs
from .net import ApiError, download, request

QUEUE_BASE = "https://queue.fal.run"

# Логическое имя -> endpoint fal. Ключи совпадают с costs.PRICES.
# TODO(проверить по docs): точные ID эндпоинтов Kling 3 Pro, MiniMax H3 Max Turbo,
# Nano Banana 2 и их параметры на https://fal.ai/models — ниже предположения.
IMAGE_MODELS: dict[str, str] = {
    "nano-banana": "fal-ai/nano-banana",
    "nano-banana-edit": "fal-ai/nano-banana/edit",
    "nano-banana-2": "fal-ai/nano-banana-2",  # проверено по OpenAPI fal 2026-11-23
    "nano-banana-2-edit": "fal-ai/nano-banana-2/edit",
    "nano-banana-pro": "fal-ai/nano-banana-pro",  # проверено по OpenAPI fal 2026-11-23
    "nano-banana-pro-edit": "fal-ai/nano-banana-pro/edit",
}
VIDEO_MODELS: dict[str, str] = {
    "kling-2.5-turbo-pro": "fal-ai/kling-video/v2.5-turbo/pro/image-to-video",
    "kling-3-pro": "fal-ai/kling-video/v3/pro/image-to-video",  # TODO проверить по docs
    "minimax-h3-max-turbo": "fal-ai/minimax/hailuo-03/max-turbo/image-to-video",  # TODO проверить по docs
}

# Разрешённые длительности (сек). Kling принимает строку "5" / "10".
# TODO(проверить по docs): допустимые duration для Kling 3 Pro и MiniMax H3.
VIDEO_DURATIONS: dict[str, tuple[int, ...]] = {
    "kling-2.5-turbo-pro": (5, 10),
    "kling-3-pro": (5, 10),
    "minimax-h3-max-turbo": (6, 10),
}

TERMINAL_OK = "COMPLETED"
POLL_INTERVAL = 3.0


def _headers() -> dict[str, str]:
    return {"Authorization": f"Key {config.get('FAL_KEY')}", "Content-Type": "application/json"}


def to_image_url(image: str | Path) -> str:
    """http(s)-URL возвращается как есть; локальный файл -> data URI (base64).

    fal принимает data URI в полях *_url. Для больших файлов (>~10 МБ) лучше
    сначала загрузить в R2 и передать presigned URL (storage.presigned_url).
    """
    s = str(image)
    if s.startswith(("http://", "https://", "data:")):
        return s
    p = Path(s)
    mime = mimetypes.guess_type(p.name)[0] or "image/png"
    return f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"


# ---------------------------------------------------------------- очередь ---

def submit(endpoint: str, payload: dict[str, Any]) -> dict:
    """Поставить задачу в очередь. Ретраев нет, чтобы не оплатить дважды."""
    resp = request("POST", f"{QUEUE_BASE}/{endpoint}", service="fal.submit",
                   headers=_headers(), json=payload, retries=1)
    data = resp.json()
    if "request_id" not in data:
        raise ApiError("fal.submit", resp.status_code, resp.text)
    return data


def _app_base(endpoint: str) -> str:
    # Для вложенных эндпоинтов статус/результат живут на уровне приложения:
    # fal-ai/kling-video/v2.5-turbo/pro/image-to-video -> fal-ai/kling-video
    parts = endpoint.split("/")
    return "/".join(parts[:2])


def status(endpoint: str, request_id: str, status_url: str | None = None, logs: bool = False) -> dict:
    url = status_url or f"{QUEUE_BASE}/{_app_base(endpoint)}/requests/{request_id}/status"
    resp = request("GET", url, service="fal.status", headers=_headers(),
                   params={"logs": 1} if logs else None)
    return resp.json()


def result(endpoint: str, request_id: str, response_url: str | None = None) -> dict:
    url = response_url or f"{QUEUE_BASE}/{_app_base(endpoint)}/requests/{request_id}"
    return request("GET", url, service="fal.result", headers=_headers()).json()


def run(endpoint: str, payload: dict[str, Any], *, timeout_s: float = 900,
        on_status=None) -> tuple[str, dict]:
    """submit -> ждать COMPLETED -> result. Возвращает (request_id, output)."""
    sub = submit(endpoint, payload)
    rid = sub["request_id"]
    deadline = time.monotonic() + timeout_s
    while True:
        st = status(endpoint, rid, sub.get("status_url"))
        state = st.get("status")
        if on_status:
            on_status(st)
        if state == TERMINAL_OK:
            # TODO(проверить по docs): при ошибке модели fal может вернуть COMPLETED с полем error
            if st.get("error"):
                raise ApiError("fal.run", 500, str(st.get("error")))
            break
        if state not in ("IN_QUEUE", "IN_PROGRESS"):
            raise ApiError("fal.run", 500, f"неожиданный статус {state}: {st}")
        if time.monotonic() > deadline:
            raise TimeoutError(f"fal {endpoint} {rid}: не завершилось за {timeout_s} с")
        time.sleep(POLL_INTERVAL)
    return rid, result(endpoint, rid, sub.get("response_url"))


# --------------------------------------------------------------- высокоуровневое ---

def generate_image(prompt: str, out_path: str | Path, *, model: str = "nano-banana",
                   reference_images: list[str | Path] | None = None,
                   aspect_ratio: str | None = "16:9", extra: dict | None = None) -> Path:
    """Text-to-image (или edit, если переданы reference_images). Сохраняет первую картинку."""
    if reference_images and not model.endswith("-edit"):
        model = model + "-edit"
    if model not in IMAGE_MODELS:
        raise ValueError(f"Неизвестная модель картинок {model!r}; есть: {list(IMAGE_MODELS)}")
    endpoint = IMAGE_MODELS[model]
    payload: dict[str, Any] = {"prompt": prompt, "num_images": 1, "output_format": "png"}
    if aspect_ratio:
        payload["aspect_ratio"] = aspect_ratio  # поддерживается всеми nano-banana (OpenAPI fal)
    if reference_images:
        payload["image_urls"] = [to_image_url(i) for i in reference_images]
    payload.update(extra or {})

    costs.guard(model, 1)
    try:
        rid, out = run(endpoint, payload, timeout_s=300)
    except Exception as e:
        costs.log(model, 1, provider="fal", endpoint=endpoint, status=f"error: {type(e).__name__}")
        raise
    images = out.get("images") or []
    if not images:
        costs.log(model, 1, provider="fal", endpoint=endpoint, request_id=rid, status="error: no images")
        raise ApiError("fal.generate_image", 500, f"нет images в ответе: {str(out)[:300]}")
    costs.log(model, 1, provider="fal", endpoint=endpoint, request_id=rid,
              extra={"prompt": prompt[:200]})
    return download(images[0]["url"], out_path, service="fal.download")


def image_to_video(image: str | Path, prompt: str, out_path: str | Path, *,
                   model: str = "kling-2.5-turbo-pro", duration: int = 5,
                   negative_prompt: str | None = "blur, distort, low quality",
                   extra: dict | None = None) -> Path:
    """Image-to-video. Сохраняет mp4."""
    if model not in VIDEO_MODELS:
        raise ValueError(f"Неизвестная видеомодель {model!r}; есть: {list(VIDEO_MODELS)}")
    allowed = VIDEO_DURATIONS.get(model)
    if allowed and duration not in allowed:
        raise ValueError(f"{model}: duration должна быть одной из {allowed}, получено {duration}")
    endpoint = VIDEO_MODELS[model]
    payload: dict[str, Any] = {
        "prompt": prompt,
        "image_url": to_image_url(image),
        "duration": str(duration),
    }
    if model.startswith("kling") and negative_prompt:
        payload["negative_prompt"] = negative_prompt
    if model.startswith("minimax"):
        # TODO проверить по docs: у MiniMax поле prompt_optimizer, duration строкой "6"/"10"
        payload["prompt_optimizer"] = True
    payload.update(extra or {})

    costs.guard(model, duration)
    try:
        rid, out = run(endpoint, payload, timeout_s=1200)
    except Exception as e:
        costs.log(model, duration, provider="fal", endpoint=endpoint, status=f"error: {type(e).__name__}")
        raise
    video = out.get("video") or {}
    if not video.get("url"):
        costs.log(model, duration, provider="fal", endpoint=endpoint, request_id=rid, status="error: no video")
        raise ApiError("fal.image_to_video", 500, f"нет video.url в ответе: {str(out)[:300]}")
    costs.log(model, duration, provider="fal", endpoint=endpoint, request_id=rid,
              extra={"prompt": prompt[:200]})
    return download(video["url"], out_path, service="fal.download")


# TODO: липсинк (например fal-ai/sync-lipsync / kling lipsync) — после выбора модели директором.


def _cli() -> None:
    ap = argparse.ArgumentParser(description="fal.ai: картинка / image-to-video (ПЛАТНО)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("image")
    a.add_argument("prompt")
    a.add_argument("out")
    a.add_argument("--model", default="nano-banana", choices=[m for m in IMAGE_MODELS if not m.endswith("-edit")])
    a.add_argument("--ref", action="append", help="референс (путь или URL), можно несколько")
    a.add_argument("--aspect", default="16:9")
    b = sub.add_parser("video")
    b.add_argument("image")
    b.add_argument("prompt")
    b.add_argument("out")
    b.add_argument("--model", default="kling-2.5-turbo-pro", choices=list(VIDEO_MODELS))
    b.add_argument("--duration", type=int, default=5)
    args = ap.parse_args()
    if args.cmd == "image":
        print(generate_image(args.prompt, args.out, model=args.model, reference_images=args.ref,
                             aspect_ratio=args.aspect))
    else:
        print(image_to_video(args.image, args.prompt, args.out, model=args.model, duration=args.duration))


if __name__ == "__main__":
    _cli()
