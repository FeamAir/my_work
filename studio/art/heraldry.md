# HOLLOWSTONE — гербы великих домов и сил S1

Версия 0.1 · 2026-11-22 · автор: художник-концептер · статус: рабочий лист (рисунок гербов зафиксирован в `story/houses/*` и `art_and_music_sheet.md`; всё, что помечено *(предложение)*, — на сверку хранителю канона)
Уровень спойлеров: безопасно для команды и для маркетинга (кроме §5 — гобелен, см. ограничения).

## 0. Как делаем гербы

1. **Мастер-эмблема** — плоский рисунок герба на поле, без текста, по центру квадрата. Это главный референс; всё остальное (знамя, табард, сургуч, вышивка, ткань гобелена) делается **edit-режимом от мастер-эмблемы**.
2. **Бесплатный путь, рекомендую:** мастер-эмблемы можно нарисовать вручную векторно (SVG) — это идеальная точность формы, цвета и **направления спирали**, ноль затрат и легко масштабируется для карты, титров и мерча. AI-генерация тогда нужна только для «живых» вариантов (знамя на ветру, вышивка). В смете (`generation_plan.md`) заложен AI-путь как верхняя граница.
3. **Модели:** черновик — Nano Banana ($0.04), финал мастер-эмблемы — Nano Banana Pro ($0.15) (лучше держит симметрию и плоскую графику). Варианты (знамя, сургуч) — Nano Banana 2 edit ($0.08).
4. **Приёмка:** форма фигуры по описанию, цвета поля/фигуры, нет текста и девизов, спирали по часовой от центра, нет лишних элементов (короны, щитодержатели, ленты с надписями — у нас **их нет**: гербы дельты — знаки на поле, без европейского щита).

**Форма носителя** *(предложение)*: гербы мира — не щиты, а **прямоугольное вертикальное полотнище с косым срезом внизу** (знамя-«вымпел шлюза») для знамён и простой **круг** для печатей и брошей. Это отличает мир от узнаваемой европейской геральдики.

### Общие блоки промпта

`{EMBLEM_STYLE}` =
```
flat heraldic emblem design, bold simple shapes, clean hand-inked outlines in dark umber, flat colour fills with very subtle woven-cloth texture, centred on a plain square field, symmetrical balanced composition, no shield shape, no crown, no supporters, no scroll, no lettering
```
`{EMBLEM_AVOID}` =
```
Avoid: text, letters, mottos, banners with words, shield outline, crown, gradients, 3D bevel, metallic chrome shine, photorealism, extra figures, watermark.
```
Варианты от мастер-эмблемы (edit, Nano Banana 2):
- **Знамя:** `Use the emblem from image 1 exactly. Show it as a tall vertical cloth banner with a slanted cut at the bottom edge, hanging from a dark wooden crossbar in a stone hall, soft side light, cloth folds, same colours, emblem undistorted. {EMBLEM_AVOID}`
- **Табард/вышивка:** `Use the emblem from image 1 exactly, embroidered in thread on the chest of a {colour} tabard, flat front view, fabric texture visible.`
- **Печать/брошь:** `Use the emblem from image 1 exactly, simplified to one colour, as a round {metal} brooch / as an impression in red sealing wax, top view.`

---

## 1. Великие дома (держатели голосов Кольца)

### H-01 Корвейн (HS-001) — «Страж»
- **Описание:** поле **глубокий синий**; **чёрный баклан** с полусложенными крыльями, клювом вниз, входит в стилизованную **серебряную волну с тремя гребнями**. Никогда — баклан с рыбой.
- **Цвета:** `#1F3A68` · чёрный `#15171C` · серебро `#C9CDD2`.
- **Носители:** пряжка-баклан Руэла (серебро), паруса флота (чёрный баклан на синем поле), шлемы морпехов (без герба, чёрный гребень).
- **Промпт:** `{EMBLEM_STYLE}, deep blue field, a black cormorant diving downward with wings half-folded and beak pointing down, plunging into a stylised silver wave with exactly three curling crests at the bottom, the bird's body angled diagonally, no fish. {EMBLEM_AVOID}`

### H-02 Даск (HS-002) — «Сноп»
- **Описание:** поле **охра**; **бронзовый серп лезвием вверх** над **тремя тёмно-коричневыми бороздами**. Не полумесяц: видны рукоять и заточка.
- **Цвета:** `#B88A3E` · бронза `#8C6A35` · борозды `#4A3220`.
- **Промпт:** `{EMBLEM_STYLE}, ochre earth-yellow matte field, a bronze harvest sickle with a short wooden handle, blade curving upward, clearly a tool not a crescent moon, set above three parallel horizontal dark brown ploughed furrows. {EMBLEM_AVOID}`

