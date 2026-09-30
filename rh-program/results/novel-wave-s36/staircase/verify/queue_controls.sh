#!/bin/sh
# waits for the current heavy job of this seed, then runs the queued censuses one at a time
PY="/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math/df16ac7a-b541-4904-8ae5-51d2ec1d5445/scratchpad/venv-gmp/bin/python"
cd "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/novel-wave-s36/staircase/verify"
while pgrep -f "reverify.py|rigor_xi1.py" > /dev/null; do sleep 20; done
run() { echo "$(date '+%H:%M:%S') start $*" >> queue_controls.log; "$PY" census.py "$@" > "census_$(echo $1 | tr ':' '_')_N$2_T$3.log" 2>&1; echo "$(date '+%H:%M:%S') done $*" >> queue_controls.log; }
for N in 1 2 3 4 6 7 8 9 11 12 13 14; do run DH $N 200; done
for N in 1 2 3 4 5 6; do run Faq:2.9:2 $N 200; done
for N in 1 3 5 7 9 11 13; do run chi4 $N 200; done
for N in 1 2 3; do run smooth $N 200; done
run zeta 6 230
echo "$(date '+%H:%M:%S') ALL DONE" >> queue_controls.log
