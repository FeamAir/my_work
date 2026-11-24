#!/usr/bin/env python3
"""S01E01 animatic, step 5: placeholder sound.

  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=70 python3 -I sound.py sfx     # ElevenLabs SFX library subset (cap 15k credits)
  python3 -I sound.py synth                                          # $0: lullaby, stone tone, death tone, fork, temp music
Files: output/S01E01/animatic/audio/{sfx,synth}/  (R2 S01E01/animatic/audio/)

Prompts and IDs: studio/sound/pilot_sound_design.md §2 (library). Ambiences are cut to 10 s and looped in assembly.
Lullaby rule (production notes §6): the five notes exist only in Sc 1, 3, 20 (Sc 20: stone tone only, no melody).
Temp music = synthesized pads, labelled on screen as TEMP MUSIC; never the lullaby.
"""
import json
import os
import subprocess
import sys

ROOT = "/home/user/my_work"
sys.path.insert(0, ROOT)
AU = f"{ROOT}/output/S01E01/animatic/audio"
SFX_DIR, SYN = f"{AU}/sfx", f"{AU}/synth"

# (id, prompt, seconds, influence) — prompts verbatim from pilot_sound_design.md §2
SFX = [
    ("amb_flood-night-street", "Night flood in a narrow street of wooden stilt houses, heavy rain falling on deep still black water, water lapping against doors and walls, gutters overflowing, no music, no speech", 10, 0.4),
    ("amb_underwater", "Underwater perspective in a flooded street, muffled pressure, slow drifting bubbles, distant muffled thuds, no deep rumble, no music, no speech", 6, 0.4),
    ("amb_lows-dawn-ebb", "Dawn in a stilt town at low tide, wet mud flats ticking and popping, slow drips from wooden houses, distant gulls, a wooden rope bridge creaking, very calm, no music, no speech", 10, 0.4),
    ("amb_sump-pool", "Small enclosed pool of still black water under an old stone sluice, slow echoing drips, very quiet, eerie stillness, no music, no speech", 10, 0.4),
    ("amb_lows-house-interior", "Inside a small wooden stilt house in the morning, faint water lapping below the floor, wood creaks, quiet, no music, no speech", 10, 0.4),
    ("amb_treadmill-pump", "Giant wooden treadmill wheels turning slowly over a pump sump, deep wooden creaking, rhythmic heavy footfalls of many workers on step boards, water churning in a sump, no music, no speech", 10, 0.4),
    ("amb_spire-stair", "Inside a spiral stair of a huge black stone tower, cool resonant air, faint deep tonal hum in the walls, very quiet, no music, no speech", 10, 0.4),
    ("amb_harbour", "Busy harbour seen from high above in strong wind, choppy waves slapping stone quays, ships rigging creaking, seagulls calling, no music, no speech", 10, 0.4),
    ("amb_tithe-hall", "Very large stone hall with high ceiling, low murmur of a gathered noble crowd, cloth rustle, distant footsteps on marble, indistinct, no intelligible words, no music", 10, 0.4),
    ("amb_tithe-hall-empty", "Very large stone hall, silent, faint air, distant wind at tall windows, no music, no speech", 8, 0.3),
    ("amb_counting-hall", "Huge quiet hall of clerks, felt floors, dozens of quill pens scratching on paper, pages turned with ivory blades, almost silent, no music, no speech", 10, 0.4),
    ("amb_relay-room", "Small stone room with a wall of caged stones, faint electric-like resonance, no music, no speech", 8, 0.4),
    ("amb_mids-gate-dusk", "City gate at dusk, distant pump gears, a barracks drum far away, guards' armour shifting, no music, no speech", 10, 0.4),
    ("amb_lows-dusk-tide", "Dusk in a stilt town with the tide back in, water lapping under wooden houses and plank walks, lanterns creaking on hooks, quiet, no music, no speech", 10, 0.4),
    ("sfx_whistles-alarm", "Long shrill whistles blown from rooftop to rooftop at night in heavy rain, alarm, distant and near, iron beaten on iron", 6, 0.5),
    ("sfx_gate-bar-drag", "Heavy iron bar dragged across a great iron gate, long grinding scrape, then a deep heavy clang as it drops into its brackets, outdoor, rain", 6, 0.6),
    ("sfx_fists-iron-gate", "Many fists pounding on an iron gate from the far side, desperate, irregular, metallic booming, outdoor rain", 6, 0.5),
    ("walla_flood-crowd", "Frightened crowd crushed against a closed gate at night in rain, panicked cries and shouts, indistinct, no intelligible words, medium distance", 8, 0.4),
    ("sfx_rowboat-oars", "Small wooden rowboat moving slowly on still flood water at night, gentle oar dips, wood creaks, close", 6, 0.5),
    ("foley_knock-doorpost", "Fist knocking three times on an old wet wooden doorpost, outdoor, close", 2, 0.6),
    ("foley_chain-box", "Small iron box chained to a wrist, chain clinking, lid opening, coins dropped in, close", 3, 0.6),
    ("foley_mud-steps", "Footsteps squelching in deep wet mud, suction pulls, slow, close", 5, 0.6),
    ("sfx_rake-snag", "Rake snagging on something under black water, rope creaking taut, a small splash as it is pulled up, close", 4, 0.6),
    ("sfx_ripple-tremble", "Still water surface trembling into fine rings, delicate liquid shiver, very close, quiet, glassy", 5, 0.5),
    ("foley_ladder", "Wooden ladder creaking under small quick footsteps climbing", 3, 0.6),
    ("foley_net-chest", "Heavy wooden chest dragged a few inches by a rope handle on wooden floor, then someone sits down on it with a thump", 3, 0.6),
    ("foley_parchment", "Large parchment map unrolled across a wooden table, stiff paper crackle", 3, 0.6),
    ("foley_page-turn", "A single heavy old book page turned slowly, dry paper, close, quiet room", 1.5, 0.6),
    ("sfx_reed-whistle", "One sharp short blast on a small reed whistle, outdoor", 1, 0.7),
    ("foley_silver-cup", "Silver cup set down on a stone table a little too hard, a single clink, close", 2, 0.6),
    ("sfx_fall-table", "Old man collapsing forward across a wooden table, chair scraping back, heavy thud, a rolled parchment sliding off the table and rolling across a stone floor", 5, 0.5),
    ("walla_hall-laugh", "Large hall of nobles laughing warmly together at a joke, indistinct, no intelligible words", 4, 0.5),
    ("walla_hall-gasp", "Large hall crowd gasps and goes silent, chairs scrape, indistinct, no intelligible words", 3, 0.5),
    ("foley_staff-strike", "Iron-shod wooden staff struck once on a polished stone floor in a large hall, resonant", 1.5, 0.6),
    ("foley_stick-felt", "Wooden stick tapping once on a felt floor, soft dull thud, then many chairs creaking at once as people straighten", 3, 0.5),
    ("foley_brass-clip", "Small brass ledger clip laid down on paper, a soft precise metallic click", 1, 0.7),
    ("sfx_ink-drop", "A single drop of ink falling onto paper in total silence, tiny, close, exaggerated", 1, 0.7),
    ("foley_bell-small", "Small bronze bell in a stone hall rung once by a rope, clear, short decay", 3, 0.6),
    ("foley_guards-file", "File of armoured guards shifting and marching a few steps, helmets, leather and mail", 5, 0.5),
    ("sfx_wheel-stop", "Giant wooden treadmill wheel slowing down and stopping, long creak, footsteps stop", 5, 0.5),
    ("foley_rope-creak", "Thick wet rope pulled taut and creaking under strain, close", 3, 0.6),
    ("foley_tin-buttons", "Handful of small buttons and a buckle dropped one by one into a tin box, close", 3, 0.6),
]


