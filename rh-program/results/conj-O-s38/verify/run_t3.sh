#!/bin/bash
# conj-O-s38 task 3 driver (after run_seeds.sh). Sequential, one CPU-heavy process at a time, idempotent. Log: logs/run_t3.log
#  (1) rung 1: finite R = {2,...,13} and {3,5,7,11,13,17,19} to X = 1e8 (Prop. 5.1 must be reproduced by the dyadic code);
#  (2) greedy c = 2, alpha = 0.75 at X = 1e10 (only 1e9 on disk);
#  (3) R-prime dumps (<= 1e10) and R-number enumeration (rnums) for the designs analysed against the Franel diagonal;
#  (4) the new design: feedback deletion, alpha = 0.6, 0.75, c = 1, 2, band K = 0.5, 2, 8 at X = 1e9 (then the best at 1e10).
set -u
D="$(cd "$(dirname "$0")" && pwd)"; cd "$D"; log="$D/logs/run_t3.log"; stamp() { date "+%Y-%m-%d %H:%M:%S"; }
run() { local out="$1"; shift; if [ ! -s "$out" ]; then echo "[$(stamp)] $* > $(basename "$out")" >> "$log";
  /usr/bin/time -p "$@" > "$out.part" 2>> "$log" && mv "$out.part" "$out"; fi; }
echo "[$(stamp)] start run_t3" >> "$log"
run data/finite_2-13_1e8.csv ./thin2 finite 1e8 2 3 5 7 11 13
run data/finite_3-19_1e8.csv ./thin2 finite 1e8 3 5 7 11 13 17 19
run data_big/greedy_a0.75_c2.csv ./thin_fr greedy 0.75 1e10 2e10 2
mkdir -p rdump rn
dumpone() { local tag="$1"; shift; if [ ! -s "rn/$tag.csv" ]; then echo "[$(stamp)] dumpR $* ($tag)" >> "$log";
  RDUMP="rdump/$tag.bin" /usr/bin/time -p ./thin2 dumpR "$@" 2>> "$log" && /usr/bin/time -p ./rnums "rdump/$tag.bin" 1e10 > "rn/$tag.csv" 2>> "$log"; fi; }
dumpone greedy_a0.60_c1 greedy 0.60 1e10 1
dumpone greedy_a0.75_c1 greedy 0.75 1e10 1
dumpone greedy_a0.60_c2 greedy 0.60 1e10 2
dumpone greedy_a0.75_c2 greedy 0.75 1e10 2
for s in 1 2 3 4; do dumpone bern_a0.75_s$s bern 0.75 1e10 $s; dumpone bern_a0.60_s$s bern 0.60 1e10 $s; done
for a in 0.60 0.75; do for c in 1 2; do for K in 0.5 2 8; do
  run "data/feedback_a${a}_c${c}_K${K}_1e9.csv" env RDUMP="rdump/feedback_a${a}_c${c}_K${K}_1e9.bin" ./thin2 feedback $a 1e9 4e9 $K $c
done; done; done
echo "[$(stamp)] all done" >> "$log"
