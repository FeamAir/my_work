# Референсы «Бумажного кита»: персонажи, кит, локации, реквизит

Версия 1.0 · 2026-11-22 · автор: режиссёр-постановщик
Основа: `visual_bible.md` (стиль «Бумажный фонарь»), `consistency.md` (состав референс-листа, ID-блоки), `studio/story/bible.md` (внешность, локации, табу).
Статус: **промпты готовы, генерация не запускалась.**

Решения директора студии, учтённые здесь:
- кадр **16:9** (референс-листы тоже 16:9, чтобы не было пересчёта композиции);
- **кириллицу не генерируем**: штемпели, адреса, номер «14», табличка «ПОЧТА», надпись на баке башни — в генерации пустые или нечитаемые, текст накладывается на монтаже;
- **минимум синхронной речи**: в пилоте липсинк не нужен, поэтому лист ртов `06_mouth` отложен (см. §1.4).

---

## 0. Общие правила для всех референсов

1. К каждому промпту автоматически добавляются **базовый стилевой промпт** (visual_bible §10) и **негатив** (§12) или фраза `Avoid: …` для моделей без поля negative_prompt.
2. Для референсов персонажей фон нейтральный кремовый `plain warm cream paper background`, свет ровный тёплый `soft even neutral warm studio light, no strong cast shadows`, иначе закатный свет «запечётся» во внешность.
3. Ко всем кадрам с бумагой, конвертами, штемпелями, табличками добавляется **текстовый негатив**:
   ```
   readable text, letters, words, numbers, Cyrillic, Latin alphabet, typography, fake writing that looks like real words
   ```
   и позитивная формула: `blank`, `illegible abstract scribble lines`, `empty stamp frame`.
4. Реальные марки, бренды и логотипы запрещены (библия §7): марки на ките — только выдуманные мотивы (волна, птица, круг, лист), без текста и номиналов.
5. ID-блоки ниже — **канон**. Копировать дословно, в том же порядке. Изменение → новая версия блока с датой.
6. Модели: персонажи и кит — **Nano Banana 2** (t2i для `00_master`, edit для остальных листов); локации и реквизит без персонажей — **Nano Banana** (при плохом удержании стиля — Nano Banana 2).
7. Файлы — в `studio/direction/refs/<id>/` по схеме consistency.md §1; рядом `card.md` с промптом, моделью, seed, датой.

---

## 1. Персонажи

### 1.1. ID-блоки (канон v1)

```
{SORA}
[ID: SORA] 15-year-old girl, petite slim build, short;
hair: dark brown straight shoulder-length hair with short uneven bangs, one thin braid tied with red thread at her left temple;
eyes: large amber-brown eyes with golden flecks;
face: soft round face, light freckles across the nose;
outfit: oversized mustard-yellow knit cardigan over a white t-shirt, navy knee-length skirt, black tights, brown lace-up boots;
signature item: long postal-red scarf, small beige canvas shoulder bag with a blue wave patch, strap over her right shoulder, bag at her left hip
```

```
{NATSU}
[ID: NATSU] 17-year-old girl, tall athletic build, a head taller than Sora;
hair: short black hair with an undercut at the back, one long front strand tucked behind her right ear;
eyes: narrow grey-green eyes;
face: lightly tanned skin, beige adhesive bandage across the bridge of her nose, small silver hoop earring in her right ear;
outfit: olive-green windbreaker with rolled-up sleeves over a grey hoodie, dark rolled-up jeans, white sneakers;
signature item: orange cycling goggles pushed up on her forehead
```

```
{GEN}
[ID: GEN] 72-year-old man, short, slightly stooped but sturdy;
hair: short thick white hair, bushy white eyebrows;
eyes: squinting dark eyes with deep wrinkles around them;
face: neat white mustache, no beard, round thin brass-rimmed glasses low on the nose;
outfit: faded navy-blue postman jacket with brass buttons and no patches, beige turtleneck sweater, grey trousers, wooden geta sandals;
signature item: old wristwatch with a brown leather strap on his right wrist
```

Реквизит, привязанный к персонажу (вставляется только когда предмет в кадре):
```
{BIKE}  old light-blue bicycle with a large wire front basket holding a stack of newspapers tied with twine
{CRANE} small origami paper crane folded from plain yellow paper, no markings
```

### 1.2. Якоря, стороны, рост, палитра

