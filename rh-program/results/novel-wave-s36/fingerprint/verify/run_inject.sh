#!/bin/bash
# visibility grid: one off-line quadruple (T, delta) injected into zeta's zero set; chunks < 10 min each
cd "$(dirname "$0")"
python3 u5_inject.py zeta 24000 1000 30,0.3 30,0.03 30,0.003 60,0.3 60,0.03 60,0.003 > run_inject_1.out 2>&1
python3 u5_inject.py zeta 24000 1000 100,0.3 100,0.1 100,0.03 100,0.01 100,0.003 100,0.001 > run_inject_2.out 2>&1
python3 u5_inject.py zeta 24000 1000 200,0.3 200,0.03 200,0.003 300,0.3 300,0.03 > run_inject_3.out 2>&1
echo "INJECT DONE" >> run_inject_3.out
