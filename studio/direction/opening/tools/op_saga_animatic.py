#!/usr/bin/env python3
"""Saga OP animatic v3 ($0, ffmpeg + PIL only, no API calls). Storyboard SAGA_OP v2.2: 68 shots + 9 frames of black,
87.0 s, 24 fps, 1920x1080, music output/music/lib_mus_theme-op-anthem_v1a.mp3 (investor's choice; v2a retired).

  python3 -I op_saga_animatic.py [--only A01a,C13] [--jobs 4] [--no-final]
  python3 -I op_saga_animatic.py --check FILE        # §12 rule 5: freezedetect + mpdecimate
  python3 -I op_saga_animatic.py --contact FILE      # cut sheet + hit sheet with the music onset envelope
  python3 -I op_saga_animatic.py --posters           # P1-P13 (§7.2): clean full-size stills of what exists now + manifest

PAID material is cut from the S1 OP v3 renders (output/opening/build_work/seg, accepted and keeper-signed) or from the
raw paid clips; C13 is the logo reveal on the final hit (LOGO.md v1.1, refs/LOGO). A01 (the redesigned swell, KA01) is stood in by
PAID K16 + K01 take 2 at 1.0x; the map C11 is a sheet on a table with diagonal passes. Every NEW item (W/KW/KA) is a card with
the shot text, land colour key and a moving drift so that rhythm and sync can be checked; it is labelled PENDING.
Output: output/opening/SAGA_OP_animatic_v3.mp4 (+ work files in output/opening/saga_animatic_work/).
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys
import textwrap

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import op_build as ob  # noqa: E402

an = ob.an
ROOT, OUTD = an.ROOT, an.OUTD
WK = f"{OUTD}/saga_animatic_work"
an.WK, an.SEG = WK, f"{WK}/seg"
S1SEG = f"{OUTD}/build_work/seg"
CL = f"{OUTD}/clips"
OUT = f"{OUTD}/SAGA_OP_animatic_v3.mp4"
CONTACT = f"{OUTD}/contact_saga_v3"
POSTERS = f"{OUTD}/posters_saga"
W, H, FPS = an.W, an.H, an.FPS
FONT, FONTB = an.FONT, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
A = an.A

# ---------------------------------------------------------------------------------------- cut list v2.2 ---
# 68 shots + 9 frames of black. Theme 1.5 s; rise 0.75 s; banners 0.75 s (banner on the hit, its land on the beat).
CUTS = [("A01a", 0, 36), ("A01b", 36, 36), ("A02", 72, 36), ("A03", 108, 36), ("A04a", 144, 36), ("A04b", 180, 36),
        ("A05a", 216, 36), ("A05b", 252, 36), ("A06", 288, 36), ("A07", 324, 36), ("A08", 360, 36), ("A09", 396, 36),
        ("A10", 432, 36), ("A11", 468, 36)]
THEME = ["B01a", "B01b", "B02a", "B02b", "B03a", "B04a", "B03b", "B04b",          # two clips of a land, alternating
         "B05a", "B06a", "B05b", "B06b", "B07a", "B08a", "B07b", "B08b"]
CUTS += [(c, 504 + 36 * k, 36) for k, c in enumerate(THEME)]
RISE = ["B09", "B10a", "B11a", "B10b", "B11b", "B12a", "B13a", "B12b", "B13b", "B12c", "B13c", "B12d", "B13d", "B14"]
CUTS += [(c, 1080 + 18 * k, 18) for k, c in enumerate(RISE)]
CUTS += [("B15", 1332, 28), ("B16", 1360, 9), ("C01a", 1369, 35), ("C01b", 1404, 36)]
CUTS += [("C02", 1440, 18), ("C02L", 1458, 18), ("C03", 1476, 18), ("C03L", 1494, 18), ("C04", 1512, 36),
         ("C05", 1548, 18), ("C05L", 1566, 18), ("C06", 1584, 18), ("C06L", 1602, 18), ("C07", 1620, 36),
         ("C08", 1656, 36), ("C09", 1692, 36), ("C10", 1728, 36)]
CUTS += [(f"C11{x}", 1764 + 36 * i, 36) for i, x in enumerate("abcd")]
CUTS += [("C12a", 1908, 36), ("C12b", 1944, 36), ("C13", 1980, 108)]
assert sum(n for _, _, n in CUTS) == an.TOTAL
assert all(CUTS[i][1] + CUTS[i][2] == CUTS[i + 1][1] for i in range(len(CUTS) - 1))
an.CUTS = CUTS
an.START = {c: s for c, s, _ in CUTS}
an.NFR = {c: n for c, _, n in CUTS}
an.MUSIC = f"{ROOT}/output/music/lib_mus_theme-op-anthem_v1a.mp3"   # investor 2026-11-24; v2a retired
LOGO = f"{ROOT}/studio/direction/refs/LOGO/HOLLOWSTONE_logo_master_alpha.png"
L_ = an.loc

HITS = [(289, "A06 stamp POP"), (325, "A07 stamp"), (361, "A08 stamp"), (491, "A11 whistle POP"),
        (1081, "B09 brass SHAKE"), (1117, "B11a POP"), (1153, "B11b POP"), (1189, "B13a POP"), (1225, "B13b POP"),
        (1261, "B13c POP"), (1297, "B13d POP"), (1332, "B15 flash 1"), (1360, "B16 black"), (1369, "C01a INK"),
        (1441, "C02 POP"), (1477, "C03 POP"), (1513, "C04 POP"), (1549, "C05 POP"), (1585, "C06 POP"),
        (1621, "C07 POP"), (1657, "C08 INK"), (1765, "C11a pass 1"), (1801, "C11b pass 2"), (1837, "C11c pass 3"),
        (1873, "C11d pull-back to the sheet"), (1945, "C12b POP"), (1981, "C13 last hit: logo lands"),
        (1989, "C13 drain starts"), (2000, "C13 glint (v2.9: 2000-2040, LOGO.md v1.4)"), (2040, "C13 drop leaves (drip cue)")]

# land colour keys (§4.2) for the cards
KEY = {"A": ((70, 92, 96), (150, 132, 104)), "B01": ((222, 220, 230), (150, 140, 170)), "B02": ((222, 220, 230), (150, 140, 170)),
       "B03": ((214, 176, 92), (120, 86, 48)), "B04": ((214, 176, 92), (120, 86, 48)),
       "B05": ((40, 70, 140), (190, 200, 210)), "B06": ((40, 70, 140), (190, 200, 210)),
       "B07": ((224, 150, 92), (210, 200, 186)), "B08": ((224, 150, 92), (210, 200, 186)),
       "B09": ((84, 120, 104), (214, 206, 186)), "B10": ((60, 80, 76), (150, 140, 120)), "B11": ((84, 120, 104), (214, 206, 186)),
       "B12": ((150, 56, 40), (30, 24, 24)), "B13": ((150, 56, 40), (30, 24, 24)), "B14": ((150, 56, 40), (30, 24, 24)),
       "C01": ((210, 170, 90), (60, 90, 110)), "C02": ((40, 70, 140), (190, 200, 210)), "C03": ((214, 176, 92), (120, 86, 48)),
       "C04": ((180, 170, 200), (150, 60, 50)),
       "C08": ((210, 170, 90), (80, 110, 100)), "C09": ((210, 170, 90), (80, 110, 100)), "C10": ((210, 170, 90), (80, 110, 100)),
       "C11": ((214, 200, 168), (120, 100, 80)), "C12": ((214, 168, 84), (70, 84, 110))}

# placeholder text per NEW cut: (source tag, short shot text)
NEW = {
    "B01a": ("W01 → KW01 0.5–2.0 s", "Pale Crag · Ilvane — dawn, the sun behind the cliff; the Pale Spire on the cliff summit, the cloister round its foot; violet-and-white pennants"),
    "B01b": ("W01 → KW01 3.0–4.5 s, crop 1.8×", "Pale Crag — cut-in on galleries and terraces, pennants stirring, mist drifting right to left; no Spire"),
    "B02a": ("W02 → KW02 1.0–2.5 s", "Pale Crag · the Choir — rows of hooded Cantors, backs to camera, facing the sea; sun behind camera; no Spire"),
    "B02b": ("W02 → KW02 3.0–4.5 s, crop 1.8×", "the Choir — hems and hood edges rippling in the wind (backs only)"),
    "B03a": ("W03 → KW03 0.5–2.0 s", "The Polders · Dask — noon gold; wind-pumps with ochre sails on the dike; the Sheaf Spire alone among the fields on a low rise; pan left"),
    "B04a": ("W04 → KW04 1.0–2.5 s", "The Polders · the dike workers — wide-brimmed hats, spades, walking away along the crest; canal flowing right to left; no tower"),
    "B03b": ("W03 → KW03 2.5–4.0 s, crop 1.6×", "Polders — cut-in on ochre pump sails turning the same way; grain waves; no Spire"),
    "B04b": ("W04 → KW04 3.0–4.5 s, crop 1.4×", "dike workers — low cut-in: spades on shoulders, ochre pennants snapping"),
    "B05a": ("W05 → KW05 0.5–2.0 s", "Gullmouth · Corvane — morning, sun high behind the town; the Sentinel Spire on the crown of the headland; the mole, posts unlit; glide left"),
    "B06a": ("W06 → KW06 0.5–2.0 s", "Gullmouth · the fleet — Corvane column under white sails, deep-blue pennants, past the mole's end, right to left; no tower"),
    "B05b": ("W05 → KW05 2.5–4.0 s, crop 1.5×", "Gullmouth — along the mole: many identical unlit posts, none singled out; waves run right to left"),
    "B06b": ("W06 → KW06 3.0–4.5 s", "the fleet — the nearest mainsail fills toward the lens → MATCH into the kite"),
    "B07a": ("W07 → KW07 1.0–2.5 s", "The Ossari uplands — ochre-pink terraced town, kites on roof poles, flyers in hoods (head only, faces never covered), backs"),
    "B08a": ("W08 → KW08 0.5–2.0 s", "The Ossari · the sky — tilt up into the kites; gliders far off, flying away inland"),
    "B07b": ("W07 → KW07 3.0–4.5 s, crop 1.5×", "Ossari — cut-in on plain kites tugging, more kites cut by the frame edges (never a countable few)"),
    "B08b": ("W08 → KW08 2.5–4.0 s", "the sky — the tilt carries on; gliders moving away"),
    "B09": ("W09 → KW09 0.5–1.25 s", "RISE 0.75 s · The Shoals · Quell — storm-dark; salt pans; Brackwater, the Storm Spire small in it"),
    "B10a": ("W10 → KW10 0.5–1.25 s", "The Shoals · the beacons — squat beacon towers fading into rain; rain gusts sweep the reeds; no tower"),
    "B11a": ("W09 → KW09 2.0–2.75 s, crop 1.6×", "The Shoals · the salt — salt heaps, sea-green-and-bone pennants, rain; no tower, boat or fire"),
    "B10b": ("W10 → KW10 2.5–3.25 s, crop 1.8×", "the reed channel — low dark boats slipping landward, away from camera; rain gusts"),
    "B11b": ("W09 → KW09 3.5–4.25 s, crop 2.0×", "salt sheds — yellowish sea-green-and-bone pennants flutter in rain; no tower, boat or fire"),
    "B12a": ("W11 → KW11 0.5–1.25 s", "The Stair · Rusk — last sun; the falls; the Falls Spire on its spur, crown above the edge; nothing on the lip"),
    "B13a": ("W12 → KW12 0.5–1.25 s", "The Stair · the pikes — camera TRACKS along the ranks, pike shafts passing in the foreground; soldiers still"),
    "B12b": ("W11 → KW11 1.75–2.5 s, crop 1.8×", "the white column of the falls; the lip bare"),
    "B13b": ("W12 → KW12 1.5–2.25 s", "the pikes — the tracking shot continues, parallax of shafts"),
    "B12c": ("W11 → KW11 2.75–3.5 s, crop 2.0×", "mist and spray rising at the foot of the falls"),
    "B13c": ("W12 → KW12 2.5–3.25 s", "the pikes — tracking, black cloaks rippling"),
    "B12d": ("W11 → KW11 3.75–4.5 s", "the Stair wide again, the push continues; nothing on the lip"),
    "B13d": ("W12 → KW12 3.25–4.0 s", "the pikes — tracking; the plain far below in haze"),
    "B14": ("W12 → KW12 4.1–4.85 s, crop 1.8×", "pike heads and rust-red pennants streaming (snare)"),
    "C01a": ("W13 → KW13 0.0–1.5 s", "CONVERGENCE — the realm from the western sea; eight Spires at their v0.10 places (schematic)"),
    "C01b": ("W13 → KW13 1.5–3.0 s, crop 1.4×, window right→left", "cut-in toward Highwater: two Spires on the hill, the Sluice Spire at the SW foot"),
    "C02L": ("W06 → KW06 1.5–2.25 s, crop 1.4×", "CORVANE's land — the fleet under white sails and deep-blue pennants (0.75 s on the beat)"),
    "C03L": ("W03 → KW03 4.0–4.75 s, crop 2.0×", "DASK's land — the nearest ochre pump sails turning; no Spire in the crop"),
    "C04": ("W14 → KW14 0.5–2.9 s @1.6×", "three pennants close together in the central third: Ilvane, Rusk, Quell"),
    "C08": ("W15 → KW15 0.0–1.5 s", "ONE WATER — ordinary river traffic both ways, every house colour; current right to left; no warships"),
    "C09": ("W15 → KW15 1.5–3.0 s, crop 1.8×", "hulls of at least three colours, bow waves"),
    "C10": ("W15 → KW15 3.0–4.5 s, crop 1.3×, window right→left", "sails passing the reed islands"),
    "C12a": ("W13 → KW13 3.0–4.5 s, low gold sun", "MAP → LAND — the realm in low gold sun, the sun still above the sea; camera pushing in"),
    "C12b": ("W13 → KW13 3.5–5.0 s, crop 1.3×, window right→left", "Highwater in low gold sun; the 1:21.0 hit on the cut"),
}
MAPTXT = {"C11a": "MAP pass 1 — KW16 0.0–1.2 s reversed @0.8×, crop 2.0×: along the painted river from the falls, right→left",
          "C11b": "MAP pass 2 — KW16 0.0–1.2 s reversed @0.8×, crop 1.8×: on down the river across the ruled fields",
          "C11c": "MAP pass 3 — KW16 1.3–2.5 s reversed @0.8×, crop 1.6×: through the channels past the hill city to the sea",
          "C11d": "MAP 4 — KW16 0.0–1.2 s reversed @0.8×: the pull-back ends on the whole sheet (W16) → C12a"}
FLASHES = ["B02a", "B04a", "B06a", "B08a", "B11a", "B13a"]   # B15: KW02, KW04, KW06, KW08, KW09 crop, KW12 (+ K05)


def key(cut):
    for k in (cut[:3], cut[:1]):
        if k in KEY:
            return KEY[k]
    return KEY["A"]


# ------------------------------------------------------------------------------------------------ cards ---
def schematic(d, box, persp=False):
    """canon v0.10 compass: north up, sea west (left); eight tower marks at their sites."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    P = lambda fx, fy: (x0 + fx * w, y0 + fy * h)
    d.rectangle(box, fill=(196, 180, 140))
    d.rectangle((x0, y0, x0 + 0.16 * w, y1), fill=(70, 96, 110))                      # sea (west)
    d.rectangle((x0 + 0.9 * w, y0, x1, y1), fill=(150, 60, 44))                       # escarpment (east)
    d.line([P(0.9, 0.48), P(0.6, 0.5), P(0.35, 0.52), P(0.16, 0.5)], fill=(90, 120, 140), width=8)   # the Aun
    for fy in (0.38, 0.62):
        d.line([P(0.35, 0.52), P(0.16, fy)], fill=(90, 120, 140), width=4)
    for k in range(4):                                                                # barrier islands
        d.ellipse((*P(0.06, 0.36 + 0.08 * k), *P(0.1, 0.4 + 0.08 * k)), fill=(210, 200, 170))
    marks = {"Crown": (0.26, 0.48), "Choir": (0.285, 0.46), "Sluice": (0.235, 0.555), "Sentinel": (0.17, 0.2),
             "Pale": (0.17, 0.82), "Sheaf": (0.6, 0.38), "Falls": (0.885, 0.46), "Storm": (0.08, 0.5)}
    f = ImageFont.truetype(FONT, 18)
    for n, (fx, fy) in marks.items():
        x, y = P(fx, fy)
        d.polygon([(x, y - 26), (x - 7, y + 6), (x + 7, y + 6)], fill=(16, 16, 20))
        d.text((x + 9, y - 14), n, fill=(30, 26, 22), font=f)
    d.text(P(0.02, 0.02), "N ↑   sea W   escarpment E", fill=(20, 20, 20), font=ImageFont.truetype(FONT, 20))


