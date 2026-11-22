# World

Canon: v0.2 · Status: **approved** (foundation r2, approved by the director 2026-11-22; transfer by lore-keeper)

Source: `studio/story/` r2 (series_bible, houses_overview, cast_overview, saga_arc, season01_outline, franchise) and `studio/story/sealed/master_mystery.md` (sealed parts only in `sealed/`).

Holds: laws of the world, magic / technology and their limits, society, calendar, geography (places), saga objects. Eras are in `timeline.md`. Pronunciation of every name: `glossary.md`.

---

## 1. Premise

**THE LOW NOTE.** The Concord of Tessary is a great river delta and barrier archipelago at the mouth of the Aun, most of it below sea level. It stays dry only because of nine colossal towers of black singing stone - the Spires - publicly believed to be the work of a vanished race (the Builders). When a trained Cantor sings into a Spire, the stone answers and the sea obeys. Whoever holds a Spire decides which districts stay dry. The Helm is elected for life by a Conclave of eight votes; money is paper printed by a bank against deeds to dry land; the poor live below the waterline, pay a dry-tithe and are forbidden by law to sing. The Spires have been slowly detuning for three centuries. Low fantasy with one law of wonder: no dragons, prophecies, chosen ones or levels. Rating TV 16+.

## 2. World rules

A world rule is a law that scripts may never break without a recorded exception. Each has a cost and a limit. Rules whose truth is restricted live in `sealed/` (RULE-013, RULE-014).

```canon
id: RULE-001
type: world_rule
canon: approved
area: magic
rule: A person with the ear, singing a sustained true tone into a Spire, makes it answer: water within the Spire's sight-line is held back, turned or calmed.
cost: The singer's voice: every song roughens it, a long song leaves a Cantor hoarse for days, a Great Song (hours) can take it forever. A singer with no voice left who keeps singing pays with breath and dies (singing out). A mute Cantor can still force one unvoiced breath-tone; the Spire answers it weakly and takes the breath.
limit: Moves and holds water only (never creates, destroys, heats or poisons it); only within sight of the Spire's crown (~30 km clear, less in fog or rain); one voice holds a Great Song for a few hours at most.
known_publicly: true
```

On screen: black glassy spiral-grooved towers (60-200 m) crowned by a ring of open "throats"; when sung, a deep hum, the grooves glow faint blue-white, water within sight flattens like glass. The singing Cantor stands in a throat, back to camera - the iconic lip-sync-free shot. First singing-out on screen: Cantor Sabin, S01E10.

```canon
id: RULE-002
type: world_rule
canon: approved
area: biology
rule: The ear - the ability to make a Spire answer - is rare; publicly it is believed to be inherited in the songblood of the great houses, above all Ilvane.
cost: Children found with the ear are gleaned into the Choir.
limit: Without the ear, singing into a Spire does nothing.
known_publicly: true
secrets: [SEC-005]
```

The belief only. The truth is SEC-005.

```canon
id: RULE-003
type: world_rule
canon: approved
area: magic
rule: A Spire not sung each day, or sung badly, detunes and its answer weakens; a fully silent Spire lets the sea in within days; every Spire has lost some tone over 312 years (publicly: because the stone is old).
cost: Districts in sight of a weak Spire flood more often.
limit: Detuning is slow (years) unless a Spire is damaged or deliberately left unsung.
known_publicly: true
secrets: [SEC-008]
```

The public cause (old stone) is a belief; the real cause is in SEC-008 and the sealed part.

```canon
id: RULE-004
type: world_rule
canon: approved
area: technology
rule: Echo-stones (chips of Spire stone) ring in sympathy with a Spire's tone; the Relay sends coded tones Spire to Spire across the delta in minutes.
cost: Relay fees; stones crack after heavy use; an unlicensed echo-shard is a crime.
limit: Simple tone-codes only, no speech; anyone with a stone and the codebook can read; line of sight only; stones ring only on the Spires' known home-tones - keepers' lore: very old stones ring low and are thrown back as unlucky.
known_publicly: true
secrets: [SEC-002]
```

