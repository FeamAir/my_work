#!/usr/bin/env python3
"""S01E01 animatic v3: Wick frames that read grey-haired (analyst, v2 20:16 / 21:08).

  sc20-sh180 -> $0: re-uses sc20-sh050_a.png (Wick at the table, lamp-lit, hair reads brown) — set in cut_v3.py.
  sc20-sh010 -> no existing night frame has Pell on the chest AND Wick: one NB2 /edit of the v2 frame with the
                Wick master + turnaround as refs; only his hair / tuft change (and the glowing wall lines go, QA V10).

  python3 -I regen_v3.py plan
  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=55 python3 -I regen_v3.py run sc20-sh010 [take]   # $0.08 a take, max 2
  python3 -I regen_v3.py grade sc20-sh010 1        # $0 hair-colour pull on take 1 -> take "1g"
  python3 -I regen_v3.py accept sc20-sh010 <take>   # v2 frame kept in frames_rejected/<id>_a_v2grey.png
"""
import json
import os
import shutil
import sys

ROOT = "/home/user/my_work"
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from frames import AVOID, STYLE, _ONE  # noqa: E402

A = f"{ROOT}/output/S01E01/animatic"
FR, REJ, REFS = f"{A}/frames", f"{A}/frames_rejected", f"{ROOT}/studio/direction/refs"
MAXT = 2

JOBS = {
    "sc20-sh010": dict(
        refs=[f"{FR}/sc20-sh010_a.png", f"{REFS}/CH-0007/A02_00_master_v1.png", f"{REFS}/CH-0007/A02_01_turnaround_v1.png"],
        prompt=("Edit image 1, a frame of a 2D anime TV episode. Keep everything in image 1 exactly as it is: the "
                "composition, the camera, the room, the girl sitting on the chest (her face, red-brown hair, braid, "
                "clothes and pose unchanged), the table, the bowl, the oil lamp and the night light. Change only the "
                "boy standing by the table: he is WICK from images 2 and 3 (character master and turnaround). Give him "
                "the hair exactly as in images 2 and 3: a warm medium-brown messy mop, clearly brown and not grey, not "
                "ash, not silver, not white, with ONE single tuft sticking straight up at his right temple (on the "
                "left side of the picture as he faces us). Keep his face, oatmeal knitted jumper, brown trousers, bare "
                "feet and pose as in image 1. The lamp light falls warm on his hair. Also remove the thin glowing cyan "
                "zig-zag lines on the walls and the floor: plain dark wood, no glowing lines. " + _ONE + STYLE + ". "
                + AVOID)),
}


def take_path(sid, t):
    return f"{FR}/{sid}_a_v3t{t}.png"


def run(sid, t=None):
    from pipeline import fal_client
    done = [i for i in range(1, MAXT + 1) if os.path.exists(take_path(sid, i))]
    t = int(t) if t else (max(done) + 1 if done else 1)
    if t > MAXT:
        sys.exit(f"{sid}: {MAXT} takes used")
    j = JOBS[sid]
    seed = 9100 + t * 137
    r = fal_client.generate_image(j["prompt"], take_path(sid, t), model="nano-banana-2-edit",
                                  reference_images=j["refs"], aspect_ratio="16:9", extra={"seed": seed})
    meta_p = f"{FR}/meta.json"
    meta = json.load(open(meta_p))
    meta[f"{sid}_a_v3t{t}"] = dict(prompt=j["prompt"], refs=[os.path.relpath(x, ROOT) for x in j["refs"]], seed=seed,
                                   model="nano-banana-2-edit", attempt=t, note="v3: Wick hair read grey (analyst)")
    json.dump(meta, open(meta_p, "w"), indent=1, ensure_ascii=False)
    print(sid, t, r)


def grade(sid="sc20-sh010", t=1):
    """$0 local fix of take 1: NB2 gave Wick ginger-orange hair with a lamp halo; pull the hair (box above the eyes
    only, orange hue, saturated) to mouse-brown: saturation and value x0.62; halo pixels desaturated. -> *_v3t1g.png"""
    import numpy as np
    from PIL import Image
    im = Image.open(take_path(sid, t)).convert("RGB")
    hsv = np.array(im.convert("HSV")).astype(float)
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    yy, xx = np.mgrid[0:hsv.shape[0], 0:hsv.shape[1]]
    hair = (xx >= 630) & (xx < 860) & (yy >= 60) & (yy < 203) & (h > 8) & (h < 35) & (s > 90) & (v > 60)
    halo = (xx >= 620) & (xx < 880) & (yy >= 40) & (yy < 200) & (h > 5) & (h < 40) & (s > 40) & ~hair
    s[hair] *= 0.62
    v[hair] *= 0.62
    s[halo] *= 0.6
    v[halo] *= 0.85
    out = take_path(sid, f"{t}g")
    Image.fromarray(np.stack([h, s, v], -1).clip(0, 255).astype(np.uint8), "HSV").convert("RGB").save(out)
    print(out)


def accept(sid, t):
    os.makedirs(REJ, exist_ok=True)
    dst, old = f"{FR}/{sid}_a.png", f"{REJ}/{sid}_a_v2grey.png"
    if os.path.exists(dst) and not os.path.exists(old):
        shutil.copy(dst, old)
    shutil.copy(take_path(sid, t), dst)
    print("accepted", sid, "take", t)


if __name__ == "__main__":
    c = sys.argv[1]
    if c == "plan":
        for k, j in JOBS.items():
            print(k, j["prompt"], "\nrefs", j["refs"])
    elif c == "run":
        run(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    elif c == "grade":
        grade(sys.argv[2], int(sys.argv[3]))
    elif c == "accept":
        accept(sys.argv[2], sys.argv[3])
