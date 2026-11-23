# Video model test — 2026-11-23

3 shots × 3 models, 5 s each, image-to-video. Sources: `refs/PL-0008/D02_C1_dawn-ebb_v1.png` (alley, no people), `refs/keyframes/styletest_pell_ladder_v1.png` (action), `refs/keyframes/styletest_pell_closeup_v1.png` (close-up). Prompts: `meta.json`. Clips: R2 `video_test/2026-11-23/`. Frame grids: `rev_*.jpg` (rows: MiniMax H3 Max Turbo 768P · Kling 2.5 Turbo Pro · Kling 3 Pro; columns: frames 0/60/119).
Cost: $3.33 (MiniMax $0.20, Kling 2.5 $0.35, Kling 3 Pro $0.56 per clip; prices verified in fal catalog, MiniMax promo ended Nov 16 — old estimate $0.09 was wrong).

| Shot | MiniMax H3 Max Turbo (768P) | Kling 2.5 Turbo Pro (1080p) | Kling 3 Pro (1080p, no audio) |
|---|---|---|---|
| Alley ambient | ✗ brightened the whole scene, lit the lantern, **drew glowing marks on the silt** (forbidden magic glow) | ✓ subtle, stable, light unchanged | ~ stable, lit the lantern amber (light change not asked) |
| Pell on ladder | ~ action done; net bag drifts into the jacket mid-clip | ✓ best: action done, character stable, braid swings | ~ adds unrequested action (turns away at the end), costume simplifies in back view |
| Close-up | ✓ calm, stable, adds mist | ✓ stable, clean blink | ✗ turns head to profile (unrequested), braid side logic breaks |

## Decision (director, 2026-11-23)
- **Class C (action) and default for any character motion → Kling 2.5 Turbo Pro** ($0.07/s). Most obedient, no drift.
- **Class B (cheap motion) → MiniMax H3 Max Turbo 768P** ($0.04/s, upscale locally) **only for character close-ups/medium shots with subtle motion**; environments/water/light → Kling 2.5 or LA (ffmpeg). Prompt must add: "no new light sources, lighting unchanged, no glowing marks".
- **Class D (hero) → Kling 3 Pro** only where Kling 2.5 fails twice or 6–15 s continuous change is needed; prompt must say "the character does not turn around / does not turn her head unless stated".
- Wording rule for all video prompts: list what must NOT change (light, costume, head direction).
- Re-test MiniMax on 2–3 more character shots during animatic drafts before relying on it.
