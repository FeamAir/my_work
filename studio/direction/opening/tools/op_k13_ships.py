#!/usr/bin/env python3
"""S1 OP v3, keeper R4.2 (lore-op-2026-11-24.md §R4): hold the harbour fleet of K13 on the plate positions. $0, local.

  python3 -I op_k13_ships.py [track] [render] [check]        (no argument = track + render)

Studio director's call (2026-11-24): free fix, no retake. K13 keeps its water; every ship (hull, masts, rigging) is a
STATIC patch from the plate: H1 for 31 / 31b / 31c, H2 for 32. Pipeline (all in 1920x1080 plate geometry; K13 frame 0
is pixel-aligned to H1, H1 and H2 ships are pixel-aligned to each other, checked):

  1. cores   per ship: GrabCut on H1 inside a hand-set box (+ dark-line rigging, close, hole fill) -> soft matte
             (4 px feather); plus static landmark cores (both piers, their lamps and bollards). These are pasted
             from the plate on every frame -> the ships cannot move (0 px by construction).
  2. track   per ship: drift d_k(t) of the ship in K13 (masked template match of the H1 ship on K13, +-110 px,
             sub-pixel), smoothed by a weighted cubic fit. Table in output/opening/clips/K13_v3_tracks.json.
  3. water   per ship a feathered ZONE around the core (radius = max drift used + 18 px, plus the long sun
             shadows of the big ship, mid-left ship, c_mid and the three-master). Inside a zone the K13 water is
             sampled at p + d_k(t) (= the water that travels with that ship), so the moving water and the ship's own
             shadow sit where the plate has them. Anywhere the sampled K13 pixel is a DRIFTED ship (any other ship
             at its K13 position, dilated 8 px), the plate water (H1, with the L-10 ripple displacement so it is
             not frozen) is used instead. Same for the open water outside the zones: K13 as is, drifted ships
             replaced. -> no second hull anywhere.
  4. output  clips/K13_v3.mp4 (H1 ships, K13 frames 0-80, for 31: 0-1.5 s, 31b: 1.5-3.0 s, 31c: 0-1.5 s again in its
             1.3x top crop; this halves the drift the zones have to absorb) and clips/K13_v3_H2.mp4 (H2 ships,
             frames 0-40, the A side of the GLASS in 32). Both 1920x1080, 24 fps.
  check    measures every 10th frame of 31, 31b, 31c, 32 in the master: camera (push/crop/shake) from SIFT on the
           landmarks only (piers, lamps, sky, islands, railing, never the ships), frame warped back to plate
           geometry, every visible ship matched against the plate (+-30 px, masked TM_CCOEFF_NORMED). Writes output/opening/K13_v3_check.json.
"""
import json
import os
import subprocess
import sys

import cv2
import numpy as np

ROOT = "/home/user/my_work"
OUTD = f"{ROOT}/output/opening"
CL = f"{OUTD}/clips"
WK = f"{OUTD}/build_work"
W, H, FPS = 1920, 1080, 24
H1P, H2P = f"{WK}/H1_1080.png", f"{WK}/H2_1080.png"      # written by op_animatic.make_assets (plates v2 + R3.1)
MASTER = f"{OUTD}/S1_OP_v3.mp4"
N_USED = 81             # K13 frames 0-80 are used (31: 0-36, 31b: 36-72, 31c: 0-36, 32: 0-37)

