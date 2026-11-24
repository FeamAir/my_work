#!/usr/bin/env python3
"""Saga OP v1.2 — vertical 9:16 teasers V1-V4 (marketer v1.1 report; board §7.3), $0, OpenCV + ffmpeg. NOT published.

  python3 -I op_saga_vertical_v12.py all  [--audio WAV]    # V1..V4 -> output/opening/vertical/
  python3 -I op_saga_vertical_v12.py sheet V2               # review sheet: first / mid / last frame of every cut, cropped

Source picture: the finished v1.2 picture WITHOUT the burned-in label (saga_c_build_v12/fin_logo.mov); the end card from
fin_textless.mov (C13 without the logo) + the logo layer rendered alone on transparent (seg/C13_logo_rgba.mov).
Crop: a 608 x 1080 window (x = its left edge), keyed per cut (linear between the keys inside a cut, a hard jump on the
cut), upscaled to 1080 x 1920 (Lanczos + light unsharp). "LB" = the 16:9 picture inside 9:16 on a blurred, darkened,
half-desaturated backing (panorama, the three pennants: board §7.3, keeper Q3). Safe frame x 60-940, y 250-1500.
End card (every teaser): C13 1981-2087 (the last hit, spray wipe, the logo lands, drains, glint, drop), the K17C plate
cropped at x = 656, the WHOLE word on one line, 760 px wide (board said ~560; wider reads better on a phone and stays
inside the safe frame), centre y 1173. Badge "AI-ANIMATED" top left (x 60, y 262), bold, white on a black box.
Audio: the same seconds of the OP mix + the logo hit 82.54-87.0, joined with a 20 ms crossfade on the cut.
"""
import argparse
import os
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import op_saga_build_c12 as b  # noqa: E402

an, sa = b.an, b.sa
FPS = an.FPS
VW, VH, CW = 1080, 1920, 608
OUTV = f"{an.OUTD}/vertical"
SRC = f"{b.WK}/fin_logo.mov"
SRC_TL = f"{b.WK}/fin_textless.mov"
LOGO_RGBA = f"{b.SEG}/C13_logo_rgba.mov"
CARD = (1981, 2087)
LOGO_W, LOGO_CY = 760, 1173

# V3 starts on 941 (0:39.21), not 0:38.8: no Gullmouth neighbour (marketer: Ossari only with the logo) and the
# B07a whip-in (936-940) is a blur, not a first frame.
# teaser -> (first frame, last frame, keys {cut: [x0, x1] | "LB"}); frames of the 87.0 s OP at 24 fps
T = {
    "V1": ("The Drop", 1272, 1475, {"B13c": [656], "B12d": [760], "B13d": [656], "B14": [600, 700], "B15": [656],
                                    "B16": [656], "C01a": "LB", "C01b": "LB", "C02": [640, 620], "C02L": [656]}),
    "V2": ("Raise your banner", 1440, 1655, {"C02": [640, 620], "C02L": [656], "C03": [820, 880], "C03L": [200],
                                             "C04": "LB", "C05": [620, 660], "C05L": [1180], "C06": [600, 640],
                                             "C06L": [640], "C07": [160, 240]}),
    "V3": ("Kite sky", 941, 1079, {"B07a": [656], "B08a": [656], "B07b": [656], "B08b": [656]}),
    "V4": ("Highwater groove", 288, 491, {"A06": [400], "A07": [656], "A08": [210], "A09": [656], "A10": [400],
                                          "A11": [0, 400]}),
}


def read_frames(path, f0, f1, rgba=False):
    """frames f0..f1 of a file as numpy (BGR, or BGRA for the logo layer)."""
    w, h = an.W, an.H
    pf = "bgra" if rgba else "bgr24"
    ch = 4 if rgba else 3
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"select='between(n\\,{f0}\\,{f1})'", "-vsync", "0",
                          "-f", "rawvideo", "-pix_fmt", pf, "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w, ch)


def upscale(win):
    up = cv2.resize(win, (VW, VH), interpolation=cv2.INTER_LANCZOS4)
    bl = cv2.GaussianBlur(up, (0, 0), 1.6)
    return cv2.addWeighted(up, 1.35, bl, -0.35, 0)


