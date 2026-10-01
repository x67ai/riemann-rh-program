#!/bin/bash
# run_all.sh — lemmaG-s39 production runs at X = 1e9 (one heavy process at a time; waits while >= 4 processes are above 50% CPU)
cd "$(dirname "$0")"
LOG=logs/run_all.log
waitload() { while [ "$(ps -Ao pcpu | awk '$1>50' | wc -l)" -ge 4 ]; do echo "[$(date '+%F %T')] load high, waiting" >> $LOG; sleep 60; done; }
run() { name=$1; shift; waitload; echo "[$(date '+%F %T')] START $name: ./lg $*" >> $LOG
  /usr/bin/time -p ./lg "$@" > data/$name.csv 2> data/$name.rn; echo "[$(date '+%F %T')] END $name rc=$? $(tail -3 data/$name.rn | grep real)" >> $LOG
  head -1 data/$name.csv >> $LOG; }
run sq2_1e9      sq 2 1e9
run nsq2_1e9     nsq 2 1e9
run weyl060_1e9  weyl 0.6 1 1e9 4e9
run weyl075_1e9  weyl 0.75 1 1e9 4e9
run neck2_1e9    neck 2 1e9 22
run necksp2_1e9  neck 2 1e9 20 spread
run planted_1e9  planted 0.6 1 0.45 5 1 1e9 4e9
echo "[$(date '+%F %T')] ALL DONE (1e9 batch)" >> $LOG
