# S01E01 «The Ninth Sluice» — SFX и эмбиент

Версия 1.1 · 2026-11-23 (таймкоды Sc 5–8, дорожки V2/V4) · звукорежиссёр · статус: **план** (генерация не запускалась)
Основа: `beat_sheet.md` v1.1, `production_notes.md` v1.1 (§1, §4, §6), `lows_and_mids_life.md` §7, `story/houses/art_and_music_sheet.md` §5, разбор аналитика `research/pilot_hook_review.md` (О-10).
Модель SFX: **`eleven_text_to_sound_v3`** — в каждом запросе указывать явно. По документации API значение по умолчанию до сих пор `eleven_text_to_sound_v2`, а v2 снимается 01.03.2027. `duration_seconds` 0.5–30, `loop` для петель, `prompt_influence` по умолчанию 0.3 (для точных звуков ставим 0.5–0.7).
Именование: `lib_*` — библиотека сезона, `s01e01_*` — одноразовое для серии (`sfx_music_workflow.md` §5). Формат: WAV 48 кГц / 24 бит.

---

## 0. Правила звука пилота

1. **Кто что делает.** Композитор: колыбельная (Liss, младенец, три ноты Pell), нота Wick, тон Ione, партитура, титр, эндинг. Звукорежиссёр: голоса, SFX, эмбиент, **диегетические тоны** (гул Шпилей, тон смерти, камни реле, камертон, колокол, свистки) и **отклик камня**. Высоты всех диегетических тонов задаёт композитор в «карте высот» (`art_and_music_sheet.md` §5: Crown = C, Sluice = C♯ с уходом вниз). Камертон, тон смерти и гул Шпиля Crown должны стоять ровно на высоте Crown. Это открытый вопрос к директору — разграничение надо подтвердить (отчёт r3).
2. **Низ регистра пуст.** Нота камня — самая низкая высота в серии (`production_notes` §6). Поэтому все остальные элементы (эмбиент, SFX, гул Шпилей, шум толпы, вода) режутся фильтром ВЧ ниже **F_STONE × 1.5** (при F_STONE ≈ 41 Гц это ~60 Гц), и ниже ~110 Гц в них нет тонального содержания. Вес воды и железа даём в полосе 70–250 Гц, без саба.
3. **Отклик камня слышен на телефоне** (указание директора по О-10). Подробно — §1.1.
4. **Подсказки звуком не подсвечиваем.** Царапина кольца (Sc 10), второй лист под бюваром (Sc 7), уход человека со значком-зайцем (Sc 12), руки на засове (Sc 1 ↔ Sc 18) звучат на естественном уровне, без акцентов и стингов. Честная загадка: увидел — молодец.
5. **Тишина — это не цифровой ноль.** Минимум — комнатный тон или тон места на −42…−48 LUFS. Охраняемые тишины перечислены в §5.
6. **Слова — только в DX и DXW.** Всё, что сгенерировано как SFX (толпа, зал, смех), должно быть неразборчивым, без слов: так M&E годится для любого дубляжа (`dubbing_ready.md`). В промпты толпы всегда добавляем «indistinct, no intelligible words».
7. **Одна петля — одна локация, один слой.** Детали ставятся отдельными one-shot с интервалом 4–12 с (`sfx_music_workflow.md` §4.2).

---

## 1. Фирменные тоны (диегетика, частично синтез в ffmpeg)

Точную высоту генеративная модель не держит. Поэтому **ядро тона синтезируем бесплатно в ffmpeg** (`aevalsrc`, точная частота), а **тело и фактуру** берём из генерации SFX и подмешиваем. Высоты — из карты композитора. Ниже рабочие значения, их заменяют утверждённые.

### 1.1. Отклик камня — `lib_des_stone-answer` (Sc 3, Sc 20; весь сезон)

Задача: «низкий, под полом слуха, его скорее чувствуешь». На больших колонках главное — бас. Но **на телефоне камень обязан ответить**: на 3:00 и в последнюю секунду серии большинство зрителей смотрят с телефона, а динамик телефона почти ничего не воспроизводит ниже 200–300 Гц.

**Конструкция — три слоя:**

| Слой | Что | Полоса | Уровень (относительно слоя A) | Источник |
|---|---|---|---|---|
| A — фундамент | синус F_STONE + 2-я и 3-я гармоники | 30–130 Гц | 0 dB | синтез |
| B — «голос камня» | **целые гармоники F_STONE** (×8, ×12, ×16, ×24, ×48 → при F=41.2 Гц это 330 / 494 / 659 / 989 / 1978 Гц). Каждая — парой с расстройкой 0.6–0.8 Гц: медленные биения дают «звон» и «зуд», который отличает камень от любого инструмента | **300 Гц – 3 кГц** | −6 dB (вычисляется подгонкой по телефонной проверке) | синтез |
| C — фактура | «стекло/обсидиан», едва заметный треск трещины, дрожь | 400 Гц – 6 кГц | −18…−24 dB | SFX-генерация, ФВЧ 400 Гц |

