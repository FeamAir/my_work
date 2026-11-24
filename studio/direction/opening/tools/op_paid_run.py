#!/usr/bin/env python3
"""S1 OP paid run (storyboard v1.4 §5, §6). PAID: only with the studio director's permission.

  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=64 python3 op_paid_run.py frames F01 F04 ...   [--take 2]
  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=64 python3 op_paid_run.py clips  K01 K03 ...   [--take 2]
  python3 op_paid_run.py show F21 | K12          # print the exact prompt that would be sent ($0)

NB2: fal-ai/nano-banana-2/edit through pipeline.fal_client.generate_image with exactly the parameters of the
earlier 164 calls: aspect_ratio "16:9", num_images 1, output_format "png", image_urls, a fixed seed per frame,
no `resolution` key (1K default, 1376x768, $0.08). Kling 2.5 TP: 5 s, image_url + prompt + negative_prompt.
Every call goes through costs.guard (STUDIO_ALLOW_PAID, BUDGET_LIMIT_USD, the $20 fal floor) and costs.log.
K13 is refused here until the studio director gives the go (C2): pass --k13-go only then.
Outputs: output/opening/frames/<id>[_tN].png, output/opening/clips/<id>[_tN].mp4, each with a .json of the full
prompt, refs, seed and timing. Takes are never overwritten.
"""
import argparse
import json
import os
import sys
import time

ROOT = "/home/user/my_work"
sys.path.insert(0, ROOT)
os.chdir(ROOT)
from pipeline import costs, fal_client  # noqa: E402

REF = "studio/direction/refs"
ANI = "output/S01E01/animatic/frames"
FR = "output/opening/frames"
CL = "output/opening/clips"
PL = "output/opening/plates"

STYLE_BASE = ("2D anime-style TV series still, original character and world design, clean cel-shaded characters with crisp thin "
              "dark blue-black ink outlines of slightly varying weight, flat color fills with two shadow tones, cool violet-blue "
              "shadows, restrained highlights only on eyes, hair, metal and wet surfaces, detailed painterly matte-painting "
              "background with atmospheric haze, wet reflective stone and water, motivated cinematic lighting, muted desaturated "
              "palette with deep teal-black shadows, subtle film grain, grounded epic fantasy, 16:9 widescreen composition")
CHRONICLE = ("a flat woven tapestry panel, visible textile weave and thread texture, faded indigo, madder red, ochre and undyed "
             "linen, stylized flat figures in profile, no perspective, decorative border")
AVOID_OP = ("One single full-frame image: no inset, no letterbox bars, no frames or boxes drawn on top. No people and no faces "
            "(unless tiny distant silhouettes are allowed below). Avoid: photorealism, 3D look, chibi style, neon colors, any "
            "text, letters, numbers or labels, watermark, logo, multiple panels, split screen, glowing objects, glowing lines or "
            "cracks, light inside tower grooves, magic sparkles, lightning, mirrored image, shields, gates or bars across gates, "
            "stones or pebbles on cords, finger rings, rings on water.")
AVOID_OP_F18 = ("One single full-frame image: no inset, no letterbox bars, no frames or boxes drawn on top. Avoid: photorealism, "
                "3D look, anime character, cel shading, neon colors, any text, letters, numbers or labels, watermark, logo, "
                "multiple panels, split screen, glowing objects, magic sparkles, mirrored image, shields, weapons, spears, swords, "
                "blood, faces in close-up, open mouths, stones or pebbles on cords.")
SPIRE = ("the towers are smooth glassy black stone cones, each crowned by a ring of open arches, with deep spiral grooves winding "
         "up the whole height; on the near side of each tower the grooves rise from lower-left to upper-right ( / ); the grooves "
         "are dark, nothing lights up; the foot of each tower is dark unlit stone")

