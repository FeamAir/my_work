# S1E01 «The Ninth Sluice» — покадровая постановка сцен-«денег»

Версия 1.0 · 2026-11-22 · автор: постановщик битв и спецэффектов
Основа: `story/episodes/S01E01/beat_sheet.md` v1.1, `production_notes.md` v1.1 (§1 M1–M6), закрытая выдержка для режиссёра и художника, `vfx/magic_look.md`, `vfx/water_and_disaster.md`.
Для: режиссёра (сводит в общий шот-лист серии по `direction/shotlist_template.md`), художника-концептера (референсы), IT-инженера (сборка LA).
Статус: **черновик постановки для раскадровки.** Ничего не генерируется до утверждённой раскадровки и аниматика (решение директора: пилот — сначала аниматик из дешёвых кадров со звуком, инвестор смотрит его).

---

## 0. Условные обозначения и правила

| Код | Значение |
|---|---|
| NB2 | Nano Banana 2 ($0.08/img) — все ключевые кадры с персонажами и героические плейты |
| NB | Nano Banana ($0.04/img) — служебные плейты без персонажей, состояния воды (edit) |
| MM | MiniMax H3 Max Turbo ($0.015/с; клип, по данным режиссёра, 6 с ≈ $0.09 — подтверждает IT) — черновик движения; финал для простых кадров; петли ткани L-13 |
| K25 | Kling 2.5 Turbo Pro ($0.07/с) — финал для лиц, тканей, простых объектов на воде |
| K3 | Kling 3 Pro ($0.14/с) — финал только для 4 героических кадров со сложным движением |
| LA | ограниченная анимация: статика + движение камеры/параллакс/слои/свет в ffmpeg (бесплатно) |
| HERO | героический кадр из `production_notes.md` §1 |

**Порядок работы над каждым кадром** (правило дублей BRIEF + особый режим пилота):
1. Ключевой кадр NB2 по референсам (2–4 попытки, приёмка по `consistency.md` §6 + `magic_look.md` §9).
2. **Аниматик:** этот же ключевой кадр в LA (движение камеры, слои) — со звуком. Инвестор смотрит аниматик.
3. Черновик движения на MM (1–2 дубля) — утверждаем движение и тайминг.
4. Финал на K25/K3 — **не больше 5 финальных дублей** (лимит пилота). Цель — 1–2.
5. Не вышло за 5 — **не жмём «ещё раз»**: кадр уходит в резервный приём LA (указан у каждого кадра) или меняем подход (ракурс, референс, разбивка на два клипа); вывод — в библиотеку приёмов (`vfx/lessons.md`, создаётся при первом выводе).

**Сквозные запреты пилота (из выдержки и production_notes):**
- Осколок и перстень Руэла **никогда в одном кадре** и **не в соседних вставках**. Вставки осколка (сц. 3, 20) и жемчужины (сц. 10–12) монтажно разнесены; на них нельзя делать склейку по форме.
- Сц. 1 — **ни одного лица**. Колыбель — **без узла**.
- Все косы — **слева** (Лисс в сц. 1, Пелл).
- Сц. 1 кадр 1E и сц. 18 — **одинаковая рамка рук** (§1, «Рамка рук»).
- Пелл и Иона — без липсинка; поющая Иона — только спиной.
- Не больше четырёх читаемых лиц в кадре.

Плейсхолдеры ID-блоков: `{PELL}`, `{WICK}`, `{IONE}`, `{LUCAN}` и т. д. — дословные ID-блоки из `direction/refs/<ID>/card.md` (готовит режиссёр/художник по `_anchors_matrix.md`). `{STYLE}` = STYLE_BASE, `{NEG}` = негатив, `{MOTION}` = промпт движения — `direction/visual_bible.md` v2.0 §10.1, §10.4, §10.3. Модули света v2 (`LOWS_NIGHT_FLOOD`, `LOWS_DAWN`, `LOWS_DUSK`, `MIDS_INTERIOR`, `STEPS_GOLD`) можно подставлять вместо описания света в промптах ниже — смысл совпадает. Рецепты LA — `direction/limited_animation.md` (L-xx); мои пресеты `LA-*`/`VFX-*` — `water_and_disaster.md` §4, `magic_look.md` §8. `{SPIRE_DESC}`, `{SPIRE_LIT}`, `{GLASS_WATER}`, `{SHARD_DESC}`, `{SOUND_RINGS}` — `magic_look.md` §10.1; `{WATER_STYLE}` — `water_and_disaster.md` §3.

Для вертикальных нарезок (production_notes §9: V1 сц. 1, V2 сц. 3, V3 сц. 9, V5 сц. 16) — главный объект в **центральной трети** кадра.

---

## M1 · Сц. 1 — Ночь Тихой Воды (0:00–1:15)

**Карта воды:** течение справа налево (от ворот к открытой воде); дождь из левого верхнего угла, 15°; ворота — справа в кадре, открытая вода — слева; уровень растёт. Свет: модуль `LOWS_NIGHT_FLOOD` (v2): янтарь фонарей `#E39B3A`, чёрно-бирюзовая вода; акцент сцены — янтарь фонаря. Музыки нет до 0:35.
**Переиспользование:** все плейты, маски и движения камеры сохраняются как `S1-SC01-*` — E10 повторяет сцену кадр в кадр (тот же переулок, тот же косяк, те же ворота).

