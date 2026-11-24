"""OP drum rework: onset detection on the low and tom bands (writes JSON: kick/tom [time, peak_db, jump_db])."""
import sys, subprocess, json, numpy as np
SR=48000
def load(p,f):
    r=subprocess.run(["ffmpeg","-v","error","-i",p,"-af",f,"-ac","1","-ar",str(SR),"-f","f32le","-"],capture_output=True,check=True).stdout
    return np.frombuffer(r,dtype=np.float32).astype(float)
def onsets(x, thr_db, gap):
    hop=240; e=np.sqrt(np.convolve(x**2,np.ones(hop)/hop,'same'))[::hop]  # 5 ms frames
    edb=20*np.log10(e+1e-9); d=np.diff(edb,prepend=edb[0]); d=np.convolve(d,np.ones(3),'same')
    slow=np.convolve(edb,np.ones(60)/60,'same')
    out=[];last=-1e9
    for i in range(2,len(d)-2):
        if d[i]>thr_db and d[i]==max(d[i-2:i+3]) and (i-last)*hop/SR>gap:
            pk=edb[i:i+12].max(); out.append((round(i*hop/SR,3),round(float(pk),1),round(float(pk-slow[i]),1))); last=i
    return out
p=sys.argv[1]
k=onsets(load(p,"highpass=f=35,lowpass=f=110,lowpass=f=110"),3.0,0.14)
t=onsets(load(p,"highpass=f=110,lowpass=f=260"),3.5,0.12)
json.dump({"kick":k,"tom":t},open(sys.argv[2],"w"))
print(len(k),len(t))
for s in range(0,90,3):
    ks=[f"{(o[0]-s)/0.75:.2f}" for o in k if s<=o[0]<s+3 and o[1]>-45]
    print(s, "kick beats:", " ".join(ks))