Почему именно целые гармоники: ухо по ряду гармоник «достраивает» отсутствующий основной тон (эффект недостающего фундамента). На телефоне зритель слышит **ту же низкую ноту**, только «звенящую», а не другой звук. На колонках слой B прячется под фундаментом и даёт «живость».

**Проверено на синтетике (ffmpeg 6.1.1, 2026-11-22), F = 41.2 Гц:**

| Вариант | Полный диапазон, I | Имитация телефона, I | Потеря |
|---|---|---|---|
| Только слой A (бас) | −9.1 LUFS | −53.3 LUFS | ~44 LU, на телефоне практически не слышно |
| A + B | −9.6 LUFS | −25.6 LUFS | ~16 LU, отчётливо слышно |

**Рецепт (рабочий, F_STONE подставить из карты композитора):**

```bash
F=41.2
# слой A — фундамент
ffmpeg -y -f lavfi -i "aevalsrc='0.55*sin(2*PI*$F*t)+0.25*sin(2*PI*2*$F*t)+0.12*sin(2*PI*3*$F*t)':s=48000:d=8" stone_A.wav
# слой B — целые гармоники с биениями 0.7 Гц
ffmpeg -y -f lavfi -i "aevalsrc='0.10*(sin(2*PI*8*$F*t)+sin(2*PI*(8*$F+0.7)*t))+0.08*(sin(2*PI*12*$F*t)+sin(2*PI*(12*$F+0.7)*t))+0.06*(sin(2*PI*16*$F*t)+sin(2*PI*(16*$F+0.7)*t))+0.04*(sin(2*PI*24*$F*t)+sin(2*PI*(24*$F+0.7)*t))+0.02*(sin(2*PI*48*$F*t)+sin(2*PI*(48*$F+0.7)*t))':s=48000:d=8" stone_B.wav
# сборка: B на -6 dB, огибающая «поднимается из-под пола»
ffmpeg -y -i stone_A.wav -i stone_B.wav -i stone_C.wav -filter_complex \
 "[1:a]volume=-6dB[b];[2:a]highpass=f=400,volume=-20dB[c];[0:a][b][c]amix=inputs=3:normalize=0,afade=t=in:d=1.5,afade=t=out:st=6.5:d=1.5,pan=stereo|c0=c0|c1=c0[o]" \
 -map "[o]" -c:a pcm_s24le lib_des_stone-answer_v1.wav
```

Варианты из одного мастера, без новой генерации:
- `…_rise` (Sc 3): нарастание 1.5 с из тишины пруда, держится 4–5 с, синхронно с кольцами на воде (кольца стартуют на первом ощутимом биении слоя B);
- `…_join` (Sc 20): вступает **под третий удар** тона смерти, держится до конца сцены и **1 с в черноте**. В эту секунду слой B обязателен: иначе зритель с телефоном услышит в финале пилота пустоту;
- `…_bowl`: тот же тон + рябь в чаше (§2, `lib_water_ripple-tremble`).

**Слой C (промпт):**
```text
Close, sustained resonant hum of a small cracked black glass stone, glassy shimmering overtones with a faint fizzing crackle along the crack, slow beating, no low rumble, no music, no voice
```
`duration_seconds` 10 · `prompt_influence` 0.5 · `loop` false.

**Приёмка (§6):** в имитации телефона отклик камня в контексте сцены (с эмбиентом и тоном смерти) отчётливо слышен двум слушателям из двух, а потеря громкости при фильтре не больше 18 LU. На спектрограмме видны полосы слоя B. Высота слоя B не спорит с тоном смерти (биения с ним проверяет композитор).

### 1.2. Тон смерти — `lib_tone_death-relay` (Sc 16–20; возвращается при каждой смерти правителя)
- Рисунок (`production_notes` §6): **три долгих тона на высоте Crown и пауза длиной в тон**, по кругу. Рабочий тайминг: тон 1.8 с, зазор 0.3 с, пауза 1.8 с, цикл ≈ 7.8 с. Тайминг утверждают главный сценарист и композитор.
- Ядро — синтез: C (октаву ставит композитор; камни реле «звучат только на высоких домашних тонах») + неровные обертоны «каменной пластины» (×2.76, ×5.40) с мягкой атакой 150 мс. Камень звенит резонансом, не от удара.
- Тело — SFX: `Sustained singing tone of a resonant stone slab in a small brass cage, soft swelling attack, faint metallic cage buzz, long natural decay, no music, no voice` (6 с, influence 0.5).
- **Перспективы (все из одного мастера):** `near-cage` (Sc 16, Sc 17: дребезг клетки, близко) · `wall` (Sc 17: 12–20 копий с задержкой 20–120 мс, мелкий разброс ±3 цента, стерео) · `hill` (Sc 16 улица: 4 копии с нарастающей задержкой 0.2–0.8 с, ФНЧ от 6 до 2 кГц, всё тише — «тон спускается с холма») · `far` (Sc 18, Sc 19: дальний, ФНЧ 2 кГц, ревер) · `through-wall` (Sc 20: тонко, ФВЧ 400 Гц + ФНЧ 1.5 кГц, тихо).
- **Остановка пальцем** (Sc 17): `s01e01_des_stone-damp` — тон в комнате обрывается посреди звона: мягкий глухой «тык» пальца + срез всех копий `wall` за 30–60 мс. Промпт тела: `A fingertip touching a ringing stone, the ringing stops dead with a soft muted tick, close, dry` (1.5 с).

