#!/bin/bash
# Structured surgery with the leading prime-square branch point canceled (greedy, w_p = min(1, c p^(alpha-1)), c = 2, 6).
# Waits for run_big.sh; swaps in the rebuilt binary thin.new first. Sequential, idempotent.
set -u
D="$(cd "$(dirname "$0")" && pwd)"
cd "$D"
log="$D/logs/run_c2.log"
stamp() { date "+%Y-%m-%d %H:%M:%S"; }
while pgrep -f run_big.sh > /dev/null; do sleep 10; done
[ -x thin.new ] && mv thin.new thin
echo "[$(stamp)] start run_c2" >> "$log"
for spec in "0.60 2 1e9 4e9" "0.75 2 1e9 4e9" "0.90 2 1e9 4e9" "0.60 6 1e9 4e9" "0.75 6 1e9 4e9" "0.60 2 1e10 2e10" "0.60 6 1e10 2e10"; do
  set -- $spec
  dir="$D/data"; [ "$3" = "1e10" ] && dir="$D/data_big"
  f="$dir/greedy_a$1_c$2.csv"
  if [ ! -s "$f" ]; then
    echo "[$(stamp)] greedy alpha=$1 c=$2 X=$3 Y=$4" >> "$log"
    /usr/bin/time -p ./thin greedy "$1" "$3" "$4" "$2" > "$f.part" 2>> "$log" && mv "$f.part" "$f"
  fi
done
echo "[$(stamp)] all done" >> "$log"
