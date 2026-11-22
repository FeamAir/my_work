# Главная тема и лейтмотивы «Бумажного кита»

Версия 1.0 от 2026-11-22. Автор: звукорежиссёр.
Документ привязывает слоты из `sound_bible.md` (п. 3.1–3.2) к героям сериала. Где слот изменён, источник правды — этот файл.
Решение директора: заставка только инструментальная, 5–8 с.
Статус: план (без генерации).

## 1. Привязка

| Слот | Кому / чему | Характер | Тональность / темп | Тембр | Где в пилоте |
|---|---|---|---|---|---|
| **THEME «Бумажный кит»** | сериал, кит, **доставленное письмо** | надежда с лёгкой грустью; короткая восходящая фраза с широким скачком вверх и мягким оседанием на шаг вниз, второй раз окончание выше | ре мажор / 92 BPM | фортепиано с войлочными молоточками, тёплые струнные, пэд, рамочный барабан во второй половине | sc06 (шов, «Одно письмо — один стежок»), заставка-титр |
| **L1 «Сора · журавлики»** | Сора | мечтательный, тихий, будто складывает бумагу; фраза заканчивается вопросом, без тоники (как её привычка переспрашивать) | ре мажор / 84 BPM | деревянная флейта с придыханием, фортепиано, редкое пиццикато | sc01 |
| **L2 «Гэн · почтальон»** | дед Гэн, почтовый дом | медленный нисходящий мотив, тепло и вина; под ним ровное пиццикато, как ход часов | си минор / 72 BPM | виолончель соло, низкое старое пианино, пиццикато-«часы» | sc05, финал сцены |
| **L3 «Тень»** | прорехи, тень кита, тревога (злодея в сериале нет) | два низких тона на полутон (ре — до-диез), без мелодии; не страх, а «что-то огромное рядом» | ре минор / без пульса | низкие струнные флажолеты, мягкий синт-бас, бумажно-зернистая текстура | sc02, тень ползёт по улице |
| **L4 «Кит · небо»** | кит в небе, магия | мерцающие арпеджио, неустойчивые гармонии, простор; восторг с долей тревоги | **ре лидийский** (в `sound_bible.md` был ми лидийский; исправлено, чтобы остаться в семье ре мажора) / свободный темп | челеста и музыкальная шкатулка, струнные флажолеты, далёкий хор «а» без слов, широкий пэд | sc03–sc04 |
| **L5 «Нацу · велосипед»** | Нацу | пружинистый, суховатый, с усмешкой; короткие фразы. Для серьёзного момента (серия 7) — тот же мотив медленно на одном кларнете в ми миноре | соль мажор / 116 BPM | пиццикато, приглушённая нейлоновая гитара (strum), стаккато кларнета, шейкер | sc02, появление Нацу |
| **L6 «Ветер»** (резерв, вместо «Экшена») | дождь, подъём на башню, полёт к киту (серии 3, 6) | текучее остинато, нарастание без ударов | ре дорийский / 100 BPM | остинато струнных, рамочный барабан, флейта | в пилоте нет, не генерируем |
| **L7 «Мама · письмо»** (новый слот) | мама Соры, письмо «Соре» | одно фортепиано, очень редко; начальный скачок темы сыгран один раз и оставлен висеть | ре мажор с тенью си минора / 66 BPM | фортепиано соло (войлок), в конце один тихий тон струнных | sc07, письмо «Соре» |

Связи между мотивами (словами, потому что модель Music не воспроизводит ноты точно):
- **L7 — «осколок» THEME.** Тот же характер скачка вверх, но без ответа. В финале сезона THEME звучит полностью и «отвечает» на L7.
- **Голос кита** (`whale_song.md`) настроен на ре: в тревожной версии зависает на до-диезе (как L3), в мягкой разрешается в ре (как THEME).
- **L1 и THEME** обе в ре мажоре и обе ведёт тембр фортепиано: Сора «растёт» в тему сериала.

## 2. Ядра промптов (английские, без имён людей и произведений)

Ядро не меняется от серии к серии. В вариациях меняется только хвост: интенсивность, длительность, «sparse/full». Всё фоновое — `force_instrumental: true`. `model_id` указываем явно: кандидаты `music_v2_5` и `music_v2`, выбор на первом треке (THEME). `music_v1` не используем: по документации его снимают 31 января 2027.

