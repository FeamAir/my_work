#!/usr/bin/env python3
"""Saga OP run, storyboard v2.3/v2.4, style C (SAGA_OP_storyboard.md §5, §6, §8.3, §9). PAID only with the studio
director's permission; `show`, `check`, `accept`, `pick`, `peaks` cost $0.

  python3 -I op_saga_run.py show                 # every prompt, negative and image order of every step ($0)
  python3 -I op_saga_run.py show T               # one step: T (test) | L (logo) | R (re-render) | N (new) | K (Kling)
  python3 -I op_saga_run.py show W11 KA01        # single items
  python3 -I op_saga_run.py check                # only the text checks against the board ($0)
  STUDIO_ALLOW_PAID=1 python3 -I op_saga_run.py run T [IDS...] [--take N]
  python3 -I op_saga_run.py pick with|without    # the coordinator's pick after step T (§5.2)
  python3 -I op_saga_run.py accept ID TAKE       # record an accepted take; it is skipped from then on
  python3 -I op_saga_run.py peaks CLIP           # action peaks of an accepted clip for the beat windows (§4.6)

Texts: every prompt block and content text is read from the storyboard at run time (so the call is what the board
says); the v1.4 texts that the board cites as "verbatim" are held here (from op_paid_run.py v1.4) with the v2.4
edits, and every held text is checked to appear in the board or in op_paid_run.py. `show` fails if any check fails.

Seeds (NB2): fixed per frame (board tables); take N uses seed + 1000 * (N - 1). T1 / T2 use the production seeds of
D01_A_C / W11 on purpose: the picked T image IS take 1 of that frame, so steps R / N start those two at take 2
(seed + 1000) and never re-send the same seed with the same prompt. LOGO_C: takes 1-3 = seeds 410801-410803 (§5.3).
Kling 2.5 TP on fal takes no seed: a retake is a new sample (take N file name only).

Budget (§8.3): each step runs under its own cumulative ceiling: T 65.79, L 66.03 (67.35 if step R has run),
R 67.35, N 69.39, K 84.50; the lower of that and a hand-set BUDGET_LIMIT_USD is used; a BUDGET_LIMIT_USD above
84.50 is refused. Every call goes through pipeline.fal_client -> costs.guard (permission, limit, $20 fal floor)
and costs.log (output/costs.jsonl); the script also checks the step ceiling itself before each call.
"""
import argparse
import json
import os
import re
import shutil
import sys
import time

ROOT = "/home/user/my_work"
sys.path.insert(0, ROOT)
sys.path.insert(0, f"{ROOT}/studio/art/style_c")
os.chdir(ROOT)
from style_base_c import NEGATIVE_C, STYLE_BASE_C  # noqa: E402

BOARD_PATH = f"{ROOT}/studio/direction/opening/SAGA_OP_storyboard.md"
V14_PATH = f"{ROOT}/studio/direction/opening/tools/op_paid_run.py"
REF = "studio/direction/refs"
OPF = "output/opening/frames"
OUT = "output/opening/saga_c"
STATE = f"{OUT}/state.json"
NB2_USD, KLING_USD = 0.08, 0.35

LOG_AT_PLAN = 65.4651
STEP_LIMITS = {"T": 65.79, "L": 66.03, "R": 67.35, "N": 69.39, "K": 84.50}
L_AFTER_R = 67.35
HARD_CAP = 84.50

BOARD = open(BOARD_PATH, encoding="utf-8").read()
V14 = open(V14_PATH, encoding="utf-8").read()
CHECKS = []          # (ok, message)
V14_FLAT = re.sub(r'"\s*\n\s*"', "", V14)     # op_paid_run.py with its split string literals joined


def v14_has(t):
    return t in V14_FLAT


def chk(ok, msg):
    CHECKS.append((bool(ok), msg))
    return ok


# ------------------------------------------------------------------ board parsing
def block(name):
    m = re.search(r"^`\{" + name + r"\}`[^\n]*?(?: = |=\n|:\n)`([^`]*)`", BOARD, re.M)
    chk(m, f"block {{{name}}} found in the board")
    return m.group(1) if m else f"<{name} MISSING>"


def rx(pattern, what):
    m = re.search(pattern, BOARD, re.M)
    chk(m, f"{what} found in the board")
    return m.group(1) if m else f"<{what} MISSING>"


def row(rid):
    """Cells of the table row whose first cell is `rid` or `**rid**` (optionally followed by a label)."""
    pat = r"^\| (?:\*\*)?" + re.escape(rid) + r"(?:\*\*)?(?: [^|]*)? \|(.*)$"
    m = re.search(pat, BOARD, re.M)
    chk(m, f"table row {rid} found")
    return [c.strip() for c in m.group(1).split(" | ")] if m else []


def span(cell, i=0):
    s = re.findall(r"`([^`]*)`", cell)
    return s[i] if len(s) > i else "<MISSING>"


SPIRE = ("the towers are smooth glassy black stone cones, each crowned by a ring of open arches, with deep spiral grooves "
         "winding up the whole height; on the near side of each tower the grooves rise from lower-left to upper-right "
         "( / ); the grooves are dark, nothing lights up; the foot of each tower is dark unlit stone")
