# Glossary and pronunciation

Canon: v0.2 · Status: **draft** (respellings proposed by the keeper; to be confirmed by the lead screenwriter and tested with the TTS voice) (foundation r2, approved by the director 2026-11-22; transfer by lore-keeper)

Every name spoken on screen has one entry. Voice synthesis reads `say` (stressed syllable in CAPS); subtitles and on-screen text use `term`. Entries for restricted names are in `sealed/`.

## Fields

```canon-template
id: TERM-NNNN
type: term
canon: draft
term:          # exact spelling, as in subtitles
say:           # respelling for TTS, stressed syllable in CAPS
ipa:           # optional
kind:          # person | house | place | title | word | phrase | object
ref:           # CH-/HS-/PL-/… id this term names
meaning:       # for invented words
```

## Naming rules

1. **No two important names start with the same 3 letters** within one region or house generation; avoid names differing by one letter. Known exceptions in the foundation are listed in the keeper's report 2026-11-22-r2 (Corr/Corvane, Marl/Maren, Lantern/Lantry; Quire = Choir by sound).
2. Each culture has its own sound palette (below).
3. No names from existing well-known works, no real historical figures, no real brands.
4. Spelling must be pronounceable by an English TTS voice from the respelling alone; test the `say` line before approval.
5. Titles and forms of address are entries too.

## Sound palettes by culture

| Culture / region | Sounds / syllables | Example | Avoid |
|---|---|---|---|
| Concord nobility | two syllables, consonant-heavy | Corvane, Fennick, Garrick | soft -eh endings |
| old Ashare / Lirenne | soft vowels, -eh, -enne, -ra | Neveh, Lirenne, Oshra | hard stops |
| Ossari | ts / k / d + open vowels | Tsura, Kadu, Esk | Concord two-syllable surnames |
| the Shoals | j / r sailors' names | Jaro | — |
| Lowfolk | one-syllable given names; surname = their sluice ("Pell of the Ninth") | Pell, Wick, Nan, Liss, Dov, Mags | (exceptions in the foundation: Lio, Orrie - see report) |

## Entries

### People

```canon
id: TERM-0001
type: term
canon: draft
term: Pell
say: PEL
kind: person
ref: CH-0001
```

```canon
id: TERM-0002
type: term
canon: draft
term: Ione Ilvane
say: eye-OH-nee IL-vayn
kind: person
ref: CH-0002
```

```canon
id: TERM-0003
type: term
canon: draft
term: Hollis Kett
say: HOL-iss KET
kind: person
ref: CH-0003
```

```canon
id: TERM-0004
type: term
canon: draft
term: Kes Mabry
say: KESS MAY-bree
kind: person
ref: CH-0004
```

```canon
id: TERM-0005
type: term
canon: draft
term: Ruel Corvane
say: ROO-el kor-VAYN
kind: person
ref: CH-0005
```

```canon
id: TERM-0006
type: term
canon: draft
term: Maren Corvane
say: MAR-en kor-VAYN
kind: person
ref: CH-0006
```

```canon
id: TERM-0007
type: term
canon: draft
term: Wick
say: WIK
kind: person
ref: CH-0007
```

```canon
id: TERM-0008
type: term
canon: draft
term: Odo Fennick
say: OH-doh FEN-ik
kind: person
ref: CH-0010
```

```canon
id: TERM-0009
type: term
canon: draft
term: Ursel Lantry
say: UR-sel LAN-tree
kind: person
ref: CH-0011
```

```canon
id: TERM-0010
type: term
canon: draft
term: Vesna Ilvane
say: VEZ-nah IL-vayn
kind: person
ref: CH-0012
```

```canon
id: TERM-0011
type: term
canon: draft
term: Tsura Den
say: TSOO-rah DEN
kind: person
ref: CH-0013
```

```canon
id: TERM-0012
type: term
canon: draft
term: Mother Silt
say: MUH-ther SILT
kind: person
ref: CH-0014
```

```canon
id: TERM-0013
type: term
canon: draft
term: Nan Oshra
say: NAN OSH-rah
kind: person
ref: CH-0015
```

```canon
id: TERM-0014
type: term
canon: draft
term: Lucan Dask
say: LOO-kan DASK
kind: person
ref: CH-0016
```

```canon
id: TERM-0015
type: term
canon: draft
term: Garrick Dask
say: GARR-ik DASK
kind: person
ref: CH-0017
```

```canon
id: TERM-0016
type: term
canon: draft
term: Brenna Rusk
say: BREN-ah RUSK
kind: person
ref: CH-0018
```

```canon
id: TERM-0017
type: term
canon: draft
term: Jaro Quell
say: JAH-roh KWEL
kind: person
ref: CH-0019
```

