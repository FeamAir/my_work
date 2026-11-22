# Шот-лист · «Бумажный кит» · ep01 «Кит над крышами»

Версия 1.0 · 2026-11-22 · автор: режиссёр-постановщик
Основа: `studio/story/ep01_script.md` v1.0 · шаблон `shotlist_template.md` · референсы `references.md` · звук `studio/sound/*`
Статус: **план, генерация не запускалась.**

## Сводка

| Параметр | Значение |
|---|---|
| Хронометраж | **2:45.0** (165 с) = сценарий ~2:45, сцены совпадают с таймкодами сценария |
| Кадров | **42** (41 генерируемый + 1 титр на монтаже) |
| Средняя длина кадра | 4,0 с (диапазон 2–5 с) |
| Формат | 16:9, целевое 1080p |
| Реплик | 17 (+ одна реплика Гэна разбита на 2 кадра) |
| Синхронная речь (липсинк) | **0 кадров** — липсинк в пилоте не нужен |
| Речь «в кадре, без синка» | 3 реплики: дальний / общий снизу / профиль на среднем |
| Закадр (ЗК) | 14 реплик, из них 3 — говорящий в кадре спиной |
| Видео: модели | MiniMax H3 Max Turbo — 20, Kling 2.5 Turbo Pro — 16, Kling 3 Pro — 5 |
| Ключевые кадры | Nano Banana 2 — 36 (+1 конечный кадр), Nano Banana — 5 |
| Смета (повторяющиеся затраты) | **≈ $33** с резервом 20% · разово референсы ≈ $16–19 · итого ≈ **$50** (см. конец файла) |

## Условные обозначения

- **TC** — таймкод от начала серии, `ММ:СС` (начало–конец кадра). Таймкоды реплик (`≈`) — оценка до синтеза речи (≈ 12–15 символов/с); после TTS звукорежиссёр присылает фактические длительности, кадры подрезаются в пределах «ручек» 5-секундных клипов.
- **Речь:** `—` — реплики нет; `ЗК` — говорящего нет в кадре; `ЗК (спиной)` — говорящий в кадре, рот не виден; `в кадре, без синка` — рот виден мелко (дальний/общий план или профиль), используется общее движение рта из промпта движения, липсинк не применяется. **`СИНХ` (липсинк) в пилоте не используется.**
- **Модели:** NB = Nano Banana, NB2 = Nano Banana 2 (edit/multi-reference), MM = MiniMax H3 Max Turbo, K25 = Kling 2.5 Turbo Pro, K3 = Kling 3 Pro. В скобках — референсы (файлы из `refs/`, `references.md`).
- **Промпты:** `{SORA}`, `{NATSU}`, `{GEN}`, `{BIKE}`, `{WHALE_FAR}`, `{WHALE_DETAIL}`, `{LOC_…}`, `{PROP_…}` раскрываются в ID-блоки из `references.md`; световой режим (`SUNSET`/`DUSK`/`NIGHT`/`INT_DUSK`) — в строку из `references.md` §3; в конец автоматически добавляются акцент сцены, базовый стилевой промпт и негатив (visual_bible §10–12). К вставкам с конвертами/табличками — текстовый негатив (`references.md` §0.3). К промпту движения — базовый промпт движения (§11).
- **Колонка «Сцена» шаблона** вынесена в шапку сцены (таблицы разбиты по сценам), вместо неё добавлены колонки TC и «Речь».
- **Текст на монтаже** (решение директора): все штемпели, адреса, «14», «Соре», титр — накладываются на монтаже. Кадры с надписями сняты **статичной камерой**, предмет развёрнут к камере плоско — чтобы наложение не требовало трекинга.
- Ось и ракурсы: Сора по умолчанию **лицом влево по кадру** (видна косичка у левого виска), Нацу и Гэн — **лицом вправо** (видны прядь/серёжка Нацу, часы Гэна). Кит плывёт **справа налево**, к камере левым боком. Ветер дует слева, шарф Соры летит вправо.

---

## Сцена 1. Крыша почтового дома — закат · 00:00–00:25

```
Эпизод: ep01 · Сцена: sc01 · Локация: LOC_L2 (крыша) · Время суток: закат (SUNSET)
Персонажи: {SORA} · В кадре одна; смотрит влево по кадру, на горизонт
Акцентный цвет сцены: киноварь #D9482B (шарф) · Настроение: тихое, одинокое, тёплое
Хронометраж сцены: 25 с (00:00–00:25) · Вход: из чёрного, первая нота эмбиента
```

