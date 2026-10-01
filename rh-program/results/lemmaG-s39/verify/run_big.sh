#!/bin/bash
# run_big.sh — lemmaG-s39 production runs at X = 1e10 (one heavy process at a time; waits while >= 4 processes are above 50% CPU)
cd "$(dirname "$0")"
LOG=logs/run_big.log
waitload() { while [ "$(ps -Ao pcpu | awk '$1>50' | wc -l)" -ge 4 ]; do echo "[$(date '+%F %T')] load high, waiting" >> $LOG; sleep 60; done; }
run() { name=$1; shift; waitload; echo "[$(date '+%F %T')] START $name: ./lg $*" >> $LOG
  LG_SUME=data/$name.sume /usr/bin/time -p ./lg "$@" > data/$name.csv 2> data/$name.rn; echo "[$(date '+%F %T')] END $name rc=$? $(tail -3 data/$name.rn | grep real)" >> $LOG
  head -1 data/$name.csv >> $LOG; }
run nsq2_1e10     nsq 2 1e10
run sq2_1e10      sq 2 1e10
run neck2_1e10    neck 2 1e10 22
run necksp2_1e10  neck 2 1e10 22 spread
run weyl075_1e10  weyl 0.75 1 1e10 4e10
run weyl060_1e10  weyl 0.6 1 1e10 4e10
run planted_1e10  planted 0.6 1 0.45 5 1 1e10 4e10
echo "[$(date '+%F %T')] ALL DONE (1e10 batch)" >> $LOG