F19_TEXT = ("Two tall silk banners side by side, each filling one half of the frame, hanging from poles on a granite terrace and "
            "snapping in a strong wind; each banner is vertical with a slanted cut at the bottom and the long point at the pole "
            "side. Left banner: deep blue field, a black cormorant with half-folded wings diving beak-down into a silver wave with "
            "exactly three crests, no fish. Right banner: ochre field, a bronze sickle with its blade up, set above three parallel "
            "dark-brown furrows; it reads as a tool with a short handle, not as a crescent moon. Emblems exactly as in the "
            "references. The two banners fill the frame edge to edge, each emblem centred at mid-height of its banner. Low golden "
            "afternoon sun from the left, pale open sky behind, crisp shadows in the folds.")
F19_LR = ("Left banner: deep blue field, a black cormorant with half-folded wings diving beak-down into a silver wave with exactly "
          "three crests, no fish. Right banner: ochre field, a bronze sickle with its blade up, set above three parallel dark-brown "
          "furrows; it reads as a tool with a short handle, not as a crescent moon.")
F21_LR = ("Left banner: black field, a polished copper beam balance with a level beam, the left pan holding a level surface of "
          "blue-grey water, the right pan empty. Right banner: acid sulphur-yellow field (not gold), a grey hare seated in profile "
          "facing left, both ears straight up and slightly apart, one eye visible.")
assert F19_TEXT.count(F19_LR) == 1

