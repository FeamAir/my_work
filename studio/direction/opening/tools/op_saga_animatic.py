#!/usr/bin/env python3
"""Saga OP animatic v2 ($0, ffmpeg + PIL only, no API calls). Storyboard SAGA_OP v2.1: 57 shots + 9 frames of black,
87.0 s, 24 fps, 1920x1080, music output/music/lib_mus_theme-op-anthem_v1a.mp3 (investor's choice; v2a retired).

  python3 -I op_saga_animatic.py [--only A01a,C13] [--jobs 4] [--no-final]
  python3 -I op_saga_animatic.py --check FILE        # §12 rule 5: freezedetect + mpdecimate
  python3 -I op_saga_animatic.py --contact FILE      # cut sheet + hit sheet with the music onset envelope

PAID material is cut from the S1 OP v3 renders (output/opening/build_work/seg, accepted and keeper-signed) or from the
raw paid clips; C13 is the logo reveal on the final hit (LOGO.md, refs/LOGO); A01 is re-timed with minterpolate mci (no "on threes", §12). Every NEW item (W/KW/KA) is a card with
the shot text, land colour key and a moving drift so that rhythm and sync can be checked; it is labelled PENDING.
Output: output/opening/SAGA_OP_animatic_v2.mp4 (+ work files in output/opening/saga_animatic_work/).
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
OUT = f"{OUTD}/SAGA_OP_animatic_v2.mp4"
CONTACT = f"{OUTD}/contact_saga_v2"
W, H, FPS = an.W, an.H, an.FPS
FONT, FONTB = an.FONT, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
A = an.A

# ---------------------------------------------------------------------------------------- cut list v2.1 ---
CUTS = [("A01a", 0, 36), ("A01b", 36, 36), ("A02", 72, 36), ("A03", 108, 36), ("A04a", 144, 36), ("A04b", 180, 36),
        ("A05a", 216, 36), ("A05b", 252, 36), ("A06", 288, 36), ("A07", 324, 36), ("A08", 360, 36), ("A09", 396, 36),
        ("A10", 432, 36), ("A11", 468, 36)]
CUTS += [(f"B0{k}{x}", 504 + 72 * (k - 1) + (36 if x == "b" else 0), 36) for k in range(1, 9) for x in "ab"]
CUTS += [("B09", 1080, 36), ("B10", 1116, 36), ("B11", 1152, 36), ("B12a", 1188, 36), ("B12b", 1224, 36),
         ("B13", 1260, 36), ("B14", 1296, 36), ("B15", 1332, 28), ("B16", 1360, 9),
         ("C01a", 1369, 35), ("C01b", 1404, 36)]
CUTS += [(f"C0{k}", 1440 + 36 * (k - 2), 36) for k in range(2, 10)] + [("C10", 1728, 36)]
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
        (1081, "B09 brass SHAKE"), (1117, "B10 POP"), (1153, "B11 POP"), (1189, "B12a POP"), (1225, "B12b POP"),
        (1261, "B13 POP"), (1297, "B14 POP"), (1332, "B15 flash 1"), (1360, "B16 black"), (1369, "C01a INK"),
        (1441, "C02 POP"), (1477, "C03 POP"), (1513, "C04 POP"), (1549, "C05 POP"), (1585, "C06 POP"),
        (1621, "C07 POP"), (1657, "C08 INK"), (1765, "C11a step 1"), (1801, "C11b step 2"), (1837, "C11c step 3"),
        (1873, "C11d step 4"), (1945, "C12b POP"), (1981, "C13 last hit: logo lands"), (1990, "C13 wipe / drain"),
        (2040, "C13 drop leaves")]

# land colour keys (§4.2) for the cards
KEY = {"A": ((70, 92, 96), (150, 132, 104)), "B01": ((222, 220, 230), (150, 140, 170)), "B02": ((222, 220, 230), (150, 140, 170)),
       "B03": ((214, 176, 92), (120, 86, 48)), "B04": ((214, 176, 92), (120, 86, 48)),
       "B05": ((40, 70, 140), (190, 200, 210)), "B06": ((40, 70, 140), (190, 200, 210)),
       "B07": ((224, 150, 92), (210, 200, 186)), "B08": ((224, 150, 92), (210, 200, 186)),
       "B09": ((84, 120, 104), (214, 206, 186)), "B10": ((60, 80, 76), (150, 140, 120)), "B11": ((84, 120, 104), (214, 206, 186)),
       "B12": ((150, 56, 40), (30, 24, 24)), "B13": ((150, 56, 40), (30, 24, 24)), "B14": ((150, 56, 40), (30, 24, 24)),
       "C01": ((210, 170, 90), (60, 90, 110)), "C04": ((180, 170, 200), (150, 60, 50)),
       "C08": ((210, 170, 90), (80, 110, 100)), "C09": ((210, 170, 90), (80, 110, 100)), "C10": ((210, 170, 90), (80, 110, 100)),
       "C11": ((214, 200, 168), (120, 100, 80)), "C12": ((180, 110, 70), (40, 40, 70))}

# placeholder text per NEW cut: (source tag, short shot text)
NEW = {
    "B01a": ("W01 → KW01 0.5–2.0 s", "Pale Crag · Ilvane — dawn, the sun behind the cliff; the Pale Spire on the cliff summit, the cloister round its foot; violet-and-white pennants"),
    "B01b": ("W01 → KW01 3.0–4.5 s, crop 1.5×", "Pale Crag — cut-in on galleries and terraces, pennants stirring, mist; no Spire"),
    "B02a": ("W02 → KW02 1.0–2.5 s", "Pale Crag · the Choir — rows of hooded Cantors, backs to camera, facing the sea; sun behind camera; no Spire"),
    "B02b": ("W02 → KW02 3.0–4.5 s, crop 1.4×", "the Choir — hems and hood edges rippling in the wind (backs only)"),
    "B03a": ("W03 → KW03 0.5–2.0 s", "The Polders · Dask — noon gold; wind-pumps with ochre sails on the dike; the Sheaf Spire alone among the fields on a low rise"),
    "B03b": ("W03 → KW03 2.5–4.0 s, crop 1.6×", "Polders — cut-in on ochre pump sails turning the same way; grain waves; no Spire"),
    "B04a": ("W04 → KW04 1.0–2.5 s", "The Polders · the dike workers — wide-brimmed hats, spades, walking away along the crest; no tower"),
    "B04b": ("W04 → KW04 3.0–4.5 s, crop 1.4×", "dike workers — low cut-in: spades on shoulders, ochre pennants snapping"),
    "B05a": ("W05 → KW05 0.5–2.0 s", "Gullmouth · Corvane — morning, sun high behind the town; the Sentinel Spire on the crown of the headland; the mole, posts unlit"),
    "B05b": ("W05 → KW05 2.5–4.0 s, crop 1.5×", "Gullmouth — along the mole: many identical unlit posts, none singled out"),
    "B06a": ("W06 → KW06 0.5–2.0 s", "Gullmouth · the fleet — Corvane column under white sails, deep-blue pennants, past the mole's end; no tower"),
    "B06b": ("W06 → KW06 3.0–4.5 s", "the fleet — the nearest mainsail fills toward the lens → MATCH into the kite"),
    "B07a": ("W07 → KW07 1.0–2.5 s", "The Ossari uplands — ochre-pink terraced town, kites on roof poles, flyers in hoods (backs)"),
    "B07b": ("W07 → KW07 3.0–4.5 s, crop 1.5×", "Ossari — cut-in on plain kites tugging, tails whipping"),
    "B08a": ("W08 → KW08 0.5–2.0 s", "The Ossari · the sky — tilt up into the kites; gliders far off, flying away inland"),
    "B08b": ("W08 → KW08 2.5–4.0 s", "the sky — the tilt carries on; gliders moving away"),
    "B09": ("W09 → KW09 0.5–2.0 s  (UPGRADE)", "The Shoals · Quell — storm-dark; salt pans; Brackwater on its sandbars, the Storm Spire small in it"),
    "B10": ("W10 → KW10 0.5–2.0 s", "The Shoals · the beacons — squat timber beacon towers along the outer bar fading into rain; low dark boats in the reeds"),
    "B11": ("W09 → KW09 3.0–4.5 s, crop 1.6×  (UPGRADE)", "The Shoals · the salt — salt heaps, sea-green-and-bone pennants, light rain; no tower, boat or fire"),
    "B12a": ("W11 → KW11 0.5–2.0 s", "The Stair · Rusk — last sun; the falls; the Falls Spire on its spur, crown above the edge; nothing on the lip"),
    "B12b": ("W11 → KW11 2.5–4.0 s, crop 1.4×", "the Stair — the white column of the falls, mist at its foot; the lip bare"),
    "B13": ("W12 → KW12 0.5–2.0 s", "The Stair · the pikes — ranks from behind, black cloaks, plain helmets; sun ahead beyond the plain"),
    "B14": ("W12 → KW12 2.5–4.0 s, crop 1.5×", "the pikes — pike heads and pennants streaming"),
    "C01a": ("W13 → KW13 0.0–1.5 s  (UPGRADE)", "CONVERGENCE — the realm from the western sea; eight Spires at their v0.10 places (schematic)"),
    "C01b": ("W13 → KW13 1.5–3.0 s, crop 1.4×  (UPGRADE)", "cut-in toward Highwater: two Spires on the hill, the Sluice Spire at the SW foot"),
    "C04": ("W14 → KW14 0.5–2.0 s", "three pennants: Ilvane (violet/white), Rusk (rust/black), Quell (yellowish sea-green/bone)"),
    "C08": ("W15 → KW15 0.0–1.5 s", "ONE WATER — ordinary river traffic both ways, every house colour; no warships, no lights"),
    "C09": ("W15 → KW15 1.5–3.0 s, crop 1.5×", "hulls of at least three colours, bow waves"),
    "C10": ("W15 → KW15 3.0–4.5 s, crop 1.3×", "sails passing the reed islands"),
    "C11a": ("W16 → KW16 0.0–1.2 s @0.8×  (UPGRADE)", "MAP cut 1 — close on Highwater's hill"),
    "C11b": ("W16 → KW16 1.3–2.5 s @0.8×  (UPGRADE)", "MAP cut 2 — Gullmouth (north) and Pale Crag (south) in frame"),
    "C11c": ("W16 → KW16 2.6–3.8 s @0.8×  (UPGRADE)", "MAP cut 3 — the Polders and the Shoals"),
    "C11d": ("W16 → KW16 3.8–5.0 s @0.8×  (UPGRADE)", "MAP cut 4 — the whole delta, escarpment to islands"),
    "C12a": ("W13 → KW13 3.0–4.5 s, last light  (UPGRADE)", "MAP → LAND — the C01 view at last light"),
    "C12b": ("W13 → KW13 3.5–5.0 s, crop 1.3×  (UPGRADE)", "Highwater at last light; the 1:21.0 hit on the cut"),
}
FLASHES = ["B02a", "B04a", "B06a", "B08a", "B11", "B13"]   # B15: KW02, KW04, KW06, KW08, KW09 crop, KW12 (+ K05)


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


def card(cut):
    p = f"{WK}/card_{cut}.png"
    c0, c1 = key(cut)
    yy = np.linspace(0, 1, H)[:, None, None]
    img = (np.array(c0) * (1 - yy) + np.array(c1) * yy).repeat(W, 1)
    im = Image.fromarray(img.astype(np.uint8))
    d = ImageDraw.Draw(im)
    if cut.startswith(("C01", "C11", "C12")):
        schematic(d, (360, 330, 1560, 1000))
    if cut == "C04":
        for i, (a, b) in enumerate([((178, 160, 210), (240, 240, 236)), ((160, 60, 40), (20, 18, 18)), ((150, 178, 120), (230, 222, 200))]):
            x = 420 + i * 420
            d.polygon([(x, 340), (x + 300, 380), (x + 300, 560), (x, 600)], fill=a)
            d.polygon([(x, 600), (x + 300, 560), (x + 300, 700), (x, 860)], fill=b)
    tag, txt = NEW[cut]
    d.rectangle((60, 60, W - 60, 300), fill=(0, 0, 0))
    d.text((90, 80), f"{cut}  ·  PENDING  ·  NEW {tag}", fill=(250, 220, 120), font=ImageFont.truetype(FONTB, 44))
    for i, ln in enumerate(textwrap.wrap(txt, 78)[:3]):
        d.text((90, 150 + 44 * i), ln, fill=(236, 236, 236), font=ImageFont.truetype(FONT, 34))
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


def piece(g, path, ss, src_t, speed=1.0, z=1.0, fx=0.5, fy=0.5, mci=False, every=1):
    """a piece of a clip: ss..ss+src_t played at `speed`, interpolated with mci when < 0.8x (§12), cover-cropped.
    No tpad: the source window must hold enough frames (§12 rule 3)."""
    i = g.clip(path, ss, src_t + 0.05)
    o = g.lab()
    tim = f"setpts=(PTS-STARTPTS)/{speed}"
    interp = (f",minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" if mci else f",fps={FPS}")
    g.add(f"[{i}]{tim}{interp},scale={int(W * z + 0.5) // 2 * 2 + 4}:{int(H * z + 0.5) // 2 * 2 + 4}:"
          f"force_original_aspect_ratio=increase,crop={W}:{H}:x='(iw-ow)*{fx}':y='(ih-oh)*{fy}',setsar=1[{o}]")
    return o


def card_motion(g, path, z0=1.0, z1=1.07, fx=0.5, fy=0.5):
    """placeholder card: linear push (never eased to a stop) + drifting clouds, so no frame repeats."""
    s = an.zp(g, g.still(path), z0, z1, fx, fx, fy, fy, curve="lin")
    return an.clouds(g, s, 900)


def run(g, s, out):
    o = g.lab()
    g.add(f"[{s}]format=yuv420p,setsar=1[{o}]")
    return an.run_cut(g, o, out)


def from_seg(cut, s1, first=0, z=1.0, fx=0.5, fy=0.5, speed=1.0, label=""):
    """frames of an S1 OP v3 render (24 fps, 1920x1080)."""
    g = an.G(cut)
    i = g.clip(f"{S1SEG}/{s1}.mp4", first / FPS, g.n / FPS * speed + 0.1)
    o = g.lab()
    blend = ",tmix=frames=2" if speed >= 2 else ""
    g.add(f"[{i}]setpts=(PTS-STARTPTS)/{speed},fps={FPS}{blend},scale={int(W * z) // 2 * 2}:-2,"
          f"crop={W}:{H}:x='(iw-ow)*{fx}':y='(ih-oh)*{fy}',setsar=1[{o}]")
    return run(g, tag(g, o, label), f"{an.SEG}/{cut}.mp4")


# ------------------------------------------------------------------------------------------------ build ---
def build(cut):
    out = f"{an.SEG}/{cut}.mp4"
    g = an.G(cut)
    L = lambda f: L_(cut, f)
    if cut == "A01a":
        s = piece(g, f"{CL}/K01a.mp4", 0.0, 0.62, speed=0.4, mci=True)
        s = an.rain(g, an.mist(g, an.spray_burst(g, s, 0.3, 0.3, 0.2), 0.15), darken=False)
        return run(g, tag(g, s, "A01a PAID K01a 0.0-0.6 s @0.4x mci (was on threes)"), out)
    if cut == "A01b":
        s = piece(g, f"{CL}/K01a.mp4", 0.5, 0.52, speed=0.333, z=1.4, fx=0.3, fy=0.4, mci=True)
        s = an.rain(g, an.spray_burst(g, s, 0.3, 0.3, 0.2), darken=False)
        return run(g, tag(g, s, "A01b PAID K01a 0.5-1.0 s @0.33x mci, crop 1.4x"), out)
    if cut == "A02":
        return from_seg(cut, "02", label="A02 PAID plate D01_A, LA stand-in -> NEW KA02 PENDING (upgrade)")
    if cut == "A03":
        return from_seg(cut, "02b", label="A03 PAID K03 0.0-1.5 s")
    if cut in ("A04a", "A04b"):
        # the video-test alley clip with the v1.4 static patches (plain brick over the double gate, plain planks over
        # the ring knocker), a LINEAR push (an eased push stalls at its ends: §12 check), mist drifting
        b = cut == "A04b"
        c = g.clip(an.ALLEY, 2.0 if b else 0.5, 1.6)
        o, pa, pb = g.lab(), g.lab(), g.lab()
        z0, z1 = (1.30, 1.36) if b else (1.0, 1.06)
        g.add(f"[{c}]setpts=PTS-STARTPTS,split=3[{o}a][{o}b][{o}c];[{o}b]trim=end_frame=1,loop=loop=-1:size=1,crop=140:130:775:495[{pa}];"
              f"[{o}c]trim=end_frame=1,loop=loop=-1:size=1,crop=44:80:60:568[{pb}];"
              f"[{o}a][{pa}]overlay=915:495:shortest=1[{o}d];[{o}d][{pb}]overlay=122:568:shortest=1,fps={FPS},"
              f"scale=w='2*trunc(1950*({z0}+{z1 - z0:.3f}*t/1.5)/2)':h=-2:eval=frame,crop={W}:{H}:x='(iw-ow)/2':y='(ih-oh)*0.6',setsar=1[{o}]")
        s = an.overlay_field(g, o, A["fog"], "screen", 0.2, f"crop={W}:{H}:x='(iw-ow)*t/6':y=0")
        return run(g, tag(g, s, f"{cut} PAID alley clip {'2.0-3.5 s crop 1.3x' if b else '0.5-2.0 s'} (gate + knocker patched)"), out)
    if cut == "A05a":
        s = piece(g, f"{CL}/K07_fix.mp4", 0.5, 1.5)
        return run(g, tag(g, an.mist(g, s, 0.12), "A05a PAID K07_fix 0.5-2.0 s"), out)
    if cut == "A05b":
        s = piece(g, f"{CL}/K07_fix.mp4", 2.0, 1.875, speed=1.25)
        return run(g, tag(g, an.mist(g, s, 0.12), "A05b PAID K07_fix 2.0-3.875 s @1.25x"), out)
    if cut == "A06":
        return from_seg(cut, "05", label="A06 PAID wheel plate, LA ROT stand-in -> NEW KA06 PENDING (upgrade)")
    if cut == "A07":
        return from_seg(cut, "06", label="A07 PAID K04 0.5-2.0 s")
    if cut == "A08":
        return from_seg(cut, "07", label="A08 PAID K05 0.0-1.5 s")
    if cut == "A09":
        return from_seg(cut, "13", label="A09 PAID hall plate, LA stand-in -> NEW KA09 PENDING (upgrade)")
    if cut == "A10":
        return from_seg(cut, "14", speed=2.0, label="A10 PAID K10 0.5-3.5 s @2x")
    if cut == "A11":
        s = an.zp(g, g.still(A["F17"]), 1.08, 1.16, 0.0, 1.0, 0.5, 0.5, curve="in")
        s = an.clouds(g, s, 400)
        o = g.lab()
        pk = L(491)
        g.add(f"[{s}]gblur=sigma=10:sigmaV=0.01:enable='between(n,{pk - 6},{pk - 3})',"
              f"gblur=sigma=40:sigmaV=0.01:enable='between(n,{pk - 2},{g.n})'[{o}]")
        s = an.pop(g, o, [pk])
        return run(g, tag(g, s, "A11 PAID F17, LA stand-in -> NEW KA11 PENDING (upgrade); WHIP right, POP 491"), out)
    if cut == "B15":
        k05 = f"{WK}/k05_f12.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{CL}/K05.mp4", "-vf", "select=eq(n\\,12)", "-frames:v", "1", k05], check=True)
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
    if cut in ("C02", "C03", "C05", "C06"):
        s1 = {"C02": "19", "C03": "20", "C05": "21", "C06": "22"}[cut]
        return from_seg(cut, s1, label=f"{cut} PAID {'K11' if cut < 'C04' else 'K12'} (S1 v3 render)")
    if cut == "C07":
        s = an.zp(g, g.still(A["F17"]), 2.2, 2.29, 0.436, 0.436, 0.37, 0.37, curve="lin")
        o = g.lab()
        g.add(f"[{s}]noise=alls=8:allf=t[{o}]")
        s = an.pop(g, o, [L(1621)])
        return run(g, tag(g, s, "C07 PAID F17 crop 2.2x, stand-in -> KA11 piece PENDING (upgrade); POP 1621"), out)
    if cut == "C13":
        return build_title()
    # ---- NEW: cards
    p = f"{WK}/card_{cut}.png"
    crop = {"B01b": 1.5, "B02b": 1.4, "B03b": 1.6, "B04b": 1.4, "B05b": 1.5, "B07b": 1.5, "B11": 1.6, "B12b": 1.4,
            "B14": 1.5, "C01b": 1.4, "C09": 1.5, "C10": 1.3, "C12b": 1.3}.get(cut, 1.0)
    if cut.startswith("C11"):
        crop = {"a": 2.4, "b": 1.8, "c": 1.35, "d": 1.0}[cut[-1]]
        s = card_motion(g, p, crop * 1.04, crop, 0.21, 0.52)          # camera pulling back inside the cut
    else:
        s = card_motion(g, p, crop, crop * 1.07, 0.5, 0.0 if crop > 1 else 0.5)
    if cut.startswith("C12"):
        o = g.lab()
        g.add(f"[{s}]colorbalance=rs=0.08:bs=-0.06:rm=0.05,eq=brightness='-0.10*t/1.5':eval=frame[{o}]")
        s = o
    pops = [h for h, _ in HITS if an.START[cut] <= h < an.START[cut] + g.n and "INK" not in _ and "SHAKE" not in _
            and "flash" not in _ and "black" not in _]
    s = an.pop(g, s, [L(h) for h in pops])
    if cut == "B09":
        s = an.shake(g, s, [(L(1081), 6, 9)])
    if cut.startswith("C11") or cut in ("C09", "C10", "B14"):
        s = an.shake(g, s, [(1, 6, 9)])
    if cut == "C01a":
        s = an.shake(g, an.ink(g, s, 0), [(0, 12, 3)])
    if cut == "C08":
        s = an.ink(g, s, 0)
    return run(g, s, out)


def build_title():
    """C13, the logo reveal on the final hit (LOGO.md §4 shifted so the logo lands on 1981 instead of 1995):
    C12b continues under INK 1981-1982 and the torn spray wipe 1981-1992; K17 0.0-4.5 s (crown framing, push 3 %,
    variant B) comes in under it; the Tidemark logotype (1300 px, centre y 660) lands 1981-1988 wet (114 % -> 100 %),
    SHAKE 1981-1986, water drains 1989-2013, glint 1996-2020, logo +1.5 % parallax, a drop leaves on 2040."""
    cut = "C13"
    g = an.G(cut)
    out = f"{an.SEG}/{cut}.mp4"
    L = lambda f: L_(cut, f)
    hit = L(1981)
    dusk = f"{WK}/card_C12b_dusk.png"
    im = Image.open(f"{WK}/card_C12b.png").convert("RGB")
    Image.blend(im, Image.new("RGB", im.size, (40, 36, 60)), 0.35).save(dusk)
    a = an.zp(g, g.still(dusk), 1.3 * 1.07, 1.3 * 1.09, 0.5, 0.5, 0.0, 0.0, curve="lin")
    a = an.ink(g, a, hit)
    a = an.spray_burst(g, a, 0.5, 0.9, 0.6, t0=hit / FPS, dur=13 / FPS)
    b = piece(g, f"{CL}/K17.mp4", 0.0, 4.5, z=1.5, fx=0.42, fy=0.0)
    b = an.vpush(g, b, 1.0, 1.03, 0.5, 0.3)
    o = g.lab()
    g.add(f"[{b}]colorbalance=rs=-0.04:bs=0.06:rm=-0.03:bm=0.04[{o}]")
    w = g.lab()
    g.add(f"[{a}]settb=AVTB,fps={FPS}[{w}a];[{o}]settb=AVTB,fps={FPS}[{w}b];[{w}a][{w}b]xfade=transition=custom:"
          f"duration=0.5:offset={hit / FPS:.5f}:expr='if(gt(Y/H+0.06*sin(X/W*23)+0.03*sin(X/W*71),P*1.12),B,A)'[{w}]")
    LW, TIDE, s0 = 1300, 243, hit          # logo frames counted from the hit
    li = g.still(LOGO)
    lg = g.lab()
    g.add(f"[{li}]scale={LW}:-1,format=rgba,split=3[{lg}d][{lg}w0][{lg}g0];"
          f"[{lg}w0]eq=brightness=-0.16:saturation=0.75,colorbalance=bs=0.08:bm=0.05,"
          f"geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='alpha(X,Y)*clip((Y-{TIDE}*clip((N-{s0 + 8})/24,0,1))/10+1,0,1)*(1-gte(Y,{TIDE})*clip((N-{s0 + 32})/13,0,1))'[{lg}w];"
          f"[{lg}g0]geq=r=235:g=242:b=250:a='alpha(X,Y)*lt(Y,{TIDE})*0.32*exp(-pow((X-0.35*Y-(-300+(W+600)*clip((N-{s0 + 15})/24,0,1)))/34,2))'[{lg}g];"
          f"[{lg}d][{lg}w]overlay=0:0:format=auto[{lg}1];[{lg}1][{lg}g]overlay=0:0:format=auto,"
          f"scale=w='2*trunc(iw*if(lt(n,{s0 + 8}),1.14-0.14*clip((n-{s0})/8,0,1),1)*(1+0.015*n/108)/2)':h=-2:eval=frame[{lg}]")
    o = g.lab()
    g.add(f"[{w}][{lg}]overlay=x='(W-w)/2+if(between(n,{s0},{s0 + 5}),6*sin(n*2.6),0)':"
          f"y='660-h/2+if(between(n,{s0},{s0 + 5}),4*cos(n*3.1),0)':eval=frame:format=auto:enable='gte(n,{s0})'[{o}]")
    s = o
    # the drop: gathers under a letter below the tide line from 2016, leaves on 2040, falls out of frame
    di, d_ = g.still(A["drop"]), g.lab()
    t_g0, t_go = L(2016) / FPS, L(2040) / FPS
    g.add(f"[{di}]format=rgba,scale=w='2*trunc(max(4,34*min(1,max(0,(t-{t_g0:.3f})/{t_go - t_g0:.3f})))/2)':h=-2:eval=frame[{d_}m];"
          f"[{s}][{d_}m]overlay=x={int(W / 2 + LW * 0.17)}-w/2:y='{660 + 488 // 2 - 40}+if(gt(t,{t_go:.3f}),1500*pow(t-{t_go:.3f},2),0)':"
          f"eval=frame:enable='gte(t,{t_g0:.3f})':shortest=1[{d_}]")
    o2 = g.lab()
    g.add(f"[{d_}]trim=end_frame={g.n},format=yuv420p,setsar=1[{o2}]")
    s = tag(g, o2, "C13 LOGO REVEAL on the final hit 1981: INK + spray wipe, Tidemark logotype lands wet, drains, glint; PAID K17")
    return run(g, s, out)


# ===MASTER===
def master():
    lst = f"{WK}/concat.txt"
    with open(lst, "w") as f:
        for c, _, _ in CUTS:
            f.write(f"file '{an.SEG}/{c}.mp4'\n")
    bug = f"{WK}/bug.txt"
    open(bug, "w").write("ANIME-STYLE · AI-ANIMATED  ·  SAGA OP ANIMATIC v2 (storyboard v2.1, music anthem v1a)")
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
    p1 = f"{CONTACT}/SAGA_OP_v2_cuts.png"
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
    p2 = f"{CONTACT}/SAGA_OP_v2_hits.png"
    im.save(p2)
    json.dump(res, open(f"{CONTACT}/hit_onsets.json", "w"), indent=0)
    print(p1, p2)
    for r_ in res:
        print(r_)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--no-final", action="store_true")
    ap.add_argument("--check", default="")
    ap.add_argument("--contact", default="")
    a = ap.parse_args()
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
