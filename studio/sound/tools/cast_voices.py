"""Voice Design runner for the S01E01 cast (PAID: needs STUDIO_ALLOW_PAID=1).

    python3 -m studio.sound.tools.cast_voices design V01 [--iter N] [--desc-file f] [--guidance g]
    python3 -m studio.sound.tools.cast_voices measure V01
    python3 -m studio.sound.tools.cast_voices create V01 <iter> <preview_no>

Prompts and test texts are read from studio/sound/pilot_voices.md (section «Voice Design (EN)» and
«Тестовая фраза»), or from studio/sound/casting/prompts.json overrides (iterations 2–3, new cards).
Previews: output/S01E01/animatic/casting/<VID>/i<iter>_p<n>.mp3. Log: studio/sound/casting/casting_log.json.
Run from the repo root (cwd) so that `pipeline` imports.
"""
import argparse, json, re, sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(Path(__file__).parent))
from pipeline import elevenlabs_client as el  # noqa: E402
import audio_measure as am  # noqa: E402

CARDS = REPO / "studio/sound/pilot_voices.md"
OVR = REPO / "studio/sound/casting/prompts.json"
LOG = REPO / "studio/sound/casting/casting_log.json"
OUT = REPO / "output/S01E01/animatic/casting"

# id -> (voice name in ElevenLabs, F0 target Hz)
VOICES = {
    "V01": ("HS S1 V01", 195), "V02": ("HS S1 V02", 290), "V03": ("HS S1 V03", 230),
    "V04": ("HS S1 V04", 255), "V05": ("HS S1 V05", 130), "V06": ("HS S1 V06", 105),
    "V07": ("HS S1 V07", 95), "V08": ("HS S1 V08", 175), "V09": ("HS S1 V09", 115),
    "V10": ("HS S1 V10", 85), "V11": ("HS S1 V11", 240), "V12": ("HS S1 V12", 145),
    "V13": ("HS S1 V13", 200), "V14": ("HS S1 V14", 150), "V15": ("HS S1 V15", 110),
    "V16": ("HS S1 V16", 140), "V17": ("HS S1 V17", 125), "NARR01": ("HS NARR A cand", 115),
}


def card(vid):
    ovr = json.loads(OVR.read_text(encoding="utf-8")) if OVR.exists() else {}
    if vid in ovr and "description" in ovr[vid] and "text" in ovr[vid]:
        return ovr[vid]["description"], ovr[vid]["text"]
    md = CARDS.read_text(encoding="utf-8")
    head = "### NARR-01" if vid == "NARR01" else f"### V-{vid[1:]} "
    sec = md[md.index(head):]
    sec = sec[:sec.find("\n### ", 5)] if "\n### " in sec[5:] else sec
    blocks = re.findall(r"```text\n(.*?)\n```", sec, re.S)
    desc, text = blocks[0].strip(), blocks[1].strip()
    if vid in ovr:
        desc = ovr[vid].get("description", desc)
        text = ovr[vid].get("text", text)
    return desc, text


def load_log():
    return json.loads(LOG.read_text(encoding="utf-8")) if LOG.exists() else {}


def save_log(d):
    LOG.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")


def design(vid, it, guidance, model, seed):
    desc, text = card(vid)
    seed = seed if seed is not None else 3100 + list(VOICES).index(vid) * 10 + it
    before = el.subscription()["character_count"]
    prev = el.design_voice(desc, text, OUT / vid, prefix=f"i{it}", model_id=model,
                           guidance_scale=guidance, seed=seed, loudness=0.0, should_enhance=False)
    after = el.subscription()["character_count"]
    target = VOICES[vid][1]
    for p in prev:
        m = am.measure(p["file"])
        p.update(m)
        if "f0_med" in m:
            p["f0_off_st"] = round(float(am.semitones(m["f0_med"], target)), 1)
    log = load_log()
    log.setdefault(vid, {"name": VOICES[vid][0], "f0_target": target, "iterations": []})
    log[vid]["iterations"].append({"iter": it, "model": model, "seed": seed, "guidance": guidance,
                                   "description": desc, "text": text, "credits": after - before,
                                   "previews": prev})
    save_log(log)
    print(json.dumps({"vid": vid, "iter": it, "credits": after - before, "count_after": after,
                      "previews": [{k: p.get(k) for k in ("file", "dur", "f0_med", "f0_p10", "f0_p90", "f0_off_st")}
                                   for p in prev]}, indent=1))


def create(vid, it, pno):
    log = load_log()
    entry = next(x for x in log[vid]["iterations"] if x["iter"] == it)
    p = entry["previews"][pno - 1]
    labels = {"project": "hollowstone", "role": vid, "stage": "candidate" if vid == "NARR01" else "draft-cast"}
    voice_id = el.create_voice(VOICES[vid][0], entry["description"], p["generated_voice_id"], labels)
    log[vid]["selected"] = {"iter": it, "preview": pno, "voice_id": voice_id, "seed": entry["seed"],
                            "model": entry["model"], "guidance": entry["guidance"],
                            "generated_voice_id": p["generated_voice_id"], "file": p["file"]}
    save_log(log)
    print(vid, voice_id)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["design", "create", "show"])
    ap.add_argument("vid")
    ap.add_argument("args", nargs="*", type=int)
    ap.add_argument("--iter", type=int, default=1)
    ap.add_argument("--guidance", type=float, default=5.0)
    ap.add_argument("--model", default="eleven_ttv_v3")
    ap.add_argument("--seed", type=int)
    a = ap.parse_args()
    if a.cmd == "design":
        design(a.vid, a.iter, a.guidance, a.model, a.seed)
    elif a.cmd == "create":
        create(a.vid, *a.args)
    else:
        d, t = card(a.vid)
        print(len(d), d, "\n", len(t), t)
