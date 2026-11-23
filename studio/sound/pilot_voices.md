# HOLLOWSTONE — голоса пилота S01E01 «The Ninth Sluice»

Версия 1.2 · 2026-11-23 · звукорежиссёр · статус: **черновой кастинг для аниматика выполнен 2026-11-23** (`voice_id` — §6; финальный кастинг — после picture lock)
Источники: `story/characters/voice_fingerprints.md` (r3), досье CH-…, `_minor-*.md`, `beat_sheet.md` v1.1, `production_notes.md` v1.1 §3, §7, `canon/glossary.md` (v0.4).
Связанные файлы: `tts_pronunciation_test.md`, `emotion_markup.md`, `dubbing_ready.md`.

Язык озвучки — **английский**. Реплики, промпты и тестовые фразы — на английском. Пояснения — на русском.

---

## 0. Общие правила кастинга (для всех карточек)

1. **Только Voice Design по текстовому описанию.** Клонирование не используем. В промптах нет имён реальных актёров, певцов и персонажей чужих произведений, нет фраз «sounds like…» и «in the style of…».
2. **Модель дизайна — `eleven_ttv_v3`** (70+ языков, нужно для будущего дубляжа). Две карточки (Pell, Hollis) дополнительно дизайним на `eleven_multilingual_ttv_v2` как контроль для A/B (`emotion_markup.md` §6).
3. **Запрос** `POST /v1/text-to-voice/design`: `voice_description` = промпт карточки, `text` = тестовая фраза (100–1000 символов, все фразы ниже уложены в лимит), `guidance_scale` = 5 (если звучит «пластиково», снижаем до 3–4), `seed` фиксируем и записываем, `loudness` = 0 (≈ −24 LUFS по документации), `should_enhance` = false (промпт не должен «дописываться» чужими словами). `reference_audio_base64` не используем: исключение одно, о нём ниже, в карточке NARR-01.
4. **До трёх итераций промпта на голос.** Не получилось за три — меняем подход (описание тембра, возраст, акцент), а не жмём «ещё раз» (правило дублей из BRIEF).
5. **Подростки и дети** описываются как «young adult voice with a youthful sound» или как «adult female voice performing a boy». Это обычная практика озвучки аниме и меньше рисков с политиками сервиса.
6. **Акценты мира** записаны словами (§1), без пародии на реальные национальности.
7. **Голос закрепляется после утверждения.** Записываем `voice_id`, модель TTS, её версию и все настройки. Без записи в журнал карточки ничего не меняется. Для главных голосов (Pell, Wick, Nan, Ione, Hollis, Ruel, Ursel, Odo, NARR-01) архивируем **эталонный набор**: 3–5 минут чтения по фиксированному тексту. Он нужен, если модель снимут с поддержки и придётся переносить голос.
8. **Безымянные голоса не переиспользуем для других ролей со словами.** Зрители детективной саги заметят «тот же голос» и построят на нём теорию. Одноразовые голоса пилота (сборщик, хранитель реле, стражник, служительница) потом идут только в бессловесную массовку.
9. **Генерация — по одной реплике на файл, по одному персонажу.** Эндпоинт многоголосого диалога (`text-to-dialogue`) — только для теста: он склеивает голоса в один файл и ломает раздельные дорожки для дубляжа.

### Модели TTS (сверено с документацией ElevenLabs 2026-11-22)

| Модель | Статус по документации | Что важно нам |
|---|---|---|
| `eleven_multilingual_v2` | «previous generation», 29 языков, 10 000 симв./запрос | самая предсказуемая; аудиотеги не поддерживает (читает их вслух); есть `style`, `speed` 0.7–1.2 |
| `eleven_v3` | «previous generation», 70+ языков, 5 000 симв./запрос | аудиотеги; stability-пресеты Creative / Natural / Robust; SSML `<break>` не поддерживает |
| `eleven_v4` | новая (с 28.09.2026), 90+ языков | ElevenLabs рекомендует её вместо v3; теги понимает точнее; **Style и Speed недоступны**; по документации голоса из Voice Design на v4 «могут звучать менее выразительно». Есть нативный IPA |

**Вывод:** заказанный A/B «v3 против multilingual_v2» расширяю третьим плечом — v4. Сравнение на тех же `voice_id` стоит дёшево (подробно — `emotion_markup.md` §6). Значения настроек ниже — стартовые, уточняются на пробе.

---

## 1. Палитра акцентов (английский)

| Код | Где | Описание для промпта (EN) |
|---|---|---|
| ACC-LOWS | Нижний город (Pell, Wick, Mags, Corr) | rough working-class English dock accent: dropped "g" endings, glottal "t" in the middle of words, flat short vowels |
| ACC-LOWS-OLD | старшее поколение Низов (Nan) | the same dock accent but broader and older, old-fashioned rhythm, words snapped off at the ends |
| ACC-MIDS | клерки, ремесленники (Hollis, сборщик, хранитель реле) | clear, neutral, educated city English, crisp consonants, every word finished |
| ACC-STEPS | знать, двор, банк (Ursel, Odo, Lucan) | refined, formal upper-class English with long, smooth, rounded vowels |
| ACC-CRAG | Pale Crag, Хор (Ione, служительница) | precise, cool, formal diction, long pure vowels, complete sentences |
| ACC-GULL | Gullmouth, побережье (Ruel) | warm coastal accent with broad open vowels, carrying and easy |
| ACC-UPLAND | Rusk, нагорья (стражник) | rural hill-country accent with a rolled "r" and long "o" vowels |

**Правило текста:** акцент даёт голос, а не орфография. В сценарии пишем нормативное английское написание: без «wa'er» и «nothin'». Так субтитры и перевод для дубляжа берутся из того же текста. Если на пробе акцент Низов выходит слабым, в поле `tts_text` (`emotion_markup.md` §2) можно точечно записать «nothin'». Текст субтитров при этом не меняется.

---

## 2. Матрица различения (пять осей)

Голоса различаем по пяти осям: высота, фактура, атака, темп, подача/акцент. Возраст сам по себе голоса не различает. F0 — целевая медиана основного тона на пробе, проверяется замером.

