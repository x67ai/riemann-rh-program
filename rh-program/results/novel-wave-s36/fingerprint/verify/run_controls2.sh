#!/bin/bash
# Unit 5 controls, circle side (Li coefficients and Verblunsky), sequential.
cd "$(dirname "$0")"
run() { echo "=== $*"; python3 u2_prod.py "$@" 2>&1 | grep -E "FUNC|lambda_1 =|not certified|verified digits|>= 1|saved|Error|Traceback"; }
run eul:2 circle 3000 60 4000
run faq:3:2 circle 4000 150 5400
run chi4 circle 16000 600 20000
run dh circle 24000 1000 30000
echo "=== CONTROLS2 DONE"