# ship boxes (x0, y0, x1, y1) in 1080p plate px: hull + masts + rigging
SHIPS = {
    "big": (1060, 72, 1345, 668), "lp_ship": (40, 515, 378, 968), "rp_ship": (1545, 560, 1795, 925),
    "rp_up": (1770, 400, 1895, 612), "mid_l": (570, 348, 660, 612), "three": (300, 160, 500, 345),
    "l_far": (88, 272, 182, 348), "l_edge": (0, 335, 140, 452), "l_small": (212, 348, 298, 478),
    "c_l1": (488, 272, 562, 366), "c_far1": (582, 188, 638, 242), "c_mid": (718, 252, 778, 398),
    "c_far2": (848, 232, 892, 302), "bk_l": (1062, 148, 1115, 265), "bk_r": (1265, 165, 1355, 272),
    "r_mid_a": (1408, 220, 1482, 304), "r_mid_b": (1398, 294, 1484, 404), "r_far": (1718, 272, 1835, 368),
    "r_edge": (1865, 375, 1920, 465), "tiny1": (918, 220, 946, 270), "tiny2": (962, 292, 992, 328),
    "tiny3": (670, 222, 694, 250),
}
# long sun shadows on the water (belong to the ship's zone, so they stay with the plate)
SHADOWS = {
    "big": [(1110, 640), (1330, 640), (1520, 1010), (1300, 1020)],
    "mid_l": [(560, 590), (650, 600), (520, 790), (430, 780)],
    "c_mid": [(715, 380), (770, 390), (690, 500), (650, 490)],
    "three": [(300, 320), (480, 330), (420, 420), (230, 400)],
    "lp_ship": [(120, 940), (370, 700), (380, 960), (200, 1000)],
    "rp_ship": [(1560, 900), (1760, 920), (1790, 1000), (1600, 980)],
}
# static landmarks (never move, d = 0): pier slabs, lamp posts (dark pixels inside the rect), bollards, near railing
PIERS = [
    [(0, 688), (308, 508), (422, 508), (424, 564), (0, 887)],          # left pier
    [(1474, 496), (1530, 492), (1920, 700), (1920, 887), (1474, 534)],  # right pier
    [(0, 1036), (W, 1036), (W, H), (0, H)],                             # near railing
]
LAMPS = [(138, 508, 166, 634), (288, 426, 316, 526), (1574, 416, 1604, 514), (1698, 486, 1728, 614),
         (564, 876, 598, 1070), (1494, 876, 1528, 1070), (0, 830, 36, 1070), (1876, 572, 1920, 668),
         (352, 476, 398, 518), (1492, 468, 1538, 508)]
LANDMARKS = PIERS + [[(x0, y0), (x1, y0), (x1, y1), (x0, y1)] for x0, y0, x1, y1 in LAMPS]


