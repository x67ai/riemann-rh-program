#!/bin/sh
# U4-sparse production runs (sequential; one heavy process at a time). Scratch under /private/tmp/rh-s41-lemmaB-U4-sparse.
S=/private/tmp/rh-s41-lemmaB-U4-sparse; V="$(cd "$(dirname "$0")" && pwd)"
cd "$S" || exit 1
run(){ D=$1; X=$2; M=$3; W=$4; C=$5; tag=r${D}_m${M}_${X}
  while [ "$(ps -Ao pcpu,comm | awk '$1>50' | wc -l)" -ge 4 ]; do sleep 30; done
  /usr/bin/time -l ./s8sp $D $X $M $tag.tsv $W $C 2> $tag.err
  cp $tag.tsv "$V/logs/"; tail -1 $tag.err > "$V/logs/$tag.err"; grep -E 'real|maximum resident' $tag.err >> "$V/logs/$tag.err"
  date '+%H:%M IST %Y-%m-%d' >> "$V/logs/$tag.err"; }
# 1. lattice monoid (mode 1) with e-dumps, then S8 (mode 0) compared step by step: domination check e_k <= e_k^lat
for D in 128 64 32; do run $D 1e9 1 elat_${D}.u16 ""; run $D 1e9 0 - elat_${D}.u16; rm -f elat_${D}.u16; done
# 2. S8 at scale
run 128 5e10 0 - ""
run 64 2e10 0 - ""
run 32 5e9 0 - ""
echo ALLDONE > "$V/logs/run_main.done"
