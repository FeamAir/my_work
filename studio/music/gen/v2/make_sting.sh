#!/usr/bin/env bash
# Logo sting (r5): 3.0 s from the finished anthem, 82.50-85.50 s (hit at ~0.045 s = picture frame 1981),
# 8 ms fade-in, natural ring then 0.9 s fade (curve exp), -14 LUFS-I, true peak <= -1 dBTP, mp3 256k + wav 48k/24.
#   make_sting.sh ANTHEM.mp3 OUT_BASENAME(without extension)
set -euo pipefail
IN=$1; OUT=$2; T=$(mktemp -d)
ffmpeg -v error -y -ss 82.50 -t 3.0 -i "$IN" -af "afade=t=in:d=0.004,afade=t=out:st=2.1:d=0.9:curve=exp" -ar 48000 -c:a pcm_s24le "$T/cut.wav"
L=$(ffmpeg -hide_banner -nostats -i "$T/cut.wav" -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1 | awk '{print $2}')
G=$(python3 -c "print(round(-14.0-($L)+0.2,2))")
ffmpeg -v error -y -i "$T/cut.wav" -af "aresample=192000,volume=${G}dB,alimiter=limit=0.80:attack=1:release=50:level=disabled:asc=1,aresample=48000" -c:a pcm_s24le "$OUT.wav"
ffmpeg -v error -y -i "$OUT.wav" -c:a libmp3lame -b:a 256k -ar 48000 "$OUT.mp3"
for f in "$OUT.wav" "$OUT.mp3"; do ffmpeg -hide_banner -nostats -i "$f" -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|Peak):" | tr -s ' ' | tr '\n' ' '; echo " <- $f"; done
rm -rf "$T"