# id: (seed, refs, text, style)    style "base" = text + STYLE_BASE + AVOID_OP; "chron" = text + CHRONICLE + AVOID_OP_F18
FRAMES = {
    "F01": (26110, [f"{REF}/PL-0004/D01_A_dawn-ebb_v1.png"],
            "Wide low shot from the sea side of a colossal brick sea dike under a grey storm sky in daylight: a huge dark green-grey wave is just striking the dike's sloping outer face, a wall of white spray starting to rise; the top edge of the dike stays dry, no water pours over it. Wind-torn clouds, flying foam, cold grey light, rain. No people, no buildings breaking.", "base"),
    "F01a": (26111, [f"{REF}/PL-0004/D01_A_dawn-ebb_v1.png", f"{FR}/F01.png"],
             "Wide low shot from the sea side of a colossal brick sea dike under a grey storm sky in daylight: a huge dark green-grey wave rolls toward the dike, its crest curling and torn by wind, still one wave-length away from the sloping outer face; the face is wet, the top edge of the dike dry and empty. Wind-torn clouds, flying foam, cold grey light, rain. No people. The wave fills the left half of the frame, the dike face rises on the right from the bottom edge to well above mid-frame, only sky beyond its top edge; one bold silhouette that reads at phone size.", "base"),
    "F04": (26104, [f"{REF}/PL-0008/D02_C1_dawn-ebb_v1.png"],
            "Extreme close-up of a heavy tarred fishing net hung to dry on a wooden pole in a stilt-town lane at dawn, the knotted mesh fills the left two thirds of the frame, clear water drops gathering on the knots, one drop about to fall. On the right, softly out of focus, a sagging rope strung between two stilt-houses with exactly nine small unlit tin lanterns hanging from it. Cold grey-teal dawn light from above, no direct sun, thin mist.", "base"),
    "F10": (26210, [f"{REF}/PL-0004/D01_A_dawn-ebb_v1.png", f"{REF}/PL-0008/D02_C1_dawn-ebb_v1.png"],
            "High aerial view looking forward over a vast stilt-town below sea level in the morning: a maze of narrow water lanes, plank bridges and tarred roofs, washing lines, small boats tied to pilings; in the middle distance the long brick dike with three-storey brick houses along its crest, the town's roofs lying well below the dike's crest; beyond it a granite hill with terraces and a palace; on the hill two tall black towers, the left one the tallest; a third, shorter black tower stands lower down to the right at the edge of the stilt-town, its dark foot in the water. {SPIRE}. Cool grey light in the town, sun only on the hill and the tower tops. Tiny distant specks of people on far bridges allowed, none larger than a dot.", "base"),
    "F11": (26211, [f"{REF}/PL-0008/D02_C3_dusk_v1.png"],
            "Low shot at water level under a plank bridge between stilt-houses: tarred wooden pilings rising out of shallow dark water over wet silt, the pilings stained darker below an old weed line; no painted marks, no lines, no numbers, no post standing alone in open water; small eddies around the posts. Diffuse cool afternoon light, soft ripple reflections on the underside of the bridge. No people.", "base"),
    "F14": (26214, [f"{REF}/M-LEDGER/E12_ledger_page-a_v1.png"],
            "Top-down view of an open clerk's ledger on worn green felt, ruled columns of tiny illegible ink scribbles, a wide empty margin on the left page, a brass inkwell and a quill at the top edge, a tall leaning tower of rough copper coins standing on the felt to the right of the ledger. Flat cool light from a tall window, dust motes. No hands, no readable text or numbers.", "base"),
    "F15": (26215, [f"{REF}/PL-0004/D01_C_late-aft_v1.png", f"{REF}/PL-0014/D08_S1_late-aft_v1.png"],
            "Use image 1 exactly — same hill, terraces, palace, three towers, ships and harbour, same camera. Change only: (1) remove the cluster of stilt-houses, piers and plank-walks in front of the great wall on the left; in their place open harbour water meeting the foot of the wall; (2) remove every crack, break and rough patch from the right-hand tower: its surface smooth glassy black like the others; (3) relight as late afternoon with the low sun behind the camera in the west: warm light on the face of the wall, the terraces and the towers; the sky behind the hill clear pale blue with a few warm clouds, no sunset glow behind the city. {SPIRE}.", "base"),
    "F17": (26217, [f"{ANI}/sc10-sh030_a.png", f"{REF}/HERALDRY/H01_corvane.png", f"{REF}/HERALDRY/H02_dusk.png",
                    f"{REF}/HERALDRY/H08_choir.png", f"{REF}/HERALDRY/H07_lantry.png", f"{REF}/HERALDRY/H06_fennike.png"],
            "Use image 1 exactly — same granite wall, rail, poles, golden late-afternoon light and shadows, the city, harbour and sea on the right, same camera. Replace the row of banners with five banners evenly spaced along the same rail, each a tall vertical cloth banner with a slanted cut at the bottom and the long point at the pole side, simple flat emblems exactly as in the references, left to right: (1) deep blue field, a black cormorant with half-folded wings diving beak-down into a silver wave of exactly three crests, no fish; (2) ochre field, a bronze sickle with its blade up above three parallel dark-brown furrows, a tool with a short handle, not a crescent moon; (3) undyed linen field, nine short black strokes above one level black line; (4) black field, a copper beam balance with a level beam, the left pan holding a level surface of blue-grey water, the right pan empty; (5) acid sulphur-yellow field, a grey hare seated in profile facing left, both ears straight up and slightly apart, one eye visible. No other banners; no hands, no stones, no eels, no rings, no gates or bars.", "base"),
    "F18": (26218, [f"{REF}/TAPESTRY/E06_panel2_v1.png", f"{REF}/TAPESTRY/E06_panel1_v1.png", f"{REF}/HERALDRY/H01_corvane.png",
                    f"{REF}/HERALDRY/H02_dusk.png", f"{REF}/HERALDRY/H04_rusk.png", f"{REF}/HERALDRY/H05_quell.png",
                    f"{REF}/GROUPS/C06_emblem_strip_ref.png", f"{REF}/HERALDRY/H16_ashare_reference_spiral.png"],
            "Re-weave this tapestry panel keeping its weave, palette, border and the reed-and-river strip at the bottom: nine tall woven banners on a shore, each vertical with a slanted cut at the bottom and the long point at the pole; nine small woven figures, one under each banner, each with one hand raised in an oath, mouths closed, all turned in three-quarter back view toward a black tower rising from the woven sea beyond the shore; no weapons, no spears, no blades. Banners from left to right: (1) a black cliff of angular strata filling the banner, set with a small rust-red gate of vertical bars and two cross-bars, flat top, no spikes; (2) straw-yellow field, a black dike-spade crossed with a reed; (3) deep blue field, a black cormorant with half-folded wings diving beak-down into a silver wave of three crests; (4) ochre field, a bronze sickle blade up above three dark-brown furrows; (5) pale violet field, a white open RIGHT hand, palm toward the viewer, thumb on the viewer's right, fingers slightly spread, a small grey stone with a clockwise spiral resting in the palm; (6) bone-white field, a sea-green eel with a fin ridge making one full coil through a dark iron ring, head up, mouth closed; (7) white field, a grey harrow over a moss-green hill; (8) slate blue-green field, a white waterfall between two grey stones; (9) dark red field, a white unlit lantern on a black tower. Banners 1 and 2 stand together at the left edge, banners 3 to 8 in the centre, banner 9 alone at the right edge. Border spirals turn clockwise from the centre outward. Fabric fills the whole frame.", "chron"),
    "F19": (26219, [f"{REF}/HERALDRY/H01_corvane.png", f"{REF}/HERALDRY/H02_dusk.png", f"{REF}/PL-0004/D01_C_late-aft_v1.png"],
            F19_TEXT, "base"),
    "F21": (26221, [f"{REF}/HERALDRY/H07_lantry.png", f"{REF}/HERALDRY/H06_fennike.png", f"{REF}/PL-0004/D01_C_late-aft_v1.png"],
            F19_TEXT.replace(F19_LR, F21_LR), "base"),
    "F23": (26223, [f"{REF}/TAPESTRY/E06_panel5_v1.png", f"{REF}/HERALDRY/H01_corvane.png", f"{REF}/HERALDRY/H16_ashare_reference_spiral.png"],
            "Use image 1 exactly — same weave, border, ships, sea, wave band and framing. Change only: (1) the emblem on the central white sail becomes a black cormorant with half-folded wings diving beak-down into a silver wave of three crests, no fish; (2) the small pennants at every masthead become deep blue; (3) the green-teal sails of the right-hand ship become ochre. Border spirals stay clockwise from the centre outward. Fabric fills the whole frame.", "chron"),
    "F26": (26226, [f"{REF}/PL-0008/D02_C3_dusk_v1.png"],
            "Low close view along a wet tarred plank-walk between stilt-houses at the start of a storm in daylight: many wet bare footprints of mixed sizes criss-cross the dark planks in different directions and overlap, as on a busy lane; no single trail, no pair of prints walking side by side, no prints leading to the edge of the planks; the first heavy raindrops spatter on the wood; the water below the planks is far down and out of frame. Cold grey storm light. No people, no feet, no legs, no shoes, no shadows of people, no puddles.", "base"),
    "F27": (26227, [f"{REF}/PL-0018/D09_H1_late-aft_v1.png"],
            "Low angle at the seaward end of a long granite harbour mole in a storm in daylight: a grey-green wave bursts against the outer blocks, a thick sheet of white spray is thrown up and falls back into the open sea; wet granite, squat stone bollards, rain, wind-torn clouds, cold grey light. The mole stands well above the sea; the harbour side and the town are out of frame. No gates, no beams or bars, no sluices or channels, no lamps, no people.", "base"),
    "F28": (26228, [f"{REF}/PL-0008/D02_C3_dusk_v1.png", f"{REF}/PL-0008/D02_C1_dawn-ebb_v1.png"],
            "Point of view just above the water, looking straight down a long narrow canal between two rows of stilt-houses in a squall: tarred pilings on both sides, low plank bridges crossing ahead, ropes and hanging nets, wind-driven rain, dark wind-ruffled water lying low between the pilings, far below the plank-walks, wet silt showing at the posts, strong one-point perspective toward a strip of grey sky at the far end. No people, no boats in the path.", "base"),
    "F30": (26230, [],
            "Wide view west over the open sea under a breaking storm in the late afternoon: heavy grey rain sheets slanting across a dark grey-green swell, low torn clouds racing, and just above the horizon a gap opening in the clouds where pale low sunlight falls on the sea in one soft broad shaft. Only sea and sky: no land, no towers, no buildings, no ships, no people.", "base"),
}