SHEET = (150, 100, 1770, 980)        # the map card: a sheet on a dark wooden table (v2.2, no title-map grammar)


def map_card():
    p = f"{WK}/card_map_table.png"
    rng = np.random.default_rng(7)
    wood = np.zeros((H, W, 3), np.float32) + np.array([58, 40, 28], np.float32)
    grain = np.cumsum(rng.normal(0, 1, (H, 1)), 0) * 0.8 + 6 * np.sin(np.arange(W)[None, :] / 37.0 + np.arange(H)[:, None] / 90.0)
    wood += grain[..., None] * np.array([0.8, 0.55, 0.4])
    im = Image.fromarray(np.clip(wood, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(im)
    d.rectangle((110, 60, 1810, 1020), fill=(214, 200, 168))                          # the linen sheet
    schematic(d, SHEET)
    paper = np.array(im).astype(np.float32)
    paper[60:1021, 110:1811] *= (1 + rng.normal(0, 0.025, (961, 1701, 1)))           # paper grain
    xx = np.linspace(-1, 1, W)[None, :, None]
    paper *= (1.08 - 0.16 * (xx + 1) / 2)                                             # low raking light from the left
    Image.fromarray(np.clip(paper, 0, 255).astype(np.uint8)).save(p)
    return p


def card(cut):
    p = f"{WK}/card_{cut}.png"
    c0, c1 = key(cut)
    yy = np.linspace(0, 1, H)[:, None, None]
    img = (np.array(c0) * (1 - yy) + np.array(c1) * yy).repeat(W, 1)
    im = Image.fromarray(img.astype(np.uint8))
    d = ImageDraw.Draw(im)
    if cut.startswith(("C01", "C12")):
        schematic(d, (360, 330, 1560, 1000))
    if cut == "C04":     # v2.2: three pennants close together in the central third (vertical-safe, W14)
        for i, (a, b) in enumerate([((178, 160, 210), (240, 240, 236)), ((160, 60, 40), (20, 18, 18)), ((150, 178, 120), (230, 222, 200))]):
            x = 700 + i * 190
            d.polygon([(x, 340), (x + 150, 380), (x + 150, 560), (x, 600)], fill=a)
            d.polygon([(x, 600), (x + 150, 560), (x + 150, 700), (x, 860)], fill=b)
    tag_, txt = NEW[cut]
    d.rectangle((60, 60, W - 60, 300), fill=(0, 0, 0))
    d.text((90, 80), f"{cut}  ·  PENDING  ·  NEW {tag_}", fill=(250, 220, 120), font=ImageFont.truetype(FONTB, 40))
    for i, ln in enumerate(textwrap.wrap(txt, 78)[:3]):
        d.text((90, 150 + 44 * i), ln, fill=(236, 236, 236), font=ImageFont.truetype(FONT, 34))
    im.save(p)
    return p


def tally_overlay(n=3):
    """variant A (§7): n bold dark-ink strokes on the clean left page, 10 % of frame height, visible from frame 1."""
    p = f"{WK}/tally_{n}.png"
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x0, y0, hh = 560, 560, 108
    for k in range(n):
        if k % 5 == 4:   # the fifth stroke crosses the four
            d.line([(x0 + (k // 5) * 150 - 14, y0 + hh * 0.75), (x0 + (k // 5) * 150 + 96, y0 + hh * 0.2)], fill=(38, 30, 30, 240), width=11)
            continue
        x = x0 + (k // 5) * 150 + (k % 5) * 26
        d.line([(x, y0 + hh), (x + 10, y0)], fill=(38, 30, 30, 240), width=11)
    im.save(p)
    return p


# ----------------------------------------------------------------------------------------- primitives ---
def tag(g, s, text):
    p = f"{WK}/tag_{g.cut}.txt"
    open(p, "w").write(text)
    o = g.lab()
    g.add(f"[{s}]drawtext=fontfile={FONT}:textfile={p}:fontsize=22:fontcolor=white@0.9:x=16:y=14:"
          f"box=1:boxcolor=black@0.5:boxborderw=5[{o}]")
    return o


def piece(g, path, ss, src_t, speed=1.0, z=1.0, fx=0.5, fy=0.5, mci=False, every=1, reverse=False):
    """a piece of a clip: ss..ss+src_t played at `speed`, interpolated with mci when < 0.8x (§12), cover-cropped.
    No tpad: the source window must hold enough frames (§12 rule 3)."""
    i = g.clip(path, ss, src_t + 0.05)
    o = g.lab()
    rev = f"trim=end_frame={int(round(src_t * FPS)) + 1},reverse," if reverse else ""
    tim = f"setpts=(PTS-STARTPTS)/{speed}"
    interp = (f",minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" if mci else f",fps={FPS}")
    g.add(f"[{i}]{rev}{tim}{interp},scale={int(W * z + 0.5) // 2 * 2 + 4}:{int(H * z + 0.5) // 2 * 2 + 4}:"
          f"force_original_aspect_ratio=increase,crop={W}:{H}:x='(iw-ow)*{fx}':y='(ih-oh)*{fy}',setsar=1[{o}]")
    return o


def card_motion(g, path, z0=1.0, z1=1.07, fx=0.5, fy=0.5, fx1=None, fy1=None, speed=900):
    """placeholder card: linear camera move (never eased to a stop) + drifting clouds, so no frame repeats."""
    s = an.zp(g, g.still(path), z0, z1, fx, fx if fx1 is None else fx1, fy, fy if fy1 is None else fy1, curve="lin")
    return an.clouds(g, s, speed)


def fxy(c, z, full):
    """crop-window centre (px) -> zoompan fraction, clamped inside the frame"""
    return min(1.0, max(0.0, (c / full - 0.5 / z) / (1 - 1 / z))) if z > 1 else 0.5


def run(g, s, out):
    o = g.lab()
    g.add(f"[{s}]format=yuv420p,setsar=1[{o}]")
    return an.run_cut(g, o, out)


def from_seg(cut, s1, first=0, z=1.0, fx=0.5, fy=0.5, speed=1.0, label="", over=None):
    """frames of an S1 OP v3 render (24 fps, 1920x1080)."""
    g = an.G(cut)
    i = g.clip(f"{S1SEG}/{s1}.mp4", first / FPS, g.n / FPS * speed + 0.1)
    o = g.lab()
    blend = ",tmix=frames=2" if speed >= 2 else ""
    g.add(f"[{i}]setpts=(PTS-STARTPTS)/{speed},fps={FPS}{blend},scale={int(W * z) // 2 * 2}:-2,"
          f"crop={W}:{H}:x='(iw-ow)*{fx}':y='(ih-oh)*{fy}',setsar=1[{o}]")
    if over:
        oi, o2 = g.still(over), g.lab()
        g.add(f"[{o}][{oi}]overlay=0:0:format=auto:shortest=1[{o2}]")
        o = o2
    return run(g, tag(g, o, label), f"{an.SEG}/{cut}.mp4")


# ------------------------------------------------------------------------------------------------ build ---
BANNER = {"C02": ("K11", 0.5, 0.0, "CORVANE"), "C03": ("K11", 2.5, 1.0, "DASK"),
          "C05": ("K12", 0.5, 0.0, "LANTRY"), "C06": ("K12", 2.5, 1.0, "FENNICK")}


def build(cut):
    out = f"{an.SEG}/{cut}.mp4"
    g = an.G(cut)
    L = lambda f: L_(cut, f)
    if cut == "A01a":   # v2.2 stand-in for KA01 (the redesigned swell): PAID K16 heavy dark swell, 1.0x, crop 1.25x
        s = piece(g, f"{CL}/K16.mp4", 0.0, 1.5, z=1.25, fx=0.5, fy=0.85)
        s = an.rain(g, an.mist(g, s, 0.12), darken=False)
        return run(g, tag(g, s, "A01a stand-in PAID K16 0.0-1.5 s @1.0x crop 1.25x -> NEW KA01 (swell, no curling crest) PENDING"), out)
    if cut == "A01b":   # v2.2 stand-in: PAID K01 take 2, the swell striking the wall face, 1.0x, crop 1.8x low on the face
        s = piece(g, f"{CL}/K01_t2.mp4", 0.0, 1.5, z=1.8, fx=0.3, fy=0.8)
        s = an.rain(g, s, darken=False)
        return run(g, tag(g, s, "A01b stand-in PAID K01_t2 0.0-1.5 s @1.0x crop 1.8x -> NEW KA01 1.5-3.0 s (strike) PENDING"), out)
    if cut == "A02":
        return from_seg(cut, "02", label="A02 PAID plate D01_A, LA stand-in -> NEW KA02 PENDING")
    if cut == "A03":
        return from_seg(cut, "02b", label="A03 PAID K03 0.0-1.5 s")
    if cut in ("A04a", "A04b"):
        # the video-test alley clip with the v1.4 static patches (plain brick over the double gate, plain planks over
        # the ring knocker), a LINEAR push (an eased push stalls at its ends: §12 check), mist drifting
        b = cut == "A04b"
        c = g.clip(an.ALLEY, 2.0 if b else 0.5, 1.6)
        o, pa, pb = g.lab(), g.lab(), g.lab()
        z0, z1 = (1.80, 1.87) if b else (1.0, 1.06)
        g.add(f"[{c}]setpts=PTS-STARTPTS,split=3[{o}a][{o}b][{o}c];[{o}b]trim=end_frame=1,loop=loop=-1:size=1,crop=140:130:775:495[{pa}];"
              f"[{o}c]trim=end_frame=1,loop=loop=-1:size=1,crop=44:80:60:568[{pb}];"
              f"[{o}a][{pa}]overlay=915:495:shortest=1[{o}d];[{o}d][{pb}]overlay=122:568:shortest=1,fps={FPS},"
              f"scale=w='2*trunc(1950*({z0}+{z1 - z0:.3f}*t/1.5)/2)':h=-2:eval=frame,crop={W}:{H}:x='(iw-ow)*0.45':y='(ih-oh)*0.45',setsar=1[{o}]")
        s = an.overlay_field(g, o, A["fog"], "screen", 0.2, f"crop={W}:{H}:x='(iw-ow)*t/6':y=0")
        return run(g, tag(g, s, f"{cut} PAID alley clip {'2.0-3.5 s crop 1.8x' if b else '0.5-2.0 s'} (gate + knocker patched)"), out)
    if cut == "A05a":
        s = piece(g, f"{CL}/K07_fix.mp4", 0.5, 1.5)
        return run(g, tag(g, an.mist(g, s, 0.12), "A05a PAID K07_fix 0.5-2.0 s"), out)
    if cut == "A05b":
        s = piece(g, f"{CL}/K07_fix.mp4", 2.0, 1.875, speed=1.25)
        return run(g, tag(g, an.mist(g, s, 0.12), "A05b PAID K07_fix 2.0-3.875 s @1.25x"), out)
    if cut == "A06":    # v2.2: KA06 dropped (budget for KA01); PAID K05 hub crop 2.0x on the first stamp
        s = piece(g, f"{CL}/K05.mp4", 2.0, 1.5, z=2.0, fx=0.3, fy=0.45)
        s = an.shake(g, an.pop(g, s, [L(289)]), [(L(289), 8, 6)])
        return run(g, tag(g, s, "A06 PAID K05 2.0-3.5 s crop 2.0x (hub), POP + SHAKE 289"), out)
    if cut == "A07":
        return from_seg(cut, "06", label="A07 PAID K04 0.5-2.0 s")
    if cut == "A08":
        return from_seg(cut, "07", label="A08 PAID K05 0.0-1.5 s")
    if cut == "A09":    # v2.2: KA09 dropped (budget for KA01); PAID K04 rim at 1.8x on the loudest groove half-bar
        s = piece(g, f"{CL}/K04.mp4", 2.5, 1.5, z=1.8, fx=0.6, fy=0.4)
        s = an.shake(g, s, [(0, 6, 9)])
        return run(g, tag(g, s, "A09 PAID K04 2.5-4.0 s crop 1.8x (rim slats rushing)"), out)
    if cut == "A10":
        return from_seg(cut, "14", speed=2.0, over=tally_overlay(3),
                        label="A10 PAID K10 0.5-3.5 s @2x · variant A tally (sample E3) visible from frame 1")
    if cut == "A11":
        s = an.zp(g, g.still(A["F17"]), 1.08, 1.16, 0.0, 1.0, 0.5, 0.5, curve="in")
        s = an.clouds(g, s, 400)
        o = g.lab()
        pk = L(491)
        g.add(f"[{s}]gblur=sigma=10:sigmaV=0.01:enable='between(n,{pk - 6},{pk - 3})',"
              f"gblur=sigma=40:sigmaV=0.01:enable='between(n,{pk - 2},{g.n})'[{o}]")
        s = an.pop(g, o, [pk])
        return run(g, tag(g, s, "A11 PAID F17, LA stand-in -> NEW KA11 PENDING; WHIP right, POP 491"), out)
    if cut == "B15":
        srcs = [f"{WK}/card_{c}.png" for c in FLASHES]
        base = None
        for k, pth in enumerate(srcs + [None]):
            if pth is None:   # K05 frames 12-15 as real motion
                s0 = piece(g, f"{CL}/K05.mp4", 12 / FPS, 0.3)
                s = g.lab()
                g.add(f"[{s0}]setpts=PTS+{4 * k}/{FPS}/TB[{s}]")      # frames 12-15 land on flash slot 7
            else:
                s = card_motion(g, pth, 1.0 + 0.02 * k, 1.04 + 0.02 * k)
            if base is None:
                base = s
            else:
                o = g.lab()
                g.add(f"[{base}][{s}]overlay=0:0:enable='between(n,{4 * k},{4 * k + 3})'[{o}]")
                base = o
        o = g.lab()
        g.add(f"[{base}]eq=brightness='0.04*(" + "+".join(f"eq(n,{4 * k})" for k in range(7)) + ")':eval=frame[" + o + "]")
        s = an.shake(g, o, [(f, 6, 9) for f in (0, 9, 18, 27)])
        return run(g, tag(g, s, "B15 FLASH: KW02 KW04 KW06 KW08 KW09 KW12 (PENDING) + PAID K05 f12-15"), out)
    if cut == "B16":
        i = g.still(A["F01"])
        o = g.lab()
        g.add(f"[{i}]scale={W}:{H},eq=brightness=-1:contrast=0,setsar=1[{o}]")
        return run(g, o, out)
    if cut in BANNER:   # v2.2: 0.75 s on the hit, sped up 1.8x (constant), PUSH 3 %
        clip, ss, fx, name = BANNER[cut]
        s = piece(g, f"{CL}/{clip}.mp4", ss, 1.35, speed=1.8, z=1 / 0.6, fx=fx, fy=0.35)
        s = an.vpush(g, s, 1.0, 1.03)
        s = an.shake(g, an.pop(g, s, [L(an.START[cut] + 1)]), [(1, 5, 9)])
        return run(g, tag(g, s, f"{cut} PAID {clip} banner {name} {ss}-{ss + 1.35:.2f} s @1.8x, PUSH 3%"), out)
    if cut == "C05L":   # Lantry's land: the coins, another window of K10
        s = piece(g, f"{CL}/K10.mp4", 0.0, 1.5, speed=2.0, z=1.6, fx=1.0, fy=0.15)
        return run(g, tag(g, s, "C05L PAID K10 0.0-1.5 s @2x crop 1.6x (Lantry: the coins)"), out)
    if cut == "C06L":   # Fennick's land: the wheels of the Lows, another window of K05
        s = piece(g, f"{CL}/K05.mp4", 3.5, 0.75, z=1.8, fx=0.7, fy=0.5)
        return run(g, tag(g, s, "C06L PAID K05 3.5-4.25 s crop 1.8x (Fennick: the wheels)"), out)
    if cut == "C07":
        s = an.zp(g, g.still(A["F17"]), 2.2, 2.29, 0.436, 0.436, 0.37, 0.37, curve="lin")
        o = g.lab()
        g.add(f"[{s}]noise=alls=8:allf=t[{o}]")
        s = an.pop(g, o, [L(1621)])
        return run(g, tag(g, s, "C07 PAID F17 crop 2.2x, stand-in -> KA11 0.0-2.4 s @1.6x keyed on banner 3 PENDING; POP 1621"), out)
    if cut == "C13":
        return build_title()
    if cut.startswith("C11"):   # v2.2: diagonal passes along the painted river over a sheet on a table, then the pull-back
        x0, y0, x1, y1 = SHEET
        P = lambda fx, fy: (x0 + fx * (x1 - x0), y0 + fy * (y1 - y0))
        path = {"a": (2.0, P(0.88, 0.42), P(0.66, 0.53)), "b": (1.8, P(0.68, 0.58), P(0.42, 0.45)),
                "c": (1.6, P(0.46, 0.58), P(0.12, 0.47)), "d": (1.15, (960, 540), (960, 540))}[cut[-1]]
        z, (ax, ay), (bx, by) = path
        z1 = 1.0 if cut == "C11d" else z
        s = card_motion(g, map_card(), z, z1, fxy(ax, z, W), fxy(ay, z, H), fxy(bx, z, W), fxy(by, z, H), speed=300)
        s = an.shake(g, an.pop(g, s, [L(an.START[cut] + 1)]), [(1, 6, 9)])
        return run(g, tag(g, s, f"{cut} PENDING (UPGRADE) · " + MAPTXT[cut]), out)
    # ---- NEW: cards
    p = f"{WK}/card_{cut}.png"
    crop = {"B01b": 1.8, "B02b": 1.8, "B03b": 1.6, "B04b": 1.4, "B05b": 1.5, "B07b": 1.5, "B10b": 1.8, "B11a": 1.6,
            "B11b": 2.0, "B12b": 1.8, "B12c": 2.0, "B14": 1.8, "C01b": 1.4, "C02L": 1.4, "C03L": 2.0, "C09": 1.8,
            "C10": 1.3, "C12b": 1.3}.get(cut, 1.0)
    if cut.startswith("B13"):        # KW12 tracks along the ranks (right to left)
        s = card_motion(g, p, 1.15, 1.15, 0.8, 0.0, 0.5, 0.5)
    elif cut in ("C01b", "C10", "C12b", "B03a", "B03b", "B05a", "B05b"):   # windows / camera moving right to left
        s = card_motion(g, p, crop * 1.08, crop * 1.10, 0.7, 0.0, 0.3, 0.3)
    else:
        s = card_motion(g, p, crop, crop * 1.07, 0.5, 0.0 if crop > 1 else 0.5)
    if cut.startswith("C12"):        # low gold sun, never dusk (keeper R2.2)
        o = g.lab()
        g.add(f"[{s}]colorbalance=rs=0.06:gs=0.02:bs=-0.08:rm=0.05:bm=-0.04,eq=saturation=1.1[{o}]")
        s = o
    pops = [h for h, _ in HITS if an.START[cut] <= h < an.START[cut] + g.n and "INK" not in _ and "SHAKE" not in _
            and "flash" not in _ and "black" not in _]
    s = an.pop(g, s, [L(h) for h in pops])
    if cut == "B09":
        s = an.shake(g, s, [(L(1081), 6, 9)])
    if cut in ("C09", "C10", "B14"):
        s = an.shake(g, s, [(1, 6, 9)])
    if cut == "C01a":
        s = an.shake(g, an.ink(g, s, 0), [(0, 12, 3)])
    if cut == "C08":
        s = an.ink(g, s, 0)
    return run(g, s, out)


def plate_band():
    """the darker plate under the word (analyst #5, marketer §2.1): -40 % behind the dry upper half, -60 % behind the
    wet lower half, soft edges; the logo itself is never darkened (keeper R2.5)."""
    p = f"{WK}/plate_band.png"
    y = np.arange(H, dtype=np.float32)
    sm = lambda e0, e1: (lambda u: u * u * (3 - 2 * u))(np.clip((y - e0) / (e1 - e0), 0, 1))
    a = (0.40 + 0.20 * sm(540, 780)) * sm(250, 470) * (1 - sm(930, 1080))    # no visible step anywhere
    x = np.linspace(-1, 1, W, dtype=np.float32)
    a = a[:, None] * (0.75 + 0.25 * np.abs(x)[None, :])          # a touch more at the outer letters (H, O, N, E)
    rgba = np.zeros((H, W, 4), np.uint8)
    rgba[..., 3] = (np.clip(a, 0, 1) * 255).astype(np.uint8)
    Image.fromarray(rgba, "RGBA").save(p)
    return p


def build_title(clean=False, out=None):
    """C13, the logo reveal on the final hit (LOGO.md §4 v1.1, landing on 1981), tail scripted second by second:
    1981 hit, INK + spray wipe 1981-1992, logo lands 1981-1988 (114 % -> 100 %), SHAKE 1981-1986; 1989-2004 the water
    drains top-down to the tide line, ABOVE the line only (below it the master as painted in every frame); 2016-2039
    one glint on the dry letters; 2020-2039 a drop gathers under a lower letter, sky/stone-tinted, never brighter than
    the dry letters, leaves on 2040 (drip cue, composer); 2041-2075 clouds stream past the crown; 2076-2087 fade.
    The plate under the word is darkened (plate_band); the logo keeps its own colours."""
    cut = "C13"
    g = an.G(cut)
    out = out or f"{an.SEG}/{cut}.mp4"
    L = lambda f: L_(cut, f)
    hit = L(1981)
    gold = f"{WK}/card_C12b_gold.png"
    im = Image.open(f"{WK}/card_C12b.png").convert("RGB")
    Image.blend(im, Image.new("RGB", im.size, (200, 150, 70)), 0.2).save(gold)
    a = an.zp(g, g.still(gold), 1.3 * 1.07, 1.3 * 1.09, 0.5, 0.5, 0.0, 0.0, curve="lin")
    a = an.ink(g, a, hit)
    a = an.spray_burst(g, a, 0.5, 0.9, 0.6, t0=hit / FPS, dur=13 / FPS)
    b = piece(g, f"{CL}/K17.mp4", 0.0, 4.5, z=1.5, fx=0.42, fy=0.0)
    b = an.vpush(g, b, 1.0, 1.03, 0.5, 0.3)
    o = g.lab()
    g.add(f"[{b}]colorbalance=rs=-0.04:bs=0.06:rm=-0.03:bm=0.04[{o}]")
    bi, ob = g.still(plate_band()), g.lab()
    g.add(f"[{o}][{bi}]overlay=0:0:format=auto:shortest=1[{ob}]")
    w = g.lab()
    g.add(f"[{a}]settb=AVTB,fps={FPS}[{w}a];[{ob}]settb=AVTB,fps={FPS}[{w}b];[{w}a][{w}b]xfade=transition=custom:"
          f"duration=0.5:offset={hit / FPS:.5f}:expr='if(gt(Y/H+0.06*sin(X/W*23)+0.03*sin(X/W*71),P*1.12),B,A)'[{w}]")
    LW, TIDE, s0 = 1300, 243, hit          # logo frames counted from the hit
    li = g.still(LOGO)
    lg = g.lab()
    # wet layer: ABOVE the tide line only (lt(Y,TIDE)); the edge slides down 1989-2004; a residue fades by 2010
    g.add(f"[{li}]scale={LW}:-1,format=rgba,split=3[{lg}d][{lg}w0][{lg}g0];"
          f"[{lg}w0]eq=brightness=-0.16:saturation=0.75,colorbalance=bs=0.08:bm=0.05,"
          f"geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='alpha(X,Y)*lt(Y,{TIDE})*clip((Y-{TIDE}*clip((N-{s0 + 8})/16,0,1))/10+1,0,1)*(1-clip((N-{s0 + 23})/6,0,1))'[{lg}w];"
          f"[{lg}g0]geq=r=235:g=242:b=250:a='alpha(X,Y)*lt(Y,{TIDE})*0.32*exp(-pow((X-0.35*Y-(-300+(W+600)*clip((N-{s0 + 35})/24,0,1)))/34,2))'[{lg}g];"
          f"[{lg}d][{lg}w]overlay=0:0:format=auto[{lg}1];[{lg}1][{lg}g]overlay=0:0:format=auto,"
          f"scale=w='2*trunc(iw*if(lt(n,{s0 + 8}),1.14-0.14*clip((n-{s0})/8,0,1),1)*(1+0.015*n/108)/2)':h=-2:eval=frame[{lg}]")
    o = g.lab()
    g.add(f"[{w}][{lg}]overlay=x='(W-w)/2+if(between(n,{s0},{s0 + 5}),6*sin(n*2.6),0)':"
          f"y='660-h/2+if(between(n,{s0},{s0 + 5}),4*cos(n*3.1),0)':eval=frame:format=auto:enable='gte(n,{s0})'[{o}]")
    s = o
    # the drop: sky/stone-tinted (no white core, never brighter than the dry letters), gathers 2020, leaves on 2040
    di, d_ = g.still(A["drop"]), g.lab()
    t_g0, t_go = L(2020) / FPS, L(2040) / FPS
    g.add(f"[{di}]format=rgba,colorchannelmixer=rr=0.50:gg=0.52:bb=0.58:rb=0.06,"
          f"scale=w='2*trunc(max(4,34*min(1,max(0,(t-{t_g0:.3f})/{t_go - t_g0:.3f})))/2)':h=-2:eval=frame[{d_}m];"
          f"[{s}][{d_}m]overlay=x={int(W / 2 + LW * 0.17)}-w/2:y='{660 + 488 // 2 - 40}+if(gt(t,{t_go:.3f}),1500*pow(t-{t_go:.3f},2),0)':"
          f"eval=frame:enable='gte(t,{t_g0:.3f})':shortest=1[{d_}]")
    o2 = g.lab()
    g.add(f"[{d_}]trim=end_frame={g.n},format=yuv420p,setsar=1[{o2}]")
    s = o2 if clean else tag(g, o2, "C13 LOGO REVEAL 1981: INK + spray wipe; lands, upper part wet (above the tide line only), "
                                    "drains to 1:23.5, glint 1:24.0, drop 1:25.0; darker plate under the word; PAID K17")
    return run(g, s, out)


# ===MASTER===
def master():
    lst = f"{WK}/concat.txt"
    with open(lst, "w") as f:
        for c, _, _ in CUTS:
            f.write(f"file '{an.SEG}/{c}.mp4'\n")
    bug = f"{WK}/bug.txt"
    open(bug, "w").write("ANIME-STYLE · AI-ANIMATED  ·  SAGA OP ANIMATIC v3 (storyboard v2.2, music anthem v1a)")
    pre = f"atrim=0:{an.TOTAL / FPS},asetpts=PTS-STARTPTS,afade=t=out:st={an.FADE_ST}:d={an.FADE_D}"
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", an.MUSIC, "-af", f"{pre},loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True)
    js = json.loads(r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={js['input_i']}:measured_TP={js['input_tp']}:"
          f"measured_LRA={js['input_lra']}:measured_thresh={js['input_thresh']}:offset={js['target_offset']}:linear=true")
    vf = (f"setpts=N/{FPS}/TB,fps={FPS},"
          f"drawtext=fontfile={FONT}:textfile={bug}:fontsize=18:fontcolor=white@0.55:x=w-tw-24:y=h-th-20,"
          f"drawtext=fontfile={FONT}:text='f %{{frame_num}}  %{{pts\\:hms}}':fontsize=22:fontcolor=white@0.9:"
          f"x=16:y=h-th-18:box=1:boxcolor=black@0.5:boxborderw=4,"
          f"fade=t=out:st={an.FADE_ST}:d={an.FADE_D}")
    af = f"{pre},{ln},aresample=48000,atrim=0:{an.TOTAL / FPS}"
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", an.MUSIC,
           "-filter_complex", f"[0:v]{vf}[v];[1:a]{af}[a]", "-map", "[v]", "-map", "[a]",
           "-frames:v", str(an.TOTAL), "-r", str(FPS), "-c:v", "libx264", "-preset", "slow", "-crf", "14", "-tune", "film",
           "-g", "48", "-maxrate", "40M", "-bufsize", "80M",
           "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-t", f"{an.TOTAL / FPS}",
           "-movflags", "+faststart", OUT]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr[-2000:])


# ----------------------------------------------------------------------------------------------- checks ---
def cut_of(f):
    for c, s0, n in CUTS:
        if s0 <= f < s0 + n:
            return c
    return "?"


CROP = "crop=iw:ih-130:0:60,"   # the animatic burns a frame counter and tags in; they are cropped off for the check


def check(path):
    """§12 rule 5: freezedetect (n=0.001, d=0.15) + mpdecimate near-duplicates; the planned black is allowed."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-vf", f"{CROP}freezedetect=n=0.001:d=0.15", "-an", "-f", "null", "-"],
                       capture_output=True, text=True)
    st = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", r.stderr)]
    en = [float(x) for x in re.findall(r"freeze_end: ([\d.]+)", r.stderr)]
    freezes = []
    for k, a in enumerate(st):
        b = en[k] if k < len(en) else an.TOTAL / FPS
        fa, fb = round(a * FPS), round(b * FPS) - 1
        planned = fa >= 1360 - 1 and fb <= 1368 + 1
        freezes.append({"from": fa, "to": fb, "cut": cut_of(fa), "planned": planned})
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-vf", f"{CROP}mpdecimate=hi=64*4:lo=64*2:frac=0.33,showinfo",
                        "-an", "-f", "null", "-"], capture_output=True, text=True)
    times = [float(x) for x in re.findall(r"pts_time:([\d.]+)", r.stderr)]
    keptf = {round(t * FPS) for t in times}
    dups = [f for f in range(an.TOTAL) if f not in keptf]
    unplanned = [f for f in dups if not (1360 <= f <= 1368) and f < 2076]
    by_cut = {}
    for f in unplanned:
        by_cut.setdefault(cut_of(f), []).append(f)
    rep = {"freezedetect": freezes, "mpdecimate_dropped": len(dups),
           "mpdecimate_unplanned": {c: [v[0], v[-1], len(v)] for c, v in by_cut.items()}}
    print(json.dumps(rep, indent=1))
    return rep


def onset_env(hop=240, sr=24000, win=1024):
    """spectral-flux onset envelope at 10 ms steps (hop 240 @ 24 kHz); returns (env, seconds per step)."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", an.MUSIC, "-t", "87", "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
                         capture_output=True).stdout
    x = np.frombuffer(raw, np.float32)
    n = len(x) // hop
    pad = np.pad(x, (win // 2, win // 2))
    S = np.abs(np.fft.rfft(np.stack([pad[i * hop:i * hop + win] * np.hanning(win) for i in range(n)]), axis=1))
    f = np.concatenate([[0], np.maximum(np.diff(np.log1p(S), axis=0), 0).sum(1)])
    return f / f.max(), hop / sr


def onset_near(env, dt, t, w=0.12):
    a, b = int((t - w) / dt), int((t + w) / dt)
    k = a + int(np.argmax(env[a:b]))
    return k * dt


def contact(path):
    os.makedirs(CONTACT, exist_ok=True)
    TW, TH = 320, 180
    font = ImageFont.truetype(FONT, 14)

    def grab(idx):
        idx = sorted(set(idx))
        sel = "+".join(f"eq(n\\,{i})" for i in idx)
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"select='{sel}',scale={TW}:{TH}", "-vsync", "0",
                              "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
        return dict(zip(idx, np.frombuffer(raw, np.uint8).reshape(-1, TH, TW, 3)))

    # 1. cut sheet: first and last frame of every cut
    fr = grab([s for _, s, _ in CUTS] + [s + n - 1 for _, s, n in CUTS])
    cols = 6
    rows = (len(CUTS) + cols - 1) // cols
    im = Image.new("RGB", (cols * (2 * TW + 8), rows * (TH + 20)), (18, 18, 18))
    d = ImageDraw.Draw(im)
    for k, (c, s0, n) in enumerate(CUTS):
        x, y = (k % cols) * (2 * TW + 8), (k // cols) * (TH + 20)
        im.paste(Image.fromarray(fr[s0]).resize((TW, TH)), (x, y))
        im.paste(Image.fromarray(fr[s0 + n - 1]).resize((TW, TH)), (x + TW, y))
        d.text((x + 4, y + TH + 2), f"{c}  f{s0}-{s0 + n - 1}  {s0 / FPS:.3f}s  ({n} fr)", fill=(240, 230, 190), font=font)
    p1 = f"{CONTACT}/SAGA_OP_v3_cuts.png"
    im.save(p1)
    # 2. hit sheet: frames h-1, h, h+1 + music onset envelope h-12..h+12 (grid = h-1, placed = h)
    env, dt = onset_env()
    fr = grab([f for h, _ in HITS for f in (h - 1, h, h + 1) if 0 <= f < an.TOTAL])
    cols = 3
    cw, chh = 3 * 200 + 260, 112 + 22
    rows = (len(HITS) + cols - 1) // cols
    im = Image.new("RGB", (cols * cw, rows * chh), (18, 18, 18))
    d = ImageDraw.Draw(im)
    res = []
    for k, (h, lab) in enumerate(HITS):
        x, y = (k % cols) * cw, (k // cols) * chh
        for j, f in enumerate((h - 1, h, h + 1)):
            if f in fr:
                im.paste(Image.fromarray(fr[f]).resize((200, 112)), (x + j * 200, y))
        d.rectangle((x + 200, y, x + 399, y + 111), outline=(255, 210, 60), width=2)
        # envelope from frame h-3 to h+3 at 10 ms; yellow = placed frame span, blue = grid frame span
        gx, t0 = x + 604, (h - 3) / FPS
        steps = int(7 / FPS / dt)
        for j in range(steps):
            t = t0 + j * dt
            v = env[int(t / dt)]
            fno = int(t * FPS + 1e-6)
            col = (255, 210, 60) if fno == h else (120, 200, 255) if fno == h - 1 else (170, 170, 170)
            d.rectangle((gx + j * 8, y + 108 - int(100 * v), gx + j * 8 + 5, y + 108), fill=col)
        on = onset_near(env, dt, (h - 1) / FPS + 0.02)
        df = on * FPS - (h - 1)
        res.append((h, lab, round(on, 3), round(df, 2)))
        d.text((x + 4, y + 114), f"{lab}  placed f{h}  onset {on:.3f}s = grid {df:+.2f} fr", fill=(240, 230, 190), font=font)
    p2 = f"{CONTACT}/SAGA_OP_v3_hits.png"
    im.save(p2)
    json.dump(res, open(f"{CONTACT}/hit_onsets.json", "w"), indent=0)
    print(p1, p2)
    for r_ in res:
        print(r_)


# ---------------------------------------------------------------------------------------------- posters ---
PLIST = [  # marketer §2.3, storyboard §7.2: (id, what, final source, stand-in available now or None)
    ("P1", "Crown Spire at dawn, palace, mist of the Lows (vertical, crop x=656)", "KA02 / plate D01_A_op", ("img", "plates/D01_A_op.png")),
    ("P2", "Wall of five banners in late sun, city and sea", "KA11 first 1.0 s / F17", ("img", "frames/F17_op.png")),
    ("P3", "The whole Concord from the west in gold (channel banner 2560x1440)", "W13 / KW13", None),
    ("P4", "The falls and the Stair in last sun (vertical)", "W11 / KW11", None),
    ("P5", "Ossari kite sky", "W08 / KW08", None),
    ("P6", "Flyover over the Lows, hill with three Spires", "K07_fix 0.5 s", ("clip", "clips/K07_fix.mp4", 0.5)),
    ("P7", "Gullmouth mole (no post singled out)", "W05 / KW05", None),
    ("P8", "Polders, pumps with ochre sails", "W03 / KW03", None),
    ("P9", "Pale Crag in mist", "W01 / KW01", None),
    ("P10", "Shoals salt fields (crop as B11, no lights)", "W09 / KW09", None),
    ("P11", "Ossari terraced town", "W07 / KW07", None),
    ("P12", "The logo over the crown (frame 2028)", "C13 frame 2028, clean render", ("title", 48)),
    ("P13a", "Banner Corvane (K11 left)", "K11 0.5 s", ("clip", "clips/K11.mp4", 0.5)),
    ("P13b", "Banner Dask (K11 right)", "K11 2.5 s", ("clip", "clips/K11.mp4", 2.5)),
    ("P13c", "Banner Lantry (K12 left)", "K12 0.5 s", ("clip", "clips/K12.mp4", 0.5)),
    ("P13d", "Banner Fennick (K12 right)", "K12 2.5 s", ("clip", "clips/K12.mp4", 2.5)),
    ("P13e", "Banner the Choir (F17 banner 3)", "KA11 / F17", ("img", "frames/F17_op.png")),
    ("P13f", "Three pennants Ilvane, Rusk, Quell", "W14 / KW14", None),
]


def posters():
    """saves clean (no tag, counter or bug) full-size stills of every poster frame that exists now; NEW ones are
    listed as pending in manifest.json and are saved the same way from the accepted W frames / clips."""
    os.makedirs(POSTERS, exist_ok=True)
    man = []
    for pid, what, src, sb in PLIST:
        dst = f"{POSTERS}/{pid}.png"
        if sb is None:
            man.append({"id": pid, "what": what, "final_source": src, "status": "pending (NEW, saved at render)"})
            continue
        if sb[0] == "img":
            Image.open(f"{OUTD}/{sb[1]}").convert("RGB").save(dst)
        elif sb[0] == "clip":
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{sb[2]}", "-i", f"{OUTD}/{sb[1]}", "-frames:v", "1", dst], check=True)
        else:
            os.makedirs(an.SEG, exist_ok=True)
            ob.load_accept()
            ob.assets()
            card("C12b")
            tmp = f"{WK}/C13_clean.mp4"
            build_title(clean=True, out=tmp)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-vf", f"select=eq(n\\,{sb[1]})", "-frames:v", "1", dst], check=True)
        man.append({"id": pid, "what": what, "final_source": src, "status": "saved (stand-in)" if "stand" in src or sb[0] == "img" else "saved", "file": dst})
    json.dump(man, open(f"{POSTERS}/manifest.json", "w"), indent=1, ensure_ascii=False)
    print(json.dumps(man, indent=1, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--no-final", action="store_true")
    ap.add_argument("--check", default="")
    ap.add_argument("--contact", default="")
    ap.add_argument("--posters", action="store_true")
    a = ap.parse_args()
    if a.posters:
        posters()
        return
    if a.check:
        check(a.check)
        return
    if a.contact:
        contact(a.contact)
        return
    os.makedirs(an.SEG, exist_ok=True)
    ob.load_accept()
    ob.assets()
    for c in NEW:
        card(c)
    todo = [c for c, _, _ in CUTS if not a.only or c in a.only.split(",")]
    errs = []
    jobs = list(todo)
    with cf.ThreadPoolExecutor(a.jobs) as ex:
        futs = {ex.submit(build, c): c for c in jobs}
        for fu in cf.as_completed(futs):
            try:
                fu.result()
                print("ok", futs[fu], flush=True)
            except Exception as e:
                errs.append(futs[fu])
                print("FAIL", futs[fu], str(e)[:3000], flush=True)
    if errs:
        sys.exit(f"failed: {errs}")
    if not a.no_final:
        master()
        print("master", OUT)


if __name__ == "__main__":
    main()
