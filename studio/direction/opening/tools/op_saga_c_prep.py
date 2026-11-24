#!/usr/bin/env python3
"""Saga OP v2.4, style C: $0 local preparation of two NB2 input images (gate 2026-11-24, B1/R3.2 and B2).

  python3 -I op_saga_c_prep.py alley      # keeper R3.2: f_alley.png -> f_alley_patched.png
  python3 -I op_saga_c_prep.py d01a       # gate B2: plates/D01_A_op.png (768x1376, vertical) -> D01_A_op_169.png (1376x768)
  python3 -I op_saga_c_prep.py all        # both + check sheets

alley (R3.2, keeper text): the double gate and its bars at the end of the lane replaced by plain brick wall (cloned
      from the plain wall on both sides of it, same rows, so the mist gradient matches), the ring knocker on the left
      door removed (cloned from the planks above it), the lantern glass darkened to unlit (bright pane pixels pulled
      down to a dull dark grey), the column of notches on the left door frame removed (dark marks on the frame board
      inpainted; v2.5 R5.4: down to y 532), lantern glass v2.5 R5.4: flat dark grey-teal below the wall's tone. Output: output/style_test/f_alley_patched.png + output/style_test/f_alley_patched_check.png
      (before/after, details at 2x). The keeper checks it at full size before the alley_C call.

d01a (gate B2): the NB2 call runs at 16:9, the v1.4 plate is vertical. Two steps:
  1. OpenCV: canon v0.10 / W13: two Spires on the hill, the Sluice Spire at the south-west foot among the stilt-houses.
     The plate has all three on the hilltop; the right-hand tower is cut out (inpainted over sky, palace and dome)
     and set back in at 0.85x, lower and to the right, its foot in the mist among the first stilt-houses in front of
     the dike (the shorter third tower of v1.4 F10 / W13).
  2. ffmpeg: crop y 110-1010 (crown arches of the Crown Spire down to the first rows of the Lows), scale to 768 high,
     pad to 1376x768 centred, the side bands filled by `fillborders=mode=smear` and blurred (`gblur`), so they carry
     only sky / hill / dike / Lows tone bands and no copy of any tower. The prompt (D01_A_C, storyboard v2.4 §5.1)
     says the soft sides are placeholders to be built as more of the same city.
  Output: output/opening/plates/D01_A_op_169.png (+ _check.png: source, step 1, result).
"""
import os
import subprocess
import sys

import cv2
import numpy as np

ROOT = "/home/user/my_work"
ALLEY_IN = f"{ROOT}/output/style_test/f_alley.png"
ALLEY_OUT = f"{ROOT}/output/style_test/f_alley_patched.png"
PLATE_IN = f"{ROOT}/output/opening/plates/D01_A_op.png"
PLATE_MID = f"{ROOT}/output/opening/plates/D01_A_op_sluice.png"
PLATE_OUT = f"{ROOT}/output/opening/plates/D01_A_op_169.png"


def feather(mask, r):
    m = mask.astype(np.float32)
    if r > 0:
        m = cv2.GaussianBlur(m, (0, 0), r)
    return np.clip(m, 0, 1)[..., None]


def clone(img, src_box, dx, dy, r=2):
    """Copy img[src_box] to the box shifted by (dx, dy), feathered edges."""
    x0, y0, x1, y1 = src_box
    out = img.copy()
    patch = img[y0:y1, x0:x1].astype(np.float32)
    m = np.zeros((y1 - y0, x1 - x0), np.float32)
    m[r:-r or None, r:-r or None] = 1
    a = feather(m, r)
    dst = out[y0 + dy:y1 + dy, x0 + dx:x1 + dx].astype(np.float32)
    out[y0 + dy:y1 + dy, x0 + dx:x1 + dx] = (patch * a + dst * (1 - a)).astype(np.uint8)
    return out


