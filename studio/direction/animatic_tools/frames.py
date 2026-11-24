#!/usr/bin/env python3
"""S01E01 animatic, step 3: one frame per shot (nano-banana /edit with reference sheets).

  python3 -I frames.py plan                 # list jobs, cost estimate, no calls
  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=70 python3 -I frames.py run [--scenes sc01,sc02] [--pass a|b] [--only id,id]
  python3 -I frames.py plates               # $0: copy accepted ref plates for plate/refplate shots
  python3 -I frames.py contact sc01 ...     # contact sheets -> studio/direction/animatic_contacts/

Frames: output/S01E01/animatic/frames/<shot>_a.png (start / only pose), <shot>_b.png (end pose, classes C/D,
edit from _a). Prompts + refs + seeds: frames/meta.json. Existing files are never regenerated unless --force.
All on-screen text is drawtext later; prompts ask for blank spaces.
"""
import concurrent.futures as cf
import glob
import json
import os
import re
import shutil
import sys

ROOT = "/home/user/my_work"
sys.path.insert(0, ROOT)
A = f"{ROOT}/output/S01E01/animatic"
FR = f"{A}/frames"
REFS = f"{ROOT}/studio/direction/refs"
META = f"{FR}/meta.json"

STYLE = ("2D anime-style TV series still, original character and world design, clean cel-shaded characters with crisp thin "
         "dark blue-black ink outlines of slightly varying weight, flat color fills with two shadow tones, cool violet-blue "
         "shadows, restrained highlights only on eyes, hair, metal and wet surfaces, detailed painterly matte-painting "
         "background with atmospheric haze, wet reflective stone and water, motivated cinematic lighting, muted desaturated "
         "palette with deep teal-black shadows, subtle film grain, grounded epic fantasy, 16:9 widescreen composition")
AVOID = ("Avoid: photorealism, 3D look, chibi style, neon colors, any text, letters, numbers or labels, watermark, "
         "model-sheet layout, multiple panels, split screen, deformed hands, extra fingers, glowing objects, "
         "mirrored image, accessories switching sides, extra people.")
