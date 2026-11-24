#!/usr/bin/env python3
"""Contact sheets of the style-C saga OP takes ($0): every take of steps L, R, N with its 168x94 thumbnail;
accepted takes framed green, others grey. Out: output/opening/contact_saga_c/contact_r16_{L,R,N}*.jpg
  python3 -I studio/direction/opening/tools/op_saga_contact_c.py"""
import glob, json, os, re
from PIL import Image, ImageDraw

ROOT = "/home/user/my_work"
OUT = f"{ROOT}/output/opening/saga_c"
DST = f"{ROOT}/output/opening/contact_saga_c"
TW, TH = 456, 256          # cell image (16:9)
st = json.load(open(f"{OUT}/state.json"))["accepted"]


def cells(paths):
    res = []
    for p in paths:
        m = re.match(r"(.+)_t(\d+)\.png$", os.path.basename(p))
        if not m:
            continue
        fid, take = m.group(1), m.group(2)
        res.append((fid, take, p, st.get(fid) == take))
    return res


def sheet(name, items, cols=4):
    rows = (len(items) + cols - 1) // cols
    W, H = cols * (TW + 12) + 12, rows * (TH + 130) + 12
    s = Image.new("RGB", (W, H), (18, 18, 20))
    d = ImageDraw.Draw(s)
    for k, (fid, take, p, ok) in enumerate(items):
        x, y = 12 + (k % cols) * (TW + 12), 12 + (k // cols) * (TH + 130)
        im = Image.open(p).convert("RGB")
        s.paste(im.resize((TW, TH), Image.LANCZOS), (x, y))
        s.paste(im.resize((168, 94), Image.LANCZOS), (x, y + TH + 6))
        d.rectangle([x - 3, y - 3, x + TW + 2, y + TH + 2], outline=(60, 200, 90) if ok else (90, 90, 90), width=3)
        d.text((x + 178, y + TH + 10), f"{fid}  take {take}", fill=(255, 255, 255))
        d.text((x + 178, y + TH + 28), "ACCEPTED" if ok else "not accepted", fill=(60, 200, 90) if ok else (170, 170, 170))
    s.save(f"{DST}/{name}.jpg", quality=86)
    print(f"{DST}/{name}.jpg", len(items))


os.makedirs(DST, exist_ok=True)
logo = cells(sorted(glob.glob(f"{OUT}/logo/LOGO_C_t*.png")))
sheet("contact_r16_L_logo", logo, cols=3)
fr = cells(sorted(glob.glob(f"{OUT}/frames/*_t*.png")))
rr = [c for c in fr if c[0].endswith("_C")]
nn = [c for c in fr if not c[0].endswith("_C")]
sheet("contact_r16_R", rr)
for i in range(0, len(nn), 16):
    sheet(f"contact_r16_N{i // 16 + 1}", nn[i:i + 16])
