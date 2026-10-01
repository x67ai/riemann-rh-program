#!/bin/bash
cd /private/tmp/rh-s41-lemmaB-U7-patterns
W="/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/lemmaB-s41/U7-patterns/verify/winvar.py"
R16=0.19634954084936207; R32=0.098174770424681035
python3 "$W" b16_1e10 $R16 0.5 3.16227766e9 3.98107171e9 1 > b16_top.win 2>&1
python3 "$W" b32_1e10 $R32 0.5 3.16227766e9 3.98107171e9 1 > b32_top.win 2>&1
python3 "$W" b16_1e10 $R16 0.5 3.16227766e8 3.98107171e8 1 > b16_mid.win 2>&1
python3 "$W" b32_1e10 $R32 0.5 3.16227766e8 3.98107171e8 1 > b32_mid.win 2>&1
for v in tq t3q d8 d4 dh; do
  case $v in tq) TAU=0.25;; t3q) TAU=0.75;; *) TAU=0.5;; esac
  python3 "$W" v16_${v}_1e9 $R16 $TAU 3.16227766e8 3.98107171e8 1 > v16_${v}_mid.win 2>&1
  python3 "$W" v32_${v}_1e9 $R32 $TAU 3.16227766e8 3.98107171e8 1 > v32_${v}_mid.win 2>&1
done
echo done > run_winvar.done
