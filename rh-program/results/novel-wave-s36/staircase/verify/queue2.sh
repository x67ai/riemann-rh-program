#!/bin/sh
PY="/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math/df16ac7a-b541-4904-8ae5-51d2ec1d5445/scratchpad/venv-gmp/bin/python"
cd "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/novel-wave-s36/staircase/verify"
while ! grep -q "ALL DONE" queue_controls.log 2>/dev/null; do sleep 30; done
for job in rouche_N7 taylor_chain natural_split; do
  echo "$(date '+%H:%M:%S') start $job" >> queue2.log
  "$PY" $job.py > $job.log 2>&1
  echo "$(date '+%H:%M:%S') done $job" >> queue2.log
done
echo "$(date '+%H:%M:%S') ALL DONE" >> queue2.log