| ID | Персонаж | F0 цель | Фактура | Атака | Темп | Подача / акцент |
|---|---|---|---|---|---|---|
| V-01 | Pell | ~195 Гц (лёгкий альт) | сухая, зернистая, без воздуха | жёсткая, обрубленные концы | быстрый | колючая, через шутку; LOWS |
| V-02 | Wick | ~290 Гц | яркая, «ломается» на эмоции | быстрая, захлёбывающаяся | очень быстрый | комментирует всё вслух; LOWS (гуще, чем у Pell) |
| V-03 | Nan | ~230 Гц | тонкая, надтреснутая, громкая | резкая, «отщёлкивает» слова | быстрый | ругает любя; LOWS-OLD |
| V-04 | Ione | ~255 Гц | чистая, светлая, полётная | мягкая, точная | размеренный | полные фразы, вопрос-утверждение; CRAG |
| V-05 | Hollis | ~130 Гц (лёгкий баритон) | сухая, светлая | чёткая | быстрый; медленный перед смелостью | ироничный к себе; MIDS |
| V-06 | Ruel | ~105 Гц | тёплая, круглая, большая | мягкая, широкая | средний | на улыбке, «на причал»; GULL |
| V-07 | Lucan | ~95 Гц | тяжёлая, хрипящая, с одышкой | вязкая | медленный | достоинство и усталость; STEPS |
| V-08 | Ursel | ~175 Гц (низкое меццо) | мягкая, тёплая | очень мягкая | очень медленный | ласковая и неумолимая; STEPS |
| V-09 | Odo | ~115 Гц, почти шёпот | мягкая, с придыханием, без хрипа | очень мягкая | очень медленный | заставляет наклониться; STEPS |
| V-10 | Corr | ~85 Гц (бас) | плотная, низкая | тяжёлая, «шаг» | медленный, паузы | спокойная власть; LOWS |
| V-11 | Mags | ~240 Гц | хриплая, с гоготом | широкая, громкая | средний, тянет | на публику; LOWS (шире и медленнее, чем у Pell) |
| V-12 | Tithe-collector | ~145 Гц | носовая, тонкая | чиновничья | средний, списком | важный → испуганный; MIDS |
| V-13 | Choir attendant | ~200 Гц | мягкая, полушёпот | суетливая | быстрый | хлопочет; CRAG |
| V-14 | Relay-keeper | ~150 Гц | светлая, сбивчивое дыхание | быстрая | быстрый | докладывает; MIDS |
| V-15 | Rusk guard | ~110 Гц | грубая, усталая | тупая, короткая | средний | коротко; UPLAND |
| NARR-01 | The Chronicler | ~115 Гц | сухая, «бумажная», лёгкая хрипотца | очень чёткая | медленный, ~110 слов/мин | архивная, ровная; без окраски |

### Рискованные пары и чем их разводим

| Пара | Риск | Разведение |
|---|---|---|
| Pell / Mags | две девочки 15 лет из Низов в одной сцене (Sc 3) | Pell ниже на 3+ полутона, сухая и быстрая; Mags выше, хриплая, тянет слова, громкая. Mags всегда далеко (дальний план + расстояние в миксе) |
| Lucan / NARR-01 | два старика, оба «читают документ» (Sc 12 и Sc 5/7/19) | Lucan ниже, тяжелее, с одышкой и в акустике зала. NARR-01 светлее, суше, без дыхания на слух, предельно чёткий, сухой и близкий. Голос рассказчика никогда не звучит рядом с Lucan |
| Nan / Ursel | две старые женщины | Nan тонкая, громкая, быстрая, LOWS. Ursel низкая, тихая, очень медленная, STEPS |
| Odo / Ursel | оба мягкие и медленные | разный пол и регистр; Odo почти шёпотом, Ursel полным тихим голосом |
| Hollis / Ruel | два баритона | Hollis светлее (+4 полутона), сухой, быстрый, MIDS; Ruel круглый, тёплый, широкий, GULL |
| Hollis / NARR-01 | мужские голоса «ровного» склада | Hollis быстрый, нервный, светлый; NARR-01 старый, медленный, ровный. Различимость с первого прослушивания обязательна (`production_notes` §7). Проверяем в общем слепом тесте наравне с остальными парами |
| Ione / служительница | два голоса Хора в Sc 8 | служительница ниже, полушёпотом, суетится; Ione — ясная, полная фраза |
| Wick / Pell | дети одной улицы | Wick на октаву-полторы выше, захлёбывается, акцент гуще |

### Приёмка различимости (до утверждения голосов)

1. **Слепой тест:** 20 случайных отрывков по 3 с (по 1–2 от каждого голоса). Директор и звукорежиссёр называют персонажа. Порог — ≥ 90 % верных у обоих.
2. **Замер F0** (медиана, praat/parselmouth или numpy — скрипт у IT). Голоса из одной сцены разнесены минимум на 3 полутона, если остальные оси не расходятся резко.
3. **Телефонная полоса:** тот же тест через фильтр телефона (`mix_plan.md`, раздел «Phone check»). Различимость не должна падать ниже 85 %.
4. Эквалайзер и сдвиг высоты на диалоге **не** используем как способ различения: голос должен различаться сам.

---

## 3. Карточки голосов

Формат настроек:
- **v2** — `stability / similarity_boost / style / speed`, `use_speaker_boost = true`;
- **v3** — пресет stability: Creative (0.0), Natural (0.5), Robust (1.0). Соответствие пресетов числам проверяем на пробе;
- **v4** — стартовая stability (style и speed в v4 недоступны).

Режимы: **Б** — базовый, **Э** — эмоциональный, **Т** — тихий.

---

### V-01 · Pell (CH-0001) — главная героиня, 15 лет, Низы

| Поле | Значение |
|---|---|
| Сцены пилота | 2, 3, 4, 9, 19 (в Sc 20 без реплики). Lip-sync в пилоте нет |
| Звучание | голос молодой взрослой (18–20), звучащий как 15 |
| Эмоциональный диапазон | база: сухая, деловая, колючая → смех носом, бравада; страх **без слов** (молчит, дышит, мычит); злость короткими рублеными фразами; шёпот-приказ («hold the rope»). Плача нет, в S1 он не нужен |
| Запреты подачи | «please» вверх по интонации; никакой мягкости к знати; страх словами не озвучивается |
| ElevenLabs | имя голоса `HS S1 V01`; ttv `eleven_ttv_v3` (+ контроль `eleven_multilingual_ttv_v2`); `voice_id` —; seed —; guidance 5 |
| Статус | черновик |

