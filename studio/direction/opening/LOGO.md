# HOLLOWSTONE logotype — "Tidemark" (v1.1, 2026-11-24)

Owner: concept artist. Used in: OP cut 33 / SAGA OP C13 (title sting 1:22.5–1:27.0), posters, thumbnails, end card.
Assets: `studio/direction/refs/LOGO/` (copies of `studio/art/logo/final/`). Source frame: `studio/art/logo/gen/LOGO_A2_v1.png` (NB2, seed 410722).
v1.1 (director, with the keeper's R2.5 of `reports/lore-saga-op-2026-11-24.md` word for word and the investor's 1981 landing): tide line at half the cap height in the text (the asset was always there); darkening above the tide line only; the drop never brighter than the dry letters; the landing on the final hit, 1981; the keeper's conditions for every carrier (§2 p. 9–11); a darker plate under the word and a scripted tail (§4). The assets are unchanged.

## Кратко (RU)

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
| 2005–2015 | 1:23.5–1:24.0 | dry | the word stands dry above the line; the plate push and the clouds carry the motion |
| 2016–2039 | 1:24.0–1:25.0 | **glint** | one soft cold-white band (`#EBF2FA`, 32 % max, slanted 0.35, ~70 px wide) crosses the dry upper part left → right, masked strictly inside the letters (`lt(Y,TIDE)`); nothing outside the letters brightens: it is a specular sheen on wet stone, not a glow |
| 2020–2039 | 1:24.2–1:25.0 | drop gathers | under a lower letter, below the tide line, the drop grows |
| 2040 | 1:25.0 | **drop + drip cue** | the drop leaves the lower edge of a letter below the tide line and falls out of frame (keeper R2.1; never lands, never glows). The drop is tinted by the sky and the stone, never brighter than the dry letters, no white core. Six drops on the master stay six. Sound: one quiet drip + a low soft tap (composer, $0) — the audio-visual mark of the brand |
| 2041–2075 | 1:25.0–1:26.5 | **hold** | still letters, clouds stream past the crown, the plate push continues; no tagline, no text |
| 1980–2087 | whole cut | **push** | plate +3 % (as storyboard), logo +1.5 % (slight parallax, the word feels set in front of the sky) |
| 1980–2087 | whole cut | **plate under the word** | soft band on the plate only: −40 % behind the upper half, −60 % behind the lower half, smooth edges (y ≈ 250–1080, centred on the word), a touch more behind the outer letters; the logo itself is never darkened (§2 p. 10–11) |
| 2076–2087 | 1:26.5–1:27.0 | fade | picture and audio fade as in the storyboard |

Working recipe (tested on `PL-0014/D08_S1_dusk_v1.png`, crown framing): `studio/art/logo/motion/reveal_test.sh` → `reveal_test.mp4` (v1.1 script; the tracked `.mp4` is the v1 render until the artist re-renders it with one command, $0). Its t = 0 is frame 1980; the logo lands on n = 1 (no INK/wipe/K17 — the OP build supplies those). The core:

```
[logo]split=3[dry][wet0][gl0];
[wet0]eq=brightness=-0.16:saturation=0.75,colorbalance=bs=0.08:bm=0.05,
  geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='alpha(X,Y)*lt(Y,TIDE)*clip((Y-TIDE*clip((N-9)/16,0,1))/10+1,0,1)*(1-clip((N-24)/6,0,1))'[wet];
[gl0]geq=r=235:g=242:b=250:a='alpha(X,Y)*lt(Y,TIDE)*0.32*exp(-pow((X-0.35*Y-(-300+(W+600)*clip((N-36)/24,0,1)))/34,2))'[glint];
[dry][wet]overlay[l1]; [l1][glint]overlay,
  scale=w='iw*if(lt(n,9),1.14-0.14*clip((n-1)/8,0,1),1)*(1+0.015*n/108)':h=-1:eval=frame[logo2]
```
(`N`/`n` counted from frame 1980; TIDE = 243 for a 1300-px logo.) `lt(Y,TIDE)` keeps the wetness above the tide line. Variant-B LUT goes on the plate, wipe and spray only; the logo keeps its own colours so the brand reads the same in every episode. The OP build of the same recipe: `direction/opening/tools/op_saga_animatic.py` (`build_title`, `plate_band`).

## 5. Keeper check requested

*Answered 2026-11-24 (`reports/lore-saga-op-2026-11-24.md` R2.5): both confirmed, with the conditions now in §2 p. 9–11 and §4.*

- Tide line on the letters: static mark, water only drains, no marked post, no rising water (OP-5, PL-0022) — please confirm.
- Granite letters instead of black glassy stone (RULE-005 / restricted truth) — please confirm.
