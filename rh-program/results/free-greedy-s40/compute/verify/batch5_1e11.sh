#!/bin/bash
# batch5_1e11.sh -- after the 1e11 run: E analysis, half-decade table, zeros at X = 1e11, X/2, X/4, explicit formula,
# Rouche margin of rho_1 at X = 1e11, then a high-zero scan (sigma >= 0.7, t <= 1000) at X = 1e11.  Sequential.
cd "$(dirname "$0")"
T=/private/tmp/rh-s40-free-greedy
python3 analyze_E.py win_pi4_1e11 "pi/4" > logs/win_pi4_1e11.Eanalysis.txt 2>&1
python3 table_halfdecade.py win_pi4_1e11 1e3 > logs/table_pi4_1e11.md 2>&1
python3 tail_shape.py win_pi4_1e11 > logs/tail_shape_pi4_1e11.txt 2>&1
for x in 1.000000e+11 5.000000e+10 2.500000e+10; do
  python3 zeros_scan.py $T/win_pi4_1e11.mom.$x 200 0.5 1.05 0.005 --count > logs/zeros_pi4_X$x.txt 2>&1
  echo "$x: $(grep -E '^# (argument|largest|real)' logs/zeros_pi4_X$x.txt | tr '\n' ' ')"
done
python3 explicit.py logs/zeros_pi4_X1.000000e+11.txt win_pi4_1e11 1e4 > logs/explicit_pi4_1e11.txt 2>&1
python3 rouche.py $T/win_pi4_1e11.mom.1.000000e+11 0.896212491 14.549935589 0.01 0.03 0.1 > logs/rouche_pi4_1e11_z1.txt 2>&1
python3 zeros_scan.py $T/win_pi4_1e11.mom.1.000000e+11 1000 0.7 1.05 0.005 > logs/zeros_pi4_X1e11_high.txt 2>&1
echo "batch5 end $(date '+%H:%M:%S')"
