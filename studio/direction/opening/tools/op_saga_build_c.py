#!/usr/bin/env python3
"""Saga OP, style C, build v1 ($0, ffmpeg + PIL + OpenCV; no API calls). Storyboard SAGA_OP v2.7, 68 shots + 9 frames
of black, 87.0 s, 24 fps, 1920x1080, music output/music/lib_mus_theme-op-anthem_v1a.mp3, -14 LUFS, TP <= -1.

  python3 -I op_saga_build_c.py [--only A01a,C13] [--jobs 4] [--no-final]
  python3 -I op_saga_build_c.py --check FILE         # §12 p. 5: freezedetect + mpdecimate (op_saga_animatic.check)
  python3 -I op_saga_build_c.py --contact FILE       # contact sheet, one frame every 0.5 s
  python3 -I op_saga_build_c.py --probe FILE         # §12 p. 7: LOGO_C wet-half contrast at frame 2028

Every cut is a piece of an accepted style-C Kling clip (output/opening/saga_c/clips/<K>.mp4, op_saga_run.py accept),
cut per the board §4 / §6.3. Windows marked in §4.6 slide <= ±0.75 s so the measured action peak lands on the hit
(motion energy per frame over the region the crop shows). The KA11 banner crops (C05, C06, C07) follow the clip's pan
(phase correlation), keyed at the start and the end of the piece. A clip that is held or failed twice is replaced:
  - KW13 held (keeper R7.3: W13 fixes need a keeper look at the crops): PLACEHOLDER = a 5 s linear push with cloud
    shadows on the $0-fixed W13 (frames/W13_t1_p.png), same windows as KW13; swapped out by re-running
    --only C01a,C01b,C12a,C12b,C13 once KW13 exists.
  - FAILED: a clip that failed twice (KA01 in r18): its cuts take $0 pieces of accepted clips of the same land (§6.1).
No labels, no counter; the corner bug "ANIME-STYLE · AI-ANIMATED" stays (marketer И12). No tpad, no freeze; pieces
below 0.8x only through minterpolate mci (only the map: C11a-d at 0.8x).
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import op_saga_animatic as sa  # noqa: E402

an, ob = sa.an, sa.ob
ROOT, OUTD = an.ROOT, an.OUTD
SC = f"{OUTD}/saga_c"
KC = f"{SC}/clips"
FRC = f"{SC}/frames"
WK = f"{OUTD}/saga_c_build"
an.WK, an.SEG = WK, f"{WK}/seg"
sa.WK = WK
OUT = f"{OUTD}/SAGA_OP_C_v1.mp4"
CONTACT = f"{OUTD}/contact_saga_c"
W, H, FPS = an.W, an.H, an.FPS
A = an.A
CUTS, START, NFR = sa.CUTS, an.START, an.NFR
L_ = an.loc
sa.tag = lambda g, s, text: s           # final: no labels

STATE = json.load(open(f"{SC}/state.json"))
HELD = {"KW13"}                         # r18: W13 fixes wait for the keeper's look at the crops
FAILED = {"KA01", "K03C", "KA04", "KW06"}                       # r18: failed twice (t1 and t2: orange burst, curling crest, spray over the top)


def clip(k):
    """accepted clip path; KW13 -> placeholder while held."""
    if k in HELD:
        return placeholder_kw13()
    p = f"{KC}/{k}.mp4"
    if not os.path.exists(p):
        raise FileNotFoundError(f"{k} not accepted: {p}")
    return conform(p)


def conform(p):
    """§12 p. 1: 24 fps; a 25/30 fps source goes through minterpolate mci, never drop/duplicate."""
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate",
                        "-of", "csv=p=0", p], capture_output=True, text=True).stdout.strip()
    num, den = (int(x) for x in r.split("/"))
    if num == 24 * den:
        return p
    q = f"{WK}/conf_{os.path.basename(p)}"
    if not os.path.exists(q):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", p, "-vf",
                        "minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1", "-c:v", "libx264",
                        "-crf", "12", "-pix_fmt", "yuv420p", q], check=True)
    return q


def placeholder_kw13():
    q = f"{WK}/KW13_placeholder.mp4"
    if os.path.exists(q):
        return q
    src = f"{FRC}/W13_t1_p.png"
    g = an.G("C13")                       # any cut: only for the graph helpers
    g.n = 121
    g.d = 121 / FPS + 0.6
    s = an.zp(g, g.still(src), 1.0, 1.07, 0.5, 0.52, 0.5, 0.45, curve="lin")     # very slow push toward the hill city
    s = an.overlay_field(g, s, A["clouds"], "multiply", 0.55, f"crop={W}:{H}:x='t*160':y=0")
    o = g.lab()
    g.add(f"[{s}]format=yuv420p,setsar=1[{o}]")
    an.run_cut(g, o, q)
    return q


# ------------------------------------------------------------------------------------------- analysis ---
_ENERGY = {}


def energy(path, box=(0, 1, 0, 1)):
    """frame-difference energy per frame over a box (fractions x0, x1, y0, y1), smoothed over 3 frames."""
    key = (path, box)
    if key in _ENERGY:
        return _ENERGY[key]
    cap = cv2.VideoCapture(path)
    prev, e = None, []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        g = cv2.cvtColor(cv2.resize(f, (480, 270)), cv2.COLOR_BGR2GRAY).astype(np.float32)
        x0, x1, y0, y1 = (int(box[0] * 480), int(box[1] * 480), int(box[2] * 270), int(box[3] * 270))
        g = g[y0:y1, x0:x1]
        e.append(0.0 if prev is None else float(np.abs(g - prev).mean()))
        prev = g
    e = np.convolve(np.array(e), np.ones(3) / 3, mode="same")
    _ENERGY[key] = e
    return e


def nframes(path):
    return len(energy(path))


SLIDES = {}


def slide(cut, k, ss, src_t, speed, local_hit, box=(0, 1, 0, 1)):
    """§4.6: move the window <= 0.75 s so the strongest action peak lands on the local hit frame."""
    p = clip(k)
    e = energy(p, box)
    last = (len(e) - 1) / FPS
    off = local_hit * speed / FPS                      # source seconds from the window start to the hit
    lo, hi = max(0.0, ss - 0.75), min(last - src_t - 0.06, ss + 0.75)
    best, bv = ss, -1.0
    for f in range(len(e)):
        t = f / FPS
        s0 = t - off
        if lo <= s0 <= hi and 1 <= f < len(e) - 1 and e[f] >= e[f - 1] and e[f] >= e[f + 1] and e[f] > bv:
            best, bv = s0, e[f]
    med = float(np.median(e[1:])) if len(e) > 2 else 0
    clear = bv > 1.25 * med
    SLIDES[cut] = {"clip": k, "nominal": ss, "used": round(best if clear else ss, 3), "peak_energy": round(bv, 2),
                   "median": round(med, 2), "clear_peak": bool(clear)}
    return best if clear else ss


_PAN = {}


def pan_x(path):
    """cumulative horizontal shift (px of the clip's width) per frame, by phase correlation on the luma."""
    if path in _PAN:
        return _PAN[path]
    cap = cv2.VideoCapture(path)
    prev, xs, acc = None, [0.0], 0.0
    while True:
        ok, f = cap.read()
        if not ok:
            break
        g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32)
        if prev is not None:
            (dx, _), _ = cv2.phaseCorrelate(prev, g)
            acc += dx
            xs.append(acc)
        prev = g
    w = f.shape[1] if prev is None else prev.shape[1]
    _PAN[path] = (np.array(xs), w)
    return _PAN[path]


