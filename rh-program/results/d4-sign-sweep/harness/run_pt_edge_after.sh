#!/bin/zsh
# run_pt_edge_after.sh -- waits for the (1e12, 28.35) rehearsal job (pid 18700) to exit, then runs the PT-edge point
# t = 3000175332900 (the double 3000175332900.0), L = 28.35, end to end through d4_point.py (8 threads, one heavy job at a time).
cd "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/d4-sign-sweep"
while kill -0 18700 2>/dev/null; do sleep 30; done
echo "=== (1e12, 28.35) finished; PT-edge point starting $(date) ==="
python3 harness/d4_point.py --t 3000175332900 --L 28.35 --threads 8 --tier rehearsal --label "PT-edge point"
echo "=== PT-edge point done $(date) ==="
