"""Anthem v2 composition plans (composer r5). Same 7-section grid as r4 (12+9+24+12+12+12+6 = 87.0 s, 80 BPM,
bar 3.0 s). Intro, hook, answer and logo are conditioned on the uploaded 42 s call guide (placeholder THEME,
resolved by run_music.py --theme-id; guide = guide 0-12 s + guide 57-87 s), groove / theme / rise on the same
ranges of take2 s8032 (the approved groove, song 2pOkETSO6yen6lzuOL7j). Variants differ in condition_strength.

    python3 make_v2_plans.py   -> anthem_v2_plan_a.json (full 87 s, take1) + _h1/_h2.json (second half, takes 2/3)
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TAKE2 = "2pOkETSO6yen6lzuOL7j"
# section -> (song, ref start ms) ; refs have the chunk's own duration
REF = [("THEME", 0), (TAKE2, 12000), (TAKE2, 21000), (TAKE2, 45000), ("THEME", 12000), ("THEME", 24000), ("THEME", 36000)]
BANS = ["key change", "modulation", "F-sharp major chord", "F major chord", "Picardy third", "low drone",
        "pedal tone", "sustained sub bass", "808", "vocals", "choir", "humming", "singing", "vocal chops",
        "synth pad", "synth brass", "General MIDI", "EDM", "trap hi-hats", "drum machine", "electric guitar",
        "riser synth", "fade out to silence"]
BASE = ["instrumental", "heroic cinematic main title anthem", "live symphony orchestra recording, real brass section",
        "F minor", "80 BPM", "4/4"]
GROOVE = ["live ensemble drums in a big wooden hall: deep short kick, fat toms, foot stamps on planks, hand claps",
          "stamps on beats 1 and 3, syncopated claps, the same groove all the way"]
CALL = ("the call: a short low C, a leap up a full octave to a long high C, then B-flat A-flat G, home on A-flat; "
        "again the octave leap C to C, a turn D-flat C, then B-flat A-flat down to a long F")

SECTIONS = [
    ("Intro - the call", 0, 12000,
     "{instrumental, one huge orchestral hit at 0:00, then the horns call the main motif, loud and clear}",
     ["at 0:00 one huge tutti hit: timpani, bass drum, low brass chord, loud from the very first moment",
      "right on the hit four French horns in unison call the motif, bold and proud, middle register", CALL,
      "a trumpet joins the second octave leap", "strings hold soft F minor chords underneath, no groove yet"],
     ["drums groove", "pad", "soft intro", "quiet intro", "fade in"]),
    ("Groove - the Lows", 12000, 9000,
     "{instrumental, the drum groove enters, staccato strings drive}",
     GROOVE + ["staccato low strings and harp ostinato in eighth notes grouped 3+3+2",
               "short horn stabs on the offbeats echo the call", "stubborn, alive"],
     ["melody"]),
    ("Theme", 21000, 24000,
     "{instrumental, the main melody in strings and horns over the groove}",
     GROOVE + ["violins, violas and French horns in unison carry the main melody, singing, middle register",
               "each phrase starts with a short note and leaps up to a long note, then falls by steps",
               "a countermelody in the cellos", "proud, hopeful"],
     []),
    ("Rise - the Steps", 45000, 12000,
     "{instrumental, building to the climax, then one breath}",
     GROOVE + ["trumpets and horns answer with rising fanfare calls",
               "snare roll and tom fill grow louder every bar",
               "the last half bar drops to drums only, then one breath of silence before the climax"],
     []),
    ("Hook - the call, full orchestra", 57000, 12000,
     "{instrumental, the climax: the whole brass section plays the call with the octave leap, over the groove}",
     ["the biggest moment: everything enters together on the first downbeat with a huge hit",
      "all horns, trumpets and trombones in unison play the call, violins double it an octave higher", CALL,
      "the melody is loud, clear and in front of everything, easy to hum",
      "timpani on every downbeat"] + GROOVE + ["triumphant, heroic, unforgettable"],
     []),
    ("Answer - the call returns", 69000, 12000,
     "{instrumental, the call returns, the second half climbs higher and ends open}",
     ["a hit on the first downbeat, the full brass section plays the call again with violins an octave higher",
      "first half the same as before: short low C, octave leap to a long high C, then B-flat A-flat G A-flat",
      "second half climbs: a short E-flat, octave leap to a long high E-flat, then D-flat C B-flat, ending open on C"]
     + GROOVE + ["big ensemble drum hits every half bar", "proud, rising"],
     []),
    ("Logo sting", 81000, 6000,
     "{instrumental, two tutti hits, the last one resolves to F minor and rings}",
     ["beat 1: tutti hit on a C major chord, the brass plays a quick octave leap C to C",
      "beat 3: the biggest hit of the piece on F minor, trumpets leap F to a long high F, horns hold F",
      "the F minor chord rings out on brass and strings for three seconds, strong and resolved",
      "no new melody, no groove after the last hit"],
     ["drum groove", "new melody", "fade in"]),
]

VARIANTS = {  # condition_strength per section (intro, groove, theme, rise, hook, answer, logo)
    "a": ["high", "low", "low", "low", "high", "high", "high"],
}


def plan(v):
    chunks = []
    for (name, start, dur, head, pos, neg), s, (song, rs) in zip(SECTIONS, VARIANTS[v], REF):
        chunks.append({
            "text": f"[{name}]\n{head}",
            "duration_ms": dur,
            "positive_styles": BASE + pos,
            "negative_styles": neg + BANS,
            "conditioning_ref": {"song_id": song, "range": {"start_ms": rs, "end_ms": rs + dur},
                                 "condition_strength": s},
        })
    return {"chunks": chunks}


if __name__ == "__main__":
    for v in VARIANTS:
        p = f"{HERE}/anthem_v2_plan_{v}.json"
        json.dump(plan(v), open(p, "w"), indent=1)
        print(p)


# --- r5 round 2: second-half takes (57.0-87.0 + 3 s tail chunk that is cut off). Take1 showed that the FIRST chunk
# follows its reference closely (intro = guide, chroma sim 0.99) while later chunks drift to the context (hook 0.39).
# So the hook gets its own generation in which it is the first chunk; it is spliced onto a full take at the 57.0 hit.
TAIL = ("Ring", 3000, "{instrumental, the last F minor chord still ringing, decaying slowly}",
        ["the F minor chord from the last hit keeps ringing in strings and horns, slowly getting softer"],
        ["new melody", "drum groove", "new hit"])


def half_plan(strength, adherence="high"):
    chunks = []
    for (name, start, dur, head, pos, neg), (song, rs) in zip(SECTIONS[4:], REF[4:]):
        chunks.append({"text": f"[{name}]\n{head}", "duration_ms": dur, "positive_styles": BASE + pos,
                       "negative_styles": neg + BANS, "context_adherence": adherence,
                       "conditioning_ref": {"song_id": song, "range": {"start_ms": rs, "end_ms": rs + dur},
                                            "condition_strength": strength}})
    name, dur, head, pos, neg = TAIL
    chunks.append({"text": f"[{name}]\n{head}", "duration_ms": dur, "positive_styles": BASE + pos,
                   "negative_styles": neg + BANS})
    return {"chunks": chunks}


if __name__ == "__main__":
    for tag, st, ad in (("h1", "high", "high"), ("h2", "medium", "high")):
        p = f"{HERE}/anthem_v2_plan_{tag}.json"
        json.dump(half_plan(st, ad), open(p, "w"), indent=1)
        print(p)
