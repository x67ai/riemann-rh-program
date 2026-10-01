#!/bin/bash
# run_certify.sh — certify the zero of F_{x_K} for every generated run (X ~ 10^6 .. 10^10, D = 16, 32); logs/certify_pi{D}_1e{d}.log
HERE="$(cd "$(dirname "$0")" && pwd)"; S=/private/tmp/rh-s41-U6-second
for D in 16 32; do
  if [ $D = 16 ]; then A=0.79; B=0.80; X1="0.794755370097 0.794755370098"; else A=0.89; B=0.90; X1="0.895076517592 0.895076517593"; fi
  for d in 6 7 8 9 10; do
    [ -f "$HERE/logs/certify_pi${D}_1e${d}.log" ] && grep -q CERTIFIED "$HERE/logs/certify_pi${D}_1e${d}.log" && continue
    K=$(grep -m1 '^# run_gen' "$HERE/logs/gen_pi${D}_1e${d}.log" | sed 's/.*K=\([0-9]*\).*/\1/')
    python3 "$HERE/certify_O.py" $D $K "$S/m_pi${D}_1e${d}" $A $B 15 $X1 > "$HERE/logs/certify_pi${D}_1e${d}.log" 2>&1
    grep CERTIFIED "$HERE/logs/certify_pi${D}_1e${d}.log"
  done
done