### 1.3. Гул Шпиля Sluice, «фальшивый» — `lib_tone_spire-sluice-flat` (Sc 2, Sc 4; весь сезон для Низов)
- Тонкий, плоский, «что-то не так» (`production_notes` §6). Ядро: C♯ (октава — композитор) **ниже строя на 25–40 центов** с медленным дрейфом ±10 центов (период 20–40 с) + едва заметные биения со второй, ещё более низкой по строю струной гула.
- Тело — SFX: `Distant thin metallic hum from a tall stone tower across a city, slightly unstable and wavering, airy, no music, no voice` (20 с, loop).
- В Sc 4 — сквозь стену: ФНЧ 2 кГц. Это «утреннее пение» Шпиля: подъём 3–4 с, затем держится.

### 1.4. Шпиль Crown — пение и ответ (Sc 9; библиотека — каждый раз, когда поют Шпиль)
- Тон Ione — композитор. Ответ Шпиля «приходит под неё». Ядро — синтез: Crown C в низкой октаве, но **выше F_STONE не меньше чем на октаву** (например, C2 ≈ 65 Гц при F_STONE ≈ 41 Гц) + обертоны в 200–2000 Гц (на телефоне Шпиль тоже должен «ответить»).
- «Бороздки загораются виток за витком вниз»: `lib_des_groove-ignite` — короткие резонансные вспышки-«вздохи» камня, по одной на виток, спускаются по высоте и громкости (12–16 штук, через 0.35–0.5 с). Промпт: `Single soft resonant shimmer of a huge stone tower lighting up from inside, glassy swell, short, no music` (1.5 с; 4 варианта, дальше перепитчим в ffmpeg).
- **Выглаживание гавани — вычитанием** (§2.6): слои гавани гаснут по очереди. Пока Ione поёт, в гавани остаются только ветер наверху и тон.

### 1.5. Камертон Ione — `lib_foley_tuning-fork` (Sc 8; сезон)
- Удар о костяшку + звон на высоте Crown C (синтез ядра: синус + слабая 6-я гармоника, затухание 6–8 с) + тело из SFX: `Small silver tuning fork struck on a knuckle, bright pure ring, close, dry` (3 с).
- Камертон к кости за ухом: переход на «внутреннюю» перспективу (ФНЧ 1.2 кГц, моно, ближе) за 0.3 с.

### 1.6. Колокол Counting House — `lib_bell_counting-house` (Sc 15–16; сезон)
`Single medium bronze bell struck once inside a large quiet stone building, warm ring, long decay, no music` (8 с, influence 0.5). Высота колокола не совпадает с Crown C и не совпадает с нотой камня (композитор). Тон смерти «едва колокол стих» — вступает за 0.5–0.8 с до конца хвоста колокола.

### 1.7. Свисты Низов — `lib_whistle_*` (весь сезон)
Словарь (`lows_and_mids_life.md` §7): *Listeners* — нисходящее двузвучие · *all clear* — восходящие три · *tide turning* — трель · *help* — долгий один. Источник: SFX «two-finger whistle» (one-shots), высоты собираем перепитчем в ffmpeg.
- `Single loud two-finger whistle across open water, clear, short, outdoor, distant echo off wooden houses, no music` (1.5 с; 4 варианта, influence 0.6).
- `Soft lip whistle, two short notes, close, quiet, nervous` (1.5 с).
- `Reed whistle on a leather thong, one short shrill pip, outdoor, wooden machinery nearby` (1 с; это свисток Corr).
- **Обязательно:** интервалы свистов проверяет композитор. Ни один свист не должен совпадать с началом колыбельной: пять нот звучат только в Sc 1, 3, 20.

---

## 2. Библиотека по семействам (промпты EN)

Колонки: ID · промпт · длит. (с) · loop · influence · где в E1. Все промпты эмбиента заканчиваются на `no music, no speech`.

