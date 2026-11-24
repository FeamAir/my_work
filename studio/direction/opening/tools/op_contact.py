#!/usr/bin/env python3
"""Contact sheet for the OP animatic: the middle frame of every cut + the hit frames. $0.

  python3 -I op_contact.py [video]
"""
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, "/home/user/my_work/studio/direction/opening/tools")
from op_animatic import CUTS, FONT  # noqa: E402

VID = sys.argv[1] if len(sys.argv) > 1 else "/home/user/my_work/output/opening/S1_OP_animatic_v1.mp4"
OUT = "/home/user/my_work/output/opening/contact"
TW, TH = 384, 216
HITS = [(1368, "1368 last black"), (1369, "1369 INK / K01 f0"), (1371, "1371 impact"), (1657, "1657 INK S6"),
        (1765, "1765 glass 1"), (1801, "1801 glass 2"), (1837, "1837 glass 3"), (1873, "1873 glass 4"),
        (1981, "1981 INK last hit"), (1989, "1989 wipe"), (1995, "1995 logo lands"), (2040, "2040 drop leaves"),
        (2075, "2075 pre-fade"), (2087, "2087 last frame")]


def frames(idx):
    sel = "+".join(f"eq(n\\,{i})" for i in idx)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", VID, "-vf", f"select='{sel}',scale={TW}:{TH}", "-vsync", "0",
                          "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.uint8).reshape(-1, TH, TW, 3)
    return dict(zip(sorted(idx), a))


def sheet(items, cols, name):
    font = ImageFont.truetype(FONT, 15)
    rows = (len(items) + cols - 1) // cols
    im = Image.new("RGB", (cols * TW, rows * (TH + 22)), (20, 20, 20))
    fr = frames([i for i, _ in items])
    d = ImageDraw.Draw(im)
    for k, (i, t) in enumerate(items):
        x, y = (k % cols) * TW, (k // cols) * (TH + 22)
        im.paste(Image.fromarray(fr[i]), (x, y))
        d.text((x + 4, y + TH + 3), t, fill=(240, 240, 200), font=font)
    im.save(f"{OUT}/{name}")
    return f"{OUT}/{name}"


if __name__ == "__main__":
    mid = [(s + n // 2, f"{c}  f{s}-{s + n - 1}  mid {s + n // 2}") for c, s, n in CUTS]
    print(sheet(mid[:20], 5, "S1_OP_animatic_v1_contact_a.png"))
    print(sheet(mid[20:], 5, "S1_OP_animatic_v1_contact_b.png"))
    print(sheet(HITS, 5, "S1_OP_animatic_v1_hits.png"))
