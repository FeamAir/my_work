#!/usr/bin/env python3
"""One-off: storyboard v1.2 -> v1.3 (gate B1-B4, keeper R2). Every replacement must match exactly once."""
import sys

P = "/home/user/my_work/studio/direction/opening/S1_OP_storyboard.md"
s = open(P, encoding="utf-8").read()
R = []


def rep(old, new):
    n = s.count(old)
    if n != 1:
        sys.exit(f"expected 1 match, got {n}: {old[:90]!r}")
    R.append((old, new))


# ---------------------------------------------------------------- header ---
rep("# HOLLOWSTONE — Season 1 opening (instrumental, 90.0 s) — storyboard v1.2",
    "# HOLLOWSTONE — Season 1 opening (instrumental, 87.0 s) — storyboard v1.3")
rep("Version 1.2 · 2026-11-24 · author: director (anime-director) · status: **storyboard only. No paid call made. Signed by the canon keeper with edits (all applied word for word in this version); the keeper re-checks only the new frames F15, F17, F18, F23 (+ F26, new in v1.2) before Kling. Next: gatekeeper; nothing is generated before the gate opens.**",
    "Version 1.3 · 2026-11-24 · author: director (anime-director) · status: **storyboard only. No paid call made. v1.3 = v1.2 + the gate's blockers B1–B4 (`qa/gate/gate-op-2026-11-24.md`) + the keeper's rulings §R2 (`reports/lore-op-2026-11-24.md`), all applied word for word. Signed by the canon keeper (R2.7: the signature holds after R2.2–R2.4 and R2.6 p. 1); the keeper checks F15, F17, F18, F23 and F26 at full size. Next: the gatekeeper re-checks the v1.3 diff; nothing is generated before the gate opens.**\n"
    "v1.3 changes: B1 `{AVOID_OP_F18}` verbatim again (`magic sparkles, ` restored); B2 §R2.1–R2.6 applied (drops on the logo letters only; F26 and cut 26 with many mixed prints; no steam in 13, OP-14, §3, §7; GLASS = even full-frame steps, no front; the H1/H2 crop + finial paint-out + dark lamps, plates prepared at $0); B3 the OP is **87.0 s** (cut 33 1:22.5–1:27.0, K17 0.0–4.5 s at 1×, picture and audio fade 1:26.5–1:27.0); B4 NB2 output size and parameters pinned (§5), price $0.08 confirmed. The $0 animatic of §9 step 1 is built: `output/opening/S1_OP_animatic_v1.mp4`.")
rep("Music: **`output/music/lib_mus_theme-op-drums_v2a.mp3`** (90.0 s). `…_v2b.mp3` shares the same grid (measured, §2); the investor's final choice between v2a and v2b does not move any cut.",
    "Music: **`output/music/lib_mus_theme-op-drums_v2a.mp3`**, used 0:00.0–1:27.0 with an audio fade 1:26.5–1:27.0 (studio director: master on v2a, 87.0 s = 29 bars). `…_v2b.mp3` shares the same grid (measured, §2) and can be swapped in without moving any cut.")

# ---------------------------------------------------------------- §0 RU ---
rep("Человеческий след без людей: следы босых ног под первым ливнем (26), пар над стаканом в пустом зале (13), тканые фигуры панели 2 (18).",
    "Человеческий след без людей: множество следов босых ног разного размера на переулке под первым ливнем (26, R2.2), тканые фигуры панели 2 (18). Пара в 13 нет (R2.3).")
rep("затем гавань стекленеет четырьмя ступенями на ударах 1:13.5 / 1:15.0 / 1:16.5 / 1:18.0, фронт идёт от моря к берегу (нейтрально, флаг привратнику), чистое стекло 1:19.5–1:22.5,",
    "затем гавань стекленеет четырьмя ступенями на ударах 1:13.5 / 1:15.0 / 1:16.5 / 1:18.0, каждая ступень ровно по всему кадру сразу, без фронта и направления (хранитель R2.4), чистое стекло 1:19.5–1:22.5,")
