#!/bin/bash
# run_gen.sh D d1 [d2 ...] — for X ~ 10^d: K = floor(rho (10^d - 1) + 1/2) (so x_K <= 10^d < x_{K+1}), certified
# constants (consts.py), generator run (s8gen), log to logs/gen_pi{D}_1e{d}.log, moments to the scratch directory
# (sha256 recorded in the log). Waits while 4 or more processes use > 50% CPU (compute policy).
HERE="$(cd "$(dirname "$0")" && pwd)"; S=/private/tmp/rh-s41-U6-second; G=$S/s8gen
cc -O2 -Wall -Wno-unused-function -o "$G" "$HERE/s8gen.c" -lm || exit 1
D=$1; shift
for d in "$@"; do
  while [ "$(ps -Ao pcpu,comm | awk '$1>50' | wc -l)" -ge 4 ]; do sleep 60; done
  K=$(python3 -c "from flint import arb; print(int((arb.pi()*(10**$d-1)/$D+arb(1)/2).floor().unique_fmpz()))")
  LOG="$HERE/logs/gen_pi${D}_1e${d}.log"
  {
    echo "# run_gen.sh D=$D d=$d K=$K start $(date '+%H:%M:%S IST %Y-%m-%d') host $(uname -m)"
    python3 "$HERE/consts.py" $D $K "$S/params_pi${D}_1e${d}.txt"
    /usr/bin/time -l "$G" "$S/params_pi${D}_1e${d}.txt" "$S/m_pi${D}_1e${d}" 27 2>&1 | grep -v '^\[' | grep -E -v '^ +[0-9]+ +(page|block|messages|signals|voluntary|involuntary|instructions|cycles|average|hard|swaps|elapsed)'
    shasum -a 256 "$S/m_pi${D}_1e${d}.blk" "$S/m_pi${D}_1e${d}.ind" "$S/params_pi${D}_1e${d}.txt" | sed "s#$S/##"
    echo "# end $(date '+%H:%M:%S IST %Y-%m-%d')"
  } > "$LOG" 2>&1
  grep -E 'FINAL|composites|wall|maximum resident' "$LOG"
done
