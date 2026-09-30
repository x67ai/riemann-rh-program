#!/bin/bash
# conj-O-s38 task 3, second batch: the corrected feedback criterion (|e + rho_hat D|) at X = 1e9, and the one unbound plain-feedback
# design (alpha = 0.75, c = 1, K = 2: band never binds) extended to X = 1e10. Sequential, idempotent. Log: logs/run_t3.log
set -u
D="$(cd "$(dirname "$0")" && pwd)"; cd "$D"; log="$D/logs/run_t3.log"; stamp() { date "+%Y-%m-%d %H:%M:%S"; }
run() { local out="$1"; shift; if [ ! -s "$out" ]; then echo "[$(stamp)] $* > $(basename "$out")" >> "$log";
  /usr/bin/time -p "$@" > "$out.part" 2>> "$log" && mv "$out.part" "$out"; fi; }
for a in 0.60 0.75; do for K in 0.5 2; do
  run "data/feedback_a${a}_c1_K${K}_corr_1e9.csv" env RDUMP="rdump/feedback_a${a}_c1_K${K}_corr_1e9.bin" ./thin2 feedback $a 1e9 4e9 $K 1 corr
done; done
run "data_big/feedback_a0.75_c1_K2_1e10.csv" env RDUMP="rdump/feedback_a0.75_c1_K2_1e10.bin" ./thin2 feedback 0.75 1e10 2e10 2 1
for f in rdump/feedback_*corr_1e9.bin; do [ -e "$f" ] || continue; b=$(basename "$f" .bin); [ -s "rn/$b.csv" ] || ./rnums "$f" 1e9 > "rn/$b.csv"; done
[ -s rn/feedback_a0.75_c1_K2_1e10.csv ] || [ ! -e rdump/feedback_a0.75_c1_K2_1e10.bin ] || ./rnums rdump/feedback_a0.75_c1_K2_1e10.bin 1e10 > rn/feedback_a0.75_c1_K2_1e10.csv
echo "[$(stamp)] run_t3b all done" >> "$log"
