# Character template

Copy to `characters/CH-NNNN-slug.md`. One named character per file. Minor characters (one or two episodes, few lines) may share a file `characters/_minor-<group>.md` with one block each.

Rules:
- Parents only by ID. If the real parent differs from the official one, the official one goes in `father`/`mother`, the real one in `true_father`/`true_mother`, and `parentage_secret` must point to a secret in `secrets.md`.
- What the character *knows* is recorded in `secrets.md` (`known_by`), not here.
- `status_track` records changes of state by episode: `alive`, `dead`, `missing`, `presumed_dead`, `captive`, `revealed` (true identity revealed), `unborn`. Dead → alive is an error unless `may_return: true` and a world rule allows it.
- Teen characters: write the age band in `look`; no romantic or sexual content with minors (see BRIEF).

```canon-template
id: CH-NNNN
type: character
canon: draft
name:              # full name as spoken; spelling and pronunciation go to glossary.md
epithet:           # "the Younger", "Ashhand" ...
house:             # HS-… or empty
class:             # ruler | noble | knight | clergy | merchant | craftsman | soldier | servant | poor | outlaw | ...
role:              # protagonist | antagonist | major | supporting | minor
born:              # date
born_at:           # PL-…
died:              # date
died_at:           # PL-…
father:            # CH-… (official)
mother:            # CH-… (official)
true_father:       # CH-… (only if secret)
true_mother:       # CH-… (only if secret)
parentage_secret:  # SEC-…
adoptive_parents: []
relations: []      # [CH-…:kind] kind: spouse, betrothed, sibling, rival, mentor, sworn_sword, friend, enemy, lover(adults only), ward ...
secrets: []        # SEC-… about this character
status_track: []   # [S01E01:alive, S03E09:dead]
may_return:        # true only if world rules allow return from death
first_episode:     # SxxEyy
```

## Look (story-level, for the art team)
Canonical traits that must never change (the director turns them into the prompt ID-block in `studio/direction/refs/<ID>/card.md`):
- Age band and build:
- Hair (colour, length, signature detail):
- Eyes:
- Distinctive mark (side!):
- Usual clothes and colours:
- Signature item:
- Changes over the saga (scar after S02E05, new armour in S04…):

## Voice (for the sound team)
- Voice character (pitch, tempo, timbre, accent of region/class):
- Speech habits (formal/slang, catchphrase, never says …):
- Sample line (English, 1-2 sentences):

## Goals
- Wants (outer goal):
- Needs (inner goal):
- Fears:
- Heroism — what heroic act defines them:

## Biography
_Prose. Dates are linked, not restated: "lost her brother at the Ford (EV-…)"._

## Arc by season
| Season | Where they are (PL-…) | What they do | State at season end |
|---|---|---|---|
| S01 | | | |

---

## EXAMPLE (placeholder, not canon)

```canon
id: CH-EX-0003
type: character
canon: draft
example: true
name: Tamsin Varnel
house: HS-EX-001
class: noble
role: protagonist
born: SR 146-08-20
born_at: PL-EX-0002
father: CH-EX-0001
mother: CH-EX-0002
true_father: CH-EX-0004
parentage_secret: SEC-EX-001
relations: [CH-EX-0004:mentor]
secrets: [SEC-EX-001]
status_track: [S01E01:alive]
first_episode: S01E01
```

Look (EXAMPLE): young woman around 16; ash-dark braid with a white heron feather on the left side; grey eyes; salt-burn scar on the right palm; grey wool coat; carries her father's tide-stone pendant.
Voice (EXAMPLE): low, calm, speaks slowly; never swears. "The tide always comes back. So do I."
