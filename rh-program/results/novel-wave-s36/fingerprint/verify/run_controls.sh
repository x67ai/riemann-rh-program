#!/bin/bash
# Unit 5 controls, run sequentially (one CPU-heavy process at a time).  Each line < 10 min.
cd "$(dirname "$0")"
run() { echo "=== $*"; python3 u2_prod.py "$@" 2>&1 | grep -E "FUNC|first|certified digits:|not certified|verified digits|lambda_1 =|Lambda\(1/2\)|saved|Error|Traceback"; }
run faq:3:2 real 4000 150
run faq:2.9:2 real 4000 150
run faq:4.5:5 real 4000 150
run eul:2 real 3000 60
run eul:3 real 3000 60
run eul:7 real 3000 60
run eul:1000000007 real 3000 60
run faq:2:2 real 16000 600
run chi4 real 16000 600
run dh real 16000 600
echo "=== CONTROLS DONE"
