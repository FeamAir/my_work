"""Сборка серии через ffmpeg по спецификации звукорежиссёра (studio/sound/mix_plan.md).

Этапы (каждый — отдельный вызов ffmpeg, промежуточные файлы в <output>_work/):
  0. video      — склейка клипов, приведение к W×H / fps → video.mp4 (без звука);
  1. normalize  — каждый аудиоклип → WAV 48 кГц/24 бит, уровень по категории (LUFS, измеряется
                  ebur128), DX: HPF 80 Гц + компрессор 2.5:1, потолок −3 dBFS (alimiter 0.708),
                  микрофейды 5/10 мс; клипы < 0.4 с — по пику (−6 dBFS);
  2. stems      — DX, FX, FOLEY, AMB, MUS, STING (+ CLIP — звук исходных видеоклипов):
                  adelay на таймкод, панорама, петли (aloop+atrim), фейды, amix normalize=0,
                  длина каждого стема = длина видео D;
  3. premix     — ducking: MUS ≈ 9 dB и AMB ≈ 3 dB под DX (sidechaincompress), amix normalize=0;
                  дополнительно пишутся mus_ducked.wav / amb_ducked.wav для калибровки;
  4. master     — loudnorm в два прохода: I = −14 LUFS, TP = −1 dBTP,
                  LRA = min(20, max(11, измеренный LRA + 1)), linear=true, aresample=48000;
  5. mux        — видео (copy) + AAC 320 кбит/с 48 кГц стерео, +faststart;
  6. control    — ebur128 (I, LRA, true peak) по готовому mp4 → <output>_work/mix_report.json.

Вход — JSON (или dict):
{
  "output": "output/ep01/ep01.mp4",
  "width": 1920, "height": 1080, "fps": 24,
  "clips": [{"path": "sc01-sh010.mp4", "duration": 4.0, "trim_start": 0}],
  "tracks": [
    {"id": "ep01_dx_001", "stem": "dx", "path": "dx_001.wav", "start": 2.0},
    {"id": "ep01_hard_001", "stem": "fx", "path": "door.wav", "start": 15.8,
     "target_lufs": -18, "pan": "R30", "gain_db": -3},
    {"id": "ep01_amb_001", "stem": "amb", "path": "amb.wav", "start": 0, "end": 35.5,
     "loop": true, "fade_in": 1.0, "fade_out": 0.5},
    {"id": "ep01_mus_001", "stem": "mus", "path": "theme.wav", "start": 52, "duration": 40,
     "fade_in": 1.5, "fade_out": 3}
  ],
  "keep_clip_audio": false,     # звук исходных клипов отдельным стемом CLIP (−12 dB, без нормализации)
  "ducking": true,              # или false, или {"mus": {...параметры...}, "amb": false}
  "master": {"I": -14, "TP": -1, "LRA_min": 11, "LRA_max": 20},   # или "loudnorm": false
  "pan_scale": 2.0              # см. pan_gains()
}
Поля дорожки: stem (dx|fx|foley|amb|mus|sting; синонимы dialog/vox→dx, sfx/hard/des→fx,
music→mus), path, start, end | duration (длина на таймлайне), trim_start, loop, fade_in, fade_out,
target_lufs (по умолчанию по стему), normalize (true), gain_db (подстройка по месту; старое
volume_db — синоним), pan (C | L30 | R30 | stereo | число −1…1), filter (доп. цепочка ffmpeg
по месту, напр. "lowpass=f=900"). Прочие поля (meta, generation, warnings…) игнорируются.
Пути — относительно JSON (или абсолютные).

CLI:
    python3 -m pipeline.assemble spec.json [--dry-run]
    python3 -m pipeline.assemble --selftest      # синтетика через lavfi
"""
from __future__ import annotations

import argparse
import json
import math
import re
import shlex
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

AUDIO_RATE = 48000
STEMS = ("dx", "fx", "foley", "amb", "mus", "sting", "clip")
STEM_ALIASES = {
    "dx": "dx", "dialog": "dx", "dialogue": "dx", "vox": "dx",
    "fx": "fx", "sfx": "fx", "hard": "fx", "des": "fx",
    "foley": "foley", "amb": "amb", "ambience": "amb",
    "mus": "mus", "music": "mus", "sting": "sting",
}
# mix_plan.md §1, §8 / sound_bible.md §5.2 — целевой уровень клипа в премиксе
DEFAULT_TARGET_LUFS = {"dx": -16.0, "fx": -18.0, "foley": -26.0, "amb": -32.0, "mus": -18.0, "sting": -18.0}
DX_PROCESS = "highpass=f=80,acompressor=threshold=-20dB:ratio=2.5:attack=5:release=120:makeup=2dB"
CLIP_LIMITER = "alimiter=limit=0.708:level=false:attack=5:release=50:latency=1"   # −3 dBFS
SHORT_CLIP_S = 0.4          # короче — нормализация по пику
SHORT_CLIP_PEAK_DB = -6.0
SILENCE_LUFS = -70.0
CLIP_AUDIO_DB = -12.0       # звук исходных видеоклипов
# mix_plan.md §4
DUCKING = {
    "mus": {"threshold": 0.063, "ratio": 4, "attack": 40, "release": 600, "knee": 4,
            "detection": "rms", "makeup": 1},
    "amb": {"threshold": 0.1, "ratio": 1.5, "attack": 80, "release": 900, "knee": 6,
            "detection": "rms", "makeup": 1},
}
# mix_plan.md §5 — решение директора: −14 LUFS, ≤ −1 dBTP, 2 прохода
MASTER = {"I": -14.0, "TP": -1.0, "LRA_min": 11.0, "LRA_max": 20.0}
ACCEPT_I_TOL = 1.0
AAC_BITRATE = "320k"


