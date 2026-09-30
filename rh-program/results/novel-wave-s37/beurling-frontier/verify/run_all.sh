#!/bin/bash
# Driver for the M1b simulations. Sequential (one CPU-heavy process at a time). Paths contain spaces: all quoted.
set -u
D="$(cd "$(dirname "$0")" && pwd)"
cd "$D"
log="$D/logs/run_all.log"
stamp() { date "+%Y-%m-%d %H:%M:%S"; }
echo "[$(stamp)] start run_all (host $(hostname -s))" >> "$log"
for a in 0.60 0.75 0.90; do
  f="$D/data/bern_a${a}.csv"
  if [ ! -s "$f" ]; then
    echo "[$(stamp)] bern alpha=$a X=1e9 Y=4e9 seeds 1-8" >> "$log"
    /usr/bin/time -p ./thin bern "$a" 1e9 4e9 1 2 3 4 5 6 7 8 > "$f.part" 2>> "$log" && mv "$f.part" "$f"
    echo "[$(stamp)] done $f ($(grep -c . "$f") lines)" >> "$log"
  fi
done
for a in 0.60 0.75 0.90; do
  f="$D/data/greedy_a${a}.csv"
  if [ ! -s "$f" ]; then
    echo "[$(stamp)] greedy alpha=$a X=1e9 Y=4e9" >> "$log"
    /usr/bin/time -p ./thin greedy "$a" 1e9 4e9 > "$f.part" 2>> "$log" && mv "$f.part" "$f"
    echo "[$(stamp)] done $f" >> "$log"
  fi
done
f="$D/data/none.csv"
if [ ! -s "$f" ]; then
  echo "[$(stamp)] none X=1e9" >> "$log"
  /usr/bin/time -p ./thin none 1e9 > "$f.part" 2>> "$log" && mv "$f.part" "$f"
fi
for s in 1 2 3 4; do
  f="$D/data/cramer_s${s}.csv"
  if [ ! -s "$f" ]; then
    echo "[$(stamp)] cramer X=2e8 Y=2e9 seed=$s" >> "$log"
    /usr/bin/time -p ./thin_aux cramer 2e8 2e9 "$s" > "$f.part" 2>> "$log" && mv "$f.part" "$f"
  fi
done
z06=3.105547277977581011; z075=4.5951118258429435315; z09=10.584448464950801494
for pair in "0.60 $z06" "0.75 $z075" "0.90 $z09"; do
  set -- $pair
  f="$D/data/mean_a$1.csv"
  if [ ! -s "$f" ]; then
    echo "[$(stamp)] mean alpha=$1 X=2e8 zeta(2-alpha)=$2" >> "$log"
    /usr/bin/time -p ./thin_aux mean "$1" 2e8 "$2" > "$f.part" 2>> "$log" && mv "$f.part" "$f"
  fi
done
echo "[$(stamp)] all done" >> "$log"