chk(v14_has(SPIRE), "SPIRE = v1.4 §5 verbatim (op_paid_run.py)")

C_NOTE = block("C_NOTE")
SIGNATURE_C = block("SIGNATURE_C")
PHONE = block("PHONE")
RR = block("RR")
RR_169 = block("RR_169")
AVOID_OP = block("AVOID_OP")
AVOID_MASS = block("AVOID_MASS")
VSAFE = block("VSAFE")
VSAFE_MASS = block("VSAFE_MASS")
FLOW = block("FLOW")
SAGA_SAFE = block("SAGA_SAFE")
NEGATIVE_C_LOGO = rx(r"`\{NEGATIVE_C_LOGO\}` \([^)]*\) = `([^`]*)`", "{NEGATIVE_C_LOGO}")
ANCHOR_INTRO = rx(r"Every prompt opens with: `([^`]*)`", "C_ANCHOR intro sentence")
PRE_ACT = rx(r"\*\*Action prefix C\*\* = `([^`]*)`", "Kling action prefix C")
PRE_QUIET = rx(r"\*\*Quiet prefix C\*\* = `([^`]*)`", "Kling quiet prefix C")
NEG_K = rx(r"replaced by the C motion terms \(`STYLE_BASE_C.md` §3\): `([^`]*)`", "Kling C negative")
NEG_K_SIG = rx(r"\(\+ `([^`]*)` if `\{SIGNATURE_C\}` is picked", "Kling negative add for the signature layer")
NEG_K_ALL = rx(r"Negative for all: v1.4 list \+ `([^`]*)`", "Kling all-clips negative list")
MNC_SIG = "; the stepped light stays fixed to the forms and never runs along a tower groove"
chk(MNC_SIG[2:] in BOARD, "signature MUST NOT CHANGE tail in board (R3.4)")


def neg_variant(kind, sig):
    n = NEGATIVE_C
    if kind == "mass":
        chk(n.endswith(", extra people"), "NEGATIVE_C ends in extra people")
        n = n[: -len(", extra people")]
    elif kind == "map":
        n = n.replace("2D painting, brush strokes, ", "")
    if sig:
        n = n.replace("hard two-tone shadows, ", "")
    return n


def avoid(kind, sig):
    if kind == "op":
        return AVOID_OP.replace("{NEGATIVE_C}", neg_variant("op", sig))
    if kind == "map":
        return AVOID_OP.replace("{NEGATIVE_C}", neg_variant("map", sig))
    return AVOID_MASS.replace("{NEGATIVE_C_MASS}", neg_variant("mass", sig))


# ------------------------------------------------------------------ v1.4 texts (verbatim) + v2.4 edits
F04_V14 = ("Extreme close-up of a heavy tarred fishing net hung to dry on a wooden pole in a stilt-town lane at dawn, the knotted mesh fills the left two thirds of the frame, clear water drops gathering on the knots, one drop about to fall. On the right, softly out of focus, a sagging rope strung between two stilt-houses with exactly nine small unlit tin lanterns hanging from it. Cold grey-teal dawn light from above, no direct sun, thin mist.")
F10_V14 = ("High aerial view looking forward over a vast stilt-town below sea level in the morning: a maze of narrow water lanes, plank bridges and tarred roofs, washing lines, small boats tied to pilings; in the middle distance the long brick dike with three-storey brick houses along its crest, the town's roofs lying well below the dike's crest; beyond it a granite hill with terraces and a palace; on the hill two tall black towers, the left one the tallest; a third, shorter black tower stands lower down to the right at the edge of the stilt-town, its dark foot in the water. {SPIRE}. Cool grey light in the town, sun only on the hill and the tower tops. Tiny distant specks of people on far bridges allowed, none larger than a dot.")
F14_V14 = ("Top-down view of an open clerk's ledger on worn green felt, ruled columns of tiny illegible ink scribbles, a wide empty margin on the left page, a brass inkwell and a quill at the top edge, a tall leaning tower of rough copper coins standing on the felt to the right of the ledger. Flat cool light from a tall window, dust motes. No hands, no readable text or numbers.")
F17_V14 = ("Use image 1 exactly — same granite wall, rail, poles, golden late-afternoon light and shadows, the city, harbour and sea on the right, same camera. Replace the row of banners with five banners evenly spaced along the same rail, each a tall vertical cloth banner with a slanted cut at the bottom and the long point at the pole side, simple flat emblems exactly as in the references, left to right: (1) deep blue field, a black cormorant with half-folded wings diving beak-down into a silver wave of exactly three crests, no fish; (2) ochre field, a bronze sickle with its blade up above three parallel dark-brown furrows, a tool with a short handle, not a crescent moon; (3) undyed linen field, nine short black strokes above one level black line; (4) black field, a copper beam balance with a level beam, the left pan holding a level surface of blue-grey water, the right pan empty; (5) acid sulphur-yellow field, a grey hare seated in profile facing left, both ears straight up and slightly apart, one eye visible. No other banners; no hands, no stones, no eels, no rings, no gates or bars.")
F19_V14 = ("Two tall silk banners side by side, each filling one half of the frame, hanging from poles on a granite terrace and snapping in a strong wind; each banner is vertical with a slanted cut at the bottom and the long point at the pole side. Left banner: deep blue field, a black cormorant with half-folded wings diving beak-down into a silver wave with exactly three crests, no fish. Right banner: ochre field, a bronze sickle with its blade up, set above three parallel dark-brown furrows; it reads as a tool with a short handle, not as a crescent moon. Emblems exactly as in the references. The two banners fill the frame edge to edge, each emblem centred at mid-height of its banner. Low golden afternoon sun from the left, pale open sky behind, crisp shadows in the folds.")
F19_LR = ("Left banner: deep blue field, a black cormorant with half-folded wings diving beak-down into a silver wave with exactly three crests, no fish. Right banner: ochre field, a bronze sickle with its blade up, set above three parallel dark-brown furrows; it reads as a tool with a short handle, not as a crescent moon.")
F21_LR = ("Left banner: black field, a polished copper beam balance with a level beam, the left pan holding a level surface of blue-grey water, the right pan empty. Right banner: acid sulphur-yellow field (not gold), a grey hare seated in profile facing left, both ears straight up and slightly apart, one eye visible.")
F21_V14 = F19_V14.replace(F19_LR, F21_LR)
for nm, t in (("F04", F04_V14), ("F10", F10_V14), ("F14", F14_V14), ("F17", F17_V14), ("F19 L/R", F19_LR), ("F21 L/R", F21_LR)):
    chk(v14_has(t), f"v1.4 {nm} text = op_paid_run.py verbatim")

