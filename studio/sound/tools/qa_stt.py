"""QA of draft reads by speech-to-text (PAID, small): flags dropped/extra words and tags read aloud.
Writes `stt` and `qa` into output/S01E01/animatic/vo/manifest.json. Transcripts are hints, not truth.

    python3 studio/sound/tools/qa_stt.py [--force]
"""
import argparse, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO))
from pipeline import elevenlabs_client as el  # noqa: E402

OUT = REPO / "output/S01E01/animatic/vo"
MAN = OUT / "manifest.json"
NUM = {"forty-one": "41", "forty": "40", "fifteen": "15", "thirty": "30"}


def toks(t):
    t = t.lower().replace("’", "'")
    t = re.sub(r"\[[^\]]*\]", " ", t)
    return [w for w in re.findall(r"[a-z0-9']+", t)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    man = json.loads(MAN.read_text(encoding="utf-8"))
    for rel, e in sorted(man.items()):
        if "stt" in e and not a.force:
            continue
        r = el.speech_to_text(OUT / rel)
        e["stt"] = r.get("text", "")
        want, got = toks(e["text"]), toks(e["stt"])
        tagwords = set(toks(" ".join(re.findall(r"\[([^\]]*)\]", e["tts_text"]))))
        missing = [w for w in want if w not in got]
        extra = [w for w in got if w not in want]
        spoken_tags = [w for w in extra if w in tagwords]
        e["qa"] = "ok" if not missing and not spoken_tags and len(extra) <= 1 else \
            f"check: missing={missing} extra={extra}" + (f" TAG-READ={spoken_tags}" if spoken_tags else "")
        MAN.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
        print(rel, "|", e["qa"], "|", e["stt"][:90], flush=True)


if __name__ == "__main__":
    main()
