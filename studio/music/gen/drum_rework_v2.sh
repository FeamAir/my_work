#!/usr/bin/env bash
# OP drum rework v2 (free, local; composer-2026-11-24-r3). Reproduces lib_mus_theme-op-drums_v2a/b.mp3
# from lib_mus_theme-op-fullrange_v1.wav. Needs ffmpeg + numpy. Room IR: 1.6 s synthetic hall (see r3 report).
set -euo pipefail
G=$(cd "$(dirname "$0")" && pwd); M="$G/../../../output/music"; T=${TMPDIR:-/tmp}/opdrums; mkdir -p "$T"
IN="$M/lib_mus_theme-op-fullrange_v1.wav"
python3 - "$T/room_ir.wav" <<'P'
import sys,wave,numpy as np
sr=48000;n=int(1.6*sr);rng=np.random.default_rng(7);t=np.arange(n)/sr;ir=np.zeros((n,2))
for ch in range(2):
    x=rng.standard_normal(n)*np.exp(-t*6.9/1.4);y=np.copy(x)
    for i in range(1,n): y[i]=0.55*y[i-1]+0.45*x[i]
    y[:int(0.012*sr)]=0
    for d,g in [(0.017,0.5),(0.023,0.4),(0.031,0.35),(0.043,0.3),(0.061,0.22)]: y[int((d+0.002*ch)*sr)]+=g*(1 if ch else -1)
    ir[:,ch]=y/np.abs(y).sum()*4
w=wave.open(sys.argv[1],'wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((np.clip(ir,-1,1)*32767).astype('<i2').tobytes());w.close()
P
python3 "$G/drum_onsets.py" "$IN" "$T/on.json" >/dev/null
python3 "$G/drum_reinforce.py" "$T/on.json" "$T/layer_a.wav" 90.0
python3 "$G/drum_reinforce.py" "$T/on.json" "$T/layer_b.wav" 90.0 kitonly
mix(){ ffmpeg -v error -y -i "$IN" -i "$1" -i "$T/room_ir.wav" -filter_complex "
[0:a]equalizer=f=116.5:t=q:w=6:g=-7,equalizer=f=250:t=q:w=1:g=-1.5[o];
[1:a]asplit=2[ld][lw];[lw]highpass=f=60,lowpass=f=6000[lw1];[lw1][2:a]afir=dry=0:wet=10[lr];
[ld][lr]amix=inputs=2:weights=1 $2:normalize=0,volume=$3[l];
[o][l]amix=inputs=2:weights=1 1:normalize=0,acompressor=threshold=-14dB:ratio=1.8:attack=40:release=160:makeup=1,alimiter=limit=0.9:attack=3:release=50:level=disabled" -c:a pcm_s24le "$4"
ffmpeg -v error -y -i "$4" -af "aresample=192000,volume=$5dB,alimiter=limit=0.80:attack=2:release=60:level=disabled:asc=1,aresample=48000,atrim=0:90,afade=t=out:st=89.6:d=0.4" -c:a libmp3lame -b:a 256k -ar 48000 "$6"; }
mix "$T/layer_a.wav" 0.4 0.7 "$T/mix_a.wav" 1.1 "$M/lib_mus_theme-op-drums_v2a.mp3"
mix "$T/layer_b.wav" 0.3 0.5 "$T/mix_b.wav" 1.2 "$M/lib_mus_theme-op-drums_v2b.mp3"