def fpos(c, z):
    """crop-window centre (fraction of the frame) -> crop position fraction of (iw - ow)"""
    return min(1.0, max(0.0, (c - 0.5 / z) / (1 - 1 / z))) if z > 1 else 0.5


# ------------------------------------------------------------------------------------------ primitives ---
def piece(g, path, ss, src_t, speed=1.0, z=1.0, cx=0.5, cy=0.5, cx1=None, cy1=None, mci=False, reverse=False):
    """a piece of a clip, ss..ss+src_t at a constant `speed`; crop window centre (fractions) cx,cy -> cx1,cy1
    linear over the piece (a moving window, OP-21). No tpad (§12 p. 3)."""
    n = nframes(path)
    assert ss >= 0 and ss + src_t <= (n - 1) / FPS + 1e-6, f"{g.cut}: window {ss:.3f}+{src_t:.3f} past the clip ({n} fr)"
    i = g.clip(path, ss, src_t + 0.05)
    o = g.lab()
    rev = f"trim=end_frame={int(round(src_t * FPS)) + 1},reverse," if reverse else ""
    interp = (f",minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" if mci else f",fps={FPS}")
    T = max(g.n - 1, 1) / FPS
    fx0, fy0 = fpos(cx, z), fpos(cy, z)
    fx1, fy1 = fpos(cx if cx1 is None else cx1, z), fpos(cy if cy1 is None else cy1, z)
    xe = f"(iw-ow)*({fx0}+({fx1 - fx0:.5f})*min(1,t/{T:.4f}))"
    ye = f"(ih-oh)*({fy0}+({fy1 - fy0:.5f})*min(1,t/{T:.4f}))"
    g.add(f"[{i}]{rev}setpts=(PTS-STARTPTS)/{speed}{interp},scale={int(W * z + 0.5) // 2 * 2 + 4}:{int(H * z + 0.5) // 2 * 2 + 4}:"
          f"force_original_aspect_ratio=increase,crop={W}:{H}:x='{xe}':y='{ye}',setsar=1[{o}]")
    return o


def tmix(g, s, n=3):
    o = g.lab()
    g.add(f"[{s}]tmix=frames={n}[{o}]")
    return o


def run(g, s, out):
    return sa.run(g, s, out)


def grade_gold(g, s):
    o = g.lab()
    g.add(f"[{s}]colorbalance=rs=0.06:gs=0.02:bs=-0.08:rm=0.05:bm=-0.04,eq=saturation=1.1[{o}]")
    return o


def whip_out(g, s, frames=6, sigma=30):
    """WHIP-lite: directional blur growing over the last `frames` frames."""
    o = g.lab()
    n0 = g.n - frames
    g.add(f"[{s}]gblur=sigma={sigma // 3}:sigmaV=0.01:enable='between(n,{n0},{n0 + frames // 2 - 1})',"
          f"gblur=sigma={sigma}:sigmaV=0.01:enable='gte(n,{n0 + frames // 2})'[{o}]")
    return o