### 1A · 0:00–0:08 · общий, уровень глаз · 8 с · HERO — колыбель
- **Что:** колыбель плывёт по середине *улицы*, вода до притолок, медленно поворачивается; рядом на столбе ещё горит фонарь. Первый кадр серии: читается за полсекунды на телефоне.
- **Композиция:** колыбель в центре (безопасная зона 9:16), фонарь — правее и выше; переулок уходит в глубину; дверной косяк с отметками прилива — правый передний план (тот же, что в сц. 2).
- **Камера:** статика с очень медленным наездом (≈5% за 8 с).
- **KF (NB2):**
```
Night, eye-level wide shot down a narrow lane of wooden stilt houses flooded with black water up to the door
lintels. In the exact centre of the frame an empty wooden baby cradle floats on the water, slightly turned,
plain wood with no ropes and no knots. A small lantern on a post just right of the cradle still burns with
warm gold light, its reflection trembling on the water. Rain falls at a slight angle from the upper left.
A wooden doorpost carved with a ladder of tide-marks stands in the right foreground. No people.
{WATER_STYLE}. {STYLE}
```
- **Motion:**
```
Very slow push-in. The cradle drifts slowly from right to left with the current and turns gently a quarter
turn, rocking on small ripples; rain rings on the water; the lantern flame flickers and its reflection
trembles. Nothing else moves, no people appear. {MOTION}
```
- **Черновик:** MM 10 с ×1–2 · **Финал:** K3 10 с (≤5) · **Резерв LA:** вырезанная колыбель `LA-FLOAT` по плейту W-1 + `LA-RAIN` + `LA-REFLECT` + мерцание фонаря.
- **Приёмка:** колыбель пустая, без узла; не меняет форму; течение справа налево; лиц нет.

### 1B · 0:08–0:13 · общий, тот же переулок · 5 с — фонари гаснут
- **Что:** фонари на мостках гаснут один за другим, от дальнего к нам.
- **Камера:** статика.
- **KF:** плейт W-1 в состоянии «вода до притолок» (NB edit от 1A без колыбели) — `Keep everything identical. Remove the cradle. Add a row of six small lanterns on posts along the plank walkways receding into depth.`
- **Движение:** только LA — `LA-LANTERN-OUT` (6 масок, интервал 0,7 с, отражение гаснет на 2–3 кадра позже) + `LA-RAIN`.
- **Модель:** нет (LA) · **Резерв:** не нужен.

### 1C · 0:13–0:18 · крупный, косяк · 5 с — вода выше всех отметок
- **Что:** вода поднимается по «лестнице» отметок прилива на дверном косяке, проходит самую верхнюю.
- **Камера:** статика; вода поднимается в кадре.
- **KF (NB2, два состояния одной композиции):**
```
Night, close-up of a weathered wooden doorpost carved with a vertical ladder of old tide-marks — short horizontal
notches with small scratched marks beside them, the highest notch near the top of the frame. Black flood water
covers the lower part of the post, rain rings on its surface, warm lantern light from the left. {WATER_STYLE}. {STYLE}
```
второй — edit: `Keep everything identical. Raise the water so that it covers every notch, just above the highest one.`
- **Движение:** LA — `LA-RISE` (маска уровня + кромка + рябь) + `LA-RAIN`.
- **Модель:** нет (LA). Этот же косяк — сц. 2 (сухой, отметка той ночи высоко над другими) и сц. 19.
- **Приёмка:** отметки — без читаемых цифр/букв (надписи, если нужны, — монтажом).

### 1D · 0:18–0:24 · общий, низкий ракурс · 6 с — толпа у ворот
- **Что:** толпа в темноте у огромных ворот; силуэты против света фонарей с той стороны; дождь.
- **Композиция:** ворота справа (карта воды); толпа — сплошная масса спин и поднятых рук, **ни одного лица**.
- **KF (NB2):**
```
Night, low-angle wide shot from behind a dense crowd pressing against a huge iron-barred gate set in a brick dike wall,
the gate on the right half of the frame, warm lantern light glowing beyond the bars, the crowd entirely in black
silhouette seen from behind — heads, shoulders, raised arms, bundles — knee-deep in dark water, heavy rain.
No faces visible. {WATER_STYLE}. {STYLE}
```
- **Motion:** `Static camera. The silhouetted crowd sways and presses forward slightly, a few raised arms move, rain falls, lantern light flickers beyond the bars. No faces, no one turns around. {MOTION}`
- **Черновик/финал:** MM 5 с (финал на MM; ≤5) · **Резерв LA:** параллакс 3 слоя (толпа / ворота / свет) + лёгкое «дыхание» слоя толпы (масштаб ±1%) + `LA-RAIN`.

### 1E · 0:24–0:29 · крупный, руки · 5 с · HERO — засов задвигают
- **Что:** пара молодых солдатских рук — без лица — тянет засов и **закрывает** ворота.
- **Рамка рук (фиксирована; сц. 18 повторяет её точно):** крупный план, камера на высоте засова, перпендикулярно воротам, нормальный объектив (≈50 мм экв.); засов идёт горизонтально по линии **верхней трети**; обе кисти на засове — левая у левой трети кадра, правая в центре; засов движется **справа налево** в железную скобу у левого края кадра; за прутьями — расфокус. Свет: тёплый фонарь сверху-справа. Рукава тёмные, обшлаг нечитаем (цвет — по согласованию со сценаристом).
- **KF (NB2) — два кадра (start/end):**
```
Night, close-up at the height of a heavy iron gate bar: two young, slender but strong hands grip a thick
horizontal iron bar running across the upper third of the frame, left hand at the left third, right hand
in the centre, dark sleeves, the hands pull the bar to the left toward an iron bracket at the left edge of
the frame; beyond the vertical gate bars everything is out of focus darkness; rain drops on the iron,
warm lantern light from upper right. No face, only hands. {STYLE}
```
end-кадр: edit — `Same image, the bar is now fully inside the bracket at the left edge, the hands still gripping it.`
- **Motion:** `Static camera. The two hands drag the heavy iron bar from right to left with effort until it slams into the bracket; the knuckles whiten; rain drips. The hands keep exactly five fingers each. {MOTION}`
- **Черновик:** MM 5 с ×2 · **Финал:** K3 5 с, start+end frame (≤5) · **Резерв:** по «правилу честности» режиссёра (`limited_animation.md` §1: руки в действии — только генерация) не маскируем действие плохой LA, а меняем постановку: **начало и результат** — кадр «руки берутся за засов» (статика) → склейка на ударе железа (звук, тряска L-05 2–3 фрейма) → кадр «засов в скобе, руки на нём» (статика). Тот же резерв действует для сц. 18.
- **Приёмка:** 5 пальцев, кисти не слиплись; засов движется налево; лица нет. **Сохранить кадр, объектив, сторону и свет как `S1-SC01-HANDS` для сц. 18.**

