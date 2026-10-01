#!/bin/bash
cd /private/tmp/rh-s41-read-localgreedy
until [ -f boxes1e9.done ]; do sleep 2; done
until [ $(ps -Ao pcpu,comm | awk '$1>50' | wc -l) -lt 4 ]; do sleep 60; done
bash "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/local-greedy-s40/verify-O/run_dens.sh"
RHO_NUM=3 RHO_DEN=4 python3 "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/local-greedy-s40/verify-O/zo.py" g_r3-4_1e8.u16 1e8 "0.81+92.34j" "0.75+46.69j" "0.73+29.77j" "0.71+30.70j" > "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/local-greedy-s40/verify-O/logs/zeros_r3-4_X1e8.log" 2>&1
RHO_NUM=4 RHO_DEN=5 python3 "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/local-greedy-s40/verify-O/zo.py" g_r4-5_1e8.u16 1e8 "0.75+30.70j" "0.75+29.86j" "0.74+59.17j" > "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/local-greedy-s40/verify-O/logs/zeros_r4-5_X1e8.log" 2>&1
RHO_NUM=11 RHO_DEN=10 python3 "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/local-greedy-s40/verify-O/zo.py" g_r11-10_1e8.u16 1e8 "0.84+20.34j" "0.81+29.98j" > "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/local-greedy-s40/verify-O/logs/zeros_r11-10_X1e8.log" 2>&1
python3 "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/local-greedy-s40/verify-O/stripo.py" g_c0_1e9.u16 1e7 0.70 1.10 0.1 100 80 3996 > "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/local-greedy-s40/verify-O/logs/strip_r06_X1e7_070-110.log" 2>&1
echo finished > chain.done