| | Сора | Нацу | Гэн |
|---|---|---|---|
| Якоря (проверять в каждом кадре) | красный шарф, горчичный кардиган, косичка с красной ниткой **у левого виска** | пластырь на переносице, оливковая ветровка, оранжевые очки на лбу, прядь и серёжка **справа** | белые брови и усы, круглые латунные очки, синий пиджак с латунными пуговицами, часы **на правом запястье** |
| Рабочий ракурс (чтобы якорь был виден) | лицом **влево по кадру** (видна левая сторона лица) | лицом **вправо по кадру** (видна правая сторона) | лицом вправо по кадру (видны часы на правой руке) |
| Рост (Сора = 1,0) | 1,0 · ~5,5 головы | ~1,15 · ~6 голов | ~1,08 (сутулость) · ~6,5 головы |
| Кожа / тень | `#F3D9C4` / `#C9A6A8` | `#E2BC98` / `#B8918E` | `#EBCDB5` / `#BFA0A0` |
| Волосы / тень | `#4A2E22` / `#2F1D18` | `#22222A` / `#14141C` | `#ECE8E0` / `#B9B3C4` |
| Глаза | `#B8792E` (амбра) | `#7E9488` (серо-зелёный) | `#3E2F2A` |
| Одежда 1 / 2 / 3 | кардиган `#D4A33C`, шарф `#C8402E`, юбка `#2E3A5C` | ветровка `#6E7444`, худи `#8D8C8A`, очки `#E07A2E` | пиджак `#34466B`, свитер `#D9C7A6`, пуговицы/очки `#B98F45` |

Цвета — ориентир для `07_palette.png` и пипетки при приёмке; в промпты HEX не вставляем (consistency §2). Шарф Соры и киноварь сцены совпадают по тону намеренно: в сценах, где акцент — киноварь, шарф и есть акцент.

Разведение силуэтов в заливке одним цветом: Сора — шарф с летящими концами + косичка; Нацу — андеркат с длинной прядью + очки на лбу + велосипед; Гэн — сутулость + круглые очки + пиджак почтальона.

### 1.3. Промпты референс-листа (на каждого персонажа)

Порядок генерации: `00_master` (t2i, 12–16 вариантов, режиссёр выбирает один) → остальные листы edit-ом от утверждённого `00_master`.

**00_master — паспортный портрет** (Nano Banana 2, text-to-image)
```
character reference portrait, waist-up, three-quarter view facing left, neutral calm expression,
looking slightly off-camera, {ID}, plain warm cream paper background,
soft even neutral warm studio light, no strong cast shadows, centered composition, 16:9
```
Для Нацу и Гэна — `facing right` (рабочий ракурс, см. таблицу).

**01_turnaround** (Nano Banana 2 edit, ref: 00_master)
```
character turnaround sheet of the same character from image 1, full body, four poses in one row
evenly spaced: front view, three-quarter view, side profile, back view, relaxed standing pose,
arms slightly away from the body, identical outfit, hair and colors in every pose, same scale,
plain warm cream paper background, soft even neutral light, no text, no labels, 16:9
```

**02_front / 03_three_quarter / 04_profile** (edit, ref: 00_master)
```
head and shoulders close-up of the same character from image 1, [front view | three-quarter view facing left | side profile facing left],
neutral expression, mouth closed, same hair, eyes, face details and outfit collar,
plain warm cream paper background, soft even neutral light, 16:9
```
(Нацу и Гэн — `facing right`.)

**05_emotions** (edit, ref: 02_front)
```
expression sheet of the same character from image 1, six head close-ups in a 3x2 grid, front view,
neutral, gentle smile, sadness, surprise, worry, quiet wonder, mouth closed in all except surprise,
identical hair, face details and colors in every cell, plain warm cream background, no text, no labels
```
Набор эмоций под сериал (вместо гнева/страха из шаблона): у нас тихая драма, нужны «тихое изумление» и «тревога».

**06_mouth** — **отложено**: в пилоте нет кадров с липсинком (см. шот-лист). Делается, если в следующих сериях появится синхрон.

**07_palette** — вручную по `00_master`, HEX из таблицы §1.2 сверяются пипеткой и правятся под фактический результат.