PRE_ACT = ("2D anime animation, the colors and line art stay exactly as in the source image, stable outlines, no morphing, "
           "consistent lighting, no new light sources, no glowing marks.")
PRE_QUIET = "Subtle " + PRE_ACT
NEG = ("morphing, flickering line art, warping background, people appearing, faces, hands, glowing objects, light inside the "
       "tower grooves, lightning, sudden cuts, text")
NEG_X = ", explosion, fire, smoke, steam cloud, debris, broken bricks, water pouring over the dike, night"
K11_TEXT = ("Locked-off camera, no camera shake. Both banners ripple and sway in a steady strong wind from the left; waves of "
            "cloth travel down to the slanted bottom points; the emblems stay flat, whole and readable; the poles do not move.")

# id: (source image, quiet?, text, extra negative?). Sources are the accepted frames after op_frame_fixes.py (*_op.png).
CLIPS = {
    "K01": (f"{FR}/F01_op.png", False, "Locked-off camera, no camera shake. White spray rises high above the dike in one heavy column, slowly spreads at the top and falls back toward the sea; sheets of foam slide down the wet sloping face; rain streaks. The brick dike does not move or change; its top edge stays dry and empty; no water flows over the top. Daylight storm, lighting unchanged, no smoke, no fire, no explosion.", True),
    "K01a": (f"{FR}/F01a_op.png", False, "Locked-off camera, no camera shake. The large dark wave swells and rolls steadily toward the dike; wind tears foam off its crest; rain streaks. The dike does not move or change; no water reaches its top.", True),
    "K03": (f"{FR}/F04_op.png", True, "Static camera. Water drops gather on the net knots and fall one by one out of frame; a gust makes the rope of lanterns swing; the lanterns stay unlit and their number does not change.", False),
    "K04": (f"{REF}/PL-0008W/D05_W2_morning_v1.png", False, "Locked-off camera, no camera shake. The wooden slats of the drum move past steadily from top to bottom like a turning wheel; water drips from the slats. The drum keeps its shape; no people.", False),
    "K05": (f"{REF}/PL-0008W/D05_W1_morning_v1.png", True, "Very slow push-in. The three wooden treadwheels turn slowly and steadily, all at the same speed; water drips from the buckets. Wheel shape, spoke count and the shed do not change; no people appear.", False),
    "K07": (f"{FR}/F10_op.png", True, "Smooth slow forward glide of the camera over the town toward the dike and the hill; thin smoke drifts from a few chimneys; mist moves along the water lanes.", False),
    "K08": (f"{FR}/F11_op.png", True, "Very slow push-in toward the pilings. The ebb runs out: the water level drops slowly by a hand's breadth, baring wet silt and the dark stain on the pilings; small eddies swirl around the posts, ripple reflections shimmer under the bridge.", False),
    "K09": (f"{ANI}/sc16-sh040_a.png", True, "Static camera. The bell swings and its clapper strikes once, its rope sways; a little dust falls through the window light.", False),
    "K10": (f"{FR}/F14_op.png", False, "Locked-off top-down camera. The tall leaning stack of copper coins slowly topples to the right in one piece; the coins spread and slide a short way across the felt and stop. Ledger, inkwell and quill do not move; no hands; no text.", False),
    "K11": (f"{FR}/F19_op.png", False, K11_TEXT, False),
    "K12": (f"{FR}/F21_op.png", False, K11_TEXT, False),
    "K13": (f"{PL}/D09_H1_op.png", False, "Locked-off camera, no camera shake. Choppy waves with white caps roll across the harbour the whole time; the ships rock very gently in place. Number, shape and position of all ships stay exactly the same; the sun stays where it is; no people.", False),
    "K14": (f"{FR}/F27_op.png", False, "Static camera. The wave breaks against the mole; spray is thrown up and falls back into the open sea; foam slides back off the blocks; rain.", True),
    "K15": (f"{FR}/F28_op.png", False, "The camera moves steadily forward at a moderate speed low over the water along the canal; pilings pass by on both sides; wind-driven rain. Houses and pilings keep their shape; no boats, no people.", False),
    "K16": (f"{FR}/F30_op.png", False, "Static camera with a slow tilt up. Rain sheets sweep across the sea; the clouds move fast and the gap above the horizon slowly widens; the swell rolls.", False),
    "K17": (f"{REF}/PL-0014/D08_S1_dusk_v1.png", True, "Very slow push-in. Clouds stream past the crown of the tower from left to right; the sky darkens very slightly.", False),
    "K18": (f"{FR}/F26_op.png", True, "Locked-off camera. Heavy rain falls on the planks; the wet footprints slowly blur, spread and fade as the rain washes over them.", False),
}


