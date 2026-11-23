# Лейтмотивы сезона 1: дома, герои, загадка, катастрофа, битва, горе

Версия 0.1 · 2026-11-22 · композитор · статус: **черновик** (тоны домов утверждаются вместе со звукорежиссёром на тесте — `canon/world.md` §7.10 draft)
Источники: `story/houses/art_and_music_sheet.md` §2–§5, `canon/world.md` §7.10, §8.7, `story/series_bible.md` §5, §10, §12.3, `story/episodes/S01E01/beat_sheet.md`, `production_notes.md` §6, указание директора 2026-11-22 (телефон).
Колыбельная здесь не описывается: она не лейтмотив героя или дома, а мотив загадки по особым правилам (`lullaby.md`, закрыто). Главная тема — `main_theme.md`.

---

## 0. Общие правила для всех тем (проверяются перед каждой генерацией)

1. **Резервный тон R.** Одна высота зарезервирована за загадкой (её значение — в закрытом `lullaby.md`). Ни одна тема не берёт R тоникой, педалью или долгой нотой. На практике **все лады ниже выбраны без R**: если вариант темы требует другого лада, сначала спросить композитора.
2. **Никаких пятёрок.** Ни одна тема не пишется в 5/4 и не делится на группы из пяти нот или долей (квинтоли, 5/8, пятиударные фигуры). Пятидольность в сериале означает только одно, поэтому её не тратим.
3. **Не цитировать и не делить материал** с мотивом загадки (§0 выше). Сходство одного интервала — не материал, но контур, ритм и ступени разные.
4. **Нижний регистр пуст** (`production_notes.md` §6, `art_and_music_sheet.md` §5):
   - ни одна тема дома не берёт низкий регистр тоникой: тоники и мелодии — в среднем и высоком регистре;
   - **в пилоте: никакого тонального звука ниже F♯2 (92,5 Гц) в музыке**, кроме одного тона в Sc 3 и Sc 20 (`pilot_cue_sheet.md`). Гул Шпилей (SFX) — не ниже C2 (65,4 Гц). Стемы музыки пилота получают ФВЧ 85–90 Гц;
   - в остальных сериях бас допустим только как опора (ритм, короткие ноты), без выдержанных педалей и дронов в самом низу.
5. **Телефон** (указание директора): узнаваемая часть каждой темы — мелодия или ритм — живёт в полосе **300 Гц–3 кГц** (примерно E♭4–F♯7). Тема должна узнаваться через фильтр ФВЧ 300 Гц + ФНЧ 8 кГц. Бас только поддерживает.
6. **Хор и Канторы всегда неполны:** без басового инструмента, самый низкий голос не ниже G3, аккорды — квинты, кварты, задержания, без «пола». Это закон звучания всего, что поёт Хор или Кантор, включая Иону и Ильване.
7. **Низы без голоса:** свист, хлопки, топот, барабаны (вёдра, бочки, лодки, ступени колёс), дыхание, ритм на одной высоте. Голос появляется только когда прорывается в кадре: Лио — S1E2, Гул — S5.
8. **Перстень Руэла не звучит.** У перстня нет мотива; под вставками с перстнем — ни стинга, ни R, ни низкого тона; никакой музыкальной склейки между перстнем и камнем Пелл.
9. **Оригинальность** (`sound_bible.md` §2): в промптах нет имён людей, групп, тайтлов, «in the style of». Каждый утверждённый трек прослушивается на сходство.
10. **Одна генерация — навсегда.** Каждая тема генерируется один раз (`composition_plan` + `seed`), утверждается и переиспользуется. Вариации (тихая, напряжённая, торжественная) делаются с `conditioning_ref` на утверждённую тему (`music_v2_5`), а не новыми генерациями с нуля.

---

## 1. Великие дома сезона 1

Тон Шпиля = тоника темы (`art_and_music_sheet.md` §5). Лад выбран без R. «Ядро промпта» — неизменная английская строка; в вариациях меняется только хвост.

