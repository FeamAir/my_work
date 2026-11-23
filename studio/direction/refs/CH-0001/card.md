# CH-0001 Pell — reference card

## A01_00_master_v1.png — style test master (2026-11-23)
- Model: nano-banana-2 /edit, seed 3001, 3:4, ref = draft `pell_master_B2_1` (nano-banana, seed 2001). Pro version for comparison: `style_test/A01_00_master_v1_pro.png`.
- Prompts: `style_test/finals_meta.json` (final), `style_test/drafts2_meta.json` (draft round 2), `style_test/drafts_meta.json` (round 1, styles A/B).
- Raw files: R2 `style_test/2026-11-23/`.
- Status: **candidate**, awaiting director style approval and investor viewing.

## Style test findings
1. **Style B (visual bible v2 STYLE_BASE, "Tidemark") beats style A** (artist's gouache/umber block): crisper line, reads as TV anime; A is softer, more illustrative. Proposal: STYLE_BASE replaces `{STYLE}` in `art/pilot_references.md`.
2. **Side anchors:** the ID-block wording "HER OWN LEFT side (right side of the image…)" failed 8/8 on nano-banana — braid AND net bag flipped. Image-relative wording only ("hangs on the RIGHT side of the picture … the left side of the picture has only short hair") + negative "braid on the left side of the picture" → 4/4 correct. Update `consistency.md` §side rule: lead with picture side, avoid "her own left".
3. **Framing:** full-body items in the ID-block (feet, leggings) override "waist-up" → 8/8 full body. For portraits, state "cropped at the waist, legs and feet not visible" and drop lower-body items.
4. "leans forward slightly" → literal hands-on-knees pose. Keep it out of master prompts.
5. Tag "IX" migrates to the jacket unless prompt says "tied to the braid tip (the tag is on the braid, not on her clothes)".
6. **Model decision (step 1.5): Pro and NB2 finals are near-identical** at 896×1200 → finals on NB2 (−≈17% of reference budget), Pro only if a specific sheet fails twice on NB2.
7. Open: hair still reads slightly orange; director to judge vs `#` palette.

Spent on this step: $0.71 (8+4 drafts × $0.04, Pro $0.15, NB2 $0.08).

## Steps 1.6–1.9 (2026-11-23) — all finals on nano-banana-2 /edit
| File | From draft | Notes |
|---|---|---|
| `A01_01_turnaround_v1.png` | d_turn_3 (of 3) | only draft with logically consistent sides (profile faces right → braid hidden; back → braid picture-left). Small tag near net in 3/4 view — minor. |
| `A01_02_heads_v1.png` | d_heads_2 (of 2) | **known flaw:** profile faces right yet braid visible (side logic). Accepted for refs; redo only if it misleads a shot. |
| `A01_04_emotions_v1.png` | d_emo_3 (of 3) | drafts missed "fear"; explicit physical cues in final fixed it. d_emo_1 produced 7 cells. |
| `A01_06_details_v1.png` | d_det_1 (of 2) | clean. |
| `../PL-0008/D02_C1_dawn-ebb_v1.png` | d_alley_3 (of 4) | NB drew towers as tiers/pagodas/trees → final prompt "smooth glassy towers with spiral grooves, ring of arches, not tiered/pagodas/trees" fixed it. Grooves still faint. |
| `../M-SHD/E01_sheet_v1.png` | d_stone_2 (of 4) | drafts drilled a hole + too big; fixed by "cord knotted around the stone, covers < 1/3 of palm". |
| `../keyframes/styletest_pell_ladder_v1.png` | d_key_2 (of 2) | refs: plate + master + turnaround. Drafts looked pasted-in (character brighter/warmer than scene) → final with explicit "same cold dawn light, darker desaturated values, rim light, colours not brighter than surroundings" integrates well. Staging still off (ladder logic: she stands on foreground deck, not on silt) → key frames need explicit pose/blocking from the storyboard panel. |

Spent steps 1.6–1.9: $1.36 → **style test total $2.07** (plan $2.6).
Prompts/seeds for every file: `style_test/meta_all.json`; raw: R2 `style_test/2026-11-23/`.

### Lessons for production prompts
- Character-into-plate: always pass plate + master + turnaround, and a lighting-match sentence.
- Name the picture side for every asymmetric anchor per view; profiles: state which edge she faces.
- Emotions: physical cues, not labels.
- Set "exactly N cells" for grids.
