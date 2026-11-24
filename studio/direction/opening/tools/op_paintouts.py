#!/usr/bin/env python3
"""S1 OP, gate R2 free fix 9 ($0, local only): crack paint-outs for cuts 02 and 05, tier tints for cut 24.

  python3 -I op_paintouts.py

  02  refs/PL-0004/D01_A_dawn-ebb_v1.png -> output/opening/plates/D01_A_op.png
      every crack line on all three Spires painted out (OP-5): thin dark features inside hand-drawn crack zones,
      minus the long groove lines (line openings at 5-35 deg, the "/" grooves stay), inpainted (Telea).
  05  output/S01E01/animatic/frames/sc06-sh010_a.png -> output/opening/plates/sc06_wheel_op.png
      crack lines on the great wall behind the wheel painted out (the dike reads intact, OP-5): thin dark wiggly
      features on the pale wall inside wall polygons, minus long straight lines (joints, beams), minus ink outlines.
  24  refs/M-MAP/E05_map_base_v1.png -> output/opening/plates/E05_map_tints_op.png
      three tier tints (Steps gold, Mids sage, Lows slate) as soft multiply washes on the land only; no IX wash,
      no fourth tint, no legend, no text, nothing on the compass or cartouches (OP-5, OP-13).
"""
import os
import numpy as np
import cv2
from PIL import Image

ROOT = "/home/user/my_work"
REF = f"{ROOT}/studio/direction/refs"
OUT = f"{ROOT}/output/opening/plates"


def line_k(ang, ln):
    kk = np.zeros((ln, ln), np.uint8)
    c = ln // 2
    dx, dy = np.cos(np.radians(ang)), -np.sin(np.radians(ang))
    cv2.line(kk, (int(round(c - dx * c)), int(round(c - dy * c))), (int(round(c + dx * c)), int(round(c + dy * c))), 1, 1)
    return kk


def keep_components(m, min_px):
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    out = np.zeros_like(m)
    for i in range(1, n):
        if st[i, 4] >= min_px:
            out[lab == i] = 1
    return out


def spires_02():
    a = np.asarray(Image.open(f"{REF}/PL-0004/D01_A_dawn-ebb_v1.png").convert("RGB"))
    L = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
    zones = [  # (polygon, threshold): left tower lower web, left upper, centre x3, right
        ([(146, 415), (175, 405), (215, 440), (240, 530), (232, 552), (150, 552), (142, 500)], 7),
        ([(176, 318), (208, 318), (208, 415), (176, 415)], 7),
        ([(352, 222), (398, 222), (398, 278), (352, 278)], 7),
        ([(318, 335), (352, 335), (352, 368), (318, 368)], 7),
        ([(318, 405), (352, 405), (352, 478), (318, 478)], 13),
        ([(518, 322), (560, 322), (600, 440), (590, 470), (525, 470), (525, 430), (530, 400)], 7)]
    zone = np.zeros(L.shape, np.uint8)
    thr = np.full(L.shape, 255, np.int32)
    for poly, t in zones:
        zz = np.zeros(L.shape, np.uint8)
        cv2.fillPoly(zz, [np.array(poly, np.int32)], 1)
        zone |= zz
        thr[zz > 0] = t
    tower = cv2.erode((cv2.GaussianBlur(L, (0, 0), 3) < 185).astype(np.uint8), np.ones((5, 5), np.uint8))
    bh = cv2.morphologyEx(L, cv2.MORPH_BLACKHAT, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))).astype(int)
    md = cv2.medianBlur(L, 11).astype(int)
    feat = np.clip(np.maximum(bh, md - L.astype(int)), 0, 255).astype(np.uint8)
    groove = np.zeros_like(feat)
    for ang in range(5, 36, 3):
        groove = np.maximum(groove, cv2.morphologyEx(feat, cv2.MORPH_OPEN, line_k(ang, 31)))
    crack = ((feat.astype(int) - cv2.dilate(groove, np.ones((3, 3), np.uint8)).astype(int)) > thr).astype(np.uint8)
    m = cv2.dilate(keep_components(crack & zone & tower, 5), np.ones((3, 3), np.uint8))
    fix = cv2.inpaint(np.ascontiguousarray(a), m * 255, 4, cv2.INPAINT_TELEA)
    Image.fromarray(fix).save(f"{OUT}/D01_A_op.png")
    print("02 D01_A: crack px painted", int(m.sum()))


