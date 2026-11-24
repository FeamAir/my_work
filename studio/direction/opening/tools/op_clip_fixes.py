#!/usr/bin/env python3
"""S1 OP: $0 per-frame fixes on accepted Kling clips (ffmpeg pipe + numpy). Writes <id>_fix.mp4 next to the clip.

  python3 -I op_clip_fixes.py K03

  K03  the nine lanterns light up warm from ~frame 55 (Kling ignored "stay unlit", OP-3). Inside the lantern band
       (x 1000-1880, y 270-560 of the 1928x1072 clip) every warm or bright pane pixel (R-B excess over the band's
       own frame-0 level, or luma well above the fog) is pulled back to unlit dark glass, with a 1 px feather, and
       the warm haze around the panes is neutralised. Motion of the rope and lanterns is kept.
"""
import subprocess
import sys
import numpy as np
import cv2

CL = "/home/user/my_work/output/opening/clips"


def frames(path):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", path, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         stdout=subprocess.PIPE)
    w, h = 1928, 1072
    while True:
        b = p.stdout.read(w * h * 3)
        if len(b) < w * h * 3:
            break
        yield np.frombuffer(b, np.uint8).reshape(h, w, 3).copy()


def writer(path):
    return subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1928x1072",
                             "-r", "24", "-i", "-", "-c:v", "libx264", "-crf", "14", "-preset", "slow",
                             "-pix_fmt", "yuv420p", path], stdin=subprocess.PIPE)


def k03():
    x0, x1, y0, y1 = 1000, 1880, 270, 560
    out = writer(f"{CL}/K03_fix.mp4")
    base = None
    for f in frames(f"{CL}/K03.mp4"):
        reg = f[y0:y1, x0:x1].astype(float)
        warm = reg[..., 0] - reg[..., 2]
        L = reg.mean(2)
        if base is None:
            base = (float(np.median(warm)), float(np.median(L)))
        ex = np.clip((warm - base[0] - 6) / 18, 0, 1)
        br = np.clip((L - base[1] - 18) / 30, 0, 1) * np.clip((warm - base[0] + 2) / 10, 0, 1)
        sel = np.maximum(ex, br)
        sel = cv2.GaussianBlur(sel.astype(np.float32), (0, 0), 1.0)[..., None]
        glass = np.array([52, 58, 60], float) + 0.15 * (L[..., None] - base[1])
        cool = np.stack([L, L + 4, L + 6], -1) * 0.8
        tgt = np.where(sel > 0.5, glass, cool)
        f[y0:y1, x0:x1] = np.clip(reg * (1 - sel) + tgt * sel, 0, 255).astype(np.uint8)
        out.stdin.write(f.tobytes())
    out.stdin.close()
    out.wait()


if __name__ == "__main__":
    for k in sys.argv[1:]:
        {"K03": k03}[k]()
        print(k, "fixed")
