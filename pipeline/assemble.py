"""Сборка серии через ffmpeg.

Вход — JSON-описание (или dict):
{
  "output": "output/ep01/ep01.mp4",
  "width": 1920, "height": 1080, "fps": 24,          # по умолчанию 1080p24
  "clips": [                                          # склеиваются по порядку
    {"path": "output/ep01/shot01.mp4"},
    {"path": "output/ep01/shot02.mp4", "trim_start": 0.5, "duration": 3.0}
  ],
  "tracks": [                                         # аудиодорожки поверх видео
    {"type": "dialog", "path": "line01.mp3", "start": 1.2},
    {"type": "sfx",    "path": "door.mp3",   "start": 4.0, "volume_db": -4},
    {"type": "music",  "path": "theme.mp3",  "start": 0, "loop": true,
     "fade_in": 1.0, "fade_out": 2.0}
  ],
  "duck_music": true,        # приглушать музыку под диалогами (sidechain)
  "keep_clip_audio": false,  # оставить звук исходных клипов (если есть)
  "loudnorm": true           # нормализация громкости EBU R128 (-16 LUFS, веб)
}
Пути в JSON — относительно файла JSON (или абсолютные).
Уровни по умолчанию (dB): dialog 0, sfx -6, music -18, clip -12.

CLI:
    python3 -m pipeline.assemble spec.json [--dry-run]
    python3 -m pipeline.assemble --selftest      # синтетика через lavfi testsrc/sine
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

DEFAULT_VOLUME_DB = {"dialog": 0.0, "sfx": -6.0, "music": -18.0, "clip": -12.0}
BUS_ORDER = ("dialog", "sfx", "music", "clip")
AUDIO_RATE = 48000


class AssembleError(RuntimeError):
    pass


def _need(tool: str) -> str:
    path = shutil.which(tool)
    if not path:
        raise AssembleError(f"{tool} не найден в PATH — установите ffmpeg")
    return path


def probe(path: str | Path) -> dict:
    """Длительность и наличие аудио/видео через ffprobe."""
    out = subprocess.run(
        [_need("ffprobe"), "-v", "error", "-show_entries",
         "format=duration:stream=codec_type,width,height,r_frame_rate", "-of", "json", str(path)],
        capture_output=True, text=True)
    if out.returncode != 0:
        raise AssembleError(f"ffprobe не смог прочитать {path}: {out.stderr.strip()}")
    data = json.loads(out.stdout)
    streams = data.get("streams", [])
    v = next((s for s in streams if s.get("codec_type") == "video"), None)
    return {
        "duration": float(data.get("format", {}).get("duration", 0) or 0),
        "has_audio": any(s.get("codec_type") == "audio" for s in streams),
        "has_video": v is not None,
        "width": v.get("width") if v else None,
        "height": v.get("height") if v else None,
    }


def _resolve(p: str, base: Path) -> Path:
    path = Path(p)
    return path if path.is_absolute() else (base / path)


def build_command(spec: dict, base_dir: Path | None = None) -> tuple[list[str], float]:
    """Собрать команду ffmpeg. Возвращает (argv, длительность серии в сек)."""
    base = base_dir or Path.cwd()
    W, H = int(spec.get("width", 1920)), int(spec.get("height", 1080))
    fps = spec.get("fps", 24)
    clips = spec.get("clips") or []
    if not clips:
        raise AssembleError("spec.clips пуст")
    tracks = spec.get("tracks") or []
    keep_clip_audio = bool(spec.get("keep_clip_audio", False))

    inputs: list[str] = []
    filters: list[str] = []
    vlabels: list[str] = []
    clip_audio_labels: list[str] = []
    clip_offsets: list[float] = []
    total = 0.0

    for i, c in enumerate(clips):
        path = _resolve(c["path"], base)
        if not path.is_file():
            raise AssembleError(f"клип не найден: {path}")
        info = probe(path)
        start = float(c.get("trim_start", 0) or 0)
        dur = c.get("duration")
        dur = float(dur) if dur else max(info["duration"] - start, 0)
        if dur <= 0:
            raise AssembleError(f"клип {path}: нулевая длительность")
        inputs += ["-i", str(path)]
        filters.append(
            f"[{i}:v]trim=start={start}:duration={dur},setpts=PTS-STARTPTS,"
            f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
            f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1,fps={fps},format=yuv420p[v{i}]")
        vlabels.append(f"[v{i}]")
        if keep_clip_audio and info["has_audio"]:
            vol = c.get("volume_db", DEFAULT_VOLUME_DB["clip"])
            ms = int(round(total * 1000))
            filters.append(
                f"[{i}:a]atrim=start={start}:duration={dur},asetpts=PTS-STARTPTS,"
                f"aresample={AUDIO_RATE},aformat=channel_layouts=stereo,volume={vol}dB,"
                f"adelay={ms}|{ms}[ca{i}]")
            clip_audio_labels.append(f"[ca{i}]")
        clip_offsets.append(total)
        total += dur

    filters.append(f"{''.join(vlabels)}concat=n={len(vlabels)}:v=1:a=0[vout]")

    buses: dict[str, list[str]] = {b: [] for b in BUS_ORDER}
    buses["clip"] = clip_audio_labels
    idx = len(clips)
    for k, t in enumerate(tracks):
        ttype = t.get("type", "sfx")
        if ttype not in DEFAULT_VOLUME_DB or ttype == "clip":
            raise AssembleError(f"track[{k}]: type должен быть dialog|sfx|music, получено {ttype!r}")
        path = _resolve(t["path"], base)
        if not path.is_file():
            raise AssembleError(f"аудио не найдено: {path}")
        start = float(t.get("start", 0) or 0)
        if start >= total:
            continue  # дорожка за пределами серии
        max_len = total - start
        if t.get("loop"):
            inputs += ["-stream_loop", "-1"]
        inputs += ["-i", str(path)]
        length = float(t["duration"]) if t.get("duration") else max_len
        length = min(length, max_len)
        if not t.get("loop"):
            length = min(length, probe(path)["duration"] or length)
        chain = [f"atrim=duration={length:.3f}", "asetpts=PTS-STARTPTS",
                 f"aresample={AUDIO_RATE}", "aformat=channel_layouts=stereo"]
        if t.get("fade_in"):
            chain.append(f"afade=t=in:st=0:d={float(t['fade_in'])}")
        if t.get("fade_out"):
            fo = float(t["fade_out"])
            chain.append(f"afade=t=out:st={max(length - fo, 0):.3f}:d={fo}")
        chain.append(f"volume={t.get('volume_db', DEFAULT_VOLUME_DB[ttype])}dB")
        ms = int(round(start * 1000))
        if ms:
            chain.append(f"adelay={ms}|{ms}")
        filters.append(f"[{idx}:a]{','.join(chain)}[t{k}]")
        buses[ttype].append(f"[t{k}]")
        idx += 1

    bus_out: dict[str, str] = {}
    for b in BUS_ORDER:
        labels = buses[b]
        if not labels:
            continue
        if len(labels) == 1:
            bus_out[b] = labels[0]
        else:
            filters.append(f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:duration=longest[bus_{b}]")
            bus_out[b] = f"[bus_{b}]"

    if spec.get("duck_music", True) and "music" in bus_out and "dialog" in bus_out:
        filters.append(f"{bus_out['dialog']}asplit=2[dlg_main][dlg_sc]")
        filters.append(f"{bus_out['music']}[dlg_sc]sidechaincompress="
                       f"threshold=0.03:ratio=8:attack=20:release=500:makeup=1[music_ducked]")
        bus_out["dialog"], bus_out["music"] = "[dlg_main]", "[music_ducked]"

    post = [f"apad=whole_dur={total:.3f}", f"atrim=duration={total:.3f}"]
    if spec.get("loudnorm", True):
        post.append("loudnorm=I=-16:TP=-1.5:LRA=11")
        post.append(f"aresample={AUDIO_RATE}")  # loudnorm апсемплирует до 192k
    if bus_out:
        labels = [bus_out[b] for b in BUS_ORDER if b in bus_out]
        if len(labels) == 1:
            filters.append(f"{labels[0]}{','.join(post)}[aout]")
        else:
            filters.append(f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:duration=longest,"
                           f"{','.join(post)}[aout]")
    else:
        filters.append(f"anullsrc=r={AUDIO_RATE}:cl=stereo,atrim=duration={total:.3f}[aout]")

    out = _resolve(spec.get("output", "output/episode.mp4"), base)
    cmd = [_need("ffmpeg"), "-y", "-hide_banner", "-loglevel", "error", *inputs,
           "-filter_complex", ";".join(filters), "-map", "[vout]", "-map", "[aout]",
           "-c:v", "libx264", "-preset", spec.get("preset", "medium"), "-crf", str(spec.get("crf", 18)),
           "-pix_fmt", "yuv420p", "-r", str(fps),
           "-c:a", "aac", "-b:a", "192k", "-ar", str(AUDIO_RATE),
           "-movflags", "+faststart", "-t", f"{total:.3f}", str(out)]
    return cmd, total


def assemble(spec: dict | str | Path, dry_run: bool = False) -> Path:
    """Собрать серию по spec (dict или путь к JSON). Возвращает путь к mp4."""
    base = Path.cwd()
    if not isinstance(spec, dict):
        spec_path = Path(spec)
        base = spec_path.resolve().parent
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
    cmd, total = build_command(spec, base)
    out = Path(cmd[-1])
    if dry_run:
        print(" ".join(cmd))
        return out
    out.parent.mkdir(parents=True, exist_ok=True)
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise AssembleError(f"ffmpeg завершился с ошибкой:\n{res.stderr[-3000:]}")
    return out


# ================================================================ selftest ===

def _lavfi(args: list[str]) -> None:
    res = subprocess.run([_need("ffmpeg"), "-y", "-hide_banner", "-loglevel", "error", *args],
                         capture_output=True, text=True)
    if res.returncode != 0:
        raise AssembleError(res.stderr)


def _mean_volume(path: Path, start: float, dur: float) -> float:
    res = subprocess.run([_need("ffmpeg"), "-hide_banner", "-ss", str(start), "-t", str(dur), "-i",
                          str(path), "-af", "volumedetect", "-vn", "-f", "null", "-"],
                         capture_output=True, text=True)
    for line in res.stderr.splitlines():
        if "mean_volume" in line:
            return float(line.split("mean_volume:")[1].split("dB")[0])
    return float("-inf")


def selftest(workdir: str | Path | None = None) -> dict:
    """Синтетические клипы (разные размеры/fps, один со звуком) + диалог/SFX/музыка -> mp4."""
    from . import config
    wd = Path(workdir) if workdir else config.output_dir() / "selftest"
    wd.mkdir(parents=True, exist_ok=True)
    _lavfi(["-f", "lavfi", "-i", "testsrc=size=1280x720:rate=30:duration=2", "-pix_fmt", "yuv420p",
            str(wd / "clip1.mp4")])
    _lavfi(["-f", "lavfi", "-i", "testsrc2=size=640x480:rate=25:duration=3",
            "-f", "lavfi", "-i", "sine=frequency=330:duration=3", "-shortest", "-pix_fmt", "yuv420p",
            str(wd / "clip2.mp4")])
    _lavfi(["-f", "lavfi", "-i", "smptebars=size=1920x1080:rate=24:duration=2", "-pix_fmt", "yuv420p",
            str(wd / "clip3.mp4")])
    _lavfi(["-f", "lavfi", "-i", "sine=frequency=440:duration=1.5", "-ac", "1", str(wd / "line1.wav")])
    _lavfi(["-f", "lavfi", "-i", "sine=frequency=520:duration=1.0", "-c:a", "libmp3lame",
            str(wd / "line2.mp3")])
    _lavfi(["-f", "lavfi", "-i", "sine=frequency=1200:duration=0.3", str(wd / "sfx.wav")])
    _lavfi(["-f", "lavfi", "-i", "sine=frequency=220:duration=2", "-c:a", "libmp3lame",
            str(wd / "music.mp3")])
    spec = {
        "output": "episode_selftest.mp4",
        "clips": [{"path": "clip1.mp4"}, {"path": "clip2.mp4", "trim_start": 0.5},
                  {"path": "clip3.mp4", "duration": 1.5}],
        "tracks": [
            {"type": "music", "path": "music.mp3", "start": 0, "loop": True, "fade_in": 0.5, "fade_out": 1},
            {"type": "dialog", "path": "line1.wav", "start": 0.5},
            {"type": "dialog", "path": "line2.mp3", "start": 3.0},
            {"type": "sfx", "path": "sfx.wav", "start": 4.5},
        ],
        "duck_music": True,
        "keep_clip_audio": True,
        "loudnorm": True,
    }
    (wd / "spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    out = assemble(wd / "spec.json")
    info = probe(out)
    expected = 2 + 2.5 + 1.5
    checks = {
        "output": str(out),
        "resolution_1080p": (info["width"], info["height"]) == (1920, 1080),
        "has_audio": info["has_audio"],
        "duration": round(info["duration"], 2),
        "duration_ok": abs(info["duration"] - expected) < 0.15,
        # диалог (0.5–2.0 c) должен быть громче, чем музыка без диалога (2.1–2.9 c)
        "vol_dialog_db": _mean_volume(out, 0.7, 1.0),
        "vol_music_only_db": _mean_volume(out, 2.1, 0.8),
    }
    checks["dialog_louder_than_music"] = checks["vol_dialog_db"] > checks["vol_music_only_db"]
    checks["passed"] = all(checks[k] for k in ("resolution_1080p", "has_audio", "duration_ok",
                                                  "dialog_louder_than_music"))
    return checks


def _cli() -> None:
    ap = argparse.ArgumentParser(description="Сборка серии через ffmpeg")
    ap.add_argument("spec", nargs="?", help="JSON-описание серии")
    ap.add_argument("--dry-run", action="store_true", help="только напечатать команду ffmpeg")
    ap.add_argument("--selftest", action="store_true", help="проверка на синтетических данных")
    args = ap.parse_args()
    if args.selftest:
        res = selftest()
        print(json.dumps(res, ensure_ascii=False, indent=2))
        sys.exit(0 if res["passed"] else 1)
    if not args.spec:
        ap.error("укажите spec.json или --selftest")
    print(assemble(args.spec, dry_run=args.dry_run))


if __name__ == "__main__":
    _cli()
