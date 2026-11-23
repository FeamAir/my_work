"""Учёт платных вызовов и лимит бюджета.

Каждый платный вызов:
    1. до запроса — guard(service, units): проверка разрешения (STUDIO_ALLOW_PAID=1)
       и того, что потрачено + оценка <= BUDGET_LIMIT_USD; иначе исключение;
    2. после ответа — log(...): строка в output/costs.jsonl.

Цены — ОЦЕНКИ (по данным директора студии на 2026-11-22). Фактическое
списание смотрите в биллинге fal.ai / ElevenLabs.
"""
from __future__ import annotations

import json
import threading
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from . import config


class BudgetExceeded(RuntimeError):
    """Вызов превысил бы BUDGET_LIMIT_USD."""


class BalanceFloorReached(RuntimeError):
    """Вызов опустил бы баланс сервиса ниже неприкасаемого остатка — сообщить инвестору."""


class PaidCallsDisabled(RuntimeError):
    """Платные вызовы не разрешены (STUDIO_ALLOW_PAID != 1)."""


@dataclass(frozen=True)
class Price:
    label: str
    unit: str  # "second" | "image" | "credit" | "minute"
    usd: float  # цена за единицу


# Ключи — логические имена моделей/услуг, используемые клиентами.
PRICES: dict[str, Price] = {
    # --- fal.ai, видео (за секунду ролика) ---
    "kling-2.5-turbo-pro": Price("Kling 2.5 Turbo Pro (image-to-video)", "second", 0.07),
    "kling-3-pro": Price("Kling 3 Pro (image-to-video)", "second", 0.14),
    "minimax-h3-max-turbo": Price("MiniMax H3 Max Turbo (image-to-video)", "second", 0.015),
    # --- fal.ai, картинки (за изображение) ---
    "nano-banana": Price("Nano Banana (text-to-image)", "image", 0.04),
    "nano-banana-edit": Price("Nano Banana (image edit)", "image", 0.04),
    "nano-banana-2": Price("Nano Banana 2 (text-to-image)", "image", 0.08),
    "nano-banana-2-edit": Price("Nano Banana 2 (image edit)", "image", 0.08),
    "nano-banana-pro": Price("Nano Banana Pro (text-to-image)", "image", 0.15),
    "nano-banana-pro-edit": Price("Nano Banana Pro (image edit)", "image", 0.15),
    # --- ElevenLabs: по плану, оценка через кредиты ---
    # TODO: проверить по docs/pricing текущего плана. Цена кредита задаётся
    # ELEVENLABS_USD_PER_CREDIT (Creator: $22 / 100k кредитов ~ 0.00022; overage ~0.0003).
    "elevenlabs-tts": Price("ElevenLabs TTS (1 кредит/символ; flash/turbo 0.5)", "credit", 0.0003),
    "elevenlabs-sfx": Price("ElevenLabs Sound Effects (оценка ~40 кредитов/сек)", "credit", 0.0003),
    "elevenlabs-music": Price("ElevenLabs Music (оценка, USD/мин)", "minute", 0.50),
}

_lock = threading.Lock()


def _elevenlabs_credit_usd() -> float:
    raw = config.get("ELEVENLABS_USD_PER_CREDIT", required=False, default="")
    try:
        return float(raw) if raw else PRICES["elevenlabs-tts"].usd
    except ValueError:
        return PRICES["elevenlabs-tts"].usd


def estimate(service: str, units: float) -> float:
    """Оценка стоимости в USD для `units` единиц услуги."""
    if service not in PRICES:
        raise KeyError(f"Неизвестная услуга {service!r}; добавьте цену в pipeline/costs.py PRICES")
    price = PRICES[service]
    usd = price.usd
    if price.unit == "credit":
        usd = _elevenlabs_credit_usd()
    return round(units * usd, 6)


def log_path() -> Path:
    return config.output_dir() / "costs.jsonl"


def read_log(path: Path | None = None) -> list[dict]:
    p = path or log_path()
    if not p.is_file():
        return []
    rows = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def total_spent(path: Path | None = None) -> float:
    return round(sum(float(r.get("usd_estimate", 0) or 0) for r in read_log(path)), 6)