class AssembleError(RuntimeError):
    pass


# ================================================================= helpers ===

def _need(tool: str) -> str:
    path = shutil.which(tool)
    if not path:
        raise AssembleError(f"{tool} не найден в PATH — установите ffmpeg")
    return path


def _ff(*args: str) -> list[str]:
    return [_need("ffmpeg"), "-y", "-hide_banner", "-loglevel", "error", *args]


def _run(argv: list[str], what: str) -> subprocess.CompletedProcess:
    res = subprocess.run(argv, capture_output=True, text=True)
    if res.returncode != 0:
        raise AssembleError(f"ffmpeg ({what}) завершился с ошибкой:\n{res.stderr[-3000:]}")
    return res


def probe(path: str | Path) -> dict:
    """Длительность, наличие аудио/видео, размер кадра, число аудиоканалов."""
    out = subprocess.run(
        [_need("ffprobe"), "-v", "error", "-show_entries",
         "format=duration:stream=codec_type,width,height,channels", "-of", "json", str(path)],
        capture_output=True, text=True)
    if out.returncode != 0:
        raise AssembleError(f"ffprobe не смог прочитать {path}: {out.stderr.strip()}")
    data = json.loads(out.stdout)
    streams = data.get("streams", [])
    v = next((s for s in streams if s.get("codec_type") == "video"), None)
    a = next((s for s in streams if s.get("codec_type") == "audio"), None)
    return {
        "duration": float(data.get("format", {}).get("duration", 0) or 0),
        "has_audio": a is not None,
        "has_video": v is not None,
        "width": v.get("width") if v else None,
        "height": v.get("height") if v else None,
        "channels": int(a.get("channels") or 0) if a else 0,
    }


def _resolve(p: str, base: Path) -> Path:
    path = Path(p)
    return path if path.is_absolute() else (base / path)


def _f(x: float) -> str:
    """Число для фильтров ffmpeg без лишних нулей."""
    return f"{x:.3f}".rstrip("0").rstrip(".") if x != int(x) else str(int(x))


def lra_target(measured_lra: float, lra_min: float = MASTER["LRA_min"],
               lra_max: float = MASTER["LRA_max"]) -> float:
    """LRA = max(11, измеренный + 1), но не больше 20 — чтобы loudnorm остался в linear-режиме."""
    return round(min(lra_max, max(lra_min, measured_lra + 1.0)), 1)


_PAN_RE = re.compile(r"^\s*([LR])\s*(\d+(?:\.\d+)?)\s*$", re.I)


def pan_position(pan) -> float | None:
    """Позиция −1 (лево) … +1 (право); None — стерео/центр без обработки.

    'C' → 0, 'L30' → −0.3, 'R30' → +0.3 (как в mix_plan.md: 0.65/0.35 ≈ L30), число — как есть.
    """
    if pan is None:
        return None
    if isinstance(pan, (int, float)):
        return max(-1.0, min(1.0, float(pan)))
    s = str(pan).strip()
    if not s or s.lower() in ("stereo", "st", "—", "-", "lr"):
        return None
    if s.upper() in ("C", "CENTER", "Ц"):
        return 0.0
    m = _PAN_RE.match(s)
    if not m:
        raise AssembleError(f"панорама {pan!r} не распознана (C, L30, R30, stereo или число −1…1)")
    v = min(float(m.group(2)), 100.0) / 100.0
    return -v if m.group(1).upper() == "L" else v


def pan_gains(position: float, scale: float = 2.0) -> tuple[float, float]:
    """Коэффициенты (левый, правый) для моно-клипа.

    Закон из mix_plan.md: центр 0.5/0.5, R30 0.35/0.65 (линейный, сумма = 1). Умножается на
    scale: при scale=2 центр = 1.0/1.0, как у DX (`pan=stereo|c0=c0|c1=c0`), — тогда целевые
    LUFS клипов FX/FOLEY и DX сопоставимы. scale=1 — буквально как в mix_plan.md (−6 dB к центру).
    """
    right = 0.5 + position / 2.0
    left = 1.0 - right
    return round(left * scale, 4), round(right * scale, 4)


def parse_loudnorm_json(stderr: str) -> dict:
    """Последний JSON-блок loudnorm из stderr ffmpeg."""
    start = stderr.rfind("{")
    end = stderr.rfind("}")
    if start < 0 or end < start:
        raise AssembleError("loudnorm не вернул JSON:\n" + stderr[-1500:])
    return json.loads(stderr[start:end + 1])


def parse_ebur128(stderr: str) -> dict:
    """I, LRA, peak (true или sample — что запрошено) из сводки ebur128."""
    summary = stderr[stderr.rfind("Summary:"):] if "Summary:" in stderr else stderr

    def grab(pattern: str) -> float:
        m = re.search(pattern, summary)
        if not m:
            return float("nan")
        v = m.group(1)
        return float("-inf") if v.startswith("-inf") else float(v)

    return {"I": grab(r"I:\s+(-?inf|-?\d+(?:\.\d+)?) LUFS"),
            "thresh": grab(r"Threshold:\s+(-?inf|-?\d+(?:\.\d+)?) LUFS"),
            "LRA": grab(r"LRA:\s+(-?\d+(?:\.\d+)?) LU"),
            "peak": grab(r"Peak:\s+(-?inf|-?\d+(?:\.\d+)?) dBFS")}