```canon
id: TERM-0018
type: term
canon: draft
term: Aurin Ilvane
say: OR-in IL-vayn
kind: person
ref: CH-0020
```

```canon
id: TERM-0019
type: term
canon: draft
term: Cressa Ilvane
say: KRESS-ah IL-vayn
kind: person
ref: CH-0021
```

```canon
id: TERM-0020
type: term
canon: draft
term: Brother Elm
say: BRUH-ther ELM
kind: person
ref: CH-0022
```

```canon
id: TERM-0021
type: term
canon: draft
term: Liss
say: LISS
kind: person
ref: CH-0023
```

```canon
id: TERM-0022
type: term
canon: draft
term: Dov
say: DAHV
kind: person
ref: CH-0024
```

```canon
id: TERM-0023
type: term
canon: draft
term: Teodor Kett
say: TAY-oh-dor KET
kind: person
ref: CH-0025
```

```canon
id: TERM-0024
type: term
canon: draft
term: Neveh Ashare
say: NEH-veh ah-SHAH-reh
kind: person
ref: CH-0030
```

```canon
id: TERM-0025
type: term
canon: draft
term: Oshra
say: OSH-rah
kind: person
ref: CH-0031
```

```canon
id: TERM-0026
type: term
canon: draft
term: Esk
say: ESK
kind: person
ref: CH-0040
```

```canon
id: TERM-0027
type: term
canon: draft
term: Dorran Strand
say: DOR-an STRAND
kind: person
ref: CH-0041
```

```canon
id: TERM-0028
type: term
canon: draft
term: Zev Fennick
say: ZEV FEN-ik
kind: person
ref: CH-0042
```

```canon
id: TERM-0029
type: term
canon: draft
term: Lio
say: LEE-oh
kind: person
ref: CH-0043
```

```canon
id: TERM-0030
type: term
canon: draft
term: Nell Tern
say: NEL TURN
kind: person
ref: CH-0044
```

```canon
id: TERM-0031
type: term
canon: draft
term: Daro Vey
say: DAH-roh VAY
kind: person
ref: CH-0045
```

```canon
id: TERM-0032
type: term
canon: draft
term: Tibb
say: TIB
kind: person
ref: CH-0046
```

```canon
id: TERM-0033
type: term
canon: draft
term: Kadu
say: KAH-doo
kind: person
ref: CH-0047
```

```canon
id: TERM-0034
type: term
canon: draft
term: Corr
say: KOR
kind: person
ref: CH-0048
```

```canon
id: TERM-0035
type: term
canon: draft
term: Mags
say: MAGZ
kind: person
ref: CH-0049
```

```canon
id: TERM-0036
type: term
canon: draft
term: Sister Marl
say: SIS-ter MARL
kind: person
ref: CH-0050
```

```canon
id: TERM-0037
type: term
canon: draft
term: Doctor Ambry
say: DOK-ter AM-bree
kind: person
ref: CH-0051
```

```canon
id: TERM-0038
type: term
canon: draft
term: Bede Lark
say: BEED LARK
kind: person
ref: CH-0052
```

```canon
id: TERM-0039
type: term
canon: draft
term: Captain Fitch
say: KAP-tin FITCH
kind: person
ref: CH-0053
```

```canon
id: TERM-0040
type: term
canon: draft
term: Widow Pruitt
say: WID-oh PROO-it
kind: person
ref: CH-0054
```

```canon
id: TERM-0041
type: term
canon: draft
term: Fossett
say: FOSS-et
kind: person
ref: CH-0055
```

```canon
id: TERM-0042
type: term
canon: draft
term: Sister Venn
say: SIS-ter VEN
kind: person
ref: CH-0056
```

```canon
id: TERM-0043
type: term
canon: draft
term: Cantor Sabin
say: KAN-tor SAY-bin
kind: person
ref: CH-0057
```

```canon
id: TERM-0044
type: term
canon: draft
term: Ysa Corvane
say: EE-sah kor-VAYN
kind: person
ref: CH-0058
```

```canon
id: TERM-0045
type: term
canon: draft
term: Rook Danner
say: ROOK DAN-er
kind: person
ref: CH-0059
```

```canon
id: TERM-0046
type: term
canon: draft
term: Archivist Ferro
say: AR-kiv-ist FERR-oh
kind: person
ref: CH-0060
```

```canon
id: TERM-0047
type: term
canon: draft
term: Piers Lantry
say: PEERZ LAN-tree
kind: person
ref: CH-0061
```

```canon
id: TERM-0048
type: term
canon: draft
term: Ottar
say: OT-ar
kind: person
ref: CH-0062
```

