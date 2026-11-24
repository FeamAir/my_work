"""STYLE_ALIVE test (2026-11-24): 3 rendering directions x 2 subjects on nano-banana-2 /edit.

Run from repo root:
  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=65 python3 studio/art/style_alive/gen_style_alive.py [job ...]
Jobs: A_pell A_house B_pell B_house C_pell C_house (default: all six).
Outputs: output/style_alive/<job>.png ; prompts/refs/seeds: studio/art/style_alive/meta.json
"""
import json
import random
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from pipeline import fal_client  # noqa: E402

R = "studio/direction/refs/"
OUT = Path("output/style_alive")
META = Path("studio/art/style_alive/meta.json")

STYLES = {
    "A": (
        "Feature-quality 2D hand-drawn animated film still, original character and world design. "
        "Refined clean line art with thin tapered lines of varied weight: slightly heavier on the outer "
        "contour and in shadow, thinning and breaking where light hits the form; line colour tinted by the "
        "local colour, not uniform black. Soft multi-tone shading with gentle gradients over faces, hands and "
        "clothes, warm bounce light filling the shadows, a thin rim light separating figures from the "
        "background. Subtle skin colour variation: warmer cheeks, nose tip and ears, cooler jaw and temples. "
        "Expressive eyes with layered iris colour, a soft upper-lid shadow and clear catchlights; brows and "
        "eyelids shaped by the emotion. Hair in soft locks with light passing through the edges. Atmospheric "
        "depth: layered haze, softer and cooler in the distance, painted environment. Muted desaturated palette "
        "with deep teal-black shadows and cool violet-blue shadows, subtle film grain, grounded epic fantasy."
    ),
    "B": (
        "Painterly animated feature film still, original character and world design. Characters painted "
        "with visible textured brush strokes over a light underdrawing; outlines appear only in shadowed "
        "edges and dissolve into light on the lit side. Shading built from soft brushy planes of warm and cool "
        "colour, light wrapping around faces and hands, glowing edges where light catches hair and skin. "
        "Cinematic motivated lighting with clear light-and-shadow shapes, dust in the light beam, damp air. "
        "Rich detailed painted environment with depth, wet reflective surfaces, tactile wood, rope and cloth. "
        "Muted desaturated palette with deep teal-black shadows and cool violet-blue shadows, subtle canvas "
        "grain, grounded epic fantasy."
    ),
    "C": (
        "Stylized 3D animated feature film still, original character and world design. Keep exactly the "
        "stylized proportions and facial design of the reference sheets, translated into soft sculpted "
        "volumes. Soft skin with gentle subsurface warmth in ears, nose and fingertips, soft global "
        "illumination and contact shadows, a soft area light from the main light source, subtle rim light. "
        "Hair as sculpted soft locks with fine strand texture at the edges. Fabrics with tactile texture: "
        "tarred oilskin, knitted wool, worn linen. Hand-painted simplified textures, stylized and not "
        "photoreal, shallow depth of field, atmospheric haze. Muted desaturated palette with deep teal-black "
        "shadows and cool violet-blue shadows, grounded epic fantasy."
    ),
}

AVOID_COMMON = (
    "comic book look, heavy uniform black outlines, flat cel shading with hard two-tone shadows, halftone "
    "dots, crosshatching, stiff frontal pose, plain empty background, text, letters, labels, captions, "
    "watermark, logo, signature, extra fingers, fused hands, extra limbs, accessories switching sides, "
    "mirrored image, magical glow, extra people, chibi proportions, neon colours"
)
AVOID_STYLE = {
    "A": "photorealism, 3D render look",
    "B": "photorealism, 3D render look, messy unreadable faces",
    "C": "photorealism, realistic skin pores, uncanny realistic face, glossy plastic toy look, doll eyes",
}

PELL_ID = (
    "the 15-year-old girl from images 1-2, small and wiry; olive-brown sun-darkened skin, freckles across "
    "the nose; cropped ragged rust-brown hair (red-brown, not orange); exactly one long thin braid, and it "
    "hangs on the RIGHT side of the picture, in front of her shoulder; the left side of the picture has only "
    "short cropped hair; the braid ends in a small blue tin tag tied to the braid tip (the tag is on the "
    "braid, not on her clothes); narrow sea-grey eyes; patched tar-brown oilskin jacket; the strap of a "
    "salvage net bag crosses her chest; hands mud-dark to the wrist"
)

PELL_PORTRAIT = (
    "Images 1-2 are the character master and turnaround: keep her face, proportions, hair, outfit and "
    "colours exactly the same character; change only the rendering style. Waist-up portrait, cropped at the "
    "waist, legs and feet not visible, 3:4. Subject: " + PELL_ID + ". Living pose and natural emotion: she "
    "has just come in out of the cold dawn and stands by a small window inside a dark wooden stilt-house, "
    "body in three-quarter view, weight on one hip, shoulders slightly hunched against the cold, one "
    "mud-dark hand pulling the net-bag strap higher on her chest; head turned toward the viewer, a small "
    "tired, wary half-smile at one corner of the mouth, brows slightly raised, eyes alive and focused, a few "
    "loose strands of hair stuck to her damp cheek. Lighting: soft cool grey-teal morning light from the "
    "window on the RIGHT side of the picture, rim light on her cheek, hair and braid, warm faint bounce from "
    "the wooden floor in the shadows; behind her a softly out-of-focus interior with hanging nets and a "
    "beam. "
)

