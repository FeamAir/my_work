#!/usr/bin/env python3
"""S1 OP v1 build without K13 ($0, ffmpeg + PIL). Storyboard v1.4, 87.0 s, 24 fps, 1920x1080, music v2a.

  python3 -I op_build.py [--only 25,33] [--jobs 4] [--no-final]

Reuses the ffmpeg pass library of op_animatic.py (PUSH/PAN/TILT, RAIN, SPRAY, MIST, DUST, CLOUD, SHAKE, POP, INK,
WHIP, ROT, GLASS, WIPE, logo, drops) with the real sources: the accepted NB2 frames (output/opening/frames/*_op.png),
the 16 Kling 2.5 TP clips (output/opening/clips/K*.mp4; a clip that failed twice is replaced by its §6.1 fallback,
listed in FALLBACK), the $0 paint-out plates (02, 05, 24) and the H1/H2 plates v2. No labels, no frame counter; the
corner bug ANIME-STYLE · AI-ANIMATED stays.
K13 is not made yet (C2): cuts 31, 31b, 31c and 32 use the K13 placeholder = the §6.1 K13 fallback (ripple L-10 on
the cropped H1 v2; GLASS runs on top unchanged). Swap in K13 by adding it to KCLIP and re-running --only 31,31b,31c,32.
Cut 33: the spray of the wipe is laid on the outgoing picture only, so it leaves with the wipe edge (gone by 1994) and
never sits on the tower (gate N1). Audio: v2a 0-87.0 s, fade 86.5-87.0, two-pass loudnorm to -14 LUFS, TP <= -1.
Output: output/opening/S1_OP_v1_noK13.mp4
"""
import argparse
import concurrent.futures as cf
import json
import os
import subprocess
import sys

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import op_animatic as an  # noqa: E402

ROOT = an.ROOT
OUTD = an.OUTD
FR = f"{OUTD}/frames"
CL = f"{OUTD}/clips"
PL = f"{OUTD}/plates"
an.WK = f"{OUTD}/build_work"
an.SEG = f"{an.WK}/seg"
an.label = lambda g, src, text: src          # final: no labels
W, H, FPS = an.W, an.H, an.FPS
A = an.A
L_ = an.loc

KCLIP = {k: f"{CL}/{k}.mp4" for k in ("K01", "K01a", "K03", "K04", "K05", "K07", "K08", "K09", "K10", "K11", "K12",
                                       "K14", "K15", "K16", "K17", "K18")}
FALLBACK = set()             # clips that failed twice (filled from clips/_accept.json)
OUT = f"{OUTD}/S1_OP_v1_noK13.mp4"


def load_accept():
    p = f"{CL}/_accept.json"
    if os.path.exists(p):
        acc = json.load(open(p))
        for k, v in acc.items():
            if v.get("use"):
                KCLIP[k] = f"{CL}/{v['use']}"
            if v.get("fallback"):
                FALLBACK.add(k)


def kc(g, kid, ss, t, speed=1.0, z=1.0, fx=0.5, fy=0.5, threes=False):
    """a Kling piece fitted to 1920x1080: ss..ss+t*speed of the clip, played at `speed` (or held on threes)."""
    i = g.clip(KCLIP[kid], ss, t * speed + 0.2)
    o = g.lab()
    tim = "setpts=3*(PTS-STARTPTS)" if threes else f"setpts=(PTS-STARTPTS)/{speed}"
    blend = ",tmix=frames=3" if speed >= 2 else ""
    g.add(f"[{i}]{tim},fps={FPS}{blend},scale={int(W * z + 0.5) // 2 * 2 + 4}:{int(H * z + 0.5) // 2 * 2 + 4}:force_original_aspect_ratio=increase,crop={W}:{H}:x='(iw-ow)*{fx}':y='(ih-oh)*{fy}',"
          f"setsar=1,tpad=stop_mode=clone:stop_duration=2[{o}]")
    return o


def cover_save(src, name, box=None):
    im = Image.open(src).convert("RGB")
    if box:
        im = im.crop(box)
    return an.save(an.cover(im), name)


