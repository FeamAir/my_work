# Отчёт IT-специалиста — 2026-11-22

**Задача:** каркас производственного пайплайна (fal.ai, ElevenLabs, R2, учёт расходов, сборка ffmpeg, проверка сервисов).
**Условия:** из shell нет интернета, pip install не работает, ключей нет. Реальных сетевых и платных вызовов не было.

## Среда
- Python 3.13.18, ffmpeg/ffprobe 6.1.1 (libx264, aac, libmp3lame, sidechaincompress, loudnorm — есть).
- Установлено: `requests` 2.34.2, `python-dotenv`. **Нет** `boto3`, `httpx`.
- Поэтому R2 работает через `boto3`, если он установлен, иначе через встроенный клиент S3 (подпись SigV4 на `requests`).

## Что сделано
| Файл | Содержимое |
|---|---|
| `.env.example` | все ключи с комментариями (что обязательно и где взять) + `BUDGET_LIMIT_USD=20`, `STUDIO_ALLOW_PAID=0` |
| `.gitignore` (новый, в корне) | `.env`, `.env.*` (кроме `.env.example`), `output/`, `__pycache__/`, `.idea/`, venv |
| `requirements.txt` | requests (обязательно), python-dotenv, boto3 (необязательно) |
| `pipeline/config.py` | ключи из окружения + автозагрузка `.env`; `MissingConfigError` с подсказкой; `mask()` для логов |
| `pipeline/net.py` | HTTP с ретраями (429/5xx), потоковое скачивание; платные POST без ретраев (чтобы не заплатить дважды) |
| `pipeline/costs.py` | таблица цен, `guard()` (разрешение и бюджет до вызова), `log()` в `output/costs.jsonl`, сводка |
| `pipeline/fal_client.py` | очередь queue.fal.run: submit → status → result → скачивание; `generate_image` (Nano Banana / 2, с референсами → /edit), `image_to_video` (Kling 2.5 Turbo Pro, Kling 3 Pro, MiniMax H3 Max Turbo); локальные картинки уходят как data URI |
| `pipeline/elevenlabs_client.py` | `tts` (voice_id, текст, модель, voice_settings, previous/next_text), `sfx`, `music`; mp3 или wav (pcm→WAV); бесплатные `subscription()`, `list_voices()` |
| `pipeline/storage.py` | R2: upload / download / ls / delete / presigned URL; endpoint `https://<account>.r2.cloudflarestorage.com`, регион `auto` |
| `pipeline/assemble.py` | сборка серии по JSON: склейка клипов (приведение к 1920×1080/24fps), дорожки dialog/sfx/music со стартом, громкостью, loop, fade; приглушение музыки под диалогами; loudnorm −16 LUFS; H.264+AAC; `--dry-run`, `--selftest` |
| `pipeline/check_services.py` | без флага: переменные + python/ffmpeg/библиотеки; `--live`: DNS/HTTPS к хостам + бесплатные тестовые вызовы (fal auth probe, ElevenLabs subscription, R2 ListObjects, Anthropic /v1/models, Gemini /v1beta/models) |
| `pipeline/README.md` | инструкция |
| `pipeline/tests/test_offline.py` | 18 офлайн-тестов (HTTP замокан) |

Защита от расходов: любой платный вызов падает с `PaidCallsDisabled`, пока не задано `STUDIO_ALLOW_PAID=1`, и с `BudgetExceeded`, если «потрачено + оценка» > `BUDGET_LIMIT_USD`. Обе проверки срабатывают **до** отправки запроса.

