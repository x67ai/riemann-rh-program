#!/bin/bash
# Robustness of the S5 crossing: target offsets delta (different tie-breaks give different systems) at X = 1e8.
X=${1:-1e8}; cd "$(dirname "$0")"; mkdir -p logs/robust
for r in 0.8 0.95 1.05; do for d in -0.3 0.3 0.45; do
  ./pseudoN "$r" "$X" "r${r}d${d}" - "$d" > "logs/robust/S5_r${r}_d${d}_${X}.log"
done; done
python3 fit_bins.py logs/robust/S5_r*_${X}.log
