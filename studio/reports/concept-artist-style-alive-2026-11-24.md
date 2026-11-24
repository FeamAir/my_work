# Концепт-художник — тест стиля «живее» (2026-11-24)

Задача: отзыв инвестора «очень похоже на комикс, хочу живее, уровень анимационного фильма». Шаг 1: диагноз (бесплатно). Шаг 2: три направления рендера × 2 сюжета на NB2 edit.

**Лист сравнения:** `studio/direction/refs/STYLE_ALIVE/style_alive_compare.jpg` (2688×2721, 1.0 МБ). Я его просмотрел.
**Потрачено:** 10 изображений × $0.08 = **$0.80** (лимит $0.80; 6 основных + 4 пересъёмки). Остаток бюджета по `pipeline.costs`: $47.7.

## 1. Диагноз: почему читается как комикс

Смотрел мастера CH-0001 Пелл, CH-0007 Вик, CH-0015 Нан, CH-0003 Холлис, кадр `keyframes/test_pell_wick_nan_house_v1.png` и 6 кадров аниматика (sc01 sh050/sh120, sc02 sh050/sh120/sh150/sh190).

1. **Контур одинаковый и тёмный.** Сине-чёрная линия почти одной толщины обводит всё, включая внутренние складки, веснушки и вязку свитера Вика. Она не тоньше на свету и не рвётся. Это главный «комиксный» признак. STYLE_BASE прямо требует «crisp ink outlines».
2. **Плоская cel-заливка с двумя жёсткими тонами** (§2 библии: «мягкие переходы — нет»). Формы лица и рук не поворачиваются, щёки и нос одного цвета с челюстью, нет подповерхностного тепла.
3. **Плоский свет на листах.** На мастерах «flat even neutral lighting» и пустой светло-серый фон. Нет контрового света и отражённого света, поэтому персонажи выглядят вырезанными. В кадрах это переносится: в `test_..._house_v1` фигуры обведены и залиты, а комната написана живописно, и персонажи выглядят наклеенными на фон.
4. **Скованные позы.** Все мастера стоят прямо в три четверти, руки висят или сложены, вес на обеих ногах, нейтральное лицо. В кадре дома Пелл стоит «как на листе», Вик повторяет позу с листа.
5. **Мёртвые глаза.** Блик есть, но один и плоский. Радужка однотонная, нет тени от верхнего века, взгляд не сфокусирован («смотрит в камеру» вместо «смотрит на кого-то»).
6. **Аниматик:** фоны хорошие (дымка, мокрый камень), но персонажи в sc01-sh120 и sc02-sh190 — та же обводка и заливка поверх живописного фона. Свет в кадрах не моделирует персонажа: нет контрового света из окна или от фонаря.
7. **Причина в системе.** STYLE_BASE §10.1 и §1–2 *предписывают* комиксный рендер (ink outlines, flat fills, two shadow tones, highlights restrained). Модель делает ровно это. Менять нужно текст STYLE_BASE и **мастера-референсы** (см. п. 3.1).

## 2. Три направления: варианты STYLE_BASE

Дизайн, палитра (teal-black, violet-blue тени, приглушённость) и канон-якоря не меняются. Полные промпты, рефы и seed — в `studio/art/style_alive/meta.json` (копия: `refs/STYLE_ALIVE/meta.json`), генератор: `studio/art/style_alive/gen_style_alive.py`.

