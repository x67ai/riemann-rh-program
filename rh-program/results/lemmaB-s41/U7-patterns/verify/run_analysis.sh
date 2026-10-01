#!/bin/bash
# stats + inherit on the variants (1e9) and inherit on the base runs (1e10)
cd /private/tmp/rh-s41-lemmaB-U7-patterns
for D in 16 32; do
  T=$(python3 -c "import math; print(repr($D/math.pi))"); R=$(python3 -c "import math; print(repr(math.pi/$D))")
  for spec in "tq 0.25 0" "t3q 0.75 0" "d8 0.5 0.125" "d4 0.5 0.25" "dh 0.5 h"; do
    set -- $spec; tag=v${D}_$1_1e9
    if [ "$3" = "h" ]; then DL=0.5; else DL=$(python3 -c "print(repr($3*$T))"); fi
    P1=$(python3 -c "print(repr(1+$2*$T-$DL))")
    ./stats $tag $T $R $2 $P1 1e9 50 > $tag.stats 2> $tag.stats.err
    ./inherit $tag $T $R $2 $DL 1e9 > $tag.inh 2> $tag.inh.err
  done
  ./inherit b${D}_1e10 $T $R 0.5 0 1e10 > b${D}_1e10.inh 2> b${D}_1e10.inh.err
done
echo done > run_analysis.done