### H-03 Илвейн (HS-003) — «Бледные»
- **Описание:** поле **бледно-фиолетовое**; **белая открытая правая ладонь**, ладонью к зрителю, пальцы слегка разведены; в ладони **маленький серый спиральный камень** (три витка **по часовой стрелке**). Спираль всегда **в руке**, никогда отдельно.
- **Цвета:** `#B9A6CF` · белый `#F1F0EC` · серый `#8B8F94`.
- **Внимание:** правая рука = большой палец **слева** от зрителя (ладонь к нам). Проверять при приёмке.
- **Промпт:** `{EMBLEM_STYLE}, pale violet field, a white open right hand seen palm-forward with the thumb on the viewer's left, fingers slightly spread, resting in the centre of the palm a small grey stone carved with a spiral of three turns running clockwise from the centre outward. {EMBLEM_AVOID}`

### H-04 Раск (HS-004) — «Лестница»
- **Описание:** **ржаво-красные ворота** — вертикальные прутья и **две** поперечины, **без пик**, — врезаны в **чёрный утёс** угловатых пластов. Поля нет: утёс и есть поле.
- **Цвета:** ржавчина `#8E3B24` (кирпичный оксид, не алый) · чёрный `#1C1A1A` · пласты `#3A3533`.
- **Промпт:** `{EMBLEM_STYLE}, a black cliff face made of angular rock strata filling the whole square, set into it a rust-red iron gate of six vertical bars and two horizontal cross-bars, flat top with no spikes, brick-oxide red not scarlet. {EMBLEM_AVOID}`

### H-05 Квелл (HS-005) — «Буря»
- **Описание:** поле **кость** (тёплый белый); **морско-зелёный угорь** (виден гребень плавника) делает **один полный виток сквозь тёмное железное кольцо**, голова вверх, пасть закрыта. Не змея.
- **Цвета:** `#E8DFC8` · зелень `#5E8A4E` (с жёлтым, **никогда не бирюза**) · железо `#3B3D40`.
- **Промпт:** `{EMBLEM_STYLE}, warm bone-white field, a sea-green eel with a visible dorsal fin ridge along its back, making one full coil through a dark iron ring, head raised upward, mouth closed, yellowish sea-green not teal, clearly an eel not a snake. {EMBLEM_AVOID}`

### H-06 Феннике (HS-006) — «Слушающий дом»
- **Описание:** поле **кислотно-серно-жёлтое**; **серый заяц сидит в профиль**, **оба уха прямо вверх** и чуть врозь, виден один глаз.
- **Цвета:** `#D6C626` (кислота, не золото) · сланец `#4F5A63`.
- **Носители:** серебряная брошь «заячье ухо» (одно ухо — знак семьи; Одо, правый воротник); жёлтая полоса на сланцевом табарде сборщика дани.
- **Промпт:** `{EMBLEM_STYLE}, acid sulphur-yellow field, a grey hare sitting upright in side profile facing left, both long ears raised straight up and slightly apart, one eye visible, calm and alert. {EMBLEM_AVOID}`
- **Брошь (отдельный референс, нужен для пилота):** `a small silver brooch shaped like a single upright hare's ear, slightly curved, fine engraved fur lines, pin back, plain cream background, top view.`

### H-07 Лантри (HS-007) — «Счётный дом»
- **Описание:** поле **чёрное**; **медные коромысловые весы**; в **левой** чаше — **ровная сине-серая поверхность воды**, правая **пуста** — и коромысло **ровное**.
- **Цвета:** `#16161A` · медь `#B56F4A` · вода `#7E8C99`.
- **Носители:** медные пуговицы, весы над дверью банка, ручка трости Урсулы.
- **Промпт:** `{EMBLEM_STYLE}, black field, a copper beam balance with a central post, the beam perfectly level, the left pan holding a flat level surface of blue-grey water, the right pan empty, polished pinkish copper. {EMBLEM_AVOID}`
- **Приёмка:** коромысло горизонтально (модель любит «наклонять» весы — это ломает шутку герба). Если наклонено — правка edit-ом, не перегенерация.

### H-08 Хор (HS-090) *(рисунок — предложение)*
- **Описание:** поле **неотбелённый лён**; **девять коротких чёрных штрихов дугой** (горла Шпиля) над **одной ровной линией**.
- **Цвета:** `#D9CBB0` · чёрный.
- **Внимание:** в зале десятины блок Хора в `production_notes.md` §4 назван «фиолетовый и лён». Предлагаю: знамя — лён с чёрными штрихами (как здесь), фиолетовый — только ленты на горле стюардов Хора. Фиолетовое **поле** — у Илвейнов; два фиолетовых блока рядом в зале смешаются. Вопрос режиссёру.
- **Промпт:** `{EMBLEM_STYLE}, warm undyed coarse linen field with visible weave, nine short vertical black brush strokes arranged in a gentle upward arc, above one straight horizontal black line, austere and calm. {EMBLEM_AVOID}`

