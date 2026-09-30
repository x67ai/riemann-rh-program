#!/bin/bash
cd "$(dirname "$0")"
until grep -q "INJECT DONE" run_inject_3.out 2>/dev/null; do sleep 10; done
echo "=== dh circle 16000 600 20000 (rerun: the 24000-bit run returned non-finite lambda_n >= 2)"
python3 u2_prod.py dh circle 16000 600 20000 2>&1 | grep -E "FUNC|lambda_1 =|not certified|verified digits|>= 1|saved|Error|Traceback"
echo "=== u4b_primes"
python3 u4b_primes.py 2>&1 | tail -20
echo "=== QUEUE2 DONE"
