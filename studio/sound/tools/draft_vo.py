"""Draft TTS read of every S01E01 line for the animatic (PAID: STUDIO_ALLOW_PAID=1).

    python3 studio/sound/tools/draft_vo.py gen [--only L001,L002] [--alt]   # generate (skips existing)
    python3 studio/sound/tools/draft_vo.py table                           # durations md + csv
    python3 studio/sound/tools/draft_vo.py upload                          # R2: S01E01/animatic/vo/<name>

Inputs: extract_lines.py (segments), studio/sound/S01E01_vo_plan.json (tags/modes),
studio/sound/casting/casting_log.json (voice_ids), studio/sound/lexicon/hollowstone_en_draft_v1.json.
Outputs: output/S01E01/animatic/vo/<shot>_<line>_<VOICE>.mp3 (+ alt/ takes), manifest
output/S01E01/animatic/vo/manifest.json, studio/sound/S01E01_vo_durations.{md,csv}.
"""
import argparse, csv, json, re, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
TOOLS = Path(__file__).parent
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(TOOLS))
from pipeline import elevenlabs_client as el  # noqa: E402
import audio_measure as am  # noqa: E402

OUT = REPO / "output/S01E01/animatic/vo"
PLAN = json.loads((REPO / "studio/sound/S01E01_vo_plan.json").read_text(encoding="utf-8"))
CAST = json.loads((REPO / "studio/sound/casting/casting_log.json").read_text(encoding="utf-8"))
LEX = json.loads((REPO / "studio/sound/lexicon/hollowstone_en_draft_v1.json").read_text(encoding="utf-8"))
MANIFEST = OUT / "manifest.json"
SEEDS = (101, 202)
NAMES = {"V01_PELL": "Pell", "V02_WICK": "Wick", "V03_NAN": "Nan", "V04_IONE": "Ione", "V05_HOLLIS": "Hollis",
         "V06_RUEL": "Ruel", "V07_LUCAN": "Lucan (the Helm)", "V08_URSEL": "Ursel", "V09_ODO": "Lord of the Relay (Odo)",
         "V10_CORR": "Reedmaster (Corr)", "V11_MAGS": "Mags", "V12_COLLECTOR": "Tithe-collector",
         "V13_ATTENDANT": "Choir attendant", "V14_RELAYKEEPER": "Relay-keeper", "V15_GUARD": "Rusk guard",
         "V16_CLERK": "Clerk at the next desk", "V17_STEWARD": "Steward", "NARR01": "The Chronicler"}


def segments():
    raw = subprocess.run([sys.executable, "-I", str(TOOLS / "extract_lines.py")], capture_output=True,
                         text=True, check=True).stdout
    return json.loads(raw)


def voice_id(v):
    key = "NARR01" if v == "NARR01" else v[:3]
    return CAST[key]["selected"]["voice_id"]


def tts_text(text):
    t = re.sub(r"^[—…\s]+", "", text)          # leading dash/ellipsis: continuation marks, not speech
    t = re.sub(r"\s*—\s*$", "—", t)            # keep a trailing cut-off dash attached
    return t


def request_for(seg, alt_model=False):
    v, lid = seg["voice"], seg["line_id"]
    spec = PLAN["lines"].get(lid, {})
    text = tts_text(seg["text"])
    dicts = [(LEX["elevenlabs"]["id"], LEX["elevenlabs"]["version_id"])]
    if v == "NARR01" and not alt_model:
        vs = dict(PLAN["narr_v2"], speed=PLAN["narr_speed"].get(lid, 0.85))
        return dict(text=text, model_id=PLAN["narr_model"], voice_settings=vs, pronunciation_dictionaries=dicts)
    st = PLAN["stability"][v]
    mode = spec.get("mode", "B")
    vs = {"stability": st.get(mode, st["B"]), "similarity_boost": 0.8}
    tags = spec.get("tags", "")
    return dict(text=(tags + " " + text).strip(), model_id=PLAN["model"], voice_settings=vs,
                pronunciation_dictionaries=dicts)


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}


