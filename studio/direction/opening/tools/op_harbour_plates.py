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

v2 (2026-11-24, gate R2 items 1 and 7): the v1 clone left a dark pointed ghost of the finial (H1) and a light
streak (H2); the v1 lamp pass left a warm halo ring, an orange bar on lamp x 801 (H2) and a blotchy blue head
on lamp x 842 (H2). v2:
  - finial: the mask is widened by 6 px and filled with a shifted copy of the same rows of the same plate
    (one dx for both plates, chosen where the source has no gulls), gain-matched per row to the flanks and
    feathered 3 px: chop texture continues, no outline. The quay parapet joints are copied the same way.
  - lamps: the head keeps its shape but is re-toned as unlit dark glass in a dark bronze frame (luma kept,
    chroma removed, no flat patch); the halo ring (all warm or bright pixels within 18 px of the head that are
    not post or frame) is inpainted from the surrounding water (OpenCV Telea).
Check: halo ring R-B excess and finial fill vs flanks are printed per plate.
"""
import os
import numpy as np
import cv2
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


FIN_PAD = 6


def finial_mask_v2(w, h):
    m = finial_mask(w, h)
    m[563:h, 474:532] = True                      # collar knobs on the quay face
    k = np.ones((2 * FIN_PAD + 1, 2 * FIN_PAD + 1), np.uint8)
    return cv2.dilate(m.astype(np.uint8), k).astype(bool)


def pick_dx(plates, m):
    """One dx for both plates: no gull, speck or bollard in the source window on either plate."""
    best = None
    for dx in list(range(-260, -70, 2)) + list(range(70, 260, 2)):
        sc = [score_dx(a, m, dx) for a in plates]
        if None in sc:
            continue
        if best is None or sum(sc) < best[0]:
            best = (sum(sc), dx)
    return best[1]


def score_dx(a, m, dx):
    ys, xs = np.nonzero(m)
    L = a.mean(2)
    med = cv2.medianBlur(np.clip(L, 0, 255).astype(np.uint8), 9).astype(float)
    sx = xs + dx
    if sx.min() < 0 or sx.max() >= a.shape[1]:
        return None
    odd = (np.abs(L[ys, sx] - med[ys, sx]) > 18).sum()      # gulls, specks, bollard tops, joints
    score = odd * 20.0
    for y in range(ys.min(), ys.max() + 1, 4):
        row = xs[ys == y]
        if row.size == 0:
            continue
        fl = np.r_[L[y, row.min() - 10:row.min() - 2], L[y, row.max() + 3:row.max() + 11]].mean()
        score += abs(L[y, row.min() + dx:row.max() + dx + 1].mean() - fl)
    return score


def paint_out_v2(a, m, dx):
    """Shifted copy of the same rows (dx), Poisson-blended into the mask (cv2.seamlessClone):
    the chop texture comes from the source, the tone comes from the mask border, so no outline or ghost."""
    src = np.roll(a, -dx, axis=1)                 # src[y, x] = a[y, x + dx]
    ys, xs = np.nonzero(m)
    y0, y1, x0, x1 = ys.min() - 2, ys.max() + 1, xs.min() - 2, xs.max() + 3
    mm = np.zeros(m.shape, np.uint8)
    mm[m] = 255
    mm[y1 - 1:, :] = 0                            # seamlessClone needs a border row inside the image
    dst = np.clip(a, 0, 255).astype(np.uint8)
    srcu = np.clip(src, 0, 255).astype(np.uint8)
    # pad by 8 px so the mask never touches the image border
    P = 8
    dstp = cv2.copyMakeBorder(dst, P, P, P, P, cv2.BORDER_REFLECT)
    srcp = cv2.copyMakeBorder(srcu, P, P, P, P, cv2.BORDER_REFLECT)
    mmp = cv2.copyMakeBorder(np.where(m, 255, 0).astype(np.uint8), P, P, P, P, cv2.BORDER_CONSTANT, value=0)
    by, bx = np.nonzero(mmp)
    bb = (bx.min(), by.min(), bx.max() - bx.min() + 1, by.max() - by.min() + 1)
    patch = srcp[bb[1]:bb[1] + bb[3], bb[0]:bb[0] + bb[2]]
    pmask = mmp[bb[1]:bb[1] + bb[3], bb[0]:bb[0] + bb[2]]
    center = (bb[0] + bb[2] // 2, bb[1] + bb[3] // 2)
    out = cv2.seamlessClone(cv2.cvtColor(patch, cv2.COLOR_RGB2BGR), cv2.cvtColor(dstp, cv2.COLOR_RGB2BGR),
                            pmask, center, cv2.NORMAL_CLONE)
    out = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)[P:-P, P:-P].astype(float)
    # the dark quay face under the parapet (y >= 562): straight shifted copy, side edges feathered
    q = np.zeros(m.shape, np.float32)
    q[562:, :] = m[562:, :]
    q = cv2.GaussianBlur(q, (0, 0), 1.5)[..., None]
    q[562:][m[562:]] = 1.0
    return out * (1 - q) + src * q


def lamps_dark_v2(a):
    """Every lamp head is redrawn as the same small unlit lantern (dark bronze cage, dark glass, cap),
    at the measured size; the glow around it is inpainted from the water; the post stays."""
    a = a.copy()
    h, w, _ = a.shape
    for cx, cy, hw, hh in LAMPS:
        R = 10 + 2 * max(hw, hh)
        y0, y1, x0, x1 = max(0, cy - R), min(h, cy + R + 1), max(0, cx - R), min(w, cx + R + 1)
        reg = a[y0:y1, x0:x1].copy()
        yy, xx = np.mgrid[y0:y1, x0:x1]
        d = np.hypot(xx - cx, yy - cy)
        ring = (d > R - 3) & (d <= R)
        L = reg.mean(2)
        bgL = L[ring].mean()
        post = (np.abs(xx - cx) <= 1) & (yy > cy + hh + 1) & (L < bgL - 5)
        hole = (d <= R - 3)
        u8 = np.ascontiguousarray(np.clip(reg, 0, 255).astype(np.uint8))
        clean = cv2.inpaint(u8, hole.astype(np.uint8) * 255, 3, cv2.INPAINT_TELEA).astype(float)
        # only the halo is replaced; plain water inside the disc stays as painted
        warm = (reg[..., 0] - reg[..., 2]) - (reg[ring][:, 0] - reg[ring][:, 2]).mean()
        halo = hole & ((warm > 2) | (L > bgL + 3))
        halo = cv2.dilate(halo.astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool) & hole
        hs = cv2.GaussianBlur(halo.astype(np.float32), (0, 0), 1.2)[..., None]
        out = reg * (1 - hs) + clean * hs
        # post back (it is dark, it is not light)
        out[post] = reg[post]
        # lantern: body (2hw+1) x (2hh+1), a cap of width hw above, a 1 px darker cage outline
        body = (np.abs(xx - cx) <= hw) & (np.abs(yy - cy) <= hh)
        cap = (np.abs(xx - cx) <= max(1, hw // 2)) & (yy >= cy - hh - 2) & (yy < cy - hh)
        inner = (np.abs(xx - cx) <= hw - 1) & (np.abs(yy - cy) <= hh - 1)
        glass = np.array([44, 46, 46], float)
        cage = np.array([40, 35, 30], float)
        out[body | cap] = cage
        out[inner] = glass
        if hw >= 5:                                   # near lamps: a vertical cage bar in the middle
            out[inner & (xx == cx)] = cage
        out[(yy == cy + hh + 1) & (np.abs(xx - cx) <= hw - 1)] = cage   # bottom collar onto the post
        lan = cv2.dilate((body | cap).astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool)
        soft = cv2.GaussianBlur(out.astype(np.float32), (0, 0), 0.6)
        out[lan] = soft[lan]
        a[y0:y1, x0:x1] = out
    return a


def halo_report(a, tag):
    out = []
    for cx, cy, hw, hh in LAMPS:
        yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
        d = np.hypot(xx - cx, yy - cy)
        ring = (d >= 8) & (d <= 14) & ~((np.abs(xx - cx) <= 1) & (yy > cy)) & ~((np.abs(xx - cx) <= hw + 2) & (np.abs(yy - cy) <= hh + 4))
        bg = (d >= 22) & (d <= 28)
        rb = lambda s: float((a[s][:, 0] - a[s][:, 2]).mean())
        out.append(f"x{cx}: ring R-B {rb(ring):+.1f} vs bg {rb(bg):+.1f}")
    print(tag, "halo:", "; ".join(out))


def fill_report(a, m, tag):
    L = a.mean(2)
    diffs = []
    for y in range(470, 555, 5):
        xs = np.nonzero(m[y])[0]
        if xs.size == 0:
            continue
        inner = L[y, xs[0] + 6:xs[-1] - 5].mean()
        flank = np.r_[L[y, xs[0] - 14:xs[0] - 2], L[y, xs[-1] + 3:xs[-1] + 15]].mean()
        diffs.append(inner - flank)
    print(tag, f"finial fill - flanks (luma, rows 470-555): mean {np.mean(diffs):+.2f}, worst {max(diffs, key=abs):+.2f}")


def main():
    os.makedirs(OUT, exist_ok=True)
    checks = []
    names = (("H1", "D09_H1_late-aft_v1.png"), ("H2", "D09_H2_glass_v1.png"))
    srcs = {t: Image.open(f"{SRC}/{n}").convert("RGB").crop(CROP) for t, n in names}
    m = finial_mask_v2(*srcs["H1"].size)
    dx = pick_dx([np.asarray(srcs[t], float) for t, _ in names], m)
    print("finial fill source dx (both plates):", dx)
    for tag, name in names:
        src = srcs[tag]
        a = np.asarray(src, float)
        b = glows_out(lamps_dark_v2(paint_out_v2(a, m, dx)))
        fill_report(b, m, tag)
        halo_report(b, tag)
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
