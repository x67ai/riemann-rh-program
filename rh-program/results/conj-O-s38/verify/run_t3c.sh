#!/bin/bash
# conj-O-s38 task 3, third batch: the corrected-sign feedback design (minimise |e - rho_hat D|) at alpha = 0.75, c = 1, K = 2 and 0.5,
# extended to X = 1e10 (at 1e9 it fell below the greedy calibration). Sequential, idempotent. Log: logs/run_t3.log
set -u
D="$(cd "$(dirname "$0")" && pwd)"; cd "$D"; log="$D/logs/run_t3.log"; stamp() { date "+%Y-%m-%d %H:%M:%S"; }
run() { local out="$1"; shift; if [ ! -s "$out" ]; then echo "[$(stamp)] $* > $(basename "$out")" >> "$log";
  /usr/bin/time -p "$@" > "$out.part" 2>> "$log" && mv "$out.part" "$out"; fi; }
for K in 2 0.5; do
  run "data_big/feedback_a0.75_c1_K${K}_corr_1e10.csv" env RDUMP="rdump/feedback_a0.75_c1_K${K}_corr_1e10.bin" ./thin2 feedback 0.75 1e10 2e10 $K 1 corr
  [ -s "rn/feedback_a0.75_c1_K${K}_corr_1e10.csv" ] || ./rnums "rdump/feedback_a0.75_c1_K${K}_corr_1e10.bin" 1e10 > "rn/feedback_a0.75_c1_K${K}_corr_1e10.csv"
done
echo "[$(stamp)] run_t3c all done" >> "$log"