rep("- **Хвост:** музыка затихает к ≈1:26.5. Мастер 90.0 с: облака K17 растянуты без стоп-кадра, капля с края буквы падает на 1:25.0 (рифма с каплей 0:11.25). Короткая версия 86.5 с — на решение инвестора.",
    "- **Хвост, опенинг 87.0 с:** склейка 33 = 1:22.5–1:27.0 (4.5 с); облака K17 — кусок 0.0–4.5 с на 1×, без растяжки и без стоп-кадра; капля с края буквы падает на 1:25.0 (рифма с каплей 0:11.25), все капли уходят из кадра до 1:26.5; изображение и звук гаснут 1:26.5–1:27.0 (музыка на 1:27.0 ещё ≈ −40 дБ, поэтому фейд, а не обрыв).")

# ---------------------------------------------------------------- §1 OP-14 (R2.3) ---
rep("footprints (26), steam over a glass on a desk (13), woven figures", "footprints (26), woven figures")

# ---------------------------------------------------------------- §2 music (B3) ---
rep("Both files: 90.0 s, identical grid;", "Both files: identical grid, both run past the OP end (the OP uses 0:00.0–1:27.0);")
rep("| S7 Last hit + tail | 1:21.0–1:30.0 | 28–30 | hits every 1.5 s, **last hit 1:22.5**, silence from ≈1:26.5 | title sting on the last hit; tail carried by moving clouds and one falling drop (§4.3) |",
    "| S7 Last hit + tail | 1:21.0–1:27.0 | 28–29 | hits every 1.5 s, **last hit 1:22.5**, silence from ≈1:26.5 (≈ −40 dB residual at 1:27.0) | title sting on the last hit; tail carried by moving clouds and one falling drop; picture and audio fade 1:26.5–1:27.0 (§4.3) |")
rep("| Music silence | ≈1:26.5 | 2076 | — | 33 |",
    "| Music silence; all drops out of frame | ≈1:26.5 | 2076 | — | 33 |\n"
    "| **Picture + audio fade** | 1:26.5–1:27.0 | 2076–2087 | **2076–2087** (last frame of the OP = 2087) | 33 |")

# ---------------------------------------------------------------- §3 (R2.3, R2.4) ---
rep("| **MIST / DUST** | mist drift, dust in beams, steam | L-08, L-07; steam = MIST sprite at 10–15% rising from one point | shafts only where the source is in frame |",
    "| **MIST / DUST** | mist drift, dust in beams | L-08, L-07 | shafts only where the source is in frame |")
rep("| **GLASS** | stepped glass front | `xfade` custom, 4 steps on hits; **direction from the sea (horizon) toward the shore (camera)**, see below | nothing glows on the front (OP-3) |",
    "| **GLASS** | stepped calm | 4 steps on the drum hits; each step lowers the chop **evenly over the whole harbour at once** (K13 retimed 1× → 0.6× → 0.3×, mixed into H2 at 25 / 50 / 75 / 100 %); no front, no edge, no direction | nothing glows on the water (OP-3) |")
old_glass = s[s.index("GLASS, v1.2 direction ("):s.index("## 4. Shot table")]
rep(old_glass,
    "GLASS, keeper R2.4: no moving front; each step is an even mix over the whole frame.\n"
    "```\n"
    "[A][B]xfade=transition=custom:duration=6:offset=OFF:expr='st(0,(1-P)*4);st(1,ld(0)-floor(ld(0)));st(2,(floor(ld(0))+min(1,ld(1)*3))/4);A*(1-ld(2))+B*ld(2)'\n"
    "```\n"
    "A = K13 (chop, slowing 1× → 0.6× → 0.3× with frame blend), B = H2 (glass). The sky band above the horizon is taken from H2 from the start of cut 32 (pixel-aligned with H1). Each step jumps in the first third of its 1.5 s and holds. OFF = 1 frame after the start of cut 32, so step 1 starts on the placed hit frame 1765 (§2.1).\n\n")

# ---------------------------------------------------------------- §4 table ---
rep("Analyst #3: thin steam (MIST 10–15%) rising from the glass on the nearest right-hand desk — someone has just left",
    "Analyst #3: no human trace in 13 (keeper R2.3): no steam; no glass, chair or pen singled out; no close view of the water in a glass")