NINE_OLD = "with exactly nine small unlit tin lanterns hanging from it"
NINE_NEW = ("with many small unlit tin lanterns of different sizes hanging from it at uneven heights, bunched and overlapping, "
            "the rope and its lanterns running on past the right edge of the frame; no even row and no lantern set apart from "
            "the others; do not keep the number or the spacing of the lanterns in image 2")   # v2.5 keeper R5.1
chk(f"`{NINE_NEW}` (v2.5: keeper R5.1" in BOARD and NINE_OLD in F04_V14, "F04_C nine-lantern edit written in the board (И2)")
F04_C = F04_V14.replace(NINE_OLD, NINE_NEW)
chk("`Use image 1 exactly —` → `Use image 2 exactly —`" in BOARD, "F17_C image index edit written in the board (B4)")
F17_C = F17_V14.replace("Use image 1 exactly —", "Use image 2 exactly —")
F10_ADD = row("F10_C") and span(row("F10_C")[-1], 0)
FLAT = "The emblems are flat dyed shapes on the cloth exactly as in images 3–7; only the cloth folds, poles, rail, wall, city and sea are 3D."
chk(FLAT in BOARD, "flat-emblem sentence in the board")
FLAT34 = FLAT.replace("images 3–7", "images 3–4")

K03_V14 = "Static camera. Water drops gather on the net knots and fall one by one out of frame; a gust makes the rope of lanterns swing; the lanterns stay unlit and their number does not change."
K04_V14 = "Locked-off camera, no camera shake. The wooden slats of the drum move past steadily from top to bottom like a turning wheel; water drips from the slats. The drum keeps its shape; no people."
K05_V14 = "Very slow push-in. The three wooden treadwheels turn slowly and steadily, all at the same speed; water drips from the buckets. Wheel shape, spoke count and the shed do not change; no people appear."
K07_V14 = "Smooth slow forward glide of the camera over the town toward the dike and the hill; thin smoke drifts from a few chimneys; mist moves along the water lanes."
K10_V14 = "Locked-off top-down camera. The tall leaning stack of copper coins slowly topples to the right in one piece; the coins spread and slide a short way across the felt and stop. Ledger, inkwell and quill do not move; no hands; no text."
K11_V14 = "Locked-off camera, no camera shake. Both banners ripple and sway in a steady strong wind from the left; waves of cloth travel down to the slanted bottom points; the emblems stay flat, whole and readable; the poles do not move."
K17_V14 = "Very slow push-in. Clouds stream past the crown of the tower from left to right; the sky darkens very slightly."
for nm, t in (("K03", K03_V14), ("K04", K04_V14), ("K05", K05_V14), ("K07", K07_V14), ("K10", K10_V14), ("K11", K11_V14), ("K17", K17_V14)):
    chk(v14_has(t), f"v1.4 {nm} text = op_paid_run.py verbatim")
K07C = rx(r"— sent: `([^`]*)`", "K07C text as sent (no smoke)")
chk(K07C == K07_V14.replace(" thin smoke drifts from a few chimneys;", ""), "K07C = v1.4 K07 minus the smoke clause (И3)")
K03C_MNC = "lanterns stay unlit and only sway; no lantern appears, vanishes or lights up"   # v2.5 keeper R5.1
chk(f"`{K03C_MNC}`" in BOARD, "K03C lantern MUST NOT CHANGE in the board")

# ------------------------------------------------------------------ frames
P04, P08, P14, P18 = f"{REF}/PL-0004", f"{REF}/PL-0008", f"{REF}/PL-0014", f"{REF}/PL-0018"
H, G = f"{REF}/HERALDRY", f"{REF}/GROUPS"
C_HOUSE = f"{REF}/STYLE_ALIVE/C_final_house.jpg"
ANCHOR = f"{OUT}/frames/D01_A_C.png"           # {C_ANCHOR} once D01_A_C is accepted


