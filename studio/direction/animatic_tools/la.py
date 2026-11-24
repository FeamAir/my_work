#!/usr/bin/env python3
"""S01E01 animatic, step 4: limited-animation render of every shot, 1280x720, 24 fps (ffmpeg only, $0).

  python3 -I la.py [--scenes sc01,sc02] [--only id,...] [--force]

Per shot: frame -> camera move parsed from the LA code / camera column (L-01 push/pull, L-02 pan, L-03 tilt,
L-05 shake), overlays (L-06 rain, L-09 lantern flicker, L-11 rings), C/D start->end pose dissolve, D draft clip if
present (drafts/<id>_mm.mp4). Burned in: shot id + class (top-left) and the episode's on-screen text (drawtext,
never generated). Output: output/S01E01/animatic/la/<id>.mp4 (no audio).
"""
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys

ROOT = "/home/user/my_work"
A = f"{ROOT}/output/S01E01/animatic"
FR, LA, DR = f"{A}/frames", f"{A}/la", f"{A}/drafts"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
W, H, FPS = 1280, 720, 24

# on-screen text (drawtext): id -> list of (text, font, size, x, y, t_in)
TEXT = {
    "sc01-sh170": [("The Night of Still Water", SERIF, 34, "(w-tw)/2", "h*0.80", 2.0)],
    "sc02-sh010": [("IX", SERIF, 40, "w*0.80", "h*0.42", 0.0), ("Seventeen years later.", SERIF, 26, "w*0.05", "h*0.88", 0.8)],
    "sc05-sh100": [("HOLLOWSTONE", SERIF, 78, "(w-tw)/2", "(h-th)/2", 1.0)],
    "sc07-sh040": [("STEPS", SERIF, 22, "w*0.30", "h*0.30", 0.0), ("MIDS", SERIF, 22, "w*0.30", "h*0.42", 0.0),
                   ("LOWS", SERIF, 22, "w*0.30", "h*0.54", 0.0)],
    "sc13-sh150": [("ACCOUNT NINE", SERIF, 46, "(w-tw)/2", "h*0.30", 0.0)],
    "sc16-sh130": [("ACCOUNT NINE", SERIF, 46, "(w-tw)/2", "h*0.30", 0.0)],
    "sc14-sh040": [("1,470", SERIF, 64, "(w-tw)/2", "h*0.55", 0.0)],
    "sc14-sh050": [("1,740", SERIF, 64, "(w-tw)/2", "h*0.35", 0.0)],
}
RINGS = {"sc03-sh230": (0.42, 0.62), "sc20-sh160": (0.5, 0.55)}  # centre of rings, fraction of frame


def shots():
    return json.load(open(f"{A}/spec/shots.json"))["shots"]


def esc(t):
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace(",", "\\,")


def move(s):
    la, cam = s["la"] or "", (s["cam"] or "").lower()
    m = re.search(r"L-01\s*(отъезд\s*)?([0-9.]+)", la)
    if "L-05" in la:
        return ("shake", 0.0)
    if "L-03" in la or "подъём" in cam or "снизу вверх" in cam:
        return ("tilt", 0.0)
    if "L-02" in la or "панорама" in cam:
        return ("panL" if "справа налево" in cam else "panR", 0.0)
    if m:
        z = float(m.group(2))
        out = bool(m.group(1)) or "отъезд" in cam
        return ("out" if out else "in", min(z, 0.2))
    if "наезд" in cam:
        return ("in", 0.05)
    if "отъезд" in cam:
        return ("out", 0.05)
    return ("static", 0.0)