def alley():
    img = cv2.imread(ALLEY_IN)
    assert img is not None and img.shape[:2] == (768, 1376), ALLEY_IN
    src = img.copy()
    # 1. gate (x 655-755, y 356-450) -> plain brick: left half from the wall at x 575-625, right half from x 785-835
    img = clone(img, (575, 352, 627, 420), 80, 0)
    img = clone(img, (783, 352, 835, 420), -80, 0)
    low = np.zeros(img.shape[:2], np.uint8)          # the gate's foot in the mist (y 414-452): no wall source free of
    low[414:452, 652:758] = 255                       # the plank-walk posts at those rows, so it is inpainted
    img = cv2.inpaint(img, low, 9, cv2.INPAINT_TELEA)
    # 2. ring knocker on the left door (x 88-120, y 410-465) -> planks above (dy -60)
    img = clone(img, (86, 348, 122, 407), 0, 62)
    # 3. notches on the left door frame board (x 160-197, y 212-512): dark marks inpainted
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.int16)
    loc = cv2.medianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 21).astype(np.int16)
    mask = np.zeros(g.shape, np.uint8)
    roi = (slice(212, 532), slice(162, 196))      # v2.5 keeper R5.4 p. 1: down to y 532 (the last mark at y 506-522)
    mask[roi] = ((loc[roi] - g[roi]) > 10).astype(np.uint8) * 255
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8))
    img = cv2.inpaint(img, mask, 6, cv2.INPAINT_TELEA)
    # 4. lantern glass (x 1020-1078, y 130-202): bright pane pixels -> dull dark grey (unlit)
    box = img[130:202, 1020:1078].astype(np.float32)
    lum = box.mean(axis=2, keepdims=True)
    # v2.5 keeper R5.4 p. 2: the v2.4 grey (64, 66, 60) read warm pink against the teal wall. Now a flat dark
    # grey-teal, darker than the house wall behind it (BGR ~45, 45, 25, luma ~37), no red, no highlight inside.
    k = np.clip((lum - 45) / 15, 0, 1)
    dark = np.array([33, 32, 20], np.float32)  # BGR: dark grey-teal (unlit glass), luma ~28
    grey = np.repeat(lum, 3, axis=2) * 0.03 + dark * 0.97
    img[130:202, 1020:1078] = (box * (1 - k) + grey * k).astype(np.uint8)
    # v2.5 R5.4: the top strip of the right pane (x 1041-1068, y 137-146, luma 40-45) was left lighter than the wall
    st = img[137:147, 1041:1068].astype(np.float32)
    sl = st.mean(axis=2, keepdims=True)
    ks = np.clip((sl - 33) / 6, 0, 1)
    img[137:147, 1041:1068] = (st * (1 - ks) + dark * ks).astype(np.uint8)
    cv2.imwrite(ALLEY_OUT, img)
    # check sheet: before/after full, then the four details at 2x
    det = [(600, 330, 820, 470), (60, 200, 220, 520), (990, 100, 1110, 220)]
    rows = [np.hstack([src, img])]
    for x0, y0, x1, y1 in det:
        a = cv2.resize(src[y0:y1, x0:x1], None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
        b = cv2.resize(img[y0:y1, x0:x1], None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
        rows.append(np.hstack([a, b]))
    w = max(r.shape[1] for r in rows)
    sheet = np.vstack([cv2.copyMakeBorder(r, 4, 4, 0, w - r.shape[1], cv2.BORDER_CONSTANT, value=(20, 20, 20)) for r in rows])
    cv2.imwrite(ALLEY_OUT[:-4] + "_check.png", sheet)
    print("->", ALLEY_OUT)


def d01a():
    img = cv2.imread(PLATE_IN)
    assert img is not None and img.shape[:2] == (1376, 768), PLATE_IN
    src = img.copy()
    # the right-hand tower on the hilltop (crown y 284, foot y 562, x 496-606)
    poly = np.array([(511, 282), (592, 282), (607, 470), (606, 564), (494, 564), (499, 470)], np.int32)
    tmask = np.zeros(img.shape[:2], np.uint8)
    cv2.fillPoly(tmask, [poly], 255)
    # tower pixels to move: inside the outline, darker than the sky (the arches keep their sky gaps), above y 525
    # (below that it merges with palace and dome)
    tower = src[282:525, 494:607].copy()
    lum = cv2.cvtColor(tower, cv2.COLOR_BGR2GRAY)
    talpha = (tmask[282:525, 494:607] > 0).astype(np.float32)
    talpha[:40][lum[:40] > 175] = 0                  # only the sky gaps between the crown arches stay open
    talpha = cv2.GaussianBlur(talpha, (0, 0), 0.8)
    fade = np.ones(talpha.shape[0], np.float32)
    fade[-45:] = np.linspace(1, 0, 45)              # the foot fades into the mist of the Lows
    talpha = talpha * fade[:, None]
    # remove it: each row of the hole is filled by a linear blend between the pixels just left and right of it
    # (open sky above the dome; palace stone -> dome below), plus a little of the plate's own grain
    hole = cv2.dilate(tmask, np.ones((9, 9), np.uint8))
    fill = img.astype(np.float32).copy()
    rng = np.random.default_rng(7)
    for y in np.where(hole.any(axis=1))[0]:
        xs = np.where(hole[y] > 0)[0]
        xl, xr = xs.min() - 2, xs.max() + 2
        L = img[y, xl - 3:xl].astype(np.float32).mean(0)
        R = img[y, xr:xr + 3].astype(np.float32).mean(0)
        t = ((xs - xl) / (xr - xl))[:, None]
        fill[y, xs] = L * (1 - t) + R * t + rng.normal(0, 1.5, (len(xs), 1))
    a = feather(hole > 0, 2)
    img = (fill * a + img * (1 - a)).clip(0, 255).astype(np.uint8)
    # set it back in at 0.85x, foot at y 885 among the first stilt-houses, centre x 700 (right, in front of the dike)
    s = 0.85
    tw = cv2.resize(tower, None, fx=s, fy=s, interpolation=cv2.INTER_AREA).astype(np.float32)
    ta = cv2.resize(talpha, (tw.shape[1], tw.shape[0]), interpolation=cv2.INTER_AREA)[..., None]
    # the v1.4 plate lit this tower pale; the Spire is glassy black (OP-4): darken, plus a touch of the Lows' haze
    tw = tw * 0.42 + np.array([118, 122, 112], np.float32) * 0.12
    y1, cx = 885, 700
    y0, x0 = y1 - tw.shape[0], cx - tw.shape[1] // 2
    reg = img[y0:y1, x0:x0 + tw.shape[1]].astype(np.float32)
    img[y0:y1, x0:x0 + tw.shape[1]] = (tw * ta + reg * (1 - ta)).astype(np.uint8)
    cv2.imwrite(PLATE_MID, img)
    # ffmpeg: crop 768x900 from y 110, scale to 768 high, pad centred to 1376x768, smear + blur the side bands
    h = 768
    w = int(round(768 * h / 900 / 2)) * 2           # 656
    pad = (1376 - w) // 2                             # 360
    fc = (f"[0:v]crop=768:900:0:110,scale={w}:{h}:flags=lanczos,pad=1376:{h}:{pad}:0,"
          f"fillborders=left={pad}:right={1376 - w - pad}:mode=smear,split[a][b];"
          f"[a]gblur=sigma=22[bl];[b]null[sharp];[bl][sharp]hstack,format=rgb24")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", PLATE_MID, "-filter_complex", fc, "-frames:v", "1", PLATE_OUT],
                   check=True)
    both = cv2.imread(PLATE_OUT)                      # [blurred | sharp] side by side
    bl, sh = both[:, :1376], both[:, 1376:]
    ramp = np.zeros(1376, np.float32)                 # sharp centre, 48-px feathered seams into the soft sides
    ramp[pad:pad + w] = 1
    ramp = np.convolve(ramp, np.ones(48) / 48, mode="same")[None, :, None]
    out = (sh * ramp + bl * (1 - ramp)).astype(np.uint8)
    cv2.imwrite(PLATE_OUT, out)
    assert out.shape[:2] == (768, 1376), out.shape
    a = cv2.resize(src, (429, 768), interpolation=cv2.INTER_AREA)
    b = cv2.resize(img, (429, 768), interpolation=cv2.INTER_AREA)
    sheet = np.hstack([a, np.full((768, 6, 3), 20, np.uint8), b, np.full((768, 6, 3), 20, np.uint8), out])
    cv2.imwrite(PLATE_OUT[:-4] + "_check.png", sheet)
    print("->", PLATE_OUT, out.shape[1], "x", out.shape[0])


if __name__ == "__main__":
    job = sys.argv[1] if len(sys.argv) > 1 else "all"
    if job in ("alley", "all"):
        alley()
    if job in ("d01a", "all"):
        d01a()