LIGHT = {
    "LOWS_DAWN": "stilt-town below sea level in the shadow of a towering brick dike, cold grey-teal dawn light from above, no direct sunlight on the ground, exposed wet silt and tar-black pilings reflecting a pale sky, thin mist over the drained canals",
    "LOWS_DAY": "cramped lanes of wooden stilt-houses and plank-walks under a high dike wall, diffuse cool daylight from a narrow strip of sky, wet tarred wood, ropes and nets, rust stains, puddles reflecting the sky",
    "LOWS_DUSK": "stilt-town at dusk, tide back in the lanes, dark water between the houses, first lanterns lit in doorways, warm amber lantern light against cold blue dusk, reflections on the water",
    "LOWS_NIGHT_FLOOD": "night flood, black water up to the door lintels, rain, a few amber lanterns as the only light, long lantern reflections broken by ripples, silhouettes, deep teal-black shadows",
    "MIDS_INTERIOR": "high hall of brick and grey stone, tall clerestory windows with soft cool light, dust in the light beams, dark wood, brass fittings, ink and paper",
    "STEPS_GOLD": "on a granite hill above the city, low clean golden sunlight, long crisp shadows, polished pale granite, silk banners, open sky",
    "SPIRE_SILENT": "a colossal tower of glassy black stone with deep spiral grooves winding up its whole height, crowned by a ring of open arches, cold faint sheen on the stone, no glow",
    "SPIRE_SUNG": "a colossal tower of glassy black stone with deep spiral grooves, the grooves glowing faint blue-white from inside turn by turn, the harbor water around it perfectly flat like a mirror, exact reflections",
    "HARBOR_GLASS": "a wide harbor turned perfectly still like glass, ship masts motionless, exact mirror reflections of hulls and sky, no waves",
    "CHRONICLE": "a flat woven tapestry panel, visible textile weave and thread texture, faded indigo, madder red, ochre and undyed linen, stylized flat figures in profile, no perspective, decorative border",
    "DOCUMENT": "top-down view of an old hand-drawn map or ledger on a dark wooden table, flat even light, paper texture, ink lines, no readable text",
}
# Short ID blocks (pilot_references.md, with the style-test side lessons). The reference image carries the look.
ID = {
    "PELL": "PELL, a wiry 15-year-old girl: olive-brown freckled skin, cropped ragged rust-brown hair with exactly ONE long thin braid ending in a small blue tin tag (the tag is tied to the braid tip, never on her clothes), narrow sea-grey eyes, patched tar-brown oilskin jacket, mud-grey wading leggings, rag-wrapped bare feet, salvage net bag on a cord, hands mud-dark to the wrist",
    "WICK": "WICK, a skinny 11-year-old boy: olive-brown skin, messy mouse-brown mop with one tuft sticking straight up at one temple, big sea-grey eyes, oversized oatmeal hand-knitted jumper with rolled sleeves, rope belt, patched brown knee trousers, bare feet, no hat",
    "NAN": "NAN, a tiny bent elderly woman of 70: deep brown wrinkled skin, faded indigo headscarf knotted at the nape, sharp black eyes, a single small spiral-shell earring in ONE ear only (as on the reference), brown net-mender's apron over a faded blue-grey dress",
    "IONE": "IONE, an 18-year-old tall slender singer: long straight pale-silver hair to the waist (silver from the roots, no dark roots), two thin side-plaits, dark brown eyes, layered white robes with pale-violet trim, long sleeves, undyed-linen stole, violet silk band around the throat, small silver tuning-fork pendant",
    "RUEL": "RUEL, a big heavy-chested man of 48: sea-weathered tan, salt-and-pepper hair in a short queue, grey-streaked square dark beard, warm hazel eyes, deep-blue admiral's long coat to the calves with silver braid and a silver cormorant clasp, white shirt, dark boots, black pearl ring on his LEFT hand only",
    "HOLLIS": "HOLLIS, a very tall thin stooped clerk of 26: pale skin, flat straw-blond hair with a cowlick, pale blue eyes, round wire spectacles with ONE cracked lens (as on the reference), ink-stained fingers, long light ash-grey clerk's coat, white stock, black sleeve-guards",
    "URSEL": "URSEL, a small very upright woman of 62: light-brown skin, iron-grey hair in a tight coil with copper pins, dark amused eyes, pince-nez on a copper chain, black gown with copper embroidery, black walking stick with a small copper balance-scale handle",
    "ODO": "ODO, a short slight round-shouldered man of 55: pale skin, shaved head, no beard, heavy-lidded pale grey eyes, slate-grey robe with acid sulphur-yellow lining at the cuffs, hands in sleeves, small silver hare's-ear brooch at the collar",
    "LUCAN": "LUCAN, the Helm, a tall stooped frail old man of 71: fair weathered skin, square white beard, thin white hair combed back, floor-length ochre robe under a storm-grey high-collared mantle, heavy bronze sickle-shaped ring on his right hand",
    "JUNO": "JUNO, a short plump young woman of 19: kitchen-pale skin, auburn hair under a white taster's coif, nervous green-brown eyes, plain grey servant's dress with white apron, small silver spoon on a chain",
    "FOSSETT": "FOSSETT, a short round clerk of 30: pink complexion, pomaded chestnut hair with a sharp centre parting, long light ash-grey clerk's coat, white stock, spotless white sleeve-guards, small copper lapel pin",
    "MAGS": "MAGS, a tall gangly 15-year-old girl: olive skin, frizz of black hair tied up with a strip of red rag, oversized dark man's waistcoat full of pockets, rolled trousers, bare muddy feet",
    "CORR": "CORR, a barrel-bodied man of 55: sun-blackened deep brown skin, grey beard twisted into a single rope, his LEFT forearm ends in a leather-wrapped stump (no left hand), reed whistle in his right hand, sleeveless patched leather jerkin, knee breeches, bare feet",
    "COLLECTOR": "the TITHE-COLLECTOR, a lean sallow man in his forties: thin moustache, tired narrow eyes, slate-grey tabard with a single sulphur-yellow stripe over a dark coat, felt hat, small iron-bound wooden box chained to his left wrist",
    "MAREN": "MAREN, a tall lean young woman of 19 seen from behind or in profile: dark curls tied high with a silver cord, deep-blue SHORT riding coat cut at the hip, grey breeches, sea boots, brass spyglass at her hip, hands clasped behind her back",
}
# storyboard ref-ID -> reference folder
BMAP = {"B-01": "CH-0016", "B-02": "CH-0063", "B-03": "CH-0055", "B-04": "CH-0049", "B-05": "CH-0048", "B-06": "B-06",
        "B-07": "CH-0006", "B-08": "CH-0004", "B-09": "CH-0023", "B-10": "CH-0056", "B-11": "B-11", "B-12": "CH-0012",
        "B-13": "CH-0022"}
