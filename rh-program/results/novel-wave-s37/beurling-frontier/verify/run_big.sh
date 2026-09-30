#!/bin/bash
# Extension to X = 1e10 (Y = 2e10) for T_alpha (seeds 1-4) and greedy. Sequential; idempotent (skips finished files).
# Memory ~2.6 GB (prime bitset 1.25 GB + R-free bitset 1.25 GB). Waits for run_all.sh to finish first.
set -u
D="$(cd "$(dirname "$0")" && pwd)"
cd "$D"
log="$D/logs/run_big.log"
stamp() { date "+%Y-%m-%d %H:%M:%S"; }
while pgrep -f run_all.sh > /dev/null; do sleep 10; done
echo "[$(stamp)] start run_big" >> "$log"
for a in 0.60 0.75 0.90; do
  f="$D/data_big/bern_a${a}.csv"
  if [ ! -s "$f" ]; then
    echo "[$(stamp)] bern alpha=$a X=1e10 Y=2e10 seeds 1-4" >> "$log"
    /usr/bin/time -l ./thin bern "$a" 1e10 2e10 1 2 3 4 > "$f.part" 2>> "$log" && mv "$f.part" "$f"
    echo "[$(stamp)] done $f" >> "$log"
  fi
done
for a in 0.60 0.75 0.90; do
  f="$D/data_big/greedy_a${a}.csv"
  if [ ! -s "$f" ]; then
    echo "[$(stamp)] greedy alpha=$a X=1e10 Y=2e10" >> "$log"
    /usr/bin/time -l ./thin greedy "$a" 1e10 2e10 > "$f.part" 2>> "$log" && mv "$f.part" "$f"
    echo "[$(stamp)] done $f" >> "$log"
  fi
done
echo "[$(stamp)] all done" >> "$log"
