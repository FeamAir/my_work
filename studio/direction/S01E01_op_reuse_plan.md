> **ОТМЕНЕНО инвестором 2026-11-24.** Опенинг существует отдельно от мультфильма: ни одного кадра, клипа или композиции опенинга в сериях. Кадры опенинга не используются и как основа NB2-правок. Общими остаются только дизайн мира и стиль C (через референс-листы локаций/героев, не через кадры OP). План ниже — только для истории.

# S01E01 — reuse of saga-opening footage as establishing shots (style C)

Version 1.0 · 2026-11-24 · author: director (режиссёр-постановщик) · status: **plan, $0, nothing generated or cut**
Basis: investor's go-ahead to reuse opening footage as establishing shots of places in S01E01 (consistency in style C, saving money). Shot ids, TCs and durations = shot list v4.0 (`shotlists/S01E01_shotlist.md`, `S01E01_shots_v4.json`); shot content = storyboard `storyboard/S01E01/sc*.md` (prompts column) + finals checklist v1.1 (`S01E01_finals_checklist.md`). Opening sources = `opening/SAGA_OP_storyboard.md` v2.8 §4–§6, `opening/tools/op_saga_build_c.py` (v1.1 cut list) and, read only, `op_saga_build_c12.py` (v1.2 changes). Opening files and scripts are not touched by this plan.

## 0. Кратко (RU)

- **Что берём.** Из всего опенинга в серию по-настоящему подходят 4 места Хайуотера: общий вид города с Низов (D01_A_C / клип KA02), переулок Девятого (alley_C), колёса (D05_W1_C / K05C), венец Шпиля Короны (D08_S1_dusk_C). Ещё F10_C (пролёт над Низами) годится как основа одного нового кадра. Остальные земли, карта дельты, общий вид Конкорда, знамёна, гроссбух и шторм у дамбы в серию **не идут**: в E1 их нет, или объект другой, или это спойлер (§4).
- **Прямой повтор отснятого (сам клип, $0): 2 кадра.**
  1. **sc02-sh150** (1:51.00, 5.0 с, подъём над городом на рассвете) ← **KA02** вперёд, полный кадр, окно кропа 1.12× идёт **снизу вверх**. В опенинге A02 тот же клип идёт 1.5 с окном 1.3× сверху вниз. Реверс клипа запрещён: каскады на террасах потекут вверх (условие хранителя R8.2c п. 2).
  2. **sc19-sh200** (21:04.50, 2.0 с, колесо замирает в темноте) ← **K05C**, кроп 1.5× только на колёса 1–2, торможение скоростью, грейд в сумерки. **Нужна подпись хранителя:** в опенинге правило C06L прямо запрещает, чтобы колесо замедлялось или вставало, а здесь остановка и есть сюжетный удар. Запасной вариант без хранителя — план v4 (ночная правка NB2 от кадра sc06-sh020).
- **Основа для правки NB2 (новый ключевой кадр, клип опенинга в кадр не идёт): 5 кадров.** sc06-sh020 ← D05_W1_C; sc09-sh040 ← D08_S1_dusk_C (золото вместо сумерек); sc09-sh120 ← F10_C (пазы горят, VFX); sc15a-sh100 ← D01_A_C (последнее солнце); sc15a-sh060 ← alley_C (сумерки, вернуть ворота). Из них правки sc09-sh120, sc09-sh040 (через пазы sh050) и sc15a-sh060 тоже **требуют подписи хранителя** (§3).
- **Повтор опенинга не чувствуется:** на каждое место по одному прямому повтору, оба далеко от блока OP (3:37.25–5:07.25): за 1:46 до него и через 16 мин после. Окно, направление движения и время суток другие. alley_C в опенинге на экран вообще не попал (KA04 дважды брак), поэтому повтора там нет.
- **Спойлеров не добавляем.** Подножие и проём Шлюзового Шпиля вне кадра, как в R8.2a. Карта дельты, знамёна Ильвейна, Раска и Квелла с девизами, буря у дамбы и пересчёт фонарей в серию не идут.
- **Экономия честно маленькая.** Против строки ремастера ключевых кадров $33.90 (326 × 1.3 × $0.08): **≈ $0.45** (1.3 %). Вместе с уже готовыми плейтами C (статья 5 ремастера) ≈ $0.95. Если финал оживляет эти LA-кадры через Kling, добавляется ≈ $1.05, итого до ≈ $2.0. Главный выигрыш не в деньгах. Нам достаются кадры, которые хранитель уже принял: резьба «/» (G5), тёмные пазы и подножие (G4), каскады (R8.2c). Шпили — самый дорогой брак в C (F10_C ушёл в 4 дубля). Плюс настоящее движение вместо ffmpeg на 2 кадрах и одна картинка города в серии и в опенинге.
- **Открытые вопросы:** подписи хранителя по §3; блок OP в шот-листе v4 стоит на 90.0 с со ссылкой на старый `S1_OP_storyboard.md`, а сага-OP идёт 87.0 с. Решает директор.

