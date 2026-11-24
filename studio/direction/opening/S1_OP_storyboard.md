# HOLLOWSTONE — Season 1 opening (instrumental, 87.0 s) — storyboard v1.4

Version 1.4 · 2026-11-24 · author: director (anime-director) · status: **gate OPEN with conditions (`qa/gate/gate-op-2026-11-24.md` §R2). Studio director on the conditions: C1 waived (the picture carries the build; the 0:57.0 hit lands on the 9-frame black + INK + wave cut); C2 moved (K13 waits until the keeper has looked at the fixed H1/H2 plates and the studio director gives the go; everything else is generated); C3 holds (the OP is the only paid run); C4 waived (guard + log estimate). v1.4 = v1.3 + the gate's free fixes 1–9 (below). Paid run of 16 NB2 frames + 16 Kling clips (all but K13) follows v1.4.**
v1.4 changes: H1/H2 plates v2 (finial re-filled with no ghost or streak; the 6 lamp heads redrawn unlit, halo ring removed, no orange bar, no blue patch); G1 `{AVOID_OP}` ends `finger rings, rings on water.`; G5 K12 written out in full; §8 numbers (limit 64, log $54.15, headroom $9.85, retakes only from the $1.12 reserve); G2 "before acceptance / assembly"; F2 the third flash stays on 1356 (text aligned); N1 cut 33 spray field ends with the wipe on 1994, never on the tower; cuts 02 and 05 crack paint-outs and cut 24 tier tints done at $0 (`tools/op_paintouts.py`).
v1.3 status (kept for the record): storyboard only. v1.3 = v1.2 + the gate's blockers B1–B4 (`qa/gate/gate-op-2026-11-24.md`) + the keeper's rulings §R2 (`reports/lore-op-2026-11-24.md`), all applied word for word. Signed by the canon keeper (R2.7: the signature holds after R2.2–R2.4 and R2.6 p. 1); the keeper checks F15, F17, F18, F23 and F26 at full size. Next: the gatekeeper re-checks the v1.3 diff; nothing is generated before the gate opens.**
v1.3 changes: B1 `{AVOID_OP_F18}` verbatim again (`magic sparkles, ` restored); B2 §R2.1–R2.6 applied (drops on the logo letters only; F26 and cut 26 with many mixed prints; no steam in 13, OP-14, §3, §7; GLASS = even full-frame steps, no front; the H1/H2 crop + finial paint-out + dark lamps, plates prepared at $0); B3 the OP is **87.0 s** (cut 33 1:22.5–1:27.0, K17 0.0–4.5 s at 1×, picture and audio fade 1:26.5–1:27.0); B4 NB2 output size and parameters pinned (§5), price $0.08 confirmed. The $0 animatic of §9 step 1 is built: `output/opening/S1_OP_animatic_v1.mp4`.
Music: **`output/music/lib_mus_theme-op-drums_v2a.mp3`**, used 0:00.0–1:27.0 with an audio fade 1:26.5–1:27.0 (studio director: master on v2a, 87.0 s = 29 bars). `…_v2b.mp3` shares the same grid (measured, §2) and can be swapped in without moving any cut. Bars of 3.0 s from 0:00.0; cuts on bar lines or half-bars (1.5 s = 2 beats at 80 BPM). **Drum attacks in v2a/v2b land +0.04–0.05 s late, so every hit frame sits on grid +1 frame (24 fps), see §2.1.**
Binding inputs: investor decisions 2026-11-24 (instrumental OP in every S1 episode; **no characters**; "never skipped": motion in every cut; **hard cap $10 for the whole OP including retakes**, Kling 2.5 TP only), **`reports/lore-op-2026-11-24.md` (binding, applied verbatim)**, `reports/vfx-op-review-2026-11-24.md`, `reports/analyst-op-review-2026-11-24.md`, `reports/lore-v4-2026-11-24.md` §1(d), `canon/excerpts/for_director_and_artist.md` §1–§3, §7, `direction/visual_bible.md` §5, §8, §10, `direction/limited_animation.md` (L-codes), `direction/video_test/RESULTS.md`.
v1.1 is superseded by this file. Cut ids of v1.1 are kept so the keeper's edits map one to one; new cuts carry a letter (02b, 13b, 24b, 31b, 31c, 32b).

## 0. Кратко (RU)

- **38 планов + 9 кадров чёрного** перед дропом, ASL ≈2.4 с, движение в каждом плане. Персонажей нет. Человеческий след без людей: множество следов босых ног разного размера на переулке под первым ливнем (26, R2.2), тканые фигуры панели 2 (18). Пара в 13 нет (R2.3).
- **Новых кадров NB2: 16. Клипов Kling 2.5 TP: 17** (по 1 дублю). K06 → ffmpeg (VFX). K16 остаётся клипом: хранитель заменил источник на открытое море, и причины VFX для перевода в ffmpeg (Шпили, достройка крыш) отпали. Добавлены F01a/K01a (волна до удара) и F26/K18 (следы).
- **Смета: $7.23 (из них K13 $0.35 ждёт хранителя и директора студии) + резерв на передубли $1.12 = $8.35**; потолок прогона $9.85 (`BUDGET_LIMIT_USD=64`), инвесторский потолок $10 (§8).
- **Крючок 0:00:** без фейда из чёрного, сразу читаемый кадр: огромная волна идёт на дамбу со стороны моря, склейка до удара. Ответ на вопрос — на 0:57.0. Петля волны: подход (01) → удар (25) → брызги стирают кадр в титр (33).
- **Кульминация 1:09–1:22.5** перемонтирована из уже заложенных клипов: склейка на каждый удар тайко, затем гавань стекленеет четырьмя ступенями на ударах 1:13.5 / 1:15.0 / 1:16.5 / 1:18.0, каждая ступень ровно по всему кадру сразу, без фронта и направления (хранитель R2.4), чистое стекло 1:19.5–1:22.5, титр на 1:22.5. Условия хранителя (шторм кончается над открытым морем, без Шпилей, без дождя в гавани, только вайп брызгами перед титром) соблюдены.
- **«Вдох» перед 0:57:** вспышки волны в наезде на карту, на атаке 0:56.63 — 9 кадров чёрного, удар K01 с кадра 0.
- **Варианты по сериям видимые:** A — крупные зарубки на чистом поле гроссбуха (14), камера в конце плана стоит на них; B — грейд титульной плиты по часу серии, держится весь хвост и красит брызги вайпа. C отклонён хранителем.
- **Хвост, опенинг 87.0 с:** склейка 33 = 1:22.5–1:27.0 (4.5 с); облака K17 — кусок 0.0–4.5 с на 1×, без растяжки и без стоп-кадра; капля с края буквы падает на 1:25.0 (рифма с каплей 0:11.25), все капли уходят из кадра до 1:26.5; изображение и звук гаснут 1:26.5–1:27.0 (музыка на 1:27.0 ещё ≈ −40 дБ, поэтому фейд, а не обрыв).

---

## 1. Rules checked on every cut

