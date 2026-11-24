# HOLLOWSTONE — Season 1 opening (instrumental, 90.0 s) — storyboard v1.1

Version 1.1 · 2026-11-24 · author: director (anime-director) · status: **storyboard only. No paid call made. Review order: VFX director → analyst → canon keeper → gatekeeper; nothing is generated before the gate opens.**
Music: `output/music/lib_mus_theme-op-fullrange_v1.wav` (90.0 s; the pilot uses the `op-pilot` HPF file, same timing). Bars of 3.0 s from 0:00.0; cuts on bar lines or half-bars (1.5 s = 2 beats at 80 BPM).
Binding inputs: investor decisions 2026-11-24 (instrumental OP in every S1 episode; **no characters**; "never skipped": motion in every cut; **hard cap $10 for the whole OP including retakes**, Kling 2.5 TP only), `reports/lore-v4-2026-11-24.md` §1(d), `canon/excerpts/for_director_and_artist.md` §1–§3, §7, `story/episodes/S01E01/v4_dialogue_pass.md` §2–§3.3, `direction/S01E01_finals_checklist.md` G1–G16, `direction/visual_bible.md` §5, §8, §10, `direction/limited_animation.md` (L-codes), `direction/video_test/RESULTS.md`.
v1.0 (character run-through, then world-only at $16) is superseded by this file.

## 0. Кратко (RU)

- **33 склейки** на сетке такта/полутакта, **движение в каждой**. Персонажей нет: город, Низы, колёса, вода, Шпили, гобелен (панели 2 и 5), гербы, карта, предметы, погода. Безымянные крошечные силуэты — только как масштаб.
- **Новых кадров NB2: 10** (1 дубль). **Клипов Kling 2.5 TP: 16** (1 дубль, 5 с), из них нарезается 23 склейки (по 1–3 куска из клипа, со спид-рампами), ещё 1 — из готового клипа видеотеста. Kling 3 Pro не используется. 9 склеек — бесплатно: существующие плиты и кадры аниматика + ffmpeg (параллакс, наезды, частицы, вспышки, тряска, вайпы).
- **Смета: $6.40 + резерв на пересъёмки $1.50 = $7.90** при потолке $10 (запас $2.10 не трогаем). BUDGET_LIMIT_USD=63 при текущих ≈$53 — помещается.
- Крючок в первые 3 с: замедленный взрыв брызг — это та же волна, что бьёт в дамбу на 0:57 (деталь для повторного просмотра). Логотип HOLLOWSTONE — на **последнем ударе 1:22.5** (измерено по файлу): брызги волны стирают кадр и открывают титр.
- Варианты по сериям бесплатно: (A) зарубки-счёт номера серии на полях гроссбуха, (B) грейд финальной плиты под время суток серии. (C) траурная лента после E1 — вопрос хранителю.
- Строже списка v4 §3.3: **свет в пазах Шпиля не используем вообще**, камня/осколка и перстня нет, ворот и засовов нет, вода через дамбу в Низы не переливается.

---

## 1. Rules checked on every cut

