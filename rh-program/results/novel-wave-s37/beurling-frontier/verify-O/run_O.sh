#!/bin/bash
# reader O: independent re-run at X = 1e8, Y = 4e8, seeds 1-8; three alphas in parallel (3 heavy processes), then controls.
D="$(cd "$(dirname "$0")" && pwd)"; cd "$D"
stamp() { date "+%Y-%m-%d %H:%M:%S"; }
echo "[$(stamp)] start run_O" >> logs/run_O.log
for a in 0.60 0.75 0.90; do
  ( /usr/bin/time -l python3 thin_O.py bern $a 1e8 4e8 1 2 3 4 5 6 7 8 > "data/bernO_a$a.csv.part" 2> "logs/bernO_a$a.err" \
    && mv "data/bernO_a$a.csv.part" "data/bernO_a$a.csv"; echo "[$(stamp)] done bern a=$a" >> logs/run_O.log ) &
done
wait
python3 thin_O.py none 0 1e8 1 0 > data/noneO.csv 2> logs/noneO.err
python3 thin_O.py fin 6 1e8 1 0 > data/finO_K6.csv 2> logs/finO.err
echo "[$(stamp)] all done" >> logs/run_O.log