def landmark_mask(h1):
    """pier slabs (polygon) + the dark posts/heads/bollards inside each lamp rect (not the water around them)."""
    m = np.zeros((H, W), np.float32)
    for pp in PIERS:
        poly(pp, 1.0, m)
    g = cv2.cvtColor(h1, cv2.COLOR_BGR2GRAY).astype(np.float32)
    bg = cv2.medianBlur(g.astype(np.uint8), 31).astype(np.float32)
    for x0, y0, x1, y1 in LAMPS:
        dark = ((bg - g)[y0:y1, x0:x1] > 12).astype(np.uint8)
        dark = cv2.morphologyEx(dark, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
        m[y0:y1, x0:x1] = np.maximum(m[y0:y1, x0:x1], cv2.dilate(dark, np.ones((3, 3), np.uint8)))
    return m


# landmark mask for the camera solve in `check` (no ships): pier tops, lamps, sky band, islands, bottom railing
CAM_LM = LANDMARKS + [[(0, 0), (W, 0), (W, 60), (0, 60)], [(0, 205), (240, 205), (240, 262), (0, 262)],
                      [(1630, 205), (W, 205), (W, 262), (1630, 262)], [(0, 1035), (W, 1035), (W, H), (0, H)]]


def frames_of(p, n=None):
    cap, fr = cv2.VideoCapture(p), []
    while n is None or len(fr) < n:
        ok, f = cap.read()
        if not ok:
            break
        fr.append(cv2.resize(f, (W, H), interpolation=cv2.INTER_LANCZOS4) if f.shape[:2] != (H, W) else f)
    return fr


def poly(pts, val=1.0, m=None):
    m = np.zeros((H, W), np.float32) if m is None else m
    cv2.fillPoly(m, [np.array(pts, np.int32)], val)
    return m


def core_of(im, box, pad=24):
    x0, y0, x1, y1 = box
    a, b, c, d = max(0, x0 - pad), max(0, y0 - pad), min(W, x1 + pad), min(H, y1 + pad)
    sub = im[b:d, a:c].copy()
    m = np.full(sub.shape[:2], cv2.GC_BGD, np.uint8)
    m[y0 - b:y1 - b, x0 - a:x1 - a] = cv2.GC_PR_FGD
    cv2.grabCut(sub, m, None, np.zeros((1, 65)), np.zeros((1, 65)), 6, cv2.GC_INIT_WITH_MASK)
    f = ((m == cv2.GC_FGD) | (m == cv2.GC_PR_FGD)).astype(np.uint8)
    g = cv2.cvtColor(sub, cv2.COLOR_BGR2GRAY)
    bh = cv2.morphologyEx(g, cv2.MORPH_BLACKHAT, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    rig = np.zeros_like(f)
    rig[y0 - b:y1 - b, x0 - a:x1 - a] = bh[y0 - b:y1 - b, x0 - a:x1 - a] > 14
    f = cv2.morphologyEx(f | rig, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
    # fill holes
    ff = f.copy()
    cv2.floodFill(ff, np.zeros((ff.shape[0] + 2, ff.shape[1] + 2), np.uint8), (0, 0), 1)
    f = f | (1 - ff)
    box_m = np.zeros_like(f)
    box_m[max(0, y0 - b - 4):y1 - b + 4, max(0, x0 - a - 4):x1 - a + 4] = 1
    full = np.zeros((H, W), np.uint8)
    full[b:d, a:c] = f & box_m
    return full


def cores(h1):
    c = {k: core_of(h1, bx) for k, bx in SHIPS.items()}
    for k, (x0, y0, x1, y1) in SHIPS.items():
        if c[k].sum() < 50:            # GrabCut finds nothing on the faintest far ships: the ellipse of the box
            cv2.ellipse(c[k], ((x0 + x1) // 2, (y0 + y1) // 2), ((x1 - x0) // 2, (y1 - y0) // 2), 0, 0, 360, 1, -1)
    return c


def soft(m, grow, sig):
    m = m.astype(np.float32)
    if grow > 0:
        m = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * grow + 1, 2 * grow + 1)))
    return cv2.GaussianBlur(m, (0, 0), sig) if sig > 0 else m


def track(h1, fr, core, box, R=110):
    """template match (TM_CCOEFF_NORMED, grey, sigma 1) of the H1 ship box on each K13 frame, +-R px, sub-pixel."""
    def grey(im):
        return cv2.GaussianBlur(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(np.float32), (0, 0), 1.0)
    x0, y0, x1, y1 = box
    T = grey(h1)[y0:y1, x0:x1]
    out = []
    for f in fr:
        G = cv2.copyMakeBorder(grey(f), R, R, R, R, cv2.BORDER_REFLECT)
        m = cv2.matchTemplate(G[y0:y1 + 2 * R, x0:x1 + 2 * R], T, cv2.TM_CCOEFF_NORMED)
        _, mv, _, ml = cv2.minMaxLoc(m)
        px, py = ml

        def sub(v, i):
            if 0 < i < len(v) - 1:
                den = v[i - 1] - 2 * v[i] + v[i + 1]
                return i + (0.5 * (v[i - 1] - v[i + 1]) / den if den != 0 else 0)
            return float(i)
        out.append((sub(m[py], px) - R, sub(m[:, px], py) - R, mv))
    return np.array(out)


# tracking box overrides (a neighbour's moving hull would pull the match) and search radii for small far ships
TRACK_BOX = {"c_l1": (508, 280, 562, 366)}
TRACK_FIT = {"c_l1": (40, 1), "tiny2": (40, 1)}      # (fit only frames < N, polynomial degree): overlap/noise later
TRACK_R = {"c_l1": 40, "tiny1": 30, "tiny2": 30, "tiny3": 30, "c_far1": 40, "c_far2": 40, "c_mid": 40}


def smooth(tr, n, upto=None, deg=3):
    """robust polynomial fit through frame 0 = (0, 0): low-score and outlier frames (> 3 px off the fit) are dropped."""
    tr = tr[:upto] if upto else tr
    t = np.arange(len(tr), dtype=float)
    res = np.zeros((n, 2))
    for j in (0, 1):
        keep = tr[:, 2] > 0.5
        for _ in range(3):
            A = np.stack([t ** (i + 1) for i in range(deg)], 1)
            cf, *_ = np.linalg.lstsq(A[keep], tr[keep, j], rcond=None)
            fit = A @ cf
            keep = keep & (np.abs(fit - tr[:, j]) < 3.0)
        tn = np.arange(n, dtype=float)
        res[:, j] = np.stack([tn ** (i + 1) for i in range(deg)], 1) @ cf
    return res


def cmd_track():
    h1 = cv2.imread(H1P)
    fr = frames_of(f"{CL}/K13_fix.mp4", N_USED)
    c = cores(h1)
    raw, sm = {}, {}
    for k, bx in SHIPS.items():
        tr = track(h1, fr, c[k], TRACK_BOX.get(k, bx), TRACK_R.get(k, 110))
        raw[k] = tr.tolist()
        sm[k] = smooth(tr, N_USED, *TRACK_FIT.get(k, (None, 3))).tolist()
        i = [12, 36, 60, 72, 80]
        print(f"{k:8s}", " ".join(f"{tr[j, 0]:+6.1f},{tr[j, 1]:+6.1f}({tr[j, 2]:.2f})>{sm[k][j][0]:+6.1f},{sm[k][j][1]:+6.1f}"
                                    for j in i), flush=True)
    json.dump({"raw": raw, "smooth": sm, "note": "K13 drift vs H1 per ship, 1080p px, frames 0-80"},
              open(f"{CL}/K13_v3_tracks.json", "w"))
    np.savez_compressed(f"{WK}/K13_v3_cores.npz", **c)


def shift(img, dx, dy, border=cv2.BORDER_REFLECT):
    """img sampled at p + (dx, dy)."""
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR | cv2.WARP_INVERSE_MAP, borderMode=border)


def ripple_maps():
    rng = np.random.default_rng(7)
    nz = cv2.GaussianBlur(rng.random((H, W)).astype(np.float32), (0, 0), 24)
    nz = (nz - nz.min()) / (nz.max() - nz.min())
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    return xx, yy, nz


def rippled(plate, n, maps):
    xx, yy, nz = maps
    ph = 2 * np.pi * n / 36.0
    dx = 4.0 * np.sin(yy / 5.0 + 6 * nz + ph)
    dy = 2.0 * np.sin(xx / 37.0 + yy / 9.0 + 5 * nz + 0.7 * ph)
    return cv2.remap(plate, xx + dx, yy + dy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


def render(plate_path, out, frames_idx, label):
    plate = cv2.imread(plate_path).astype(np.float32)
    h1 = cv2.imread(H1P).astype(np.float32)          # the water fill is always H1 (choppy); H2 is calm glass
    tr = json.load(open(f"{CL}/K13_v3_tracks.json"))["smooth"]
    cz = dict(np.load(f"{WK}/K13_v3_cores.npz"))
    fr = frames_of(f"{CL}/K13_fix.mp4", max(frames_idx) + 1)
    maps = ripple_maps()
    names = sorted(SHIPS, key=lambda k: SHIPS[k][3])          # far ships first, near ships painted last
    dmax = {k: max(np.hypot(*np.array(tr[k])[i]) for i in frames_idx) for k in SHIPS}
    zones, ghost_src = {}, {}
    for k in names:
        z = cz[k].astype(np.float32)
        if k in SHADOWS:
            z = np.maximum(z, poly(SHADOWS[k]))
        zones[k] = soft(z, int(dmax[k]) + 18, 6)[..., None]
        ghost_src[k] = soft(cz[k], 8, 2)
    lm_hard = landmark_mask(h1.astype(np.uint8))
    lm = soft(lm_hard, 2, 1.5)
    ships_soft = np.clip(sum(soft(cz[k], 3, 2) for k in SHIPS), 0, 1)
    core_all = np.maximum(ships_soft, lm)[..., None]
    # ship pixels from the given plate (H1 or H2), but the rim of each soft core and the landmarks from H1: the H2 rim
    # is calm glass water and would ring the ships with a light halo over the K13 chop
    inner = soft(cv2.erode(np.clip(sum(cz[k] for k in SHIPS), 0, 1).astype(np.uint8), np.ones((5, 5), np.uint8)), 0, 1.0)
    inner = inner * (1 - lm)
    # H2: only where it is the same ship as H1 (|H2 - H1| < 15, full H1 above 30): the gaps between the rigging and
    # the reflections inside the core are glass water in H2
    dif = cv2.GaussianBlur(np.abs(plate - h1).mean(2), (0, 0), 1.5)
    inner = (inner * np.clip((30 - dif) / 15, 0, 1))[..., None]
    patch = plate * inner + h1 * (1 - inner)
    ghost_lm = soft(lm_hard, 6, 2)
    lm3 = lm[..., None]
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "12", "-pix_fmt", "yuv420p", out],
                         stdin=subprocess.PIPE)
    for n in frames_idx:
        K = fr[n].astype(np.float32)
        F = rippled(h1, n, maps) * (1 - lm3) + h1 * lm3
        d = {k: tr[k][n] for k in SHIPS}
        drifted = {k: shift(ghost_src[k], -d[k][0], -d[k][1], cv2.BORDER_CONSTANT) for k in SHIPS}   # ship k where K13 has it
        drifted["_landmarks"] = ghost_lm
        G = np.clip(sum(drifted.values()), 0, 1)[..., None]
        o = K * (1 - G) + F * G
        for k in names:
            dx, dy = d[k]
            S = shift(K, dx, dy)
            gk = np.clip(sum(v for j, v in drifted.items() if j != k), 0, 1)
            gk = shift(gk, dx, dy, cv2.BORDER_CONSTANT)[..., None]
            S = S * (1 - gk) + F * gk
            o = o * (1 - zones[k]) + S * zones[k]
        o = o * (1 - core_all) + patch * core_all
        p.stdin.write(np.clip(o, 0, 255).astype(np.uint8).tobytes())
    p.stdin.close()
    p.wait()
    print(label, out, len(frames_idx), "frames")