| Дом · Шпиль · тон | Лад, темп, размер | Мотив (ноты и ритм) | Тембр | Драматургия в S1 |
|---|---|---|---|---|
| **Corvane** · Sentinel · **D** | D миксолидийский, 76, 4/4 | **«Нырок»**: D5 (♩.) → A4 (♪) — кварта вниз (нырок), затем A4 (♩) → **F♯5** (𝅗𝅥) — секста вверх (вынырнул). «We go under and come up» без слов | латунь: валторна, тёплые низкие струнные (от F♯2), перекатывающийся «морской» барабан | Руэл (тепло, щедрость). По листу: мотив **теряет сексту**, когда Марен носит перстень (S6E12) |
| **Dask** · Sheaf · **F** | F лидийский, 66, 3/4 | Медленная опора щипковых: F4–C5–B4–C5 (лидийская B — «солнце над полем»), молотильная трещотка на 3-ю долю | щипковые струнные, трещотка-цеп, деревянные духовые | лорды-зерновики; осторожно — Хельм Лукан из Даск, но в пилоте тема не звучит |
| **Ilvane** · Pale · **E** | E фригийский, свободный | **Один долгий унисон женских голосов** на E5, без гармонии; переход на F5 (фригийская секунда) и обратно; разрешается **только в тишину** | женские голоса в унисон (без слов, «ah»), стеклянная гармоника | Иона, Весна, Аурин. Голоса разрешены: это знать, а не Низы. Всегда без баса (правило 6) |
| **Rusk** · Falls · **A** | A эолийский, 96, 4/4 | Маршевые барабаны, один сигнал трубы A4–E5–A5, двухаккордовые «ворота» **Am – F** (закрывающиеся створки); горная скрипка-бурдон на A3–E4 | малые и тенор-барабаны, труба, скрипка с бурдоном | гарнизоны, Кес. Тема Ванта — тот же тон, тихо и с обрывом (истории) |
| **Quell** · Storm · **B** | B дорийский, 6/8 | Шанти-фигура **только свистом, никогда не поётся**: B4–D5–F♯5–E5 / D5–C♯5–B4; поющая пила, стук по корпусу лодки | свист, поющая пила, удары по дереву | контрабандисты, мели. Свист Низов и Квелла различаются: у Квелла мелодия, у Низов — сигналы |
| **Fennick** · Sluice · **C♯, плывёт вниз** | C♯ минор, 60, 4/4 | Глухое пиццикато «тиканье» восьмыми; настроенные камни эстафеты; одна **«слушающая» нота C♯5, медленно сползающая на −30 центов**. В Хайуотере больной Шпиль бьётся о C Короны | пиццикато с сурдиной, камни эстафеты (SFX-тон), высокий флажолет | Одо, Слушатели, Слушания |
| **Lantry** (без Шпиля, на тон-кодах эстафеты) | C ионийский, 104, 2/4 | Сухой «часовой механизм»: клавесин и цимбалы шестнадцатыми, **звон монеты на слабую долю**; мелодии почти нет | клавесин, цимбалы, медная монета | Урсель, Счётный дом; по листу **останавливается в ночь пожара (S6)** |
| **the Choir** · Choir · **G** | G, свободный | **Ретюнинг-хорал**: унисон на G, который передаётся от голоса к голосу так, что линия не рвётся; вокруг — пустые квинты и кварты (G–D–A, D–A–E). С каждым сезоном тоньше | хор без слов, только верхние голоса (сопрано, альты, высокие тенора), никакого баса | всё, что поёт Хор. Звучит «неполным» — так задумано (правило 6) |
| **Crown / Хельм** · Crown · **C** | C, 72, 4/4 | **Фанфара Хельма** — старый гимн-аккорд Харроу: плагальный оборот **F – C** в меди, архаичный и неизменный с CY 1 | медь: трубы, валторны, тромбоны (от C3) | Хельм. Ирония: оборот начинается с F — тона Даска. В пилоте **не звучит** (Лукан читает карту без фанфар) |
| **the Ossari** (без Шпиля до CY 313) | открытые квинты на A–E, 6/8 | Эоловый бурдон струн воздушных змеев, рамочные барабаны 6/8, призыв рога **открытой квинтой** | эоловая арфа, рамочные барабаны, рог | горцы; в битвах — 6/8 против 4/4 Даска и Раска |