def assets():
    A.update(an.make_assets())
    for fid in ("F01a", "F01", "F27", "F30", "F04", "F11", "F26", "F28", "F10", "F15", "F14", "F17", "F19", "F21"):
        A[fid] = cover_save(f"{FR}/{fid}_op.png", f"op_{fid}.png")
    A["P5"] = cover_save(f"{FR}/F23_op.png", "op_F23.png")
    f18 = Image.open(f"{FR}/F18_op.png").convert("RGB")
    A["P2"] = an.save(f18.resize((2150, 1200), Image.LANCZOS), "op_F18_wide.png")
    da = Image.open(f"{PL}/D01_A_op.png").convert("RGB")
    A["D01A_tall"] = an.save(da.resize((W, round(da.height * W / da.width)), Image.LANCZOS), "D01A_tall_op.png")
    A["wheel"] = f"{PL}/sc06_wheel_op.png"
    A["map"] = cover_save(f"{PL}/E05_map_tints_op.png", "map_op.png")


def fin(g, s, out):
    return an.finish(g, s, "", out, plain=True)


def build(cut):
    g = an.G(cut)
    L = lambda f: L_(cut, f)
    out = f"{an.SEG}/{cut}.mp4"
    ok = lambda k: k in KCLIP and k not in FALLBACK and os.path.exists(KCLIP[k])
    if cut == "01":
        if ok("K01a"):
            s = kc(g, "K01a", 0.0, 1.0, threes=True)
        else:
            s = an.zp(g, g.still(A["F01a"]), 1.0, 1.06, 0.5, 0.56, 0.5, 0.5)
        s = an.spray_burst(g, s, 0.3, 0.3, 0.2)
        s = an.rain(g, an.mist(g, s, 0.15), darken=False)
        return fin(g, s, out)
    if cut == "02b":
        s = kc(g, "K03", 0.0, 1.5, z=1.5, fx=0.15, fy=0.55) if ok("K03") else an.zp(g, g.still(A["F04"]), 1.5, 1.47, 0.15, 0.15, 0.55, 0.55)
        s = an.vpush(g, s, 1.02, 1.0)
        o = g.lab()
        g.add(f"[{s}]noise=alls=6:allf=t[{o}]")
        return fin(g, o, out)
    if cut == "04":
        return an.build(cut)      # K03 lanterns light up after 2.2 s: LA fallback (F04 + PULL + the drop leaving on 270)
    if cut == "06":
        if ok("K04"):
            s = kc(g, "K04", 0.5, 1.5)
            o = g.lab()
            g.add(f"[{s}]tmix=frames=3[{o}]")
            s = o
        else:
            return an.build(cut)
        s = an.shake(g, s, [(L(325), 8, 9)])
        return fin(g, s, out)
    if cut == "07":
        if not ok("K05"):
            return an.build(cut)
        s = an.vpush(g, kc(g, "K05", 0.0, 3.0), 1.0, 1.06)
        s = an.mist(g, s, 0.15)
        s = an.shake(g, s, [(L(361), 8, 9), (L(397), 8, 9)])
        return fin(g, s, out)
    if cut == "08":
        s = kc(g, "K03", 0.8, 1.5, z=1.67, fx=0.88, fy=0.32) if ok("K03") else an.zp(g, g.still(A["F04"]), 1.67, 1.67, 0.88, 0.88, 0.32, 0.32)
        o = g.lab()
        g.add(f"[{s}]noise=alls=8:allf=t[{o}]")
        s = an.shake(g, o, [(L(433), 8, 9)])
        return fin(g, s, out)
    if cut == "09":
        if not ok("K05"):
            return an.build(cut)
        s = kc(g, "K05", 4.0, 1.0)
        o = g.lab()
        tw0 = 16 / FPS
        g.add(f"[{s}]scale={W}:{int(H * 1.8)},crop={W}:{H}:x=0:y='(ih-oh)*(1-pow(min(1,max(0,(t-{tw0:.3f})/{(36 - 16) / FPS:.3f})),2))',"
              f"gblur=sigma=0.5:sigmaV=14:enable='between(n,19,22)',gblur=sigma=0.5:sigmaV=40:enable='gte(n,23)',setsar=1[{o}]")
        s = an.pop(g, o, [L(491)])
        s = an.shake(g, s, [(L(469), 8, 9)])
        return fin(g, s, out)
    if cut == "10":
        s = kc(g, "K07", 0.5, 3.0) if ok("K07") else an.zp(g, g.still(A["F10"]), 1.0, 1.08, 0.5, 0.5, 0.6, 0.4)
        s = an.mist(g, s, 0.15)
        return fin(g, s, out)
    if cut == "11":
        s = kc(g, "K08", 1.0, 3.0) if ok("K08") else an.zp(g, g.still(A["F11"]), 1.0, 1.05, 0.5, 0.5, 0.5, 0.5)
        s = an.vpush(g, s, 1.0, 1.04)
        return fin(g, s, out)
    if cut == "12":
        if not ok("K09"):
            return an.build(cut)
        acc = json.load(open(f"{CL}/_accept.json")) if os.path.exists(f"{CL}/_accept.json") else {}
        strike = float(acc.get("K09", {}).get("strike_s", 1.6))
        ss = max(0.0, strike - (685 - 648) / FPS)
        # crop x <= 960 of the 1344-wide source = left 71 %; push centred on the bell
        s = kc(g, "K09", ss, 3.0, z=1.42, fx=0.0, fy=0.35)
        s = an.dust(g, s)
        s = an.pop(g, s, [L(685)])
        return fin(g, s, out)
    if cut == "14":
        if not ok("K10"):
            return an.build(cut)
        s = kc(g, "K10", 0.5, 3.0, z=1.05)
        o = g.lab()
        T = g.n / FPS
        # variant A (E1): one bold ink tally stroke in the clean left margin; rotate-push 3 deg, 8 %, ends on the margin
        g.add(f"[{s}]drawbox=x=575:y=520:w=16:h=118:color=0x1a171c@0.92:t=fill,"
              f"scale={W * 2}:{H * 2},rotate=a='0.052*{an.ease(f't/{T:.3f}')}':c=black,"
              f"zoompan=z='1.10+0.08*{an.ease(f'on/{g.n - 1}')}':x='(iw-iw/zoom)*(0.45-0.40*{an.ease(f'on/{g.n - 1}')})':"
              f"y='(ih-ih/zoom)*0.5':d=1:s={W}x{H}:fps={FPS},setsar=1[{o}]")
        return fin(g, o, out)
    if cut == "18":
        i = g.still(A["P2"])
        o = g.lab()
        g.add(f"[{i}]crop={W}:{H}:x='(iw-ow)*{an.ease(f't/{g.n / FPS}')}':y='(ih-oh)/2',setsar=1[{o}]")
        s = an.dust(g, o, 0.3)
        return fin(g, s, out)
    if cut in ("19", "20", "21", "22"):
        k = "K11" if cut in ("19", "20") else "K12"
        if not ok(k):
            return an.build(cut)
        left = cut in ("19", "21")
        piece = (0.5, 1.5) if left else (2.5, 1.5)
        s = kc(g, k, piece[0], piece[1], z=1 / 0.6, fx=0.0 if left else 1.0, fy=0.30)
        s = an.pop(g, s, [1])
        s = an.shake(g, s, [(1, 5, 9)]) if cut == "19" else s
        return fin(g, s, out)
    if cut == "25":
        if not ok("K01"):
            return an.build(cut)
        s = kc(g, "K01", 0.0, g.n / FPS)
        s = an.spray_burst(g, s, 0.6, 0.5, 0.35)
        s = an.rain(g, s)
        s = an.ink(g, s, L(1369))
        s = an.shake(g, s, [(L(1369), 20, 4)])
        return fin(g, s, out)
    if cut == "26":
        # 1.4x on the planks: the two big lamp heads are out of frame (OP-3), the small far lamps stay small
        s = kc(g, "K18", 0.5, 1.5, z=1.4, fx=0.5, fy=1.0) if ok("K18") else an.zp(g, g.still(A["F26"]), 1.4, 1.43, 0.5, 0.5, 1.0, 1.0)
        s = an.rain(g, s)
        s = an.shake(g, s, [(L(1441), 8, 9)])
        return fin(g, s, out)
    if cut == "27":
        s = kc(g, "K14", 0.0, 1.5) if ok("K14") else an.zp(g, g.still(A["F27"]), 1.0, 1.04, 0.5, 0.5, 0.5, 0.5)
        s = an.spray_burst(g, s, 0.45, 0.35, 0.35)
        s = an.rain(g, an.mist(g, s, 0.15), darken=False)
        s = an.pop(g, s, [1])
        return fin(g, s, out)
    if cut == "28":
        if not ok("K15"):
            return an.build(cut)
        s = kc(g, "K15", 0.0, 1.5, speed=2.0)
        o = g.lab()
        g.add(f"[{s}]gblur=sigma=0.5:sigmaV=20:enable='lt(n,4)'[{o}]")
        s = an.rain(g, o, fast=True, darken=False)
        return fin(g, s, out)
    if cut == "29":
        if not ok("K04"):
            return an.build(cut)
        s = kc(g, "K04", 2.0, 1.5, speed=2.0)
        s = an.shake(g, s, [(1, 8, 9)])
        return fin(g, s, out)
    if cut == "30":
        if not ok("K16"):
            return an.build(cut)
        s = kc(g, "K16", 0.5, 3.0)
        s = an.rain(g, s)
        return fin(g, s, out)
    if cut == "33":
        return build_33(g, out)
    return an.build(cut)          # 02, 03, 05, 13, 13b, 15, 16, 17, 23, 24, 24b, 31-32b: the v1.3 recipes on the new plates


