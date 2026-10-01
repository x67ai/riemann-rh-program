#!/bin/bash
# run_s8.sh RHONAME MODE X THETA TAG [resume]     (binary: $S8BIN in /private/tmp/rh-s40-free-greedy, default s8gen)
#   runs the generator; big outputs (moment snapshots, E histograms, checkpoints) go to /private/tmp/rh-s40-free-greedy/,
#   the text log (sample rows S, fine series F, records R, prototype rows P) to verify/logs/TAG.log
set -euo pipefail
V="$(cd "$(dirname "$0")" && pwd)"
S=/private/tmp/rh-s40-free-greedy
mkdir -p "$V/logs" "$S"
read -r RH RL TH TL < <(python3 "$V/params.py" "$1")
if [ "${6:-}" = "resume" ]; then
  "$S/${S8BIN:-s8gen}" "$2" "$3" "$4" "$RH" "$RL" "$TH" "$TL" "$S/$5" resume >> "$V/logs/$5.log" 2>> "$V/logs/$5.err"
else
  rm -f "$S/$5.hist"
  "$S/${S8BIN:-s8gen}" "$2" "$3" "$4" "$RH" "$RL" "$TH" "$TL" "$S/$5" > "$V/logs/$5.log" 2> "$V/logs/$5.err"
fi