```canon
id: TERM-0049
type: term
canon: draft
term: Juno Brisk
say: JOO-noh BRISK
kind: person
ref: CH-0063
```

```canon
id: TERM-0050
type: term
canon: draft
term: Patch
say: PATCH
kind: person
ref: CH-0064
```

```canon
id: TERM-0051
type: term
canon: draft
term: Saltwife Orrie
say: SALT-wife OR-ee
kind: person
ref: CH-0065
```

```canon
id: TERM-0052
type: term
canon: draft
term: Sal Tern
say: SAL TURN
kind: person
ref: CH-0067
```

```canon
id: TERM-0053
type: term
canon: draft
term: Ilse Ilvane
say: IL-seh IL-vayn
kind: person
ref: CH-0068
```

### Houses and powers

```canon
id: TERM-0054
type: term
canon: draft
term: House Corvane
say: HOWSS kor-VAYN
kind: house
ref: HS-001
```

```canon
id: TERM-0055
type: term
canon: draft
term: House Dask
say: HOWSS DASK
kind: house
ref: HS-002
```

```canon
id: TERM-0056
type: term
canon: draft
term: House Ilvane
say: HOWSS IL-vayn
kind: house
ref: HS-003
```

```canon
id: TERM-0057
type: term
canon: draft
term: House Rusk
say: HOWSS RUSK
kind: house
ref: HS-004
```

```canon
id: TERM-0058
type: term
canon: draft
term: House Quell
say: HOWSS KWEL
kind: house
ref: HS-005
```

```canon
id: TERM-0059
type: term
canon: draft
term: House Fennick
say: HOWSS FEN-ik
kind: house
ref: HS-006
```

```canon
id: TERM-0060
type: term
canon: draft
term: House Lantry
say: HOWSS LAN-tree
kind: house
ref: HS-007
```

```canon
id: TERM-0061
type: term
canon: draft
term: House Ashare
say: HOWSS ah-SHAH-reh
kind: house
ref: HS-008
```

```canon
id: TERM-0062
type: term
canon: draft
term: House Harrow
say: HOWSS HARR-oh
kind: house
ref: HS-009
```

```canon
id: TERM-0063
type: term
canon: draft
term: House Moll
say: HOWSS MOL
kind: house
ref: HS-010
```

```canon
id: TERM-0064
type: term
canon: draft
term: House Ostry
say: HOWSS OSS-tree
kind: house
ref: HS-011
```

```canon
id: TERM-0065
type: term
canon: draft
term: House Vanth
say: HOWSS VANTH
kind: house
ref: HS-012
```

```canon
id: TERM-0066
type: term
canon: draft
term: the Choir
say: thuh KWIRE
kind: house
ref: HS-090
```

```canon
id: TERM-0067
type: term
canon: draft
term: the Ossari
say: thee oh-SAH-ree
kind: house
ref: HS-091
```

```canon
id: TERM-0068
type: term
canon: draft
term: the Pumpwrights' Guild
say: thuh PUMP-rites GILD
kind: house
ref: HS-092
```

```canon
id: TERM-0069
type: term
canon: draft
term: the Undertow
say: thee UN-der-toh
kind: house
ref: HS-093
```

```canon
id: TERM-0070
type: term
canon: draft
term: the Quiet
say: thuh KWY-et
kind: house
ref: HS-094
```

```canon
id: TERM-0071
type: term
canon: draft
term: the Lantern Company
say: thuh LAN-tern KUM-puh-nee
kind: house
ref: HS-095
```

### Places

```canon
id: TERM-0072
type: term
canon: draft
term: the Concord of Tessary
say: thuh KON-kord uv TESS-uh-ree
kind: place
ref: PL-0001
```

```canon
id: TERM-0073
type: term
canon: draft
term: the Aun
say: thee AWN
kind: place
ref: PL-0002
```

```canon
id: TERM-0074
type: term
canon: draft
term: the Many Mouths
say: thuh MEN-ee MOWTHZ
kind: place
ref: PL-0003
```

```canon
id: TERM-0075
type: term
canon: draft
term: Highwater
say: HY-waw-ter
kind: place
ref: PL-0004
```

```canon
id: TERM-0076
type: term
canon: draft
term: the Steps
say: thuh STEPS
kind: place
ref: PL-0005
```

```canon
id: TERM-0077
type: term
canon: draft
term: the Mids
say: thuh MIDZ
kind: place
ref: PL-0006
```

```canon
id: TERM-0078
type: term
canon: draft
term: the Lows
say: thuh LOHZ
kind: place
ref: PL-0007
```

```canon
id: TERM-0079
type: term
canon: draft
term: Ninth Sluice
say: NYNTH SLOOSS
kind: place
ref: PL-0008
```