**Voice Design (EN)** — v1.2, фактически использованный промпт (возраст персонажа убран из промпта: формулировка «…fifteen-year-old…» заблокирована фильтром сервиса (403)):
```text
Young adult woman around twenty with a light, youthful sound, playing a tough street scavenger in an animated series. Light alto, lower than most young women; dry and slightly grainy, with no breathiness. Fast, clipped delivery: short phrases, hard stops, endings swallowed, and a quick dry laugh through the nose. Rough working-class English dock accent with dropped "g" endings, glottal "t" in the middle of words and flat short vowels. Wary, sharp and unsentimental; she jokes instead of showing fear. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 431 симв.):**
```text
You want it found, you pay the mud. Mud doesn't do favours. Six coppers by dusk? Fine. I've pulled more than that out of worse water than this. No, don't look at me like that, I'm not scared of a puddle. Just hold the rope, Wick. Hold it with both hands and don't say a word. Not one. Buttons! It's all buttons over here, Mags, go on, have a laugh! ... Water doesn't care who you are. That's the only fair thing in this whole city.
```

**Настройки:**

| Режим | v2 | v3 | v4 |
|---|---|---|---|
| Б | 0.45 / 0.80 / 0.15 / 1.06 | Natural | 0.45 |
| Э | 0.32 / 0.78 / 0.30 / 1.10 | Creative | 0.30 |
| Т | 0.55 / 0.80 / 0.05 / 1.00 | Natural | 0.55 |

**Отдельная дорожка (V2):** напев Пелл в Sc 3 (три ноты с закрытым ртом; мелодия — композитор) записывается **отдельным файлом**, не в общем стеме VOX-NL. Напев кончается не позже **3,5 с** от начала sc03-sh180, сразу за ним идёт «Pell. Mouth.» Уика (тоже отдельный файл). Композитор предлагает для V2 версию без напева. Дорожку всё равно держим отдельно: так монтаж может выбрать любой вариант.

**Боевые фразы (пилот):** «You want it found, you pay the mud. Mud doesn't do favours.» · «Buttons!» · «It's six coppers.» · «Water doesn't care who you are.»

---

### V-02 · Wick (CH-0007) — 11 лет, Низы

| Поле | Значение |
|---|---|
| Сцены | 2, 3, 4, 6, 9, 20. Lip-sync №5 (Sc 20, последняя реплика пилота) |
| Звучание | взрослый женский голос, играющий мальчика 11 лет |
| Эмоциональный диапазон | база: восторг, болтовня, «почему?» → шёпот-шипение («Pell. Mouth.»), онемение (Sc 3 — без слов), благоговейный испуганный шёпот (Sc 20). «I'm scared» не говорит никогда, говорит «I'm cold» |
| Отдельные дорожки (V2, режиссёр §4.3) | «Pell. Mouth.» (Sc 3, sc03-sh180) — **отдельный файл**, вход сразу после напева Пелл; для вертикального ролика V2 |
| Особое | одна громкая **спетая нота** в Sc 4. Это вокал без слов: высоту ставит композитор, нота идёт в стем M&E (`dubbing_ready.md`). Пробуем двумя способами: TTS v3/v4 с тегом `[sings]` голосом Wick плюс подгонка высоты в ffmpeg, или вокал от композитора |
| ElevenLabs | `HS S1 V02`; `eleven_ttv_v3`; `voice_id` — |
| Статус | черновик |

**Voice Design (EN)** — v1.2, фактически использованный промпт («eleven-year-old» убран превентивно после блокировки V-01):
```text
Adult female voice actor performing a boyish cartoon character, as in animation dubbing: high, bright and quick, slightly scratchy, with an excited crack when he gets carried away. Talks fast, tumbling over his own words, cheeky and curious, always asking why. Thick working-class English dock accent: dropped "g" endings, glottal "t", flat vowels. Can drop instantly into a hushed, awed whisper. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 331 симв.):**
```text
Nan drowned! Twice! And the second time she took the money with her, honest, I saw it. ... No I didn't. Pell! Pell, wait for me! Why's everyone go quiet when the tower sings? Why do we always have to cover our mouths? Nobody ever says. ... I'm not scared. I'm cold. That's different. ... Pell. Mouth. ... Pell... it's singing back.
```

**Настройки:**

| Режим | v2 | v3 | v4 |
|---|---|---|---|
| Б | 0.40 / 0.80 / 0.20 / 1.10 | Natural | 0.40 |
| Э | 0.30 / 0.78 / 0.30 / 1.12 | Creative | 0.30 |
| Т (шёпот, Sc 3 и Sc 20) | 0.55 / 0.82 / 0.05 / 0.95 | Natural + `[whispers]` | 0.50 + `[whispers]` |

**Боевые:** «Pell. Mouth.» · «It answered you.» · «Pell… it's singing back.» (`[LIPSYNC-CU]`; дубль утверждается до видео-липсинка)

---

### V-03 · Nan (CH-0015) — бабушка Pell, около 70, старые Низы

| Поле | Значение |
|---|---|
| Сцены | 2 (`[OS]`, из дома), 4. Lip-sync №1 (Sc 4) |
| Эмоциональный диапазон | база: ворчание-забота, быстрый выговор → обрыв на полуслове («Not since—», Sc 4); тихий **ужас** на «Never sing, chick» (сжатый, низкий, почти шёпот, без крика). Мычание с закрытым ртом — не TTS, это вокал к композитору |
| ElevenLabs | `HS S1 V03`; `eleven_ttv_v3`; `voice_id` — |

**Voice Design (EN):**
```text
Elderly woman around seventy, tiny and fierce. Thin, cracked, reedy voice that is surprisingly loud for her size. Quick scolding rhythm, words snapped off at the ends; love expressed as nagging. Broad, old-fashioned working-class English dock accent, older and rougher than the young people around her. When frightened she goes low, tight and very quiet instead of shouting. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 391 симв.):**
```text
Did you eat? Don't tell me you ate, I can see the bread from here. Sit. Sit! And you, stop wriggling, chick, you'll have the table over. Bare, he says. The old sill, bare. Not in my floods it wasn't. Not since... Never mind since. Eat your bread. ... Salt for the Lady, a shell for the dead, and your mouth shut for the living. ... Never sing, chick. Hum if you must, and only for the house.
```

**Настройки:**

| Режим | v2 | v3 | v4 |
|---|---|---|---|
| Б | 0.42 / 0.80 / 0.20 / 1.05 | Natural | 0.42 |
| Э (страх, Sc 4 CU) | 0.50 / 0.82 / 0.10 / 0.92 | Natural + `[quietly]`/`[tense]` | 0.50 |
| Т | 0.55 / 0.82 / 0.05 / 0.95 | Natural | 0.55 |

**Отдельная дорожка (V4, режиссёр §4.3):** «Never sing, chick. Hum if you must, and only for the house.» — сухой отдельный файл (без комнаты), чтобы в вертикальном ролике V4 положить её за кадр поверх sc04-sh150/sh160. Акустику комнаты добавляет сведение каждой версии.

**Боевые:** «Never sing, chick. Hum if you must, and only for the house.» (CU, фиксированная строка) · «Not since—» (обрыв: генерируем фразу целиком и режем в монтаже, см. `emotion_markup.md` §4)

---

### V-04 · Ione Ilvane (CH-0002) — 18 лет, новиция Хора, Pale Crag

| Поле | Значение |
|---|---|
| Сцены | 8, 10, 12 (молча). Lip-sync в пилоте нет (только спиной) |
| Эмоциональный диапазон | база: ясная, собранная, серьёзная; любопытство — вопрос, произнесённый как утверждение → после пения (Sc 10) **лёгкая сиплость** голоса. Это физическое состояние, а не эмоция; кричать не умеет |
| Особое | спетый тон в Sc 9 — партия композитора. Звукорежиссёр передаёт композитору эталон речевого голоса Ione, чтобы спетый тон и речь были одним человеком. Вариант для пробы: `[sings]` на v3/v4 голосом Ione + подгонка высоты к тону Crown (C) |
| ElevenLabs | `HS S1 V04`; `eleven_ttv_v3`; `voice_id` — |

**Voice Design (EN):**
```text
Young woman around eighteen to twenty, a trained young singer from an old, formal family. Clear, light, high-mid soprano speaking voice, pure and unhurried, with a singer's breath control: she never runs out of air in the middle of a sentence. Precise, cool, formal diction with long pure vowels and complete sentences, an almost scriptural cadence. Serious and composed, with curiosity underneath; never coy, never breathy. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 337 симв.):**
```text
Is that what the song is for? Forgive me. I ask only because no one answers. If the song is a gift, then whom is it given to? ... The water lies flat, Your Steadiness. The Cantor sends her word. ... I am well. It is only the throat; it always passes. ... Hear, and be still. The people of the Ninth will hear it too, though not as we do.
```