**А — 2D полнометражный (STYLE_BASE_A)**
```
Feature-quality 2D hand-drawn animated film still, original character and world design. Refined clean line art with thin tapered lines of varied weight: slightly heavier on the outer contour and in shadow, thinning and breaking where light hits the form; line colour tinted by the local colour, not uniform black. Soft multi-tone shading with gentle gradients over faces, hands and clothes, warm bounce light filling the shadows, a thin rim light separating figures from the background. Subtle skin colour variation: warmer cheeks, nose tip and ears, cooler jaw and temples. Expressive eyes with layered iris colour, a soft upper-lid shadow and clear catchlights; brows and eyelids shaped by the emotion. Hair in soft locks with light passing through the edges. Atmospheric depth: layered haze, softer and cooler in the distance, painted environment. Muted desaturated palette with deep teal-black shadows and cool violet-blue shadows, subtle film grain, grounded epic fantasy.
```
**Б — живописный (STYLE_BASE_B)**
```
Painterly animated feature film still, original character and world design. Characters painted with visible textured brush strokes over a light underdrawing; outlines appear only in shadowed edges and dissolve into light on the lit side. Shading built from soft brushy planes of warm and cool colour, light wrapping around faces and hands, glowing edges where light catches hair and skin. Cinematic motivated lighting with clear light-and-shadow shapes, dust in the light beam, damp air. Rich detailed painted environment with depth, wet reflective surfaces, tactile wood, rope and cloth. Muted desaturated palette with deep teal-black shadows and cool violet-blue shadows, subtle canvas grain, grounded epic fantasy.
```
**В — стилизованный 3D-объём (STYLE_BASE_C)**
```
Stylized 3D animated feature film still, original character and world design. Keep exactly the stylized proportions and facial design of the reference sheets, translated into soft sculpted volumes. Soft skin with gentle subsurface warmth in ears, nose and fingertips, soft global illumination and contact shadows, a soft area light from the main light source, subtle rim light. Hair as sculpted soft locks with fine strand texture at the edges. Fabrics with tactile texture: tarred oilskin, knitted wool, worn linen. Hand-painted simplified textures, stylized and not photoreal, shallow depth of field, atmospheric haze. Muted desaturated palette with deep teal-black shadows and cool violet-blue shadows, grounded epic fantasy.
```
Общий негатив добавляет: `comic book look, heavy uniform black outlines, flat cel shading with hard two-tone shadows, halftone dots, crosshatching, stiff frontal pose, plain empty background`. Для В дополнительно: `realistic skin pores, uncanny realistic face, glossy plastic toy look, doll eyes`.

## 3. Результаты

| Файл (`refs/STYLE_ALIVE/`) | В листе | Оценка |
|---|---|---|
| `A_pell.jpg` | да | Заметно живее: окружение, свет из окна, контровой свет на волосах, полуулыбка, рука тянет ремень сумки. Линия всё ещё довольно ровная. Прядь на щеке похожа на слезу (мелочь). |
| `B_pell.jpg` | да | **Лучший кадр:** луч света с пылью, лицо мягко вылеплено светом, тёплый рефлекс, глаза живые, цвет волос ближе к rust. |
| `C_pell.jpg` | да | Объём и подповерхностное тепло, но получилось «2.5D-живопись», а не настоящее 3D. Лицо немного взрослее и тяжелее. |
| `A_house.jpg`, `B_house.jpg`, `C_house.jpg` | нет | **Брак теста:** со старым кадром как image 1 NB2 почти копирует его, стиль не меняется. Значок на куртке повторён из старого кадра. |
| `A_house_r1.jpg`, `B_house_r1.jpg`, `C_house_r1.jpg` | да | Пересъёмка без старого кадра (плейт + 6 листов). Стал живее свет: лучи из двери и окна, пыль, глубокие углы. Б даёт самую живую мизансцену (Нан склонилась над сетью). Рендер персонажей при этом почти не изменился: комнату и людей держат плейт и листы в старом стиле. |
| `C_house_r2.jpg` | нет | Отбракован: «сделай всё 3D» не сработал, и Пелл получила фартук и юбку Нан (дрейф костюма). |

### Проверка якорей и лиц
- **Коса Пелл** на правой стороне кадра, одна, жетон на кончике: 3/3 портретов и 3/3 r1. В кадрах v1 жетон на куртке (унаследован от старого кадра); в r1 исправлено.
- **Серьга Нан**: одна, на правой стороне кадра, во всех кадрах дома. Мелко, направление спирали на этом масштабе не читается.
- **Вик:** без кепки, свитер и вихор на месте. В профиль вихор читается слабо.
- **Костюм Пелл в кадрах дома:** в A_r1 и C_r1 сетка-сумка надета как жилет поверх куртки, это дрейф. В B_r1 куртка верная.
- **Лица:** на портретах это та же Пелл (разрез глаз, веснушки, причёска, цвет). В В черты чуть тяжелее. В кадрах дома лица мелкие и согласованы с листами.