### 2.1. Наводнение (ночь CY 295 — Sc 1; повтор в E10)

| ID | Промпт | Длит. | Loop | Infl. | Где |
|---|---|---|---|---|---|
| lib_amb_flood-night-street | Night flood in a narrow street of wooden stilt houses, heavy rain falling on deep still black water, water lapping against doors and walls, gutters overflowing, no music, no speech | 30 | да | 0.4 | Sc 1 |
| lib_amb_flood-rain-close | Heavy rain on dark water surface, close, dense, steady, no thunder, no music, no speech | 30 | да | 0.3 | Sc 1 |
| lib_sfx_cradle-drift | Small wooden cradle floating and slowly turning on flood water, soft wooden knocks and creaks, water lapping against it, close, rain | 10 | нет | 0.6 | Sc 1, 0:00 |
| lib_sfx_lantern-gutter | Oil lantern flame on a post sputtering and going out with a small hiss in the rain, single | 3 | нет | 0.6 | Sc 1 (×6–8 вариантов перепитчем, справа налево, издалека к нам) |
| lib_sfx_water-rising-post | Flood water rising up a wooden doorpost, gurgling, trickling into cracks, wood soaking, slow, close | 12 | нет | 0.5 | Sc 1 |
| lib_sfx_gate-bar-drag | Heavy iron bar dragged across a great iron gate, long grinding scrape, then a deep heavy clang as it drops into its brackets, outdoor, rain | 6 | нет | 0.6 | Sc 1, Sc 18 (сухая версия без дождя, тот же файл + другой эмбиент) |
| lib_sfx_fists-iron-gate | Many fists pounding on an iron gate from the far side, desperate, irregular, metallic booming, outdoor rain | 12 | нет | 0.5 | Sc 1 |
| lib_walla_flood-crowd | Frightened crowd crushed against a closed gate at night in rain, panicked cries and shouts, indistinct, no intelligible words, medium distance | 20 | нет | 0.4 | Sc 1 |
| lib_amb_underwater | Underwater perspective in a flooded street, muffled pressure, slow drifting bubbles, distant muffled thuds, no deep rumble, no music, no speech | 20 | да | 0.4 | Sc 1, 0:35 (ФВЧ по §0 п. 2) |
| lib_sfx_rowboat-oars | Small wooden rowboat moving slowly on still flood water at night, gentle oar dips, wood creaks, close | 15 | нет | 0.5 | Sc 1 |
| s01e01_foley_wet-sleeve | Wet heavy wool robe sleeve reaching and lifting, cloth rustle with dripping water, close | 3 | нет | 0.6 | Sc 1 |

### 2.2. Вода дня (Низы и гавань)

| ID | Промпт | Длит. | Loop | Infl. | Где |
|---|---|---|---|---|---|
| lib_amb_lows-dawn-ebb | Dawn in a stilt town at low tide, wet mud flats ticking and popping, slow drips from wooden houses, distant gulls, a wooden rope bridge creaking, very calm, no music, no speech | 30 | да | 0.4 | Sc 2, 3 |
| lib_foley_mud-steps | Footsteps squelching in deep wet mud, suction pulls, slow, close | 10 | нет | 0.6 | Sc 2, 3 |
| lib_foley_rake-mud | Iron rake dragging through wet silt and mud, scraping, small stones, close | 8 | нет | 0.6 | Sc 3 |
| lib_amb_sump-pool | Small enclosed pool of still black water under an old stone sluice, slow echoing drips, very quiet, eerie stillness, no music, no speech | 30 | да | 0.4 | Sc 3 |
| s01e01_sfx_rake-snag | Rake snagging on something under black water, rope creaking taut, a small splash as it is pulled up, close | 4 | нет | 0.6 | Sc 3 |
| lib_sfx_stone-surface | Small stone on a rotted cord lifted out of still water, tiny drip and plip, close | 2 | нет | 0.6 | Sc 3 |
| lib_water_ripple-tremble | Still water surface trembling into fine rings, delicate liquid shiver, very close, quiet, glassy | 6 | нет | 0.5 | Sc 3 (пруд), Sc 20 (чаша; ФВЧ, тише) |
| lib_amb_lows-dusk-tide | Dusk in a stilt town with the tide back in, water lapping under wooden houses and plank walks, lanterns creaking on hooks, quiet, no music, no speech | 30 | да | 0.4 | Sc 19 |
| lib_amb_harbour-chop | Busy harbour seen from high above, choppy waves, swell slapping stone quays, no music, no speech | 30 | да | 0.4 | Sc 9 (слой 1) |
| lib_amb_harbour-rigging | Many ships at anchor, ropes and rigging creaking, halyards tapping masts, wind, no music, no speech | 30 | да | 0.4 | Sc 9 (слой 2) |
| lib_amb_harbour-gulls | Seagulls calling over a harbour, scattered, no music, no speech | 30 | да | 0.4 | Sc 9 (слой 3) |
| lib_amb_spire-crown-wind | Strong high wind at the open top of a tall stone tower, cloth robes snapping, no music, no speech | 30 | да | 0.4 | Sc 9 |

