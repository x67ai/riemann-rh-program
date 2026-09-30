#!/bin/bash
# S5 sweep over the density rho at fixed X (no dumps). Usage: bash run_S5_sweep.sh X
X=${1:-1e8}; cd "$(dirname "$0")"; mkdir -p logs/sweep
for r in 0.52 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 0.99 1.01 1.05 1.1 1.2 1.3 1.4 1.5 1.6180339887498949; do
  ./pseudoN "$r" "$X" "r$r" > "logs/sweep/S5_r${r}_${X}.log"
done
python3 fit_bins.py logs/sweep/S5_r*_${X}.log
