#!/bin/sh
# U4-sparse: extra values of rho for the scaling comparison (sequential, one heavy process at a time).
S=/private/tmp/rh-s41-lemmaB-U4-sparse; V="$(cd "$(dirname "$0")" && pwd)"
cd "$S" || exit 1
run(){ D=$1; X=$2; M=$3; tag=r${D}_m${M}_${X}
  while [ "$(ps -Ao pcpu,comm | awk '$1>50' | wc -l)" -ge 4 ]; do sleep 30; done
  /usr/bin/time -l ./s8sp $D $X $M $tag.tsv 2> $tag.err
  cp $tag.tsv "$V/logs/"; tail -1 $tag.err > "$V/logs/$tag.err"; grep -E 'real|maximum resident' $tag.err >> "$V/logs/$tag.err"
  date '+%H:%M IST %Y-%m-%d' >> "$V/logs/$tag.err"; }
run 256 1e11 0
run 192 1e11 0
run 96 3e10 0
run 48 1e10 0
run 24 5e9 0
run 16 4e9 0
run 128 1e10 1
run 64 1e10 1
echo ALLDONE > "$V/logs/run_extra.done"
