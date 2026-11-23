"""Проверка готовности пайплайна.

    python3 -m pipeline.check_services          # только переменные окружения + локальные инструменты
    python3 -m pipeline.check_services --live   # + сетевой доступ к хостам + бесплатные тестовые вызовы API

Тестовые вызовы с --live не тарифицируются (информация об аккаунте / список моделей):
    fal.ai      — GET статуса несуществующей задачи: 401/403 = ключ неверный, 404/422 = ключ принят
                  (TODO проверить по docs: есть ли официальный бесплатный эндпоинт проверки ключа)
    ElevenLabs  — GET /v1/user/subscription (тариф, остаток символов)
    R2          — ListObjectsV2 max-keys=1 в бакете (операция класса A, копейки/бесплатный лимит)
    Anthropic   — GET /v1/models
    Gemini      — GET /v1beta/models
Значения ключей никогда не печатаются.
"""
from __future__ import annotations

import argparse
import shutil
import socket
import subprocess
import sys
from typing import Callable

from . import config

OK, FAIL, WARN, SKIP = "OK  ", "FAIL", "WARN", "SKIP"


def _line(status: str, name: str, msg: str = "") -> None:
    print(f"[{status}] {name}" + (f" — {msg}" if msg else ""))


# ------------------------------------------------------------- переменные ---

def check_env() -> bool:
    print("== Переменные окружения ==")
    ok = True
    for name, (required, desc, _where) in config.KEYS.items():
        val = config.get(name, required=False)
        if val:
            shown = val if name in ("R2_BUCKET",) else config.mask(val)
            _line(OK, name, f"{desc}: задано {shown}")
        elif required:
            ok = False
            _line(FAIL, name, f"{desc}: НЕ ЗАДАНО")
        else:
            _line(WARN, name, f"{desc}: не задано (необязательно)")
    limit = config.budget_limit_usd()
    _line(OK if limit else WARN, "BUDGET_LIMIT_USD", f"${limit:.2f}" if limit else "лимит не задан!")
    _line(OK, "STUDIO_ALLOW_PAID", "платные вызовы РАЗРЕШЕНЫ" if config.paid_calls_allowed()
          else "платные вызовы запрещены (по умолчанию)")
    return ok


def check_tools() -> bool:
    print("== Локальные инструменты ==")
    ok = True
    _line(OK if sys.version_info >= (3, 10) else FAIL, "python", sys.version.split()[0])
    ok &= sys.version_info >= (3, 10)
    for tool in ("ffmpeg", "ffprobe"):
        path = shutil.which(tool)
        if path:
            ver = subprocess.run([tool, "-version"], capture_output=True, text=True).stdout.split("\n")[0]
            _line(OK, tool, ver[:60])
        else:
            ok = False
            _line(FAIL, tool, "не найден в PATH")
    for mod, required in (("requests", True), ("boto3", False), ("dotenv", False)):
        try:
            m = __import__(mod)
            _line(OK, mod, getattr(m, "__version__", "установлен"))
        except ImportError:
            if required:
                ok = False
            _line(FAIL if required else WARN, mod,
                  "не установлен" + ("" if required else " (необязательно, есть встроенная замена)"))
    return ok


# ------------------------------------------------------------------ сеть ---

def hosts() -> dict[str, str]:
    acct = config.get("R2_ACCOUNT_ID", required=False)
    h = {
        "fal (queue)": "queue.fal.run",
        "fal (cdn)": "v3.fal.media",  # результаты отдаются с поддоменов (v3/v3b.fal.media); корень fal.media не резолвится
        "ElevenLabs": "api.elevenlabs.io",
        "Anthropic": "api.anthropic.com",
        "Gemini": "generativelanguage.googleapis.com",
    }
    h["R2"] = f"{acct}.r2.cloudflarestorage.com" if acct else "r2.cloudflarestorage.com"
    return h