```text
THEME : Hopeful, slightly bittersweet instrumental main theme in D major, 92 BPM, 4/4. Soft felt piano carries a short rising melody that leaps up and gently settles one step down, then repeats with a higher ending. Warm small string ensemble, airy analog pad, light frame drum entering in the second half. Intimate, cinematic, warm paper-and-lantern atmosphere.
L1    : Gentle, dreamy instrumental cue in D major, 84 BPM. Breathy wooden flute plays a short tender melody over soft felt piano and sparse string pizzicato; each phrase ends on an unresolved, questioning note. Quiet, introspective, like folding paper at sunset. Sparse arrangement, leaves space for dialogue.
L2    : Slow, warm, nostalgic instrumental cue in B minor, 72 BPM. Solo cello plays long descending phrases over low soft upright piano chords, with a steady quiet pizzicato pulse like a ticking wall clock. Wise, tired, tender, a hint of old regret. Sparse arrangement, leaves space for dialogue.
L3    : Restrained, uneasy instrumental underscore in D minor, no beat. Two low notes a semitone apart (D and C-sharp) slowly pulsing in low string harmonics and a soft synth bass, faint grainy papery texture. Vast presence approaching, awe rather than horror, no melody, no percussion hits.
L4    : Shimmering, wondrous instrumental cue in D lydian, free tempo. Celesta and music-box arpeggios, high string harmonics, distant wordless choir pad, wide reverb. Awe and discovery with a slight unease, enormous and slow, like something floating in the evening sky.
L5    : Playful, springy instrumental cue in G major, 116 BPM. Bouncy string pizzicato, muted nylon guitar strums, staccato clarinet, light shaker. Dry, cheeky, short phrases, a confident smirk. Sparse arrangement, leaves space for dialogue.
L6    : Flowing instrumental cue in D dorian, 100 BPM. Rolling string ostinato, frame drum, soaring flute phrases, rising tension without hits. Wind, height, movement.
L7    : Very sparse solo felt piano in D major with B minor shadows, 66 BPM. A single rising leap played once and left hanging, long silences between notes, one quiet sustained string tone at the end. Intimate, aching, tender, like reading an old handwritten letter.
```

Запрещённые слова в промптах проверяются перед отправкой (`sound_bible.md` п. 3.2).

## 3. Главная тема: один мастер, из которого режутся заставка, титр и «Доставка»

Модель Music не повторяет мелодию нота в ноту. Если заставку, титр и музыку доставки генерировать отдельно, получатся три разные мелодии, и тема не запомнится. Поэтому:

1. Генерируем **один мастер темы ≈ 26 с** через `composition_plan`: у секций заданы длительности. `seed` в Music работает только с `composition_plan`, не с `prompt`. План можно бесплатно получить из промпта через `POST /v1/music/plan`, поправить и отправить в `POST /v1/music`.
2. Из мастера режем **заставку** (первые ≈ 7 с), **титр** (финальный каданс ≈ 4.5 с) и **«Доставку»** для кульминаций серий (секции A′ и каданс ≈ 14 с).
3. Делаем 3–4 дубля мастера и берём тот, где первая фраза **законченная**: первые 7 с режутся без обрыва на полуслове.
4. Запасной путь, если ни один дубль не режется чисто: заставка генерируется отдельным планом (раздел 4.2). Тогда титр и «Доставка» всё равно режутся из мастера.

### 3.1. План мастера (схема полей — из документации `/v1/music/plan`; у моделей v2 структура объекта может отличаться, сверить при подключении)

```json
{
  "positive_global_styles": ["instrumental", "hopeful bittersweet main theme", "D major", "92 BPM", "soft felt piano lead", "warm small string ensemble", "airy analog pad", "intimate cinematic"],
  "negative_global_styles": ["vocals", "lyrics", "drum kit", "electric guitar", "EDM", "trap beat", "orchestral bombast"],
  "sections": [
    {"section_name": "First note", "duration_ms": 1200, "lines": [],
     "positive_local_styles": ["a single soft felt piano note on D, ringing, near silence around it"],
     "negative_local_styles": ["strings", "percussion"]},
    {"section_name": "Motif A", "duration_ms": 5800, "lines": [],
     "positive_local_styles": ["felt piano plays a short complete rising phrase that leaps up and settles one step down", "soft strings enter underneath", "phrase resolves gently at the end"],
     "negative_local_styles": ["percussion"]},
    {"section_name": "Motif A prime", "duration_ms": 8000, "lines": [],
     "positive_local_styles": ["the same phrase repeats with a higher ending", "warm pad and light frame drum enter", "slight build"],
     "negative_local_styles": ["loud drums"]},
    {"section_name": "Cadence", "duration_ms": 6000, "lines": [],
     "positive_local_styles": ["warm full D major chord", "strings swell", "soft cymbal swell", "clean resolved ending"],
     "negative_local_styles": ["abrupt stop"]},
    {"section_name": "Tail", "duration_ms": 5000, "lines": [],
     "positive_local_styles": ["chord rings out and fades naturally to silence"],
     "negative_local_styles": ["new melody"]}
  ]
}
```

