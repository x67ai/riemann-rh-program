#!/bin/bash
# conj-O-s38 task 3: 8 extra seeds (5-12) of T_0.75 at X = 1e10, Y = 2e10 with the frontier NOTE's own C code
# (thin_fr.c = byte-identical copy of fr verify/thin.c, sha256 6d359b51...; cross-checked bin-for-bin at X = 1e9, seed 1).
# One seed per process so that each run stays well under 30 min; sequential; idempotent. Log: logs/run_seeds.log
set -u
D="$(cd "$(dirname "$0")" && pwd)"
cd "$D"
log="$D/logs/run_seeds.log"
stamp() { date "+%Y-%m-%d %H:%M:%S"; }
echo "[$(stamp)] start run_seeds" >> "$log"
for s in 5 6 7 8 9 10 11 12; do
  f="$D/data_big/bern_a0.75_s$s.csv"
  if [ ! -s "$f" ]; then
    echo "[$(stamp)] bern alpha=0.75 X=1e10 Y=2e10 seed $s" >> "$log"
    /usr/bin/time -l ./thin_fr bern 0.75 1e10 2e10 "$s" > "$f.part" 2>> "$log" && mv "$f.part" "$f"
    echo "[$(stamp)] done $f" >> "$log"
  fi
done
echo "[$(stamp)] all done" >> "$log"
