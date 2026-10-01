#!/bin/bash
# extreme rigid-share variants at 1e9 (pi/16): threshold 0.1 and early placement delta = 0.4 t (both p1 = 1 + 0.1 t)
cd /private/tmp/rh-s41-lemmaB-U7-patterns
C=$(python3 consts.py 16); T=$(python3 -c "import math; print(repr(16/math.pi))"); R=$(python3 -c "import math; print(repr(math.pi/16))")
/usr/bin/time -l ./s8gen2 $C 0.1 0 0 1e9 v16_t01_1e9 2> v16_t01_1e9.err > v16_t01_1e9.log
/usr/bin/time -l ./s8gen2 $C 0.5 0.4 0 1e9 v16_d40_1e9 2> v16_d40_1e9.err > v16_d40_1e9.log
P1=$(python3 -c "print(repr(1+0.1*$T))"); DL=$(python3 -c "print(repr(0.4*$T))")
./stats v16_t01_1e9 $T $R 0.1 $P1 1e9 50 > v16_t01_1e9.stats 2>/dev/null; ./inherit v16_t01_1e9 $T $R 0.1 0 1e9 > v16_t01_1e9.inh 2>/dev/null
./stats v16_d40_1e9 $T $R 0.5 $P1 1e9 50 > v16_d40_1e9.stats 2>/dev/null; ./inherit v16_d40_1e9 $T $R 0.5 $DL 1e9 > v16_d40_1e9.inh 2>/dev/null
W="/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/lemmaB-s41/U7-patterns/verify/winvar.py"
python3 "$W" v16_t01_1e9 $R 0.1 3.16227766e8 3.98107171e8 1 > v16_t01_mid.win 2>&1
python3 "$W" v16_d40_1e9 $R 0.5 3.16227766e8 3.98107171e8 1 > v16_d40_mid.win 2>&1
echo done > run_variants2.done
