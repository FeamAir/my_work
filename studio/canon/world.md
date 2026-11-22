# World

Canon: v0.1 · Status: **empty** — to be filled from the lead screenwriter's world document.

Holds: laws of the world, magic / technology and their limits, geography (places), calendar. Everything that is true everywhere and at all times (or that changes only through recorded events).

---

## 1. Premise (prose, 1 paragraph)

_Setting type (fantasy / SF / mix), tone, what makes this world different. Filled by the lead screenwriter, recorded by the keeper._

## 2. World rules

A world rule is a law that scripts may never break without a recorded exception. Magic and technology must have **costs and limits**: they make plots possible and keep mysteries fair.

Blank record:

```canon-template
id: RULE-NNN
type: world_rule
canon: draft
area:            # magic | technology | biology | society | religion | law | economy
rule:            # one sentence, testable
cost:            # what it costs to use / break
limit:           # what it can never do
known_publicly:  # true | false (if false, link a secret in secrets.md)
```

Below the block (prose): how it looks on screen, examples, known exceptions (each exception links a `SEC-` or `EV-`).

## 3. Society and power

_Classes (poor, middle, rich, rulers), how power is inherited, law and courts, money, religion. One subsection each; houses are in `houses/`._

## 4. Calendar

Exactly one calendar record. Eras (how years are counted) are in `timeline.md`.

```canon-template
id: CAL-MAIN
type: calendar
canon: draft
month_days: [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
month_names: [ ... ]
week_days: 7
```

Prose: names of days, seasons, festivals, how characters say dates aloud.

## 5. Geography (places)

One record per place that appears in scripts or on maps. Hierarchy by `parent` (continent → region → city → district → building).

```canon-template
id: PL-NNNN
type: place
canon: draft
name:
kind:            # continent | region | city | town | village | castle | district | building | sea | river | ...
parent:          # PL-…
held_by:         # HS-… (current holder; history goes to timeline events)
climate:
```

Prose: what it looks like (for the art team), who lives there, what it is famous for, travel times to neighbours.

### Travel times

Travel times between key places (so that "who is where" can be checked):

| From | To | On foot | Horse / vehicle | Fastest possible | Notes |
|---|---|---|---|---|---|
| | | | | | |

---

## EXAMPLE (placeholder, not canon)

```canon
id: CAL-EX-MAIN
type: calendar
canon: draft
example: true
month_days: [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 35]
month_names: [Thaw, Seed, Rain, Bloom, Sun, High, Gold, Reap, Mist, Frost, Dark, Long]
week_days: 6
```

```canon
id: RULE-EX-001
type: world_rule
canon: draft
example: true
area: magic
rule: Saltreading shows the reader one true memory of whoever last touched the salt.
cost: The reader loses the memory of the same day of their own life.
limit: Never shows the future; never works on the dead.
known_publicly: true
```

```canon
id: PL-EX-0001
type: place
canon: draft
example: true
name: Saltmere
kind: region
climate: cold coast, salt marshes
```

```canon
id: PL-EX-0002
type: place
canon: draft
example: true
name: Greyhold
kind: castle
parent: PL-EX-0001
held_by: HS-EX-001
```

Greyhold (EXAMPLE): a low grey keep on a tidal island; reachable on foot only at low tide.