### 1F · 0:29–0:35 · средний, через прутья · 6 с — кулаки «не с той стороны»
- **Что:** кулаки бьют по железу с другой стороны ворот.
- **KF (NB2):**
```
Night, medium shot through vertical iron gate bars from the dry side: several fists and open palms of
silhouetted people strike and grip the bars from the far side, faces hidden in darkness and rain, warm
lantern light catching the wet knuckles. No faces visible. {STYLE}
```
- **Motion:** `Static camera. Fists hit the bars and hands grip and shake them, rain splashes off the iron. No faces. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5) · **Резерв LA:** статичный кадр, удары — микротряска кадра + вспышка блика на костяшках синхронно со звуком.

### 1G · 0:35–0:42 · под водой · 7 с — тишина
- **Что:** тишина под водой. Затем сверху — женский хамминг (пять нот, звук).
- **KF:** W-3 (`water_and_disaster.md` §8).
- **Движение:** LA — медленный подъём пузырей (слой), дрейф ткани, свет фонаря сверху «дышит».
- **Модель:** нет · **Резерв:** не нужен. Людей в кадре нет.

### 1H · 0:42–0:50 · общий, силуэт на коньке крыши · 8 с — та, что поёт
- **Что:** силуэт женщины на коньке крыши, одна длинная коса **слева**; дождь; она поёт с закрытым ртом (звук).
- **KF (NB2):**
```
Night, wide shot of a woman's silhouette crouching on the ridge of a flooded stilt-house roof, seen from the side
and slightly behind, one long braid hanging over her LEFT shoulder, plain wrapped dress, black flood water all
around, a faint warm glow of distant lanterns behind her, heavy rain. Pure silhouette, no face visible.
{WATER_STYLE}. {STYLE}
```
- **Motion:** `Static camera. Rain falls, the braid and the hem of her dress stir in the wind, her shoulders rise slowly with breath. She does not turn. {MOTION}`
- **Черновик/финал:** MM 10 с (финал на MM; ≤5) · **Резерв LA:** параллакс + `LA-RAIN` + «дыхание» силуэта (масштаб ±0,5%).
- **Приёмка:** коса слева; лица нет; ничего не светится (хамминг не «магичен»).

### 1I · 0:50–1:00 · средний, лодка · 10 с · HERO — младенец отвечает
- **Что:** спасательная лодка с одним фонарём; запелёнатый младенец в ней «отвечает» двумя нотами (звук).
- **KF (NB2):**
```
Night, medium shot of a small wooden rescue boat on black flood water, a single lantern on a short pole at the bow
with warm gold light, in the bottom of the boat a tightly wrapped baby bundle in pale cloth, the baby's face hidden
in the folds, rain rings on the water, dark stilt houses behind. No adult visible. {WATER_STYLE}. {STYLE}
```
- **Motion:** `Static camera. The boat rocks gently on small ripples and drifts slightly left, the lantern sways and its reflection trembles, the cloth bundle moves very slightly as if breathing. {MOTION}`
- **Черновик:** MM 10 с · **Финал:** K25 10 с (≤5) · **Резерв LA:** `LA-FLOAT` лодки + качание фонаря (поворот слоя ±3°) + `LA-REFLECT`.
- **Приёмка:** лица младенца не видно; свёрток не меняет форму.

### 1J · 1:00–1:08 · средне-крупный · 8 с · HERO — рукав
- **Что:** серый рукав рясы протягивается в лодку и поднимает младенца из кадра.
- **Композиция:** лодка как в 1I, ближе; рукав входит **сверху справа**, уходит туда же.
- **KF (NB2) start/end:**
```
Night, medium close-up of the same small boat with the lantern and the wrapped baby bundle; from the upper right
a grey hooded robe's wide sleeve and a pale hand reach down into the boat toward the bundle. Rain. {STYLE}
```
end: edit — `Same image, the bundle and the sleeve are gone, the boat is empty, only the lantern remains.`
- **Motion:** `Static camera. The grey sleeve reaches down, the hand lifts the wrapped bundle gently and withdraws up and out of frame to the upper right; the boat rocks from the lost weight. {MOTION}`
- **Черновик:** MM 5 с ×2 · **Финал:** K3 5 с start+end (≤5), подрезать до 8 с со стоп-кадром в конце · **Резерв LA:** два кадра (рукав над свёртком / пустая лодка) — склейка на звуке, рукав-слой уходит вверх с motion blur за 0,3 с, лодка качается (`LA-FLOAT`).
- **Приёмка:** только рукав и кисть — без лица и фигуры; рукав серый.

### 1K · 1:08–1:15 · общий, высокая точка · 7 с — фонарь уходит
- **Что:** фонарь лодки уходит без младенца, маленький на чёрной воде. Поверх (без склейки в чёрное) — титр *The Night of Still Water* (монтаж).
- **KF (NB):** `High wide shot over black flood water at night between half-drowned roofs, one tiny boat with a single lantern far away in the centre, rain. {WATER_STYLE}. {STYLE}`
- **Движение:** LA — лодка-огонёк дрейфует влево (`LA-FLOAT` на малом масштабе), `LA-RAIN`, медленный отъезд.
- **Переход:** склейка по форме — фонарь на чёрной воде → солнце на мокром иле (сц. 2, тот же косяк).

---

## E-1 · Сц. 2 — подъём над Хайуотером (6 с, мастер-кадр сезона)

- **Что:** камера поднимается за взглядом Пелл: город на сваях в собственной тени → кирпичная дамба → гранитные террасы → над всем чёрные Шпили, один звучит плоско (Шлюзовой, расстроенный).
- **KF (NB2, высокий кадр 1080×3240 или склейка трёх кадров по вертикали):**
```
Tall vertical panorama of a delta capital at dawn, bottom to top: a stilt town of wooden houses and plank walkways
in deep morning shadow below the waterline, canals drained to wet silt; above it a massive brick dike with walkways;
above that granite terraces with tiled roofs and stairs climbing a hill; above everything three colossal black
towers — {SPIRE_DESC} — one of them nearer and weaker, its grooves dull; early pale turquoise sky.
{STYLE}
```
- **Движение:** LA — вертикальная панорама вверх (4 с), задержка 1 с, обратно вниз (1 с). Параллакс по слоям (сваи / дамба / террасы / Шпили).
- **Модель видео:** нет. Это мастер-кадр сезона: тратим на картинку (до 6 попыток NB2), не на движение.
- **Шпили:** спираль по солнцу (`magic_look.md` §3); Шлюзовой — без свечения (утро, песни нет), гул плоский (звук).

---

## M2 · Сц. 3 — пруд: находка и ответ (≈2:25–3:15 сцены)

**Карта:** пруд-отстойник за голым порогом шлюза; Пелл на пороге **слева**, тёмная вода **справа**; Уик держит верёвку за ней, левее. Утро, отлив, модуль `LOWS_DAWN`. Акцент сцены — по шот-листу режиссёра, **не бело-голубой** (Шпиль здесь не поёт; ответ осколка — без света).
**Синхронизация:** кольца и низкий гул приходят **вместе на 3:00** (production_notes M2).

### 3A · ~2:40 · средний, сбоку · 5 с · HERO — Пелл над чёрной водой
- **Что:** Пелл, обвязанная верёвкой, наклоняется над чёрной водой с граблями на вытянутых руках; за ней Уик в натянутой верёвке.
- **KF (NB2, рефы: Пелл, Уик, локация PL-0020):**
```
Morning, medium side shot at the edge of a bare old stone sluice sill: {PELL} leans far out over a still pool of
black water on the right, a rope tied around her waist pulled taut behind her, a long wooden rake held at arm's
length into the water, her face tense and frightened, mouth closed; behind her on the left {WICK} braces his feet
in the mud holding the rope with both fists. Wet silt, mossy stones, pale turquoise sky. {STYLE}
```
- **Motion:** `Static camera. She leans a little further, the rope tightens and trembles, the rake moves slowly under the water; the boy shifts his grip. Small ripples around the rake. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5) · **Резерв LA:** статика + дрожь верёвки (слой) + рябь у граблей (`displace`).
- **Приёмка:** коса Пелл слева, бирка «IX» (нечитаемо — нормально); шнурка с осколком ещё нет; 180°: Пелл слева, вода справа.

