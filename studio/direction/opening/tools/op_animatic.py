#!/usr/bin/env python3
"""S1 OP animatic v1 ($0, ffmpeg + PIL only, no API calls). Storyboard v1.3, 87.0 s, 24 fps, 1920x1080.

  python3 -I op_animatic.py [--only 25,31] [--jobs 4] [--no-final]

Builds every cut of `studio/direction/opening/S1_OP_storyboard.md` v1.3 §4 from existing plates and frames.
A new NB2 frame or a Kling clip that does not exist yet is stood in by a placeholder still (a reference plate
or a drawn card), labelled small in the top-left corner; the ffmpeg passes of §3 (PUSH/PAN/TILT, PX-lite,
RAIN, SPRAY, MIST, DUST, CLOUD, SHAKE, POP, INK, WHIP, ROT, GLASS, WIPE, logo, drops) are applied so that
rhythm and sync can be checked. Hit frames per §2.1 (0-based frame index of the 87.0 s master).

Inputs: refs plates, two S01E01 animatic frames, the video-test alley clip, the harbour plates prepared by
op_harbour_plates.py (run it first), music output/music/lib_mus_theme-op-drums_v2a.mp3.
Output: output/opening/S1_OP_animatic_v1.mp4 (+ work files in output/opening/animatic_work/).
"""
import argparse
import concurrent.futures as cf
import math
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = "/home/user/my_work"
REF = f"{ROOT}/studio/direction/refs"
ANI = f"{ROOT}/output/S01E01/animatic/frames"
OUTD = f"{ROOT}/output/opening"
WK = f"{OUTD}/animatic_work"
SEG = f"{WK}/seg"
MUSIC = f"{ROOT}/output/music/lib_mus_theme-op-drums_v2a.mp3"
ALLEY = f"{ROOT}/output/video_test/alley__kling-2.5-turbo-pro.mp4"
H1 = f"{OUTD}/plates/D09_H1_op.png"
H2 = f"{OUTD}/plates/D09_H2_op.png"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
W, H, FPS = 1920, 1080, 24
TOTAL = 2088                      # 87.0 s x 24
FADE_ST, FADE_D = 86.5, 0.5       # picture and audio fade, 1:26.5-1:27.0
RAIN_A = 0.22                     # one rain angle for all storm cuts 25-30 (wind from screen left)

# ------------------------------------------------------------------------------------------- cut list ---
# id, first frame (grid), frames, label. Hits are absolute placed frames (§2.1) and are converted to local.
CUTS = [
    ("01", 0, 72), ("02", 72, 36), ("02b", 108, 36), ("03", 144, 72), ("04", 216, 72),
    ("05", 288, 36), ("06", 324, 36), ("07", 360, 72), ("08", 432, 36), ("09", 468, 36),
    ("10", 504, 72), ("11", 576, 72), ("12", 648, 72), ("13", 720, 36), ("13b", 756, 36),
    ("14", 792, 72), ("15", 864, 72), ("16", 936, 72), ("17", 1008, 72), ("18", 1080, 72),
    ("19", 1152, 36), ("20", 1188, 36), ("21", 1224, 36), ("22", 1260, 36), ("23", 1296, 36),
    ("24", 1332, 28), ("24b", 1360, 9), ("25", 1369, 71), ("26", 1440, 36), ("27", 1476, 36),
    ("28", 1512, 36), ("29", 1548, 36), ("30", 1584, 72), ("31", 1656, 36), ("31b", 1692, 36),
    ("31c", 1728, 36), ("32", 1764, 144), ("32b", 1908, 72), ("33", 1980, 108),
]
START = {c: s for c, s, n in CUTS}
NFR = {c: n for c, s, n in CUTS}
assert sum(n for _, _, n in CUTS) == TOTAL
assert all(CUTS[i][1] + CUTS[i][2] == CUTS[i + 1][1] for i in range(len(CUTS) - 1))

INK_FRAMES = (1369, 1657, 1981)   # the three INK hits; each INK lasts 2 frames from these


def loc(cut, absf):
    return absf - START[cut]


# --------------------------------------------------------------------------------------- assets (PIL) ---
def cover(im, w=W, h=H, fx=0.5, fy=0.5):
    """scale to cover w x h and crop at fractional position."""
    s = max(w / im.width, h / im.height)
    im = im.resize((max(w, round(im.width * s)), max(h, round(im.height * s))), Image.LANCZOS)
    x, y = round((im.width - w) * fx), round((im.height - h) * fy)
    return im.crop((x, y, x + w, y + h))


def save(im, name):
    p = f"{WK}/{name}"
    im.save(p)
    return p


def field_points(w, h, density, blur, gain, seed, streak=0):
    rng = np.random.default_rng(seed)
    a = (rng.random((h, w)) > 1 - density).astype(np.float32) * 255
    if streak:
        k = np.ones(streak, np.float32) / streak
        a = np.apply_along_axis(lambda c: np.convolve(c, k, mode="same"), 0, a)
    im = Image.fromarray(np.clip(a * gain, 0, 255).astype(np.uint8), "L")
    if blur:
        im = im.filter(ImageFilter.GaussianBlur(blur))
        a = np.asarray(im, np.float32)
        im = Image.fromarray(np.clip(a * gain, 0, 255).astype(np.uint8), "L")
    return im


def noise_field(w, h, cells, blur, seed, contrast=2.0, bright=0.0):
    rng = np.random.default_rng(seed)
    small = Image.fromarray((rng.random((cells[1], cells[0])) * 255).astype(np.uint8), "L")
    im = small.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(blur))
    a = np.asarray(im, np.float32) / 255.0
    a = np.clip((a - 0.5) * contrast + 0.5 + bright, 0, 1)
    return Image.fromarray((a * 255).astype(np.uint8), "L")