**Настройки:**

| Режим | v2 | v3 | v4 |
|---|---|---|---|
| Б | 0.60 / 0.82 / 0.10 / 0.97 | Natural | 0.60 |
| Сиплость после пения (Sc 10) | 0.50 / 0.80 / 0.15 / 0.95 | Natural + `[hoarse]` (свободный тег, проверить) | 0.50 + `[hoarse]` |
| Т | 0.62 / 0.82 / 0.05 / 0.95 | Natural | 0.60 |

**Боевые:** «Is that what the song is for?» · Sc 10: слова Кантора о плоской воде (из сценария)

---

### V-05 · Hollis Kett (CH-0003) — 26 лет, клерк банка Lantry

| Поле | Значение |
|---|---|
| Сцены | 13 (`[VO]` над цифрами), 14, 15. Lip-sync в пилоте нет |
| Эмоциональный диапазон | база: быстро, сухо, точно, ирония над собой → страх (ещё быстрее, глотает воздух, «something about the damp») → смелость (**очень медленно**, по слову, Sc 15) |
| Обработка | его `[VO]` в Sc 13 — внутренний голос в зале: лёгкое отражение помещения и шорох перьев под ним. Темп, каденция и обработка не совпадают ни с чьим закадровым голосом (`production_notes` §7) |
| В E1 не говорит | «carried forward» (`beat_sheet` §4) |
| ElevenLabs | `HS S1 V05`; `eleven_ttv_v3` (+ контроль `eleven_multilingual_ttv_v2`); `voice_id` — |

**Voice Design (EN):**
```text
Man in his mid-twenties, a junior bank clerk who thinks in figures. Light, dry baritone, bright rather than deep. Quick, exact speech with crisp consonants; he finishes every word even when he is in a hurry. Clear, neutral, educated city accent. Nervous energy and self-deprecating humour; he speeds up and runs short of breath when anxious, and slows right down, word by word, when he is about to do something brave. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 398 симв.):**
```text
Twelve, carry the four, nineteen... It balances. Which is exactly why I don't trust it. No street, no district, no name. Just a heading: Account Nine. ... Not yet reconciled. ... Is it damp in here, or is it me? It's the damp. Definitely the damp. Columns. ... Dame Ursel. I can balance it. I can't tell you what it is. ... Money doesn't lie. People lie, and money keeps very careful records of it.
```

**Настройки:**

| Режим | v2 | v3 | v4 |
|---|---|---|---|
| Б | 0.50 / 0.80 / 0.15 / 1.08 | Natural | 0.50 |
| Э (страх, скороговорка) | 0.38 / 0.78 / 0.25 / 1.12 | Creative | 0.38 |
| «Смелый» (медленно) | 0.60 / 0.82 / 0.05 / 0.88 | Natural + `[slowly]` | 0.60 + `[slowly]` |
| Т / VO | 0.55 / 0.80 / 0.05 / 1.04 | Natural | 0.55 |

---

### V-06 · Ruel Corvane (CH-0005) — около 48, адмирал, Gullmouth

| Поле | Значение |
|---|---|
| Сцены | 10, 11, 12. Lip-sync №2 (Sc 11) |
| Эмоциональный диапазон | база: тепло, обаяние, всех знает по имени → дружеская шутка → тихая твёрдость с Lucan → смех со всем залом (Sc 11) → крик «за лекарем», убедительный, с силой, но без истерики (Sc 12) |
| Запреты | «sorry»; ирония или «злодейские» нотки голосом. Зритель должен любить его до E11 |
| ElevenLabs | `HS S1 V06`; `eleven_ttv_v3`; `voice_id` — |

**Voice Design (EN)** — v1.2, фактически использованный промпт (итерация 2: «deep … bass-baritone, low resonant chest voice» — в итерации 1 голос вышел на уровне Hollis):
```text
Man around fifty, a beloved sea-lord and admiral. Deep, warm, round bass-baritone with a low, resonant chest voice, big enough to carry across a harbour without effort. Easy, generous, smiling delivery, unhurried but never slow; a ready, low laugh. Warm coastal English accent with broad open vowels. Charismatic and kind-sounding: the voice of a man you would follow into a boat in a storm. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 373 симв.):**
```text
Warden! And how's that daughter of yours, still beating you at dice? Good. Somebody should. ... Read it differently, old friend. Just this once. ... I know. I know it's drawn. We go under and come up. ... My lady, you've flattened my whole harbour. My captains will be bored to tears. ... No. Thank you. I don't drink before a storm. ... A physician! Now! Get him here now!
```

**Настройки:**

| Режим | v2 | v3 | v4 |
|---|---|---|---|
| Б | 0.50 / 0.80 / 0.20 / 1.00 | Natural | 0.50 |
| Э (крик, Sc 12) | 0.35 / 0.78 / 0.30 / 1.05 | Creative + `[shouts]` | 0.35 + `[shouting]` |
| Т | 0.58 / 0.82 / 0.10 / 0.97 | Natural | 0.58 |

**Боевые:** «We go under and come up.» · «I don't drink before a storm.» (CU, `[ECHO]`; монтаж ничего не режет)

---

### V-07 · Helm Lucan Dask (CH-0016) — 71, правитель

| Поле | Значение |
|---|---|
| Сцены | 10, 12. Lip-sync №3 (Sc 12, «…and the Ninth Sluice—») |
| Эмоциональный диапазон | база: тяжело, ровно, «читает счёт» → сбивается, облизывает губы, теряет место (Sc 12): паузы, сглатывание (`[swallows]`), дыхание тяжелеет. Обрыв на «Sluice—» |
| Различие с NARR-01 | см. §2: ниже, тяжелее, одышка, акустика зала |
| ElevenLabs | `HS S1 V07`; `eleven_ttv_v3`; `voice_id` — |