### 3.1 Главный вывод теста
**Стиль сидит в референсах, а не только в тексте промпта.** Портрет, сделанный только с мастера и разворота, сменил рендер. Кадр, где плейт и 6 листов нарисованы в Tidemark, почти не меняется. Значит, смена стиля — это **ремастер референсов**: сначала мастера и развороты главных героев и 2–3 ключевых плейта в новом стиле, затем все кадры от них. Один STYLE_BASE не поможет. Оценка: ~15 героев × (мастер + разворот) + ~10 плейтов ≈ 40 изображений NB2 ≈ $3.2 + пересъёмки, итого ~$5.

## 4. Рекомендация

**Рекомендую А как базу и взять из Б свет («А+»):** тонкая переменная линия, многотоновая мягкая тень, контровой и отражённый свет, живые глаза. Из Б — мотивированные лучи, пыль, тёплый рефлекс в тенях. Живописную фактуру мазка из Б не берём.

Почему так, с учётом Kling и 450 планов:
- **Устойчивость в видео.** Kling на чистых формах с тонкой линией и мягкими градиентами держит персонажа лучше всего: мало мелкой фактуры, которая «кипит» между кадрами. **Б** в видео рискованнее всех: мазки и фактура холста мерцают и плывут от кадра к кадру. На 450 планах это заметный брак, хотя стоп-кадр Б самый красивый.
- **Реализм движения.** **В** (3D-объём) потенциально даёт самое естественное движение в Kling: модель обучена в основном на объёмном видео, линия не мерцает, свет поворачивается вместе с формой. Но тест показал, что NB2 из 2D-листов настоящее 3D не делает (C_house_r1, r2 — по сути 2D). Для В нужен полный ремастер всех рефов в 3D и отдельная проверка лиц. Риск: «пластиковость» и уход лиц в зловещую долину. Это смена всего пайплайна, а не правка.
- **А** ближе всего к текущему пайплайну и правилам (якоря по стороне кадра, листы). Ремастер дешёвый и даёт явное «живее», чего и просит инвестор.
- Отдельно, независимо от стиля, **живость дают постановка и свет**: позы с весом и действием, взгляд на партнёра, мотивированный контровой свет. Это прописать в шотлисте и в §10 библии.

## 5. Открытые вопросы и следующий шаг

1. **Нужно решение директора и режиссёра:** А+ или проверка В. Предлагаю перед решением проверку движения в Kling: один и тот же план (портрет Пелл, 5 с, Kling 2.5 Turbo) из A_pell, B_pell и C_pell, 3 × $0.35 = **$1.05**. Это покажет, что мерцает. Нужно разрешение на платные вызовы.
2. После выбора: правка §1, §2, §10.1, §10.3 и §10.4 визуальной библии (режиссёр; сейчас там требование «crisp ink outlines, flat fills»), затем ремастер рефов (~$5) с моей стороны.
3. Мастер-листы: в новом стиле делать их **не на пустом сером фоне**, а со светом от источника и простым окружением. Нейтральный лист для ID держать отдельно.
4. Хранителю канона: якоря не затронуты, правок канона не требуется.
5. Названия студий и художников в промптах не использовались.

## Файлы
- `studio/direction/refs/STYLE_ALIVE/style_alive_compare.jpg` — лист сравнения (Сейчас / А / Б / В)
- `studio/direction/refs/STYLE_ALIVE/*.jpg` — все 10 генераций (превью jpg, 1376 px), `meta.json` — промпты, рефы, seed
- `studio/art/style_alive/gen_style_alive.py`, `studio/art/style_alive/meta.json`
- исходники PNG: `output/style_alive/` (не коммитятся)
