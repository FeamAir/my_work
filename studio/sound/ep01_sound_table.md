# Звуки серии EP01 «Кит над крышами»

Версия 1.0 от 2026-11-22. Автор: звукорежиссёр.
Источники: `studio/story/ep01_script.md` v1.0; `voices.md`; `whale_song.md`; `leitmotifs.md`; правила — `sound_bible.md`, `sfx_music_workflow.md`, `mix_plan.md`.
Статус: план (без генерации).

> **Таймкоды оценочные (`TC≈`).** Шот-листа `studio/direction/ep01_shotlist.md` на момент сдачи нет. Таймкоды взяты по хронометражу сцен сценария. Длительность реплик оценена так: Сора ≈ 13 симв./с, Нацу ≈ 16, Гэн ≈ 10–11 с паузами. Когда появится шот-лист, ID звуков не меняются, пересчитываются только колонки TC.
>
> Место файла: директор указал `studio/sound/ep01_sound_table.md`. В `sfx_music_workflow.md` раньше значилось `episodes/epNN_sound_list.md`. Принимаем путь директора: `studio/sound/epNN_sound_table.md`.

Хронометраж: сцены 0:00–2:45 по сценарию, затем заставка-титр 2:45.5–2:52.5 (см. `leitmotifs.md` п. 5). Итого ≈ **2:53**.

---

## 1. Сводка по сценам (порядок событий)

| Сцена | TC≈ | Эмбиент | Ключевые звуки | Музыка | Реплики |
|---|---|---|---|---|---|
| sc01 Крыша, закат | 0:00–0:25 | крыша-закат | бумага журавлика, порыв ветра, камешек | L1 Сора (с 0:03) | dx01, dx02 |
| sc02 Улица, закат | 0:25–0:45 | улица-закат | велосипед, газеты, **музыка обрывается**, тень, треск фонарей | L5 Нацу → тишина → L3 Тень | dx03–dx05 |
| sc03 Небо, закат | 0:45–1:15 | небо + присутствие кита | скрип-рост бумаги, глаз-штемпель, **песня кита (тревожная)**, отрыв листа | L4 Кит | dx06, dx07 |
| sc04 Крыша, закат | 1:15–1:35 | крыша-закат + кит | кружение листа, поимка, конверт | L4 Кит (истончается) | dx08, dx09 |
| sc05 Почтовый дом, сумерки | 1:35–2:00 | интерьер + **часы** | дверь, бег по доскам, очки, конверт, кит за окном | без музыки → L2 Гэн (с 1:50) | dx10–dx13 |
| sc06 Улица, дом № 14, сумерки | 2:00–2:30 | улица-сумерки, гул фонарей | шаги, **тишина → щелчок ящика**, окно, шов, **песня кита (мягкая)** | без музыки → THEME «Доставка» (с 2:20) | dx14–dx17 |
| sc07 Крыша/небо, ночь | 2:30–2:45 | крыша-ночь | «швартовка» к башне, второй лист, поимка, порыв ветра, срез в тишину | L7 «Мама · письмо» | — |
| Титр | 2:45.5–2:52.5 | — | — | заставка (THEME intro) | — |

Без музыки ≈ 37 с из 172 (≈ 21 %): 0:00–0:03, 0:36–0:37.5, 1:35–1:50, 2:00–2:20 (с учётом наложений).

---

## 2. Диалог (DX)

Общие правила:
- Модель и настройки — из карточек `voices.md`. Режимы: **Б** — базовый, **Э** — эмоциональный, **Т** — тихий.
- Каждая реплика — отдельный клип, 3 дубля (разный seed). Уровень −16 LUFS на реплику (крик до −13, шёпот до −22), панорама C.
- `previous_text` / `next_text` (поддерживаются клиентом IT) — соседние реплики сцены. Это помогает интонации и не попадает в звук.
- Реплики **В КАДРЕ** нужны до липсинка: озвучка идёт в конвейере **раньше** видео-липсинка (audio-first).
- Текст для TTS отличается от сценарного только там, где это нужно движку. Правки отмечены в «Прим.». Ударения в именах — через словарь (`voices.md`, раздел 6).

