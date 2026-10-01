#!/bin/bash
# run_family.sh -- route 2 at three more densities (0.75, 0.8, 1.1): a_n dumps to 10^8, argument-principle scans of F_X at X = 10^7
# on [0.70, 1.00] x [0.1, 100] (lines sigma = 0.70, 0.80, 0.90, 1.00), counts by zcount7.py.  One heavy process at a time, load-gated.
set -u
V="$(cd "$(dirname "$0")" && pwd)"; T=/private/tmp/rh-s40-local-greedy
gate(){ while [ "$(ps -Ao pcpu,comm | awk '$1>50' | wc -l)" -ge 4 ]; do sleep 10; done; }
for r in "3 4 r075" "4 5 r08" "11 10 r11"; do
  set -- $r
  gate; "$T/s7gen" "$1" "$2" 100000000 0 "${3}_1e8" "$T" 1 > "$V/logs/sweep/s7_v0_${3}_X100000000_dump.log"
  gate; SIGS="0.70 0.80 0.90 1.00" HS0=0.70 HS1=1.00 bash "$V/scan7b.sh" "$T/a_${3}_1e8.u16" 10000000 "$1" "$2" "$3" > /dev/null 2>&1
  SIGS="0.70 0.80 0.90 1.00" python3 "$V/zcount7.py" "$V/logs/zeros" "$3" 10000000 > "$V/logs/zeros/zcount_${3}_1e7.log" 2>&1
  echo "$(date +%H:%M:%S) family $3 done"
done