def master_measurement(ln: dict, eb: dict) -> dict:
    """Значения measured_* для второго прохода loudnorm.

    Проход 1 — loudnorm (как в mix_plan.md) + ebur128 в той же цепочке. В выборе I/порога
    приоритет у ebur128: им же меряется приёмка, а input_i loudnorm в первом проходе на коротком
    материале отличается от фактического до ~0.6 LU (замер в selftest: −14.29 против −13.70),
    и тогда мастер промахивается мимо −14 на столько же. TP — худший из двух.
    """
    m = dict(ln)
    m["loudnorm_input_i"] = ln.get("input_i")
    if math.isfinite(eb.get("I", float("nan"))) and eb["I"] > SILENCE_LUFS:
        m["input_i"] = f"{eb['I']:.2f}"
        if math.isfinite(eb.get("thresh", float("nan"))):
            m["input_thresh"] = f"{eb['thresh']:.2f}"
    if math.isfinite(eb.get("peak", float("nan"))):
        m["input_tp"] = f"{max(float(ln['input_tp']), eb['peak']):.2f}"
    m["ebur128"] = eb
    return m


def clip_gain(target_lufs: float, integrated: float, peak: float, duration: float) -> tuple[float, str]:
    """Усиление нормализации клипа (dB) и способ ('lufs' | 'peak' | 'none')."""
    if duration >= SHORT_CLIP_S and math.isfinite(integrated) and integrated > SILENCE_LUFS:
        return round(target_lufs - integrated, 2), "lufs"
    if math.isfinite(peak):
        return round(SHORT_CLIP_PEAK_DB - peak, 2), "peak"
    return 0.0, "none"


# ==================================================================== plan ===

@dataclass
class Item:
    id: str
    stem: str
    src: Path
    start: float
    length: float
    trim_start: float = 0.0
    loop: bool = False
    fade_in: float = 0.0
    fade_out: float = 0.0
    target_lufs: float | None = None
    normalize: bool = True
    gain_db: float = 0.0
    pan: float | None = 0.0
    src_duration: float = 0.0
    src_channels: int = 1
    cut: bool = False              # обрезан относительно исходника — нужен микрофейд
    filter: str = ""               # доп. фильтры ffmpeg для клипа по месту (напр. lowpass=f=900)
    norm_path: Path | None = None
    norm: dict = field(default_factory=dict)

    @property
    def out_channels(self) -> int:
        return 1 if (self.stem == "dx" or self.src_channels <= 1) else 2


@dataclass
class Plan:
    output: Path
    work: Path
    duration: float
    width: int
    height: int
    fps: float
    clips: list[dict]
    items: list[Item]
    keep_clip_audio: bool
    ducking: dict
    master: dict | None
    pan_scale: float
    preset: str = "medium"
    crf: int = 18
    warnings: list[str] = field(default_factory=list)


def _ducking_cfg(spec: dict) -> dict:
    raw = spec.get("ducking", spec.get("duck_music", True))
    if raw is False:
        return {}
    cfg = {k: dict(v) for k, v in DUCKING.items()}
    if isinstance(raw, dict):
        for k, v in raw.items():
            if v is False:
                cfg.pop(k, None)
            elif isinstance(v, dict):
                cfg.setdefault(k, {}).update(v)
    return cfg