**Не в S1:** тема **Ashare** (на тоне Затонувшего Шпиля; по листу до S5E10 — только обрывки напева с закрытым ртом). Риск: напев с закрытым ртом на том же тоне легко спутать с мотивом загадки. Тему Ashare надо сочинять отдельно и показать хранителю канона до первого использования (вопрос в отчёте).

### Ядра промптов (английский)

```text
CORVANE : Instrumental naval house theme in D mixolydian, 76 BPM, 4/4. Warm French horn plays a short motif that dives down a fourth and surfaces with a rising major sixth, over rolling sea-drum and warm strings in the middle register. Proud, generous, seafaring. No vocals, no sub bass.
DASK    : Instrumental pastoral house theme in F lydian, 66 BPM, 3/4. Slow plucked strings walking a steady ground line, a threshing-flail wooden clapper on beat three, soft woodwinds. Earthy, patient, heavy with harvest. No vocals, no low drone.
ILVANE  : One long held unison of women's voices on a single high note, wordless "ah", no harmony, glass harmonica shimmer around it, free tempo, E phrygian colour, ends by fading into silence. Cold, pure, noble. No bass, no instruments below the voices.
RUSK    : Instrumental martial house theme in A aeolian, 96 BPM, 4/4. Marching snare and tenor drums, one solo trumpet call rising A-E-A, two-chord gate figure A minor to F major, upland fiddle with a drone in the middle register. Hard, disciplined, mountain fortress. No vocals, no sub bass.
QUELL   : Instrumental smuggler shanty in B dorian, 6/8. A sea-shanty melody whistled by a human whistler, never sung, with singing saw and knocks on a wooden boat hull. Salty, sly, rolling. No vocals, no lyrics, no bass.
FENNICK : Instrumental surveillance theme in C-sharp minor, 60 BPM. Muted string pizzicato ticking in eighth notes, small tuned stone chimes, one long high listening note that slowly drifts flat. Quiet, watchful, cold. No vocals, no low end.
LANTRY  : Instrumental clockwork banking theme in C major, 104 BPM, 2/4. Dry harpsichord and hammered dulcimer in fast even sixteenths, a single copper coin drop on the off-beat, almost no melody. Precise, polite, merciless. No vocals, no bass.
CHOIR   : Wordless upper-voice choir (sopranos, altos, high tenors) passing one sustained G from voice to voice so the line never breaks, open fifths and fourths around it, no bass voices, no instruments, sounds beautiful but hollow, as if a floor is missing. Free tempo, temple acoustics.
HELM    : Short archaic brass hymn fanfare in C major: a plagal F major to C major cadence for trumpets, horns and trombones, slow and ceremonial, unchanged for centuries. No vocals, no percussion.
OSSARI  : Instrumental upland theme, 6/8, aeolian harp drone of kite strings, frame drums, a horn call on an open fifth A-E. Dry wind, high plateau, fierce. No vocals, no sub bass.
```

---

## 2. Народ: Низы и Середина

| Слой | Мотив | Тембр | Правило |
|---|---|---|---|
| **Низы** (Lows) | **«Доски»**: топот–хлопок–топот-топот (♩ ♩ ♪♪ ♩) в 4/4, свистовые сигналы из словаря (`world.md` §8.7: падающие два тона = Слушатели, восходящие три = всё чисто, трель = прилив, долгий = помощь), счёт шагов колеса на одной высоте, тростниковый свисток Корра | тела, вёдра, лодки, ступени колёс, свист | **без голоса**; весело, упрямо, никогда не жалобно. Сигналы свиста — диегетика (SFX), не мелодия темы |
| **Середина** (Mids) | **«Смена»**: работа как музыка — шестерни насосов, скрип пера, колокол клерков, барабаны казарм; ровный метр 2/4 | метал, дерево, колокол | песен нет: Середине петь не хочется («это для Низов») |