```canon
id: TERM-0080
type: term
canon: draft
term: the Dry Palace
say: thuh DRY PAL-iss
kind: place
ref: PL-0009
```

```canon
id: TERM-0081
type: term
canon: draft
term: the Ring
say: thuh RING
kind: place
ref: PL-0010
```

```canon
id: TERM-0082
type: term
canon: draft
term: the Lantry Counting House
say: thuh LAN-tree KOWN-ting howss
kind: place
ref: PL-0011
```

```canon
id: TERM-0083
type: term
canon: draft
term: the Listening House
say: thuh LISS-en-ing howss
kind: place
ref: PL-0012
```

```canon
id: TERM-0084
type: term
canon: draft
term: the Choir temple
say: thuh KWIRE TEM-pul
kind: place
ref: PL-0013
```

```canon
id: TERM-0085
type: term
canon: draft
term: the Crown Spire
say: thuh KROWN SPY-er
kind: place
ref: PL-0014
```

```canon
id: TERM-0086
type: term
canon: draft
term: the Choir Spire
say: thuh KWIRE SPY-er
kind: place
ref: PL-0015
```

```canon
id: TERM-0087
type: term
canon: draft
term: the Sluice Spire
say: thuh SLOOSS SPY-er
kind: place
ref: PL-0016
```

```canon
id: TERM-0088
type: term
canon: draft
term: the Ilvane townhouse
say: thee IL-vayn TOWN-howss
kind: place
ref: PL-0017
```

```canon
id: TERM-0089
type: term
canon: draft
term: Highwater harbour
say: HY-waw-ter HAR-ber
kind: place
ref: PL-0018
```

```canon
id: TERM-0090
type: term
canon: draft
term: Nan's stilt-house
say: NANZ STILT-howss
kind: place
ref: PL-0019
```

```canon
id: TERM-0091
type: term
canon: draft
term: the Ninth Sluice back-canal
say: thuh NYNTH SLOOSS BAK-kuh-nal
kind: place
ref: PL-0020
```

```canon
id: TERM-0092
type: term
canon: draft
term: the Ninth Sluice evacuation gate
say: thuh NYNTH SLOOSS ee-vak-yoo-AY-shun GAYT
kind: place
ref: PL-0021
```

```canon
id: TERM-0093
type: term
canon: draft
term: the Ninth Sluice tide-post
say: thuh NYNTH SLOOSS TYD-post
kind: place
ref: PL-0022
```

```canon
id: TERM-0094
type: term
canon: draft
term: Mother Silt's barge
say: MUH-ther SILTS BARJ
kind: place
ref: PL-0023
```

```canon
id: TERM-0095
type: term
canon: draft
term: Hollis's garret
say: HOL-iss-iz GARR-et
kind: place
ref: PL-0024
```

```canon
id: TERM-0096
type: term
canon: draft
term: the Sluice Gates
say: thuh SLOOSS GAYTS
kind: place
ref: PL-0026
```

```canon
id: TERM-0097
type: term
canon: draft
term: the Ninth Bridge
say: thuh NYNTH BRIJ
kind: place
ref: PL-0027
```

```canon
id: TERM-0098
type: term
canon: draft
term: the Hundred Locks
say: thuh HUN-dred LOKS
kind: place
ref: PL-0028
```

```canon
id: TERM-0099
type: term
canon: draft
term: Gullmouth
say: GUL-mowth
kind: place
ref: PL-0030
```

```canon
id: TERM-0100
type: term
canon: draft
term: the Sentinel Spire
say: thuh SEN-tin-el SPY-er
kind: place
ref: PL-0031
```

```canon
id: TERM-0101
type: term
canon: draft
term: the Ostry harbour-forts
say: thee OSS-tree HAR-ber-forts
kind: place
ref: PL-0032
```

```canon
id: TERM-0102
type: term
canon: draft
term: the Polders
say: thuh POHL-derz
kind: place
ref: PL-0035
```

```canon
id: TERM-0103
type: term
canon: draft
term: Dask Barrows
say: DASK BARR-ohz
kind: place
ref: PL-0036
```

```canon
id: TERM-0104
type: term
canon: draft
term: the Sheaf Spire
say: thuh SHEEF SPY-er
kind: place
ref: PL-0037
```

```canon
id: TERM-0105
type: term
canon: draft
term: the Moll polders
say: thuh MOL POHL-derz
kind: place
ref: PL-0038
```

```canon
id: TERM-0106
type: term
canon: draft
term: Pale Crag
say: PAYL KRAG
kind: place
ref: PL-0040
```

