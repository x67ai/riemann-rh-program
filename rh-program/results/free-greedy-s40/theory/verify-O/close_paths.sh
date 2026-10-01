#!/bin/sh
# For each run: list decisions with relative margin < 1e-12, re-run with those values flagged so that the
# generator prints each one's factorization (lattice indices n_k of its g-prime factors); then mp_recheck.py
# recomputes every such decision at 60 significant digits.
cd "$(dirname "$0")" || exit 1
for spec in pi16:1e7 pi4:1e7 pi32:1e8; do
  R=${spec%%:*}; X=${spec#*:}
  sh run_s8dd.sh "$R" "$X" 0 0 > /dev/null
  F="s8dd_${R}_${X}.close.txt"
  awk '{split($3,a,"="); print a[2], $4}' "$F" > "flag_${R}_${X}.txt"
  S8DD_FLAG="$PWD/flag_${R}_${X}.txt" sh run_s8dd.sh "$R" "$X" 0 0 > /dev/null
  grep "^PATH" "s8dd_${R}_${X}.log" > "path_${R}_${X}.txt"
  echo "$R $X: $(wc -l < "$F") close decisions, $(wc -l < "path_${R}_${X}.txt") factorizations"
done
