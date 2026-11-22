"""Производственный пайплайн AI-аниме-студии.

Модули:
    config          — ключи и настройки из окружения (.env)
    costs           — учёт платных вызовов и лимит бюджета
    fal_client      — fal.ai: картинки и image-to-video через очередь
    elevenlabs_client — ElevenLabs: TTS, SFX, музыка
    storage         — Cloudflare R2 (S3 API)
    assemble        — сборка серии через ffmpeg
    check_services  — проверка ключей и доступа к сервисам
"""

__version__ = "0.1.0"