Relay stones are cut from living, solo-sung Spires and ring only on the high home-tones (why no keeper ever heard the lullaby answered). Pell's shard is the exception (SEC-002; origin sealed).

```canon
id: RULE-005
type: world_rule
canon: approved
area: magic
rule: Hollowstone cannot be carved, cast or made (public belief); no new Spire has been raised in recorded history.
cost: -
limit: -
known_publicly: true
secrets: [SEC-014]
```

```canon
id: RULE-006
type: world_rule
canon: approved
area: law
rule: The Hush Law (since CY 1): no commoner may sing within sight of a Spire; work-chants, clapping, whistling and wordless drumming are allowed.
cost: Punishment: a night on the tide-post at low tide in the Lows.
limit: Applies to commoners; Cantors and nobles are exempt.
known_publicly: true
secrets: [SEC-003]
```

Lows culture is percussive and whistled - a deliberate sonic identity for the composer.

```canon
id: RULE-007
type: world_rule
canon: approved
area: technology
rule: Pumps (wind and treadmill, walked by paid or indebted labourers) lift water one dike-step.
cost: Huge labour; treadmill debt-walkers are the poorest of the poor.
limit: Cannot replace a Spire: ~400 walkers working a day undo one hour of a Spire's silence.
known_publicly: true
secrets: [SEC-028]
```

```canon
id: RULE-008
type: world_rule
canon: approved
area: technology
rule: Powder: matchlock muskets, ship cannon, siege guns.
cost: Saltpeter comes mainly from the Ossari uplands.
limit: Damp and rain make powder unreliable; pike, crossbow and blade still decide most fights.
known_publicly: true
```

```canon
id: RULE-009
type: world_rule
canon: approved
area: law
rule: The Conclave of eight votes elects the Helm for life by 5 of 8; in a 4-4 tie the Sunken Vote is cast by whoever holds Lirenne, and while Lirenne is under water the First Cantor speaks for the drowned.
cost: -
limit: The Helm can be removed only by a unanimous Conclave or by death.
known_publicly: true
```

```canon
id: RULE-010
type: world_rule
canon: approved
area: ritual
rule: The Still Days: five days at year's end when the Choir retunes every Spire in turn, each silent for hours; elections are by law held on the Still Days.
cost: The most dangerous days of the year: floods, sabotage, riots.
limit: -
known_publicly: true
```

```canon
id: RULE-011
type: world_rule
canon: approved
area: metaphysics
rule: Death is final: no resurrection, no acting ghosts, no prophecy, no mind-reading, no shapeshifting; visions are dreams or lies.
cost: Every death is real; every mystery is solvable by human means.
limit: Return only from missing or presumed_dead.
known_publicly: true
```

```canon
id: RULE-012
type: world_rule
canon: approved
area: magic
rule: A Spire sung by solo voices without the low part cannot hold the sea by itself: it draws fresh water toward itself, and the pull passes Spire to Spire in sympathy up the delta to the Falls Spire, whose sight-line covers the plateau rim and the Shelf lakes.
cost: The Aun runs fuller in the delta (more river floods); the plateau drains faster than rain refills it.
limit: Works only through RULE-001 (sight-line) and RULE-004 (sympathy); never makes water.
known_publicly: false
secrets: [SEC-008]
```

Added by the keeper from the foundation's mechanism of SEC-008 (master file r2 §4); not public. Clues: falls swell with no rain when the Falls Spire is sung (S03E08); the falls run thin and Shelf wells rise when the Sluice Spire is sung by many (S05E12).

## 3. Society and power

### 3.1 The three tiers

| Tier | Who | How they live | Their schemes |
|---|---|---|---|
| **the Lows** (PL-0007; ~60%) | mudlarks, sluice-workers, salt-rakers, treadmill walkers, boat-people | below sea level; pay the dry-tithe; flood every few years; forbidden to sing | smuggling echo-shards; the Undertow's dry-pledges; rumour networks; secret singing; salvage fights; fake drownings to escape debts |
| **the Mids** (PL-0006; ~30%) | clerks, pumpwrights, relay-keepers, soldiers, shopkeepers, low clergy | dike level; dry unless a big breach | the Pumpwrights' breakage; clerks forge, skim and sell ledger secrets; relay-keepers sell messages early; soldiers sell gate passes in floods |
| **the Steps** (PL-0005; ~10%) | great houses, bankers, Cantors, Conclave | granite hill and crags; never flood | vote-buying; grain cornering; flood speculation; falsified relay messages; the Choir's priority songs |