Итого 26 000 мс. `force_instrumental` в документации описан только для режима `prompt`. С планом инструментальность держим через `negative_global_styles` и пустые `lines`. Проверить при подключении.

### 3.2. Нарезка

| Ассет | Откуда | Длительность | Обработка | Файл |
|---|---|---|---|---|
| Заставка | 0:00–≈7.0 мастера (First note + Motif A) | 6.5–7.5 с | без фейда на входе; фейд-аут 0.4 с после разрешения фразы | `lib_mus_theme-intro_v1.wav` |
| Титр | Cadence + начало Tail (≈ 15.0–19.5 мастера) | 4–5 с | фейд-ин 0.15 с, фейд-аут 1 с | `lib_mus_theme-title_v1.wav` |
| «Доставка» | Motif A′ + Cadence + Tail (≈ 7.0–26.0) | до 19 с, в серии 10–14 с | вход фейдом 1–1.5 с из мягкой песни кита | `lib_mus_theme-delivery_v1.wav` |
| Мастер | целиком | 26 с | — | `lib_mus_theme-master_v1.wav` |

## 4. Заставка 5–8 с (инструментальная)

### 4.1. Синхронизация с картинкой (для режиссёра)
| Время | Звук | Картинка (предложение) |
|---|---|---|
| 0.0 с | одна нота фортепиано (ре) | появляется логотип/надпись «Бумажный кит» (наложение на монтаже) |
| ≈ 1.2 с | вход фразы, струнные | кит проплывает / с него слетает лист |
| ≈ 4.5–5.5 с | вершина фразы и разрешение | лист ложится, янтарный шов вспыхивает |
| 6.5–7.5 с | фейд-аут | переход в первую сцену |

### 4.2. Запасной промпт (если заставка не режется из мастера)
`composition_plan` на 7 000 мс: First note 1 000 мс → Motif 4 500 мс → Resolve 1 500 мс. Стили — как в мастере, плюс в Resolve: `"warm D major chord", "very short clean ending"`.

Однострочный вариант для `prompt` (`music_length_ms: 7000`, `force_instrumental: true`):
```text
Short 7-second instrumental opening theme in D major, 92 BPM. It begins with a single soft felt piano note, then the piano plays one short rising melody that leaps up and settles one step down over warm strings and an airy pad, ending on a gentle resolved D major chord with a soft cymbal swell. Hopeful, slightly bittersweet, intimate, clean ending, no vocals.
```

## 5. Титр (4–5 с)

Основной путь — вырезка каданса из мастера (п. 3.2). Запасной промпт (`music_length_ms: 5000`, `force_instrumental: true`):
```text
Short 5-second instrumental end sting in D major: soft felt piano plays the last two notes of a gentle rising phrase and lands on a warm D major chord, strings swell softly, a faint glass-like shimmer, then a clean natural fade. Hopeful, tender, conclusive, no vocals.
```

### Где звучат заставка и титр (предложение, решение за директором)
- **Пилот (серия 1)** построен как холодное открытие: название появляется в конце («ТИТР: Бумажный кит»), и сценарист просит на титр «первую ноту темы». Поэтому в пилоте **заставка стоит в конце**, ≈ 2:45.5–2:52.5. Её первая нота и есть «первая нота темы». Серия ≈ 2:53, в пределах 3:00.
- **Серии 2–8:** заставка в начале (0:00–≈0:07), в конце — титр 4–5 с.
- Если директор хочет заставку в начале и пилота: серия выходит ≈ 2:58–3:00 (2:45 + 7 с + титр 5 с) — на границе допуска. Тогда в пилоте титр в конце убираем, а название показываем на последней ноте сцены 7.

## 6. Музыка пилота

Подробно, с таймкодами, — в `ep01_sound_table.md` (раздел 5). Сводка: 8 треков, из них 7 библиотечных (переиспользуются весь сезон). Без музыки ≈ 21 % хронометража: начало sc01, пауза перед тенью в sc02, начало sc05, начало sc06 до щелчка.