| № | TC | Длит. | План | Камера | Действие | Реплика / звук | Речь | Промпт ключевого кадра | Промпт движения | Модель | Статус |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sc01-sh010 | 00:00–00:05 | 5 с | establishing WS, без персонажей | чуть сверху, медленная панорама слева направо, параллакс | Склон Каминосаки: черепичные крыши спускаются к бухте, маяк справа, ветер колышет бельё | Эмбиент: ветер, хлопанье белья, далёкие чайки; музыка: тихое вступление (L4 «Тайна»/тема) | — | `wide establishing shot, slightly high angle from a hillside roof, {LOC_L2} view downhill over many tiled rooftops in dark blue and terracotta to a calm bay, small white lighthouse on a cape on the right, laundry lines fluttering between houses, SUNSET, no people` | `very slow horizontal pan from left to right with gentle parallax between rooftop layers, laundry flutters in the wind, the sea glitters softly, a few distant birds glide` | NB (L2_wide_downhill) → MM | план |
| sc01-sh020 | 00:05–00:10 | 5 с | WS | eye-level, static | Сора сидит на черепице у трубы, поджав колени, складывает журавлика; шарф развевается | Сора ЗК ≈00:05.5–00:13.0: «Говорят, если сложить тысячу журавликов, можно сказать то, что не получается сказать вслух.» | ЗК | `wide shot, eye level, {SORA} sitting on dark blue roof tiles next to an old red-brick chimney on the left, knees drawn up, three-quarter view facing left, folding a small yellow paper crane in her lap, red scarf ends fluttering to the right, the town and the bay below in the background, {LOC_L2}, SUNSET` | `red scarf ends and hair flutter in the wind from the left, her hands make small folding movements, laundry far below sways gently, camera static` | NB2 edit (SORA 03_three_quarter, 01_turnaround; L2_wide_downhill) → MM | план |
| sc01-sh030 | 00:10–00:13 | 3 с | ECU insert | eye-level, static | Пальцы Соры загибают крыло журавлика | ЗК продолжается; шелест бумаги (фоли) | ЗК | `extreme close-up insert, a girl's hands with sleeves of an oversized mustard-yellow knit cardigan at the wrists, folding the wing of a small yellow paper crane, five clearly separated fingers on each hand, warm sunset side light from the left, softly blurred dark blue roof tiles behind` | `the fingers slowly press and fold the paper wing down in one gentle motion, the paper bends slightly, camera static` | NB2 edit (SORA 08_props; sh020 kf) → K25 | план |
| sc01-sh040 | 00:13–00:17 | 4 с | CU insert, без персонажей | eye-level, медленный наезд | Ряд журавликов на трубе под камешками; новый жёлтый — с краю | Ветер, лёгкий трепет бумаги | — | `close-up insert, {PROP_CRANES} on top of an old red-brick chimney, the newest yellow crane at the right end of the row, a small red ribbon tied around the chimney, blurred rooftops and sunset sky behind, SUNSET` | `the paper cranes tremble slightly in the wind, the red ribbon flutters, slow push-in` | NB edit (PROP_CRANES; L2_chimney_mid) → MM | план |
| sc01-sh050 | 00:17–00:21 | 4 с | MCU | eye-level, static | Сора, положив подбородок на колени, смотрит на горизонт | Пауза в речи; ветер | — | `medium close-up, eye level, {SORA} three-quarter view facing left, chin resting on her knees, looking at the distant horizon, quiet thoughtful expression, mouth closed, warm sunset key light from the left, thin vermilion rim light on her hair, softly blurred sky and rooftops behind, {LOC_L2}, SUNSET` | `she blinks slowly once, hair, the thin braid and the scarf move gently in the wind, natural breathing, camera static` | NB2 edit (SORA 03; sh020 kf) → K25 | план |
| sc01-sh060 | 00:21–00:25 | 4 с | CU insert | eye-level, static | Порыв ветра приподнимает жёлтого журавлика, рука Соры прижимает его камешком | Порыв ветра (DES); Сора ЗК ≈00:21.3–00:24.9: «У меня их уже сто двенадцать. А сказать всё ещё нечего.» | ЗК | `close-up insert, top of an old red-brick chimney with a row of small paper cranes held by pebbles, the yellow crane at the end tilting up in a gust of wind, a girl's right hand in a mustard-yellow cardigan sleeve holding a small grey pebble just above its tail, SUNSET` | `the yellow crane lifts slightly in the gust, the hand sets the pebble on its tail and the crane settles, the other cranes tremble, camera static` | NB2 edit (sh040 kf; SORA 08_props) → K25 | план |

Склейка в сц. 2 — прямая.

---

## Сцена 2. Улица Ступеней — закат · 00:25–00:45

```
Эпизод: ep01 · Сцена: sc02 · Локация: LOC_L3 (улица Ступеней) + LOC_L2 (вид с крыши) · Время: закат (SUNSET), фонари только что зажглись
Персонажи: {NATSU} {BIKE}, {SORA} · Ось: Нацу внизу, слева по кадру, смотрит вверх-вправо; Сора на крыше, справа, смотрит вниз-влево
Акцентный цвет сцены: золото фонаря #E9A93B · Настроение: лёгкое, бытовое → тревога
Хронометраж сцены: 20 с (00:25–00:45)
```

| № | TC | Длит. | План | Камера | Действие | Реплика / звук | Речь | Промпт ключевого кадра | Промпт движения | Модель | Статус |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sc02-sh010 | 00:25–00:30 | 5 с | WS | нижний ракурс вверх по лестнице, static | Нацу поднимается по пандусу, ведёт голубой велосипед с газетами; очки на лбу | Шаги, тиканье спиц велосипеда, эмбиент улицы; музыка: L5 «Быт» коротко | — | `wide shot, low angle looking up a stone staircase street, {LOC_L3}, {NATSU} walking her {BIKE} up the smooth ramp on the right side of the steps toward the camera, three-quarter view, at the top of the street the post house roof against the sunset sky, street lamps glowing faintly, SUNSET` | `she walks slowly up the ramp pushing the bicycle, the wheels turn, laundry sways above the street, camera static` | NB2 edit (NATSU 03; BIKE 08_props; L3_up_from_below) → K25 | план |
| sc02-sh020 | 00:30–00:33 | 3 с | WS, верхний ракурс (POV с крыши) | сверху вниз, static | Нацу остановилась внизу, задрала голову и кричит, приставив ладонь ко рту | Нацу ≈00:30.3–00:32.8 (громко, насмешливо): «Эй, Почтовая! Опять журавлей пасёшь?» | в кадре, без синка (дальний план, рот прикрыт ладонью) | `high angle wide shot from a roof edge looking down at a stone staircase street, dark blue roof tiles and the fluttering end of a red scarf in the bottom right foreground, {NATSU} small in the street below standing next to her {BIKE}, looking up toward the camera, calling out with one hand raised beside her mouth, {LOC_L3}, SUNSET, long warm shadows` | `she calls upward with a lively gesture, small mouth movement, the scarf end flutters in the foreground, camera static` | NB2 edit (NATSU 01; L3_down_from_roof) → MM | план |
| sc02-sh030 | 00:33–00:36 | 3 с | MS-WS, нижний ракурс | снизу вверх, static | Сора на краю крыши, справа, лениво машет рукой, не улыбаясь | Сора ≈00:34.4–00:34.9 (спокойно): «Пасу.» | в кадре, без синка (общий снизу, одно слово) | `medium wide shot, low angle from the street, {SORA} sitting at the edge of the dark blue tiled roof of an old house in the right part of the frame, looking down to the left, raising one hand in a lazy wave, calm unsmiling face, red scarf fluttering against the peach-orange sunset sky, {LOC_L2}` | `she waves her hand once lazily, the scarf and hair flutter, camera static` | NB2 edit (SORA 03; L2_from_street) → MM | план |
| sc02-sh040 | 00:36–00:40 | 4 с | MCU | лёгкий нижний ракурс, static | Нацу хмыкает, усмешка гаснет: на лицо наползает огромная тень | Тихо: «гул» приближения (DES, низкий); эмбиент приглушается | — | `medium close-up, slight low angle, {NATSU} three-quarter view facing right, looking up to the right, a half-amused smirk, hands out of frame, warm sunset light on her face, the upper part of the frame starting to darken with the soft edge of a huge shadow, {LOC_L3}, SUNSET` | `a vast soft shadow slowly slides down over her face, the warm light dims, her smirk fades and she freezes, eyes widening slightly, camera static` | NB2 edit (NATSU 03; L3_up_from_below) → K25 | план |
| sc02-sh050 | 00:40–00:45 | 5 с | WS, без персонажей | eye-level вверх по улице, static | Огромная тень сползает по ступеням, фонари один за другим мигают | Потрескивание фонарей (HARD) с 00:40.5; Нацу ЗК ≈00:41.8–00:43.0 (растерянно, тише): «…Это ещё что?» | ЗК | `wide shot, eye level looking up a stone staircase street, {LOC_L3}, an enormous soft shadow covering the upper half of the empty street, cast-iron street lamps glowing warm yellow, fading sunset light, no people` | `the huge shadow slides slowly down the steps toward the camera, the street lamps flicker one after another from top to bottom, laundry sways, camera static` | NB (L3_up_from_below) → MM | план |

