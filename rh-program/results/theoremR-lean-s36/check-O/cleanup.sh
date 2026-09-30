#!/bin/bash
# CHECK-O pre-run cleanup (checker, Session 36): the builder's tools/prerun-cleanup.sh with this comment line and the cd target changed to the clean clone.
# The program modules Zeta23.ResidueRank.* stay built (the untrusted side either way).  There is no ChallengeDeps module for this topic.
cd "$HOME/rh-lean-work/checker-clone-s36-residue" || exit 99
echo "== $(date) pre-run cleanup for topic ResidueRank in $(pwd)"
for d in lib/lean ir; do for m in Challenge/ResidueRank Solution/ResidueRank; do for f in .lake/build/$d/$m.*; do [ -e "$f" ] && { echo "$f"; rm -f "$f"; }; done; done; done
n=0; for d in lib/lean ir; do for m in Challenge/ResidueRank Solution/ResidueRank; do for f in .lake/build/$d/$m.*; do [ -e "$f" ] && n=$((n+1)); done; done; done
echo "remaining: $n"
echo "program modules still built:"; ls -1 .lake/build/lib/lean/Zeta23/ResidueRank/ | sed 's/^/  /'
