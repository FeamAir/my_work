# World

Canon: v0.4 · Status: **approved** (foundation r2, approved by the director 2026-11-22; §5a, §7, §8 approved by the lead screenwriter in r3, `studio/story/decisions_resolved.md`; transfer by lore-keeper)

Source: `studio/story/` r2 (series_bible, houses_overview, cast_overview, saga_arc, season01_outline, franchise) and `studio/story/sealed/master_mystery.md` (sealed parts only in `sealed/`).

Holds: laws of the world, magic / technology and their limits, society, calendar, geography (places), saga objects. Eras are in `timeline.md`. Pronunciation of every name: `glossary.md`.

---

## 1. Premise

**HOLLOWSTONE.** (Saga title since r3; *The Low Note* is Act II and Season 12 - and, in-world, the low part of the song.) The Concord of Tessary is a great river delta and barrier archipelago at the mouth of the Aun, most of it below sea level. It stays dry only because of nine colossal towers of black singing stone - the Spires - publicly believed to be the work of a vanished race (the Builders). When a trained Cantor sings into a Spire, the stone answers and the sea obeys. Whoever holds a Spire decides which districts stay dry. The Helm is elected for life by a Conclave of eight votes; money is paper printed by a bank against deeds to dry land; the poor live below the waterline, pay a dry-tithe and are forbidden by law to sing. The Spires have been slowly detuning for three centuries. Low fantasy with one law of wonder: no dragons, prophecies, chosen ones or levels. Rating TV 16+.

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
rule: A Spire not sung each day, or sung badly, detunes and its answer weakens; a fully silent Spire lets the sea in within days - within hours on a storm tide, or where the Spire is already failing; every Spire has lost some tone over 312 years (publicly: because the stone is old).
cost: Districts in sight of a weak Spire flood more often.
limit: Detuning is slow (years) unless a Spire is damaged or deliberately left unsung.
known_publicly: true
secrets: [SEC-008]
```

The public cause (old stone) is a belief; the real cause is in SEC-008 and the sealed part.

Amended in v0.4 (DEC-05): the clause "within hours on a storm tide, or where the Spire is already failing" keeps "days" true for healthy Spires (S4, S12) and explains the one-night flood of S1E10. S1E9 carries the line: *"The Sluice has been singing on two voices and a mute since the summer. Miss it one night in this weather and you won't have days."* (CY 312 census of the Sluice Spire: two voices and the mute Sabin - HS-090.)

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


## 5a. New places (v0.3; approved v0.4)

Status: **approved** (lead screenwriter, r3: PL-0070…0083). Source in each entry. The twelve sluices of the Highwater Lows are numbered First to Twelfth from the dike down to the sea; Cobbet wards the First to Fourth, Dunmore the Seventh to Twelfth (HS-013, HS-014). Only sluices that a character or event needs have a record.

```canon
id: PL-0070
type: place
canon: approved
name: the Rim
kind: region
parent: PL-0050
held_by: HS-091
```

Escarpment rim above the Stair: terrace forts, kite signal-towers; clan Den country. Held by the Ossari since the Stair Treaty (EV-0268). Source: writer-houses.

```canon
id: PL-0071
type: place
canon: approved
name: the Table House
kind: building
parent: PL-0005
held_by: HS-007
```

Harrow Hall, the old seat of House Harrow on the Steps; Lantry foreclosed on it in CY 252 and the partners of the Table sit here at one long black table. Kept "Harrow Hall" in the old Chronicle. Source: writer-houses.

```canon
id: PL-0072
type: place
canon: approved
name: Rimgate
kind: fort
parent: PL-0045
held_by: HS-025
```

The one terrace fort Rusk kept after the Kite War (EV-0270); seat of the Hadden border family. Source: writer-houses.

```canon
id: PL-0073
type: place
canon: approved
name: the Goat Stair
kind: path
parent: PL-0045
held_by: HS-025
```

Unguarded goat-path up the escarpment two miles from the Stair; the smugglers' and quartermasters' route (SEC-039). Source: writer-houses.

```canon
id: PL-0074
type: place
canon: approved
name: the Brackwater salt pans
kind: works
parent: PL-0055
held_by: HS-021
```

Salt pans of the inner islands; Clan Jutt. Source: writer-houses.

```canon
id: PL-0075
type: place
canon: approved
name: the Long Mole
kind: harbour work
parent: PL-0030
held_by: HS-001
```

Gullmouth's mile-long mole with lantern posts every hundred paces, built by Lady Admiral Edda (CY 44-71); berths inside it are the "storm-berths". Source: writer-houses.

```canon
id: PL-0076
type: place
canon: approved
name: the Concord Arsenal
kind: works
parent: PL-0006
held_by: HS-033
```

Arsenal and powder mills in the Highwater Mids; every barrel bears the Arsenal ring-stamp, "the Concord stamp". Source: writer-houses.

```canon
id: PL-0077
type: place
canon: approved
name: the Rusk House-in-Exile
kind: building
parent: PL-0006
held_by: HS-004
```

Leased barracks block in the Mids; seat of House Rusk from Mistcall CY 313 (after EV-0311). Source: writer-houses.

```canon
id: PL-0078
type: place
canon: approved
name: the Map Office
kind: office
parent: PL-0009
```

The Helm's Map Office in the Dry Palace, where the Inchley cartographers draw the Tithe Map. Source: writer-houses.

```canon
id: PL-0079
type: place
canon: approved
name: Hobb's Gate
kind: dike
parent: PL-0038
held_by: HS-002
```

Dike in the Moll polders where Lord Rawlin Moll was killed in the Furrow War (EV-0250). Source: keeper (named in the dossiers).

```canon
id: PL-0080
type: place
canon: approved
name: the Second Sluice
kind: district
parent: PL-0007
held_by: HS-006
```

Upper Lows (Cobbet wardens). Tuck's lane. Source: keeper (for writer-characters).

```canon
id: PL-0081
type: place
canon: approved
name: the Third Sluice
kind: district
parent: PL-0007
held_by: HS-006
```

Upper Lows (Cobbet wardens); Mother Silt's birthplace. Source: keeper (for writer-characters).

```canon
id: PL-0082
type: place
canon: approved
name: the Fourth Sluice
kind: district
parent: PL-0007
held_by: HS-006
```

Upper Lows (Cobbet wardens); Gant's treadmills. Source: keeper (for writer-characters).

```canon
id: PL-0083
type: place
canon: approved
name: the Fifth Sluice
kind: district
parent: PL-0007
held_by: HS-006
```

Middle Lows; Captain Fitch's birthplace (SEC-033). Source: keeper (for writer-characters).

### Travel times

| From | To | On foot | Boat / barge | Fastest | Notes |
|---|---|---|---|---|---|
| Highwater | Gullmouth | - | 1 day by canal barge | 6 h by fast boat |  |
| Highwater | the Stair | - | 6 days upstream by river | 4 days downstream | S01E12 tag is stamped "six days later" |
| Highwater | Pale Crag | - | 1 day | - |  |
| Highwater | Brackwater | - | 2 days by sail | - |  |
| Highwater | Lirenne shallows | - | 3 days by sail | - |  |
| anywhere in the delta | anywhere in sight of a Spire | - | - | minutes (Relay tone-code) | line of sight only (RULE-004) |

Overland and upland legs (DEC-64, approved; refined with the S2-S3 outlines only if a scene needs it):

| Leg | Time |
|---|---|
| Highwater → Dask Barrows | 2 days by barge up the Aun · 3 days by dike road |
| Dask Barrows → the Stair | 4 days upstream (Highwater → the Stair 6, as above) |
| the Stair → Dask Barrows → Highwater, downstream | 2½ + 1½ days (4, as above) |
| the Stair → the Rim (switchback road) | half a day; the Rim → the Shelf lakes: half a day |
| the Rim → the inner terrace towns | 2–3 days on foot; kite-signal along the Rim: minutes |
| Gullmouth ↔ Brackwater | 1 day by sail |
| an army on dike roads | ~20 km a day: Highwater → the Stair 12 days |
| a flood bore, the Stair → Highwater | about half a day (DEC-17): a bore does not tie up at night or wait at locks |

## 6. Saga objects (custody)

Exact owners by episode. The objects' origins before the saga, where restricted, are in `sealed/`. No type of its own: objects are tracked here.

| Object | Description (story-level) | Custody |
|---|---|---|
| **Pell's echo-shard** | cracked black stone no bigger than a thumbnail, on a cord | found by Pell in the back-canal (PL-0020) S01E01 → hidden in Nan's net-chest S01E03 → Pell → Ione S04E08 → Pell S04E11 → Pell to the end (cracks further S09E05) |
| **Ruel's black pearl ring** ("the Admiral's Pearl") | black pearl, hinged and hollow, on Ruel's **left** hand | Ruel to S01E09 (on his hand at the wake) → Maren takes it at the wake and hides it S01E11 → hidden S2-S6 (Ysa knows she has it, S02E10) → worn openly by Maren from S06E12 → coronation S09E12 → Maren to S12E11 |
| **Hollis's brass ledger-clip** | brass clerk's clip | Ursel → Hollis S01E01 → Hollis (on every copy S2-S4) → found melted in the fire S06E09 → (S06E10 → S10E05: `sealed/`, DEC-48) → seen again S10E05 (Quire's seal), S11E06, S12E13 |
| **Ione's tuning fork** | silver tuning-fork pendant | Ione S01E01 → Pell S04E12 → struck on a tide-post S05E01 → gives the Great Chorus its pitch S12E12 |
| **Nan's spiral-shell earring** | single spiral-shell earring, left ("it had a mate") | Nan S01E02 → Pell wears it from S02E08 (left ear) |
| **Wick's cap** | Maren's Corvane cadet cap | stolen by Wick S01E02 → worn on watch (S2, S5) → Maren finds it on his body at the Ninth Bridge S09E10 |
| **Corr's sawn pump-pin** | clean-sawn treadmill axle-pin | pocketed by Corr S01E10 → on Dorran's desk S05E08 |
| **Silt's book of sold men** | ledger | Mother Silt (from S04E10) → Tibb S09E05 → source of Pell's knowledge S10E11 |
| **Lucan's sealed chest** | a sealed chest: Lucan's will **and** the unsigned Tithe Map with Ursel's marginal hand and the Inchley draft marks (SEC-037) (DEC-49) | withheld by Garrick S01E12 ("everything but one sealed chest") → opened S02E06 |
| **The Breaking spears** ("the Ilvane spearheads") | white-bronze leaf-shaped spearheads stamped with the open hand of Ilvane; a rack kept as relics in the Pale Crag crypt. Public reading: "the spears that ended the mad Queen's guard" (DEC-12) | the Pale Crag crypt (PL-0040); first seen S02E05, again S03E06 |

## 7. Power and money (v0.3; approved v0.4)

Status: **approved** (writer-houses, `studio/story/houses/power_and_money.md`, 2026-11-22; merged by lore-keeper; approved by the lead screenwriter in r3; §7.10 stays a draft working sheet for the sound director). Laws and customs that the stories rely on are machine records RULE-015...024 (law / custom / economy); the text below is the dossier, with IDs updated. §5, §6 and §9 contain secrets (writers' room only).

```canon
id: RULE-015
type: world_rule
canon: approved
area: law
rule: A Conclave voice is cast by the head of the voting house or by a voice-bearer carrying the head's seal-ring; a bearer under 21 must be confirmed by the house's eldest adult member; the Choir's voice is cast by the First Cantor or her Voice; the Helm votes only through his own house.
cost: A young heir depends on the elder who confirms (Ysa's condition, S01E11).
limit: Confirmation is per vote.
known_publicly: true
```

Approved (DEC-03, r3): in S1 only this Ring law is spoken (S1E9, Odo's Challenge of the Voice: Maren is 19).

```canon
id: RULE-016
type: world_rule
canon: approved
area: law
rule: A Helm is elected on the first Still Days at least thirty days after the death or removal; the Master of the Hearings keeps the roll; any head of a voting house or anyone sponsored by two seats may stand; each pending Challenge of the Voice or of Precedence postpones the vote by one Still Day; the vote must be taken before dusk on the fifth Still Day; challenges go to the Hearings except when Fennick is a party (then the unchallenged seats decide); seats vote from the youngest seal to the oldest.
cost: Odo is judge in his own election everywhere but the Ring (S1).
limit: Interregnum: the Ring governs by simple majority of seats present; the last signed Tithe Map stays in force.
known_publicly: true
```

Approved (DEC-07, r3): the Night of a Thousand Voices is Still 3, CY 320 (EV-0319); the election follows on the Still Days of CY 321 (S6).

```canon
id: RULE-017
type: world_rule
canon: approved
area: law
rule: Since CY 1 one voice of the Ring - the Hill Voice, given to House Harrow for surrendering its Hill Spire to the Helm's office (the Crown Spire) - belongs to a house and not to a Spire; it can therefore be bequeathed (Lantry, CY 252) and is the precedent for Rusk's voice in exile and the Guild's claim.
cost: A standing quarrel: every vote of a voice without a Spire can be challenged.
limit: The Ring has never voted on the precedent.
known_publicly: true
```

Approved (DEC-02, r3).

```canon
id: RULE-018
type: world_rule
canon: approved
area: custom
rule: Sea Right of House Corvane: only one who has commanded a ship of the line becomes head; until then the eldest adult kin on land holds the seal in trust and confirms the heir's acts.
cost: Gives Lady Ysa legal power over Maren (S1-S2).
limit: House law of Corvane only.
known_publicly: true
```

Approved (DEC-03, r3): seen in S1E11 (the Corvane seal stays on Ysa's hand when she confirms Maren), first named in S2. Heads of HS-001 after Ruel: `houses/HS-001-corvane.md` (DEC-31).

```canon
id: RULE-019
type: world_rule
canon: approved
area: custom
rule: The Choir retunes the Spires on the Still Days in a fixed, public order: Still 1 Storm and Sentinel; Still 2 Sheaf and Pale; Still 3 Highwater's three - Choir at dawn, Crown at noon, Sluice at dusk; Still 4 Falls (Cantors travel upriver beforehand) and the Lament for the Drowned over Lirenne; Still 5 the Joining, every Spire sung together at dusk. Retuning means the Spire is let fall silent for some hours and then woken by the retuning song; a Spire in mid-retuning does not answer an ordinary solo tide-song.
cost: Still 3 is the most dangerous day in Highwater (S1 flood, S4 wave).
limit: Public knowledge: it points at nobody.
known_publicly: true
```

Approved with the retuning clarification (DEC-04, r3).

```canon
id: RULE-020
type: world_rule
canon: approved
area: economy
rule: The Tithe Map sets four tiers of song: First Song (always sung; 12 coppers a month per household), Second Song (sung if voices allow; 6), Last Song (if voices remain; 3), Let Go (not sung, pumps only, tithe forgiven; drowned deeds go "for reclamation" under the Dry Charter model). A district can buy a lift (~500 marks a year to the Spire's holder).
cost: The value of the realm's money is decided every year by the map (dry-notes are backed only by land above Let Go).
limit: Drawn by the Map Office (Inchley) from the Choir's song-reckoning and the wardens' reports; signed by the Helm.
known_publicly: true
secrets: [SEC-007]
```

```canon
id: RULE-021
type: world_rule
canon: approved
area: economy
rule: Money: the mark is a silver coin worth 60 coppers; dry-notes of the Counting House come in 1, 5, 10, 50 and 100 marks, backed (Paper Ordinance, CY 224) by deeds above the waterline in the Dry Book, countersigned by a Merriden notary, with a silver reserve of about one mark in twenty.
cost: Notes on drowned land are worthless ("wet notes").
limit: Prices and wages: §7.4.
known_publicly: true
secrets: [SEC-007]
```

```canon
id: RULE-022
type: world_rule
canon: approved
area: custom
rule: The Ossari Dry Queen is an office, not a crown: when the Udra knot-reckoners declare the wells below the red knot, the council of clan mothers gives "the dry" to a daughter with full power over water, grain and war until the wells rise above the red knot again; her badge is a copper ring in the left ear.
cost: Relief from thirst weakens the Dry Queen (CY 314, CY 320).
limit: Always a woman by the clan mothers' custom.
known_publicly: true
```

Approved (DEC-09, r3).

```canon
id: RULE-023
type: world_rule
canon: approved
area: custom
rule: The Exchange of Sleeves (Stair Treaty, CY 142): each generation the clans send a child of a ruling family to live at the Stair and Rusk sends one of its own to the Rim, each wearing the other's sleeve as a sign of guest-right; Rusk stopped sending after CY 206.
cost: The uplands count Rusk's broken half as the oldest unpaid debt.
limit: —
known_publicly: true
```

```canon
id: RULE-024
type: world_rule
canon: approved
area: magic
rule: A Spire is safe with about eight voiced Cantors (daily tide-songs and a rested reserve for a storm); below five it detunes faster; below three it is sung in shifts and by children; a Cantor's voice lasts about fifteen to twenty years of service, less with Great Songs.
cost: Weaker Spires need more Great Songs, which burn voices faster - the shortage feeds itself (census: HS-090).
limit: Follows from RULE-001 and RULE-003.
known_publicly: false
secrets: [SEC-005]
```

Approved with the census in HS-090 (DEC-11, r3). Numbers stay off screen; one line pays it in S5E6 (Ione's journal: every Ilvane-born Cantor of her lifetime had a Lows nurse).

### 7.1 The Conclave (the Ring)

#### 7.1.1 Eight voices and the ninth — how the seats came to be

The Charter of the Ring (CY 1, EV-0101) gave the realm **eight voices** and set the ninth aside for drowned Lirenne. A voice was given to each Spire-warden house — and, uniquely, a second voice to House Harrow as the price of surrendering its Hill Spire to the Helm's office (the Crown Spire). The sword houses (Rusk, Moll, Ostry) got none.

| Voice | CY 1 | CY 141 | CY 251–252 | CY 312 |
|---|---|---|---|---|
| the Sentinel voice | Corvane | Corvane | Corvane | **Corvane** |
| the Sheaf voice | Dask | Dask | Dask | **Dask** |
| the Pale voice | Ilvane | Ilvane | Ilvane | **Ilvane** |
| the Storm voice | Quell | Quell | Quell | **Quell** |
| the Bell (Choir) voice | the Choir | the Choir | the Choir | **the Choir** |
| the Falls voice | Vanth | → **Rusk** (by conquest) | Rusk | **Rusk** (in exile from S3) |
| the Sluice voice | Harrow | Harrow | → **Fennick** (CY 251, with the Spire) | **Fennick** |
| the **Hill Voice** (no Spire) | Harrow | Harrow | → **Lantry** (CY 252, by will: "the Purchased Seat") | **Lantry** |
| the **Sunken Vote** | "whoever holds Lirenne" — in practice the First Cantor in a tie | | | (cast S1E12 by Vesna) |

**The Hill Voice precedent.** Since CY 1 one voice of eight has belonged to a house, not to a stone. That is why a bank could buy it (CY 252); why the Pumpwrights' Guild argues it deserves one; and why **Rusk keeps its voice in exile** after the Stair falls (S3) — "a voice is a house's, not a rock's". Fennick and the Choir argue the Falls voice lapsed with the Spire; the Ring has never voted on it, so every time Rusk's voice decides something it is challenged. (A standing quarrel for S4–S12.)

#### 7.1.2 Who may cast a voice
- the head of the house, or a **voice-bearer** carrying the head's seal-ring;
- a bearer under 21 must be **confirmed** by the house's eldest adult member (in CY 312: Maren, 19, needs Lady Ysa — Ysa's "condition", S1E11);
- the Choir's voice is cast by the First Cantor or her Voice (sign voiced aloud by a Brother — Elm in S1);
- the Helm votes only through his own house (the Helm's office has no voice of its own).

#### 7.1.3 Calling a Helm vote
1. **Death or removal** of a Helm is announced by the Relay's **death-tone** (S1E1).
2. The **Master of the Hearings** (Fennick since the Clerks' Ordinance, CY 160) keeps the Ring's roll and proclaims the vacancy.
3. **Date:** by law a Helm is chosen on the **Still Days** — the first Still Days at least thirty days after the death. (Lucan dies Longdark 6, CY 312 → the Still Days of CY 312, "thirty days". Odo dies on the Night of a Thousand Voices, Still 3 of CY 320 (CY 320-11-03, EV-0319) → the Still Days of CY 321 (S6), DEC-07.)
4. **Interregnum:** the Ring governs by simple majority of seats present; the Crown Spire is sung by the Choir; the Tithe Map in force is the last one signed.
5. **Candidates:** any head of a voting house, or anyone sponsored by two seats.

#### 7.1.4 Challenges and postponement
- **Challenge of the Voice** — "is this bearer entitled?" (S1E9: Odo contests Maren's right). **Challenge of Precedence** — the order of voting; seats vote from the youngest seal to the oldest, so the oldest house has the "last word" and sees every other vote first (S1E8: Corvane vs. Fennick).
- A challenge is heard by the Hearings — **except** a challenge involving Fennick, which the Ring hears itself by majority of the unchallenged seats. (Odo is judge in his own election everywhere else — the first thing every fan notices.)
- Each pending challenge **postpones the vote by one Still Day**. The vote must be taken **before dusk on the fifth Still Day**.
- **Majority:** 5 of 8. A Helm is elected for life.

#### 7.1.5 The Sunken Vote clause (Charter of the Ring, Article Nine — in-world wording)
> *"Should the voices of the Ring stand evenly divided, the ninth voice shall be given by whoever holds Lirenne; and while Lirenne lies under the water, the First of the Cantors shall speak for the drowned."*

- It applies only to an **exact tie** (4–4) between two candidates at dusk on Still 5 (S1E12).
- **"Whoever holds Lirenne"** is not defined. The Sunk Charter (CY 3) gives Quell salvage of Lirenne "until the city be raised". The Pretender and the salvage bonds (S6) sell exactly this ambiguity; the Raising (S9–S11) aims at it; the clause is cast again in S6E12 and decided for good at S11E12–S12.

#### 7.1.6 Removal
Only a **unanimous** Conclave (all eight) or death removes a Helm (RULE-009). The Helm's own house must vote against him — it has never happened.

#### 7.1.7 The S1 vote as a worked example (S1E12)
Corvane (Maren, confirmed by Ysa), Quell, Ilvane (Aurin, defying his mother), Rusk **for Corvane** · Fennick, Lantry, the Choir, Dask (Garrick) **for Fennick** → 4–4 at dusk on Still 5 → Article Nine → the First Cantor speaks for the drowned → **Odo Fennick, Helm**.

---

### 7.2 The Helms (CY 1–312)

| # | Years (CY) | Helm | House | Remembered for |
|---|---|---|---|---|
| 1 | 1 – 17 | Aldous | Harrow | the Charter; the Relay (CY 9) |
| 2 | 17 – 39 | Avel | Ilvane | the Unison Decree passed under him (CY 34) |
| 3 | 39 – 58 | Ulric | Dask | "the bread vote" |
| 4 | 58 – 80 | Lambert | Harrow | |
| 5 | 80 – 102 | Galen | Corvane | sanctioned the Furrow War (CY 88) |
| 6 | 102 – 126 | Grimald | Dask | |
| 7 | 126 – 149 | Evander | Ilvane | the writ against Vanth (CY 140–141) |
| 8 | 149 – 171 | Ebbard | Dask | |
| 9 | 171 – 198 | Jolle | Quell | "the Pirate Helm" |
| 10 | 198 – 221 | Hallam | Corvane | the mouth-toll made perpetual |
| 11 | 221 – 249 | Tancred | Harrow | the Paper Ordinance (CY 224) — dry-notes |
| 12 | 249 – 268 | Tavian | Ilvane | Harrow's extinction; Fennick raised; the Purchased Seat |
| 13 | 268 – 290 | Stellan | Corvane | "the years the boats came" |
| 14 | 290 – 312 | Lucan | Dask | the Night of Still Water; the Dry Charter (CY 295); dies S1E1 |
| 15 | 312 – 320 | Odo | Fennick | the first Fennick Helm; Listener Law; killed S5E11 |

Rusk has never had a Helm; neither has Lantry.

---

### 7.3 The Tithe Map

**What:** the yearly plan of which districts are sung first in a storm (and, by consequence, which districts pay which dry-tithe). Read aloud at the **tithe-reading** in the Dry Palace before the Still Days (S1E1), signed by the Helm.

**Who draws it:** the **Map Office** in the Dry Palace (hereditary cartographers, House Inchley, HS-015) from (a) the Choir's **song-reckoning** — how many Cantor-hours each Spire can give in a storm (the shortage shrinks this every year, `houses/HS-090-choir.md`), (b) the sluice-wardens' and dike-reeves' reports, (c) the Helm's instructions.

**Tiers of song**
| Tier | Meaning | Dry-tithe per household (paid monthly to the collector) |
|---|---|---|
| **First Song** | always sung first; never let go | 12 coppers a month (2 marks a year) |
| **Second Song** | sung in a storm if voices allow | 6 coppers a month (1 mark a year) |
| **Last Song** | sung only if voices remain | 3 coppers a month (half a mark a year) |
| **Let Go** | not sung; "pumps only"; tithe forgiven | none — and, after a flood, the drowned deeds go "for reclamation" (the Dry Charter model) |

Ninth Sluice: Second Song until CY 295 · Last Song after the Night of Still Water · **Let Go** in the CY 312 draft (the line Lucan dies reading: *"…and the Ninth Sluice—"*).

**How it is bought (all floors):**
- **Steps:** seats trade map favours for votes (the S1 bread vote); the Choir sells **priority songs** that override the map on the crown; the bank asks for districts to be *Let Go* where it holds Account titles.
- **Mids:** Inchley clerks sell drafts (SEC-037); relay-keepers sell the map's tone-codes early (Bede Lark, CY 312); sluice-wardens (Cobbet) buy their own districts up a tier.
- **Lows:** a district can buy a **lift** (~500 marks a year to the Spire's holder) — the Undertow's dry-pledges are, in effect, a Lows savings club for lifts that never come.

---

### 7.4 Money, prices and fees (CY 312)

| Unit | Value |
|---|---|
| **mark** (silver coin) | 60 **coppers** (as §8) — scarce |
| **dry-note** | paper of the Counting House, 1, 5, 10, 50, 100 marks; at par in CY 312 |

| Thing | Price | | Wage | Pay |
|---|---|---|---|---|
| a loaf of silt-bread in the Lows | 2 coppers (4 after the S1E5 barges; relief loaf 6) | | treadmill walker | 10 coppers a 6-hour walk (debt-walkers: a mark off the debt) |
| a sack of grain (50 kg) | 1 mark (3 in a famine) | | mudlark's best day | 10–20 coppers |
| a stilt-house in the Lows | ~10 marks | | junior clerk (Hollis) | 3 marks a month |
| a Mids room | ~2 marks a month | | Rusk pikeman | 2 marks a month + bread |
| a gate pass in a flood | 5 marks a family | | Cantor's stipend | 100 marks a year (the house pays the Choir ~600) |
| a dry-pledge | 1 copper a week a household | | relay-keeper | 4 marks a month + fees |
| a storm-berth at Gullmouth | ~5 marks a night | | sergeant (Kes) | 4 marks a month |
| a barrel of powder (50 kg) | ~30 marks in Highwater | | Gleaner (ear-money) | 3 marks a head + 10 if the child takes the ear |
| saltpeter | 1 mark / 10 kg at the Rim, 4 at the Arsenal | | free-company sword | 3 marks a month in notes |

**Relay fees:** within Highwater 5 coppers a tone-group; across the delta 1 mark per 10 groups; **first-tone** subscription (messages an hour before the public) 50 marks a year; the death-tone and flood-tones are free and cannot be delayed — by law (they are delayed anyway).

**Hearings fees:** filing 1 mark; **speed fee** 5–50 marks (a verdict this week instead of next year); a commoner's testimony against a noble needs a **Mids sponsor** (guildmaster, sealed clerk, Cantor) — Lows rate for a sponsor ~2 marks.

**Grain:** Dask grows ~60% of the delta's bread; the **Ember contracts** sell Dask harvests forward to the bank at a fixed price, paid in advance (Dask lives on the advance; the bank lives on the margin).

**Saltpeter:** `houses/HS-091-ossari.md` §5. The licence tenth: Rusk until CY 313, the Dry Queen under the Weir Terms.

---

### 7.5 Dry-notes and Account Nine (SEC-007 — writers' room only)

#### 7.5.1 How a note is backed (the official rule — Paper Ordinance, CY 224)
- The Counting House may issue notes **only against deeds to land above the waterline** held in its vault, entered in the **Dry Book**, countersigned by a Merriden notary — plus a **silver reserve** for those who want coin (about 1 mark in 20).
- "Above the waterline" is not a survey. It means **on the Tithe Map above Let Go**. So the value of the realm's money is decided, every year, by the map.

#### 7.5.2 The Dry Charter (CY 295)
After the Night of Still Water the Charter (EV-0203) passed the deeds of drowned Ninth Sluice to the Counting House **"for reclamation"**: the bank pumps the land and owns what comes up dry ("reclaimed land"). Later reclamations copy it: the Helm declares a drowned district "reclaimed land" (Odo, S1E12) and its deeds go to whoever finances the pumps — always the bank. (Its forgery is SEC-006, not this file's business.)

#### 7.5.3 A reclamation account, in simple numbers — Account Nine (Ninth Sluice, CY 312)
| Step | | Marks |
|---|---|---|
| 1 | Ninth Sluice: ~4,000 household plots, 20,000 people. Wet value of the plots (as Lows land) | ~40,000 |
| 2 | The bank buys deeds, mortgages and the **Undertow's dry-pledges** for the district at a discount (the pledges are worthless if the district is let go — the Undertow sells them gladly) | pays ~15,000 |
| 3 | Value of the same land **after** a flood, reclamation and pumping, sold as dry Mids building land (~60 a plot) | ~240,000 |
| 4 | **Pre-sale:** the bank sells "reclaimed plots, to be delivered" at 40 a plot to the Steps (houses, the Choir's chapter, partners) — closing on **the third Still Day** | brings in ~160,000 now |
| 5 | **Note issue:** the bank books the *future* reclaimed land in the Dry Book as "reclamation title" at 240,000 and prints notes against it | ~200,000 new notes |
| 6 | Cost: pumps and dike works over two years | ~25,000 |

If the district floods on time and is pumped dry, the bank turns 15,000 into ~360,000 (pre-sales + notes), and 20,000 people pay with their homes or lives. **Why the third Still Day:** the pre-sale contracts allow buyers their money back if the land is not "let go" by then — so the water must come by Still 3 (SEC-015: the bribed retuning).

#### 7.5.4 The numbered accounts
Reclamation accounts are numbered as opened. One–Four (CY 231–290): small districts in the Highwater Lows and the Moll polders, each after a "natural" flood. **Five** (CY 295): the first half of Ninth Sluice — canon EV-0200: Lantry paid for the Sluice Spire's retuning to be delayed, and the Night of Still Water followed. Account Nine is the same operation, seventeen years later. Six–Eight (CY 298–309): Third, Eleventh, Twelfth sluices. **Nine** (CY 312): the rest of Ninth Sluice.

#### 7.5.5 Why the paper rots — backing by year
| Year | Notes in circulation | Silver reserve | Real dry deeds | "Reclamation title" (under water or never dried) | **Real backing** |
|---|---|---|---|---|---|
| CY 295 | 0.60 M | 0.05 M | 0.50 M | 0.05 M | ~92% |
| CY 312 | 1.20 M | 0.06 M | 0.78 M | 0.36 M | ~70% |
| CY 315 | 1.70 M | 0.05 M | 0.80 M | 0.85 M | ~50% |
| CY 320 | 2.40 M | 0.04 M | 0.80 M | 1.56 M | ~35% |
| CY 321 (S6) | 3.00 M | 0.03 M | 0.87 M | 2.10 M | **~30% → about 70% unbacked** |

Why it grows: the bank prints to fund Helm Odo's war (S2–S3) and occupation (S4), to carry Dask's Ember shortfall (CY 314), and to roll over the Choir and Corvane; and the reclaimed lands **don't stay dry**, because pumps cannot replace Spires (RULE-007) and the Spires are short of singers. Each year more "reclamation title" is simply sea.

Market sign: a 10-mark note buys 10 marks of silver in CY 312, 9 in CY 320, **2** in the week of the run (S6E9). Free companies demand silver first (`houses/HS-092…095`).

---

### 7.6 Lirenne salvage bonds (SEC-016 — writers' room only)

**Who invents:** Clan Tarrow's salvage-brokers (HS-023) with **Piers Lantry** (CH-0061), after the dry-note crash (S6E9). They need a face: the **Pearl Pretender** (Lio, CH-0043 — who believes it).

**The paper:** a **Lirenne Salvage Bond**, face 10 marks, printed in teal with a spiral shell. Sold from barges in the Lows and the Mids (S6E5).

**What it is "backed" by (the pitch):**
1. a share in **Quell's salvage of Lirenne** under the Sunk Charter (CY 3) — "the Tide-Kings' vaults";
2. a share in **the Lirenne Voice**: the Pretender, "heir of Ashare", pledges that when Lirenne is raised or held, its ninth voice will be cast as a **Bondholders' Council** directs (Article Nine: "whoever holds Lirenne");
3. the Pretender's word and blood.

**How it is paid for (the trick):** a saver may pay **half in silver and half in old dry-notes at face value**. Savers rush to turn dead paper into something. The brokers keep the silver — and the dry-notes: Piers knows which notes are **first-ranked** in the bank's winding-up (notes on real deeds, countersigned before CY 295) and which are Account paper. The brokers end up as the bank's largest creditors at pennies — the bank's corpse pays them.

**Who buys:** ruined Mids savers (clerks, widows, guild members), burial clubs and Lows hum circles, free-company captains stuck with notes, minor houses (Cobbet), a few desperate Steps families.

**Why bondholders later pay for boats (S9):** a bond is worth nothing unless Lirenne is raised or "held". After the Pretender is exposed (S8E6) the paper should die — but Lio's dying appeal ("raise it anyway") turns the brokers' slogan into the movement's aim, and the **Bondholders' Council** pays for the Raising's boats, pumps and camp bread in S9: sunk cost turned into a cause. *Upward consequence:* S6 — splits the Lows' vote in the Helm election; S9 — finances the Raising; S11 — makes Lirenne a prize every power wants.

---

### 7.7 The Hearings

Run by House Fennick since the Clerks' Ordinance (CY 160). Courts in the Listening House and in district halls.
- **Who may testify:** nobles and Mids freely; a commoner against a noble only with a **Mids sponsor**.
- **Speed and delay are for sale** (§4). A Hearing can sit on a file for years (the Kilbride will, SEC-036).
- **Punishments:** fines, debt-walking (sentenced to the treadmills), the tide-post (Hush Law, RULE-006), exile upriver (Kes, S1E12), drowning for treason (rare, public).
- **The Ring's challenges** go to the Hearings except when Fennick is party (§1.4).
- After Odo (S5) and the bank (S6), **who runs the Hearings** becomes a political prize — Zev Fennick holds them in S7 and opens the Relay logs to Dorran.

---

### 7.8 The Still Days — retuning schedule (fixed by the Choir)

| Day | Spires retuned (silent for hours, one after another) | Political use |
|---|---|---|
| Still 1 | the outer coast: **Storm** (Brackwater), **Sentinel** (Gullmouth) | the Ring sits; challenges are filed |
| Still 2 | **Sheaf** (Polders), **Pale** (Pale Crag) | |
| Still 3 | Highwater's three: **Choir** (dawn), **Crown** (noon), **Sluice** (dusk) | "the city holds its breath" — the most dangerous day: S1 (the skipped Sluice retuning, the flood), S4 (the weir wave) |
| Still 4 | **Falls** (Cantors travel upriver beforehand); in Highwater the **Lament for the Drowned** — Cantors in boats over Lirenne, no answer expected | |
| Still 5 | **the Joining** — every Spire sung together at dusk | the Helm vote must be cast before dusk |

**Retuning (DEC-04, approved):** the Spire is let fall silent for some hours, then woken by the retuning song; a Spire in mid-retuning does not answer an ordinary solo tide-song. In CY 312 the Sluice Spire falls silent at dusk on Still 3 and its retuning song never comes (EV-0304, EV-0305).

> The schedule is public knowledge in-world: every power in the delta knows it, and it points at no one.

---

### 7.9 Schemes on every floor — the table (24 rows)

Columns: **who invents / who executes / who pays / who in the cast could discover it / when it can surface / upward consequence — which decision of the Steps it changes, and in which season** (bible §12.6.2). Rows marked † are from `saga_arc.md`'s Intrigue ladder (kept exactly); the rest are new from this package and are consistent with it.

| # | Scheme | Invents | Executes | Pays | Could discover | Surfaces | Upward consequence (Steps decision · season) |
|---|---|---|---|---|---|---|---|
| 1 | **Account Nine** — notes against land to be let go (SEC-007) | Ursel, the Table | clerks (Hollis, Fossett), Merriden notaries, Undertow pledge-sellers | Ninth Sluice (S1); Mids savers (S6) | Hollis (S1E3–E6), Pell, Merriden auction (S6) | S1 → S6E7 | Odo's first act declares Ninth "reclaimed" (S1E12); the crash makes Maren Helm (**S6**) |
| 2 | **† A relay-keeper sells one message twice** | Bede Lark | Bede, on a Tennant tower | Ruel, Lucan (dead) | Hollis (S1E7), Zev (Relay logs) | S1E7 → S2E6 | Ruel poisons the Helm; Ursel has Ruel killed (**S1**) |
| 3 | **Tithe Map drafts sold** (SEC-037) | Inchley clerks | Map Office copyists | Lows households (dry-pledges priced to fail) | Hollis (S2E6, Lucan's chest), Silt | S1E1 → S2E6 | the bank knows the map before the Helm signs it → Account Nine timed to Still 3 (**S1**) |
| 4 | **Bribed retuning** (SEC-015) | Ursel | Fennick's steward, Cantor Sabin | Ninth Sluice | Hollis (S2E6) | S1E9 → S2E6 | Odo's election is stained by a crime he didn't commit; he must give up his own steward to the Hearings (proposal) (**S2**) |
| 5 | **Under-sung Sluice Spire** (Cantor-rent skim) | Odo's treasury | Choir rent clerks | Ninth Sluice | Ione (S1E3, E8) | S1 | one bribed retuning is enough to drown a district; Ione's Great Song (**S1E10**) |
| 6 | **Priority songs** | Choir chapter | Cantors on the crown | districts that can't pay | Ione (S1), Elm | S1E7–E8 | the Choir's bank debt → **the Choir votes Fennick** (**S1E12**) |
| 7 | **† Ear-money** (SEC-029) | Gleaner novices | an Undertow under-boss | Lows children (Patch) | Silt (S4E6), Ione | S1E5 → S4E6 | Silt's ledger → the songblood doctrine falls (**S5E6**) |
| 8 | **† Pump "breakage"** (SEC-028) | Guild masters | journeymen, warden clerks | Ninth Sluice (doubled dead) | Corr (holds the pin), Dorran | S1E5 → S5E8 | the walkers force the Guild to hold Ninth Sluice on the Night of a Thousand Voices (**S5**) |
| 9 | **† Gate passes** (three floors, DEC-55) | Dunmore warden's clerk issues (5 marks a family); the Rusk quartermaster's office strikes extra copies | guardsman Ansel Fray sells them at the gate (S1E4) | families without passes | Kes (S1E4, E10) | S1E4, S1E10 | Kes opens the gate → stripped, sent to the Stair (**S1E12 → S3**) |
| 10 | **Relief bread** at triple price | Garrick, Orsley | barge-masters (Gillam), Undertow middlemen | the Lows | Pell (S1E5) | S1E5 | Dask's vote is bought with bread → **Odo Helm** (**S1**) |
| 11 | **Flag-hiring** (other houses' seals on barges) | Gillam | lock-keepers who look away | rival convoys | Maren (S2) | S1E5, S2E11 | Dask barges block the canal → Maren loses the Sluice Gates (**S2**) |
| 12 | **† Storm-berths and padded powder** | Corvane flag-captains (Whitlow) | pursers, gunners' mates | wrecked merchant crews; Lows gunners | Nell Tern, Maren (S2E11) | S2E11 | guns silent → Maren loses the Helm's War; the Sovereign's war on small thieves (**S2 → S10**) |
| 13 | **† A regent tidies a crime** (SEC-023) | Lady Ysa | her household; Skarra pilots (SEC-038) | Sister Marl; Maren's war | Maren (S2E10) | S1E7 → S2E10 | Gullmouth opened to Fennick (**S2E11**) |
| 14 | **† Ledger kept as insurance** | Fossett | Fossett | — | Hollis | S2E7 | names Ruel's killers (**S2E11**); testifies (**S6**) |
| 15 | **† Saltpeter sold twice** | Grell quartermasters | clerks, Hadden guides (Goat Stair), Varra sloops, Undertow fences | Rusk pikemen; powder-mill workers | Kes, Ottar, Brenna (knows) | S3E10–11; S4 | Ossari guns fire Rusk powder → **the Stair falls** (**S3**); a second sale in CY 314 (SEC-024, sealed) |
| 16 | **Ember contracts and the vote-lien** | the bank's futures desk, Orsley | Dask stewards | Dask peasants (salt-burned harvest) | Garrick (POV S7) | S4 | Dask's voice pledged to the bank in the dry summer (**S4**); Maren buys Dask with water (**S7**) |
| 17 | **† Men hired out with no questions** | the Undertow | Silt's hirers | — (sealed) | Silt; Tibb; Pell | S4E10 → S10E11 | her book of sold men → what Pell learns about the wave (**S10**) |
| 18 | **† Fake drownings** | the Undertow, Widow Pruitt | Dunmore roll-keepers (paid) | — | Hollis (S2E3) | S2E3 → S6E9 | the Lows' death rolls are unreliable → S6 election arithmetic; a hero's "death" (**S6**) |
| 19 | **Dry-pledges sold to the bank** | Undertow | collectors | the Lows (their insurance becomes the bank's collateral) | Silt, Hollis | S1E6 → S2 | Silt hides Hollis because the bank broke her pledges (**S2**) |
| 20 | **† The walkers' secret union** | Corr | wheel-cells | — | Dorran | S1E5 → S6 | the treadmill strike prices the S6 election (**S6**) |
| 21 | **† The Hum hires out singers** | Pell | Hum circles | — | the Choir, Maren | S6 | houses with failing Spires buy Lows voices → **Maren elected** (**S6**) |
| 22 | **† Lirenne salvage bonds + a pretender** (SEC-016) | Tarrow brokers, Piers Lantry | barge-sellers, Lio | ruined savers | Pell, Jaro (who exposes it in S8E6 is the lead's) | S6E5 → S8E6 | splits the Lows' vote (**S6**); pays for the Raising (**S9**) |
| 23 | **Notes for swords** — free companies paid in dry-notes | the bank, Helm Odo | company captains (Rook Danner) | the companies' men | Maren, Jaro | S6E11 | the mercenary fleet changes sides mid-battle → the Battle of the Shoals (**S6**) |
| 24 | **The Purchased Seat's deathbed will** (SEC-036) | Lantry clerks (CY 251), Fennick witness | — | Harrow's natural line (Kilbride) | Zev (Hearings, S7), Piers | S7E4–E5 (DEC-39) | Piers casts the Purchased Seat from S6E12 and through S7–S9 under challenge; the Hearings never rule — the suit is still pending when the Conclave is dissolved (S9E12) |

Rows 1–24 change or freeze a named decision of the Steps in the season given (row 24: DEC-39). Every season S1–S9 has at least one Lows or Mids scheme in this table that moves the top (S1: 2, 8, 9, 10; S2: 11, 12, 19; S3: 15; S4: 16; S5: 8; S6: 18, 20, 21, 22; S7: 16; S8: 22; S9: 22); S10–S12 continue through rows 12 and 17 and the lead's own outlines.


### 7.10 Spire home tones (draft, for the sound director)

Still **draft** in v0.4: a working sheet (decisions_resolved 3.4), confirmed by the composer and the sound director at the style and voice tests. Proposal of writer-houses (`studio/story/houses/art_and_music_sheet.md` §5). Canon fixes only that each house theme is built on its Spire's tone and that relay stones ring only on the high home-tones (RULE-004).

| Spire | Home tone | House theme |
|---|---|---|
| Crown | C | the Helm's fanfare (old Harrow chord) |
| Sluice | C sharp, drifting flat | Fennick |
| Sentinel | D | Corvane |
| Pale | E | Ilvane |
| Sheaf | F | Dask |
| Choir | G | the Choir |
| Falls | A | Rusk (Vanth before CY 141) |
| Storm | B | Quell |
| Sunken | not fixed (lead and composer) | Ashare |

No house theme uses the low register as its tonic.


## 8. Life of the Lows and the Mids (v0.3; approved v0.4)

Status: **approved** by the lead screenwriter in r3 (writer-characters, `studio/story/characters/lows_and_mids_life.md`, 2026-11-22; merged by lore-keeper without the story hooks; slang of §11 is in `glossary.md`). Folk beliefs are marked **(belief)**. Agrees with §7 (prices, wages, 1 mark = 60 coppers). The Lows' Still 3 "Remembering" (lanterns) and the Choir's Still 4 "Lament for the Drowned" (RULE-019) are two different rites.

### 8.1 Work

#### The Lows (below the waterline)
| Trade | What they do | Day | Pay (proposal) | Dangers / schemes |
|---|---|---|---|---|
| **Mudlarks** | children and the old wade the back-canals and silt flats at low tide for metal, buttons, coins, purses, echo-chips | by the tide, not the clock: two "ebbs" a day | what they find; sold to fences by weight | drowning in soft silt; fights over "lanes"; selling unlicensed echo-chips is a crime (RULE-004) |
| **Treadmill walkers** | walk the great wheels that drive the pumps (RULE-007) — 20 to a wheel, in shifts | 6-hour "walks", day and night in storm season | 10 coppers a walk; debt-walkers get nothing but a mark off their debt | debt for life; the reedmaster's whistle sets the pace; crushed feet |
| **Sluice-workers** | keep the gates, counterweights and sumps of each numbered sluice | watches by the bell | 2 marks a month, tied to the district | chains part in storms (Dov); paid by the Spire-house that takes the dry-tithe |
| **Salt-rakers** | rake the salt pans at the delta's edge (and on the Quell Shoals) | summer: dawn to noon | by the basket | salt-blind eyes, cracked hands; salt is the Lady's offering and the Lows' cheapest currency |
| **Lime-pit workers** | burn and slake lime for the dikes' mortar | long shifts | low | burns; they **whistle** whole conversations across the pits — the best whistlers in the city |
| **Boat-people** | ferry, haul, fish eels, carry the dead to the ebb | — | by the trip | the Undertow owns the moorings |
| **Net-menders** (Nan) | mend nets, sails, sandbag sacks | by the piece | 1 copper a fathom | eyes; the Quiet hides in this trade (proposal) |

#### The Mids (dike level)
| Trade | What they do | Pay (proposal) | Schemes (`series_bible.md` §7.1) |
|---|---|---|---|
| **Clerks** (Lantry, the Hearings, the guilds) | copy, count, reconcile; a "trusted clerk gets a clip" | junior: 3 marks a month + a dry room if lucky | forging, skimming, selling ledger secrets |
| **Relay-keepers** | sit with a licensed echo-stone, log every tone, pass it on | 4 marks a month + fees | sell messages early (Bede Lark sells one twice) |
| **Pumpwrights** | build and mend the wind- and treadmill pumps, locks, powder-mills | guild rates | the yearly "breakage" racket (SEC-028) |
| **Soldiers & the watch** | house guards, the city watch, the Listeners | 2 marks a month + bread | gate passes sold in floods |
| **Shopkeepers, chandlers, bakers** | dike-crest shops | — | bread "short weight" in a grain squeeze |


---

### 8.2 Money
- **Marks** (silver coin; the only "real" money). **Coppers** (proposal: 60 coppers = 1 mark) — what the Lows actually hold. A loaf of silt-bread: 2 coppers (4 after the S1E5 barges).
- **Dry-notes** — Lantry paper "promise of dry ground", in ones, fives and tens ("a one-dry", "a fiver", "a tenner"). The Lows take them at a discount and call notes backed by low land **"wet notes"** (proposal: you can see it in the serial — every note names the deed-district; Lows people check it before accepting).
- **The dry-tithe** — paid per household, per month, to the house of the nearest Spire (the Ninth pays Fennick); the tithe-collector's box is chained to his wrist.
- **Dry-pledges** — the Undertow's protection racket: pay and your lane gets sandbags first in a flood; don't, and your sandbags go missing.
- **Debts** — the Lows run on debt-paper. A debt can be **"walked"** (on a treadmill), **"sold"** (to an under-boss), or **"drowned on paper"** (Widow Pruitt's trick: you are entered as drowned in the flood-roll and start again under another name — see S2E3, S6E9).
- **Salt** — small change of the poor and the Lady's offering; a pinch of salt settles a bet.


---

### 8.3 Food
- **Lows:** silt-bread (barley and reed flour, grey, sour); eel stew; mussels raked from the sluice piles; samphire and duckweed soup; salted sprats; bog-myrtle tea; on feast days, eel pie with an egg. Food is bought daily — nothing keeps in the damp.
- **Mids:** brown wheat bread, pies, small beer, cheese from the polders, river fish; coffee is a Steps luxury (proposal: Mids clerks drink chicory "clerk's coffee").
- **Steps:** white bread from Dask wheat, sea fish, wine from the uplands (when there is peace).
- **Hunger politics:** Dask controls the grain; "relief bread" is sold to the Lows at triple price through Undertow middlemen (houses_overview).


---

### 8.4 Homes
- **Stilt-houses (the Lows):** timber on tarred piles, two or three rooms stacked, joined lane to lane by **plank-walks and rope-bridges**; boats tied under the floor; a **"dry-shelf"** under the roof-ridge where the family keeps everything that matters (Nan's net-chest is the exception — she keeps it on the floor "so nobody thinks it matters"). Every flood the family raises the floor **one rung** — old houses have a ladder of tide-marks on the doorpost.
- **Roofs** are the escape road (S1E10): Lows children learn the roof-lanes before the water-lanes.
- **Dike terraces (the Mids):** brick houses built along and into the crest of the great dike, three storeys, **no cellars** (sumps instead); garrets rented to clerks (Hollis's garret under Widow Pruitt's roof). A "dry room" — a room above the last recorded flood line — is the Mids' status symbol.
- **The Steps:** granite, terraces, gardens; nobody on the Steps owns a boat they row themselves.


---

### 8.5 Calendar, rites and festivals
- **Counting years by floods:** "two floods after the Still Water". Children's ages are counted by floods survived.
- **The Still Days (Still 1–5):** every Spire falls silent in turn for retuning. In the Lows: as each Spire's hum stops, everyone **kneels and covers the mouth with the right hand** until the hum returns. **(belief)** The folk explanations disagree, which is the point (SEC-003 clue — the true origin is not given here): "so the sea doesn't hear us breathe and come looking"; "so we don't steal the Cantors' note while it's loose"; "because the Lady is listening for her children's voices"; Saltwife Orrie only says "because our grandmothers did".
  - **Salt on the threshold** each Still night; no fires on the water.
  - **Still 3 — the Remembering (proposal):** since CY 295, the Ninth floats paper lanterns down the back-canal for the Night of Still Water and **mouths the names of the dead without sound**. (Makes the S1E10 flood on the same night unbearable.)
- **Firstwater morning:** children splash the first water of the year on each other ("wet for luck").
- **The Low Ebb Fair (Ember, lowest tide of the year — proposal):** mudlark fair on the open silt; salvage auctions, eel races, clap-dances; the one day Lows and Mids mix freely.
- **Births and deaths:** a newborn is shown the water at the first ebb; the dead are given "to the ebb" with salt in the hands (boat burial at the sluice mouth), or, in a dry year, to the lime-pits (a disgrace).


---

### 8.6 The Lady Below
- **Belief:** the sea is a drowned mother who takes back what she is owed — no more, no less. The spiral shell is her sign; salt and shells are her offerings. Drowning is "going to the Lady"; a narrow escape is "the Lady spat you out".
- **Saltwives:** her priestesses (Orrie): older women of the Lows who keep shell-shrines on moored hulks, wash the dead, bless boats, and judge small quarrels with a handful of salt.
- **Worship is silent or whispered** (the Hush Law): prayers are said with the lips only, or **signed** with a short set of hand-shapes (proposal: a few overlap with Choir sign — nobody asks why).
- **The Steps** mock it ("shell-kissers"); the Choir tolerates it as harmless.
- **The Quiet hides inside it** (`houses_overview.md` §3): the mud-spiral of the Quiet looks like a Lady's shell drawn in the silt. Most worshippers do not know the Quiet exists.


---

### 8.7 Hush-Law culture — notes for the composer and sound team
The Hush Law (RULE-006) forbids commoners to sing within sight of a Spire; work-chants, clapping, whistling and wordless drumming are allowed. Three hundred years of it have made the Lows **percussive and whistled**:
- **Whistle-talk:** the Lows speak across lanes in whistles — two-finger whistles for distance, lip-whistles for close. A small fixed vocabulary (proposal): *Listeners coming* (falling two-tone), *all clear* (rising three), *tide turning* (trill), *help* (long single). Pell whistles two or three notes when nervous.
- **Work-chants:** **spoken on one pitch**, rhythmic, no melody — the walkers' step-count, the net-menders' count. Legal; any interval above a step makes it "song" (proposal; the Listeners' grey zone).
- **Humming with the mouth shut:** the legal grey zone of the poor — "house noise" if indoors, "singing" if a Listener hears it outside (proposal). Nan's lullaby lives here.
- **Clapping and stamping:** clap-dances at the Low Ebb Fair; thigh-slaps and plank-stamps on the plank-walks; children's hand-clap games with counted rhymes.
- **Drumming:** on buckets, upturned boats, hulls, the treadmill's step-boards; a drum on the sluice-gate means a breach.
- **Reed whistles:** the reedmaster's whistle sets the treadmill's pace (Corr's title).
- **Sound rule for the score:** the Lows' themes should be built from whistles, claps, drums and breath; **the voice is absent** until it breaks out (Lio, S1E2; the Hum, S5). The five-note lullaby appears **only** in clue scenes (`series_bible.md` §10) — never use it as ordinary Lows colour.
- **The Mids** sound like work: pump-gears, quill-scratch, the Relay's tones, barrack drums, the clerks' bell. Mids people are allowed to sing nowhere public either (they are commoners) but they **don't want to** — singing is "a Lows thing".


---

### 8.8 Crime and the Undertow
- **Structure (proposal):** **Mother Silt** on her barge-palace; one **under-boss per sluice or trade** (Gant of the Fourth runs treadmills; others run moorings, the shard trade, the dry-pledges); **fences** (Tuck) who buy from mudlarks; **mouths** who sell rumour; **runners** (children, paid in food).
- **Trades:** smuggling (salt, echo-chips, powder in war); the **dry-pledge** racket; **salvage-rights** fights; the echo-shard black market; **fake drownings**; debt-buying and debt-walkers; hiring out men "with no questions" (S4E10, `[SEALED]` what for).
- **Silt's law:** everything is sold; no child is. (SEC-029 breaks it from inside.)
- **Undertow punishments:** "put on the wheel" (walk a debt you didn't owe); "given to the ebb" (drowned) for informers; the law's punishment is the **tide-post**.
- **With the Steps:** the Undertow sells to everyone — Listeners, bank, Corvane sailors, Dask's relief-bread trade. The Listeners tolerate it because it is the best informer they have.
- **The tide-post:** a tarred post in each sluice at the low-tide line; the condemned is tied for a night and the tide comes up to the chin (16+ — shown by water, sound and faces, never by suffering in close-up).


---

### 8.9 How news travels
- **The Relay** (RULE-004) — official tones from Spire to Spire; heard in every relay-house; the death-tone stops the city (S1E1). Keepers sell messages early.
- **Criers at the tide-post** — the Helm's decrees are read at each sluice's tide-post (S7E1: the half-repeal).
- **The Undertow's "mouths"** — rumour-sellers in eel-pie stalls and ferry-boats; a rumour costs a copper, a true one five.
- **The whistle-chain** (proposal) — a whistled message relayed roof to roof can cross all twelve sluices faster than a runner; the Lows' own Relay (echo for S11, when kite-lines replace the Relay).
- **The Mids:** broadsheets from the guild presses (printing exists — Quire's pamphlets in S9), clerks' gossip in "tide-houses" (cheap chicory houses on the dike), barracks talk.
- **The Steps:** private relay codes, letters by fast boat.


---

### 8.10 The Mids — what their life is like
- **Dry, but only just:** the Mids flood only in a great breach; their fear is not water but **falling** — into the Lows, by debt, by a bad Tithe Map, by one wrong signature.
- **Respectability:** a dry room, a clip or a guild badge, a Sunday coat; sponsoring a Lows person in court is a favour that can ruin you (commoners cannot testify against a noble without a Mids sponsor).
- **Guilds:** Pumpwrights (who want a Conclave vote — "pumps vs. songs"), Clerks' Hall (proposal), Relay-keepers' Lodge; each with its own small rackets.
- **The watch and the Listeners:** many Mids families have one son in the watch; the Listeners recruit from Lows boys who want out (Fitch).
- **Hidden origins:** many Mids people were born in the Lows and hide it (Nell Tern, Fitch) — the accent is the tell; Mids schools beat it out of children.


---

### 8.12 Lows and Mids storylines across the saga (summary for the lead)
| Line | Planted | Pays | Owner |
|---|---|---|---|
| ear-money (Gleaners → Gant → debt-walkers) | S1E5 | S4E6 → S5E6 | Silt, Patch, Sedge, Daro |
| the walkers' union and the sawn pin | S1E5, S1E10 | S5E8, S6, S11 | Corr, Dorran |
| gate passes | S1E4 | S1E10 (→ saltpeter S3, proposal) | Ansel Fray, Kes |
| a keeper sells twice | S1E7 | S2E6 | Bede Lark |
| drowned on paper | S2E3 | S6E9 | Widow Pruitt |
| the navy knot | S1E10 | S9E7 | Sal Tern, Nell, Tibb |
| the Lows-born hunter | S1E2 | S5E11–12 | Fitch |
| whistle-chain → kite-lines | S1E10 (proposal) | S11 | the Lows, Esk |
| the Still 3 lanterns | S1E8–E10 (proposal) | each Still Days finale | the Ninth |


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