def acc(fid):
    return f"{OUT}/frames/{fid}.png"


# C-RR: id -> (seed, image 2 + refs, content kind)
RR_FRAMES = {
    "D01_A_C": (70201, ["output/opening/plates/D01_A_op_169.png"]),
    "alley_C": (70202, ["output/style_test/f_alley_patched.png"]),
    "F04_C": (70203, [f"{OPF}/F04_op.png", f"{P08}/D02_C1_dawn-ebb_v1.png"]),
    "F10_C": (70204, [f"{OPF}/F10_op.png", f"{P04}/D01_A_dawn-ebb_v1.png"]),
    "F14_C": (70205, [f"{OPF}/F14_op.png", f"{REF}/M-LEDGER/E12_ledger_page-a_v1.png"]),
    "F17_C": (70206, [f"{OPF}/F17_op.png", f"{H}/H01_corvane.png", f"{H}/H02_dusk.png", f"{H}/H08_choir.png",
                      f"{H}/H07_lantry.png", f"{H}/H06_fennike.png"]),
    "F19_C": (70207, [f"{OPF}/F19_op.png", f"{H}/H01_corvane.png", f"{H}/H02_dusk.png"]),
    "F21_C": (70208, [f"{OPF}/F21_op.png", f"{H}/H07_lantry.png", f"{H}/H06_fennike.png"]),
    "D05_W2_C": (70209, [f"{REF}/PL-0008W/D05_W2_morning_v1.png"]),
    "D05_W1_C": (70210, [f"{REF}/PL-0008W/D05_W1_morning_v1.png"]),
    "D08_S1_dusk_C": (70211, [f"{P14}/D08_S1_dusk_v1.png"]),
}


def rr_content(fid):
    if fid == "F04_C":
        return F04_C
    if fid == "F10_C":
        return F10_V14 + " " + F10_ADD
    if fid == "F14_C":
        return F14_V14
    if fid == "F17_C":
        return F17_C + " " + FLAT
    if fid == "F19_C":
        return F19_V14 + " " + FLAT34
    if fid == "F21_C":
        return F21_V14 + " " + FLAT34
    return span(row(fid)[-1], 0)


# new: id -> (seed, refs after the anchor, avoid kind)
N_FRAMES = {
    "FA01": (70100, [f"{P04}/D01_A_dawn-ebb_v1.png", f"{OPF}/F01_op.png"], "op"),
    "W01": (70101, [f"{P14}/D08_S1_late-aft_v1.png", f"{P04}/D01_C_late-aft_v1.png"], "op"),
    "W02": (70102, [f"{G}/C07_choir_robes_v1.png", acc("W01")], "mass"),
    "W03": (70103, [f"{P14}/D08_S1_late-aft_v1.png"], "op"),
    "W04": (70104, [acc("W03"), f"{G}/C02_wheel_walkers_v1.png"], "mass"),
    "W05": (70105, [f"{P18}/D09_H1_late-aft_v1.png", f"{P14}/D08_S1_late-aft_v1.png"], "op"),
    "W06": (70106, [acc("W05"), f"{P18}/D09_H1_late-aft_v1.png", f"{H}/H01_corvane.png"], "mass"),
    "W07": (70107, [f"{P04}/D01_C_late-aft_v1.png"], "mass"),
    "W08": (70108, [acc("W07")], "mass"),
    "W09": (70109, [f"{P14}/D08_S1_late-aft_v1.png"], "op"),
    "W10": (70110, [acc("W09")], "mass"),
    "W11": (70111, [f"{P14}/D08_S1_late-aft_v1.png"], "op"),
    "W12": (70112, [f"{G}/C05_rusk_guards_v1.png", acc("W11")], "mass"),
    "W13": (70113, [acc("W05"), acc("W01"), acc("W03"), acc("W11"), acc("W09"), f"{P04}/D01_C_late-aft_v1.png"], "op"),
    "W14": (70114, [acc("F19_C")], "op"),
    "W15": (70115, [acc("W13"), f"{P18}/D09_H1_late-aft_v1.png"], "mass"),
    "W16": (70116, [f"{REF}/M-MAP/E05_map_base_v1.png", acc("W13"), f"{H}/H16_ashare_reference_spiral.png"], "map"),
}


ROLE_IDS = ["W%02d" % n for n in range(1, 14)] + ["W15", "F14_C"]     # v2.5 gate B9, И14 (§5.5)
ROLES = {k: span(row("ROLE-" + k)[-1], 0) for k in ROLE_IDS}


def role(fid):
    return [ROLES[fid]] if fid in ROLES else []


def subst(t):
    return (t.replace("{SPIRE}", SPIRE).replace("{VSAFE_MASS}", VSAFE_MASS).replace("{VSAFE}", VSAFE)
            .replace("{FLOW}", FLOW))


def tail(sig, kind):
    parts = [C_NOTE, STYLE_BASE_C]
    if sig:
        parts.append(SIGNATURE_C)
    parts += [PHONE, avoid(kind, sig)]
    return " ".join(parts)


