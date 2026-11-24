#!/usr/bin/env bash
# $0 test of the HOLLOWSTONE reveal (C13 from the logo landing on; the INK + spray wipe of the OP build come with it).
# v1.1 (2026-11-24, keeper R2.5 + analyst #5): the logo lands ON the final hit (frame 1981).
# t=0 here = frame 1980 (1:22.5). Logo lands n=1-8 (1981-1988), shake n=1-6; the UPPER part (above the tide line)
# arrives wet and drains top-down n=9-24 (1989-2004); below the tide line the master stays exactly as painted in every
# frame; glint n=36-59 (2016-2039); a sky/stone-tinted drop gathers n=40-59 and leaves on n=60 (2040, drip cue);
# fade n=96-107. The plate under the word is darkened (-40 % behind the upper half, -60 % behind the lower half,
# soft edges); the logo keeps its own colours, no glow. 24 fps, 4.5 s.
set -euo pipefail
R=/home/user/my_work
L=$R/studio/art/logo/final
PLATE=${PLATE:-$R/studio/direction/refs/PL-0014/D08_S1_dusk_v1.png}
OUT=${1:-$R/studio/art/logo/motion/reveal_test.mp4}
W=1300; TIDE=243   # logo width in frame; tide line y in the 1300-px logo (336 of 676 in the 1800-px assets = half the cap height)
ffmpeg -v error -y \
 -loop 1 -t 4.5 -r 24 -i "$PLATE" \
 -loop 1 -t 4.5 -r 24 -i "$L/HOLLOWSTONE_logo_master_alpha.png" \
 -f lavfi -t 4.5 -i "color=c=black:s=1920x1080:r=24,format=rgba" \
 -f lavfi -t 4.5 -i "color=c=0x7E848C:s=18x26:r=24,format=rgba" \
 -filter_complex "
 [0:v]crop=716:403:330:0,scale=3840:2160,zoompan=z='1+0.03*on/108':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s=1920x1080:fps=24,setsar=1,format=rgba[plate0];
 [2:v]geq=r=0:g=0:b=0:a='255*(0.40+0.20*clip((Y-540)/240,0,1))*clip((Y-250)/220,0,1)*(1-clip((Y-930)/150,0,1))*(0.75+0.25*abs(X/960-1))'[band];
 [plate0][band]overlay=0:0:format=auto[plate];
 [1:v]scale=$W:-1,format=rgba,split=3[dry][wet0][gl0];
 [wet0]eq=brightness=-0.16:saturation=0.75,colorbalance=bs=0.08:bm=0.05,
   geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='alpha(X,Y)*lt(Y,$TIDE)*clip((Y-$TIDE*clip((N-9)/16,0,1))/10+1,0,1)*(1-clip((N-24)/6,0,1))'[wet];
 [gl0]geq=r=235:g=242:b=250:a='alpha(X,Y)*lt(Y,$TIDE)*0.32*exp(-pow((X-0.35*Y-(-300+(W+600)*clip((N-36)/24,0,1)))/34,2))'[glint];
 [dry][wet]overlay=0:0:format=auto[l1];
 [l1][glint]overlay=0:0:format=auto,
   scale=w='2*trunc(iw*if(lt(n,9),1.14-0.14*clip((n-1)/8,0,1),1)*(1+0.015*n/108)/2)':h=-2:eval=frame,
   null[logo];
 [3:v]geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='255*lt(pow((X-9)/9,2)+pow((Y-17)/9,2),1)+255*lt(Y,17)*lt(abs(X-9),Y/2)'[drop0];
 [drop0]scale=w='2*trunc(max(2,18*clip((n-40)/20,0,1))/2)':h=-2:eval=frame[drop];
 [plate][logo]overlay=x='(W-w)/2+if(between(n,1,6),6*sin(n*2.6),0)':y='660-h/2+if(between(n,1,6),4*cos(n*3.1),0)':eval=frame:format=auto:enable='gte(n,1)'[v1];
 [v1][drop]overlay=x=1181-w/2:y='864+if(gt(n,60),1500*pow((n-60)/24,2),0)':eval=frame:format=auto:enable='gte(n,40)',
   fade=t=out:st=4.0:d=0.5,format=yuv420p[v]" \
 -map "[v]" -r 24 -frames:v 108 -c:v libx264 -crf 20 -preset medium "$OUT"
echo "$OUT"
