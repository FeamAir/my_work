# Timeline

Canon: v0.1 · Status: **empty**.

The timeline holds three kinds of records:

1. **Eras** — how years are counted (needed to compare any two dates).
2. **Events** — anything with a date: wars, coronations, foundings, conquests, murders, births that matter to the plot (normal births/deaths stay in character records).
3. **Episodes** — the in-world dates each episode covers.

## Date format

`ERA YYYY[-MM[-DD]]` — e.g. `AE 981`, `AE 981-04`, `AE 981-04-12`.
- `~AE 981` = about (±1 year). `?` = unknown.
- Months and their lengths come from the calendar in `world.md`.
- Every era counts **forward** from year 1. For the comparison tool each era has `abs_start` = absolute year number of its year 1 (an arbitrary common scale). Example: era OLD starts at abs 0, era NEW at abs 1200 → `NEW 1` comes after `OLD 1200`.
- Characters in dialogue may use other dating ("the third winter after the Burning"); the canon always stores the formal date.

## 1. Eras

```canon-template
id: ERA-ABBR
type: era
canon: draft
abbr:           # 1-6 capital letters, used in dates
name:
abs_start:      # integer
ended_by:       # EV-… that ended the era (optional)
```

## 2. Before the saga (history)

Ordered by date. Each important event is one record; prose under it can tell the story (as it really happened — and, separately, as people *believe* it happened, linking the secret).

```canon-template
id: EV-NNNN
type: event
canon: draft
name:
date:           # ERA YYYY[-MM[-DD]] or ?
date_end:       # optional, for wars, sieges, reigns
place:          # PL-…
houses: []      # HS-… involved
participants: []# CH-… present
killed: []      # CH-… who die here (must match their died date)
secrets: []     # SEC-… if the public version is false
episode:        # SxxEyy if shown on screen; add flashback: true if shown out of order
```

Prose: what happened / what people believe happened / consequences.

## 3. During the saga (by episode)

One episode record per episode, filled when the episode outline is approved. Dates are in-world dates covered by the episode's present-day story (flashbacks are events with `flashback: true`).

```canon-template
id: SxxEyy
type: episode
canon: draft
title:
date_start:
date_end:
pov: []         # CH-… main point-of-view characters
```

## 4. Season overview

| Season | In-world dates | Main arc | Key events (EV-…) | Secrets revealed (SEC-…) |
|---|---|---|---|---|
| S01 | | | | |

---

## EXAMPLE (placeholder, not canon)

```canon
id: ERA-EX-OT
type: era
canon: draft
example: true
abbr: OT
name: Old Tides
abs_start: 0
```

```canon
id: ERA-EX-SR
type: era
canon: draft
example: true
abbr: SR
name: Salt Reckoning
abs_start: 600
ended_by:
```

```canon
id: EV-EX-0001
type: event
canon: draft
example: true
name: Founding of House Varnel
date: SR 120
place: PL-EX-0002
houses: [HS-EX-001]
participants: [CH-EX-0001]
```

```canon
id: EV-EX-0002
type: event
canon: draft
example: true
name: The Low-Tide Drowning
date: SR 146-11-03
place: PL-EX-0002
houses: [HS-EX-001]
killed: [CH-EX-0001]
secrets: [SEC-EX-001]
episode: S01E02
flashback: true
```

Prose (EXAMPLE): Publicly, Oren Varnel drowned crossing to Greyhold. In truth — see SEC-EX-001.

```canon
id: S01E01
type: episode
canon: draft
example: true
title: Low Water
date_start: SR 162-03-01
date_end: SR 162-03-04
pov: [CH-EX-0003]
```

```canon
id: S01E02
type: episode
canon: draft
example: true
title: Salt Memory
date_start: SR 162-03-05
date_end: SR 162-03-09
pov: [CH-EX-0003]
```
