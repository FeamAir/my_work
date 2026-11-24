"""r4 delivery check: duration, integrated LUFS, true peak (ebur128 peak=true), hit times near the grid
(0:57.0, 1:09.0, 1:21.0, 1:22.5: strongest onset within -0.10..+0.15 s, and its level jump vs the preceding 0.5 s),
hook lift (0.75 s after 57.0 vs 0.75 s before), tail level at 86.5, A-sharp share per section (chroma 200-2000 Hz),
sub band < 90 Hz pitch-class peakiness (drone check), and writes FILE_phone.wav (HPF 300 + LPF 8k, mono).
    python3 op_verify.py FILE.mp3"""
import sys, re, json, subprocess, numpy as np
p = sys.argv[1]; SR = 48000
def ff(a): return subprocess.run(["ffmpeg", "-hide_banner", "-nostats", *a], capture_output=True, text=True).stderr
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True).stdout)
e = ff(["-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"])
I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", e)[-1]); TP = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)[-1])
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32).astype(float)
hop = 240; en = np.sqrt(np.convolve(x**2, np.ones(hop)/hop, "same"))[::hop]; edb = 20*np.log10(en+1e-9); fps = SR/hop
d = np.convolve(np.diff(edb, prepend=edb[0]), np.ones(3), "same")
def lvl(t0, t1): s = x[int(t0*SR):int(t1*SR)]; return 10*np.log10(np.mean(s**2)+1e-12)
hits = {}
for g in (57.0, 69.0, 81.0, 82.5):
    i0, i1 = int((g-0.10)*fps), int((g+0.15)*fps); i = i0+int(np.argmax(d[i0:i1]))
    hits[f"{g}"] = {"onset": round(i/fps, 3), "frame24": int(np.floor(i/fps*24))+1 if (i/fps*24) % 1 else int(i/fps*24),
                    "peak_dB": round(float(edb[i:i+int(0.1*fps)].max()), 1), "jump_vs_prev0.5s_dB": round(float(edb[i:i+int(0.1*fps)].max()-lvl(g-0.6, g-0.1)), 1)}
res = {"file": p.split("/")[-1], "duration_s": round(dur, 3), "LUFS_I": I, "TP_dBTP": TP, "hits": hits,
       "hook_lift_dB(57-57.75 vs 56.25-57)": round(lvl(57.0, 57.75)-lvl(56.25, 57.0), 1),
       "hook12_vs_rise12_dB": round(lvl(57, 69)-lvl(45, 57), 1), "tail_86.0-86.5_dB": round(lvl(86.0, 86.5), 1), "last_0.1s_dB": round(lvl(86.9, 87.0), 1)}
n = 8192; w = np.hanning(n); f = np.fft.rfftfreq(n, 1/SR)
pc = np.round(12*np.log2(np.maximum(f, 1)/440)+9).astype(int) % 12
secs = [0, 12, 21, 45, 57, 69, 81, 87]; ash = {}; sub = {}
for t0, t1 in zip(secs, secs[1:]):
    S = sum(np.abs(np.fft.rfft(x[i:i+n]*w))**2 for i in range(int(t0*SR), int(t1*SR)-n, 4096))
    m = (f >= 200) & (f <= 2000); prof = np.array([S[m][pc[m] == k].sum() for k in range(12)]); prof /= prof.sum()
    ash[f"{t0}-{t1}"] = round(float(prof[10]), 3)
    ms = (f > 25) & (f < 90); sp = np.array([S[ms][pc[ms] == k].sum() for k in range(12)]); sp /= sp.sum()+1e-12
    sub[f"{t0}-{t1}"] = f"{['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'][int(np.argmax(sp))]} {sp.max():.2f}"
res["A#_share"] = ash; res["sub_top_pc"] = sub
ph = p.rsplit(".", 1)[0] + "_phone.wav"
ff(["-y", "-i", p, "-af", "highpass=f=300,highpass=f=300,lowpass=f=8000,lowpass=f=8000", "-ac", "1", ph])
res["phone_file"] = ph.split("/")[-1]
print(json.dumps(res, indent=1))
