"""STYLE C (stylised 3D volume) — C-final frames + Kling motion test (2026-11-24).

Run from repo root:
  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=66 python3 studio/art/style_c/gen_style_c.py img C2_pell
  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=66 python3 studio/art/style_c/gen_style_c.py img C2_house
  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=66 python3 studio/art/style_c/gen_style_c.py vid <image.png> <pell|house> <out.mp4>
Approach: the style lives in the references (see style_alive report §3.1). So the C-final frame is a
conversion EDIT of the already-volumetric test frame (image 1), with the 2D sheets only as identity refs.
"""
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from pipeline import fal_client  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from style_base_c import STYLE_BASE_C, NEGATIVE_C, MOTION_NEGATIVE  # noqa: E402

R = "studio/direction/refs/"
OUT = Path("output/style_c")
META = Path("studio/art/style_c/meta.json")

CONVERT = (
    "Convert image 1 into a finished frame of a stylized 3D CG animated feature film: the same shot "
    "rebuilt as sculpted 3D models in a lit 3D set, rendered with soft global illumination. Keep the "
    "composition, camera, pose, expression and every costume detail of image 1; change only the "
    "rendering from painted 2D to true 3D volume: rounded sculpted forms that turn in the light, "
    "soft subsurface skin, real cast and contact shadows, depth of field. No outlines anywhere. "
)

PELL = (
    CONVERT +
    "Images 2-3 are the character master and turnaround of the same girl: use them only to keep her "
    "identity exact. She is 15, small and wiry, with a youthful slightly angular face, large-ish narrow "
    "sea-grey eyes, a small nose and a dusting of freckles across the nose and cheeks; olive-brown "
    "sun-darkened skin; cropped ragged rust-brown hair (red-brown, not orange); exactly one long thin "
    "braid hanging on the RIGHT side of the picture in front of her shoulder, ending in a small blue tin "
    "tag tied to the braid tip (the tag is on the braid, not on the jacket); the left side of the picture "
    "shows only short cropped hair; patched tar-brown oilskin jacket, the strap of a salvage net bag "
    "across her chest, hands mud-dark to the wrist. Waist-up portrait, 3:4, window light from the RIGHT "
    "side of the picture, warm bounce from the floor, dark wooden stilt-house interior softly out of focus "
    "behind her. Keep her young: not older, not heavier in the face. "
)

HOUSE = (
    CONVERT +
    "Image 1 is the approved staging. Image 2 shows the girl already in the target 3D style: match her "
    "face, hair and outfit to image 2. Images 3 and 4 are the identity sheets of the small boy and the "
    "old woman. Keep: the old woman sitting at the table mending a net in her lap, a headscarf, exactly one "
    "small spiral-shell earring in the ear on the RIGHT side of the picture; the small boy on a stool at "
    "the left end of the table reaching for the loaf, cream knitted sweater, the single tuft of hair at "
    "his temple on the LEFT side of the picture, no cap; the girl standing on the right in a patched "
    "tar-brown oilskin JACKET (the net bag hangs at her hip on its strap, it is not worn as a vest), single "
    "braid on the RIGHT side of the picture with the small blue tin tag at its tip, rag-wrapped bare feet. "
    "Soft cool grey-teal light from the window and the open doorway, a soft light shaft with dust, warm "
    "faint bounce from the table and floorboards, corners in deep teal-black shadow; the people lit by the "
    "same light as the room. 16:9 widescreen. "
)

PELL_R1 = (
    "Image 1 is a frame from our stylized 3D CG animated feature: match its 3D rendering exactly (sculpted "
    "rounded volumes, soft global illumination, matte hand-painted textures, depth of field). Images 2-3 "
    "are the character master and turnaround of the girl: build her as the same kind of 3D character "
    "model, keeping her identity exact, then render a NEW waist-up portrait of her, 3:4. "
    + PELL.split("Images 2-3 are the character master and turnaround of the same girl: use them only to keep her "
                 "identity exact. ")[1]
)