Склейка в сц. 3 — прямая, на звуке кита.

---

## Сцена 3. Небо над городом — закат · 00:45–01:15

```
Эпизод: ep01 · Сцена: sc03 · Локация: LOC_L5 (небо) + LOC_L2 (крыша) · Время: закат (SUNSET)
Персонажи: {WHALE_DETAIL}/{WHALE_FAR} (состояние ep01-A: прорехи A, B, C открыты), {SORA} · Кит плывёт справа налево
Акцентный цвет сцены: киноварь #D9482B (глаза-штемпели) · Настроение: благоговение, тревога
Хронометраж сцены: 30 с (00:45–01:15) · Кульминация серии №1
```

| № | TC | Длит. | План | Камера | Действие | Реплика / звук | Речь | Промпт ключевого кадра | Промпт движения | Модель | Статус |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sc03-sh010 | 00:45–00:50 | 5 с | WS, нижний ракурс | снизу, медленный подъём камеры (tilt up) | Из-за крыш выплывает край плавника, покрытый марками | Низкий гул, шелест бумаги нарастает; музыка: L4 «Тайна» | — | `low angle shot, {LOC_L5} rooftops and chimneys along the bottom edge, the tip of a giant pectoral fin covered in invented postage stamps like scales rising slowly from behind the roofs on the right, {WHALE_DETAIL}, peach-orange sunset sky, warm light glowing through the paper, SUNSET` | `the stamp-covered fin rises slowly from behind the rooftops and glides to the left, camera tilts up slowly, stamps ripple slightly like scales, wires sway` | NB2 edit (whale 12_fin_stamps; L5_low_sunset) → K3 | план |
| sc03-sh020 | 00:50–00:55 | 5 с | MS (фрагмент кита) | снизу, static | Бок кита — сотни пожелтевших листов, строчки чужого почерка — скользит через кадр | **Песня кита №1** (мощно, тревожно) ≈00:51–00:58 | — | `medium shot from below, the left flank of a giant paper whale filling the frame, {WHALE_DETAIL}, hundreds of overlapping yellowed letter sheets with illegible handwriting lines, sunset light glowing through the paper, the large torn hole right behind the left pectoral fin is open, SUNSET` | `the whale's flank glides slowly from right to left across the frame like a ship, paper sheet edges ripple gently, light flickers through thin spots, camera static` | NB2 edit (whale 10_master_detail_flank) → K25 | план |
| sc03-sh030 | 00:55–00:59 | 4 с | ECU | static, очень медленный наезд | Глаз кита — круглый красный штемпель — мягко загорается изнутри | Песня кита продолжается; тихий «звон» загорания (DES) | — | `extreme close-up, the eye of a giant paper whale, a round red postmark seal with concentric rings and wavy cancellation lines and no text, set into faceted yellowed paper folds, unlit, warm sunset light, {WHALE_DETAIL}` | `the red seal slowly lights up from within with a soft warm glow, the paper folds around it shift very slightly, very slow push-in` | NB2 edit (whale 11_eye) → K25 | план |
| sc03-sh040 | 00:59–01:04 | 5 с | establishing EWS | static, лёгкий параллакс | Кит над всем городом, закрывает полнеба; свет просвечивает бумагу; видны тёмные прорехи | Песня кита — пик; музыка вырастает | — | `extreme wide establishing shot, a small town of tiled roofs on a hillside above a calm bay, {WHALE_FAR} floating above the town and covering half of the sky, peach-orange sunset light glowing through its paper body, small white lighthouse on the right, SUNSET` | `the whale drifts very slowly from right to left, its tail fin sways gently, a few single sheets drift down from its belly, clouds move slowly, slight parallax between rooftops and sky` | NB2 edit (whale 00_master_far, 02_far_sunset_silhouette; L2_wide_downhill) → K3 | план |
| sc03-sh050 | 01:04–01:08 | 4 с | MS, нижний ракурс | снизу, лёгкий tilt up за героиней | Сора медленно встаёт на крыше; шарф и косичка развеваются | Сора ЗК ≈01:05.0–01:06.8 (шёпотом, заворожённо): «Кит. Из бумаги.» | ЗК | `medium shot, low angle, {SORA} on dark blue roof tiles next to a red-brick chimney, three-quarter view facing left, half-risen from sitting, looking up in awe, lips slightly parted, red scarf ends and the thin braid at her left temple fluttering in the wind, a huge pale paper shape filling the upper left sky, {LOC_L2}, SUNSET` | `she slowly rises to her feet while looking up, scarf and hair flutter in the wind, camera tilts up slightly following her` | NB2 edit (SORA 03, 01; L2_low_sky) → K25 | план |
| sc03-sh060 | 01:08–01:12 | 4 с | MS (брюхо кита), нижний ракурс | снизу, static | От брюха кита отрывается один лист и, кружась, начинает падать | Отрыв листа (DES, шорох); Нацу ЗК ≈01:10.4–01:12.0 (снизу, кричит): «Сорка! На тебя летит!» | ЗК | `low angle shot from below, the belly of a giant paper whale filling the upper part of the frame, {WHALE_DETAIL}, one single ivory letter sheet peeling off its belly, sunset light through the paper, SUNSET` | `one sheet slowly detaches from the belly and begins to fall, spinning gently, the whale drifts slowly to the left, camera static` | NB2 edit (whale 14_belly_sheet) → MM | план |
| sc03-sh070 | 01:12–01:15 | 3 с | WS, верхний ракурс | сверху, static | Лист кружит вниз к крыше, Сора маленькая, смотрит вверх | Шорох падающего листа, ветер | — | `high angle wide shot from above, a single ivory paper sheet spinning in the air in the foreground, below it the dark blue tiled roof of an old house with {SORA} small, standing next to the chimney and looking up toward the camera, red scarf fluttering, the stone staircase street below, SUNSET` | `the paper sheet spins and falls slowly away from the camera toward the girl, her scarf flutters, camera static` | NB2 edit (SORA 01; L2_wide_downhill) → MM | план |

