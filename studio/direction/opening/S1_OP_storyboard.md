# HOLLOWSTONE — Season 1 opening (instrumental, 90.0 s) — storyboard v1.0

Version 1.0 · 2026-11-24 · author: director (anime-director) · status: **for the gatekeeper and the canon keeper. No paid call has been made. Nothing is generated until the gate is open.**
Music: `output/music/lib_mus_theme-op-fullrange_v1.wav` (90.0 s; pilot uses the `op-pilot` HPF version, same timing). Bars of 3.0 s from 0:00.0; cuts sit on bar lines or half-bars (1.5 s = two beats).
Binding sources: investor decision of 2026-11-24 (instrumental OP in every S1 episode; **no characters**, coordinator message 2026-11-24), `studio/reports/lore-v4-2026-11-24.md` §1(d), `canon/excerpts/for_director_and_artist.md` §2, §3, §7, `story/episodes/S01E01/v4_dialogue_pass.md` §2–§3.3, `direction/S01E01_finals_checklist.md` G1–G16, `direction/visual_bible.md` §10, `direction/video_test/RESULTS.md`.

## 0. Кратко (RU)

- **32 склейки**, все на сетке такта (3,0 с) или полутакта (1,5 с). Персонажей нет: только мир — город, Низы, колёса, вода, Шпили, гобелен (панели 2 и 5), гербы, карта, предметы, погода. Крошечные безымянные силуэты — только как масштаб (в колёсах, далеко на мостках).
- **Новых кадров NB2: 17** (+ 0 для LA), **клипов Kling: 21** (16 × 2.5 TP по 5 с, 4 × 3 Pro по 5 с, 1 × 3 Pro 10 с). Остальное — существующие плиты из `refs/` и один готовый клип из видеотеста, $0.
- **Смета ожидаемая: $16.16** (картинки ×2, движение ×1,5). Потолок поручения $20, запас $3.84.
- Логотип HOLLOWSTONE — на **последнем ударе 1:22.5** (фактический аудиоанализ: последний удар — 3-я доля 28-го такта; спад до тишины к 1:30). Переклад нового барабанщика такты не меняет — после него перепроверить одну метку 1:22.5 (§6).
- Отличия от списка v4 §3.3 (строже): **свет в пазах Шпиля не используем вообще** (правило директора «no glow»), камень/осколок не показываем ни разу, никаких ворот и засовов, наводнение не переливается в Низы (волны бьют только по внешней стороне дамбы).

---

## 1. Rules for this OP (checked on every cut)