**Voice Design (EN):**
```text
Elderly man around seventy, an old ruler worn down by office. Deep, heavy, rasping voice with a dry wheeze at the end of long phrases; slow, weighty and dignified. Refined old court accent with long rounded vowels. He speaks as if every sentence costs him breath, and he reads lists in the flat tone of a man reading out a bill. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 323 симв.):**
```text
It is drawn, Ruel. I only read it. ... You will lose this one. You know you will. ... First Song: the Steps, the harbour, the First Sluice through the Fourth. Second Song... forgive me. Where was I. Second Song. ... Last Song. ... And the Ninth Sluice, and the Ninth Sluice is... ... Leave it. The hall is waiting. Read on.
```
(«and the Ninth Sluice is...» нужно только для пробы: так проверяем, как модель обрывает фразу. В эфир идёт только фиксированная строка.)

**Настройки:**

| Режим | v2 | v3 | v4 |
|---|---|---|---|
| Б | 0.62 / 0.82 / 0.05 / 0.90 | Natural | 0.62 |
| Сбой (Sc 12) | 0.48 / 0.80 / 0.15 / 0.88 | Natural + `[swallows]`, `[exhales]` | 0.48 |

**Боевая (CU):** «…and the Ninth Sluice—» (обрыв: делаем 3 дубля, режем на «Sluice» с микрофейдом 15–25 мс и коротким вдохом, см. `emotion_markup.md` §4)

---

### V-08 · Dame Ursel Lantry (CH-0011) — 62, глава банка

| Поле | Значение |
|---|---|
| Сцены | 15 (+ Sc 16 молча). Lip-sync №4 (Sc 15) |
| Эмоциональный диапазон | узкий по замыслу: ласковая неподвижность. Похвала и приговор звучат одинаково тепло. Повышения голоса нет никогда |
| ElevenLabs | `HS S1 V08`; `eleven_ttv_v3`; `voice_id` — |

**Voice Design (EN):**
```text
Woman in her early sixties, the gentle-seeming head of a great bank. Soft, low, warm mezzo, grandmotherly; very slow and very still, and she never raises her voice. Refined formal accent with long, smooth vowels and perfect diction. Endearments like "my dear" and "child" sound kind and completely certain. Calm, intimate and unhurried, with an undertone of total control. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 303 симв.):**
```text
No, my dear, finish the line first. Always finish the line. ... You found it balanced, and you checked it again because it balanced. That is a rare habit, child. Rarer than you know. Then you have done exactly what was asked of you. ... A clerk who is trusted gets a clip. ... All water finds its level.
```

**Настройки:**

| Режим | v2 | v3 | v4 |
|---|---|---|---|
| Б | 0.65 / 0.82 / 0.05 / 0.88 | Robust или Natural (по A/B) | 0.65 |
| Т (`[OS]` «All water…») | 0.65 / 0.82 / 0.05 / 0.86 | Natural | 0.65 |

---

### V-09 · Odo Fennick (CH-0010) — около 55, мастер слушателей

| Поле | Значение |
|---|---|
| Сцены | 17 (одна фиксированная реплика, `[MS]`). Lip-sync нет |
| Эмоциональный диапазон | почти шёпот всегда. Повторяет чужое слово вопросом. Угроза — только мягкостью |
| Примечание | по разбору аналитика (О-11) имя Odo в E1 вслух не звучит. Голос всё равно ставим сейчас: он нужен с E2 |
| ElevenLabs | `HS S1 V09`; `eleven_ttv_v3`; `voice_id` — |

**Voice Design (EN):**
```text
Man in his mid-fifties, a soft-spoken master of informers. Mid-low voice kept almost at a whisper, never hurried; soft consonants and precise, old-fashioned clerkly diction with a refined accent. Gentle, patient, faintly tender; people have to lean in to hear him. Intimate, close-microphone delivery: quiet and clear, not raspy, not seductive. Clean studio recording, no background noise, no music.
```

**Тестовая фраза (EN, 238 симв.):**
```text
The tone came quickly? ... Quickly. Yes. ... Order is a kindness, my dear. The flood is not cruel; it is only untidy. Did you hear the hall? Did you hear who left it first, and who stayed? ... Not yet. ... Steadiness. ... Nothing unheard.
```

**Настройки:** Б v2 0.62 / 0.82 / 0.05 / 0.86 · v3 Natural (**без** постоянного `[whispers]`: шёпот должен быть в самом голосе) · v4 0.62.

---

### V-10 · Corr (CH-0048) — около 50, рид-мастер колёс

| Поле | Значение |
|---|---|
| Сцены | 6. По О-11 имя в E1 не звучит |
| Эмоциональный диапазон | спокойная тяжесть; «не со зла»; тихо и низко, когда говорит о чтении карты |
| ElevenLabs | `HS S1 V10`; `eleven_ttv_v3`; `voice_id` — |

**Voice Design (EN):**
```text
Man around fifty, the boss of a gang of treadmill labourers. Deep, heavy bass voice, slow and steady; every sentence lands like a footstep, with a pause after it. Rough working-class English dock accent, plain words, not unkind. The calm authority of a lifetime of hard physical work. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 260 симв.):**
```text
No half-walks today. ... Short a pin. Two wheels, half the walks, and grown backs first. ... A wheel doesn't care who walks it. ... Reading's today, girl. Come dusk, they'll all know what the Ninth is worth. ... Keep the count. Keep it flat. One note, no more.
```

**Настройки:** Б v2 0.60 / 0.82 / 0.05 / 0.90 · v3 Natural · v4 0.60.

---

### V-11 · Mags (CH-0049) — 15, мадларк, соперница Pell

| Поле | Значение |
|---|---|
| Сцены | 3 (через канал, дальний план). Её **гогот** без слов идёт в M&E, реплика со словами — в DX |
| Эмоциональный диапазон | насмешка, азарт, любопытство («What've you got?») |
| ElevenLabs | `HS S1 V11`; `eleven_ttv_v3`; `voice_id` — |

**Voice Design (EN)** — v1.2, фактически использованный промпт (возраст убран (как у V-01)):
```text
Young adult woman around twenty with a youthful sound, playing a loud street scavenger in an animated series. Hoarse, raspy mid-high voice and a big cackling laugh; brash and broad, a little drawling, she loves an audience. Rough working-class English dock accent, broader and slower than her friends'. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 255 симв.):**
```text
Oi, Pell! Your lane's all buttons again! Ha! Buttons and bent spoons, you'll be rich by the Still! ... What've you got there? Go on, show us. ... Finders keep, losers weep, that's the rule, innit? ... Wick, you little eel, I can see you hiding behind her!
```

**Настройки:** Б v2 0.40 / 0.78 / 0.30 / 1.00 · v3 Creative/Natural · v4 0.40.

---

### V-12 · Tithe-collector (без имени, новый) — сборщик налога

