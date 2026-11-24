#!/usr/bin/env python3
"""One-off: storyboard v1.3 -> v1.4 (gate R2 free fixes 1-9 + studio director rulings on C1-C4). Every replacement must match exactly once."""
import sys

P = "/home/user/my_work/studio/direction/opening/S1_OP_storyboard.md"
s = open(P, encoding="utf-8").read()
R = []


def rep(old, new):
    n = s.count(old)
    if n != 1:
        sys.exit(f"expected 1 match, got {n}: {old[:90]!r}")
    R.append((old, new))


K11_PROMPT = "`Locked-off camera, no camera shake. Both banners ripple and sway in a steady strong wind from the left; waves of cloth travel down to the slanted bottom points; the emblems stay flat, whole and readable; the poles do not move.`"
K11_MNC = "both emblems and colours exactly as in the source; banner shape (slanted cut, long point at the pole); light"
assert s.count(K11_PROMPT) == 1 and s.count(K11_MNC) == 1

# header
rep("# HOLLOWSTONE — Season 1 opening (instrumental, 87.0 s) — storyboard v1.3",
    "# HOLLOWSTONE — Season 1 opening (instrumental, 87.0 s) — storyboard v1.4")
rep("Version 1.3 · 2026-11-24 · author: director (anime-director) · status: **storyboard only. No paid call made. v1.3 = v1.2",
    "Version 1.4 · 2026-11-24 · author: director (anime-director) · status: **gate OPEN with conditions (`qa/gate/gate-op-2026-11-24.md` §R2). Studio director on the conditions: C1 waived (the picture carries the build; the 0:57.0 hit lands on the 9-frame black + INK + wave cut); C2 moved (K13 waits until the keeper has looked at the fixed H1/H2 plates and the studio director gives the go; everything else is generated); C3 holds (the OP is the only paid run); C4 waived (guard + log estimate). v1.4 = v1.3 + the gate's free fixes 1–9 (below). Paid run of 16 NB2 frames + 16 Kling clips (all but K13) follows v1.4.**\n"
    "v1.4 changes: H1/H2 plates v2 (finial re-filled with no ghost or streak; the 6 lamp heads redrawn unlit, halo ring removed, no orange bar, no blue patch); G1 `{AVOID_OP}` ends `finger rings, rings on water.`; G5 K12 written out in full; §8 numbers (limit 64, log $54.15, headroom $9.85, retakes only from the $1.12 reserve); G2 \"before acceptance / assembly\"; F2 the third flash stays on 1356 (text aligned); N1 cut 33 spray field ends with the wipe on 1994, never on the tower; cuts 02 and 05 crack paint-outs and cut 24 tier tints done at $0 (`tools/op_paintouts.py`).\n"
    "v1.3 status (kept for the record): storyboard only. v1.3 = v1.2")
rep("- **Смета: $7.23 + резерв $1.50 = $8.73**, запас до потолка $10 — $1.27 (§8).",
    "- **Смета: $7.23 (из них K13 $0.35 ждёт хранителя и директора студии) + резерв на передубли $1.12 = $8.35**; потолок прогона $9.85 (`BUDGET_LIMIT_USD=64`), инвесторский потолок $10 (§8).")

# §2.1 F2
rep("| Wave flashes in the map push | 0:55.5 / 0:56.25 / 0:56.44 | 1332 / 1350 / 1355 | **1333 / 1351 / 1356** | 24 |",
    "| Wave flashes in the map push | 0:55.5 / 0:56.25 / 0:56.44 | 1332 / 1350 / 1355 (1354.6 rounded) | **1333 / 1351 / 1356** (all three = grid + 1; 1356 kept, director F2) | 24 |")

# cuts 02, 05, 24 (fix 9)
rep("(paint out locally every crack line on all three Spires — left, centre AND right; full-size check, OP-5)",
    "(paint out locally every crack line on all three Spires — left, centre AND right; full-size check, OP-5; done at $0: `tools/op_paintouts.py` → `output/opening/plates/D01_A_op.png`)")