## Что протестировано (локально)
- `python3 -m pipeline.assemble --selftest`: **пройдено.** 3 синтетических клипа (1280×720@30, 640×480@25 со звуком, 1920×1080@24) + 2 диалога (wav/mp3) + SFX + зацикленная музыка с фейдами → `output/selftest/episode_selftest.mp4`: h264 1920×1080 24fps, AAC 48 kHz stereo, длительность 6.000 с (ожидалось 6.0). Громкость на диалоге −15.5 dB, только музыка −27.4 dB: уровни и приглушение работают.
- `python3 -m unittest pipeline.tests.test_offline`: **18/18 OK.** В том числе:
  - подпись SigV4 и presigned URL совпадают с официальными тестовыми примерами AWS. Значит, встроенный клиент R2 подписывает запросы правильно;
  - полный цикл fal (submit → IN_PROGRESS → COMPLETED → result → скачивание) на моках, формат заголовка `Authorization: Key …`;
  - бюджет: блокировка до submit, ошибочные вызовы стоят $0, лог `costs.jsonl`;
  - ElevenLabs: URL/параметры TTS, упаковка pcm в WAV, подсчёт символов;
  - config: текст ошибки при отсутствии ключа, парсер `.env`, маскирование.
- `python3 -m pipeline.check_services` (без `--live`): работает, корректно показывает отсутствие всех ключей (exit 1 — ожидаемо).
- CLI `fal_client image` без разрешения → `PaidCallsDisabled` (платный вызов заблокирован).

## Что НЕ проверено (нет сети и ключей)
- Ни одного реального запроса к fal.ai, ElevenLabs, R2, Anthropic и Gemini не было: формат ответов взят из моих знаний API.
- `check_services --live` не запускался.
- Ветка `storage` через `boto3` не проверялась: boto3 не установлен. Проверялся только встроенный клиент, и только на моках.
- Цены — оценки из задания; реальное списание не сверялось.

## TODO (проверить по docs / при первом live-запуске)
1. **fal, ID эндпоинтов (проверить по docs):** `fal-ai/kling-video/v3/pro/image-to-video`, `fal-ai/minimax/hailuo-03/max-turbo/image-to-video` (MiniMax H3 Max Turbo), `fal-ai/nano-banana-2` и `/edit`. Также допустимые `duration` для Kling 3 / MiniMax и поддержка `aspect_ratio` у nano-banana.
2. **fal:** как выглядит ошибка модели в статусе COMPLETED; есть ли официальный бесплатный способ проверить ключ (сейчас — GET статуса фиктивного request_id: 401/403 = ключ отклонён); домены CDN результатов.
3. **fal:** лимит размера data URI. Для больших референсов — загрузка в R2 + presigned URL (функция есть) или fal storage upload.
4. **ElevenLabs Music:** эндпоинт `/v1/music`, поля `music_length_ms`, `model_id=music_v1`, `force_instrumental`, тарификация (проверить по docs).
5. **ElevenLabs:** стоимость SFX в кредитах (заложено ~40/сек), нужен ли тариф Pro для `pcm_44100` (wav), диапазон `speed`, параметр `loop` у SFX.
6. **ElevenLabs:** задать `ELEVENLABS_USD_PER_CREDIT` по фактическому плану.
7. **Липсинк** (fal) — не реализован, нужен выбор модели от режиссёра или директора.
8. `pip install -r requirements.txt` (boto3 для multipart-загрузки больших файлов в R2).
9. После выдачи ключей: `python3 -m pipeline.check_services --live`. Вызовы бесплатные, кроме R2 ListObjects: это операция класса A, она в пределах бесплатного лимита.

## Блокеры
- Нет ключей: FAL_KEY, ELEVENLABS_API_KEY, R2_* (ACCOUNT_ID, ACCESS_KEY_ID, SECRET_ACCESS_KEY), ANTHROPIC_API_KEY; GEMINI_API_KEY необязателен.
- Из shell нет интернета: нельзя запустить live-проверку и `pip install`.
- Для первого платного теста нужно разрешение директора (`STUDIO_ALLOW_PAID=1`) и лимит бюджета.

## Примечание для директора
Создан `.gitignore` в корне (раньше его не было). В нём также игнорируется `.idea/`: в рабочем дереве `.idea/*` уже помечены удалёнными. Папка `output/` (selftest) в git не попадёт.
