#!/usr/bin/env python3
"""S01E01 animatic v3: the one new VO take approved by the studio director (continuity_check §9.4).

  STUDIO_ALLOW_PAID=1 BUDGET_LIMIT_USD=55 python3 vo_v3.py l014 [take]   # take 1..3 (seed 101, 202, 303)

L014 Pell, sc03-sh110: "Hold the rope." -> "Hold the rope, Wick."  Same voice (V01_PELL), model (eleven_v3),
settings (stability 0.5, similarity 0.8), tag ([whispers], vo_plan.json) and dictionary as the v2 take; only the
text changes. Max 3 takes. Output: output/S01E01/animatic/vo/sc03-sh110_L014_V01_PELL_v3[_tN].mp3
"""
import json
import sys
from pathlib import Path

ROOT = Path("/home/user/my_work")
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "studio/sound/tools"))
from pipeline import elevenlabs_client as el  # noqa: E402
import audio_measure as am  # noqa: E402

VO = ROOT / "output/S01E01/animatic/vo"
MAN = json.loads((ROOT / "studio/sound/S01E01_vo_manifest.json").read_text(encoding="utf-8"))
LEX = json.loads((ROOT / "studio/sound/lexicon/hollowstone_en_draft_v1.json").read_text(encoding="utf-8"))
SEEDS = {1: 101, 2: 202, 3: 303}


def l014(take=1):
    assert take in SEEDS, "max 3 takes"
    old = MAN["sc03-sh110_L014_V01_PELL.mp3"]
    text = old["tts_text"].replace("Hold the rope.", "Hold the rope, Wick.")
    assert text == "[whispers] Hold the rope, Wick.", text
    out = VO / ("sc03-sh110_L014_V01_PELL_v3.mp3" if take == 1 else f"alt/sc03-sh110_L014_V01_PELL_v3_t{take}.mp3")
    el.tts(text, old["voice_id"], out, model_id=old["model_id"], seed=SEEDS[take],
           voice_settings=old["voice_settings"],
           pronunciation_dictionaries=[(LEX["elevenlabs"]["id"], LEX["elevenlabs"]["version_id"])])
    m = am.measure(out)
    rec = dict(old, tts_text=text, text="Hold the rope, Wick.", seed=SEEDS[take], kind="v3" if take == 1 else f"v3_t{take}",
               **{k: m.get(k) for k in ("dur", "speech_start", "speech_end", "speech_dur", "f0_med")})
    rec.pop("stt", None)
    rec["qa"] = "director listen-proxy: duration/F0 vs v2 take"
    (VO / (out.stem + ".json")).write_text(json.dumps(rec, indent=1), encoding="utf-8")
    print(out, json.dumps({k: rec[k] for k in ("dur", "speech_start", "speech_end", "speech_dur", "f0_med")}),
          "v2 take:", {k: old[k] for k in ("speech_dur", "f0_med")})


if __name__ == "__main__":
    {"l014": l014}[sys.argv[1]](*(int(x) for x in sys.argv[2:]))