PMAP = {"CH-0001": "PELL", "CH-0007": "WICK", "CH-0015": "NAN", "CH-0002": "IONE", "CH-0005": "RUEL", "CH-0003": "HOLLIS",
        "CH-0011": "URSEL", "CH-0010": "ODO", "CH-0016": "LUCAN", "CH-0063": "JUNO", "CH-0055": "FOSSETT",
        "CH-0049": "MAGS", "CH-0048": "CORR", "B-06": "COLLECTOR", "CH-0006": "MAREN"}
EMAP = {"E-01": "M-SHD", "E-02": "M-RNG", "E-03": "M-CLP", "E-04": "M-FRK", "E-05": "M-MAP", "E-06": "TAPESTRY",
        "E-07": "M-CUP", "E-08": "M-BOX", "E-09": "M-CHEST", "E-10": "M-CRD", "E-11": "M-ECHO", "E-12": "M-LEDGER"}
DMAP = {"D-01": "PL-0004", "D-02": "PL-0008", "D-03": "PL-0021", "D-04": "PL-0020", "D-05": "PL-0008W", "D-06": "PL-0019",
        "D-07": "PL-0078", "D-08": "PL-0014", "D-09": "PL-0018", "D-10": "PL-0009", "D-11": "PL-0011", "D-12": "PL-0012"}
LIGHTWORDS = [("night-rain", ["night", "rain"]), ("flood", ["flood", "night"]), ("night", ["night"]), ("dawn-ebb", ["dawn"]),
              ("dusk", ["dusk", "toward evening", "evening"]), ("last-light", ["last light"]), ("evening", ["evening"]),
              ("late-aft", ["late afternoon", "afternoon"]), ("morning", ["morning"]), ("noon", ["noon"]), ("glass", ["still", "glass"]),
              ("sung", ["glowing"])]
# accepted location plates used directly for no-character shots ($0; LA move gives the shot)
PLATE_DIRECT = {
    "sc02-sh170": "PL-0008/D02_C4_dawn-ebb_v1.png", "sc03-sh060": "PL-0020/D04_K1_dawn-ebb_v1.png",
    "sc08-sh010": "PL-0014/D08_S3_late-aft_v1.png", "sc08-sh200": "PL-0014/D08_S4_late-aft_v1.png",
    "sc09-sh020": "PL-0018/D09_H1_late-aft_v1.png", "sc09-sh070": "PL-0018/D09_H2_glass_v1.png",
    "sc09-sh120": "PL-0004/D01_A_late-aft_v1.png", "sc15a-sh060": "PL-0008/D02_C1_dusk_v1.png",
    "sc15a-sh100": "PL-0004/D01_A_late-aft_v1.png", "sc16-sh180": "PL-0004/D01_B_dusk_v1.png",
    "sc17-sh010": "PL-0012/D12_R1_dusk_v1.png", "sc18-sh010": "PL-0021/D03_G2_dusk_v1.png",
    "sc19-sh320": "PL-0008/D02_C3_dusk_v1.png",
    # ref plates (storyboard refplate=True)
    "sc02-sh150": "PL-0004/D01_A_dawn-ebb_v1.png", "sc05-sh010": "TAPESTRY/E06_panel1_v1.png",
    "sc05-sh020": "TAPESTRY/E06_panel2_v1.png", "sc05-sh030": "TAPESTRY/E06_panel3_v1.png",
    "sc05-sh040": "TAPESTRY/E06_panel4_v1.png", "sc05-sh050": "TAPESTRY/E06_panel5_v1.png",
    "sc05-sh060": "TAPESTRY/E06_panel6_v1.png", "sc07-sh010": "M-MAP/E05_map_base_v1.png",
    "sc12-sh010": "M-MAP/E05_map_base_v1.png",
}


def shots():
    return json.load(open(f"{A}/spec/shots.json"))["shots"]


