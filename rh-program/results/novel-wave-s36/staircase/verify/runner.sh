#!/bin/sh
# dynamic job runner: one job at a time from jobs.txt (first line popped atomically); log to runner.log
PY="/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math/df16ac7a-b541-4904-8ae5-51d2ec1d5445/scratchpad/venv-gmp/bin/python"
cd "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/novel-wave-s36/staircase/verify"
while pgrep -f "census.py|reverify.py|rigor_xi1.py|lobe_scan.py" > /dev/null; do sleep 10; done
while [ -s jobs.txt ]; do
  job=$(head -n 1 jobs.txt)
  tail -n +2 jobs.txt > jobs.tmp && mv jobs.tmp jobs.txt
  logname=$(echo "$job" | sed 's/\.py//; s/[ :]/_/g')
  echo "$(date '+%H:%M:%S') start $job" >> runner.log
  $PY $job > "run_$logname.log" 2>&1
  echo "$(date '+%H:%M:%S') done  $job (exit $?)" >> runner.log
done
echo "$(date '+%H:%M:%S') QUEUE EMPTY" >> runner.log