JOBS = {
    "C2_pell": (PELL, ["output/style_alive/C_pell.png", R + "CH-0001/A01_00_master_v1.png",
                       R + "CH-0001/A01_01_turnaround_v1.png"], "3:4",
                ", braid on the left side of the picture, two braids, tag on the jacket, older face, "
                "earrings, jewellery, clean hands"),
    "C2_pell_r1": (PELL_R1, ["output/style_c/C2_house.png", R + "CH-0001/A01_00_master_v1.png",
                          R + "CH-0001/A01_01_turnaround_v1.png"], "3:4",
                   ", braid on the left side of the picture, two braids, tag on the jacket, older face, "
                   "earrings, jewellery, clean hands, the old woman, the boy, other people"),
    "C2_house": (HOUSE, ["output/style_alive/B_house_r1.png", "output/style_c/C2_pell.png",
                         R + "CH-0007/A02_00_master_v1.png", R + "CH-0015/A03_00_master_v1.png"], "16:9",
                 ", braid on the left side of the picture, cap on the boy, earrings on the girl, earring "
                 "in both ears, net bag worn as a vest, apron on the girl, skirt on the girl, shoes on the girl"),
}

MOTION = {
    "pell": (
        "Static camera, very slow gentle push-in. The girl breathes calmly, shoulders rising slightly; she "
        "blinks once naturally, her eyes shift a little toward the window and back to the viewer, a faint "
        "tired half-smile forms at one corner of her mouth; her mud-dark hand tightens on the net-bag strap. "
        "A few loose hair strands stir slightly; dust drifts in the window light. Must NOT change: her face "
        "and identity, eye colour, freckles, hair length and colour, exactly one braid on the RIGHT side of "
        "the picture with the small blue tin tag at its tip, the jacket and net bag, the room and the light "
        "direction. No morphing, no face changes, no new objects, no camera cut."
    ),
    "house": (
        "Static locked-off camera. Small natural actions: the old woman's hands work the net needle through "
        "a mesh, she glances up briefly; the boy pulls the loaf toward himself and breaks off a piece; the "
        "girl shifts her weight and her face softens as she watches the boy. Dust drifts slowly in the light "
        "shaft. Must NOT change: the three faces and outfits, the girl's single braid on the RIGHT side of the "
        "picture with its small blue tin tag, the old woman's single earring on the RIGHT side of the picture, "
        "the boy's bare head with the tuft of hair, the room layout and the light. No morphing, no new people, "
        "nobody leaves or enters, no camera move, no cut."
    ),
}


def img(job):
    prompt, refs, aspect, extra_neg = JOBS[job]
    prompt = prompt + STYLE_BASE_C + " Avoid: " + NEGATIVE_C + extra_neg + "."
    seed = random.randint(1, 999999)
    out = OUT / f"{job}.png"
    try:
        fal_client.generate_image(prompt, out, model="nano-banana-2", reference_images=refs,
                                  aspect_ratio=aspect, extra={"seed": seed})
        status = "ok"
    except Exception as e:  # noqa: BLE001
        status = f"error: {type(e).__name__}: {e}"[:300]
    return job, {"prompt": prompt, "refs": refs, "aspect": aspect, "seed": seed,
                 "model": "nano-banana-2", "status": status}


def vid(image, subj, out):
    prompt = MOTION[subj]
    try:
        fal_client.image_to_video(image, prompt, out, model="kling-2.5-turbo-pro", duration=5,
                                  negative_prompt=MOTION_NEGATIVE)
        status = "ok"
    except Exception as e:  # noqa: BLE001
        status = f"error: {type(e).__name__}: {e}"[:300]
    return Path(out).stem, {"image": image, "prompt": prompt, "negative_prompt": MOTION_NEGATIVE,
                            "model": "kling-2.5-turbo-pro", "duration": 5, "status": status}


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    meta = json.loads(META.read_text()) if META.exists() else {}
    if sys.argv[1] == "img":
        name, m = img(sys.argv[2])
        if len(sys.argv) > 3:  # retake suffix
            Path(OUT / f"{name}.png").rename(OUT / f"{name}{sys.argv[3]}.png") if m["status"] == "ok" else None
            name += sys.argv[3]
    else:
        name, m = vid(sys.argv[2], sys.argv[3], sys.argv[4])
    meta[name] = m
    print(name, m["status"])
    META.write_text(json.dumps(meta, indent=1, ensure_ascii=False))