| ID | Сц. | TC≈ | Персонаж | Подача | Текст сценария | Текст для TTS | Режим | Длит.≈ | Факт | Прим. |
|---|---|---|---|---|---|---|---|---|---|---|
| ep01_dx_01 | sc01 | 0:04.0–0:11.3 | Сора | З.К., тихо, задумчиво | Говорят, если сложить тысячу журавликов, можно сказать то, что не получается сказать вслух. | Говорят, если сложить тысячу журавликов... можно сказать то, что не получается сказать вслух. | Т | 7.3 с | — | многоточие = паузы-вдох посередине |
| ep01_dx_02 | sc01 | 0:18.5–0:23.0 | Сора | З.К., с лёгкой самоиронией | У меня их уже сто двенадцать. А сказать всё ещё нечего. | У меня их уже сто двенадцать. А сказать всё ещё нечего. | Т | 4.5 с | — | число уже словами; «всё ещё» с ё |
| ep01_dx_03 | sc02 | 0:31.0–0:33.5 | Нацу | В КАДРЕ, громко, насмешливо | Эй, Почтовая! Опять журавлей пасёшь? | Эй, Почтовая! Опять журавлей пасёшь? | Э | 2.5 с | — | крик снизу вверх, −14 LUFS |
| ep01_dx_04 | sc02 | 0:35.0–0:35.7 | Сора | В КАДРЕ, спокойно | Пасу. | Пасу. | Б | 0.7 с | — | `previous_text` = dx_03; иначе одно слово выходит вопросом или обрывком. 3–5 дублей |
| ep01_dx_05 | sc02 | 0:42.4–0:43.8 | Нацу | В КАДРЕ, растерянно, тише | …Это ещё что? | Это ещё что? | Т | 1.4 с | — | ведущее многоточие убрано (даёт артефакт на старте); паузу даёт монтаж |
| ep01_dx_06 | sc03 | 1:03.0–1:04.8 | Сора | З.К., шёпотом, заворожённо | Кит. Из бумаги. | Кит. Из бумаги. | Т | 1.8 с | — | шёпот −20…−22 LUFS; в варианте v3 — тег шёпота |
| ep01_dx_07 | sc03 | 1:13.0–1:14.6 | Нацу | В КАДРЕ, снизу, кричит | Сорка! На тебя летит! | Сорка! На тебя летит! | Э | 1.6 с | — | ударение Со́рка — словарь; −13 LUFS; **после** хвоста песни кита |
| ep01_dx_08 | sc04 | 1:23.5–1:26.5 | Сора | З.К., читает медленно, удивлённо | «Улица Ступеней, дом четырнадцать»… | Улица Ступеней... дом четырнадцать... | Т | 3.0 с | — | кавычки убраны; интонация чтения по слогам — паузами |
| ep01_dx_09 | sc04 | 1:31.5–1:33.3 | Сора | В КАДРЕ, тихо, себе | Ты… потерял письмо? | Ты... потерял письмо? | Т | 1.8 с | — | |
| ep01_dx_10 | sc05 | 1:38.5–1:40.5 | Сора | В КАДРЕ, взволнованно | Деда! Там… в небе… | Деда! Там... в небе... | Э | 2.0 с | — | запыхавшись; единственный «громкий» момент Соры |
| ep01_dx_11 | sc05 | 1:49.5–1:51.6 | Гэн | В КАДРЕ, очень тихо, с тяжестью | Значит, он вернулся. | Значит... он вернулся. | Э | 2.1 с | — | многоточие = пауза перед важным словом (манера Гэна); −18 LUFS |
| ep01_dx_12 | sc05 | 1:52.2–1:53.2 | Нацу | В КАДРЕ, недоверчиво | Кто — «он»? | Кто — он? | Б | 1.0 с | — | кавычки убраны; ударение на «он» задаёт `previous_text` = dx_11 |
| ep01_dx_13 | sc05 | 1:54.0–1:59.8 | Гэн | В КАДРЕ, медленно, с паузой | Письмо не опаздывает, внучка. Опаздывают люди. Отнеси. | Письмо не опаздывает, внучка... Опаздывают люди. Отнеси. | Б | 5.8 с | — | **риск перебора сцены** (см. ниже). Запасной путь: 2 клипа («…внучка» / «Опаздывают люди. Отнеси.») и пауза 0.6 с в монтаже |
| ep01_dx_14 | sc06 | 2:06.5–2:10.7 | Нацу | В КАДРЕ, вполголоса, скептически | Там живёт старая госпожа Оно. Она лет десять никому не открывает. | Там живёт старая госпожа О́но. Она лет десять никому не открывает. | Т | 4.2 с | — | **«О́но» — ударение в тексте** (омограф «оно́»), см. `voices.md` п. 6 |
| ep01_dx_15 | sc06 | 2:11.4–2:14.4 | Сора | В КАДРЕ, тихо, решительно | Ей не надо открывать. Это же письмо. | Ей не надо открывать. Это же письмо. | Б | 3.0 с | — | |
| ep01_dx_16 | sc06 | 2:26.6–2:27.9 | Нацу | В КАДРЕ, ошеломлённо, почти шёпотом | …Он зашился. | Он зашился. | Т | 1.3 с | — | ведущее многоточие убрано; −20 LUFS |
| ep01_dx_17 | sc06 | 2:28.2–2:30.5 | Сора | З.К., тепло | Одно письмо. Один стежок. | Одно письмо... Один стежок. | Т | 2.3 с | — | заходит на 0.5 с в sc07 (L-cut), это допустимо |