---

## Сцена 4. Крыша почтового дома — закат · 01:15–01:35

```
Эпизод: ep01 · Сцена: sc04 · Локация: LOC_L2 · Время: закат (SUNSET)
Персонажи: {SORA}, {WHALE_DETAIL}/{WHALE_FAR} (ep01-A) · Сора смотрит влево-вверх на кита; кит слева вверху
Акцентный цвет сцены: киноварь #D9482B (глаз кита) · Настроение: удивление, контакт
Хронометраж сцены: 20 с (01:15–01:35)
Монтаж: на sc04-sh020 — штемпель «НЕ ДОСТАВЛЕНО. 1986» и адрес «Улица Ступеней, дом 14»
```

| № | TC | Длит. | План | Камера | Действие | Реплика / звук | Речь | Промпт ключевого кадра | Промпт движения | Модель | Статус |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sc04-sh010 | 01:15–01:19 | 4 с | MS, нижний ракурс | снизу, static | Сора тянется и ловит лист обеими руками | Шорох, хлопок бумаги о ладони (FOLEY) ≈01:17 | — | `medium shot, low angle, {SORA} standing on dark blue roof tiles next to a red-brick chimney, three-quarter view facing left, stretching both arms up toward an ivory envelope spinning just above her hands, sunset sky behind, {LOC_L2}, SUNSET` | `the spinning envelope falls into her raised hands, she catches it with both hands and pulls it to her chest, the scarf flutters, camera static` | NB2 edit (SORA 03, 01; L2_low_sky; PROP_ENV_1986) → K3 | план |
| sc04-sh020 | 01:19–01:24 | 5 с | ECU insert | static, **без движения камеры** (наложение текста) | Конверт цвета слоновой кости в руках, загнутый угол, пустая рамка штемпеля | Шелест бумаги; Сора ЗК ≈01:20.0–01:23.3 (читает медленно): «„Улица Ступеней, дом четырнадцать“…» | ЗК | `extreme close-up insert, {PROP_ENV_1986} held flat and facing the camera in a girl's two hands with mustard-yellow cardigan sleeves, a blank purple rectangular stamp frame in the upper right with nothing inside, faint illegible scribble lines in the address area, no readable text, warm sunset light` | `almost static, the envelope trembles very slightly in the wind, a thumb shifts a little, no camera movement` | NB2 edit (PROP_ENV_1986; SORA 08_props) → MM | план |
| sc04-sh030 | 01:24–01:28 | 4 с | MCU | eye-level, static | Сора поднимает глаза от конверта на кита | Тишина ветра; низкий отзвук кита | — | `medium close-up, eye level, {SORA} three-quarter view facing left, holding an ivory envelope at chest level, eyes lowered to the envelope, mouth closed, sunset light from the left, a huge pale paper shape out of focus in the sky behind, {LOC_L2}, SUNSET` | `she slowly raises her eyes from the envelope up toward the sky, the wind moves her hair and scarf, camera static` | NB2 edit (SORA 03; sc04-sh010 kf) → K25 | план |
| sc04-sh040 | 01:28–01:31 | 3 с | CU | POV Соры, лёгкий нижний ракурс, static | Красный глаз-штемпель смотрит прямо на неё | Мягкий пульс-«дыхание» кита (DES) | — | `close-up, the eye of a giant paper whale looking straight at the camera, a round red postmark seal with concentric rings and wavy cancellation lines and no text, glowing softly, faceted yellowed paper folds around it, warm sunset light, {WHALE_DETAIL}` | `the red seal's glow pulses softly once, the paper folds around the eye shift slightly, camera static` | NB2 edit (whale 11_eye) → K25 | план |
| sc04-sh050 | 01:31–01:35 | 4 с | OTS (через плечо со спины) | eye-level, очень медленный наезд | Сора спиной к нам, перед ней в небе кит | Сора ≈01:31.6–01:33.8 (тихо, себе): «Ты… потерял письмо?» | ЗК (спиной) | `over-the-shoulder shot from behind {SORA}, her back, red scarf and dark brown hair in the left foreground, looking up at {WHALE_FAR} hanging huge in the sunset sky above the rooftops, the whale's glowing red eyes visible, {LOC_L2}, SUNSET` | `scarf and hair flutter in the wind, the whale drifts slowly to the left, very slow push-in` | NB2 edit (SORA 01 back view; whale 02_far_sunset_silhouette; L2_low_sky) → MM | план |

Переход в сц. 5 — наплыв 0,5 с (смена времени суток).

---

## Сцена 5. Почтовый дом (интерьер) — сумерки · 01:35–02:00

```
Эпизод: ep01 · Сцена: sc05 · Локация: LOC_L1 · Время: сумерки (INT_DUSK), за окном — остаток заката
Персонажи: {GEN}, {SORA}, {NATSU} · Ось: Гэн слева (лицом вправо), Сора справа (лицом влево), вход — справа
Акцентный цвет сцены: золото фонаря #E9A93B (лампа под зелёным абажуром) · Настроение: тихая тяжесть, тайна деда
Хронометраж сцены: 25 с (01:35–02:00)
Монтаж: на sc05-sh030 — «1986» на штемпеле
```

