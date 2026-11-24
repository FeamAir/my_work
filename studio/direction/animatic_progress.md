# S01E01 animatic v1 — progress checklist (resume file)

Updated: 2026-11-24 — **animatic v1 COMPLETE**. Next: director/studio viewing → v2 fixes (notes §3) → picture lock. Tools: `studio/direction/animatic_tools/`. Outputs: `output/S01E01/animatic/`.
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
| 4 | Spec + assemble + overlay | DONE: `S01E01_animatic_v1.mp4` 28:18.75, −14.1 LUFS, −1.3 dBTP | — |
| 5 | R2 upload | DONE (final mp4, raw, la_concat, frames 375, rejects 37, la 451, drafts, audio, spec, mix_report) | — |
| 6 | Notes `S01E01_animatic_v1_notes.md`, report, HANDOFF | DONE | — |

## v2 — the 21:30 cut (2026-11-24) — COMPLETE

Studio director's decisions on v1 → `direction/S01E01_animatic_v2_notes.md`. Budget guard for this step: `STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=55`, paid only the 2 restaged frames (max 3 takes each).

| # | Step | Status | How to resume |
|---|---|---|---|
| v2-1 | Cut + re-time (386 shots, 21:29.75, hook 2:58.25) | DONE | `python3 -I animatic_tools/cut_v2.py write` |
| v2-2 | Restaged frames sc02-sh050, sc04-sh180 (NB2, 1 take each, $0.16) | DONE, awaiting the lead writer's approval | `restage_v2.py run/accept` |
| v2-3 | LA of 264 changed shots → `la_v2/` | DONE | `cut_v2.py la` (FORCE=1 to redo) |
| v2-4 | spec / assemble / master (LRA fix) / overlay | DONE: −14.7 LUFS, −1.6 dBTP, LRA 10.9 | `ANIM_V=v2 python3 -I animatic_tools/spec.py build|assemble|master|overlay` |
| v2-5 | R2 upload `S01E01/animatic/` (mp4, raw, master wav, la_concat_v2, la_v2/, spec, frames) | DONE | — |
