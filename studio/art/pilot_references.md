# HOLLOWSTONE — референсы пилота S1E01 «The Ninth Sluice»

Версия 0.1 · 2026-11-22 · автор: художник-концептер · статус: **промпты готовы к стилевому тесту; генерация не запускалась**
Источник списка: `story/episodes/S01E01/production_notes.md` §5 (51 референс + 2 необязательных). Опора: `_anchors_matrix.md`, досье `story/characters/`, `art_and_music_sheet.md`, `canon/world.md`, `beat_sheet.md` v1.1, закрытая выдержка для режиссёра и художника (правила без причин).
Связанные файлы: `art/peoples_and_costume.md` (народы, классы, материалы), `art/heraldry.md` (гербы), `art/generation_plan.md` (порядок и смета), `art/sealed/` (закрытые материалы — только художник и режиссёр).

Уровень спойлеров: **безопасно для производственной команды.** Причин «фиксированных» правил здесь нет.

---

## 0. Как пользоваться

### 0.1 Сборка промпта
`[ID-блок(и)] + [вид / ракурс / задача листа] + {STYLE} + {SHEET или LOC} + [специфический Avoid] + {AVOID}`

- **ID-блок копируется дословно и в том же порядке** (`direction/consistency.md` §2). Режиссёр переносит утверждённые блоки в `direction/refs/<ID>/card.md`.
- `{STYLE}` — стилевой блок. Ниже — **временный** блок художника (предложение под сагу). Когда режиссёр утвердит визуальную библию v2, её базовый промпт заменяет `{STYLE}` **в одном месте**, все промпты этого файла остаются валидными.
- У Nano Banana нет поля negative — `Avoid:` идёт последней фразой промпта (`visual_bible.md` §12).

### 0.2 Общие блоки (временные)

`{STYLE}` *(предложение художника до визуальной библии v2)*:
```
hand-drawn 2D TV anime illustration for a mature epic fantasy drama, clean cel shading with one hard shadow step and soft lavender-grey shadows, crisp dark umber ink linework with slight brush taper, grounded realistic proportions, restrained muted palette of silt browns, sea greys and slate blues with one saturated accent, painterly gouache background texture, atmospheric haze, cinematic composition
```
`{SHEET}` (листы персонажей и предметов):
```
character model sheet, plain warm light-grey background, flat even neutral lighting, no cast shadows on the background, all figures at the same scale and evenly spaced, full body fully visible, no text, no labels, no frames
```
`{LOC}` (мастер-локации):
```
background art plate, empty of people unless stated, wide 16:9 frame, consistent architecture, clear readable depth layers for parallax (foreground, midground, background)
```
`{AVOID}`:
```
Avoid: photorealism, 3D render look, chibi or super-deformed proportions, text, letters, labels, captions, watermark, logo, signature, extra fingers, fused hands, extra limbs, accessories switching sides, mirrored image, magical glow, extra people.
```

### 0.3 Стороны (главная ловушка AI)
Каждая асимметричная деталь пишется **с двойной привязкой**: «на ЕЁ ЛЕВОЙ стороне (справа на картинке, когда она смотрит на зрителя)». На виде со спины — наоборот. При приёмке проверяется **каждая** сторона. Картинки с персонажами **нельзя** исправлять зеркальным отражением. Картинки без асимметричных якорей (раковина, знак, пейзаж без табличек) — можно, это бесплатно.

### 0.4 Модели
- **Черновик (D):** Nano Banana — $0.04. Здесь утверждаются композиция, поза, ракурс, раскладка листа.
- **Финал (F):** по умолчанию **Nano Banana Pro — $0.15** для главных листов, сага-предметов и мастер-локаций; **Nano Banana 2 — $0.08** для лёгких референсов, групп, дополнительных ракурсов и световых режимов (edit от финального мастера). Окончательный выбор — по стилевому тесту на Пелл (`generation_plan.md` §1): если Nano Banana 2 даёт то же качество, все финалы Pro переводятся на NB2.
- **Цепочка консистентности:** производные листы (разворот, эмоции, головы) делаются **от финального мастера**, а не от черновика: черновик раскладки (NB edit с финальным мастером как референсом) → финал (edit с финальным мастером + утверждённой раскладкой).
- **Бесплатно, локально:** силуэт (порог/заливка разворота), палитра (пипетка), сборные листы, лист масштаба — скриптом/в редакторе.
- **Лимит:** не больше 5 платных финальных дублей на референс (режим пилота). После 2 неудач — меняем подход (промпт, референс, раскладка), а не жмём ещё раз.

### 0.5 Имена файлов
`direction/refs/<ID>/<код>_<вид>_v<N>.png`, например `CH-0001/A01_00_master_v1.png`. Имена файлов описывают **что изображено**, а не что это значит. Рядом в `card.md` — промпт, модель, seed, дата.

### 0.6 Состав полного листа персонажа (A)
| Код | Вид | Как | Платно? |
|---|---|---|---|
| `00_master` | поясной портрет 3/4, нейтральное лицо, ровный свет | t2i | да |
| `01_turnaround` | полный рост в ряд: фронт · 3/4 · профиль · спина | edit от `00` | да |
| `02_heads` | три головы: фронт · 3/4 · профиль | edit от `00` | да |
| `03_silhouette` | силуэт разворота одной заливкой | локально из `01` | нет |
| `04_emotions` | сетка 2×3 характерных эмоций | edit от `02` | да |
| `05_mouth` | 6 форм рта (только у тех, у кого липсинк в пилоте) | edit от `02` | да |
| `06_details` | якорные детали крупно (коса, бирка, кольцо, руки) | edit от `00` | да |
| `07_palette` | плашки цветов с HEX | локально из `00` | нет |

### 0.7 Общие шаблоны листов (подставляется ID-блок)
- **Разворот:** `Use the character from image 1 exactly: same face, hair, outfit, colours and proportions. {ID-BLOCK}. Character turnaround: the same person shown four times in one row, standing relaxed with arms slightly away from the body: 1) front view, 2) three-quarter view turned to the viewer's left, 3) side profile showing {PROFILE SIDE}, 4) back view. {SIDE NOTE FOR BACK VIEW}. {STYLE}, {SHEET}. {AVOID}`
- **Головы:** `Use the character from image 1 exactly. {ID-BLOCK}. Three head-and-shoulders views in one row at equal scale: front, three-quarter, side profile showing {PROFILE SIDE}. Neutral expression, mouth closed. {STYLE}, {SHEET}. {AVOID}`
- **Эмоции:** `Use the character from image 1 exactly, same face and hair and outfit. {ID-BLOCK}. Expression sheet: a 2 by 3 grid of head-and-shoulders portraits of the same person, three-quarter view, each cell showing one expression: {E1}; {E2}; {E3}; {E4}; {E5}; {E6}. Keep every anchor detail on its correct side in every cell. {STYLE}, {SHEET}. {AVOID}`
- **Рты:** `Use the character from image 1 exactly. Mouth chart for lip-sync: six identical front-view head portraits, only the mouth changes: closed and relaxed; open "A"; rounded "O"; wide "EE"; pressed lips "M/B/P"; small smile. Everything else identical. {STYLE}, {SHEET}. {AVOID}`

---

# A. Полные листы персонажей — 8

## A-01 Пелл — CH-0001 · **стилевой тест студии**
- **Назначение:** героиня; сц. 2, 3, 4, 6, 9 (крыша), 19, 20. Без липсинка в пилоте (тихие крупные планы); первая лип-синк-реплика — E2 → лист ртов делаем к E2, не сейчас.
- **Народ / класс:** P1 дельта · Низы. Самая низкая из героев S1.
- **Состав:** 00, 01, 02, 03, 04, 06, 07 (без 05).
- **Эмоции (характерные):** (1) calculating squint — narrowed eyes, one corner of the mouth tight; (2) cocky lopsided grin, laughing through her nose; (3) silent fear of deep water — wide eyes, lips pressed shut, breath held, chin tucked; (4) stubborn defiance — jaw set, eyes level, unimpressed; (5) guarded tenderness — a small softening of the eyes, looking down and sideways (at Wick); (6) stunned wonder — eyes wide, lips slightly parted, very still.
- **ID-блок `[ID: PELL]`:**
```
[ID: PELL] 15-year-old girl, short and wiry, small for her age, leans forward slightly; olive-brown sun-darkened skin, freckles across the nose; hair: cropped ragged rust-brown (red-brown, not bright auburn), one long thin braid hanging on HER OWN LEFT side (right side of the image when she faces us), ending in a small blue tin tag stamped "IX"; eyes: sea-grey, narrow; outfit: patched tar-brown oilskin jacket, mud-grey wading leggings rolled to the knee, rag-wrapped bare feet, salvage net bag on her right hip; hands mud-dark to the wrist
```
- **Суффикс с осколком (с сц. 4):** `; a tiny cracked black stone on a knotted cord at her throat, mostly tucked under the oilskin` — **в листах не используем** (у предмета свой лист E-01; на мастере его нет, чтобы модель не «приклеила» камень к образу).
- **Промпт `00_master`:**
```
[ID: PELL] … (ID-block verbatim). Waist-up portrait, three-quarter view toward the viewer's left so her left side and the braid are clearly visible, neutral calm expression, mouth closed, looking at the viewer, modest age-appropriate clothing. {STYLE}, plain warm light-grey background, flat even neutral lighting. Avoid: braid on her right side, two braids, long loose hair, bright orange hair, clean hands, jewellery, earrings, photorealism, 3D render look, chibi proportions, text, watermark, extra fingers.
```
- **Промпт `01_turnaround`:** шаблон 0.7, `{PROFILE SIDE}` = `her LEFT side, so the braid hangs toward the viewer`; `{SIDE NOTE FOR BACK VIEW}` = `In the back view the braid hangs on the LEFT side of the image`.
- **Промпт `04_emotions`:** шаблон 0.7 с эмоциями (1)–(6) выше.
- **Промпт `06_details`:** `Use the character from image 1 exactly. Detail sheet, four close-ups in a row: 1) the end of her left braid with the small blue tin tag stamped "IX", slightly dented; 2) her mud-dark hands, nails broken short; 3) her shins with fine old shell-cut scars and rolled mud-grey leggings; 4) the salvage net bag on the right hip. {STYLE}, {SHEET}. {AVOID}`
- **Негатив (специально):** `braid on her right side, auburn or orange hair, pretty clean skin, earrings, shoes, adult body proportions, glamour`.
- **Модели (весь лист):** D — NB × 18 (из них мастер — 8: две версии `{STYLE}` по 4, см. план) · F — NB Pro × 5 + NB2 × 1 (мастер дважды: Pro и NB2 — сравнение для выбора финальной модели студии).
- **Приёмка особая:** коса — слева у неё на всех видах; бирка синяя; рост — «самая низкая»; руки грязные; нет серёг (серьга Нан появляется только с S2E8).