**08_props** (edit, ref: 00_master)
- Сора: `prop sheet: the long postal-red scarf laid flat, the small beige canvas shoulder bag with a blue wave patch, a small yellow origami paper crane, plain cream background, no text`
- Нацу: `prop sheet: orange cycling goggles, {BIKE} in side view, plain cream background, no text, no logos`
- Гэн: `prop sheet: round thin brass-rimmed glasses, old wristwatch with a brown leather strap, a faded blue canvas postman bag with a brass buckle, plain cream background, no text, no logos`

### 1.4. Особые указания по персонажам

- **Сора:** косичка строго у **левого** виска; самая частая ошибка модели — зеркалить. Шарф всегда в кадре, концы летят по ветру **вправо по кадру** (ветер в пилоте дует слева). Сумка — на левом бедре.
- **Нацу:** пластырь бежевый, **поперёк** переносицы (не на щеке). Очки на лбу, **не на глазах**. Серёжка и заправленная прядь — справа. Капюшон худи лежит поверх воротника ветровки.
- **Гэн:** очки низко на носу, глаза смотрят поверх очков. Без бороды (модель любит дорисовывать). Сутулость заметна в профиль. Пиджак **без нашивок и надписей**.

---

## 2. Бумажный кит — два уровня детализации

Кит — немой персонаж, и к нему те же правила, что к людям: канон, ID-блок, приёмка. Сложность (марки, почерк, швы) решается разделением на две модели внешности, которые описывают **одно и то же тело**:

- **WHALE_FAR** — общие и дальние планы: кит занимает меньше трети кадра или виден целиком. Крупные грани, почерк и марки — текстура, а не детали.
- **WHALE_DETAIL** — фрагменты крупно: глаз, плавник, участок бока, прореха, шов. Кит **никогда не показывается целиком в детальной версии**: крупный план — всегда фрагмент.

### 2.1. Фиксированная анатомия (общая для обеих версий)

| Параметр | Канон |
|---|---|
| Направление движения | в пилоте кит плывёт **справа налево по кадру**, к камере повёрнут **левым боком** |
| Тело | ~12 крупных граней по борту (как сложенный лист оригами), острый «нос», клиновидный хвост с плавником-веером |
| Цвет | слоновая кость, крем, светло-коричневый; на закате бумага **просвечивает** тёплым светом |
| Глаза | два круглых красных почтовых штемпеля (кольца + волнистые линии гашения, **без текста**), мягко светятся изнутри |
| Плавники и хвост | «чешуя» из выдуманных марок: приглушённые синий, зелёный, охра, розовый; мотивы — волна, птица, круг, лист |
| Прорехи на левом боку | **A** — большая, сразу за левым грудным плавником (зашивается в ep01 sc06); **B** — средняя, под спинным изломом; **C** — малая, у хвоста |
| Шов | янтарные светящиеся стежки, как золотая нитка, крестиком вдоль края бывшей прорехи |
| Падающие листы | отрываются от брюха, по одному, падают кружась |

Состояния кита по серии (для приёмки): **ep01-A** — прорехи A, B, C открыты (сц. 3–6 до доставки); **ep01-B** — A зашита янтарным швом, B и C открыты (с sc06-sh070 до конца серии).

### 2.2. ID-блоки

```
{WHALE_FAR}
[ID: WHALE_FAR] colossal origami whale seen from far away, simplified silhouette built from about twelve large flat faceted paper planes in ivory, cream and pale brown, swimming from right to left with its left side toward the viewer, faint thin sepia line texture suggesting old handwriting, pectoral fins and fan-shaped tail covered in a mosaic of small muted colored squares like postage stamps, two small glowing round red eyes, three dark torn holes along its left flank, warm light glowing through the thin paper
```

```
{WHALE_DETAIL}
[ID: WHALE_DETAIL] giant origami whale made of hundreds of overlapping yellowed letter sheets in ivory, cream and pale brown, crisp faceted origami folds, faded sepia and blue handwriting rendered as illegible abstract scribble lines, fins and tail covered in invented postage stamps like scales with simple wave, bird, circle and leaf motifs and no text, eye is a round red postmark seal with concentric rings and wavy cancellation lines and no text, glowing softly from within, dark ragged torn holes showing empty darkness
```

Модификаторы состояния (добавляются в конец):
- `the large torn hole right behind the left pectoral fin is open` (ep01-A)
- `the large hole right behind the left pectoral fin is mended with glowing amber cross-stitches like gold thread` (ep01-B)