def cmd_render():
    render(H1P, f"{CL}/K13_v3.mp4", list(range(N_USED)), "H1 ships")
    render(H2P, f"{CL}/K13_v3_H2.mp4", list(range(41)), "H2 ships")


# ---------------------------------------------------------------- check (master, every 10th frame of 31-32)
def cmd_check():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import op_animatic as an
    cuts = {c: (s, n) for c, s, n in an.CUTS}
    h1, h2 = cv2.imread(H1P), cv2.imread(H2P)
    cz = dict(np.load(f"{WK}/K13_v3_cores.npz"))
    lm = (sum(poly(p) for p in CAM_LM) > 0).astype(np.uint8) * 255
    sift = cv2.SIFT_create(4000)
    refs = {}
    for name, im in (("H1", h1), ("H2", h2)):
        g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        refs[name] = (g, *sift.detectAndCompute(g, lm))
    first, last = cuts["31"][0], cuts["32"][0] + cuts["32"][1] - 1
    want = sorted(set(list(range(first, last + 1, 10)) + [cuts["31c"][0] + cuts["31c"][1] - 1, cuts["32"][0]]))
    video = os.environ.get("K13_CHECK_VIDEO", MASTER)      # e.g. the v2 master, to validate the method
    cap = cv2.VideoCapture(video)
    cap.set(cv2.CAP_PROP_POS_FRAMES, first)
    rows, n = [], first
    bf = cv2.BFMatcher()
    while n <= last:
        ok, f = cap.read()
        if not ok:
            break
        if n in want:
            cut = [c for c in ("31", "31b", "31c", "32") if cuts[c][0] <= n < cuts[c][0] + cuts[c][1]][0]
            # 32 is the GLASS: A side (K13 + ships from H2 where H2 = H1, H1 elsewhere) stepping to H2 -> both refs,
            # the better match counts; the camera is solved on the landmarks of the H1 reference (same geometry)
            ref = "H1/H2" if cut == "32" else "H1"
            g0, kp0, de0 = refs["H1"]
            g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
            kp, de = sift.detectAndCompute(g, None)
            mt = [m for m, m2 in bf.knnMatch(de0, de, k=2) if m.distance < 0.75 * m2.distance]
            src = np.float32([kp0[m.queryIdx].pt for m in mt])
            dst = np.float32([kp[m.trainIdx].pt for m in mt])
            A, inl = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=2.0)
            zoom = float(np.hypot(A[0, 0], A[1, 0]))
            back = cv2.warpAffine(g, A, (W, H), flags=cv2.INTER_LINEAR | cv2.WARP_INVERSE_MAP)
            vis = cv2.warpAffine(np.ones((H, W), np.uint8), A, (W, H), flags=cv2.WARP_INVERSE_MAP)
            row = {"frame": n, "cut": cut, "ref": ref, "zoom": round(zoom, 3), "landmark_inliers": int(inl.sum()), "ships": {}}
            for k, (x0, y0, x1, y1) in SHIPS.items():
                if vis[y0:y1, x0:x1].mean() < 0.999:
                    continue                      # ship not fully in this frame
                R = 30
                a, b, c, d = max(0, x0 - R), max(0, y0 - R), min(W, x1 + R), min(H, y1 + R)
                M = cv2.dilate(cz[k][y0:y1, x0:x1], np.ones((3, 3), np.uint8)).astype(np.float32)
                Sg = back[b:d, a:c].astype(np.float32)
                best = None
                for rn in (("H1", "H2") if cut == "32" else ("H1",)):
                    T = refs[rn][0][y0:y1, x0:x1].astype(np.float32)
                    m = np.nan_to_num(cv2.matchTemplate(Sg, T, cv2.TM_CCOEFF_NORMED, mask=M), nan=-1.0)
                    _, mv, _, ml = cv2.minMaxLoc(m)
                    px, py = ml

                    def sub(v, i):
                        if 0 < i < len(v) - 1:
                            den = v[i - 1] - 2 * v[i] + v[i + 1]
                            return i + (0.5 * (v[i - 1] - v[i + 1]) / den if den != 0 else 0)
                        return float(i)
                    dx, dy = sub(m[py], px) - (x0 - a), sub(m[:, px], py) - (y0 - b)
                    if best is None or mv > best[3]:
                        best = (dx, dy, rn, mv)
                dx, dy, rn, mv = best
                row["ships"][k] = [round(float(dx), 2), round(float(dy), 2), round(float(np.hypot(dx, dy) * zoom), 2),
                                   round(float(mv), 4), rn]
            row["max_screen_px"] = max([v[2] for v in row["ships"].values()] or [0])
            rows.append(row)
            print(n, cut, ref, f"zoom {zoom:.3f} inl {int(inl.sum())} ships {len(row['ships'])} max {row['max_screen_px']:.2f}px "
                  + " ".join(f"{k}:{v[2]:.1f}" for k, v in row["ships"].items()), flush=True)
        n += 1
    mx = max(r["max_screen_px"] for r in rows)
    json.dump({"video": video, "tolerance_px": 4, "max_screen_px": mx, "rows": rows}, open(os.environ.get("K13_CHECK_OUT", f"{OUTD}/K13_v3_check.json"), "w"), indent=1)
    print("MAX deviation (screen px):", mx)


if __name__ == "__main__":
    todo = sys.argv[1:] or ["track", "render"]
    for t in todo:
        globals()[f"cmd_{t}"]()