Итого: 17 реплик (Сора 9, из них 5 закадровых; Нацу 6; Гэн 2), ≈ 545 символов. Три дубля ≈ 1 650 символов TTS.

**Риск хронометража sc05.** В сцене 25 с, а действия и реплик в ней на ≈ 26–27 с при медленном темпе Гэна (speed 0.88). Чтобы уложиться, я сжал паузы между dx_11 → dx_12 → dx_13 до 0.6–0.8 с. Если фактическая длина dx_13 больше 6 с, сцену нужно удлинить на 1–2 с за счёт sc04 или sc07 (там нет реплик) — это решают сценарист и режиссёр.

---

## 3. Эмбиент (AMB)

База — петля (`loop: true`), растягивается `aloop` до длины сцены. Детали — отдельные one-shot файлы (раздел 4, тип AMB-d). Все эмбиенты библиотечные (`lib_`): локации повторяются весь сезон. Модель SFX `eleven_text_to_sound_v3`.

| ID | Сц. | TC≈ | Локация / вариант | Промпт (EN) | Длит. | Loop | p_inf | LUFS | Подпись локации |
|---|---|---|---|---|---|---|---|---|---|
| lib_amb_roof-sunset | sc01, sc04 | 0:00–0:25.5; 1:14.5–1:35.5 | Л2 крыша, закат | `Rooftop of a small seaside hill town at sunset: steady gentle wind, laundry flapping softly on lines nearby, distant calm sea waves far below, a few faraway seagulls, quiet and peaceful, no traffic, no music, no speech` | 30 с | да | 0.35 | −32 | хлопанье белья + далёкие чайки |
| lib_amb_street-steps-sunset | sc02 | 0:24.5–0:45.5 | Л3 улица Ступеней, закат | `Quiet stone stairway street in a small seaside town at sunset: light wind humming through overhead wires, distant gentle sea waves at the bottom of the hill, a far-off seagull, faint creak of a hanging laundry line, very calm, no cars, no music, no speech` | 30 с | да | 0.35 | −32 | гул ветра в проводах |
| lib_amb_sky-high | sc03 | 0:44.5–1:15.5 | Л5 небо над городом | `High open sky over a town at sunset: wide airy wind at altitude, soft whooshing gusts, distant sea far below, spacious and empty, no birds close by, no music, no speech` | 30 с | да | 0.3 | −30 | высотный ветер |
| lib_amb_whale-presence | sc03–sc04, sc06 (тихо), sc07 | 0:46–1:35; 2:21–2:30; 2:30–2:45 | присутствие кита (слой поверх локации) | `Slow, enormous, distant creaking and rustling of thousands of paper sheets drifting overhead, soft papery flutter, faint low airy drone, calm and continuous, wide stereo, no music, no speech` | 30 с | да | 0.35 | −32 (sc06/07: −36) | бумажный шорох сверху = «кит рядом» |
| lib_amb_postoffice-int | sc05 | 1:34.5–2:00.5 | Л1 почтовый дом, интерьер, сумерки | `Quiet old wooden post office interior at dusk: soft room tone, faint electric hum of an old desk lamp, muffled wind outside the windows, occasional soft creak of wooden floorboards, calm, no clock, no music, no speech` | 30 с | да | 0.35 | −34 | — (часы — отдельно, ниже) |
| lib_amb_postoffice-clock | sc05 | 1:34.5–2:00.5 | Л1, **подпись** | `Old round wall clock ticking steadily in a quiet wooden room, clear mechanical tick, medium-close perspective, no other sounds` | 20 с | да | 0.6 | −30 | **тиканье часов** (в первые 2 с сцены) |
| lib_amb_street-steps-dusk | sc06 | 1:59.5–2:30.5 | Л3 улица, синие сумерки | `Quiet stone stairway street in a seaside town at blue dusk: faint warm buzz of old street lamps, first crickets, distant soft sea waves, light breeze in overhead wires, still and hushed, no cars, no music, no speech` | 30 с | да | 0.35 | −33 | гудение фонарей |
| lib_amb_roof-night | sc07 | 2:29.5–2:45.0 | Л2 крыша, ночь, луна | `Rooftop of a seaside hill town at night: soft steady wind, crickets, very distant calm sea, a faint laundry flap, peaceful moonlit night, no music, no speech` | 30 с | да | 0.35 | −33 | ветер + сверчки |