def build_plan(spec: dict, base_dir: Path | None = None) -> Plan:
    """Разобрать spec, проверить файлы (ffprobe), посчитать таймлайн. ffmpeg не запускается."""
    base = base_dir or Path.cwd()
    clips = spec.get("clips") or []
    if not clips:
        raise AssembleError("spec.clips пуст")
    out = _resolve(spec.get("output", "output/episode.mp4"), base)
    work = _resolve(spec["workdir"], base) if spec.get("workdir") else out.with_name(out.stem + "_work")

    clip_list: list[dict] = []
    total = 0.0
    for c in clips:
        path = _resolve(c["path"], base)
        if not path.is_file():
            raise AssembleError(f"клип не найден: {path}")
        info = probe(path)
        start = float(c.get("trim_start", 0) or 0)
        dur = c.get("duration")
        dur = float(dur) if dur else max(info["duration"] - start, 0)
        if info["duration"] and dur > info["duration"] - start + 0.05:
            raise AssembleError(f"клип {path}: запрошено {dur} с, в файле {info['duration'] - start:.2f} с")
        if dur <= 0:
            raise AssembleError(f"клип {path}: нулевая длительность")
        clip_list.append({"path": path, "trim_start": start, "duration": dur, "offset": total,
                          "has_audio": info["has_audio"], "volume_db": c.get("volume_db", CLIP_AUDIO_DB)})
        total += dur
    D = round(total, 3)

    master = None
    if spec.get("loudnorm", True) is not False and spec.get("master", True) is not False:
        master = dict(MASTER)
        if isinstance(spec.get("master"), dict):
            master.update({k: float(v) for k, v in spec["master"].items()})

    plan = Plan(output=out, work=work, duration=D, width=int(spec.get("width", 1920)),
                height=int(spec.get("height", 1080)), fps=spec.get("fps", 24), clips=clip_list,
                items=[], keep_clip_audio=bool(spec.get("keep_clip_audio", False)),
                ducking=_ducking_cfg(spec), master=master,
                pan_scale=float(spec.get("pan_scale", 2.0)),
                preset=spec.get("preset", "medium"), crf=int(spec.get("crf", 18)))

    seen: set[str] = set()
    for k, t in enumerate(spec.get("tracks") or []):
        raw_stem = str(t.get("stem") or t.get("type") or "fx").lower()
        stem = STEM_ALIASES.get(raw_stem)
        if not stem:
            raise AssembleError(f"track[{k}]: stem {raw_stem!r} не поддерживается; "
                                f"есть {sorted(set(STEM_ALIASES))}")
        tid = re.sub(r"[^A-Za-z0-9_.-]", "_", str(t.get("id") or f"{stem}_{k:03d}"))
        if tid in seen:
            tid = f"{tid}_{k}"
        seen.add(tid)
        path = _resolve(t["path"], base)
        if not path.is_file():
            raise AssembleError(f"track {tid}: аудио не найдено: {path}")
        start = float(t.get("start", 0) or 0)
        if start < 0:
            raise AssembleError(f"track {tid}: start < 0")
        if start >= D:
            plan.warnings.append(f"{tid}: старт {start:.3f} с за пределами серии ({D:.3f} с) — пропущен")
            continue
        info = probe(path)
        trim = float(t.get("trim_start", 0) or 0)
        loop = bool(t.get("loop", False))
        available = D - start
        if t.get("end") is not None:
            want = float(t["end"]) - start
        elif t.get("duration"):
            want = float(t["duration"])
        else:
            want = available
        length = min(want, available)
        src_left = max(info["duration"] - trim, 0.0)
        if not loop:
            length = min(length, src_left)
        if length <= 0.001:
            plan.warnings.append(f"{tid}: нулевая длина на таймлайне — пропущен")
            continue
        pan = pan_position(t.get("pan", "C" if stem in ("dx", "fx", "foley") else None))
        if stem == "dx":
            pan = 0.0                       # диалог всегда в центре
        item = Item(id=tid, stem=stem, src=path, start=start, length=round(length, 3), trim_start=trim,
                    loop=loop, fade_in=float(t.get("fade_in", 0) or 0),
                    fade_out=float(t.get("fade_out", 0) or 0),
                    target_lufs=float(t["target_lufs"]) if t.get("target_lufs") is not None
                    else DEFAULT_TARGET_LUFS[stem],
                    normalize=bool(t.get("normalize", True)),
                    gain_db=float(t.get("gain_db", t.get("volume_db", 0)) or 0),
                    pan=pan, src_duration=info["duration"], src_channels=info["channels"] or 1,
                    cut=(not loop and (trim > 0 or length < src_left - 0.01)),
                    filter=str(t.get("filter") or ""))
        if item.filter and re.search(r"[;\[\]]", item.filter):
            raise AssembleError(f"track {tid}: filter должен быть простой цепочкой (без ; и [меток])")
        if item.fade_in + item.fade_out > item.length + 1e-6:
            plan.warnings.append(f"{tid}: фейды ({item.fade_in}+{item.fade_out} с) длиннее отрезка "
                                 f"{item.length} с — укорочены")
            scale = item.length / (item.fade_in + item.fade_out)
            item.fade_in, item.fade_out = round(item.fade_in * scale, 3), round(item.fade_out * scale, 3)
        item.norm_path = work / "clips" / f"{len(plan.items):03d}_{tid}.wav"
        plan.items.append(item)

    # перекрытие реплик одного персонажа не проверяем (нет поля персонажа), но предупреждаем об
    # одновременных DX вообще — это может быть и перебивание, и ошибка таймкода
    dx = sorted((i for i in plan.items if i.stem == "dx"), key=lambda i: i.start)
    for a, b in zip(dx, dx[1:]):
        if b.start < a.start + a.length - 0.05:
            plan.warnings.append(f"DX перекрываются: {a.id} и {b.id} (проверьте, что это перебивание)")
    return plan


# =========================================================== stage commands ===

