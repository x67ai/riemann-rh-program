#!/bin/bash
cd "$(dirname "$0")"
run() { echo "=== $*"; python3 u2_prod.py "$@" 2>&1 | grep -E "FUNC|lambda_1 =|not certified|verified digits|>= 1|saved|Error|Traceback"; }
run chi4 circle 16000 600 20000
run dh circle 24000 1000 30000
echo "=== CONTROLS3 DONE"