Переходы между сценами: J-cut 0.5–1 с (эмбиент следующей сцены начинается раньше картинки), кроссфейд 0.3–0.5 с. Исключение — **sc07 → титр**: жёсткий срез всего звука в 2:45.0 (затемнение), 0.5 с тишины, затем первая нота заставки.

---

## 4. SFX: жёсткие, фоли, дизайн, детали эмбиента

Модель `eleven_text_to_sound_v3`, длительность задаётся явно, 2–3 дубля. Поле **Библ.**: `lib` — переиспользуемый на сезон, `ep` — только для этой серии.

| ID | Сц. | TC≈ старт | Синхро-точка | Тип | Описание (RU) | Промпт (EN) | Длит. | p_inf | LUFS | Пан. | Библ. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ep01_sfx_01 | sc01 | 0:07.5 | сгиб 0:08.6 | FOLEY | Пальцы загибают крыло журавлика | `Close-up of fingers carefully folding a small sheet of origami paper, two crisp creases and a soft paper slide, quiet and intimate` | 3 | 0.6 | −28 | C | lib |
| ep01_sfx_02 | sc01 | 0:12.0 | стук 0:12.6 | FOLEY | Журавлик ставят на трубу, сверху кладут камешек | `A tiny paper crane placed on a brick ledge, then a small pebble set down on it with a light stone tap on brick` | 2 | 0.6 | −28 | R20 | lib |
| ep01_sfx_03 | sc01 | 0:14.5 | пик 0:15.8 | AMB-d | Порыв ветра на крыше | `Sudden gust of wind sweeping across a rooftop, rising and falling, fabric and laundry snapping briefly, no howl` | 3 | 0.5 | −26 | stereo | lib |
| ep01_sfx_04 | sc01 | 0:15.6 | прижатие 0:16.6 | FOLEY | Журавлик трепещет, Сора прижимает его камешком | `Small paper crane fluttering in the wind against brick, then quickly pressed down, soft paper rattle and a light pebble tap` | 2 | 0.6 | −28 | R20 | ep |
| ep01_sfx_05 | sc01 | 0:20.0 | — | FOLEY | Шарф хлопает на ветру (крупный план) | `Long knitted scarf flapping softly in the wind, close perspective, gentle fabric flutter` | 4 | 0.5 | −30 | C | lib |
| ep01_sfx_06 | sc02 | 0:25.0 | — | FOLEY | Нацу ведёт велосипед вверх по пандусу: трещотка колеса, шаги кед по камню | `Old bicycle being walked uphill on a stone ramp: steady freewheel ticking, light sneaker footsteps on stone, a gentle rattle of a wire basket` | 6 | 0.55 | −26 | L30→C | lib |
| ep01_sfx_07 | sc02 | 0:30.0 | стоп 0:30.4 | FOLEY | Велосипед останавливается: короткий скрип тормоза, корзина звякает | `Old bicycle coming to a stop: short soft brake squeak and a wire basket rattling once` | 1.5 | 0.6 | −26 | C | lib |
| ep01_sfx_08 | sc02 | 0:34.0 | — | FOLEY | Сора машет с крыши (шорох рукава кардигана, далеко) | `Soft rustle of a knitted sleeve as someone waves, distant perspective` | 1 | 0.5 | −34 | R30 | ep |
| ep01_sfx_09 | sc02 | 0:36.3 | — | FOLEY | Нацу тянется к газете, газеты шуршат под бечёвкой | `Bundle of newspapers tied with string, a hand pulling at the top paper, dry newsprint rustle, close` | 1.5 | 0.6 | −28 | C | lib |
| ep01_sfx_10 | sc02 | 0:37.0 | обрыв музыки 0:36.0 | DES | Тень ползёт по улице: давление воздуха, низкий нарастающий гул | `Low slow rising swell of air pressure, deep soft whoosh as a huge shadow moves over a street, subtle rumble, no impact` | 6 | 0.5 | −24 | stereo | lib |
| ep01_sfx_11 | sc02 | 0:39.0 | 0:39.3 / 0:40.4 / 0:41.4 | HARD | Фонари мигают один за другим: электрическое потрескивание, 3 вспышки, удаляются вниз по улице | `Old street lamps flickering one after another: three short electric buzz-crackles, each one slightly farther away down the street` | 3.5 | 0.6 | −24 | L20→R40 | lib |
| ep01_sfx_12 | sc03 | 0:45.0 | — | DES | Из-за крыш выплывает плавник: огромный бумажный скрип-шелест нарастает | `Gigantic sheet of folded paper slowly bending and creaking as it rises, deep papery groan and swelling rustle, enormous and slow` | 7 | 0.5 | −22 | stereo | lib |
| ep01_sfx_13 | sc03 | 0:54.5 | вспышка 0:55.5 | DES | Глаз-штемпель загорается изнутри: тёплое «гудение света» | `Warm soft glow igniting: low gentle hum rising with a faint airy shimmer, like a lantern lighting from inside, magical, subtle` | 3 | 0.5 | −24 | C | lib |
| ep01_sfx_14 | sc03 | 1:02.5 | — | FOLEY | Сора встаёт на черепице; шарф и косичка на ветру | `Girl standing up slowly on clay roof tiles, a soft tile clink, fabric rustle, scarf fluttering in wind` | 3 | 0.55 | −28 | C | ep |
| ep01_des_whale_alarm | sc03 | 1:05.5 | пик 1:08.5 | DES | **Песня кита — тревожная** | см. `whale_song.md` п. 4.1 (сборка из слоёв) | 7 | — | −16 | stereo | lib |
| ep01_sfx_15 | sc03 | 1:09.8 | отрыв 1:10.2 | DES | От брюха отрывается лист: мягкий бумажный надрыв и начало кружения | `A single large sheet of old paper tearing softly away from a bigger paper mass, gentle rip, then light fluttering as it begins to fall` | 3 | 0.55 | −24 | C | lib |
| ep01_sfx_16 | sc04 | 1:15.0 | — | FOLEY | Лист кружит над крышей, приближается | `Single sheet of paper fluttering and spinning as it falls through the air, approaching from far to close, light airy flaps` | 4.5 | 0.55 | −26 | L20→C | lib |
| ep01_sfx_17 | sc04 | 1:19.2 | поимка 1:19.6 | FOLEY | Сора ловит конверт обеими руками | `Hands catching a paper envelope out of the air, a soft slap of paper against palms, close` | 1 | 0.65 | −24 | C | lib |
| ep01_sfx_18 | sc04 | 1:20.5 | — | FOLEY | Крупно: конверт в руках, загнутый уголок | `Old stiff paper envelope handled close to the microphone, fingers sliding along the edge, a corner being straightened` | 2.5 | 0.6 | −28 | C | lib |
| ep01_sfx_19 | sc04 | 1:27.5 | вспышка 1:28.0 | DES | Глаз-штемпель смотрит на Сору: повтор свечения, тише | = ep01_sfx_13 (переиспользование, −4 dB) | 3 | — | −28 | C | lib |
| ep01_sfx_20 | sc05 | 1:37.0 | удар двери 1:37.4 | HARD | Сора врывается: деревянная раздвижная дверь резко отъезжает | `Old wooden sliding door pulled open quickly and hitting its frame, wooden rattle of glass panes, interior perspective` | 1.5 | 0.6 | −22 | L30 | lib |
| ep01_sfx_21 | sc05 | 1:37.3 | — | FOLEY | Шаги бегом по тёмным доскам: ботинки Соры, за ней кеды Нацу | `Two pairs of quick footsteps running into a room on old wooden floorboards, boots first then sneakers, slight creaks` | 2.5 | 0.55 | −26 | L30→C | lib |
| ep01_vox_01 | sc05 | 1:40.8 | — | VOX | Нацу запыхалась: два коротких выдоха | TTS голосом Нацу: «Х-ха... ха...» (Т). Если звучит неестественно: SFX `young woman catching her breath after running, two short breaths, close` | 1.2 | — | −26 | C | ep |
| ep01_sfx_22 | sc05 | 1:41.5 | щелчок 1:42.3 | FOLEY | Гэн надевает очки, берёт конверт | `Old man putting on thin metal-rimmed glasses, tiny metallic click of the arms, then taking a paper envelope, soft paper rustle` | 2 | 0.6 | −30 | C | lib |
| ep01_sfx_23 | sc05 | 1:45.0 | — | FOLEY | Крупно: пальцы на штемпеле, ремешок часов на запястье | `Fingertips slowly rubbing over an old paper envelope, faint creak of a leather watch strap, very close and quiet` | 2.5 | 0.6 | −32 | C | ep |
| ep01_sfx_24 | sc05 | 1:46.5 | — | DES | За окном проплывает бок кита: приглушённый шелест сквозь стекло | = `lib_amb_whale-presence`, lowpass 900 Гц, −8 dB (обработка, без генерации) | 4 | — | −34 | R20 | lib |
| ep01_sfx_25 | sc05 | 1:53.6 | — | FOLEY | Гэн двумя руками возвращает конверт (как вручают почту) | `Paper envelope handed over carefully with both hands, slow gentle paper slide, close` | 1.5 | 0.6 | −30 | C | lib |
| ep01_sfx_26 | sc06 | 2:00.0 | — | FOLEY | Спуск по каменным ступеням: ботинки Соры + кеды Нацу; трещотка велосипеда на пандусе | `Two people walking slowly down stone steps at dusk, boots and sneakers on stone, with a bicycle freewheel ticking beside them` | 6 | 0.55 | −28 | C | lib |
| ep01_sfx_27 | sc06 | 2:15.2 | 2:16.0 | FOLEY | Конверт входит в щель ящика | `Paper envelope sliding into the narrow slot of a metal mailbox, soft paper-on-metal scrape, close` | 1.5 | 0.65 | −26 | C | lib |
| ep01_hard_mailbox | sc06 | 2:16.9 | **щелчок 2:17.0** | HARD | **Металлическая крышка ящика щёлкает: ключевой звук серии** | `Small spring-loaded metal mailbox flap snapping shut: one crisp clean metallic click with a tiny ring, close perspective, dry, nothing else` | 1 | 0.7 | −18 (пик), без ducking | C | lib |
| ep01_sil_01 | sc06 | 2:15.5–2:19.5 | — | ПРИЁМ | **Тишина до и после щелчка.** Эмбиент уходит с −33 до −45 LUFS за 0.8 с (2:15.5–2:16.3), держится до 2:19.5, затем возвращается за 1.5 с. Музыки нет. Комнатный тон не ниже −45: цифрового нуля нет | — | 4 | — | −45 | — | — |
| ep01_sfx_28 | sc06 | 2:19.5 | вспышка 2:20.0 | DES | Окно второго этажа загорается тёплым светом | `Soft warm light switching on in a distant window: a very gentle low glow swell with a faint airy shimmer, subtle, no click` | 2.5 | 0.5 | −28 | L20 | lib |
| ep01_des_stitch | sc06 | 2:21.8 | стежки 2:22.2–2:24.0 | DES | **Янтарный шов**: прореха стягивается, «нить» бежит стежками | `Magical golden thread stitching paper: a quick run of soft rhythmic paper pulls and tiny warm chimes, ending in a gentle glowing shimmer` | 3 | 0.55 | −22 | L10→R10 | lib |
| ep01_des_whale_soft | sc06 | 2:22.5 | — | DES | **Песня кита — мягкая** (кит «благодарит») | см. `whale_song.md` п. 4.2 | 5 | — | −22 | stereo | lib |
| ep01_sfx_29 | sc07 | 2:31.0 | касание 2:33.0 | DES | Хвост кита касается водонапорной башни: далёкий глухой скрип металла и бумаги, «швартовка» | `Distant soft deep creak of an old metal water tower as something huge and light touches it, a muted papery rustle, slow and gentle, far away, no impact` | 4 | 0.5 | −30 | R30 | lib |
| ep01_sfx_30 | sc07 | 2:37.0 | поимка 2:40.0 | FOLEY | Второй лист летит прямо к Соре, поимка | = ep01_sfx_16 (2:37.0) + ep01_sfx_17 (2:39.6), переиспользование | 3.5 | — | −26 | R20→C | lib |
| ep01_sfx_31 | sc07 | 2:42.6 | пик 2:44.2, **срез 2:45.0** | AMB-d | Порыв ветра поднимает шарф, затемнение | = ep01_sfx_03 + ep01_sfx_05, обрезка в 2:45.0 без фейда | 2.4 | — | −24 | stereo | lib |