def frame_call(fid, sig, take=1):
    """-> dict(model, seed, images, prompt) for an NB2 frame (C-RR, new, test or logo)."""
    if fid in ("T1a", "T1b", "T2a", "T2b"):
        base = "D01_A_C" if fid.startswith("T1") else "W11"
        c = frame_call(base, fid.endswith("b"), 1)
        c["images"] = [C_HOUSE] + c["images"][1:]          # no C world frame exists yet (§5.2)
        c["id"] = fid
        return c
    if fid == "LOGO_C":
        line = rx(r"^- Prompt \(v2.4: keeper R3.3 in\): ([^\n]*)$", "LOGO_C prompt line")
        prompt = span(line, 0) + " " + span(line, 1).replace("{NEGATIVE_C_LOGO}", NEGATIVE_C_LOGO)
        return {"id": fid, "model": "nano-banana-2-edit", "seed": 410801 + (take - 1),
                "images": [ANCHOR, f"{REF}/LOGO/HOLLOWSTONE_logo_master_dark_1920.png",
                           f"{REF}/LOGO/HOLLOWSTONE_logo_clean_alpha.png"], "prompt": prompt}
    if fid in RR_FRAMES:
        seed, refs = RR_FRAMES[fid]
        anchor = C_HOUSE if fid == "D01_A_C" else ANCHOR
        rr = RR_169 if fid == "D01_A_C" else RR
        prompt = " ".join([ANCHOR_INTRO, rr, subst(rr_content(fid))] + role(fid) + [tail(sig, "op")])
        return {"id": fid, "model": "nano-banana-2-edit", "seed": seed + 1000 * (take - 1),
                "images": [anchor] + refs, "prompt": prompt}
    seed, refs, kind = N_FRAMES[fid]
    content = subst(span(row(fid)[-1], 0))
    prompt = " ".join([ANCHOR_INTRO, content] + role(fid) + [tail(sig, kind), SAGA_SAFE])
    return {"id": fid, "model": "nano-banana-2-edit", "seed": seed + 1000 * (take - 1),
            "images": [ANCHOR] + refs, "prompt": prompt}


# ------------------------------------------------------------------ clips
ACTION = {"KW02", "KW04", "KW06", "KW08", "KW12", "KW14", "KA01", "K04C", "K10C", "K11C", "K12C"}
SOURCE = {"KA01": "FA01", "KA02": "D01_A_C", "KA11": "F17_C", "KA04": "alley_C", "K03C": "F04_C",
          "K04C": "D05_W2_C", "K05C": "D05_W1_C", "K07C": "F10_C", "K10C": "F14_C", "K11C": "F19_C",
          "K12C": "F21_C", "K17C": "D08_S1_dusk_C"}
SOURCE.update({f"KW{i:02d}": f"W{i:02d}" for i in range(1, 17)})
V14_CLIPS = {"K03C": K03_V14, "K04C": K04_V14, "K05C": K05_V14, "K07C": K07C, "K10C": K10_V14,
             "K11C": K11_V14, "K12C": K11_V14, "K17C": K17_V14}
NEG_ADD_LINE = rx(r"^(Negative additions: [^\n]*)$", "§6.2 negative additions line")
NEG_ADD = {}
for ids, t in re.findall(r"((?:K[A-Z]\d\d)(?:, K[A-Z]\d\d)*): `([^`]*)`", NEG_ADD_LINE):
    for i in ids.split(", "):
        NEG_ADD.setdefault(i, []).append(t)
for ids, t in re.findall(r"Add for ((?:KW\d\d)(?:, KW\d\d)*): `([^`]*)`", BOARD):
    for i in ids.split(", "):
        NEG_ADD.setdefault(i, []).append(t)
NEG_ADD.setdefault("KA04", []).append(rx(r"Negative add: ([^|]*?)\. \|", "KA04 negative add (R3.2)"))
CUES = {}
for line in re.findall(r"^\| (K[^|]*) \| `([^`]*)`", BOARD[BOARD.index("### 6.5"):], re.M):
    for i in line[0].split(", "):
        CUES[i.strip()] = line[1]
chk(len(CUES) == 15, f"§6.5 cues parsed ({len(CUES)} of 15)")
ALL_CLIPS = (["KA01", "KA02", "KA11", "KA04"] + [f"KW{i:02d}" for i in range(1, 17)] +
             ["K03C", "K04C", "K05C", "K07C", "K10C", "K11C", "K12C", "K17C"])


