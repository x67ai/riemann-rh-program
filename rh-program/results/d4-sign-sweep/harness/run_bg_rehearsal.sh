#!/bin/zsh
# run_bg_rehearsal.sh -- D4 rehearsal: (1e12, 20) then (1e12, 28.35), 8 threads, one at a time, in the background (nohup).
B="/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/d4-sign-sweep/harness/d4_twisted_sum"
cd "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/d4-sign-sweep"
echo "=== zeta t1e12 L20 $(date) ==="
/usr/bin/time -l "$B" --mode zeta --t 1000000000000 --L 20 --threads 8 --selftest 1000 --seed 20260925 --out out/zeta_t1000000000000_L20.json
echo "=== zeta t1e12 L28.35 $(date) ==="
/usr/bin/time -l "$B" --mode zeta --t 1000000000000 --L 28.35 --threads 8 --selftest 1000 --seed 20260925 --out out/zeta_t1000000000000_L28.35.json
echo "=== done $(date) ==="
