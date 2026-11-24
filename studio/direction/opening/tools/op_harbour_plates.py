#!/usr/bin/env python3
"""S1 OP, keeper R2.5 / gate C2: prepare the two harbour plates for K13 and the glass (cuts 31-32b). $0, local only.

  python3 -I op_harbour_plates.py

For BOTH D09_H1_late-aft and D09_H2_glass, with the SAME geometry (pixel for pixel):
  1. crop to the top 74 %: x 179-1197, y 0-572 (1018x572): dark arch, side finials and near quay out;
  2. paint out the tip of the central finial left at the bottom edge (one fixed mask; fill = horizontal
     clone from both sides of the mask, cross-faded; identical mask and method on both plates);
  3. pier lamps dark (OP-3): the 6 lamp heads in the crop are turned to unlit dark glass, their warm halo
     is neutralised, and the warm reflections on the wet pier tops are replaced by the local median.
Output: output/opening/plates/D09_H1_op.png, D09_H2_op.png (+ _check.png side by side, 3x on the edits).
"""
import os
import numpy as np
from PIL import Image, ImageFilter

ROOT = "/home/user/my_work"
SRC = f"{ROOT}/studio/direction/refs/PL-0018"
OUT = f"{ROOT}/output/opening/plates"
CROP = (179, 0, 1197, 572)          # keeper R2.5
# finial tip in crop coordinates: apex (502, 478); at the bottom edge (y 571) it spans x 479-525 (+collar)
APEX, BASE_Y, BASE_L, BASE_R, PAD = (502, 478), 571, 477, 527, 3
# lamp heads (crop coords, centre x, centre y, half-w, half-h) and warm pier-top reflections (x0, y0, x1, y1)
LAMPS = [(79, 280, 4, 5), (159, 236, 4, 5), (842, 232, 4, 5), (908, 268, 4, 5), (307, 477, 6, 8), (801, 477, 6, 8)]  # warmest pixel, measured
GLOWS = [(140, 240, 185, 275), (60, 285, 100, 320), (815, 270, 870, 310), (880, 325, 925, 365), (985, 395, 1018, 440),
         (285, 490, 330, 520), (780, 490, 825, 520)]


def finial_mask(w, h):
    m = np.zeros((h, w), bool)
    for y in range(APEX[1], h):
        f = (y - APEX[1]) / max(1, BASE_Y - APEX[1])
        xl = APEX[0] - f * (APEX[0] - BASE_L) - PAD
        xr = APEX[0] + f * (BASE_R - APEX[0]) + PAD
        m[y, int(np.floor(xl)):int(np.ceil(xr)) + 1] = True
    return m


def paint_out(a, m):
    a = a.copy()
    for y in np.nonzero(m.any(1))[0]:
        xs = np.nonzero(m[y])[0]
        xl, xr = xs[0], xs[-1]
        span = xr - xl + 1
        ref = np.median(a[y, max(0, xl - 3 * span):xr + 3 * span].mean(1))
        for x in range(xl, xr + 1):
            t = (x - xl + 0.5) / span
            left = a[y, x - span]           # clone from the left neighbour strip
            right = a[y, x + span]          # clone from the right neighbour strip
            if np.abs(a[max(0, y - 3):y + 4, x - span - 2:x - span + 3].mean(2) - ref).max() > 14:           # a gull in the source strip: take the other side
                left = right
            if np.abs(a[max(0, y - 3):y + 4, x + span - 2:x + span + 3].mean(2) - ref).max() > 14:
                right = left
            a[y, x] = (1 - t) * left + t * right
    return a


