#!/usr/bin/env python3
"""Contact sheet of cuts 31-32 every 0.25 s (6 frames) for the keeper R4.2 check. $0.

  python3 -I op_contact_k13.py [video] [outdir]

Every tile is labelled with the master frame, time and cut; the cut boundaries 31c -> 32 (1763/1764) are always in.
"""
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from op_animatic import CUTS, FONT, FPS  # noqa: E402

VID = sys.argv[1] if len(sys.argv) > 1 else "/home/user/my_work/output/opening/S1_OP_v3.mp4"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/home/user/my_work/output/opening/contact_v3"
TW, TH, COLS = 480, 270, 4


def main():
    os.makedirs(OUT, exist_ok=True)
    cuts = {c: (s, n) for c, s, n in CUTS}
    a, b = cuts["31"][0], cuts["32"][0] + cuts["32"][1]
    idx = sorted(set(range(a, b, FPS // 4)) | {cuts["31c"][0] + cuts["31c"][1] - 1, cuts["32"][0]})
    sel = "+".join(f"eq(n\\,{i})" for i in idx)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", VID, "-vf", f"select='{sel}',scale={TW}:{TH}", "-vsync", "0",
                          "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True, check=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, TH, TW, 3)
    font = ImageFont.truetype(FONT, 16)

    def cut_of(n):
        return [c for c in ("31", "31b", "31c", "32") if cuts[c][0] <= n < cuts[c][0] + cuts[c][1]][0]
    per = 24
    outs = []
    for p in range(0, len(idx), per):
        chunk = list(zip(idx[p:p + per], fr[p:p + per]))
        rows = (len(chunk) + COLS - 1) // COLS
        im = Image.new("RGB", (COLS * TW, rows * (TH + 24)), (18, 18, 18))
        d = ImageDraw.Draw(im)
        for k, (n, f) in enumerate(chunk):
            x, y = (k % COLS) * TW, (k // COLS) * (TH + 24)
            im.paste(Image.fromarray(f), (x, y))
            d.text((x + 4, y + TH + 3), f"{cut_of(n)}  f{n}  {n / FPS:.2f}s", fill=(240, 240, 200), font=font)
        path = f"{OUT}/k13_31-32_sheet_{p // per + 1:02d}.png"
        im.save(path)
        outs.append(path)
    print("\n".join(outs))


if __name__ == "__main__":
    main()