def cmd_sfx():
    from pipeline import elevenlabs_client as el
    os.makedirs(SFX_DIR, exist_ok=True)
    before = el.subscription()["character_count"]
    print("credits used before", before)
    est = sum(s for _, _, s, _ in SFX) * el.SFX_CREDITS_PER_SECOND
    print("estimate", est)
    for sid, prompt, secs, infl in SFX:
        out = f"{SFX_DIR}/{sid}.mp3"
        if os.path.exists(out):
            continue
        used = el.subscription()["character_count"] - before
        if used > 14000:
            print("STOP: SFX credit cap reached", used)
            break
        try:
            el.sfx(prompt, out, duration_seconds=max(0.5, secs), prompt_influence=infl, loop=sid.startswith("amb_"))
            print("ok", sid, flush=True)
        except Exception as e:
            print("ERR", sid, str(e)[:200], flush=True)
    after = el.subscription()["character_count"]
    print("credits used after", after, "this run", after - before)
    json.dump(dict(before=before, after=after, used=after - before), open(f"{SFX_DIR}/credits.json", "w"))


def ff(args):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + args, check=True)


def hz(note):
    names = {"C": 0, "Db": 1, "D": 2, "Eb": 3, "E": 4, "F": 5, "Gb": 6, "G": 7, "Ab": 8, "A": 9, "Bb": 10, "B": 11, "G#": 8, "F#": 6, "C#": 1}
    n, o = note[:-1], int(note[-1])
    return 440.0 * 2 ** ((names[n] + 12 * (o + 1) - 69) / 12)