def cam_filter(kind, z, dur, tall, fit=False, fitcap=0.03):
    n = max(1, int(round(dur * FPS)))
    p = f"(on/{max(1, n - 1)})"
    e = f"(0.5-0.5*cos(PI*{p}))"
    base = "scale=2560:1440:force_original_aspect_ratio=increase,crop=2560:1440,setsar=1"
    if fit:  # tapestry panels / very wide strips: show the whole image on a dark ground (no crop)
        base = ("scale=2560:1440:force_original_aspect_ratio=decrease,pad=2560:1440:(ow-iw)/2:(oh-ih)/2:color=0x141210,"
                "setsar=1")
        kind = "in" if kind not in ("in", "out") else kind
        z = min(z or 0.03, fitcap)
    if tall and kind in ("tilt", "static", "in", "out"):
        # tall plate: tilt bottom -> top
        return (f"scale=2560:-2,setsar=1,zoompan=z=1:x=0:y='(ih-ih*{W}/{H}*0+0)*0+(ih-1440)*(1-{e})':d=1:s=2560x1440:fps={FPS},"
                f"scale={W}:{H}")
    if kind == "in":
        zz = f"1+{z}*{e}"
    elif kind == "out":
        zz = f"1+{z}*(1-{e})"
    elif kind in ("panR", "panL", "tilt"):
        zz = "1.18"
    elif kind == "shake":
        zz = "1.05"
    else:
        zz = "1"
    if kind == "panR":
        x, y = f"(iw-iw/zoom)*{e}", "(ih-ih/zoom)/2"
    elif kind == "panL":
        x, y = f"(iw-iw/zoom)*(1-{e})", "(ih-ih/zoom)/2"
    elif kind == "tilt":
        x, y = "(iw-iw/zoom)/2", f"(ih-ih/zoom)*(1-{e})"
    elif kind == "shake":
        x = "(iw-iw/zoom)/2+10*sin(2*PI*on/24*1.3)+5*sin(2*PI*on/24*3.7)"
        y = "(ih-ih/zoom)/2+7*sin(2*PI*on/24*1.1+1)"
    else:
        x, y = "(iw-iw/zoom)/2", "(ih-ih/zoom)/2"
    return f"{base},zoompan=z='{zz}':x='{x}':y='{y}':d=1:s=2560x1440:fps={FPS},scale={W}:{H}"


def label(s):
    t = f"S01E01 {s['id']} [{s['cls']}]"
    return (f"drawtext=fontfile={FONT}:text='{esc(t)}':x=14:y=10:fontsize=20:fontcolor=white:"
            f"box=1:boxcolor=black@0.5:boxborderw=5")


def texts(s):
    out = []
    for txt, font, size, x, y, tin in TEXT.get(s["id"], []):
        out.append(f"drawtext=fontfile={font}:text='{esc(txt)}':x={x}:y={y}:fontsize={size}:fontcolor=0xEDE6D6:"
                   f"shadowcolor=black@0.7:shadowx=2:shadowy=2:alpha='min(1,max(0,(t-{tin})/0.6))'")
    return out


def ensure_fx():
    os.makedirs(f"{A}/la_fx", exist_ok=True)
    rain = f"{A}/la_fx/rain_field.png"
    if not os.path.exists(rain):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
                        f"color=black:s={W}x{H},format=gray,geq=lum='if(gt(random(1),0.9975),255,0)',avgblur=sizeX=1:sizeY=16,lut=y='min(val*8\\,255)'",
                        "-frames:v", "1", "-update", "1", rain], check=True)
    for sid, (cx, cy) in RINGS.items():
        rm = f"{A}/la_fx/rings_{sid}.mp4"
        if not os.path.exists(rm):
            X, Y = int(640 * cx), int(360 * cy)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
                            f"color=black:s=640x360:r={FPS}:d=6,format=gray,geq=lum='clip(128+127*sin(hypot(X-{X}\\,(Y-{Y})*2.2)/5-T*9)*exp(-abs(hypot(X-{X}\\,(Y-{Y})*2.2)-T*70)/35)*exp(-T*0.3)\\,0\\,255)'",
                            "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", rm], check=True)
    return rain


