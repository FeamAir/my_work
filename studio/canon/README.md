# Canon — how it works

Canon version: **v0.3** (foundation of THE LOW NOTE r2, approved + writer dossiers on houses and characters, draft) · Keeper: `lore-keeper` · Language of canon content: English.

The canon is the single source of truth for the saga: world laws, chronology, houses, characters, bloodlines, secrets and names. Scripts, art, sound and marketing must follow it. If a script and the canon disagree, the canon wins until the keeper records a change.

## 1. Files

| File / folder | What it holds | Machine records (`type`) |
|---|---|---|
| `README.md` | This document: rules, formats, workflow | — |
| `CHANGELOG.md` | Every canon change: version, date, who proposed, what changed | — |
| `world.md` | World laws, magic / technology, geography (places), calendar; §7 power and money (laws RULE-015…024), §8 life of the Lows and the Mids | `calendar`, `world_rule`, `place` |
| `timeline.md` | Eras, pre-saga history, episode dates | `era`, `event`, `episode` |
| `houses/HS-NNN-slug.md` | One great or minor house per file | `house` |
| `characters/CH-NNNN-slug.md` | One named character per file | `character` |
| `characters/_minor-*.md` | Several minor characters per file (crowds, servants, one-episode roles); `_minor-houses.md` = house lineages CH-0200…0299 | `character` |
| `genealogy/README.md` | How bloodlines are recorded and drawn | (generated, no records) |
| `secrets.md` | Registry of secrets and mysteries: truth, who knows, hints, reveal | `secret` |
| `glossary.md` | Spelling and pronunciation of every name for voice synthesis | `term` |
| `sealed/sealed.md` | **Restricted** part of the canon: answers of restricted secrets, sealed characters, overlays, true versions of events, sealed rules and names (§8a) | any type; `overlay: true` |
| `checklist.md` | Checklist for reviewing script materials against the canon | — |
| `decisions_for_lead.md` | The one list of open decisions for the lead screenwriter (DEC-NN): what blocks season 1, options, the keeper's recommendation. TODO stubs point here (§6a) | — |
| `tools/validate.py` | Automatic consistency checker | — |
| `*/_template.md`, examples | Empty templates + one EXAMPLE each (`example: true`) | ignored by the normal run |

Places may be split into `places/PL-NNNN-slug.md` when `world.md` grows; the validator reads every `.md` under `studio/canon/`.

## 2. One fact — one place

Every fact is written **once**, in its owning record. Everything else links to it by ID.

| Fact | Lives in | Not in |
|---|---|---|
| Birth / death date, parents | the character record | house file, timeline, genealogy |
| House membership | character `house` | house member list (generated) |
| Who heads a house and since when | house `heads` | character file |
| Relationship between two characters | relations of **one** of the two (by convention the lower ID) | both |
| Who knows a secret and since which episode | `secrets.md` `known_by` | character file (it only lists secret IDs) |
| When an event happened | `timeline.md` event | character biography (it links `EV-…`) |
| Pronunciation | `glossary.md` | character file |
| Custody of saga objects (shard, ring, clip…) | `world.md` §6 (pre-saga custody of restricted objects: `sealed/`) | character file |
| A restricted truth (answer, hidden parent, hidden knower) | `sealed/sealed.md` (§8a) | anywhere else |
| Exact prompt ID-block, reference images | `studio/direction/refs/<ID>/card.md` (director) | canon holds only the story-level look: what must never change |
| `voice_id`, TTS settings | `studio/sound/` (sound director) | canon holds only the voice character |

Prose (biographies, history) may *mention* facts, but must not restate dates or numbers that live elsewhere; link instead: `born in the Siege of X (EV-0012)`.

## 3. IDs

IDs are permanent. A renamed character keeps the ID; a deleted record leaves its ID retired (never reused).

| Kind | Format | Example |
|---|---|---|
| Character | `CH-NNNN` | `CH-0042` |
| House | `HS-NNN` | `HS-007` |
| Place | `PL-NNNN` | `PL-0103` |
| Event | `EV-NNNN` | `EV-0350` |
| Secret | `SEC-NNN`, a split secret `SEC-NNNa`/`b` | `SEC-014`, `SEC-011b` |
| Glossary term | `TERM-NNNN` | `TERM-0200` |
| World rule | `RULE-NNN` | `RULE-005` |
| Era | `ERA-ABBR` | `ERA-AE` |
| Episode | `SxxEyy` | `S03E07` |

Allocation (v0.3):