| Поле | Значение |
|---|---|
| Сцены | 2, 19 |
| Эмоциональный диапазон | скучная важность, считает вслух → Sc 19: голос **садится**, тонко и тихо: «Helm's dead.» |
| ElevenLabs | `HS S1 V12`; `eleven_ttv_v3`; `voice_id` —; после пилота голос только для массовки (§0 п. 8) |

**Voice Design (EN):**
```text
Middle-aged man, a petty tax collector. Nasal, reedy tenor; officious, bored and a little self-important; he reads amounts out like a list. Clear city accent, slightly pinched. When frightened his voice goes thin, quiet and uncertain. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 256 симв.):**
```text
Last Song, three coppers the month. Two months owing. That's six. ... Six coppers by dusk, or I take it in goods. Nets will do. ... Four. That's four. You're two short, girl. ... Helm's dead. ... The Helm. He's... I don't... Never mind. Never mind the box.
```

**Настройки:** Б v2 0.55 / 0.80 / 0.10 / 1.00 · испуг 0.45 / 0.80 / 0.15 / 0.92 · v3 Natural · v4 0.55.

---

### V-13 · Choir attendant (без имени) — служительница Хора

| Поле | Значение |
|---|---|
| Сцены | 8 (`[OS]`) |
| ElevenLabs | `HS S1 V13`; `eleven_ttv_v3`; `voice_id` — |

**Voice Design (EN):**
```text
Woman in her forties, a fussy temple attendant. Mid-alto, soft but hurried, half-whispered urgency; precise formal diction with long vowels. She fusses constantly and worries about appearances, never about meaning. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 259 симв.):**
```text
Stand still, my lady, your stole is crooked. There. No, there. ... Sing it flat for the lords, please. Nothing clever. They don't want clever, they want the water quiet and the hall on time. ... Throat-band. Where is your... ah. Good. Go, go, they're waiting.
```

**Настройки:** v2 0.50 / 0.80 / 0.15 / 1.08 · v3 Natural · v4 0.50.

---

### V-14 · Relay-keeper (без имени) — хранитель реле

| Поле | Значение |
|---|---|
| Сцены | 17 (`[OS]`) |
| ElevenLabs | `HS S1 V14`; `eleven_ttv_v3`; `voice_id` — |

**Voice Design (EN):**
```text
Young man in his early twenties, a junior signals keeper. Light tenor, a little breathless; respectful, quick and nervous, eager to report correctly. Clear, neutral city accent. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 194 симв.):**
```text
My lord. The tone. It came very quickly, my lord. Three long, and the rest. From the Crown. ... Should I log it? I'll log it. I'll log the time, my lord. Every stone on the wall took it at once.
```

**Настройки:** v2 0.50 / 0.80 / 0.10 / 1.08 · v3 Natural · v4 0.50.

---

### V-15 · Rusk guard (без имени) — стражник у ворот

| Поле | Значение |
|---|---|
| Сцены | 18 (`[OS]`, одна реплика; сержант Kes молчит) |
| ElevenLabs | `HS S1 V15`; `eleven_ttv_v3`; `voice_id` — |

**Voice Design (EN)** — v1.2, фактически использованный промпт (по сценарию v1.0.2 стражник молодой (A GUARD (young…))):
```text
Young man in his early twenties, a hill-country soldier on gate duty. Gruff, rough mid-low voice, blunt and tired beyond his years; rural accent with a rolled "r" and long "o" vowels. Speaks in short lines to fill an uneasy quiet and expects no answer. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN, 178 симв.):**
```text
Bar's down, Sergeant. ... Thirty days of this, then. Thirty days of the gate shut and that lot down there shouting at it. ... Right. Not my business. Never is. Roll on the Still.
```

**Настройки:** v2 0.55 / 0.80 / 0.10 / 0.98 · v3 Natural · v4 0.55.

---

### NARR-01 · The Chronicler — рассказчик (закадр)

| Поле | Значение |
|---|---|
| Сцены пилота | 5 (5:20–6:11.5), 7 (7:20–7:57.5), 19. Никогда до 5:20 (сценарий `script.md`); никогда поверх лица |
| Темп Sc 5 (режиссёр, приёмка раскадровки §4.3) | фразы 1, 3, 5 — ~110 сл/мин; фразы 2 и 4 — ~120–125 сл/мин, сухо, **без ускорения на числах**. Темп набирается настройкой `speed` и паузами в монтаже, текст не меняется (таблица ниже) |
| В титрах | только **"The Chronicler"** |
| Эмоциональный диапазон | **намеренно нулевой.** Архивное ровное чтение. Слышно лишь едва заметное удовлетворение на числах и датах. Аудиотеги эмоций **не используются** вообще |
| Темп | ~110 слов/мин. Медленнее любого персонажа S1 |
| Текст | только дословно по сценарию: без сокращений, перефразов и правок чисел. Если строка не ложится в TTS, через директора идёт запрос главному сценаристу. На месте не правим. Произношение — только через словарь (`tts_pronunciation_test.md`), сам текст не трогаем |
| Подпись | «…and the water kept its counsel.» — **один** утверждённый дубль, архивируется и ставится в конце каждого сезона тем же файлом |
| Сведение | сухо и близко, «человек читает за столом»; перед первым словом Sc 5 — только перелистывание страницы. Голос рассказчика не стоит встык ни с одной репликой персонажа: между ними всегда ≥ 2 с другого звука или смена сцены |
| Версии голоса | NARR-01a — S1–S6; NARR-01b — с S7E1, заметно более хриплый. Оба голоса и их эталонные дубли делаются и утверждаются **сейчас**, вместе. Потом не перегенерируются |
| Закрепление | `voice_id`, модель TTS и её версия, все настройки, seed, текст пробы — фиксируются на всю сагу (`production_notes` §7: «lock the voice ID at the first TTS probe»). Смена модели — только решением директора. Порядок генерации и закрепления — служебный протокол SD-R1 (у директора) |
| ElevenLabs | имя голоса `HS NARR A` / `HS NARR B`; `voice_id` — |

**Voice Design (EN), NARR-01a:**
```text
Elderly man over eighty, a record-keeper reading aloud from an official chronicle. Dry, precise, papery voice in a light baritone range: not deep, not booming, no trailer-voice colour. A light natural hoarseness. Every consonant clear and every word finished; unhurried, about one hundred and ten words a minute. Neutral and archival, emotionally even: he reads entries, he does not tell stories, and only numbers and dates get the faintest satisfaction. Educated, old-fashioned neutral accent. Very close, dry microphone, no room, no reverb, no music.
```

**NARR-01b (с S7E1):** тот же промпт, но вместо «A light natural hoarseness» стоит «A clearly hoarser, rougher voice than before, the same precision». Способ получения — по протоколу SD-R1.