# ------------------------------------------------------------------------------------------- the cut list ---
# cut -> (clip, ss, src_len, speed, z, cx, cy, extra); src_len = frames * speed / 24
def spec(cut):
    n = NFR[cut]
    d = n / FPS
    S = {
        # r18: K03C and KA04 failed twice (lanterns / crowns light up) -> $0 pieces of accepted Highwater clips (§6.1)
        "A03": ("KA02", 1.8, d, 1.0, 2.4, 0.62, 0.86, 0.45),
        "A04a": ("K07C", 0.0, d, 1.0, 2.2, 0.22, 0.82),
        "A04b": ("KA02", 3.3, d, 1.0, 2.0, 0.8, 0.72),
        "A05a": ("K07C", 0.5, d, 1.0, 1.0, 0.5, 0.5),
        "A05b": ("K07C", 2.0, d * 1.25, 1.25, 1.0, 0.5, 0.5),
        "A06": ("K05C", 2.0, d, 1.0, 2.0, 0.3, 0.45),
        "A07": ("K04C", 0.5, d, 1.0, 1.0, 0.5, 0.5),
        "A08": ("K05C", 0.0, d, 1.0, 1.0, 0.5, 0.5),
        "A09": ("K04C", 2.5, d, 1.0, 1.8, 0.6, 0.4),
        "A10": ("K10C", 0.5, d * 2.0, 2.0, 1.0, 0.5, 0.5),
        "B01a": ("KW01", 0.5, d, 1.0, 1.0, 0.5, 0.5),
        "B01b": ("KW01", 3.0, d, 1.0, 1.8, 0.45, 0.6),
        "B02a": ("KW02", 1.0, d, 1.0, 1.0, 0.5, 0.5),
        "B02b": ("KW02", 3.0, d, 1.0, 1.8, 0.5, 0.65),
        "B03a": ("KW03", 0.5, d, 1.0, 1.0, 0.5, 0.5),
        "B04a": ("KW04", 1.0, d, 1.0, 1.0, 0.5, 0.5),
        "B03b": ("KW03", 2.5, d, 1.0, 1.6, 0.4, 0.45),
        "B04b": ("KW04", 3.0, d, 1.0, 1.4, 0.5, 0.75),
        "B05a": ("KW05", 0.5, d, 1.0, 1.0, 0.5, 0.5),
        "B06a": ("KW05", 3.0, d, 1.0, 2.0, 0.40, 0.62, 0.30),   # r18: KW06 failed twice -> KW05 ships
        "B05b": ("KW05", 2.5, d, 1.0, 1.5, 0.62, 0.62),
        "B06b": ("KW05", 1.4, d, 1.0, 2.2, 0.30, 0.60),
        "B07a": ("KW07", 1.0, d, 1.0, 1.0, 0.5, 0.5),
        "B08a": ("KW08", 0.5, d, 1.0, 1.0, 0.5, 0.5),
        "B07b": ("KW07", 3.0, d, 1.0, 1.5, 0.5, 0.3),
        "B08b": ("KW08", 2.5, d, 1.0, 1.0, 0.5, 0.5),
        "B09": ("KW09", 0.5, d, 1.0, 1.0, 0.5, 0.5),
        "B10a": ("KW10", 0.5, d, 1.0, 1.0, 0.5, 0.5),
        "B11a": ("KW09", 2.0, d, 1.0, 2.2, 0.227, 0.77),   # r18: no tower, foot or reflection in the crop
        "B10b": ("KW10", 2.5, d, 1.0, 1.8, 0.5, 0.8),
        "B11b": ("KW09", 3.5, d, 1.0, 2.4, 0.21, 0.63),    # r18: the shed pennant, tower out of the crop
        "B12a": ("KW11", 0.5, d, 1.0, 1.0, 0.5, 0.5),
        "B13a": ("KW12", 0.5, d, 1.0, 1.0, 0.5, 0.5),
        "B12b": ("KW11", 1.75, d, 1.0, 1.8, 0.5, 0.5),
        "B13b": ("KW12", 1.5, d, 1.0, 1.0, 0.5, 0.5),
        "B12c": ("KW11", 2.75, d, 1.0, 2.0, 0.5, 0.75),
        "B13c": ("KW12", 2.5, d, 1.0, 1.0, 0.5, 0.5),
        "B12d": ("KW11", 3.75, d, 1.0, 1.0, 0.5, 0.5),
        "B13d": ("KW12", 3.25, d, 1.0, 1.0, 0.5, 0.5),
        "B14": ("KW12", 4.1, d, 1.0, 1.8, 0.5, 0.25),
        "C01a": ("KW13", 0.0, d, 1.0, 1.0, 0.5, 0.5),
        "C01b": ("KW13", 1.5, d, 1.0, 1.4, 0.62, 0.5, 0.5),
        "C02": ("K11C", 0.5, d * 1.8, 1.8, 1 / 0.6, 0.28, 0.42),
        "C02L": ("KW05", 0.2, d, 1.0, 2.0, 0.36, 0.62, 0.26),
        "C03": ("K11C", 2.5, d * 1.8, 1.8, 1 / 0.6, 0.72, 0.42),
        "C03L": ("KW03", 4.0, d, 1.0, 2.0, 0.35, 0.4),
        "C04": ("KW14", 0.5, d * 1.6, 1.6, 1.5, 0.62, 0.36),
        "C05": ("KA11", 2.5, d * 1.8, 1.8, 2.6, 0.585, 0.43),
        "C06": ("KA11", 3.6, d * 1.8, 1.8, 2.6, 0.46, 0.40, 0.385),   # keyed on the hare (measured), no tracking
        "C06L": ("K05C", 3.5, d, 1.0, 1.8, 0.7, 0.5),
        "C07": ("KA11", 0.0, d * 1.6, 1.6, 4.0, 0.52, 0.38),
        "C08": ("KW15", 0.0, d, 1.0, 1.0, 0.5, 0.5),
        "C09": ("KW15", 1.5, d, 1.0, 1.8, 0.5, 0.6),
        "C10": ("KW15", 3.0, d, 1.0, 1.3, 0.62, 0.55, 0.38),
        "C12a": ("KW13", 3.0, d, 1.0, 1.0, 0.5, 0.5),
        "C12b": ("KW13", 3.45, d, 1.0, 1.3, 0.6, 0.5, 0.45),
    }
    return S.get(cut)


