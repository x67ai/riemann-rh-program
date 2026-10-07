#!/bin/zsh
CODE="$(cd "$(dirname "$0")" && pwd)"
RUNS="$CODE/../runs"
cd "$CODE" || exit 1
/usr/bin/python3 followup_run.py t2resume >> "$RUNS/followup_t2n64.log" 2>&1
echo "t2resume exit: $?" >> "$RUNS/followup_chain.log"
/usr/bin/python3 followup_run.py t2n128 >> "$RUNS/followup_t2n128.log" 2>&1
echo "t2n128 exit: $?" >> "$RUNS/followup_chain.log"
/usr/bin/python3 followup_run.py p1 >> "$RUNS/followup_p1.log" 2>&1
echo "p1 exit: $?" >> "$RUNS/followup_chain.log"
echo "CHAIN DONE" >> "$RUNS/followup_chain.log"