rep("The first heavy rain on a tarred plank-walk between stilt-houses: a trail of wet bare footprints, adult and child, crosses the planks and leaves the frame; the rain blurs them away",
    "The first heavy rain on a tarred plank-walk between stilt-houses: many wet bare footprints of mixed sizes criss-cross the planks in different directions, the everyday traffic of the lane; the rain blurs them away")
rep("pier lamp-posts unlit: darken their flames and remove their reflections locally on the plate (OP-3) | INK on 1:09.0",
    "pier lamp-posts unlit: darken their flames and remove their reflections locally on the plate (OP-3); both plates prepared at $0 by `direction/opening/tools/op_harbour_plates.py` → `output/opening/plates/D09_H1_op.png`, `D09_H2_op.png` (same mask on both, pixel for pixel; keeper to check before Kling, C2) | INK on 1:09.0")
rep("| the glass front of 32 starts here, at the horizon |",
    "| no glass yet; the calm of 32 has no front and no direction (keeper R2.4) |")
rep("| **CLIMAX part 2:** wide again; the harbour turns to glass in four steps on the drum hits, the front coming from the sea toward the shore; behind it exact mirror reflections of hulls and masts, sun on the horizon; from 1:18.0 the whole harbour is glass | K13 piece 2.0–5.0 s retimed under the front (1× → 0.6× → 0.3×, frame blend) → LA plate |",
    "| **CLIMAX part 2:** wide again; on each of four drum hits the chop drops one step everywhere at once, until the water lies still; exact mirror reflections of hulls and masts, sun on the horizon; from 1:18.0 the whole harbour is glass | K13 piece 2.0–5.0 s retimed under the steps (1× → 0.6× → 0.3×, frame blend) → LA plate |")
rep("no RAIN; nothing glows on the front; no Spire, no singer and no tapestry in this cut or in the cuts on either side | VFX top-5 #1 + analyst #1 (the turn to glass is earned on screen, on the beat). Direction kept neutral (sea → shore), flagged to the gatekeeper |",
    "no RAIN; nothing glows on the water; no Spire, no singer and no tapestry in this cut or in the cuts on either side | VFX top-5 #1 + analyst #1 (the turn to glass is earned on screen, on the beat). no front, no direction (keeper R2.4) |")
rep("| 33 | **1:22.5**–1:30.0 | 7.5 | S7 last hit + tail |", "| 33 | **1:22.5**–1:27.0 | 4.5 | S7 last hit + tail |")
rep("falls out of frame on 1:25.0; fade to black 1:29.2–1:30.0 (tail, §4.3) | K17 piece 0.0–5.0 s stretched to 7.5 s (`framerate` blend, 0.667×, no freeze frame); spray wipe |",
    "falls out of frame on 1:25.0; picture and audio fade 1:26.5–1:27.0 (tail, §4.3) | K17 piece 0.0–4.5 s at 1× (no stretch, no frame blend, no freeze frame); spray wipe |")
rep("no water and no foot of the tower in frame; grooves dark",
    "no water surface (sea, harbour, pool or glass) and no foot of the tower in frame; the only water allowed is graphic spray residue on the logo letters: drops gather and slide on the letters only, never on the tower, never glow, and leave the frame without landing on anything; no rings; grooves dark")
rep("The drop on the logo is graphic spray residue, not water in the scene — keeper to confirm (§10) |",
    "The drop on the logo is graphic spray residue, not water in the scene — confirmed by the keeper (R2.1). All drops leave the frame by 1:26.5 (frame 2076) |")

# ---------------------------------------------------------------- §4.1 / §4.2 (R2.4, R2.1) ---
rep("| 1:13.5 | step 1 | wide: the far water (horizon band) goes to glass | K13 → H2 |",
    "| 1:13.5 | step 1 | wide: the chop drops one step over the whole harbour at once (25 %) | K13 → H2 |")
rep("| 1:15.0 | step 2 | glass reaches the outer ships | K13 → H2 |",
    "| 1:15.0 | step 2 | the whole harbour one step calmer (50 %) | K13 → H2 |")
