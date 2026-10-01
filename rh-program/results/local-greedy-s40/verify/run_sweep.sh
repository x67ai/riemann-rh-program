#!/bin/bash
# run_sweep.sh -- S7(rho) sweep: s7gen at X for the brief's densities (variant $2, default 0); logs to verify/logs/sweep/.
# Usage: bash run_sweep.sh X [variant] [rho list as num/den ...]
set -u
V="$(cd "$(dirname "$0")" && pwd)"; T=/private/tmp/rh-s40-local-greedy; X=$1; VAR=${2:-0}; shift; shift || true
LIST=("$@"); [ ${#LIST[@]} -eq 0 ] && LIST=(3/5 3/4 4/5 9/10 11/10 5/4 3/2)
mkdir -p "$V/logs/sweep"
for r in "${LIST[@]}"; do
  num=${r%/*}; den=${r#*/}
  while [ "$(ps -Ao pcpu,comm | awk '$1>50' | wc -l)" -ge 4 ]; do sleep 20; done
  out="$V/logs/sweep/s7_v${VAR}_r${num}-${den}_X${X}.log"
  /usr/bin/time -l "$T/s7gen" "$num" "$den" "$X" "$VAR" "v${VAR}_r${num}-${den}" "$T" 0 > "$out" 2> "$out.time"
  echo "$(date '+%H:%M:%S') done rho=$r X=$X var=$VAR -> $(basename "$out")"
done