```text
LOWS    : Instrumental street-percussion cue, 100 BPM, 4/4: foot stamps on wooden planks, hand claps, buckets and an upturned boat as drums, short two-finger whistle calls between phrases, a reed whistle keeping pace. Alive, cheeky, stubborn, never mournful. No vocals, no singing, no humming, no melody instruments, no bass.
MIDS    : Instrumental work-rhythm cue, 2/4, 92 BPM: pump gears and ratchets, quill scratching, a small clerk's bell on the downbeat, distant barracks drum. Busy, orderly, grey. No vocals, no bass.
```

---

## 3. Ключевые герои пилота

Темы героев не обязаны стоять на тоне дома, но берут его тембр, если герой — часть дома. В пилоте **темы героев почти не звучат** (`production_notes.md` §6: дома — со E2; в пилоте только краска Корвейна под входом Руэла). Ниже — материал на сезон; что звучит в пилоте, указано в последней колонке.

| Герой | Мотив (ноты, ритм) | Тембр | Чем держится образ | В пилоте |
|---|---|---|---|---|
| **Пелл** (CH-0001) | **«Подскок»**, A дорийский, 6/8, свист двумя пальцами: A4–C5–E5 (♪♪♩ — подскок вверх) → D5 (♩.) — приземление на IV ступень, дерзко, не на тонику. Вариант страха: та же фигура, оборванная на C5 | свист, бочка, хлопок; позже — одна скрипка без вибрато | смекалка и упрямство Низов. **Без голоса**; не связан с напевом (другой лад, 6/8, фигура-арпеджио) | Sc 2→3: короткий подскок в уличном треке M03 |
| **Вик** (CH-0007) | щелчки языком, свистовой «съезд» вниз (глиссандо), шлепок по доске — 2/4, быстро | губной свист, деревянные шлепки | рот, который не закрывается | диегетика (SFX); его спетая нота в Sc 4 — реплика, не музыка |
| **Нан** (CH-0015) | **«Соль и нитка»**: E минор, 3/4, вздох из двух нот G4→F♯4 на щипковой струне, тиканье сетевой иглы | щипковая струна с низким натяжением (в среднем регистре), игла | жёсткая нежность. **Её мотив — не напев**, и напев ей не тема (`lullaby.md` §8, закрыто) | нет |
| **Иона** (CH-0002) | **«Вопрос»**: E4 → B4 (квинта вверх) → C5 (полутон вверх, к тону Короны) — тянется и не разрешается | стеклянная гармоника, флажолет скрипки; когда она поёт в кадре — только её голос | её вопрос «Is that what the song is for?». Как всё у Канторов, **без баса** (правило 6) | Sc 8 — внутри хорового трека M05 (два проведения, тихо) |
| **Холлис** (CH-0003) | **«Колонка»**, A минор, 3/4, ровные восьмые: A4–C5–B4–E5 (1–3–2–5) по кругу. **«Перестановка»** — та же фигура с переставленными нотами 2 и 3 (A4–B4–C5–E5) = подлог, кража, неверная цифра. Фанаты будут её ловить | пиццикато, цимбалы (родство с Лантри), позже челеста | ум, который видит ошибку; трусость — фигура обрывается на 3-й ноте | нет (Счётный дом в пилоте без музыки) |
| **Руэл** (CH-0005) | «нырок» Корвейна в тёплой валторне, медленно, с лишней задержкой на верхней сексте — «человек, за которым идёшь в лодку» | валторна, струнные | любовь зрителя до E11. **Никакого мотива на перстень, никакого R** (правило 8) | Sc 10: краска под входом (M06), до рукопожатия |
| **Урсель** (CH-0011) | **«Уровень»**: одна и та же верхняя нота (E5) ровными четвертями на клавесине, гармония под ней меняется (средний регистр), а верх не двигается: «All water finds its level». Звон монеты | клавесин, медь | доброта, которой надо бояться | нет |
| **Одо** (CH-0010) | «слушающая» нота Фенника + тиканье; подпись — **мотив обрывается посреди звона**, как камень под его пальцем | пиццикато с сурдиной, камни эстафеты | «Nothing unheard» | Sc 17: пульс M08 пропускает один удар, когда он гасит камень |
| **Кес** (CH-0004) | «ворота» Раска (Am – F) у одной трубы с сурдиной; подпись — дробь малого барабана, оборванная ударом железа | труба с сурдиной, малый барабан | молчание о Девятом | **нет** (руки на засове — без музыки, никакой склейки Sc 1 ↔ Sc 18) |
| **Хельм Лукан** (CH-0016) | фанфара Хельма (F – C) | медь | должность, а не человек | нет (умирает без музыки) |

