# pipeline/ — производственный пайплайн студии

Python 3.10+, `ffmpeg`/`ffprobe` в PATH, зависимости — `pip install -r requirements.txt`
(обязателен только `requests`; `boto3` и `python-dotenv` необязательны — есть встроенные замены).

Все команды запускаются из корня репозитория как модули: `python3 -m pipeline.<модуль>`.

## 1. Ключи

```bash
cp .env.example .env      # заполнить; .env в .gitignore, не коммитить
python3 -m pipeline.check_services          # переменные + ffmpeg/python (без сети)
python3 -m pipeline.check_services --live   # + доступ к хостам и бесплатные тест-вызовы API
```

Ключи читаются только из окружения (`pipeline/config.py`); если ключа нет — `MissingConfigError`
с подсказкой, где его взять. Значения ключей нигде не печатаются.

## 2. Деньги: разрешение и бюджет

Каждый платный вызов проходит `costs.guard()`:

* `STUDIO_ALLOW_PAID=1` — без этого любой платный вызов падает с `PaidCallsDisabled`
  (включается только с разрешения директора студии);
* `BUDGET_LIMIT_USD` — если «уже потрачено (по `output/costs.jsonl`) + оценка вызова» больше лимита,
  вызов не отправляется, выбрасывается `BudgetExceeded`.

После вызова в `output/costs.jsonl` пишется строка: время, провайдер, модель, единицы, оценка USD,
статус, request_id. Сводка: `python3 -m pipeline.costs`.

Цены (оценки, `pipeline/costs.py: PRICES`):

| Ключ | Модель | Цена |
|---|---|---|
| `kling-2.5-turbo-pro` | Kling 2.5 Turbo Pro i2v | $0.07 / сек |
| `kling-3-pro` | Kling 3 Pro i2v | $0.14 / сек |
| `minimax-h3-max-turbo` | MiniMax H3 Max Turbo i2v | $0.015 / сек |
| `nano-banana`, `nano-banana-edit` | Nano Banana | $0.04 / изобр. |
| `nano-banana-2`, `nano-banana-2-edit` | Nano Banana 2 | $0.08 / изобр. |
| `elevenlabs-tts` | ElevenLabs TTS | 1 кредит/символ (flash/turbo 0.5) × `ELEVENLABS_USD_PER_CREDIT` |
| `elevenlabs-sfx` | ElevenLabs SFX | ~40 кредитов/сек (оценка) |
| `elevenlabs-music` | ElevenLabs Music | ~$0.50 / мин (оценка) |

## 3. Генерация

```python
from pipeline import fal_client, elevenlabs_client as el, storage

# картинка (Nano Banana); с референсами автоматически используется /edit
fal_client.generate_image("anime girl on a rooftop at dusk, cel shading", "output/ep01/shot01.png",
                          model="nano-banana", reference_images=["output/chars/hero.png"])
# image-to-video (очередь queue.fal.run: submit -> status -> result -> скачивание mp4)
fal_client.image_to_video("output/ep01/shot01.png", "she turns her head, wind in hair",
                          "output/ep01/shot01.mp4", model="kling-2.5-turbo-pro", duration=5)

el.tts("Я не отступлю.", voice_id="<voice_id>", out_path="output/ep01/line01.mp3")
el.sfx("heavy wooden door slams", "output/ep01/door.mp3", duration_seconds=2)
el.music("melancholic piano, anime ending theme", "output/ep01/theme.mp3", length_seconds=60)
el.list_voices()      # бесплатно

storage.upload("output/ep01/ep01.mp4", "episodes/ep01.mp4")
storage.presigned_url("episodes/ep01.mp4", expires=3600)
```

CLI-аналоги: `python3 -m pipeline.fal_client image|video ...`,
`python3 -m pipeline.elevenlabs_client tts|sfx|music|voices ...`,
`python3 -m pipeline.storage upload|download|ls|url ...`.

Файл `.wav` в ElevenLabs: запрашивается `pcm_44100` и оборачивается в WAV локально.

## 4. Сборка серии

```bash
python3 -m pipeline.assemble output/ep01/spec.json      # сборка
python3 -m pipeline.assemble output/ep01/spec.json --dry-run   # показать команду ffmpeg
python3 -m pipeline.assemble --selftest                 # проверка на синтетике (lavfi)
```

Формат `spec.json` описан в начале `pipeline/assemble.py`. Кратко: `clips` склеиваются по порядку
(любой размер/fps приводится к 1920×1080, 24 fps, letterbox), `tracks` — дорожки `dialog` / `sfx` /
`music` со временем старта, громкостью (`volume_db`; по умолчанию 0 / −6 / −18 dB), `loop`,
`fade_in`/`fade_out`. Музыка приглушается под диалогами (`duck_music`), итог нормализуется
до −16 LUFS (`loudnorm`). Выход: H.264 CRF 18 + AAC 192k, `+faststart`.

## 5. Тесты

```bash
python3 -m unittest pipeline.tests.test_offline -v   # без сети, HTTP замокан
python3 -m pipeline.assemble --selftest
```
