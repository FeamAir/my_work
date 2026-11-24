#!/usr/bin/env python3
"""Saga OP r19 ($0): keeper R8.3 #11 / E9 on W16 — letter-like squiggles in the reed hatching (small dark components
only, outlines kept) inpainted and replaced by short vertical strokes. Still only: not carried into KW16 (see
op_saga_kw16_fix.py, REEDS = False).

  python3 -I op_saga_w16_reeds_r19.py W16.png W16_r19_reeds.png preview.png
"""
import cv2, numpy as np, sys
src, dst, prevp = sys.argv[1:4]
im = cv2.imread(src)
g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# squiggle groups (W16 1376x768): x0,y0,x1,y1, and vertical strokes to draw (x, ytop, len)
R = [((677, 505, 706, 513), [(684, 505, 6), (692, 506, 5), (700, 505, 6)]),     # "llo-den"
     ((670, 434, 690, 448), [(675, 436, 7), (684, 437, 6)]),                    # "o dr"
     ((652, 490, 677, 500), [(657, 491, 7), (664, 490, 7), (671, 491, 6)]),     # "m ll o"
     ((620, 518, 676, 530), [(626, 520, 7), (633, 519, 7), (640, 520, 6), (656, 520, 6), (664, 519, 7)]),  # "wUll o ll"
     ((697, 544, 712, 558), [(701, 546, 8), (707, 547, 7)])]                    # "IS"
dark = (g < 105).astype(np.uint8)
n, lab, stats, _ = cv2.connectedComponentsWithStats(dark, connectivity=8)
small = np.isin(lab, np.where(stats[:, cv2.CC_STAT_AREA] < 70)[0]) & (lab > 0)   # outlines are long: keep them
m = np.zeros(g.shape, np.uint8)
for (x0, y0, x1, y1), _ in R:
    m[y0:y1, x0:x1] = small[y0:y1, x0:x1].astype(np.uint8) * 255
m = cv2.dilate(m, np.ones((3, 3), np.uint8)) & ~cv2.dilate(((dark > 0) & ~small).astype(np.uint8) * 255, np.ones((2, 2), np.uint8))
out = cv2.inpaint(im, m, 3, cv2.INPAINT_TELEA)
ink = (40, 62, 58)
for _, strokes in R:
    for x, y, L in strokes:
        cv2.line(out, (x, y), (x, y + L), ink, 1, cv2.LINE_AA)
cv2.imwrite(dst, out)
z = lambda a: cv2.resize(a[400:560, 580:780], (1000, 800), interpolation=cv2.INTER_LANCZOS4)
cv2.imwrite(prevp, np.hstack([z(im), z(out)]))