def hum(notes, out, beat=0.44, gain=0.35, oct_shift=0, breathy=0.02):
    """Closed-mouth hum: sine + soft 2nd/3rd partial, slow vibrato, soft attack per note (rhythm 3-1-2-1-3 eighths)."""
    parts = []
    t = 0.0
    for note, eighths in notes:
        f = hz(note) * (2 ** oct_shift)
        d = eighths * beat
        parts.append((t, d, f))
        t += d
    total = t + 0.6
    expr = "+".join(
        f"between(t,{a:.3f},{a + d + 0.25:.3f})*min(1,(t-{a:.3f})/0.08)*max(0,min(1,({a + d + 0.25:.3f}-t)/0.25))"
        f"*(sin(2*PI*{f:.2f}*t+0.8*sin(2*PI*5.2*t))+0.35*sin(4*PI*{f:.2f}*t)+0.12*sin(6*PI*{f:.2f}*t))"
        for a, d, f in parts)
    ff(["-f", "lavfi", "-i", f"aevalsrc='{gain}*({expr})':s=48000:d={total:.2f}",
        "-f", "lavfi", "-i", f"anoisesrc=d={total:.2f}:c=pink:a={breathy}:r=48000",
        "-filter_complex", "[0][1]amix=inputs=2:normalize=0,lowpass=f=2400,aecho=0.6:0.4:60:0.2", "-ac", "1", out])


def tone(out, dur, partials, attack=0.25, release=1.0, beat_hz=0.0, gain=0.3):
    expr = "+".join(f"{a}*sin(2*PI*{f}*t)" + (f"*(1+0.3*sin(2*PI*{beat_hz}*t))" if beat_hz else "") for f, a in partials)
    env = f"min(1,t/{attack})*min(1,({dur}-t)/{release})"
    ff(["-f", "lavfi", "-i", f"aevalsrc='{gain}*({expr})*{env}':s=48000:d={dur}", "-ac", "1", out])


def pad(out, dur, chord, gain=0.12, lp=1800, trem=0.15):
    """Temp music placeholder: slow detuned pad on a chord (no lullaby notes as melody)."""
    expr = "+".join(f"sin(2*PI*{hz(n):.2f}*t)+0.6*sin(2*PI*{hz(n) * 1.003:.2f}*t)" for n in chord)
    env = f"min(1,t/2.5)*min(1,({dur}-t)/2.5)*(1+{trem}*sin(2*PI*0.13*t))"
    ff(["-f", "lavfi", "-i", f"aevalsrc='{gain}*({expr})*{env}':s=48000:d={dur}",
        "-af", f"lowpass=f={lp},aecho=0.7:0.5:300|700:0.25|0.15", "-ac", "2", out])