def pick(folder, prefix, hint):
    fs = sorted(glob.glob(f"{REFS}/{folder}/{prefix}*.png"))
    if not fs:
        return None
    h = (hint or "").lower()
    for lw, words in LIGHTWORDS:
        if any(w in h for w in words):
            for f in fs:
                if f"_{lw}_" in f:
                    return f
    return fs[0]


def resolve(shot):
    """-> (char_names, char_imgs, loc_img, prop_imgs)"""
    chars, cimgs, loc, props = [], [], None, []
    kf = shot["kf"] or ""
    hint = kf[:60] + " " + shot["light"][:20]
    for tok in [t.strip() for t in (shot["refs"] or "").split(";")]:
        if not tok or tok == "—":
            continue
        m = re.match(r"(CH-\d{4})", tok)
        b = re.match(r"(B-\d\d)", tok)
        folder = None
        if b:
            folder = BMAP.get(b.group(1))
        elif m:
            folder = m.group(1)
        if folder:
            name = PMAP.get(folder)
            if folder == "CH-0004":  # Kes: hands / back
                f = pick(folder, "B08_hands_B" if "B" in tok.split("руки")[-1] and "руки" in tok else "B08_hands_A", "")
                if "руки" not in tok:
                    f = f"{REFS}/CH-0004/B08_back_v1.png"
                cimgs.append(f)
                continue
            fs = sorted(glob.glob(f"{REFS}/{folder}/*_00_master_v1.png")) or sorted(glob.glob(f"{REFS}/{folder}/*sheet*_v1.png")) \
                or sorted(glob.glob(f"{REFS}/{folder}/*.png"))
            if fs and fs[0] not in cimgs:
                cimgs.append(fs[0])
            if name and name not in chars:
                chars.append(name)
            continue
        c = re.match(r"C-0(\d)", tok)
        if c:
            n = c.group(1)
            fs = sorted(glob.glob(f"{REFS}/GROUPS/C0{n}_*.png"))
            fs = [f for f in fs if "emblem" not in f]
            if n == "3":
                fs = [f for f in fs if ("_B_" in f) == (" b" in tok)] or fs
            if n == "8" and fs:
                pass
            if fs:
                props.append(fs[0])
            continue
        e = re.match(r"(E-\d\d)", tok)
        if e and e.group(1) in EMAP:
            fs = sorted(glob.glob(f"{REFS}/{EMAP[e.group(1)]}/*.png"))
            if e.group(1) == "E-05":
                fs = [f for f in fs if ("small" in f) == ("малая" in tok)] or fs
            if e.group(1) == "E-12":
                fs = [f for f in fs if ("page-b" in f) == ("Фоссетт" in tok)] or fs
            if e.group(1) == "E-06":
                continue
            if fs:
                props.append(fs[0])
            continue
        d = re.match(r"(D-\d\d)\s*([A-Z]\d)?\s*(.*)", tok)
        if d and loc is None and d.group(1) in DMAP:
            pre = d.group(1).replace("-", "") + ("_" + d.group(2) if d.group(2) else "")
            loc = pick(DMAP[d.group(1)], pre, (d.group(3) or "") + " " + hint)
    if loc is None and not shot["nochar"] or (loc is None and shot["plan"] not in ("insert", "INSERT", "ECU")):
        d = re.search(r"(D-\d\d)\s*([A-Z]\d)?", shot["loc"] or "")
        if d and d.group(1) in DMAP:
            pre = d.group(1).replace("-", "") + ("_" + d.group(2) if d.group(2) else "")
            loc = pick(DMAP[d.group(1)], pre, hint)
    # PELL needs the turnaround when alone (side anchors)
    if chars == ["PELL"] and shot["plan"] not in ("ECU", "insert", "INSERT"):
        cimgs.append(f"{REFS}/CH-0001/A01_01_turnaround_v1.png")
    return chars, cimgs, loc, props


def expand(text):
    def rep(m):
        k = m.group(1)
        if k in LIGHT:
            return LIGHT[k]
        if k in ID:
            return ID[k].split(":")[0]
        return k
    return re.sub(r"\{([A-Z_]+)\}", rep, text or "")