## A-02 Уик — CH-0007
- **Назначение:** сц. 2 (вниз головой на верёвочном мосту), 3, 4, 6, 9, 19, 20; **липсинк #5** «Pell… it's singing back».
- **Народ / класс:** P1 · Низы. **В пилоте без кепки** (кепку Марен он крадёт в E2): лист E1 — без кепки; вариант с кепкой — один edit к E2.
- **Состав:** 00, 01, 02, 03, 04, **05**, 06, 07.
- **Эмоции:** (1) bursting to tell — cheeks puffed, eyes sparkling, lips pressed against a grin; (2) cheeky gap-toothed grin; (3) wordless awe — mouth open, eyes huge, looking slightly up; (4) caught out — eyes wide above an imagined hand over his mouth (draw the hand only in a separate keyframe, here just the eyes and hunched shoulders); (5) indignant pout of a little brother; (6) frightened whisper — leaning in, eyebrows up, mouth small.
- **ID-блок `[ID: WICK]`:**
```
[ID: WICK] 11-year-old boy, skinny and small, all knees and elbows, quick; olive-brown skin, scabbed knees; hair: messy mouse-brown mop with one tuft sticking straight up at HIS OWN RIGHT temple (left side of the image when he faces us); eyes: big sea-grey; small gap between the front teeth; outfit: oversized oatmeal hand-knitted jumper with sleeves rolled up many times, rope belt, patched brown knee-length trousers, bare feet; no hat
```
- **Промпт `00_master`:** `[ID: WICK] … verbatim. Waist-up portrait, three-quarter view toward the viewer's right so his right temple tuft is clearly visible, neutral open expression, mouth closed, looking at the viewer, child proportions. {STYLE}, plain warm light-grey background, flat even neutral lighting. Avoid: cap or hat, tuft on the left side, neat hair, shoes, older-looking face, photorealism, 3D render look, text, watermark, extra fingers.`
- **Разворот:** `{PROFILE SIDE}` = `his RIGHT side, with the tuft toward the viewer`; спина — `in the back view the tuft is on the RIGHT side of the image`.
- **Рты:** шаблон 0.7 (липсинк E1).
- **`06_details`:** закатанные рукава свитера; верёвочный пояс; щербинка (крупно, улыбка); поза «вниз головой» силуэтом (для сц. 2 — референс позы, не кадр).
- **Модели (весь лист):** D — NB × 20 · F — NB Pro × 6.
- **Приёмка:** вихор справа у него; щербинка; рост ≈ плечо Пелл; без кепки.