| № | TC | Длит. | План | Камера | Действие | Реплика / звук | Речь | Промпт ключевого кадра | Промпт движения | Модель | Статус |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sc05-sh010 | 01:35–01:39 | 4 с | WS | eye-level, static | Жёлтая лампа под зелёным абажуром; Гэн у стены ячеек протирает очки краем свитера | Тиканье часов, комнатный тон; стук двери ≈01:36.4; Сора ЗК ≈01:36.7–01:38.9 (взволнованно, J-cut): «Деда! Там… в небе…» | ЗК | `wide shot, eye level, {LOC_L1}, INT_DUSK, {GEN} standing in front of the wall of wooden sorting pigeonholes on the left side of the frame, three-quarter view facing right, wiping his round glasses with the edge of his sweater, warm yellow lamp under a green metal shade, round wall clock above the counter, the door at the right edge of the frame` | `he slowly wipes his glasses, the lamp light flickers slightly, dust floats in the lamp light, camera static` | NB2 edit (GEN 03, 01; L1_wide_door) → MM | план |
| sc05-sh020 | 01:39–01:43 | 4 с | MS | eye-level, static | Сора влетела в дверь с конвертом у груди, за ней в проёме запыхавшаяся Нацу | Тяжёлое дыхание обеих (VOX/FOLEY) | — | `medium shot, eye level, {SORA} just inside an open door on the right side of the frame, three-quarter view facing left, out of breath, clutching an ivory envelope to her chest, {NATSU} behind her in the doorway, panting, one hand on the door frame, blue dusk outside, warm lamp light on their faces, {LOC_L1}, INT_DUSK` | `both girls breathe heavily, shoulders rising and falling, Sora's scarf settles after running, camera static` | NB2 edit (SORA 03; NATSU 01; L1_wide_door) → K25 | план |
| sc05-sh030 | 01:43–01:47 | 4 с | CU insert | static, **без движения камеры** (наложение) | Руки Гэна с часами на запястье держат конверт; пальцы замирают на штемпеле | Тиканье часов громче (крупно); шорох бумаги | — | `close-up insert, an old man's hands holding {PROP_ENV_1986} flat under warm lamp light, an old wristwatch with a brown leather strap on his right wrist, cuff of a faded navy jacket with a brass button, his right index finger resting next to the blank purple stamp frame, no readable text, INT_DUSK` | `the fingers slide slowly toward the stamp and stop with a slight tremble, no camera movement` | NB2 edit (GEN 08_props; PROP_ENV_1986; L1_counter_detail) → K25 | план |
| sc05-sh040 | 01:47–01:52 | 5 с | MS со спины | eye-level, static | Гэн спиной к нам, силуэтом у окна; за стеклом проплывает бок кита с янтарными отблесками | Гэн ≈01:47.8–01:50.3 (очень тихо, с тяжестью): «Значит, он вернулся.» · Нацу ЗК ≈01:50.8–01:51.8 (недоверчиво): «Кто — „он“?» · далёкая песня кита сквозь стекло | ЗК (спиной) / ЗК | `medium shot from behind, {GEN} seen from the back in silhouette standing at a window, glasses on, the window filled with the left flank of {WHALE_DETAIL} passing outside with amber sunset glints on the paper, sloping rooftops below, dim warm lamp light from the right, {LOC_L1}, INT_DUSK` | `the whale's flank glides slowly from right to left past the window, amber reflections move across his shoulders, he stays still, camera static` | NB2 edit (GEN 01 back view; whale 10_master_detail_flank; L1_reverse_window) → MM | план |
| sc05-sh050 | 01:52–01:56 | 4 с | MS two-shot, профиль | eye-level, static | Гэн бережно, двумя руками возвращает конверт Соре — как вручают почту | Гэн ≈01:52.6–01:55.4 (медленно): «Письмо не опаздывает, внучка.» | в кадре, без синка (профиль, средний план) | `medium two-shot, eye level, side view, {GEN} on the left facing right in profile, {SORA} on the right facing left in profile, he holds an ivory envelope out to her with both hands in a formal way, she reaches for it with both hands, warm lamp light between them, wooden sorting pigeonholes behind, {LOC_L1}, INT_DUSK` | `he slowly passes the envelope into her hands and she takes it carefully, he speaks a short calm phrase with small mouth movement, natural breathing, camera static` | NB2 edit (GEN 04_profile; SORA 04_profile; L1_counter_detail) → K25 | план |
| sc05-sh060 | 01:56–02:00 | 4 с | MCU | eye-level, static | Сора с конвертом у груди слушает и коротко, решительно кивает | Гэн ЗК ≈01:56.6–01:59.4 (с паузой): «Опаздывают люди. Отнеси.» | ЗК | `medium close-up, eye level, {SORA} three-quarter view facing left, holding an ivory envelope at chest level with both hands, looking slightly up at someone off-screen left, serious determined expression, mouth closed, warm lamp light from the left, {LOC_L1}, INT_DUSK` | `she listens, then gives one small determined nod, slight breathing, camera static` | NB2 edit (SORA 03; sh050 kf) → K25 | план |

Переход в сц. 6 — наплыв 0,5 с.

---

## Сцена 6. Улица Ступеней, у дома № 14 — сумерки · 02:00–02:30

```
Эпизод: ep01 · Сцена: sc06 · Локация: LOC_L3 + LOC_L3_H14 + LOC_L5 · Время: синие сумерки (DUSK), фонари горят
Персонажи: {SORA}, {NATSU} {BIKE}, {WHALE_DETAIL} (ep01-A → ep01-B на sh070) · Ось: Нацу слева, Сора справа; дом № 14 перед ними
Акцентный цвет сцены: золото #E9A93B (окно, шов) · Почтовый ящик — приглушённый красный, не ярче шарфа
Настроение: сомнение → тишина → чудо
Хронометраж сцены: 30 с (02:00–02:30) · Кульминация серии №2
Монтаж: «14» на табличке ящика (sh020, sh040)
```