def build_33(g, out):
    L = lambda f: L_("33", f)
    # A: the 32b framing continued, INK on 1981, the spray rides on A only (leaves with the wipe edge, never on the tower)
    ai, a = g.still(A["H2"]), g.lab()
    g.add(f"[{ai}]scale={W * 2}:{H * 2},zoompan=z='1.16+0.01*on/{g.n}':x='(iw-iw/zoom)*0.5':y='(ih-ih/zoom)*0.10':"
          f"d=1:s={W}x{H}:fps={FPS},setsar=1[{a}]")
    a = an.ink(g, a, L(1981))
    a = an.spray_burst(g, a, 0.5, 0.9, 0.6, t0=L(1983) / FPS, dur=(1994 - 1983 + 1) / FPS)
    # B: K17 piece 0.0-4.5 s at 1x, framed on the crown and upper shaft (foot below frame), push 3 %, dusk grade (variant B)
    if os.path.exists(KCLIP["K17"]) and "K17" not in FALLBACK:
        b = kc(g, "K17", 0.0, 4.5, z=1.5, fx=0.42, fy=0.0)
        b = an.vpush(g, b, 1.0, 1.03, 0.5, 0.3)
    else:
        b = an.zp(g, g.still(A["title"]), 1.0, 1.03, 0.5, 0.5, 0.3, 0.3, curve="lin")
        b = an.clouds(g, b, 120)
    o = g.lab()
    g.add(f"[{b}]colorbalance=rs=-0.04:bs=0.06:rm=-0.03:bm=0.04[{o}]")
    b = o
    w = g.lab()
    g.add(f"[{a}]settb=AVTB,fps={FPS}[{w}a];[{b}]settb=AVTB,fps={FPS}[{w}b];[{w}a][{w}b]xfade=transition=custom:"
          f"duration=0.5:offset={L(1983) / FPS:.5f}:expr='if(gt(Y/H+0.06*sin(X/W*23)+0.03*sin(X/W*71),P*1.12),B,A)'[{w}]")
    s = w
    lw, lh = A["logo_wh"]
    li, lo = g.still(A["logo"]), g.lab()
    tl = L(1995) / FPS
    g.add(f"[{li}]format=rgba,setpts=PTS-STARTPTS,scale=w='2*trunc({lw}*(1+0.14*exp(-max(0,t-{tl:.4f})*9)*cos(max(0,t-{tl:.4f})*22))/2)':"
          f"h=-2:eval=frame,fade=t=in:st={tl:.4f}:d=0.17:alpha=1[{lo}l];"
          f"[{s}][{lo}l]overlay=x='(W-w)/2':y='H*0.30-h/2':eval=frame:enable='gte(n,{L(1995)})':shortest=1[{lo}]")
    s = lo
    di = g.still(A["drop"])
    t_g0, t_go = L(2016) / FPS, L(2040) / FPS
    ylow = int(H * 0.30 + lh / 2 - 34)
    x_main = int(W / 2 + lw * 0.17)
    o = g.lab()
    g.add(f"[{di}]format=rgba,split=3[{o}d1][{o}d2][{o}d3];"
          f"[{o}d1]scale=w='2*trunc(max(4,40*min(1,max(0,(t-{t_g0:.3f})/{t_go - t_g0:.3f})))/2)':h=-2:eval=frame[{o}m];"
          f"[{s}][{o}m]overlay=x={x_main}-w/2:y='{ylow}+if(gt(t,{t_go:.3f}),1500*pow(t-{t_go:.3f},2),0)':"
          f"eval=frame:enable='gte(t,{t_g0:.3f})':shortest=1[{o}x]")
    t_s0, t_f = L(2021) / FPS, L(2050) / FPS
    g.add(f"[{o}d2]scale=24:-2,colorchannelmixer=aa=0.4[{o}s1];[{o}d3]scale=20:-2,colorchannelmixer=aa=0.4[{o}s2];"
          f"[{o}x][{o}s1]overlay=x={int(W / 2 - lw * 0.33)}:y='{ylow - 50}+28*min(1,max(0,(t-{t_s0:.3f})/{t_f - t_s0:.3f}))"
          f"+if(gt(t,{t_f:.3f}),1500*pow(t-{t_f:.3f},2),0)':enable='gte(t,{t_s0:.3f})':shortest=1[{o}y];"
          f"[{o}y][{o}s2]overlay=x={int(W / 2 + lw * 0.40)}:y='{ylow - 60}+24*min(1,max(0,(t-{t_s0 + 0.2:.3f})/{t_f - t_s0:.3f}))"
          f"+if(gt(t,{t_f + 0.2:.3f}),1500*pow(t-{t_f + 0.2:.3f},2),0)':enable='gte(t,{t_s0 + 0.2:.3f})':shortest=1[{o}]")
    s = an.shake(g, o, [(L(1995), 6, 18)])
    o2 = g.lab()
    g.add(f"[{s}]trim=end_frame={g.n},format=yuv420p,setsar=1[{o2}]")
    return an.run_cut(g, o2, out)


def master():
    lst = f"{an.WK}/concat.txt"
    with open(lst, "w") as f:
        for c, _, _ in an.CUTS:
            f.write(f"file '{an.SEG}/{c}.mp4'\n")
    bug = f"{an.WK}/bug.txt"
    open(bug, "w").write("ANIME-STYLE · AI-ANIMATED")
    # audio: v2a 0-87.0 with the 86.5-87.0 fade, two-pass loudnorm to -14 LUFS / TP -1.5 (<= -1)
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
           "-frames:v", str(an.TOTAL), "-r", str(FPS), "-c:v", "libx264", "-preset", "slow", "-crf", "16",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-t", f"{an.TOTAL / FPS}",
           "-movflags", "+faststart", OUT]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr[-2000:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--no-final", action="store_true")
    a = ap.parse_args()
    os.makedirs(an.SEG, exist_ok=True)
    load_accept()
    assets()
    todo = [c for c, _, _ in an.CUTS if not a.only or c in a.only.split(",")]
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
    if errs:
        sys.exit(f"failed: {errs}")
    if not a.no_final:
        master()
        print("master", OUT)


if __name__ == "__main__":
    main()