### H-09 Должность Хелма и флаг Конкорда *(предложение — на сверку хранителю; в каноне флаг упомянут, но не описан)*
- **Описание:** поле **штормово-серое**; **кольцо из девяти чёрных силуэтов Шпилей**, восемь залиты чёрным, **девятый — только контур** (Затонувший); в центре кольца — **белый круг** (гладь воды).
- **Цвета:** `#8A9097` · чёрный · белый.
- **Почему так:** публичная структура мира (восемь голосов и девятый пустой) читается с одного взгляда, работает на фанатские карты; серый совпадает с «серой» частью мантии Лукана и «серо-синей мантией Хелма» Марен (S7).
- **Опасность:** не путать с сланцем Феннике — серый Хелма светлее и теплее.
- **Промпт:** `{EMBLEM_STYLE}, storm-grey field, a ring of nine slender tower silhouettes standing upright around a plain white disc in the centre, eight towers filled solid black, one tower at the bottom of the ring drawn only as a black outline with an empty interior, evenly spaced. {EMBLEM_AVOID}`

## 2. Силы вне Кольца

### H-10 Оссари (HS-091) *(рисунок — предложение)*
- **Описание:** поле **пыльно-белое**; **песочно-оранжевый ромб-змей** с **хвостом из трёх узлов**.
- **Цвета:** `#ECE6D8` · `#D9A066` (светлый, пыльный — не охра Дасков) · бечева `#7A5A3A`.
- **Внимание:** знаки «мать» и «дом» в коде змеев — отдельная задача (код сдаётся хранителю; не путать герб с сигнальными змеями).
- **Промпт:** `{EMBLEM_STYLE}, dusty white field, a sand-orange diamond-shaped kite seen flat, thin crossed spars visible, a long thin tail string hanging down with exactly three small knots, light dusty orange not ochre. {EMBLEM_AVOID}`

### H-11 Гильдия насосников (HS-092) *(предложение)*
- **Описание:** поле **кирпично-оранжевое** (тёмное, красно-коричневое); **чёрное зубчатое колесо** с **ведром на каждом зубце**.
- **Промпт:** `{EMBLEM_STYLE}, dark brick-orange red-brown field, a black cog-wheel with eight teeth, a small bucket hanging from each tooth, iron-black. {EMBLEM_AVOID}`

### H-12 Подводное течение (HS-093)
- **Описание:** **знамени нет.** Знак — **шнур с тремя узлами**, привязанный к дверному столбу. Делаем не эмблему, а вставку-реквизит.
- **Промпт:** `close-up of a weathered wooden door-post in a stilt-house lane, a short tarred rope-brown cord with exactly three knots tied around it, damp wood, no text.`

### H-13 Тихие (HS-094)
- **Описание:** **спираль, нарисованная в иле пальцем**, — **всегда от руки, никогда печатно**; по часовой от центра. Не печатаем как эмблему; делаем вставку-реквизит.
- **Промпт:** `top-down close-up of wet grey-brown mud, a spiral drawn by a fingertip, three turns running clockwise from the centre outward, uneven hand-drawn groove, no other marks.`
- **Приёмка:** если спираль против часовой — горизонтальное отражение картинки (на ней нет асимметричных якорей), бесплатно.

### H-14 Компания Фонаря (HS-095)
- **Описание:** значок-фонарь на чёрно-медных шарфах (найм Лантри).
- **Промпт:** `{EMBLEM_STYLE}, black field with a thin copper border, a simple copper lantern with a ring handle and four glass panes, flat. {EMBLEM_AVOID}`

### H-15 Слушатели (Феннике)
- Герба нет: **жёлтый шнур на горле** под серым воротником и **заячьи уши** на капюшоне *(предложение `_anchors_matrix.md` §2b)*. Делается в групповом листе C8.

## 3. Угасшие дома (гобелен, история, Пустое кресло)

### H-16 Ашаре (HS-008) — эталон спирали
- **Описание:** поле **глубокая бирюза**; **серебряная спиральная раковина, вид сверху**, спираль **по часовой стрелке от центра наружу**. Это эталон для каждой спирали в сериале.
- **Цвета:** `#1F5E63` · жемчуг `#E6E2DA` · серебро.
- **Где в S1:** бордюры и детали гобелена (S1E1), пустое кресло Затонувшего голоса в Кольце под бирюзой (S1E12).
- **Промпт:** `{EMBLEM_STYLE}, deep teal field, a silver spiral seashell seen from directly above, its spiral turning clockwise from the centre outward, about four turns, pearl-white highlights. {EMBLEM_AVOID}`
- **Приёмка:** направление спирали — обязательный пункт. Отражение для исправления разрешено.