| # | Rule | Source |
|---|---|---|
| OP-1 | **No characters.** No named or recognizable person, no face, no portrait, no hands in close-up. Anonymous tiny distant silhouettes allowed only as scale (walkers inside the treadwheels, specks on far plank-walks); never more than ~3% of frame height each | investor, 2026-11-24 |
| OP-2 | **No stone, no shard**, no black pebble on a cord, no cracked black stone anywhere (props, nets, silt close-ups). The **ring** never appears either. Heraldic devices that contain a ring (Quell eel) or a stone (Ilvane hand) appear **only woven, small, inside tapestry panel 2**, never as a close-up, never in neighbouring cuts | SEC-027, S-13, excerpt §1 |
| OP-3 | **Nothing glows.** No light in Spire grooves (stricter than v4 §3.3, by the studio rule for this OP), no glowing water, cracks, veins, sparks, lightning on walls. Lanterns are ordinary practical flames: small, no bloom halo, no light change in motion | G3, G4, G15; director |
| OP-4 | **Spires:** smooth glassy black towers, ring of open arches at the crown, deep spiral grooves; on the near side the grooves run "/" (lower-left to upper-right). The foot stays dark stone in water. Never fix by mirroring. Check at full size on every Spire frame | G5, excerpt §3 |
| OP-5 | **No spoilers for any S1 episode:** no water pouring over the dike into the Lows, no flooded houses, no ruin, no night flood (E10); no gate, no bar, no beam across a gate, no evacuation gate plate (PL-0021) (SEC-009, Sc 1/18); no tide-post (PL-0022, from S1E3); no cracked or damaged Spire; no pale IX wash or Ninth tier reading on the map; no signature line, no seal on the map; no book or page titled *The Chronicle of the Dry Years*; no rings on water (the stone's motif) | v4 §3.3, keeper §7 |
| OP-6 | **Tapestry: panels 1, 2 and 5 only** (this board uses 2 and 5). Never 3, 4, 6. Fabric fills the frame, no pillarbox | keeper §7, G13 |
| OP-7 | **Heraldry:** one banner shape — tall vertical banner, slanted cut at the bottom, long point at the pole (DEC-66); fields and devices per `refs/HERALDRY/H0x` and G11; no shields anywhere; seals are round. Rusk (gate device) is not shown as a close-up (OP-5) | G11, DEC-66 |
| OP-8 | Spirals anywhere (borders, shells, map rose) turn **sunwise** (clockwise from the centre outward as the camera sees it). Pass `refs/HERALDRY/H16_ashare_reference_spiral.png` when a spiral must read | excerpt §3 |
| OP-9 | **Compass:** sea and harbour west, sunset over the sea; the hill with the Steps east; dawn comes from behind the hill. The Lows sit in the dike's shadow, never in direct high sun | DEC-65, visual bible §3.3 |
| OP-10 | No text in any generated frame. The only text in the OP is the HOLLOWSTONE logo (cut 32) and the small corner bug ANIME-STYLE · AI-ANIMATED from the OP on (v4 §2). Lower 15% of every frame free of key detail | visual bible §5, v4 §2 |
| OP-11 | **No hflip** of any frame or clip | visual bible §11.2 |
| OP-12 | Video: anything with a Spire or water → Kling only (never MiniMax). Every motion prompt lists what must not change | G15, RESULTS.md |

## 2. Music map (measured on the file, 2026-11-24)

Measured with band energy per bar and a 0.1 s RMS envelope (`ffmpeg` → numpy, $0). The actual take differs from the plan table in `main_theme.md` §4: the full-energy block runs on to the last hit.

| Section | OP time | Bars | What is heard | Picture job |
|---|---|---|---|---|
| S1 Intro — the call | 0:00.0–0:12.0 | 1–4 | solo cello, open fifth, no drums | the world wakes at dawn: wide, slow |
| S2 Groove — the Lows | 0:12.0–0:21.0 | 5–7 | stamps on 1 and 3, claps, barrel; whistle on the last beat ≈0:20.25 | the Lows at work: cuts on the beat (1.5 s) |
| S3 Theme | 0:21.0–0:45.0 | 8–15 | strings carry the melody | the city climbs, bottom to top, morning to afternoon (3.0 s cuts) |
| S4 Rise — the Steps | 0:45.0–0:57.0 | 16–19 | brass calls, snare build | houses, banners, tapestry, the map (accelerating to 1.5 s) |
| S5 Hook | **0:57.0**–1:09.0 | 20–23 | octave leap on the downbeat 0:57.0 (cymbal: high band +7 dB), full drums | action burst: water as force |
| S6 Answer | 1:09.0–1:21.0 | 24–27 | full energy, cadence | the storm settles; climax image |
| S7 Last hit + tail | 1:21.0–1:30.0 | 28–30 | strong hits every 1.5 s, **last hit 1:22.5**, then decay (−12 → −31 dB by 1:23.5, silence by 1:29) | logo on the last hit, held on the decay; fade 0.4 s at the end |

## 3. Techniques that AI generation can carry here (energy without characters)

1. **One generated motion per clip** (Kling), and the edit makes the rhythm: every 5 s clip is trimmed to its best 1.5 or 3.0 s, the impact frame placed on the beat.
2. **Speed ramps in ffmpeg** (`setpts`, `minterpolate` off — frame blending only): one clip reused faster in the hook (cut 28 = cut 4 at 2×). No extra cost.
3. **Ink-frames on hits** (2 frames, ffmpeg `negate`+`lutyuv` posterize to blue-black and linen): a dark "impact frame" instead of a white flash, so nothing reads as glow. Used at 0:57.0, 1:01.5, 1:04.5, 1:06.0.
4. **Whip-pan transitions** (L-19 style: directional blur 4 frames + cut), max three in the OP.
5. **Camera shake** (L-05) on the wave impact only (0:57.0–0:58.0, decaying).
6. **LA moves on existing plates** (L-01 push, L-02 pan, L-03 tilt, L-06 rain, L-08 mist, L-10 ripple): free, and they hold the style best.
7. **Start/end frame** for the one transformation (chop → glass, cut 31) on Kling 3 Pro; if the endpoint is not supported, prompt-only from the start frame (§7 Q2).
8. Big scale **without crowds**: scale comes from architecture (dike, wheels, Spires, ship masts) and from water; no generated crowd.

## 4. Shot table

Class: **LA** = ffmpeg on a still (limited_animation codes); **K25** = Kling 2.5 Turbo Pro i2v 5 s; **K3P** = Kling 3 Pro i2v 5 s; **K3P10** = Kling 3 Pro 10 s. Frame source: **EX** = existing file ($0), **NEW** = NB2 /edit frame (prompt in §5).

| # | In – Out | Sec | Music | Content and camera | Class | Frame source |
|---|---|---|---|---|---|---|
| 01 | 0:00.0–0:06.0 | 6.0 | S1 bars 1–2 | Highwater at dawn: tilt DOWN from the crown arches of the Crown Spire along its grooves to the misty Lows below the dike (L-03 reversed, slow ease-in; L-08 mist layer) | LA | EX `refs/PL-0004/D01_A_dawn-ebb_v1.png` (9:16). Paint out the crack lines on the left Spire locally ($0) before use (OP-5) |
| 02 | 0:06.0–0:09.0 | 3.0 | S1 bar 3 | The Ninth's lane at dawn, mist drifting, puddles shiver, rope bridge sways; no people | K25 (done) | EX clip `output/video_test/alley__kling-2.5-turbo-pro.mp4` (passed the video test: "subtle, stable, light unchanged"); use 0.5–3.5 s |
| 03 | 0:09.0–0:12.0 | 3.0 | S1 bar 4 (phrase hangs) | ECU: a tarred net hung to dry, drops gather and fall from the mesh; behind it, out of focus, a string of unlit lanterns sways between stilt-houses | K25 | NEW F03 |
| 04 | 0:12.0–0:13.5 | 1.5 | S2 bar 5 (first stamp) | Inside the rim of a giant treadwheel: wooden slats rush past camera as the drum turns | K25 | EX `refs/PL-0008W/D05_W2_morning_v1.png` |
| 05 | 0:13.5–0:15.0 | 1.5 | S2 bar 5 b3 | A wooden pump spout bursts out water into a plank channel, counterweight chain jerks | K25 | NEW F05 |
| 06 | 0:15.0–0:18.0 | 3.0 | S2 bar 6 | The three great treadwheels in a row under their shed, turning; tiny anonymous walker silhouettes inside (scale only) | K25 | EX `refs/PL-0008W/D05_W1_morning_v1.png` |
| 07 | 0:18.0–0:19.5 | 1.5 | S2 bar 7 | A row of drying nets on poles snaps in a gust across a plank-walk | K25 | NEW F07 |
| 08 | 0:19.5–0:21.0 | 1.5 | S2 bar 7 b3 (whistle ≈0:20.25) | Whip-pan UP from a stilt-house roof into the pale sky, blur peaks on the whistle → cut | LA (L-02 + whip blur) | EX `refs/PL-0008/D02_C2_dawn-ebb_v1.png` (top third) |
| 09 | 0:21.0–0:24.0 | 3.0 | S3 bar 8 (theme enters) | Flyover: camera glides forward over the stilt-town — lanes of water, plank bridges, tar roofs, washing lines — toward the dike and the hill with the three Spires far behind | K3P | NEW F09 |
| 10 | 0:24.0–0:27.0 | 3.0 | S3 bar 9 | Rooftops in rain: tarred roofs, gutters overflowing, rain lines, chimney smoke bending | K25 (+L-06 rain layer if thin) | NEW F10 |
| 11 | 0:27.0–0:30.0 | 3.0 | S3 bar 10 | The tide comes back: water climbs the tarred pilings past painted white tide marks, under a plank bridge; slow push-in | K25 (fallback LA L-16) | NEW F11 |
| 12 | 0:30.0–0:33.0 | 3.0 | S3 bar 11 | A bronze watch bell on a sluice-worker's post swings and strikes; rain-wet rope | K25 | NEW F12 |
| 13 | 0:33.0–0:36.0 | 3.0 | S3 bar 12 (Mids) | The Lantry counting hall, rows of empty desks with open ledgers, dust in the window beams; slow push down the aisle (L-01 + L-07 dust) | LA | EX `refs/PL-0011/D11_L1_late-aft_v1.png` (check the far end: no figure) |
| 14 | 0:36.0–0:39.0 | 3.0 | S3 bar 13 | INS top-down: an open ledger with ruled columns of illegible ink, a stack of copper coins tips and slides across green felt | K25 | NEW F14 |
| 15 | 0:39.0–0:42.0 | 3.0 | S3 bar 14 (Steps) | The city on its granite hill seen from the harbour: terraces, palace, ships, three Spires; slow lateral pan right (L-02) | LA | EX `refs/PL-0004/D01_C_late-aft_v1.png` (check OP-9: the light must come from the west/camera side; if the sun reads behind the hill → swap to `D01_A_late-aft`) |
| 16 | 0:42.0–0:45.0 | 3.0 | S3 bar 15 | Low angle on the Crown Spire, tilt UP the grooves to the ring of arches against a pale sky (L-03) | LA | EX `refs/PL-0014/D08_S1_late-aft_v1.png` (G5 check at full size; if it fails → re-frame from reserve) |
| 17 | 0:45.0–0:48.0 | 3.0 | S4 bar 16 (brass) | Tapestry panel 2: the nine banners on the shore, the nine families facing the black tower; slow pan left→right across the weave (L-02) | LA | NEW F17 = the panel-2 re-weave already required by the finals checklist (sc05-sh020/070); serves pilot and OP |
| 18 | 0:48.0–0:49.5 | 1.5 | S4 bar 17 | Banner CORVANE fills the frame, snapping in the wind on a granite terrace | K25 | NEW F18 |
| 19 | 0:49.5–0:51.0 | 1.5 | S4 bar 17 b3 | Banner DASK | K25 | NEW F19 |
| 20 | 0:51.0–0:52.5 | 1.5 | S4 bar 18 | Banner LANTRY | K25 | NEW F20 |
| 21 | 0:52.5–0:54.0 | 1.5 | S4 bar 18 b3 | Banner FENNICK | K25 | NEW F21 |
| 22 | 0:54.0–0:55.5 | 1.5 | S4 bar 19 (snare) | Tapestry panel 5: the cormorant sail across the harbour mouth, ships at sea; fast push-in (L-01, 10% in 1.5 s) | LA | EX `refs/TAPESTRY/E06_panel5_v1.png` |
| 23 | 0:55.5–0:57.0 | 1.5 | S4 bar 19 b3 (roll) | The Tithe Map top-down with its three tier tints; fast accelerating push toward the hill (east), ending in a whip into the hook | LA (L-01 + L-17 tints) | EX `refs/M-MAP/E05_map_base_v1.png` + the three tint overlays of Sc 7; **no IX wash, no legend row 4, no signature line, push never toward the Ninth (south-west)** |
| 24 | **0:57.0**–1:00.0 | 3.0 | S5 bar 20 — **octave leap** | HERO: a grey storm wave smashes into the outer face of the great sea dike; spray towers above the crest and falls back to the sea side. Impact frame on 0:57.0, ink-frame + shake (L-05) | K3P | NEW F24 |
| 25 | 1:00.0–1:01.5 | 1.5 | S5 bar 21 | The harbour in chop: ships pitch, masts sway, gulls thrown sideways | K25 | EX `refs/PL-0018/D09_H1_late-aft_v1.png` |
| 26 | 1:01.5–1:03.0 | 1.5 | S5 bar 21 b3 | A stone weir: the sea roars over its lip into a sluice channel (no gate leaves, no beam) | K25 | NEW F26 |
| 27 | 1:03.0–1:04.5 | 1.5 | S5 bar 22 | Low rush: camera races forward a metre above a canal between stilt-houses, pilings flicking past | K3P | NEW F27 |
| 28 | 1:04.5–1:06.0 | 1.5 | S5 bar 22 b3 | Treadwheel rim at speed (cut 04 clip at 2×, frame blend) | LA (reuse) | cut 04 clip |
| 29 | 1:06.0–1:09.0 | 3.0 | S5 bar 23 | Crane UP from rain-lashed rooftops of the Mids to the three Spires dark against a breaking storm sky | K3P | NEW F29 |
| 30 | 1:09.0–1:12.0 | 3.0 | S6 bar 24 | Dusk in the lane: the tide lies in the canal, lanterns lit in doorways, the water's ripples settle until it is calm | K25 | EX `refs/PL-0008/D02_C3_dusk_v1.png` |
| 31 | 1:12.0–1:22.5 | 10.5 | S6 bars 25–27 + bar 28 b1–2 | **CLIMAX:** the harbour at last light. The chop dies down; the water turns perfectly still like glass; ships and masts freeze with exact mirror reflections; slow push toward the sunset over the sea. Last 0.5 s = held frame (L-21) | K3P10 | EX start `refs/PL-0018/D09_H1_late-aft_v1.png`, end `refs/PL-0018/D09_H2_glass_v1.png` |
| 32 | **1:22.5**–1:30.0 | 7.5 | S7 last hit + tail | **TITLE:** HOLLOWSTONE lands on the last hit over the Crown Spire silhouette at dusk; plate pushes 3% over 7.5 s; logo holds on the decay; fade to black 1:29.6–1:30.0 | LA + logo | EX `refs/PL-0014/D08_S1_dusk_v1.png` (G5 check) + logo graphic |

**32 cuts**; average shot length 2.8 s (hook 1.5–3 s, climax deliberately long).
Adjacency checks done on the table: no Corvane cut (18, 22) is next to any stone or ring device; the Ilvane and Quell devices appear only woven and small inside cut 17; no gate, bar or Rusk close-up anywhere; tapestry cuts (17, 22) are not adjacent to any Spire-crown image.

## 5. NB2 frame prompts (new frames only)

All new frames: `fal-ai/nano-banana-2/edit`, 16:9, at the largest size the endpoint gives (LA push needs ≥1.25× margin), with the listed reference images. Each prompt = text below + `{STYLE_BASE}` + `{AVOID_OP}`.

`{STYLE_BASE}` = visual bible §10.1, verbatim:
`2D anime-style TV series still, original character and world design, clean cel-shaded characters with crisp thin dark blue-black ink outlines of slightly varying weight, flat color fills with two shadow tones, cool violet-blue shadows, restrained highlights only on eyes, hair, metal and wet surfaces, detailed painterly matte-painting background with atmospheric haze, wet reflective stone and water, motivated cinematic lighting, muted desaturated palette with deep teal-black shadows, subtle film grain, grounded epic fantasy, 16:9 widescreen composition`

`{AVOID_OP}` =
`One single full-frame image: no inset, no letterbox bars, no frames or boxes drawn on top. No people and no faces in the frame (unless the prompt allows tiny distant silhouettes). Avoid: photorealism, 3D look, chibi style, neon colors, any text, letters, numbers or labels, watermark, logo, multiple panels, split screen, glowing objects, glowing lines or cracks, light inside the tower grooves, magic sparkles, lightning, mirrored image, shields, gates or bars across gates, stones or pebbles on cords, rings.`

`{SPIRE}` (when a Spire is visible) =
`the towers are smooth glassy black stone cones, each crowned by a ring of open arches, with deep spiral grooves winding up the whole height; on the near side of each tower the grooves rise from lower-left to upper-right ( / ); the grooves are dark, nothing lights up; the foot of each tower is dark stone standing in water`

| Frame | Refs (in order) | Prompt (before STYLE_BASE + AVOID_OP) |
|---|---|---|
| **F03** net + lanterns | `PL-0008/D02_C1_dawn-ebb_v1.png` (light, materials) | `Extreme close-up of a heavy tarred fishing net hung to dry on a wooden pole in a stilt-town lane at dawn, the knotted mesh fills the left two thirds of the frame, clear water drops gathering on the knots, one drop about to fall. Behind it, softly out of focus, a sagging rope strung between two stilt-houses with four small unlit tin lanterns hanging from it. Cold grey-teal dawn light from above, no direct sun, thin mist. Shallow depth of field.` |
| **F05** pump spout | `PL-0008W/D05_W1_morning_v1.png` | `Close shot of a crude wooden pump spout on a plank walkway beside the great treadwheel shed, a thick gush of grey-green water bursting out of the spout into a narrow plank channel, white foam, an iron counterweight hanging on a heavy chain beside it. Wet tarred timber, rust stains, cold morning light from a narrow strip of sky.` |
| **F07** drying nets | `PL-0008/D02_C1_dawn-ebb_v1.png` | `A row of six tall poles along a plank walkway between stilt-houses, long brown fishing nets hung between them, all billowing hard in a sudden gust from the left, ropes taut, the dike wall high above the roofs at the top edge. Diffuse cool daylight, wet wood, puddles. No people.` |
| **F09** flyover start | `PL-0004/D01_A_dawn-ebb_v1.png` (city layout, towers), `PL-0008/D02_C1_dawn-ebb_v1.png` (materials) | `High aerial view looking forward over a vast stilt-town below sea level in the early morning: a maze of narrow water lanes, plank bridges and tarred roofs, washing lines, small boats tied to pilings; in the middle distance a towering brick sea dike, and beyond it a granite hill with terraces and a palace, and three tall black towers on the hill, the middle one the tallest. {SPIRE}. Cold grey-teal light in the town, the first sun touching only the hill and the tower tops. Tiny distant specks of people on far bridges are allowed, no figure larger than a dot.` |
| **F10** rooftops in rain | `PL-0008/D02_C3_dusk_v1.png` (materials) | `Rooftops of a crowded stilt-town in heavy rain, seen from a slightly higher roof: steep tarred plank roofs at different heights, overflowing wooden gutters pouring water, crooked chimneys with smoke bent flat by the wind, washing lines whipping. Dark rain clouds, cold blue-grey light, long vertical rain streaks, splashes on every surface. No people.` |
| **F11** tide on pilings | `PL-0008/D02_C3_dusk_v1.png` | `Low shot at water level under a plank bridge between stilt-houses: tarred wooden pilings rising out of dark water, each piling marked with painted white horizontal tide lines; the water stands just below the lowest line and is creeping upward, small eddies around the posts. Diffuse cool afternoon light reflected from the water onto the underside of the bridge (soft ripple caustics). No people.` |
| **F12** watch bell | `PL-0008W/D05_W1_morning_v1.png` (materials) | `Medium close shot of a small bronze watch bell hanging from an iron bracket on a thick tarred sluice-worker's post, a wet rope tied to the clapper, rain dripping from the bracket; behind, out of focus, the treadwheel shed and a water channel. Cold grey daylight, wet surfaces. No people, no gate, no bar.` |
| **F14** ledger + coins | `M-LEDGER/E12_ledger_page-a_v1.png` (paper and ink style only) | `Top-down view of an open clerk's ledger on worn green felt, two pages of ruled columns filled with tiny illegible ink scribbles, a brass inkwell and a quill at the top edge, a small tower of rough copper coins standing on the right page, about to tip over. Flat cool light from a tall window, dust motes. No hands, no readable text or numbers.` |
| **F17** panel 2 re-weave | `TAPESTRY/E06_panel2_v1.png`, `TAPESTRY/E06_panel1_v1.png` (style), `HERALDRY/H01…H07` emblem PNGs, `GROUPS/C06_emblem_strip_ref.png` | As finals checklist sc05-sh020: `Re-weave this tapestry panel keeping its weave, palette and border: nine tall woven banners on a shore, each banner tall and vertical with a slanted cut at the bottom and the long point at the pole; six banners in the centre and three at the edges (two at the left, one at the right); nine small woven figures stand under them with one hand raised, all facing a black tower rising from the woven sea; no weapons, no spears; the open-hand banner shows a RIGHT hand, palm forward, thumb on the viewer's right, holding a small grey spiral stone; the cormorant banner shows a black cormorant diving beak-down into a silver wave. Border spirals turn clockwise from the centre outward. Fabric fills the whole frame.` + `CHRONICLE` module **instead of** STYLE_BASE (visual bible §10.2), negative "anime character, cel shading, 3D". Order and fields of all nine banners per keeper §2 and G11; keeper checks before use |
| **F18** banner Corvane | `HERALDRY/H01_corvane.png`, `PL-0004/D01_C_late-aft_v1.png` (light) | `A single tall silk banner fills the frame, hanging from a pole on a granite terrace and snapping in a strong wind, the banner is vertical with a slanted cut at the bottom, the long point at the pole side; deep blue field, a black cormorant diving beak-down into a silver wave with exactly three crests, exactly as in the emblem reference. Low golden afternoon sun from the left, open pale sky behind, crisp shadows in the folds.` |
| **F19** banner Dask | `HERALDRY/H02_dusk.png`, same light ref | same wording; `ochre field, a bronze sickle with its handle (a farm tool) above three dark furrows, exactly as in the emblem reference` |
| **F20** banner Lantry | `HERALDRY/H07_lantry.png`, same light ref | same wording; `black field, a polished rose-copper balance with a level beam, the left pan holding water, the right pan empty, exactly as in the emblem reference` |
| **F21** banner Fennick | `HERALDRY/H06_fennike.png`, same light ref | same wording; `acid sulphur-yellow field, a grey hare sitting in profile facing left, both ears up and apart, exactly as in the emblem reference` |
| **F24** wave on the dike | `PL-0004/D01_A_dawn-ebb_v1.png` (dike design) | `Wide low shot from the sea side of a colossal brick sea dike under a grey storm sky in daylight: a huge dark green-grey wave crashes against the dike's sloping outer face, a towering wall of white spray rising high above the dike crest and curling back toward the sea; the top edge of the dike stays dry, no water pours over it. Wind-torn clouds, flying foam, cold grey light. No people, no buildings breaking.` |
| **F26** weir | `PL-0008W/D05_W1_morning_v1.png` (materials) | `Low angle at the lip of a wide stone weir: grey-green sea water roars over the smooth stone edge in a thick curved sheet and crashes into a deep brick sluice channel below, white foam and mist. Iron rings set in the stone walls, wet black brick, cold storm light. No gate leaves, no beams or bars across the channel. No people.` |
| **F27** canal rush | `PL-0008/D02_C3_dusk_v1.png` (lane), `PL-0008/D02_C1_dawn-ebb_v1.png` | `Point of view just above the water, looking straight down a long narrow canal between two rows of stilt-houses in a squall: tarred pilings on both sides, low plank bridges crossing ahead, ropes and hanging nets, wind-driven rain, dark choppy water. Strong one-point perspective toward a bright strip of grey sky at the far end. No people, no boats in the path.` |
| **F29** crane-up start | `PL-0004/D01_A_late-aft_v1.png` (towers), `PL-0011/D11_L1_late-aft_v1.png` (Mids materials) | `Looking up from wet slate and brick rooftops of the middle town in hard rain, chimneys and gables in the foreground, and above them, filling the upper half, three tall black towers on the hill against a storm sky that is breaking open, a band of pale light behind the clouds. {SPIRE}. Rain streaks, dark blue-grey palette, no lightning. No people.` |

Pre-check for every new frame before acceptance (in this order): people/faces (OP-1) → stone/ring (OP-2) → glow (OP-3) → groove direction "/" and dark foot (OP-4) → gate/bar/flood-over-dike (OP-5) → text/labels (OP-10) → heraldry per H0x (OP-7).

## 6. Kling motion prompts

Base (visual bible §10.3, as used in the video test): `Subtle 2D anime animation, the colors and line art stay exactly as in the source image, stable outlines, no morphing, consistent lighting.` + the camera + the one motion + **MUST NOT CHANGE** list. Negative (all clips): `morphing, flickering line art, warping background, people appearing, faces, glowing objects, light inside the tower grooves, lightning, new light sources, sudden cuts, text`.
Duration 5 s unless marked; output 1080p; one take, a second only if the first fails acceptance.

| Cut | Model | Camera + motion | MUST NOT CHANGE |
|---|---|---|---|
| 03 | K25 | `Static camera. Water drops gather on the net knots and fall one by one; the net sways very slightly; the lanterns in the background swing gently on their rope.` | lanterns stay unlit; light level; no people; net shape |
| 04 | K25 | `Static camera. The giant wooden drum turns steadily toward camera, its slats moving past from top to bottom; water drips from the slats.` | drum geometry; light; no figures appear inside the drum |
| 05 | K25 | `Static camera. Water gushes from the spout in strong pulses, foam spreads along the channel; the counterweight chain jerks down once.` | spout and channel shape; light; no hands, no people |
| 06 | K25 | `Very slow push-in. All three treadwheels turn steadily at the same speed; tiny distant figures inside walk in place.` | wheel count (3) and design; figures stay tiny and anonymous; light |
| 07 | K25 | `Static camera. A strong gust from the left: the nets billow and snap, the poles flex slightly, then the nets fall back.` | number of poles; dike wall; light; no people |
| 09 | K3P | `The camera glides slowly forward and slightly down over the town toward the dike and the hill; parallax between the near roofs and the far towers; smoke drifts.` | towers keep their shape, height order and groove direction; nothing lights up; no new buildings; no people larger than dots |
| 10 | K25 | `Static camera. Heavy rain falls, the gutters overflow and pour, the smoke bends in the wind, washing lines whip.` | roof layout; light (no lightning, no flashes); no people |
| 11 | K25 | `Very slow push-in toward the pilings. The water level rises steadily by about one tide mark, small eddies swirl around the posts, caustic ripples shimmer under the bridge.` | painted marks stay fixed on the pilings; water does not reach the bridge; no light change; no people |
| 12 | K25 | `Static camera. The bell swings once to the right and back, the clapper strikes, rain drips from the bracket.` | bell size and shape; post; light; no hands, no people, no gate |
| 14 | K25 | `Static camera, top-down. The tower of copper coins tips over and the coins slide and roll across the felt; one coin spins and settles.` | ledger pages and scribbles stay still and illegible; no hands; no text appears; coins stay copper |
| 18–21 | K25 (×4) | `Static camera. The banner snaps and ripples hard in a strong wind from the left; the pole stays still.` | the emblem and its colours stay exactly as in the source; banner shape (slanted cut, long point at the pole); light |
| 24 | K3P | `Static camera, low. A huge wave rolls in and crashes against the dike; spray explodes upward above the crest and falls back toward the sea; foam slides down the face.` | the dike stays intact; **no water flows over the crest into the town**; daylight storm (not night); no people; no lightning |
| 25 | K25 | `Static camera. Choppy waves roll across the harbour, ships pitch and their masts sway, gulls are blown sideways.` | ship count and positions; sun position; no people on decks |
| 26 | K25 | `Static camera. Water pours over the weir lip in a thick sheet and crashes into the channel, foam and mist billow.` | weir and channel shape; no gate or bars appear; light |
| 27 | K3P | `The camera races straight forward low over the water along the canal, passing under one plank bridge; pilings flick past on both sides; rain.` | canal stays empty (no boats, no people); house design; no light change |
| 29 | K3P | `The camera cranes up from the rooftops until the three towers fill the upper frame; rain streaks; the clouds behind the towers slowly part.` | towers: shape, order, groove direction "/", grooves stay dark; no lightning; no people |
| 30 | K25 | `Static camera. Small ripples on the canal slowly settle until the water is calm; the lantern flames flicker faintly.` | lanterns: same brightness, no halo; sky colour; no people; no rings on the water |
| 31 | K3P10 (start H1, end H2) | `Slow push-in toward the sunset over the sea. The choppy waves calm down little by little until the whole harbour is perfectly still like glass, the ships and masts stop moving, and the water shows exact mirror reflections.` | sun position and colour; ship count and positions; nothing glows; no light change except the water calming; no people |

Logo (cut 32): typeset title HOLLOWSTONE built from the animatic v3 title card (sc05-sh100) as the starting point; flat ink and linen colours, no glow, no bloom, no lens flare; enters on 1:22.5 with a 3-frame ink-wipe (left to right), centred in the upper-middle third (clear of the lower 15%). Final logo design: artist + marketing (§7 Q4).

## 7. Cost (paid steps not started; gatekeeper first)

Prices: NB2 /edit $0.08 per image; Kling 2.5 TP $0.35 per 5 s clip; Kling 3 Pro $0.56 per 5 s, $1.12 per 10 s (fal catalog, video test 2026-11-23). Takes per the brief: 2 per new frame, 1.5 per motion clip.

| Item | Count | Takes | Unit | $ |
|---|---|---|---|---|
| New frames NB2 (F03, F05, F07, F09, F10, F11, F12, F14, F17, F18–F21, F24, F26, F27, F29) | 17 | 2 | 0.08 | **2.72** |
| Kling 2.5 TP 5 s (cuts 03, 04, 05, 06, 07, 10, 11, 12, 14, 18, 19, 20, 21, 25, 26, 30) | 16 | 1.5 | 0.35 | **8.40** |
| Kling 3 Pro 5 s (cuts 09, 24, 27, 29) | 4 | 1.5 | 0.56 | **3.36** |
| Kling 3 Pro 10 s (cut 31) | 1 | 1.5 | 1.12 | **1.68** |
| LA cuts (01, 08, 13, 15, 16, 17 move, 22, 23, 28, 32), existing clip (02), logo, upscale, assembly | 11 | — | — | **0.00** |
| **Total expected** | | | | **$16.16** |
| Reserve to the $20 cap | | | | $3.84 (first use: re-frame cut 16 or 32 if the G5 groove check fails, $0.16 each; then one extra K3P take) |

Worst case under the pilot take rule is not budgeted here: the OP runs at 2 frame takes / 1.5 motion takes and stops at $20; any cut that fails twice falls back to its LA version (all K25 cuts have one: L-10, L-06, L-13 loop, still + L-01).

## 8. Order of work (after the gate opens)

1. $0: build the LA animatic of the OP now from the existing plates and grey placeholders for NEW frames, on the music (cut list §4) → gatekeeper + keeper look at timing and content.
2. Frames F03…F29 (17 × NB2, up to 2 takes) → acceptance §5.
3. Kling clips in this order: hero cuts 24, 31 first (they decide whether the OP works), then 09, 27, 29, then the K25 set.
4. Assembly in ffmpeg on `lib_mus_theme-op-fullrange_v1.wav` (and the HPF pilot version); ink-frames, shake, whips; logo; corner bug.
5. Re-check the last-hit timecode 1:22.5 (and 0:57.0) against the composer's re-drummed file; bar lines do not move, so only the logo frame may shift by a beat.

## 9. Open questions

1. **Keeper:** sign the OP list. Points to check: no characters (investor); panels 2 and 5 only; no light in the grooves at all; storm wave on the **outer** dike face in daylight (not the E10 flood); Lantry banner "left pan water" and Fennick banner in close-up; the Rusk device kept out of close-ups.
2. **IT engineer:** does `fal-ai/kling-video/v3/pro/image-to-video` take an end frame (`tail_image_url` or equivalent) at 10 s? If not, cut 31 runs prompt-only from H1 (same price).
3. **Composer:** confirm the last hit stays on 1:22.5 after the drum re-work (the plan table in `main_theme.md` §4 says 1:18.0, the current file has it at 1:22.5).
4. **Artist / marketing:** final HOLLOWSTONE logo lettering (cut 32 uses the animatic title card until then).
5. **Studio director:** the investor's earlier character run-through is replaced by the world-only board; when a season-2 OP or a character OP is wanted, the character rules from v4 §3.3 and keeper §7 (Kes, Ione, Ruel, Corr from his left side) still apply.