def lamps_dark(a):
    a = a.copy()
    h, w, _ = a.shape
    for cx, cy, hw, hh in LAMPS:
        R = 4 * max(hw, hh)
        y0, y1, x0, x1 = max(0, cy - R), min(h, cy + R), max(0, cx - R), min(w, cx + R)
        yy, xx = np.mgrid[y0:y1, x0:x1]
        d = np.hypot((xx - cx) / R, (yy - cy) / R)
        bg = a[y0:y1, x0:x1][(d > 0.8) & (d < 1.0)].mean(0)      # colour of the surroundings
        # 1. the head: pixels brighter and warmer than the surroundings become unlit dark glass
        hy0, hy1, hx0, hx1 = cy - hh - 2, cy + hh + 3, cx - hw - 2, cx + hw + 3
        reg = a[hy0:hy1, hx0:hx1]
        lum = reg.mean(2, keepdims=True)
        warm = reg[..., 0:1] - reg[..., 2:3]
        rel = warm - (bg[0] - bg[2])
        top = max(10.0, float(rel.max()))
        sel = np.clip((rel - 0.35 * top) / (0.25 * top), 0, 1) * np.clip((lum - bg.mean() + 15) / 25, 0, 1)
        dark = np.array([46, 52, 56], float)
        a[hy0:hy1, hx0:hx1] = reg * (1 - sel) + dark * sel
        # 2. halo outside the head: pull the warm excess back to the surroundings, fading to 0 at R
        reg = a[y0:y1, x0:x1]
        k = np.clip(1.0 - d, 0, 1)[..., None]
        excess = np.clip((reg[..., 0:1] - reg[..., 2:3]) - (bg[0] - bg[2]), 0, None) / 40.0
        bright = np.clip((reg.mean(2, keepdims=True) - bg.mean()) / 30, 0, 1)
        sel = k * np.clip(excess, 0, 1) * bright
        a[y0:y1, x0:x1] = reg * (1 - sel) + bg * sel
    return a


def glows_out(a):
    a = a.copy()
    img = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    for x0, y0, x1, y1 in GLOWS:
        pad = 12
        box = (max(0, x0 - pad), max(0, y0 - pad), min(img.width, x1 + pad), min(img.height, y1 + pad))
        med = np.asarray(img.crop(box).filter(ImageFilter.MedianFilter(13)), float)
        reg = a[box[1]:box[3], box[0]:box[2]]
        lum, mlum = reg.mean(2), med.mean(2)
        warm = (reg[..., 0] - reg[..., 2]) - (med[..., 0] - med[..., 2])
        sel = np.clip(((lum - mlum) - 6) / 25, 0, 1) * np.clip((warm + 4) / 20, 0, 1)
        inner = np.zeros_like(sel)
        inner[y0 - box[1]:y1 - box[1], x0 - box[0]:x1 - box[0]] = 1
        sel = (sel * inner)[..., None]
        a[box[1]:box[3], box[0]:box[2]] = reg * (1 - sel) + med * sel
    return a


def main():
    os.makedirs(OUT, exist_ok=True)
    checks = []
    for tag, name in (("H1", "D09_H1_late-aft_v1.png"), ("H2", "D09_H2_glass_v1.png")):
        src = Image.open(f"{SRC}/{name}").convert("RGB").crop(CROP)
        a = np.asarray(src, float)
        m = finial_mask(a.shape[1], a.shape[0])
        b = glows_out(lamps_dark(paint_out(a, m)))
        out = Image.fromarray(np.clip(b, 0, 255).astype(np.uint8))
        out.save(f"{OUT}/D09_{tag}_op.png")
        # check sheet: before / after, finial area and two lamp areas at 3x
        tiles = [(420, 420, 600, 572), (40, 210, 200, 330), (780, 200, 1018, 440), (260, 440, 360, 572)]
        row = Image.new("RGB", (4 * 360, 2 * 300))
        for i, t in enumerate(tiles):
            row.paste(src.crop(t).resize((360, 300)), (i * 360, 0))
            row.paste(out.crop(t).resize((360, 300)), (i * 360, 300))
        checks.append(row)
        print(tag, out.size, "finial mask px:", int(m.sum()))
    sheet = Image.new("RGB", (1440, 1200))
    for i, r in enumerate(checks):
        sheet.paste(r, (0, i * 600))
    sheet.save(f"{OUT}/D09_op_check.png")


if __name__ == "__main__":
    main()
