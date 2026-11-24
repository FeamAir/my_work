#!/usr/bin/env python3
"""Saga OP r19 ($0): keeper R8.2a on KW16 (the map clip, C11a-d).

  python3 -I op_saga_kw16_fix.py [OUT.mp4]      # default: output/opening/saga_c_build_v11/KW16_r19.mp4

1. the Sheaf mark's pennant (W16 ~x 885-925, y 250-275, red-brown like Rask's) -> ochre over earth-brown (OP-17, Dusk);
2. the letter-like squiggles in the reed hatching (W16 ~x 620-712, y 434-558, keeper E9) -> vertical strokes only:
   painted on the still (W16_r19_reeds.png, small dark components inpainted, outlines kept, short vertical strokes drawn)
   and carried into every frame as a warped difference W16_r19_reeds - W16.
   r19: OFF (REEDS = False). Kling redraws the hatching a little in every frame, so the warped difference leaves pale
   ghost strokes next to the clip's own (checked on frames 60-115) — worse than the keeper's Low item it fixes. The
   painted still stays for any later render; on screen the squiggles run 1.5 s inside a 1.6x crop (keeper: they read
   as reeds).
The map is a flat sheet and the clip only moves the camera, so W16 -> frame is tracked as an affine (ECC, chained frame to
frame from W16 itself), the two boxes are mapped into every frame and changed in place (the clip's own grade is kept).
Frame count and rate are unchanged (121 frames, 24/1). Writes a json log of the per-frame transforms next to the output.
"""
import json
import subprocess
import sys

import cv2
import numpy as np

ROOT = "/home/user/my_work"
SRC = f"{ROOT}/output/opening/saga_c/clips/KW16.mp4"
W16 = f"{ROOT}/output/opening/saga_c/frames/W16.png"
REEDS = False
W16R = f"{ROOT}/output/opening/saga_c/frames/W16_r19_reeds.png"   # op_saga_w16_reeds_r19.py: squiggles -> vertical strokes
OUT = sys.argv[1] if len(sys.argv) > 1 else f"{ROOT}/output/opening/saga_c_build_v11/KW16_r19.mp4"
PENNANT = (878, 244, 932, 282)        # x0, y0, x1, y1 in W16 (1376x768)


def main():
    cap = cv2.VideoCapture(SRC)
    frames = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        frames.append(f)
    h, w = frames[0].shape[:2]
    ref = cv2.resize(cv2.imread(W16), (w, h), interpolation=cv2.INTER_AREA)
    sx, sy = w / 1376, h / 768
    delta = (cv2.resize(cv2.imread(W16R), (w, h), interpolation=cv2.INTER_CUBIC).astype(np.float32) -
             cv2.resize(cv2.imread(W16), (w, h), interpolation=cv2.INTER_CUBIC).astype(np.float32))
    delta[np.abs(delta).max(-1) < 3] = 0
    small = lambda im: cv2.cvtColor(cv2.resize(im, (w // 2, h // 2)), cv2.COLOR_BGR2GRAY).astype(np.float32)
    rg = small(ref)
    warp = np.eye(2, 3, dtype=np.float32)
    crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 200, 1e-6)
    log, out = [], []
    for i, f in enumerate(frames):
        try:
            _, warp = cv2.findTransformECC(rg, small(f), warp, cv2.MOTION_AFFINE, crit, None, 5)
        except cv2.error as e:
            print("ECC failed on frame", i, e)
        A = warp.copy()
        A[:, 2] *= 2                                     # half-res translation -> full res
        log.append(A.tolist())
        g = f.copy()
        # 1) pennant: red-brown -> ochre over earth-brown
        x0, y0, x1, y1 = PENNANT
        pts = cv2.transform(np.array([[[x0 * sx, y0 * sy], [x1 * sx, y0 * sy], [x1 * sx, y1 * sy], [x0 * sx, y1 * sy]]],
                                     np.float32), A)[0]
        m = np.zeros((h, w), np.uint8)
        cv2.fillConvexPoly(m, pts.astype(np.int32), 255)
        hsv = cv2.cvtColor(g, cv2.COLOR_BGR2HSV).astype(np.float32)
        H_, S_, V_ = hsv[..., 0] * 2, hsv[..., 1] / 255, hsv[..., 2] / 255
        red = (m > 0) & ((H_ < 30) | (H_ > 340)) & (S_ > 0.38) & (V_ < 0.62)
        red = cv2.dilate(red.astype(np.uint8), np.ones((3, 3), np.uint8)) & (m > 0) & (S_ > 0.25) & (V_ < 0.7)
        hsv2 = hsv.copy()
        hsv2[..., 0] = np.where(red > 0, 40 / 2, hsv[..., 0])                        # ochre hue
        hsv2[..., 1] = np.where(red > 0, np.clip(S_ * 1.25, 0, 0.85) * 255, hsv[..., 1])
        hsv2[..., 2] = np.where(red > 0, np.clip(V_ * 1.22 + 0.04, 0, 0.78) * 255, hsv[..., 2])   # dark folds stay earth-brown
        g = cv2.cvtColor(hsv2.astype(np.uint8), cv2.COLOR_HSV2BGR)
        # 2) reeds: the painted difference, warped into the frame (off in r19, see the docstring)
        if not REEDS:
            out.append(g)
            continue
        # local refinement: Kling drifts the drawing a little; a translation-only ECC on the reed patch
        A2 = A.copy()
        c = A @ np.array([668 * sx, 496 * sy, 1.0])
        r = int(110 * float(np.sqrt(abs(np.linalg.det(A[:, :2])))))
        x0, y0, x1, y1 = int(c[0]) - r, int(c[1]) - r, int(c[0]) + r, int(c[1]) + r
        if x0 > 0 and y0 > 0 and x1 < w and y1 < h:
            tpl = cv2.cvtColor(cv2.warpAffine(ref, A, (w, h)), cv2.COLOR_BGR2GRAY)[y0:y1, x0:x1].astype(np.float32)
            cur = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY)[y0:y1, x0:x1].astype(np.float32)
            try:
                _, T = cv2.findTransformECC(tpl, cur, np.eye(2, 3, dtype=np.float32), cv2.MOTION_TRANSLATION, crit, None, 5)
                if abs(T[0, 2]) < 25 and abs(T[1, 2]) < 25:
                    A2[:, 2] += T[:, 2]
            except cv2.error:
                pass
        dw = cv2.warpAffine(delta, A2, (w, h), flags=cv2.INTER_LINEAR, borderValue=0)
        g = np.clip(g.astype(np.float32) + dw, 0, 255).astype(np.uint8)
        out.append(g)
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{w}x{h}", "-r", "24",
                          "-i", "-", "-c:v", "libx264", "-crf", "10", "-preset", "slow", "-pix_fmt", "yuv420p", "-r", "24", OUT],
                         stdin=subprocess.PIPE)
    for g in out:
        p.stdin.write(g.tobytes())
    p.stdin.close()
    p.wait()
    json.dump({"src": SRC, "frames": len(out), "affine_W16_to_frame": log}, open(OUT.rsplit(".", 1)[0] + ".json", "w"))
    print(OUT, len(out), "frames; scale first/last", round(float(np.sqrt(abs(np.linalg.det(np.array(log[0])[:, :2])))), 4),
          round(float(np.sqrt(abs(np.linalg.det(np.array(log[-1])[:, :2])))), 4))


if __name__ == "__main__":
    main()
