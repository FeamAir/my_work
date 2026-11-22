# House template

Copy to `houses/HS-NNN-slug.md` (e.g. `HS-007-varnel.md`). One house per file. Cadet branches are separate houses with `cadet_of`.

Members are **not** listed here: membership lives in each character's `house` field; the family tree is generated (`tools/validate.py --mermaid HS-NNN`).

```canon-template
id: HS-NNN
type: house
canon: draft
name:             # "House X"
rank:             # great | major | minor | merchant | extinct | ...
words:            # motto, exact wording
sigil:            # one line, exact (art team draws from it)
colors: []        # simple colour words, 2-3, e.g. [slate grey, salt white]
seat:             # PL-…
lands: []         # PL-…
liege:            # HS-… (current)
cadet_of:         # HS-… if a branch
founded:          # date
founder:          # CH-…
extinct:          # date, if ended
heads: []         # [CH-…@date, CH-…@date] in order of succession
alliances: []     # [HS-…:marriage@date, HS-…:sworn@date, HS-…:enemy@date]
secrets: []       # SEC-… the house hides
leitmotif:        # short music idea; details in studio/music/
```

## Public history
_How the house is known to the world: rise, conquests, how it got its lands (link EV-…)._

## True history
_What really happened, where it differs from the public version. Every difference links a SEC-…._

## Culture and look
_Customs, faith, how members dress, the household's servants and soldiers (useful for crowd scenes)._

## Power and money
_Armies (rough size), wealth source, debts, who they owe and who owes them._

## Notes for production
_Sigil description for the art team, colour cautions (no two great houses with the same main colour), leitmotif idea for the composer._

---

## EXAMPLE (placeholder, not canon)

```canon
id: HS-EX-001
type: house
canon: draft
example: true
name: House Varnel
rank: minor
words: "What the tide takes, we remember."
sigil: a white heron standing on a grey tide-stone
colors: [slate grey, salt white]
seat: PL-EX-0002
lands: [PL-EX-0001]
founded: SR 120
founder: CH-EX-0001
heads: [CH-EX-0001@SR 120, CH-EX-0002@SR 146-11]
secrets: [SEC-EX-001]
```

Public history (EXAMPLE): Oren Varnel built Greyhold on a tidal island after the salt wars (EV-EX-0001).
