#!/bin/bash
# regenerate the 1e10 runs with all per-cell arrays and the watch dumps of the top-20 excursions (+ controls)
cd /private/tmp/rh-s41-lemmaB-U7-patterns
C=$(python3 consts.py 16); /usr/bin/time -l ./s8gen2 $C 0.5 0 0 1e10 b16_1e10 b16_1e10.watch.in 2>b16_1e10.m.err > b16_1e10.m.log
C=$(python3 consts.py 32); /usr/bin/time -l ./s8gen2 $C 0.5 0 0 1e10 b32_1e10 b32_1e10.watch.in 2>b32_1e10.m.err > b32_1e10.m.log
echo done > run_multi.done