**Вычитание гавани (Sc 9):** слои гаснут по очереди за 6–10 с непрерывного кадра: зыбь (2 с) → такелаж (2 с) → чайки (1.5 с). Остаются ветер наверху и тон. Тишина воды — главный звук сцены. На перебивке с крышей Ninth: `lib_amb_lows-dusk-tide` замедляем (растягивание 0.7×, без смены высоты) — «вода под их домом только замедляется».

### 2.3. Камень, дерево, железо

| ID | Промпт | Длит. | Loop | Infl. | Где |
|---|---|---|---|---|---|
| lib_amb_spire-stair | Inside a spiral stair of a huge black stone tower, cool resonant air, faint deep tonal hum in the walls, very quiet, no music, no speech | 30 | да | 0.4 | Sc 8 |
| lib_foley_steps-black-stone | Light footsteps of a barefoot or soft-shoed young woman climbing smooth stone stairs, resonant, spiral echo | 10 | нет | 0.6 | Sc 8 |
| lib_foley_knock-doorpost | Fist knocking three times on an old wet wooden doorpost, outdoor, close | 2 | нет | 0.6 | Sc 2, Sc 19 (тот же файл — рифма) |
| lib_foley_chain-box | Small iron box chained to a wrist, chain clinking, lid opening, close | 3 | нет | 0.6 | Sc 2, 19 |
| s01e01_foley_buttons-box | Handful of small buttons and a buckle dropped one by one into a tin box, close | 4 | нет | 0.6 | Sc 19 |
| lib_foley_net-chest | Heavy wooden chest dragged a few inches by a rope handle on wooden floor, then someone sits down on it with a thump | 4 | нет | 0.6 | Sc 4, 19 |
| lib_foley_rope-bridge | Rope and plank bridge creaking and swinging between wooden houses | 10 | да | 0.5 | Sc 2 |
| lib_foley_ladder | Wooden ladder creaking under small quick footsteps climbing | 4 | нет | 0.6 | Sc 2, 20 |
| lib_foley_brass-clip | Small brass ledger clip laid down on paper, a soft precise metallic click | 1 | нет | 0.7 | Sc 15 (предмет саги: один утверждённый звук на все сезоны) |
| lib_foley_cage-brass | Small brass cage rattling faintly on a stone wall | 2 | нет | 0.6 | Sc 16, 17 |

### 2.4. Город (локации)

| ID | Промпт | Длит. | Loop | Infl. | Где |
|---|---|---|---|---|---|
| lib_amb_treadmill-pump | Giant wooden treadmill wheels turning slowly over a pump sump, deep wooden creaking, rhythmic heavy footfalls of many workers on step boards, water churning in a sump, no music, no speech | 30 | да | 0.4 | Sc 2 (издали), Sc 6 |
| lib_sfx_wheel-stop | Giant wooden treadmill wheel slowing down and stopping, long creak, footsteps stop | 6 | нет | 0.5 | Sc 19 |
| lib_amb_lows-house-interior | Inside a small wooden stilt house in the morning, faint water lapping below the floor, wood creaks, quiet, no music, no speech | 30 | да | 0.4 | Sc 4, 20 |
| lib_amb_map-office | Quiet room with a large table, faint distant city, paper stillness, no music, no speech | 30 | да | 0.3 | Sc 7 |
| lib_foley_parchment | Large parchment map unrolled across a wooden table, stiff paper crackle; then rolled up into a leather case | 6 | нет | 0.6 | Sc 7, 10–12 |
| lib_amb_tithe-hall | Very large stone hall with high ceiling, low murmur of a gathered noble crowd, cloth rustle, distant footsteps on marble, indistinct, no intelligible words, no music | 30 | да | 0.4 | Sc 10–12 |
| lib_amb_tithe-hall-empty | Very large stone hall, silent, faint air, distant wind at tall windows, no music, no speech | 30 | да | 0.3 | Sc 12 (после падения) |
| s01e01_foley_silver-cup | Silver cup carried and set down on a stone table, wine poured, a single clink, close | 5 | нет | 0.6 | Sc 11 |
| s01e01_sfx_fall-table | Old man collapsing forward across a wooden table, chair scraping back, heavy thud, a rolled parchment sliding off the table and rolling across a stone floor | 5 | нет | 0.5 | Sc 12 |
| lib_amb_counting-hall | Huge quiet hall of clerks, felt floors, dozens of quill pens scratching on paper, pages turned with ivory blades, almost silent, no music, no speech | 30 | да | 0.4 | Sc 13–16 |
| lib_foley_quill-close | Single quill pen writing on paper, close, steady | 10 | да | 0.6 | Sc 13–16 (перо Hollis; перо Ursel, которое продолжает писать) |
| s01e01_sfx_ink-drop | A single drop of ink falling onto paper in total silence, tiny, close, exaggerated | 1 | нет | 0.7 | Sc 16 |
| lib_foley_stick-felt | Wooden stick tapping once on a felt floor, soft dull thud, then many chairs creaking at once as people straighten | 3 | нет | 0.5 | Sc 14 |
| lib_amb_relay-room | Small stone room with a wall of caged stones, faint electric-like resonance, no music, no speech | 30 | да | 0.4 | Sc 17 |
| lib_amb_mids-gate-dusk | City gate at dusk, distant pump gears, a barracks drum far away, guards' armour shifting, no music, no speech | 30 | да | 0.4 | Sc 18 |
| lib_foley_guards-file | File of armoured guards shifting and marching a few steps, helmets, leather and mail | 8 | нет | 0.5 | Sc 18 |
| lib_amb_city-rise | (сборка) низ: Низы рассвет → дамба: шестерни насосов → террасы: тише, ветер → Шпили: гул Sluice | 6 | — | — | Sc 2, подъём камеры (6 с). Мастер-план сезона — переиспользуется |