### 3.2 Power
- **Spires = votes = water.** A great house holds a Spire, therefore a vote, therefore a say over the Tithe Map.
- **The Helm** (elected for life, RULE-009) commands the Concord fleet, holds the Crown Spire in trust, signs the Tithe Map. Addressed "Helm" or "Your Steadiness". Seat: the Dry Palace (PL-0009).
- **The Conclave** (the Ring, PL-0010), 8 votes: Corvane, Dask, Ilvane, Rusk, Quell, Fennick, the Choir, Lantry (the Purchased Seat). Ninth, vacant: the Sunken Vote.
- **Board at CY 312:** Crown Spire - the Helm in trust · Choir Spire - the Choir · Sluice Spire (failing) - Fennick · Sentinel - Corvane · Sheaf - Dask · Pale - Ilvane · Falls - Rusk · Storm - Quell · Sunken (silent) - nobody. Lantry holds a vote and no Spire.
- **Law:** Fennick runs the Hearings and the Relay; commoners cannot testify against a noble without a Mids sponsor.
- **Army and fleet:** each great house keeps its own troops; the fleet is mostly Corvane ships under the Helm's flag; free companies are paid in dry-notes.

### 3.3 Money
- **Marks** - silver coin, scarce. **Dry-notes** - Lantry paper backed by deeds to dry land; when land floods its notes are worthless (the central scheme of Acts I-II, SEC-007). **Dry-tithe** - protection tax of every Lows household to the holder of the nearest Spire. **Grain** - mostly Dask. **Saltpeter** (uplands) and **echo-stones** (Relay) - strategic goods.

### 3.4 Religion
- **The Choir** (HS-090) - official faith and order of Cantors; venerates the First Voices and the Spires as their gift; novices trained from childhood; children with the ear are gleaned.
- **The Lady Below** - Lows folk faith: the sea as a drowned mother who takes back what she is owed; offerings of salt and shells; sign: the spiral shell. Tolerated, mocked by the Steps.

## 4. Calendar

```canon
id: CAL-MAIN
type: calendar
canon: approved
month_days: [36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 5]
month_names: [Firstwater, Rains, Silting, Reedmonth, Highsun, Saltdry, Ember, Fallow, Mistcall, Longdark, Still]
week_days: 6
```

- 10 months of 36 days + **Still** (the 5 Still Days, RULE-010) = 365 days. The year begins on Firstwater 1, the morning after the last Still Day.
- **Week (6 days):** Humday, Reedday, Bellday, Drumday, Hornday, Restday.
- **Seasons:** the Wet (Firstwater-Silting), the Green (Reedmonth-Saltdry), the Ember (Ember-Fallow; hottest, low water), the Mist (Mistcall-Longdark; storms), then the Still Days.
- **Spoken dates:** "the ninth of Fallow", "three days before the Still". Lows people count years by floods ("two floods after the Still Water"). The canon always stores the formal date (`CY 312-10-06` = Longdark 6, CY 312).

## 5. Geography (places)

