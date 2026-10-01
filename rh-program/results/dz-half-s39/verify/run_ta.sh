#!/bin/zsh
# run_ta.sh — the frontier's random surgery T_alpha near alpha = 1 (alpha = 0.90, 0.95), 5 seeds, X = 1e8.
cd "${0:A:h}"
X=1e8
waitload() { while [ $(ps -Ao pcpu,comm | awk '$1>50' | wc -l) -ge 4 ]; do sleep 30; done }
step() { waitload; echo "== $(date '+%H:%M:%S') $*"; "$@" | cut -c1-400; }
for A in 0.90 0.95; do for S in 1 2 3 4 5; do
  P=data/ctl_ta${A}_s${S}
  step python3 controls.py ta $A $S $X $P
  step ./dzcount $P.primes.f64 $X 1024 27 $P.i64
  step python3 analyze.py $P
done; done
echo "== $(date '+%H:%M:%S') done"
