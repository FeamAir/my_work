#!/usr/bin/env python3
"""S1 OP, keeper review R3 (lore-op-2026-11-24.md §R3): the $0 fixes before K13 and the v2 rebuild. Local only.

  python3 -I op_r3_fixes.py [plates] [stills] [k07] [k18] [k13]      (no argument = all; k13 needs clips/K13.mp4)

Every input is first copied once to <name>_preR3.<ext> and always read from that copy, so the script is idempotent.

  plates  R3.1 (optional, done before K13): the inpaint smudge beside the upper lamp of the left pier
          (plate x 147-181, y 218-247) is replaced by the plain water (H1) / fog (H2) beside it (Poisson clone);
          the dark lamp body (x 155-164, y 228-244) is kept.
  stills  R3.2-2 F18, F23: every border strip (top, bottom, left, right) is mirrored on its own, inside its own
          bounds, left-right (top/bottom along the strip, sides across it about their spirals' centre line, fringe
          kept): every spiral turns sunwise (clockwise from the centre outward, as H16);
          the field is untouched, no whole-frame flip (OP-11).
          R3.2-6 F18: the keep tower (crenellated, windows) -> a Spire in flat woven colour: smooth black tapering
          cone, a ring of open arches on top, grooves "/" on the near side; same place and size.
          R3.2-3 F10: the dark span between the two centre pilasters is rebuilt as plain brick from the neighbour
          span, the light jet and mist under it -> plain ground (the same rows 70 px to the left).
  k07     R3.2-3 on the clip K07 (cut 10): the same rebuild, tracked per frame (ORB similarity to frame 12 on the
          dike), patched in reference geometry and warped back with a feathered mask -> clips/K07_fix.mp4.
  k18     R3.2-7 on the clip K18 (cut 26): the warm halo on the wall around the two near wall lamps (source
          x 474-492 / 1473-1493, y 464-496) is graded down to the wall tone: a per-channel gain (wall low-pass
          inpainted inward from the ring r 54-60, over the low-pass of the median frame, glass excluded, <= 1) is
          applied to every frame; the glass stays lit (OP-3: small live lamps allowed) -> clips/K18_fix.mp4.
  k13     R3.1-2 on the paid clip K13: Kling lit the six lamps -> static patch of the H1 lamp heads (see k13()).
A before/after sheet: output/opening/frames/_r3_check.png.
"""
import os
import shutil
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw

OUTD = "/home/user/my_work/output/opening"
FR, CL, PL = f"{OUTD}/frames", f"{OUTD}/clips", f"{OUTD}/plates"
TMP = f"{OUTD}/build_work/r3"


def orig(path):
    b, e = os.path.splitext(path)
    o = f"{b}_preR3{e}"
    if not os.path.exists(o):
        shutil.copy2(path, o)
    return o


def rgb(path):
    return np.asarray(Image.open(path).convert("RGB")).copy()


