#!/bin/sh
PY="/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math/df16ac7a-b541-4904-8ae5-51d2ec1d5445/scratchpad/venv-gmp/bin/python"
cd "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/novel-wave-s36/staircase/verify"
while ! grep -q "ALL DONE" queue2.log 2>/dev/null; do sleep 30; done
for N in 1 2 3 4 5 6; do
  echo "$(date '+%H:%M:%S') start haglund $N" >> queue3.log
  "$PY" census.py haglund $N 200 > census_haglund_N${N}_T200.log 2>&1
done
"$PY" monotone_check.py census_haglund_N*_T200.json > monotone_haglund.log 2>&1
echo "$(date '+%H:%M:%S') start rigor R1 R4" >> queue3.log
"$PY" rigor_xi1.py R1 R4 > rigor_xi1_R1_R4.log 2>&1
echo "$(date '+%H:%M:%S') start rigor R2" >> queue3.log
"$PY" rigor_xi1.py R2 > rigor_xi1_R2.log 2>&1
echo "$(date '+%H:%M:%S') ALL DONE" >> queue3.log