rep("| 1:16.5 | step 3 | glass reaches the piers | K13 → H2 |",
    "| 1:16.5 | step 3 | the whole harbour one step calmer (75 %) | K13 → H2 |")
rep("| 1:18.0 | step 4 | the whole harbour is glass; hold to 1:19.5 | H2 |",
    "| 1:18.0 | step 4 | the whole harbour is glass (100 %); hold to 1:19.5 | H2 |")
rep("5. 33 has no water and no foot of the tower.",
    "5. 33 has no water and no foot of the tower (the only exception is graphic spray residue on the logo letters, keeper R2.1, §4 cut 33).")

# ---------------------------------------------------------------- §4.3 tail (B3) ---
old_tail = s[s.index("### 4.3 Tail (1:22.5–1:30.0)"):s.index("## 5. NB2 frames")]
rep(old_tail,
    "### 4.3 Tail (1:22.5–1:27.0)\n\n"
    "- 1:22.5: INK, then the wipe, then the logo lands and settles; 6 frames of SHAKE, then still letters.\n"
    "- 1:22.5–1:27.0: K17 clouds keep moving: **piece 0.0–4.5 s at 1×** (no stretch, no frame blend, no freeze). The variant-B grade is held for the whole tail, the most visible place for it.\n"
    "- 1:24.0–1:25.0: a drop gathers on the lower edge of one letter and leaves it on 1:25.0 (frame 2040), falling out of frame. It rhymes with the drop of 0:11.25 and closes the loop. One or two smaller drops (opacity 0.4) slide slowly down other letters and fall out of frame. **Every drop is out of frame by 1:26.5 (frame 2076).** Drops stay on the letters only (R2.1).\n"
    "- ≈1:26.5: the music is silent (≈ −40 dB residual at 1:27.0, measured on v2a and v2b), so the end is a fade, not a hard stop.\n"
    "- **The OP is 87.0 s (frames 0–2087).** Picture fade to black and audio fade 1:26.5–1:27.0 (frames 2076–2087), both linear.\n\n")

# ---------------------------------------------------------------- §5 (B4, B1, R2.2) ---
rep("All: `fal-ai/nano-banana-2/edit`, 16:9, largest output size, refs as listed.",
    "All: `fal-ai/nano-banana-2/edit` with **exactly the parameters of the 164 earlier NB2 edit calls**: `aspect_ratio: \"16:9\"`, `num_images: 1`, `output_format: \"png\"`, `image_urls` = refs as listed, a fixed `seed` per frame, and **no `resolution` key** (fal default `1K`; no web search, no high thinking). Output size **1376×768 px** (as every existing 16:9 NB2 plate, e.g. `PL-0018/D09_H1`, `PL-0008W/D05_W1`; checked against the `meta.json` files and the PNGs). Price **$0.08 per image**, as booked in `pipeline/costs.py` and logged for all 164 calls; fal's pricing for this endpoint (read 2026-11-24, $0): $0.08 per image at 1K, 2K ×1.5, 4K ×2, so do not ask for a higher resolution. `pipeline/fal_client.generate_image(..., aspect_ratio=\"16:9\", extra={\"seed\": N})` sends exactly this; the run script must not add `resolution`. The 1920×1080 frame is made in the edit (`scale`/`crop`, as for all plates).")
rep("glowing objects, mirrored image, shields, weapons, spears, swords, blood, faces in close-up, open mouths, stones or pebbles on cords.`",
    "glowing objects, magic sparkles, mirrored image, shields, weapons, spears, swords, blood, faces in close-up, open mouths, stones or pebbles on cords.`")
