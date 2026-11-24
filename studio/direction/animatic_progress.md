# S01E01 animatic v1 — progress checklist (resume file)

Updated: 2026-11-24 (resume after container restart). Tools: `studio/direction/animatic_tools/`. Outputs: `output/S01E01/animatic/`.
Budget guard: `STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=70`. Studio total at resume: $47.11.

| # | Step | Status | How to resume |
|---|---|---|---|
| 0 | Draft VO + timed shot list (451 shots, 28:19) | DONE | — |
| 1a | Frames `_a` (one per non-reuse shot, 327) | DONE 327/327 (sc02-sh050, sc04-sh180 refused by fal content checker -> $0 placeholders copied from sc02-sh200/sc04-sh070; director decision) | — |
| 1b | Contact-sheet review vs §11 + concept-artist flaws | DONE: 27 `_a` retaken (EXTRA dict in frames.py), 4 needed retry 2; sc01-sh070 kept r0; rejects in `frames_rejected/` | — |
| 1c | End poses `_b` for C/D (48) | DONE 47/47 (+5 retakes: sc01-sh010, sc19-sh110 x2, sc20-sh150, sc20-sh170) | — |
| 2a | MiniMax drafts class D | DONE 5 clips ($1.24): sc03-sh220 used; 4 rejected for glow (`*_mm_REJECTED.mp4`) | — |
| 2b | LA render 720p | DONE 451/451 (log `la_run2.log`) | — |
| 3 | SFX (ElevenLabs) + synth | DONE (SFX 2,311 credits this run; account usage 14,860) | — |
| 4 | Spec + assemble + overlay | assemble DONE (LA pre-concatenated: 451 inputs OOM'd assemble.py; SFX trims; I −13.5, TP −0.9) → overlay with −0.5 dB | `spec.py overlay` |
| 5 | R2 upload | frames, rejects, la, drafts, audio, spec uploaded; final mp4 TODO | `scratchpad up.py` logic: storage.upload per file |
| 6 | Notes `S01E01_animatic_v1_notes.md`, report, HANDOFF | TODO | |
