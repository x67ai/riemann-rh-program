#!/bin/sh
# U4-sparse: Poisson-model maxima for the large runs (sequential).
V="$(cd "$(dirname "$0")" && pwd)"; cd "$V/logs" || exit 1
for f in r32_m0_5e9 r128_m0_5e10 r256_m0_1e11 r192_m0_1e11 r96_m0_3e10; do
  while [ "$(ps -Ao pcpu,comm | awk '$1>50' | wc -l)" -ge 4 ]; do sleep 30; done
  python3 ../sim_pq.py $f.tsv 8 10 1 > sim_pq_$f.log 2>&1
done
echo ALLDONE > sim.done
