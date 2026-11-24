#!/usr/bin/env python3
"""Saga OP v1.2 — frames for the keeper ($0): every changed frame family -> output/opening/v1_2_lore/.
  hook_f0000 … : first / middle / last frame of A01a-A04b (full size, from the master) + hook_0-215_sheet.jpg (every 6th)
  whip_f0928 … whip_f0943 : the B06b -> B07a whip, every frame (full size) + whip_sheet.jpg
  V1_*/V2_*   : first / middle / last frame of every cut of the vertical teasers V1 and V2 (1080x1920, as delivered)
                + V1_sheet.jpg / V2_sheet.jpg; endcard_*: the vertical logo end card (4 frames)
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


def main():
    os.makedirs(D, exist_ok=True)
    m = b.OUT
    hook = sorted({f for c, s, n in sa.CUTS if s < 216 for f in (s, s + n // 2, s + n - 1)})
    grab(m, hook, "hook_f{f:04d}.png")
    sheet(m, list(range(0, 216, 6)), "hook_0-215_sheet.jpg")
    whip = list(range(928, 944))
    grab(m, whip, "whip_f{f:04d}.png")
    sheet(m, whip, "whip_928-943_sheet.jpg", cols=8)
    grab(m, [2028], "C13_f{f:04d}_v1_2.png")
    for name in ("V1", "V2"):
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
    print(D)


if __name__ == "__main__":
    main()
