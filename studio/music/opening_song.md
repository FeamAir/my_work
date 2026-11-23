# HOLLOWSTONE — песня-опенинг «Louder Than the Tide»

Версия 0.2 · 2026-11-22 · композитор · статус: **черновик к утверждению** (v0.2: решения директора — S1E2 инструментальный опенинг, песня с S1E3; `store_for_inpainting` для мастера темы; «Доски» без пятёрок) (текст и концепция утверждает директор; платные генерации только с его разрешения)
Источники: решение инвестора и директора 2026-11-22 (опенинг серий 2–12 — песня с вокалом на английском на мелодии главной темы; инструментальная версия остаётся; уточнение директора: в S1 песня звучит с E3, в E2 — инструментальный опенинг), `BRIEF.md`, `music/main_theme.md`, `music/leitmotifs.md` §0, `canon/excerpts/for_composer.md` (закрыто, все запреты §3 соблюдены), `story/series_bible.md` §2, §5, §9, §12.3, `story/saga_arc.md` (только тон), `story/season01_outline.md` (E2, E3), `marketing/title.md` §5.
Документация ElevenLabs, сверено 2026-11-22: [composition plans](https://elevenlabs.io/docs/eleven-api/guides/how-to/music/composition-plans.md), [inpainting / conditioning](https://elevenlabs.io/docs/ja/eleven-api/guides/how-to/music/inpainting).

Рабочее имя трека — **Louder Than the Tide** (запасное — **Hush Law**, см. §9). Файлы: `lib_mus_op-song_v1.wav` и нарезки (§6).

---

## 0. Что это и как соотносится с главной темой

- **Песня = главная тема со словами.** Мелодия припева — крючок темы (октавный скачок C♯4 → C♯5, затем B4 A4 G♯4 A4), предприпев — фраза B темы, куплет — фраза A. Тональность та же (F♯ минор), сетка та же (такт темы 3,0 с), поэтому песня и инструментальный мастер монтируются одним и тем же клипом и узнаются как одно целое.
- **Инструментальный мастер темы не меняется** (`main_theme.md`): он остаётся для титра пилота, эндинга пилота, титров и для серий, где песня неуместна (§8.3).
- **Голос в опенинге — смысловое событие, а не просто «так принято».** В мире, где беднякам запрещено петь, песня начинается одним голосом в тишине и говорит то, что Низы вслух сказать не могут. Поэтому припев не «про героя», а про право голоса — главную открытую тему саги (`series_bible.md` §9.2).

## 1. Концепция

| Параметр | Решение |
|---|---|
| **Жанр** | оригинальный **кинематографичный рок-гимн с оркестром и телесной перкуссией** («tide-rock»): живая ударная установка в двойном темпе, струнные и валторны из главной темы, топот и хлопки Низов, свист двумя пальцами, плотный бас, перегруженная ритм-гитара **только в припевах** как стена (без соло). Энергия современного аниме-опенинга, звук — из мира саги, а не из жанрового шаблона |
| **Темп** | **160 BPM в ударных** (двойной темп) при **80 BPM в мелодии** (как у темы). Такт 160 = 1,5 с, такт темы = 3,0 с. Все секции кратны 3,0 с — склейки клипа ложатся на тактовую черту |
| **Тональность** | **F♯ минор (эолийский)**, без модуляций. Ключевой подъём в финале делается не сменой тональности, а выходом голоса на верхнюю квинту (C♯5) и полным составом |
| **Размер** | 4/4 везде |
| **Вокал** | один **женский голос**, альт–меццо, рабочий диапазон **C♯4–F♯5** (середина полосы телефона). Плотная грудь и белтинг на верхних долгих нотах, лёгкая хрипотца и «зерно», прямая подача почти без вибрато (вибрато только в самом хвосте долгих нот), чёткая английская дикция. Звучит как человек с улицы, который впервые поёт в полный голос: **не оперно и не «церковно»** — это противоположность Канторам и Хору. Голос никому из героев не принадлежит и не озвучивает персонажа |
| **Подголоса** | только **выкрики толпы в унисон** («Hey!», «Who's gonna pay?») в среднем регистре, как речёвка. Без хора, без аккордового пения, без бессловесных «ah/ooh» и без пения с закрытым ртом |
| **Длительность** | **1:30,0 ровно** (30 тактов темы × 3,0 с), TV-size |
| **Характер** | тревожная надежда → злость → упрямое «мы здесь». Слушатель должен после одного прослушивания пропеть «Sing — louder than the tide» |

### 1.1. Что сохранено из правил студии (проверено построчно)

1. **Не цитирует колыбельную и мотив загадки:** другая тональность и тоника, 4/4, контур каждой фразы начинается со скачка вверх. Ни одной мелодической или ритмической группы из пяти нот или долей: строка-крючок — 6 слогов и 6 нот, все строки припева 6–8 слогов; выкрик толпы — 4 слога. Девиз «who pays for the dry» (5 слогов) в песне нарочно растянут до «who's gonna pay for the dry» (8).
2. **Резервный тон (A♯/B♭) не звучит вообще:** его нет в ладу, в мелодии, в гармонии и в басе. Поэтому запрещены аккорд F♯ мажор (пикардийская терция) и модуляции вверх на тон или полутон (обе целевые тональности его содержат). Финальный аккорд — **пустая квинта F♯–C♯**, как у темы.
3. **Нижний регистр:** бас только короткими нотами (опора ритма); никакого выдержанного тона, дрона, педали и саб-баса ниже F♯2, никаких 808. Бочка — короткая, без настроенного «гудящего» хвоста.
4. **Телефон:** вся мелодия C♯4–F♯5 (277–740 Гц), крючок C♯4–C♯5. Проверка фильтром ФВЧ 300 Гц + ФНЧ 8 кГц обязательна.
5. **Без хора, гула и пения с закрытым ртом;** нет темы дома или героя внутри песни; нет звука перстня, камня, осколка.
6. **Ритм для фанатов** — простой бэкбит: топот на 1 и 3, хлопок на 2 и 4 (в счёте темы — топот на сильную, хлопок на третью долю). В бридже (1:12–1:15) допустимы «Доски» в исправленном виде (`leitmotifs.md` §2, v0.2: ♩. ♪ ♩ ♩, четыре удара в такте); «Часы» (три удара и пауза) — никогда.

## 2. Структура и таймкоды (для монтажа)

Счёт: **T** = такт темы 3,0 с (= 2 такта ударных по 1,5 с). Сильная доля каждого T — склейка.

| # | Секция | Время | T | Мелодия (из темы) | Гармония (предложение) | Что звучит |
|---|---|---|---|---|---|---|
| 1 | **Intro — the call** | 0:00,0–0:06,0 | 2 | крючок | — (подразумевается F♯m) | **голос a cappella**, близко, сухо, в тишине: первая строка припева. Последние 0,4 с — вдох |
| 2 | **Groove — the Lows** | 0:06,0–0:12,0 | 2 | — | F♯m | **удар всего состава на 0:06,0**, затем топот/хлопки, ударная установка 160, остинато струнных и арфы F♯–C♯–E–C♯ (3+3+2), бас короткими нотами. Свист двумя пальцами на 0:11,25 |
| 3 | **Verse** | 0:12,0–0:30,0 | 6 | фраза A + A′ | F♯m – D – F♯m – E – D – E | голос в среднем регистре, плотно и ритмично; каждая строка = 3,0 с и начинается на тактовой черте; ударные «вполсилы» (римшот, хлопки) |
| 4 | **Pre-chorus — the Steps** | 0:30,0–0:42,0 | 4 | фраза B (D5 → F♯5 → C♯5) | D – E – C♯sus4 – C♯ | валторны отвечают голосу, нарастание, дробь малого. На «now» (0:39,0) голос держит C♯5. **0:41,25–0:42,0 — полная пауза («воздушный карман», 0,75 с)** |
| 5 | **Chorus** | 0:42,0–1:06,0 | 8 | крючок ×2 + ответ | F♯m – A – D – E (×2), конец на F♯m | весь состав: ударная установка в полную, гитарная стена, струнные и валторны в унисон с голосом, топот и хлопки. **Скачок на «LOU-» в 0:42,75** |
| 6 | **Bridge — the water** | 1:06,0–1:15,0 | 3 | речитатив C♯4–E4 | D – Bm – (без гармонии) | внезапный спад: голос + одна виолончель (1:06–1:12); 1:12–1:15 — только топот/хлопки и выкрик толпы, дробь в финал |
| 7 | **Final chorus** | 1:15,0–1:27,0 | 4 | крючок + ответ на квинте | F♯m – A – D – E | максимум; скачок на 1:15,75; последнее «own» голос держит на **C♯5** (открыто, как конец фразы B темы) с 1:22,5 до 1:27,0 |
| 8 | **Outro — the button** | 1:27,0–1:30,0 | 1 | — | пустая квинта F♯–C♯ | **удар-аккорд на 1:27,0**, хвост арфы и тарелки, чистое затухание к **1:30,0** (жёсткий конец под титр серии) |

Итого 2+2+6+4+8+3+4+1 = **30 T = 1:30,0**.

### 2.1. Привязка мелодии к словам (для гайда и проверки)

- **Крючок** (2 T = 6 с): `Sing` — C♯4, ♩ (0,75 с) · `LOU-` — **C♯5**, 𝅗𝅥. (2,25 с) · `-der than` — B4 A4, ♪♪ · `the` — G♯4, ♩ · `TIDE` — A4, 𝅗𝅥 (1,5 с). Долгие ноты стоят на открытых гласных /aʊ/ и /aɪ/ — их удобно петь громко и узнавать.
- Строка 2 припева (`we were never made to hide`) — та же форма со скачком на малую септиму (C♯4 → B4), конец на G♯4 — «вопрос».
- Строка 4 (`this voice is all we own`) — каденция: `ALL` на E5, `own` разрешается на F♯4 (в финальном припеве — остаётся на C♯5).
- **Куплет:** каждая строка начинается короткой нотой C♯4 и скачком на ударный слог (A4 в строках 1–2, B4 в строках 3–4), затем оседает ступенями; строки 5–6 поднимаются речитативом E4–F♯4–A4 и повисают на B4 перед D5 предприпева.
- **Предприпев:** `Keep` — D5 (долгая), далее по фразе B; `now` — C♯5 на целый T.

## 3. Текст (English, оригинал)

```text
[Intro — a cappella]
Sing — louder than the tide...

[Groove]
(Hey!)

[Verse]
Down where the lanterns float in the street,
we keep the time with our hands and our feet.
Up on the towers the song is for sale —
calm can be bought by the ones who don't bail.
Whistle the warning, the water is high:
so who's gonna pay for the dry?

[Pre-chorus]
Keep your head down, keep it in your chest,
let the ones up high do the rest —
but the water's at the window,
and the hollow stone won't save us now...

[Chorus]
Sing — louder than the tide,
we were never made to hide.
Sing — louder than the tide:
this voice is all we own.

[Bridge]
They can buy the calm and the quiet,
and the water keeps its counsel —
(Who's gonna pay?)

[Final chorus]
Sing — louder than the tide:
this voice is all we own!
```

### 3.1. Пасхалки (только открытое, без раскрытий)

| Строка | Что знает внимательный зритель |
|---|---|
| `calm can be bought` | девиз Низов «Calm is bought» (S1E2) |
| `who's gonna pay for the dry` | девиз саги «Who pays for the dry?» (S1E4), звучит в каждом сезоне |
| `the hollow stone won't save us now` | название сериала; Шпили слабеют — это открытая завязка |
| `the water keeps its counsel` | эхо подписи Летописца «…and the water kept its counsel» |
| `whistle the warning` | свистовые сигналы Низов вместо голоса |
| `ones who don't bail` | знать не вычерпывает воду из домов — Ступени не тонут |
| `this voice is all we own` | цена песни — голос; беднякам принадлежит только он |

### 3.2. Чего в тексте нет (проверено)

Имён и топонимов, которых зритель не знает; слов *hum, lullaby, cradle, sleep, five, verse, blood, mouth, ring, pearl, shard, drowned queen, builders*; оборота *sing out* (в каноне это гибель певца); строк о том, что камень или вода отвечают голосу бедняка; намёков на затонувший Шпиль, на «тон, которым не пользуется ни один камень», на родство героев. Песня о праве голоса, а не о том, *чья* песня на самом деле, — это остаётся тайной саги.

## 4. Крючок для TikTok / Shorts

| Нарезка | Время в мастере | Длина | Зачем | Файл |
|---|---|---|---|---|
| **Hook (основная)** | 0:40,5–0:48,0 | 7,5 с | хвост предприпева «…won't save us **now**», пауза 0,75 с, **удар на 0:42,0** (через 1,5 с от начала клипа) — точка для монтажных переходов; затем вся первая строка «Sing — louder than the tide». Конец на тактовой черте 0:48,0, хвост «tide» обрезается фейдом 0,3 с | `lib_mus_op-song_hook7_v1.wav` |
| **A cappella (для каверов и дуэтов)** | 0:00,0–0:07,5 | 7,5 с | голос один, без инструментов, затем удар группы на 6,0 с. Идеально для «спой со мной» и дуэтов | `lib_mus_op-song_acap7_v1.wav` |

**Как вырезать (бесплатно, ffmpeg):** резать по тактовой черте с точностью до семпла, без фейда на входе (вход хука начинается с ноты, а не с тишины); фейд-аут 0,3 с; отдельный мастер −14 LUFS / −1 dBTP; моно-совместимость проверить (телефон). Проверка: удар 0:42,0 должен попадать ровно на 1,5 с от начала нарезки — монтажёры будут ставить переход именно туда.

**Жест для тренда** (предложение маркетологу, без раскрытий): на «Sing —» (0:42,0) человек закрывает рот ладонью («закон тишины»), на скачке «LOU-» (0:42,75) отбрасывает руку и поёт. Простой, читается без звука, привязан к главной теме мира.

**Для каверов:** выкладываем также инструментал (караоке) и чистый вокал — без них перепевают намного реже (§6).

## 5. План генерации ElevenLabs Music

`POST /v1/music`, `model_id: "music_v2_5"` (передавать явно), `composition_plan` в схеме v2 (`chunks`), каждый чанк 3–120 с, до 30 чанков; стили — по-английски, текст — в `text` строками через `\n`, звуки в `( )`, указания в `{ }`. `seed` фиксируем и записываем. Чтобы на результат можно было ссылаться (`conditioning_ref`, вставка куска `song_id` + `range`), генерация идёт с `store_for_inpainting: true`. `conditioning_ref` — до 30 000 мс, `condition_strength`: `low | medium | high | xhigh`.

### 5.0. Условие старта

План стартует **только после утверждения мастера темы** (`lib_mus_theme-master_v1`). **Решение директора 2026-11-22:** мастер темы (и эскиз темы) генерируются с `store_for_inpainting: true` — внесено в `main_theme.md` §7. Так `song_id` мастера сразу доступен для `conditioning_ref`, загрузка через `/v1/music/upload` не нужна. Эскиз и финал песни тоже генерируются с `store_for_inpainting: true`; все `song_id` и `seed` записываются в журнал генераций.

Обозначения ниже: `THEME` — `song_id` мастера темы; `SKETCH` — `song_id` утверждённого эскиза песни.

### 5.1. Шаги

| Шаг | Что | Длина | Дубли | Цена |
|---|---|---|---|---|
| 0 | Гайд: ноты голоса (§2.1) по слогам, синтез 80/160 BPM; чтение текста вслух на ритм; проверка текста поиском по строкам; прослушивание мелодии на сходство с известными | — | — | бесплатно |
| 1 | **Эскиз: предприпев + припев** (2 чанка: 12 с + 24 с), чанк припева с `conditioning_ref` на крючок темы `THEME 60000–72000`, `condition_strength: medium` | 36 с | ≤ 3 (разные `seed`) | платно |
| 1a | *Только если шаг 1 не держит октавный скачок:* загрузить гайд-мелодию 24 с и дать её в `conditioning_ref` (`high`) — меняем подход, а не жмём «ещё раз» | 24 с | 1 | платно (как генерация) |
| 2 | **Финал 1:30** — план §5.2: припевы с `conditioning_ref` на припев утверждённого эскиза (`SKETCH`), грув — на грув темы | 90 с | ≤ 3 | платно |
| 3 | Точечная правка (если брак в одном месте: слово, лишний инструмент): план из чанков-вставок `song_id`+`range` финала и одного перегенерируемого чанка | 90 с (см. ниже) | ≤ 2 | платно |
| 4 | Инструментал и чистый вокал — **разделение на стемы бесплатным локальным инструментом** (открытый сепаратор источников); нарезки, громкость, проверки | — | — | бесплатно |

**Критерии отбора эскиза и финала:** (1) скачок C♯4 → C♯5 на «Sing — LOU-» есть и узнаётся через фильтр «телефон»; (2) слова припева разборчивы с первого прослушивания; (3) директор после одного прослушивания пропевает крючок; (4) голос — не оперный, без хора и «ooh»; (5) нет модуляции и мажорного финала; (6) нет тонального гула ниже F♯2 (спектр); (7) нет сходства с известными песнями. Брак по пунктам 1–3 после трёх дублей → меняем план (стили, `condition_strength`, гайд), фиксируем вывод в библиотеке приёмов.

### 5.2. План финала (`composition_plan`, 8 чанков, 90 000 мс)

```json
{
  "chunks": [
    {
      "text": "[Intro]\nSing — louder than the tide...\n{a cappella, solo voice in silence, short breath at the end}",
      "duration_ms": 6000,
      "positive_styles": ["cinematic anime opening rock anthem", "F-sharp minor", "80 BPM melody over 160 BPM double-time drums", "solo female lead vocal, alto to mezzo, strong chest voice, slightly raspy grainy edge, direct and unpolished, minimal vibrato, clear English diction", "a cappella for this section, close and dry", "the first note is short and low, the second leaps a full octave up and is held", "defiant, hopeful, urgent"],
      "negative_styles": ["drums", "instruments", "choir", "backing vocals", "humming", "operatic", "auto-tune", "reverb wash"],
      "context_adherence": "high",
      "conditioning_ref": { "song_id": "SKETCH", "range": { "start_ms": 12000, "end_ms": 18000 } },
      "condition_strength": "medium"
    },
    {
      "text": "[Groove]\n{full band hit on the downbeat, then body percussion groove}\n(Hey!)",
      "duration_ms": 6000,
      "positive_styles": ["instrumental", "huge full-band hit on beat one", "live drum kit at 160 BPM, tight and punchy", "foot stamps on wooden planks and hand claps on the backbeat", "harp and string pizzicato ostinato in eighth notes grouped 3+3+2", "punchy bass guitar in short notes", "one sharp two-finger whistle at the end", "group shout 'Hey!' in unison"],
      "negative_styles": ["lead vocals", "choir", "sub bass", "808", "synth pad", "EDM drop", "5/4"],
      "context_adherence": "high",
      "conditioning_ref": { "song_id": "THEME", "range": { "start_ms": 12000, "end_ms": 24000 } },
      "condition_strength": "medium"
    },
    {
      "text": "[Verse]\nDown where the lanterns float in the street,\nwe keep the time with our hands and our feet.\nUp on the towers the song is for sale —\ncalm can be bought by the ones who don't bail.\nWhistle the warning, the water is high:\nso who's gonna pay for the dry?",
      "duration_ms": 18000,
      "positive_styles": ["female lead vocal in the middle register, rhythmic and tight", "each line starts with a short note and leaps up to the stressed word", "drums at half intensity: rimshots, claps, kick", "string ostinato continues", "bass guitar short notes", "building tension", "street energy, stubborn"],
      "negative_styles": ["choir", "harmonies", "rap", "humming", "sub bass", "distorted guitar"],
      "context_adherence": "high"
    },
    {
      "text": "[Pre-Chorus]\nKeep your head down, keep it in your chest,\nlet the ones up high do the rest —\nbut the water's at the window,\nand the hollow stone won't save us now...\n{full stop, half a beat of silence before the chorus}",
      "duration_ms": 12000,
      "positive_styles": ["melody climbs to a high F-sharp and settles on a long held C-sharp", "French horns answer the voice with proud descending calls", "harmony climbs D major, E major, C-sharp suspended, C-sharp major", "snare drum roll building", "rising tension", "ends with a sudden silent gap"],
      "negative_styles": ["choir", "riser synth", "EDM build", "key change", "sub bass"],
      "context_adherence": "high"
    },
    {
      "text": "[Chorus]\nSing — louder than the tide,\nwe were never made to hide.\nSing — louder than the tide:\nthis voice is all we own.",
      "duration_ms": 24000,
      "positive_styles": ["anthemic chorus, full power", "the melody leaps a full octave on 'louder' right after the downbeat", "female lead vocal belting in chest voice", "live drums at 160 BPM full energy, big crash on the downbeat", "overdriven rhythm guitar wall", "strings and French horns in unison with the vocal melody", "foot stamps and hand claps on the backbeat", "catchy, easy to sing along"],
      "negative_styles": ["choir", "harmonized backing vocals", "guitar solo", "key change", "sub bass", "808", "major ending"],
      "context_adherence": "high",
      "conditioning_ref": { "song_id": "SKETCH", "range": { "start_ms": 12000, "end_ms": 36000 } },
      "condition_strength": "high"
    },
    {
      "text": "[Bridge]\nThey can buy the calm and the quiet,\nand the water keeps its counsel —\n{band drops out, only stamps and claps}\n(Who's gonna pay?)",
      "duration_ms": 9000,
      "positive_styles": ["sudden drop to near silence", "intimate low female voice, almost spoken, with one solo cello", "then only foot stamps and hand claps", "group shout in unison, not sung", "snare fill into the final chorus"],
      "negative_styles": ["choir", "pad", "drone", "sub bass", "humming", "guitar"],
      "context_adherence": "high"
    },
    {
      "text": "[Final Chorus]\nSing — louder than the tide:\nthis voice is all we own!",
      "duration_ms": 12000,
      "positive_styles": ["biggest moment of the song", "octave leap on 'louder' right after the downbeat", "the last word held long on the high fifth, open and unresolved", "full band, strings and horns in unison with the voice", "stamps and claps at full", "triumphant and desperate at once"],
      "negative_styles": ["key change", "choir", "fade out", "sub bass", "major chord"],
      "context_adherence": "high",
      "conditioning_ref": { "song_id": "SKETCH", "range": { "start_ms": 12000, "end_ms": 24000 } },
      "condition_strength": "high"
    },
    {
      "text": "[Outro]\n{one final full-band hit, ringing open fifth, clean decay}",
      "duration_ms": 3000,
      "positive_styles": ["instrumental", "single final hit on an open fifth F-sharp and C-sharp, no third", "harp and cymbal tail", "clean natural decay to silence"],
      "negative_styles": ["vocals", "new melody", "major chord", "abrupt cut", "sub bass"],
      "context_adherence": "high"
    }
  ]
}
```

**Эскиз (шаг 1)** — те же чанки `[Pre-Chorus]` (12 000) и `[Chorus]` (24 000); первым идёт припевный жанровый набор стилей из чанка 5, чтобы первый чанк задал жанр (по документации стили первого чанка задают тон всей вещи). У припева `conditioning_ref: THEME 60000–72000`, `medium`. В эскизе припев начинается на 12,0 с — отсюда диапазоны `SKETCH` выше.

### 5.3. Оценка минут генерации

| | Ожидаемо | Потолок |
|---|---|---|
| Эскиз 36 с | 2 дубля = 72 с | 3 = 108 с |
| Загрузка гайда (1a) | 0 | 24 с |
| Финал 90 с | 2 дубля = 180 с | 3 = 270 с |
| Правка (3) | 1 = 90 с | 2 = 180 с |
| **Итого** | **≈ 5,7 мин** | **≈ 9,7 мин** |

Правку считаю по полной длине плана (90 с): по документации не ясно, списываются ли вставленные без изменений куски — **проверить у IT до шага 3**; если не списываются, правка стоит ≈ 10–15 с. Стемы, нарезки, громкость, проверки — бесплатно. Стоимость в кредитах считает продюсер по тарифу. Платных вызовов не было.

## 6. Что сдаётся

| Ассет | Длина | Громкость | Файл |
|---|---|---|---|
| Опенинг-песня (TV size) | 1:30,0 | отдельный файл −14 LUFS / ≤ −1 dBTP; в серии MUS по `sound_bible.md` §5.2 | `lib_mus_op-song_v1.wav` |
| Инструментал (караоке, для каверов) | 1:30,0 | −14 LUFS | `lib_mus_op-song_inst_v1.wav` |
| Чистый вокал (для дуэтов и ремиксов) | 1:30,0 | — | `lib_mus_op-song_vox_v1.wav` |
| Hook 7,5 с | 0:40,5–0:48,0 | −14 / −1 | `lib_mus_op-song_hook7_v1.wav` |
| A cappella 7,5 с | 0:00,0–0:07,5 | −14 / −1 | `lib_mus_op-song_acap7_v1.wav` |
| Инструментальный опенинг (из мастера темы, без изменений) | 1:30 | как в `main_theme.md` §5 | `lib_mus_theme-op_v1.wav` |

Обе версии опенинга идут по **одной сетке 3,0 с** — один и тот же видеоклип опенинга можно подложить под любую. Сильные доли совпадают точно: удар 0:42,0 песни = такт 15 мастера; если режиссёр хочет, чтобы «гавань в стекло» совпадала в обеих версиях, монтаж инструментальной версии сдвигается под песню (решает режиссёр, §7).

**Пометки AI (обязательно, `marketing/title.md` §5.4):** на YouTube опенинг, плейлисты и Shorts с песней — AI-музыка как главная часть видео, раскрытие обязательно. В описании песни: «Music and vocals generated with AI (ElevenLabs Music) · HOLLOWSTONE». Звук в TikTok называть `Louder Than the Tide — HOLLOWSTONE (AI-generated)`. Никаких выдуманных имён исполнителя или композитора.

## 7. Пометки для режиссёра (акценты под монтаж)

Склейки на тактовой черте каждые 3,0 с; внутри — 1,5 с. Предложения по содержанию — на решение режиссёра.

| Время | Музыкальное событие | Предложение по кадру |
|---|---|---|
| 0:00,0 | голос в полной тишине | чернота → одна фигура на крыше свайного дома **со спины**, рта не видно. **Никакого липсинка песни ни у кого из героев** (и производственно, и по смыслу — голос «ничей») |
| 0:05,6 | вдох | вспышка спиральных борозд Шпиля |
| **0:06,0** | **удар всего состава** | **логотип HOLLOWSTONE** (самое сильное место для титра) |
| 0:06,0–0:12,0 | топот 0:06,0 / 0:07,5 / 0:09,0 / 0:10,5, хлопки между ними | Низы: доски, руки, колёса — монтаж в такт топоту; свист **0:11,25** — резкий поворот головы |
| 0:12 / 0:15 / 0:18 / 0:21 / 0:24 / 0:27 | начала строк куплета | герои по одному на каждую строку, каждый на своём этаже города; «towers… song is for sale» (0:18) — Ступени; «who's gonna pay for the dry» (0:27) — Карта податей |
| 0:30,0 | вход валторн | Ступени, Ринг, знамёна по цветам домов |
| 0:36,0 | «the water's at the window» | вода у стекла / у порога изнутри дома |
| 0:39,0–0:41,25 | «hollow stone won't save us **now**» (C♯5 держится) | свечение Шпиля гаснет, борозды тускнеют |
| **0:41,25–0:42,0** | **полная пауза 0,75 с** | один кадр черноты или вода без звука |
| **0:42,0** | **удар, «Sing»** | взрыв движения |
| **0:42,75** | **октавный скачок «LOU-»** | **гавань превращается в стекло** (тот же образ, что в инструментальной версии на 1:00) |
| 0:48,0 | «we were never made to hide» | армии и флоты, большие планы |
| 0:54,75 | второй скачок | Кантор в горле короны, спиной к камере |
| 1:00,0 | «this voice is all we own» | герои вместе (без раскрытий связей) |
| **1:06,0** | **спад: голос + виолончель** | тишина воды, рука с солью |
| 1:09,0 | «the water keeps its counsel» | раскрытая хроника / гобелен (без текста крупно) |
| 1:12,0–1:15,0 | только топот и хлопки; выкрик **1:13,5** | толпа Низов, руки вверх; дробь — быстрый монтаж |
| **1:15,0 / 1:15,75** | финальный припев, скачок | самый большой кадр опенинга (все Шпили, вал воды, флот) |
| 1:22,5–1:27,0 | «own» на C♯5, открыто | медленный наезд на одну фигуру |
| **1:27,0** | **финальный удар** | стоп-кадр / логотип малый |
| 1:27–1:30,0 | хвост квинты | титр серии; к 1:30,0 — чистая тишина |

**В опенинге никогда** (как и в инструментальной версии, `main_theme.md` §6): колыбельная, её ритм, тон камня, перстень и камень в одном кадре. Добавлю: никто из героев не поёт эту песню в кадре.

## 8. Решения и ограничения

1. **Отступление от `main_theme.md` §3 только для песни:** разрешены ударная установка, бас-гитара (короткие ноты) и перегруженная ритм-гитара в припевах — это язык аниме-опенинга. Электрогитара без соло и без «шреда», только стена в припевах. Мастер темы остаётся без вокала и гитар.
2. **Голос — один, выкрики толпы — речёвка, не хор.** Многоголосное пение остаётся сюжетным событием саги и не тратится на заставку.
3. **Где песня неуместна — инструментальный опенинг** (`lib_mus_theme-op_v1.wav`) или без опенинга (решает директор). **S1E2 — инструментальный опенинг, песня впервые звучит в S1E3** (решение директора 2026-11-22): голос Низов впервые прорывается в кадре в конце E2 (выдержка §3.8), и песня входит в заставку только после него. Мои предложения по остальным сериям S1 (на решение директора): **E9** (серия после ранения Руэла, его смерть) — инструментальный; **E10** (наводнение и Великая песня) — без опенинга, холодный пролог переходит прямо в серию; **E12** — песня.

## 9. Запасные варианты припева

Оба — на той же мелодии крючка (6 слогов в строке-крючке, долгая открытая гласная на скачке), без пятёрок, без раскрытий.

**Вариант B — «Rise» (светлее, про прилив):**
```text
Rise — higher than the sea,
every voice they took from me.
Rise — higher than the sea:
nobody sings for free.
```
Скачок на «HIGH» (/aɪ/), строка-ответ «nobody sings for free» — двойной смысл: беднякам петь нельзя, а знать продаёт песню. Минус: «sea» (/iː/) на долгой ноте поётся хуже, чем «tide».

**Вариант C — «Hush Law» (злее, перекличка с толпой; название песни сменится на *Hush Law*):**
```text
Break — every word of the law, (Hey!)
we've been quiet long enough.
Break — every word of the law: (Hey!)
who's gonna pay for the dry?
```
Скачок на «EV-» (/ɛ/), выкрики толпы на паузах — сильнее для хлопков и каверов. Минус: менее певуче, «закон» без контекста непонятен новому зрителю.

Рекомендую основной вариант: лучшая фонетика на скачке, крючок самодостаточен для TikTok, название песни совпадает с первой строкой — его ищут по строке.
