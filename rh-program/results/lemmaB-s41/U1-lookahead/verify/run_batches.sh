#!/bin/bash
# U1-lookahead: all rule comparisons with the FIXED generators (boundary bug fixed this session, see SHARED.md; logs batch1-4 before the fix are in superseded/).
# Usage: bash run_batches.sh > batches_v2.log   (binaries go to $BIN, default /private/tmp/rh-s41-lemmaB-U1-lookahead)
set -u
V="$(cd "$(dirname "$0")" && pwd)"; BIN="${BIN:-/private/tmp/rh-s41-lemmaB-U1-lookahead}"; mkdir -p "$BIN"
clang++ -O2 -std=c++17 -o "$BIN/rules" "$V/rules.cpp" && clang++ -O2 -std=c++17 -o "$BIN/rules2" "$V/rules2.cpp" || exit 1
R16=0.19634954084936207; R32=0.09817477042468103
log() { echo "== $*"; }
{
log "A: greedy, thresholds, pi/16, X=1e7 and 1e8"
for X in 1e7 1e8; do for tau in 0.5 0.25 0.1 0.02; do "$BIN/rules2" $R16 $X greedy $tau | grep -E "^x=1e\+0[5-8]|EXC|L=4187|L=6250|RESULT"; done; done
log "B: deterministic early placement (W = offset), pi/16, X=1e7"
for w in 1 2.5 5 10 20 100; do "$BIN/rules" $R16 1e7 early 0.5 $w | grep RESULT; done
log "C: look-ahead anti-clustering (W K J H), pi/16, X=1e7"
for cfg in "5 6 3 2" "5 6 6 2" "5 11 6 5" "2.5 6 6 2" "10 11 6 5"; do set -- $cfg; "$BIN/rules" $R16 1e7 look 0.5 $1 $2 $3 $4 | grep RESULT; done
log "D: open-loop template (beatty lambda) and Poisson (lambda seed) + greedy feedback, pi/16, X=1e7 and 1e8"
for X in 1e7 1e8; do for cfg in "beatty 1.0 1" "beatty 0.97 1" "beatty 0.95 1" "beatty 0.9 1" "beatty 0.8 1" "poisson 1.0 1" "poisson 0.9 1" "poisson 0.9 2" "poisson 0.9 3"; do
  set -- $cfg; log "$X $cfg"; "$BIN/rules2" $R16 $X $1 0.5 $2 $3 | grep -E "^x=1e\+0[5-8]|EXC|L=4187|L=6250|RESULT"; done; done
log "E: greedy pi/32, X=1e8"
"$BIN/rules2" $R32 1e8 greedy 0.5 | grep -E "^x=1e\+0[5-8]|EXC|LEMMA_M|RESULT"
} 2>&1