### 3B · ~2:48 · крупный, тихий · 5 с — Пелл хмыкает от страха
- **Что:** немой крупный план: она, не замечая, хмыкает три ноты закрытым ртом (звук). Без липсинка.
- **KF (NB2):** `Close-up of {PELL} in three-quarter profile facing right, looking down at dark water below frame, lips pressed shut, nostrils flared, a drop of sweat at her temple, cold morning light from the right reflected from the water. {STYLE}`
- **Motion:** `Static camera. Her throat moves slightly as she hums with closed lips, her breathing is shallow, eyes fixed down. Mouth stays closed. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5) · **Резерв LA:** статика + микронаезд + дыхание (масштаб ±0,5%).

### 3C · ~2:55 · вставка · 3 с — грабли зацепились
- **KF (NB):** `Insert: the head of a wooden rake under black still water, a rotted cord snagged on one tine, the rope above it taut. {STYLE}`
- **Движение:** MM 5 с (подрезать до 3 с) — `The rake pulls upward against resistance, the cord tightens. {MOTION}` · **Резерв LA:** сдвиг слоя граблей вверх на 10 px + рябь.

### 3D · 3:00 · макро · 4 с · HERO — камень выходит из воды
- **Что:** грабли поднимают сгнивший шнурок, на нём чёрный камешек с трещиной; в момент выхода из воды он «отвечает» — низко, под порогом слышимости (звук). **Не светится.**
- **KF (NB2, реф: осколок E1 props):**
```
Extreme close-up: a rake tine lifting out of black water, from it hangs a rotted dark cord and on the cord
{SHARD_DESC}, water dripping from the stone, the stone half out of the water surface, cold morning light,
the black pool behind. {STYLE}
```
- **Motion:** `Static camera. The stone rises clear of the water on its cord, drops of water fall from it, the stone trembles very slightly on the cord. The stone does not glow. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5), эскалация — K3 · **Резерв LA:** стоп-кадр + `VFX-SHARD-TREMOR` + капли (слой) + кольца у точки выхода.
- **Приёмка:** камень — не больше ногтя большого пальца относительно зубцов граблей; трещина поперёк; свечения нет; перстня/жемчужины нет нигде в соседних кадрах.

### 3E · 3:00–3:06 · общий, верхний ракурс · 6 с · HERO — кольца по всему пруду
- **Что:** весь чёрный пруд вздрагивает кольцами от точки, где вышел камень; ровные, без всплеска.
- **KF (NB2):** `High-angle wide shot of a still black pool beyond an old stone sluice sill, a small figure on a rope at the left edge, a boy behind her, wet silt around, the water perfectly smooth. {STYLE}`
- **Движение:** **LA — библиотечный `VFX-RINGS`** (центр — точка у граблей; интервал колец 0,4 с; кольца доходят до краёв пруда). Это тот же элемент, что в сц. 20 (склейка по мотиву «кольца», production_notes §8).
- **Модель видео:** нет (опционально K25 5 с для сравнения в тесте T4) · **Резерв:** не нужен.
- **Приёмка:** кольца равномерные, без капли в центре, без света.

