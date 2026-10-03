#!/bin/zsh
# after queue1: checks for k = 1..3, Q2, then k = 4, 5 and their checks (one heavy process at a time)
cd "$(dirname "$0")"
while [ ! -f ../data/queue1.done ]; do sleep 30; done
python3 checks.py 1 0,3,8,14 > ../data/k1-checks.log 2>&1
python3 checks.py 2 auto > ../data/k2-checks.log 2>&1
python3 checks.py 3 auto > ../data/k3-checks.log 2>&1
python3 realaxis.py 1 98.55 0.05 0.01 60 > ../data/q3-k1-dps60.log 2>&1
python3 realaxis.py 3 199.08 0.025 0.005 > ../data/q3-k3-half.log 2>&1
echo QUEUE2A-DONE > ../data/queue2a.done
./q2_run.sh
./run_k.sh 4 70 0.1
python3 checks.py 4 auto > ../data/k4-checks.log 2>&1
./run_k.sh 5 80 0.1
python3 checks.py 5 auto > ../data/k5-checks.log 2>&1
echo QUEUE2-DONE > ../data/queue2.done