def storm_card(kind):
    """Drawn placeholder for frames that have no plate yet (F01a, F01, F27, F30): sky, sea, dike or mole."""
    rng = np.random.default_rng({"F01a": 1, "F01": 2, "F27": 3, "F30": 4}[kind])
    yy = np.linspace(0, 1, H)[:, None]
    sky = np.array([118, 126, 128]) * (1 - yy) + np.array([86, 94, 98]) * yy
    img = np.ones((H, W, 3)) * sky[:, None, :].reshape(H, 1, 3)
    hor = 0.42 if kind != "F30" else 0.55
    sea_y = int(H * hor)
    n = np.asarray(noise_field(W, H, (240, 40), 2, 7, 1.4), float)[..., None] / 255.0
    sea = np.array([40, 58, 56]) + 22 * (n - 0.5)
    img[sea_y:] = sea[sea_y:]
    clouds = np.asarray(noise_field(W, H, (24, 14), 30, 11, 2.2), float)[..., None] / 255.0
    img[:sea_y] = img[:sea_y] * (0.75 + 0.35 * clouds[:sea_y])
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im)
    if kind in ("F01a", "F01"):
        # dike face on the right: a dark brick slope from the bottom edge to above mid-frame, dry top edge
        d.polygon([(1180, H), (1330, 380), (W, 380), (W, H)], fill=(62, 52, 48))
        for yb in range(400, H, 26):
            d.line([(1330 - (yb - 380) * 150 / 700, yb), (W, yb)], fill=(48, 40, 37), width=2)
        d.line([(1330, 380), (W, 380)], fill=(120, 112, 104), width=6)
        if kind == "F01a":   # the wave fills the left half
            d.polygon([(0, H), (0, 360), (300, 300), (620, 330), (900, 470), (1000, H)], fill=(34, 52, 50))
            d.polygon([(300, 300), (620, 330), (900, 470), (760, 410), (520, 360)], fill=(190, 196, 192))
        else:                # spray column rising from the face
            col = Image.new("L", (W, H), 0)
            ImageDraw.Draw(col).ellipse((980, -120, 1480, 900), fill=235)
            col = col.filter(ImageFilter.GaussianBlur(60))
            im = Image.composite(Image.new("RGB", (W, H), (214, 218, 216)), im, col)
    elif kind == "F27":      # the seaward end of a mole, spray thrown up and falling back seaward
        d.polygon([(900, H), (1100, 520), (W, 520), (W, H)], fill=(92, 92, 90))
        d.line([(1100, 520), (W, 520)], fill=(140, 140, 136), width=5)
        col = Image.new("L", (W, H), 0)
        ImageDraw.Draw(col).ellipse((700, 120, 1160, 760), fill=220)
        col = col.filter(ImageFilter.GaussianBlur(55))
        im = Image.composite(Image.new("RGB", (W, H), (208, 212, 210)), im, col)
    return im