# local hit frames for the §4.6 windows: cut -> (local frame, energy box)
BEAT = {"B07a": (0, (0, 1, 0, 0.7)),
        "B10a": (0, (0, 1, 0.3, 1)), "B10b": (0, (0, 1, 0.5, 1)), "B11a": (1, (0, 0.45, 0.55, 1)), "B11b": (1, (0, 0.42, 0.42, 0.84)),
        "C02": (1, (0, 0.5, 0, 1)), "C03": (1, (0.5, 1, 0, 1)), "C04": (1, (0, 1, 0, 1)),
        "C05": (1, (0.5, 0.68, 0.2, 0.7)), "C06": (1, (0.6, 0.78, 0.3, 0.75)), "C07": (1, (0.38, 0.55, 0.15, 0.65))}
# POPs inside cuts (absolute placed frames), as the animatic
POPS = {h for h, lab in sa.HITS if "INK" not in lab and "SHAKE" not in lab and "flash" not in lab and "black" not in lab
        and "C13" not in lab}


def tally_c(n=3):
    """variant A (§7) on F14_C: n bold dark-ink strokes on the clean left page, upper left (the K10C coins land on the
    page's lower middle), 10 % of frame height, visible from frame 1."""
    p = f"{WK}/tally_C_{n}.png"
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x0, y0, hh = 440, 430, 108
    for k in range(n):
        x = x0 + k * 26
        d.line([(x, y0 + hh), (x + 10, y0)], fill=(38, 30, 30, 240), width=11)
    im.save(p)
    return p


# --------------------------------------------------------------------------------------------- KA01 peak ---
def ka01_peak():
    """the swell's strike: max motion energy over the wall half, inside 1.2-3.8 s (the cue: about mid-clip)."""
    p = clip("KA01")
    e = energy(p, (0.45, 1, 0.2, 0.8))
    lo, hi = int(1.6 * FPS), int(3.45 * FPS)
    f = lo + int(np.argmax(e[lo:hi]))
    return f / FPS


def ka01_strike_centre(tp):
    """centre of the spray burst at the peak (fractions), for the A01b 1.8x crop."""
    cap = cv2.VideoCapture(clip("KA01"))
    fr = []
    for k in range(int((tp + 0.3) * FPS) + 1):
        ok, f = cap.read()
        if not ok:
            break
        fr.append(f)
    a = cv2.cvtColor(fr[int(tp * FPS)], cv2.COLOR_BGR2GRAY).astype(np.float32)
    b = cv2.cvtColor(fr[max(0, int((tp - 0.6) * FPS))], cv2.COLOR_BGR2GRAY).astype(np.float32)
    d = np.clip(a - b, 0, None)
    d = cv2.GaussianBlur(d, (0, 0), 15)
    y, x = np.unravel_index(np.argmax(d), d.shape)
    return x / d.shape[1], y / d.shape[0]