**Тестовая фраза (EN, 432 симв.):**
```text
The Chronicle of the Dry Years. In the matter of the tithe, the following is set down, as written. Neveh Ashare. House Ilvane. Oshra. Highwater. The Ninth Sluice. ... The First Voices raised the Spires. They are not heard now. ... Of the nine Spires, eight still answered. One of the eight answered badly. ... Three hundred and twelve years, each with its tithe, and each balance carried forward. ... and the water kept its counsel.
```

**Настройки (старт):**

| Режим | v2 | v3 | v4 |
|---|---|---|---|
| Единственный | 0.75 / 0.85 / 0.00 / 0.85 | Robust | 0.75 |

**Sc 5 по кадрам (раскадровка `storyboard/S01E01/sc05.md`):**

| Фраза | Кадр, старт | Окно | Текст (FIXED, дословно) | Темп | v2 speed (старт) | Дубли |
|---|---|---|---|---|---|---|
| 1 | sc05-sh010, 5:20.0 | 6 с | «The First Voices raised the Spires. They are not heard now.» | ~110 сл/мин | 0.85 | 1 файл |
| 2 | sc05-sh020, 5:26.0 | 11 с | «In the last year of the old kingdom, the nine warden families found Queen Neveh past reason, and her court with her.» | ~120–125 | 0.93 | 1 файл |
| — | sh030–sh050, 5:37–5:46 | 3 × 3 с | молчат (допуск ±1 с на кадр, не короче 2,5 с) | — | — | — |
| 3 | sc05-sh060, 5:46.0 | 5.5 с | «She sang her city into the sea.» | ~110 | 0.85 | 1 файл |
| 4a | sc05-sh070, 5:51.5 | 5 с | «The Nine made their Concord on what stayed dry.» | ~120–125 | 0.93 | **отдельный файл** |
| 4b | sc05-sh080, 5:56.5 | 12 с | «This is the three hundred and twelfth year of that Concord: three hundred and twelve years, each with its tithe, and each balance carried forward.» | ~120–125, на числах без разгона | 0.93 | **отдельный файл** |
| 5 | sc05-sh090, 6:08.5 | 3 с | «…and the water kept its counsel.» | ~110 | архивный дубль подписи | — |

- Фраза 4 пишется **двумя дублями**, она делится по точке. Между 4a и 4b — пауза ~0,6 с (склейка sh070 → sh080). Каждый дубль генерируется на одних настройках, чтобы на склейке не прыгали тембр и уровень. Перед утверждением проверяем шов на слух.
- «Без ускорения на числах»: «three hundred and twelve years…» идёт тем же темпом, что весь 4b. Если модель разгоняется, берём другой дубль, а не поднимаем `speed`.
- В v4 параметра `speed` нет. Темп на v4 — только выбором дубля и паузами в монтаже (растяжение не больше ±5 %).
- Окончательные длительности — по черновой озвучке на шаге 1 аниматика. Монтаж подгоняет молчаливые панели 3–5 (допуск ±1 с, не короче 2,5 с), а не голос.

Для этого голоса главный критерий A/B — **неизменность между дублями и через годы**, а не выразительность. Если 110 слов/мин не получается через `speed`, темп набираем паузами между фразами в монтаже. Текст ради темпа не меняется.

---

### V-16 · Clerk at the next desk (без имени, новый) — клерк банка Lantry

| Поле | Значение |
|---|---|
| Сцены | 14 (`[MS]` «Yes, Kett?», `[OS]` «It gets into everything.») |
| Звучание | маслянистый тенор, сама учтивость (сценарий v1.0.2) |
| ElevenLabs | `HS S1 V16`; `eleven_ttv_v3`; voice_id — §6; после пилота — только массовка (§0 п. 8) |

