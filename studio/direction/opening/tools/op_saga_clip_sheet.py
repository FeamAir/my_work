#!/usr/bin/env python3
"""Clip acceptance sheets for step K ($0): every 10th frame of a Kling take, with the source frame first, fps and
frame count, and the frame-difference energy trace (a jump = a cut or a morph; a flat zero tail = a freeze).

  python3 -I op_saga_clip_sheet.py KA01_t1 [KW02_t1 ...]     # -> output/opening/saga_c/clips/sheets/<take>.jpg
"""
import json
import os
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = "/home/user/my_work/output/opening/saga_c"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def sheet(take):
    mp4 = f"{OUT}/clips/{take}.mp4"
    meta = json.load(open(f"{OUT}/clips/{take}.json"))
    fps = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate,width,height",
                          "-of", "csv=p=0", mp4], capture_output=True, text=True).stdout.strip()
    cap = cv2.VideoCapture(mp4)
    frames, e, prev = [], [], None
    while True:
        ok, f = cap.read()
        if not ok:
            break
        frames.append(f)
        g = cv2.cvtColor(cv2.resize(f, (480, 270)), cv2.COLOR_BGR2GRAY).astype(np.float32)
        e.append(0.0 if prev is None else float(np.abs(g - prev).mean()))
        prev = g
    TW, TH = 384, 216
    idx = list(range(0, len(frames), 10))
    if idx[-1] != len(frames) - 1:
        idx.append(len(frames) - 1)
    tiles = [("source", cv2.cvtColor(np.asarray(Image.open(os.path.join("/home/user/my_work", meta["source"])).convert("RGB")), cv2.COLOR_RGB2BGR))]
    tiles += [(f"f{i} {i / 24:.2f}s", frames[i]) for i in idx]
    cols = 5
    rows = (len(tiles) + cols - 1) // cols
    im = Image.new("RGB", (cols * (TW + 4), rows * (TH + 18) + 150), (16, 16, 16))
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT, 13)
    for k, (lab, f) in enumerate(tiles):
        x, y = (k % cols) * (TW + 4), (k // cols) * (TH + 18)
        im.paste(Image.fromarray(cv2.cvtColor(cv2.resize(f, (TW, TH), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2RGB)), (x, y))
        d.text((x + 3, y + TH + 2), lab, fill=(240, 230, 190), font=font)
    y0 = rows * (TH + 18) + 10
    ea = np.array(e)
    mx = max(ea.max(), 1e-6)
    gw = im.width - 20
    for i, v in enumerate(ea):
        x = 10 + int(i / max(len(ea) - 1, 1) * gw)
        d.line([(x, y0 + 110), (x, y0 + 110 - int(100 * v / mx))], fill=(120, 200, 255), width=3)
    d.text((10, y0 + 115), f"{take}  {fps}  {len(frames)} frames  energy max {mx:.2f} @ f{int(ea.argmax())}  "
           f"median {np.median(ea[1:]):.2f}  zero-diff frames {int((ea[1:] < 0.05).sum())}", fill=(240, 230, 190), font=font)
    os.makedirs(f"{OUT}/clips/sheets", exist_ok=True)
    p = f"{OUT}/clips/sheets/{take}.jpg"
    im.save(p, quality=85)
    return p, {"take": take, "fps": fps, "frames": len(frames), "e_max": round(float(mx), 2), "e_argmax": int(ea.argmax()),
               "e_median": round(float(np.median(ea[1:])), 2), "zero_diff": int((ea[1:] < 0.05).sum())}


if __name__ == "__main__":
    for t in sys.argv[1:]:
        p, info = sheet(t)
        print(p, json.dumps(info))