### 2.3. Референс-лист кита (Nano Banana 2)

| Файл | Промпт | Режим |
|---|---|---|
| `whale/00_master_far.png` | `character reference: {WHALE_FAR}, full side view of the whole whale from its left side, swimming right to left, neutral warm daylight, plain warm cream paper background, the whole body fits in frame with margins, 16:9` — 12–16 вариантов | t2i |
| `whale/01_turnaround_far.png` | `turnaround sheet of the same whale from image 1, four views in one row: left side, front, belly from below, top, identical shape, fold layout, colors, stamp fins, red eyes and three holes, plain cream background, no text, no labels` | edit от 00 |
| `whale/02_far_sunset_silhouette.png` | `the same whale from image 1 floating high in a peach-orange sunset sky, backlit, warm light glowing through the thin paper, seen from below at a distance, no ground, 16:9` | edit от 00 |
| `whale/10_master_detail_flank.png` | `close-up fragment of {WHALE_DETAIL}, left flank section right behind the left pectoral fin, overlapping letter sheets with illegible handwriting lines, the large dark torn hole in the center, edge of the stamp-covered fin on the left, neutral warm light, cream background, 16:9` | edit от 00 (структура) |
| `whale/11_eye.png` | `extreme close-up of the eye of the same paper whale: a round red postmark seal with concentric rings and wavy cancellation lines and no text, glowing softly from within, set into faceted yellowed paper folds, 16:9` | edit от 10 |
| `whale/12_fin_stamps.png` | `close-up of the pectoral fin of the same paper whale, covered in overlapping invented postage stamps like fish scales, muted blue, green, ochre and pink, simple wave, bird, circle and leaf motifs, perforated edges, no text, no numbers, 16:9` | edit от 10 |
| `whale/13_seam.png` | `the same flank fragment from image 1, the large hole now pulled closed and mended with glowing amber cross-stitches like gold thread, everything else identical` | edit от 10 |
| `whale/14_belly_sheet.png` | `view from below of the belly of the same paper whale, one single ivory letter sheet peeling off and starting to fall, 16:9` | edit от 10 |

Указания:
- Для дальнего плана кит сначала генерируется на нейтральном фоне, затем **edit-ом вписывается** в мастер-небо или мастер-локацию (ref: `whale/00_master_far` + мастер-локация). Так кит одинаков во всех общих планах.
- Почерк — только абстрактные линии. Если модель выдаёт читаемые латинские или кириллические «слова», кадр **бракуется** (визуальная ложь + брак по тексту).
- Проверка при приёмке: направление (справа налево), левый бок к камере, положение прорехи A у грудного плавника, красные глаза без текста, марки без надписей.
- Видео с китом: «кит плывёт очень медленно, как в воде», движение только по горизонтали или от камеры; никаких изгибов тела (бумага ломается и «плывёт» в генерации).

---

## 3. Мастер-кадры локаций

Генерируются **без персонажей** (Nano Banana, t2i; при плохом стиле — Nano Banana 2). Каждая локация: общий план + 2–3 ракурса + световые режимы, нужные пилоту. Файлы: `studio/direction/refs/loc/<id>_<ракурс>_<свет>.png`.

Геометрия города (едина для всех локаций): склон спускается к бухте; если смотреть **с крыши почтового дома вниз по склону**, бухта на горизонте, белый маяк на мысе **справа**, вершина холма с водонапорной башней — **за спиной** (в обратном ракурсе — слева вверху). Ветер в пилоте дует слева по кадру.

Световые режимы (добавляются к промпту локации):
```
SUNSET : low golden-hour sun from the left, peach-orange sky fading to pale turquoise at the top, long warm shadows, lavender shade
DUSK   : deep blue twilight, last violet glow on the horizon, warm yellow street lamps glowing, cool blue shadows
NIGHT  : dark navy night sky with a bright moon, cool moonlight rim, a few warm windows and lamps as the only warm spots
INT_DUSK: interior at dusk, single warm yellow lamp under a green metal shade as key light, cool blue window light as fill
```

### L1 — Почтовый дом Мидзухара (интерьер) · `LOC_L1`