**Voice Design (EN):**
```text
Man in his thirties, a short, round, well-groomed senior bank clerk. Light, high, smooth tenor, oily and pleasant; all courtesy and smiles, with a faint condescension under the politeness. Clear, neutral, educated city accent with soft, precise consonants. He speaks lightly and quietly, as if to a friend across a desk. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN):**
```text
Yes, Kett? ... It gets into everything, the damp. The paper, the ink, the ledgers, the clerks. One learns to blot, and to smile. Of course, sir. I'll have the column on your desk before noon, sir.
```

---

### V-17 · Steward (без имени, новый) — распорядитель зала

| Поле | Значение |
|---|---|
| Сцены | 11 (`[OS]`, формула «The tithe cup…») |
| Звучание | ровный церемониальный голос, говорит формулу, произнесённую сотни раз |
| ElevenLabs | `HS S1 V17`; `eleven_ttv_v3`; voice_id — §6; после пилота — только массовка |

**Voice Design (EN):**
```text
Man in his sixties, a palace steward who announces ceremonies. Measured, resonant mid-range voice, formal and impersonal, reciting a formula he has said every year of his life; refined court accent with long rounded vowels, unhurried and faintly sing-song, projecting to a large hall without effort. Clean studio recording, close microphone, no background noise, no music.
```

**Тестовая фраза (EN):**
```text
The tithe cup. First the taster. Then the Helm. Then the guest of the reading. ... Be upstanding, my lords and ladies, for the reading of the Tithe Map. The hall will keep silence until the Helm has signed.
```

---

## 4. Реплики без отдельной карточки и вокал без слов

| Что | Сцена | Чей | Куда |
|---|---|---|---|
| Счёт шагов на колесе («one… two…» на одной высоте) | 2, 6 | 3–4 голоса массовки (MALE-WALLA-A…D, Voice Design «working men, flat monotone count») | стем **DXW** (слова массовки, `dubbing_ready.md`) |
| Шум зала, смех зала, гул толпы у ворот | 1, 10–12 | SFX-генерация, неразборчиво | M&E |
| Гогот Mags, вздохи и ахи без слов | 3 и др. | голос персонажа (TTS) | M&E (VOX-NL) |
| Мычание Liss (5 нот), младенец (2 ноты), Pell (3 ноты, Sc 3), нота Wick (Sc 4), тон Ione (Sc 9) | 1, 3, 4, 9 | **композитор** (мелодия и высота); звукорежиссёр передаёт эталоны речевых голосов Pell, Wick, Ione | M&E (вокал без слов не дублируется) |
| Juno, Fossett, Maren, Kes | 10–15, 18 | в E1 без реплик | карточки — к E2/E3 (у Juno и Fossett реплики в E3/E11) |

---

## 6. Журнал закрепления — черновой кастинг аниматика (2026-11-23)

Статус: **черновой** (для аниматика). Финальное закрепление по §0 п. 7 — после picture lock и слепого теста §2. NARR-01 — **кандидат**, не закреплён (animatic.md §3, протокол SD-R1 у директора).

Параметры дизайна у всех: `POST /v1/text-to-voice/design`, loudness 0, should_enhance false, без reference audio; превью сохранены (`output/S01E01/animatic/casting/<ID>/i<итерация>_p<номер>.mp3`, R2 `S01E01/animatic/casting/…`). Промпт и тестовая фраза каждой итерации, замеры всех превью — `casting/casting_log.json`; правки промптов — `casting/prompts.json`. Выбор превью — по замерам (медиана F0 к цели §2, темп), а не на слух: **прослушивание директором обязательно** до финала.

| ID | Персонаж | Имя в EL | voice_id | Модель дизайна | seed | guidance | итераций | превью | F0 превью / цель, Гц |
|---|---|---|---|---|---|---|---|---|---|
| V-01 | Pell | `HS S1 V01` | `iXg6m3okqCpdUH3cAzLs` | `eleven_ttv_v3` | 3101 | 5.0 | 1 | i1·p2 | 205.1 / 195 |
| V-02 | Wick | `HS S1 V02` | `K3PkIvwIWSsVOFh6ZwRq` | `eleven_ttv_v3` | 3111 | 5.0 | 1 | i1·p1 | 363.6 / 290 |
| V-03 | Nan | `HS S1 V03` | `yQutTeU9ri2pPwzgY7SO` | `eleven_ttv_v3` | 3121 | 5.0 | 1 | i1·p3 | 210.5 / 230 |
| V-04 | Ione | `HS S1 V04` | `JDqVQUWrTkqKJUi5V0Xo` | `eleven_ttv_v3` | 3131 | 5.0 | 1 | i1·p1 | 266.7 / 255 |
| V-05 | Hollis | `HS S1 V05` | `v0bxs05N6L36WwOa09ep` | `eleven_ttv_v3` | 3141 | 5.0 | 1 | i1·p3 | 131.1 / 130 |
| V-06 | Ruel | `HS S1 V06` | `WFG5Ms3p5WkToImSDDnd` | `eleven_ttv_v3` | 3152 | 5.0 | 2 | i2·p2 | 108.8 / 105 |
| V-07 | Lucan | `HS S1 V07` | `H2ScA5AaNufRh2PPnMdi` | `eleven_ttv_v3` | 3161 | 5.0 | 1 | i1·p3 | 119.4 / 95 |
| V-08 | Ursel | `HS S1 V08` | `4NQbUoR4U0anhExNcJRR` | `eleven_ttv_v3` | 3171 | 5.0 | 1 | i1·p3 | 173.9 / 175 |
| V-09 | Odo | `HS S1 V09` | `UmbFuACrLtlTZUAXLccZ` | `eleven_ttv_v3` | 3181 | 5.0 | 1 | i1·p3 | 116.8 / 115 |
| V-10 | Corr | `HS S1 V10` | `PWqxdNZLI6s0YLJIi8fG` | `eleven_ttv_v3` | 3191 | 5.0 | 1 | i1·p3 | 83.8 / 85 |
| V-11 | Mags | `HS S1 V11` | `Dac4C4KLxg2pJlsoYnoj` | `eleven_ttv_v3` | 3201 | 5.0 | 1 | i1·p1 | 266.7 / 240 |
| V-12 | Tithe-collector | `HS S1 V12` | `qG3cnlGxJgmMXqt4bbIm` | `eleven_ttv_v3` | 3211 | 5.0 | 1 | i1·p2 | 179.8 / 145 |
| V-13 | Choir attendant | `HS S1 V13` | `PJX2NeYe2aBGqobdcWhI` | `eleven_ttv_v3` | 3221 | 5.0 | 1 | i1·p3 | 179.8 / 200 |
| V-14 | Relay-keeper | `HS S1 V14` | `YFZRbyIZyYTBQIAglqXJ` | `eleven_ttv_v3` | 3231 | 5.0 | 1 | i1·p3 | 148.8 / 150 |
| V-15 | Rusk guard | `HS S1 V15` | `wsnsRkBo3fRmnw5VGA2N` | `eleven_ttv_v3` | 3241 | 5.0 | 1 | i1·p3 | 106.0 / 110 |
| V-16 | Clerk | `HS S1 V16` | `ezK9nLZpUgIsAhjVGvj1` | `eleven_ttv_v3` | 3252 | 5.0 | 2 | i2·p3 | 144.8 / 140 |
| V-17 | Steward | `HS S1 V17` | `3IeVnlQ7Cn67uf7nTumG` | `eleven_ttv_v3` | 3261 | 5.0 | 1 | i1·p1 | 158.4 / 125 |
| NARR-01 | The Chronicler (кандидат) | `HS NARR A cand` | `Kq376vQT4X9raogOKEpK` | `eleven_ttv_v3` | 3271 | 5.0 | 2 | i1·p2 | 106.0 / 115 |

**Озвучка аниматика (TTS):** персонажи — `eleven_v3`, stability 0.5 (Natural), similarity 0.8, seed 101 (дубль t2 — 202), аудиотеги по `S01E01_vo_plan.json`; NARR-01 — `eleven_multilingual_v2`, stability 0.75 / similarity 0.85 / style 0 / speaker boost, speed 0.72 (≈110 сл/мин) и 0.80 (фразы 2 и 4 Sc 5). Словарь произношений `hollowstone_en_draft_v1` (`lexicon/`). Паспорт каждого файла — `S01E01_vo_manifest.json`.

**Важное наблюдение для A/B (§«Модели TTS»):** голоса, задизайненные на `eleven_ttv_v3`, сохраняют тембр на `eleven_v3`, но на `eleven_v4` / `eleven_v4_turbo` уходят вверх: Corr 84 → 147 Гц, Ruel 105 → 135 Гц, Lucan 117 → 132 Гц (та же фраза, тот же seed); тяжёлые голоса на v4 читают на 20–25 % быстрее. Т.е. документация права: Voice Design + v4 = «менее выразительно», и для нашего каста это ещё и потеря регистра. Если финал пойдёт на v4 — голоса надо дизайнить заново под v4 (или проверить ремикс), иначе матрица §2 развалится.

---

## 5. Журнал изменений

| Дата | Что | Кто |
|---|---|---|
| 2026-11-22 | v1.0: 15 карточек персонажей + рассказчик; матрица различения; A/B расширен до трёх моделей (v2 / v3 / v4) | звукорежиссёр |
| 2026-11-23 | v1.1: поручения режиссёра (приёмка раскадровки §4.3): темп Sc 5 по фразам, фраза 4 — двумя дублями; отдельные дорожки «Pell. Mouth.» (V2) и реплики Nan (V4); новые таймкоды | звукорежиссёр |
| 2026-11-23 | v1.2: черновой кастинг аниматика — 18 голосов (15 карточек + V-16 Clerk, V-17 Steward, NARR-01 кандидат), §6 журнал; промпты V-01/V-02/V-11 без возраста (блок фильтра), V-06 итерация 2, V-15 молодой | звукорежиссёр |