def cmd_synth():
    os.makedirs(SYN, exist_ok=True)
    core = [("Db5", 3), ("Bb4", 1), ("Eb4", 2), ("F4", 1), ("Bb4", 3)]
    hum(core, f"{SYN}/lullaby_woman_v1.wav")                                    # Sc 1 (x2: second quieter in mix)
    hum([("Db6", 2), ("Bb5", 3)], f"{SYN}/lullaby_baby2_v1.wav", beat=0.3, gain=0.18, breathy=0.01)  # Sc 1 baby
    hum(core[:3], f"{SYN}/hum_pell3_v1.wav", beat=0.4, oct_shift=-1, gain=0.3, breathy=0.05)       # Sc 3 Pell, 3 notes
    bb1 = hz("Bb1")
    stone = [(bb1, 1.0), (bb1 * 2, 0.5), (bb1 * 3, 0.35), (bb1 * 4, 0.3), (hz("Bb4"), 0.08), (hz("F5"), 0.06)]
    tone(f"{SYN}/stone_tone_6s_v1.wav", 6, stone, attack=0.25, release=1.5, beat_hz=2.5, gain=0.35)
    tone(f"{SYN}/stone_tone_12s_v1.wav", 12, stone, attack=0.25, release=3.0, beat_hz=2.5, gain=0.35)
    c5 = hz("C5")
    # death relay: three long tones ~1.6 s, gap 1.6 s
    for i in range(3):
        tone(f"{SYN}/_dt{i}.wav", 1.6, [(c5, 1), (c5 * 2, 0.2)], attack=0.1, release=0.5, gain=0.25)
    ff(["-i", f"{SYN}/_dt0.wav", "-i", f"{SYN}/_dt1.wav", "-i", f"{SYN}/_dt2.wav", "-filter_complex",
        "[0]apad=pad_dur=1.6[a];[1]apad=pad_dur=1.6[b];[a][b][2]concat=n=3:v=0:a=1,aecho=0.8:0.6:400:0.3", f"{SYN}/death_tone_v1.wav"])
    tone(f"{SYN}/fork_c5_v1.wav", 6, [(c5, 1), (c5 * 2.76, 0.05)], attack=0.01, release=5.0, gain=0.25)
    tone(f"{SYN}/ione_c5_v1.wav", 12, [(c5, 1), (c5 * 2, 0.3), (c5 * 3, 0.1)], attack=0.8, release=2.0, beat_hz=5.0, gain=0.22)
    tone(f"{SYN}/spire_hum_c2c3_v1.wav", 20, [(hz("C2"), 1), (hz("C3"), 0.6), (hz("G3"), 0.15)], attack=3, release=3, beat_hz=0.5, gain=0.3)
    tone(f"{SYN}/spire_flat_v1.wav", 8, [(hz("C2") * 0.97, 0.6), (hz("C3") * 0.97, 0.4), (hz("C4") * 0.97, 0.2)], attack=1.5, release=2, beat_hz=1.3, gain=0.2)
    tone(f"{SYN}/heartbeat_v1.wav", 4, [(55, 1)], attack=0.01, release=0.2, gain=0.0)  # placeholder silence bed
    # temp music pads (labelled TEMP MUSIC on screen)
    pad(f"{SYN}/mus_M03_lows_v1.wav", 20, ["D3", "A3", "E4"], trem=0.4)
    pad(f"{SYN}/mus_M05_archive_v1.wav", 60, ["G2", "D3", "A3", "C4"])
    pad(f"{SYN}/mus_TITLE_v1.wav", 9, ["E3", "B3", "G#4", "E4"], gain=0.15)
    pad(f"{SYN}/mus_M06_pitch_v1.wav", 30, ["C3", "G3", "D4"])
    pad(f"{SYN}/mus_M07_corvane_v1.wav", 25, ["F2", "C3", "A3", "F4"])
    pad(f"{SYN}/mus_M08_held_v1.wav", 40, ["A3", "E4"], trem=0.05)
    pad(f"{SYN}/mus_M09_clock_v1.wav", 32, ["D3", "A3", "F4"], trem=0.6)
    for i in range(3):
        os.remove(f"{SYN}/_dt{i}.wav")
    print("synth ok", sorted(os.listdir(SYN)))


if __name__ == "__main__":
    {"sfx": cmd_sfx, "synth": cmd_synth}[sys.argv[1]]()
