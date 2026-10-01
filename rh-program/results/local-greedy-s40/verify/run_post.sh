#!/bin/bash
# run_post.sh -- sequential follow-up jobs for rho = 0.6 (one heavy process at a time, load-gated):
#  (1) H_theta check at 10^9; (2) winding-number boxes for the two top zeros at 10^9 (Taylor moments + direct corners);
#  (3) the 4e9 run with the current generator (adds the Beurling Moebius sums M_P); (4) the x-dump analysis.
set -u
V="$(cd "$(dirname "$0")" && pwd)"; T=/private/tmp/rh-s40-local-greedy; A=$T/a_r06_1e9.u16
gate(){ while [ "$(ps -Ao pcpu,comm | awk '$1>50' | wc -l)" -ge 4 ]; do sleep 10; done; }
gate; "$T/hcheck" "$A" 1000000000 3 5 > "$V/logs/zeros/hcheck_r06_1e9.log"; echo "$(date +%H:%M:%S) hcheck done"
gate; python3 "$V/cert7.py" "$A" 1000000000 3 5 "$1" "$2" 0.02 24 400 > "$V/logs/zeros/cert_r06_z1_1e9.log" 2>&1; echo "$(date +%H:%M:%S) cert z1 done"
gate; python3 "$V/cert7.py" "$A" 1000000000 3 5 "$3" "$4" 0.02 24 400 > "$V/logs/zeros/cert_r06_z2_1e9.log" 2>&1; echo "$(date +%H:%M:%S) cert z2 done"
gate; cc -O2 -o "$T/s7gen" "$V/s7gen.c" -lm && /usr/bin/time -l "$T/s7gen" 3 5 4000000000 0 r06_4e9 "$T" 0 > "$V/logs/sweep/s7_v0_r3-5_X4000000000.log" 2> "$V/logs/sweep/s7_v0_r3-5_X4000000000.time"; echo "$(date +%H:%M:%S) 4e9 done"
gate; python3 "$V/analyze_x.py" "$T/x_r06_1e9.u32" 1000000000 > "$V/logs/sweep/analyze_x_r06_1e9.log" 2>&1; echo "$(date +%H:%M:%S) analyze_x done"