| # | Rule | Source |
|---|---|---|
| OP-1 | **No characters.** No named or recognizable person, no face, no portrait, no hands in close-up. Tiny anonymous distant silhouettes only as scale (≤ ~3% of frame height each) | investor 2026-11-24 |
| OP-2 | **No stone, no shard**, no black pebble on a cord, no cracked black stone, no relay stones or their cages; **no ring**; **no gate and no bars**. Heraldic devices that hold a stone (Ilvane hand), a ring (Quell eel) or a gate (Rusk) appear only small and woven inside tapestry panel 2: never in a close-up, never in a push-in or a hold on that banner, never in neighbouring cuts | SEC-027, S-13, SEC-009, excerpt §1 |
| OP-3 | **Nothing glows.** No light in Spire grooves (stricter than v4 §3.3), no glowing water, cracks, veins, lightning. Lanterns are small practical flames, no bloom halo. Flashes in the edit are short exposure pops or dark ink-frames, never a light source in the picture | G3, G4, G15; studio rule |
| OP-4 | **Spires:** smooth glassy black, ring of open arches at the crown, deep spiral grooves, near side "/" (lower-left to upper-right), dark unlit foot (standing in water only for a tower that stands among the stilt-houses; the Crown Spire stands on the hill). Check at full size on every Spire frame and on every 10th frame of a Spire clip | G5, excerpt §3 |
| OP-5 | **No spoilers for any S1 episode:** no water over the dike into the Lows, no flooded houses or ruin, no night flood (E10); no gate, no bar across a gate, nothing from the Sc 1/Sc 18 gate (PL-0021); no tide-post (PL-0022, from S1E3); no cracked or damaged Spire; no IX wash, no Ninth tier reading, no signature line or seal on the map; no *Chronicle of the Dry Years* book or page; no rings on water (the stone's motif); no water rising on a marked post (tide-post motif); no weir or sluice channel taking in the sea; no cracked dike or wall; no puddles that shiver; nothing from the back-canal sill where the shard is found (sc03-sh060/070) | v4 §3.3, keeper §7 |
| OP-6 | **Tapestry panels 1, 2, 5 only** (this board: 2 and 5). Never 3, 4, 6. Fabric fills the frame | keeper §7, G13 |
| OP-7 | **Heraldry:** tall vertical banner, slanted cut at the bottom, long point at the pole (DEC-66); fields and devices per `refs/HERALDRY/H0x` and G11; no shields; seals round | G11, DEC-66 |
| OP-8 | Spirals turn **sunwise** (clockwise from the centre outward as the camera sees it); pass `refs/HERALDRY/H16_ashare_reference_spiral.png` when a spiral must read. Rotation whose direction matters is done in ffmpeg, never asked of Kling in words | excerpt §3; VFX §2.1.5 |
| OP-9 | **Compass:** sea and harbour west, the sun sets over the sea; the hill (Steps, Crown Spire) east; the Lows in the dike's shadow, never in high direct sun | DEC-65 |
| OP-10 | No text in generated frames. Only on-screen text: the HOLLOWSTONE logo and the small corner bug ANIME-STYLE · AI-ANIMATED (from the OP on). Lower 15% free of key detail | visual bible §5, v4 §2 |
| OP-11 | **No hflip** of any frame or clip (also not for whips, match cuts or the "reversed" spray wipe: reverse only in time or by mask direction) | visual bible §11.2 |
| OP-12 | Video: Kling 2.5 TP only. Each motion prompt lists what must not change; "no new light sources, lighting unchanged, no glowing marks" in every prompt. One action per clip; phase changes (rise → hang → fall, choppy → still) are made in the edit | RESULTS.md, investor, VFX §2.1 |
| OP-13 | **Own title language.** The tapestry is finished cloth filmed by a camera: it never weaves itself, threads never move. The map is a flat printed sheet: nothing grows, rises, turns or assembles on it | analyst §1 (similarity) |
| OP-14 | **Human traces without people** (analyst #3, within OP-1/lore): footprints (26), woven figures of panel 2 (18), washing lines and chimney smoke (10). Never feet, shoes, hands, figures or silhouettes added by generation; every trace is checked by the keeper as "not a specific scene" | analyst #3, keeper |

## 2. Music map (measured on `lib_mus_theme-op-drums_v2a.mp3`, 2026-11-24)

Measured: 10 ms RMS envelope + onset flux (ffmpeg + numpy, $0), v2a and v2b. Both files: identical grid, both run past the OP end (the OP uses 0:00.0–1:27.0); hits at 12.03, 69.03, 73.53, 75.03, 76.53, 82.53 s (+0.03…+0.05 s late, matching the analyst's 57.05 / 82.55 and the VFX director's attack scan). Tail: −21.6 dB at 1:23, −33.9 at 1:25, **−44 dB from ≈1:26** → effective silence from **≈1:26.5**.

| Section | OP time | Bars | Heard | Picture job |
|---|---|---|---|---|
| S1 Intro | 0:00.0–0:12.0 | 1–4 | solo cello, no drums (optional taiko on 0:00.0 asked of the composer, §10) | hook image readable at frame 0, then the world wakes at dawn |
| S2 Groove | 0:12.0–0:21.0 | 5–7 | stamps on beats 1 and 3, claps, barrel; whistle attack **0:20.45** | the Lows at work, cuts on the beat |
| S3 Theme | 0:21.0–0:45.0 | 8–15 | strings carry the melody; loudness flat from 0:24 | the city climbs, Lows → Mids → Steps, morning → afternoon; camera speed rises cut by cut |
| S4 Rise | 0:45.0–0:57.0 | 16–19 | brass calls, snare build; loudest half-bar is the fill at **0:55.5**; pre-hit attack **0:56.63** | houses: tapestry, banners, the map; cuts shorten to 1.5 s; inhale: wave flashes, then 9 frames of black |
| S5 Hook | **0:57.0**–1:09.0 | 20–23 | octave leap on 0:57.0, full drums | payoff: the sea hits the wall; the Lows take the storm; the storm breaks over the open sea |
| S6 Answer | 1:09.0–1:21.0 | 24–27 | full energy, taiko every 1.5 s, cadence | climax: the storm breaks over the open sea; at last light the harbour turns to glass (the S01E01 Sc 9 image; no Spire, no singer in frame) |
| S7 Last hit + tail | 1:21.0–1:27.0 | 28–29 | hits every 1.5 s, **last hit 1:22.5**, silence from ≈1:26.5 (≈ −40 dB residual at 1:27.0) | title sting on the last hit; tail carried by moving clouds and one falling drop; picture and audio fade 1:26.5–1:27.0 (§4.3) |

### 2.1 Hit frames (24 fps; grid frame = t × 24; **placed = grid + 1 frame**)

Cut points stay on grid frames. Everything that must *hit* (impact frame, INK, POP, SHAKE onset, glass step, logo landing) sits one frame later. Measured attacks that are already off-grid (whistle, pre-hit) are used as measured, rounded up to the next frame.

| Event | Grid / measured | Grid frame | **Placed frame** | Cut |
|---|---|---|---|---|
| First stamp, groove hits every 1.5 s | 0:12.0 + 1.5 k | 288 + 36 k | **289 + 36 k** | 05–09 |
| Whistle POP | measured 0:20.45 | — | **491** | 09 |
| Bell strike | 0:28.5 | 684 | **685** | 12 |
| Coin settles | 0:35.25 | 846 | **847** | 14 |
| Wave flashes in the map push | 0:55.5 / 0:56.25 / 0:56.44 | 1332 / 1350 / 1355 (1354.6 rounded) | **1333 / 1351 / 1356** (all three = grid + 1; 1356 kept, director F2) | 24 |
| Cut to black (pre-hit) | measured 0:56.63 | 1359.1 | **1360** (black 1360–1368) | 24b |
| **Octave leap: K01 frame 0 + INK** | 0:57.0 | 1368 | **1369** (INK 1369–1370) | 25 |
| Rain-hit on the footprints | 1:00.0 | 1440 | **1441** | 26 |
| **S6 downbeat: INK** | 1:09.0 | 1656 | **1657** (INK 1657–1658) | 31 |
| Glass steps 1–4 (POP + SHAKE 6 px) | 1:13.5 / 1:15.0 / 1:16.5 / 1:18.0 | 1764 / 1800 / 1836 / 1872 | **1765 / 1801 / 1837 / 1873** | 32 |
| Penultimate hit (POP only) | 1:21.0 | 1944 | **1945** | 32b |
| **Last hit: INK → spray wipe → logo** | 1:22.5 | 1980 | **1981** (INK 1981–1982, wipe 1983–1994, logo lands 1995–2002) | 33 |
| Drop leaves the logo (no drum hit; rhymes with the drop of 0:11.25, frame 270) | 1:25.0 | 2040 | **2040** (not shifted) | 33 |
| Music silence; all drops out of frame | ≈1:26.5 | 2076 | — | 33 |
| **Picture + audio fade** | 1:26.5–1:27.0 | 2076–2087 | **2076–2087** (last frame of the OP = 2087) | 33 |

## 3. Free VFX toolkit (ffmpeg passes; code names used in §4)

Working recipes for every code (tested on ffmpeg 6.1.1 by the VFX director) are in `reports/vfx-op-review-2026-11-24.md` §3; the table names the section. Pass order: plate → in-world effects (spray, caustics, cloud shadows) → camera (PUSH/PX/WHIP, **SHAKE last**, plate margin ≥ 1.05×) → screen effects (rain on lens, POP, INK) → grade and grain. Kling output 1928×1072 is fitted with `scale=1940:1080,crop=1920:1080`.

| Code | Pass | How (ffmpeg) | Rule |
|---|---|---|---|
| **PX** | multi-plane parallax from one still | soft masks (sky / far / near), each layer moved at its own speed, L-04 | plate margin ≥ 1.25× |
| **PUSH / PULL / TILT / PAN** | camera moves on stills or on clips | `zoompan`/`crop`, eased (L-01…L-03) | ≤ 15% scale per 3 s except whip and rush; mid-theme chain 4 → 6 → 8 → 10 → 12% (cuts 13–17) |
| **RAMP** | speed ramp | `setpts` piecewise; slow-mo only at exactly 1/3 ("on threes") or via `framerate` blend; fast parts `tmix` | never 0.35×; never `minterpolate` (VFX §3.4) |
| **RAIN** | rain layer | L-06, 2 depths, plate darkened `eq=brightness=-0.05:contrast=1.08` first; **one angle for all storm cuts 25–30: `rotate=a=0.22`, wind from screen left** (same as the banners) | grey-white, never bright (VFX §3.6) |
| **SPRAY** | spray / droplets | drop field + radial `zoompan` + gravity layer (VFX §3.5) | grey-white, opacity 0.35–0.6 |
| **MIST / DUST** | mist drift, dust in beams | L-08, L-07 | shafts only where the source is in frame |
| **CLOUD** | cloud shadows + rolling light | noise field → blur → multiply 28% scrolling; rolling light = soft diagonal band, `softlight` 0.25, always from the west (sea side) (VFX §3.7) | motivated by sky in or just out of frame |
| **SHAKE** | camera shake on hits | decaying sine, 6–12 px per beat, 20 px on big hits (VFX §3.1) | starts on the placed hit frame (§2.1) |
| **POP** | exposure pop | `eq=brightness=+0.06` for 2 frames | never a white-out |
| **INK** | impact ink-frame | 2 frames `negate` + posterize to blue-black and linen | only 0:57.0, 1:09.0, 1:22.5 |
| **WHIP** | whip transition | directional blur ramp, cut on the beat (VFX §3.3) | max 3 in the OP (09, 16 in, 28) |
| **ROT** | wheel / coin rotation | rim mask + `rotate` with ease-in (VFX §3.8); coin = `scale=w=abs(cos)` sprite (VFX §3.9) | positive angle = clockwise (OP-8) |
| **GLASS** | stepped calm | 4 steps on the drum hits; each step lowers the chop **evenly over the whole harbour at once** (K13 retimed 1× → 0.6× → 0.3×, mixed into H2 at 25 / 50 / 75 / 100 %); no front, no edge, no direction | nothing glows on the water (OP-3) |
| **WIPE** | torn spray wipe | `xfade` custom torn edge bottom→top, 0.5 s, K01 spray column ×1.6 `screen` 0.6 over the edge (VFX §3.12) | no dissolve before the title (keeper) |
| **GRADE** | per-episode LUT | `lut3d` dawn / day / dusk / night for the title plate, wipe and spray | variant B, §7 |

GLASS, keeper R2.4: no moving front; each step is an even mix over the whole frame.
```
[A][B]xfade=transition=custom:duration=6:offset=OFF:expr='st(0,(1-P)*4);st(1,ld(0)-floor(ld(0)));st(2,(floor(ld(0))+min(1,ld(1)*3))/4);A*(1-ld(2))+B*ld(2)'
```
A = K13 (chop, slowing 1× → 0.6× → 0.3× with frame blend), B = H2 (glass). The sky band above the horizon is taken from H2 from the start of cut 32 (pixel-aligned with H1). Each step jumps in the first third of its 1.5 s and holds. OFF = 1 frame after the start of cut 32, so step 1 starts on the placed hit frame 1765 (§2.1).

## 4. Shot table

Class: **K** = cut from a Kling 2.5 TP 5 s clip (K01…K18); **EXK** = existing Kling clip ($0); **LA** = ffmpeg only on a still. Source: **NEW** = NB2 frame (§5), **EX** = existing file. The keeper's text is kept verbatim in columns 1–8; v1.2 additions from the VFX director and the analyst are in the last column.

| # | In – Out | Sec | Music | Content and camera | Class / clip piece | Frame source | VFX passes | v1.2 additions (VFX / analyst) |
|---|---|---|---|---|---|---|---|---|
| 01 | 0:00.0–0:03.0 | 3.0 | S1 b1 | **HOOK:** the first frame is a finished, fully exposed picture at 0:00.0 (no fade from black). From the sea side, a huge dark wave rolls in toward the colossal brick dike, wind tearing foam off its crest; the dike's top edge is dry and nothing beyond it is visible but sky. Cut on 0:03.0, before it strikes: the question is answered at 0:57.0 | K01a piece 0.0–1.0 s at exactly 1/3 ("on threes") | NEW F01a (wave before impact) | SPRAY (foam torn off the crest, slow), MIST, light RAIN | analyst #2 (new first 3 s, no fade, a question not an abstraction; no longer pre-shows the payoff) + VFX §2.3 (F01a/K01a); keeper: outer face, daylight, the city beyond the wall not visible |
| 02 | 0:03.0–0:04.5 | 1.5 | S1 b2 | Highwater at dawn: tilt DOWN from the crown arches of the Crown Spire to the misty Lows below the dike; three planes slide apart | LA | EX refs/PL-0004/D01_A_dawn-ebb_v1.png (paint out locally every crack line on all three Spires — left, centre AND right; full-size check, OP-5; done at $0: `tools/op_paintouts.py` → `output/opening/plates/D01_A_op.png`) | TILT, PX (sky / Spires+hill / Lows), MIST | shortened to 1.5 s (analyst #2); CLOUD shadow drifting over the Lows (VFX) |
| 02b | 0:04.5–0:06.0 | 1.5 | S1 b2 beat 3 | ECU: one knot of the tarred net; a drop swells and falls out of frame (it never lands on water in frame) | K03 piece 0.0–1.5 s, crop 1.5× on the knots (left part of F04) | NEW F04 | PULL 2%, grain | analyst #2: the pulse starts before the groove; the drop leaves the knot ≈0:05.25 |
| 03 | 0:06.0–0:09.0 | 3.0 | S1 b3 | The Ninth's lane at dawn: mist drifts, the rope bridge sways; the puddles stay still | EXK piece 0.5–3.5 s | EX output/video_test/alley__kling-2.5-turbo-pro.mp4 + static patch of plain brick wall over the double gate at the end of the lane and over the ring knocker on the left door (the clip camera is static; patch under the MIST layer); if the puddles ripple in the clip, freeze them from frame 0 with the same patch | MIST second layer (over the patch), slow PUSH 4% | — |
| 04 | 0:09.0–0:12.0 | 3.0 | S1 b4 (phrase hangs) | ECU: a tarred net hung to dry, drops gather and fall from the knots; behind, a rope with nine small unlit lanterns sways | K03 piece 1.5–4.5 s (window slid so the last drop leaves on 0:11.25) | NEW F04 (net) | PULL 3% (focus feel), RACK-like blur ramp; the last drop leaves the knot on 0:11.25 and falls out of frame — no drop lands on water in frame, no rings on water | window may slide ±2 s inside the 5 s clip (VFX) |
| 05 | 0:12.0–0:13.5 | 1.5 | S2 b5 (first stamp) | The hub of a giant treadwheel lurches into motion, spokes start to turn | **LA** (was K06) | EX animatic sc06-sh010_a.png (paint out locally the crack lines on the great wall behind the wheel: the dike reads intact, OP-5; done at $0: `output/opening/plates/sc06_wheel_op.png`) | SHAKE on 0:12.0, POP | VFX top-5 #4: ROT recipe — the rim circle rotates clockwise from rest, start on frame 289, ease-in to 1.8 rad/s; the vertical post and brace in front are cut from the plate and laid on top, still. Wall paint-out done before the mask is cut |
| 06 | 0:13.5–0:15.0 | 1.5 | S2 b5 beat 3 | Inside the drum's rim: slats rush past the lens | K04 piece 0.5–2.0 s | EX `refs/PL-0008W/D05_W2_morning_v1.png` | SHAKE on 0:13.5, motion-blur streaks | streaks = `tmix=frames=3`; K04 safer wording (§6) |
| 07 | 0:15.0–0:18.0 | 3.0 | S2 b6 | The three great treadwheels in a row turning; push in | K05 piece 0.0–3.0 s | EX `refs/PL-0008W/D05_W1_morning_v1.png` | PUSH 6%, SHAKE on 0:15.0 and 0:16.5, MIST | VFX fix: no "tiny figures" in the prompt (Kling would paint people onto a plate that has none); spoke count checked every 10th frame |
| 08 | 0:18.0–0:19.5 | 1.5 | S2 b7 | Punch-in: the nine lanterns swing on their rope in the gust | K03 piece 2.5–4.0 s (crop 60%, local upscale) | NEW F04 | SHAKE; the nine lanterns stay unlit — no spark, no flame, no single lantern singled out | grain over the 1.67× upscale |
| 09 | 0:19.5–0:21.0 | 1.5 | S2 b7 beat 3 (whistle) | Wheel shed → **WHIP UP** into the morning sky, blur peaks on the whistle, cut on 0:21.0 | K05 piece 4.0–4.75 s + WHIP | EX (K05) | WHIP (up), POP on the whistle | POP on the measured attack 0:20.45 (frame 491), not on the grid |
| 10 | 0:21.0–0:24.0 | 3.0 | S3 b8 (theme enters) | Flyover: the camera glides forward over the stilt-town — lanes of water, plank bridges, washing lines — toward the dike and the hill; the town lies below the dike's crest | K07 piece 0.5–3.5 s | NEW F10 (aerial) | PX on the sky band, MIST | K07 one move only (no "slightly down") |
| 11 | 0:24.0–0:27.0 | 3.0 | S3 b9 | Under a plank bridge: the ebb runs out between the tarred pilings, baring wet silt | K08 piece 1.0–4.0 s | NEW F11 (pilings) | caustic shimmer on the bridge underside (L-15, soft), slow PUSH | if the level does not move in K08: L-16 level mask on top, **falling only**, −25 px over 3 s (VFX fallback, keeper direction) |
| 12 | 0:27.0–0:30.0 | 3.0 | S3 b10 (Mids) | A small bronze bell in its niche swings and its clapper strikes once; dust shakes down through a window beam | K09 piece slid so the strike lands on 0:28.5 | EX animatic sc16-sh040_a.png, crop to x ≤ 960 px (the two lit desk lamps on the right out of frame, OP-3) | DUST in the beam, shafts from the window, POP on the strike | strike / POP on frame 685 |
| 13 | 0:30.0–0:31.5 | 1.5 | S3 b11 | The counting hall: rows of empty desks with open ledgers and glasses, light falling through tall windows; dolly down the aisle | LA | EX refs/PL-0011/D11_L1_late-aft_v1.png (check the far end: no figure; paint out locally the brass cage with the dark stone above the far door — a relay stone, OP-2; keep the balance) | PUSH along the aisle, PX (window wall vs desks), DUST, shafts moving 2% | VFX #2: split at the string attack 0:31.5; PUSH 4% (first step of the speed chain); CLOUD rolling light from the windows (west). Analyst #3: no human trace in 13 (keeper R2.3): no steam; no glass, chair or pen singled out; no close view of the water in a glass |
| 13b | 0:31.5–0:33.0 | 1.5 | S3 b11 beat 3 | Same hall, cut in 1.4× on the open ledger of the nearest left-hand desk; dust turns in the beam | LA | EX (plate of 13, same paint-outs) | PUSH 6%, DUST | VFX #2: ledger → ledger rhyme with 14 |
| 14 | 0:33.0–0:36.0 | 3.0 | S3 b12 | Top-down: the tall leaning stack of copper coins topples to the right and slides across the felt beside an open ledger; one coin spins and settles | K10 piece 0.5–3.5 s | NEW F14 (coins) | slow rotate-PUSH 3°; **variant A** tally marks (§7) | spinning coin = ROT sprite (VFX §3.9), settles on frame 847; PUSH 8%; **variant A made visible** (analyst #4): bold ink strokes in the clean left margin, the coins fall away from it, the move ends with the margin in the left third for the last 1.0 s |
| 15 | 0:36.0–0:39.0 | 3.0 | S3 b13 (Steps) | The city on its granite hill seen from the harbour: the great wall rising from the harbour water, terraces, palace, ships, three Spires lit from the west (camera side); the Lows lie behind and below the wall, out of sight; lateral move | LA | NEW F15 (edit of refs/PL-0004/D01_C_late-aft_v1.png; D01_A_late-aft is not a fallback: cracked, pale towers) | PX (water / ships / hill / sky), PAN right, slow cloud drift on the sky layer | VFX #2: CLOUD shadows run across the city + rolling light from the west; PAN 10%; its speed carries into the tilt of 16 (one vector, no WHIP) |
| 16 | 0:39.0–0:42.0 | 3.0 | S3 b14 | Low angle on the Crown Spire: tilt UP the grooves to the ring of arches; clouds stream past the crown | LA | EX `refs/PL-0014/D08_S1_late-aft_v1.png` (G5 full-size check) | TILT, PX (tower vs sky), cloud layer drift, MIST at the foot | enters at the speed of 15's pan ("lift"); TILT 12% |
| 17 | 0:42.0–0:45.0 | 3.0 | S3 b15 | The palace wall with a row of five banners (Corvane, Dask, the Choir, Lantry, Fennick), the city and the sea far below; slow pan along the banners | LA | NEW F17 (edit of animatic sc10-sh030_a.png; the animatic frame itself is not used in the OP) | PAN, PX (wall+banners vs city), banner sway faked by 1–2 px per-banner sine displacement (displace with a vertical gradient) | displace on the 2–3 nearest banners only (VFX); CLOUD shadows; last frames line the row of banners up with the woven row of 18 (shape match cut, analyst #3; no push-in on 18) |
| 18 | 0:45.0–0:48.0 | 3.0 | S4 b16 (brass) | Tapestry panel 2 (finished cloth): nine woven banners on the shore, nine small woven figures in three-quarter back view, each with one hand raised, facing the black tower | LA | NEW F18 (panel 2 re-weave; also fixes pilot sc05-sh020/070) | PAN left→right holding the full height of the panel; no push-in, no hold and no punch-in on banners 1, 5 or 6 (gate, hand, eel); lint/dust in raking light, fabric micro-ripple (displace, 2 px) | OP-13: nothing is woven on screen. The woven figures are the OP's faceless people (analyst #3) |
| 19 | 0:48.0–0:49.5 | 1.5 | S4 b17 | Banner CORVANE snaps in the wind | K11 piece, left 0.6 of the width, 0.5–2.0 s | NEW F19 (banners A) | SHAKE light, POP | crop 0.6 W ≈ 1.66× (VFX banner split); emblem whole at mid-height |
| 20 | 0:49.5–0:51.0 | 1.5 | S4 b17 beat 3 | Banner DASK | K11 piece, right 0.6 of the width, 2.5–4.0 s | NEW F19 | MATCH (fold-to-fold), POP | as 19 |
| 21 | 0:51.0–0:52.5 | 1.5 | S4 b18 | Banner LANTRY | K12 piece, left 0.6, 0.5–2.0 s | NEW F21 (banners B) | POP | as 19 |
| 22 | 0:52.5–0:54.0 | 1.5 | S4 b18 beat 3 | Banner FENNICK | K12 piece, right 0.6, 2.5–4.0 s | NEW F21 | POP | as 19; same order in every episode (a per-episode order would be a signal, keeper on variant C) |
| 23 | 0:54.0–0:55.5 | 1.5 | S4 b19 (snare) | Tapestry panel 5: the cormorant sail across the harbour mouth, ships at sea | LA | NEW F23 (edit of refs/TAPESTRY/E06_panel5_v1.png; also replaces panel 5 in pilot Sc 4) | fast PUSH 12%, fabric ripple, snare-roll micro-SHAKE | — |
| 24 | 0:55.5–0:56.667 | 1.17 | S4 b19 beat 3 (fill, roll) | The Tithe Map top-down with its three tier tints; accelerating push **toward the hill (east)** | LA | EX `refs/M-MAP/E05_map_base_v1.png` + the three tier tints, Steps / Mids / Lows (drawn at $0 by `tools/op_paintouts.py` → `output/opening/plates/E05_map_tints_op.png`; no IX wash, no legend row 4, no signature line; never pushes toward the Ninth, south-west) | PUSH ease-in 0→25% | VFX #3: three 2-frame wave flashes (K01 frames through INK) on frames 1333, 1351, 1356; SHAKE every 0.375 s from 0:55.5 (analyst: loudest half-bar). The v1.1 whip-out is replaced by the cut to black. OP-13: a flat sheet, nothing grows on it |
| 24b | 0:56.667–0:57.042 | 9 fr | pre-hit attack 0:56.63 | **Black** (frames 1360–1368) | — | — | — | VFX #3 "inhale"; the only cut without motion, by design |
| 25 | **0:57.042**–1:00.0 | 2.96 | S5 b20 — **octave leap** | **PAYOFF:** the wave strikes the outer face of the great sea dike; white spray rises high above the crest in one heavy column and falls back to the sea; the crest stays dry | K01 piece 0.0–2.96 s at 1× (**impact = K01 frame 0 on frame 1369**) | NEW F01 | INK on 0:57.0, SHAKE 20 px decaying 1 s, SPRAY overlay (extra), RAIN | VFX fix: F01 already shows contact, so the hit is made by the cut (black → INK → frame 0), not by Kling physics. INK frames 1369–1370 |
| 26 | 1:00.0–1:01.5 | 1.5 | S5 b21 | The first heavy rain on a tarred plank-walk between stilt-houses: many wet bare footprints of mixed sizes criss-cross the planks in different directions, the everyday traffic of the lane; the rain blurs them away | K18 piece 0.5–2.0 s | NEW F26 (footprints) | RAIN, SHAKE on 1:00.0 | analyst #3 (human trace, keeper check); also the VFX fix: the K13 piece is gone from 26, so 31 no longer repeats it. The keeper's lamp-post note for 26 moves with the harbour plate to 31–32b |
| 27 | 1:01.5–1:03.0 | 1.5 | S5 b21 beat 3 | The seaward end of the harbour mole: a wave bursts on the outer blocks and the spray falls back into the open sea | K14 piece 1.0–2.5 s | NEW F27 (mole) | SPRAY, MIST, POP | — |
| 28 | 1:03.0–1:04.5 | 1.5 | S5 b22 | Low rush along a canal between stilt-houses in the squall, pilings flicking past; the water lies low, far below the plank-walks | K15 piece 0.0–3.0 s at RAMP 2× + `tmix=3` | NEW F28 (canal) | RAMP, RAIN (fast angle), WHIP in | VFX: speed is made in the edit (K15 asks for a moderate speed). Acceptance: pilings stable 0–3 s; if only 0–2 s hold → piece 0.0–2.0 at 1.33× + zoom-blur (§6 fallback) |
| 29 | 1:04.5–1:06.0 | 1.5 | S5 b22 beat 3 | The treadwheel rim at full speed (rhyme with cut 06) | K04 piece 2.0–5.0 s at RAMP 2× | EX (K04) | MATCH to cut 28's direction, SHAKE | — |
| 30 | 1:06.0–1:09.0 | 3.0 | S5 b23 | Out over the open sea west of the city: rain sheets sweep the swell, the storm clouds tear and a gap opens low over the horizon | K16 piece 0.5–3.5 s | NEW F30 (open sea) | RAIN 2 depths, TILT assist, cloud gap opening = soft light shaft (motivated by the cloud gap) | K16 stays a Kling clip: with the open-sea source the VFX reasons for LA (Spires, invented roofs) are gone |
| 31 | 1:09.0–1:10.5 | 1.5 | S6 b24 | **CLIMAX part 1:** the harbour at last light in a hard wind (the wind-chop of S01E01 Sc 9) — the chop dies down, the masts slow and stop; no Spire in frame | K13 piece 0.0–1.5 s | EX `refs/PL-0018/D09_H1_late-aft_v1.png`, cropped **before Kling** to the top 74% (x 179–1197, y 0–572: the dark arch, the side finials and the near quay are out; paint out locally the tip of the central finial left at the bottom edge); pier lamp-posts unlit: darken their flames and remove their reflections locally on the plate (OP-3); both plates prepared at $0 by `direction/opening/tools/op_harbour_plates.py` → `output/opening/plates/D09_H1_op.png`, `D09_H2_op.png` (same mask on both, pixel for pixel; plates v2, gate R2 fixes 1 and 7: the finial re-filled with a shifted, Poisson-blended copy of the same rows — no ghost, no streak; the 6 lamp heads redrawn as unlit dark lanterns, the halo ring inpainted from the water — no warm ring, no orange bar, no blue patch; the keeper looks at them before K13, which waits for the studio director's go, C2) | INK on 1:09.0 (storm → evening), no RAIN in this cut, slow PUSH 5% | analyst #1: per-hit cuts 31 / 31b / 31c, all from K13; INK frames 1657–1658. "The chop dies down" happens across 31–32 in the edit (VFX: never asked of Kling) |
| 31b | 1:10.5–1:12.0 | 1.5 | S6 b24 beat 3 | Same harbour, cut in 1.5× on the big ship: masts swing in the chop; no Spire in frame | K13 piece 1.5–3.0 s, crop 1.5× | as 31 (same crop and paint-outs) | no RAIN, SHAKE 6 px on the hit | analyst #1 |
| 31c | 1:12.0–1:13.5 | 1.5 | S6 b25 | Cut in 1.3× on the harbour mouth under the low sun: the chop runs in from the open sea | K13 piece 3.0–4.5 s, crop 1.3× | as 31 | no RAIN, SHAKE 6 px on the hit | no glass yet; the calm of 32 has no front and no direction (keeper R2.4) |
| 32 | 1:13.5–1:19.5 | 6.0 | S6 b25 beat 3 – b27 beat 1 | **CLIMAX part 2:** wide again; on each of four drum hits the chop drops one step everywhere at once, until the water lies still; exact mirror reflections of hulls and masts, sun on the horizon; from 1:18.0 the whole harbour is glass | K13 piece 2.0–5.0 s retimed under the steps (1× → 0.6× → 0.3×, frame blend) → LA plate | EX `refs/PL-0018/D09_H2_glass_v1.png` (same crop as 31, pixel-aligned; K13 drift ≤ 4 px or `deshake`/crop shift); pier lamp-posts unlit: darken their flames and remove their reflections locally on the plate (OP-3) | GLASS (§3), POP + SHAKE 6 px on each step (frames 1765, 1801, 1837, 1873), no RAIN; nothing glows on the water; no Spire, no singer and no tapestry in this cut or in the cuts on either side | VFX top-5 #1 + analyst #1 (the turn to glass is earned on screen, on the beat). no front, no direction (keeper R2.4) |
| 32b | 1:19.5–1:22.5 | 3.0 | S6 b27 beat 3 – b28 beat 2 | Glass: cut in 1.12× toward the sun; the harbour perfectly still like glass, exact mirror reflections; the 1:21.0 hit lands here | LA | EX `refs/PL-0018/D09_H2_glass_v1.png` (crop of 32); pier lamp-posts unlit: darken their flames and remove their reflections locally on the plate (OP-3) | slow PUSH 4% toward the sun, the only motion = a drifting high-cloud layer (PX); nothing is added to the water; POP on frame 1945; no Spire, no singer and no tapestry in this cut or in the cuts on either side | 3 s of stillness as the inhale before the title (VFX, analyst) |
| 33 | **1:22.5**–1:27.0 | 4.5 | S7 last hit + tail | **TITLE STING:** on the last hit a torn wall of spray sweeps up across frame and leaves HOLLOWSTONE over the Crown Spire at dusk; clouds stream past the crown, the plate pushes 3%; one drop gathers on the lower edge of a letter and falls out of frame on 1:25.0; picture and audio fade 1:26.5–1:27.0 (tail, §4.3) | K17 piece 0.0–4.5 s at 1× (no stretch, no frame blend, no freeze frame); spray wipe | EX `refs/PL-0014/D08_S1_dusk_v1.png` (G5 check), framed on the crown and upper shaft, the foot below frame; logo graphic | INK on 1:22.5, WIPE (torn edge, K01 spray ×1.6 over the edge; the spray field ends with the wipe edge on frame 1994 and never stays on the tower, N1), logo lands with 114% → 100% overshoot in 8 frames, SHAKE 6 frames then still; **variant B** grade; the cut from 32 is the spray wipe only (no dissolve); no water surface (sea, harbour, pool or glass) and no foot of the tower in frame; the only water allowed is graphic spray residue on the logo letters: drops gather and slide on the letters only, never on the tower, never glow, and leave the frame without landing on anything; no rings; grooves dark in every variant-B grade; variant-B LUTs only dawn / day / dusk / night, never a sunset grade that matches cut 32 | VFX #5 + analyst #5: no freeze, the drop rhymes with 0:11.25; variant B also grades the wipe and spray. The drop on the logo is graphic spray residue, not water in the scene — confirmed by the keeper (R2.1). All drops leave the frame by 1:26.5 (frame 2076) |

**38 shots + 9 frames of black** (v1.1: 33). ASL ≈ 2.4 s. Every shot moves: 27 carry generated motion (26 from the 17 paid clips, cut 03 from the existing clip), 11 carry ffmpeg motion (parallax, push/tilt, rotation, particles, fabric displacement, the glass close-up).
Adjacency checks: no stone, ring or gate device outside panel 2 (cut 17 is the F17 row of five banners; Ilvane, Quell and Rusk appear only woven in cut 18, with no push-in); no gate or bar anywhere else (the gate at the end of the lane in cut 03 is patched out); no relay stone (cut 13 patched); tapestry cuts (18, 23) not adjacent to a Spire-crown image; no Spire in cuts 30–32; the map (24) never shows the Ninth.
v1.2 adjacency notes: "no Spire in cuts 30–32" covers 30, 31, 31b, 31c, 32, 32b; the harbour plates are cropped so the dark arch never shows (VFX flag); no Lows image (wheels, pilings, footprints) touches the glass sequence (§4.2).

Paid clips: K01, K01a, K03, K04, K05, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18 = **17 clips**. K02 = the existing video-test clip; K06 is now LA.

### 4.1 Per-cut layout of the climax (1:09.0–1:22.5)

| Time | Hit | Picture | Source |
|---|---|---|---|
| 1:09.0 | INK | harbour wide, hard wind-chop, masts swaying | K13 0.0–1.5 |
| 1:10.5 | SHAKE | ship close: masts swing | K13 1.5–3.0 ×1.5 |
| 1:12.0 | SHAKE | harbour mouth, chop running in from the sea | K13 3.0–4.5 ×1.3 |
| 1:13.5 | step 1 | wide: the chop drops one step over the whole harbour at once (25 %) | K13 → H2 |
| 1:15.0 | step 2 | the whole harbour one step calmer (50 %) | K13 → H2 |
| 1:16.5 | step 3 | the whole harbour one step calmer (75 %) | K13 → H2 |
| 1:18.0 | step 4 | the whole harbour is glass (100 %); hold to 1:19.5 | H2 |
| 1:19.5 | cut | glass close toward the sun; 1:21.0 POP | H2 |
| 1:22.5 | INK | spray wipe → HOLLOWSTONE | K17 |

### 4.2 Glass conditions (keeper, binding)

1. The storm ends over the open sea with no Spire (30).
2. 31 is the wind-chop of Sc 9 with no rain (31, 31b, 31c).
3. No Spire, singer or tapestry anywhere in 30–32b.
4. 32b and 33 are separated only by the spray wipe; there is no dissolve.
5. 33 has no water and no foot of the tower (the only exception is graphic spray residue on the logo letters, keeper R2.1, §4 cut 33).

v1.2 adds one director's rule on top: the analyst's "the Lows hold the water" images (wheels, pilings, banners) stay in S5 (0:57–1:09) and never sit next to the glass, so the cut cannot suggest who or what makes the water smooth.

### 4.3 Tail (1:22.5–1:27.0)

- 1:22.5: INK, then the wipe, then the logo lands and settles; 6 frames of SHAKE, then still letters.
- 1:22.5–1:27.0: K17 clouds keep moving: **piece 0.0–4.5 s at 1×** (no stretch, no frame blend, no freeze). The variant-B grade is held for the whole tail, the most visible place for it.
- 1:24.0–1:25.0: a drop gathers on the lower edge of one letter and leaves it on 1:25.0 (frame 2040), falling out of frame. It rhymes with the drop of 0:11.25 and closes the loop. One or two smaller drops (opacity 0.4) slide slowly down other letters and fall out of frame. **Every drop is out of frame by 1:26.5 (frame 2076).** Drops stay on the letters only (R2.1).
- ≈1:26.5: the music is silent (≈ −40 dB residual at 1:27.0, measured on v2a and v2b), so the end is a fade, not a hard stop.
- **The OP is 87.0 s (frames 0–2087).** Picture fade to black and audio fade 1:26.5–1:27.0 (frames 2076–2087), both linear.

## 5. NB2 frames (16 new, 1 take each)

All: `fal-ai/nano-banana-2/edit` with **exactly the parameters of the 164 earlier NB2 edit calls**: `aspect_ratio: "16:9"`, `num_images: 1`, `output_format: "png"`, `image_urls` = refs as listed, a fixed `seed` per frame, and **no `resolution` key** (fal default `1K`; no web search, no high thinking). Output size **1376×768 px** (as every existing 16:9 NB2 plate, e.g. `PL-0018/D09_H1`, `PL-0008W/D05_W1`; checked against the `meta.json` files and the PNGs). Price **$0.08 per image**, as booked in `pipeline/costs.py` and logged for all 164 calls; fal's pricing for this endpoint (read 2026-11-24, $0): $0.08 per image at 1K, 2K ×1.5, 4K ×2, so do not ask for a higher resolution. `pipeline/fal_client.generate_image(..., aspect_ratio="16:9", extra={"seed": N})` sends exactly this; the run script must not add `resolution`. The 1920×1080 frame is made in the edit (`scale`/`crop`, as for all plates). Each prompt = text below + `{STYLE_BASE}` + `{AVOID_OP}`, except F18 and F23 (CHRONICLE module + `{AVOID_OP_F18}`).

`{STYLE_BASE}` = visual bible §10.1 verbatim:
`2D anime-style TV series still, original character and world design, clean cel-shaded characters with crisp thin dark blue-black ink outlines of slightly varying weight, flat color fills with two shadow tones, cool violet-blue shadows, restrained highlights only on eyes, hair, metal and wet surfaces, detailed painterly matte-painting background with atmospheric haze, wet reflective stone and water, motivated cinematic lighting, muted desaturated palette with deep teal-black shadows, subtle film grain, grounded epic fantasy, 16:9 widescreen composition`

`{AVOID_OP}` =
`One single full-frame image: no inset, no letterbox bars, no frames or boxes drawn on top. No people and no faces (unless tiny distant silhouettes are allowed below). Avoid: photorealism, 3D look, chibi style, neon colors, any text, letters, numbers or labels, watermark, logo, multiple panels, split screen, glowing objects, glowing lines or cracks, light inside tower grooves, magic sparkles, lightning, mirrored image, shields, gates or bars across gates, stones or pebbles on cords, finger rings, rings on water.`

`{AVOID_OP_F18}` (only for F18 and F23, instead of `{AVOID_OP}`) =
`One single full-frame image: no inset, no letterbox bars, no frames or boxes drawn on top. Avoid: photorealism, 3D look, anime character, cel shading, neon colors, any text, letters, numbers or labels, watermark, logo, multiple panels, split screen, glowing objects, magic sparkles, mirrored image, shields, weapons, spears, swords, blood, faces in close-up, open mouths, stones or pebbles on cords.`

`{SPIRE}` = `the towers are smooth glassy black stone cones, each crowned by a ring of open arches, with deep spiral grooves winding up the whole height; on the near side of each tower the grooves rise from lower-left to upper-right ( / ); the grooves are dark, nothing lights up; the foot of each tower is dark unlit stone`

| Frame | Used in | Refs | Prompt (before STYLE_BASE + AVOID_OP) |
|---|---|---|---|
| **F01** wave impact | 25, 24 (flashes), 33 (wipe spray) | `PL-0004/D01_A_dawn-ebb_v1.png` (dike design) | `Wide low shot from the sea side of a colossal brick sea dike under a grey storm sky in daylight: a huge dark green-grey wave is just striking the dike's sloping outer face, a wall of white spray starting to rise; the top edge of the dike stays dry, no water pours over it. Wind-torn clouds, flying foam, cold grey light, rain. No people, no buildings breaking.` |
| **F01a** wave before impact (new, VFX) | 01 | `PL-0004/D01_A_dawn-ebb_v1.png` (dike design), F01 once accepted (same dike, same light) | `Wide low shot from the sea side of a colossal brick sea dike under a grey storm sky in daylight: a huge dark green-grey wave rolls toward the dike, its crest curling and torn by wind, still one wave-length away from the sloping outer face; the face is wet, the top edge of the dike dry and empty. Wind-torn clouds, flying foam, cold grey light, rain. No people.` + composition for the hook (analyst #2): `The wave fills the left half of the frame, the dike face rises on the right from the bottom edge to well above mid-frame, only sky beyond its top edge; one bold silhouette that reads at phone size.` |
| **F04** net + lanterns | 02b, 04, 08 | `PL-0008/D02_C1_dawn-ebb_v1.png` | `Extreme close-up of a heavy tarred fishing net hung to dry on a wooden pole in a stilt-town lane at dawn, the knotted mesh fills the left two thirds of the frame, clear water drops gathering on the knots, one drop about to fall. On the right, softly out of focus, a sagging rope strung between two stilt-houses with exactly nine small unlit tin lanterns hanging from it. Cold grey-teal dawn light from above, no direct sun, thin mist.` |
| **F10** aerial | 10 | `PL-0004/D01_A_dawn-ebb_v1.png`, `PL-0008/D02_C1_dawn-ebb_v1.png` | `High aerial view looking forward over a vast stilt-town below sea level in the morning: a maze of narrow water lanes, plank bridges and tarred roofs, washing lines, small boats tied to pilings; in the middle distance the long brick dike with three-storey brick houses along its crest, the town's roofs lying well below the dike's crest; beyond it a granite hill with terraces and a palace; on the hill two tall black towers, the left one the tallest; a third, shorter black tower stands lower down to the right at the edge of the stilt-town, its dark foot in the water. {SPIRE}. Cool grey light in the town, sun only on the hill and the tower tops. Tiny distant specks of people on far bridges allowed, none larger than a dot.` |
| **F11** pilings | 11 | `PL-0008/D02_C3_dusk_v1.png` | `Low shot at water level under a plank bridge between stilt-houses: tarred wooden pilings rising out of shallow dark water over wet silt, the pilings stained darker below an old weed line; no painted marks, no lines, no numbers, no post standing alone in open water; small eddies around the posts. Diffuse cool afternoon light, soft ripple reflections on the underside of the bridge. No people.` |
| **F14** coins | 14 | `M-LEDGER/E12_ledger_page-a_v1.png` (paper and ink style) | `Top-down view of an open clerk's ledger on worn green felt, ruled columns of tiny illegible ink scribbles, a wide empty margin on the left page, a brass inkwell and a quill at the top edge, a tall leaning tower of rough copper coins standing on the felt to the right of the ledger. Flat cool light from a tall window, dust motes. No hands, no readable text or numbers.` |
| **F15** city from the harbour (new, keeper) | 15 | `PL-0004/D01_C_late-aft_v1.png`, `PL-0014/D08_S1_late-aft_v1.png` (tower look) | `Use image 1 exactly — same hill, terraces, palace, three towers, ships and harbour, same camera. Change only: (1) remove the cluster of stilt-houses, piers and plank-walks in front of the great wall on the left; in their place open harbour water meeting the foot of the wall; (2) remove every crack, break and rough patch from the right-hand tower: its surface smooth glassy black like the others; (3) relight as late afternoon with the low sun behind the camera in the west: warm light on the face of the wall, the terraces and the towers; the sky behind the hill clear pale blue with a few warm clouds, no sunset glow behind the city. {SPIRE}.` |
| **F17** palace banners (new, keeper) | 17 | `output/S01E01/animatic/frames/sc10-sh030_a.png`, `HERALDRY/H01_corvane.png`, `H02_dusk.png`, `H08_choir.png`, `H07_lantry.png`, `H06_fennike.png` | `Use image 1 exactly — same granite wall, rail, poles, golden late-afternoon light and shadows, the city, harbour and sea on the right, same camera. Replace the row of banners with five banners evenly spaced along the same rail, each a tall vertical cloth banner with a slanted cut at the bottom and the long point at the pole side, simple flat emblems exactly as in the references, left to right: (1) deep blue field, a black cormorant with half-folded wings diving beak-down into a silver wave of exactly three crests, no fish; (2) ochre field, a bronze sickle with its blade up above three parallel dark-brown furrows, a tool with a short handle, not a crescent moon; (3) undyed linen field, nine short black strokes above one level black line; (4) black field, a copper beam balance with a level beam, the left pan holding a level surface of blue-grey water, the right pan empty; (5) acid sulphur-yellow field, a grey hare seated in profile facing left, both ears straight up and slightly apart, one eye visible. No other banners; no hands, no stones, no eels, no rings, no gates or bars.` |
| **F18** panel 2 re-weave | 18 (+ pilot sc05-sh020/070) | `TAPESTRY/E06_panel2_v1.png`, `TAPESTRY/E06_panel1_v1.png`, `HERALDRY/H01_corvane.png, H02_dusk.png, H04_rusk.png, H05_quell.png`, `GROUPS/C06_emblem_strip_ref.png`, `HERALDRY/H16_ashare_reference_spiral.png`. **Do not pass `H03_ilvane.png`** (the master shows a left hand; HS-003 needs the right hand) | `CHRONICLE` module **instead of** STYLE_BASE; avoid block `{AVOID_OP_F18}`: `Re-weave this tapestry panel keeping its weave, palette, border and the reed-and-river strip at the bottom: nine tall woven banners on a shore, each vertical with a slanted cut at the bottom and the long point at the pole; nine small woven figures, one under each banner, each with one hand raised in an oath, mouths closed, all turned in three-quarter back view toward a black tower rising from the woven sea beyond the shore; no weapons, no spears, no blades. Banners from left to right: (1) a black cliff of angular strata filling the banner, set with a small rust-red gate of vertical bars and two cross-bars, flat top, no spikes; (2) straw-yellow field, a black dike-spade crossed with a reed; (3) deep blue field, a black cormorant with half-folded wings diving beak-down into a silver wave of three crests; (4) ochre field, a bronze sickle blade up above three dark-brown furrows; (5) pale violet field, a white open RIGHT hand, palm toward the viewer, thumb on the viewer's right, fingers slightly spread, a small grey stone with a clockwise spiral resting in the palm; (6) bone-white field, a sea-green eel with a fin ridge making one full coil through a dark iron ring, head up, mouth closed; (7) white field, a grey harrow over a moss-green hill; (8) slate blue-green field, a white waterfall between two grey stones; (9) dark red field, a white unlit lantern on a black tower. Banners 1 and 2 stand together at the left edge, banners 3 to 8 in the centre, banner 9 alone at the right edge. Border spirals turn clockwise from the centre outward. Fabric fills the whole frame.` |
| **F19** banners A | 19, 20 | `HERALDRY/H01_corvane.png`, `HERALDRY/H02_dusk.png`, `PL-0004/D01_C_late-aft_v1.png` (light) | `Two tall silk banners side by side, each filling one half of the frame, hanging from poles on a granite terrace and snapping in a strong wind; each banner is vertical with a slanted cut at the bottom and the long point at the pole side. Left banner: deep blue field, a black cormorant with half-folded wings diving beak-down into a silver wave with exactly three crests, no fish. Right banner: ochre field, a bronze sickle with its blade up, set above three parallel dark-brown furrows; it reads as a tool with a short handle, not as a crescent moon. Emblems exactly as in the references. The two banners fill the frame edge to edge, each emblem centred at mid-height of its banner. Low golden afternoon sun from the left, pale open sky behind, crisp shadows in the folds.` |
| **F21** banners B | 21, 22 | `HERALDRY/H07_lantry.png`, `HERALDRY/H06_fennike.png`, same light ref | same wording as F19 with: `Left banner: black field, a polished copper beam balance with a level beam, the left pan holding a level surface of blue-grey water, the right pan empty. Right banner: acid sulphur-yellow field (not gold), a grey hare seated in profile facing left, both ears straight up and slightly apart, one eye visible.` |
| **F23** panel 5 fix (new, keeper) | 23 (+ pilot Sc 4) | `TAPESTRY/E06_panel5_v1.png`, `HERALDRY/H01_corvane.png`, `H16_ashare_reference_spiral.png` | `CHRONICLE` module; avoid block `{AVOID_OP_F18}`: `Use image 1 exactly — same weave, border, ships, sea, wave band and framing. Change only: (1) the emblem on the central white sail becomes a black cormorant with half-folded wings diving beak-down into a silver wave of three crests, no fish; (2) the small pennants at every masthead become deep blue; (3) the green-teal sails of the right-hand ship become ochre. Border spirals stay clockwise from the centre outward. Fabric fills the whole frame.` |
| **F26** footprints (new, analyst #3; prompt = keeper R2.2) | 26 | `PL-0008/D02_C3_dusk_v1.png` (planks, materials) | `Low close view along a wet tarred plank-walk between stilt-houses at the start of a storm in daylight: many wet bare footprints of mixed sizes criss-cross the dark planks in different directions and overlap, as on a busy lane; no single trail, no pair of prints walking side by side, no prints leading to the edge of the planks; the first heavy raindrops spatter on the wood; the water below the planks is far down and out of frame. Cold grey storm light. No people, no feet, no legs, no shoes, no shadows of people, no puddles.` |
| **F27** mole | 27 | `PL-0018/D09_H1_late-aft_v1.png` (mole stone) | `Low angle at the seaward end of a long granite harbour mole in a storm in daylight: a grey-green wave bursts against the outer blocks, a thick sheet of white spray is thrown up and falls back into the open sea; wet granite, squat stone bollards, rain, wind-torn clouds, cold grey light. The mole stands well above the sea; the harbour side and the town are out of frame. No gates, no beams or bars, no sluices or channels, no lamps, no people.` |
| **F28** canal | 28 | `PL-0008/D02_C3_dusk_v1.png`, `PL-0008/D02_C1_dawn-ebb_v1.png` | `Point of view just above the water, looking straight down a long narrow canal between two rows of stilt-houses in a squall: tarred pilings on both sides, low plank bridges crossing ahead, ropes and hanging nets, wind-driven rain, dark wind-ruffled water lying low between the pilings, far below the plank-walks, wet silt showing at the posts, strong one-point perspective toward a strip of grey sky at the far end. No people, no boats in the path.` |
| **F30** open sea (new, keeper) | 30 | none | `Wide view west over the open sea under a breaking storm in the late afternoon: heavy grey rain sheets slanting across a dark grey-green swell, low torn clouds racing, and just above the horizon a gap opening in the clouds where pale low sunlight falls on the sea in one soft broad shaft. Only sea and sky: no land, no towers, no buildings, no ships, no people.` |

| Frame / Used in | |
|---|---|
| **F01** wave | 25 (+ flashes 24, spray 33) |
| **F01a** wave before impact | 01 |
| **F04** net | 02b, 04, 08 |
| **F10** aerial | 10 |
| **F11** pilings | 11 |
| **F14** coins | 14 |
| **F15** city from the harbour | 15 |
| **F17** palace banners | 17 |
| **F18** panel 2 | 18 |
| **F19** banners A | 19, 20 |
| **F21** banners B | 21, 22 |
| **F23** panel 5 | 23 |
| **F26** footprints | 26 |
| **F27** mole | 27 |
| **F28** canal | 28 |
| **F30** open sea | 30 |

Acceptance order for every frame and clip: people/faces (OP-1) → stone/ring/gate (OP-2) → glow (OP-3) → grooves "/" and dark foot (OP-4) → gate/bar/water over the dike/marked post/cracks (OP-5) → text (OP-10) → heraldry per H0x (OP-7). **The keeper checks F15, F17, F18, F23 and F26 at full size before acceptance / assembly** (F15, F17, F18 and F23 have no clip; F26 feeds K18, which is accepted together with F26).

## 6. Kling 2.5 TP motion prompts (17 paid clips, 5 s, 1 take)

Prefix, **action clips** (K01, K01a, K04, K10, K11, K12, K13, K14, K15, K16): `2D anime animation, the colors and line art stay exactly as in the source image, stable outlines, no morphing, consistent lighting, no new light sources, no glowing marks.`
Prefix, **quiet clips** (K03, K05, K07, K08, K09, K17, K18): `Subtle 2D anime animation, the colors and line art stay exactly as in the source image, stable outlines, no morphing, consistent lighting, no new light sources, no glowing marks.`
Negative for all: `morphing, flickering line art, warping background, people appearing, faces, hands, glowing objects, light inside the tower grooves, lightning, sudden cuts, text`. Add for K01, K01a, K14: `explosion, fire, smoke, steam cloud, debris, broken bricks, water pouring over the dike, night`.
Words never used (VFX red list): "explodes", "crash", "fast", "first … then …", "clockwise / counter-clockwise". Where the edit adds SHAKE, the clip says `Locked-off camera, no camera shake`.

| Clip | Source | Camera + motion | MUST NOT CHANGE | Cuts |
|---|---|---|---|---|
| K01 | F01 | `Locked-off camera, no camera shake. White spray rises high above the dike in one heavy column, slowly spreads at the top and falls back toward the sea; sheets of foam slide down the wet sloping face; rain streaks. The brick dike does not move or change; its top edge stays dry and empty; no water flows over the top. Daylight storm, lighting unchanged, no smoke, no fire, no explosion.` | the dike stays intact; no water flows over the crest into the town; daylight storm, not night; no people | 25, 24 (flashes), 33 (wipe spray) |
| K01a | F01a | `Locked-off camera, no camera shake. The large dark wave swells and rolls steadily toward the dike; wind tears foam off its crest; rain streaks. The dike does not move or change; no water reaches its top.` | the dike stays intact; the wave does not reach the face within the clip; nothing beyond the crest; daylight; no people | 01 |
| K03 | F04 | `Static camera. Water drops gather on the net knots and fall one by one out of frame; a gust makes the rope of lanterns swing; the lanterns stay unlit and their number does not change.` | lanterns stay unlit and count nine; no spark or flame; drops fall out of frame and never land on water in frame; no rings on water; light; net shape | 02b, 04, 08 |
| K04 | `D05_W2_morning` | `Locked-off camera, no camera shake. The wooden slats of the drum move past steadily from top to bottom like a turning wheel; water drips from the slats. The drum keeps its shape; no people.` | drum geometry; light; no figures appear | 06, 29 |
| K05 | `D05_W1_morning` | `Very slow push-in. The three wooden treadwheels turn slowly and steadily, all at the same speed; water drips from the buckets. Wheel shape, spoke count and the shed do not change; no people appear.` | wheel count (3) and design; spoke count; no people; light | 07, 09 |
| K07 | F10 | `Smooth slow forward glide of the camera over the town toward the dike and the hill; thin smoke drifts from a few chimneys; mist moves along the water lanes.` | towers keep shape, height order, position (two on the hill, the third low at the edge of the stilt-town) and groove direction; nothing lights up; no new buildings; no people larger than dots | 10 |
| K08 | F11 | `Very slow push-in toward the pilings. The ebb runs out: the water level drops slowly by a hand's breadth, baring wet silt and the dark stain on the pilings; small eddies swirl around the posts, ripple reflections shimmer under the bridge.` | the water only falls, never rises; no marks appear on the pilings; no rings spreading from a single point; light; no people | 11 |
| K09 | animatic `sc16-sh040` (crop x ≤ 960 applied after) | `Static camera. The bell swings and its clapper strikes once, its rope sways; a little dust falls through the window light.` | bell, clapper, niche and door design; window light unchanged; desk lamps stay as they are (cropped out); no people | 12 |
| K10 | F14 | `Locked-off top-down camera. The tall leaning stack of copper coins slowly topples to the right in one piece; the coins spread and slide a short way across the felt and stop. Ledger, inkwell and quill do not move; no hands; no text.` | ledger and scribbles stay still and illegible; the left margin stays empty; no hands; no text; coins stay copper | 14 |
| K11 | F19 | `Locked-off camera, no camera shake. Both banners ripple and sway in a steady strong wind from the left; waves of cloth travel down to the slanted bottom points; the emblems stay flat, whole and readable; the poles do not move.` | both emblems and colours exactly as in the source; banner shape (slanted cut, long point at the pole); light | 19, 20 |
| K12 | F21 | `Locked-off camera, no camera shake. Both banners ripple and sway in a steady strong wind from the left; waves of cloth travel down to the slanted bottom points; the emblems stay flat, whole and readable; the poles do not move.` | both emblems and colours exactly as in the source; banner shape (slanted cut, long point at the pole); light | 21, 22 |
| K13 | `D09_H1_late-aft`, cropped as in cut 31, lamps darkened | `Locked-off camera, no camera shake. Choppy waves with white caps roll across the harbour the whole time; the ships rock very gently in place. Number, shape and position of all ships stay exactly the same; the sun stays where it is; no people.` | ship count and positions (drift ≤ 4 px against H2); sun position and colour; pier lamps stay dark; no people on decks; nothing glows | 31, 31b, 31c, 32 |
| K14 | F27 | `Static camera. The wave breaks against the mole; spray is thrown up and falls back into the open sea; foam slides back off the blocks; rain.` | the mole stays intact; no water crosses the mole to the harbour side; no gate, bars, channel or lamp appears; light | 27 |
| K15 | F28 | `The camera moves steadily forward at a moderate speed low over the water along the canal; pilings pass by on both sides; wind-driven rain. Houses and pilings keep their shape; no boats, no people.` | canal stays empty (no boats, no people); the water stays low and never rises toward the plank-walks; house design; light | 28 |
| K16 | F30 | `Static camera with a slow tilt up. Rain sheets sweep across the sea; the clouds move fast and the gap above the horizon slowly widens; the swell rolls.` | only sea and sky; no land, towers or ships appear; no lightning; the light stays soft, no new light sources; nothing glows on the water | 30 |
| K17 | `D08_S1_dusk` | `Very slow push-in. Clouds stream past the crown of the tower from left to right; the sky darkens very slightly.` | the tower's shape and groove direction "/"; grooves dark; the foot dark and below frame; no birds or lights added | 33 (piece 0.0–4.5 s at 1×) |
| K18 | F26 | `Locked-off camera. Heavy rain falls on the planks; the wet footprints slowly blur, spread and fade as the rain washes over them.` | no people, feet or shadows appear; no new footprints; no puddles; the planks keep their shape; light | 26 |

Note on K16: the keeper's text keeps the word "fast" for the clouds; it is binding and is left as written. The VFX concern ("fast" = boiling walls) does not apply to open sky; if the swell boils, the cut falls back to LA (below).

### 6.1 Fallbacks (VFX) — a failed first take never blocks the edit

| Clip | Risk | Acceptance | Fallback ($0, ffmpeg) |
|---|---|---|---|
| K01 | high | crest dry in every frame; no smoke, fire or debris; spray grey-white | LA: F01 + SPRAY burst (radial + gravity layer) + MIST + SHAKE 20 + INK |
| K01a | medium | the wave never touches the face; nothing over the crest | LA: F01a + PX (wave layer pushed 6% toward the dike) + foam SPRAY + RAIN |
| K06 → LA | — | — | built as ROT from the start (cut 05); no clip is made |
| K08 | high | level falls or stays, never rises; no marks appear | keep the clip if it is stable and overlay L-16 level mask, falling only (−25 px over 3 s, foam edge); else LA: F11 + caustics L-15 + mask |
| K10 | high | coins stay copper, do not merge or multiply; scribbles stay illegible | LA: F14 + coin sprites sliding on `overlay` paths + the ROT coin + DUST + rotate-push |
| K13 | high | ships count and positions fixed, drift ≤ 4 px vs H2 | LA: cropped H1 + ripple L-10 on a water mask; GLASS runs on top unchanged |
| K15 | high | pilings stable for the piece used | first 2 s good: piece 0.0–2.0 at 1.33× + zoom-blur; else LA: F28 + zoom-blur rush 1.0 → 1.35 in 1.5 s + slanted RAIN (VFX §3.10) |
| K16 | low–medium | only sea and sky; no glow | LA: F30 + RAIN 2 layers + cloud PX + light-shaft band opening by `crop` |
| K18 | medium | prints fade, nothing appears | LA: F26 + a luma-masked dissolve of the prints to a locally painted clean plank plate + RAIN |
| others | low | §5 order | LA version of the same source (still + PUSH/PX + RAIN/SPRAY/MIST) |

Retake reserve goes first to the hero clips K01, K01a, K13, K15.

## 7. Rewatch value

**Hidden details (3rd–5th viewing):**
1. **The wave loop.** The wave rolling in at 0:00 (01) is the one that hits the dike on the octave leap (25), and its spray wipes in the title (33). One wave, three moments; the hook's question is answered on the drop.
2. **Nine.** Nine banners in panel 2 (18), three Spires × three planes in cut 02. Counting fans will find the nine without anything being said.
3. **Two wheels.** The rim at 0:13.5 turns slowly, the same rim at 1:04.5 races (cuts 06 → 29): the Lows' work speeds up as the sea rises.
4. **Coin → hub rhyme.** The spinning coin (14) and the turning wheel hub (05) share a circle at the same screen position: money and labour drawn as one shape (MATCH framing note for the editor).
5. **Sunwise.** Every spiral in the OP (tapestry border, map rose) turns clockwise from the centre; the canon fans who learn the rule later will check it here.
6. **Two drops.** The drop that leaves the net at 0:11.25 and the drop that leaves the logo at 1:25.0.
7. **Someone was here.** The lane's footprints washed away by the first rain (26).

**Per-episode variants (free, ffmpeg only, no new generation; visible on purpose):**
- **A — the tally.** In cut 14 the clean left margin of the ledger carries bold hand-drawn ink tally strokes equal to the episode number (E1: one stroke … E12: two groups of five and two), each stroke ≈ 8–10% of frame height. The coins fall to the right, away from the margin, and the move ends on the margin for the last 1.0 s. Overlay drawn once as 12 PNG strokes ($0). No letters, no numbers. No spoiler.
- **B — the hour.** The title plate, the wipe and its spray (cut 33) are graded to the time of day in which that episode's cold open ends: four clearly different LUTs (dawn: grey-rose; day: pale blue; dusk: blue-violet after sundown, no gold; night: blue-black with a lighter cloud edge). Held for the whole tail, where it is seen longest. Grooves dark in every grade; never a sunset grade that matches cut 32. No spoiler.
- **C — rejected by the keeper (2026-11-24):** a mourning streamer is not a custom the canon has, and a banner that changes from episode to episode becomes a signal the viewer reads. Not built.
- Not built either (analyst ideas the canon rules out): water higher on the pilings each week (tide-post motif, OP-5) and a per-episode banner order in 19–22 (a changing banner is a signal, same reason as C).

## 8. Cost (hard cap $10 including retakes; no paid call made)

Prices: NB2 /edit $0.08 per image (1K default, 1376×768, §5); Kling 2.5 TP $0.35 per 5 s clip (fal catalog, video test 2026-11-23).

| Item | Count | Takes | Unit $ | $ |
|---|---|---|---|---|
| New frames NB2 (F01, F01a, F04, F10, F11, F14, F15, F17, F18, F19, F21, F23, F26, F27, F28, F30) | 16 | 1 | 0.08 | **1.28** |
| Kling 2.5 TP 5 s (K01, K01a, K03, K04, K05, K07–K18) | 17 | 1 | 0.35 | **5.95** |
| Existing assets: 9 ref plates, 2 animatic frames, 1 video-test clip, map overlays | — | — | 0 | 0.00 |
| ffmpeg: parallax, pushes, particles, ramps, shake, ink, glass steps, wheel and coin rotation, whips, logo, variants, assembly, local paint-outs and upscale | — | — | 0 | 0.00 |
| **Subtotal (first takes)** | | | | **7.23** |
| Retake reserve (studio director 2026-11-24: retakes only from **$1.12** = $9.85 − $8.73; a clip that fails twice uses its §6.1 ffmpeg fallback) | | | | **1.12** |
| **Total planned** | | | | **$8.35** |
| Run ceiling for the whole OP (`BUDGET_LIMIT_USD=64` − $54.15 logged) | | | | $9.85 |
| Untouched margin to the investor's $10 cap | | | | $1.65 |

How v1.2 moves from v1.1 ($7.90):

| Change | Source | $ |
|---|---|---|
| + F15, F17, F23, F30 | keeper | +0.32 |
| + F01a, K01a (hook / wave before impact) | VFX | +0.43 |
| − K06 (wheel hub → ffmpeg ROT) | VFX | −0.35 |
| K16 stays a clip (open-sea source) | keeper over VFX | 0.00 |
| + F26, K18 (footprints) | analyst | +0.43 |
| **v1.2** | | **8.73** |

Run cap (gate R2 §5): `STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=64`; the log before the OP is **$54.15** (fal $43.36, ElevenLabs $10.79; 1512 rows, no OP rows), so the run headroom is **$9.85**, the hard ceiling for the whole OP; the guard stops every call above it. K13 ($0.35) is not in this run: it waits for the keeper's look at the fixed H1/H2 plates and the studio director's go (C2). No other paid run (ElevenLabs or fal) while the OP runs (C3). fal balance: log estimate $100.00 − $43.36 = ≈$56.64, after the plan ≈$48.3, above the $20 floor (C4 waived by the studio director).

## 9. Order of work (after the gate opens)

1. **$0 first: the OP animatic** on `lib_mus_theme-op-drums_v2a.mp3` at 87.0 s, with every LA recipe: even glass steps on cropped H1 → H2 (ripple L-10 standing in for K13), ROT hub, coin top, cloud shadows and rolling light, the inhale (flashes + black), the title wipe and tail; grey cards for the 16 new frames. The analyst re-runs the energy-vs-picture measure on it; if the dips of 0:30–0:45 and 1:09–1:22.5 are not closed here, no clip will close them.
2. **First paid batch, heroes only ($1.56):** F01, F01a, K01, K01a, K13, K15 → acceptance per §6.1.
3. Remaining 14 NB2 frames, 1 take each → acceptance (§5 order); **the keeper checks F15, F17, F18, F23, F26 at full size before acceptance / assembly.**
4. Clips: K05, K04, K11/K12 (heraldry checked against H0x at full size), then K03, K07, K08, K09, K10, K14, K16, K17, K18.
5. Assembly: ffmpeg passes per §4, hit frames per §2.1, logo sting, corner bug; master on drums v2a at 87.0 s with the 1:26.5–1:27.0 picture and audio fade (v2b swaps in with no re-cut); per-episode variants A and B rendered as 12 files.

## 10. Open questions

1. ~~Gatekeeper (flag): glass direction~~ — **closed by the keeper R2.4:** four even full-frame steps, no front, no direction.
2. **Canon keeper:**
   - ~~F26 footprints~~ — closed: R2.2 (many mixed prints, no pair);
   - ~~steam over a glass (13)~~ — closed: R2.3 (no steam);
   - ~~the drop on the logo in 33~~ — closed: R2.1 (letters only);
   - F01a, the wave before impact, uses the same set-up as the signed 01/25;
   - ~~the 74% crop plus finial paint-out~~ — closed: R2.5 (plates prepared in v1.3; keeper checks them before Kling);
   - may Lows images (wheels, pilings) ever sit next to the glass? Until the keeper answers, no.
3. ~~Investor: master length; v2a or v2b~~ — **closed by the studio director:** the OP is 87.0 s (29 bars), master on v2a; v2b has the same grid and swaps in with no re-cut.
4. **Composer:**
   - optional taiko on 0:00.0 under the cello (analyst #2; the picture hook works without it);
   - keep the pre-hit attack 0:56.63 and the short gap before 0:57.0;
   - confirm the whistle attack at 0:20.45.
5. **Lead screenwriter + keeper:** the analyst's "one clue readable only on pause, paid off in S2+" (map 24 or panel 18). Not built; needs the sealed mythology.
6. **Artist:** `HERALDRY/H03_ilvane` shows a left hand. HS-003 needs a right hand. Redraw it; mirroring is not allowed because of the spiral. F18 goes ahead without H03.
7. **Studio director:**
   - pilot fixes found by the keeper: Sc 10 (`sc10-sh030`: heraldry) and Sc 20 (`sc20-sh210`: grooves "\");
   - F18 and F23 also fix pilot Sc 5 and Sc 4, and their $0.16 is booked here;
   - where the Sluice Spire stands on the other plates is for the lead screenwriter.
8. **IT engineer:** the ffmpeg build has no `vidstab`. Use `deshake` or a manual crop shift to align K13 with H2.
