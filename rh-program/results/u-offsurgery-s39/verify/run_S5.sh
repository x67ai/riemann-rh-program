#!/bin/bash
# Driver for S5 (integer-greedy pseudo-N systems). Usage: bash run_S5.sh X
set -e
X=${1:-1e8}
BIG="/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math/a1ca2244-cf17-4f92-9355-9db717d0d6ae/scratchpad/big"
cd "$(dirname "$0")"
for pair in "1 one" "1.5 r1p5" "1.6180339887498949 phi" "2 two" "1.4142135623730951 sqrt2" "0.75 r0p75"; do
  set -- $pair
  /usr/bin/time -p ./pseudoN "$1" "$X" "$2" "$BIG" > "logs/S5_${2}_${X}.log" 2> "logs/S5_${2}_${X}.time"
  head -1 "logs/S5_${2}_${X}.log"; grep real "logs/S5_${2}_${X}.time"
done
