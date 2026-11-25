#!/usr/bin/env python3
"""Saga OP v1.2 — frames for the keeper ($0): every changed frame family -> output/opening/v1_2_lore/.
  hook_f0000 … : first / middle / last frame of A01a-A04b (full size, from the master) + hook_0-215_sheet.jpg (every 6th)
  whip_f0928 … whip_f0943 : the B06b -> B07a whip, every frame (full size) + whip_sheet.jpg
  V1_*..V4_*  : first / middle / last frame of every cut of the vertical teasers V1-V4 (1080x1920, as delivered)
                + V*_sheet.jpg; V*_endcard_*: the vertical logo end card (4 frames)
  finish_*    : the unified finish, before | after at 1:1 (960x540 centre crop of prefinish.mp4 | the master), 2D-painted
                and 3D-render shots, the Spire frames 1369 / 1657 / 1981 + finish_sheet.jpg
  C13_f2028_v1_2.png : the logo hold (no own logo scale any more, И10), for comparison with v1.1
    python3 -I op_saga_lore_v12.py"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import op_saga_build_c12 as b  # noqa: E402

an, sa = b.an, b.sa
D = f"{an.OUTD}/v1_2_lore"
V = f"{an.OUTD}/vertical"


def grab(src, frames, pattern):
    sel = "+".join(f"eq(n\\,{f})" for f in frames)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", f"select='{sel}'", "-vsync", "0", "-start_number", "0",
                    f"{D}/_tmp_%04d.png"], check=True)
    for k, f in enumerate(sorted(frames)):
        os.replace(f"{D}/_tmp_{k:04d}.png", f"{D}/{pattern.format(f=f)}")


def sheet(src, frames, out, w=480, cols=6):
    sel = "+".join(f"eq(n\\,{f})" for f in frames)
    rows = (len(frames) + cols - 1) // cols
    h = int(w * (1920 / 1080 if "9x16" in src else 1080 / 1920)) // 2 * 2
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf",
                    f"select='{sel}',scale={w}:{h},drawtext=fontfile={an.FONT}:text='f%{{n}}':x=6:y=6:fontsize=16:fontcolor=yellow:box=1:boxcolor=black@0.5,"
                    f"tile={cols}x{rows}", "-frames:v", "1", "-vsync", "0", f"{D}/{out}"], check=True)


FINISH = [(30, "A01a wheel rim (2D)"), (60, "A01b wheels, crisp -> blur b2"), (530, "B01a Highwater fog (2D)"),
          (830, "B05a mole (3D)"), (1020, "B07b kites (2D, soft -> unsharp u1)"), (1200, "B13a pikes (3D, b2)"),
          (1369, "C01a INK, all Spires"), (1530, "C04 pennants (flat, u2)"), (1657, "C08 INK, fleet (3D)"),
          (1940, "C12a KW13 towers"), (1981, "C13 INK, logo lands")]


def one(src, f):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{f / an.FPS:.5f}", "-i", src, "-frames:v", "1", "-f", "rawvideo",
                          "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
    import numpy as np
    return np.frombuffer(raw, np.uint8).reshape(an.H, an.W, 3)


def finish_pairs():
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    pre = f"{b.WK}/prefinish.mp4"
    font = ImageFont.truetype(an.FONT, 22)
    tiles = []
    for f, what in FINISH:
        a, c = one(pre, f), one(b.OUT, f)
        y0, x0 = (an.H - 540) // 2, (an.W - 960) // 2
        im = Image.fromarray(np.concatenate([a[y0:y0 + 540, x0:x0 + 960], np.full((540, 8, 3), 255, np.uint8),
                                             c[y0:y0 + 540, x0:x0 + 960]], 1))
        d = ImageDraw.Draw(im)
        d.text((10, 8), f"f{f} {what} | BEFORE (no finish)", fill=(255, 255, 0), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
        d.text((978, 8), "AFTER (v1.2 finish)", fill=(255, 255, 0), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
        im.save(f"{D}/finish_f{f:04d}.png")
        tiles.append(im.resize((964, 270)))
    sh = Image.new("RGB", (964, 270 * len(tiles)))
    for k, t in enumerate(tiles):
        sh.paste(t, (0, 270 * k))
    sh.save(f"{D}/finish_sheet.jpg", quality=88)


def main():
    os.makedirs(D, exist_ok=True)
    m = b.OUT
    finish_pairs()
    if os.path.exists(f"{D}/whip_928-943_sheet.jpg") and "--all" not in sys.argv:
        hook_done = True
    else:
        hook_done = False
    if not hook_done:
        _hook(m)
    for name in ("V1", "V2", "V3", "V4"):
        _vertical(name)
    print(D)


def _hook(m):
    hook = sorted({f for c, s, n in sa.CUTS if s < 216 for f in (s, s + n // 2, s + n - 1)})
    grab(m, hook, "hook_f{f:04d}.png")
    sheet(m, list(range(0, 216, 6)), "hook_0-215_sheet.jpg")
    whip = list(range(928, 944))
    grab(m, whip, "whip_f{f:04d}.png")
    sheet(m, whip, "whip_928-943_sheet.jpg", cols=8)
    grab(m, [2028], "C13_f{f:04d}_v1_2.png")


def _vertical(name):
    for old in os.listdir(D):
        if old.startswith(name + "_"):
            os.remove(f"{D}/{old}")
    if True:
        _, f0, f1, _ = __import__("op_saga_vertical_v12").T[name]
        src = f"{V}/SAGA_OP_v1_2_{name}_9x16.mp4"
        loc = set()
        for c, s, n in sa.CUTS:
            for f in (s, s + n // 2, s + n - 1):
                if f0 <= f <= f1:
                    loc.add(f - f0)
        loc = sorted(loc | {0})
        grab(src, loc, name + "_t{f:04d}.png")
        sheet(src, loc, f"{name}_sheet.jpg", w=270, cols=10)
        n_body = f1 - f0 + 1
        grab(src, [n_body, n_body + 12, n_body + 47, n_body + 100], name + "_endcard_t{f:04d}.png")


if __name__ == "__main__":
    main()