def prompt_a(shot):
    chars, cimgs, loc, props = resolve(shot)
    imgs, legend = [], []
    for n, f in zip(chars + [None] * 9, cimgs):
        imgs.append(f)
        if n:
            legend.append(f"Image {len(imgs)} is the character reference sheet for {ID[n]} — copy face, hair, outfit and which side each asymmetric detail is on exactly.")
        else:
            legend.append(f"Image {len(imgs)} is a character/hands reference — match it.")
    for f in props[:2]:
        imgs.append(f)
        legend.append(f"Image {len(imgs)} is a reference for the prop or crowd type shown — match design and scale.")
    if loc:
        imgs.append(loc)
        legend.append(f"Image {len(imgs)} is the location plate — keep its architecture, palette and light, re-staged for this camera angle.")
    imgs = imgs[:5]
    body = expand(shot["kf"])
    chronicle = "{CHRONICLE}" in (shot["kf"] or "")
    p = ("Create ONE new single frame of a 2D anime TV episode (a finished background with characters, not a model sheet, "
         "no grid, no panels, no captions). " + " ".join(legend[:len(imgs)]) + " Shot: " + body.rstrip(". ") + ". ")
    if shot["nochar"]:
        p += "The frame is EMPTY of people: no figures, no characters, no faces anywhere (ignore any people in the reference images). "
    if chars:
        p += ("Characters are lit by the same light as the scene, colours no brighter than the surroundings, clean consistent anatomy. ")
    if "PELL" in chars:
        p += "Pell has exactly one braid; the blue tin tag is only on the braid tip, never on her jacket. "
    if "CORR" in chars:
        p += "Corr has no left hand: his left forearm ends in a leather-wrapped stump. "
    p += ("Leave any place for writing blank (no letters or numbers). " if re.search(r"ledger|map|label|page|number", body, re.I) else "")
    p += (LIGHT["CHRONICLE"] + ". Avoid: anime characters, cel shading, 3D, text, letters." if chronicle else STYLE + ". " + AVOID)
    return p, imgs


def prompt_b(shot):
    mot = shot["mot"] or shot["act"]
    return ("Image 1 is a frame from a 2D anime episode. Draw the SAME shot a few seconds later: same camera, framing, location, "
            "light, characters, faces, outfits and art style; change only the pose to the END of this action: " + expand(mot) +
            " Keep every asymmetric detail on the same side. No text. " + AVOID)


def jobs(scenes=None, which="a", only=None, force=False):
    out = []
    for s in shots():
        if scenes and s["scene"] not in scenes:
            continue
        if only and s["id"] not in only:
            continue
        if s["reuse"] or s["id"] in PLATE_DIRECT or s["id"] == "sc05-sh080" or s["id"] == "sc20-sh240":
            continue
        if which == "a":
            path = f"{FR}/{s['id']}_a.png"
            if os.path.exists(path) and not force:
                continue
            p, imgs = prompt_a(s)
            out.append((s["id"] + "_a", p, imgs))
        elif which == "b" and s["cls"] in "CD":
            path = f"{FR}/{s['id']}_b.png"
            src = f"{FR}/{s['id']}_a.png"
            if (os.path.exists(path) and not force) or not os.path.exists(src):
                continue
            out.append((s["id"] + "_b", prompt_b(s), [src]))
    return out


def run(js, workers=6):
    from pipeline import fal_client
    try:
        meta = json.load(open(META))
    except Exception:
        meta = {}

    def go(j):
        name, p, imgs = j
        seed = abs(hash(name)) % 900000 + 1000
        try:
            if imgs:
                r = fal_client.generate_image(p, f"{FR}/{name}.png", model="nano-banana-edit", reference_images=imgs,
                                              aspect_ratio="16:9", extra={"seed": seed})
            else:
                r = fal_client.generate_image(p, f"{FR}/{name}.png", model="nano-banana", aspect_ratio="16:9",
                                              extra={"seed": seed})
            return name, str(r), seed
        except Exception as e:
            return name, f"ERROR {type(e).__name__}: {str(e)[:200]}", seed
    with cf.ThreadPoolExecutor(workers) as ex:
        for (name, r, seed), j in zip(ex.map(go, js), js):
            print(name, r[-60:], flush=True)
            if not r.startswith("ERROR"):
                old = meta.get(name, {})
                meta[name] = dict(prompt=j[1], refs=[os.path.relpath(x, ROOT) for x in j[2]], seed=seed,
                                  model="nano-banana-edit" if j[2] else "nano-banana",
                                  attempt=old.get("attempt", 0) + 1)
                json.dump(meta, open(META, "w"), indent=1, ensure_ascii=False)
            if "BudgetExceeded" in r or "PaidCallsDisabled" in r or "Floor" in r:
                print("STOP: guard", r)
                os._exit(3)