def cmd_video(plan: Plan) -> list[str]:
    inputs, filters, labels = [], [], []
    W, H, fps = plan.width, plan.height, plan.fps
    for i, c in enumerate(plan.clips):
        inputs += ["-i", str(c["path"])]
        filters.append(
            f"[{i}:v]trim=start={_f(c['trim_start'])}:duration={_f(c['duration'])},setpts=PTS-STARTPTS,"
            f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
            f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1,fps={fps},format=yuv420p[v{i}]")
        labels.append(f"[v{i}]")
    filters.append(f"{''.join(labels)}concat=n={len(labels)}:v=1:a=0[vout]")
    return _ff(*inputs, "-filter_complex", ";".join(filters), "-map", "[vout]", "-an",
               "-c:v", "libx264", "-preset", plan.preset, "-crf", str(plan.crf), "-pix_fmt", "yuv420p",
               "-r", str(fps), "-t", _f(plan.duration), str(plan.work / "video.mp4"))


def _pre_chain(item: Item) -> list[str]:
    chain = [f"aresample={AUDIO_RATE}"]
    if item.stem == "dx":
        chain.append(DX_PROCESS)
    return chain


def cmd_measure(item: Item) -> list[str]:
    af = ",".join(_pre_chain(item) + ["ebur128=peak=sample:framelog=quiet"])
    return [_need("ffmpeg"), "-hide_banner", "-nostats", "-i", str(item.src), "-af", af, "-f", "null", "-"]


def cmd_normalize(item: Item, gain_db: float | str) -> list[str]:
    """Этап 1: клип → WAV 48k/24 бит на целевом уровне, потолок −3 dBFS, микрофейды."""
    gain = gain_db if isinstance(gain_db, str) else f"{gain_db:.2f}"
    chain = _pre_chain(item) + [f"volume={gain}dB", CLIP_LIMITER]
    if not item.loop and item.src_duration > 0.03:   # петли не трогаем — стык должен остаться чистым
        chain += ["afade=t=in:d=0.005", f"afade=t=out:st={item.src_duration - 0.01:.3f}:d=0.01"]
    return _ff("-i", str(item.src), "-af", ",".join(chain), "-ac", str(item.out_channels),
               "-c:a", "pcm_s24le", str(item.norm_path))


def _item_chain(item: Item, pan_scale: float) -> str:
    c: list[str] = []
    if item.loop:
        c += ["aloop=loop=-1:size=2e9", f"atrim=0:{_f(item.length)}"]
    else:
        c += [f"atrim=start={_f(item.trim_start)}:duration={_f(item.length)}"]
    c.append("asetpts=PTS-STARTPTS")
    if item.fade_in:
        c.append(f"afade=t=in:st=0:d={_f(item.fade_in)}")
    elif item.trim_start > 0:
        c.append("afade=t=in:d=0.005")
    if item.fade_out:
        c.append(f"afade=t=out:st={_f(max(item.length - item.fade_out, 0))}:d={_f(item.fade_out)}")
    elif item.cut or item.loop:
        c.append(f"afade=t=out:st={_f(max(item.length - 0.01, 0))}:d=0.01")
    if item.out_channels == 1:
        pos = item.pan if item.pan is not None else 0.0
        if item.stem == "dx":
            c.append("pan=stereo|c0=c0|c1=c0")
        else:
            gl, gr = pan_gains(pos, pan_scale)
            c.append(f"pan=stereo|c0={gl}*c0|c1={gr}*c0")
    else:
        c.append("aformat=channel_layouts=stereo")
        if item.pan:
            c.append(f"stereotools=balance_out={item.pan:.2f}")
    if item.filter:
        c.append(item.filter)
    if item.gain_db:
        c.append(f"volume={item.gain_db:.2f}dB")
    if item.start > 0:
        # Постановка на таймкод (см. _place): в ffmpeg 6.1 adelay после atrim=start>0 выдаёт тишину с pts=NOPTS,
        # amix такие кадры теряет — стем лишался ведущей тишины и уезжал раньше (S01E01 v2: DX на 72.7 с
        # раньше картинки, стем 1217.05 с вместо 1289.75; QA A1–A5).
        c.append(_place(item.start))
    return ",".join(c)


def _place(start: float) -> str:
    """Поставить поток на таймкод start: adelay вставляет тишину, asetpts=N/SR/TB заново нумерует pts по счёту
    сэмплов (лечит NOPTS у тишины adelay), точно по сэмплу и без больших буферов."""
    return f"adelay={int(round(start * 1000))}:all=1,asetpts=N/SR/TB"


def _stem_tail(D: float) -> str:
    return f"apad=whole_dur={_f(D)},atrim=0:{_f(D)},aformat=sample_rates={AUDIO_RATE}:channel_layouts=stereo"


def cmd_stem(plan: Plan, stem: str) -> list[str] | None:
    """Этап 2: один стем на всю длину серии."""
    D = plan.duration
    inputs, filters, labels = [], [], []
    if stem == "clip":
        if not plan.keep_clip_audio:
            return None
        for c in plan.clips:
            if not c["has_audio"]:
                continue
            n = len(labels)
            inputs += ["-i", str(c["path"])]
            ms = int(round(c["offset"] * 1000))
            filters.append(f"[{n}:a]atrim=start={_f(c['trim_start'])}:duration={_f(c['duration'])},"
                           f"asetpts=PTS-STARTPTS,aresample={AUDIO_RATE},aformat=channel_layouts=stereo,"
                           f"volume={float(c['volume_db']):.2f}dB" + (f",{_place(c['offset'])}" if ms else "")
                           + f"[a{n}]")
            labels.append(f"[a{n}]")
    else:
        for item in (i for i in plan.items if i.stem == stem):
            n = len(labels)
            inputs += ["-i", str(item.norm_path)]
            filters.append(f"[{n}:a]{_item_chain(item, plan.pan_scale)}[a{n}]")
            labels.append(f"[a{n}]")
    if not labels:
        return None
    if len(labels) == 1:
        filters.append(f"{labels[0]}{_stem_tail(D)}[{stem}]")
    else:
        filters.append(f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:dropout_transition=0,"
                       f"{_stem_tail(D)}[{stem}]")
    return _ff(*inputs, "-filter_complex", ";".join(filters), "-map", f"[{stem}]",
               "-c:a", "pcm_s24le", str(plan.work / f"stem_{stem}.wav"))


def _sc_params(p: dict) -> str:
    return ":".join(f"{k}={v}" for k, v in p.items())


def cmd_premix(plan: Plan, stems: list[str]) -> list[str]:
    """Этап 3: ducking MUS/AMB под DX + сумма. Возвращает команду (пишет premix и *_ducked.wav)."""
    inputs: list[str] = []
    for s in stems:
        inputs += ["-i", str(plan.work / f"stem_{s}.wav")]
    idx = {s: i for i, s in enumerate(stems)}
    lab = {s: f"[{i}:a]" for s, i in idx.items()}
    filters: list[str] = []
    monitors: list[tuple[str, Path]] = []
    ducked = [s for s in ("mus", "amb") if s in idx and s in plan.ducking] if "dx" in idx else []
    if ducked:
        sc = [f"[sc_{s}]" for s in ducked]
        filters.append(f"{lab['dx']}asplit={len(ducked) + 1}[dx]{''.join(sc)}")
        lab["dx"] = "[dx]"
        for s in ducked:
            filters.append(f"{lab[s]}[sc_{s}]sidechaincompress={_sc_params(plan.ducking[s])},"
                           f"asplit=2[{s}_d][{s}_mon]")
            lab[s] = f"[{s}_d]"
            monitors.append((f"[{s}_mon]", plan.work / f"{s}_ducked.wav"))
    labels = [lab[s] for s in stems]
    if len(labels) == 1:
        filters.append(f"{labels[0]}anull[premix]")
    else:
        filters.append(f"{''.join(labels)}amix=inputs={len(labels)}:normalize=0:"
                       f"duration=longest:dropout_transition=0[premix]")
    outs = ["-map", "[premix]", "-c:a", "pcm_s24le", str(plan.work / "premix.wav")]
    for label, path in monitors:
        outs += ["-map", label, "-c:a", "pcm_s24le", str(path)]
    return _ff(*inputs, "-filter_complex", ";".join(filters), *outs)


def cmd_master_pass1(plan: Plan) -> list[str]:
    m = plan.master
    return [_need("ffmpeg"), "-hide_banner", "-nostats", "-i", str(plan.work / "premix.wav"),
            "-af", "ebur128=peak=true:framelog=quiet,"
            f"loudnorm=I={_f(m['I'])}:TP={_f(m['TP'])}:LRA={_f(m['LRA_min'])}:print_format=json",
            "-f", "null", "-"]


def cmd_master_pass2(plan: Plan, meas: dict, lra_t: float | str) -> list[str]:
    m = plan.master
    af = (f"loudnorm=I={_f(m['I'])}:TP={_f(m['TP'])}:LRA={lra_t}:"
          f"measured_I={meas['input_i']}:measured_TP={meas['input_tp']}:"
          f"measured_LRA={meas['input_lra']}:measured_thresh={meas['input_thresh']}:"
          f"offset={meas['target_offset']}:linear=true:print_format=json,aresample={AUDIO_RATE}")
    return [_need("ffmpeg"), "-y", "-hide_banner", "-nostats", "-i", str(plan.work / "premix.wav"),
            "-af", af, "-c:a", "pcm_s24le", str(plan.work / "master.wav")]


def cmd_mux(plan: Plan, audio: Path) -> list[str]:
    return _ff("-i", str(plan.work / "video.mp4"), "-i", str(audio),
               "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
               "-c:a", "aac", "-b:a", AAC_BITRATE, "-ar", str(AUDIO_RATE), "-ac", "2",
               "-shortest", "-movflags", "+faststart", str(plan.output))


def cmd_control(path: Path) -> list[str]:
    return [_need("ffmpeg"), "-hide_banner", "-nostats", "-i", str(path), "-map", "0:a",
            "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"]


# ================================================================ execute ===

def _show(title: str, argv: list[str]) -> None:
    print(f"# {title}\n{shlex.join(argv)}\n")


def run_plan(plan: Plan, dry_run: bool = False) -> dict:
    """Выполнить этапы 0–6. В dry_run печатает команды; измеряемые значения — плейсхолдеры."""
    report: dict = {"output": str(plan.output), "duration": plan.duration, "workdir": str(plan.work),
                    "warnings": list(plan.warnings), "clips": []}
    if not dry_run:
        (plan.work / "clips").mkdir(parents=True, exist_ok=True)
        plan.output.parent.mkdir(parents=True, exist_ok=True)

    # 0. видео
    if dry_run:
        _show("0. video", cmd_video(plan))
    else:
        _run(cmd_video(plan), "video")

    # 1. нормализация клипов
    for item in plan.items:
        if dry_run:
            if item.normalize:
                _show(f"1. measure {item.id}", cmd_measure(item))
                g = f"<{item.target_lufs:g}-I_{item.id}>"
            else:
                g = "0"
            _show(f"1. normalize {item.id} → {item.target_lufs:g} LUFS", cmd_normalize(item, g))
            continue
        if item.normalize:
            meas = parse_ebur128(_run(cmd_measure(item), f"measure {item.id}").stderr)
            gain, mode = clip_gain(item.target_lufs, meas["I"], meas["peak"], item.src_duration)
        else:
            meas, gain, mode = {}, 0.0, "off"
        if mode in ("peak", "none") and item.normalize:
            report["warnings"].append(f"{item.id}: короткий/тихий клип — нормализация по пику "
                                      f"({SHORT_CLIP_PEAK_DB} dBFS), проверить на слух")
        _run(cmd_normalize(item, gain), f"normalize {item.id}")
        item.norm = {"measured_I": meas.get("I"), "measured_peak": meas.get("peak"),
                     "gain_db": gain, "mode": mode}
        report["clips"].append({"id": item.id, "stem": item.stem, "start": item.start,
                                "length": item.length, "target_lufs": item.target_lufs, **item.norm})

    # 2. стемы
    stems: list[str] = []
    for s in STEMS:
        argv = cmd_stem(plan, s)
        if argv is None:
            continue
        stems.append(s)
        if dry_run:
            _show(f"2. stem {s}", argv)
        else:
            _run(argv, f"stem {s}")
            got = probe(plan.work / f"stem_{s}.wav")["duration"]
            if abs(got - plan.duration) > 0.05:
                raise AssembleError(f"stem {s}: длина {got:.3f} с вместо {plan.duration:.3f} с "
                                    f"(таймлайн стема сдвинут — проверить постановку на таймкод)")
    report["stems"] = stems

    # 3. премикс (или тишина)
    premix = plan.work / "premix.wav"
    if not stems:
        argv = _ff("-f", "lavfi", "-i", f"anullsrc=r={AUDIO_RATE}:cl=stereo", "-t", _f(plan.duration),
                   "-c:a", "pcm_s24le", str(premix))
        report["warnings"].append("нет ни одной аудиодорожки — серия без звука")
    else:
        argv = cmd_premix(plan, stems)
    if dry_run:
        _show("3. premix (ducking MUS/AMB под DX)", argv)
    else:
        _run(argv, "premix")

    # 4. мастер
    audio_for_mux = premix
    if plan.master and stems:
        audio_for_mux = plan.work / "master.wav"
        if dry_run:
            _show("4. master, проход 1 (измерение)", cmd_master_pass1(plan))
            ph = {k: f"<{k}>" for k in ("input_i", "input_tp", "input_lra", "input_thresh", "target_offset")}
            _show("4. master, проход 2 (LRA = min(20, max(11, input_lra+1)))",
                  cmd_master_pass2(plan, ph, "<LRA_T>"))
        else:
            err = _run(cmd_master_pass1(plan), "loudnorm pass 1").stderr
            meas = master_measurement(parse_loudnorm_json(err), parse_ebur128(err))
            in_i = float(meas["input_i"])
            if not math.isfinite(in_i) or in_i <= SILENCE_LUFS:
                report["warnings"].append("премикс почти беззвучный — loudnorm пропущен")
                audio_for_mux = premix
            else:
                lra_t = lra_target(float(meas["input_lra"]), plan.master["LRA_min"], plan.master["LRA_max"])
                res = parse_loudnorm_json(_run(cmd_master_pass2(plan, meas, _f(lra_t)), "loudnorm pass 2").stderr)
                report["master"] = {"target": plan.master, "pass1": meas, "lra_target": lra_t,
                                    "normalization_type": res.get("normalization_type"),
                                    "pass2": res}
                if res.get("normalization_type") != "linear":
                    report["warnings"].append(
                        "loudnorm ушёл в dynamic-режим: опустить самые громкие эффекты в премиксе "
                        "на 2–3 dB и пересобрать (mix_plan.md §5)")

    # 5. mux
    argv = cmd_mux(plan, audio_for_mux)
    if dry_run:
        _show("5. mux", argv)
        _show("6. control", cmd_control(plan.output))
        return report
    _run(argv, "mux")

    # 6. контроль
    ctl = parse_ebur128(_run(cmd_control(plan.output), "control").stderr)
    report["control"] = ctl
    if plan.master and "master" in report:
        report["control"]["I_ok"] = abs(ctl["I"] - plan.master["I"]) <= ACCEPT_I_TOL
        report["control"]["TP_ok"] = ctl["peak"] <= plan.master["TP"] + 1e-9
        if not report["control"]["I_ok"]:
            report["warnings"].append(f"I = {ctl['I']} LUFS вне −14 ±1")
        if not report["control"]["TP_ok"]:
            report["warnings"].append(f"true peak {ctl['peak']} dBFS выше {plan.master['TP']} dBTP")
    (plan.work / "mix_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2,
                                                         default=str), encoding="utf-8")
    return report


