#!/bin/bash
# batch7_smallrho_zeros.sh -- zeros of F_X (real axis + rectangle 0.5 < sigma < 1.05, t <= 200) for rho = pi/16, pi/32
# at X = 1e10 and 1e11, the explicit formula against psi_P - x, and the E analysis.  Sequential.
cd "$(dirname "$0")"
T=/private/tmp/rh-s40-free-greedy
for r in pi16 pi32; do
  python3 analyze_E.py win_${r}_1e11 "pi/${r#pi}" > logs/win_${r}_1e11.Eanalysis.txt 2>&1
  for x in 1.000000e+10 1.000000e+11; do
    python3 zeros_scan.py $T/win_${r}_1e11.mom.$x 200 0.5 1.05 0.005 --count > logs/zeros_${r}_X$x.txt 2>&1
    echo "$r $x: $(grep -E '^# (argument|largest|real)' logs/zeros_${r}_X$x.txt | tr '\n' ' ')"
  done
  python3 explicit.py logs/zeros_${r}_X1.000000e+11.txt win_${r}_1e11 1e4 > logs/explicit_${r}_1e11.txt 2>&1
  echo "$r explicit: $(tail -1 logs/explicit_${r}_1e11.txt)"
done
echo "batch7 end $(date '+%H:%M:%S')"