# ---------------------------------------------------------------------------------------------- build ---
def build(cut):
    out = f"{an.SEG}/{cut}.mp4"
    g = an.G(cut)
    L = lambda f: L_(cut, f)
    pops = [L(h) for h in POPS if START[cut] <= h < START[cut] + NFR[cut]]
    if cut in ("A01a", "A01b") and "KA01" in FAILED:   # §6.1: KA01 failed twice -> $0 pieces of accepted Highwater clips
        if cut == "A01a":   # KA02 later moment, low on the dike crest and the misty Lows; the storm by RAIN + MIST
            s = piece(g, clip("KA02"), 3.0, 1.5, z=1.6, cx=0.5, cy=0.7)
            o = g.lab()
            g.add(f"[{s}]eq=brightness=-0.06:contrast=1.06:saturation=0.85[{o}]")
            s = an.rain(g, an.mist(g, o, 0.14), darken=False)
        else:               # K04C late window: the wet rim slats rushing, crop 2.2x low left (K03C failed twice too)
            s = piece(g, clip("K04C"), 3.5, 1.5, z=2.2, cx=0.15, cy=0.82)
            s = an.shake(g, an.rain(g, s, darken=False), [(0, 6, 9)])
        return run(g, s, out)
    if cut in ("A01a", "A01b"):
        tp = ka01_peak()
        SLIDES["KA01"] = {"peak_s": round(tp, 3)}
        if cut == "A01a":
            ss = max(0.0, tp - 1.5)
            s = piece(g, clip("KA01"), ss, 1.5, z=1.25, cx=0.62, cy=0.55)
            s = an.rain(g, an.mist(g, s, 0.12), darken=False)
        else:
            cx, cy = ka01_strike_centre(tp)
            SLIDES["KA01"]["strike_centre"] = [round(cx, 3), round(cy, 3)]
            ss = min(tp, (nframes(clip("KA01")) - 1) / FPS - 1.5 - 0.06)
            s = piece(g, clip("KA01"), ss, 1.5, z=1.8, cx=cx, cy=min(cy, 0.62))
            s = an.shake(g, an.rain(g, s, darken=False), [(0, 6, 9)])
        return run(g, s, out)
    if cut == "A02":   # KA02 0.5-2.0 s; the tilt = a 1.3x window travelling top to bottom over the moving clip
        s = piece(g, clip("KA02"), 0.5, 1.5, z=1.3, cx=0.5, cy=0.0, cy1=1.0)
        return run(g, an.mist(g, s, 0.1), out)
    if cut == "A10":   # K10C at 2x (tmix=2); the lean >= 0.375 s into the cut (§4.6); the tally sample of variant A
        p = clip("K10C")
        e = energy(p, (0.75, 1.0, 0.0, 1.0))
        base = float(np.median(e[1:20]))
        lean = next((f for f in range(12, len(e)) if e[f] > max(3 * base, base + 1.0)), int(1.25 * FPS))
        ss = min(max(0.0, lean / FPS - 0.375 * 2), (len(e) - 1) / FPS - 3.0 - 0.06)
        SLIDES["A10"] = {"clip": "K10C", "lean_s": round(lean / FPS, 3), "used": round(ss, 3), "nominal": 0.5}
        s = piece(g, p, ss, 3.0, speed=2.0)
        s = tmix(g, s, 2)
        oi, o = g.still(tally_c(3)), g.lab()
        g.add(f"[{s}][{oi}]overlay=0:0:format=auto:shortest=1[{o}]")
        return run(g, o, out)
    if cut == "A11":   # KA11 1.0-2.5 s, its own pan right carries into the WHIP; POP 491
        s = piece(g, clip("KA11"), 1.0, 1.5)
        o = g.lab()
        pk = L(491)
        g.add(f"[{s}]gblur=sigma=10:sigmaV=0.01:enable='between(n,{pk - 6},{pk - 3})',"
              f"gblur=sigma=40:sigmaV=0.01:enable='between(n,{pk - 2},{g.n})'[{o}]")
        return run(g, an.pop(g, o, [pk]), out)
    if cut == "B15":   # 7 flashes x 4 frames of motion + K05C frames 12-15; no Spire in any
        fl = [("KW02", 2.0, 1.0, 0.5, 0.5), ("KW04", 2.0, 1.0, 0.5, 0.5), ("KW05", 4.4, 2.0, 0.36, 0.62),
              ("KW08", 2.0, 1.0, 0.5, 0.5), ("KW09", 4.5, 2.2, 0.227, 0.77), ("KW12", 0.1, 1.0, 0.5, 0.5),
              ("K05C", 0.5, 1.0, 0.5, 0.5)]
        parts = []
        for k, (kk, ss, z, cx, cy) in enumerate(fl):
            s0 = piece(g, clip(kk), ss, 0.2, z=z, cx=cx, cy=cy)
            s = g.lab()
            g.add(f"[{s0}]trim=end_frame=4,setpts=PTS-STARTPTS,format=yuv420p[{s}]")
            parts.append(s)
        base = g.lab()
        g.add("".join(f"[{x}]" for x in parts) + f"concat=n={len(parts)}:v=1:a=0[{base}]")
        # the 7th flash ends at frame 27; the last frame (27) shows K05C frame 15
        o = g.lab()
        g.add(f"[{base}]eq=brightness='0.04*(" + "+".join(f"eq(n,{4 * k})" for k in range(7)) + ")':eval=frame[" + o + "]")
        s = an.shake(g, o, [(f, 6, 9) for f in (0, 9, 18, 27)])
        return run(g, s, out)
    if cut == "B16":
        i = g.still(f"{FRC}/D01_A_C.png")
        o = g.lab()
        g.add(f"[{i}]scale={W}:{H},eq=brightness=-1:contrast=0,setsar=1[{o}]")
        return run(g, o, out)
    if cut == "C05L":  # K10C, frames before the stack first leans, 0.75 s at 1x, crop 1.6x on the stacks (R4.2)
        p = clip("K10C")
        e = energy(p, (0.75, 1.0, 0.0, 1.0))
        base = float(np.median(e[1:20]))
        lean = next((f for f in range(12, len(e)) if e[f] > max(3 * base, base + 1.0)), int(1.0 * FPS))
        ss = max(0.0, lean / FPS - 0.75 - 2 / FPS)
        SLIDES["C05L"] = {"clip": "K10C", "lean_s": round(lean / FPS, 3), "used": round(ss, 3)}
        if lean / FPS < 0.75 + 2 / FPS:
            raise RuntimeError(f"C05L: K10C leans at {lean / FPS:.2f} s, less than 0.75 s of pre-lean frames")
        s = piece(g, p, ss, 0.75, z=2.2, cx=0.9, cy=0.38)
        o = g.lab()                                    # linear PX 8 % (an eased push stalls on frame 1: §12 p. 5)
        g.add(f"[{s}]scale=w='2*trunc({W}*(1.0+0.08*t/{g.n / FPS:.4f})/2)':h=-2:eval=frame,"
              f"crop={W}:{H}:x='(iw-ow)*0.6':y='(ih-oh)*0.4',setsar=1[{o}]")
        s = o                                          # (R4.2): the standing stacks never read as a freeze
        return run(g, s, out)
    if cut.startswith("C11"):   # KW16 reversed @0.8x through mci; crop passes right -> left along the river
        P = {"C11a": (0.0, 2.0, (0.80, 0.40), (0.62, 0.50)), "C11b": (0.0, 1.8, (0.66, 0.55), (0.44, 0.45)),
             "C11c": (1.3, 1.6, (0.48, 0.56), (0.18, 0.48)), "C11d": (0.0, 1.0, (0.5, 0.5), (0.5, 0.5))}[cut]
        ss, z, (ax, ay), (bx, by) = P
        p = clip("KW16")
        nlast = (nframes(p) - 1) / FPS
        # reversed: the window [ss, ss+1.2] counted from the END of the clip (the edit is a pull-back)
        st = max(0.0, nlast - ss - 1.32)     # r18: 1.3 s of source so mci yields the full 36 frames (was 34)
        s = piece(g, p, st, 1.3, speed=0.8, z=z, cx=ax, cy=ay, cx1=bx, cy1=by, mci=True, reverse=True)
        s = an.shake(g, an.pop(g, s, [L(START[cut] + 1)]), [(1, 6, 9)])
        return run(g, s, out)
    if cut == "C13":
        return build_title()
    sp = spec(cut)
    k, ss, src_t, speed, z, cx, cy = sp[:7]
    cx1 = sp[7] if len(sp) > 7 else None
    p = clip(k)
    if cut in BEAT and k not in HELD:
        lh, box = BEAT[cut]
        ss = slide(cut, k, ss, src_t, speed, lh, box)
    if k == "KA11" and cut in ("C05", "C07"):   # key the window on the banner: follow the clip's pan
        xs, w = pan_x(p)
        f0, f1 = int(round(ss * FPS)), min(len(xs) - 1, int(round((ss + src_t) * FPS)))
        cxa, cxb = cx + xs[f0] / w, cx + xs[f1] / w
        SLIDES.setdefault(cut, {})["pan_keys"] = [round(cxa, 4), round(cxb, 4)]
        s = piece(g, p, ss, src_t, speed, z, cxa, cy, cx1=cxb)
    else:
        s = piece(g, p, ss, src_t, speed, z, cx, cy, cx1=cx1)
    # passes
    if cut in ("A07", "A09"):
        s = an.shake(g, tmix(g, s, 3), [(0, 6, 9)])
    if cut in ("A04a", "A04b", "A05a", "A05b", "B12a", "B12b", "B12c", "B12d"):
        s = an.mist(g, s, 0.12)
    if cut in ("B07a", "B07b"):
        s = an.dust(g, s, 0.4)
    if cut in ("B11a", "B11b"):
        s = an.rain(g, s, darken=False)
    if cut == "B06b":
        s = whip_out(g, s)
    if cut in ("C12a", "C12b"):
        s = grade_gold(g, s)
    if cut in ("C02", "C03", "C05", "C06"):
        s = an.vpush(g, s, 1.0, 1.03)
        s = an.shake(g, s, [(1, 5, 9)])
    s = an.pop(g, s, pops)
    if cut in ("A06", "A08"):
        s = an.shake(g, s, [(L(289) if cut == "A06" else 0, 8 if cut == "A06" else 5, 6)])
    if cut == "B09":
        s = an.shake(g, s, [(L(1081), 6, 9)])
    if cut in ("B13d", "B14"):
        s = an.shake(g, s, [(0, 4, 12)])
    if cut in ("C09", "C10"):
        s = an.shake(g, s, [(1, 6, 9)])
    if cut == "C01a":
        s = an.shake(g, an.ink(g, s, 0), [(0, 12, 3)])
    if cut == "C08":
        s = an.ink(g, s, 0)
    return run(g, s, out)


