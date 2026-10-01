#!/bin/bash
# batch6_smallrho.sh -- the theory unit's request (SHARED 11:55, 12:16): sup E and the largest g-prime gap for
# rho = pi/16 and pi/32 out to 1e10 and 1e11 (double-double windowed generator), then their zeros (real axis and rectangle).
cd "$(dirname "$0")"
T=/private/tmp/rh-s40-free-greedy
for r in pi16 pi32; do
  S8BIN=s8win ./run_s8.sh $r rule 1e10 0.5 win_${r}_1e10
  echo "$r 1e10: $(grep '^# done' logs/win_${r}_1e10.log | cut -c1-160)"
done
for r in pi16 pi32; do
  S8BIN=s8win ./run_s8.sh $r rule 1e11 0.5 win_${r}_1e11
  echo "$r 1e11: $(grep '^# done' logs/win_${r}_1e11.log | cut -c1-160)"
done
echo "batch6 end $(date '+%H:%M:%S')"
