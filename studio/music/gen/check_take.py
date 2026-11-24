"""Free objective checks for a music take (ffmpeg only, no paid calls).

    python3 studio/music/gen/check_take.py TAKE.mp3 --target 90.0 [--bar 3.0]

Prints: duration vs target and nearest bar-line trim point; integrated loudness / true peak;
low-register energy (< 90 Hz band level vs full band: the 'no drone / no sub' rule);
and writes TAKE_phone.wav (HPF 300 Hz + LPF 8 kHz, mono) for the phone-band listening test.
Listening criteria (hook leap, forbidden tone, choir, similarity) stay with the composer's ear.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


def ff(args: list[str]) -> str:
    return subprocess.run(["ffmpeg", "-hide_banner", "-nostats", *args], capture_output=True,
                          text=True).stderr


def duration(p: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                          "default=nw=1:nk=1", str(p)], capture_output=True, text=True).stdout
    return float(out.strip())


def band_rms(p: Path, filt: str) -> float:
    err = ff(["-i", str(p), "-af", f"{filt}astats=metadata=0:measure_overall=RMS_level", "-f", "null", "-"])
    vals = re.findall(r"RMS level dB:\s*(-?[\d.]+|-inf)", err)
    return float(vals[-1]) if vals and vals[-1] != "-inf" else -120.0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("take")
    ap.add_argument("--target", type=float, required=True)
    ap.add_argument("--bar", type=float, default=3.0)
    a = ap.parse_args()
    p = Path(a.take)
    d = duration(p)
    bars = round(d / a.bar)
    lo = ff(["-i", str(p), "-af", "ebur128=peak=true", "-f", "null", "-"])
    i_lufs = re.findall(r"I:\s*(-?[\d.]+) LUFS", lo)
    tp = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", lo)
    full = band_rms(p, "")
    sub = band_rms(p, "lowpass=f=90,lowpass=f=90,")
    phone = p.with_name(p.stem + "_phone.wav")
    ff(["-y", "-i", str(p), "-af", "highpass=f=300,highpass=f=300,lowpass=f=8000,lowpass=f=8000",
        "-ac", "1", str(phone)])
    res = {"file": str(p), "duration_s": round(d, 3), "target_s": a.target,
           "delta_s": round(d - a.target, 3), "nearest_bar_line_s": round(bars * a.bar, 3),
           "trimmable_to_target": d >= a.target - 0.05,
           "integrated_lufs": float(i_lufs[-1]) if i_lufs else None,
           "true_peak_dbfs": float(tp[-1]) if tp else None,
           "rms_full_db": full, "rms_below_90hz_db": sub, "sub_vs_full_db": round(sub - full, 1),
           "phone_band_file": str(phone)}
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
