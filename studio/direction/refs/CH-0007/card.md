# CH-0007 Wick — reference card

## Stage 2 (2026-11-23) — `CH-0007`

Prompts, refs, seeds for every file: `meta.json` (this folder). Raw outputs incl. drafts: R2 `refs_stage/CH-0007/`. Drafts: 11 × nano-banana; finals: 7 × nano-banana-2 (/edit).

| File | Final | Model | Seed | From draft | Known flaws |
|---|---|---|---|---|---|
| `A02_00_master_v1.png` | m_f2 | nano-banana-2 | 256523 | m_d4 → m_f1 → m_f2 (hair edit) | m_f1 rejected: main spike on the wrong side; m_f2 is an edit fixing the tuft |
| `A02_01_turnaround_v1.png` | turn_f | nano-banana-2 | 223792 | turn_d2 | small extra spikes on top of the mop; the single tuft reads best in front/3/4 views |
| `A02_02_heads_v1.png` | heads_f | nano-banana-2 | 744108 | heads_d1 | — |
| `A02_04_emotions_v1.png` | emo_f | nano-banana-2 | 125028 | emo_d2 | — |
| `A02_05_mouth_v1.png` | mouth_f | nano-banana-2 | 251005 | mouth_d1 | — |
| `A02_06_details_v1.png` | det_f | nano-banana-2 | 758384 | det_d1 | cell 1 shows the rolled sleeve without much forearm |

No cap in E1 (cap variant = one edit for E2). ID-block used is in meta.json (portrait version drops legs/feet).
`*_03_silhouette` and `*_07_palette` built locally (threshold / median-cut quantize), $0.

## Three-character test (stage 2.4)
`../keyframes/test_pell_wick_nan_house_v1.png` — Pell + Wick + Nan in Nan's house (D-06 N1), nano-banana-2 /edit, refs: draft d1 + plate + master and turnaround of each (8 images), prompt in `../keyframes/test_pell_wick_nan_house_meta.json`.
Result: scale relation, sides (braid picture-right, tuft picture-left, one earring picture-right) and lighting match pass. **Flaw:** Pell's blue tag migrated onto her jacket again (it must be on the braid tip only) — in multi-character key frames add "no tag on the jacket" to the fix line and check it first.
