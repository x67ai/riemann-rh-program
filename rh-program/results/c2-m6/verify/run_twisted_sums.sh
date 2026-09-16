#!/bin/zsh
# run_twisted_sums.sh -- the five heavy twisted sums, ONE AT A TIME (heavy jobs <= 4; this is one), 8 threads each.
# Binary built from twisted_sum.rs:  rustc -O -C target-cpu=native -o $BIN twisted_sum.rs
BIN="/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math-riemann/f0642f49-dab5-4c05-a061-651fcb3ec7a7/scratchpad/twisted_sum"
cd "$(dirname "$0")"
export PATH="$HOME/.cargo/bin:$PATH"
date
T85="85.69934848537759"
for spec in "zeta $T85 20 zeta_t85p7_L20" "zeta 1000000 10 zeta_t1e6_L10" "zeta 1000000 20 zeta_t1e6_L20" "dh $T85 10 dh_t85p7_L10" "dh $T85 20 dh_t85p7_L20"; do
  set -- ${=spec}
  echo "=== $4 ===  $(date)"
  /usr/bin/time -l "$BIN" --mode $1 --t $2 --L $3 --threads 8 --out "out/$4.json" 2>&1
  echo "=== done $4  $(date)"
done
echo "ALL DONE $(date)"