### H-17 Харроу (HS-009)
- **Описание:** поле **мохово-зелёное** (сероватое, старое); **серая борона над зелёным холмом**; белый как второй цвет.
- **Промпт:** `{EMBLEM_STYLE}, muted grey-green moss field, a grey wooden harrow frame with spikes seen flat, set above a rounded green hill with a thin white outline, old faded colours. {EMBLEM_AVOID}`

### H-18 Молл (HS-010)
- **Промпт:** `{EMBLEM_STYLE}, straw-yellow field, a black dike-spade crossed diagonally with a single black reed stalk. {EMBLEM_AVOID}`

### H-19 Остри (HS-011)
- **Промпт:** `{EMBLEM_STYLE}, dark red field, a white lantern on top of a black square tower. {EMBLEM_AVOID}`

### H-20 Вант (HS-012)
- **Описание:** сине-зелёный сланец (сероватый, **не** зелень Квеллов и **не** бирюза Ашаре) + белый.
- **Промпт:** `{EMBLEM_STYLE}, greyish slate blue-green field, a white waterfall pouring between two grey standing stones. {EMBLEM_AVOID}`

## 4. Малые дома, нужные в S1 (кратко)

Шаблон: `{EMBLEM_STYLE}, {поле}, {фигура}. {EMBLEM_AVOID}`. Финал — Nano Banana 2 ($0.08), черновики 2 × $0.04. Генерируем **только когда дом появляется в кадре** (не в смете пилота, кроме Инчли).

| ID | Дом | Поле / фигура (англ.) | S1 |
|---|---|---|---|
| H-21 | Инчли HS-015 (картографы) | `parchment field, a compass-rose drawn as a spiral of fine ink lines turning clockwise from the centre outward, ink black` | **E1 Sc 7** — ливрея рук картографа (обшлаг с вышитым знаком) |
| H-22 | Данмор HS-013 (Седьмой–Двенадцатый шлюзы) | `slate grey field with rust-brown border, a grey sluice-gate with a black key laid across it` | столбы шлюзов Девятого (фон) |
| H-23 | Коббет HS-014 | `slate grey field, a lamp-yellow lantern on a grey dike-post` | Верхние Низы |
| H-24 | Мерриден HS-016 (нотариусы) | `black field, a pale copper seal-ring over a closed black ledger` | Счётный дом |
| H-25 | Уитлоу HS-028 | `deep blue field with white border, a silver anchor through a blue ledger` | флот |
| H-26 | Паллис HS-029 | `white field, a white key with grey outline over a violet book` | стюарды Илвейнов |
| H-27 | Хадден HS-025 | `rust-red field, a black gate-tower with a sand-orange kite flying above it` + костюм: ржавый с **одним** песочно-оранжевым рукавом | Лестница |
| H-28 | Теннант HS-030 | `slate grey field, a grey relay-tower with three pale-yellow rings around it` + костюм: сланец с бледно-жёлтой полосой-кольцом | Ретранслятор |
| H-29 | Рэй HS-033 («печать Конкорда») | `iron grey field, a black barrel with a white ring-stamp` | Арсенал |
| H-30 | Гиллам, Келлоу, Даск из Предела, кланы Квеллов, Грелл, Корвейн Дорог, Орсли, Килбрайд | по `art_and_music_sheet.md` §4 | по мере появления |

## 5. Гобелен «Разлом»: знамёна Девяти (архаичные формы)

Панель «Девять и основание Конкорда» показывает **девять семей-хранителей** (канон, `timeline.md`): Корвейн, Даск, Илвейн, Квелл, Харроу, Вант (Шпили) и Раск, Молл, Остри (мечи). **Феннике и Лантри на гобелене нет** (их тогда не было у Кольца). Детали панели — **на сверку хранителю** (правило выдержки §2).

Предложение по архаике: те же фигуры, что в §1–§3, но **грубее и проще** (тканый рисунок, 3–4 цвета нити), металлы — светлой и охристой нитью. Менять сами фигуры (например, «старый» герб без волны у Корвейнов) — только по решению хранителя; по умолчанию — современные формы, упрощённые ткачеством.

Порядок знамён на берегу *(предложение)*: шесть «шпилевых» семей в центре, три семьи меча по краям (Раск, Молл слева; Остри справа). Знамя Корвейнов — ещё и на парусе (отдельная панель с парусом-бакланом). Подробно о гобелене и о том, какие панели можно показывать вне серий, — `pilot_references.md`, E-06.
