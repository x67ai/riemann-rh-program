#!/bin/bash
# variants at 1e9: thresholds 1/4, 3/4; early placement delta = t/8, t/4 (proportional) and 1/2 (absolute); both densities
cd /private/tmp/rh-s41-lemmaB-U7-patterns
for D in 16 32; do
  C=$(python3 consts.py $D)
  for spec in "tq 0.25 0 0" "t3q 0.75 0 0" "d8 0.5 0.125 0" "d4 0.5 0.25 0" "dh 0.5 0 0.5"; do
    set -- $spec; tag=v${D}_$1_1e9
    /usr/bin/time -l ./s8gen2 $C $2 $3 $4 1e9 $tag 2>$tag.err > $tag.log
  done
done
echo done > run_variants.done
