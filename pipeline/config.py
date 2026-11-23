"""Загрузка ключей и настроек из переменных окружения.

Ключи никогда не печатаются: для логов используйте mask().
.env в корне репозитория подхватывается автоматически (python-dotenv, если
установлен, иначе встроенный простой парсер). Уже заданные переменные окружения
имеют приоритет над .env.
"""
from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Переменная -> (обязательна ли, описание, где взять)
KEYS: dict[str, tuple[bool, str, str]] = {
    "FAL_KEY": (True, "fal.ai (картинки, видео)", "https://fal.ai/dashboard/keys"),
    "ELEVENLABS_API_KEY": (True, "ElevenLabs (TTS, SFX, музыка)", "https://elevenlabs.io/app/settings/api-keys"),
    "R2_ACCOUNT_ID": (True, "Cloudflare R2: ID аккаунта", "Cloudflare Dashboard -> R2 -> Overview"),
    "R2_ACCESS_KEY_ID": (True, "Cloudflare R2: Access Key ID", "R2 -> Manage R2 API Tokens"),
    "R2_SECRET_ACCESS_KEY": (True, "Cloudflare R2: Secret Access Key", "R2 -> Manage R2 API Tokens"),
    "R2_BUCKET": (True, "Cloudflare R2: имя бакета", "по умолчанию anime-studio"),
    "ANTHROPIC_API_KEY": (True, "Anthropic (агенты-LLM)", "https://console.anthropic.com/settings/keys"),
    "GEMINI_API_KEY": (False, "Google Gemini (необязательно)", "https://aistudio.google.com/apikey"),
}

DEFAULTS = {
    "R2_BUCKET": "anime-studio",
    # Ключ fal.ai хранится как «сетевой секрет» среды Claude: прокси сам подставляет
    # заголовок Authorization в запросы к queue.fal.run. В переменной — только заглушка.
    # Без прокси (локальный запуск) задайте настоящий FAL_KEY в .env.
    "FAL_KEY": "proxy-injected",
    "ELEVENLABS_API_KEY": "proxy-injected",  # тоже сетевой секрет (заголовок xi-api-key)
    "OUTPUT_DIR": "output",
}


class MissingConfigError(RuntimeError):
    """Нет обязательной переменной окружения."""


def _parse_env_file(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export "):]
        name, _, value = line.partition("=")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        elif " #" in value:
            value = value.split(" #", 1)[0].rstrip()
        result[name.strip()] = value
    return result


_loaded = False


def load_dotenv(path: Path | None = None) -> None:
    """Подгрузить .env (один раз). Не перезаписывает существующие переменные."""
    global _loaded
    if _loaded:
        return
    _loaded = True
    env_path = path or (REPO_ROOT / ".env")
    if not env_path.is_file():
        return
    try:
        from dotenv import load_dotenv as _ld  # type: ignore
        _ld(env_path, override=False)
    except ImportError:
        for k, v in _parse_env_file(env_path).items():
            os.environ.setdefault(k, v)


def get(name: str, required: bool = True, default: str | None = None) -> str | None:
    """Значение переменной. Пустая строка считается отсутствием."""
    load_dotenv()
    value = os.environ.get(name, "").strip()
    if value:
        return value
    if default is None:
        default = DEFAULTS.get(name)
    if default is not None:
        return default
    if required:
        info = KEYS.get(name)
        hint = f" ({info[1]}; где взять: {info[2]})" if info else ""
        raise MissingConfigError(
            f"Не задана переменная окружения {name}{hint}. "
            f"Добавьте её в .env (шаблон: .env.example) или экспортируйте в shell."
        )
    return None


def require(*names: str) -> dict[str, str]:
    """Проверить сразу несколько переменных; ошибка перечисляет все недостающие."""
    missing, values = [], {}
    for n in names:
        try:
            values[n] = get(n, required=True)  # type: ignore[assignment]
        except MissingConfigError:
            missing.append(n)
    if missing:
        lines = []
        for n in missing:
            info = KEYS.get(n)
            lines.append(f"  - {n}" + (f": {info[1]} (где взять: {info[2]})" if info else ""))
        raise MissingConfigError(
            "Не заданы переменные окружения:\n" + "\n".join(lines)
            + "\nЗаполните .env по шаблону .env.example."
        )
    return values


def mask(value: str | None) -> str:
    """Безопасное представление секрета для логов: только длина и последние 2 символа."""
    if not value:
        return "<пусто>"
    if len(value) <= 8:
        return "***"
    return f"***{value[-2:]} (длина {len(value)})"


def output_dir() -> Path:
    p = Path(get("OUTPUT_DIR", required=False) or "output")
    if not p.is_absolute():
        p = REPO_ROOT / p
    p.mkdir(parents=True, exist_ok=True)
    return p


def budget_limit_usd() -> float | None:
    raw = get("BUDGET_LIMIT_USD", required=False, default="")
    if not raw:
        return None
    try:
        val = float(raw)
    except ValueError as e:
        raise MissingConfigError(f"BUDGET_LIMIT_USD должно быть числом, получено {raw!r}") from e
    return val if val > 0 else None


def paid_calls_allowed() -> bool:
    return (get("STUDIO_ALLOW_PAID", required=False, default="0") or "0").strip().lower() in {"1", "true", "yes"}
