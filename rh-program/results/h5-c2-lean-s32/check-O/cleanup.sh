#!/bin/bash
# CHECK-O pre-run cleanup: remove every comparator-layer build artifact of the two H5 topics and of ChallengeDeps.WeilContainment
# from the clean clone, so that comparator builds each comparator-layer module itself.  usage: cleanup.sh <label>
cd "$HOME/rh-lean-work/checker-clone-s32-h5" || exit 99
echo "== $(date) pre-run cleanup [$1]"
for p in Challenge/WeilContainmentC2One Challenge/WeilContainmentC2 Solution/WeilContainmentC2One Solution/WeilContainmentC2 ChallengeDeps/WeilContainment PrintAxioms/WeilContainmentC2One PrintAxioms/WeilContainmentC2; do
  for f in .lake/build/lib/lean/$p.* .lake/build/ir/$p.*; do [ -e "$f" ] && { echo "$f"; rm -f "$f"; }; done
done
n=0; for p in Challenge/WeilContainmentC2One Challenge/WeilContainmentC2 Solution/WeilContainmentC2One Solution/WeilContainmentC2 ChallengeDeps/WeilContainment; do
  for f in .lake/build/lib/lean/$p.* .lake/build/ir/$p.*; do [ -e "$f" ] && n=$((n+1)); done; done
echo "remaining: $n"
