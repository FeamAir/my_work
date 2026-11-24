#!/usr/bin/env python3
"""S1 OP: local $0 fixes on the accepted NB2 frames before Kling and assembly (acceptance 2026-11-24, report r7).

  python3 -I op_frame_fixes.py

Reads output/opening/frames/<id>[_tN].png, writes output/opening/frames/<id>_op.png (the file used by Kling and by the
edit) and a before/after sheet output/opening/frames/_fixes_check.png. Nothing is generated; no hflip of any frame
(OP-11): the one mirror below is local to the hand emblem of banner 5 and its spiral stone is pasted back unmirrored.

  F01   far-left horizon silhouettes (spiky skyline) painted out: nothing beyond the sea but sky (keeper, cut 01/25)
  F01a  the distant three-tower skyline on the left horizon painted out (a Spire group across the sea breaks OP-9 and
        the "nothing but sky" hook)
  F04   10 lanterns -> 9 (the rightmost one painted out); both background towers painted out (their grooves read "\",
        OP-4); the double door at the end of the lane painted out to plain wall (no gate, OP-2/OP-5)
  F10   four towers -> three (the left hill tower painted out: two on the hill, the left of them the tallest, the third
        low at the edge of the stilt-town, as the prompt and K07 ask); the small door in the dike's centre pier painted out
  F11   the light concentric rings around the piling feet painted out (no rings on water, OP-5)
  F14   the pseudo-handwriting on the right page softened to illegible scribble (OP-10); ruled lines kept soft
  F17   banner 4 (Lantry): the right pan was drawn with water; recoloured to empty copper (H07)
  F18   banner 5: the hand was a LEFT hand (thumb on the viewer's left, G3); the hand shape is mirrored locally inside
        the banner field and the original clockwise spiral stone is pasted back unmirrored in the palm; banner 9: the
        flame outline over the candle painted out (an unlit lantern)
  F19   two tiny figures on the terrace between the poles painted out (OP-1)
  F21   take 2 (take 1 had both points away from the pole, DEC-66, and a crowd): two figure pairs painted out (OP-1);
        the dark vertical divider line in the middle painted out (no split screen)
  F27   take 2: thin letterbox bars top and bottom cropped off, rescaled to 1376x768
  F28   take 2 accepted as is (take 1 had two big towers with "\" grooves)
"""
import os
import numpy as np
import cv2
from PIL import Image

FR = "/home/user/my_work/output/opening/frames"


def load(name):
    return np.asarray(Image.open(f"{FR}/{name}").convert("RGB")).copy()


def save(a, fid):
    Image.fromarray(a).save(f"{FR}/{fid}_op.png")


def inpaint(a, m, r=5):
    return cv2.inpaint(np.ascontiguousarray(a), (m > 0).astype(np.uint8) * 255, r, cv2.INPAINT_TELEA)


def box_mask(shape, boxes):
    m = np.zeros(shape[:2], np.uint8)
    for x0, y0, x1, y1 in boxes:
        m[y0:y1, x0:x1] = 1
    return m


