"""Pronunciation probe for world names (PAID). Carrier phrase from tts_pronunciation_test.md §2.2.

    python3 studio/sound/tools/pron_probe.py run <tag> [--dict ID:VER] [--terms a,b] [--voices V,..]
Writes output/S01E01/animatic/pron/<tag>/<voice>_<term>.mp3 and appends rows to
studio/sound/probe/pron_results.csv (with an automatic speech-to-text transcript as a hint only).
"""
import argparse, csv, json, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO))
from pipeline import elevenlabs_client as el  # noqa: E402

MODEL = "eleven_v4_turbo"
VOICES = {"NARR01": "Kq376vQT4X9raogOKEpK", "V01": "iXg6m3okqCpdUH3cAzLs", "V08": "4NQbUoR4U0anhExNcJRR"}
TERMS = {  # term: (say from glossary, carrier override or None)
    "Ashare": "ah-SHAH-reh", "Ilvane": "IL-vayn", "Oshra": "OSH-rah", "Neveh": "NEH-veh",
    "Ione": "eye-OH-nee", "Ruel": "ROO-el", "Lucan Dask": "LOO-kan DASK", "Longdark": "LONG-dark",
    "Highwater": "HY-waw-ter", "Corvane": "kor-VAYN", "Cantor": "KAN-tor", "Wren Roan": "REN ROHN",
    "Ninth Sluice": "NYNTH SLOOSS", "tithe": "TYTHE", "Lows": "LOHZ", "Spires": "SPY-erz",
    "Choir": "KWIRE", "Concord": "KON-kord",
}
HOMOGRAPHS = {
    "read_past": "By law the Helm reads the map aloud, and signs it; and the balance of that year was read on the sixth of Longdark.",
    "read_present": "It is drawn, Ruel. I only read it.",
    "counsel": "…and the water kept its counsel.",
    "lows_mids": "The Steps, the Mids and the Lows. Second Song. The Mids, dike to dike.",
}
CSV = REPO / "studio/sound/probe/pron_results.csv"
FIELDS = ["tag", "voice", "model", "term", "say", "text", "dict", "file", "stt", "verdict", "heard_as", "fix_step"]


def carrier(t):
    return f"{t}. That is how the name is written. They spoke of {t} in the hall, and the clerk wrote down {t}."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tag")
    ap.add_argument("--dict")
    ap.add_argument("--terms")
    ap.add_argument("--voices", default="NARR01,V01")
    ap.add_argument("--homographs", action="store_true")
    a = ap.parse_args()
    dicts = [tuple(a.dict.split(":"))] if a.dict else None
    items = {}
    terms = a.terms.split(",") if a.terms else list(TERMS)
    for t in terms:
        items[t] = carrier(t)
    if a.homographs:
        items.update(HOMOGRAPHS)
    out = REPO / "output/S01E01/animatic/pron" / a.tag
    new = not CSV.exists()
    with CSV.open("a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, FIELDS)
        if new:
            w.writeheader()
        for v in a.voices.split(","):
            for t, text in items.items():
                f = out / f"{v}_{t.replace(' ', '_')}.mp3"
                el.tts(text, VOICES[v], f, model_id=MODEL, voice_settings={"stability": 0.5, "similarity_boost": 0.8},
                       seed=11, pronunciation_dictionaries=dicts)
                stt = el.speech_to_text(f).get("text", "")
                row = dict(tag=a.tag, voice=v, model=MODEL, term=t, say=TERMS.get(t, ""), text=text,
                           dict=a.dict or "", file=str(f.relative_to(REPO)), stt=stt)
                w.writerow(row)
                print(v, t, "|", stt, flush=True)


if __name__ == "__main__":
    main()
