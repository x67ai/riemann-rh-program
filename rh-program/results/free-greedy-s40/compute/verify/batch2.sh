#!/bin/bash
# batch2.sh -- sequential (one heavy process at a time): windowed-generator validation, the rational-prime control,
# and the variants of task 4, all at X = 1e8.  Logs in verify/logs/.
set -uo pipefail
V="$(cd "$(dirname "$0")" && pwd)"
cd "$V"
echo "batch2 start $(date '+%H:%M:%S')"
S8BIN=s8win ./run_s8.sh pi4 rule 1e8 0.5 win_pi4_1e8
cmp <(grep '^S' logs/pi4_1e8.log | cut -d' ' -f1-22) <(grep '^S' logs/win_pi4_1e8.log | cut -d' ' -f1-22) && echo "s8win == s8gen on S rows (cols 1-21), pi/4, 1e8"
./run_s8.sh one sieve 1e8 0 ctrl_sieve_1e8
S8BIN=s8win ./run_s8.sh one sieve 1e8 0 win_ctrl_sieve_1e8
cmp <(grep '^S' logs/ctrl_sieve_1e8.log | cut -d' ' -f1-22) <(grep '^S' logs/win_ctrl_sieve_1e8.log | cut -d' ' -f1-22) && echo "s8win == s8gen on S rows, sieve control, 1e8"
for v in "eoverpi 0.5" "rsqrt2 0.5" "r0995 0.5" "r098 0.5" "r08 0.5" "pi4 0.25" "pi4 0.75"; do
  set -- $v
  tag="var_${1}_th${2}_1e8"
  S8BIN=s8win ./run_s8.sh "$1" rule 1e8 "$2" "$tag"
  echo "$tag: $(grep '^# done' logs/$tag.log | cut -c1-150)"
done
echo "batch2 end $(date '+%H:%M:%S')"