def clone(a, m, dx=0, dy=0):
    """fill mask m with the same image shifted by (dx, dy) (pixel (x,y) <- (x+dx, y+dy)), Poisson-blended."""
    src = np.roll(np.roll(a, -dx, axis=1), -dy, axis=0)
    P = 12
    d = cv2.copyMakeBorder(cv2.cvtColor(a, cv2.COLOR_RGB2BGR), P, P, P, P, cv2.BORDER_REFLECT)
    s = cv2.copyMakeBorder(cv2.cvtColor(src, cv2.COLOR_RGB2BGR), P, P, P, P, cv2.BORDER_REFLECT)
    mm = cv2.copyMakeBorder((m > 0).astype(np.uint8) * 255, P, P, P, P, cv2.BORDER_CONSTANT, value=0)
    ys, xs = np.nonzero(mm)
    x0, y0, x1, y1 = xs.min(), ys.min(), xs.max() + 1, ys.max() + 1
    out = cv2.seamlessClone(s[y0:y1, x0:x1], d, mm[y0:y1, x0:x1], ((x0 + x1) // 2, (y0 + y1) // 2), cv2.NORMAL_CLONE)
    return cv2.cvtColor(out, cv2.COLOR_BGR2RGB)[P:-P, P:-P]


def box(shape, x0, y0, x1, y1):
    m = np.zeros(shape[:2], np.uint8)
    m[y0:y1, x0:x1] = 1
    return m


# ------------------------------------------------------------------------------------------------ plates ---
def plates():
    for t in ("H1", "H2"):
        p = f"{PL}/D09_{t}_op.png"
        a = rgb(orig(p))
        if t == "H1":       # water both sides: right <- 28 px above, then the grey gap hull..lamp <- that clean water
            b = clone(a, box(a.shape, 164, 218, 181, 247), 0, -28)
            b = clone(b, box(a.shape, 147, 218, 156, 247), 20, 0)
        else:               # fog: the light blob right of the lamp <- the fog 22 px further right
            b = clone(a, box(a.shape, 164, 220, 181, 246), 22, 0)
        b[228:245, 155:164] = a[228:245, 155:164]           # the lamp body itself stays
        Image.fromarray(b).save(p)
        print("plate", t, "spot cleaned")


# ------------------------------------------------------------------------------------------------ stills ---
def flip_border(a, top, bot, left, right, edge=(0, 0, 12, 12)):
    """Mirror each border strip on its own, left-right, inside its own bounds. Top and bottom strips (corners
    included) are flipped along their length; the side strips across their width about the centre line of their
    spirals (dark-pixel centroid), with the fringe (edge px) left alone, so the side spirals stay at their heights
    and meet the corners as before. top/bot/left/right = band thickness in px."""
    h, w = a.shape[:2]
    b = a.copy()
    L = a.mean(2)

    def axis_flip(lo, hi, prof, ax):
        idx = np.arange(lo, hi)
        wgt = prof[lo:hi]
        c = float((idx * wgt).sum() / max(wgt.sum(), 1))
        r = int(min(c - lo, hi - 1 - c))
        c0 = int(round(c - r))
        sl = slice(c0, c0 + 2 * r + 1)
        return sl

    dark = (L < 90).astype(float)
    b[:top] = a[:top, ::-1]                  # top and bottom: left-right along the strip (edge lines run along it)
    b[h - bot:] = a[h - bot:, ::-1]
    sl = axis_flip(edge[2], left, dark[top:h - bot].sum(0), 1)
    b[top:h - bot, sl] = a[top:h - bot, sl][:, ::-1]
    sl = axis_flip(w - right, w - edge[3], dark[top:h - bot].sum(0), 1)
    b[top:h - bot, sl] = a[top:h - bot, sl][:, ::-1]
    return b


def spire(a):
    """F18: the keep tower (x 722-764, y 386-505) -> a Spire in flat woven colour, same place and size."""
    h, w = a.shape[:2]
    b = a.astype(float)
    # 1) paint the old tower out above y 482 where the new cone does not cover it: its dark pixels (the heads and
    #    capes of the figures are left of x 718 / below y 490) <- linen tiled from the clean area left of it
    tex = b[388:446, 668:718]
    tile = np.concatenate([tex, tex[::-1]], 0)
    tile = np.concatenate([tile, tile[:, ::-1]], 1)
    X0, Y0, X1, Y1 = 718, 383, 768, 482
    reg = np.tile(tile, (3, 2, 1))[:Y1 - Y0, :X1 - X0]
    old = b[Y0:Y1, X0:X1]
    m = (old.mean(2) < 110).astype(np.uint8)
    m = cv2.dilate(m, np.ones((5, 5), np.uint8)).astype(np.float32)
    m = cv2.GaussianBlur(m, (0, 0), 0.8)[..., None]
    b[Y0:Y1, X0:X1] = old * (1 - m) + reg * m
    # the wider old base (y 482-506) sticks out right of the cone: x 758-768 only (the red cape is left of x 736)
    old = b[482:506, 758:768]
    m = cv2.dilate((old.mean(2) < 110).astype(np.uint8), np.ones((3, 3), np.uint8)).astype(np.float32)[..., None]
    b[482:506, 758:768] = old * (1 - m) + np.tile(tile, (1, 1, 1))[:24, :10] * m
    weave_src = np.tile(tile, (3, 2, 1))
    # 2) the Spire, drawn at 4x and reduced: cone from y 505 (half-width 21) to y 404 (half-width 11),
    #    a crown band y 389-404 (half-width 13) with three open arches, a thin cap; grooves "/" on the face
    S = 4
    cx, yb, yt, hb, ht = 743, 506, 404, 21, 11
    cw, ch = 60, 130
    ox, oy = cx - cw // 2, 384
    big = Image.new("L", (cw * S, ch * S), 0)
    grv = Image.new("L", (cw * S, ch * S), 0)
    arch = Image.new("L", (cw * S, ch * S), 0)
    out = Image.new("L", (cw * S, ch * S), 0)
    d, dg, da, do = ImageDraw.Draw(big), ImageDraw.Draw(grv), ImageDraw.Draw(arch), ImageDraw.Draw(out)
    P = lambda x, y: ((x - ox) * S, (y - oy) * S)
    cone = [P(cx - hb, yb), P(cx - ht, yt), P(cx + ht, yt), P(cx + hb, yb)]
    crown = [P(cx - 13, 404), P(cx - 13, 391), P(cx + 13, 391), P(cx + 13, 404)]
    cap = [P(cx - 14, 391), P(cx - 9, 387), P(cx + 9, 387), P(cx + 14, 391)]
    for poly in (cone, crown, cap):
        d.polygon(poly, fill=255)
        do.line(poly + [poly[0]], fill=255, width=S * 2)
    for ax in (-8, 0, 8):                                   # three open arches (round heads), linen shows through
        x0, x1 = cx + ax - 2.6, cx + ax + 2.6
        da.rectangle([P(x0, 396.5), P(x1, 402.5)], fill=255)
        da.ellipse([P(x0, 393.5), P(x1, 399.5)], fill=255)
    for k in range(-6, 9):                                  # grooves rising lower-left -> upper-right ( / )
        y0 = yb - 4 + k * 13
        dg.line([P(cx - hb - 2, y0), P(cx + hb + 2, y0 - 16)], fill=255, width=int(S * 1.3))
    red = lambda im: cv2.resize(np.asarray(im, np.float32) / 255, (cw, ch), interpolation=cv2.INTER_AREA)
    body, gro, arc, edge = red(big), red(grv), red(arch), red(out)
    gro *= red(Image.fromarray((np.asarray(big) > 0).astype(np.uint8) * 255).crop((0, 0, cw * S, ch * S)))
    gro[:404 - oy + 1] = 0                                  # no grooves on the crown
    reg = b[oy:oy + ch, ox:ox + cw]
    # flat woven colours: body near-black, grooves a dull dark grey (no light), outline darker; weave kept
    weave = weave_src[:ch, :cw].mean(2)
    weave = ((weave - cv2.GaussianBlur(weave, (0, 0), 2)) * 0.5)[..., None]       # linen weave, not old bricks
    col_body = np.array([38, 37, 40.0])
    col_gro = np.array([70, 68, 72.0])
    col_edge = np.array([22, 21, 24.0])
    paint = col_body + gro[..., None] * (col_gro - col_body)
    paint = paint * (1 - edge[..., None] * 0.6) + col_edge * edge[..., None] * 0.6
    paint = paint + weave
    alpha = np.clip(body - arc, 0, 1)
    # the figure cape over the lower left of the tower stays in front (the original occluders: not linen, not tower)
    Lr = reg.mean(2)
    front = np.zeros(Lr.shape, np.float32)
    front[108:, :24] = (Lr[108:, :24] > 70) & (Lr[108:, :24] < 205) & (np.abs(reg[108:, :24, 0] - reg[108:, :24, 2]) > 28)
    front = cv2.dilate(front, np.ones((3, 3), np.uint8))
    # the woven sea and mound under the old tower (y >= 497) stay; the cone sits on them
    alpha[506 - oy:] = 0
    alpha = alpha * (1 - front)
    b[oy:oy + ch, ox:ox + cw] = reg * (1 - alpha[..., None]) + paint * alpha[..., None]
    return np.clip(b, 0, 255).astype(np.uint8)


def dike_patch(a, s=1.0, ox=0.0, oy=0.0):
    """K07/F10 dike: geometry in K07 frame-12 coordinates (1928x1072), mapped by x' = ox + s*x. Straight copies
    (1 px feather), no Poisson: the dark pilaster shadows must not bleed back in."""
    T = lambda x, y: (int(round(ox + s * x)), int(round(oy + s * y)))
    b = a.astype(np.float32)
    for (x0, y0, x1, y1, dx) in ((950, 412, 981, 507, -46), (936, 500, 994, 524, 62)):
        (X0, Y0), (X1, Y1) = T(x0, y0), T(x1, y1)
        d = int(round(dx * s))
        m = cv2.GaussianBlur(box(a.shape, X0, Y0, X1, Y1).astype(np.float32), (0, 0), 0.9)[..., None]
        b = b * (1 - m) + np.roll(b, -d, axis=1) * m
    return np.clip(b, 0, 255).astype(np.uint8)


def stills():
    for fid, bands in (("F18", (55, 55, 52, 47)), ("F23", (57, 58, 60, 55))):
        p = f"{FR}/{fid}_op.png"
        a = flip_border(rgb(orig(p)), *bands)
        if fid == "F18":
            a = spire(a)
        Image.fromarray(a).save(p)
        print(fid, "borders mirrored per strip" + (", Spire drawn" if fid == "F18" else ""))
    p = f"{FR}/F10_op.png"
    a = rgb(orig(p))
    s = 1376 / 1928
    Image.fromarray(dike_patch(a, s, 0, 0)).save(p)
    print("F10 span + jet rebuilt")


# ------------------------------------------------------------------------------------------------- clips ---
def frames_of(path):
    cap = cv2.VideoCapture(path)
    fr = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        fr.append(cv2.cvtColor(f, cv2.COLOR_BGR2RGB))
    return fr


def write(frames, path):
    h, w = frames[0].shape[:2]
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
                          "-r", "24", "-i", "-", "-c:v", "libx264", "-preset", "slow", "-crf", "12",
                          "-pix_fmt", "yuv420p", path], stdin=subprocess.PIPE)
    for f in frames:
        p.stdin.write(np.ascontiguousarray(f).tobytes())
    p.stdin.close()
    if p.wait():
        sys.exit(f"ffmpeg failed on {path}")


