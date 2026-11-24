"""r4: harmonic/percussive split (median filtering) per section: harmonic level, H/P ratio,
harmonic energy by register (lead 250-800 Hz, brass/upper 800-2.5k), and harmonic loudness jump at the hook.
    python3 op_hpss.py FILE [--sections 0,12,21,45,57,69,81,87]"""
import argparse, subprocess, json, numpy as np
from scipy.ndimage import median_filter
SR=22050
ap=argparse.ArgumentParser(); ap.add_argument("f"); ap.add_argument("--sections",default="0,12,21,45,57,69,81,87"); a=ap.parse_args()
x=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",a.f,"-ac","1","-ar",str(SR),"-f","f32le","-"],capture_output=True,check=True).stdout,dtype=np.float32).astype(float)
n,hop=2048,512; w=np.hanning(n)
S=np.abs(np.array([np.fft.rfft(x[i:i+n]*w) for i in range(0,len(x)-n,hop)]))**2
f=np.fft.rfftfreq(n,1/SR); t=np.arange(len(S))*hop/SR
H=median_filter(S,size=(17,1)); P=median_filter(S,size=(1,17)); Mh=H**2/(H**2+P**2+1e-20)
Sh=S*Mh; Sp=S*(1-Mh)
def db(v): return round(float(10*np.log10(v+1e-20)),1)
secs=[float(s) for s in a.sections.split(",")]; out=[]
ref=Sh.sum()/len(Sh)
for t0,t1 in zip(secs,secs[1:]):
    m=(t>=t0)&(t<t1)
    hl=Sh[m].sum()/m.sum(); pl=Sp[m].sum()/m.sum()
    lead=Sh[m][:,(f>=250)&(f<800)].sum()/m.sum(); up=Sh[m][:,(f>=800)&(f<2500)].sum()/m.sum()
    out.append({"t":f"{t0:g}-{t1:g}","harm_db":db(hl/ref),"perc_db":db(pl/ref),"H/P_db":db(hl/pl),"lead250-800_db":db(lead/ref),"upper0.8-2.5k_db":db(up/ref)})
def hw(t0,t1):
    m=(t>=t0)&(t<t1); return db(Sh[m].sum()/m.sum()/ref)
print(json.dumps({"file":a.f.split('/')[-1],"sections":out,"harm_55.5-57":hw(55.5,57),"harm_57-58.5":hw(57,58.5),"harm_48-57":hw(48,57),"harm_57-69":hw(57,69)}))