### 3F · 3:06–3:11 · крупный, тихий · 5 с — Уик видел
- **Что:** Уик смотрит с колец на неё — и впервые без слов.
- **KF (NB2):** `Close-up of {WICK}, wide-eyed, mouth slightly open with no words, eyes moving from the water to someone on the left, cold reflected light rippling on his face. {STYLE}`
- **Motion:** `Static camera. His eyes shift from the water to the left, soft rippling light plays on his face, he swallows. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5) · **Резерв LA:** статика + бегущий отсвет ряби на лице (маска + `displace`).

---

## M3 · Сц. 9 — корона (1:45)

**Карта:** Иона в горле короны **спиной** к камере, смотрит на гавань; гавань — внизу перед ней; закатное солнце — слева (`STEPS_GOLD`). Перекрёстный монтаж: крыша в Девятом, Пелл и Уик **спиной**, далёкий светящийся Шпиль — в правой трети. Акцент сцены — **бело-голубой Шпиля** (v2 §3.5: закон мира); золото низкого солнца — ключевой свет, не акцент.
**Звук:** один чистый тон; гул Шпиля «под» ней; шум моря **вычитается** на фронте стекла (`magic_look.md` §4.1). Музыки нет, пока она поёт.
**Библиотека:** кадры 9B, 9D, 9E — `VFX-CROWN-*`, переиспользуются каждый раз, когда поют Шпиль в сезоне.

### 9A · 0:00–0:05 · общий, изнутри короны · 5 с — выход в горло
- **KF (NB2, рефы: Иона, PL-0014 горло):** `Wide shot from inside the crown of a black stone tower: {IONE}, seen from behind, steps into a tall open arched throat facing the sky, wind catching her white robe and long silver hair with two side-plaits joined behind, beyond her an open golden late-afternoon sky. {STYLE}`
- **Motion:** `Static camera. She steps forward into the opening and stops, her robe and hair lift in the wind. {MOTION}`
- **Финал:** MM 5 с (≤5) · **Резерв LA:** статика + ветер (слой волос/ткани не трогаем — только наезд и пыль в луче).

### 9B · 0:05–0:15 · средний, со спины · 10 с · HERO — фирменный кадр
- **Что:** Иона в горле, спиной к нам, одежда бьётся на ветру; один долгий тон. Композиция — как последняя панель гобелена (одна певица на вершине).
- **KF (NB2):**
```
Medium-wide shot from directly behind: {IONE} stands alone in an open arched throat at the very top of a colossal
black glassy tower, back to camera, head slightly raised, arms at her sides, a silver tuning fork glinting at her
breastbone seen only as a glint, her white robe and violet throat-band, long silver hair with two side-plaits joined
behind whipping in a strong wind; far below and in front of her a harbour city and a fleet of tall ships on choppy
water under a golden late-afternoon sun from the left. {STYLE}
```
- **Motion:** `Locked-off camera. Strong wind snaps her robe and hair; her shoulders rise slowly as she draws a long breath and hold still as she sings; she never turns her head. Far below, the water is choppy. {MOTION}`
- **Черновик:** MM 10 с · **Финал:** K25 10 с (≤5) · **Резерв LA:** ключевой кадр + ветер только на волосах/ткани через короткий MM-клип с вырезанной маской фигуры, или полностью LA: медленный отъезд + пыль/соль в воздухе.
- **Приёмка:** лица нет; волосы серебряные, две боковые косы соединены сзади; без липсинка.

### 9C · 0:15–0:20 · общий снаружи · 5 с — гул
- **Что:** гул приходит раньше света: дрожь воздуха над горлом, чайки срываются с карнизов короны.
- **KF:** MK-1 (`magic_look.md` §10.2), ближе к короне.
- **Motion:** `Static camera. Gulls burst from the ledges of the tower's crown and wheel away; a faint shimmer of air trembles above the crown. No glow yet. {MOTION}`
- **Финал:** MM 5 с (≤5) · **Резерв LA:** стая чаек — слой с траекториями; марево — `displace` по шуму над короной.

### 9D · 0:20–0:28 · общий, низкий ракурс · 8 с · HERO — свет по бороздкам
- **Что:** бороздки загораются сине-белым изнутри, виток за витком, вниз по всей башне.
- **KF:** MK-1 (тёмный) + MK-2 (светящийся) — та же композиция.
- **Движение:** **LA — `VFX-GROOVE-LIGHT`** (маска бороздок, свет спускается от горла вниз ≈ виток за 0,5 с, затем «дышит» ±10%). Облака — медленный сдвиг слоя. **Видеомодель не используем** (модели размазывают свет и путают спираль).
- **Приёмка:** `magic_look.md` §9 — свет только в бороздках, спираль по солнцу, без лучей.

### 9E · 0:28–0:38 · общий сверху, от короны на гавань · 10 с · HERO — гавань становится стеклом
- **Что:** одним непрерывным кадром: рябь → зыбь → ничего; фронт спокойствия расходится от подножия Шпиля (нижний левый угол кадра) по всей гавани.
- **KF:** MK-3 «рябь» и MK-3 «стекло» (одна композиция; edit).
- **Вариант A (основной для аниматика и резерв):** **LA — `VFX-GLASS-WIPE`** (радиальная маска 5 с + светлая линия фронта + сначала гаснет мелкая рябь-слой, потом зыбь).
- **Вариант B (финал, если тест T1 даст лучше):** K3 10 с, start = «рябь», end = «стекло», промпт движения — `magic_look.md` §10.3. Черновик — MM 10 с.
- Решение A/B — по тесту T1. Цель — один непрерывный кадр без склейки.
- **Приёмка:** переход виден как процесс; дальняя вода у горизонта спокойна слабее; композиция кораблей не меняется.

