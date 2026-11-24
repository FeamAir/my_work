#!/usr/bin/env python3
"""S1 OP: acceptance sheets for Kling clips ($0). Every 10th frame of each clip (frames 0, 10, 20 ... 120) is
extracted with ffmpeg and laid out 4 across with its frame number: output/opening/clips/_review/<id>.png.

  python3 -I op_clip_review.py K01 K03 ...
"""
import os
import subprocess
import sys
from PIL import Image, ImageDraw, ImageFont

CL = "/home/user/my_work/output/opening/clips"
RV = f"{CL}/_review"
FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)


def sheet(name):
    d = f"{RV}/{name}"
    os.makedirs(d, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{CL}/{name}.mp4", "-vf", "select='not(mod(n\\,10))'",
                    "-vsync", "vfr", f"{d}/f%03d.png"], check=True)
    fs = sorted(os.listdir(d))
    tw, th = 480, 267
    cols = 4
    out = Image.new("RGB", (cols * tw, ((len(fs) + cols - 1) // cols) * th))
    for i, f in enumerate(fs):
        im = Image.open(f"{d}/{f}").convert("RGB").resize((tw, th))
        ImageDraw.Draw(im).text((6, 4), str(i * 10), fill=(255, 255, 0), font=FONT)
        out.paste(im, ((i % cols) * tw, (i // cols) * th))
    out.save(f"{RV}/{name}.png")
    print(name, len(fs), "frames checked")


if __name__ == "__main__":
    for n in sys.argv[1:]:
        sheet(n)