def clone_fill(a, m, dx=0, dy=0):
    """fill mask m with a copy of the same image shifted by (dx, dy), Poisson-blended at the border."""
    src = np.roll(np.roll(a, -dx, axis=1), -dy, axis=0)
    P = 10
    dstp = cv2.copyMakeBorder(cv2.cvtColor(a, cv2.COLOR_RGB2BGR), P, P, P, P, cv2.BORDER_REFLECT)
    srcp = cv2.copyMakeBorder(cv2.cvtColor(src, cv2.COLOR_RGB2BGR), P, P, P, P, cv2.BORDER_REFLECT)
    mm = cv2.copyMakeBorder((m > 0).astype(np.uint8) * 255, P, P, P, P, cv2.BORDER_CONSTANT, value=0)
    ys, xs = np.nonzero(mm)
    x0, y0, x1, y1 = xs.min(), ys.min(), xs.max() + 1, ys.max() + 1
    out = cv2.seamlessClone(srcp[y0:y1, x0:x1], dstp, mm[y0:y1, x0:x1], ((x0 + x1) // 2, (y0 + y1) // 2), cv2.NORMAL_CLONE)
    return cv2.cvtColor(out, cv2.COLOR_BGR2RGB)[P:-P, P:-P]


def dark_silhouette(a, box, thr):
    """pixels in box darker than the local sky (median of the box's top rows) by > thr, dilated 3 px."""
    x0, y0, x1, y1 = box
    L = a.mean(2)
    sky = np.median(L[y0:y0 + 6, x0:x1])
    m = np.zeros(L.shape, np.uint8)
    m[y0:y1, x0:x1] = (L[y0:y1, x0:x1] < sky - thr).astype(np.uint8)
    return cv2.dilate(m, np.ones((7, 7), np.uint8))


def f01():
    a = load("F01.png")
    m = dark_silhouette(a, (0, 520, 118, 588), 30)
    save(inpaint(a, m, 6), "F01")


def f01a():
    a = load("F01a.png")
    m = dark_silhouette(a, (0, 445, 196, 592), 30)
    m[:, 196:] = 0
    save(inpaint(a, m, 6), "F01a")


def f04():
    a = load("F04.png")
    L = a.mean(2)
    m = box_mask(a.shape, [(1296, 196, 1350, 278)])           # the 10th (rightmost) lantern and its hook
    b = inpaint(a, m, 7).astype(float)
    # the two background towers: the fog sky between the net pole and the right-hand houses is rebuilt as a
    # per-row gradient taken from the clear sky strip left of the towers (x 805-835); rope and lanterns stay on top
    x0, x1, y1 = 696, 1000, 352
    grad = np.median(b[0:y1, 805:835], axis=1)                  # (rows, 3): the sky between the two towers
    grad = cv2.GaussianBlur(grad[:, None, :].astype(np.float32), (0, 0), 3)[:, 0, :]
    sky = np.repeat(grad[:, None, :], x1 - x0, axis=1)
    noise = cv2.GaussianBlur(np.random.default_rng(4).normal(0, 2.0, sky.shape[:2]).astype(np.float32), (0, 0), 1)
    sky = sky + noise[..., None]
    front = cv2.morphologyEx((L[0:y1, x0:x1] < 80).astype(np.uint8), cv2.MORPH_CLOSE, np.ones((17, 17), np.uint8))
    front = cv2.dilate(front, np.ones((3, 3), np.uint8)).astype(np.float32)
    front = cv2.GaussianBlur(front, (0, 0), 0.8)
    keep = np.clip(front, 0, 1)[..., None]
    # feather into the houses on the right and into the wall below
    fx = np.clip((x1 - np.arange(x0, x1)) / 18.0, 0, 1)[None, :, None]
    fy = np.clip((y1 - np.arange(0, y1)) / 10.0, 0, 1)[:, None, None]
    region = b[0:y1, x0:x1]
    houses = (L[0:y1, x0:x1] < 120) & (np.arange(x0, x1)[None, :] > 975)
    w = (1 - keep) * fx * fy * (1 - houses[..., None])
    b[0:y1, x0:x1] = region * (1 - w) + sky * w
    b = np.clip(b, 0, 255).astype(np.uint8)
    # the double door in the end wall -> the same rows of plain wall from the left (x 700-780), feathered
    wall = np.median(b[396:512, 700:780].astype(float), axis=1)
    m = np.zeros(b.shape[:2], np.float32)
    m[398:510, 786:900] = 1
    m = cv2.GaussianBlur(m, (0, 0), 3)[396:512, :, None]
    seg = b[396:512].astype(float)
    b[396:512] = np.clip(seg * (1 - m) + wall[:, None, :] * m, 0, 255).astype(np.uint8)
    save(b, "F04")


def f10():
    a = load("F10.png")
    m = dark_silhouette(a, (546, 54, 618, 206), 22)
    m[200:, :] = 0
    b = inpaint(a, m, 6)
    b = inpaint(b, box_mask(a.shape, [(680, 330, 699, 364)]), 3)                 # the door in the centre pier
    save(b, "F10")


def f11():
    a = load("F11.png")
    L = cv2.cvtColor(a, cv2.COLOR_RGB2GRAY)
    th = cv2.morphologyEx(L, cv2.MORPH_TOPHAT, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
    zone = np.zeros(L.shape, np.uint8)
    for cx, cy, ax, ay in ((255, 650, 215, 62), (1130, 650, 215, 62), (440, 550, 120, 34), (945, 550, 120, 34),
                           (537, 500, 70, 18), (852, 500, 70, 18)):
        cv2.ellipse(zone, (cx, cy), (ax, ay), 0, 0, 360, 1, -1)
    zone[:470] = 0
    m = cv2.dilate(((th > 7) & (zone > 0)).astype(np.uint8), np.ones((3, 3), np.uint8))
    save(inpaint(a, m, 4), "F11")


def f14():
    a = load("F14.png")
    soft = cv2.GaussianBlur(a, (0, 0), 2.4)
    m = np.zeros(a.shape[:2], np.float32)
    cv2.fillPoly(m, [np.array([(700, 255), (1080, 262), (1150, 668), (712, 668)], np.int32)], 1.0)
    m = cv2.GaussianBlur(m, (0, 0), 4)[..., None]
    save((a * (1 - m) + soft * m).astype(np.uint8), "F14")


def f17():
    a = load("F17.png").astype(float)
    # banner 4 (Lantry): the light water line on the RIGHT pan (x 819-836, y 349-355) -> the pan's own copper
    copper = np.median(a[356:360, 822:834].reshape(-1, 3), axis=0)
    reg = a[348:357, 818:838]
    sel = reg.mean(2) > copper.mean() + 12
    sel = cv2.dilate(sel.astype(np.uint8), np.ones((2, 2), np.uint8)).astype(bool)
    reg[sel] = copper
    a[348:357, 818:838] = cv2.GaussianBlur(reg.astype(np.float32), (0, 0), 0.6) * sel[..., None] + reg * (~sel[..., None])
    save(np.clip(a, 0, 255).astype(np.uint8), "F17")


def f18():
    a = load("F18.png")
    b = a.copy()
    x0, y0, x1, y1 = 650, 148, 732, 268          # inside the violet field of banner 5
    b[y0:y1, x0:x1] = a[y0:y1, x0:x1][:, ::-1]
    cx, cy, r = 694, 232, 13                     # the spiral stone in the palm (original, unmirrored)
    ncx = (x0 + x1 - 1) - cx                      # where the palm centre lands after the local mirror
    yy, xx = np.mgrid[-r:r + 1, -r:r + 1]
    disc = (np.hypot(xx, yy) <= r)
    patch = a[cy - r:cy + r + 1, cx - r:cx + r + 1]
    tgt = b[cy - r:cy + r + 1, ncx - r:ncx + r + 1]
    tgt[disc] = patch[disc]
    # banner 9: the flame outline over the candle -> plain linen pane
    b = inpaint(b, box_mask(a.shape, [(1229, 182, 1243, 201)]), 3)
    save(b, "F18")


def f19():
    a = load("F19.png")
    m = box_mask(a.shape, [(660, 616, 724, 702)])
    save(clone_fill(a, m, dx=-70), "F19")


def f21():
    a = load("F21_t2.png")
    b = clone_fill(a, box_mask(a.shape, [(528, 578, 594, 686)]), dx=78)
    b = clone_fill(b, box_mask(a.shape, [(1216, 578, 1284, 686)]), dx=64)
    L = b.mean(2)
    line = np.zeros(L.shape, np.uint8)
    line[:, 680:694] = (L[:, 680:694] < L[:, 672:676].mean(1, keepdims=True) - 25).astype(np.uint8)
    line = cv2.dilate(line, np.ones((3, 5), np.uint8))
    save(inpaint(b, line, 4), "F21")


def f27():
    a = Image.open(f"{FR}/F27_t2.png").convert("RGB")
    L = np.asarray(a.convert("L")).astype(float)
    rows = L.mean(1)
    top = int(np.argmax(rows > 25)) + 2
    bot = len(rows) - int(np.argmax(rows[::-1] > 25)) - 2
    h = bot - top
    w = round(h * 1376 / 768)
    x0 = (a.width - w) // 2
    a.crop((x0, top, x0 + w, bot)).resize((1376, 768), Image.LANCZOS).save(f"{FR}/F27_op.png")
    print("F27 crop rows", top, bot)


def f28():
    Image.open(f"{FR}/F28_t2.png").save(f"{FR}/F28_op.png")


def sheet():
    pairs = [("F01.png", "F01_op.png", (0, 480, 260, 620)), ("F01a.png", "F01a_op.png", (0, 420, 260, 620)),
             ("F04.png", "F04_op.png", (700, 0, 1376, 520)), ("F10.png", "F10_op.png", (500, 30, 860, 380)),
             ("F11.png", "F11_op.png", (60, 460, 1320, 720)), ("F14.png", "F14_op.png", (680, 230, 1180, 680)),
             ("F17.png", "F17_op.png", (760, 280, 860, 420)), ("F18.png", "F18_op.png", (620, 100, 1300, 300)),
             ("F19.png", "F19_op.png", (600, 580, 780, 720)), ("F21_t2.png", "F21_op.png", (480, 540, 1376, 720))]
    rows = []
    for a, b, box in pairs:
        A = Image.open(f"{FR}/{a}").convert("RGB").crop(box)
        B = Image.open(f"{FR}/{b}").convert("RGB").crop(box)
        s = 700 / A.width
        A, B = A.resize((700, round(A.height * s))), B.resize((700, round(B.height * s)))
        r = Image.new("RGB", (1400, A.height))
        r.paste(A, (0, 0))
        r.paste(B, (700, 0))
        rows.append(r)
    out = Image.new("RGB", (1400, sum(r.height for r in rows)))
    y = 0
    for r in rows:
        out.paste(r, (0, y))
        y += r.height
    out.save(f"{FR}/_fixes_check.png")


if __name__ == "__main__":
    for f in (f01, f01a, f04, f10, f11, f14, f17, f18, f19, f21, f27, f28):
        f()
    for fid in ("F15", "F23", "F26", "F30"):
        Image.open(f"{FR}/{fid}.png").save(f"{FR}/{fid}_op.png")   # accepted as generated
    sheet()
    print("ok")
