#!/bin/bash
# CHECK-O pre-run cleanup (checker-written, Session 33): remove the comparator-layer artifacts of the topic PairChannel in the clean clone.
cd "$HOME/rh-lean-work/checker-clone-s33-h4" || exit 99
echo "== $(date) pre-run cleanup for topic PairChannel in $(pwd)"
for d in lib/lean ir; do for m in ChallengeDeps/PairChannel Challenge/PairChannel Solution/PairChannel; do for f in .lake/build/$d/$m.*; do [ -e "$f" ] && { echo "$f"; rm -f "$f"; }; done; done; done
n=0; for d in lib/lean ir; do for m in ChallengeDeps/PairChannel Challenge/PairChannel Solution/PairChannel; do for f in .lake/build/$d/$m.*; do [ -e "$f" ] && n=$((n+1)); done; done; done
echo "remaining: $n"
