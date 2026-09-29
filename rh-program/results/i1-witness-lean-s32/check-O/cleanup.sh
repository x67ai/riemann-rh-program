#!/bin/bash
# CHECK-O pre-run cleanup (checker-written): remove the comparator-layer artifacts of one topic and of ChallengeDeps.I1Witness in the clean clone.
cd "$HOME/rh-lean-work/checker-clone-s32-i1" || exit 99
echo "== $(date) pre-run cleanup for topic $1 (and ChallengeDeps.I1Witness) in $(pwd)"
for d in lib/lean ir; do for m in ChallengeDeps/I1Witness Challenge/$1 Solution/$1; do for f in .lake/build/$d/$m.*; do [ -e "$f" ] && { echo "$f"; rm -f "$f"; }; done; done; done
n=0; for d in lib/lean ir; do for m in ChallengeDeps/I1Witness Challenge/$1 Solution/$1; do for f in .lake/build/$d/$m.*; do [ -e "$f" ] && n=$((n+1)); done; done; done
echo "remaining: $n"
