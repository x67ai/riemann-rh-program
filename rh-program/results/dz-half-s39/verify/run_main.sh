#!/bin/zsh
# run_main.sh — the finite rung of dz-half-s39: DZ construction (templates R = Thm 17.11, C = Thm 17.14), 5 seeds, X = 1e8;
# controls: rational primes, P_det, T1 (5 seeds). Sequential (one heavy process at a time); waits while >= 4 heavy
# processes run on the machine. Each step < 2 min at X = 1e8.
cd "${0:A:h}"
X=1e8
waitload() { while [ $(ps -Ao pcpu,comm | awk '$1>50' | wc -l) -ge 4 ]; do sleep 30; done }
step() { waitload; echo "== $(date '+%H:%M:%S') $*"; "$@" | cut -c1-400; }
for T in R C; do for S in 1 2 3 4 5; do
  P=data/dz_${T}_s${S}
  step python3 dzgen.py $T $S $X $P
  step ./dzcount $P.primes.f64 $X 1024 27 $P.i64
  step python3 analyze.py $P
done; done
step python3 controls.py primes $X data/ctl_primes
step ./dzcount data/ctl_primes.primes.f64 $X 1024 27 data/ctl_primes.i64
step python3 analyze.py data/ctl_primes
step python3 controls.py det $X data/ctl_det
step ./dzcount data/ctl_det.primes.f64 $X 1024 27 data/ctl_det.i64
step python3 analyze.py data/ctl_det
for S in 1 2 3 4 5; do
  P=data/ctl_t1_s${S}
  step python3 controls.py t1 $S $X $P
  step ./dzcount $P.primes.f64 $X 1024 27 $P.i64
  step python3 analyze.py $P
done
echo "== $(date '+%H:%M:%S') done"
