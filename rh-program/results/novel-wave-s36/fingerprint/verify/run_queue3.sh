#!/bin/bash
cd "$(dirname "$0")"
until grep -q "QUEUE2 DONE" run_queue2.out 2>/dev/null; do sleep 10; done
echo "=== u5c_announce"
python3 u5c_announce.py 2>&1 | tail -60
echo "=== QUEUE3 DONE"