| Kind | Range | Who |
|---|---|---|
| Characters | CH-0001…0065 | the lead (foundation) |
| | CH-0066…0099 | keeper and writer-characters (second circle, new people); CH-0070 was never issued (proposal = CH-0067) |
| | CH-0100…0199 | reserved for future cast (S2-S12 outlines) |
| | CH-0200…0299 | house lineages (writer-houses: founders, last heads, the last three generations) |
| Houses | HS-001…012 great and fallen · HS-013…089 minor houses and clans (writer-houses: HS-013…033) · HS-090…099 non-house powers | |
| Places | PL-0001…0065 foundation · PL-0070…0079 writer-houses / keeper · PL-0080+ keeper (sluices and the like) | |
| Events | EV-0001…0249 by prequel period (`franchise.md` §3) · EV-0250…0299 other pre-saga history (keeper; v0.3 up to EV-0275) · EV-0300+ the saga | |
| Secrets | SEC-001…029 foundation (+ SEC-011b) · SEC-030+ keeper's numbering of new secrets; numbers proposed by writers are temporary until the keeper confirms them (writer-houses' SEC-C01…C07 = SEC-034…040; SEC-032 not issued) | |
| World rules | RULE-001…014 foundation (013-014 sealed) · RULE-015+ new (v0.3: law, custom, economy) | |
| Terms | TERM-0001…0213 foundation · TERM-0214+ v0.3 | |

EXAMPLE records use an `EX-` infix (`CH-EX-0001`) and `example: true`; the normal validator run ignores them. They are deleted or kept as reference once real canon exists; they never mix with real canon.

## 4. Statuses and versions

Each record has `canon:`

| Status | Meaning | Who can change it |
|---|---|---|
| `draft` | Proposed / being worked on. May change freely. | keeper, on request of any writer |
| `approved` | Approved by the lead screenwriter. Changes need a change request. | keeper, after lead screenwriter agrees |
| `locked` | Already shown on screen (episode produced). Cannot be changed — only reinterpreted (new secret, unreliable narrator, etc.). | nobody; a retcon needs director + lead screenwriter |
| `retconned` | Kept for history, no longer true. Points to the replacement in prose. | keeper |

A dossier that adds to an **approved** record does not change it: its additions sit in an `amend` block (status `draft`) right under the approved record (§6). When the lead approves, the keeper folds the amend into the record and deletes the amend block. A value that contradicts an approved one is never written into an amend: it goes to `decisions_for_lead.md`.

Canon version `vMAJOR.MINOR`:
- **MINOR** +1 for every accepted batch of changes (one line per change in `CHANGELOG.md`).
- **MAJOR** = number of the last season whose scripts are approved (v1.x = season 1 is fixed). When a season goes into production all its records become `locked`.

Every script, storyboard and report states which canon version it was written against (`Canon: v1.4`).

## 5. How changes happen (only through the keeper)

1. Anyone (lead screenwriter, writers, director, composer…) proposes a change in **their own report** using a block:

   ```text
   ### Canon change request
   - Target: CH-0042 (or "new character", "new secret", …)
   - Change: born AE 981 -> AE 979
   - Why: needs to be 18 at the Battle of … (EV-0120) in S02E05
   - Affects: S02E05 script, SEC-014 hints
   ```

2. The keeper checks it against the canon (`checklist.md` + `tools/validate.py`), then either applies it, or replies with a list of conflicts in the keeper's report.
3. Applied changes go into `CHANGELOG.md` with the new version number.
4. Changes to `approved` records need the lead screenwriter's consent; to `locked` records — director + lead screenwriter.
5. Nobody but the keeper edits files in `studio/canon/`.

## 6. Machine blocks (format)

Each record is a fenced block with the language tag `canon`. Inside: one `key: value` per line, lower-case keys, lists in square brackets, comments start with `#`. No nesting, no multi-line values (long text goes in prose below the block). The format is a strict subset of YAML, so YAML tools can read it, but the validator needs only the Python standard library.

```text
  ```canon
  id: CH-0042
  type: character
  canon: draft
  name: Example Name
  house: HS-007
  born: AE 981-04-12
  relations: [CH-0043:rival, CH-0050:sworn_sword]
  ```
```