# ------------------------------------------------------------------------------------------------ logo ---
def logo_c():
    """LOGO_C matte (LOGO.md §6, $0): luma key of the letters against #0B0D12, cropped, 1300 px wide; the tide line
    from the r16/r17 measurement (median y 382 in the 1376x768 frame) scaled to the logo."""
    p, tf = f"{WK}/LOGO_C_alpha_1300.png", f"{WK}/LOGO_C_tide.txt"
    src = np.asarray(Image.open(f"{SC}/logo/LOGO_C.png").convert("RGB")).astype(np.float32)
    lum = src.mean(-1)
    a = np.clip((lum - 24) / 16, 0, 1)
    a = cv2.morphologyEx(a, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
    ys, xs = np.where(a > 0.5)
    x0, x1, y0, y1 = xs.min() - 6, xs.max() + 7, ys.min() - 6, ys.max() + 7
    rgba = np.dstack([src, a * 255])[y0:y1, x0:x1]
    im = Image.fromarray(np.clip(rgba, 0, 255).astype(np.uint8), "RGBA")
    s = 1300 / im.width
    im = im.resize((1300, int(round(im.height * s))), Image.LANCZOS)
    im.save(p)
    tide = int(round((382 - y0) * s))
    open(tf, "w").write(str(tide))
    return p, tide, im.height


def plate_band_c():
    """LOGO.md §2 p. 11 band, with the §12 p. 7 step taken in r18 (probe 53.6 < 60 at 2028): -40 % behind the upper
    half, -75 % behind the lower half (plate only; the logo keeps its colours)."""
    p = f"{WK}/plate_band_c.png"
    y = np.arange(H, dtype=np.float32)
    sm = lambda e0, e1: (lambda u: u * u * (3 - 2 * u))(np.clip((y - e0) / (e1 - e0), 0, 1))
    a = (0.40 + 0.35 * sm(540, 780)) * sm(250, 470) * (1 - sm(930, 1080))
    x = np.linspace(-1, 1, W, dtype=np.float32)
    a = a[:, None] * (0.80 + 0.20 * np.abs(x)[None, :])
    rgba = np.zeros((H, W, 4), np.uint8)
    rgba[..., 3] = (np.clip(a, 0, 1) * 255).astype(np.uint8)
    Image.fromarray(rgba, "RGBA").save(p)
    return p


def build_title():
    """C13 (LOGO.md §4, v1.3 on LOGO_C): hit 1981 = local 1; INK + torn spray wipe 1981-1992 (the KA01 strike, 12
    frames around its peak, screened on the outgoing picture only, so it leaves with the wipe edge); logo lands
    114 % -> 100 % over 8 frames, wet above the tide line only; drain 1989-2004; glint 2016-2039; drop gathers 2020 and
    leaves 2040; K17C 0.0-4.5 s at 1x full frame +3 % push under the plate band; fade in the master."""
    cut = "C13"
    g = an.G(cut)
    out = f"{an.SEG}/{cut}.mp4"
    L = lambda f: L_(cut, f)
    hit = L(1981)
    # outgoing: C12b's picture carried on (KW13 3.45+1.5 s ... the last frame of the clip region), gold grade
    kw = clip("KW13")
    last = (nframes(kw) - 1) / FPS
    a = piece(g, kw, max(0.0, last - 0.65), 0.6, z=1.3, cx=0.45, cy=0.45)
    a = grade_gold(g, a)
    a = an.ink(g, a, hit)
    # KA01 spray, 12 frames around the burst peak, luma-keyed (the bright spray only) and screened on the outgoing;
    # KA01 failed twice -> the free SPRAY particles alone (board §4 C13 fallback)
    if "KA01" in FAILED:
        a = an.spray_burst(g, a, 0.5, 0.9, 0.7, t0=hit / FPS, dur=13 / FPS)
        a = an.spray_burst(g, a, 0.35, 0.95, 0.5, t0=hit / FPS, dur=13 / FPS)
        return title_rest(g, a, hit, out, L)
    tp = ka01_peak()
    cx, cy = ka01_strike_centre(tp)
    sp = piece(g, clip("KA01"), max(0.0, tp - 6 / FPS), 0.5, z=1.6, cx=cx, cy=min(cy, 0.6))
    o, sp2 = g.lab(), g.lab()
    g.add(f"[{sp}]setpts=PTS+{hit}/{FPS}/TB,split[{o}c][{o}m0];[{o}m0]lutyuv=y='clip((val-110)*2.2,0,255)',format=gray[{o}m];"
          f"[{o}c]format=rgba[{o}c2];[{o}c2][{o}m]alphamerge[{o}]")
    g.add(f"[{a}][{o}]overlay=0:0:format=auto:eof_action=pass[{sp2}]")
    a = an.spray_burst(g, sp2, 0.5, 0.9, 0.5, t0=hit / FPS, dur=13 / FPS)
    return title_rest(g, a, hit, out, L)


def title_rest(g, a, hit, out, L):
    b = piece(g, clip("K17C"), 0.0, 4.5)
    b = an.vpush(g, b, 1.0, 1.03, 0.5, 0.3)
    bi, ob_ = g.still(plate_band_c()), g.lab()
    g.add(f"[{b}][{bi}]overlay=0:0:format=auto:shortest=1[{ob_}]")
    w = g.lab()
    g.add(f"[{a}]settb=AVTB,fps={FPS}[{w}a];[{ob_}]settb=AVTB,fps={FPS}[{w}b];[{w}a][{w}b]xfade=transition=custom:"
          f"duration=0.5:offset={hit / FPS:.5f}:expr='if(gt(Y/H+0.06*sin(X/W*23)+0.03*sin(X/W*71),P*1.12),B,A)'[{w}]")
    lp, TIDE, LH = logo_c()
    s0 = hit
    li = g.still(lp)
    lg = g.lab()
    g.add(f"[{li}]format=rgba,split=3[{lg}d][{lg}w0][{lg}g0];"
          f"[{lg}w0]eq=brightness=-0.16:saturation=0.75,colorbalance=bs=0.08:bm=0.05,"
          f"geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='alpha(X,Y)*lt(Y,{TIDE})*clip((Y-{TIDE}*clip((N-{s0 + 8})/16,0,1))/10+1,0,1)*(1-clip((N-{s0 + 23})/6,0,1))'[{lg}w];"
          f"[{lg}g0]geq=r=235:g=242:b=250:a='alpha(X,Y)*lt(Y,{TIDE})*0.32*exp(-pow((X-0.35*Y-(-300+(W+600)*clip((N-{s0 + 35})/24,0,1)))/34,2))'[{lg}g];"
          f"[{lg}d][{lg}w]overlay=0:0:format=auto[{lg}1];[{lg}1][{lg}g]overlay=0:0:format=auto,"
          f"scale=w='2*trunc(iw*if(lt(n,{s0 + 8}),1.14-0.14*clip((n-{s0})/8,0,1),1)*(1+0.015*n/108)/2)':h=-2:eval=frame[{lg}]")
    o = g.lab()
    g.add(f"[{w}][{lg}]overlay=x='(W-w)/2+if(between(n,{s0},{s0 + 5}),6*sin(n*2.6),0)':"
          f"y='660-h/2+if(between(n,{s0},{s0 + 5}),4*cos(n*3.1),0)':eval=frame:format=auto:enable='gte(n,{s0})'[{o}]")
    s = o
    di, d_ = g.still(A["drop"]), g.lab()
    t_g0, t_go = L(2020) / FPS, L(2040) / FPS
    g.add(f"[{di}]format=rgba,colorchannelmixer=rr=0.50:gg=0.52:bb=0.58:rb=0.06,"
          f"scale=w='2*trunc(max(4,30*min(1,max(0,(t-{t_g0:.3f})/{t_go - t_g0:.3f})))/2)':h=-2:eval=frame[{d_}m];"
          f"[{s}][{d_}m]overlay=x={int(W / 2 + 1300 * 0.17)}-w/2:y='{660 + LH // 2 - 30}+if(gt(t,{t_go:.3f}),1500*pow(t-{t_go:.3f},2),0)':"
          f"eval=frame:enable='gte(t,{t_g0:.3f})':shortest=1[{d_}]")
    o2 = g.lab()
    g.add(f"[{d_}]trim=end_frame={g.n},format=yuv420p,setsar=1[{o2}]")
    return run(g, o2, out)


# ---------------------------------------------------------------------------------------------- master ---
def master():
    lst = f"{WK}/concat.txt"
    with open(lst, "w") as f:
        for c, _, _ in CUTS:
            f.write(f"file '{an.SEG}/{c}.mp4'\n")
    bug = f"{WK}/bug.txt"
    open(bug, "w").write("ANIME-STYLE · AI-ANIMATED")
    pre = f"atrim=0:{an.TOTAL / FPS},asetpts=PTS-STARTPTS,afade=t=out:st={an.FADE_ST}:d={an.FADE_D}"
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", an.MUSIC, "-af", f"{pre},loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True)
    js = json.loads(r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:"
          f"measured_LRA={js['input_lra']}:measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true")
    vf = (f"setpts=N/{FPS}/TB,fps={FPS},"
          f"drawtext=fontfile={an.FONT}:textfile={bug}:fontsize=18:fontcolor=white@0.55:x=w-tw-24:y=h-th-20,"
          f"fade=t=out:st={an.FADE_ST}:d={an.FADE_D}")
    af = f"{pre},{ln},aresample=48000,atrim=0:{an.TOTAL / FPS}"
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", an.MUSIC,
           "-filter_complex", f"[0:v]{vf}[v];[1:a]{af}[a]", "-map", "[v]", "-map", "[a]",
           "-frames:v", str(an.TOTAL), "-r", str(FPS), "-c:v", "libx264", "-profile:v", "high", "-preset", "slow",
           "-crf", "14", "-tune", "film", "-g", "48", "-maxrate", "40M", "-bufsize", "80M",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-t", f"{an.TOTAL / FPS}",
           "-metadata", "comment=AI-generated (Kling 2.5 TP, Nano Banana 2); HOLLOWSTONE saga OP style C v1",
           "-movflags", "+faststart", OUT]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr[-2000:])