```canon
id: TERM-0107
type: term
canon: draft
term: the Pale Spire
say: thuh PAYL SPY-er
kind: place
ref: PL-0041
```

```canon
id: TERM-0108
type: term
canon: draft
term: the Red Escarpment
say: thuh RED es-KARP-ment
kind: place
ref: PL-0045
```

```canon
id: TERM-0109
type: term
canon: draft
term: the Stair
say: thuh STAIR
kind: place
ref: PL-0046
```

```canon
id: TERM-0110
type: term
canon: draft
term: the Falls Spire
say: thuh FAWLZ SPY-er
kind: place
ref: PL-0047
```

```canon
id: TERM-0111
type: term
canon: draft
term: the falls of the Aun
say: thuh FAWLZ uv thee AWN
kind: place
ref: PL-0048
```

```canon
id: TERM-0112
type: term
canon: draft
term: the weir
say: thuh WEER
kind: place
ref: PL-0049
```

```canon
id: TERM-0113
type: term
canon: draft
term: the Ossari Uplands
say: thee oh-SAH-ree UP-lundz
kind: place
ref: PL-0050
```

```canon
id: TERM-0114
type: term
canon: draft
term: the Shelf lakes
say: thuh SHELF LAYKS
kind: place
ref: PL-0051
```

```canon
id: TERM-0115
type: term
canon: draft
term: the Shoals
say: thuh SHOHLZ
kind: place
ref: PL-0055
```

```canon
id: TERM-0116
type: term
canon: draft
term: Brackwater
say: BRAK-waw-ter
kind: place
ref: PL-0056
```

```canon
id: TERM-0117
type: term
canon: draft
term: the Storm Spire
say: thuh STORM SPY-er
kind: place
ref: PL-0057
```

```canon
id: TERM-0118
type: term
canon: draft
term: the Sunk
say: thuh SUNK
kind: place
ref: PL-0060
```

```canon
id: TERM-0119
type: term
canon: draft
term: Lirenne
say: lih-REN
kind: place
ref: PL-0061
```

```canon
id: TERM-0120
type: term
canon: draft
term: the Sunken Spire
say: thuh SUNK-en SPY-er
kind: place
ref: PL-0062
```

```canon
id: TERM-0121
type: term
canon: draft
term: the Open Grey
say: thee OH-pen GRAY
kind: place
ref: PL-0065
```

### Titles, words, calendar, phrases

```canon
id: TERM-0122
type: term
canon: draft
term: Helm
say: HELM
kind: title
meaning: elected ruler of the Concord, for life
```

```canon
id: TERM-0123
type: term
canon: draft
term: Your Steadiness
say: yor STED-ee-ness
kind: title
meaning: form of address to the Helm
```

```canon
id: TERM-0124
type: term
canon: draft
term: Sovereign
say: SOV-rin
kind: title
meaning: Maren's title from S09E12
```

```canon
id: TERM-0125
type: term
canon: draft
term: Cantor
say: KAN-tor
kind: title
meaning: a singer of the Spires; priest of the Choir
```

```canon
id: TERM-0126
type: term
canon: draft
term: First Cantor
say: FURST KAN-tor
kind: title
meaning: head of the Choir
```

```canon
id: TERM-0127
type: term
canon: draft
term: Lord Admiral
say: LORD AD-mer-ul
kind: title
meaning: head of the Concord fleet
```

```canon
id: TERM-0128
type: term
canon: draft
term: Captain-Lord
say: KAP-tin LORD
kind: title
meaning: elected head of the Quell island clans
```

```canon
id: TERM-0129
type: term
canon: draft
term: Dry Queen
say: DRY KWEEN
kind: title
meaning: war-leader of the Ossari
```

```canon
id: TERM-0130
type: term
canon: draft
term: Reedmaster
say: REED-mas-ter
kind: title
meaning: boss of a treadmill gang
```

```canon
id: TERM-0131
type: term
canon: draft
term: Saltwife
say: SALT-wife
kind: title
meaning: priestess of the Lady Below
```

```canon
id: TERM-0132
type: term
canon: draft
term: Gleaner
say: GLEE-ner
kind: word
meaning: Choir child-finder
```

```canon
id: TERM-0133
type: term
canon: draft
term: Listener
say: LISS-en-er
kind: word
meaning: Fennick informer or secret policeman
```

```canon
id: TERM-0134
type: term
canon: draft
term: Conclave
say: KON-klayv
kind: word
meaning: the eight-vote council that elects the Helm (meets in the Ring)
```

```canon
id: TERM-0135
type: term
canon: draft
term: the Sunken Vote
say: thuh SUNK-en VOHT
kind: word
meaning: the ninth vote of Lirenne (RULE-009)
```