def wall_05():
    a = np.asarray(Image.open(f"{ROOT}/output/S01E01/animatic/frames/sc06-sh010_a.png").convert("RGB"))
    L = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
    close = cv2.morphologyEx(L, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)))
    bh = (close.astype(int) - L.astype(int)).clip(0, 255).astype(np.uint8)
    straight = np.zeros_like(bh)
    for ang in range(0, 180, 6):
        straight = np.maximum(straight, cv2.morphologyEx(bh, cv2.MORPH_OPEN, line_k(ang, 41)))
    region = np.zeros(L.shape, np.uint8)
    for poly in ([(165, 212), (322, 212), (322, 360), (205, 276), (165, 300)],
                 [(362, 212), (428, 212), (428, 440), (362, 392)],
                 [(962, 212), (1018, 212), (1018, 336), (968, 336)],
                 [(1064, 212), (1170, 212), (1140, 300), (1100, 336), (1064, 336)]):
        cv2.fillPoly(region, [np.array(poly, np.int32)], 1)
    cv2.circle(region, (690, 400), 182, 1, -1)
    region[470:] = 0
    region &= 1 - cv2.dilate((L < 70).astype(np.uint8), np.ones((5, 5), np.uint8))
    pale = (cv2.GaussianBlur(close, (0, 0), 3) > 118).astype(np.uint8)
    crack = ((bh.astype(int) - cv2.dilate(straight, np.ones((3, 3), np.uint8)).astype(int)) > 9).astype(np.uint8)
    m = cv2.dilate(keep_components(crack & region & pale, 8), np.ones((3, 3), np.uint8))
    fix = cv2.inpaint(np.ascontiguousarray(a), m * 255, 3, cv2.INPAINT_TELEA)
    Image.fromarray(fix).save(f"{OUT}/sc06_wheel_op.png")
    print("05 sc06 wall: crack px painted", int(m.sum()))


def map_24():
    a = np.asarray(Image.open(f"{REF}/M-MAP/E05_map_base_v1.png").convert("RGB")).astype(float)
    L = a.mean(2)
    dens = cv2.GaussianBlur((L < 175).astype(np.float32), (0, 0), 9)
    land = (dens > 0.17).astype(np.uint8)
    land[:, :70] = 0
    land[0:420, 940:] = 0            # compass rose
    land[0:240, 0:340] = 0           # title cartouche
    land[580:, 0:320] = 0            # legend box (stays empty: no legend row 4)
    n, lab, st, _ = cv2.connectedComponentsWithStats(land, 8)
    land = (lab == 1 + np.argmax(st[1:, 4])).astype(np.uint8)
    land = cv2.morphologyEx(land, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    h, w = land.shape
    ff = land.copy()
    cv2.floodFill(ff, np.zeros((h + 2, w + 2), np.uint8), (0, 0), 1)
    land = land | (1 - ff)
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.hypot((xx - 560) / 1.15, yy - 365)          # the hill: Steps core, Mids ring, Lows the rest
    steps = (r < 120).astype(np.float32)
    mids = ((r >= 120) & (r < 215)).astype(np.float32)
    lows = 1 - np.clip(steps + mids, 0, 1)
    out = a.copy()
    for z, c in zip((steps, mids, lows), ([226, 196, 128], [168, 184, 150], [150, 166, 186])):
        z = cv2.GaussianBlur(z * land, (0, 0), 6)[..., None] * 0.55
        out = out * (1 - z) + (out * np.array(c, float) / 255.0) * z
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(f"{OUT}/E05_map_tints_op.png")
    print("24 map: three tier tints")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    spires_02()
    wall_05()
    map_24()