def k07():
    fr = frames_of(orig(f"{CL}/K07.mp4"))
    ref = fr[12]
    orb = cv2.ORB_create(3000)
    roi = np.zeros(ref.shape[:2], np.uint8)
    roi[330:620, 560:1400] = 255
    g = lambda f: cv2.cvtColor(f, cv2.COLOR_RGB2GRAY)
    kr, dr = orb.detectAndCompute(g(ref), roi)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    fixed = dike_patch(ref)
    mref = np.zeros(ref.shape[:2], np.float32)
    mref[404:560, 926:1004] = 1
    mref = cv2.GaussianBlur(mref, (0, 0), 3)
    out, log = [], []
    for i, f in enumerate(fr):
        if i == 12:
            M = np.array([[1, 0, 0], [0, 1, 0]], np.float64)
        else:
            kf, df = orb.detectAndCompute(g(f), None)
            mt = bf.match(dr, df)
            src = np.float32([kr[m.queryIdx].pt for m in mt])
            dst = np.float32([kf[m.trainIdx].pt for m in mt])
            M, inl = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=2.0)
        h, w = f.shape[:2]
        Minv = cv2.invertAffineTransform(M)
        fr_ref = cv2.warpAffine(f, Minv, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
        pat = dike_patch(fr_ref)
        back = cv2.warpAffine(pat, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
        mk = cv2.warpAffine(mref, M, (w, h))[..., None]
        out.append((f * (1 - mk) + back * mk).astype(np.uint8))
        log.append((i, round(float(np.hypot(*M[:, 0])), 4), round(float(M[0, 2]), 1), round(float(M[1, 2]), 1)))
    write(out, f"{CL}/K07_fix.mp4")
    print("K07 tracked (i, scale, tx, ty):", log[::20])
    for i in (12, 48, 84):
        Image.fromarray(np.concatenate([fr[i][380:580, 860:1100], out[i][380:580, 860:1100]], 1)).save(f"{TMP}/k07_{i}.png")


def k18():
    fr = frames_of(orig(f"{CL}/K18.mp4"))
    med = np.median(np.stack(fr[::6]), 0).astype(np.float32)
    h, w = med.shape[:2]
    gain = np.ones_like(med)
    for (gx0, gy0, gx1, gy1) in ((472, 462, 494, 497), (1471, 465, 1495, 498)):
        cx, cy, R = (gx0 + gx1) / 2, (gy0 + gy1) / 2, 72
        X0, Y0, X1, Y1 = int(cx - R), int(cy - R), int(cx + R), int(cy + R)
        reg = med[Y0:Y1, X0:X1]
        yy, xx = np.mgrid[Y0:Y1, X0:X1]
        rr = np.hypot(xx - cx, yy - cy)
        inbox = (xx >= gx0 - 2) & (xx < gx1 + 2) & (yy >= gy0 - 2) & (yy < gy1 + 2)
        glass = (inbox & (reg.mean(2) > 120)).astype(np.uint8)
        glass = cv2.dilate(glass, np.ones((3, 3), np.uint8)).astype(np.float32)
        wgt = cv2.GaussianBlur(1 - glass, (0, 0), 5) + 1e-4
        smooth = cv2.GaussianBlur(reg * (1 - glass)[..., None], (0, 0), 5) / wgt[..., None]
        # the wall without the halo: the low-pass inpainted inward from the ring r 54-60 (TELEA)
        hole = (rr < 54).astype(np.uint8) * 255
        bg = cv2.inpaint(np.clip(smooth, 0, 255).astype(np.uint8), hole, 18, cv2.INPAINT_TELEA).astype(np.float32)
        bg = cv2.GaussianBlur(bg, (0, 0), 4)
        ratio = np.clip((bg + 1) / (smooth + 1), 0.25, 1.0)
        fall = np.clip((60 - rr) / 10, 0, 1) * (1 - cv2.GaussianBlur(glass, (0, 0), 1.0))
        gain[Y0:Y1, X0:X1] = 1 - fall[..., None] + fall[..., None] * ratio
    out = [np.clip(f.astype(np.float32) * gain, 0, 255).astype(np.uint8) for f in fr]
    write(out, f"{CL}/K18_fix.mp4")
    Image.fromarray(np.concatenate([np.concatenate([fr[24][400:560, 400:570], out[24][400:560, 400:570]], 1),
                                    np.concatenate([fr[24][400:560, 1400:1570], out[24][400:560, 1400:1570]], 1)], 0)
                    ).save(f"{TMP}/k18_24.png")
    print("K18 halo graded out")


def k13():
    """R3.1-2: Kling lit the six pier lamps of K13 (from frame ~10). Static patch: every lamp head (+cap, collar)
    is taken from the H1 plate (lamps dark) on all frames; around it (r <= 3.2 R, and the pier-top glow boxes of
    op_harbour_plates.GLOWS) the warm low-frequency excess over the plate is removed (only darkening), so the
    waves keep moving and no glow is left on the water or the pier tops -> clips/K13_fix.mp4."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from op_harbour_plates import LAMPS, GLOWS
    fr = frames_of(f"{CL}/K13.mp4")
    h, w = fr[0].shape[:2]
    plate = cv2.resize(rgb(f"{PL}/D09_H1_op.png"), (w, h), interpolation=cv2.INTER_LANCZOS4).astype(np.float32)
    sx, sy = w / 1018, h / 572
    head = np.zeros((h, w), np.float32)
    zone = np.zeros((h, w), np.float32)
    yy, xx = np.mgrid[0:h, 0:w]
    for cx, cy, hw, hh in LAMPS:
        X, Y = cx * sx, cy * sy
        HW, HH = (hw + 2.5) * sx, (hh + 3.5) * sy
        head = np.maximum(head, ((np.abs(xx - X) <= HW) & (np.abs(yy - Y) <= HH)).astype(np.float32))
        R = (10 + 2 * max(hw, hh)) * sx
        zone = np.maximum(zone, np.clip((3.2 * R - np.hypot(xx - X, yy - Y)) / (0.6 * R), 0, 1))
    for x0, y0, x1, y1 in GLOWS:
        zone[int(y0 * sy):int(y1 * sy), int(x0 * sx):int(x1 * sx)] = 1
    for x0, y0, x1, y1 in ((0, 840, 34, 920), (1880, 580, 1920, 660)):   # two more lamps cut by the frame edges
        head[y0:y1, x0:x1] = 1
    zone = cv2.GaussianBlur(zone, (0, 0), 4)[..., None]
    head = cv2.GaussianBlur(cv2.dilate(head, np.ones((3, 3), np.uint8)), (0, 0), 1.0)[..., None]
    plo = cv2.GaussianBlur(plate, (0, 0), 6)
    out = []
    for f in fr:
        f = f.astype(np.float32)
        excess = np.clip(cv2.GaussianBlur(f, (0, 0), 6) - plo, 0, None)
        warm = np.clip(excess[..., 0:1] - excess[..., 2:3], 0, None) / (excess[..., 0:1] + 1)   # only warm light
        g = f - excess * zone * np.clip(warm * 3, 0, 1)
        g = g * (1 - head) + plate * head
        out.append(np.clip(g, 0, 255).astype(np.uint8))
    write(out, f"{CL}/K13_fix.mp4")
    for i in (0, 60, 120):
        Image.fromarray(np.concatenate([fr[i], out[i]], 0)[::2, ::2]).save(f"{TMP}/k13_{i}.png")
    print("K13 lamp heads patched from H1, warm glow removed")


def sheet():
    rows = []
    for name, bx in (("F18_op.png", (0, 0, 700, 200)), ("F18_op.png", (660, 370, 840, 540)), ("F23_op.png", (0, 0, 700, 200)),
                     ("F10_op.png", (620, 260, 760, 420))):
        A = Image.open(f"{FR}/{name[:-4]}_preR3.png").convert("RGB").crop(bx)
        B = Image.open(f"{FR}/{name}").convert("RGB").crop(bx)
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
    out.save(f"{FR}/_r3_check.png")


if __name__ == "__main__":
    os.makedirs(TMP, exist_ok=True)
    todo = sys.argv[1:] or ["plates", "stills", "k07", "k18", "k13"]
    for t in todo:
        globals()[t]()
    if "stills" in todo:
        sheet()
    print("ok")