```canon
id: TERM-0136
type: term
canon: draft
term: the Purchased Seat
say: thuh PUR-chast SEET
kind: word
meaning: Lantry's vote, bought from Harrow CY 252
```

```canon
id: TERM-0137
type: term
canon: draft
term: the Relay
say: thuh REE-lay
kind: word
meaning: Spire-to-Spire tone-code network (RULE-004)
```

```canon
id: TERM-0138
type: term
canon: draft
term: the Hearings
say: thuh HEER-ingz
kind: word
meaning: the courts, run by Fennick
```

```canon
id: TERM-0139
type: term
canon: draft
term: echo-stone
say: EK-oh stohn
kind: object
meaning: chip of Spire stone used by the Relay
```

```canon
id: TERM-0140
type: term
canon: draft
term: echo-shard
say: EK-oh shard
kind: object
meaning: an unlicensed echo-stone fragment
```

```canon
id: TERM-0141
type: term
canon: draft
term: hollowstone
say: HOL-oh-stohn
kind: word
meaning: the black singing stone of the Spires
```

```canon
id: TERM-0142
type: term
canon: draft
term: Spire
say: SPY-er
kind: word
meaning: one of the nine singing towers
```

```canon
id: TERM-0143
type: term
canon: draft
term: the ear
say: thee EER
kind: word
meaning: the gift of making a Spire answer
```

```canon
id: TERM-0144
type: term
canon: draft
term: songblood
say: SONG-blud
kind: word
meaning: the belief that the ear is inherited
```

```canon
id: TERM-0145
type: term
canon: draft
term: Great Song
say: GRAYT SONG
kind: word
meaning: a song of hours against storm or breach
```

```canon
id: TERM-0146
type: term
canon: draft
term: singing out
say: SING-ing OWT
kind: phrase
meaning: death of a voiceless singer who keeps singing
```

```canon
id: TERM-0147
type: term
canon: draft
term: breath-tone
say: BRETH-tohn
kind: word
meaning: the unvoiced tone a mute Cantor can still force
```

```canon
id: TERM-0148
type: term
canon: draft
term: Low Note
say: LOH NOHT
kind: word
meaning: the lullaby's part of the Spires' song (sealed meaning: SEC-002)
```

```canon
id: TERM-0149
type: term
canon: draft
term: dry-note
say: DRY-noht
kind: object
meaning: Lantry paper money
```

```canon
id: TERM-0150
type: term
canon: draft
term: dry-tithe
say: DRY-tythe
kind: word
meaning: protection tax paid by the Lows
```

```canon
id: TERM-0151
type: term
canon: draft
term: mark
say: MARK
kind: object
meaning: silver coin
```

```canon
id: TERM-0152
type: term
canon: draft
term: Tithe Map
say: TYTHE map
kind: object
meaning: yearly plan of which districts are sung first in a storm
```

```canon
id: TERM-0153
type: term
canon: draft
term: dry-pledge
say: DRY-plej
kind: word
meaning: Undertow protection racket
```

```canon
id: TERM-0154
type: term
canon: draft
term: Account Nine
say: uh-KOWNT NYNE
kind: word
meaning: Lantry's flood-speculation account
```

```canon
id: TERM-0155
type: term
canon: draft
term: Account Five
say: uh-KOWNT FYVE
kind: word
meaning: precursor of Account Nine (CY 295)
```

```canon
id: TERM-0156
type: term
canon: draft
term: Dry Charter
say: DRY CHAR-ter
kind: object
meaning: CY 295 deed transfer of drowned Ninth Sluice
```

```canon
id: TERM-0157
type: term
canon: draft
term: Hush Law
say: HUSH LAW
kind: word
meaning: RULE-006
```

```canon
id: TERM-0158
type: term
canon: draft
term: tide-post
say: TYD-post
kind: object
meaning: punishment post of the Lows
```

```canon
id: TERM-0159
type: term
canon: draft
term: Still Days
say: STIL DAYZ
kind: word
meaning: the five retuning days at year's end (RULE-010)
```

```canon
id: TERM-0160
type: term
canon: draft
term: mudlark
say: MUD-lark
kind: word
meaning: salvager of the flooded lanes
```

```canon
id: TERM-0161
type: term
canon: draft
term: treadmill walker
say: TRED-mil WAW-ker
kind: word
meaning: pump labourer
```

```canon
id: TERM-0162
type: term
canon: draft
term: debt-walker
say: DET-waw-ker
kind: word
meaning: treadmill walker working off a debt
```

```canon
id: TERM-0163
type: term
canon: draft
term: the Lady Below
say: thuh LAY-dee bih-LOH
kind: word
meaning: Lows folk faith
```