def assemble(spec: dict | str | Path, dry_run: bool = False) -> Path:
    """Собрать серию по spec (dict или путь к JSON). Возвращает путь к mp4."""
    return assemble_report(spec, dry_run)[0]


def assemble_report(spec: dict | str | Path, dry_run: bool = False) -> tuple[Path, dict]:
    base = Path.cwd()
    if not isinstance(spec, dict):
        spec_path = Path(spec)
        base = spec_path.resolve().parent
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
    plan = build_plan(spec, base)
    report = run_plan(plan, dry_run=dry_run)
    for w in report["warnings"]:
        print(f"ВНИМАНИЕ: {w}", file=sys.stderr)
    return plan.output, report


# ================================================================ selftest ===

def _lavfi(args: list[str]) -> None:
    _run(_ff(*args), "selftest/lavfi")


def _mean_volume(path: Path, start: float, dur: float) -> float:
    res = subprocess.run([_need("ffmpeg"), "-hide_banner", "-ss", str(start), "-t", str(dur), "-i",
                          str(path), "-af", "volumedetect", "-vn", "-f", "null", "-"],
                         capture_output=True, text=True)
    for line in res.stderr.splitlines():
        if "mean_volume" in line:
            return float(line.split("mean_volume:")[1].split("dB")[0])
    return float("-inf")


