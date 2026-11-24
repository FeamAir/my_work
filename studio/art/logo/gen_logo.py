"""HOLLOWSTONE logotype, NB2 text-to-image. Usage: python gen_logo.py KEY [KEY...]
Params as the earlier NB2 calls: aspect 16:9, num_images 1, png, fixed seed, no resolution key."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from pipeline import fal_client

OUT = Path(__file__).resolve().parent / "gen"

LETTERS = ('The single word "HOLLOWSTONE" in capital letters, spelled exactly H-O-L-L-O-W-S-T-O-N-E '
           '(eleven letters: H, O, L, L, O, W, S, T, O, N, E), one line, centred, filling about 80% of the width. ')
STYLE = ('Designed title logotype for an original 2D anime-style fantasy TV series, painterly but crisp, '
         'thin dark blue-black outline (#1C1F2A) of slightly varying weight around every letter, '
         'muted desaturated palette, cool violet-blue shadow side, one soft natural highlight on the upper bevel '
         'edges from a low cold key light at upper left. ')
FACE = ('Custom display capitals in the manner of an old harbour-wall inscription cut by a mason\'s chisel: '
        'tall, slightly condensed, flat-topped, with short sharp wedge-cut serifs, V-section chisel bevels inside each stroke, '
        'strong even stroke weight, generous even letter spacing. The O letters are plain upright ovals with empty open '
        'counters (nothing inside them, no hole set with anything). ')
TIDE = ('The letters are cut from weathered pale grey granite (#B8B4AC), lightly pitted, with fine chips at the edges. '
        'One single straight horizontal tide line crosses the whole word at about one third of the letter height: '
        'below the line the stone is darker and damp blue-grey (#5C6B72) with a thin crisp crust of white salt along the line '
        'and faint dark green weed staining; above the line the stone is dry and pale. A few small clear drops cling to the '
        'lower edges of the letters. ')
SPIRE_T = ('Only the letter T is special: its stem is a slim tapering cone of smooth black glassy stone (#0D0F14) widening slightly '
           'toward the bottom, with three deep dark spiral grooves winding around it that rise from lower-left to upper-right ( / ) '
           'on the visible face; its crossbar is a short crown band pierced by a row of small open round-topped arches. '
           'The T still reads clearly as a capital T. The grooves are dark, nothing lights up. ')
BG = 'Isolated on a flat, perfectly even pure black background (#000000), no texture, no vignette, no horizon. '
AVOID = ('Avoid: any other text, tagline, subtitle, numbers, extra letters, misspelling, watermark; no glow, no halo, no light '
         'inside grooves, no magic light, no sparkles, no lens flare; no rings, no circles or discs behind the word, no shields, '
         'no frames, banners, ribbons or emblems; no gems, pebbles, shards or stones set into or hanging from letters; no cords; '
         'no hands; no water surface, no sea, no waves, no reflection; no 3D render look, no photorealism, no metal or gold letters, '
         'no neon colors, no mirrored image.')

JOBS = {
    "A1": (LETTERS + STYLE + FACE + TIDE + BG + AVOID, 410711),
    "A2": (LETTERS + STYLE + FACE + TIDE + BG + AVOID, 410722),
    "B1": (LETTERS + STYLE + FACE + TIDE + SPIRE_T + BG + AVOID, 410733),
    "B2": (LETTERS + STYLE + FACE + TIDE + SPIRE_T + BG + AVOID, 410744),
    # A3: the A face less condensed (thumbnail legibility), deeper chisel bevels, same tide line
    "A3": (LETTERS + STYLE + FACE.replace("tall, slightly condensed", "medium width, not condensed, letters about as wide as they are three quarters tall")
           .replace("strong even stroke weight", "heavy even stroke weight, deep V-section chisel bevels that catch the light on one side")
           + TIDE + BG + AVOID, 410755),
}

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    meta_p = OUT / "meta.json"
    meta = json.loads(meta_p.read_text()) if meta_p.exists() else {}
    for key in sys.argv[1:]:
        prompt, seed = JOBS[key]
        out = OUT / f"LOGO_{key}_v1.png"
        try:
            fal_client.generate_image(prompt, out, model="nano-banana-2", aspect_ratio="16:9", extra={"seed": seed})
            st = "ok"
        except Exception as e:
            st = f"error: {e}"
        meta[key] = {"prompt": prompt, "model": "nano-banana-2", "refs": [], "aspect": "16:9", "seed": seed, "status": st}
        meta_p.write_text(json.dumps(meta, indent=1, ensure_ascii=False))
        print(key, st)