| # | Rule | Source |
|---|---|---|
| OP-1 | **No characters.** No named or recognizable person, no face, no portrait, no hands in close-up. Tiny anonymous distant silhouettes only as scale (≤ ~3% of frame height each) | investor 2026-11-24 |
| OP-2 | **No stone, no shard**, no black pebble on a cord, no cracked black stone, no relay stones; **no ring**. Heraldic devices that hold a stone (Ilvane hand) or a ring (Quell eel) appear only small and woven inside tapestry panel 2 or cropped out of frame; never as a close-up, never in neighbouring cuts | SEC-027, S-13, excerpt §1 |
| OP-3 | **Nothing glows.** No light in Spire grooves (stricter than v4 §3.3), no glowing water, cracks, veins, lightning. Lanterns are small practical flames, no bloom halo. Flashes in the edit are short exposure pops or dark ink-frames, never a light source in the picture | G3, G4, G15; studio rule |
| OP-4 | **Spires:** smooth glassy black, ring of open arches at the crown, deep spiral grooves, near side "/" (lower-left to upper-right), dark foot in water. Check at full size on every Spire frame and on every 10th frame of a Spire clip | G5, excerpt §3 |
| OP-5 | **No spoilers for any S1 episode:** no water over the dike into the Lows, no flooded houses or ruin, no night flood (E10); no gate, no bar across a gate, nothing from the Sc 1/Sc 18 gate (PL-0021); no tide-post (PL-0022, from S1E3); no cracked or damaged Spire; no IX wash, no Ninth tier reading, no signature line or seal on the map; no *Chronicle of the Dry Years* book or page; no rings on water (the stone's motif); nothing from the back-canal sill where the shard is found (sc03-sh060/070) | v4 §3.3, keeper §7 |
| OP-6 | **Tapestry panels 1, 2, 5 only** (this board: 2 and 5). Never 3, 4, 6. Fabric fills the frame | keeper §7, G13 |
| OP-7 | **Heraldry:** tall vertical banner, slanted cut at the bottom, long point at the pole (DEC-66); fields and devices per `refs/HERALDRY/H0x` and G11; no shields; seals round | G11, DEC-66 |
| OP-8 | Spirals turn **sunwise** (clockwise from the centre outward as the camera sees it); pass `refs/HERALDRY/H16_ashare_reference_spiral.png` when a spiral must read | excerpt §3 |
| OP-9 | **Compass:** sea and harbour west, the sun sets over the sea; the hill (Steps, Crown Spire) east; the Lows in the dike's shadow, never in high direct sun | DEC-65 |
| OP-10 | No text in generated frames. Only on-screen text: the HOLLOWSTONE logo and the small corner bug ANIME-STYLE · AI-ANIMATED (from the OP on). Lower 15% free of key detail | visual bible §5, v4 §2 |
| OP-11 | **No hflip** of any frame or clip (also not for whips or match cuts) | visual bible §11.2 |
| OP-12 | Video: Kling 2.5 TP only. Each motion prompt lists what must not change; "no new light sources, lighting unchanged, no glowing marks" in every prompt | RESULTS.md, investor |

## 2. Music map (measured on the file, 2026-11-24)

Measured with band energy per bar and a 0.1 s RMS envelope (ffmpeg + numpy, $0). The take's form differs from the plan table in `main_theme.md` §4: full energy runs to the last hit.

| Section | OP time | Bars | Heard | Picture job |
|---|---|---|---|---|
| S1 Intro | 0:00.0–0:12.0 | 1–4 | solo cello, no drums | hook image in 3 s, then the world wakes at dawn |
| S2 Groove | 0:12.0–0:21.0 | 5–7 | stamps on beats 1 and 3, claps, barrel; whistle ≈0:20.25 | the Lows at work, cuts on the beat |
| S3 Theme | 0:21.0–0:45.0 | 8–15 | strings carry the melody | the city climbs, Lows → Mids → Steps, morning → afternoon |
| S4 Rise | 0:45.0–0:57.0 | 16–19 | brass calls, snare build | houses: tapestry, banners, the map; cuts shorten to 1.5 s |
| S5 Hook | **0:57.0**–1:09.0 | 20–23 | octave leap on 0:57.0 (cymbal, high band +7 dB), full drums | payoff: the sea hits the wall, action burst of water |
| S6 Answer | 1:09.0–1:21.0 | 24–27 | full energy, cadence | climax: the storm breaks, the harbour turns to glass |
| S7 Last hit + tail | 1:21.0–1:30.0 | 28–30 | hits every 1.5 s, **last hit 1:22.5**, decay to silence by 1:29 | title sting on the last hit, held on the decay, fade 0.4 s |

Drum hits used for shake/pops: every 1.5 s from 0:12.0 (beats 1 and 3). Big hits: 0:57.0, 1:09.0, 1:22.5.

## 3. Free VFX toolkit (ffmpeg passes; code names used in §4)

| Code | Pass | How (ffmpeg) | Rule |
|---|---|---|---|
| **PX** | multi-plane parallax from one still | 2–3 layers cut from the plate by soft masks (sky / far / near), each scaled and moved at its own speed (`overlay` + `crop` with t-expressions), L-04 | never reveal a hole: plate margin ≥ 1.25× |
| **PUSH / PULL / TILT / PAN** | camera moves on stills or on top of a clip | `zoompan`/`crop` with eased expressions (L-01…L-03) | ≤ 15% scale per 3 s, except whip and rush |
| **RAMP** | speed ramp | `setpts` piecewise (e.g. 0.35× → 1× → 2×), `tblend`/`framestep` blend for the fast part | slow parts only from clean Kling motion; no `minterpolate` warping |
| **RAIN** | rain layer | L-06 (`la_fx/rain_field.png` scrolled + `gblur` streaks), 2 depths | grey-white streaks, never bright |
| **SPRAY** | spray / droplet particles | noise field → threshold → `gblur` → `overlay` screen at 35–60%, moving up and out from the impact point; reuse the luma of clip K01 as a matte | white-grey water, not light |
| **MIST / DUST** | mist drift, dust in beams | L-08, L-07; light shafts = soft diagonal gradient multiplied in at 10–20% (motivated by a window or a cloud gap) | shafts only where the source is in frame |
| **SPARK** | lantern sparks | 4–8 tiny warm dots rising from a flame over 1 s, fading, L-09 flicker on the flame | small, short, no halo |
| **SHAKE** | camera shake on drum hits | L-05, 3–6 frames decaying, 6–12 px; big hits 20 px | not on the title letters after they settle |
| **POP** | exposure pop on a stamp | `eq=brightness=+0.06` for 2 frames | never a white-out |
| **INK** | impact ink-frame | 2 frames: `negate` + posterize to blue-black and linen (`lutyuv`) | only on big hits (0:57.0, 1:09.0, 1:22.5) |
| **WHIP** | whip transition | directional blur ramp 4 frames out + 4 frames in (`gblur` with `sigmaV` or `boxblur` along the move), cut on the beat | max 4 in the OP |
| **MATCH** | match cut / match dissolve | shape or motion continuity (circle → circle, swing → swing), dissolve 6–12 frames only in the climax | — |
| **GRADE** | per-episode LUT | `lut3d` dawn / dusk / night variants for the title plate | variant B, §6 |

## 4. Shot table

Class: **K** = cut taken from a Kling 2.5 TP 5 s clip (clip id K01…K16); **EXK** = existing Kling clip ($0); **LA** = ffmpeg only on a still. Source: **NEW** = NB2 frame (§5), **EX** = existing file.

| # | In – Out | Sec | Music | Content and camera | Class / clip piece | Frame source | VFX passes |
|---|---|---|---|---|---|---|---|
| 01 | 0:00.0–0:03.0 | 3.0 | S1 b1 | **HOOK:** out of black, a wall of sea spray bursts upward in slow motion across the frame, droplets hanging; we don't yet see what it hit | K01 piece 2.0–3.0 s at RAMP 0.35× | NEW F01 (wave) | RAMP, SPRAY (slow, large drops), MIST; open from black in 4 frames |
| 02 | 0:03.0–0:06.0 | 3.0 | S1 b2 | Highwater at dawn: tilt DOWN from the crown arches of the Crown Spire to the misty Lows below the dike; three planes slide apart | LA | EX `refs/PL-0004/D01_A_dawn-ebb_v1.png` (paint out the crack lines on the left Spire locally, OP-5) | TILT, PX (sky / Spires+hill / Lows), MIST |
| 03 | 0:06.0–0:09.0 | 3.0 | S1 b3 | The Ninth's lane at dawn: mist drifts, puddles shiver, the rope bridge sways | EXK piece 0.5–3.5 s | EX `output/video_test/alley__kling-2.5-turbo-pro.mp4` | MIST second layer, slow PUSH 4% |
| 04 | 0:09.0–0:12.0 | 3.0 | S1 b4 (phrase hangs) | ECU: a tarred net hung to dry, drops gather and fall from the knots; behind, a rope with **nine** small unlit lanterns sways | K03 piece 0.0–3.0 s | NEW F04 (net) | PULL 3% (focus feel), RACK-like blur ramp; last drop falls on 0:11.25 |
| 05 | 0:12.0–0:13.5 | 1.5 | S2 b5 (first stamp) | The hub of a giant treadwheel lurches into motion, spokes start to turn | K06 piece 1.0–2.5 s | EX animatic `sc06-sh010_a.png` | SHAKE on 0:12.0, POP |
| 06 | 0:13.5–0:15.0 | 1.5 | S2 b5 beat 3 | Inside the drum's rim: slats rush past the lens | K04 piece 0.5–2.0 s | EX `refs/PL-0008W/D05_W2_morning_v1.png` | SHAKE on 0:13.5, motion-blur streaks |
| 07 | 0:15.0–0:18.0 | 3.0 | S2 b6 | The three great treadwheels in a row turning; tiny anonymous walkers inside; push in | K05 piece 0.0–3.0 s | EX `refs/PL-0008W/D05_W1_morning_v1.png` | PUSH 6%, SHAKE on 0:15.0 and 0:16.5, MIST |
| 08 | 0:18.0–0:19.5 | 1.5 | S2 b7 | Punch-in: the nine lanterns swing on their rope in the gust | K03 piece 2.5–4.0 s (crop 60%, local upscale) | NEW F04 | SPARK (one lantern, tiny, as if a wick is being trimmed — no flame grows), SHAKE |
| 09 | 0:19.5–0:21.0 | 1.5 | S2 b7 beat 3 (whistle) | Wheel shed → **WHIP UP** into the morning sky, blur peaks on the whistle, cut on 0:21.0 | K05 piece 4.0–4.75 s + WHIP | EX (K05) | WHIP (up), POP on the whistle |
| 10 | 0:21.0–0:24.0 | 3.0 | S3 b8 (theme enters) | Flyover: the camera glides forward over the stilt-town — lanes of water, plank bridges, washing lines — toward the dike and the hill with three Spires | K07 piece 0.5–3.5 s | NEW F10 (aerial) | PX on the sky band, MIST |
| 11 | 0:24.0–0:27.0 | 3.0 | S3 b9 | Under a plank bridge: the tide climbs the tarred pilings past painted white tide marks | K08 piece 1.0–4.0 s | NEW F11 (pilings) | caustic shimmer on the bridge underside (L-15, soft), slow PUSH |
| 12 | 0:27.0–0:30.0 | 3.0 | S3 b10 (Mids) | A small bronze bell in its niche swings and strikes; dust shakes down through a window beam | K09 piece 0.5–3.5 s | EX animatic `sc16-sh040_a.png` | DUST in the beam, shafts from the window, POP on the strike |
| 13 | 0:30.0–0:33.0 | 3.0 | S3 b11 | The counting hall: rows of empty desks with open ledgers, light falling through tall windows; dolly down the aisle | LA | EX `refs/PL-0011/D11_L1_late-aft_v1.png` (check the far end: no figure) | PUSH 10% along the aisle, PX (window wall vs desks), DUST, shafts moving 2% |
| 14 | 0:33.0–0:36.0 | 3.0 | S3 b12 | Top-down: a tower of copper coins tips and slides across the felt beside an open ledger; one coin spins | K10 piece 0.5–3.5 s | NEW F14 (coins) | slow rotate-PUSH 3°; **variant A** tally marks (§6) |
| 15 | 0:36.0–0:39.0 | 3.0 | S3 b13 (Steps) | The city on its granite hill seen from the harbour: terraces, palace, ships, three Spires; lateral move | LA | EX `refs/PL-0004/D01_C_late-aft_v1.png` (OP-9 check: light must read from the west/camera side; else swap to `D01_A_late-aft_v1.png`) | PX (water / ships / hill / sky), PAN right, slow cloud drift on the sky layer |
| 16 | 0:39.0–0:42.0 | 3.0 | S3 b14 | Low angle on the Crown Spire: tilt UP the grooves to the ring of arches; clouds stream past the crown | LA | EX `refs/PL-0014/D08_S1_late-aft_v1.png` (G5 full-size check) | TILT, PX (tower vs sky), cloud layer drift, MIST at the foot |
| 17 | 0:42.0–0:45.0 | 3.0 | S3 b15 | The palace wall with the row of house banners, the city and the sea far below; slow pan along the banners | LA | EX animatic `sc10-sh030_a.png`, **crop starts right of the first (open-hand) banner** (OP-2) | PAN, PX (wall+banners vs city), banner sway faked by 1–2 px per-banner sine displacement (`displace` with a vertical gradient) |
| 18 | 0:45.0–0:48.0 | 3.0 | S4 b16 (brass) | Tapestry panel 2: nine woven banners on the shore, nine small figures facing the black tower | LA | NEW F18 (panel 2 re-weave; also fixes pilot sc05-sh020/070) | PAN left→right, lint/dust in raking light, fabric micro-ripple (`displace`, 2 px) |
| 19 | 0:48.0–0:49.5 | 1.5 | S4 b17 | Banner CORVANE snaps in the wind | K11 piece (left half) 0.5–2.0 s | NEW F19 (banners A) | SHAKE light, POP |
| 20 | 0:49.5–0:51.0 | 1.5 | S4 b17 beat 3 | Banner DASK | K11 piece (right half) 2.5–4.0 s | NEW F19 | MATCH (fold-to-fold), POP |
| 21 | 0:51.0–0:52.5 | 1.5 | S4 b18 | Banner LANTRY | K12 piece (left half) 0.5–2.0 s | NEW F21 (banners B) | POP |
| 22 | 0:52.5–0:54.0 | 1.5 | S4 b18 beat 3 | Banner FENNICK | K12 piece (right half) 2.5–4.0 s | NEW F21 | POP |
| 23 | 0:54.0–0:55.5 | 1.5 | S4 b19 (snare) | Tapestry panel 5: the cormorant sail across the harbour mouth, ships at sea | LA | EX `refs/TAPESTRY/E06_panel5_v1.png` | fast PUSH 12%, fabric ripple, snare-roll micro-SHAKE |
| 24 | 0:55.5–0:57.0 | 1.5 | S4 b19 beat 3 (roll) | The Tithe Map top-down with its three tier tints; accelerating push **toward the hill (east)** → whip into the hook | LA | EX `refs/M-MAP/E05_map_base_v1.png` + the three tint overlays of Sc 7 (no IX wash, no legend row 4, no signature line; never pushes toward the Ninth, south-west) | PUSH ease-in 0→25%, WHIP out on 0:56.75 |
| 25 | **0:57.0**–1:00.0 | 3.0 | S5 b20 — **octave leap** | **PAYOFF:** a storm wave smashes into the outer face of the great sea dike, spray towers over the crest and falls back to the sea. The impact frame lands on 0:57.0 | K01 piece 1.2–4.2 s at 1× (impact frame on the downbeat) | NEW F01 | INK on 0:57.0, SHAKE 20 px decaying 1 s, SPRAY overlay (extra), RAIN |
| 26 | 1:00.0–1:01.5 | 1.5 | S5 b21 | The harbour in chop: ships pitch, masts sway | K13 piece 0.0–1.5 s | EX `refs/PL-0018/D09_H1_late-aft_v1.png` | RAIN, SHAKE on 1:00.0 |
| 27 | 1:01.5–1:03.0 | 1.5 | S5 b21 beat 3 | A stone weir: the sea roars over the lip into a sluice channel | K14 piece 1.0–2.5 s | NEW F27 (weir) | SPRAY, MIST, POP |
| 28 | 1:03.0–1:04.5 | 1.5 | S5 b22 | Low rush along a canal between stilt-houses in the squall, pilings flicking past | K15 piece 0.5–3.5 s at RAMP 2× | NEW F28 (canal) | RAMP, RAIN (fast angle), WHIP in |
| 29 | 1:04.5–1:06.0 | 1.5 | S5 b22 beat 3 | The treadwheel rim at full speed (rhyme with cut 06) | K04 piece 2.0–5.0 s at RAMP 2× | EX (K04) | MATCH to cut 28's direction, SHAKE |
| 30 | 1:06.0–1:09.0 | 3.0 | S5 b23 | Rain-lashed rooftops; the camera tilts up until the three Spires stand dark against the storm | K16 piece 0.5–3.5 s | EX animatic `sc20-sh210_a.png` (re-graded to storm grey; paint out the moon locally) | RAIN 2 depths, TILT assist, cloud gap opening = soft light shaft from the top (motivated by the cloud gap) |
| 31 | 1:09.0–1:16.5 | 7.5 | S6 b24–26 | **CLIMAX part 1:** the harbour at last light — the chop dies down, the masts slow and stop | K13 piece 0.0–5.0 s at RAMP 1× → 0.6× (frame blend) | EX `refs/PL-0018/D09_H1_late-aft_v1.png` | INK on 1:09.0 (storm → evening), RAIN fading out over 1.5 s, slow PUSH 5% |
| 32 | 1:16.5–1:22.5 | 6.0 | S6 b26 beat 3 – b28 beat 2 | **CLIMAX part 2:** match-dissolve (12 frames) to the harbour perfectly still like glass, exact mirror reflections of hulls and masts, sun on the horizon | LA | EX `refs/PL-0018/D09_H2_glass_v1.png` | MATCH dissolve, slow PUSH 4% toward the sun, the only motion = a drifting high-cloud layer (PX); nothing is added to the water |
| 33 | **1:22.5**–1:30.0 | 7.5 | S7 last hit + tail | **TITLE STING:** on the last hit a wall of spray (the K01 wave, reversed direction) wipes across frame and leaves HOLLOWSTONE over the Crown Spire at dusk; clouds stream past the crown, the plate pushes 3%; fade to black 1:29.6–1:30.0 | K17 piece 0.0–5.0 s + hold; spray wipe from K01 luma | EX `refs/PL-0014/D08_S1_dusk_v1.png` (G5 check); logo graphic | INK on 1:22.5, SPRAY wipe (matte from K01), SHAKE 6 frames then still, letters settle 8 frames; **variant B** grade |

**33 cuts** (the climax is two cuts: 31 and 32). ASL 2.7 s. Every cut moves: 24 cuts carry generated motion (23 from the 16 paid clips, cut 03 from the existing clip), 9 carry ffmpeg motion (parallax, push/tilt, particles, fabric displacement).
Adjacency checks done: no stone or ring device in any frame (cut 17 crop starts after the open-hand banner; Quell appears only woven in cut 18); no gate or bar; tapestry cuts (18, 23) not adjacent to a Spire-crown image; the map (24) never shows the Ninth.

Clip K17 (title plate) is the 16th paid clip; clip ids K02 = the existing video-test clip. Paid list: K01, K03–K17 = **16 clips**.

## 5. NB2 frames (10 new, 1 take each)

All: `fal-ai/nano-banana-2/edit`, 16:9, largest output size, refs as listed. Each prompt = text below + `{STYLE_BASE}` + `{AVOID_OP}`.

`{STYLE_BASE}` = visual bible §10.1 verbatim:
`2D anime-style TV series still, original character and world design, clean cel-shaded characters with crisp thin dark blue-black ink outlines of slightly varying weight, flat color fills with two shadow tones, cool violet-blue shadows, restrained highlights only on eyes, hair, metal and wet surfaces, detailed painterly matte-painting background with atmospheric haze, wet reflective stone and water, motivated cinematic lighting, muted desaturated palette with deep teal-black shadows, subtle film grain, grounded epic fantasy, 16:9 widescreen composition`

`{AVOID_OP}` =
`One single full-frame image: no inset, no letterbox bars, no frames or boxes drawn on top. No people and no faces (unless tiny distant silhouettes are allowed below). Avoid: photorealism, 3D look, chibi style, neon colors, any text, letters, numbers or labels, watermark, logo, multiple panels, split screen, glowing objects, glowing lines or cracks, light inside tower grooves, magic sparkles, lightning, mirrored image, shields, gates or bars across gates, stones or pebbles on cords, rings.`

`{SPIRE}` = `the towers are smooth glassy black stone cones, each crowned by a ring of open arches, with deep spiral grooves winding up the whole height; on the near side of each tower the grooves rise from lower-left to upper-right ( / ); the grooves are dark, nothing lights up; the foot of each tower is dark stone standing in water`

| Frame | Used in | Refs | Prompt (before STYLE_BASE + AVOID_OP) |
|---|---|---|---|
| **F01** wave | 01, 25, 33 (wipe) | `PL-0004/D01_A_dawn-ebb_v1.png` (dike design) | `Wide low shot from the sea side of a colossal brick sea dike under a grey storm sky in daylight: a huge dark green-grey wave is just striking the dike's sloping outer face, a wall of white spray starting to rise; the top edge of the dike stays dry, no water pours over it. Wind-torn clouds, flying foam, cold grey light, rain. No people, no buildings breaking.` |
| **F04** net + lanterns | 04, 08 | `PL-0008/D02_C1_dawn-ebb_v1.png` | `Extreme close-up of a heavy tarred fishing net hung to dry on a wooden pole in a stilt-town lane at dawn, the knotted mesh fills the left two thirds of the frame, clear water drops gathering on the knots, one drop about to fall. On the right, softly out of focus, a sagging rope strung between two stilt-houses with exactly nine small unlit tin lanterns hanging from it. Cold grey-teal dawn light from above, no direct sun, thin mist.` |
| **F10** aerial | 10 | `PL-0004/D01_A_dawn-ebb_v1.png`, `PL-0008/D02_C1_dawn-ebb_v1.png` | `High aerial view looking forward over a vast stilt-town below sea level in the morning: a maze of narrow water lanes, plank bridges and tarred roofs, washing lines, small boats tied to pilings; in the middle distance a towering brick sea dike, beyond it a granite hill with terraces and a palace and three tall black towers, the middle one the tallest. {SPIRE}. Cool grey light in the town, sun only on the hill and the tower tops. Tiny distant specks of people on far bridges allowed, none larger than a dot.` |
| **F11** pilings | 11 | `PL-0008/D02_C3_dusk_v1.png` | `Low shot at water level under a plank bridge between stilt-houses: tarred wooden pilings rising out of dark water, each piling marked with painted white horizontal tide lines; the water stands just below the lowest line, small eddies around the posts. Diffuse cool afternoon light, soft ripple reflections on the underside of the bridge. No people.` |
| **F14** coins | 14 | `M-LEDGER/E12_ledger_page-a_v1.png` (paper and ink style) | `Top-down view of an open clerk's ledger on worn green felt, ruled columns of tiny illegible ink scribbles, a wide empty margin on the left page, a brass inkwell and a quill at the top edge, a tall leaning tower of rough copper coins standing on the felt beside the ledger. Flat cool light from a tall window, dust motes. No hands, no readable text or numbers.` |
| **F18** panel 2 re-weave | 18 (+ pilot sc05-sh020/070) | `TAPESTRY/E06_panel2_v1.png`, `TAPESTRY/E06_panel1_v1.png`, `HERALDRY/H01…H07`, `GROUPS/C06_emblem_strip_ref.png`, `HERALDRY/H16_ashare_reference_spiral.png` | `CHRONICLE` module **instead of** STYLE_BASE (negative "anime character, cel shading, 3D"): `Re-weave this tapestry panel keeping its weave, palette and border: nine tall woven banners on a shore, each vertical with a slanted cut at the bottom and the long point at the pole; six banners in the centre, two at the left edge and one at the right edge; nine small woven figures under them with one hand raised, all facing a black tower rising from the woven sea; no weapons, no spears; the open-hand banner shows a RIGHT hand palm forward, thumb on the viewer's right, holding a small grey spiral stone; the cormorant banner shows a black cormorant diving beak-down into a silver wave. Border spirals turn clockwise from the centre outward. Fabric fills the whole frame.` Banner order and fields per keeper §2 and G11 — keeper checks before use |
| **F19** banners A | 19, 20 | `HERALDRY/H01_corvane.png`, `HERALDRY/H02_dusk.png`, `PL-0004/D01_C_late-aft_v1.png` (light) | `Two tall silk banners side by side, each filling one half of the frame, hanging from poles on a granite terrace and snapping in a strong wind; each banner is vertical with a slanted cut at the bottom and the long point at the pole side. Left banner: deep blue field, a black cormorant diving beak-down into a silver wave with exactly three crests. Right banner: ochre field, a bronze sickle with its handle above three dark furrows. Emblems exactly as in the references. Low golden afternoon sun from the left, pale open sky behind, crisp shadows in the folds.` |
| **F21** banners B | 21, 22 | `HERALDRY/H07_lantry.png`, `HERALDRY/H06_fennike.png`, same light ref | same wording; `Left banner: black field, a polished rose-copper balance with a level beam, the left pan holding water, the right pan empty. Right banner: acid sulphur-yellow field, a grey hare sitting in profile facing left, both ears up and apart.` |
| **F27** weir | 27 | `PL-0008W/D05_W1_morning_v1.png` (materials) | `Low angle at the lip of a wide stone weir in a storm: grey-green sea water roars over the smooth stone edge in a thick curved sheet and crashes into a deep brick sluice channel below, white foam and mist, rain. Wet black brick, cold storm light. No gate leaves, no beams or bars across the channel. No people.` |
| **F28** canal | 28 | `PL-0008/D02_C3_dusk_v1.png`, `PL-0008/D02_C1_dawn-ebb_v1.png` | `Point of view just above the water, looking straight down a long narrow canal between two rows of stilt-houses in a squall: tarred pilings on both sides, low plank bridges crossing ahead, ropes and hanging nets, wind-driven rain, dark choppy water, strong one-point perspective toward a strip of grey sky at the far end. No people, no boats in the path.` |

Acceptance order for every frame and clip: people/faces (OP-1) → stone/ring (OP-2) → glow (OP-3) → grooves "/" and dark foot (OP-4) → gate/bar/water over the dike (OP-5) → text (OP-10) → heraldry per H0x (OP-7).

## 6. Kling 2.5 TP motion prompts (16 paid clips, 5 s, 1 take)

Prefix for all: `Subtle 2D anime animation, the colors and line art stay exactly as in the source image, stable outlines, no morphing, consistent lighting, no new light sources, no glowing marks.`
Negative for all: `morphing, flickering line art, warping background, people appearing, faces, hands, glowing objects, light inside the tower grooves, lightning, sudden cuts, text`.

| Clip | Source | Camera + motion | MUST NOT CHANGE | Cuts |
|---|---|---|---|---|
| K01 | F01 | `Static camera, low. The wave crashes against the dike; a huge wall of spray explodes upward above the crest, hangs, and falls back toward the sea; foam slides down the face.` | the dike stays intact; no water flows over the crest into the town; daylight storm, not night; no people | 01, 25, 33 (matte) |
| K03 | F04 | `Static camera. Water drops gather on the net knots and fall one by one; a gust makes the rope of lanterns swing.` | lanterns stay unlit and count nine; light; net shape | 04, 08 |
| K04 | `D05_W2_morning` | `Static camera. The giant wooden drum turns steadily, its slats moving past from top to bottom; water drips from the slats.` | drum geometry; light; no figures appear | 06, 29 |
| K05 | `D05_W1_morning` | `Very slow push-in. All three treadwheels turn steadily at the same speed; tiny distant figures inside walk in place.` | wheel count (3) and design; figures stay tiny and anonymous; light | 07, 09 |
| K06 | animatic `sc06-sh010` | `Static camera. The great wheel hub starts to turn from rest, slowly at first, then steadily; water drips from the spokes.` | hub and spoke design; the shed; light; no people | 05 |
| K07 | F10 | `The camera glides slowly forward and slightly down over the town toward the dike and the hill; smoke drifts from chimneys.` | towers keep shape, height order and groove direction; nothing lights up; no new buildings; no people larger than dots | 10 |
| K08 | F11 | `Very slow push-in toward the pilings. The water level rises steadily by about one tide line, small eddies swirl around the posts, ripple reflections shimmer under the bridge.` | painted lines stay fixed on the pilings; the water never reaches the bridge; light; no people | 11 |
| K09 | animatic `sc16-sh040` | `Static camera. The bell swings once and strikes, its rope sways; a little dust falls through the window light.` | bell, niche and door design; window light unchanged; no people | 12 |
| K10 | F14 | `Static camera, top-down. The tower of copper coins tips over; coins slide and roll across the felt; one coin spins and settles.` | ledger and scribbles stay still and illegible; no hands; no text; coins stay copper | 14 |
| K11 | F19 | `Static camera. Both banners snap and ripple hard in a strong wind from the left; the poles stay still.` | both emblems and colours exactly as in the source; banner shape (slanted cut, long point at the pole); light | 19, 20 |
| K12 | F21 | same as K11 | same as K11 | 21, 22 |
| K13 | `D09_H1_late-aft` | `Static camera. At first choppy waves roll across the harbour and the ships pitch; then the waves die down little by little until the water is almost still and the masts stop moving.` | ship count and positions; sun position and colour; no people on decks; nothing glows | 26, 31 |
| K14 | F27 | `Static camera. Water pours over the weir lip in a thick sheet and crashes into the channel; foam and mist billow; rain.` | weir and channel shape; no gate or bars appear; light | 27 |
| K15 | F28 | `The camera moves fast straight forward low over the water along the canal, passing under one plank bridge; pilings flick past on both sides; rain.` | canal stays empty (no boats, no people); house design; light | 28 |
| K16 | animatic `sc20-sh210` (moon painted out, storm grade) | `The camera tilts slowly up from the rooftops to the dark towers on the skyline; heavy rain falls; clouds move fast.` | towers: shape, order, groove direction "/", grooves stay dark; no lightning; no lit windows added; no people | 30 |
| K17 | `D08_S1_dusk` | `Very slow push-in. Clouds stream past the crown of the tower from left to right; the sky darkens very slightly.` | the tower's shape and groove direction "/"; grooves dark; the foot dark; no birds or lights added | 33 |

If a clip fails its first take: the cut falls back to the LA version of the same source (still + PUSH/PX + RAIN/SPRAY/MIST), and only the hero clips K01 and K13 may use the retake reserve first.

## 7. Rewatch value

**Hidden details (3rd–5th viewing):**
1. **The wave loop.** The slow spray of the first 3 s (cut 01) is the same wave that hits the dike on the octave leap (cut 25), and its spray wipes in the title (cut 33). Three appearances, one wave.
2. **Nine.** Nine lanterns on the rope (04/08), nine banners in panel 2 (18), three Spires × three planes in cut 02. Counting fans will find the nine without anything being said.
3. **Two wheels.** The rim at 0:13.5 turns slowly, the same rim at 1:04.5 races (cuts 06 → 29): the Lows' work speeds up as the sea rises.
4. **Coin → hub rhyme.** The spinning coin (14) and the turning wheel hub (05) share a circle at the same screen position: money and labour drawn as one shape (MATCH framing note for the editor).
5. **Sunwise.** Every spiral in the OP (tapestry border, map rose) turns clockwise from the centre; the canon fans who learn the rule later will check it here.

**Per-episode variants (free, ffmpeg only, no new generation):**
- **A — the tally.** In cut 14 the left margin of the ledger carries hand-drawn tally strokes equal to the episode number (E1: one stroke … E12: two groups of five and two). Overlay drawn once as 12 PNG strokes ($0). No letters, no numbers. No spoiler.
- **B — the hour.** The title plate (cut 33) is graded to the time of day in which that episode's cold open ends (dawn / day / dusk / night LUT). Chosen by the editor per episode. No spoiler.
- **C — proposal to the keeper, not built:** from E2 on, a thin black mourning streamer under the banners of cut 17 (the Helm's death is shown in E1, the 30 days run to the Still Days). Only if the keeper confirms it reveals nothing beyond E1.

## 8. Cost (hard cap $10 including retakes; no paid call made)

Prices: NB2 /edit $0.08 per image; Kling 2.5 TP $0.35 per 5 s clip (fal catalog, video test 2026-11-23).

| Item | Count | Takes | Unit $ | $ |
|---|---|---|---|---|
| New frames NB2 (F01, F04, F10, F11, F14, F18, F19, F21, F27, F28) | 10 | 1 | 0.08 | **0.80** |
| Kling 2.5 TP 5 s (K01, K03–K17) | 16 | 1 | 0.35 | **5.60** |
| Existing assets: 11 ref plates, 4 animatic frames, 1 video-test clip, map overlays | — | — | 0 | 0.00 |
| ffmpeg: parallax, pushes, particles, ramps, shake, ink, whips, logo, variants, assembly, local upscale | — | — | 0 | 0.00 |
| **Subtotal (first takes)** | | | | **6.40** |
| Retake reserve (e.g. 4 clip retakes $1.40 + 1 frame $0.08) | | | | **1.50** |
| **Total planned** | | | | **$7.90** |
| Untouched margin to the $10 cap | | | | $2.10 |

Run cap: BUDGET_LIMIT_USD=63 with ≈$53 already spent leaves ≈$10, so the full plan including the reserve fits; the scripts stop at $63 in any case.

## 9. Order of work (after the gate opens)

1. **$0 first:** build the OP animatic now from existing plates/clips + grey cards for the 10 new frames, with all ffmpeg passes, on the music. VFX director, analyst, keeper and gatekeeper review timing and content on this cut.
2. 10 NB2 frames, 1 take each → acceptance (§5 order).
3. Kling clips: hero first (K01 wave, K13 harbour), then K05/K06/K04 wheels, then the rest.
4. Assembly: ffmpeg passes per §4, logo sting, corner bug; pilot version on `op-pilot` (HPF), S1 master on `op-fullrange`; per-episode variants A and B rendered as 12 files.
5. After the composer's drum re-work: re-measure 0:57.0 and 1:22.5 (bars do not move; only the sting may shift by one beat).

## 10. Open questions

1. **Canon keeper:** sign the world-only list: panels 2 and 5; no groove light at all; storm wave on the **outer** dike face in daylight (not the E10 flood); tide rising on pilings (cut 11) stays below the bridge; banner close-ups Corvane, Dask, Lantry, Fennick; the open-hand (stone) banner cropped out of cut 17; variant C (mourning streamer from E2).
2. **VFX director:** the particle, spray-matte and parallax passes (§3) — choose the overlay assets and the shake/pop curves; confirm the title sting wipe.
3. **Composer:** the last hit is at 1:22.5 in the current file (plan table §4 of `main_theme.md` says 1:18.0); keep it there in the re-drummed version.
4. **Artist / marketing:** final HOLLOWSTONE logo lettering (the animatic title card sc05-sh100 is the placeholder).
5. **Studio director:** the panel-2 re-weave (F18) also fixes pilot sc05-sh020/070; its $0.08 is booked here.
