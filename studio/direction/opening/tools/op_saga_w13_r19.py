#!/usr/bin/env python3
"""Saga OP r19 ($0): keeper R8.1 on W13 — the ship under the shorter (Sluice) tower painted out (water inpainted with
horizontal grain), the tower's body carried down to a level dark foot on the shore (no opening), grass bank continued.

  python3 -I op_saga_w13_r19.py output/opening/saga_c/frames/W13_t1_p.png output/opening/saga_c/frames/W13_t1_p2.png
"""
import numpy as np, cv2, sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
a8 = np.asarray(Image.open(src).convert("RGB"))
a = a8.astype(np.float32)
H, W = a.shape[:2]
rng = np.random.default_rng(13)
FOOT = 397
def shore(x):   # water line under the tower: y of the last land row
    if x < 862: return 401 + int(round(1.5 * np.sin((x - 790) / 7.0)))
    return int(round(401 - (x - 862) * 0.8))
# 1) ship, mast and their reflections -> inpaint water, then add water grain
m = np.zeros((H, W), np.uint8)
m[398:446, 796:848] = 255; m[384:398, 808:831] = 255
o8 = cv2.inpaint(np.ascontiguousarray(a8), m, 6, cv2.INPAINT_TELEA)
o = o8.astype(np.float32)
# smooth the inpaint with a horizontal blur (water is streaky horizontally) and add grain
reg = o[384:446, 790:854]
reg = cv2.GaussianBlur(reg, (0, 0), sigmaX=6, sigmaY=1.2)
grain = cv2.GaussianBlur(rng.normal(0, 1, reg.shape[:2]).astype(np.float32), (0, 0), sigmaX=4, sigmaY=0.6)
reg = reg + grain[..., None] * 9
mm = cv2.GaussianBlur((m[384:446, 790:854] > 0).astype(np.float32), (0, 0), 1.5)[..., None]
o[384:446, 790:854] = o[384:446, 790:854] * (1 - mm) + reg * mm
# 2) land strip: shore of grass/earth under the tower, matching the grass at the wall foot
gl = np.array([112, 111, 70], np.float32)
noise = (cv2.GaussianBlur(rng.normal(0, 1, (H, W)).astype(np.float32), (0, 0), 1.0) * 16 +
         cv2.GaussianBlur(rng.normal(0, 1, (H, W)).astype(np.float32), (0, 0), 4.0) * 22)
orig_water = (a[:, :, 2] > a[:, :, 0] + 4); orig_water[398:, :] |= (m[398:, :] > 0)
for x in range(796, 872):
    top = 380
    for y in range(top, shore(x) + 1):
        if not orig_water[y, x] and not (826 <= x <= 853 and y >= 376): continue
        k = 1.0 - 0.18 * max(0, (y - (shore(x) - 3))) / 3   # damp earth toward the water
        c = gl * k + noise[y, x]
        pass
        o[y, x] = c
    o[shore(x) + 1, x] = o[shore(x) + 1, x] * 0.8      # thin wet line
# soften seams of the land patch
lm = np.zeros((H, W), np.float32)
for x in range(796, 872):
    lm[(384 if x > 812 else 392):shore(x) + 2, x] = 1
lmb = cv2.GaussianBlur(lm, (0, 0), 1.0)[..., None]
# grass right of the tower continued down to the shore (mirror the bank x 858-870)
for y in range(372, 399):
    for x in range(846, 858):
        o[y, x] = a[y if y < 386 else 383 - (y - 386) % 8, 858 + (x - 846)] * 0.6 + o[y, x] * 0.4
# 3) tower body continued to a level dark foot on the land
tex = a[350:380]
for y in range(372, FOOT + 1):
    l = 829.0 - (y - 330) * 0.045; r = 840.0 + (y - 330) * 0.14
    li, ri = int(np.floor(l)), int(np.ceil(r))
    for x in range(li, ri + 1):
        cov = min(1.0, max(0.0, x + 1 - l)) * min(1.0, max(0.0, r + 1 - x))
        t = tex[(y - 350) % 30, min(max(x, 830), 846)]
        if y >= FOOT - 2: t = np.array([34, 33, 37], np.float32)   # plain dark foot, no opening
        o[y, x] = o[y, x] * (1 - cov) + t * cov
# shadow of the tower on the land to the right
for y in range(FOOT - 3, FOOT + 3):
    for x in range(850, 864):
        o[y, x] *= 0.82 + 0.012 * (x - 850)
out = np.clip(o, 0, 255).astype(np.uint8)
Image.fromarray(out).save(dst)
