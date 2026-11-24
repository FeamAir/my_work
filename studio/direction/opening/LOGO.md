# HOLLOWSTONE logotype — "Tidemark" (v1.4, 2026-11-24)

Owner: concept artist. Used in: OP cut 33 / SAGA OP C13 (title sting 1:22.5–1:27.0), posters, thumbnails, end card.
Assets: `studio/direction/refs/LOGO/` (copies of `studio/art/logo/final/`). Source frame: `studio/art/logo/gen/LOGO_A2_v1.png` (NB2, seed 410722).
v1.4 (director, r20, gate v1.1 И10/И11): §4 brought in line with the built C13 (SAGA OP C v1.1/v1.2): the glint runs **2000–2040** (was 2016–2039; r19 moved it right after the drain so the hold never stalls, the keeper R9.2: timing, not canon); the logo layer has **no own push** any more (its integer `scale … (1+0.015*n/108)` stepped the width 2 px every ~11 frames = a 1-px letter jump, gate И10): the slow push is one sub-pixel whole-frame push of 3 % (OpenCV, `op_saga_build_c.subpix_push`); vertical end card (9:16) in §4.1.

v1.3 (director, gate 2026-11-24 B1/B5: the keeper's R3.3 lines of `reports/lore-saga-op-2026-11-24.md` put into §6 word for word — LOGO_C keeps its own soft light, no `{SIGNATURE_C}`/`{PHONE}`; `#5C6B72` measured on the letter faces; no single-letter render; acceptance with six drops; plus the wet-half contrast probe). Owner of the assets stays the concept artist.
v1.1 (director, with the keeper's R2.5 of `reports/lore-saga-op-2026-11-24.md` word for word and the investor's 1981 landing): tide line at half the cap height in the text (the asset was always there); darkening above the tide line only; the drop never brighter than the dry letters; the landing on the final hit, 1981; the keeper's conditions for every carrier (§2 p. 9–11); a darker plate under the word and a scripted tail (§4). The assets are unchanged.

v1.2 (director, coordinator's request after the style-C reviews): a **3D version LOGO_C** for style C (§6): the same word, granite and tide line as volumetric chisel-cut letters with no 2D outline; every rule of §2 holds; the reveal of §4 runs on it unchanged except for the new `TIDE`. The 2D assets of §3 stay (thumbnails below 240 px, keying, print) until a C clean version exists. Keeper check: §5, K15 of the saga storyboard.

## Кратко (RU)

- **v1.2:** объёмная версия **LOGO_C** для стиля C (§6): та же надпись, тот же гранит и та же линия прилива, но объём и без 2D-обводки; все правила §2 в силе; раскрытие C13 строится на ней.

- Логотип — **«Приливная отметка»**: слово HOLLOWSTONE как надпись, вырубленная резцом в выветренном граните портовой стены. Одна прямая линия прилива пересекает всё слово на половине высоты букв: ниже — мокрый сине-серый камень с солевой коркой и следами водорослей, выше — сухой светлый гранит. Название стиля сериала («Tidemark») становится знаком.
- Буквы проверены побуквенно: H-O-L-L-O-W-S-T-O-N-E.
- Появление на 1:22.5 (кадр 1981, последний удар): **верхняя часть букв (выше линии прилива)** приходит мокрой, вода **уходит** сверху вниз до линии прилива (отлив, вода никогда не поднимается); ниже линии мастер всегда такой, как нарисован. Блик на сухих гранях, капля (не ярче сухих букв) уходит на 1:25.0 под звуковой знак, небо под словом затемнено. Всё в ffmpeg за $0. Тест: `studio/art/logo/motion/reveal_test.sh`.
- Условия хранителя для всех носителей: линия и мокрая зона никогда не поднимаются; знак не кропится до одной буквы или одного штриха; рядом нет верёвки, сваи, столба, фигуры.

## 1. Directions considered

| | Direction | Verdict |
|---|---|---|
| **A** | **Tidemark inscription.** Custom chisel-cut display capitals (tall, slightly condensed, short wedge serifs, V-section bevels), weathered pale granite, one straight tide line across the whole word: wet blue-grey below with a white salt crust on the line and faint weed staining, dry pale stone above; a few drops on the lower edges | **Chosen** (A2). Reads at thumbnail size, owns the series' style name, no canon risk |
| **B** | **Crown-T.** As A, but the T is a Spire: black glassy cone stem with `/` grooves, crossbar = crown band of open arches (B1, B2) | **Rejected as master.** The T reads as a hammer or drill bit; a letter made of black glassy stone suggests hollowstone can be carved or cast (RULE-005 is a public belief backed by a sealed truth); five arches in both takes (avoid counts of 5 and 9 in any brand mark); a black spiral object at word scale sits too close to a stone/shard reading. Not to be used |
| **C** | **Waterline.** Letters partly submerged, a water surface cutting the word | **Not generated.** Keeper R2.1 bans any water surface in cut 33 (only spray residue on the letters is allowed); the tide line of A carries the same idea with no water in frame |
| — | Custom face from in-world inscriptions | Folded into A: the face is the harbour-wall chisel cut. A3 is the wider, less condensed cut of the same face (light background; usable for small thumbnails, not the master) |

## 2. Rules for every use (brand bible)

1. The word is always **HOLLOWSTONE**, one line, capitals, letter-perfect. No tagline, no season number inside the mark (season / episode text goes outside the mark, in a plain face, smaller than ⅓ of the cap height).
2. **Material is granite, not hollowstone.** Pale weathered grey granite (`#B8B4AC` dry, `#5C6B72`→`#8FA3AE` wet), outline `#1C1F2A`. Never black glassy letters, never limestone, coral, reef or fossil texture.
3. **The tide line is fixed:** straight, horizontal, at about half the cap height from the baseline (y = 336 of 676 px in the 1800-px assets — `studio/art/logo/final/tide_y.txt`). It never moves up. In motion, water only drains.
4. **No glow, ever.** One natural specular glint on dry bevels is allowed in motion; no bloom, halo, rim light, light in grooves or magic light.
5. **Never with:** the stone or shard prop or anything like it (no pebble, gem, shard, cord, hole set with an object); no ring; the O counters stay empty; no circle, disc or medallion behind the word; no Spire silhouettes around it (the Concord flag uses those); no spiral device on the mark; no tapestry panel 6; no heraldic devices.
6. **No mirroring, no outline-only, no gradient fills, no metal or gold versions.** Original face, drawn for this series; not set in or modelled on any existing franchise logo or typeface.
7. Minimum size: 240 px wide on screen (thumbnails) — below that use `HOLLOWSTONE_logo_clean_alpha.png`.
8. Over the Crown Spire (cut 33): logo width 1300 px of 1920, centre y ≈ 660, crown and arches visible above it; grooves stay dark in every variant-B grade.
9. **Keeper R2.5, every carrier (incl. animated posters and social):** the tide line and the wet zone never rise; the mark is never cropped to a single letter or a single vertical stroke (L, T, N) as an icon or avatar — an icon is the whole word or `clean_alpha` whole; no rope, pile, post or figure next to the mark.
10. **No dark letters.** Below the tide line there is never any extra darkening: no part of a letter is ever darker than the master's wet zone (`#5C6B72`). Extra wetness in motion is above the tide line only.
11. **Contrast comes from the plate, never from the mark.** Behind the word the sky is kept clearly darker than the dry stone (no brighter than ~0.6 of the dry stone's luminance; in C13 a soft band −40 % behind the upper half, −60 % behind the lower half). This holds in every variant-B grade, the "day" grade above all. No glow, outline boost or recolouring of the logo.

## 3. Files (`studio/direction/refs/LOGO/`)

| File | Use |
|---|---|
| `HOLLOWSTONE_logo_master_alpha.png` | 1800×676 RGBA, painted master, transparent background — OP, posters |
| `HOLLOWSTONE_logo_master_dark_1920.png` | master on `#0B0D12`, 1920×1080 — preview, end card, social |
| `HOLLOWSTONE_logo_clean_alpha.png` | 1800×676 RGBA, flat high-contrast version (4 flat tones + white salt line + outline) — compositing over busy plates, thumbnails, keying, print |
| `HOLLOWSTONE_logo_matte.png` | white letters on black (luma matte) — `alphamerge`, masks for wipes/glints |
| `HOLLOWSTONE_logo_wetzone_matte.png` | matte of the part below the tide line — for wet/dry grading |

## 4. Motion: the reveal at 1:22.5 (cut 33 / C13), ffmpeg only, $0

Frames at 24 fps, absolute OP frame numbers (storyboard §2.1: hits sit on grid +1). v1.1: the logo lands **on** the final hit, 1981 (was 1995): INK, spray wipe and landing run together. The tail is scripted second by second (analyst #5): every half-second of the 4.5 s has its event.

| Frames | Time | Beat | Build |
|---|---|---|---|
| 1981 | 1:22.54 | last drum hit | INK 1981–1982 + torn spray wipe 1981–1992 as in the storyboard |
| 1981–1988 | 1:22.54 | **logo lands** with the wipe edge | scale 114 % → 100 % over 8 frames; the upper part (above the tide line) arrives **wet** (master darkened above the tide line only: `eq=brightness=-0.16:saturation=0.75,colorbalance=bs=0.08:bm=0.05`); below the tide line the master stays exactly as painted in every frame |
| 1981–1986 | | impact | SHAKE 6 frames (±6 px x, ±4 px y), then still |
| 1989–2004 | 1:22.88–1:23.50 | **water drains** | the wet layer's mask edge slides **down** from the cap line to the tide line (soft 10-px edge): dry pale granite appears top-down; the last soft residue above the line is gone by 2010. Below the tide line there is never any extra darkening: no part of a letter is ever darker than the master's wet zone (#5C6B72). |
| 2000–2004 | 1:23.33–1:23.5 | glint enters | (v1.4) the glint band enters from the left while the last of the drain finishes (overlap 2–4 frames, gate v1.1: acceptable) |
| 2005–2015 | 1:23.5–1:24.0 | dry + glint | the word stands dry above the line; the glint crosses it; the push and the clouds carry the motion |
| 2000–2040 | 1:23.33–1:25.0 | **glint** (v1.4; was 2016–2039) | one soft cold-white band (`#EBF2FA`, 32 % max, slanted 0.35, ~70 px wide) crosses the dry upper part left → right, masked strictly inside the letters (`lt(Y,TIDE)`); nothing outside the letters brightens: it is a specular sheen on wet stone, not a glow |
| 2020–2039 | 1:24.2–1:25.0 | drop gathers | under a lower letter, below the tide line, the drop grows |
| 2040 | 1:25.0 | **drop + drip cue** | the drop leaves the lower edge of a letter below the tide line and falls out of frame (keeper R2.1; never lands, never glows). The drop is tinted by the sky and the stone, never brighter than the dry letters, no white core. Six drops on the master stay six. Sound: one quiet drip + a low soft tap (composer, $0) — the audio-visual mark of the brand |
| 2041–2075 | 1:25.0–1:26.5 | **hold** | still letters, clouds stream past the crown, the plate push continues; no tagline, no text |
| 1980–2087 | whole cut | **push** | (v1.4) one sub-pixel push of the whole frame, linear 1.00 → 1.03 (logo and plate together) + the K17C plate +4 % linear under it; the logo has **no own scale** after the landing (gate И10: an integer logo scale makes the letters jump 1 px every ~11 frames). Was: plate +3 %, logo +1.5 % |
| 1980–2087 | whole cut | **plate under the word** | soft band on the plate only: −40 % behind the upper half, −60 % behind the lower half, smooth edges (y ≈ 250–1080, centred on the word), a touch more behind the outer letters; the logo itself is never darkened (§2 p. 10–11) |
| 2076–2087 | 1:26.5–1:27.0 | fade | picture and audio fade as in the storyboard |

Working recipe (tested on `PL-0014/D08_S1_dusk_v1.png`, crown framing): `studio/art/logo/motion/reveal_test.sh` → `reveal_test.mp4` (v1.1 script; the tracked `.mp4` is the v1 render until the artist re-renders it with one command, $0). Its t = 0 is frame 1980; the logo lands on n = 1 (no INK/wipe/K17 — the OP build supplies those). The core:

```
[logo]split=3[dry][wet0][gl0];
[wet0]eq=brightness=-0.16:saturation=0.75,colorbalance=bs=0.08:bm=0.05,
  geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='alpha(X,Y)*lt(Y,TIDE)*clip((Y-TIDE*clip((N-9)/16,0,1))/10+1,0,1)*(1-clip((N-24)/6,0,1))'[wet];
[gl0]geq=r=235:g=242:b=250:a='alpha(X,Y)*lt(Y,TIDE)*0.32*exp(-pow((X-0.35*Y-(-100+(W+400)*clip((N-20)/40,0,1)))/34,2))'[glint];
[dry][wet]overlay[l1]; [l1][glint]overlay,
  scale=w='if(lt(n,9),2*trunc(iw*(1.14-0.14*clip((n-1)/8,0,1))/2),iw)':h=-2:eval=frame[logo2]
```
(`N`/`n` counted from frame 1980; TIDE = 243 for a 1300-px logo.) `lt(Y,TIDE)` keeps the wetness above the tide line. Variant-B LUT goes on the plate, wipe and spray only; the logo keeps its own colours so the brand reads the same in every episode. The OP build of the same recipe: `direction/opening/tools/op_saga_animatic.py` (`build_title`, `plate_band`); style C v1.2: `op_saga_build_c12.py` (`build_title`, `title_logo`, modes full / textless / logo layer).

### 4.1 Vertical end card 9:16 (v1.4)

`direction/opening/tools/op_saga_vertical_v12.py`: frames 1981–2087 of the textless C13 (spray wipe + K17C plate, no logo) cropped at x = 656 (608-px window) and upscaled to 1080×1920; the logo layer rendered alone on transparent (same landing, drain, glint, drop) laid over it, the **whole word on one line**, 760 px wide, centre (540, 1173), inside the safe frame x 60–940, y 250–1500. Never a single letter, never the tower crop of a 16:9 frame (it cuts the word). Badge AI-ANIMATED top left.

## 5. Keeper check requested

*Answered 2026-11-24 (`reports/lore-saga-op-2026-11-24.md` R2.5): both confirmed, with the conditions now in §2 p. 9–11 and §4.*

- Tide line on the letters: static mark, water only drains, no marked post, no rising water (OP-5, PL-0022) — please confirm.
- Granite letters instead of black glassy stone (RULE-005 / restricted truth) — please confirm.
- *v1.2, open:* LOGO_C (§6) — the same mark in volume, the outline dropped; please confirm at full size (saga storyboard K15).

## 6. LOGO_C — the 3D version for style C (v1.2)

**Why:** the opening is now style C (`art/style_c/STYLE_BASE_C.md`); the outlined 2D master reads as a sticker over a 3D plate (marketer style-C review, p. 4). LOGO_C makes the mark an object of the same world.

**What stays (all of §2):** HOLLOWSTONE letter-perfect, one line; the chisel-cut face of A2 (same shapes, proportions, spacing); pale weathered grey granite, never black glass (RULE-005); the tide line straight and horizontal at half the cap height, wet blue-grey below with the salt crust and weed staining, dry above; water only drains, the line never rises; no glow, no rim light; the O counters empty; nothing next to or behind the mark; no cropping to one letter (R2.5) (also no single-letter 3D render, turntable or icon); contrast from the plate, never from the mark (§2 p. 11); nothing below the line darker than `#5C6B72` (§2 p. 10) — in LOGO_C measured on the letter faces; inside the cuts below the line the shadow is never darker than the shadow of the same cut above the line, the mean luma of the letters below the line is at least that of the 2D master's wet zone (≈96 of 255), and no facet of any letter is near-black (luma below 50).
**What changes:** volume (V-section bevels lit by a soft key from the upper left, soft contact shading in the cuts), **no outline** (`#1C1F2A` is not used in LOGO_C; the plate band of §2 p. 11 gives the separation).

**Generation:** NB2 edit, 1 image, up to 3 takes ($0.24 in the saga budget), prompt and acceptance in `SAGA_OP_storyboard.md` §5.3; image 1 = the accepted C anchor D01_A_C, image 2 = `HOLLOWSTONE_logo_master_dark_1920.png` (layout), image 3 = `HOLLOWSTONE_logo_clean_alpha.png` (shapes); letters on flat `#0B0D12`, the same framing as image 2. Acceptance: letter-perfect; the tide line straight and at the master's height (tide_y_C within ±2 % of the cap height of the master's line, the same y across the whole word ±3 px), else the take fails; six drops, below the line only; letters alone, no slab, block, wall or stone face behind them; no outline, glow or rim light. *v1.3 (director, gate И6):* contrast of the wet half at frame 2028 ≥ 60 (letters below the line vs the plate behind them), else the plate band behind the lower half deepens to −75 % (plate only); probe and steps in the saga storyboard §5.3.
**Matte ($0):** NB2 returns an opaque 1376×768 frame. Scale to 1920×1080 (lanczos) and align to `master_dark_1920` (phase correlation on the luma, translation + scale only). Alpha = the luma key of the letters against `#0B0D12` (the wet zone `#5C6B72` is far above the ground), OR-ed with `HOLLOWSTONE_logo_matte.png` dilated by 3 px so dark bevel cuts stay solid; edges feathered 1 px. Save `art/logo/final/HOLLOWSTONE_logo_C_alpha.png` (1800×676 crop as the master) + `tide_y_C.txt` (the measured tide line). The concept artist owns these files.
**Motion:** §4 unchanged — the wet layer, drain, glint (`lt(Y,TIDE)`), drop, plate band and push run on `HOLLOWSTONE_logo_C_alpha.png` with `TIDE` from `tide_y_C.txt` (scaled to the 1300-px logo). The wet darkening stays above the line only. LOGO_C keeps its own soft light whether or not {SIGNATURE_C} is picked for the plates (keeper R3.3).
**Fallback:** if three takes fail (spelling, line, glass look), C13 keeps the approved 2D master over the C plate with the §2 p. 11 plate band, and the keeper is told; no further paid takes.