| № | TC | Длит. | План | Камера | Действие | Реплика / звук | Речь | Промпт ключевого кадра | Промпт движения | Модель | Статус |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sc06-sh010 | 02:00–02:04 | 4 с | WS со спины | чуть сверху, static | Сора и Нацу спускаются по ступеням, Нацу ведёт велосипед по пандусу | Шаги по камню, колёса; эмбиент сумерек; Нацу ЗК с ≈02:03.6 (см. sh020) | ЗК | `wide shot, slightly high angle from behind, {LOC_L3} looking down the stone staircase toward the bay at dusk, {NATSU} and {SORA} seen from behind walking down the steps, Natsu on the left walking her {BIKE} down the smooth ramp along the left side, Sora on the right, warm yellow street lamps glowing, DUSK` | `the two walk slowly down the steps away from the camera, the bicycle wheels roll, lamps glow softly, camera static` | NB2 edit (SORA 01; NATSU 01; L3_down_to_bay) → MM | план |
| sc06-sh020 | 02:04–02:08 | 4 с | MS-WS, без персонажей | eye-level, static (наложение «14») | Дом № 14: зелёная дверь, герань, красный ящик; окна тёмные | Нацу ≈02:03.6–02:08.0 (вполголоса, скептически): «Там живёт старая госпожа Оно. Она лет десять никому не открывает.» | ЗК | `medium wide shot, eye level, {LOC_L3_H14}, green front door, clay pot of red geraniums, red metal mailbox with a blank white number plate, all windows dark, a warm street lamp on the side, DUSK, no people` | `geranium leaves move slightly in the breeze, the lamp light flickers softly, no camera movement` | NB (H14_front) → MM | план |
| sc06-sh030 | 02:08–02:12 | 4 с | MS со спины | eye-level, static | Девочки со спины перед домом; Сора делает шаг к ящику | Сора ≈02:08.5–02:11.5 (тихо, решительно): «Ей не надо открывать. Это же письмо.» | ЗК (спиной) | `medium shot from behind, {NATSU} on the left holding her {BIKE}, {SORA} on the right holding an ivory envelope, both seen from the back, facing the green door and the red mailbox of {LOC_L3_H14}, dark windows, warm lamp light, DUSK` | `Sora takes one step toward the mailbox, Natsu stays still, the scarf moves slightly, camera static` | NB2 edit (SORA 01; NATSU 01; H14_front) → MM | план |
| sc06-sh040 | 02:12–02:15 | 3 с | ECU insert | static | Рука Соры опускает конверт в щель ящика; крышка щёлкает | **Полная тишина** ≈02:12.6–02:14.6 (режиссёрский приём, ≤2 с) → **металлический щелчок крышки** 02:14.6 (ключевой звук серии) | — | `extreme close-up insert, a girl's hand in a mustard-yellow cardigan sleeve pushing an ivory envelope into the horizontal letter slot of a red metal mailbox with a small metal flap and a blank white number plate, warm lamp light, DUSK, no readable text` | `the hand slides the envelope fully into the slot and withdraws, the metal flap swings shut, camera static` | NB2 edit (H14_mailbox_detail; PROP_ENV_1986; SORA 08_props) → K25 | план |
| sc06-sh050 | 02:15–02:18 | 3 с | MS two-shot, профиль | eye-level, static | Пауза. Нацу и Сора переглядываются | Тишина, только тихий эмбиент | — | `medium two-shot, eye level, side view, {NATSU} on the left facing right, {SORA} on the right facing left, standing by a red mailbox, they turn their heads and look at each other in silence, uncertain expressions, mouths closed, warm lamp light, {LOC_L3_H14}, DUSK` | `they slowly turn their eyes to each other, a quiet pause, a light breeze moves hair and scarf, camera static` | NB2 edit (NATSU 03; SORA 03; H14_front) → MM | план |
| sc06-sh060 | 02:18–02:22 | 4 с | MS, нижний ракурс, без персонажей | снизу, static | Окно второго этажа медленно загорается янтарём; к стеклу подходит силуэт (без лица) | Мягкий «тёплый» тон (DES); музыка: первые ноты темы | — | `low angle medium shot, {LOC_L3_H14} facade at dusk, the dark second-floor window above the green door, deep blue twilight sky, DUSK, no people` | `the second-floor window slowly lights up with warm amber light, a soft blurred silhouette of a person approaches the glass from inside and stops, no face visible, camera static` | NB (H14_low_window) → MM | план |
| sc06-sh070 | 02:22–02:26 | 4 с | CU (фрагмент кита) | снизу, static | Прореха A на боку кита стягивается, по краю бежит светящийся янтарный шов | **Песня кита №2** (тише, мягче) ≈02:22.5–02:28; Нацу ЗК ≈02:25.0–02:25.9 (ошеломлённо, шёпотом): «…Он зашился.» | ЗК | `close-up from below, the left flank of a giant paper whale against a deep blue dusk sky, {WHALE_DETAIL}, the large torn hole right behind the left pectoral fin is open, DUSK` | `the edges of the dark hole slowly pull together and a line of glowing amber cross-stitches like gold thread runs along the seam from one end to the other, a soft amber glow spreads over the paper, camera static` | NB2 edit (whale 10_master_detail_flank; L5_low_dusk) + конечный кадр NB2 edit (whale 13_seam) → K3 (start+end frame) | план |
| sc06-sh080 | 02:26–02:30 | 4 с | MS two-shot, нижний ракурс со спины-сбоку | снизу, static | Девочки смотрят вверх; лица в янтарном свете | Сора ЗК ≈02:26.6–02:29.2 (тепло): «Одно письмо. Один стежок.» · музыка — тема | ЗК | `medium two-shot, low angle from slightly behind and below, {NATSU} on the left and {SORA} on the right standing side by side, faces in three-quarter rear view turned up to the sky in wonder, upturned profiles lit by a soft warm amber glow from above, mouths closed, deep blue dusk sky with street lamps, {LOC_L3}, DUSK` | `they gaze up without moving, the amber glow brightens slightly on their faces, a breeze lifts the scarf, camera static` | NB2 edit (SORA 01; NATSU 01; L5_low_dusk) → MM | план |

Ракурс sh080 — сзади-снизу, а не фронтально: фронтальный кадр перескочил бы ось (Нацу оказалась бы справа).
Переход в сц. 7 — наплыв 1 с.