def check_network(timeout: float = 5.0) -> bool:
    """DNS + HTTPS-запрос HEAD к каждому хосту (через прокси окружения, если он задан)."""
    import requests
    print("== Сетевой доступ ==")
    ok = True
    for name, host in hosts().items():
        try:
            socket.getaddrinfo(host, 443)
            dns = "DNS ok"
        except OSError as e:
            dns = f"DNS fail ({e.__class__.__name__})"
        try:
            r = requests.head(f"https://{host}/", timeout=timeout, allow_redirects=False)
            _line(OK, name, f"{host}: {dns}, HTTPS {r.status_code}")
        except requests.RequestException as e:
            ok = False
            _line(FAIL, name, f"{host}: {dns}, HTTPS недоступен ({e.__class__.__name__})")
    return ok


# ---------------------------------------------------------- тест-вызовы ---

def _probe_fal() -> str:
    import requests
    key = config.get("FAL_KEY")
    url = "https://queue.fal.run/fal-ai/nano-banana/requests/00000000-0000-0000-0000-000000000000/status"
    r = requests.get(url, headers={"Authorization": f"Key {key}"}, timeout=15)
    if r.status_code in (401, 403):
        raise RuntimeError(f"ключ отклонён (HTTP {r.status_code})")
    return f"ключ принят (HTTP {r.status_code} на фиктивный request_id — ожидаемо)"


def _probe_elevenlabs() -> str:
    from .elevenlabs_client import subscription
    s = subscription()
    used, limit = s.get("character_count"), s.get("character_limit")
    return f"тариф {s.get('tier')}, использовано {used}/{limit} символов/кредитов"


def _probe_r2() -> str:
    from . import storage
    objs = storage.list_objects(max_keys=1)
    impl = "boto3" if storage.HAVE_BOTO3 else "встроенный SigV4"
    return f"бакет {storage.bucket()} доступен ({impl}), объектов в выборке: {len(objs)}"


def _probe_anthropic() -> str:
    import requests
    r = requests.get("https://api.anthropic.com/v1/models",
                     headers={"x-api-key": config.get("ANTHROPIC_API_KEY"),
                              "anthropic-version": "2023-06-01"}, timeout=15)
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")
    return f"моделей доступно: {len(r.json().get('data', []))}"


def _probe_gemini() -> str:
    import requests
    r = requests.get("https://generativelanguage.googleapis.com/v1beta/models",
                     headers={"x-goog-api-key": config.get("GEMINI_API_KEY")}, timeout=15)
    if r.status_code != 200:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")
    return f"моделей доступно: {len(r.json().get('models', []))}"


PROBES: list[tuple[str, tuple[str, ...], Callable[[], str], bool]] = [
    ("fal.ai", ("FAL_KEY",), _probe_fal, True),
    ("ElevenLabs", ("ELEVENLABS_API_KEY",), _probe_elevenlabs, True),
    ("Cloudflare R2", ("R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY"), _probe_r2, True),
    ("Anthropic", ("ANTHROPIC_API_KEY",), _probe_anthropic, True),
    ("Gemini", ("GEMINI_API_KEY",), _probe_gemini, False),
]


def check_apis() -> bool:
    print("== Тестовые вызовы API (бесплатные) ==")
    ok = True
    for name, keys, fn, required in PROBES:
        if not all(config.get(k, required=False) for k in keys):
            _line(SKIP if not required else FAIL, name, "нет ключа")
            ok &= not required
            continue
        try:
            _line(OK, name, fn())
        except Exception as e:  # noqa: BLE001 — показываем любую причину, без ключей
            ok &= not required
            _line(FAIL if required else WARN, name, f"{e.__class__.__name__}: {str(e)[:200]}")
    return ok


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Проверка ключей и доступа к сервисам")
    ap.add_argument("--live", action="store_true",
                    help="также проверить сеть и сделать бесплатные тестовые вызовы API")
    args = ap.parse_args(argv)
    ok = check_env()
    ok &= check_tools()
    if args.live:
        ok &= check_network()
        ok &= check_apis()
    else:
        print("(сеть и API не проверялись — запустите с --live)")
    print("== ИТОГ:", "ГОТОВО" if ok else "ЕСТЬ ПРОБЛЕМЫ", "==")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