### 2.5. Толпа (только без слов)

| ID | Промпт | Длит. | Infl. | Где |
|---|---|---|---|---|
| lib_walla_hall-laugh | Large hall of nobles laughing warmly together at a joke, indistinct, no intelligible words | 6 | 0.5 | Sc 11 |
| lib_walla_hall-gasp | Large hall crowd gasps and goes silent, chairs scrape, indistinct, no intelligible words | 4 | 0.5 | Sc 12 |
| lib_walla_mudlarks-far | Distant children calling across mud flats, playful shouts and a cackling laugh, indistinct, no intelligible words, outdoor | 20 | 0.4 | Sc 3 |
| lib_walla_lane-doorways | A few people murmuring very quietly in doorways along a lane at dusk, mostly silent, indistinct | 20 | 0.4 | Sc 19 (почти неслышно: улица молчит) |
| DXW: счёт шагов | TTS, 3–4 голоса массовки, монотонно на одной высоте (`pilot_voices.md` §4) | петля 20 с | — | Sc 2, 6 (это слова → стем DXW) |

### 2.6. Переходы
- Sc 1 → 2: фонарь на чёрной воде → солнце на мокром иле. Жёсткая склейка звука: дождь обрывается, на 0.3 с тишина, затем `lows-dawn-ebb` и капля с косяка.
- Sc 4 → 5: страница переворачивается (`lib_foley_page-turn`: `Single dry page of an old heavy book turned slowly, close, dry room`, 2 с). Перед первым словом рассказчика — только этот звук.
- Sc 6 → 7: ступица колеса → роза ветров: скрип пера.
- Sc 16 → 17 → 18 → 19: «следуем за тоном вниз» — тон смерти ведёт все переходы (J-cut, 0.5–1 с).
- Sc 17 → 18: остановленный камень → падает засов (`gate-bar-drag`, только финальный удар, сухой).

---

## 3. Сцена за сценой (сводка)

