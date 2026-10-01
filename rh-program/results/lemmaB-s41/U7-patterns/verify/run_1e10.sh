#!/bin/bash
cd /private/tmp/rh-s41-lemmaB-U7-patterns
C=$(python3 consts.py 16); /usr/bin/time -l ./s8gen $C 0.5 0 0 1e10 b16_1e10 2>b16_1e10.err > b16_1e10.log
C=$(python3 consts.py 32); /usr/bin/time -l ./s8gen $C 0.5 0 0 1e10 b32_1e10 2>b32_1e10.err > b32_1e10.log
echo done > run_1e10.done
