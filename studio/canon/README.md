# Canon — how it works

Canon version: **v0.1** (structure only, no world yet) · Keeper: `lore-keeper` · Language of canon content: English.

The canon is the single source of truth for the saga: world laws, chronology, houses, characters, bloodlines, secrets and names. Scripts, art, sound and marketing must follow it. If a script and the canon disagree, the canon wins until the keeper records a change.

## 1. Files

| File / folder | What it holds | Machine records (`type`) |
|---|---|---|
| `README.md` | This document: rules, formats, workflow | — |
| `CHANGELOG.md` | Every canon change: version, date, who proposed, what changed | — |
| `world.md` | World laws, magic / technology, geography (places), calendar | `calendar`, `world_rule`, `place` |
| `timeline.md` | Eras, pre-saga history, episode dates | `era`, `event`, `episode` |
| `houses/HS-NNN-slug.md` | One great or minor house per file | `house` |
| `characters/CH-NNNN-slug.md` | One named character per file | `character` |
| `characters/_minor-*.md` | Several minor characters per file (crowds, servants, one-episode roles) | `character` |
| `genealogy/README.md` | How bloodlines are recorded and drawn | (generated, no records) |
| `secrets.md` | Registry of secrets and mysteries: truth, who knows, hints, reveal | `secret` |
| `glossary.md` | Spelling and pronunciation of every name for voice synthesis | `term` |
| `checklist.md` | Checklist for reviewing script materials against the canon | — |
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
| Secret | `SEC-NNN` | `SEC-014` |
| Glossary term | `TERM-NNNN` | `TERM-0200` |
| World rule | `RULE-NNN` | `RULE-005` |
| Era | `ERA-ABBR` | `ERA-AE` |
| Episode | `SxxEyy` | `S03E07` |

EXAMPLE records use an `EX-` infix (`CH-EX-0001`) and `example: true`; the normal validator run ignores them. They are deleted or kept as reference once real canon exists; they never mix with real canon.

## 4. Statuses and versions

Each record has `canon:`

| Status | Meaning | Who can change it |
|---|---|---|
| `draft` | Proposed / being worked on. May change freely. | keeper, on request of any writer |
| `approved` | Approved by the lead screenwriter. Changes need a change request. | keeper, after lead screenwriter agrees |
| `locked` | Already shown on screen (episode produced). Cannot be changed — only reinterpreted (new secret, unreliable narrator, etc.). | nobody; a retcon needs director + lead screenwriter |
| `retconned` | Kept for history, no longer true. Points to the replacement in prose. | keeper |

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

## 7. Tools

```text
python3 studio/canon/tools/validate.py                     # check the real canon
python3 studio/canon/tools/validate.py --examples          # check the EXAMPLE records
python3 studio/canon/tools/validate.py --mermaid HS-007 [--spoilers]   # family tree (Mermaid)
python3 studio/canon/tools/validate.py --cast S02E03 CH-0001,CH-0007   # can these characters appear?
python3 studio/canon/tools/validate.py --knows CH-0001 S03E05          # what does this character know by then?
```

The validator is run after every change and before every script review. Errors block approval; warnings must be read and either fixed or explained in the keeper's report.

## 8. Spoilers

The canon contains the full truth, including what will be revealed seasons later. Agents producing public material (marketer, opening/ending, previews) must check `secrets.md` and never use anything whose `reveal` episode has not aired.