def frame_prompt(fid):
    seed, refs, text, style = FRAMES[fid]
    text = text.replace("{SPIRE}", SPIRE)
    if style == "chron":
        return seed, refs, f"{text} {CHRONICLE}. {AVOID_OP_F18}"
    return seed, refs, f"{text} {STYLE_BASE}. {AVOID_OP}"


def clip_prompt(kid):
    src, quiet, text, neg_x = CLIPS[kid]
    return src, f"{PRE_QUIET if quiet else PRE_ACT} {text}", NEG + (NEG_X if neg_x else "")


def name(base, take):
    return base if take == 1 else f"{base}_t{take}"


def run_frames(ids, take):
    os.makedirs(FR, exist_ok=True)
    for fid in ids:
        seed, refs, prompt = frame_prompt(fid)
        seed = seed + 1000 * (take - 1)           # a retake uses a new seed, same prompt and parameters
        out = f"{FR}/{name(fid, take)}.png"
        if os.path.exists(out):
            print("exists, skip", out)
            continue
        for r in refs:
            if not os.path.exists(r):
                sys.exit(f"{fid}: missing ref {r}")
        t0 = time.time()
        print(f"{fid} take {take}: NB2 edit, {len(refs)} refs, seed {seed} ...", flush=True)
        fal_client.generate_image(prompt, out, model="nano-banana-2", reference_images=refs or None,
                                  aspect_ratio="16:9", extra={"seed": seed})
        meta = {"id": fid, "take": take, "model": "nano-banana-2-edit" if refs else "nano-banana-2", "seed": seed,
                "aspect_ratio": "16:9", "num_images": 1, "output_format": "png", "resolution": "(not sent: 1K default)",
                "refs": refs, "prompt": prompt, "usd": 0.08, "seconds": round(time.time() - t0, 1)}
        json.dump(meta, open(out[:-4] + ".json", "w"), indent=1, ensure_ascii=False)
        print("  ->", out, f"({meta['seconds']} s), spent so far ${costs.total_spent():.2f}", flush=True)


