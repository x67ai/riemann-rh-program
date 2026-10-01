#!/bin/bash
# batch4.sh -- sequential: Rouche margins for the top zeros (X = 1e10), zeros of F_X for the variants at X = 1e8.
cd "$(dirname "$0")"
T=/private/tmp/rh-s40-free-greedy
python3 rouche.py $T/pi4_1e10.mom.1.000000e+10 0.896212490990 14.549935588839 0.01 0.03 0.1 0.3 > logs/rouche_pi4_1e10_z1.txt 2>&1
python3 rouche.py $T/pi4_1e10.mom.1.000000e+10 0.716282255946 28.358983966098 0.01 0.03 0.1 > logs/rouche_pi4_1e10_z2.txt 2>&1
python3 rouche.py $T/pi4_1e10.mom.1.000000e+10 0.712605243841 67.294748104996 0.01 0.03 0.1 > logs/rouche_pi4_1e10_z3.txt 2>&1
echo "rouche done $(date '+%H:%M:%S')"
for tag in var_eoverpi_th0.5_1e8 var_rsqrt2_th0.5_1e8 var_r0995_th0.5_1e8 var_r098_th0.5_1e8 var_r08_th0.5_1e8 var_pi4_th0.25_1e8 var_pi4_th0.75_1e8; do
  python3 zeros_scan.py $T/$tag.mom.1.000000e+08 200 0.5 1.05 0.005 --count > logs/zeros_$tag.txt 2>&1
  echo "$tag: $(grep -E '^# (argument|largest|real)' logs/zeros_$tag.txt | tr '\n' ' ')"
done
echo "batch4 end $(date '+%H:%M:%S')"