| Sc | Эмбиент | Ключевые SFX / фоли | Диегетика | Тишина / особое |
|---|---|---|---|---|
| 1 | flood-night-street + rain-close | cradle-drift, lantern-gutter ×7, water-rising-post, gate-bar-drag, fists-iron-gate, walla_flood-crowd, rowboat-oars, wet-sleeve | — | **0:00–0:35 без музыки**: только вода и железо. 0:35 — `underwater` (давление, тишина), затем мычание (композитор) |
| 2 | lows-dawn-ebb; treadmill издалека | knock-doorpost, chain-box, rope-bridge, mud-steps, Wick падает в грязь | spire-sluice-flat (на подъёме камеры), счёт шагов (DXW), свисток | подъём 6 с: `city-rise` |
| 3 | lows-dawn-ebb → sump-pool | rake-mud, rope, rake-snag, stone-surface, **ripple-tremble**, walla_mudlarks-far | **stone-answer_rise** (3:00) · свисток «all clear» | пруд до гула: только капли. Гул и кольца — вместе |
| 4 | lows-house-interior | хлеб, игла для сетей, тарелка, net-chest, лестница (Nan уходит), шнурок | spire-sluice-flat сквозь стену | после руки Nan — **3 с**: только комнатный тон и Шпиль за стеной |
| 5 | — (сухо) | page-turn | — | только рассказчик + партитура композитора |
| 6 | treadmill-pump (2 колеса идут; у третьего — тишина) | шелест голов, свисток Corr (резкий) | счёт шагов (DXW) | на «sing» — счёт обрывается на 1 такт |
| 7 | map-office | parchment, перо, кожаный футляр, лист под бювар (естественно) | — | рассказчик |
| 8 | spire-stair | steps-black-stone, ткань, tuning-fork, мантия Кантора | гул Шпиля в стенах | ветер нарастает к выходу |
| 9 | spire-crown-wind; гавань ×3 слоя; Ninth roof (dusk-tide, замедлено) | groove-ignite ×12–16 | тон Ione (композитор), ответ Шпиля | **вычитание гавани** |
| 10 | tithe-hall | шаги по мрамору, двери, parchment, рукопожатие (кожа), капля крови — без звука | — | — |
| 11 | tithe-hall | silver-cup, глоток дегустатора, ладонь на кубке | — | walla_hall-laugh |
| 12 | tithe-hall → tithe-hall-empty | parchment, рука сжимается (кожа), **fall-table**, колени на камень, дверь вдалеке | (струнная нота — композитор) | **падение → тишина**, без стинга |
| 13 | counting-hall | quill-close, ivory-blade, стакан с водой «затихает» | гул Crown за окнами, далеко | самое тихое место серии |
| 14 | counting-hall | — | — | stick-felt в конце |
| 15 | counting-hall | шаги Ursel по фетру, цепочка пенсне, **brass-clip**, клип в карман | — | — |
| 16 | counting-hall → улица, сумерки | bell_counting-house, cage-brass, **перья стоп** (слой перьев обрезается), ink-drop, одно перо дальше | **death-relay near-cage → hill** | 40 перьев: тишина вокруг капли |
| 17 | relay-room | шаг Odo, касание | **death-relay wall**, stone-damp | тон обрывается на полузвоне |
| 18 | mids-gate-dusk | gate-bar-drag (сухой), guards-file | death-relay far | одна реплика стражника |
| 19 | lows-dusk-tide | knock-doorpost, buttons-box, chain-box, net-chest, шаги сборщика по доскам, далёкие быстрые шажки Nan | death-relay far + whistle-chain (свистки повторяют рисунок тона) · **wheel-stop** | после остановки колеса **вода вдруг громкая** (+4 dB к `dusk-tide`) |
| 20 | lows-house-interior (ночь) | шнурок, клеёнка, ripple-tremble (чаша, тихо), доска под Mags, лестница (быстрые лёгкие шаги) | death-relay through-wall → **stone-answer_join** на 3-м ударе | **срез в черноту на низкой ноте, 1 с, слой B слышен**, затем эндинг |

---

## 3a. Таймкоды Sc 5–8 и дорожки для вертикальных роликов (режиссёр, приёмка раскадровки §4.3–4.5)

Новые таймкоды для монтажного листа звука (сумма серии 26:39 не меняется; всё после 9:04 — без изменений):

| Сцена | Было (beat sheet v1.1) | Стало | Длина | Что двигается в звуке |
|---|---|---|---|---|
| Sc 5 гобелен | 5:55–7:05 | **5:20–6:11.5** (+ титр) | 51,5 с без титра | page-turn на 5:20.0 перед первым словом; фразы рассказчика по кадрам (`pilot_voices.md`, NARR-01); M05 Archive (композитор) |
| Титр | 12 с | **6:11.5–6:20.5** (9 с) | 9 с | T-TITLE 3 такта (композитор); звуковых эффектов нет |
| Sc 6 колесо | 7:05–8:35 | **6:20.5–7:20** | 59,5 с | treadmill-pump, DXW-счёт, свисток Corr — в окне 59,5 с; склейка звука на ступице колеса в 6:20.5 |
| Sc 7 карта | 8:35–9:15 | **7:20–7:57.5** | 37,5 с | map-office, parchment, рассказчик (часть B M05) |
| Sc 8 лестница | 9:15–10:30 | **7:57.5–9:04** | 66,5 с | spire-stair, шаги, камертон; ветер выводим к 9:04 (Корона — без изменений) |

**Отдельные дорожки для вертикальных роликов** (не смешиваются в общий стем, лежат в `S01E01_stems/vertical/`):

| Ролик | Файл | Содержимое | Тайминг |
|---|---|---|---|
| V2 | `s01e01_voxnl_pell-hum_v1.wav` | напев Пелл, Sc 3 (вокал — композитор) | кончается ≤ 3,5 с от начала sc03-sh180 |
| V2 | `s01e01_dx_<NNNN>_wick_pell-mouth.wav` | «Pell. Mouth.» Уика, шёпот-шипение, сухо | сразу после напева. В версии без напева — первая звуковая точка ролика |
| V4 | `s01e01_dx_<NNNN>_nan_never-sing.wav` | «Never sing, chick. Hum if you must, and only for the house.», сухо | за кадром поверх sc04-sh150/sh160. Комнату добавляет сведение ролика |