```
{LOC_L1} interior of a small old former post office used as a home, one large room, an old wooden
mail counter with a small blank brass plaque, behind it a wall of wooden sorting pigeonholes six rows by ten
columns with a few yellowed envelopes in some cells, dark wooden floorboards, a round wall clock with a
plain white face and no numbers above the counter, a low table on the left with a teapot and a stack of
colored origami paper, a faded blue canvas postman bag with a brass buckle hanging on the wall, a single
yellow lamp under a green metal shade, a window showing a slope of tiled roofs and a bay
```

| Файл | Ракурс | Свет | Для кадров |
|---|---|---|---|
| `L1_wide_door` | общий вдоль комнаты: стена ячеек и стойка в левой половине, входная дверь у правого края кадра, окно на заднем плане, лампа | INT_DUSK | sc05-sh010, sh020 |
| `L1_reverse_window` | обратный: от стены ячеек к окну, за стеклом закатный склон с крышами | INT_DUSK (за окном — SUNSET-остаток) | sc05-sh040 |
| `L1_counter_detail` | средний: край стойки, ячейки, абажур сверху | INT_DUSK | sc05-sh030, sh050, sh060 |

Примечание: латунная табличка «ПОЧТА» — пустая; надпись при необходимости накладывается на монтаже. Циферблат часов — без цифр (штрихи вместо цифр допустимы).

### L2 — Крыша почтового дома · `LOC_L2`

```
{LOC_L2} gently sloped roof of dark blue ceramic tiles on a hillside house, an old red-brick chimney near
the edge with a small red ribbon tied around it, a row of small paper origami cranes on top of the chimney
held down by pebbles, a small attic window behind, a view down the hill over many tiled rooftops in dark blue
and terracotta, laundry lines and wires between houses, a calm bay at the bottom with a small white
lighthouse on a cape on the right
```

| Файл | Ракурс | Свет | Для кадров |
|---|---|---|---|
| `L2_wide_downhill` | общий с крыши вниз по склону: город, бухта, маяк справа, труба в левой трети | SUNSET | sc01-sh010, sh020 |
| `L2_chimney_mid` | средний: труба с журавликами, черепица, за ней размытый город | SUNSET / NIGHT | sc01-sh040, sh060; sc07-sh020 |
| `L2_low_sky` | нижний ракурс от черепицы вверх: край трубы и большое пустое небо (место под кита) | SUNSET / NIGHT | sc03-sh050, sc04-sh010, sh050 |
| `L2_from_street` | снизу с улицы: карниз почтового дома, край крыши на фоне неба | SUNSET | sc02-sh030 |

### L3 — Улица Ступеней · `LOC_L3`

```
{LOC_L3} a wide stone staircase street climbing a steep hill, a smooth stone ramp for bicycles along the
right side of the steps, two-story old wooden houses with sliding doors on both sides, each house with a
red metal mailbox on a short post with a blank white number plate, wires and laundry lines stretched
across above the street, cast-iron street lamps with warm yellow light every twenty steps, at the bottom
the street ends at a waterfront and a calm bay
```

| Файл | Ракурс | Свет | Для кадров |
|---|---|---|---|
| `L3_up_from_below` | снизу вверх по лестнице: пандус справа (если смотреть вверх по улице; при взгляде вниз он слева), фонари, вверху — почтовый дом | SUNSET | sc02-sh010, sh040, sh050 |
| `L3_down_from_roof` | верхний ракурс с крыши почтового дома на улицу (в кадре край черепицы) | SUNSET | sc02-sh020 |
| `L3_down_to_bay` | вниз по лестнице к бухте, спиной к вершине | DUSK | sc06-sh010 |

**Под-локация `LOC_L3_H14` — дом № 14:**
```
{LOC_L3_H14} front of a two-story old wooden house on the stone staircase street, a green front door,
a clay pot of red geraniums next to a red metal mailbox on a short post with a blank white number plate
and a horizontal letter slot with a small metal flap, dark windows, a second-floor window above the door
```

| Файл | Ракурс | Свет | Для кадров |
|---|---|---|---|
| `H14_front` | средний-общий фронтально: дверь, ящик слева от двери, окно второго этажа | DUSK | sc06-sh020, sh030 |
| `H14_low_window` | нижний ракурс на фасад и окно второго этажа | DUSK | sc06-sh060 |
| `H14_mailbox_detail` | деталь: щель ящика с крышкой, пустая белая табличка | DUSK | sc06-sh040 |

Номер «14» на табличке — накладывается на монтаже (цифры модели иногда рисуют верно, но гарантии нет; в кадрах табличка пустая и **неподвижна**, чтобы трекинг был простым). Ящик — приглушённый почтовый красный, не насыщеннее шарфа Соры.