def make_assets():
    os.makedirs(SEG, exist_ok=True)
    A = {}
    # effect fields
    A["rain_far"] = save(field_points(W, H, 0.0016, 0, 6, 1, streak=14), "rain_far.png")
    A["rain_near"] = save(field_points(W, H, 0.0010, 0, 9, 2, streak=40), "rain_near.png")
    A["drops"] = save(field_points(W, H, 0.0007, 2.2, 14, 3), "drops.png")
    A["dust"] = save(field_points(W, H, 0.00015, 3, 25, 4), "dust.png")
    A["fog"] = save(noise_field(2 * W, H, (96, 27), 40, 5, 2.2, -0.1), "fog.png")
    A["clouds"] = save(noise_field(3 * W, H, (18, 4), 70, 6, 2.0).point(lambda v: 255 - int(0.22 * (255 - v))),
                       "clouds.png")   # multiply layer, 28 % depth
    # ripple maps (K13 stand-in, L-10): horizontal wave bands, 128 = no shift
    yy, xx = np.mgrid[0:H, 0:2 * W]
    nz = np.asarray(noise_field(2 * W, H, (64, 36), 12, 8, 1.0), float) / 255.0
    A["rip_x"] = save(Image.fromarray((128 + 5 * np.sin(yy / 5.0 + 6 * nz)).astype(np.uint8), "L"), "rip_x.png")
    A["rip_y"] = save(Image.fromarray((128 + 3 * np.sin(xx / 37.0 + yy / 9.0 + 5 * nz)).astype(np.uint8), "L"), "rip_y.png")
    water = Image.new("L", (W, H), 0)
    ImageDraw.Draw(water).rectangle((0, int(H * 0.165), W, H), fill=255)
    A["water"] = save(water.filter(ImageFilter.GaussianBlur(6)), "water_mask.png")

    # plates (1920x1080 cover crops unless noted)
    A["F01a"] = save(storm_card("F01a"), "ph_F01a.png")
    A["F01"] = save(storm_card("F01"), "ph_F01.png")
    A["F27"] = save(storm_card("F27"), "ph_F27.png")
    A["F30"] = save(storm_card("F30"), "ph_F30.png")
    c1 = Image.open(f"{REF}/PL-0008/D02_C1_dawn-ebb_v1.png").convert("RGB")
    c3 = Image.open(f"{REF}/PL-0008/D02_C3_dusk_v1.png").convert("RGB")
    A["F04"] = save(cover(c1.crop((0, 90, 620, 439))), "ph_F04.png")               # left houses, no gate
    A["F11"] = save(cover(c1.crop((380, 400, 1000, 749))), "ph_F11.png")           # pilings / silt, no gate
    A["F26"] = save(cover(c3.crop((288, 470, 888, 768)), fy=1.0), "ph_F26.png")     # planks, lamps out of frame
    A["F28"] = save(cover(c3.crop((330, 130, 1046, 533))), "ph_F28.png")           # canal, lamps out of frame
    da = Image.open(f"{REF}/PL-0004/D01_A_dawn-ebb_v1.png").convert("RGB")      # portrait 768x1376
    A["D01A_tall"] = save(da.resize((W, round(da.height * W / da.width)), Image.LANCZOS), "D01A_tall.png")
    A["F10"] = save(cover(da.crop((0, 700, 768, 1132))), "ph_F10.png")
    A["F15"] = save(cover(Image.open(f"{REF}/PL-0004/D01_C_late-aft_v1.png").convert("RGB")), "ph_F15.png")
    A["W1"] = save(cover(Image.open(f"{REF}/PL-0008W/D05_W1_morning_v1.png").convert("RGB")), "W1.png")
    A["W2"] = save(cover(Image.open(f"{REF}/PL-0008W/D05_W2_morning_v1.png").convert("RGB")), "W2.png")
    A["S1la"] = save(cover(Image.open(f"{REF}/PL-0014/D08_S1_late-aft_v1.png").convert("RGB")), "S1la.png")
    dusk = Image.open(f"{REF}/PL-0014/D08_S1_dusk_v1.png").convert("RGB")
    A["title"] = save(cover(dusk.crop((230, 0, 1146, 515))), "title_plate.png")    # crown + upper shaft, foot out
    A["map"] = save(cover(Image.open(f"{REF}/M-MAP/E05_map_base_v1.png").convert("RGB")), "map.png")
    A["P2"] = save(Image.open(f"{REF}/TAPESTRY/E06_panel2_v1.png").convert("RGB").resize((2546, 1080), Image.LANCZOS),
                   "panel2_wide.png")
    A["P5"] = save(cover(Image.open(f"{REF}/TAPESTRY/E06_panel5_v1.png").convert("RGB")), "panel5.png")
    bell = Image.open(f"{ANI}/sc16-sh040_a.png").convert("RGB").crop((0, 120, 960, 660))   # lit desk lamps out
    A["bell"] = save(cover(bell), "bell.png")

    # 13: hall, relay-stone cage above the far door painted out (rows interpolated), balance kept
    hall = np.asarray(Image.open(f"{REF}/PL-0011/D11_L1_late-aft_v1.png").convert("RGB"), float).copy()
    x0, x1, y0, y1 = 615, 688, 86, 178
    for x in range(x0, x1):
        top, bot = hall[y0 - 2, x], hall[y1 + 1, x]
        for y in range(y0, y1):
            t = (y - y0) / (y1 - y0)
            hall[y, x] = (1 - t) * top + t * bot
    hall_im = Image.fromarray(hall.astype(np.uint8))
    A["hall"] = save(cover(hall_im), "hall.png")
    A["hall13b"] = save(cover(hall_im.crop((60, 330, 60 + 700, 330 + 394))), "hall13b.png")

    # 05: wheel plate (1344x768) at source size; ROT done in ffmpeg on a square around the hub
    A["wheel"] = f"{ANI}/sc06-sh010_a.png"

    # 14: ledger + coin stack (placeholder F14); text softened (OP-10), tally stroke for variant A (E1)
    led = Image.open(f"{REF}/M-LEDGER/E12_ledger_page-a_v1.png").convert("RGB").filter(ImageFilter.GaussianBlur(2.2))
    led = cover(led)
    d = ImageDraw.Draw(led)
    for i in range(9):   # fallen coins to the right
        cx, cy = 1350 + (i % 3) * 120 + (i // 3) * 35, 520 + (i // 3) * 95
        d.ellipse((cx - 48, cy - 30, cx + 48, cy + 30), fill=(150, 88, 52), outline=(90, 50, 30), width=4)
    d.line([(250, 330), (262, 470)], fill=(24, 22, 26), width=16)                  # one bold tally stroke (E1)
    A["F14"] = save(led, "ph_F14.png")
    coin = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    ImageDraw.Draw(coin).ellipse((4, 4, 196, 196), fill=(176, 104, 60, 255), outline=(96, 52, 30, 255), width=10)
    A["coin"] = save(coin, "coin.png")

    # heraldry cards (placeholders F17, F19, F21): emblems from refs/HERALDRY on banner shapes
    def banner(emb, w, h):
        b = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        m = Image.new("L", (w, h), 0)
        ImageDraw.Draw(m).polygon([(0, 0), (w, 0), (w, int(h * 0.82)), (0, h)], fill=255)   # slanted cut, point at pole (left)
        e = Image.open(f"{REF}/HERALDRY/{emb}.png").convert("RGB").resize((w, w))
        bg = Image.new("RGB", (w, h), e.getpixel((6, 6)))
        bg.paste(e, (0, (h - w) // 2 - int(h * 0.05)))
        b.paste(bg, (0, 0), m)
        return b

    def sky_wall(wall_y):
        yy = np.linspace(0, 1, H)[:, None, None]
        img = np.array([150, 176, 196]) * (1 - yy) + np.array([214, 196, 160]) * yy
        img = np.repeat(img, W, 1)
        img[wall_y:] = np.array([146, 128, 104])
        return Image.fromarray(img.astype(np.uint8))

    f17 = sky_wall(860)
    for i, e in enumerate(["H01_corvane", "H02_dusk", "H08_choir", "H07_lantry", "H06_fennike"]):
        bx = 120 + i * 360
        ImageDraw.Draw(f17).line([(bx, 60), (bx, 900)], fill=(60, 48, 40), width=8)
        f17.paste(b := banner(e, 220, 640), (bx + 6, 90), b)
    A["F17"] = save(f17, "ph_F17.png")
    for name, pair in (("F19", ("H01_corvane", "H02_dusk")), ("F21", ("H07_lantry", "H06_fennike"))):
        im = sky_wall(H)
        for i, e in enumerate(pair):
            b = banner(e, 900, 1240)
            im.paste(b, (40 + i * 960, -80), b)
        A[name] = save(im, f"ph_{name}.png")

    # harbour: sky band from H2 on H1 (cut 32 starts with the H2 sky, pixel-aligned)
    h1 = Image.open(H1).convert("RGB").resize((W, H), Image.LANCZOS)
    h2 = Image.open(H2).convert("RGB").resize((W, H), Image.LANCZOS)
    A["H1"] = save(h1, "H1_1080.png")
    A["H2"] = save(h2, "H2_1080.png")
    sky = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sky).rectangle((0, 0, W, int(H * 0.15)), fill=255)
    A["H1sky"] = save(Image.composite(h2, h1, sky.filter(ImageFilter.GaussianBlur(5))), "H1_skyH2_1080.png")

    # logo + drops
    font = ImageFont.truetype(SERIF_B, 150)
    txt = "HOLLOWSTONE"
    bb = font.getbbox(txt)
    lw, lh = bb[2] - bb[0] + 40, bb[3] - bb[1] + 40
    logo = Image.new("RGBA", (lw, lh), (0, 0, 0, 0))
    ImageDraw.Draw(logo).text((20 - bb[0], 20 - bb[1]), txt, font=font, fill=(232, 226, 210, 255),
                              stroke_width=5, stroke_fill=(16, 22, 34, 255))
    A["logo"] = save(logo, "logo.png")
    A["logo_wh"] = (lw, lh)
    drop = Image.new("RGBA", (40, 60), (0, 0, 0, 0))
    dd = ImageDraw.Draw(drop)
    dd.ellipse((6, 18, 34, 56), fill=(210, 220, 226, 230), outline=(120, 140, 150, 255), width=2)
    dd.polygon([(20, 0), (8, 30), (32, 30)], fill=(210, 220, 226, 230))
    A["drop"] = save(drop, "drop.png")
    return A


# ------------------------------------------------------------------------------------------ ffmpeg bits ---
class G:
    """tiny filtergraph builder: inputs + chains, returns the ffmpeg command for one cut."""

    def __init__(self, cut):
        self.cut, self.n = cut, NFR[cut]
        self.d = self.n / FPS + 0.6
        self.inputs, self.chains, self.k = [], [], 0

    def still(self, path):
        self.inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{self.d:.3f}", "-i", path]
        return str(self._idx())

    def _idx(self):
        return sum(1 for a in self.inputs if a == "-i") - 1

    def clip(self, path, ss, t):
        self.inputs += ["-ss", f"{ss:.3f}", "-t", f"{t:.3f}", "-i", path]
        return str(self._idx())

    def lab(self):
        self.k += 1
        return f"v{self.k}"

    def add(self, s):
        self.chains.append(s)


def ease(p):          # ease in-out on 0..1
    return f"(0.5-0.5*cos(PI*min(1,max(0,{p}))))"


def zp(g, src, z0, z1, fx0, fx1, fy0, fy1, inp_scale=2, curve="io"):
    """camera on a still: zoompan over a pre-scaled input; z, centre fractions interpolated with easing."""
    n = g.n
    p = f"(on/{max(1, n - 1)})"
    e = ease(p) if curve == "io" else (f"pow({p},2)" if curve == "in" else p)
    o = g.lab()
    g.add(f"[{src}]scale={W * inp_scale}:{H * inp_scale},zoompan=z='{z0}+({z1}-{z0})*{e}':"
          f"x='(iw-iw/zoom)*({fx0}+({fx1}-{fx0})*{e})':y='(ih-ih/zoom)*({fy0}+({fy1}-{fy0})*{e})':"
          f"d=1:s={W}x{H}:fps={FPS},setsar=1[{o}]")
    return o


def vpush(g, src, z0, z1, fx=0.5, fy=0.5):
    """push on a moving source: per-frame scale then crop."""
    o = g.lab()
    T = g.n / FPS
    g.add(f"[{src}]scale=w='2*trunc({W}*({z0}+({z1}-{z0})*{ease(f't/{T:.4f}')})/2)':h=-2:eval=frame,"
          f"crop={W}:{H}:x='(iw-ow)*{fx}':y='(ih-oh)*{fy}',setsar=1[{o}]")
    return o


def overlay_field(g, src, field, mode, opacity, motion="", pre=""):
    fi = g.still(field)
    f, o = g.lab(), g.lab()
    g.add(f"[{fi}]format=gbrp{(',' + pre) if pre else ''}{(',' + motion) if motion else ''},scale={W}:{H},format=gbrp[{f}]")
    g.add(f"[{src}]format=gbrp[{f}b];[{f}b][{f}]blend=all_mode={mode}:all_opacity={opacity},format=yuv420p[{o}]")
    return o


def rain(g, src, fast=False, darken=True):
    s = src
    if darken:
        o = g.lab()
        g.add(f"[{s}]eq=brightness=-0.05:contrast=1.08[{o}]")
        s = o
    v1, v2 = (-0.03, -0.07) if not fast else (-0.06, -0.12)
    s = overlay_field(g, s, A["rain_far"], "screen", 0.3, f"scroll=vertical={v1},rotate=a={RAIN_A}:fillcolor=black")
    s = overlay_field(g, s, A["rain_near"], "screen", 0.55, f"scroll=vertical={v2},rotate=a={RAIN_A}:fillcolor=black")
    return s


def mist(g, src, op=0.22):
    return overlay_field(g, src, A["fog"], "screen", op, f"crop={W}:{H}:x='(iw-ow)*t/40':y=0")


def dust(g, src, op=0.6):
    return overlay_field(g, src, A["dust"], "screen", op, "scroll=vertical=0.004:horizontal=0.002")


def clouds(g, src, speed=260):
    return overlay_field(g, src, A["clouds"], "multiply", 1.0, f"crop={W}:{H}:x='t*{speed}':y=0")


def spray_burst(g, src, cx=0.5, cy=0.72, op=0.5, t0=0.0, dur=None):
    fi = g.still(A["drops"])
    f, o = g.lab(), g.lab()
    en = f":enable='between(t,{t0},{t0 + dur})'" if dur else ""
    g.add(f"[{fi}]zoompan=z='1+1.2*(1-exp(-max(0,on-{int(t0 * FPS)})/20))':x='iw*{cx}-(iw/zoom)*{cx}':"
          f"y='ih*{cy}-(ih/zoom)*{cy}':d=1:s={W}x{H}:fps={FPS},gblur=sigma=1:sigmaV=3,format=gbrp[{f}]")
    g.add(f"[{src}]format=gbrp[{f}b];[{f}b][{f}]blend=all_mode=screen:all_opacity={op}{en},format=yuv420p[{o}]")
    return o


def pop(g, src, frames):
    if not frames:
        return src
    o = g.lab()
    cond = "+".join(f"between(n,{f},{f + 1})" for f in frames)
    g.add(f"[{src}]eq=brightness='0.06*({cond})':eval=frame[{o}]")
    return o


def ink(g, src, f):
    o = g.lab()
    en = f"enable='between(n,{f},{f + 1})'"
    g.add(f"[{src}]negate={en},lutyuv=y='if(lt(val,90),16,if(lt(val,170),120,225))':u=128:v='val*0.6+51':{en}[{o}]")
    return o


def shake(g, src, events):
    """events: (local frame, amplitude px, decay). Decaying sine, applied last on a 1.05x plate."""
    if not events:
        return src
    xs, ys = [], []
    for f, a, k in events:
        t0 = f / FPS
        xs.append(f"gte(t,{t0:.4f})*{a}*exp(-{k}*(t-{t0:.4f}))*sin(2*PI*14*(t-{t0:.4f}))")
        ys.append(f"gte(t,{t0:.4f})*{a * 0.7:.1f}*exp(-{k}*(t-{t0:.4f}))*sin(2*PI*17*(t-{t0:.4f})+1)")
    o = g.lab()
    g.add(f"[{src}]scale=2016:1134,crop={W}:{H}:x='48+{'+'.join(xs)}':y='27+{'+'.join(ys)}'[{o}]")
    return o


def label(g, src, text):
    p = f"{WK}/label_{g.cut}.txt"
    open(p, "w").write(text)
    o = g.lab()
    g.add(f"[{src}]drawtext=fontfile={FONT}:textfile={p}:fontsize=20:fontcolor=white@0.85:x=16:y=14:"
          f"box=1:boxcolor=black@0.45:boxborderw=5,format=yuv420p[{o}]")
    return o


def run_cut(g, last, out):
    cmd = ["ffmpeg", "-v", "error", "-y", *g.inputs, "-filter_complex", ";".join(g.chains), "-map", f"[{last}]",
           "-r", str(FPS), "-frames:v", str(g.n), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "16",
           "-pix_fmt", "yuv420p", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"{g.cut}: {r.stderr[-1500:]}\n" + ";\n".join(g.chains))
    return out


# ------------------------------------------------------------------------------------------ the cuts ---
def ripple(g, plate, speed_expr="t", amp_scale=1.0):
    """K13 stand-in: L-10 displacement over the water only; map position = 90 px/s x speed integral."""
    p, mx, my, mk = g.still(plate), g.still(A["rip_x"]), g.still(A["rip_y"]), g.still(A["water"])
    a, b, c, o, base = g.lab(), g.lab(), g.lab(), g.lab(), g.lab()
    g.add(f"[{mx}]crop={W}:{H}:x='90*({speed_expr})':y=0,format=gbrp[{a}]")
    g.add(f"[{my}]crop={W}:{H}:x='{W}-60*({speed_expr})':y=0,format=gbrp[{b}]")
    g.add(f"[{p}]format=gbrp,split[{base}][{base}d];[{base}d][{a}][{b}]displace=edge=smear,format=gbrp[{c}]")
    g.add(f"[{mk}]format=gbrp[{c}m];[{base}]format=gbrp[{base}g];[{base}g][{c}][{c}m]maskedmerge,format=yuv420p[{o}]")
    return o


def build(cut):
    g = G(cut)
    L = lambda f: loc(cut, f)
    out = f"{SEG}/{cut}.mp4"
    lbl = ""
    if cut == "01":
        s = zp(g, g.still(A["F01a"]), 1.0, 1.04, 0.5, 0.45, 0.5, 0.5)
        s = spray_burst(g, s, 0.3, 0.3, 0.25)
        s = rain(g, mist(g, s, 0.18), darken=False)
        lbl = "01  PLACEHOLDER F01a card / K01a pending  (LA fallback)"
    elif cut == "02":
        i = g.still(A["D01A_tall"])
        o = g.lab()
        g.add(f"[{i}]crop={W}:{H}:x=0:y='(ih-oh)*(0.08+0.30*{ease(f't/{g.n / FPS}')})',setsar=1[{o}]")
        s = mist(g, o, 0.2)
        lbl = "02  EX D01_A  TILT down  (crack paint-out on all 3 Spires pending)"
    elif cut == "02b":
        s = zp(g, g.still(A["F04"]), 1.50, 1.47, 0.2, 0.2, 0.5, 0.5)
        lbl = "02b  PLACEHOLDER F04 (D02_C1 crop) / K03 pending"
    elif cut == "03":
        c = g.clip(ALLEY, 0.5, 3.4)
        o, pa, pb = g.lab(), g.lab(), g.lab()
        # static patches: plain brick over the double gate, plain door planks over the ring knocker
        g.add(f"[{c}]split=3[{o}a][{o}b][{o}c];[{o}b]trim=end_frame=1,loop=loop=-1:size=1,crop=140:130:775:495[{pa}];"
              f"[{o}c]trim=end_frame=1,loop=loop=-1:size=1,crop=44:80:60:568[{pb}];"
              f"[{o}a][{pa}]overlay=915:495:shortest=1[{o}d];[{o}d][{pb}]overlay=122:568:shortest=1,"
              f"scale=1940:1080,crop={W}:{H},setsar=1[{o}]")
        s = vpush(g, o, 1.0, 1.04)
        s = mist(g, s, 0.2)
        lbl = "03  EXK alley clip 0.5-3.5 s  (gate + knocker patched)"
    elif cut == "04":
        s = zp(g, g.still(A["F04"]), 1.03, 1.0, 0.5, 0.5, 0.5, 0.5)
        di, o = g.still(A["drop"]), g.lab()
        t0 = L(270) / FPS        # the drop leaves the knot on 0:11.25 (frame 270) and falls out of frame
        g.add(f"[{di}]scale=28:42[{o}d];[{s}][{o}d]overlay=x=540:y='if(lt(t,{t0}),430,430+1400*(t-{t0})*(t-{t0}))'"
              f":shortest=1[{o}]")
        s = o
        lbl = "04  PLACEHOLDER F04 / K03 pending  (drop leaves on frame 270)"
    elif cut == "05":
        # ROT: rim circle turns clockwise from rest from frame 289, ease-in to 1.8 rad/s; post laid on top
        i = g.still(A["wheel"])
        bg, w, r, post, o = g.lab(), g.lab(), g.lab(), g.lab(), g.lab()
        t0 = L(289) / FPS
        ang = f"gte(t,{t0:.4f})*(lt(t,{t0 + 1:.4f})*0.9*pow(t-{t0:.4f},2)+gte(t,{t0 + 1:.4f})*(0.9+1.8*(t-{t0 + 1:.4f})))"
        g.add(f"[{i}]split=3[{bg}][{w}][{post}a]")
        g.add(f"[{w}]crop=540:540:417:98,format=rgba,rotate=a='{ang}':c=none,"
              f"geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='255*lt(hypot(X-270,Y-270),266)'[{r}]")
        g.add(f"[{post}a]crop=66:320:658:322[{post}]")
        g.add(f"[{bg}][{r}]overlay=417:98[{o}a];[{o}a][{post}]overlay=658:322,scale={W}:-2,crop={W}:{H},setsar=1[{o}]")
        s = pop(g, o, [L(289)])
        s = shake(g, s, [(L(289), 10, 9)])
        lbl = "05  LA  EX sc06-sh010  ROT clockwise from 289  (wall crack paint-out pending)"
        return finish(g, s, lbl, out)
    elif cut == "06":
        i = g.still(A["W2"])
        o = g.lab()
        g.add(f"[{i}]scale={W}:{int(H * 1.6)},crop={W}:{H}:x=0:y='mod(t*900,{int(H * 0.6)})',tmix=frames=3,setsar=1[{o}]")
        s = shake(g, o, [(L(325), 8, 9)])
        lbl = "06  EX D05_W2 still  K04 pending  (streaks stand-in)"
        return finish(g, s, lbl, out)
    elif cut == "07":
        s = zp(g, g.still(A["W1"]), 1.0, 1.06, 0.5, 0.5, 0.5, 0.5)
        s = mist(g, s, 0.18)
        s = shake(g, s, [(L(361), 8, 9), (L(397), 8, 9)])
        lbl = "07  EX D05_W1 still  K05 pending"
        return finish(g, s, lbl, out)
    elif cut == "08":
        s = zp(g, g.still(A["F04"]), 1.67, 1.67, 0.85, 0.85, 0.35, 0.35)
        o = g.lab()
        g.add(f"[{s}]noise=alls=8:allf=t[{o}]")
        s = shake(g, o, [(L(433), 8, 9)])
        lbl = "08  PLACEHOLDER F04 punch-in / K03 pending"
        return finish(g, s, lbl, out)
    elif cut == "09":
        i = g.still(A["W1"])
        o = g.lab()
        tw0 = 16 / FPS
        g.add(f"[{i}]scale={W}:{int(H * 1.8)},crop={W}:{H}:x=0:y='(ih-oh)*(1-pow(min(1,max(0,(t-{tw0:.3f})/{(36 - 16) / FPS:.3f})),2))',"
              f"gblur=sigma=0.5:sigmaV=14:enable='between(n,19,22)',gblur=sigma=0.5:sigmaV=40:enable='gte(n,23)',setsar=1[{o}]")
        s = pop(g, o, [L(491)])
        s = shake(g, s, [(L(469), 8, 9)])
        lbl = "09  EX D05_W1  WHIP up, POP on whistle 491"
        return finish(g, s, lbl, out)
    elif cut == "10":
        s = zp(g, g.still(A["F10"]), 1.0, 1.08, 0.5, 0.5, 0.6, 0.4)
        s = mist(g, s, 0.2)
        lbl = "10  PLACEHOLDER F10 (D01_A crop) / K07 pending"
    elif cut == "11":
        s = zp(g, g.still(A["F11"]), 1.0, 1.05, 0.5, 0.5, 0.5, 0.5)
        lbl = "11  PLACEHOLDER F11 (D02_C1 crop) / K08 pending"
    elif cut == "12":
        s = zp(g, g.still(A["bell"]), 1.02, 1.02, 0.5, 0.5, 0.5, 0.5)
        s = dust(g, s)
        s = pop(g, s, [L(685)])
        lbl = "12  EX sc16-sh040 crop x<=960  K09 pending  (strike POP 685)"
    elif cut == "13":
        s = zp(g, g.still(A["hall"]), 1.0, 1.04, 0.5, 0.5, 0.5, 0.5)
        s = dust(g, s, 0.5)
        s = clouds(g, s, 220)
        lbl = "13  LA  EX D11_L1  (relay-stone cage painted out)  no steam (R2.3)"
    elif cut == "13b":
        s = zp(g, g.still(A["hall13b"]), 1.0, 1.06, 0.5, 0.5, 0.5, 0.5)
        s = dust(g, s, 0.5)
        lbl = "13b  LA  EX D11_L1 cut-in 1.4x"
    elif cut == "14":
        i = g.still(A["F14"])
        o = g.lab()
        T = g.n / FPS
        g.add(f"[{i}]scale={W * 2}:{H * 2},rotate=a='0.052*{ease(f't/{T:.3f}')}':c=black,"
              f"zoompan=z='1.10+0.08*{ease(f'on/{g.n - 1}')}':x='(iw-iw/zoom)*(0.45-0.40*{ease(f'on/{g.n - 1}')})':"
              f"y='(ih-ih/zoom)*0.5':d=1:s={W}x{H}:fps={FPS},setsar=1[{o}]")
        ci, c = g.still(A["coin"]), g.lab()
        ts = L(847) / FPS   # the spinning coin settles on frame 847
        g.add(f"[{ci}]scale=w='max(6,150*abs(cos(2*PI*t*(3.2-1.0*t))))*lt(t,{ts:.3f})+150*gte(t,{ts:.3f})':h=150:eval=frame[{c}c];"
              f"[{o}][{c}c]overlay=x='1150-w/2':y=640:eval=frame:shortest=1[{c}]")
        s = c
        lbl = "14  PLACEHOLDER F14 (ledger + drawn coins) / K10 pending  variant A tally E1, coin settles 847"
    elif cut == "15":
        s = zp(g, g.still(A["F15"]), 1.10, 1.10, 0.0, 1.0, 0.5, 0.5)
        s = clouds(g, s, 300)
        lbl = "15  PLACEHOLDER F15 (D01_C as is)  PAN right"
    elif cut == "16":
        s = zp(g, g.still(A["S1la"]), 1.12, 1.12, 0.5, 0.5, 1.0, 0.0)
        s = clouds(g, s, 200)
        s = mist(g, s, 0.15)
        lbl = "16  LA  EX D08_S1_late-aft  TILT up"
    elif cut == "17":
        s = zp(g, g.still(A["F17"]), 1.08, 1.08, 0.0, 1.0, 0.5, 0.5)
        s = clouds(g, s, 220)
        lbl = "17  PLACEHOLDER F17 (heraldry card)  PAN"
    elif cut == "18":
        i = g.still(A["P2"])
        o = g.lab()
        g.add(f"[{i}]crop={W}:{H}:x='(iw-ow)*{ease(f't/{g.n / FPS}')}':y=0,setsar=1[{o}]")
        s = dust(g, o, 0.35)
        lbl = "18  PLACEHOLDER F18 (panel 2 v1 as is)  PAN"
    elif cut in ("19", "20", "21", "22"):
        src = A["F19"] if cut in ("19", "20") else A["F21"]
        fx = 0.0 if cut in ("19", "21") else 1.0
        i = g.still(src)
        o = g.lab()
        g.add(f"[{i}]scale={int(W / 0.6)}:-2,crop={W}:{H}:x='(iw-ow)*{fx}+6*sin(2*PI*t*1.3)':y='(ih-oh)/2',setsar=1[{o}]")
        s = pop(g, o, [1])
        s = shake(g, s, [(1, 5, 9)]) if cut == "19" else s
        lbl = f"{cut}  PLACEHOLDER {'F19' if cut in ('19', '20') else 'F21'} (heraldry card) / {'K11' if cut in ('19', '20') else 'K12'} pending"
        return finish(g, s, lbl, out)
    elif cut == "23":
        s = zp(g, g.still(A["P5"]), 1.0, 1.12, 0.5, 0.5, 0.5, 0.5)
        s = shake(g, s, [(0, 3, 2)])
        lbl = "23  PLACEHOLDER F23 (panel 5 v1 as is)  fast PUSH"
        return finish(g, s, lbl, out)
    elif cut == "24":
        s = zp(g, g.still(A["map"]), 1.0, 1.25, 0.5, 0.75, 0.5, 0.4, curve="in")
        fl, o = g.still(A["F01"]), g.lab()
        fr = [L(1333), L(1351), L(1356)]
        en = "+".join(f"between(n,{f},{f + 1})" for f in fr)
        g.add(f"[{fl}]negate,lutyuv=y='if(lt(val,90),16,if(lt(val,170),120,225))':u=128:v='val*0.6+51'[{o}f];"
              f"[{s}][{o}f]overlay=0:0:enable='{en}':shortest=1[{o}]")
        s = shake(g, o, [(f, 6, 9) for f in (0, 9, 18, 27)])
        lbl = "24  LA  EX E05 map (tints pending)  flashes 1333/1351/1356"
        return finish(g, s, lbl, out)
    elif cut == "24b":
        i = g.still(A["F01"])
        o = g.lab()
        g.add(f"[{i}]scale={W}:{H},eq=brightness=-1:contrast=0,setsar=1[{o}]")
        return finish(g, o, "", out, plain=True)
    elif cut == "25":
        s = zp(g, g.still(A["F01"]), 1.0, 1.03, 0.5, 0.5, 0.5, 0.5)
        s = spray_burst(g, s, 0.62, 0.55, 0.55)
        s = rain(g, s)
        s = ink(g, s, L(1369))
        s = shake(g, s, [(L(1369), 20, 4)])
        lbl = "25  PLACEHOLDER F01 card / K01 pending (LA fallback)  impact + INK on 1369"
        return finish(g, s, lbl, out)
    elif cut == "26":
        s = zp(g, g.still(A["F26"]), 1.0, 1.03, 0.5, 0.5, 0.5, 0.5)
        s = rain(g, s)
        s = shake(g, s, [(L(1441), 8, 9)])
        lbl = "26  PLACEHOLDER F26 (D02_C3 planks; R2.2 prints pending) / K18 pending"
        return finish(g, s, lbl, out)
    elif cut == "27":
        s = zp(g, g.still(A["F27"]), 1.0, 1.04, 0.5, 0.5, 0.5, 0.5)
        s = spray_burst(g, s, 0.48, 0.45, 0.5)
        s = rain(g, mist(g, s, 0.2), darken=False)
        s = pop(g, s, [1])
        lbl = "27  PLACEHOLDER F27 card / K14 pending"
    elif cut == "28":
        i = g.still(A["F28"])
        o = g.lab()
        g.add(f"[{i}]eq=brightness=-0.08:saturation=0.55,zoompan=z='1+0.35*on/36':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
              f"d=1:s={W}x{H}:fps={FPS},split=3[{o}a][{o}b][{o}c];[{o}b]scale=iw*1.03:-2,crop={W}:{H}[{o}b2];"
              f"[{o}c]scale=iw*1.06:-2,crop={W}:{H}[{o}c2];[{o}a][{o}b2]blend=all_mode=average[{o}ab];"
              f"[{o}ab][{o}c2]blend=all_mode=average,gblur=sigma=0.5:sigmaV=20:enable='lt(n,4)',setsar=1[{o}]")
        s = rain(g, o, fast=True, darken=False)
        lbl = "28  PLACEHOLDER F28 (D02_C3 canal) / K15 pending (zoom-blur rush fallback)"
    elif cut == "29":
        i = g.still(A["W2"])
        o = g.lab()
        g.add(f"[{i}]scale={W}:{int(H * 1.6)},crop={W}:{H}:x=0:y='mod(t*1800,{int(H * 0.6)})',tmix=frames=3,setsar=1[{o}]")
        s = shake(g, o, [(1, 8, 9)])
        lbl = "29  EX D05_W2 still  K04 pending  (RAMP 2x stand-in)"
        return finish(g, s, lbl, out)
    elif cut == "30":
        s = zp(g, g.still(A["F30"]), 1.06, 1.06, 0.5, 0.5, 1.0, 0.0)
        # light shaft from the cloud gap: soft vertical band opening by width (motivated by the gap in frame)
        o = g.lab()
        g.add(f"color=c=0xd8d2c0:s={W}x{H}:r={FPS}:d={g.d:.2f},format=gbrp,"
              f"geq=r='r(X,Y)*exp(-pow((X-{W * 0.55})/(30+220*min(1,T/2.5)),2))*lt(Y,{H * 0.75})':"
              f"g='g(X,Y)*exp(-pow((X-{W * 0.55})/(30+220*min(1,T/2.5)),2))*lt(Y,{H * 0.75})':"
              f"b='b(X,Y)*exp(-pow((X-{W * 0.55})/(30+220*min(1,T/2.5)),2))*lt(Y,{H * 0.75})',gblur=sigma=30[{o}l];"
              f"[{s}]format=gbrp[{o}s];[{o}s][{o}l]blend=all_mode=screen:all_opacity=0.25,format=yuv420p[{o}]")
        s = rain(g, o)
        lbl = "30  PLACEHOLDER F30 card / K16 pending  (shaft opens from the gap)"
    elif cut in ("31", "31b", "31c"):
        s = ripple(g, A["H1"])
        z, fx, fy = {"31": (1.0, 0.5, 0.5), "31b": (1.5, 0.62, 0.38), "31c": (1.3, 0.49, 0.10)}[cut]
        if cut == "31":
            s = vpush(g, s, 1.0, 1.05)
            s = ink(g, s, L(1657))
            lbl = "31  EX D09_H1 (R2.5 crop, finial out, lamps dark) + ripple = K13 stand-in  INK 1657"
            return finish(g, s, lbl, out)
        o = g.lab()
        g.add(f"[{s}]scale={int(W * z)}:-2,crop={W}:{H}:x='(iw-ow)*{fx}':y='(ih-oh)*{fy}'[{o}]")
        s = shake(g, o, [(1, 6, 9)])
        lbl = f"{cut}  EX D09_H1 crop {z}x + ripple = K13 stand-in"
        return finish(g, s, lbl, out)
    elif cut == "32":
        # GLASS, keeper R2.4: four even full-frame steps (25/50/75/100 %), no front; step k jumps in the first
        # third of its 1.5 s from the placed hit frame (offset 1 frame) and holds.
        spd = "min(t,1.5)+0.6*min(max(t-1.5,0),1.5)+0.3*min(max(t-3,0),1.5)+0.15*max(t-4.5,0)"
        a = ripple(g, A["H1sky"], spd)
        bi, b = g.still(A["H2"]), g.lab()
        g.add(f"[{bi}]format=yuv420p,settb=AVTB,fps={FPS}[{b}]")
        o = g.lab()
        g.add(f"[{a}]settb=AVTB,fps={FPS}[{o}a];[{o}a][{b}]xfade=transition=custom:duration=6:offset={1 / FPS:.5f}:"
              "expr='st(0,(1-P)*4);st(1,ld(0)-floor(ld(0)));st(2,(floor(ld(0))+min(1,ld(1)*3))/4);"
              f"A*(1-ld(2))+B*ld(2)'[{o}]")
        steps = [L(f) for f in (1765, 1801, 1837, 1873)]
        s = pop(g, o, steps)
        s = shake(g, s, [(f, 6, 9) for f in steps])
        lbl = "32  GLASS R2.4: even full-frame steps 1765/1801/1837/1873, no front  (H1 ripple -> H2)"
        return finish(g, s, lbl, out)
    elif cut == "32b":
        s = zp(g, g.still(A["H2"]), 1.12, 1.16, 0.5, 0.5, 0.12, 0.10)
        s = clouds(g, s, 60)
        s = pop(g, s, [L(1945)])
        lbl = "32b  LA  EX D09_H2 (cropped, lamps dark)  1.12x toward the sun, POP 1945"
    elif cut == "33":
        return build_33(g, out)
    else:
        raise ValueError(cut)
    return finish(g, s, lbl, out)


def finish(g, s, lbl, out, plain=False):
    if not plain and lbl:
        s = label(g, s, lbl)
    o = g.lab()
    g.add(f"[{s}]format=yuv420p,setsar=1[{o}]")
    return run_cut(g, o, out)


def build_33(g, out):
    """1:22.5-1:27.0: 32b continues, INK 1981-1982, torn spray wipe 1983-1994, logo lands 1995-2002 (114 % -> 100 %),
    6 frames of SHAKE, still letters; title plate + cloud drift (K17 stand-in, 1x, no stretch); one drop gathers on
    a letter and leaves on 2040, two small drops slide and fall out of frame, all gone by 2076 (1:26.5);
    variant B dusk grade on plate, wipe and spray. Picture fade 1:26.5-1:27.0 is done on the master."""
    L = lambda f: loc("33", f)
    T = g.n / FPS
    # A: the 32b framing continued
    ai, a = g.still(A["H2"]), g.lab()
    g.add(f"[{ai}]scale={W * 2}:{H * 2},zoompan=z='1.16+0.01*on/{g.n}':x='(iw-iw/zoom)*0.5':y='(ih-ih/zoom)*0.10':"
          f"d=1:s={W}x{H}:fps={FPS},setsar=1[{a}]")
    a = ink(g, a, L(1981))
    # B: title plate, push 3 %, clouds (K17 stand-in), dusk grade (variant B)
    b = zp(g, g.still(A["title"]), 1.0, 1.03, 0.5, 0.5, 0.3, 0.3, curve="lin")
    b = clouds(g, b, 120)
    o = g.lab()
    g.add(f"[{b}]colorbalance=rs=-0.04:bs=0.06:rm=-0.03:bm=0.04[{o}]")
    b = o
    # WIPE: torn edge bottom -> top, 0.5 s from frame 1983
    w = g.lab()
    g.add(f"[{a}]settb=AVTB,fps={FPS}[{w}a];[{b}]settb=AVTB,fps={FPS}[{w}b];[{w}a][{w}b]xfade=transition=custom:"
          f"duration=0.5:offset={L(1983) / FPS:.5f}:expr='if(gt(Y/H+0.06*sin(X/W*23)+0.03*sin(X/W*71),P*1.12),B,A)'[{w}]")
    s = spray_burst(g, w, 0.5, 0.9, 0.6, t0=L(1983) / FPS, dur=0.55)
    # logo lands on 1995 with overshoot, alpha in 4 frames
    lw, lh = A["logo_wh"]
    li, lo = g.still(A["logo"]), g.lab()
    tl = L(1995) / FPS
    g.add(f"[{li}]format=rgba,setpts=PTS-STARTPTS,scale=w='2*trunc({lw}*(1+0.14*exp(-max(0,t-{tl:.4f})*9)*cos(max(0,t-{tl:.4f})*22))/2)':"
          f"h=-2:eval=frame,fade=t=in:st={tl:.4f}:d=0.17:alpha=1[{lo}l];"
          f"[{s}][{lo}l]overlay=x='(W-w)/2':y='H*0.30-h/2':eval=frame:enable='gte(n,{L(1995)})':shortest=1[{lo}]")
    s = lo
    # drops on the letters only: main drop gathers 1:24.0-1:25.0 on the lower edge of a letter, leaves on 2040
    di = g.still(A["drop"])
    t_g0, t_go = L(2016) / FPS, L(2040) / FPS
    ylow = int(H * 0.30 + lh / 2 - 34)
    x_main = int(W / 2 + lw * 0.17)
    o = g.lab()
    g.add(f"[{di}]format=rgba,split=3[{o}d1][{o}d2][{o}d3];"
          f"[{o}d1]scale=w='2*trunc(max(4,40*min(1,max(0,(t-{t_g0:.3f})/{t_go - t_g0:.3f})))/2)':h=-2:eval=frame[{o}m];"
          f"[{s}][{o}m]overlay=x={x_main}-w/2:y='{ylow}+if(gt(t,{t_go:.3f}),1500*pow(t-{t_go:.3f},2),0)':"
          f"eval=frame:enable='gte(t,{t_g0:.3f})':shortest=1[{o}x]")
    # two small drops (opacity 0.4): slide slowly on two letters from 1:24.2, fall from 1:25.4, gone before 1:26.5
    t_s0, t_f = L(2021) / FPS, L(2050) / FPS
    g.add(f"[{o}d2]scale=24:-2,colorchannelmixer=aa=0.4[{o}s1];[{o}d3]scale=20:-2,colorchannelmixer=aa=0.4[{o}s2];"
          f"[{o}x][{o}s1]overlay=x={int(W / 2 - lw * 0.33)}:y='{ylow - 50}+28*min(1,max(0,(t-{t_s0:.3f})/{t_f - t_s0:.3f}))"
          f"+if(gt(t,{t_f:.3f}),1500*pow(t-{t_f:.3f},2),0)':enable='gte(t,{t_s0:.3f})':shortest=1[{o}y];"
          f"[{o}y][{o}s2]overlay=x={int(W / 2 + lw * 0.40)}:y='{ylow - 60}+24*min(1,max(0,(t-{t_s0 + 0.2:.3f})/{t_f - t_s0:.3f}))"
          f"+if(gt(t,{t_f + 0.2:.3f}),1500*pow(t-{t_f + 0.2:.3f},2),0)':enable='gte(t,{t_s0 + 0.2:.3f})':shortest=1[{o}]")
    s = shake(g, o, [(L(1995), 6, 18)])
    o2 = g.lab()
    g.add(f"[{s}]trim=end_frame={g.n}[{o2}]")
    s = label(g, o2, "33  INK 1981, WIPE 1983-1994, logo 1995  EX D08_S1_dusk + cloud drift = K17 stand-in (1x)  "
                     "drops on letters only (R2.1), all out by 2076")
    o3 = g.lab()
    g.add(f"[{s}]format=yuv420p,setsar=1[{o3}]")
    return run_cut(g, o3, out)


# ------------------------------------------------------------------------------------------ master ---
def master(out):
    lst = f"{WK}/concat.txt"
    with open(lst, "w") as f:
        for c, _, _ in CUTS:
            f.write(f"file '{SEG}/{c}.mp4'\n")
    bug = f"{WK}/bug.txt"
    open(bug, "w").write("ANIME-STYLE · AI-ANIMATED")
    vf = (f"setpts=N/{FPS}/TB,fps={FPS},"
          f"drawtext=fontfile={FONT}:textfile={bug}:fontsize=18:fontcolor=white@0.55:x=w-tw-24:y=h-th-20,"
          f"drawtext=fontfile={FONT}:text='%{{frame_num}}  %{{pts\\:hms}}':start_number=0:fontsize=18:fontcolor=white@0.7:"
          f"x=16:y=h-th-20:box=1:boxcolor=black@0.4:boxborderw=4,"
          f"fade=t=out:st={FADE_ST}:d={FADE_D}")
    af = f"atrim=0:{TOTAL / FPS},asetpts=PTS-STARTPTS,afade=t=out:st={FADE_ST}:d={FADE_D}"
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", MUSIC,
           "-filter_complex", f"[0:v]{vf}[v];[1:a]{af}[a]", "-map", "[v]", "-map", "[a]",
           "-frames:v", str(TOTAL), "-r", str(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "18",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-t", f"{TOTAL / FPS}", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr[-2000:])


A = {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--no-final", action="store_true")
    args = ap.parse_args()
    for p in (H1, H2):
        if not os.path.exists(p):
            sys.exit(f"missing {p}: run op_harbour_plates.py first")
    A.update(make_assets())
    todo = [c for c, _, _ in CUTS if not args.only or c in args.only.split(",")]
    errs = []
    with cf.ThreadPoolExecutor(args.jobs) as ex:
        futs = {ex.submit(build, c): c for c in todo}
        for fu in cf.as_completed(futs):
            try:
                fu.result()
                print("ok", futs[fu], flush=True)
            except Exception as e:
                errs.append(str(e))
                print("FAIL", futs[fu], str(e)[:3000], flush=True)
    if errs:
        sys.exit(1)
    if not args.no_final:
        out = f"{OUTD}/S1_OP_animatic_v1.mp4"
        master(out)
        print("master", out)


if __name__ == "__main__":
    main()
