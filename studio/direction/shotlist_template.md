# Шаблон шот-листа

Версия 1.0 · 2026-11-22 · автор: режиссёр-постановщик

Файл серии: `studio/direction/shotlists/epXX_shotlist.md` (копия этого шаблона).

## Шапка сцены

```
Эпизод: epXX · Сцена: scYY · Локация: <id мастер-локации> · Время суток: <...>
Персонажи: <ID-блоки из refs/<id>/card.md> · Кто слева / справа (ось 180°): <...>
Акцентный цвет сцены: <киноварь / золото / кобальт> · Настроение: <...>
Хронометраж сцены (план): <сек>
```

## Колонки таблицы

| Колонка | Что писать |
|---|---|
| № | `scYY-shZZZ`, сквозная нумерация внутри сцены, шаг 10 (010, 020…) — чтобы вставлять кадры между |
| Сцена | номер сцены / короткое название |
| Длит. | длительность в монтаже, сек (генерируется клип минимальной длины модели, обычно 5 с) |
| План | WS / MS / MCU / CU / ECU / establishing / insert |
| Камера | ракурс + движение: `eye-level, static`, `low angle, slow push-in` и т.п. |
| Действие | что происходит в кадре, по-русски, одно действие |
| Реплика / звук | персонаж: «текст» / шумы / музыка |
| Промпт ключевого кадра | англ.; собирается по формуле из visual_bible.md §10; ID-блоки подставляются ссылкой `{MIRA}` и раскрываются при генерации; базовый стилевой и негативный промпты добавляются автоматически |
| Промпт движения | англ.; только движение и камера; базовый промпт движения добавляется автоматически |
| Модель | картинка → видео (+ липсинк), напр. `NB2 edit → Kling 2.5 TP` |
| Статус | `план` → `kf-ok` (ключевой кадр принят) → `vid-ok` (клип принят) → `final`; плюс версия: `kf v2 / vid t1` |

## Пустая таблица

| № | Сцена | Длит. | План | Камера | Действие | Реплика / звук | Промпт ключевого кадра | Промпт движения | Модель | Статус |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | план |

---

## Пример заполнения: тестовая сцена «Утро в мастерской»

Нейтральная тестовая сцена, не связанная со сценарием. Используется для проверки пайплайна и стиля.

```
Эпизод: ep00 (тест) · Сцена: sc01 · Локация: LOC_WORKSHOP (часовая мастерская, мансарда) · Время суток: раннее утро
Персонажи: {MIRA} (пример ID-блока в consistency.md §2) · В кадре одна, ось не задействована
Акцентный цвет сцены: золото фонаря #E9A93B · Настроение: тихое, уютное
Хронометраж сцены (план): 13 с
```

| № | Сцена | Длит. | План | Камера | Действие | Реплика / звук | Промпт ключевого кадра | Промпт движения | Модель | Статус |
|---|---|---|---|---|---|---|---|---|---|---|
| sc01-sh010 | 01 Утро в мастерской | 4 с | WS, establishing (без персонажей) | eye-level, медленная панорама слева направо | Пустая мансарда-мастерская: верстак с разобранными часами, окно, в луче света кружится пыль | Тиканье множества часов, далёкие птицы; музыка: вступление | `wide establishing shot, eye level, cozy attic clockmaker workshop with a slanted wooden ceiling, a cluttered workbench covered with disassembled pocket watches, gears and small brass tools, a round window on the right letting in low early morning sunlight, warm light beam with floating dust particles, dozens of wall clocks in the shadows, a small brass oil lamp glowing golden on the bench, no people` | `slow horizontal camera pan from left to right, dust particles drifting in the light beam, the lamp flame flickering softly, clock pendulums swinging gently` | Nano Banana → MiniMax H3 Max Turbo | план |
| sc01-sh020 | 01 Утро в мастерской | 5 с | MS | eye-level, static, лёгкий slow push-in | Мира сидит за верстаком спиной к окну, подносит к глазу карманные часы, сосредоточенно смотрит на механизм | Тиканье громче; тихий щелчок крышки часов | `medium shot, eye level, {MIRA} sitting at the cluttered workbench from image 2, three-quarter view facing left, holding an open pocket watch close to her right eye with both hands, focused calm expression, the round window behind her right shoulder with warm early morning backlight creating a golden rim light on her hair, small brass oil lamp glowing on the bench` | `very slow camera push-in, she slowly tilts the watch slightly, blinks once, a strand of hair moves gently, light dust drifting behind her` | Nano Banana 2 edit (ref: 03_three_quarter + LOC_WORKSHOP) → Kling 2.5 Turbo Pro | план |
| sc01-sh030 | 01 Утро в мастерской | 4 с | MCU | eye-level, static | Мира опускает часы, слегка улыбается и произносит реплику | Мира (тихо, себе): «Ну вот. Снова идёшь.» | `medium close-up, eye level, {MIRA} at the workbench, three-quarter view facing left, lowering the pocket watch to chest level, soft relieved smile, looking at the watch, mouth closed, warm golden rim light from the window behind her, softly blurred workshop background` | `she lowers the watch slightly and smiles softly, natural breathing, subtle blink, camera static` + липсинк по аудио реплики | Nano Banana 2 edit (ref: sh020 kf) → Kling 2.5 Turbo Pro → липсинк | план |

Примечания к примеру:
- sh010 — пейзаж без персонажа: дешёвая модель и text-to-image допустимы.
- sh020 — ключевой кадр делается edit-ом с референсом персонажа и мастер-локации; одновременно становится мастер-кадром сцены.
- sh030 — делается edit-ом **от ключевого кадра sh020** (тот же свет и одежда), рот в ключевом кадре закрыт — речь накладывается липсинком.
- Во всех промптах `{MIRA}` при генерации раскрывается в полный ID-блок; в конец автоматически добавляются базовый стилевой промпт, акцентный цвет сцены и негатив (или фраза `Avoid: …` для моделей без поля negative_prompt).