### L4 — Водонапорная башня · `LOC_L4`

```
{LOC_L4} a tall rusty metal water tower on four legs at the very top of a grassy hill, a round tank on top
with a narrow walkway and railing around it, a vertical ladder, dry grass bending in the wind, a faded
blank white painted band around the tank and a simple childlike painting of a whale on it
```

| Файл | Ракурс | Свет | Для кадров |
|---|---|---|---|
| `L4_far_from_roof` | дальний план с крыши: башня на вершине холма в правой трети кадра, силуэт | NIGHT | sc07-sh010 |
| `L4_mid` | средний общий у подножия (для серий 2+) | SUNSET | — (задел) |

Надпись «КАМИНОСАКА» на баке — белая пустая полоса; в пилоте башня только на дальнем плане, надпись не нужна.

### L5 — Небо над городом · `LOC_L5`

```
{LOC_L5} wide open sky above the rooftops of a small hillside seaside town, only the tops of tiled roofs,
chimneys and wires along the bottom edge of the frame, large empty sky
```

| Файл | Ракурс | Свет | Для кадров |
|---|---|---|---|
| `L5_low_sunset` | нижний ракурс, крыши по нижнему краю, огромное небо | SUNSET | sc03-sh010, sh040, sh060 |
| `L5_low_dusk` | то же | DUSK | sc06-sh070, sh080 |
| `L5_wide_night` | общий: силуэт города, луна, вершина холма с башней в правой трети (кит приходит справа, проплывает над холмом и останавливается хвостом у башни) | NIGHT | sc07-sh010 |

---

## 4. Реквизит пилота

| ID | Промпт | Где | Модель |
|---|---|---|---|
| `PROP_ENV_1986` | `an old ivory envelope with one folded corner, slightly yellowed and soft at the edges, a blank purple rectangular rubber-stamp frame in the upper right with nothing inside, a few faint illegible pencil-like scribble lines where the address would be, no readable text, plain cream background` | sc04, sc05, sc06 | Nano Banana 2 |
| `PROP_ENV_SORA` | `an old pale blue envelope, a blank purple rubber-stamp frame in the upper right, the center left completely empty for a single handwritten word, no text, plain cream background` | sc07 | Nano Banana 2 |
| `PROP_CRANES` | `a row of small origami paper cranes in red and yellow paper standing on top of an old red-brick chimney, each held down by a small grey pebble, no text` | sc01, sc07 | Nano Banana |
| `PROP_MAILBOX` | = `H14_mailbox_detail` | sc06 | Nano Banana |

Надписи для монтажа (выдаёт сценарист в «паспорте письма», накладывает монтаж):
- `PROP_ENV_1986`: штемпель «НЕ ДОСТАВЛЕНО. 1986» (фиолетовый, слегка смазанный), адрес «Улица Ступеней, дом 14» (аккуратный почерк, сепия);
- `PROP_ENV_SORA`: штемпель «НЕ ДОСТАВЛЕНО», слово «Соре» (мягкий округлый почерк);
- табличка ящика: «14» (белая на красном).

---

## 5. Порядок и объём генерации референсов

| Блок | Изображений (оценка) | Модель | Стоимость |
|---|---|---|---|
| Сора, Нацу, Гэн: 00 ×16 + 01–05, 08 × ~4 попытки (без 06) | 3 × ~40 = 120 | NB2 $0.08 | ≈ $9.6 |
| Кит: 00_far ×16 + 7 листов × 4 | ~44 | NB2 $0.08 | ≈ $3.5 |
| Локации: ~20 мастер-кадров (вкл. ночные варианты L2) × 3 попытки | ~60 | NB $0.04 (часть на NB2) | ≈ $2.4–4.8 |
| Реквизит: 4 × 3 | 12 | NB / NB2 | ≈ $0.7 |
| **Итого разово** | ~236 | | **≈ $16–19** |

Порядок: (1) Сора — она же стилевой тест вместо тестового MIRA (у них совпадает горчичный цвет одежды, держать обоих смысла нет); (2) мастер-локация L2 закат; (3) кит far → detail; (4) Нацу, Гэн; (5) остальные локации; (6) реквизит. Утверждение каждого блока — режиссёр по чек-листу consistency §6.