---

## Сцена 7. Крыша почтового дома / небо — ночь · 02:30–02:45

```
Эпизод: ep01 · Сцена: sc07 · Локация: LOC_L5 + LOC_L4 (дальний) + LOC_L2 · Время: ночь (NIGHT), луна
Персонажи: {WHALE_FAR} (ep01-B: шов на месте прорехи A), {SORA} · Кит справа налево; башня в правой трети кадра
Акцентный цвет сцены: киноварь #D9482B (шарф) · Настроение: тихое чудо, личный крючок
Хронометраж сцены: 15 с (02:30–02:45)
Монтаж: на sh030 — штемпель «НЕ ДОСТАВЛЕНО» и слово «Соре»; на sh050 — титр «Бумажный кит»
```

| № | TC | Длит. | План | Камера | Действие | Реплика / звук | Речь | Промпт ключевого кадра | Промпт движения | Модель | Статус |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sc07-sh010 | 02:30–02:34 | 4 с | establishing EWS | static, лёгкий параллакс облаков | Ночь, луна. Кит, проплыв над холмом, останавливается и касается хвостом водонапорной башни, «как корабль у причала» | Ночной эмбиент, ветер в траве; далёкий скрип металла башни | — | `extreme wide shot, night, {LOC_L5} town silhouette on a hillside under a bright moon, the rusty water tower of {LOC_L4} on the hilltop in the right third of the frame, {WHALE_FAR} facing left, slowing down with its tail fin resting against the top of the water tower like a ship moored at a pier, one glowing amber seam on its left flank behind the pectoral fin, a few warm windows below, NIGHT` | `the whale slowly settles and stops, its tail fin gently touching the water tower, moonlit clouds drift, warm windows twinkle, camera static` | NB2 edit (whale 00_master_far + 13_seam; L5_wide_night; L4_far_from_roof) → MM | план |
| sc07-sh020 | 02:34–02:37 | 3 с | MS | eye-level, static | Сора на крыше у трубы с журавликами; к ней летит второй лист; ловит | Шорох листа; хлопок бумаги о ладони ≈02:35.5 | — | `medium shot, eye level, night, {SORA} standing on the dark blue tiled roof next to the red-brick chimney with a row of paper cranes held by pebbles, three-quarter view facing left, both hands raised to catch a pale blue envelope falling toward her, cool moonlight rim on her hair, warm glow from the attic window, {LOC_L2}, NIGHT` | `the envelope spins down into her hands, she catches it with both hands, the scarf flutters, camera static` | NB2 edit (SORA 03, 01; L2_chimney_mid NIGHT; PROP_ENV_SORA) → K3 | план |
| sc07-sh030 | 02:37–02:40 | 3 с | ECU insert | static, **без движения камеры** (наложение) | Конверт: штемпель, вместо адреса — одно слово | Тишина ветра; первая нота музыкальной шкатулки (L4) | — | `extreme close-up insert, {PROP_ENV_SORA} held flat and facing the camera in a girl's two hands with mustard-yellow cardigan sleeves, a blank purple stamp frame, an empty center, cool moonlight with a faint warm glow from below, NIGHT, no readable text` | `almost static, the envelope trembles very slightly, no camera movement` | NB2 edit (PROP_ENV_SORA; SORA 08_props) → MM | план |
| sc07-sh040 | 02:40–02:43 | 3 с | CU | eye-level, static | Глаза Соры расширяются; порыв ветра поднимает красный шарф. Затемнение 02:42.5–02:43.0 | Порыв ветра (DES) ≈02:40.8; дыхание Соры | — | `close-up, eye level, night, {SORA} three-quarter view facing left, looking down at an envelope out of frame, eyes beginning to widen in surprise, mouth closed, red scarf around her neck, cool moonlight rim light, dark navy sky behind, NIGHT` | `her eyes slowly widen, a gust of wind lifts the red scarf up across the frame, hair flutters, camera static` | NB2 edit (SORA 03; sh020 kf) → K25 | план |
| sc07-sh050 | 02:43–02:45 | 2 с | титр на чёрном | — | Титр «Бумажный кит» | Первая нота музыкальной темы (STING) 02:43.0 | — | — (монтаж) | — | без генерации | план |

Титр 2 с укладывается в 2:45. Если директор захочет титр 4–5 с — серия станет 2:48–2:49, в допуске сценария (≤3:00).

---

## Сводная таблица реплик (для звукорежиссёра)

| TC (≈) | Кадр | Персонаж | Реплика | Подача | Речь |
|---|---|---|---|---|---|
| 00:05.5–00:13.0 | sc01-sh020/030 | Сора | Говорят, если сложить тысячу журавликов, можно сказать то, что не получается сказать вслух. | тихо, задумчиво | ЗК |
| 00:21.3–00:24.9 | sc01-sh060 | Сора | У меня их уже сто двенадцать. А сказать всё ещё нечего. | с самоиронией | ЗК |
| 00:30.3–00:32.8 | sc02-sh020 | Нацу | Эй, Почтовая! Опять журавлей пасёшь? | громко, насмешливо | в кадре, без синка |
| 00:34.4–00:34.9 | sc02-sh030 | Сора | Пасу. | спокойно | в кадре, без синка |
| 00:41.8–00:43.0 | sc02-sh050 | Нацу | …Это ещё что? | растерянно, тише | ЗК |
| 01:05.0–01:06.8 | sc03-sh050 | Сора | Кит. Из бумаги. | шёпотом | ЗК |
| 01:10.4–01:12.0 | sc03-sh060 | Нацу | Сорка! На тебя летит! | кричит снизу | ЗК |
| 01:20.0–01:23.3 | sc04-sh020 | Сора | «Улица Ступеней, дом четырнадцать»… | читает медленно | ЗК |
| 01:31.6–01:33.8 | sc04-sh050 | Сора | Ты… потерял письмо? | тихо, себе | ЗК (спиной) |
| 01:36.7–01:38.9 | sc05-sh010 | Сора | Деда! Там… в небе… | взволнованно, запыхавшись | ЗК |
| 01:47.8–01:50.3 | sc05-sh040 | Гэн | Значит, он вернулся. | очень тихо, тяжело | ЗК (спиной) |
| 01:50.8–01:51.8 | sc05-sh040 | Нацу | Кто — «он»? | недоверчиво | ЗК |
| 01:52.6–01:55.4 | sc05-sh050 | Гэн | Письмо не опаздывает, внучка. | медленно | в кадре, без синка |
| 01:56.6–01:59.4 | sc05-sh060 | Гэн | Опаздывают люди. Отнеси. | с паузой | ЗК |
| 02:03.6–02:08.0 | sc06-sh010/020 | Нацу | Там живёт старая госпожа Оно. Она лет десять никому не открывает. | вполголоса, скептически | ЗК |
| 02:08.5–02:11.5 | sc06-sh030 | Сора | Ей не надо открывать. Это же письмо. | тихо, решительно | ЗК (спиной) |
| 02:25.0–02:25.9 | sc06-sh070 | Нацу | …Он зашился. | почти шёпотом | ЗК |
| 02:26.6–02:29.2 | sc06-sh080 | Сора | Одно письмо. Один стежок. | тепло | ЗК |

