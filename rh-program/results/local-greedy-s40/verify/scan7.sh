#!/bin/bash
# scan7.sh -- argument-principle scan of F_X on [0.55, 1.10] x [0.1, 100]: vertical lines (dt = 0.025) at the sigmas below and
# horizontal segments (dsigma = 0.005) at t = 0.1, 10, 20, ..., 100.  Usage: bash scan7.sh a.u16 X num den label
set -u
V="$(cd "$(dirname "$0")" && pwd)"; T=/private/tmp/rh-s40-local-greedy; A=$1; X=$2; NUM=$3; DEN=$4; LAB=$5
O="$V/logs/zeros"; mkdir -p "$O"
for s in 0.55 0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95 1.00 1.10; do
  while [ "$(ps -Ao pcpu,comm | awk '$1>50' | wc -l)" -ge 4 ]; do sleep 20; done
  "$T/zline" "$A" "$X" "$NUM" "$DEN" v "$s" 0.1 100 0.025 > "$O/${LAB}_v${s}_X${X}.txt"
done
for t in 0.1 10 20 30 40 50 60 70 80 90 100; do
  "$T/zline" "$A" "$X" "$NUM" "$DEN" h "$t" 0.55 1.10 0.005 > "$O/${LAB}_h${t}_X${X}.txt"
done
echo "$(date '+%H:%M:%S') scan done $LAB X=$X"