```canon
id: TERM-0164
type: term
canon: draft
term: the Hum
say: thuh HUM
kind: word
meaning: Pell's illegal singing circles (S5)
```

```canon
id: TERM-0165
type: term
canon: draft
term: Weir Terms
say: WEER TURMZ
kind: word
meaning: the CY 314 settlement (EV-0317)
```

```canon
id: TERM-0166
type: term
canon: draft
term: Spiral Book
say: SPY-rul BOOK
kind: object
meaning: Ashare text fragment (S5)
```

```canon
id: TERM-0167
type: term
canon: draft
term: the Chronicler
say: thuh KRON-ik-ler
kind: title
meaning: the narrator
```

```canon
id: TERM-0168
type: term
canon: draft
term: The Chronicle of the Dry Years
say: thuh KRON-ik-ul uv thuh DRY YEERZ
kind: object
meaning: the official record the narrator reads
```

```canon
id: TERM-0169
type: term
canon: draft
term: Quire
say: KWIRE
kind: person
meaning: the masked forger of S9-S11 (homophone of Choir - see the keeper's report)
```

```canon
id: TERM-0170
type: term
canon: draft
term: Builders
say: BIL-derz
kind: word
meaning: the official belief about who raised the Spires
```

```canon
id: TERM-0171
type: term
canon: draft
term: First Voices
say: FURST VOY-siz
kind: word
meaning: the Choir's name for the Builders
```

```canon
id: TERM-0172
type: term
canon: draft
term: Tide-King
say: TYD-king
kind: title
meaning: Chronicle title of the Ashare Keepers
```

```canon
id: TERM-0173
type: term
canon: draft
term: Keeper
say: KEE-per
kind: title
meaning: elected and later hereditary conductor of Lirenne
```

```canon
id: TERM-0174
type: term
canon: draft
term: the Breaking
say: thuh BRAY-king
kind: word
meaning: OS 700 (EV-0100)
```

```canon
id: TERM-0175
type: term
canon: draft
term: the Night of Still Water
say: thuh NYT uv STIL WAW-ter
kind: word
meaning: CY 295 (EV-0200)
```

```canon
id: TERM-0176
type: term
canon: draft
term: the Night of a Thousand Voices
say: thuh NYT uv uh THOW-zund VOY-siz
kind: word
meaning: CY 320 (EV-0319)
```

```canon
id: TERM-0177
type: term
canon: draft
term: the First Raising
say: thuh FURST RAY-zing
kind: word
meaning: S09E05 (EV-0330)
```

```canon
id: TERM-0178
type: term
canon: draft
term: the Long Ebb
say: thuh LONG EB
kind: word
meaning: once-in-a-century storm season (S11)
```

```canon
id: TERM-0179
type: term
canon: draft
term: the Great Chorus
say: thuh GRAYT KOR-us
kind: word
meaning: S12E12 (EV-0339)
```

```canon
id: TERM-0180
type: term
canon: draft
term: the Admiral's Pearl
say: thee AD-mer-ulz PURL
kind: object
meaning: Corvane heirloom ring
```

```canon
id: TERM-0181
type: term
canon: draft
term: Patient Gull
say: PAY-shent GUL
kind: object
meaning: Corvane flagship
```

```canon
id: TERM-0182
type: term
canon: draft
term: the Wet Saints
say: thuh WET SAYNTS
kind: word
meaning: a free company
```

```canon
id: TERM-0183
type: term
canon: draft
term: Isembar Ashare
say: IZ-em-bar ah-SHAH-reh
kind: person
meaning: Keeper who crowned the Keepership (prequel P2)
```

```canon
id: TERM-0184
type: term
canon: draft
term: Sereth Ilvane
say: SEH-reth IL-vayn
kind: person
meaning: matriarch who led the Nine in OS 700 (prequel P3)
```

```canon
id: TERM-0185
type: term
canon: draft
term: Builders' Age
say: BIL-derz AYJ
kind: word
ref: ERA-BA
meaning: era BA
```

```canon
id: TERM-0186
type: term
canon: draft
term: Old Song
say: OHLD SONG
kind: word
ref: ERA-OS
meaning: era OS
```

```canon
id: TERM-0187
type: term
canon: draft
term: Concord Year
say: KON-kord YEER
kind: word
ref: ERA-CY
meaning: era CY
```

```canon
id: TERM-0188
type: term
canon: draft
term: Sovereign Years
say: SOV-rin YEERZ
kind: word
ref: ERA-SY
meaning: era SY
```

```canon
id: TERM-0189
type: term
canon: draft
term: Firstwater
say: FURST-waw-ter
kind: word
meaning: month 1
```