Ключевые звуковые точки: песня кита №1 — 00:51; щелчок ящика — 02:14.6 (перед ним тишина 2 с); песня кита №2 — 02:22.5; титр и первая нота темы — 02:43.0. Наплывы: 01:35 (0,5 с), 02:00 (0,5 с), 02:30 (1 с); затемнение 02:42.5–02:43.0.

## Распределение по планам

| План | Кадров | Доля | Комментарий |
|---|---|---|---|
| Establishing / WS / EWS | 13 | 32% | выше ориентира библии (10–15%): кит требует общих планов, а общие планы и съёмка со спины заменяют синхрон |
| MS (вкл. two-shot, OTS) | 13 | 32% | |
| MCU | 4 | 10% | все без речи |
| CU / ECU / insert | 11 | 27% | конверты, руки, глаз и шов кита |

## Отличия от сценария (постановочные решения)

| Место | Сценарий | Шот-лист | Причина |
|---|---|---|---|
| sc02, «Эй, Почтовая!» | В КАДРЕ | дальний план сверху, ладонь у рта | решение директора: без синхрона |
| sc02, «…Это ещё что?» | В КАДРЕ | ЗК на кадре с тенью и фонарями | синхрон + тень на лице — двойной риск |
| sc03, «Сорка! На тебя летит!» | В КАДРЕ | ЗК на кадре падающего листа | Нацу снизу, в кадре — кит и лист |
| sc04, «Ты… потерял письмо?» | В КАДРЕ | спиной, через плечо на кита | сильнее композиционно: героиня и кит в одном кадре |
| sc05, «Деда! Там… в небе…» | В КАДРЕ | ЗК, J-cut на общем плане с Гэном | ввод Гэна в сцену + без синхрона |
| sc05, «Значит, он вернулся.» | В КАДРЕ | спиной, силуэт на фоне окна с китом | без синхрона, кит в кадре |
| sc05, «Кто — „он“?» | В КАДРЕ | ЗК | — |
| sc05, «Письмо не опаздывает…» | В КАДРЕ | первая фраза — профиль на среднем плане; «Опаздывают люди. Отнеси.» — ЗК на реакции Соры | без синхрона; реакция Соры важнее лица Гэна |
| sc05, Гэн надевает очки | в кадре | за склейкой (между sh020 и sh030) | меньше мелкой работы рук |
| sc06, обе реплики у дома | В КАДРЕ | ЗК / спиной | без синхрона |
| sc06, «…Он зашился.» | В КАДРЕ | ЗК на кадре со швом | шов — главный кадр, реакцию даём в sh080 |
| sc07, кит «касается хвостом» | — | кит проплыл над холмом и останавливается, хвост у башни | направление «справа налево» сохраняется |

---

## Смета пилота (по model_choice.md)

Допущения model_choice §3: 2 дубля видео на кадр, клип 5 с; 2 попытки ключевого кадра; цены fal.ai от директора. Титр не генерируется.

### Видео

| Модель | Кадров | Секунд (×2 дубля ×5 с) | Цена/с | Сумма |
|---|---|---|---|---|
| MiniMax H3 Max Turbo | 20 | 200 | $0.015 | $3.00 |
| Kling 2.5 Turbo Pro | 16 | 160 | $0.07 | $11.20 |
| Kling 3 Pro | 5 | 50 | $0.14 | $7.00 |
| **Итого видео** | **41** | **410** | | **$21.20** |

### Ключевые кадры

| Модель | Изображений | Цена | Сумма |
|---|---|---|---|
| Nano Banana 2 (36 кадров + 1 конечный кадр sc06-sh070) × 2 | 74 | $0.08 | $5.92 |
| Nano Banana (5 кадров без персонажей) × 2 | 10 | $0.04 | $0.40 |
| **Итого картинки** | **84** | | **$6.32** |

### Итог

| Статья | Сумма |
|---|---|
| Видео + ключевые кадры | $27.52 |
| Резерв 20% (третьи дубли, эскалации) | $5.50 |
| **Пилот, производство кадров** | **≈ $33.0** (≈ $12.0 за минуту) |
| Разово: референс-листы 3 персонажей + кит + ~20 мастер-кадров локаций + реквизит (`references.md` §5) | ≈ $16–19 |
| **Пилот всего (визуал)** | **≈ $49–52** |
| Липсинк | **$0** — в пилоте не нужен |

Минута дороже микса model_choice (≈ $11): в пилоте больше вставок с руками и кадров с китом на Kling 2.5 TP, чем в типичной диалоговой серии. Синхрона нет, поэтому не нужно ни липсинка, ни Kling на говорящих крупных планах.

Чувствительность:
- если минимальный клип MiniMax 6 с, а не 5 с (уточняет IT-инженер): +$0.60;
- если все 20 MiniMax-кадров придётся поднять до Kling 2.5 TP: +$11.0;
- стилевой тест (model_choice §5): если делать его на Соре вместо MIRA, тест одновременно даёт её референс-лист, и разовые затраты снижаются на ≈ $3.5.

Не входит: синтез речи, SFX и музыка (ElevenLabs, смета звукорежиссёра), апскейл до 1080p, если модели отдают меньше.