Hierarchy by `parent`. Spires are places (`kind: spire`); the Crown Spire has no house holder (the Helm's office).

```canon
id: PL-0001
type: place
canon: approved
name: the Concord of Tessary
kind: realm
climate: river delta and barrier archipelago, mostly below sea level; wet
```

The realm at the mouth of the Aun, kept dry by nine Spires.

```canon
id: PL-0002
type: place
canon: approved
name: the Aun
kind: river
parent: PL-0001
```

Falls ~300 m from the Ossari plateau at the Red Escarpment, then crosses the Polders and the Many Mouths.

```canon
id: PL-0003
type: place
canon: approved
name: the Many Mouths
kind: region
parent: PL-0001
climate: canals, reed islands
```

The delta proper.

```canon
id: PL-0004
type: place
canon: approved
name: Highwater
kind: city
parent: PL-0003
```

Capital on a granite hill in mid-delta, three tiers: the Steps, the Mids, the Lows. Three Spires: Crown, Choir, Sluice.

```canon
id: PL-0005
type: place
canon: approved
name: the Steps
kind: district
parent: PL-0004
```

Nobles, the bank, the Dry Palace, the Ring; never floods. Includes the grand stair where Ruel is stabbed (S01E08).

```canon
id: PL-0006
type: place
canon: approved
name: the Mids
kind: district
parent: PL-0004
```

Dike level: clerks, crafts, guilds, barracks.

```canon
id: PL-0007
type: place
canon: approved
name: the Lows
kind: district
parent: PL-0004
```

Below sea level: stilt houses, flooded lanes, sluice districts numbered First to Twelfth.

```canon
id: PL-0008
type: place
canon: approved
name: Ninth Sluice
kind: district
parent: PL-0007
```

Our home district ("the Ninth"). Flooded CY 295 (EV-0200) and CY 312 (EV-0305).

```canon
id: PL-0009
type: place
canon: approved
name: the Dry Palace
kind: building
parent: PL-0005
```

Seat of the Helm; tithe hall (Tithe Map reading, S01E01).

```canon
id: PL-0010
type: place
canon: approved
name: the Ring
kind: building
parent: PL-0005
```

The Conclave chamber: eight seats and one empty chair draped in teal for the Sunken Vote.

```canon
id: PL-0011
type: place
canon: approved
name: the Lantry Counting House
kind: building
parent: PL-0005
held_by: HS-007
```

The bank: counting hall, private office, archive. Burns S06E09.

```canon
id: PL-0012
type: place
canon: approved
name: the Listening House
kind: building
parent: PL-0004
held_by: HS-006
```

Seat of House Fennick, the Relay and the Hearings. Tier not fixed by the foundation.

```canon
id: PL-0013
type: place
canon: approved
name: the Choir temple
kind: building
parent: PL-0004
held_by: HS-090
```

Temple and school of the Choir; its sealed archive lies under the Choir Spire (S8).

```canon
id: PL-0014
type: place
canon: approved
name: the Crown Spire
kind: spire
parent: PL-0009
```

Held by the sitting Helm in trust. Ione sings it in S01E01 and dies on it in S04E11.

```canon
id: PL-0015
type: place
canon: approved
name: the Choir Spire
kind: spire
parent: PL-0013
held_by: HS-090
```

```canon
id: PL-0016
type: place
canon: approved
name: the Sluice Spire
kind: spire
parent: PL-0007
held_by: HS-006
```

Failing; under-sung to save Cantor fees. Ex-Harrow (to Fennick CY 251).

```canon
id: PL-0017
type: place
canon: approved
name: the Ilvane townhouse
kind: building
parent: PL-0005
held_by: HS-003
```

```canon
id: PL-0018
type: place
canon: approved
name: Highwater harbour
kind: harbour
parent: PL-0004
```

Where the Corvane flagship *Patient Gull* lies in S1.

```canon
id: PL-0019
type: place
canon: approved
name: Nan's stilt-house
kind: building
parent: PL-0008
```

Home of Nan, Pell and Wick; Nan's net-chest hides the shard and the ledger copy. Ruined in the flood (S01E10).

```canon
id: PL-0020
type: place
canon: approved
name: the Ninth Sluice back-canal
kind: canal
parent: PL-0008
```

By the old sluice, where Pell finds the shard at the lowest ebb (S01E01).

```canon
id: PL-0021
type: place
canon: approved
name: the Ninth Sluice evacuation gate
kind: gate
parent: PL-0008
```

Gate from the Lows to the Mids; shut CY 295, opened by Kes S01E10.

```canon
id: PL-0022
type: place
canon: approved
name: the Ninth Sluice tide-post
kind: landmark
parent: PL-0008
```

The punishment post (RULE-006). Recurring motif: S01E03, S05E01, S05E11, S07E01, S09E12, S12E13.

```canon
id: PL-0023
type: place
canon: approved
name: Mother Silt's barge
kind: barge
parent: PL-0007
held_by: HS-093
```

Barge-palace of the Undertow.

```canon
id: PL-0024
type: place
canon: approved
name: Hollis's garret
kind: building
parent: PL-0006
```

```canon
id: PL-0026
type: place
canon: approved
name: the Sluice Gates
kind: locks
parent: PL-0004
```

City locks of Highwater; battle S02E11.

```canon
id: PL-0027
type: place
canon: approved
name: the Ninth Bridge
kind: bridge
parent: PL-0003
```

Battle S09E10. Exact position: with the S9 outline.

```canon
id: PL-0028
type: place
canon: approved
name: the Hundred Locks
kind: locks
parent: PL-0003
```

Battle S07E11. Exact position: with the S7 outline.

```canon
id: PL-0030
type: place
canon: approved
name: Gullmouth
kind: city
parent: PL-0003
held_by: HS-001
```

Corvane naval port at the main river mouth.

```canon
id: PL-0031
type: place
canon: approved
name: the Sentinel Spire
kind: spire
parent: PL-0030
held_by: HS-001
```

```canon
id: PL-0032
type: place
canon: approved
name: the Ostry harbour-forts
kind: fort
parent: PL-0030
held_by: HS-001
```

Old forts of House Ostry (absorbed ~CY 120).

```canon
id: PL-0035
type: place
canon: approved
name: the Polders
kind: region
parent: PL-0001
held_by: HS-002
climate: reclaimed grain flats behind dikes
```

Dask grain country; deliberately flooded in S10 (EV-0334).

```canon
id: PL-0036
type: place
canon: approved
name: Dask Barrows
kind: seat
parent: PL-0035
held_by: HS-002
```

```canon
id: PL-0037
type: place
canon: approved
name: the Sheaf Spire
kind: spire
parent: PL-0035
held_by: HS-002
```

```canon
id: PL-0038
type: place
canon: approved
name: the Moll polders
kind: region
parent: PL-0035
held_by: HS-002
```

Lands of House Moll (conquered CY 88); still restless.

```canon
id: PL-0040
type: place
canon: approved
name: Pale Crag
kind: cloister
parent: PL-0003
held_by: HS-003
```

Ilvane cliff-cloister and Choir school; crypt with the infant grave and the rack of "spears of the Breaking".

```canon
id: PL-0041
type: place
canon: approved
name: the Pale Spire
kind: spire
parent: PL-0040
held_by: HS-003
```

```canon
id: PL-0045
type: place
canon: approved
name: the Red Escarpment
kind: escarpment
parent: PL-0001
```

Where the Aun falls ~300 m from the plateau.

```canon
id: PL-0046
type: place
canon: approved
name: the Stair
kind: fortress-town
parent: PL-0045
held_by: HS-004
```

Rusk fortress-town cut into the escarpment beside the falls; the only easy road from the uplands. Ex-Vanth (to Rusk CY 141). Falls to the Ossari in S3 (EV-0311).

```canon
id: PL-0047
type: place
canon: approved
name: the Falls Spire
kind: spire
parent: PL-0046
held_by: HS-004
```

Held by Rusk at CY 312; captured by the Ossari in S3 and silenced (S4); Weir Terms CY 314.

```canon
id: PL-0048
type: place
canon: approved
name: the falls of the Aun
kind: waterfall
parent: PL-0045
```

```canon
id: PL-0049
type: place
canon: approved
name: the weir
kind: weir
parent: PL-0048
held_by: HS-091
```

Built by the Ossari at the lip of the falls in CY 314 (EV-0313); breached on the third Still Day CY 314 (EV-0315).

```canon
id: PL-0050
type: place
canon: approved
name: the Ossari Uplands
kind: plateau
held_by: HS-091
climate: dry, windy plateau; terraced towns
```

Outside the Concord. Kites, gliders, saltpeter.

```canon
id: PL-0051
type: place
canon: approved
name: the Shelf lakes
kind: lake
parent: PL-0050
```

On the plateau rim in sight of the Stair: the Aun's headwaters and the plateau's last standing water (r2).

```canon
id: PL-0055
type: place
canon: approved
name: the Shoals
kind: islands
parent: PL-0001
held_by: HS-005
```

Quell barrier islands: salt pans, wreckers' lights, smugglers. Staging camp of the First Raising (S09E05).

```canon
id: PL-0056
type: place
canon: approved
name: Brackwater
kind: town
parent: PL-0055
held_by: HS-005
```

```canon
id: PL-0057
type: place
canon: approved
name: the Storm Spire
kind: spire
parent: PL-0055
held_by: HS-005
```

```canon
id: PL-0060
type: place
canon: approved
name: the Sunk
kind: sea
parent: PL-0001
```

Shallow sea over drowned Lirenne.

```canon
id: PL-0061
type: place
canon: approved
name: Lirenne
kind: city
parent: PL-0060
```

Old capital of the Tide-Kings, under the sea since OS 700 (EV-0100). Raised S11E12 (EV-0337).

```canon
id: PL-0062
type: place
canon: approved
name: the Sunken Spire
kind: spire
parent: PL-0061
```

Silent; its crown shows at very low tide. Carries the Sunken Vote (RULE-009).

```canon
id: PL-0065
type: place
canon: approved
name: the Open Grey
kind: ocean
```

The ocean beyond the Sunk.

### Travel times

| From | To | On foot | Boat / barge | Fastest | Notes |
|---|---|---|---|---|---|
| Highwater | Gullmouth | - | 1 day by canal barge | 6 h by fast boat |  |
| Highwater | the Stair | - | 6 days upstream by river | 4 days downstream | S01E12 tag is stamped "six days later" |
| Highwater | Pale Crag | - | 1 day | - |  |
| Highwater | Brackwater | - | 2 days by sail | - |  |
| Highwater | Lirenne shallows | - | 3 days by sail | - |  |
| anywhere in the delta | anywhere in sight of a Spire | - | - | minutes (Relay tone-code) | line of sight only (RULE-004) |

Travel times not given by the foundation (the Polders, the Shoals by land, the uplands on foot): to be set with the S2-S3 outlines.

## 6. Saga objects (custody)

Exact owners by episode. The objects' origins before the saga, where restricted, are in `sealed/`. No type of its own: objects are tracked here.

| Object | Description (story-level) | Custody |
|---|---|---|
| **Pell's echo-shard** | cracked black stone no bigger than a thumbnail, on a cord | found by Pell in the back-canal (PL-0020) S01E01 → hidden in Nan's net-chest S01E03 → Pell → Ione S04E08 → Pell S04E11 → Pell to the end (cracks further S09E05) |
| **Ruel's black pearl ring** ("the Admiral's Pearl") | black pearl, hinged and hollow, on Ruel's **left** hand | Ruel to S01E09 (on his hand at the wake) → Maren takes it at the wake and hides it S01E11 → hidden S2-S6 (Ysa knows she has it, S02E10) → worn openly by Maren from S06E12 → coronation S09E12 → Maren to S12E11 |
| **Hollis's brass ledger-clip** | brass clerk's clip | Ursel → Hollis S01E01 → Hollis (on every copy S2-S4) → found melted in the fire S06E09 → seen again S10E05 (Quire's seal), S11E06, S12E13 (see report: custody gap S06E09 → S10E05) |
| **Ione's tuning fork** | silver tuning-fork pendant | Ione S01E01 → Pell S04E12 → struck on a tide-post S05E01 → gives the Great Chorus its pitch S12E12 |
| **Nan's spiral-shell earring** | single spiral-shell earring, left ("it had a mate") | Nan S01E02 → Pell wears it from S02E08 (left ear) |
| **Wick's cap** | Maren's Corvane cadet cap | stolen by Wick S01E02 → worn on watch (S2, S5) → Maren finds it on his body at the Ninth Bridge S09E10 |
| **Corr's sawn pump-pin** | clean-sawn treadmill axle-pin | pocketed by Corr S01E10 → on Dorran's desk S05E08 |
| **Silt's book of sold men** | ledger | Mother Silt (from S04E10) → Tibb S09E05 → source of Pell's knowledge S10E11 |
| **Lucan's sealed chest / will** | the unsigned Tithe Map with Ursel's marginal notes | withheld by Garrick S01E12 → surfaces S02E06 |

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