HOUSE_V1_PREFIX = (
    "Image 1 is the current approved frame: keep its composition, room, camera and the positions and "
    "actions of the three people; change only the rendering style and lighting quality. Image 2 is the room "
    "plate; images 3-4 the girl (master and turnaround), 5-6 the small boy, 7-8 the old woman. "
)
# r1: the old frame as image 1 dominated the style (v1 outputs were near-copies of the old frame),
# so retakes drop it and pass only the plate + character sheets, blocking described in text.
HOUSE_R1_PREFIX = (
    "Image 1 is the room plate (keep the room: table by the window, open doorway to the misty water on "
    "the left of centre, net-chest in the left corner, nets on the beams, shelf with jars). Images 2-3 are "
    "the girl (master and turnaround), 4-5 the small boy, 6-7 the old woman: keep their faces, hair "
    "colours, outfits and proportions exactly, but re-render them completely in the style described below, "
    "do not copy the line art or flat colouring of the sheets. Scale: the boy reaches about the girl's "
    "shoulder, the old woman is tiny and bent. "
)
HOUSE_BODY = (
    "Medium-wide shot inside a stilt-house. The old woman sits at the table mending a net in her lap, eyes "
    "on her work, with exactly one small spiral-shell earring in the ear on the RIGHT side of the picture; "
    "the boy sits on a stool at the left end of the table reaching for the loaf, the single tuft of hair at "
    "his temple on the LEFT side of the picture, no cap; the girl stands on the right side of the room, body "
    "three-quarters toward the camera, a small easy shift of weight, looking at the boy with a faint "
    "softening of her face, her single braid hanging on the RIGHT side of the picture with the small blue "
    "tin tag at its tip (the tag is tied to the braid tip, not on her jacket), rag-wrapped bare feet. Same "
    "faces, hair colours, outfits and proportions as their sheets. Lighting from the window: soft cool "
    "grey-teal morning light pours in from the window and the open doorway, a visible soft light shaft "
    "with floating dust, the light falls across the table, the loaf, the old woman's hands and the girl's "
    "face; rim light on hair and shoulders facing the window, warm faint bounce from the table and "
    "floorboards into the shadows, the corners of the room fall into deep teal-black shadow; all three lit "
    "by the same light as the room, not brighter or warmer than it. "
)
HOUSE = HOUSE_V1_PREFIX + HOUSE_BODY
RETAKE = False


def build(job):
    style, subj = job.split("_")
    avoid = AVOID_COMMON + ", " + AVOID_STYLE[style]
    if subj == "pell":
        prompt = (PELL_PORTRAIT + STYLES[style] + " Avoid: " + avoid + ", braid on the left side of the "
                  "picture, two braids, long loose hair, bright orange hair, tag pinned on the jacket, full "
                  "body, feet, clean hands, jewellery, earrings.")
        refs = [R + "CH-0001/A01_00_master_v1.png", R + "CH-0001/A01_01_turnaround_v1.png"]
        aspect = "3:4"
    else:
        prompt = ((HOUSE_R1_PREFIX + HOUSE_BODY if RETAKE else HOUSE) + STYLES[style] + " 16:9 widescreen composition. Avoid: " + avoid + ", braid on the "
                  "left side of the picture, two braids, cap on the boy, earrings on the girl, earring in "
                  "both ears, tag pinned on the jacket, shoes on the girl, characters brighter than the room.")
        refs = ([] if RETAKE else [R + "keyframes/test_pell_wick_nan_house_v1.png"]) + [
                R + "PL-0019/D06_N1_morning_v1.png",
                R + "CH-0001/A01_00_master_v1.png", R + "CH-0001/A01_01_turnaround_v1.png",
                R + "CH-0007/A02_00_master_v1.png", R + "CH-0007/A02_01_turnaround_v1.png",
                R + "CH-0015/A03_00_master_v1.png", R + "CH-0015/A03_01_turnaround_v1.png"]
        aspect = "16:9"
    return prompt, refs, aspect


def run(job, suffix=""):
    prompt, refs, aspect = build(job)
    seed = random.randint(1, 999999)
    name = job + suffix
    try:
        fal_client.generate_image(prompt, OUT / f"{name}.png", model="nano-banana-2",
                                  reference_images=refs, aspect_ratio=aspect, extra={"seed": seed})
        status = "ok"
    except Exception as e:  # noqa: BLE001
        status = f"error: {type(e).__name__}: {e}"[:300]
    return name, {"prompt": prompt, "refs": refs, "aspect": aspect, "seed": seed,
                  "model": "nano-banana-2", "status": status}


if __name__ == "__main__":
    args = sys.argv[1:]
    suffix = ""
    if args and args[0].startswith("--suffix="):
        suffix = args.pop(0).split("=", 1)[1]
        RETAKE = True  # any suffixed run is a retake (house: no old frame as ref)
    jobs = args or ["A_pell", "A_house", "B_pell", "B_house", "C_pell", "C_house"]
    OUT.mkdir(parents=True, exist_ok=True)
    meta = json.loads(META.read_text()) if META.exists() else {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        for name, m in ex.map(lambda j: run(j, suffix), jobs):
            meta[name] = m
            print(name, m["status"], m["seed"])
    META.write_text(json.dumps(meta, indent=1, ensure_ascii=False))