```text
PELL    : Instrumental street cue in A dorian, 6/8, 112 BPM. A two-finger whistle plays a quick skip up A-C-E and lands on D, cheeky and unresolved, over a barrel drum and hand claps. Quick, tough, resourceful. No vocals, no humming, no bass.
IONE    : Instrumental motif, free tempo: glass harmonica and violin harmonics reach up a fifth and then one semitone higher, stopping unresolved, open fifths around it, no bass at all. Pure, questioning, fragile.
HOLLIS  : Instrumental motif in A minor, 3/4, 96 BPM: plucked strings and hammered dulcimer repeat a four-note figure in even eighth notes like a column of figures, slightly nervous. Dry, clever, careful. No vocals, no bass.
URSEL   : Instrumental motif, 72 BPM: harpsichord repeats one unchanging high note in steady quarter notes while the harmony underneath slowly shifts, a copper coin drop on an off-beat. Calm, polite, frightening. No vocals, no low end.
RUEL    : Instrumental warm motif in D mixolydian, 70 BPM: a French horn dives down a fourth and rises a major sixth, holding the top note a little too long, soft strings. Charming, generous, trustworthy. No vocals, no sub bass.
NAN     : Instrumental motif in E minor, 3/4, 66 BPM: a low-tension plucked string sighs two notes down a semitone, a net needle ticking. Tough, tender, tired. No vocals, no humming, no bass.
```

---

## 4. Функциональная музыка сезона

| Мотив | Где | Идея | Тембр, метр | Правила |
|---|---|---|---|---|
| **Загадка — «Spiral»** | открытия, улики без мотива загадки, спирали (раковина, бороздки Шпиля, знак мелом) | клетка из четырёх нот кружит и **поднимается по часовой стрелке**: каждый круг на целый тон выше: четыре витка C–D–E–F♯, после F♯ — снова C (витков всегда четыре, не пять), 7/8 (2+2+3) — круг никогда не ложится ровно | челеста, препарированное фортепиано, смычковый вибрафон, стекло; без низа | **не колыбельная**: это музыка «думать», а не «улика» |
| **Головоломка эпизода — «Ledger»** | дедукция (подделанная бумага, украденный сундук, ложный тон) | лёгкое пиццикато 3/4, тиканье; фигура «Перестановка» Холлиса как намёк; при разгадке — **щелчок**: A минор → A мажор одним аккордом | пиццикато, цимбалы, деревянный щелчок | только внутри эпизода; закрывается в том же эпизоде |
| **Часы — «Thirty days»** | дедлайн сезона (Тихие дни), счёт времени | пульс из ритма **death-tone**: три удара и пауза длиной в удар (X X X —), 60 BPM | приглушённый рамочный барабан + высокое пиццикато (≥100 Гц) | в каждой серии; в пилоте — Sc 17–19 (M08) |
| **Хроника — «Archive»** | Летописец: гобелены, карты, документы | сухой дрон-квинта C4–G4 язычкового органа + одна смычковая линия в C ионийском, плагальные обороты: официальная история звучит в тональности Короны | язычковый орган, сухая скрипка или альт | под голос Летописца — разреженно, без мелодии в полосе речи во время слов |
| **Катастрофа / наводнение — «Breach»** | прорывы дамб, E10 | из сигнала «барабан на шлюзе = прорыв»: настойчивые четверти, разгоняются; тремоло высоких струнных кластерами, удары меди, огромные барабаны **без тонального баса — «пола нет»**, ужас от пустоты внизу | барабаны, струнные, медь | никакого R и низкой педали. В E10 — не раньше утверждения сценаристом сцены-улики (там свои правила) |
| **Битва — «Formations»** | битвы S1+ (совет над картой → строи → 2–3 личные линии → поворот → после) | **совет**: «Часы» + «Archive»; **строи**: темы домов контрапунктом (Раск 4/4 против Оссари 6/8); **личные линии**: темы героев; **поворот**: крючок главной темы (октавный скачок); **после**: «горе» | ударные, медь, струнные; полиритм 4/4 × 6/8 | ни одного 5/4; темы домов не берут низ тоникой |
| **Горе Низов — «To the ebb»** | похороны «отливу», соль в руках | **без голоса**: тростниковый свисток медленно ведёт одну линию, дыхание, мягкое сердцебиение ручного барабана | тростниковый свисток, дыхание, ручной барабан | никакого хора и напева |
| **Горе Ступеней — «The throat»** | цена песни, онемевшие Канторы, смерть знати | соло виолончели в **высоком** регистре + струнные без контрабасов; кончается на незавершённой квинте | виолончель, струнные | без низкой педали |