def loudness(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    i = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1])
    tp = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)[-1])
    return i, tp


def contact(path, step=0.5):
    os.makedirs(CONTACT, exist_ok=True)
    TW, TH = 240, 135
    font = ImageFont.truetype(an.FONT, 13)
    idx = [int(round(t * FPS)) for t in np.arange(0, an.TOTAL / FPS, step)]
    sel = "+".join(f"eq(n\\,{i})" for i in idx)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"select='{sel}',scale={TW}:{TH}", "-vsync", "0",
                          "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, TH, TW, 3)
    cols = 12
    rows = (len(fr) + cols - 1) // cols
    im = Image.new("RGB", (cols * (TW + 4), rows * (TH + 18)), (16, 16, 16))
    d = ImageDraw.Draw(im)
    for k, f in enumerate(fr):
        x, y = (k % cols) * (TW + 4), (k // cols) * (TH + 18)
        im.paste(Image.fromarray(f), (x, y))
        d.text((x + 3, y + TH + 2), f"{idx[k] / FPS:.1f}s f{idx[k]} {sa.cut_of(idx[k])}", fill=(240, 230, 190), font=font)
    p = f"{CONTACT}/SAGA_OP_C_v1_contact_0.5s.jpg"
    im.save(p, quality=88)
    return p


def probe(path):
    """§12 p. 7: mean luma of the letters below the tide line vs the plate behind them at frame 2028."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", "select='eq(n\\,2028)'", "-vsync", "0", "-f",
                          "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    f = np.frombuffer(raw, np.uint8).reshape(H, W, 3).astype(np.float32).mean(-1)
    lp, tide, lh = logo_c()
    al = np.asarray(Image.open(lp))[..., 3].astype(np.float32) / 255
    s = 1 + 0.015 * (2028 - 1980) / 108
    al = cv2.resize(al, (int(1300 * s), int(lh * s)))
    y0, x0 = int(660 - al.shape[0] / 2), int((W - al.shape[1]) / 2)
    m = np.zeros((H, W), np.float32)
    m[y0:y0 + al.shape[0], x0:x0 + al.shape[1]] = al
    t = y0 + int(tide * s)
    below = m.copy()
    below[:t] = 0
    letters = f[below > 0.9].mean()
    ring = cv2.dilate((below > 0.1).astype(np.uint8), np.ones((25, 25), np.uint8)) & (m < 0.05)
    plate = f[ring > 0].mean()
    return {"frame": 2028, "letters_below_line": round(float(letters), 1), "plate": round(float(plate), 1),
            "contrast": round(float(letters - plate), 1), "pass": bool(letters - plate >= 60)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--no-final", action="store_true")
    ap.add_argument("--check", default="")
    ap.add_argument("--contact", default="")
    ap.add_argument("--probe", default="")
    a = ap.parse_args()
    if a.check:
        rep = sa.check(a.check)
        i, tp = loudness(a.check)
        print(json.dumps({"integrated_LUFS": i, "true_peak_dBFS": tp}))
        return
    if a.contact:
        print(contact(a.contact))
        return
    if a.probe:
        print(json.dumps(probe(a.probe)))
        return
    os.makedirs(an.SEG, exist_ok=True)
    A.update(an.make_assets())
    for k in HELD:
        clip(k)
    todo = [c for c, _, _ in CUTS if not a.only or c in a.only.split(",")]
    errs = []
    with cf.ThreadPoolExecutor(a.jobs) as ex:
        futs = {ex.submit(build, c): c for c in todo}
        for fu in cf.as_completed(futs):
            try:
                fu.result()
                print("ok", futs[fu], flush=True)
            except Exception as e:
                errs.append(futs[fu])
                print("FAIL", futs[fu], str(e)[:3000], flush=True)
    json.dump(SLIDES, open(f"{WK}/slides.json", "w"), indent=1)
    if errs:
        sys.exit(f"failed: {errs}")
    if not a.no_final:
        master()
        print("master", OUT)


if __name__ == "__main__":
    main()