Итого: 31 SFX плюс 2 голоса кита, шов, тишина, 1 VOX. Новых генераций ≈ 27, остальное — повторы и обработка. Порядок затрат: ≈ 27 × 3 с × 2–3 дубля ≈ 160–240 с SFX ≈ **6 500–9 700 кредитов**. Плюс 8 эмбиентов × 30 с × 2 дубля ≈ 480 с ≈ **19 000 кредитов** (разово, на сезон), плюс кит (`whale_song.md`, ≈ 5 500).

---

## 5. Музыка (MUS)

Промпты — ядра из `leitmotifs.md` п. 2 + хвост, указанный ниже. `force_instrumental: true`, длина генерации с запасом ×1.25. Уровень −18 LUFS без речи; под речью ducking 8–10 dB.

| ID | Сц. | TC≈ | Слот | Хвост промпта / источник | Генерация | Вход / выход | LUFS | Библ. |
|---|---|---|---|---|---|---|---|---|
| ep01_mus_01 | sc01 | 0:03.0–0:25.5 | L1 Сора | `…Starts very softly with flute alone, piano joins after a few bars, fades out gently at the end. Sparse, leaves space for dialogue.` | 30 с | вход фейдом 1.5 с после установочного плана; выход — кроссфейд 1 с в mus_02 | −18 / под речью ≈ −27 | lib (`lib_mus_l1-sora_v1`) |
| ep01_mus_02 | sc02 | 0:25.0–0:36.0 | L5 Нацу | `…Short playful entrance, 12 seconds, light and cheeky.` | 15 с | **жёсткий обрыв в 0:36.0** (Нацу замирает): срез 30 мс без хвоста | −19 | lib (`lib_mus_l5-natsu_v1`) |
| ep01_mus_03 | sc02 | 0:37.5–0:47.0 | L3 Тень | `…Slow fade in from silence, growing pressure, 10 seconds, no resolution.` | 12 с | вход с тишины 1.5 с; кроссфейд 2 с в mus_04 на 0:45–0:47 | −22 → −19 | lib (`lib_mus_l3-shadow_v1`) |
| ep01_mus_04 | sc03–sc04 | 0:45.0–1:35.0 | L4 Кит | `composition_plan` ≈ 60 с: «Reveal» 0:45–1:04 (нарастание, восторг) → «Song space» 1:04–1:13 (истончение до тянущегося тона под песней кита, −6 dB) → «Falling leaf» 1:13–1:27 (мерцающие арпеджио, разреженно) → «Gaze» 1:27–1:35 (один высокий тон струнных, затухание) | 62 с | выход: затухание к 1:35.0, J-cut в интерьер без музыки | −18 (пик в Reveal), под dx ≈ −27 | lib (`lib_mus_l4-whale_v1`) |
| ep01_mus_05 | sc05 | 1:50.0–2:00.5 | L2 Гэн | `…Enters very quietly with a single cello note, 12 seconds, warm, ends on a soft unresolved chord.` | 15 с | вход под dx_11 (очень тихо, −28); выход кроссфейдом 1.5 с в эмбиент улицы | −20 / под речью ≈ −28 | lib (`lib_mus_l2-gen_v1`) |
| ep01_mus_06 | sc06 | 2:20.5–2:33.0 | THEME «Доставка» | вырезка `lib_mus_theme-delivery_v1` из мастера темы (`leitmotifs.md` п. 3.2) | — (мастер) | вход фейдом 1.5 с из мягкой песни кита; ducking под dx_16/17 **ослаблен до 5 dB**; выход кроссфейдом 2 с в mus_07 | −18 | lib |
| ep01_mus_07 | sc07 | 2:31.0–2:42.6 | L7 «Мама · письмо» | `…12 seconds; the last note sustains and is cut off.` | 15 с | на крупном плане «Соре» (≈ 2:41) остаётся один тянущийся тон; в 2:42.6 его поглощает порыв ветра; к 2:45.0 музыки нет | −20 | lib (`lib_mus_l7-mother_v1`) |
| ep01_mus_08 | титр | 2:45.5–2:52.5 | THEME заставка | `lib_mus_theme-intro_v1`: первая нота = появление титра «Бумажный кит» | — (мастер) | после 0.5 с тишины; конец — фейд-аут 0.4 с | −18 | lib |

