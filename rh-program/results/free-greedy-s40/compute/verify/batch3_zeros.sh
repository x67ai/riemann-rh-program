#!/bin/bash
# batch3_zeros.sh -- zeros of F_X for S8(pi/4) at X = 1e10, X/2, X/4, 1e9, 1e8, 1e7 (snapshots of the 1e10 run), sequential.
cd "$(dirname "$0")"
T=/private/tmp/rh-s40-free-greedy
for x in 1.000000e+10 5.000000e+09 2.500000e+09 1.000000e+09 1.000000e+07; do
  python3 zeros_scan.py $T/pi4_1e10.mom.$x 200 0.5 1.05 0.005 --count > logs/zeros_pi4_X$x.txt 2>&1
  echo "$x: $(grep -E "^# (argument|largest|real)" logs/zeros_pi4_X$x.txt | tr "\n" " ")"
done