## 1. Rules of this plan

1. **Two kinds of reuse.** *Direct* = a piece of an accepted opening clip is cut into the episode (with a different window, speed or grade, never re-generated). *Edit base* = an accepted opening frame is image 1/2 of a new NB2 /edit that becomes the episode's own key frame (new light, time of day, figures, crop); the opening picture itself never appears on screen.
2. **At most one direct reuse per location per episode** (investor). Locations: Highwater from the Lows (D-01 A) · the treadwheels (D-05 W1/W2) · the Crown Spire crown (D-08 S1) · the Ninth's lane (D-02 C1) · the flyover over the Lows (F10). Edit bases also count toward the "replay" feel, so each edit base changes **at least two** of: window/crop, time of day, figures, camera move.
3. **Distance from the OP block.** The opening sits at 3:37.25–5:07.25 in v4. A direct reuse never comes closer to it than 1:30.
4. **No reverse, no hflip.** No mirroring (G5, OP-11). No time reverse on a clip that has falling water in frame (KA02 and K07C cascades, K05C buckets: R8.2c p. 2).
5. **Every finals rule still applies** to reused material: G3 (nothing glows), G4/G5 (Spires), G10 (frame hygiene), G15 (Spire / night water → Kling, never MiniMax).
6. **Resolution.** Opening clips are 1928×1072, 24 fps, 121 frames (5.04 s); NB2 frames are 1376×768. A crop above 1.6× of a clip, or any crop of an NB2 frame, goes through a lanczos upscale with light sharpening and is checked at 100 % before acceptance. Crops above 2.0× are not used.
7. **Spoiler line (OP-15 mirrored into the episode).** Reuse brings nothing into E1 that the episode script does not already show. Anything the opening hid on purpose (the Sluice Spire's foot and doorway, the gate in the lane, the doorpost marks, a stopping wheel, the Ilvane/Rusk/Quell devices) comes back only where the E1 script needs it, and only with the keeper's sign-off (§3).

## 2. Reuse table

Clip paths: `output/opening/saga_c/clips/<K>.mp4` (accepted takes, `state.json`). Frame paths: `output/opening/saga_c/frames/<F>.png` (accepted versions). Source times are seconds inside the 5.04 s clip.

### 2.1 Direct reuse (footage, $0)

| # | Episode shot (v4 TC, dur) | Location | Source | Piece / window / speed / grade | What the opening already uses (avoid) | Replaces in v4 | Checks |
|---|---|---|---|---|---|---|---|
| **R1** | **sc02-sh150** · 1:51.00 · 5.0 s · A · own | Highwater from the Lows, dawn (D-01 A DAWN-EBB) | `clips/KA02.mp4` (from `frames/D01_A_C.png`, keeper R5.2/R6.1 signed; cascades allowed R8.2c) | **Forward**, 0.0–5.0 s at 1.0× (the clip's own slow push). Crop window 1.12×: starts bottom-anchored (stilt-town and dike fill the frame), rises to top-anchored by 3.5 s (eased, the storyboard's L-03 profile shortened to 5.0 s), holds 0.5 s on the crowns, drops back to the middle in the last 1.0 s. Grade: as is (dawn, LOWS_DAWN); slightly darker in the Lows layer (the Ninth "in its own shadow below the sea line") with a $0 gradient mask. VFX E-1 (the Sluice Spire's flat hum) only as a sound cue plus a faint air shimmer above the Sluice crown, **no light** (G3). | A02: 0.5–2.0 s, 1.3× window **top → bottom** (v1.1 and v1.2). v1.1 also A03/A04b crops at 1.8 s and 3.3 s (2.0–2.4×), gone in v1.2. | Own key frame "D-01 A DAWN-EBB plate t2i → LA L-03 + L-04 layers". Text of sc02-sh150 to update: the tower layout follows canon v0.10 / D01_A_C (two Spires on the hill, the tallest central; the short, worn **Sluice Spire at the south-west foot**, right of frame, in front of the dike), not the pre-v0.10 storyboard line "the nearest tower on the left lower and worn". | G5 "/" on all three (unchanged picture, no flip). Sluice foot: hidden by roofs and mist, no doorway (checked at full size on D01_A_C; keep the bottom anchor at ≥ the roof line, never below the frame). Cascades end on the terraces (R8.2c). Banners on the terraces are not readable at this scale (the storyboard's "banners" stays a sound and the C-06 shots). |
| **R2** | **sc19-sh200** · 21:04.50 · 2.0 s · A · kf=sc06-sh020 | Treadwheels, dusk → dark (D-05 W1 DUSK) | `clips/K05C.mp4` (from `frames/D05_W1_C.png`) | Source 1.5–3.5 s, crop **1.5× on wheels 1–2 only** (x key 0.32, y 0.55: the third wheel is out of the window, because in the episode it has stood since sc06). Speed: 1.0× for 0.8 s, then eased down to 0.15× over 1.0 s with `minterpolate` mci, the last 0.2 s held at that speed; the stop itself is sold by the sound ("the count breaks mid-number, the wood groans"). Grade: −1.3 EV, teal-black shadows, sky to deep dusk blue, no warm source (finals checklist QA C2: "in the dark of dusk, not the bright day plate"). | A06 2.0–3.5 s (near hub 2.0×), A08 0.0–1.5 s (full), C06L 3.5–4.25 s (1.8×), B15 frames 12–15; v1.2 adds A01b 0.5 s (1.6×) and A04b 3.0 s (deck 1.8×). | The v4 plan for this shot = a dusk NB2 edit of the sc06-sh020 key frame + LA rotate ramp to 0. That edit (1 paid image) is no longer needed. | **Keeper sign-off required** (§3, K1). Drips slow down with the wheels: acceptable only if they read as darkness; if they read as a freeze, fall back to the v4 plan. No walkers in the clip: continuity with sc06-sh020 (walkers inside wheels 1–2) holds only because the shot is dark; check at 168×94. |

### 2.2 Edit bases (new key frame from an opening frame; paid at finals as any key frame, NB2 /edit $0.08)

Recipe for all: image 1 = the opening frame (it is already style C, so it is also the 3D anchor, STYLE_BASE_C §4); further images = the C masters of any character in the shot; prompt = "Use image 1 for the place, the camera and every building exactly; change only: …" + the storyboard content text + `{STYLE_BASE_C}` + `Avoid:` + `{NEGATIVE_C}` + the shot's finals-checklist wording. Never "glow" or "light in the grooves" in an NB2 prompt: groove light is a VFX layer (VFX-GROOVE-LIGHT, L-17), as in the storyboard.

| # | Episode shot (v4 TC, dur) | Base frame | Change vs the opening (≥ 2 of window / time / figures / move) | Replaces in v4 | Feeds | Keeper |
|---|---|---|---|---|---|---|
| **E1** | **sc06-sh020** · 8:07.25 · 2.75 s · A · own | `frames/D05_W1_C.png` (opening A08 composition) | Window 1.15× shifted left-down (more of the sump, less roof); light LOWS_DAY late morning with roof-shadow stripes (the opening is misty morning without stripes); figures: tiny walkers seen from behind inside wheels 1–2, the farthest wheel empty and still. Motion as the storyboard: LA rotate on wheels 1–2, wheel 3 static (or Kling at finals: "the third wheel does not move"). | Own key frame "D-05 W1 MORNING; C-02" (NB → NB2 edit). | Base for the sc19-sh200 fallback (dusk edit) if R2 is refused. sc06-sh010 (hub CU) stays own: a hub close-up 3 min after the OP's hub shot (A06) would read as a replay. | No (the standing third wheel is in the E1 script; the empty pin socket stays in its own insert sc06-sh080, not in this frame). |
| **E2** | **sc09-sh040** · 10:47.25 · 4.0 s · B · own | `frames/D08_S1_dusk_C.png` (the opening's C13 logo plate, K17C) | Time: dusk violet → **late-afternoon gold** (STEPS_GOLD, low sun from the west, the crown back-lit); window 1.2× up (crown and two turns only, no logo-plate framing); figures: a tiny white figure in one arch (Ione, CH-0002 C master as ref), gulls on the crown ledges. Motion: Kling (G15), gulls burst and wheel away right-down, air shimmer above the crown, "no glow yet". | Own key frame "D-08 S1; MK-1" (NB → NB2 edit → MiniMax H3; MiniMax is barred by G15 anyway). | The new gold crown frame is the D-08 S1 LATE-AFT design for sc09-sh050 (own, low angle; VFX grooves), and the tower layer of the window shots sc13-sh010 / sh180 (D-08 look, finals checklist keeper 13) and sc10-sh010 (dark tower, higher and closer); those window plates stay own key frames, only the tower in them is matched to E2. | **Yes, K2:** the opening's last image becomes the base of the singing-Spire design. |
| **E3** | **sc09-sh120** · 11:17.75 · 2.5 s · A · own | `frames/F10_C.png` (opening A04a/A05a/b, K07C) | Time: dawn → late-afternoon gold, sun from behind the viewer (west) on the Crown Spire's face; window 1.3× right of centre, the Crown Spire centre-right (storyboard), the Sluice Spire's foot and the arch below its lowest turn **out of the crop** (R8.2a); a roof edge in the near foreground for the POV. Groove light by VFX only: white-blue, top-down from the crown to the lower turns, base dark (G4, DEC-69); the Sluice Spire and the third Spire stay dark (finals checklist sc09-sh100: only the Crown Spire lit). | Own key frame "D-01 A LATE-AFT (Шпиль горит)" (NB t2i → LA). | — | **Yes, K3:** a lit Spire on an opening composition; the cascades (R8.2c) must stay on the terraces in gold light. |
| **E4** | **sc15a-sh100** · 17:11.50 · 3.5 s · A · own | `frames/D01_A_C.png` (the same plate as R1; the opening's A02) | Time: dawn → **last sun** (gold on the palace and terraces, the dike and the Lows in shade, LOWS_DUSK); window 1.25× centred on the palace; all three Spires dark. Motion: LA L-01 0.03 as planned. Different from R1 by time, window and move (R1 rises at dawn, E4 holds on the palace at sunset); 15 min apart. | Own key frame "D-01 A LATE-AFT" (NB t2i → LA). | — | No (same context as the opening: dark Spires, no water on the dike). |
| **E5** | **sc15a-sh060** · 16:48.25 · 3.25 s · A · own | `frames/alley_C.png` (= D-02 C1 master view to the NE; **never on screen in the opening**: KA04 failed twice, A04a/b are cut from K07C/KA02 in v1.1 and K07C/K05C in v1.2) | Time: dawn-ebb → **dusk** with the water back in the lane (boats afloat, no silt); first lanterns being lit one by one toward the camera (L-09 masks, the lantern post on the right lit); the dike **gate restored** at the end of the lane (D-02 C1 canon; it was painted out for the opening, R3.2). Doorpost marks: not in this view's prompt; add them only if the keeper wants the C1 master to carry them. | Own key frame "D-02 C1 DUSK" (NB t2i → LA). | Its result is the C1 DUSK plate for **sc19-sh290** (21:24.75, own: lantern and silhouette in every doorway, tiny hunched figure far off), made from E5 by an NB2 edit, not from the opening. Optional, same base: the C1 FLOOD mode for **sc01-sh010** (0:00, the cradle, class D hero, pilot_references D-02 "FLOOD" prompt). | **Yes, K4** (gate restored; the FLOOD mode needs a separate yes). |

### 2.3 Not reused (and why)

| Opening source | Why not in E1 |
|---|---|
| `FA01` / KA01 (failed twice) — the storm swell against the dike | E1 never shows the sea side of the dike. Cut into the flood night of Sc 1 it would show *how* the water came (OP-15 line, a spoiler). No slot. |
| `W13` / KW13 — the whole Concord from the air | No realm aerial in E1; it shows the other lands and the eight Spires. Keep it for the opening only. |
| `W16` / KW16 — the delta map | A different object: E1's maps (sc07, sc12) are the Highwater tithe map M-MAP with districts, tints, IX and the towers in holders' rings. Cutting the opening's map in would mix two canon objects (keeper 19, OP-10). |
| `W15` / KW15 — the Many Mouths with river traffic | The channels upriver, not the harbour (D-09); E1's harbour (sc09) goes glass-flat, while KW15 has bow waves and moving hulls. Wrong geography and the wrong state. |
| `W01`–`W12`, `W14` — the other lands and pennants | Not in E1. |
| `F17_C` / KA11, `F19_C` / K11C — the palace-wall banners | E1's banners are inside the tithe hall (C-06, G11) and include the Ilvane, Rusk and Quell devices that the opening never shows. Use F17_C/F19_C only as **cloth and dye refs** for the C-06 re-generation (fewer retakes on the five signed devices), never as footage. |
| `F14_C` / K10C — the Lantry ledger and the toppling coins | The E1 ledger inserts (sc13–sc16) carry story figures (1,470 / 1,740, ACCOUNT NINE, the clip). The opening's page has the variant-A tally and the coins fall. Use it as a paper/ink material ref for E-12 only. |
| `F04_C` (K03C failed) — the net and the lantern string | Never on screen in the opening, so it is free. But v4 has no dawn lane cutaway it fits, and Sc 1 wants the lanterns going out one by one, a countable row (the opening made them uncountable for OP-18). Kept as a spare dawn bridge for the editor; not counted. |
| `D05_W2_C` / K04C — inside the drum | Opening-heavy (A07, A09; v1.2 A01a and A03 open the whole OP on it). The E1 inside-drum shots have walkers (sc06-sh030, sh120) → own; D05_W2_C is a geometry ref only. |
| K17C footage, K07C footage | The OP's final image (C13) and 4.5 s of its Highwater flyover: too recognisable for a direct cut. Used only as edit bases E2 and E3. |
| sc16-sh180 (D-01 B DUSK, from the bank steps west over the city) | No opening shot matches (KA11 has the city and sea at sunset, but the banners fill 3/4 of the frame and KA11 is the opening's most-seen clip). Own key frame, F17_C as a city/sea design ref. |
| sc03-sh200 (the Sluice Spire from below over roofs) | No opening angle from below. Own key frame; D01_A_C as the design ref for the short, worn Sluice Spire. |

## 3. Keeper sign-off needed (context differs from the opening)

| # | Shot | What differs from the opening | Question to the keeper |
|---|---|---|---|
| K1 | R2 sc19-sh200 | Opening board, shot C06L: "every wheel keeps the same speed through the whole window, none slows or stops". In E1 the wheels stopping on the death tone is the story beat. | May the opening's own wheel footage be the image of the wheels stopping (it ties the OP's wheels to the death), or must this shot be a new picture (v4 fallback: dusk NB2 edit of sc06-sh020)? |
| K2 | E2 sc09-sh040 (→ sh050, sc13 window, sc10-sh010) | The opening's C13 logo tower (dark, dusk, OP-4/OP-19: "the song is heard, not shown") becomes the base of the tower that sings and lights in Sc 9. | Is the same crown design acceptable for the singing Crown Spire in E1, given that the OP's final image is this tower dark? (Canon-wise it is the Crown Spire, D-08 = PL-0014.) |
| K3 | E3 sc09-sh120 | An opening composition (F10_C) shown with lit grooves; the Sluice Spire stands dark beside the lit Crown Spire in the same frame. | Confirm: only the Crown Spire lit, top-down, base dark (G4/DEC-69); the Sluice foot and its arch stay out of the crop as in R8.2a; cascades as R8.2c in gold light. |
| K4 | E5 sc15a-sh060 (+ optional sc01-sh010 FLOOD) | alley_C was patched for the opening (R3.2): gate, knocker, doorpost notches removed, lantern unlit. The E1 C1 view needs the gate (sc01/sc18 geography), lit lanterns and, for Sc 1, the flood. | May the C1 master be rebuilt from alley_C with the gate restored? Knocker and doorpost marks: restore or keep off in this view? The FLOOD mode for the cradle shot: yes/no. |

No canon change is proposed. The keeper rules on these four only; R1, E1, E4 keep the opening's context (dark Spires, morning/evening, nothing glows).

## 4. Cost estimate (no paid call in this plan)

Reference: concept-artist style-C report, remaster item 9 = 326 key frames × 1.3 takes × $0.08 = **$33.90**, i.e. $0.104 per key frame; Spire plates realistically ≈ 2 takes in C (F10_C took 4, W13 needed a fix), i.e. ≈ $0.16.

| Item | Calls saved | Takes saved | $ |
|---|---|---|---|
| R1 sc02-sh150 → KA02 | 1 key frame (a three-Spire plate) | — | 0.10–0.16 |
| R2 sc19-sh200 → K05C | 1 NB2 dusk edit | — | 0.08–0.10 |
| E1, E5 (no Spire): same call, the composition and wheel/lane geometry fixed | — | 1.3 → 1.1 each | ≈ 0.03 |
| E2, E3, E4 (Spires): same call, G5 thread, G4, cascades already accepted | — | ≈ 2.0 → 1.3 each | ≈ 0.17 |
| **Against the $33.90 key-frame line** | | | **≈ $0.40–0.46 (≈ 1.3 %)** |
| Remaster item 5 (location plates in C): D-01 A dawn, D-02 C1 dawn, D-05 W1 morning, D-05 W2, D-08 S1 dusk already exist in C from the opening | 5 plate modes × 1.3 | | + ≈ 0.52 |
| If finals give these establishing shots real motion (planned as ffmpeg LA): R1, R2 bring Kling motion for free instead of 2 × (5 s Kling 2.5 TP $0.35 × 1.5 takes) | 2 clips | | + ≈ 1.05 |
| **Total, best case** | | | **≈ $2.0** |

Conclusion: the money is small. Reuse is worth it for consistency (series = opening, one Highwater) and for acceptance risk (the Spire frames are the most expensive retakes in C). It is not worth pushing for more reuse to save money: every additional opening clip in the episode costs us the "replay" feel and more keeper checks.

## 5. Work order at finals (all $0 until step 3)

1. Keeper answers K1–K4 (from this file; frames to show: `D01_A_C`, `D05_W1_C`, `D08_S1_dusk_C`, `F10_C`, `alley_C` and the K05C window of R2).
2. R1 cut ($0): an episode-side script in `direction/animatic_tools/` (not the opening tools), reading `clips/KA02.mp4` read-only; R2 the same after K1 (or drop to the fallback). Check: 100 % and 168×94; G5 on every Spire frame.
3. E1–E5 go into the finals key-frame batch of their scenes (paid, needs the studio director's go-ahead with the rest of the batch); acceptance per the finals checklist "check first" column.
4. Update the v4 shot-list rows (frame column: `OP:KA02 0.0–5.0 1.12× rise`, `OP:K05C 1.5–3.5 1.5× ramp`, `base OP:<frame>`) in the next shot-list version (owner: whoever holds the shot list).

## 6. Open questions

1. **Studio director:** the v4 shot list books the OP block at 90.0 s with a placeholder that points to the old `S1_OP_storyboard.md`; the saga OP (v1.1/v1.2) runs 87.0 s. Either the episode's OP block becomes 87.0 s (every TC after 3:37.25 moves −3.0 s) or 3.0 s of black/room tone pad it. Not changed here.
2. **Keeper:** K1–K4 (§3).
3. **Director (me), at finals:** if R2 is refused, E1's key frame is made first and the sc19-sh200 dusk edit is made from it (as in v4).
