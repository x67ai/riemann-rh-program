#!/bin/bash
cd "$(dirname "$0")"
until grep -q "QUEUE3 DONE" run_queue3.out 2>/dev/null; do sleep 10; done
echo "=== u4b_primes (rerun)"
python3 u4b_primes.py 2>&1 | grep -v Warning | tail -20
echo "=== QUEUE4 DONE"