def run_clips(ids, take, k13_go):
    os.makedirs(CL, exist_ok=True)
    for kid in ids:
        if kid == "K13" and not k13_go:
            sys.exit("K13 waits for the keeper's look at the fixed H1/H2 plates and the studio director's go (C2)")
        src, prompt, neg = clip_prompt(kid)
        out = f"{CL}/{name(kid, take)}.mp4"
        if os.path.exists(out):
            print("exists, skip", out)
            continue
        if not os.path.exists(src):
            sys.exit(f"{kid}: missing source {src}")
        t0 = time.time()
        print(f"{kid} take {take}: Kling 2.5 TP 5 s from {src} ...", flush=True)
        fal_client.image_to_video(src, prompt, out, model="kling-2.5-turbo-pro", duration=5, negative_prompt=neg)
        meta = {"id": kid, "take": take, "model": "kling-2.5-turbo-pro", "duration": 5, "source": src, "prompt": prompt,
                "negative_prompt": neg, "usd": 0.35, "seconds": round(time.time() - t0, 1)}
        json.dump(meta, open(out[:-4] + ".json", "w"), indent=1, ensure_ascii=False)
        print("  ->", out, f"({meta['seconds']} s), spent so far ${costs.total_spent():.2f}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["frames", "clips", "show"])
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--take", type=int, default=1)
    ap.add_argument("--k13-go", action="store_true")
    a = ap.parse_args()
    if a.kind == "show":
        for i in a.ids:
            print(json.dumps(frame_prompt(i) if i in FRAMES else clip_prompt(i), indent=1, ensure_ascii=False))
        return
    if a.kind == "frames":
        run_frames(a.ids, a.take)
    else:
        run_clips(a.ids, a.take, a.k13_go)


if __name__ == "__main__":
    main()