### 9F · 0:38–0:43 · вставка · 5 с · HERO — мачты замерли, отражение чайки
- **KF (NB2):** `Low wide shot across a perfectly still harbour, the masts of anchored tall ships standing motionless, a single gull gliding low over the water with its exact mirror reflection beneath it. {GLASS_WATER}. Golden late light. {STYLE}`
- **Motion:** `Static camera. The gull glides slowly from left to right low over the mirror-still water, its reflection follows exactly; masts do not move. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5) · **Резерв LA:** чайка-слой + отзеркаленный слой отражения, движутся синхронно.

### 9G · 0:43–0:52 · средний, со спины · 9 с — крыша в Девятом
- **KF (NB2, рефы: Пелл, Уик):** `Medium shot from behind: {PELL} and {WICK} sit on the ridge of a wooden stilt-house roof, seen from behind, a small cloth bundle between them; far away in the right third of the frame a black tower glows faintly blue-white in its spiral grooves above the city in the golden haze. {STYLE}`
- **Motion:** `Static camera. They sit still, the wind moves their hair, the boy turns his head slightly toward her. {MOTION}`
- **Финал:** MM 10 с (≤5) · **Резерв LA:** статика + `LA-PARALLAX`.
- **Реплика Уика** — `[OS]`/со спины, без синка.

### 9H · 0:52–0:57 · вставка · 5 с — вода под их домом только замедляется
- **KF (NB):** `Insert: dark water among wooden stilts under a house, small ripples and floating straw, late golden light. {WATER_STYLE}. {STYLE}`
- **Движение:** LA — рябь (`displace`) с уменьшающейся амплитудой до ~40% и **не** до нуля (L3: далеко от Шпиля и за домами).

### 9I · 0:57–1:05 · средне-крупный, три четверти со спины · 8 с — «Water doesn't care who you are.»
- **KF (NB2):** `Medium close-up of {PELL} from three-quarter behind, looking toward a distant glowing tower, her mouth barely visible, her left hand resting on a thin cord at her neck that disappears under her oilskin. {STYLE}`
- **Motion:** `Static camera. She speaks a short line with minimal visible mouth movement, her fingers close around the cord at her neck. {MOTION}`
- **Финал:** MM 10 с (≤5) · **Резерв LA:** статика, реплика на мелком рте (`[MS]`, без синка).
- **Приёмка:** осколок не виден (под одеждой) — только шнурок; перстня Руэла в соседних кадрах нет.

### 9J · 1:05–1:15 · общий · 10 с — тон кончился
- **Движение:** LA — `VFX-GROOVE-LIGHT` в обратную сторону: свет уходит **снизу вверх** в горло и гаснет последним; медленнее, чем зажигание. Гавань остаётся стеклом (эффект держится, пока Шпиль не детюнится).

### 9K · 1:15–1:25 · средне-крупный, сбоку-сзади · 10 с — цена
- **Что:** рука Ионы идёт к горлу; она сглатывает дважды и начинает спуск.
- **KF (NB2):** `Medium close-up from behind and slightly to the side of {IONE} in the arched throat of the tower, her face turned away so only the line of her cheek and jaw shows, her right hand rising to the violet band at her throat, golden light, wind in her silver hair. {STYLE}`
- **Motion:** `Static camera. Her hand rises to her throat and rests there; she swallows twice, the throat moving under the band; then she lowers her head and turns away from the opening. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 10 с (≤5) · **Резерв LA:** два кадра (рука опущена / у горла) — наплыв 0,5 с + дыхание.

### 9L · переход · 5 с
- Стеклянная гавань через высокое окно — уже зал (сц. 10). LA: плейт окна + плейт MK-3 «стекло» в окне, наезд. Связь с библиотекой: тот же плейт гавани.

---

## M4 · Сц. 12 — падение (≈0:25)

Правило: показываем **начало и результат, не середину** (production_notes M4). Склейка — на раскрывающейся руке. Тишина вместо стингера.
**Запрет:** в кадрах сцены — перстень Руэла (по сюжету); осколка здесь нет и быть не может. Не делать монтажных рифм «жемчужина ↔ камень» с другими сценами.

### 12A · крупный · 4 с · HERO — «…and the Ninth Sluice—» (липсинк №3)
- **KF (NB2, реф: Лукан, лёгкий):** `Close-up of {LUCAN}, a tall stooped old man with a square white beard, reading aloud from a large map below frame, low last sunlight from a tall window on the left, his lips dry, a faint sheen of sweat. {STYLE}`
- **Motion:** `Static camera, very slow push-in. He reads, then stops mid-word, his eyes lose focus. Mouth closed at the start for lip-sync. {MOTION}`
- **Финал:** K25 5 с + липсинк (≤5) · **Резерв:** по production_notes — `[MS]` над картой, крупно рука.