def guard(service: str, units: float) -> float:
    """Проверить разрешение и бюджет ДО платного вызова. Возвращает оценку USD."""
    if not config.paid_calls_allowed():
        raise PaidCallsDisabled(
            f"Платный вызов {service} заблокирован: установите STUDIO_ALLOW_PAID=1 "
            f"(только с разрешения директора студии)."
        )
    est = estimate(service, units)
    limit = config.budget_limit_usd()
    if limit is not None:
        spent = total_spent()
        if spent + est > limit:
            raise BudgetExceeded(
                f"Бюджет исчерпан: потрачено ~${spent:.2f}, вызов {service} ~${est:.2f}, "
                f"лимит BUDGET_LIMIT_USD=${limit:.2f}."
            )
    _check_floor(service, est)
    return est


# ------------------------------------------------- остаток на балансе ---
# Правило инвестора (2026-11-23): баланс fal.ai не опускается ниже $20;
# при приближении — сообщить ему. Пополнения — studio/budget/balances.json.

BALANCES_PATH = config.REPO_ROOT / "studio" / "budget" / "balances.json"


def provider_of(service: str) -> str:
    return "elevenlabs" if service.startswith("elevenlabs") else "fal"


def balance_status(provider: str = "fal", path: Path | None = None) -> dict | None:
    """Оценка остатка: пополнения минус учтённые траты. None — правило не задано."""
    p = path or BALANCES_PATH
    if not p.is_file():
        return None
    cfg = json.loads(p.read_text(encoding="utf-8")).get(provider)
    if not cfg:
        return None
    spent = sum(float(r.get("usd_estimate", 0) or 0) for r in read_log()
                if r.get("provider") == provider)
    remaining = float(cfg["deposited_usd"]) - spent
    floor = float(cfg.get("floor_usd", 0))
    return {"provider": provider, "deposited_usd": float(cfg["deposited_usd"]),
            "spent_usd": round(spent, 4), "remaining_usd": round(remaining, 4),
            "floor_usd": floor, "warn": remaining - floor <= float(cfg.get("warn_margin_usd", 0))}


def _check_floor(service: str, est: float) -> None:
    st = balance_status(provider_of(service))
    if st is None:
        return
    if st["remaining_usd"] - est < st["floor_usd"]:
        raise BalanceFloorReached(
            f"Стоп: баланс {st['provider']} ~${st['remaining_usd']:.2f}, вызов {service} ~${est:.2f} "
            f"опустил бы его ниже неприкасаемых ${st['floor_usd']:.2f}. Сообщить инвестору о пополнении."
        )


def log(service: str, units: float, *, provider: str, endpoint: str = "",
        request_id: str | None = None, status: str = "ok", usd: float | None = None,
        extra: dict | None = None) -> dict:
    """Записать платный вызов в output/costs.jsonl. Для status != 'ok' стоимость 0."""
    if usd is None:
        usd = estimate(service, units) if status == "ok" else 0.0
    row = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "provider": provider,
        "service": service,
        "label": PRICES[service].label if service in PRICES else service,
        "endpoint": endpoint,
        "units": units,
        "unit": PRICES[service].unit if service in PRICES else "",
        "usd_estimate": round(usd, 6),
        "status": status,
        "request_id": request_id,
    }
    if extra:
        row["extra"] = extra
    with _lock:
        p = log_path()
        with p.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def summary(path: Path | None = None) -> dict:
    by_service: dict[str, float] = {}
    for r in read_log(path):
        by_service[r.get("service", "?")] = by_service.get(r.get("service", "?"), 0) + float(r.get("usd_estimate", 0) or 0)
    return {"total_usd": round(sum(by_service.values()), 4),
            "by_service": {k: round(v, 4) for k, v in sorted(by_service.items())},
            "limit_usd": config.budget_limit_usd(),
            "fal_balance": balance_status("fal")}


if __name__ == "__main__":
    print(json.dumps(summary(), ensure_ascii=False, indent=2))
