"""Общие сетевые утилиты: сессия requests с ретраями, скачивание в файл."""
from __future__ import annotations

import time
from pathlib import Path

import requests

DEFAULT_TIMEOUT = (10, 120)  # (connect, read), сек
RETRY_STATUSES = {429, 500, 502, 503, 504}


class ApiError(RuntimeError):
    def __init__(self, service: str, status: int, body: str):
        # тело обрезаем: ответы API не содержат наших ключей, но могут быть большими
        super().__init__(f"{service}: HTTP {status}: {body[:500]}")
        self.status = status
        self.body = body


def request(method: str, url: str, *, service: str, retries: int = 3,
            backoff: float = 2.0, timeout=DEFAULT_TIMEOUT, **kwargs) -> requests.Response:
    """HTTP-запрос с ретраями на 429/5xx и сетевые ошибки. Ошибки 4xx -> ApiError.

    ВНИМАНИЕ: ретраи POST безопасны только для запросов, которые не тарифицируются
    повторно при сбое соединения. Для платных submit-запросов передавайте retries=1.
    """
    last_exc: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            resp = requests.request(method, url, timeout=timeout, **kwargs)
        except (requests.ConnectionError, requests.Timeout) as e:
            last_exc = e
            if attempt == retries:
                raise
            time.sleep(backoff ** attempt)
            continue
        if resp.status_code in RETRY_STATUSES and attempt < retries:
            delay = float(resp.headers.get("Retry-After", backoff ** attempt) or backoff ** attempt)
            time.sleep(min(delay, 60))
            continue
        if resp.status_code >= 400:
            raise ApiError(service, resp.status_code, resp.text)
        return resp
    raise RuntimeError(f"{service}: запрос не удался") from last_exc


def download(url: str, dest: str | Path, *, service: str = "download", headers: dict | None = None) -> Path:
    """Скачать URL в файл потоково (через временный .part)."""
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    resp = request("GET", url, service=service, stream=True, headers=headers or {}, timeout=(10, 600))
    with tmp.open("wb") as f:
        for chunk in resp.iter_content(chunk_size=1 << 20):
            if chunk:
                f.write(chunk)
    tmp.replace(dest)
    return dest
