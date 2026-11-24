"""Free OP diagnosis (r4): per-section loudness, band balance, lead salience, melody track, lift at the hook.

    python3 studio/music/gen/op_diagnose.py FILE [--sections 0,12,21,45,57,69,81,87] [--track 21-45,57-69]

lead_salience: per frame, energy of the strongest spectral peak (+its harmonics) in 250-1200 Hz over
total 250-1200 Hz energy, averaged: a clear single lead line scores high, a pad/wash scores low.
chroma_peak: share of the top pitch class per 0.37 s frame (melody/clarity vs smear).
Melody track: dominant f0 (HPS, 250-1000 Hz) per 0.1 s merged into notes >= 0.2 s.
"""
import argparse, json, subprocess, numpy as np
SR = 22050
PCS = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
def load(p):
    r = subprocess.run(["ffmpeg","-v","error","-i",p,"-ac","1","-ar",str(SR),"-f","f32le","-"],capture_output=True,check=True).stdout
    return np.frombuffer(r,dtype=np.float32).astype(float)
def db(v): return round(float(10*np.log10(v+1e-12)),1)
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("f")
    ap.add_argument("--sections", default="0,12,21,45,57,69,81,87"); ap.add_argument("--track", default="")
    a = ap.parse_args(); x = load(a.f)
    n, hop = 8192, 2048; w = np.hanning(n)
    fr = np.array([x[i:i+n]*w for i in range(0, len(x)-n, hop)])
    S = np.abs(np.fft.rfft(fr, axis=1))**2; f = np.fft.rfftfreq(n, 1/SR); t = np.arange(len(fr))*hop/SR + n/2/SR
    bands = {"sub<90": (25,90), "low90-250": (90,250), "mid250-1k": (250,1000), "hm1-4k": (1000,4000), "air4k+": (4000,11000)}
    mel = (f>=250)&(f<=1200)
    sal = []
    for k in range(len(fr)):
        s = S[k, mel]; tot = s.sum()+1e-12; i = np.argmax(s); f0 = f[mel][i]
        e = sum(S[k, np.abs(f-h*f0) < 6].sum() for h in (1,2,3))
        sal.append(min(e/ (S[k,(f>=250)&(f<=3600)].sum()+1e-12), 1))
    sal = np.array(sal)
    pcidx = np.round(12*np.log2(np.maximum(f,1)/440)+9).astype(int)%12
    cm = (f>=200)&(f<=2000)
    C = np.stack([S[:, cm][:, pcidx[cm]==k].sum(axis=1) for k in range(12)], 1)
    cpk = C.max(1)/(C.sum(1)+1e-12)
    secs = [float(s) for s in a.sections.split(",")]
    out = []
    for t0, t1 in zip(secs, secs[1:]):
        m = (t>=t0)&(t<t1); seg = x[int(t0*SR):int(t1*SR)]
        row = {"t": f"{t0:g}-{t1:g}", "rms_db": db(np.mean(seg**2))}
        tot = S[m].sum()
        for b,(lo,hi) in bands.items():
            row[b] = db(S[m][:, (f>=lo)&(f<hi)].sum()/tot)
        row["lead_salience"] = round(float(sal[m].mean()),3)
        row["chroma_peak"] = round(float(cpk[m].mean()),3)
        prof = C[m].sum(0); prof /= prof.sum()
        row["top_pc"] = [f"{PCS[i]} {prof[i]:.2f}" for i in np.argsort(prof)[::-1][:4]]
        row["A#"] = round(float(prof[10]),3)
        out.append(row)
    res = {"file": a.f, "dur": round(len(x)/SR,3), "sections": out}
    # lift: 1 s windows around the hook
    def win(t0,t1): s=x[int(t0*SR):int(t1*SR)]; return db(np.mean(s**2))
    res["lift"] = {"55.5-57.0": win(55.5,57.0), "57.0-58.5": win(57.0,58.5), "48-57": win(48,57), "57-69": win(57,69), "69-81": win(69,81), "21-45": win(21,45)}
    if a.track:
        res["melody"] = {}
        for r in a.track.split(","):
            t0,t1 = map(float, r.split("-")); seg = x[int(t0*SR):int(t1*SR)]; nn=4096; hh=2205; notes=[]
            for i in range(0, len(seg)-nn, hh):
                fz = seg[i:i+nn]*np.hanning(nn); sp = np.abs(np.fft.rfft(fz, 4*nn)); hps = sp.copy()
                for h in (2,3): d = sp[::h]; hps[:len(d)] *= d
                ff = np.fft.rfftfreq(4*nn, 1/SR); mm = (ff>250)&(ff<1000)
                notes.append(int(round(12*np.log2(ff[mm][np.argmax(hps[mm])]/440)+69)))
            merged=[]; cur=None; c=0; st=t0
            for j,p in enumerate(notes+[None]):
                if p==cur: c+=1; continue
                if cur is not None and c>=2: merged.append(f"{t0+ (j-c)*0.1:.1f}:{PCS[cur%12]}{cur//12-1}({c/10:.1f})")
                cur, c = p, 1
            res["melody"][r] = " ".join(merged)
    print(json.dumps(res, indent=1))
main()