Генерация музыки для пилота: мастер темы (26 с × 3–4 дубля) + L1, L5, L3, L4, L2, L7 (≈ 150 с × 2 дубля). Всё это библиотека сезона: в серии 2 новых треков почти не понадобится.

---

## 6. Порядок дорожек для сведения (по `mix_plan.md`)

| Стем | Содержимое из этой таблицы |
|---|---|
| DX | ep01_dx_01…17, ep01_vox_01 |
| MUS | ep01_mus_01…08 |
| AMB | lib_amb_* и детали AMB-d (sfx_03, sfx_31), огибающая тишины sil_01 |
| FOLEY | все FOLEY |
| SFX/DES | HARD + DES, включая песни кита и шов |
| (STING) | в пилоте нет: роль акцентов выполняют обрыв mus_02 и щелчок ящика |

Особые указания сведения:
1. **Щелчок ящика (2:17.0)** — без ducking и без реверберации. Это самый «сухой» и самый близкий звук серии.
2. **Обрыв музыки в 0:36.0** — намеренный, без фейда. Проверить, что на стыке нет щелчка: микрофейд 10 мс допустим.
3. **Срез в 2:45.0** — все стемы в ноль (микрофейд 10 мс), 0.5 с тишины, затем заставка. Это единственная «цифровая» тишина в серии, как приём.
4. Ducking музыки 8–10 dB, кроме mus_06 (5 dB): тема в момент шва — главный элемент.

## 7. Что сверить, когда появится шот-лист

- [ ] Пересчитать все TC по границам кадров (ID и порядок не меняются).
- [ ] Синхро-точки: обрыв музыки 0:36 = кадр, где Нацу замирает; щелчок ящика = кадр закрытия крышки; вспышки глаза = кадры крупного плана глаза.
- [ ] Хватает ли sc05 на dx_10–dx_13 (риск перебора, раздел 2).
- [ ] Реплики В КАДРЕ: план и ракурс (если реплика ушла за кадр или на спину — меняется только пометка, не озвучка).
- [ ] Заставка: в конце (как здесь) или в начале пилота — решение директора.
