# Secrets registry

Canon: v0.1 · Status: **empty**. **Full spoilers — never use in public material before the reveal episode.**

This is the main tool for mysteries that pay off across seasons. Every hidden truth in the saga — false parentage, secret alliances, murders disguised as accidents, a hero's link to events long before the story, political frauds the common people never learn — is one record here.

## Fields

```canon-template
id: SEC-NNN
type: secret
canon: draft
title:              # short working name (internal)
tier:               # saga | season | episode  (scale of the mystery)
truth:              # the real fact, one sentence
cover_story:        # what people believe instead
status:             # sealed (no hints aired) | seeded (hints aired) | revealed
known_by: []        # [CH-…@origin, CH-…@S02E04]  who knows, and from which episode
hints: []           # episodes where clues are planted, in order
reveal:             # SxxEyy where the AUDIENCE learns the truth
public_on_reveal:   # true if the whole world learns it at reveal; false if only some characters
min_seasons_hidden: # planned minimum gap (seasons) between first hint and reveal
depends_on: []      # SEC-… that must make sense first
related: []         # CH-/HS-/EV-/PL- … ids involved
```

Below each block (prose):
- **Clues** — table: episode → what exactly is shown/said (so a re-watch makes it fair).
- **Red herrings** — false leads and where they are planted.
- **Fan-theory hooks** — what the audience may guess, and what they should *not* guess too early.
- **Consequences of the reveal** — who changes sides, who dies, which houses fall.

## Rules

1. A secret is **fair**: at least two hints before the reveal, the first at least one season earlier for `tier: saga`.
2. Hints are listed in episode order and all come before `reveal` (checked automatically).
3. `known_by` is the only place that says who knows what. A character cannot act on a secret before their `@episode` (checklist), and the dead learn nothing (checked automatically).
4. When a character learns a secret on screen, the keeper adds `CH-…@SxxEyy` here.
5. When a hint airs: `status: seeded`; when the reveal airs: `status: revealed`, and the record becomes `locked`.
6. Secret IDs never appear in public-facing files (marketing, subtitles).

## Overview

| ID | Title | Tier | First hint | Reveal | Status |
|---|---|---|---|---|---|
| | | | | | |

---

## EXAMPLE (placeholder, not canon)

```canon
id: SEC-EX-001
type: secret
canon: draft
example: true
title: The heron's true father
tier: season
truth: Tamsin is the daughter of Brannoch Hale, and Oren Varnel was drowned by Brannoch on purpose.
cover_story: Tamsin is Oren's daughter; Oren drowned by accident at low tide.
status: seeded
known_by: [CH-EX-0004@origin, CH-EX-0002@origin, CH-EX-0003@S01E02]
hints: [S01E01]
reveal: S01E02
public_on_reveal: false
min_seasons_hidden: 0
related: [CH-EX-0001, CH-EX-0003, CH-EX-0004, EV-EX-0002]
```

Clues (EXAMPLE):

| Episode | Clue |
|---|---|
| S01E01 | Brannoch's scar on the right palm matches Tamsin's salt-burn birthmark. |