def render(s, force=False):
    out = f"{LA}/{s['id']}.mp4"
    if os.path.exists(out) and not force:
        return s["id"], "skip"
    dur = s["dur"]
    src = s["reuse"] or s["id"]
    fa, fb = f"{FR}/{src}_a.png", f"{FR}/{src}_b.png"
    clip = f"{DR}/{s['id']}_mm.mp4"
    if s["id"] == "sc20-sh240" or not os.path.exists(fa):
        fa = None
    post = [label(s)] + texts(s)
    la = s["la"] or ""
    if "L-09" in la:
        post.insert(0, "eq=brightness='0.03*sin(2*PI*t*1.7)+0.02*sin(2*PI*t*5.3)':eval=frame")
    inputs, fc = [], []
    if os.path.exists(clip):
        inputs = ["-i", clip]
        fc.append(f"[0]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1,"
                  f"tpad=stop_mode=clone:stop_duration={dur},trim=duration={dur}[v0]")
    elif fa is None:
        inputs = ["-f", "lavfi", "-i", f"color=black:s={W}x{H}:r={FPS}:d={dur}"]
        fc.append("[0]null[v0]")
    else:
        from PIL import Image
        im = Image.open(fa)
        tall = im.height > im.width
        fit = (im.width / im.height > 2.0) or (s["scene"] == "sc05" and abs(im.width / im.height - 16 / 9) > 0.05)
        tall = tall and not fit
        kind, z = move(s)
        cap = 0.03
        if s.get("cam_override"):  # v3: e.g. sc05-sh080 slow pull-back on one tapestry panel
            kind, z = s["cam_override"]
            cap = z
        inputs = ["-loop", "1", "-framerate", str(FPS), "-t", str(dur), "-i", fa]
        fc.append(f"[0]{cam_filter(kind, z, dur, tall, fit, cap)},trim=duration={dur}[va]")
        if s["cls"] in "CD" and os.path.exists(fb):
            inputs += ["-loop", "1", "-framerate", str(FPS), "-t", str(dur), "-i", fb]
            fc.append(f"[1]{cam_filter(kind, z, dur, False)},trim=duration={dur}[vb]")
            off = max(0.3, dur * 0.5 - 0.3)
            fc.append(f"[va][vb]xfade=transition=fade:duration=0.6:offset={off:.2f},trim=duration={dur}[v0]")
        else:
            fc.append("[va]null[v0]")
    last = "v0"
    if "L-06" in la or (s["scene"] == "sc01" and "L-06" in la):
        rain = ensure_fx()
        k = len([x for x in inputs if x == "-i"])
        inputs += ["-loop", "1", "-framerate", str(FPS), "-t", str(dur), "-i", rain]
        fc.append(f"[{k}]format=gbrp,scroll=vertical=-0.05,rotate=a=0.12:fillcolor=black,format=gbrp[r];"
                  f"[{last}]format=gbrp[p];[p][r]blend=all_mode=screen:all_opacity=0.5[vr]")
        last = "vr"
    if s["id"] in RINGS:
        ensure_fx()
        k = len([x for x in inputs if x == "-i"])
        inputs += ["-i", f"{A}/la_fx/rings_{s['id']}.mp4"]
        fc.append(f"[{k}]scale={W}:{H},tpad=stop_mode=clone:stop_duration={dur},trim=duration={dur},format=gray,"
                  f"lut=y='128+(val-128)*0.12',format=yuv444p,split[rx][ry];[{last}]format=yuv444p[ra];"
                  f"[ra][rx][ry]displace=edge=smear[vg]")
        last = "vg"
    fc.append(f"[{last}]" + ",".join(post) + ",format=yuv420p[out]")
    cmd = ["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", ";".join(fc), "-map", "[out]",
                                                             "-t", str(dur), "-r", str(FPS), "-c:v", "libx264",
                                                             "-preset", "veryfast", "-crf", "23", "-an", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        return s["id"], "ERR " + r.stderr[-400:]
    return s["id"], "ok"


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--scenes")
    ap.add_argument("--only")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    os.makedirs(LA, exist_ok=True)
    ensure_fx()
    ss = shots()
    if a.scenes:
        ss = [s for s in ss if s["scene"] in a.scenes.split(",")]
    if a.only:
        ss = [s for s in ss if s["id"] in a.only.split(",")]
    with cf.ProcessPoolExecutor(a.workers) as ex:
        for sid, r in ex.map(render, ss, [a.force] * len(ss)):
            if r != "skip":
                print(sid, r, flush=True)