## A-03 Нан — CH-0015
- **Назначение:** сц. 2 `[OS]`, 4 (**липсинк #1** «Never sing, chick…»), 19 (крошечная фигура вдали), 20 (ноги на лестнице).
- **Народ / класс:** P1 · Низы.
- **Состав:** 00, 01, 02, 03, 04, **05**, 06, 07.
- **Эмоции:** (1) scolding without looking up — eyes on her work, mouth moving, brows knit; (2) frozen terror — eyes wide and hard, whole face rigid; (3) grave command, speaking quietly and very firmly (the lip-sync line); (4) sly dry humour — one eyebrow up, mouth crooked; (5) grief bitten back — looking aside, lips pressed, jaw working; (6) weary tenderness — tired eyes softening.
- **ID-блок `[ID: NAN]`:**
```
[ID: NAN] tiny elderly woman of about 70, bent at the shoulders from decades over nets, quick busy hands; deep brown skin with deep wrinkles; hair hidden under a faded indigo headscarf knotted at the nape, a few white wisps at the temples; eyes: black, sharp, wet at the rims; a single small spiral-shell earring in HER OWN LEFT ear only (right side of the image when she faces us), the spiral turning clockwise; crooked little finger on her right hand; outfit: brown net-mender's apron over a faded blue-grey dress
```
- **Промпт `00_master`:** `[ID: NAN] … verbatim. Waist-up portrait, three-quarter view toward the viewer's left so her left ear and its single earring are visible, neutral expression, mouth closed, looking at the viewer, hands resting on a half-mended net at the bottom of the frame. {STYLE}, plain warm light-grey background, flat even neutral lighting. Avoid: earrings in both ears, earring on the right ear, visible hair, upright posture, jewellery other than the one earring, photorealism, 3D render look, text, watermark, extra fingers.`
- **Разворот:** `{PROFILE SIDE}` = `her LEFT side, showing the single earring`; спина — `headscarf knot at the nape centred`.
- **`06_details`:** серьга-спираль крупно (спираль по часовой); руки с мозолями от сетевой бечевы и кривым мизинцем правой руки; узел платка; игла для сетей.
- **Особое правило:** серьгу **не выделяем** светом и композицией — она «просто есть» (в кадре на неё не смотрят).
- **Модели (весь лист):** D — NB × 20 · F — NB Pro × 6.
- **Приёмка:** серьга одна, левое ухо; спираль по часовой; платок скрывает волосы; сутулость.

## A-04 Иона — CH-0002
- **Назначение:** сц. 8 (MS, вопрос), 9 (**спиной** в горле Шпиля), 10–12 (зал). Без липсинка; пение — всегда со спины.
- **Народ / класс:** P2 (Илвейн) · знать / Хор.
- **Состав:** 00, 01, 02, 03, 04, 06, 07 + **`08_back_hero`** — вид со спины в горле короны, развевающиеся одежды (это главный повторяемый образ сезона; делается как отдельный референс позы).
- **Эмоции:** (1) composed serenity, still face; (2) inward listening — eyes closed, chin slightly lifted (fork to the bone behind the ear); (3) quiet doubt — the question "Is that what the song is for?", brows faintly drawn, gaze level; (4) strain after singing — eyes lowered, swallowing, right hand rising toward the throat; (5) compassionate bow — eyes down, head inclined; (6) suppressed alarm — eyes fixed on something small, lips parted, very still.
- **ID-блок `[ID: IONE]`:**
```
[ID: IONE] 18-year-old young woman, tall and slender, very upright singer's posture, long neck; pale indoor skin with a faint warm olive undertone; hair: long straight pale-silver hair to the waist, silver from the roots, two thin side-plaits joined at the back of the head; eyes: dark brown; outfit: layered white robes with pale-violet trim, sleeves long enough to cover the hands, a narrow undyed-linen stole over the shoulders, soft white boots; violet silk band around the throat; a small silver tuning-fork pendant on a fine chain at the breastbone
```
- **Промпт `00_master`:** `[ID: IONE] … verbatim. Waist-up portrait, three-quarter view, neutral serene expression, mouth closed, looking at the viewer, hands hidden in her long sleeves. {STYLE}, plain warm light-grey background, flat even neutral lighting. Avoid: dark roots, blonde or white-yellow hair, blue or violet eyes, short hair, bare hands, jewellery other than the fork pendant, earrings, photorealism, 3D render look, text, watermark.`
- **`08_back_hero`:** `Use the character from image 1 exactly. Full-body back view: she stands in a tall arched stone opening, facing away from the viewer toward open sky, robes and silver hair snapping in a strong wind to the right, arms slightly away from the body, head level. {STYLE}, {SHEET}. {AVOID}`
- **`06_details`:** камертон (крупно, на цепочке; удар о костяшку — поза руки); лента на горле; соединённые сзади косички; кисть, выходящая из рукава.
- **Модели (весь лист):** D — NB × 20 · F — NB Pro × 6.
- **Приёмка:** нет тёмных корней; глаза тёмно-карие; белое Илвейнов холодное и шелковистое, стола — тёплый грубый лён (две разные белизны в одном кадре).
- **Решение на утверждение:** оливковый подтон кожи — моё предложение (она бледная, но не «фарфоровая»); на сверку режиссёру и главному сценаристу.

## A-05 Руэл Корвейн — CH-0005
- **Назначение:** сц. 10 (вход, рукопожатие **левой**), 11 (**липсинк #2** «I don't drink before a storm.»), 12 (на коленях).
- **Народ / класс:** P3 · знать. Самая широкая фигура S1.
- **Состав:** 00, 01, 02, 03, 04, **05**, 06, 07.
- **Эмоции:** (1) big warm laugh, head back, eyes crinkled; (2) attentive man-of-the-people — leaning in, kind eyes, half smile (he knows your daughter's name); (3) gentle teasing — eyebrow raised, mouth amused; (4) mock-grave refusal — smiling eyes over a firm mouth (the lip-sync line); (5) urgent concern — brows up, mouth open calling for help; (6) unreadable stillness — face at rest, eyes steady on something below frame.
- **ID-блок `[ID: RUEL]`:**
```
[ID: RUEL] man of 48, big and heavy-chested, broad sailor's shoulders, thickening at the middle, the widest figure in any group; deep sea-weathered tan; hair: salt-and-pepper tied in a short sailor's queue, grey-streaked dark beard trimmed square; eyes: warm hazel with laugh-lines; a white rope-scar across the back of HIS RIGHT hand; outfit: deep-blue admiral's LONG coat reaching the calves, high collar, silver braid, a silver cormorant clasp at the collar, white shirt, dark boots; a black pearl ring on HIS LEFT hand
```
- **Промпт `00_master`:** `[ID: RUEL] … verbatim. Waist-up portrait, three-quarter view, warm neutral expression, mouth closed, looking at the viewer, his left hand resting on his chest so the black pearl ring is visible on the left hand, right hand at his side. {STYLE}, plain warm light-grey background, flat even neutral lighting. Avoid: ring on the right hand, rings on both hands, short jacket, bright royal blue, gold braid, thin build, photorealism, 3D render look, text, watermark, extra fingers.`
- **`06_details`:** пряжка-баклан (по `heraldry.md` H-01 в серебре); левая рука с кольцом (закрытое кольцо, обычный вид — **без механизма**); правая кисть со шрамом от верёвки; косичка-очередь сзади.
- **Правило:** на листе Руэла **нет** осколка, верёвочек на шее, чёрных камешков — ничего похожего.
- **Модели (весь лист):** D — NB × 20 · F — NB Pro × 6.
- **Приёмка:** кольцо на левой; сюртук длинный (до икр); синий глубокий, не королевский; шрам на правой.

## A-06 Холлис Кетт — CH-0003
- **Назначение:** сц. 13–16 (Счётный дом). В пилоте `[VO]`, без липсинка; крупные планы — немые.
- **Народ / класс:** светлая кожа (P5/P1) · Средние.
- **Состав:** 00, 01, 02, 03, 04, 06, 07.
- **Эмоции:** (1) absorbed calculation — eyes down, lips moving silently, brow tight; (2) suspicious double-check — head tilted, peering over the spectacles; (3) about to be brave — inhaling, eyebrows lifted, mouth just opening; (4) swallowed cowardice — mouth closing, eyes sliding away, cheeks colouring; (5) grateful flush — shy surprised half smile, ears pink; (6) dawning dread — very still, eyes moving from one thing to another, face draining.
- **ID-блок `[ID: HOLLIS]`:**
```
[ID: HOLLIS] man of 26, very tall and thin, stooped from the desk, head pushed forward, long fingers; light skin that rarely sees the sun; hair: flat straw-blond, parted on the left, one cowlick sticking up at the crown; eyes: pale blue, short-sighted; round wire spectacles with the LEFT lens cracked (cracked lens on the right side of the image when he faces us); ink stains on the index and middle fingers of HIS RIGHT hand; outfit: long light ash-grey clerk's coat, white stock, black sleeve-guards, worn shoes
```
- **Суффикс с зажимом (с сц. 15):** `; a small brass ledger-clip in his left breast pocket` (вид зажима — E-03).
- **Промпт `00_master`:** `[ID: HOLLIS] … verbatim. Waist-up portrait, three-quarter view, mild neutral expression, mouth closed, looking at the viewer over his spectacles, right hand raised near the chest so the ink-stained fingers are visible. {STYLE}, plain warm light-grey background, flat even neutral lighting. Avoid: cracked right lens, intact lenses, dark grey or slate coat, neat flat hair without the cowlick, muscular build, photorealism, 3D render look, text, watermark, extra fingers.`
- **`06_details`:** очки (трещина на левом стекле — форма трещины фиксируется: одна диагональ + две короткие); пальцы с чернилами; вихор; левый нагрудный карман (пустой — и с зажимом, edit).
- **Модели (весь лист):** D — NB × 18 · F — NB Pro × 5.
- **Приёмка:** кафтан **светлее** сланца Одо (поставить рядом с плашкой `#4F5A63` при приёмке); трещина слева у него; самый высокий в группе клерков.

## A-07 Дама Урсула Лантри — CH-0011
- **Назначение:** сц. 15 (**липсинк #4** «A clerk who is trusted gets a clip.»), 16 (продолжает писать).
- **Народ / класс:** светло-коричневая кожа (P2) · Ступени/знать.
- **Состав:** 00, 01, 02, 03, 04, **05**, 06, 07.
- **Эмоции:** (1) gentle amused smile, eyes unblinking; (2) appraising over the pince-nez — head lowered a fraction, eyes up; (3) serene indifference — eyes on her own page, face smooth; (4) quiet finality — small closed-mouth nod; (5) faint approval — the corners of the mouth lift a hair; (6) cold patience — perfectly still, eyes half-lidded.
- **ID-блок `[ID: URSEL]`:**
```
[ID: URSEL] woman of 62, small and very upright, still; light-brown skin with fine wrinkles; hair: iron-grey pinned in a tight coil at the nape with copper pins; eyes: dark, amused, unblinking; pince-nez on a fine copper chain; a plain copper widow's ring on HER RIGHT hand; outfit: black gown with copper embroidery at the cuffs and high collar; a black walking stick with a small copper balance-scale handle held in her right hand
```
- **Промпт `00_master`:** `[ID: URSEL] … verbatim. Waist-up portrait, three-quarter view, faint pleasant expression, mouth closed, looking at the viewer through the pince-nez, both hands resting on the stick handle. {STYLE}, plain warm light-grey background, flat even neutral lighting. Avoid: gold or bronze metal, yellow brass, loose hair, tall figure, glasses with arms, photorealism, 3D render look, text, watermark, extra fingers.`
- **`06_details`:** ручка трости-весы (коромысло **ровное**, как в гербе H-07); пенсне на цепочке; кольцо; медные шпильки в узле.
- **Модели (весь лист):** D — NB × 20 · F — NB Pro × 6.
- **Приёмка:** медь розоватая, не бронза; рост — ниже Холлиса на голову и больше.

## A-08 Одо Феннике — CH-0010
- **Назначение:** сц. 17 (комната ретрансляции, «Nothing unheard», `[MS]`).
- **Народ / класс:** P2 · знать.
- **Состав:** 00, 01, 02, 03, 04, 06, 07.
- **Эмоции:** (1) half-closed listening — heavy lids, head tilted a little; (2) harmless faint smile; (3) near-whisper — lips barely parted; (4) sudden alertness — eyes opening fully, nothing else moves; (5) satisfied stillness; (6) concealed calculation — gaze sliding to the side under lowered lids.
- **ID-блок `[ID: ODO]`:**
```
[ID: ODO] man of 55, short and slight, almost frail, round-shouldered, hands hidden in his sleeves; pale skin; head shaved smooth, no beard, thin dark eyebrows; eyes: pale grey, heavy-lidded, half-closed; outfit: slate-grey robe with an acid sulphur-yellow lining that shows at the cuffs and hem, soft felt slippers; a small silver brooch shaped like a single upright hare's ear at HIS RIGHT collar (left side of the image when he faces us)
```
- **Промпт `00_master`:** `[ID: ODO] … verbatim. Waist-up portrait, three-quarter view, mild half-lidded expression, mouth closed, looking slightly past the viewer, hands in sleeves. {STYLE}, plain warm light-grey background, flat even neutral lighting. Avoid: hair, beard, gold yellow, light ash-grey coat, menacing grimace, tall figure, photorealism, 3D render look, text, watermark.`
- **`06_details`:** брошь (H-06), подкладка в движении, войлочные туфли, кисти в рукавах.
- **Модели (весь лист):** D — NB × 18 · F — NB Pro × 5.
- **Приёмка:** сланец заметно темнее кафтана Холлиса; жёлтый кислотный, не золото; не «зловещий» облик — безобидность нарочитая.

---

# B. Лёгкие референсы — 11 (+2 необязательных)

Общая схема: костюм + один-два якоря; лицо — только где указано. Финал — NB2, кроме отмеченных.

## B-01 Хелм Лукан Даск — CH-0016 · **лицо нужно** (липсинк #3)
- **Назначение:** сц. 10–12; «…and the Ninth Sluice—»; падение. Больше живым не появится, но кадры 2, 3, 5 из списка липсинка архивируются для повторов.
- **Виды:** `00_master` (по пояс 3/4), `01` фронт + спина в рост (мантия), `05_mouth`, `06` правая рука с бронзовым кольцом-серпом.
- **Эмоции (в мастере не нужны; для кадра):** усталая важность; потеря места в тексте (растерянность); облизывает губы.
- **ID-блок:**
```
[ID: LUCAN] old man of 71, tall, stooped and frail; fair weathered polder skin with age spots; white beard cut square, thin white hair combed back; eyes: faded grey-green; a heavy bronze sickle-shaped ring on HIS RIGHT hand; outfit: the Helm's robe of state — a floor-length ochre robe under a storm-grey mantle with a high collar
```
- **Промпт:** `[ID: LUCAN] … verbatim. Waist-up portrait, three-quarter view, tired dignified neutral expression, mouth closed, right hand resting on a rolled map so the bronze sickle ring is visible. {STYLE}, plain warm light-grey background, flat even neutral lighting. Avoid: ring on the left hand, pearl, gold, crown, sceptre, photorealism, 3D render look, text, watermark, extra fingers.`
- **Модели:** D — NB × 8 · F — **NB Pro** × 3 (мастер, рост, рты).

## B-02 Джуно Бриск — CH-0063
- **Виды:** по пояс 3/4 (лицо, MS), в рост фронт; деталь: ложечка дегустатора на цепочке.
- **ID-блок:** `[ID: JUNO] young woman of 19, short and plump, kitchen-pale skin; auburn hair tucked under a white taster's coif; eyes: green-brown, nervous; outfit: plain grey palace servant's dress with a white apron; a small silver taster's spoon on a chain at her chest`
- **Промпт:** `[ID: JUNO] … verbatim. Two views side by side: waist-up three-quarter portrait with a polite nervous neutral face, mouth closed; full-body front view. {STYLE}, {SHEET}. Avoid: visible hair beyond a few auburn strands, jewellery, photorealism, 3D render look, text, watermark.`
- **Модели:** D — NB × 4 · F — NB2 × 1.

## B-03 Фоссетт — CH-0055
- **Виды:** по пояс 3/4 (лицо, MS — улыбка «приятная»), в рост фронт и спина (ряд клерков).
- **ID-блок:** `[ID: FOSSETT] man of 30, short and round, pink complexion; pomaded chestnut hair with a sharp centre parting; small pleasant eyes; outfit: long light ash-grey clerk's coat, white stock, spotless white sleeve-guards, a small copper pin on the lapel`
- **Промпт:** `[ID: FOSSETT] … verbatim. Two views: waist-up three-quarter portrait with a pleasant bland smile, mouth closed; full-body back view at a standing desk height. {STYLE}, {SHEET}. Avoid: spectacles, ink stains, black sleeve-guards, tall figure, photorealism, 3D render look, text, watermark.`
- **Отличие от Холлиса:** белые нарукавники (у Холлиса чёрные), рост, пробор по центру.
- **Модели:** D — NB × 4 · F — NB2 × 1.

## B-04 Магс — CH-0049 (в E1 только общий план и спина)
- **Виды:** в рост фронт и спина, силуэт; лицо — мелко.
- **ID-блок:** `[ID: MAGS] 15-year-old girl, tall for her age and gangly; olive skin; a frizz of black hair tied up with a strip of red rag; outfit: a man's oversized dark waistcoat full of pockets over a faded shirt, rolled trousers, bare muddy feet, a rake over the shoulder`
- **Промпт:** `[ID: MAGS] … verbatim. Full-body front view and full-body back view side by side, standing on mud with a cocky stance. {STYLE}, {SHEET}. Avoid: braid, earrings, red clothing other than the hair rag, photorealism, 3D render look, text, watermark.`
- **Модели:** D — NB × 4 · F — NB2 × 1.

## B-05 Корр — CH-0048
- **Виды:** средний план (сц. 6), в рост сбоку на колесе, спина.
- **ID-блок:** `[ID: CORR] older man of about 55, barrel-bodied with huge thighs from walking the wheel; sun-blackened deep brown skin; grey beard twisted into a single rope; HIS LEFT HAND IS MISSING — the left forearm ends in a stump wrapped in old leather; a reed whistle held in his right hand; outfit: sleeveless patched leather jerkin, knee breeches, bare calloused feet`
- **Промпт:** `[ID: CORR] … verbatim. Two views: waist-up three-quarter portrait, calm weathered expression, mouth closed; full-body side view walking on the slats of a big wooden treadmill wheel. {STYLE}, {SHEET}. Avoid: a left hand, two hands, a hook, whistle in the left hand, braided hair, photorealism, 3D render look, text, watermark.`
- **Приёмка:** левой кисти нет (модели упорно дорисовывают — проверять на каждом листе).
- **Модели:** D — NB × 4 · F — NB2 × 1.

## B-06 Сборщик десятины (новый, без имени)
- **Виды:** средний план 3/4 (лицо: сц. 19 — «цвет его табарда»), в рост фронт; деталь: ящик на цепи у запястья.
- **ID-блок:** `[ID: COLLECTOR] lean sallow man in his forties, thin moustache, tired narrow eyes; outfit: slate-grey tabard with a single sulphur-yellow stripe across the chest over a dark coat, a felt hat; a small iron-bound wooden box chained to his LEFT wrist`
- **Промпт:** `[ID: COLLECTOR] … verbatim. Two views: waist-up three-quarter portrait, officious neutral face, mouth closed; full-body front view with the chained box hanging from the left wrist. {STYLE}, {SHEET}. Avoid: hare brooch, weapons, rust red, photorealism, 3D render look, text, watermark.`
- **Модели:** D — NB × 4 · F — NB2 × 1.

## B-07 Марен — CH-0006 · **только спина** (полный лист — к E2)
- **Виды:** спина в рост; спина по пояс (за плечом Руэла).
- **ID-блок (полный, для E2 — использовать уже сейчас):**
```
[ID: MAREN] young woman of 19, tall, lean and long-legged; warm brown skin; hair: dark umber-brown curls tied high at the crown with a silver cord, a short bouncing tail; eyes: grey-blue, steady; outfit: deep-blue SHORT riding coat cut at the hip, white shirt, grey breeches, sea boots; a brass spyglass on her belt at HER RIGHT hip; hands clasped behind her back
```
- **Промпт:** `[ID: MAREN] … verbatim. Back view only, face not visible: full-body back view standing at attention with hands clasped behind her back, and a waist-up back view. {STYLE}, {SHEET}. Avoid: long coat, coat below the hip, visible face, ring, rings on any finger, photorealism, 3D render look, text, watermark.`
- **Правило:** **никаких колец** на её руках в S1 (кольцо — только у Руэла).
- **Модели:** D — NB × 4 · F — **NB Pro** × 1 (база будущего полного листа).

## B-08 Кес Мэбри — CH-0004 · **спина и руки** (полный лист — к E2)
- **Виды:** спина в рост (полушлем под левой рукой); руки на засове — **взрослые** (34) и **юные** (17, сц. 1) — **одна и та же хватка, тот же ракурс**.
- **ID-блок (полный, для E2):**
```
[ID: KES] woman of 34, medium height, broad and compact, heavy forearms, stiff right knee; ruddy weathered upland skin; hair: jet-black, short, both sides shaved, top swept back; eyes: dark grey; a burn scar along HER RIGHT jaw; outfit: rust-red Rusk tabard over a black gambeson, black breeches, upland boots; a dented half-helm with a painted white stripe front to back, carried under HER LEFT arm
```
- **Промпт (спина):** `[ID: KES] … verbatim. Back view only, face not visible: full-body back view, square stance, the dented half-helm tucked under her left arm (on the LEFT side of the image in the back view). {STYLE}, {SHEET}. Avoid: visible face, helmet on the head, long hair, scarlet red, photorealism, 3D render look, text, watermark.`
- **Промпт (руки, пара листов):** `Close-up insert reference: two hands gripping a heavy iron gate bar from below and pushing it upward-and-across into its bracket, seen from slightly below at a three-quarter angle, the left hand nearer the camera, black padded gambeson cuffs at the wrists. Version A: young hands of a 17-year-old, smooth, rain-wet, night lantern light. Version B: the same grip and same framing, hands of a 34-year-old soldier, broader, scarred knuckles, dusk light. {STYLE}, {SHEET}. Avoid: faces, rings, gloves, different hand positions between versions, photorealism, 3D render look, text, watermark, extra fingers.`
- **Правило:** версия B делается **edit-ом от финала версии A** (кадрирование совпадает — фиксированное правило сц. 18).
- **Модели:** D — NB × 6 · F — **NB Pro** × 3 (спина, руки A, руки B).

## B-09 Лисс — CH-0023 · силуэт (сц. 1)
- **Виды:** силуэт на коньке крыши против ночного неба; одна длинная коса слева.
- **Промпт:** `Silhouette reference: a slight young woman standing on the ridge of a stilt-house roof at night, seen from below and from her LEFT side, dark shape against a deep blue night sky with rain, one long braid hanging on her LEFT side, a neckerchief at the throat, head lifted as if humming. No face detail, pure silhouette with a thin cool rim light. {STYLE}. Avoid: visible face, two braids, braid on the right, loose hair, photorealism, 3D render look, text, watermark.`
- **Модели:** D — NB × 4 · F — NB2 × 1.

## B-10 Сестра Венн — CH-0056 · рукав и кисть (сц. 1)
- **Промпт:** `Insert reference: an old woman's hand and forearm in a heavy deep-grey wool robe sleeve reaching down from the top of the frame, the hand small, very clean, age-spotted, fingers gentle and practised, night, a single lantern below. No face, no body beyond the sleeve. {STYLE}, {SHEET}. Avoid: rings, bell, jewellery, violet, linen-coloured cloth, photorealism, 3D render look, text, watermark, extra fingers.`
- **Модели:** D — NB × 3 · F — NB2 × 1.

## B-11 Старый Кантор на лестнице (без имени, сц. 8)
- **Виды:** в рост 3/4 сбоку (уступает дорогу), кисть, делающая знак благословения (знак — из глоссария жестов режиссёра; до него — нейтральная поза кисти).
- **ID-блок:** `[ID: OLD-CANTOR] very old man, stocky and bowed, round soft face, bald with a white fringe, mouth closed and slack; a yellowed linen band wrapped around his throat; outfit: a worn undyed-linen Choir robe greyed with age, rope belt; one hand resting at his throat, the other raised in a small formal sign`
- **Промпт:** `[ID: OLD-CANTOR] … verbatim. Full-body three-quarter side view stepping aside on a curving stone stair, plus a close-up of his raised signing hand. {STYLE}, {SHEET}. Avoid: violet band, singing mouth, skeletal thinness, photorealism, 3D render look, text, watermark, extra fingers.`
- **Вопрос:** в каноне Кантор Сабин (немой, «скелет», жёлтая лента) впервые появляется в E3. Чтобы зритель не принял этого старика за Сабина, я сделал его **плотным и круглолицым**. Если сценарист задумывал здесь Сабина — заменить лист на Сабина (CH-0057).
- **Модели:** D — NB × 4 · F — NB2 × 1.

## B-12 *(необязательно)* Весна — CH-0012 · **лица нет никогда**
- **Промпт:** `Reference: a small, very straight old woman seen in full body, front three-quarter view, completely covered by a violet veil from the crown of the head to the collarbones — no face, no hair and no ears visible through the veil — over an undyed-linen Choir robe and a white-and-violet mantle; her right hand raised from the sleeve, pale, age-spotted, long fingers with a silver ring on every finger of the right hand; left hand hidden. {STYLE}, {SHEET}. Avoid: visible face, see-through veil, visible eyes, rings on the left hand, photorealism, 3D render look, text, watermark, extra fingers.`
- **Модели:** D — NB × 3 · F — NB2 × 1.

## B-13 *(необязательно)* Брат Элм — CH-0022
- **ID-блок:** `[ID: ELM] slight young man of 22, short, soft-faced; olive skin; ash-brown close-cropped hair with a shaved tonsure band from ear to ear over the crown; light brown watchful eyes; undyed-linen Choir robe; a violet cord knotted round HIS LEFT wrist; head bowed`
- **Промпт:** `[ID: ELM] … verbatim. Full-body three-quarter view, head bowed, eyes on someone's hands out of frame, and a back view showing the tonsure band. {STYLE}, {SHEET}. Avoid: cord on the right wrist, full head of hair, photorealism, 3D render look, text, watermark.`
- **Модели:** D — NB × 3 · F — NB2 × 1.

---

# C. Групповые и униформенные листы — 8

Принцип: **цвет и силуэт вместо лиц** (`production_notes.md` §4: не больше четырёх читаемых лиц в кадре). Лист = 4–6 фигур в ряд, разные народы (см. `peoples_and_costume.md` §1), без главных героев.

| ID | Группа | Промпт (англ.) | D / F |
|---|---|---|---|
| **C-01** | Грязекопы | `Group costume sheet, five mudlarks of the poor lowland district in a row, full body: two children, one teenage boy, one old woman, one old man, mixed skin tones from light olive to deep brown, patched tar-brown and oatmeal rags, rag-wrapped or bare feet, mud to the knees, rakes, sieves and net bags, one with a ragged knitted cap. {STYLE}, {SHEET}. Avoid: braids on the left, red hair rags, earrings, spiral ornaments, clean clothes, photorealism, 3D render look, text, watermark.` | NB×4 / NB2×1 |
| **C-02** | Ходоки колеса | `Group sheet, treadmill walkers seen from behind, five figures in a row, full body, mixed skin tones, bare or rag-shirted backs, rope belts, knee breeches, bare feet with thick calluses, one tiny bow-legged walker in a patchwork cap, identical posture of walking in step, plus one side view of a walker leaning into the slats. {STYLE}, {SHEET}. Avoid: faces, shoes, uniforms, photorealism, 3D render look, text, watermark.` | NB×4 / NB2×1 |
| **C-03** | Жители переулка Низов (а) ночь CY 295, (б) CY 312 | `Group sheet, lowland lane folk of a stilt-house district, six full-body figures as dark silhouettes standing in doorways, each holding one lantern, mixed body types (heavy, thin, bent, a child on a hip), oilskins, headscarves, shawls, warm lantern rim light; version A soaked in rain at night, version B dry at dusk. {STYLE}, {SHEET}. Avoid: readable faces, spiral earrings, single left braids, photorealism, 3D render look, text, watermark.` | NB×4 / NB2×2 (две версии, B — edit от A) |
| **C-04** | Клерки Лантри | `Group sheet, five bank clerks in identical long light ash-grey coats with black sleeve-guards, full body, three seen from behind at standing desks and two from the front, varied builds and skin tones, small brass clips on two of the breast pockets, neat hair, quiet posture. {STYLE}, {SHEET}. Avoid: very tall stooped straw-haired figure, spectacles, copper chains, black silk, photorealism, 3D render look, text, watermark.` | NB×4 / NB2×1 |
| **C-05** | Стража Расков (в шлемах) | `Group uniform sheet, four soldiers of an upland soldier house, full body: front, back, side, and one holding a long pike: rust-red brick-oxide tabards over black padded gambesons, black cloaks, dented open half-helms worn on the head with painted rank stripes (one white stripe for a sergeant, others plain), faces shadowed under the helmets, black iron gate badge on one officer. {STYLE}, {SHEET}. Avoid: scarlet, plate armour, plumes, full face visibility, photorealism, 3D render look, text, watermark.` | NB×4 / NB2×1 |
| **C-06** | Восемь мест в зале десятины | `Reference sheet for a council hall: eight groups seen from behind and from a high gallery, each group a block of two or three standing stewards dressed in one house's colours under its tall vertical banner with a slanted cut at the bottom: 1) cool white silk; 2) deep blue with silver; 3) rust red with black; 4) yellowish sea-green with bone; 5) slate grey with acid sulphur-yellow lining; 6) black with polished pinkish copper; 7) warm undyed linen with black and violet throat-bands; 8) matte ochre with bronze. Banners show simple flat emblems as on the attached emblem sheet. Colour blocks clearly separated. {STYLE}, {SHEET}. Avoid: readable faces, text on banners, teal, orange, photorealism, 3D render look, watermark.` (референсы: финальные эмблемы H-01…H-08) | NB×4 / **NB Pro**×1 |
| **C-07** | Одеяния Хора | `Costume sheet for a religious order of singers, four full-body figures: 1) novice in a short undyed-linen tunic with a shaved nape, seen from behind; 2) cantor in a hooded undyed-linen robe with rope belt and a violet silk throat-band, front; 3) the same cantor from behind, hood up; 4) gleaner in linen with a black stole, a small round polished stone in a silver cage on a chain, a silver hand-bell at the belt. Warm coarse linen, never bright white. {STYLE}, {SHEET}. Avoid: cracked stones, stones on cords, spiral ornaments, white silk, photorealism, 3D render look, text, watermark.` | NB×4 / NB2×1 |
| **C-08** | Люди Феннике | `Costume sheet, four full-body figures of a house of listeners and messengers: 1) relay-keeper in a slate-grey coat with yellow lining, a small tone-fork on a cord; 2) house guard in slate with a yellow stripe and a short staff; 3) informer in a matte grey hooded coat with a yellow cord at the throat half hidden under the collar, hood shaped with two small upright points like hare's ears; 4) a man in a grey coat seen from behind with a small silver hare's-ear pin at the collar, standing by a doorway. {STYLE}, {SHEET}. Avoid: gold yellow, weapons drawn, readable faces on 3 and 4, photorealism, 3D render look, text, watermark.` | NB×4 / NB2×1 |

---

# D. Локации — 12

## D-0. Общая география Хайуотера *(предложение — на сверку хранителю: в каноне сторон света нет)*

Ориентация нужна, чтобы солнце и Шпили стояли на своих местах во всех кадрах.

```
                         N
          (море)   ГАВАНЬ ●  Patient Gull
   W  ~~~~~~~~~~~~  \                          
   ~~ море ~~~~~~~~  \  ┌─ Сухой дворец ─┐  ● Храм Хора / ШПИЛЬ ХОРА
   ~~~~~~~~~~~~~~~~~  \ │ ▲ ШПИЛЬ КОРОНЫ │        ● Счётный дом (смотрит на запад: Шпиль Короны — на фоне заката)
   ~~~~~~~~~~~~~~~~~~  \└───────────────┘   ● Дом Слушания
   ~~~~~~~~~~~~~~~~~~~   СТУПЕНИ (гранит, вершина холма)
   ~~~~~~~~~~~~~~~~~~~~   СРЕДНИЕ (кирпич на гребне дамбы) — ворота эвакуации Девятого
   ~~~~~~~~~~~~~~~~~~~~~  НИЗЫ: Первый…Двенадцатый шлюз — веером к морю (юго-запад)
   ~~~~~~~~~~~~~~~~~~~~~~   ▲ ШПИЛЬ ШЛЮЗА (на нижней дамбе)   ДЕВЯТЫЙ ● задний канал → к морю
                         S                                      E (рассвет — из-за холма)
```
- **Море и гавань — на западе и северо-западе.** Закат — над морем: «низкое солнце» в окне зала десятины (окно смотрит на гавань), контражур Шпиля Короны с лестницы Счётного дома (сц. 16).
- **Рассвет — с востока, из-за гранитного холма:** Низы на рассвете **в тени холма** («stilt-town in its own shadow», сц. 2), Шпили — силуэтами на светлеющем небе.
- **Девятый шлюз — юго-запад, у моря.** С конька крыши в Девятом (сц. 9) Шпиль Короны виден **на северо-северо-востоке**, освещённый закатным солнцем с запада.
- **Шпили:** Корона ~160 м (на западной бровке вершины, внутри Дворца); Хор ~120 м (восточнее, круглый храм у подножия); Шлюз ~90 м (на нижней дамбе, ближе всех к Девятому, звучит «фальшиво»). Высоты — предложение в пределах канона (60–200 м).
- **Шпиль (общий облик):** стеклянно-чёрный камень, спиральные бороздки, восходящие **по часовой стрелке** (если смотреть сверху) — *вопрос хранителю: для бороздок Шпилей направление в выдержке не задано; ставлю по солнцу, как все спирали*; корона — кольцо открытых арочных «горл»; при пении бороздки светятся бледным сине-белым виток за витком; вода в пределах видимости — стекло.

Общий шаблон финала ракурса (edit от мастер-плана, NB2): `Use the location from image 1 exactly: same architecture, materials, colours and landmarks. New camera position: {ракурс}. {свет}. {STYLE}, {LOC}. {AVOID}`
Общий шаблон светового режима (edit от финала ракурса, NB2): `Use image 1 exactly — same composition, camera and every object in place. Change only the time of day and weather to: {режим}. {STYLE}. {AVOID}`

Режимы (тексты для `{режим}`):
- **DAWN-EBB:** `cold blue-grey dawn, the sun not yet over the hill to the east, the district in deep shadow, pale sky behind the towers, mist over wet silt`
- **MORNING:** `soft low-contrast morning light from the east, pale turquoise sky`
- **NOON:** `high flat midday light from a high window, minimal shadows`
- **LATE-AFT:** `warm low late-afternoon sun from the west over the sea, long shadows pointing east, golden light`
- **DUSK:** `dusk, the sun just set over the sea to the west, peach-to-violet sky, first lanterns lit, cool shadows`
- **NIGHT:** `night, deep blue darkness, small warm pools of lantern light`
- **RAIN:** `heavy rain, wet reflective surfaces, grey haze, rain streaks`
- **FLOOD:** `night flood, black water up to the door-lintels, lanterns half drowned, rain`

## D-01 Хайуотер, мастер-общий план — PL-0004
- **Назначение:** сц. 2 (шестисекундный подъём — **высокий кадр** для вертикальной панорамы, кадрируется и в 9:16), фоны сц. 9, 16; мастер-план сезона.
- **Ракурсы:** **A** (мастер) — из Девятого, снизу вверх на северо-восток: сваи и крыши Низов → кирпичная линия дамбы и Средние → гранитные террасы Ступеней → Шпили (Шлюз ближе слева, Корона на вершине, Хор правее). Формат **вертикальный 9:21** (высокий холст для панорамы). **B** — с лестницы Счётного дома на запад, вниз над городом к морю (сц. 16; = D-11 ракурс 3). **C** — с моря, от входа в гавань на восток: весь холм с тремя ярусами (для повторов и маркетинга).
- **Свет:** A — DAWN-EBB (пилот), LATE-AFT с горящим Шпилем Короны (фон сц. 9), DUSK (позже); B — DUSK (пилот); C — LATE-AFT (пилот). Позже: NIGHT, RAIN, FLOOD (E10).
- **Карта ракурсов:**
```
            C ← камера в море, смотрит на восток
   море ~~~ [гавань] — [Дворец ▲Корона] — [Ступени] — B камера на лестнице банка, смотрит на запад
                         \  Средние / дамба
                          \  Низы
                     A камера в Девятом, смотрит на СВ вверх по холму
```
- **Промпт A (мастер, t2i):** `Tall vertical establishing view of a capital city built on a granite hill in a vast river delta, seen from below at the foot of the hill: in the foreground a crowded town of tarred timber stilt-houses on piles, plank-walks and rope-bridges over drained canals of wet silt; above it a long brick dike crest lined with three-storey brick houses; above that grey granite terraces with noble halls and gardens; at the summit, rising above everything, three colossal black glassy towers with spiral grooves winding up their sides and crowns of open arched throats — the nearest tower on the left is lower and looks worn, the tallest stands on the summit, a third rises to the right behind a round temple. {DAWN-EBB}. {STYLE}, {LOC}, vertical composition with clear tiers for a slow upward camera pan. {AVOID}`
- **Модели:** A — D NB × 6, F NB Pro × 1; B, C — D NB × 2, F NB2 × 1 каждый; режимы A-LATE-AFT, B-DUSK — D NB × 1, F NB2 × 1.

## D-02 Переулок Девятого шлюза с дверным столбом Нан — PL-0008 / PL-0019
- **Назначение:** сц. 1 (ночь наводнения CY 295), 2 (рассвет-отлив), 19 (сумерки-прилив); склейка сц. 1→2 по **одному и тому же столбу**; повтор в E10 (все плейты сц. 1 — именованные ассеты библиотеки).
- **Ось переулка:** северо-восток (к дамбе и воротам) ↔ юго-запад (к заднему каналу и морю). Дом Нан — на **северо-западной** стороне переулка, дверь смотрит на юго-восток; столб двери — **правый** косяк, если смотреть на дверь снаружи.
- **Столб с отметками прилива (фиксированный ассет):** лестница зарубок ножом с годами, тёмные полосы воды; отметка **CY 295** — **высоко над остальными**, почти у притолоки (в сц. 1 вода доходит до притолок). Зарубки без читаемых надписей (цифры, если нужны, — накладкой на монтаже).
- **Ракурсы:**
  - **C1 (мастер)** — посреди переулка, на уровне глаз с дощатого настила, вдоль оси на СВ: дома на сваях по сторонам, фонарный столб справа на переднем плане, вдали — линия дамбы и ворота, над ними силуэты Шпилей. *Кадр колыбели (сц. 1, первый кадр сериала): колыбель плывёт по центру оси к камере, фонарь справа.*
  - **C2** — перпендикулярно двери Нан, средний план: дверь, столб с отметками, лестница вниз к илу, сундуки/лодка под полом.
  - **C3** — обратный: вдоль оси на ЮЗ, к заднему каналу и морю (сц. 19, закат за морем в конце переулка).
  - **C4** — сверху, с верёвочного моста между домами (поза Уика вниз головой; рассвет).
- **Режимы:** C1 — DAWN-EBB (мастер), FLOOD (сц. 1), DUSK (сц. 19, вода вернулась в переулок, фонари у каждой двери); C2 — DAWN-EBB, FLOOD, DUSK; C3 — DUSK; C4 — DAWN-EBB. Позже: RAIN, повторный FLOOD CY 312 (E10).
- **Карта ракурсов:**
```
   СВ (дамба, ворота, Шпили)
        ↑
   ┌────┼────┐
   │дом │    │ дом       C1 ● смотрит ↑ (СВ)    фонарный столб ◆ справа от C1
   │НАН │    │           C2 ● смотрит ← на дверь Нан (СЗ сторона)
   │дверь▐ ← C2          C3 ● смотрит ↓ (ЮЗ, к морю)
   │    │ ◆  │           C4 ● верёвочный мост над переулком, смотрит вниз-↑
   └────┼────┘
        ↓
   ЮЗ (задний канал, море, закат)
```
- **Промпт C1 (мастер):** `Eye-level view straight down the middle of a narrow lane in a poor district of tarred timber stilt-houses, two and three storeys, standing on thick tarred piles, connected by plank-walks along both sides and a sagging rope-bridge overhead, small boats tied under the floors, the canal bed between the houses exposed as wet grey-brown silt with puddles; a wooden lantern post in the right foreground; at the far end of the lane rises a long brick dike with a heavy gate, and above it, distant and huge, the silhouettes of black spiral-grooved towers. On the left, a door with a thick wooden doorpost carved with a ladder of knife-cut tide marks, one mark far above all the others near the lintel. {DAWN-EBB}. {STYLE}, {LOC}. {AVOID}`
- **Промпт режима FLOOD (C1):** `Use image 1 exactly — same lane, same houses, same lantern post. Change only to: night flood, the whole lane full of black still water up to the door-lintels, one lantern still burning on the post on the right, the other lanterns along the plank-walks dark, heavy rain, the empty middle of the lane clear for a floating object. {STYLE}. {AVOID}`
- **Модели:** C1 — D NB × 6, F NB Pro × 1; C2–C4 — D NB × 2, F NB2 × 1 каждый; режимы (C1: FLOOD, DUSK; C2: FLOOD, DUSK) — D NB × 1, F NB2 × 1 каждый.
- **Приёмка:** столб, отметки и фонарный столб — на тех же местах во всех режимах; колыбели и людей на плейте нет (колыбель — отдельный предмет E-10).

## D-03 Ворота эвакуации Девятого — PL-0021
- **Назначение:** сц. 1 (сторона Низов, ночь CY 295: толпа у ворот, юные руки задвигают засов), сц. 18 (сторона Средних, сумерки CY 312: засов падает, кадр рук — **то же кадрирование**, что в сц. 1).
- **Облик:** огромные дубовые ворота, окованные железом, в арке кирпичной дамбы; со стороны Средних — тяжёлый железный засов в скобах на уровне груди, караульная ниша, ступени; со стороны Низов — гладкие доски с железом, следы ударов, отметки воды, ступени уходят в воду.
- **Ракурсы:** **G1 (мастер)** — сторона Низов, снизу, ворота во весь кадр (толпа — силуэты, отдельно). **G2** — сторона Средних, средний план на засов и стражу. **G3** — вставка: засов и скобы, ракурс снизу 3/4 под руками (общий для сц. 1 и 18; кадрирование фиксируется один раз и копируется).
- **Режимы:** G1 — FLOOD/NIGHT-RAIN (пилот); G2 — DUSK (пилот); G3 — NIGHT-RAIN и DUSK (пилот, edit одного от другого). Позже: G1 — DUSK E10.
- **Карта:**
```
   СРЕДНИЕ (выше)   G2 ● смотрит ↓ на засов изнутри     G3 ● под засовом, снизу 3/4
   ═══════[ВОРОТА]═══════  дамба
   НИЗЫ (ниже)      G1 ● смотрит ↑ на ворота из воды/переулка
```
- **Промпт G1:** `Low-angle view from a flooded lane up at a huge iron-bound oak gate set into the arch of a tall brick dike, the gate shut, stone steps disappearing into black water, dents and scrapes on the planks, tide stains on the brick. {FLOOD}. {STYLE}, {LOC}. {AVOID}`
- **Модели:** G1 — D NB × 6, F NB Pro × 1; G2, G3 — D NB × 2, F NB2 × 1; режим G3-DUSK — D NB × 1, F NB2 × 1.

## D-04 Задний канал, голый порог старого шлюза, отстойник — PL-0020
- **Назначение:** сц. 3 (находка; кольца по воде) — деньги-сцена M2; кольца возвращаются в чаше сц. 20.
- **Облик:** обнажённое илистое дно широкого канала, серые лужи, сваи; старый каменный порог шлюза **впервые голый** — скользкие замшелые камни, ржавые петли от снятых створок; за порогом — **отстойник чёрной стоячей воды**, гладкий как масло; Шпиль Шлюза виден вдали.
- **Ракурсы:** **K1 (мастер)** — общий: илистые отмели, полосы-«делянки» грязекопов, далёкие фигурки (отдельно), порог в среднем плане. **K2** — от порога за плечом (поза Пелл, наклон над водой — отдельно): край камня и чёрная вода. **K3** — сверху вниз на отстойник: чистая чёрная поверхность для эффекта колец (VFX, один раз).
- **Режимы:** DAWN-EBB (все — пилот). Позже: прилив E2+.
- **Карта:**
```
  [Девятый, сваи]                     Шпиль Шлюза ▲ (вдали, восток-юго-восток)
   ~ ил ~ делянки ~  K1 ● смотрит → на порог
            ███ ПОРОГ ███  K2 ● на пороге, смотрит → в отстойник
                 (●) ОТСТОЙНИК   K3 ● сверху, строго вниз
                       → к морю (ЮЗ)
```
- **Промпт K1:** `Wide view across an exposed canal bed at the lowest ebb: wet grey-brown silt flats with puddles, rows of old timber piles, small marked lanes in the mud; in the middle distance an old stone sluice sill lying bare, mossy and slick, with rusted empty hinge-brackets where gates once hung; beyond the sill a dark pool of perfectly still black water; behind, stilt-houses on piles and, far off, a worn black spiral-grooved tower. {DAWN-EBB}. {STYLE}, {LOC}. {AVOID}`
- **Модели:** K1 — D NB × 6, F NB Pro × 1; K2, K3 — D NB × 2, F NB2 × 1.

## D-05 Колесо-насос Девятого — три колеса над отстойником (в PL-0008)
- **Назначение:** сц. 6 (два колеса ходят, **третье стоит**), сц. 2 (колесо над головой), сц. 19 (колесо останавливается).
- **Облик:** три огромных деревянных колеса-топчака (диаметр ~8 м) в ряд под общей крышей на сваях над отстойником; внутри — планки-ступени; цепи ковшей уходят вниз в чёрную воду; площадка мастера колеса (Корр) у переднего колеса.
- **Ракурсы:** **W1 (мастер)** — сбоку, все три колеса в ряд, третье (дальнее) — пустое и неподвижное. **W2** — из-за спин ходоков внутри колеса. **W3** — снизу, с площадки мастера (для MS Корра).
- **Режимы:** MORNING (пилот); DUSK (сц. 19, edit). Позже: NIGHT-RAIN.
- **Промпт W1:** `Side view of three enormous wooden treadmill wheels standing in a row under one long timber roof on piles over a dark sump pit, each wheel taller than a house with slatted steps inside, chains of wooden buckets descending into black water; the two nearer wheels show motion blur on their slats, the farthest wheel stands still and empty; a small raised platform at the front wheel for the wheel-master. {MORNING}. {STYLE}, {LOC}. {AVOID}`
- **Модели:** W1 — D NB × 6, F NB Pro × 1; W2, W3 — D NB × 2, F NB2 × 1; режим DUSK — D NB × 1, F NB2 × 1.

## D-06 Дом Нан на сваях, интерьер — PL-0019
- **Назначение:** сц. 4 (стол, хлеб, сети, сундук «как будто не важен»), 19–20 (дверь, сундук, лампа, **чаша с водой** — кольца).
- **Облик:** одна низкая комната, тёмное дерево, сети на балках, **сухая полка** под коньком с узлами вещей; стол у окна; **сундук для сетей стоит на полу в углу**; чаша с водой на столе; лампа; дверь и лестница вниз (люк/проём).
- **Ракурсы:** **N1 (мастер)** — от двери на стол и окно (стол в центре, сундук в левом углу на полу). **N2** — обратный: от окна на дверь и угол с сундуком. **N3** — над столом на чашу и окно.
- **Режимы:** MORNING (сц. 4); NIGHT с одной лампой (сц. 20); DUSK (сц. 19). Позже — разрушенный дом (E10).
- **Карта:**
```
   ┌──────── окно (СЗ, на соседние крыши) ────┐
   │          [СТОЛ]  чаша ○  лампа ✦          │
   │ [СУНДУК]                       сети      │
   │  угол                                     │
   └──── ДВЕРЬ (ЮВ, в переулок) ── люк к лестнице ┘
      N1 ● у двери → на стол/окно    N2 ● у окна → на дверь/сундук    N3 ● над столом ↓
```
- **Промпт N1:** `Interior of a poor one-room stilt-house home: low dark timber walls and roof beams hung with fishing nets and floats, a dry-shelf under the roof ridge stacked with wrapped bundles, a rough table by a small window with a grey loaf, a clay water bowl and an oil lamp, three-legged stools, a plain old wooden net-chest with a rope handle standing on the floor in the left corner, worn plank floor, a trapdoor to a ladder near the door. {MORNING}. {STYLE}, {LOC}. {AVOID}`
- **Модели:** N1 — D NB × 6, F NB Pro × 1; N2, N3 — D NB × 2, F NB2 × 1; режимы NIGHT, DUSK — D NB × 1, F NB2 × 1.

## D-07 Картографическая контора, стол — PL-0078
- **Назначение:** сц. 7 (стол, карта, руки картографа, кожаный тубус, вторая копия под пресс-папье). Только стол.
- **Ракурсы:** **M1 (мастер)** — строго сверху на стол (пустой стол под карту: карта — E-05, накладывается). **M2** — низкий ракурс через стол на дверь к винтовой лестнице (переход сц. 7→8).
- **Режим:** NOON (свет из высокого окна).
- **Промпт M1:** `Top-down view of a large cartographer's table of dark polished wood: brass map-weights, a leather blotter at one corner, ink pots, quills, dividers and a ruler, an empty leather map case, the centre of the table clear for a large map. {NOON}. {STYLE}, {LOC}. {AVOID}`
- **Модели:** M1 — D NB × 4, F NB2 × 1; M2 — D NB × 2, F NB2 × 1.

## D-08 Шпиль Короны — PL-0014
- **Назначение:** сц. 8 (основание и внутренняя лестница), 9 (горло короны, Иона спиной; свечение бороздок виток за витком — M3), 16 (тёмный силуэт на закате). **Ассет библиотеки на весь сезон.**
- **Ракурсы:** **S1 (мастер)** — экстерьер с террасы Дворца, снизу вверх, тёмный (не поют). **S2** — тот же, **светящиеся бороздки** (режим «поют»). **S3** — внутренняя лестница: спираль ступеней, бороздки в стенах, световые щели. **S4** — горло короны изнутри, спиной к зрителю смотрим через арку на запад, на гавань (место для фигуры Ионы).
- **Режимы:** S1 — LATE-AFT (пилот), DUSK-силуэт (сц. 16, edit); S3 — LATE-AFT лучи (пилот); S4 — LATE-AFT (пилот). Позже: NIGHT, RAIN, шторм.
- **Карта:**
```
   гавань (З) ←──── S4 ● в горле, смотрит на запад наружу
                ▲ корона: кольцо горл
                ║  S3 ● внутри, смотрит вверх по спирали
   Дворец ──────╨── S1/S2 ● терраса у основания, смотрит вверх
```
- **Промпт S1:** `Low-angle view from a granite palace terrace up the full height of a colossal tower of black glassy stone, about 160 metres tall, its surface wrapped in deep spiral grooves rising clockwise (as seen from above), the top crowned by a ring of tall open arched throats against the sky; the base merges into granite walls and a carved doorway. {LATE-AFT}. {STYLE}, {LOC}. {AVOID}`
- **Промпт S2 (edit от S1):** `Use image 1 exactly. Change only: the spiral grooves now glow from inside with a pale blue-white light, brightest near the crown and fading downward turn by turn, the stone itself stays black, a faint shimmer in the air at the crown. {STYLE}. Avoid: fire, sparks, lightning, rainbow colours, glow outside the grooves.`
- **Промпт S4:** `View from inside one of the open arched throats at the crown of a black glassy stone tower, looking out through the tall arch at a vast harbour far below and the open sea beyond, the arch edges grooved with spirals, wind, open sky, a clear standing place on the stone lip in the centre foreground. {LATE-AFT}. {STYLE}, {LOC}. {AVOID}`
- **Модели:** S1 — D NB × 6, F NB Pro × 1; S3, S4 — D NB × 3, F NB Pro × 1 (ключевой образ сезона); S2 и DUSK — D NB × 1, F NB2 × 1.

## D-09 Гавань Хайуотера сверху — PL-0018 · флагман *Patient Gull*
- **Назначение:** сц. 9 (рябь → **стекло**, мачты замирают, отражение чайки), фон окна в зале (сц. 10–12), окна банка (сц. 13).
- **Облик:** широкая гавань с каменными причалами, маяками-фонарями на молах, флот Корвейнов на якоре; флагман — трёхмачтовый линейный корабль, **синяя полоса по борту**, серебристо-белый баклан на кормовом флаге (герб H-01).
- **Ракурсы:** **H1 (мастер)** — сверху (с короны Шпиля), гавань и флот, рябь. **H2** — тот же план, **режим «стекло»** (edit). **H3** — *Patient Gull* средним планом (лист корабля: борт, корма).
- **Режимы:** LATE-AFT (пилот, оба состояния воды). Позже: шторм, ночь.
- **Промпт H1:** `High bird's-eye view from the top of a tall tower down onto a wide harbour: stone quays and moles with lantern posts, dozens of anchored sailing ships, the largest a three-masted ship of the line with a deep-blue band along its hull, choppy grey-green water with whitecaps and moving swell, gulls. {LATE-AFT}. {STYLE}, {LOC}. {AVOID}`
- **Промпт H2:** `Use image 1 exactly — same ships in the same positions. Change only the water: perfectly flat and mirror-like, no waves, every mast and a gull reflected exactly, the sails hanging still. {STYLE}. {AVOID}`
- **Модели:** H1 — D NB × 6, F NB Pro × 1; H2 — F NB2 × 1 (+1 D); H3 — D NB × 3, F NB2 × 1.

## D-10 Зал десятины в Сухом дворце — PL-0009
- **Назначение:** сц. 10–12 (вход Руэла, рукопожатие, чаша, чтение карты, падение). Восемь мест — блоками цвета (C-06).
- **Облик:** высокий зал из светлого гранита, **помост** с **картографическим столом** у **высокого окна на гавань** (запад), восемь мест полукругом под восемью знамёнами, галерея сверху, двустворчатая дверь в противоположном конце.
- **Ракурсы:** **T1 (мастер)** — с галереи (сверху, со стороны двери) на помост и окно: восемь блоков полукругом. **T2** — уровень глаз у стола: стол, окно с гаванью позади (контражур). **T3** — от помоста на дверь (вход Руэла, «зал поворачивается к нему»).
- **Правило 180°:** ось действия — стол (Лукан) ↔ дверь. Окно всегда **за** Луканом в T2; Руэл входит из T3.
- **Режимы:** LATE-AFT (сц. 10–11), «last light» (сц. 12: DUSK-переход, низкое красное солнце в окне); после падения — тот же план, пыль в луче (VFX).
- **Карта:**
```
            ОКНО на гавань (З) — низкое солнце
          ┌──── [ПОМОСТ: СТОЛ КАРТЫ] ────┐   T2 ● у стола, смотрит на окно/вдоль стола
          │  1  2  3  4 | 5  6  7  8    │   места полукругом под знамёнами
          │                              │
   галерея T1 ● (сверху, от двери → к окну)
          └──────────── ДВЕРЬ (В) ───────┘   T3 ● у помоста, смотрит на дверь
```
- **Промпт T1:** `High view from a stone gallery into a tall council hall of pale granite: at the far end a raised dais with a long map table in front of a tall arched window overlooking a harbour, eight seating places in a wide semicircle before the dais each under a tall vertical cloth banner of a different colour (cool white, deep blue, rust red, sea green, slate grey with yellow, black with copper, undyed linen, ochre), polished floor, the hall empty of people. {LATE-AFT}. {STYLE}, {LOC}. Avoid: text on banners, throne, crown, people. {AVOID}`
- **Модели:** T1 — D NB × 6, F NB Pro × 1; T2, T3 — D NB × 2, F NB2 × 1; режим «last light» — D NB × 1, F NB2 × 1.

## D-11 Счётный зал Лантри и ступени снаружи — PL-0011
- **Назначение:** сц. 13–16 (ряды пюпитров, высокий стол Урсулы, клетка с эхо-камнем на стене, стаканы воды; ступени над городом на закате).
- **Облик:** чёрный камень, медные двери, **войлочный пол**, ряды **стоячих пюпитров** в глубину, клерестори-окна (на запад: видны Шпиль Короны и гавань), высокий стол в конце, **медная клетка с эхо-камнем на стене**, колокол вечернего счёта, весы над дверью.
- **Ракурсы:** **L1 (мастер)** — вдоль рядов в глубину (повторяемая глубина «сорок спин»). **L2** — на высокий стол и стену с клеткой. **L3** — ступени снаружи над городом, на запад (= D-01 B).
- **Режимы:** LATE-AFT (сц. 13–14, Шпиль Короны светится в окнах), «к вечеру» (сц. 15), DUSK (сц. 16).
- **Промпт L1:** `Long view down a great silent counting hall of black stone: rows and rows of identical tall standing desks receding into depth, each with an open ledger and a small glass of water, a felt-covered floor, high clerestory windows letting in warm light, copper fittings, a high desk at the far end, a small brass cage with a dark stone mounted on the far wall. {LATE-AFT}. {STYLE}, {LOC}. {AVOID}`
- **Модели:** L1 — D NB × 6, F NB Pro × 1; L2 — D NB × 2, F NB2 × 1; режимы «к вечеру», DUSK — D NB × 1, F NB2 × 1 каждый. L3 = D-01 B (не дублируем).

## D-12 Дом Слушания, комната ретрансляции — PL-0012
- **Назначение:** сц. 17 (стена клеток с эхо-камнями, все звенят; Одо останавливает камень пальцем).
- **Облик:** узкая высокая каменная комната под башней-ретранслятором; **стена железных клеток-гнёзд** с камнями (сетка 8×6), конторка дежурного, ячейки-«голубятни» для записок, узкое окно.
- **Ракурсы:** **R1 (мастер)** — фронтально на стену камней. **R2** — от стены на дверь и конторку дежурного.
- **Режим:** DUSK + лампа.
- **Промпт R1:** `Interior of a narrow tall stone relay room: one whole wall is a grid of small wrought-iron cradles, each holding a dark glassy stone, a keeper's slanted writing desk with a logbook, walls of pigeon-hole slots full of paper slips, a single narrow window with dusk light and one oil lamp. {DUSK}. {STYLE}, {LOC}. Avoid: glowing stones, people. {AVOID}`
- **Модели:** R1 — D NB × 4, F NB2 × 1; R2 — D NB × 2, F NB2 × 1.

---

# E. Предметы и документы — 12

Первые пять — **предметы саги** (фиксируются на 12 сезонов). Все предметы — на `{SHEET}`-фоне, без рук, если не указано.

## E-01 Камень на шнурке (Pell's stone) — M-SHD
- **Назначение:** сц. 3, 4, 19, 20 (макро, M5). Облик фиксируется на всю сагу.
- **Виды:** фронт, профиль (толщина), на шнурке в рост, в ладони (масштаб — **не больше ногтя большого пальца**), под лампой (сц. 20, без свечения).
- **Промпт:**
```
Prop reference sheet: a tiny piece of black glassy stone no bigger than a thumbnail, irregular, with one clean crack running across its face, dull sheen with a faint cold blue-grey highlight, hanging from a rotted, frayed, knotted dark cord. Views in a row: front, side showing thickness, back, the stone on its cord at full length, and the stone resting in the palm of a small mud-stained hand for scale. {STYLE}, {SHEET}. Avoid: glow, magical light, gem facets, polished jewellery, metal setting, chain, pearl, round shape, sparkles, text, photorealism.
```
- **Правило:** **свечения нет никогда** — гул показывается дрожью и кольцами на воде. **Никогда** не подаётся в одну генерацию вместе с E-02 и с листами Руэла.
- **Модели:** D — NB × 4 · F — NB Pro × 1.

## E-02 Перстень Руэла с чёрной жемчужиной — M-RNG
- **Назначение:** сц. 10–12 (одна вставка: жемчужина у костяшки Хелма; рука над чашей — левая).
- **Виды:** на левой руке (тыльная сторона), сам перстень: фронт, сбоку, сверху. **Закрытый.** Другие состояния перстня — по запросу режиссёра к нужной серии, не в пилоте.
- **Промпт:**
```
Prop reference sheet: a heavy old silver ring set with one large round black pearl with a deep lustrous sheen, the pearl held in a sculpted silver setting with a small visible hinge at one side, worn and polished by age. Views in a row: the ring on the ring finger of a big weathered LEFT hand seen from the back of the hand, the ring alone from the front, from the side showing the hinge, from above. {STYLE}, {SHEET}. Avoid: open pearl, visible interior, gemstones, gold, right hand, cord, stone fragments, text, photorealism.
```
- **Модели:** D — NB × 4 · F — NB Pro × 1.

## E-03 Латунный зажим для гроссбуха (ledger-clip) — M-CLP
- **Назначение:** сц. 15–16; предмет саги (у Холлиса до S6, затем расплавленная версия — по досье).
- **Дизайн (фиксирую):** латунный зажим ~9 см; **головная пластина — несимметричный щиток**: ровное коромысло весов (знак Лантри) над **тремя волнистыми линиями**, на левом конце коромысла — **маленькая зарубка-клин**, внизу справа — **выбитый номер клерка «117»** (зеркально не нужен: оттиск пластины в сургуче даёт зеркальную цифру — этим и узнаваем); край пластины с **косым срезом** в правом нижнем углу. Пружинный язык под пластиной. Дизайн рассчитан на то, чтобы и зажим, и его оттиск узнавались по силуэту щитка (косой срез + зарубка) даже без цифр.
- **Виды:** фронт, сбоку, сзади (пружина), в левом нагрудном кармане (масштаб), **оттиск в красном сургуче**. Зажим и оттиск асимметричны — **отражением не исправлять**.
- **Позже (не в смете пилота):** расплавленная версия к S6 — edit от финала («the same clip half-melted, brass sagging, the shield outline and the diagonal cut still recognisable»).
- **Промпт:**
```
Prop reference sheet: a small brass ledger-clip about nine centimetres long, a spring clip with a flat head plate shaped like an asymmetric shield with one corner cut off diagonally at the lower right; embossed on the plate a perfectly level balance beam above three wavy lines, a small wedge-shaped notch on the left end of the beam, and the small stamped number 117 near the lower right; warm yellow brass slightly worn at the edges. Views in a row: front, side, back with the spring tongue, clipped in the breast pocket of a light ash-grey coat, and its impression pressed into a blob of red sealing wax. {STYLE}, {SHEET}. Avoid: copper colour, gold shine, gems, symmetrical shield, tilted balance, extra text, photorealism.
```
- **Модели:** D — NB × 4 · F — NB Pro × 1. Цифры проверить; если «117» испорчено — правка edit-ом, не перегенерация.

## E-04 Серебряный камертон Ионы — M-FRK
- **Назначение:** сц. 8–9 (удар о костяшку, к кости за ухом). С S4E12 — у Пелл на поясе.
- **Промпт:**
```
Prop reference sheet: a small slender silver tuning fork about ten centimetres long with two parallel tines and a short round stem ending in a tiny loop, hanging on a fine silver chain as a pendant; a faint engraved line pattern on the stem. Views: front, side, on its chain, held between two fingers being struck lightly on a knuckle. {STYLE}, {SHEET}. Avoid: gold, gems, spiral ornaments, large size, musical notes, glow, text, photorealism.
```
- **Модели:** D — NB × 3 · F — NB Pro × 1.

## E-05 Карта десятины (мастер) и малая копия — M-MAP
- **Назначение:** сц. 7 (подкрашивание тиров, подписи появляются), 10, 12 (сползает и сворачивается **неподписанной**). Это «доска фанатов» — **мастер-файл, перерисовывается каждый сезон**.
- **Метод (экономия и точность):** AI делает только **живописную основу** без подписей: дельта, Хайуотер, Шпили, береговая линия, картуш без текста, компас-роза (спираль по часовой — знак Инчли). **Подписи, четыре тинта тиров (First Song, Second Song, Last Song, бледная заливка внизу легенды), цвета держателей Шпилей** — векторными слоями на монтаже (бесплатно, читаемо на телефоне, правится к каждому сезону). Малая копия — edit от финала (та же береговая линия, меньший лист, грубее).
- **Промпт (основа):**
```
A large hand-drawn antique map on heavy cream parchment of a wide river delta and barrier islands at the mouth of a great river: a central granite hill city, branching canals, reed islands, polders behind dikes, a line of sandbar islands offshore, a drowned area of shallow sea marked only by faint wave lines, nine small black tower symbols placed across the land, an ornamental compass rose drawn as a spiral of fine ink lines turning clockwise from the centre, an empty decorative cartouche and an empty legend box with four empty swatches, no writing anywhere. Top-down, flat, evenly lit. {STYLE}. Avoid: any text, letters or labels, real-world coastlines, signature, seal, photorealism.
```
- **Правило:** на карте **нет подписи Хелма и печати** в пилоте.
- **Модели:** D — NB × 4 · F — NB Pro × 1 · малая копия — F NB2 × 1.

## E-06 Гобелен «Разлом» (панели)
- **Назначение:** сц. 5 (камера скользит, внутри ткани анимации нет). Стиль **тканый**, плоский — он же стиль всех будущих «Летописей».
- **Расхождение источников (вопрос режиссёру и сценаристу):** поэпизодник v1.1 даёт 5 панелей (1 — Шпили встают из моря; …; 4 — девять знамён **и** парус-баклан вместе), выдержка хранителя (канон v0.4) — 6 панелей с другим порядком. **Делаю по выдержке хранителя** (это закрытый канон); панель «Шпили встают из моря, строителей нет» из поэпизодника — как необязательная **панель 0**, если сценарист её сохранит.
- **Стилевой мини-тест ткани:** 4 черновика NB на панели 1 (тканый рисунок, 4–6 цветов нити, видимое переплетение, выцветшая ткань, бордюр со спиралями по часовой). Утверждённый финал панели 1 = референс стиля для остальных.
- **Общий блок `{WEAVE}`:** `flat medieval-style woven tapestry, visible warp and weft threads, limited palette of six faded wool and silk thread colours (pearl, deep teal, indigo, madder red, ochre, black), stylised flat figures without perspective, a woven border of small spiral shells turning clockwise from the centre outward, aged and slightly faded textile, evenly lit, flat front view`
- **Панели** (по выдержке; в маркетинге разрешены только 1, 2, 5):

| № | Содержание (фиксировано) | Промпт (англ.) | Где можно |
|---|---|---|---|
| (0) *необяз.* | Шпили встают из моря; строителей нет | `{WEAVE}. Black towers rising out of a stylised sea, waves around their bases, no people, no builders, no hands.` | внутри серии |
| 1 | Королева Невэ поёт; **за ней толпы** с открытыми ртами | `{WEAVE}. A queen in pearl and teal robes with a spiral-shell circlet, standing and singing with her right hand raised, and behind her great crowds of common people with open mouths, rows upon rows, filling the panel.` | маркетинг ✔ |
| 2 | Девять семей-хранителей, основание Конкорда (официальная версия) | `{WEAVE}. Nine noble figures standing in a row on a shore, each beneath a tall vertical banner with a flat emblem (cormorant, sickle, open hand, eel in a ring, harrow, waterfall, gate, spade and reed, lantern tower), raising their hands in an oath.` — детали оружия и знамён **на сверку хранителю** | маркетинг ✔ |
| 3 | Крупно: **чёрная жемчужина на поющей руке** Королевы | `{WEAVE}. A close woven detail of a raised woman's hand, open, with a ring bearing one black pearl, sleeve of pearl and teal.` | **только в серии** |
| 4 | Служанка с **косой слева** и **спиральной раковиной**; **кулак сжат** | `{WEAVE}. A slight servant girl half hidden behind a pillar, one long braid on her own left side, holding a spiral seashell against her chest with one arm, her other hand clenched in a closed fist.` | **только в серии** |
| 5 | **Парус с бакланом** поперёк гавани — корабли **в море** | `{WEAVE}. Ships at sea across a harbour mouth, the largest sail bearing a black diving cormorant, the ships out on the water, no shore, no people ashore.` | маркетинг ✔ |
| 6 | Королева поёт **одна на вершине Шпиля**; толпа внизу **уже лежит** | `{WEAVE}. A queen alone at the very top of a tall black tower, singing, nobody beside her, and far below at the foot of the tower the crowd lying fallen, stylised and still, the sea rising behind.` | **только в серии** |

- **Чего на гобелене нет (проверять):** что в кулаке у служанки; открытой жемчужины; руки Королевы у перстня; кого-либо рядом с Королевой на вершине (ни адмирала, ни моряков на берегу); лодки, уходящей из города; Феннике и Лантри среди знамён. Жемчужина и кулак — **в разных панелях**. Новые фигуры — только после проверки хранителем.
- **Модели:** стиль-тест D NB × 4; каждая панель — D NB × 3, F NB Pro × 1 (edit с финалом панели 1 как стилевым референсом).

## E-07 Чаша десятины
- **Промпт:** `Prop reference sheet: a ceremonial silver cup on a short stem, wide shallow bowl, plain band of engraved wave lines around the rim, polished and old. Views: front, three-quarter, top-down showing the inside empty, and on a dark wooden table for scale. {STYLE}, {SHEET}. Avoid: gems, gold, pearls, text, photorealism.`
- **Модели:** D — NB × 2 · F — NB2 × 1.

## E-08 Ящик сборщика на цепи
- **Промпт:** `Prop reference sheet: a small iron-bound wooden collection box with a coin slot and a padlock, a short iron chain ending in a cuff, slate-grey paint with a single sulphur-yellow stripe across the lid. Views: front, side, the cuff closed on a man's left wrist with the box hanging. {STYLE}, {SHEET}. Avoid: emblems, text, gold, photorealism.`
- **Модели:** D — NB × 2 · F — NB2 × 1.

## E-09 Сундук для сетей
- **Назначение:** сц. 4, 19–20; позже E3, E7, E11 (тайник). Должен выглядеть **неважным**.
- **Промпт:** `Prop reference sheet: a plain old wooden chest for fishing nets, low and long, dark weathered planks, a thick rope handle at each end, a simple iron hasp without a lock, salt stains, a coil of net spilling from the half-open lid. Views: front, three-quarter, lid open showing nets inside, and from above. {STYLE}, {SHEET}. Avoid: carvings, ornaments, treasure, metal corners, emblems, text, photorealism.`
- **Модели:** D — NB × 2 · F — NB2 × 1.

## E-10 Колыбель (сц. 1)
- **Назначение:** первый кадр сериала (M1); зеркальный образ в E10. **На колыбели нет узла** (никаких завязанных верёвок, бантов, лент).
- **Промпт:** `Prop reference sheet: a small woven-reed and wood baby cradle with a rounded hood, simple and poor, a folded worn blanket inside, empty, no rope, no ties, no knots, no ribbons. Views: front three-quarter, side, from above, and floating on black water at night lit by one lantern. {STYLE}, {SHEET}. Avoid: knots, rope, ribbons, baby, toys, ornaments, text, photorealism.`
- **Приёмка:** отсутствие любого узла — обязательный пункт.
- **Модели:** D — NB × 3 · F — NB Pro × 1 (ключевой кадр сериала).

## E-11 Эхо-камень в клетке (лицензированный)
- **Назначение:** сц. 16 (стена Счётного зала), 17 (стена ретрансляции). Должен **явно отличаться** от камня Пелл: крупнее (с кулак), обработанная огранка, в медной/железной клетке, без трещины, без шнура.
- **Промпт:** `Prop reference sheet: a fist-sized cut stone of black glassy rock with smooth worked facets, set in an ornate brass cage mounted on a wall bracket; a small hanging tag plate (blank). Views: front, side, a wall of identical iron cradles with such stones in a grid. {STYLE}, {SHEET}. Avoid: glow, cracks, cords, tiny size, text, photorealism.`
- **Модели:** D — NB × 2 · F — NB2 × 1.

## E-12 Два листа гроссбуха (ACCOUNT NINE; 1,470 / 1,740)
- **Назначение:** сц. 13–14. Цифры **1,470** и **1,740** должны читаться на телефоне по секунде каждая.
- **Метод:** AI делает **пустые разворотные листы** с линовкой и почерком-«шумом» без цифр; заголовок **ACCOUNT NINE** и обе цифры накладываются на монтаже (бесплатно, гарантированно читаемо и одинаково во всех кадрах).
- **Промпт:** `Prop reference: an open ledger book seen from above, two cream pages with ruled columns in faded red and blue ink, neat handwritten-looking ink scribbles that are illegible and contain no real letters or numbers, one heading line left blank at the top of the left page, two clear empty boxes for a carried figure at the bottom of the left and right pages, an ivory page-turning blade lying across the gutter. {STYLE}. Avoid: readable text, real numbers, letters, photorealism.`
- **Модели:** D — NB × 2 · F — NB2 × 2 (лист Холлиса и лист Фоссетта — edit от первого).

---

## F. Чек-лист приёмки референса (дополнение к `consistency.md` §6)
- [ ] Стороны всех асимметричных деталей (коса, серьга, кольцо, трещина стекла, вихор, культя, брошь, шрам, шлем под рукой).
- [ ] Спирали — по часовой от центра.
- [ ] Нет серёг-спиралей ни у кого, кроме Нан (одна, левое ухо).
- [ ] Камень Пелл и перстень Руэла — не на одном изображении, не в одной генерации.
- [ ] Нет свечения у камня Пелл; свечение — только у бороздок Шпилей.
- [ ] Цвета домов — по плашкам (`peoples_and_costume.md` §3), опасные пары различимы.
- [ ] Нет текста (кроме «IX» на бирке и «117» на зажиме).
- [ ] Записаны промпт, модель, seed, дата, стоимость в `card.md`.
