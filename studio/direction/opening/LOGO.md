# HOLLOWSTONE logotype — "Tidemark" (v1, 2026-11-24)

Owner: concept artist. Used in: OP cut 33 / SAGA OP C13 (title sting 1:22.5–1:27.0), posters, thumbnails, end card.
Assets: `studio/direction/refs/LOGO/` (copies of `studio/art/logo/final/`). Source frame: `studio/art/logo/gen/LOGO_A2_v1.png` (NB2, seed 410722).

## Кратко (RU)

- Логотип — **«Приливная отметка»**: слово HOLLOWSTONE как надпись, вырубленная резцом в выветренном граните портовой стены. Одна прямая линия прилива пересекает всё слово на ⅓ высоты букв: ниже — мокрый сине-серый камень с солевой коркой и следами водорослей, выше — сухой светлый гранит. Название стиля сериала («Tidemark») становится знаком.
- Буквы проверены побуквенно: H-O-L-L-O-W-S-T-O-N-E.
- Появление на 1:22.5: логотип приходит **целиком мокрым**, вода **уходит** сверху вниз до линии прилива (отлив, вода никогда не поднимается), по сухим граням проходит один естественный блик, лёгкий наезд, держим без слогана. Всё в ffmpeg за $0. Тест: `studio/art/logo/motion/reveal_test.mp4`.

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
3. **The tide line is fixed:** straight, horizontal, at about ⅓ of the cap height from the baseline (y = 336 of 676 px in the 1800-px assets — `studio/art/logo/final/tide_y.txt`). It never moves up. In motion, water only drains.
4. **No glow, ever.** One natural specular glint on dry bevels is allowed in motion; no bloom, halo, rim light, light in grooves or magic light.
5. **Never with:** the stone or shard prop or anything like it (no pebble, gem, shard, cord, hole set with an object); no ring; the O counters stay empty; no circle, disc or medallion behind the word; no Spire silhouettes around it (the Concord flag uses those); no spiral device on the mark; no tapestry panel 6; no heraldic devices.
6. **No mirroring, no outline-only, no gradient fills, no metal or gold versions.** Original face, drawn for this series; not set in or modelled on any existing franchise logo or typeface.
7. Minimum size: 240 px wide on screen (thumbnails) — below that use `HOLLOWSTONE_logo_clean_alpha.png`.
8. Over the Crown Spire (cut 33): logo width 1300 px of 1920, centre y ≈ 660, crown and arches visible above it; grooves stay dark in every variant-B grade.

## 3. Files (`studio/direction/refs/LOGO/`)

| File | Use |
|---|---|
| `HOLLOWSTONE_logo_master_alpha.png` | 1800×676 RGBA, painted master, transparent background — OP, posters |
| `HOLLOWSTONE_logo_master_dark_1920.png` | master on `#0B0D12`, 1920×1080 — preview, end card, social |
| `HOLLOWSTONE_logo_clean_alpha.png` | 1800×676 RGBA, flat high-contrast version (4 flat tones + white salt line + outline) — compositing over busy plates, thumbnails, keying, print |
| `HOLLOWSTONE_logo_matte.png` | white letters on black (luma matte) — `alphamerge`, masks for wipes/glints |
| `HOLLOWSTONE_logo_wetzone_matte.png` | matte of the part below the tide line — for wet/dry grading |

## 4. Motion: the reveal at 1:22.5 (cut 33 / C13), ffmpeg only, $0

Frames at 24 fps, absolute OP frame numbers (storyboard §2.1: hits sit on grid +1). Everything before 1995 (INK 1981–1982, spray wipe 1983–1994) is unchanged.

| Frames | Time | Beat | Build |
|---|---|---|---|
| 1981 | 1:22.54 | last drum hit | INK + torn spray wipe as in the storyboard |
| 1995–2002 | 1:23.13 | **logo lands** with the wipe edge | scale 114 % → 100 % over 8 frames; the whole word arrives **wet** (master darkened: `eq=brightness=-0.16:saturation=0.75,colorbalance=bs=0.08:bm=0.05`) |
| 1995–2000 | | impact | SHAKE 6 frames (±6 px x, ±4 px y), then still |
| 2003–2027 | 1:23.46–1:24.46 | **water drains** | the wet layer's mask edge slides **down** from the cap line to the tide line (soft 10-px edge): dry pale granite appears top-down. Below the tide line the extra wetness fades out 2027–2040, leaving the master's own tidemark |
| 2010–2034 | 1:23.75–1:24.75 | **glint** | one soft cold-white band (`#EBF2FA`, 32 % max, slanted 0.35, ~70 px wide) crosses the dry upper part left → right, masked strictly inside the letters (`lt(Y,TIDE)`); nothing outside the letters brightens: it is a specular sheen on wet stone, not a glow |
| 1980–2087 | whole cut | **push** | plate +3 % (as storyboard), logo +1.5 % (slight parallax, the word feels set in front of the sky) |
| 2040 | 1:25.0 | drop | the storyboard's drop leaves the lower edge of a letter below the tide line and falls out of frame (keeper R2.1; never lands, never glows) |
| 2040–2075 | 1:25.0–1:26.5 | **hold** | still letters, clouds stream past the crown; no tagline, no text |
| 2076–2087 | 1:26.5–1:27.0 | fade | picture and audio fade as in the storyboard |

Working recipe (tested on `PL-0014/D08_S1_dusk_v1.png`, crown framing): `studio/art/logo/motion/reveal_test.sh` → `reveal_test.mp4`. Its t = 0 is frame 1980; it starts at the logo landing (no INK/wipe/K17 — the OP build supplies those). The core:

```
[logo]split=3[dry][wet0][gl0];
[wet0]eq=brightness=-0.16:saturation=0.75,colorbalance=bs=0.08:bm=0.05,
  geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='alpha(X,Y)*clip((Y-TIDE*clip((N-23)/24,0,1))/10+1,0,1)*(1-gte(Y,TIDE)*clip((N-47)/13,0,1))'[wet];
[gl0]geq=r=235:g=242:b=250:a='alpha(X,Y)*lt(Y,TIDE)*0.32*exp(-pow((X-0.35*Y-(-300+(W+600)*clip((N-30)/24,0,1)))/34,2))'[glint];
[dry][wet]overlay[l1]; [l1][glint]overlay,
  scale=w='iw*if(lt(n,23),1.14-0.14*clip((n-15)/8,0,1),1)*(1+0.015*n/108)':h=-1:eval=frame[logo2]
```
(`N`/`n` counted from frame 1980; TIDE = 243 for a 1300-px logo.) Variant-B LUT goes on the plate, wipe and spray only; the logo keeps its own colours so the brand reads the same in every episode.

## 5. Keeper check requested

- Tide line on the letters: static mark, water only drains, no marked post, no rising water (OP-5, PL-0022) — please confirm.
- Granite letters instead of black glassy stone (RULE-005 / restricted truth) — please confirm.