def clip_call(kid, sig):
    pre = PRE_ACT if kid in ACTION else PRE_QUIET
    cue = CUES.get(kid, "")
    if kid in V14_CLIPS:
        text = V14_CLIPS[kid] + (" " + cue if cue else "")
        if kid == "K03C":
            text += f" Must not change: {K03C_MNC}" + (MNC_SIG if sig else "") + "."
        elif sig:
            text += " Must not change: " + MNC_SIG[2:] + "."
    else:
        if kid == "KA04":
            cell = re.search(r"^\| \*\*KA04\*\*[^|]*\| alley_C \| ([^\n]*)$", BOARD, re.M)
            chk(cell, "KA04 row found")
            motion, mnc = span(cell.group(1), 0), span(cell.group(1), 1)
        else:
            cells = row(kid)
            motion, mnc = span(cells[1], 0), cells[2].replace("**", "")   # no markdown in the call
        text = motion + (" " + cue if cue else "") + " Must not change: " + mnc.rstrip(".") + (MNC_SIG if sig else "") + "."
    neg_all = NEG_K_ALL.replace("fire, ", "large fire, spreading flames, ") if kid == "KW10" else NEG_K_ALL
    neg = ", ".join([NEG_K] + ([NEG_K_SIG] if sig else []) + [neg_all] + NEG_ADD.get(kid, []))
    return {"id": kid, "model": "kling-2.5-turbo-pro", "duration": 5, "source": acc(SOURCE[kid]),
            "prompt": f"{pre} {text}", "negative_prompt": neg}


# ------------------------------------------------------------------ steps, state
STEPS = {"T": ["T1a", "T1b", "T2a", "T2b"], "L": ["LOGO_C"], "R": list(RR_FRAMES), "N": list(N_FRAMES), "K": ALL_CLIPS}
PLAN = {"T": 0.32, "L": 0.24, "R": 1.32, "N": 2.04, "K": 15.05}


def step_of(i):
    return next(s for s, ids in STEPS.items() if i in ids)


def load_state():
    try:
        return json.load(open(STATE))
    except (OSError, ValueError):
        return {"pick": None, "accepted": {}}


def save_state(st):
    os.makedirs(OUT, exist_ok=True)
    json.dump(st, open(STATE, "w"), indent=1)


def take_path(i, take, st):
    if i in ("D01_A_C", "W11") and take == 1:          # take 1 = the picked T image
        t = ("T1" if i == "D01_A_C" else "T2") + ("b" if st.get("pick") == "with" else "a")
        return f"{OUT}/test/{t}.png"
    sub = {"T": "test", "L": "logo", "R": "frames", "N": "frames", "K": "clips"}[step_of(i)]
    ext = "mp4" if step_of(i) == "K" else "png"
    return f"{OUT}/{sub}/{i}.{ext}" if step_of(i) == "T" else f"{OUT}/{sub}/{i}_t{take}.{ext}"


def default_take(i, st):
    return 2 if i in ("D01_A_C", "W11") and os.path.exists(take_path(i, 1, st)) else 1


def step_limit(step):
    lim = STEP_LIMITS[step]
    if step == "L" and any(os.path.exists(f"{OUT}/frames/{f}_t{t}.png") for f in RR_FRAMES for t in (1, 2, 3)):
        lim = L_AFTER_R
    env = os.environ.get("BUDGET_LIMIT_USD", "").strip()
    if env:
        if float(env) > HARD_CAP:
            sys.exit(f"BUDGET_LIMIT_USD={env} is above the opening's cap {HARD_CAP} (§8.3): refused")
        lim = min(lim, float(env))
    return lim


