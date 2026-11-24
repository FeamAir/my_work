"""r4 probe: salient pitches (harmonic sum, MIDI 55-88) per 0.25 s in a window, strongest onsets, 0.5 s envelope.
    python3 op_probe.py FILE --roll 56-62 --onsets 53-60,79-87 --env 50-87"""
import argparse, subprocess, numpy as np
SR=22050; PCS=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
def load(p):
    r=subprocess.run(["ffmpeg","-v","error","-i",p,"-ac","1","-ar",str(SR),"-f","f32le","-"],capture_output=True,check=True).stdout
    return np.frombuffer(r,dtype=np.float32).astype(float)
def nm(m): return f"{PCS[m%12]}{m//12-1}"
ap=argparse.ArgumentParser(); ap.add_argument("f"); ap.add_argument("--roll",default=""); ap.add_argument("--onsets",default=""); ap.add_argument("--env",default="")
a=ap.parse_args(); x=load(a.f)
if a.roll:
    t0,t1=map(float,a.roll.split("-")); n=8192
    for tc in np.arange(t0,t1,0.25):
        i=int(tc*SR); fr=x[i:i+n]*np.hanning(n); sp=np.abs(np.fft.rfft(fr,2*n)); f=np.fft.rfftfreq(2*n,1/SR)
        def e(hz): return sp[np.abs(f-hz)<hz*0.015].max() if (np.abs(f-hz)<hz*0.015).any() else 0
        sal={m:sum(e(440*2**((m-69)/12)*h)/h**0.5 for h in (1,2,3,4)) - 0.5*e(440*2**((m-69)/12)/2) for m in range(55,89)}
        top=sorted(sal,key=sal.get,reverse=True)[:3]
        print(f"{tc:6.2f}", " ".join(nm(m) for m in top))
if a.onsets:
    hop=110; e=np.sqrt(np.convolve(x**2,np.ones(hop)/hop,'same'))[::hop]; edb=20*np.log10(e+1e-9)
    d=np.convolve(np.diff(edb,prepend=edb[0]),np.ones(4),'same')
    for r in a.onsets.split(","):
        t0,t1=map(float,r.split("-")); idx=[i for i in range(int(t0*SR/hop),int(t1*SR/hop)) if d[i]==d[max(i-20,0):i+20].max() and d[i]>4]
        print("onsets",r," ".join(f"{i*hop/SR:.2f}({d[i]:.0f},{edb[i:i+40].max():.0f}dB)" for i in idx))
if a.env:
    t0,t1=map(float,a.env.split("-"))
    print("env0.5", " ".join(f"{t:.1f}:{10*np.log10(np.mean(x[int(t*SR):int((t+.5)*SR)]**2)+1e-12):.0f}" for t in np.arange(t0,t1,0.5)))
