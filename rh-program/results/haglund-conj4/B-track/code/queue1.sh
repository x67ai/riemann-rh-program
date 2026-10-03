#!/bin/zsh
# sequential queue (one heavy process at a time): wait for the k=1 pipeline, then k=2, k=3, then Q3 for k=6..12
cd "$(dirname "$0")"
while pgrep -f "run_k.sh 1 " > /dev/null; do sleep 20; done
./run_k.sh 2 45 0.1
./run_k.sh 3 60 0.1
for k in 6 7 8 9 10 11 12; do
  python3 realaxis.py $k $((4*(k+2)*(k+2)+40)) > ../data/q3-k$k.log 2>&1
done
echo QUEUE1-DONE > ../data/queue1.done