### 12B · вставка · 2 с · HERO (точка склейки) — рука раскрывается
- **KF (NB2):** `Insert: an old man's right hand with a bronze sickle ring resting on the edge of a large painted map on a table, the fingers half closed. {STYLE}`
- **Motion:** `Static camera. The fingers slowly open and go slack. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5) · **Резерв LA:** два кадра (сжата / раскрыта), склейка на звуке.
- Перстень Лукана — **серп, правая рука** (не путать с чёрной жемчужиной Руэла на левой).

### 12C · средний, верхний ракурс · 4 с · HERO — тело на столе
- **KF (NB2):** `High-angle medium shot of the old man fallen forward across a large map-table, face hidden in his arm, the painted map crumpled and sliding off the far edge of the table under him, colour blocks of noble banners blurred in the background, last sunlight. {STYLE}`
- **Движение:** LA — стоп-кадр с дрейфующей пылью в луче (production_notes: «held frame with drifting dust»).

### 12D · вставка, низкий ракурс у пола · 5 с · HERO — карта скатывается, неподписанная
- **KF (NB2) start/end:** `Low insert at floor level: a large painted map slides off the edge of a table and falls to a stone floor. {STYLE}` / end: `The map lies rolled shut on the stone floor, the blank signature corner visible on the outer edge.`
- **Motion:** `Static camera. The map slips off the table edge, drops to the floor and rolls itself shut, rocking to a stop. {MOTION}`
- **Черновик:** MM 5 с ×2 · **Финал:** K25 5 с start+end (≤5), эскалация K3 · **Резерв LA:** (1) карта-слой уходит за нижний край кадра с ускорением; (2) склейка на звуке; (3) свёрнутая карта на полу, качнулась (поворот слоя ±2°, затухание).
- **Приёмка:** подписи нет; текст на карте — нечитаемые пятна (надписи и тинты — монтажом по мастер-файлу карты).

### 12E · общий, зал · 4 с — зал замер
- LA: стоп-кадр зала (цветовые блоки домов со спины), пыль в луче. Затем Руэл первым на коленях (MS, вне VFX-зоны).

---

## M6 · Сц. 16 — сорок перьев (сигнатура, дёшево)

**Акцент сцены:** медь (Лантри) у высокой конторки; всё остальное — пепельно-серое. Тишина, потом тон.

### 16A · вставка · 4 с — эхо-камень в клетке звенит
- **KF (NB):** `Insert: a small black glassy stone in an ornate brass cage mounted on a dark wall, evening light. {STYLE}`
- **Движение:** LA — `VFX-RELAY-SHIMMER` (блики дрожат три долгих тона и паузу — синхронно со звуком смертного тона). **Без свечения.**

### 16B · общий, симметричный · 6 с · HERO — сорок перьев в воздухе
- **Что:** ряды клерков со спины, все перья подняты и замерли; капля чернил висит; в глубине — одно перо продолжает (Урсула за высокой конторкой).
- **KF (NB2, до 6 попыток — тратим на композицию):**
```
Symmetrical wide shot down the central aisle of a long black-stone counting hall at dusk: rows of identical clerks
in ash-grey coats seen from behind at standing desks, every one of them frozen with a pen lifted in the air above
the page, perfectly still; tall clerestory windows with the last light; at the far end on a high desk a small upright
woman in black and copper is the only one writing. Felt floor, ledgers, water-glasses on every desk. {STYLE}
```
- **Движение:** LA — очень медленный наезд по оси прохода; пыль в лучах; в глубине перо Урсулы — микродвижение слоя (2–3 px). Это стоп-кадр по природе.
- **Приёмка:** клерки одинаковы (одинаковость — замысел), лиц нет; Урсула мала и читается по силуэту и меди.

### 16C · вставка · 3 с — капля чернил
- **KF (NB2):** `Extreme close-up: a steel pen nib held motionless above a ledger page, a single round drop of black ink hanging from its tip. {STYLE}`
- **Motion:** `Static camera. The ink drop swells slowly, detaches and falls onto the page, leaving a small round blot. Nothing else moves. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5) · **Резерв LA:** капля-слой падает с ускорением (8 кадров) + стоп-кадр с кляксой.

### 16D · вставка · 3 с — одно перо продолжает
- **KF (NB2):** `Insert: a small old woman's hand with a copper ring on the right hand, writing steadily with a pen on a ledger at a high desk, the line of neat figures growing. {STYLE}`
- **Motion:** `Static camera. The hand writes calmly to the end of the line, blots it and begins the next. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5) · **Резерв LA:** кадр сбоку-сверху, где кисть мала, движение пера — слой; или кадр без кисти: строка «проявляется» маской слева направо.
- Цифры — нечитаемые (текст не генерируем).

---

## M5 · Сц. 20 — «It's singing back» (≈0:30)

**Карта:** одна комната, одна лампа (тёплая, справа); Пелл сидит на сундуке слева, Уик справа у стола; миска с водой на столе в центре. Акцент — золото лампы. Облик осколка здесь фиксируется на 12 сезонов.
**Звук:** на третьем ударе смертного тона — низкий тон осколка; держится 1 с в чёрном.

### 20A · средне-крупный, руки · 4 с — шнурок из-под плаща
- **KF (NB2):** `Medium close-up of {PELL}'s hands pulling a thin rotted cord out from under the collar of her tar-brown oilskin, lamplight from the right. {STYLE}`
- **Motion:** `Static camera. Her fingers draw the cord up out of her collar slowly until a small dark stone comes free and swings. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5) · **Резерв LA:** два кадра (шнурок у ворота / камень снаружи), наплыв.

### 20B · макро · 6 с · HERO — камень гудит в свете лампы
- **KF (NB2, реф: осколок; затем это эталон предмета):**
```
Macro shot: {SHARD_DESC} hanging still on its cord in front of a dark room, warm lamplight from the right
catching the edge of the crack, the stone small enough to be dwarfed by the two fingertips holding the cord
at the top of frame. {STYLE}
```
- **Motion:** `Locked-off macro. The stone trembles very fast and very slightly on its cord, the cord vibrates, a warm lamp highlight crawls along the crack. The stone does not glow, does not spin. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5) · **Резерв LA:** `VFX-SHARD-TREMOR` (сдвиг ±1–2 px, 12–15 Гц) + блик-слой вдоль трещины.
- **Приёмка:** размер — с ноготь (по пальцам); трещина поперёк; свечения нет. **Перстня нет ни здесь, ни в соседних кадрах.** Этот кадр не используется рядом с жемчужиной ни в каком промо.

