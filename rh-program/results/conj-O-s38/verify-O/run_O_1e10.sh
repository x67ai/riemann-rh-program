#!/bin/bash
# Reader-O: 8 new seeds (1002-1009) of T_0.75 at X = 1e10, Y = 2e10 with thin_O.py (own numpy code, own RNG). Sequential,
# one process per seed (each ~2-3 min, ~2.2 GB), idempotent. Waits while >= 4 heavy processes run. Log: logs/run_O_1e10.log
set -u
D="$(cd "$(dirname "$0")" && pwd)"; cd "$D"; log="$D/logs/run_O_1e10.log"
for s in 1002 1003 1004 1005 1006 1007 1008 1009; do
  f="data/bern_O_a0.75_s${s}_1e10"
  [ -s "${f}_dec.csv" ] && continue
  while [ "$(ps -Ao pcpu,comm | awk '$1>50' | wc -l)" -ge 4 ]; do sleep 30; done
  echo "[$(date '+%F %T')] seed $s start" >> "$log"
  /usr/bin/time -l python3 thin_O.py 0.75 1e10 2e10 "$s" "$f" >> "$log" 2>&1
  rm -f "${f}_Rprimes.npy"
  echo "[$(date '+%F %T')] seed $s done" >> "$log"
done
echo "[$(date '+%F %T')] all done" >> "$log"
