#!/usr/bin/env python3
"""S01E01 animatic v2: the two restaged shots (v1 frames refused by the fal content checker; child character).

The beat is carried by implication (an adult, an object, sound / off-screen voice). The child is not in either frame.
This is a staging change written into the shot list for the lead writer's approval — not a reworded v1 prompt.

  python3 -I restage_v2.py plan
  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=55 python3 -I restage_v2.py run sc02-sh050 [take]   # NB2 /edit, $0.08 a take
  python3 -I restage_v2.py accept sc02-sh050 <take>   # copy take -> frames/<id>_a.png (v1 placeholder kept in frames_rejected/)

Limit (studio director, 2026-11-24): at most 3 takes per shot, nothing else paid.
"""
import json
import os
import shutil
import sys

ROOT = "/home/user/my_work"
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from frames import AVOID, ID, LIGHT, STYLE, _ONE  # noqa: E402

A = f"{ROOT}/output/S01E01/animatic"
FR, REJ, REFS = f"{A}/frames", f"{A}/frames_rejected", f"{ROOT}/studio/direction/refs"
MAXT = 3

JOBS = {
    "sc02-sh050": dict(
        refs=[f"{REFS}/B-06/B06_sheet_v1.png", f"{REFS}/M-BOX/E08_sheet_v1.png", f"{REFS}/PL-0008/D02_C2_dawn-ebb_v1.png"],
        legend=["Image 1 is the character reference sheet for " + ID["COLLECTOR"] + " — copy face, outfit and the box on "
                "the left wrist exactly.",
                "Image 2 is the reference for the small chained box — match design and scale.",
                "Image 3 is the location plate — keep its architecture, palette and light, re-staged for this camera angle."],
        shot=("Dawn, medium-wide shot looking slightly up at the door of a stilt-house on the plank-walk. Above the "
              "doorway a narrow rope-and-plank footbridge spans between two houses; its ropes are pulled taut and the "
              "planks bow down in the middle under a weight just above the top edge of the frame, out of sight. A little "
              "grit and two or three drops fall from the planks. Below, on the RIGHT side of the picture, the "
              "TITHE-COLLECTOR stands on the plank-walk reading his slate, not looking up, mouth closed, the chained box "
              "hanging from his wrist. Drying nets on the rail at the left edge. Nobody else in the frame: no other "
              "people, no faces, no hands or feet hanging from the bridge. " + LIGHT["LOWS_DAWN"] + ". "),
    ),
    "sc04-sh180": dict(
        refs=[f"{REFS}/CH-0015/A03_00_master_v1.png", f"{REFS}/PL-0019/D06_N1_morning_v1.png"],
        legend=["Image 1 is the character reference sheet for " + ID["NAN"] + " — use it only for her hand, skin tone and "
                "faded blue-grey sleeve; her face is not in this shot.",
                "Image 2 is the location plate — keep its architecture, palette and light, re-staged for this camera angle."],
        shot=("Morning, close insert on the end of a rough wooden table in a stilt-house room, soft grey light from an "
              "oiled-cloth window. An old woman's small wrinkled deep-brown hand with a crooked little finger, in a faded "
              "blue-grey sleeve, enters from the RIGHT edge of the picture and lies flat on the boards where she has just "
              "put it down, fingers spread hard against the wood to keep them still. Beside it a wooden net-needle with "
              "a tail of twine. At the far side of the board a bitten crust of grey bread lies where it was dropped. "
              "Only this one hand is in the frame: no faces, no other people, no other hands. "),
    ),
}


def prompt(sid):
    j = JOBS[sid]
    return ("Create ONE new single frame of a 2D anime TV episode (a finished background with characters, not a model "
            "sheet, no grid, no panels, no captions). " + " ".join(j["legend"]) + " Shot: " + j["shot"] + _ONE +
            "Characters are lit by the same light as the scene, colours no brighter than the surroundings, clean "
            "consistent anatomy. " + STYLE + ". " + AVOID)


def take_path(sid, t):
    return f"{FR}/{sid}_a_v2t{t}.png"


def run(sid, t=None):
    from pipeline import fal_client
    done = [i for i in range(1, MAXT + 1) if os.path.exists(take_path(sid, i))]
    t = int(t) if t else (max(done) + 1 if done else 1)
    if t > MAXT:
        sys.exit(f"{sid}: {MAXT} takes used — change the approach, not the seed")
    p = prompt(sid)
    seed = 7000 + t * 131 + (50 if sid.startswith("sc04") else 0)
    out = take_path(sid, t)
    r = fal_client.generate_image(p, out, model="nano-banana-2-edit", reference_images=JOBS[sid]["refs"],
                                  aspect_ratio="16:9", extra={"seed": seed})
    meta_p = f"{FR}/meta.json"
    meta = json.load(open(meta_p))
    meta[f"{sid}_a_v2t{t}"] = dict(prompt=p, refs=[os.path.relpath(x, ROOT) for x in JOBS[sid]["refs"]], seed=seed,
                                   model="nano-banana-2-edit", attempt=t, note="v2 restaging (content-checker refusal in v1)")
    json.dump(meta, open(meta_p, "w"), indent=1, ensure_ascii=False)
    print(sid, t, r)


def accept(sid, t):
    os.makedirs(REJ, exist_ok=True)
    dst = f"{FR}/{sid}_a.png"
    ph = f"{REJ}/{sid}_a_v1placeholder.png"
    if os.path.exists(dst) and not os.path.exists(ph):
        shutil.move(dst, ph)
    shutil.copy(take_path(sid, int(t)), dst)
    print("accepted", sid, "take", t)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "plan":
        for k in JOBS:
            print("---", k, "\n", prompt(k), "\n est $0.08 a take, max", MAXT)
    elif cmd == "run":
        run(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    elif cmd == "accept":
        accept(sys.argv[2], sys.argv[3])