# ------------------------------------------------------------------ checks on the assembled calls
def call_checks(sig_values=(False, True)):
    for sig in sig_values:
        for st_ in ("T", "L", "R", "N"):
            for i in STEPS[st_]:
                c = frame_call(i, sig)
                p = c["prompt"]
                chk(not re.search(r"\{[A-Z_0-9]+\}", p), f"{i}: no unresolved block")
                if i != "LOGO_C":
                    chk(STYLE_BASE_C in p and C_NOTE in p and PHONE in p, f"{i}: STYLE_BASE_C + C_NOTE + PHONE in prompt")
                    chk(("photorealism, photographic skin" in p), f"{i}: a C negative in prompt")
                    want = i.endswith("b") if i.startswith("T") else sig
                    chk((SIGNATURE_C in p) == want, f"{i}: signature layer {'on' if want else 'off'}")
                    chk(p.startswith(ANCHOR_INTRO), f"{i}: opens with the C_ANCHOR sentence")
                else:
                    chk(STYLE_BASE_C not in p and SIGNATURE_C not in p and PHONE not in p and NEGATIVE_C_LOGO in p,
                        "LOGO_C: no STYLE_BASE_C/SIGNATURE_C/PHONE, has NEGATIVE_C_LOGO (B5, R3.3)")
                    chk("Exactly six small water drops" in p and "A few water drops" not in p, "LOGO_C: six drops (R3.3)")
                chk(len(c["images"]) <= 8, f"{i}: {len(c['images'])} images")
    for i in ROLE_IDS + ["T2a", "T2b"]:                 # gate B9, И14: every image 2+ has its role in the prompt
        c = frame_call(i, False)
        for n in range(3 if i in RR_FRAMES else 2, len(c["images"]) + 1):   # C-RR: image 2 = {RR}
            chk(f"image {n} only for" in c["prompt"], f"{i}: role of image {n} in the prompt (B9)")
    chk("no pale wall, plinth or sleeve" in frame_call("T1a", False)["prompt"]
        and "nothing rises behind or above it" in frame_call("T1b", False)["prompt"], "T1a/T1b: keeper R5.2 defect lines")
    chk("do not keep the number or the spacing" in frame_call("F04_C", False)["prompt"], "F04_C: keeper R5.1 lanterns")
    fa = frame_call("FA01", False)["prompt"]
    chk("no water over any dike" in fa and "Use image 3 only for the dike" in fa, "FA01: SAGA_SAFE + image 3 protection (B4, B5)")
    chk("Use image 2 only for the paper" in frame_call("W16", False)["prompt"], "W16: image 2 = E05 protection (B4)")
    chk("from image 2." in frame_call("W14", False)["prompt"], "W14: image 2 protection (B4)")
    chk("Use image 2 exactly" in frame_call("F17_C", False)["prompt"], "F17_C: image 2 (B4)")
    chk("nine" not in frame_call("F04_C", False)["prompt"].lower(), "F04_C: no nine lanterns (И2)")
    chk("exactly as in image 2" not in frame_call("D01_A_C", False)["prompt"], "D01_A_C: no 'exactly as in image 2' (B2)")
    chk("south-west" in frame_call("D01_A_C", False)["prompt"], "D01_A_C: Sluice Spire at the south-west foot (B2)")
    chk("drifting rain" not in FLOW and "{FLOW}" not in span(row("W11")[-1], 0), "FLOW without rain, not on W11 (R4.4)")
    chk("no lamp, lantern, window or fire is lit" in C_NOTE, "C_NOTE R3.4")
    chk("no light band following a groove" in SIGNATURE_C and "no added rim light" in PHONE, "SIGNATURE_C / PHONE R3.4")
    for sig in (False, True):
        for k in ALL_CLIPS:
            c = clip_call(k, sig)
            chk(len(c["prompt"]) <= 2500, f"{k}: prompt {len(c['prompt'])} chars <= 2500")
            chk(not re.search(r"\{[A-Z_0-9]+\}", c["prompt"]), f"{k}: no unresolved block")
            if sig:
                chk("never runs along a tower groove" in c["prompt"] and "crawling light bands" in c["negative_prompt"],
                    f"{k}: signature lock + negative")
    chk("smoke" not in clip_call("K07C", False)["prompt"], "K07C: no smoke in the prompt (И3)")
    chk(", fire," not in clip_call("KW10", False)["negative_prompt"], "KW10: negative without plain 'fire'")
    chk("just below its top edge" in clip_call("KA01", False)["prompt"], "KA01: spray below the crest (R4.3)")
    chk("to the left, away from the bar" in clip_call("KW10", False)["prompt"], "KW10: boats left (R4.4)")
    chk("Negative" not in clip_call("KA04", False)["prompt"], "KA04: negative add kept out of the prompt")


# ------------------------------------------------------------------ commands
def fmt_call(c, st):
    out = [f"=== {c['id']}  [{step_of(c['id'])}]  {c['model']}"]
    if "seed" in c:
        base = c["seed"]
        out.append(f"seed {base}" + ("" if c["id"].startswith("T") else
                   ("  (retakes +1, +2 = 410802, 410803)" if c["id"] == "LOGO_C" else "  (take N: +1000*(N-1))")))
        for n, im in enumerate(c["images"], 1):
            tag = "ok" if os.path.exists(im) else ("PENDING: accept first" if OUT in im else "MISSING")
            out.append(f"  image {n}: {im}  [{tag}]")
        out.append(f"  prompt ({len(c['prompt'])} chars):\n{c['prompt']}")
    else:
        tag = "ok" if os.path.exists(c["source"]) else "PENDING: accept the frame first"
        out.append(f"  image_url: {c['source']}  [{tag}]   duration 5 s")
        out.append(f"  prompt ({len(c['prompt'])} chars):\n{c['prompt']}")
        out.append(f"  negative_prompt:\n{c['negative_prompt']}")
    if c["id"] in st.get("accepted", {}):
        out.append(f"  ACCEPTED take {st['accepted'][c['id']]} -> skipped by run")
    return "\n".join(out)


def expand(items):
    ids = []
    for a in items or ["T", "L", "R", "N", "K"]:
        ids += STEPS[a] if a in STEPS else [a]
    return ids


def cmd_show(items):
    st = load_state()
    pick = st.get("pick")
    sigs = [False, True] if pick is None else [pick == "with"]
    for i in expand(items):
        for sig in (sigs if not i.startswith("T") else [None]):
            label = "" if sig is None else (" with {SIGNATURE_C}" if sig else " without {SIGNATURE_C}")
            c = frame_call(i, bool(sig)) if step_of(i) != "K" else clip_call(i, bool(sig))
            print(fmt_call(c, st) + (f"\n  (variant:{label})" if label else "") + "\n")
    print_plan()


def print_plan():
    print("Steps (cumulative limit from the log at $%.4f):" % LOG_AT_PLAN)
    tot = 0
    for s in STEPS:
        tot += PLAN[s]
        print(f"  {s}: {len(STEPS[s]):2d} items, plan ${PLAN[s]:.2f}, limit {STEP_LIMITS[s]:.2f}")
    print(f"  total ${tot:.2f} (= $18.97 with the reserve inside K)")


def report_checks():
    call_checks()
    bad = [m for ok, m in CHECKS if not ok]
    print(f"checks: {len(CHECKS) - len(bad)} passed, {len(bad)} failed")
    for m in bad:
        print("  FAIL:", m)
    return not bad


