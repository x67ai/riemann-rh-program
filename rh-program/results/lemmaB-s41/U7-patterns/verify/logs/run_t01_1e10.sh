#!/bin/bash
cd /private/tmp/rh-s41-lemmaB-U7-patterns
C=$(python3 consts.py 16); /usr/bin/time -l ./s8gen $C 0.1 0 0 1e10 w16_t01_1e10 2> w16_t01_1e10.err > w16_t01_1e10.log
C=$(python3 consts.py 32); /usr/bin/time -l ./s8gen $C 0.1 0 0 1e10 w32_t01_1e10 2> w32_t01_1e10.err > w32_t01_1e10.log
echo done > run_t01_1e10.done