Conventions inside values:
- **Date:** `ERA YYYY[-MM[-DD]]`, e.g. `AE 981`, `AE 981-04`, `AE 981-04-12`. Prefix `~` for "about" (±1 year). `?` for unknown. Eras and their offsets are defined in `timeline.md`, months in `world.md` calendar.
- **Episode:** `S01E05`. `origin` = before the saga starts.
- **ID with a moment:** `CH-0042@S03E07` or `CH-0042@AE 990`.
- **ID with a kind:** `CH-0043:rival`, `S02E09:dead`.
- Blank templates use the fence tag `canon-template` so the validator skips them.
- No inline comments inside a real block: a `#` comment must be on its own line.
- `overlay: true` - only in `sealed/`: the block adds or replaces fields of the record with the same `id` (§8a).
- `amend: true` - a **draft** block that adds to an approved record with the same `id` (outside or inside `sealed/`): it fills fields the record lacks (or holds as `?`), may narrow a date inside the approved interval (`CY 297` → `CY 297-02`, `~CY 270` → `CY 270-08`), and extends list fields. It may never contradict an approved value - the validator reports that as an error. Merge order: record → amends → overlays.
- Relation kinds are free words in `snake_case`, seen from the record that holds them (the lower ID). Recommended: `spouse, sibling, parent_of` (only when no `father`/`mother` field can say it), `ward, guardian, mentor, friend, ally, enemy, rival, client, patron, employer_of, informant_of, commander_of, sworn_sword, killed_by, voice`. Kinship that follows from `father`/`mother` is not repeated as a relation; a secret parentage is never a relation (only `true_*`).
- `class` (open list): `ruler, noble, knight, clergy, merchant, clerk, physician, craftsman, soldier, servant, poor, outlaw`.

## 6a. TODO stubs (things not decided yet)

A field whose value is not decided yet is written as an explicit stub instead of being left empty or guessed:

```text
father: TODO(DEC-33)
heads: [CH-0018@CY 279, TODO(DEC-30)@CY 313-09]
reveal: TODO(DEC-37)
known_by: [CH-0058@TODO(DEC-41)]
date: TODO(DEC-20)
```

- `DEC-NN` must exist as a heading in `decisions_for_lead.md` (the validator checks it).
- The validator skips reference and date checks for a stub, counts it, and lists all stubs with `--todo`.
- When the lead decides, the keeper replaces the stub with the value and logs it in `CHANGELOG.md`. A stub is never shown on screen: scripts must not depend on it.

## 7. Tools

```text
python3 studio/canon/tools/validate.py                     # check the real canon
python3 studio/canon/tools/validate.py --examples          # check the EXAMPLE records
python3 studio/canon/tools/validate.py --mermaid HS-007 [--spoilers]   # family tree (Mermaid)
python3 studio/canon/tools/validate.py --cast S02E03 CH-0001,CH-0007   # can these characters appear?
python3 studio/canon/tools/validate.py --knows CH-0001 S03E05          # what does this character know by then?
python3 studio/canon/tools/validate.py --todo                          # list TODO stubs (§6a)
```

The validator is run after every change and before every script review. Errors block approval; warnings must be read and either fixed or explained in the keeper's report.

## 8. Spoilers

The canon contains the full truth, including what will be revealed seasons later. Agents producing public material (marketer, opening/ending, previews) must check `secrets.md` and never use anything whose `reveal` episode has not aired.

## 8a. Sealed (restricted) facts

Some truths are kept even from the writer-helpers (the lead screenwriter's `sealed/` file; readers: lead screenwriter, keeper, studio director). In the canon they live in **one place, `sealed/sealed.md`**, in the normal machine format, so the validator still checks them:

1. **A restricted secret** is recorded only in `sealed/sealed.md` (full record: truth, known_by, hints, reveal). `secrets.md` lists it in the overview as "(restricted)" with tier, first hint, reveal and the production constraints that may be shared - never the truth or the knowers.
2. **A restricted character** (one whose very existence gives away an answer) is a full record in `sealed/`.
3. **A restricted fact about a public record** is an **overlay**: a block with the same `id` and `overlay: true`, holding only the restricted fields (e.g. `true_mother`, `parentage_secret`, the late part of `status_track`, sealed secret IDs in `secrets`, hidden knowers in `known_by`). The validator merges overlay fields into the base record: a scalar replaces the base value, a list is **added** to the base list (v0.3); the base record stays what helpers may read. An overlay without a base record is an error.
8. Restricted secret IDs that writers put into their dossiers (e.g. SEC-024 on a house) are moved by the keeper into overlays in `sealed/`; `decisions_for_lead.md` names restricted secrets only as "закрытая" and maps them in `sealed/sealed.md` §H.
4. **Restricted IDs may appear** in public records only as bare IDs (`secrets: [SEC-024]`, `related`), never with an explanation; their names and answers do not.
5. **True versions** of public events whose truth is restricted are written in `sealed/` §D; the public event says "Truth: SEC-… (sealed)".
6. Tool output can contain restricted truths: `--knows` and `--mermaid --spoilers` are for the keeper and the lead only. Excerpts for others (composer, director, sound) are made by the keeper on the director's decision.
7. When a restricted secret's reveal airs, its record moves from `sealed/` to `secrets.md` (CHANGELOG line).

