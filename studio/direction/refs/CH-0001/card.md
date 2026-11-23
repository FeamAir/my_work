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
