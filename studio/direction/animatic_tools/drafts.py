#!/usr/bin/env python3
"""S01E01 animatic, step 4b: one MiniMax H3 Max Turbo 768P draft clip per class-D shot (+ a few hero C shots),
only to verify the motion is achievable before the final stage. Not used where LA clearly suffices.

  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=70 python3 -I drafts.py run
Output: output/S01E01/animatic/drafts/<id>_mm.mp4 (+ drafts/meta.json). la.py uses the clip if present.
"""
import concurrent.futures as cf
import json
import os
import sys

ROOT = "/home/user/my_work"
sys.path.insert(0, ROOT)
A = f"{ROOT}/output/S01E01/animatic"
DR = f"{A}/drafts"
MOTION_BASE = ("subtle 2D anime animation, the character design, colors and line art stay exactly as in the source image, "
               "stable outlines, no morphing, one simple natural motion, consistent lighting, camera as described. ")
KEEP = ("Must NOT change: lighting, no new light sources, no glowing marks or glowing objects, costume, faces, "
        "number of people, which side details are on; nobody turns around unless stated.")
# class D (all unique) + hero C shots where the motion itself is the open question
EXTRA_C = []  # resume 2026-11-24: brief limits drafts to class D where LA will not do; C shots use start/end poses
# class D where LA start->end dissolve already reads (static push / transformation dissolve): no draft
LA_OK = {"sc01-sh050": "hands push the bar: a/b pose dissolve reads", "sc18-sh060": "same set-up as sc01-sh050",
         "sc09-sh060": "harbour waves -> glass: a/b dissolve is the effect"}


def targets():
    ss = json.load(open(f"{A}/spec/shots.json"))["shots"]
    out = []
    for s in ss:
        if s["clipreuse"]:
            continue
        if (s["cls"] == "D" or s["id"] in EXTRA_C) and s["id"] not in LA_OK:
            src = s["reuse"] or s["id"]
            dur = 10 if s["dur"] >= 8 else 6 if s["dur"] > 5 else 5
            out.append((s["id"], f"{A}/frames/{src}_a.png", s["mot"] or s["act"], dur))
    return out


def run():
    from pipeline import fal_client
    os.makedirs(DR, exist_ok=True)
    try:
        meta = json.load(open(f"{DR}/meta.json"))
    except Exception:
        meta = {}
    js = [t for t in targets() if not os.path.exists(f"{DR}/{t[0]}_mm.mp4")]
    print("clips", len(js), "est $", round(sum(t[3] for t in js) * 0.04, 2), flush=True)

    def go(t):
        sid, img, mot, dur = t
        p = MOTION_BASE + mot + " " + KEEP
        try:
            fal_client.image_to_video(img, p, f"{DR}/{sid}_mm.mp4", model="minimax-h3-max-turbo", duration=dur)
            return sid, "ok", p, dur, img
        except Exception as e:
            return sid, f"ERR {type(e).__name__}: {str(e)[:200]}", p, dur, img
    with cf.ThreadPoolExecutor(5) as ex:
        for sid, r, p, dur, img in ex.map(go, js):
            print(sid, r, flush=True)
            if r == "ok":
                meta[sid] = dict(prompt=p, duration=dur, image=os.path.relpath(img, ROOT), model="minimax-h3-max-turbo")
                json.dump(meta, open(f"{DR}/meta.json", "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    if sys.argv[1] == "list":
        for t in targets():
            print(t[0], t[3], os.path.exists(t[1]))
    else:
        run()