def crop_x(f, x):
    x = float(np.clip(x, 0, an.W - CW))
    M = np.float32([[1, 0, -x], [0, 1, 0]])                      # sub-pixel window position
    return cv2.warpAffine(f, M, (CW, an.H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)


def letterbox(f):
    # a colour field, not a picture: the frame shrunk to 9 x 16 and smoothed back up (no Spire shape survives in it)
    small = cv2.resize(f[:, (an.W - CW) // 2:(an.W + CW) // 2], (9, 16), interpolation=cv2.INTER_AREA)
    back = cv2.GaussianBlur(cv2.resize(small, (VW, VH), interpolation=cv2.INTER_CUBIC), (0, 0), 60).astype(np.float32)
    grey = cv2.cvtColor(cv2.cvtColor(back, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    back = (0.5 * back + 0.5 * grey) * 0.5
    fg = cv2.resize(f, (VW, int(round(VW * an.H / an.W))), interpolation=cv2.INTER_LANCZOS4)
    y0 = (VH - fg.shape[0]) // 2
    back[y0:y0 + fg.shape[0]] = fg
    return np.clip(back, 0, 255).astype(np.uint8)


def badge():
    p = f"{OUTV}/_badge.png"
    font = ImageFont.truetype(b.FONTB, 34)
    tw = font.getbbox(b.LABEL)
    w, h = tw[2] - tw[0] + 28, tw[3] - tw[1] + 22
    im = Image.new("RGBA", (w, h), (0, 0, 0, 110))
    ImageDraw.Draw(im).text((14 - tw[0], 11 - tw[1]), b.LABEL, font=font, fill=(255, 255, 255, 240))
    im.save(p)
    return np.asarray(im).astype(np.float32)


def put_badge(fr, bd, x=60, y=262):
    a = bd[..., 3:4] / 255.0
    roi = fr[y:y + bd.shape[0], x:x + bd.shape[1]].astype(np.float32)
    rgb = bd[..., [2, 1, 0]]
    fr[y:y + bd.shape[0], x:x + bd.shape[1]] = (roi * (1 - a) + rgb * a).astype(np.uint8)
    return fr


def body(name):
    title, f0, f1, keys = T[name]
    fr = read_frames(SRC, f0, f1)
    out = []
    for i, f in enumerate(fr):
        n = f0 + i
        c = sa.cut_of(n)
        k = keys[c]
        if k == "LB":
            out.append(letterbox(f))
            continue
        s0, ln = an.START[c], an.NFR[c]
        u = (n - s0) / max(1, ln - 1)
        x = k[0] if len(k) == 1 else k[0] + (k[1] - k[0]) * u
        out.append(upscale(crop_x(f, x)))
    return out


def end_card():
    bg = read_frames(SRC_TL, *CARD)
    lg = read_frames(LOGO_RGBA, *CARD, rgba=True)
    s = LOGO_W / 1300.0
    out = []
    for f, l in zip(bg, lg):
        v = upscale(crop_x(f, 656))
        # the logo layer (16:9, the word centred at x 960, y 660) -> scale s, word centre to (540, LOGO_CY)
        M = np.float32([[s, 0, 540 - 960 * s], [0, s, LOGO_CY - 660 * s]])
        L = cv2.warpAffine(l, M, (VW, VH), flags=cv2.INTER_AREA, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
        a = L[..., 3:4].astype(np.float32) / 255
        v = (v.astype(np.float32) * (1 - a) + L[..., :3].astype(np.float32) * a).astype(np.uint8)
        out.append(v)
    return out


def write(name, frames, audio):
    _, f0, f1, _ = T[name]
    os.makedirs(OUTV, exist_ok=True)
    bd = badge()
    dst = f"{OUTV}/SAGA_OP_v1_2_{name}_9x16.mp4"
    a0, a1 = f0 / FPS, (f1 + 1) / FPS
    c0, c1 = CARD[0] / FPS, (CARD[1] + 1) / FPS
    af = (f"[1:a]atrim={a0:.4f}:{a1 + 0.02:.4f},asetpts=PTS-STARTPTS[a];[1:a]atrim={c0 - 0.02:.4f}:{c1:.4f},asetpts=PTS-STARTPTS[b];"
          f"[a][b]acrossfade=d=0.02:c1=tri:c2=tri[ab]")
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{VW}x{VH}", "-r", str(FPS),
                          "-i", "-", "-i", audio, "-filter_complex", af, "-map", "0:v", "-map", "[ab]", "-c:v", "libx264",
                          "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest",
                          "-movflags", "+faststart", "-metadata", f"title=HOLLOWSTONE {name} {T[name][0]} (AI-animated, not published)",
                          "-metadata", "comment=AI-generated (Kling 2.5 TP, Nano Banana 2; music ElevenLabs); vertical teaser v1.2",
                          dst], stdin=subprocess.PIPE)
    for f in frames:
        p.stdin.write(put_badge(np.ascontiguousarray(f), bd).tobytes())
    p.stdin.close()
    if p.wait():
        raise RuntimeError(name)
    return dst


def sheet(name, frames=None):
    _, f0, f1, _ = T[name]
    frames = frames or body(name)
    idx = []
    for c, s, n in sa.CUTS:
        for f in sorted({s, s + n // 2, s + n - 1}):
            if f0 <= f <= f1:
                idx.append(f)
    tw, th = 216, 384
    cols = 9
    rows = (len(idx) + cols - 1) // cols
    im = Image.new("RGB", (cols * (tw + 4), rows * (th + 20)), (20, 20, 20))
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(an.FONT, 13)
    for k, f in enumerate(idx):
        x, y = (k % cols) * (tw + 4), (k // cols) * (th + 20)
        fr = cv2.cvtColor(cv2.resize(frames[f - f0], (tw, th), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2RGB)
        im.paste(Image.fromarray(fr), (x, y))
        d.rectangle((x + 60 * tw / VW, y + 250 * th / VH, x + 940 * tw / VW, y + 1500 * th / VH), outline=(0, 255, 0))
        d.text((x + 3, y + th + 2), f"f{f} {sa.cut_of(f)}", fill=(240, 230, 190), font=font)
    p = f"{OUTV}/_sheet_{name}.jpg"
    im.save(p, quality=86)
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["all", "sheet"])
    ap.add_argument("name", nargs="?")
    ap.add_argument("--audio", default=b.AUDIO, help="one audio input path (the OP mix)")
    a = ap.parse_args()
    os.makedirs(OUTV, exist_ok=True)
    if a.cmd == "sheet":
        print(sheet(a.name))
        return
    card = end_card()
    for name in ([a.name] if a.name else T):
        fr = body(name)
        sheet(name, fr)
        print(write(name, fr + card, a.audio), flush=True)


if __name__ == "__main__":
    main()