rep("(paint out locally the crack lines on the great wall behind the wheel: the dike reads intact, OP-5)",
    "(paint out locally the crack lines on the great wall behind the wheel: the dike reads intact, OP-5; done at $0: `output/opening/plates/sc06_wheel_op.png`)")
rep("+ the three tint overlays of Sc 7 (no IX wash,",
    "+ the three tier tints, Steps / Mids / Lows (drawn at $0 by `tools/op_paintouts.py` → `output/opening/plates/E05_map_tints_op.png`; no IX wash,")

# cut 31 plates (fixes 1, 7)
rep("(same mask on both, pixel for pixel; keeper to check before Kling, C2)",
    "(same mask on both, pixel for pixel; plates v2, gate R2 fixes 1 and 7: the finial re-filled with a shifted, Poisson-blended copy of the same rows — no ghost, no streak; the 6 lamp heads redrawn as unlit dark lanterns, the halo ring inpainted from the water — no warm ring, no orange bar, no blue patch; the keeper looks at them before K13, which waits for the studio director's go, C2)")

# cut 33 (fix 8, N1)
rep("WIPE (torn edge, K01 spray ×1.6 over the edge),",
    "WIPE (torn edge, K01 spray ×1.6 over the edge; the spray field ends with the wipe edge on frame 1994 and never stays on the tower, N1),")

# §5 (G1, G2)
rep("stones or pebbles on cords, rings.`", "stones or pebbles on cords, finger rings, rings on water.`")
rep("**The keeper checks F15, F17, F18, F23 and F26 at full size before any Kling clip is made from them.**",
    "**The keeper checks F15, F17, F18, F23 and F26 at full size before acceptance / assembly** (F15, F17, F18 and F23 have no clip; F26 feeds K18, which is accepted together with F26).")
rep("**the keeper checks F15, F17, F18, F23, F26 at full size before their clips.**",
    "**the keeper checks F15, F17, F18, F23, F26 at full size before acceptance / assembly.**")

# §6 (G5)
rep("| K12 | F21 | same as K11 | same as K11 | 21, 22 |", f"| K12 | F21 | {K11_PROMPT} | {K11_MNC} | 21, 22 |")

# §8 (fix 4)
rep("| Retake reserve (e.g. 4 clip retakes $1.40 + 1 frame $0.08) | | | | **1.50** |\n| **Total planned** | | | | **$8.73** |\n| Untouched margin to the $10 cap | | | | $1.27 |",
    "| Retake reserve (studio director 2026-11-24: retakes only from **$1.12** = $9.85 − $8.73; a clip that fails twice uses its §6.1 ffmpeg fallback) | | | | **1.12** |\n| **Total planned** | | | | **$8.35** |\n| Run ceiling for the whole OP (`BUDGET_LIMIT_USD=64` − $54.15 logged) | | | | $9.85 |\n| Untouched margin to the investor's $10 cap | | | | $1.65 |")
rep("Run cap: BUDGET_LIMIT_USD=63 with ≈$53 already spent leaves ≈$10, so the full plan including the reserve fits; the scripts stop at $63 in any case.",
    "Run cap (gate R2 §5): `STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=64`; the log before the OP is **$54.15** (fal $43.36, ElevenLabs $10.79; 1512 rows, no OP rows), so the run headroom is **$9.85**, the hard ceiling for the whole OP; the guard stops every call above it. K13 ($0.35) is not in this run: it waits for the keeper's look at the fixed H1/H2 plates and the studio director's go (C2). No other paid run (ElevenLabs or fal) while the OP runs (C3). fal balance: log estimate $100.00 − $43.36 = ≈$56.64, after the plan ≈$48.3, above the $20 floor (C4 waived by the studio director).")

for o, n in R:
    s = s.replace(o, n)
open(P, "w", encoding="utf-8").write(s)
print(len(R), "replacements")