Для каждой такой дорожки в ролике остаются те же M&E и эмбиент, что в серии (те же файлы). Правило телефонной проверки (§6) действует и для вертикальных роликов.

## 4. Что переиспользуется на весь сезон и дальше

| Элемент | Где ещё | Почему важно |
|---|---|---|
| stone-answer (все варианты) | каждое «пение» камня, S1–S12 | один звук на всю сагу, узнаётся с полуноты |
| death-relay (все перспективы) | каждая смерть правителя, сигналы реле | — |
| spire-sluice-flat, spire-crown + groove-ignite + вычитание гавани | каждая сцена со Шпилями | `production_notes` M3: сцена-подпись повторяется |
| flood-night-*, gate-bar-drag, fists, underwater, rowboat | **E10** (повторяет Sc 1 кадр в кадр) | стоимость делят две серии |
| lows-dawn/dusk, house-interior, treadmill, whistles, knock | все серии в Низах | — |
| tithe-hall, counting-hall, relay-room, mids-gate, map-office | локации сезона | — |
| brass-clip, tuning-fork, cage-brass, parchment, page-turn | предметы саги | один утверждённый звук на предмет |
| walla_* (без слов) | любая массовка | годится для дубляжа без переделки |

Одноразовые (`s01e01_*`): rake-snag, buttons-box, silver-cup, fall-table, ink-drop, wet-sleeve, stone-damp.

---

## 5. Охраняемые тишины (`production_notes` §6)

| Где | Что звучит | Чего нет |
|---|---|---|
| 0:00–0:35 | вода, дождь, фонари, железо, толпа без слов | музыки |
| Sc 3, пруд до гула | капли в отдалении, дыхание Pell (VOX-NL) | эмбиента канала, свистов |
| Sc 4, 3 с после руки Nan | комнатный тон −45 LUFS, тонкий Шпиль за стеной | фоли, голосов |
| Sc 12, падение | `tithe-hall-empty` −46 LUFS | стинга, музыки, шума зала (зал **замолкает**) |
| Sc 16, 40 перьев | тон смерти, капля, одно перо | перьев зала |
| Финал Sc 20 | нота камня 1 с в черноте (с слоем B) | всего остального |

---

## 6. Телефонная проверка (обязательна для Sc 3, 9, 20 и всего мастера)

Имитация динамика телефона (моно, полоса ~300 Гц – 7 кГц, крутые срезы):

```bash
ffmpeg -i in.wav -af "pan=mono|c0=0.5*c0+0.5*c1,highpass=f=300:poles=2,highpass=f=300:poles=2,lowpass=f=7000:poles=2,lowpass=f=7000:poles=2" -c:a pcm_s16le phone_sim.wav
# громкость в полосе телефона
ffmpeg -nostats -i in.wav -af "pan=mono|c0=0.5*c0+0.5*c1,highpass=f=300:poles=2,highpass=f=300:poles=2,lowpass=f=7000:poles=2,lowpass=f=7000:poles=2,ebur128=peak=true" -f null -
# спектрограмма: видны ли полосы слоя B
ffmpeg -i in.wav -lavfi showspectrumpic=s=1600x600:legend=1:scale=log stone_spectrum.png
```

Критерии:
1. Отклик камня: потеря при фильтре ≤ 18 LU (эталон — §1.1). В контексте сцены оба слушателя слышат «ответ» в `phone_sim.wav` с первого раза.
2. Каждая реплика разборчива в `phone_sim.wav` (как в `sound_bible.md` §5.4).
3. Ответ Шпиля (Sc 9) и тон смерти слышны в `phone_sim.wav`.
4. Дополнительно — живая проверка на двух реальных телефонах (iOS и Android) перед сдачей пилота.

Это же правило вписано в `mix_plan.md` (раздел 9).

---

## 7. Генерация: объём и порядок (оценка)

- SFX-генерация: ≈ 62 позиции, в среднем ≈ 15 с (петли по 30 с), 2 дубля → ≈ 1 900 с. При ~40 кредитах/с (оценка из `sfx_music_workflow.md` §6, **сверить с тарифом**) ≈ 75 000 кредитов. Около 80 % — библиотека сезона, разовая трата. Экономия: петли эмбиента сначала по 1 дублю, второй — только если петля «узнаётся».
- Синтез тонов (камень, тон смерти, Шпили, камертон) — ffmpeg, бесплатно.
- Порядок: (1) карта высот от композитора → синтез ядер тонов и телефонная проверка камня (бесплатно); (2) эмбиенты Sc 1–4 и камень (холодное открытие — самое важное); (3) остальное после утверждённой раскадровки.
- Каждый файл — в манифест: промпт, модель `eleven_text_to_sound_v3`, duration, loop, influence, дата.