def cmd_run(step, ids, take_arg):
    if not report_checks():
        sys.exit("text checks failed: nothing is sent")
    from pipeline import costs, fal_client
    st = load_state()
    if step != "T" and step != "L" and st.get("pick") not in ("with", "without"):
        sys.exit("the coordinator's pick after step T is not recorded (`pick with|without`)")
    needs_anchor = step in ("L", "N", "K") or (step == "R" and any(i != "D01_A_C" for i in (ids or STEPS["R"])))
    if needs_anchor and "D01_A_C" not in st["accepted"]:
        sys.exit(f"step {step} needs D01_A_C accepted first ({{C_ANCHOR}}); run R D01_A_C alone, or accept the picked T1")
    limit = step_limit(step)
    os.environ["BUDGET_LIMIT_USD"] = f"{limit:.2f}"
    sig = st.get("pick") == "with"
    print(f"step {step}: limit {limit:.2f}, spent so far ${costs.total_spent():.4f}, signature {'on' if sig else 'off'}")
    for i in ids or STEPS[step]:
        if step_of(i) != step:
            sys.exit(f"{i} is not in step {step}")
        if i in st["accepted"]:
            print("accepted, skip", i)
            continue
        take = take_arg or (1 if step == "T" else default_take(i, st))
        out = take_path(i, take, st)
        if os.path.exists(out):
            print("exists, skip", out)
            continue
        c = clip_call(i, sig) if step == "K" else frame_call(i, sig if step != "T" else i.endswith("b"), take)
        est = KLING_USD if step == "K" else NB2_USD
        if costs.total_spent() + est > limit:
            sys.exit(f"step ceiling {limit:.2f} reached: stop")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        t0 = time.time()
        if step == "K":
            if not os.path.exists(c["source"]):
                sys.exit(f"{i}: source {c['source']} not accepted yet")
            fal_client.image_to_video(c["source"], c["prompt"], out, model=c["model"], duration=5,
                                      negative_prompt=c["negative_prompt"])
        else:
            for im in c["images"]:
                if not os.path.exists(im):
                    sys.exit(f"{i}: missing image {im}")
            fal_client.generate_image(c["prompt"], out, model="nano-banana-2", reference_images=c["images"],
                                      aspect_ratio="16:9", extra={"seed": c["seed"]})
        meta = dict(c, take=take, usd=est, seconds=round(time.time() - t0, 1), step=step, limit=limit)
        json.dump(meta, open(out.rsplit(".", 1)[0] + ".json", "w"), indent=1, ensure_ascii=False)
        print("  ->", out, f"({meta['seconds']} s), spent ${costs.total_spent():.4f}", flush=True)


def cmd_accept(i, take):
    st = load_state()
    src = take_path(i, int(take), st) if not str(take).startswith("T") else f"{OUT}/test/{take}.png"
    if not os.path.exists(src):
        sys.exit(f"no such take: {src}")
    dst = acc(i) if step_of(i) != "K" else f"{OUT}/clips/{i}.mp4"
    if step_of(i) == "L":
        dst = f"{OUT}/logo/LOGO_C.png"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    st["accepted"][i] = take
    save_state(st)
    print(f"accepted {i} take {take}: {src} -> {dst}")


def cmd_peaks(kid):
    import cv2
    import numpy as np
    path = f"{OUT}/clips/{kid}.mp4"
    cap = cv2.VideoCapture(path)
    prev, e = None, []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        g = cv2.cvtColor(cv2.resize(f, (480, 270)), cv2.COLOR_BGR2GRAY).astype(np.float32)
        e.append(0.0 if prev is None else float(np.abs(g - prev).mean()))
        prev = g
    if not e:
        sys.exit(f"cannot read {path}")
    e = np.convolve(np.array(e), np.ones(3) / 3, mode="same")
    top = sorted(range(len(e)), key=lambda k: -e[k])[:8]
    print(f"{kid}: {len(e)} frames; motion energy peaks (frame, s, energy):")
    for k in sorted(top):
        print(f"  {k:4d}  {k / 24:5.2f}  {e[k]:.2f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["show", "check", "run", "pick", "accept", "peaks"])
    ap.add_argument("args", nargs="*")
    ap.add_argument("--take", type=int)
    a = ap.parse_args()
    if a.cmd == "show":
        cmd_show(a.args)
        sys.exit(0 if report_checks() else 1)
    if a.cmd == "check":
        sys.exit(0 if report_checks() else 1)
    if a.cmd == "pick":
        if a.args not in (["with"], ["without"]):
            sys.exit("pick with|without")
        st = load_state()
        st["pick"] = a.args[0]
        save_state(st)
        print("signature layer:", a.args[0])
        return
    if a.cmd == "accept":
        cmd_accept(a.args[0], a.args[1])
        return
    if a.cmd == "peaks":
        cmd_peaks(a.args[0])
        return
    step, ids = a.args[0], a.args[1:]
    if step not in STEPS:
        sys.exit("step: T | L | R | N | K")
    cmd_run(step, ids, a.take)


if __name__ == "__main__":
    main()
