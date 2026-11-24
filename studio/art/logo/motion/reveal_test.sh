#!/usr/bin/env bash
# $0 test of the HOLLOWSTONE reveal (cut 33 from the logo landing on; the INK + spray wipe of the OP build come before it).
# t=0 here = 1:22.5 (frame 1980). Logo lands t=15f, drain 23-47f, glint 30-54f, fade 96-107f. 24 fps, 4.5 s.
set -euo pipefail
R=/home/user/my_work
L=$R/studio/art/logo/final
PLATE=${PLATE:-$R/studio/direction/refs/PL-0014/D08_S1_dusk_v1.png}
OUT=${1:-$R/studio/art/logo/motion/reveal_test.mp4}
W=1300; TIDE=243   # logo width in frame; tide line y in the 1500-px logo
ffmpeg -v error -y \
 -loop 1 -t 4.5 -r 24 -i "$PLATE" \
 -loop 1 -t 4.5 -r 24 -i "$L/HOLLOWSTONE_logo_master_alpha.png" \
 -filter_complex "
 [0:v]crop=716:403:330:0,scale=3840:2160,zoompan=z='1+0.03*on/108':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s=1920x1080:fps=24,setsar=1[plate];
 [1:v]scale=$W:-1,format=rgba,split=3[dry][wet0][gl0];
 [wet0]eq=brightness=-0.16:saturation=0.75,colorbalance=bs=0.08:bm=0.05,
   geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='alpha(X,Y)*clip((Y-$TIDE*clip((N-23)/24,0,1))/10+1,0,1)*(1-gte(Y,$TIDE)*clip((N-47)/13,0,1))'[wet];
 [gl0]geq=r=235:g=242:b=250:a='alpha(X,Y)*lt(Y,$TIDE)*0.32*exp(-pow((X-0.35*Y-(-300+(W+600)*clip((N-30)/24,0,1)))/34,2))'[glint];
 [dry][wet]overlay=0:0:format=auto[l1];
 [l1][glint]overlay=0:0:format=auto,
   scale=w='iw*if(lt(n,23),1.14-0.14*clip((n-15)/8,0,1),1)*(1+0.015*n/108)':h=-1:eval=frame,
   null[logo];
 [plate][logo]overlay=x='(W-w)/2+if(between(n,15,20),6*sin(n*2.6),0)':y='660-h/2+if(between(n,15,20),4*cos(n*3.1),0)':eval=frame:format=auto:enable='gte(n,15)',
   fade=t=out:st=4.0:d=0.5,format=yuv420p[v]" \
 -map "[v]" -r 24 -c:v libx264 -crf 20 -preset medium "$OUT"
echo "$OUT"
