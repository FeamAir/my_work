#!/usr/bin/env bash
# OP anthem finish (free, local; composer-2026-11-24-r4). TAKE.mp3 (F minor, 87.0 s plan) -> 87.0 s OP mp3 256k:
# +1 semitone to F-sharp minor (as the master) -> anthem_remix.py (hook lift) -> v2a drum layer (drum_onsets/
# drum_reinforce, same weights, hall IR, 116.5 Hz notch) -> -14 LUFS, TP <= -1 dBTP -> fade 86.5-87.0.
#   anthem_finish.sh TAKE.mp3 OUT.mp3 [remix args...]
set -euo pipefail
G=$(cd "$(dirname "$0")" && pwd); IN=$1; OUT=$2; shift 2
T=${TMPDIR:-/tmp}/opanthem_$(basename "$OUT" .mp3); mkdir -p "$T"
ffmpeg -v error -y -i "$IN" -af "aresample=48000,rubberband=pitch=1.0594630943592953:formant=preserved:pitchq=quality,apad,atrim=0:87" -ac 2 -c:a pcm_s16le "$T/shift.wav"
python3 "$G/anthem_remix.py" "$T/shift.wav" "$T/lift.wav" "$@"
# room IR identical to drum_rework_v2.sh
sed -n '/^python3 - "\$T\/room_ir.wav" <<.P.$/,/^P$/p' "$G/drum_rework_v2.sh" | sed '1d;$d' > "$T/ir.py"
python3 "$T/ir.py" "$T/room_ir.wav"
python3 "$G/drum_onsets.py" "$T/shift.wav" "$T/on.json" > "$T/onsets.txt"
python3 "$G/drum_reinforce.py" "$T/on.json" "$T/layer.wav" 87.0
ffmpeg -v error -y -i "$T/lift.wav" -i "$T/layer.wav" -i "$T/room_ir.wav" -filter_complex "
[0:a]equalizer=f=116.5:t=q:w=6:g=-7,equalizer=f=250:t=q:w=1:g=-1.5[o];
[1:a]asplit=2[ld][lw];[lw]highpass=f=60,lowpass=f=6000[lw1];[lw1][2:a]afir=dry=0:wet=10[lr];
[ld][lr]amix=inputs=2:weights=1 0.4:normalize=0,volume=0.7[l];
[o][l]amix=inputs=2:weights=1 1:normalize=0,acompressor=threshold=-14dB:ratio=1.8:attack=40:release=160:makeup=1,alimiter=limit=0.9:attack=3:release=50:level=disabled" -c:a pcm_s24le "$T/mix.wav"
L=$(ffmpeg -hide_banner -nostats -i "$T/mix.wav" -af ebur128 -f null - 2>&1 | grep -E "^\s+I:" | tail -1 | awk '{print $2}')
GAIN=$(python3 -c "print(round(-14.0-($L)+0.25,2))")   # +0.25: the limiter takes back about that much
ffmpeg -v error -y -i "$T/mix.wav" -af "aresample=192000,volume=${GAIN}dB,alimiter=limit=0.80:attack=2:release=60:level=disabled:asc=1,aresample=48000,atrim=0:87,afade=t=out:st=86.5:d=0.5" -c:a libmp3lame -b:a 256k -ar 48000 "$OUT"
echo "in-LUFS $L gain $GAIN -> $OUT"