rep("`Low close view along a wet tarred plank-walk between stilt-houses at the start of a storm in daylight: a trail of wet bare footprints, some adult-sized and some small child-sized, crosses the dark planks from the lower left and leaves the frame on the right; the first heavy raindrops spatter on the wood; the water below the planks is far down and out of frame. Cold grey storm light. No people, no feet, no legs, no shoes, no shadows of people, no puddles.`",
    "`Low close view along a wet tarred plank-walk between stilt-houses at the start of a storm in daylight: many wet bare footprints of mixed sizes criss-cross the dark planks in different directions and overlap, as on a busy lane; no single trail, no pair of prints walking side by side, no prints leading to the edge of the planks; the first heavy raindrops spatter on the wood; the water below the planks is far down and out of frame. Cold grey storm light. No people, no feet, no legs, no shoes, no shadows of people, no puddles.`")
rep("| **F26** footprints (new, analyst #3) | 26 |", "| **F26** footprints (new, analyst #3; prompt = keeper R2.2) | 26 |")

# ---------------------------------------------------------------- §6 K17 (B3) ---
rep("| the tower's shape and groove direction \"/\"; grooves dark; the foot dark and below frame; no birds or lights added | 33 |",
    "| the tower's shape and groove direction \"/\"; grooves dark; the foot dark and below frame; no birds or lights added | 33 (piece 0.0–4.5 s at 1×) |")

# ---------------------------------------------------------------- §7 (R2.3) ---
rep("7. **Someone was here.** Steam over a glass in the empty hall (13), footprints washed away by the first rain (26).",
    "7. **Someone was here.** The lane's footprints washed away by the first rain (26).")

# ---------------------------------------------------------------- §8 / §9 wording ---
rep("ffmpeg: parallax, pushes, particles, ramps, shake, ink, glass front,", "ffmpeg: parallax, pushes, particles, ramps, shake, ink, glass steps,")
rep("Prices: NB2 /edit $0.08 per image;", "Prices: NB2 /edit $0.08 per image (1K default, 1376×768, §5);")
rep("1. **$0 first: the OP animatic** on `lib_mus_theme-op-drums_v2a.mp3`, with every LA recipe: glass front on cropped H1 → H2",
    "1. **$0 first: the OP animatic** on `lib_mus_theme-op-drums_v2a.mp3` at 87.0 s, with every LA recipe: even glass steps on cropped H1 → H2")
rep("5. Assembly: ffmpeg passes per §4, hit frames per §2.1, logo sting, corner bug; master on drums v2a (swap to v2b with no re-cut if the investor picks it);",
    "5. Assembly: ffmpeg passes per §4, hit frames per §2.1, logo sting, corner bug; master on drums v2a at 87.0 s with the 1:26.5–1:27.0 picture and audio fade (v2b swaps in with no re-cut);")

# ---------------------------------------------------------------- §10 ---
old_q1 = s[s.index("1. **Gatekeeper (flag):** the glass now forms"):s.index("2. **Canon keeper:**")]
rep(old_q1, "1. ~~Gatekeeper (flag): glass direction~~ — **closed by the keeper R2.4:** four even full-frame steps, no front, no direction.\n")
rep("   - F26 footprints (adult and child, washed away by the first rain): not a hint of a specific scene?\n",
    "   - ~~F26 footprints~~ — closed: R2.2 (many mixed prints, no pair);\n")
rep("   - steam over a glass in the counting hall (13);\n", "   - ~~steam over a glass (13)~~ — closed: R2.3 (no steam);\n")
rep("   - the drop on the logo in 33 (graphic spray residue vs. \"no water in 33\");\n",
    "   - ~~the drop on the logo in 33~~ — closed: R2.1 (letters only);\n")
rep("   - the 74% crop plus finial paint-out that removes the dark arch from D09_H1/H2;\n",
    "   - ~~the 74% crop plus finial paint-out~~ — closed: R2.5 (plates prepared in v1.3; keeper checks them before Kling);\n")
rep("3. **Investor:** master length 90.0 s (moving tail) or 86.5 s (fade with the music at ≈1:26.5). Final drum version v2a or v2b: the grid is the same, so the board does not change.",
    "3. ~~Investor: master length; v2a or v2b~~ — **closed by the studio director:** the OP is 87.0 s (29 bars), master on v2a; v2b has the same grid and swaps in with no re-cut.")

for old, new in R:
    s = s.replace(old, new, 1)
open(P, "w", encoding="utf-8").write(s)
print(f"{len(R)} replacements applied")