```text
SPIRAL  : Instrumental mystery cue in 7/8 (2+2+3), 84 BPM: celesta and prepared piano circle a four-note cell that climbs one whole step on every turn, bowed vibraphone and glass textures, no bass, never resolving. Curious, uncanny, hypnotic. No vocals.
LEDGER  : Instrumental puzzle cue in A minor, 3/4, 100 BPM: light string pizzicato and hammered dulcimer, soft clock ticks, a sly four-note figure; ends with a single bright A major chord click. Clever, light. No vocals, no bass.
CLOCK   : Instrumental pulse, 60 BPM: three muffled frame-drum strokes and a rest of one beat, repeated, with high soft pizzicato on the strokes, no melody, mid register only. Counting, inevitable. No vocals, no sub bass.
ARCHIVE : Instrumental archival underscore in C major, free slow tempo: a dry reed-organ drone on an open fifth C-G in the middle register and one unaccompanied bowed fiddle line with plagal turns, very dry room. Old, precise, official. No vocals, no low drone, no percussion.
BREACH  : Instrumental disaster cue, 100 to 140 BPM accelerating: an insistent drum hit on every beat like an alarm drum, high string tremolo clusters, brass stabs, huge unpitched drums, nothing sustained in the low register, terrifying emptiness underneath. No vocals, no sub bass.
FORMATIONS: Instrumental battle cue, 120 BPM: marching snares in 4/4 against frame drums in 6/8, brass house calls answering each other, low strings in short ostinato (not below F-sharp 2), building to a single huge turn. Massive, tactical. No vocals, no choir, no sub bass.
EBB     : Instrumental funeral cue, 54 BPM: a lone reed whistle plays a slow line, audible human breath, a soft hand-drum heartbeat, nothing else. Bare, poor, dignified. No vocals, no singing, no humming.
THROAT  : Instrumental grief cue in E minor, 58 BPM: solo cello in its high register over strings without double basses, ends on an open unresolved fifth. Noble, wounded. No vocals, no low drone.
```

---

## 5. Порядок создания библиотеки S1 (после пилота)

1. Пилот: только то, что в `pilot_cue_sheet.md`.
2. Перед E2 (дома объявляют кандидатов): Corvane, Dask, Ilvane, Rusk, Quell, Fennick, Lantry, Choir, Lows — по одной генерации 30–45 с (`composition_plan`, 2–3 чанка: заявка – развитие – каденция), до 3 дублей.
3. По мере сценариев: Spiral, Ledger, Breach, Formations, EBB, THROAT, темы героев. Вариации — только через `conditioning_ref` на утверждённое.