def plates():
    """$0: plate/ref-plate shots get the accepted reference image; sc05-sh080 = all six panels; sc20-sh240 = black."""
    from PIL import Image
    os.makedirs(FR, exist_ok=True)
    for sid, rel in PLATE_DIRECT.items():
        dst = f"{FR}/{sid}_a.png"
        if not os.path.exists(dst):
            shutil.copy(f"{REFS}/{rel}", dst)
    dst = f"{FR}/sc05-sh080_a.png"
    if not os.path.exists(dst):
        ims = [Image.open(f"{REFS}/TAPESTRY/E06_panel{i}_v1.png").convert("RGB") for i in range(1, 7)]
        h = 900
        ims = [im.resize((int(im.width * h / im.height), h)) for im in ims]
        W = sum(im.width for im in ims) + 20 * 7
        canvas = Image.new("RGB", (W, h + 40), (24, 22, 20))
        x = 20
        for im in ims:
            canvas.paste(im, (x, 20))
            x += im.width + 20
        canvas.save(dst)
    dst = f"{FR}/sc20-sh240_a.png"
    if not os.path.exists(dst):
        Image.new("RGB", (1280, 720), (0, 0, 0)).save(dst)


def contact(scenes, tag=""):
    """Contact sheet per scene: every shot's frame(s) with id/class, for review."""
    from PIL import Image, ImageDraw
    out_dir = f"{ROOT}/studio/direction/animatic_contacts"
    os.makedirs(out_dir, exist_ok=True)
    allsh = shots()
    byid = {s["id"]: s for s in allsh}
    res = []
    for sc in scenes:
        cells = []
        for s in [x for x in allsh if x["scene"] == sc]:
            src = s["reuse"] or s["id"]
            for suf in ("a", "b"):
                f = f"{FR}/{src}_{suf}.png"
                if os.path.exists(f) and (suf == "a" or s["cls"] in "CD"):
                    if suf == "b" and s["reuse"]:
                        continue
                    lab = f"{s['id'][5:]} {s['cls']}{' kf=' + s['reuse'][5:] if s['reuse'] else ''}{' END' if suf == 'b' else ''}"
                    cells.append((f, lab))
        if not cells:
            continue
        W, H, cols = 384, 216, 5
        rows = (len(cells) + cols - 1) // cols
        sheet = Image.new("RGB", (W * cols, (H + 18) * rows), "white")
        d = ImageDraw.Draw(sheet)
        for i, (f, lab) in enumerate(cells):
            im = Image.open(f).convert("RGB")
            im.thumbnail((W, H))
            x, y = (i % cols) * W, (i // cols) * (H + 18)
            sheet.paste(im, (x, y))
            d.text((x + 3, y + H + 3), lab, fill="black")
        p = f"{out_dir}/{sc}{tag}.jpg"
        sheet.save(p, quality=72)
        res.append(p)
        print(p, len(cells))
    return res


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("rest", nargs="*")
    ap.add_argument("--scenes")
    ap.add_argument("--pass", dest="which", default="a")
    ap.add_argument("--only")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()
    sc = a.scenes.split(",") if a.scenes else None
    only = a.only.split(",") if a.only else None
    if a.cmd == "plan":
        ja = jobs(sc, "a", only, a.force)
        print("a-jobs", len(ja), "C/D end poses <=", sum(1 for s in shots() if s["cls"] in "CD" and not s["reuse"]))
        for n, p, imgs in ja[:int(os.environ.get("SHOW", "3"))]:
            print("---", n, [os.path.relpath(i, REFS) for i in imgs], "\n", p)
        print(f"est ${0.04 * len(ja):.2f}")
    elif a.cmd == "run":
        js = jobs(sc, a.which, only, a.force)
        print("jobs", len(js), f"est ${0.04 * len(js):.2f}", flush=True)
        run(js, a.workers)
    elif a.cmd == "plates":
        plates()
    elif a.cmd == "contact":
        contact(a.rest or sorted({s["scene"] for s in shots()}))