### 20C · вставка · 4 с · HERO — миска звенит кольцами
- **KF (NB):** `Insert: a plain clay bowl of water on a wooden table in warm lamplight, the water perfectly still. {STYLE}`
- **Движение:** **LA — `VFX-RINGS`** (тот же элемент и те же параметры, что в 3E, — монтажная рифма «кольца пруда → кольца миски»). Плюс крошки на столе подпрыгивают (по желанию).

### 20D · крупный, тихий · 4 с — Пелл видит
- **KF (NB2):** `Close-up of {PELL} in warm lamplight from the right, staring at something small in front of her face, lips parted but silent, the reflection of rippling water light on her cheek. {STYLE}`
- **Motion:** `Static camera. Her eyes widen slightly, rippling light moves on her face, she does not speak. {MOTION}`
- **Черновик:** MM 5 с · **Финал:** K25 5 с (≤5) · **Резерв LA:** статика + отсвет ряби (маска + `displace`).

### 20E · крупный · 4 с · HERO — «Pell… it's singing back.» (липсинк №5)
- **KF (NB2):** `Close-up of {WICK} in warm lamplight from the left, whispering, eyes fixed on something between them. Mouth closed at the start for lip-sync. {STYLE}`
- **Финал:** K25 5 с + липсинк (≤5) · **Резерв:** мелкий рот в средне-крупном + `[MS]` (по production_notes — допустимо, но этот кадр архивируется для поздних монтажей — постараться выиграть его).

### 20F · средний, снаружи · 3 с — красная тряпка
- **KF (NB2, реф: Мэгс лёгкий):** `Night, medium shot from behind on a plank walkway outside a stilt house: a girl with black frizzy hair tied with a red rag, seen only from behind, stops and turns her head toward the wooden wall, lantern light. No face. {STYLE}`
- **Финал:** MM 5 с (≤5) · **Резерв LA:** два кадра (идёт / голова повернута), склейка.

### 20G · вставка · 3 с — ноги на лестнице
- **KF (NB):** `Night insert: small quick bare feet climbing a wet wooden ladder of a stilt house, hem of an indigo skirt. {STYLE}`
- **Финал:** MM 5 с (≤5) · **Резерв LA:** две позы, склейка.

### 20H · чёрный · 1 с
- Склейка в чёрное на низкой ноте; звук держится 1 с. Без изображения.

---

## Прочие VFX-моменты пилота (дёшево, без героических кадров)

| Сц. | Момент | Приём |
|---|---|---|
| 2, 4 | Шлюзовой Шпиль звучит плоско (виден из окна/над крышами) | MK-4, без свечения (утро), звук |
| 8 | Ступени-спираль внутри Коронного Шпиля, бороздки | плейт PL-0014; спираль по солнцу; без света |
| 13 | Стаканы воды на столах замирают, когда поёт Шпиль | «стекло в миниатюре»: LA — рябь в стакане гаснет (маска), свет Шпиля в окнах (Spire-light вдали, MK-2) |
| 17 | Стена эхо-камней звенит; Одо останавливает один пальцем | `VFX-RELAY-SHIMMER` на плейте стены; у одного камня мерцание обрывается мгновенно |
| 18 | Руки Кес на засове | **точная рамка `S1-SC01-HANDS`** (1E): тот же объектив, ракурс, сторона, засов налево; руки старше, тот же хват; свет — сумерки вместо фонаря |
| 19 | Фонари в дверях загораются; вода вернулась в переулки | `LA-LANTERN-OUT` в обратную сторону; плейт W-1 «сумерки, прилив» |

---

## Смета VFX-кадров пилота (ориентир)

Допущения: клипы тарифицируются по 5 или 10 с (уточняет IT-инженер); ключевые кадры — в среднем 3 попытки NB2 ($0.24 на кадр); «ожидаемо» = 2 финальных дубля; «потолок» = 5 финальных дублей (лимит пилота). Липсинк — отдельно (модель не выбрана).

| Сцена | Кадров | Финалы ожидаемо | Финалы потолок | Черновики MM |
|---|---|---|---|---|
| M1 сц. 1 | 11 (4 HERO) | $8.15 | $20.38 | $1.05 |
| E-1 сц. 2 | 1 | $0 (LA) | $0 | — |
| M2 сц. 3 | 6 (3 HERO) | $2.95 | $7.38 | $0.60 |
| M3 сц. 9 | 12 (4 HERO) | $7.20 | $18.00 | $0.90 |
| M4 сц. 12 | 5 (3 HERO) | $2.10 | $5.25 | $0.45 |
| M6 сц. 16 | 4 (1 HERO) | $1.40 | $3.50 | $0.30 |
| M5 сц. 20 | 8 (3 HERO) | $3.10 | $7.75 | $0.60 |
| **Итого видео** | **47** | **$24.90** | **$62.25** | **$3.90** |

Картинки: ~40 уникальных ключевых кадров × 3 попытки × $0.08 ≈ **$9.60**; библиотечные плейты (MK-1…4, состояния W-1, мастер E-1 до 6 попыток) ≈ **$3.00**.

**Ожидаемо: ≈ $41.4; с резервом 20% — ≈ $50. Потолок (все финалы по 5 дублей): ≈ $79.** Без липсинка, апскейла и звука.
Из 47 кадров **16 — чистая LA** (бесплатно, включая затемнение 20H), **9 — финал на MM**, **18 — K25**, **4 — K3** (1A, 1E, 1J, 9E-вариант B; у 9E есть бесплатный вариант A).

Экономия, заложенная в постановку: свечение Шпиля, стекло гавани, кольца, подъём воды, гаснущие фонари — бесплатные библиотечные элементы, переиспользуемые весь сезон (каждая будущая песня Шпиля ≈ $0 на эффект).