def selftest(workdir: str | Path | None = None) -> dict:
    """Синтетика: клипы разных размеров/fps (один со звуком) + DX/FX/FOLEY/AMB/MUS/STING → mp4."""
    from . import config
    wd = Path(workdir) if workdir else config.output_dir() / "selftest"
    wd.mkdir(parents=True, exist_ok=True)
    _lavfi(["-f", "lavfi", "-i", "testsrc=size=1280x720:rate=30:duration=4", "-pix_fmt", "yuv420p",
            str(wd / "clip1.mp4")])
    _lavfi(["-f", "lavfi", "-i", "testsrc2=size=640x480:rate=25:duration=4",
            "-f", "lavfi", "-i", "sine=frequency=330:duration=4", "-shortest", "-pix_fmt", "yuv420p",
            str(wd / "clip2.mp4")])
    _lavfi(["-f", "lavfi", "-i", "smptebars=size=1920x1080:rate=24:duration=3", "-pix_fmt", "yuv420p",
            str(wd / "clip3.mp4")])
    # «речь»: тон с амплитудной модуляцией (слоги), моно
    _lavfi(["-f", "lavfi", "-i", "sine=frequency=440:duration=2.5", "-af",
            "volume='0.6+0.4*sin(2*PI*4*t)':eval=frame", "-ac", "1", str(wd / "line1.wav")])
    _lavfi(["-f", "lavfi", "-i", "sine=frequency=520:duration=1.5", "-c:a", "libmp3lame",
            str(wd / "line2.mp3")])
    _lavfi(["-f", "lavfi", "-i", "sine=frequency=1200:duration=0.3", str(wd / "hit.wav")])
    _lavfi(["-f", "lavfi", "-i", "anoisesrc=color=brown:duration=0.8:amplitude=0.3", str(wd / "steps.wav")])
    _lavfi(["-f", "lavfi", "-i", "anoisesrc=color=pink:duration=3:amplitude=0.2", "-ac", "2",
            str(wd / "amb_loop.wav")])
    _lavfi(["-f", "lavfi", "-i", "sine=frequency=220:duration=3", "-ac", "2", "-c:a", "libmp3lame",
            str(wd / "music.mp3")])
    _lavfi(["-f", "lavfi", "-i", "sine=frequency=880:duration=1.2", "-ac", "2", str(wd / "sting.wav")])
    spec = {
        "output": "episode_selftest.mp4",
        "clips": [{"path": "clip1.mp4"}, {"path": "clip2.mp4", "trim_start": 0.5},
                  {"path": "clip3.mp4", "duration": 2.5}],   # 4 + 3.5 + 2.5 = 10 с
        "tracks": [
            {"id": "amb1", "stem": "amb", "path": "amb_loop.wav", "start": 0, "end": 7.5, "loop": True,
             "fade_in": 1, "fade_out": 0.5},
            {"id": "mus1", "stem": "mus", "path": "music.mp3", "start": 0, "loop": True,
             "fade_in": 0.5, "fade_out": 2},
            {"id": "dx1", "stem": "dx", "path": "line1.wav", "start": 1.0},
            {"id": "dx2", "type": "dialog", "path": "line2.mp3", "start": 5.0},
            {"id": "hit1", "stem": "fx", "path": "hit.wav", "start": 4.2, "target_lufs": -18, "pan": "R30"},
            {"id": "foley1", "stem": "foley", "path": "steps.wav", "start": 7.0, "pan": "L30"},
            {"id": "sting1", "stem": "sting", "path": "sting.wav", "start": 8.0},
        ],
        "keep_clip_audio": True,
    }
    (wd / "spec.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    out, report = assemble_report(wd / "spec.json")
    info = probe(out)
    expected = 10.0
    work = Path(report["workdir"])
    ctl = report.get("control", {})
    # глубина ducking музыки: стем до и после sidechain на участке с репликой dx1 (1.0–3.5 с)
    duck_mus = _mean_volume(work / "stem_mus.wav", 1.5, 1.5) - _mean_volume(work / "mus_ducked.wav", 1.5, 1.5)
    duck_amb = _mean_volume(work / "stem_amb.wav", 1.5, 1.5) - _mean_volume(work / "amb_ducked.wav", 1.5, 1.5)
    checks = {
        "output": str(out),
        "resolution_1080p": (info["width"], info["height"]) == (1920, 1080),
        "has_audio": info["has_audio"],
        "duration": round(info["duration"], 2),
        "duration_ok": abs(info["duration"] - expected) < 0.1,
        "stems": report.get("stems"),
        "master_I": ctl.get("I"),
        "master_TP": ctl.get("peak"),
        "master_LRA": ctl.get("LRA"),
        "lra_target": report.get("master", {}).get("lra_target"),
        "normalization_type": report.get("master", {}).get("normalization_type"),
        "I_ok": bool(ctl.get("I_ok")),
        "TP_ok": bool(ctl.get("TP_ok")),
        "duck_mus_db": round(duck_mus, 1),
        "duck_amb_db": round(duck_amb, 1),
        "duck_mus_ok": 6.0 <= duck_mus <= 12.0,
        "duck_amb_ok": 1.0 <= duck_amb <= 5.0,
        "clip_modes": {c["id"]: c["mode"] for c in report.get("clips", [])},
        "warnings": report.get("warnings"),
    }
    checks["passed"] = all(checks[k] for k in ("resolution_1080p", "has_audio", "duration_ok",
                                                  "I_ok", "TP_ok", "duck_mus_ok", "duck_amb_ok"))
    return checks


def _cli() -> None:
    ap = argparse.ArgumentParser(description="Сборка серии через ffmpeg (mix_plan.md)")
    ap.add_argument("spec", nargs="?", help="JSON-описание серии")
    ap.add_argument("--dry-run", action="store_true",
                    help="только напечатать команды ffmpeg по этапам (измеряемые значения — <плейсхолдеры>)")
    ap.add_argument("--selftest", action="store_true", help="проверка на синтетических данных")
    args = ap.parse_args()
    if args.selftest:
        res = selftest()
        print(json.dumps(res, ensure_ascii=False, indent=2))
        sys.exit(0 if res["passed"] else 1)
    if not args.spec:
        ap.error("укажите spec.json или --selftest")
    out, report = assemble_report(args.spec, dry_run=args.dry_run)
    if not args.dry_run:
        print(json.dumps(report.get("control", {}), ensure_ascii=False))
        print(out)


if __name__ == "__main__":
    _cli()
