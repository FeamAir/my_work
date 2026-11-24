#!/usr/bin/env python3
"""Saga OP, style C, build v1.2 — a $0 polish pass over v1.1 (ffmpeg + OpenCV + numpy; no API call of any kind).
Board SAGA_OP v2.9. Same cut grid (68 shots + 9 black, 87.0 s, 24 fps), same hits 1369 / 1657 / 1981.

  python3 -I op_saga_build_c12.py build [--only A01a,C13]   # segments that change in v1.2 (rest copied from v1.1)
  python3 -I op_saga_build_c12.py finish                    # unified finish -> fin_logo.mov, fin_textless.mov (ProRes)
  python3 -I op_saga_build_c12.py master                    # master mp4 + ProRes master + textless + preview
  python3 -I op_saga_build_c12.py check FILE                # freezedetect + mpdecimate (op_saga_animatic.check) + LUFS/TP
  python3 -I op_saga_build_c12.py jitter FILE               # И10: per-frame letter-band shift on C13 (phase correlation)

What changes against v1.1 (op_saga_build_c.py, kept as is for v1.1):
  1. HOOK (analyst И4, marketer): 0:00-0:09 re-cut from accepted clips only. Foggy city in 2 shots (A02 KA02 tilt, A04a
     K07C canals) instead of 4; it opens on the most kinetic approved material, the rushing wet rim slats of the K04C
     wheel (the v1.1 A01b window), with a POP + SHAKE on frame 0 on the new audio hit; then the K05C wheels with a moving
     window, the K04C rim from the other side, the K05C wet deck. Highwater only, no water over anything, no spray wall,
     no new land, no tower foot, no light. Hook lift: a luma curve that holds the blacks (Spires stay dark) and lifts the
     mids so every second of 0-9 s is >= 70/255 mean.
  2. WHIP B06b -> B07a (gate И5): a real whip — the B06b window accelerates right over its last 6 frames (1400 px) with a
     growing horizontal blur; B07a arrives from the left over its first 6 frames with the blur decaying. The B07a window,
     zoom and the keeper's top anchor (R8.3 #2) are unchanged after frame 5.
  3. C13 letter jitter (gate И10): the logo layer had its own integer scale (1 + 1.5 % over the cut) -> its width stepped
     2 px every ~11 frames, the word jumped 1 px. Removed: after the landing the logo keeps one size; the slow push is
     only the sub-pixel whole-frame push (subpix_push), now 4.5 % (3 % + the logo's former 1.5 %). The glint stays
     2000-2040 (LOGO.md §4 updated, И11).
  4. Unified finish over every shot (analyst top 2): per-shot sharpness match toward the median (soft crops get a mild
     unsharp, the crisp 3D renders a light blur), one static paper texture and one moving 2-px grain, both luma only,
     added midtone-weighted (x 4A(1-A)): neutral on average, zero at black and white, so the per-land colour keys and
     the brightness stay and near-black does not move: the Spires stay dark, no glow. B16 (planned black) gets no finish.
  5. The AI label: "AI-ANIMATED", bold, 30 px, white 92 % on a 40 % black box, bottom right above the player bar.
  6. Audio: op_saga_audio_v12.py (hit at 0:00 from the v1a stems, intro +5 dB, -14 LUFS, TP <= -1).
  7. Deliverables (gate И8): master H.264 with the label; ProRes 422 HQ master (same picture, the label in); textless
     ProRes 422 HQ (no label, no logo: C13 = plate + spray wipe only); phone preview (crf 20, faststart).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import op_saga_build_c as bc  # noqa: E402

an, sa = bc.an, bc.sa
OUTD, FPS, W, H = an.OUTD, an.FPS, an.W, an.H
WK11 = f"{OUTD}/saga_c_build_v11"
WK = f"{OUTD}/saga_c_build_v12"
bc.WK = an.WK = sa.WK = WK
an.SEG = f"{WK}/seg"
SEG = an.SEG
OUT = f"{OUTD}/SAGA_OP_C_v1_2.mp4"
OUT_PREVIEW = f"{OUTD}/SAGA_OP_C_v1_2_preview.mp4"
OUT_PRORES = f"{OUTD}/SAGA_OP_C_v1_2_master_prores.mov"
OUT_TEXTLESS = f"{OUTD}/SAGA_OP_C_v1_2_textless_prores.mov"
AUDIO = f"{WK}/audio_v12.wav"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
CUTS, START, NFR = sa.CUTS, an.START, an.NFR
L_ = an.loc
CHANGED = ["A01a", "A01b", "A02", "A03", "A04a", "A04b", "B06b", "B07a", "C13"]
BLACK = (1360, 1368)
# И10: the logo no longer grows on its own (+1.5 % through an integer scale); the whole-frame sub-pixel push takes that
# share: 3 % + 1.5 % = 4.5 %, so the letters keep v1.1's growth without the step (and default mpdecimate keeps every
# frame of the hold even before the grain).
bc.C13_PUSH = 1.045


def setup():
    """v1.2 starts from a copy of the v1.1 work dir (segments, KW16_r19, assets); only CHANGED are rebuilt."""
    os.makedirs(WK, exist_ok=True)
    if not os.path.isdir(SEG):
        shutil.copytree(f"{WK11}/seg", SEG)
    for f in os.listdir(WK11):
        p = f"{WK11}/{f}"
        if os.path.isfile(p) and not os.path.exists(f"{WK}/{f}"):
            shutil.copy2(p, f"{WK}/{f}")


# ------------------------------------------------------------------------------------------------ pieces ---
def piece_x(g, path, ss, src_t, z, cx, cy, cx1=None, xoff="0", speed=1.0):
    """bc.piece with an extra horizontal offset expression in output pixels (`xoff`, in n), clipped to the source."""
    n = bc.nframes(path)
    assert ss >= 0 and ss + src_t <= (n - 1) / FPS + 1e-6, f"{g.cut}: window past the clip"
    i = g.clip(path, ss, src_t + 0.05)
    o = g.lab()
    T = max(g.n - 1, 1) / FPS
    fx0, fy0 = bc.fpos(cx, z), bc.fpos(cy, z)
    fx1 = bc.fpos(cx if cx1 is None else cx1, z)
    xe = f"clip((iw-ow)*({fx0}+({fx1 - fx0:.5f})*min(1,t/{T:.4f}))+({xoff}),0,iw-ow)"
    g.add(f"[{i}]setpts=(PTS-STARTPTS)/{speed},fps={FPS},scale={int(W * z + 0.5) // 2 * 2 + 4}:{int(H * z + 0.5) // 2 * 2 + 4}:"
          f"force_original_aspect_ratio=increase,crop={W}:{H}:x='{xe}':y='(ih-oh)*{fy0}',setsar=1[{o}]")
    return o


def hblur_frames(g, s, sig):
    """sig: {local frame: horizontal gaussian sigma} — one gblur per frame (timeline), motion blur of the whip."""
    o = g.lab()
    parts = [f"gblur=sigma={v}:sigmaV=0.01:enable='eq(n,{f})'" for f, v in sorted(sig.items()) if v > 0]
    g.add(f"[{s}]{','.join(parts)}[{o}]")
    return o


def hook_lift(g, s, strong=False):
    """phone brightness for 0-9 s: blacks held (0-0.08 unchanged -> the Spire bodies stay dark), mids lifted; the dark
    wheel interiors (K04C/K05C) and the canals take the stronger curve."""
    o = g.lab()
    c = "0/0 0.08/0.09 0.2/0.35 0.4/0.63 0.7/0.87 1/1" if strong else "0/0 0.08/0.08 0.2/0.27 0.4/0.53 0.7/0.81 1/1"
    g.add(f"[{s}]curves=all='{c}'[{o}]")
    return o


# the hook: cut -> (clip, ss, z, cx, cy, cx1)
HOOK = {
    "A01a": ("K04C", 3.5, 2.2, 0.15, 0.82, None),     # the rushing wet rim slats (the v1.1 A01b window): kinetic open
    "A01b": ("K05C", 0.5, 1.6, 0.22, 0.60, 0.42),     # the treadwheels turning, window travelling right
    "A03": ("K04C", 1.0, 1.9, 0.86, 0.86, 0.74),      # the same rim from the other side, window travelling left
    "A04a": ("K07C", 0.0, 2.2, 0.22, 0.82, None),     # city 2 of 2: the canals of the Lows (the v1.1 A04a window)
    "A04b": ("K05C", 3.0, 1.8, 0.20, 0.80, 0.30),     # the wet deck under the near wheel, window travelling right
}

WHIP_OUT = {30: 6, 31: 14, 32: 26, 33: 40, 34: 56, 35: 72}   # B06b local frames -> sigma
WHIP_IN = {0: 60, 1: 38, 2: 20, 3: 9, 4: 3}                  # B07a


def build(cut):
    out = f"{SEG}/{cut}.mp4"
    g = an.G(cut)
    if cut in HOOK:
        k, ss, z, cx, cy, cx1 = HOOK[cut]
        s = bc.piece(g, bc.clip(k), ss, NFR[cut] / FPS, z=z, cx=cx, cy=cy, cx1=cx1)
        if k in ("K04C", "K05C"):
            s = an.rain(g, s, darken=False)
        else:
            s = an.mist(g, s, 0.12)
        s = hook_lift(g, s, strong=True)
        if cut == "A01a":                                  # the 0:00 hit: POP 0-1 + SHAKE 9 px
            s = an.shake(g, an.pop(g, s, [0]), [(0, 9, 6)])
        return bc.run(g, s, out)
    if cut == "A02":                                       # unchanged window (KA02 tilt, city 1 of 2) + the lift
        s = piece_tilt(g)
        return bc.run(g, hook_lift(g, an.mist(g, s, 0.1)), out)
    if cut == "B06b":                                      # WHIP out: v1.1 window, accelerating right on 30-35
        k, ss, src_t, speed, z, cx, cy = bc.spec(cut)[:7]
        off = f"if(gte(n,30),1400*pow((n-29)/6,2.2),0)"
        s = piece_x(g, bc.clip(k), ss, src_t, z, cx, cy, xoff=off)
        s = hblur_frames(g, s, WHIP_OUT)
        return bc.run(g, s, out)
    if cut == "B07a":                                      # WHIP in: from the left over 0-5, then the v1.1 window
        k, ss, src_t, speed, z, cx, cy, cx1 = bc.spec(cut)[:8]
        lh, box = bc.BEAT[cut]
        ss = bc.slide(cut, k, ss, src_t, speed, lh, box)
        off = "if(lt(n,6),-420*pow(1-n/6,2),0)"
        s = piece_x(g, bc.clip(k), ss, src_t, z, cx, cy, cx1=cx1, xoff=off)
        s = hblur_frames(g, s, WHIP_IN)
        s = an.dust(g, s, 0.4)
        return bc.run(g, s, out)
    if cut == "C13":
        return build_title("full")
    raise ValueError(cut)


def piece_tilt(g):
    """A02 exactly as v1.1: KA02 0.5-2.0 s, a 1.3x window travelling top to bottom."""
    return bc.piece(g, bc.clip("KA02"), 0.5, 1.5, z=1.3, cx=0.5, cy=0.0, cy1=1.0)


# ------------------------------------------------------------------------------------------------- C13 ---
MODE = {"full": "C13.mp4", "textless": "C13_textless.mp4", "logo": "C13_logo_rgba.mov"}


def build_title(mode):
    """v1.1 build_title/title_rest with the И10 fix; mode full | textless (no logo, no drop) | logo (logo + drop on
    transparent, no push: the vertical end card)."""
    cut = "C13"
    g = an.G(cut)
    out = f"{SEG}/{MODE[mode]}"
    L = lambda f: L_(cut, f)
    hit = L(1981)
    if mode == "logo":
        bg = g.lab()
        g.add(f"color=c=black@0.0:s={W}x{H}:r={FPS}:d={g.d:.3f},format=rgba[{bg}]")
        return title_logo(g, bg, hit, out, L, mode)
    kw = bc.clip("KW13")
    last = (bc.nframes(kw) - 1) / FPS
    a = bc.piece(g, kw, max(0.0, last - 0.65), 0.6, z=1.3, cx=0.45, cy=0.45)
    a = bc.grade_gold(g, a)
    a = bc.ink_safe(g, a, hit)
    a = an.spray_burst(g, a, 0.5, 0.9, 0.7, t0=hit / FPS, dur=13 / FPS)        # KA01 failed: SPRAY particles (v1.1)
    a = an.spray_burst(g, a, 0.35, 0.95, 0.5, t0=hit / FPS, dur=13 / FPS)
    b = bc.piece(g, bc.clip("K17C"), 0.0, 4.5)
    b = bc.lpush(g, b, 1.04, 0.5, 0.3)
    bi, ob_ = g.still(bc.plate_band_c()), g.lab()
    g.add(f"[{b}][{bi}]overlay=0:0:format=auto:shortest=1[{ob_}]")
    w = g.lab()
    h5 = "(sin(X*12.9898+Y*78.233)*437.585-floor(sin(X*12.9898+Y*78.233)*437.585))"
    h6 = "(sin(X*39.346+Y*11.135+P*317.3)*246.346-floor(sin(X*39.346+Y*11.135+P*317.3)*246.346))"
    d = (f"(Y/H+0.035*sin(X/W*37.7+1.3)+0.02*sin(X/W*91.3+4.1)+0.012*sin(X/W*211.7+0.5)+0.03*({h5}-0.5)"
         f"-(P*1.45-0.35))")
    wh = f"(200+50*{h6})"
    wipe = (f"if(lt({d},0),A,if(lt({d},0.05),if(lt({h6},0.15+17*{d}),{wh},A),"
            f"if(lt({d},0.13),{wh},if(lt({d},0.25),if(lt({h6},1-({d}-0.13)/0.12),{wh},B),B))))")
    g.add(f"[{a}]settb=AVTB,fps={FPS},format=gbrp[{w}a];[{ob_}]settb=AVTB,fps={FPS},format=gbrp[{w}b];[{w}a][{w}b]xfade=transition=custom:"
          f"duration=0.5:offset={hit / FPS:.5f}:expr='{wipe}'[{w}]")
    if mode == "textless":
        o2 = g.lab()
        g.add(f"[{w}]trim=end_frame={g.n},format=yuv420p,setsar=1[{o2}]")
        tmp = out.replace(".mp4", "_nopush.mp4")
        bc.run(g, o2, tmp)
        return bc.subpix_push(tmp, out, bc.C13_PUSH)
    return title_logo(g, w, hit, out, L, mode)


def title_logo(g, w, hit, out, L, mode):
    lp, TIDE, LH = bc.logo_c()
    s0 = hit
    li = g.still(lp)
    lg = g.lab()
    # И10: after the landing the logo keeps ONE size (was x(1 + 0.015 n/108) through an integer scale: a 2-px width
    # step every ~11 frames = the 1-px letter jump). The slow push is the sub-pixel whole-frame push only.
    g.add(f"[{li}]format=rgba,split=3[{lg}d][{lg}w0][{lg}g0];"
          f"[{lg}w0]eq=brightness=-0.16:saturation=0.75,colorbalance=bs=0.08:bm=0.05,"
          f"geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='alpha(X,Y)*lt(Y,{TIDE})*clip((Y-{TIDE}*clip((N-{s0 + 8})/16,0,1))/10+1,0,1)*(1-clip((N-{s0 + 23})/6,0,1))'[{lg}w];"
          f"[{lg}g0]geq=r=235:g=242:b=250:a='alpha(X,Y)*lt(Y,{TIDE})*0.32*exp(-pow((X-0.35*Y-(-100+(W+400)*clip((N-{s0 + 19})/40,0,1)))/34,2))'[{lg}g];"
          f"[{lg}d][{lg}w]overlay=0:0:format=auto[{lg}1];[{lg}1][{lg}g]overlay=0:0:format=auto,"
          f"scale=w='if(lt(n,{s0 + 8}),2*trunc(iw*(1.14-0.14*clip((n-{s0})/8,0,1))/2),iw)':h=-2:eval=frame[{lg}]")
    o = g.lab()
    fmt = "rgb" if mode == "logo" else "auto"
    g.add(f"[{w}][{lg}]overlay=x='(W-w)/2+if(between(n,{s0},{s0 + 5}),6*sin(n*2.6),0)':"
          f"y='660-h/2+if(between(n,{s0},{s0 + 5}),4*cos(n*3.1),0)':eval=frame:format={fmt}:enable='gte(n,{s0})'[{o}]")
    s = o
    di, d_ = g.still(an.A["drop"]), g.lab()
    t_g0, t_go = L(2020) / FPS, L(2040) / FPS
    g.add(f"[{di}]format=rgba,colorchannelmixer=rr=0.50:gg=0.52:bb=0.58:rb=0.06,"
          f"scale=w='2*trunc(max(4,30*min(1,max(0,(t-{t_g0:.3f})/{t_go - t_g0:.3f})))/2)':h=-2:eval=frame[{d_}m];"
          f"[{s}][{d_}m]overlay=x={int(W / 2 + 1300 * 0.17)}-w/2:y='{660 + LH // 2 - 30}+if(gt(t,{t_go:.3f}),1500*pow(t-{t_go:.3f},2),0)':"
          f"eval=frame:format={fmt}:enable='gte(t,{t_g0:.3f})':shortest=1[{d_}]")
    o2 = g.lab()
    if mode == "logo":
        g.add(f"[{d_}]trim=end_frame={g.n},format=rgba[{o2}]")
        cmd = ["ffmpeg", "-v", "error", "-y", *g.inputs, "-filter_complex", ";".join(g.chains), "-map", f"[{o2}]",
               "-r", str(FPS), "-frames:v", str(g.n), "-an", "-c:v", "png", "-pix_fmt", "rgba", out]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            raise RuntimeError(r.stderr[-2000:])
        return out
    g.add(f"[{d_}]trim=end_frame={g.n},format=yuv420p,setsar=1[{o2}]")
    tmp = out.replace(".mp4", "_nopush.mp4")
    bc.run(g, o2, tmp)
    return bc.subpix_push(tmp, out, bc.C13_PUSH)


# ------------------------------------------------------------------------------------------------ finish ---
def sharpness(path, n):
    cap = cv2.VideoCapture(path)
    v = []
    for k in range(n):
        ok, f = cap.read()
        if not ok:
            break
        if k in (n // 4, n // 2, 3 * n // 4):
            gr = cv2.resize(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32), (960, 540), interpolation=cv2.INTER_AREA)
            v.append(cv2.Laplacian(gr, cv2.CV_32F).var())
    return float(np.median(v))


# classes by Laplacian variance at 960x540 (v1.1 range 18-730, median ~150)
SHARP_CLASSES = [("u2", 0, 60, "unsharp=lx=5:ly=5:la=0.9:cx=3:cy=3:ca=0"),
                 ("u1", 60, 110, "unsharp=lx=5:ly=5:la=0.5:cx=3:cy=3:ca=0"),
                 ("b1", 420, 600, "gblur=sigma=0.55:steps=2"),
                 ("b2", 600, 1e9, "gblur=sigma=0.8:steps=2")]


def sharp_plan():
    plan = {}
    for c, s0, n in CUTS:
        if c == "B16":
            continue
        v = sharpness(f"{SEG}/{c}.mp4", n)
        cls = next((k for k, lo, hi, _ in SHARP_CLASSES if lo <= v < hi), "")
        plan[c] = {"lap_var": round(v, 1), "class": cls or "-"}
    json.dump(plan, open(f"{WK}/sharp_plan.json", "w"), indent=1)
    return plan


def paper_texture():
    """one static paper/canvas texture, mean 128: soft cloudy tooth + fine fibres; luma only."""
    p = f"{WK}/paper_1080.png"
    if os.path.exists(p):
        return p
    rng = np.random.default_rng(20261124)
    lo = cv2.resize(rng.normal(0, 1, (34, 60)).astype(np.float32), (W, H), interpolation=cv2.INTER_CUBIC)
    mid = cv2.GaussianBlur(rng.normal(0, 1, (H, W)).astype(np.float32), (0, 0), 3.0)
    fib = rng.normal(0, 1, (H, W)).astype(np.float32)
    k = np.zeros((1, 15), np.float32)
    k[0, :] = 1 / 15
    fa = cv2.filter2D(fib, -1, k)                                  # horizontal fibres
    fb = cv2.filter2D(fib[::-1], -1, k.T)[::-1]                    # vertical fibres
    t = 0.45 * lo / lo.std() + 0.35 * mid / mid.std() + 0.25 * (fa / fa.std() + fb / fb.std())
    t = 128 + 34 * t / t.std()
    Image.fromarray(np.clip(t, 0, 255).astype(np.uint8), "L").save(p)
    return p


def ranges(cuts):
    return "+".join(f"between(n,{START[c]},{START[c] + NFR[c] - 1})" for c in cuts) or "0"


def finish_graph(plan):
    """[0:v] concat of segments, [1:v] paper -> [fin] (yuv422p10le). Neutral at mid-grey, soft light, luma only."""
    ch = [f"[0:v]setpts=N/{FPS}/TB,fps={FPS},format=yuv420p"]
    for k, lo, hi, flt in SHARP_CLASSES:
        cs = [c for c, v in plan.items() if v["class"] == k]
        if cs:
            ch.append(f"{flt}:enable='{ranges(cs)}'")
    base = ",".join(ch) + "[s]"
    noB16 = f"not(between(n,{BLACK[0]},{BLACK[1]}))"
    paper = f"[1:v]format=gray,format=yuv420p,setsar=1[p]"
    grain = (f"color=c=0x808080:s=960x540:r={FPS},format=yuv420p,noise=c0s=42:c0f=t:c0_seed=777,"
             f"scale={W}:{H}:flags=bicubic,setsar=1[gr]")
    # midtone-weighted add, exactly neutral on average (B averages 128) and zero at black and white: the per-land keys
    # and the mean brightness stay; near-black (the Spires) moves by < 1 level. (ffmpeg's softlight is NOT neutral at
    # B = 128: it darkened the hook by ~9 levels in the first try.)
    mt = "4*(A/255)*(1-A/255)"
    b1 = f"[s][p]blend=c0_expr='A+(B-128)*0.16*{mt}':c1_mode=normal:c2_mode=normal:shortest=1:enable='{noB16}'[sp]"
    b2 = f"[sp][gr]blend=c0_expr='A+(B-128)*0.22*{mt}':c1_mode=normal:c2_mode=normal:shortest=1:enable='{noB16}',format=yuv422p10le[fin]"
    return ";".join([base, paper, grain, b1, b2])


def finish():
    plan = sharp_plan()
    for name, c13 in (("fin_logo", "C13.mp4"), ("fin_textless", "C13_textless.mp4")):
        lst = f"{WK}/concat_{name}.txt"
        with open(lst, "w") as f:
            for c, _, _ in CUTS:
                f.write(f"file '{SEG}/{c13 if c == 'C13' else c + '.mp4'}'\n")
        cmd = ["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-loop", "1", "-framerate", str(FPS),
               "-i", paper_texture(), "-filter_complex", finish_graph(plan), "-map", "[fin]", "-frames:v", str(an.TOTAL),
               "-c:v", "prores_ks", "-profile:v", "3", "-vendor", "apl0", "-pix_fmt", "yuv422p10le", f"{WK}/{name}.mov"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            raise RuntimeError(r.stderr[-3000:])
        print("finished", name, flush=True)
    # the same concat without the finish (for the honest freeze / duplicate check: grain hides stills)
    lst = f"{WK}/concat_fin_logo.txt"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-vf", f"setpts=N/{FPS}/TB,fps={FPS}",
                    "-frames:v", str(an.TOTAL), "-c:v", "libx264", "-crf", "12", "-preset", "fast", "-pix_fmt", "yuv420p",
                    f"{WK}/prefinish.mp4"], check=True)
    return plan


# ------------------------------------------------------------------------------------------------ master ---
LABEL = "AI-ANIMATED"


def label_filter(size=30, x="w-tw-40", y="h-th-52"):
    p = f"{WK}/bug.txt"
    open(p, "w").write(LABEL)
    return (f"drawtext=fontfile={FONTB}:textfile={p}:fontsize={size}:fontcolor=white@0.92:x={x}:y={y}:"
            f"box=1:boxcolor=black@0.40:boxborderw=10")


def master(audio=None):
    """audio: ONE input path (coordinator: the anthem is swappable without touching the picture). Default = the v1.2
    v1a mix (op_saga_audio_v12.py). Any 87.0 s file at -14 LUFS / TP <= -1 on the same hit grid drops in."""
    global AUDIO
    AUDIO = audio or AUDIO
    if not os.path.exists(AUDIO):
        subprocess.run([sys.executable, "-I", f"{os.path.dirname(os.path.abspath(__file__))}/op_saga_audio_v12.py", AUDIO], check=True)
    fade = f"fade=t=out:st={an.FADE_ST}:d={an.FADE_D}"
    meta = ["-metadata", "comment=AI-generated (Kling 2.5 TP, Nano Banana 2; music ElevenLabs); HOLLOWSTONE saga OP style C v1.2",
            "-metadata", "title=HOLLOWSTONE - opening (AI-animated)"]
    jobs = [
        (f"{WK}/fin_logo.mov", f"{label_filter()},{fade}", ["-c:v", "libx264", "-profile:v", "high", "-preset", "slow", "-crf", "14",
         "-tune", "grain", "-g", "48", "-maxrate", "50M", "-bufsize", "100M", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k",
         "-movflags", "+faststart"], OUT),
        (f"{WK}/fin_logo.mov", f"{label_filter()},{fade}", ["-c:v", "prores_ks", "-profile:v", "3", "-vendor", "apl0",
         "-pix_fmt", "yuv422p10le", "-c:a", "pcm_s24le"], OUT_PRORES),
        (f"{WK}/fin_textless.mov", fade, ["-c:v", "prores_ks", "-profile:v", "3", "-vendor", "apl0", "-pix_fmt", "yuv422p10le",
         "-c:a", "pcm_s24le"], OUT_TEXTLESS),
    ]
    for src, vf, enc, dst in jobs:
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", src, "-i", AUDIO, "-filter_complex", f"[0:v]{vf}[v]", "-map", "[v]",
               "-map", "1:a", "-frames:v", str(an.TOTAL), "-r", str(FPS), *enc, "-ar", "48000", "-t", f"{an.TOTAL / FPS}", *meta, dst]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            raise RuntimeError(r.stderr[-3000:])
        print("wrote", dst, flush=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", OUT, "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt",
                    "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", *meta, OUT_PREVIEW], check=True)
    print("wrote", OUT_PREVIEW)


# ------------------------------------------------------------------------------------------------ checks ---
def jitter(path, f0=1990, f1=2087):
    """И10: per-frame horizontal shift of the letter band (y 430-880, x 330-1590) by phase correlation."""
    cap = cv2.VideoCapture(path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, f0)
    prev, rows = None, []
    win = None
    for k in range(f0, f1 + 1):
        ok, f = cap.read()
        if not ok:
            break
        gr = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32)[430:880, 330:1590]
        gr = cv2.GaussianBlur(gr, (0, 0), 1.2)                     # the grain out of the measurement
        if win is None:
            win = cv2.createHanningWindow(gr.shape[::-1], cv2.CV_32F)
        if prev is not None:
            (dx, dy), _ = cv2.phaseCorrelate(prev, gr, win)
            rows.append((k, round(dx, 3), round(dy, 3)))
        prev = gr
    dx = np.array([r[1] for r in rows])
    big = [r for r in rows if abs(r[1]) > 0.5 or abs(r[2]) > 0.5]
    return {"frames": f"{f0}-{f1}", "median_abs_dx": round(float(np.median(np.abs(dx))), 3),
            "max_abs_dx": round(float(np.abs(dx).max()), 3), "jumps_over_0.5px": big}


def probe(path):
    """§12 p. 7 at frame 2028 (v1.2 geometry: no own logo scale, whole-frame push C13_PUSH about the centre)."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", "select='eq(n\\,2028)'", "-vsync", "0", "-f",
                          "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    f = np.frombuffer(raw, np.uint8).reshape(H, W, 3).astype(np.float32).mean(-1)
    lp, tide, lh = bc.logo_c()
    al = np.asarray(Image.open(lp))[..., 3].astype(np.float32) / 255
    P = 1 + (bc.C13_PUSH - 1) * (2028 - 1980) / 107
    al = cv2.resize(al, (int(1300 * P), int(lh * P)))
    y0, x0 = int(540 + (660 - 540) * P - al.shape[0] / 2), int((W - al.shape[1]) / 2)
    m = np.zeros((H, W), np.float32)
    m[y0:y0 + al.shape[0], x0:x0 + al.shape[1]] = al
    below = m.copy()
    below[:y0 + int(tide * P)] = 0
    letters = f[below > 0.9].mean()
    ring = cv2.dilate((below > 0.1).astype(np.uint8), np.ones((25, 25), np.uint8)) & (m < 0.05)
    plate = f[ring > 0].mean()
    return {"frame": 2028, "letters_below_line": round(float(letters), 1), "plate": round(float(plate), 1),
            "contrast": round(float(letters - plate), 1), "pass": bool(letters - plate >= 60)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "finish", "master", "check", "jitter", "probe"])
    ap.add_argument("file", nargs="?")
    ap.add_argument("--only", default="")
    ap.add_argument("--audio", default=None, help="one audio input path (default: the v1a v1.2 mix)")
    a = ap.parse_args()
    setup()
    an.A.update(an.make_assets())
    if a.cmd == "build":
        todo = a.only.split(",") if a.only else CHANGED
        for c in todo:
            build(c)
            print("ok", c, flush=True)
        if not a.only or "C13" in todo:
            build_title("textless")
            build_title("logo")
            print("ok C13 textless + logo layer")
        json.dump(bc.SLIDES, open(f"{WK}/slides_v12.json", "w"), indent=1)
    elif a.cmd == "finish":
        print(json.dumps(finish()))
    elif a.cmd == "master":
        master(a.audio)
    elif a.cmd == "check":
        sa.check(a.file)
        print(json.dumps(dict(zip(("integrated_LUFS", "true_peak_dBFS"), bc.loudness(a.file)))))
    elif a.cmd == "probe":
        print(json.dumps(probe(a.file)))
    elif a.cmd == "jitter":
        print(json.dumps(jitter(a.file)))


if __name__ == "__main__":
    main()