```canon
id: TERM-0190
type: term
canon: draft
term: Rains
say: RAYNZ
kind: word
meaning: month 2
```

```canon
id: TERM-0191
type: term
canon: draft
term: Silting
say: SIL-ting
kind: word
meaning: month 3
```

```canon
id: TERM-0192
type: term
canon: draft
term: Reedmonth
say: REED-munth
kind: word
meaning: month 4
```

```canon
id: TERM-0193
type: term
canon: draft
term: Highsun
say: HY-sun
kind: word
meaning: month 5
```

```canon
id: TERM-0194
type: term
canon: draft
term: Saltdry
say: SALT-dry
kind: word
meaning: month 6
```

```canon
id: TERM-0195
type: term
canon: draft
term: Ember
say: EM-ber
kind: word
meaning: month 7 (season: the Ember)
```

```canon
id: TERM-0196
type: term
canon: draft
term: Fallow
say: FAL-oh
kind: word
meaning: month 8
```

```canon
id: TERM-0197
type: term
canon: draft
term: Mistcall
say: MIST-kawl
kind: word
meaning: month 9
```

```canon
id: TERM-0198
type: term
canon: draft
term: Longdark
say: LONG-dark
kind: word
meaning: month 10
```

```canon
id: TERM-0199
type: term
canon: draft
term: Still
say: STIL
kind: word
meaning: the 5 Still Days (month 11)
```

```canon
id: TERM-0200
type: term
canon: draft
term: Humday
say: HUM-day
kind: word
meaning: weekday 1
```

```canon
id: TERM-0201
type: term
canon: draft
term: Reedday
say: REED-day
kind: word
meaning: weekday 2
```

```canon
id: TERM-0202
type: term
canon: draft
term: Bellday
say: BEL-day
kind: word
meaning: weekday 3
```

```canon
id: TERM-0203
type: term
canon: draft
term: Drumday
say: DRUM-day
kind: word
meaning: weekday 4
```

```canon
id: TERM-0204
type: term
canon: draft
term: Hornday
say: HORN-day
kind: word
meaning: weekday 5
```

```canon
id: TERM-0205
type: term
canon: draft
term: Restday
say: REST-day
kind: word
meaning: weekday 6
```

```canon
id: TERM-0206
type: term
canon: draft
term: the Wet
say: thuh WET
kind: word
meaning: season: Firstwater-Silting
```

```canon
id: TERM-0207
type: term
canon: draft
term: the Green
say: thuh GREEN
kind: word
meaning: season: Reedmonth-Saltdry
```

```canon
id: TERM-0208
type: term
canon: draft
term: the Mist
say: thuh MIST
kind: word
meaning: season: Mistcall-Longdark
```

```canon
id: TERM-0209
type: term
canon: draft
term: Calm is bought.
say: KAHLM iz BAWT
kind: phrase
meaning: Quell words; recurring line
```

```canon
id: TERM-0210
type: term
canon: draft
term: Who pays for the dry?
say: hoo PAYZ for thuh DRY
kind: phrase
meaning: recurring line
```

```canon
id: TERM-0211
type: term
canon: draft
term: ...and the water kept its counsel.
say: and thuh WAW-ter KEPT its KOWN-sel
kind: phrase
meaning: the Chronicler's sign-off (changes only in S12E13)
```

---

## EXAMPLE (placeholder, not canon)

```canon
id: TERM-EX-0001
type: term
canon: draft
example: true
term: Tamsin Varnel
say: TAM-sin VAR-nel
ipa: /ˈtæmsɪn ˈvɑːrnəl/
kind: person
ref: CH-EX-0003
```

```canon
id: TERM-EX-0002
type: term
canon: draft
example: true
term: Greyhold
say: GRAY-hold
kind: place
ref: PL-EX-0002
```

```canon
id: TERM-EX-0003
type: term
canon: draft
example: true
term: Oren Varnel
say: OR-en VAR-nel
kind: person
ref: CH-EX-0001
```

```canon
id: TERM-EX-0004
type: term
canon: draft
example: true
term: Ilsa Varnel
say: IL-sah VAR-nel
kind: person
ref: CH-EX-0002
```

```canon
id: TERM-EX-0005
type: term
canon: draft
example: true
term: Brannoch Hale
say: BRAN-ock HAIL
kind: person
ref: CH-EX-0004
```

```canon
id: TERM-EX-0006
type: term
canon: draft
example: true
term: House Varnel
say: HOWSS VAR-nel
kind: house
ref: HS-EX-001
```

```canon
id: TERM-EX-0007
type: term
canon: draft
example: true
term: Saltmere
say: SALT-meer
kind: place
ref: PL-EX-0001
```
