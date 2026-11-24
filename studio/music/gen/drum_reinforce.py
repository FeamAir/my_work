"""Drum reinforcement: layer synthesized acoustic-style kick/tom/taiko hits on detected onsets of the OP."""
import sys, os, json, wave, numpy as np
SR=48000; rng=np.random.default_rng(11)
def lp(x,a):  # one-pole lowpass
    y=np.empty_like(x); acc=0.0
    for i,v in enumerate(x): acc=a*acc+(1-a)*v; y[i]=acc
    return y
def env(n,tau,att=0.001):
    t=np.arange(n)/SR; return np.minimum(t/att,1)*np.exp(-t/tau)
def membrane(f0,bend,btau,tau,dur,partials=((1,1.0),),noise=0.3,ntau=0.02,nlp=0.6):
    n=int(dur*SR); t=np.arange(n)/SR
    out=np.zeros(n)
    for ratio,g in partials:
        f=ratio*f0*(1+bend*np.exp(-t/btau)); ph=2*np.pi*np.cumsum(f)/SR
        out+=g*np.sin(ph)*env(n,tau/ratio**0.5)
    nz=lp(rng.standard_normal(n),nlp)*env(n,ntau)
    out+=noise*nz/np.max(np.abs(nz))
    out=np.tanh(1.6*out)/np.tanh(1.6)
    fade=np.ones(n); m=int(0.03*SR); fade[-m:]=np.linspace(1,0,m)
    return out*fade
def kick(v):
    k=membrane(46.25*(1+rng.uniform(-.01,.01)),1.4,0.03,0.12,0.4,((1,1.0),(2.02,0.12)),noise=0.25,ntau=0.012,nlp=0.35)
    n=len(k); click=rng.standard_normal(n)*env(n,0.004); click=click-lp(click,0.7)  # highpassed beater click
    return v*(k+0.18*click/np.max(np.abs(click)))
def tom(v,f):
    return v*membrane(f*(1+rng.uniform(-.01,.01)),0.22,0.05,0.22,0.7,((1,1.0),(1.59,0.35),(2.14,0.15)),noise=0.35,ntau=0.03,nlp=0.5)
def taiko(v):
    s=np.zeros(int(1.3*SR))
    for off,det,g in ((0,1.0,1.0),(0.009,1.014,0.8),(0.017,0.987,0.7)):
        h=membrane(55.0*det,0.28,0.06,0.34,1.1,((1,1.0),(1.52,0.4),(2.01,0.2)),noise=0.55,ntau=0.035,nlp=0.75)
        o=int(off*SR); s[o:o+len(h)]+=g*h[:len(s)-o]
    return v*s/2.0
def place(buf,t,smp,pan):
    i=int(t*SR); n=min(len(smp),buf.shape[0]-i)
    if n<=0 or i<0: return
    buf[i:i+n,0]+=smp[:n]*np.sqrt(1-pan); buf[i:i+n,1]+=smp[:n]*np.sqrt(pan)
on=json.load(open(sys.argv[1])); dur=float(sys.argv[3]); out=sys.argv[2]
B=0.75; OFF=0.04  # beat length, grid offset of the take
buf=np.zeros((int(dur*SR)+SR,2))
def vel(r): return float(np.clip(0.35+0.04*(r-10),0.3,1.0))
DRUMS=(12.0,81.0)
for t,pk,r in on["kick"]:
    if DRUMS[0]<=t<DRUMS[1] and r>=11: place(buf,t-0.002,kick(vel(r)),0.5)
for t,pk,r in on["tom"]:
    if DRUMS[0]<=t<DRUMS[1] and r>=12:
        f=92.5 if (int(t*100)%2==0) else 138.6
        place(buf,t-0.002,tom(0.55*vel(r),f),0.38 if f>100 else 0.62)
KITONLY=len(sys.argv)>4
# taiko-style ensemble hits on bar downbeats of the hook and answer, beats 1 and 3 on the last rise bar
# r4 knobs (env; defaults = v2a): HOOK_TAIKO = taiko velocity on 0:57.0, FILL57 = scale of the tom fill into 0:57.0
HOOK_TAIKO=float(os.environ.get('HOOK_TAIKO','0.9')); FILL57=float(os.environ.get('FILL57','1.0'))
for bar_t in ([] if KITONLY else np.arange(57.0,84.0,3.0)): place(buf,bar_t+OFF,taiko(1.0 if bar_t==81.0 else HOOK_TAIKO if bar_t==57.0 else 0.9 if bar_t==69.0 else 0.65),0.5)
for t in (() if KITONLY else (54.0+OFF,54.0+1.5+OFF)): place(buf,t,taiko(0.6),0.5)
if not KITONLY: place(buf,82.5+OFF,taiko(1.0),0.5)  # the last hit 1:22.5 (OP storyboard S7, logo)
# tom fills into the rise, the hook (octave leap at 0:57) and the answer: last beat, sixteenths, high to low
for end in (() if KITONLY else (45.0,57.0,69.0)):
    seq=[(138.6,0.45,0.35),(138.6,0.5,0.4),(92.5,0.6,0.6),(92.5,0.75,0.62)]
    for k,(f,v,p) in enumerate(seq):
        tt=end-B+OFF+k*B/4+rng.uniform(-0.006,0.006); place(buf,tt,tom(v*rng.uniform(0.9,1.05)*(FILL57 if end==57.0 else 1.0),f),p)
buf=buf[:int(dur*SR)]
buf/=np.max(np.abs(buf))*1.12
w=wave.open(out,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((buf*32767).astype('<i2').tobytes()); w.close(); print("ok",out)