def gen(only=None, alt=False):
    man = load_manifest()
    segs = [s for s in segments() if not (only and s["line_id"] not in only)]
    for s in segs:
        if "skip" in PLAN["lines"].get(s["line_id"], {}):
            continue
        jobs = [("main", s["name"] + ".mp3", request_for(s), SEEDS[0])]
        if alt and (s["fixed"] or "LIPSYNC" in s["meta"] or s["voice"] == "NARR01"):
            jobs.append(("t2", f"alt/{s['name']}_t2.mp3", request_for(s), SEEDS[1]))
            if s["voice"] == "NARR01":
                jobs.append(("v4t", f"alt/{s['name']}_v4turbo.mp3", request_for(s, alt_model=True), SEEDS[0]))
        for kind, rel, req, seed in jobs:
            f = OUT / rel
            key = rel
            if f.exists() and key in man:
                continue
            el.tts(req["text"], voice_id(s["voice"]), f, model_id=req["model_id"], seed=seed,
                   voice_settings=req["voice_settings"], pronunciation_dictionaries=req["pronunciation_dictionaries"])
            m = am.measure(f)
            man[key] = dict(line_id=s["line_id"], shot=s["shot"], voice=s["voice"], kind=kind,
                            voice_id=voice_id(s["voice"]), model_id=req["model_id"], seed=seed,
                            voice_settings=req["voice_settings"], tts_text=req["text"], text=s["text"],
                            dictionary=LEX["name"], **{k: m.get(k) for k in ("dur", "speech_start", "speech_end", "speech_dur", "f0_med")})
            MANIFEST.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
            print(s["line_id"], kind, s["voice"], m["speech_dur"], "|", req["text"][:70], flush=True)


def words(t):
    return len(re.findall(r"[A-Za-z0-9']+", t))


def table():
    man = load_manifest()
    rows = []
    for s in segments():
        spec = PLAN["lines"].get(s["line_id"], {})
        e = man.get(s["name"] + ".mp3")
        alts = {v["kind"]: v for k, v in man.items() if k.startswith("alt/" + s["name"] + "_")}
        sec = e["speech_dur"] if e else None
        rows.append({
            "line_id": s["line_id"], "shot_id": s["shot"], "shot_tc": s["tc"], "shot_dur_s": s["shot_dur"],
            "character": NAMES[s["voice"]], "voice": s["voice"], "delivery": s["meta"],
            "text": s["text"], "seconds": sec if sec is not None else "",
            "file_seconds": e["dur"] if e else "",
            "fits_shot": ("" if sec is None else ("yes" if sec <= s["shot_dur"] else f"over {sec - s['shot_dur']:+.1f}")),
            "wpm": round(words(s["text"]) / sec * 60) if sec else "",
            "alt_t2_s": alts.get("t2", {}).get("speech_dur", ""), "alt_v4turbo_s": alts.get("v4t", {}).get("speech_dur", ""),
            "model": e["model_id"] if e else "", "file": f"S01E01/animatic/vo/{s['name']}.mp3" if e else "",
            "note": spec.get("skip", "") or ("FIXED" if s["fixed"] else "") + (" ECHO" if s["echo"] else ""),
        })
    cpath = REPO / "studio/sound/S01E01_vo_durations.csv"
    with cpath.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    return rows


def upload():
    from pipeline import storage
    man = load_manifest()
    n = 0
    for rel in sorted(man):
        f = OUT / rel
        key = "S01E01/animatic/vo/" + rel
        storage.upload(str(f), key)
        n += 1
    storage.upload(str(MANIFEST), "S01E01/animatic/vo/manifest.json")
    print("uploaded", n + 1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["gen", "table", "upload"])
    ap.add_argument("--only")
    ap.add_argument("--alt", action="store_true")
    a = ap.parse_args()
    if a.cmd == "gen":
        gen(set(a.only.split(",")) if a.only else None, a.alt)
    elif a.cmd == "table":
        for r in table():
            print(r["line_id"], r["shot_id"], r["shot_dur_s"], r["seconds"], r["fits_shot"], r["wpm"])
    else:
        upload()
