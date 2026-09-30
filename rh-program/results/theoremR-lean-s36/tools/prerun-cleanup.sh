#!/bin/bash
# theoremR-lean-s36 pre-run cleanup (Session 36; the H4 CHECK-O cleanup.sh pattern): remove the comparator-layer artifacts of the topic ResidueRank
# in the build tree so that comparator builds Challenge.ResidueRank and Solution.ResidueRank itself (comparator README assumption 2).
# The program modules Zeta23.ResidueRank.* stay built (the untrusted side either way).  There is no ChallengeDeps module for this topic.
cd "$HOME/rh-lean-work/checker-clone-s33-h4" || exit 99
echo "== $(date) pre-run cleanup for topic ResidueRank in $(pwd)"
for d in lib/lean ir; do for m in Challenge/ResidueRank Solution/ResidueRank; do for f in .lake/build/$d/$m.*; do [ -e "$f" ] && { echo "$f"; rm -f "$f"; }; done; done; done
n=0; for d in lib/lean ir; do for m in Challenge/ResidueRank Solution/ResidueRank; do for f in .lake/build/$d/$m.*; do [ -e "$f" ] && n=$((n+1)); done; done; done
echo "remaining: $n"
echo "program modules still built:"; ls -1 .lake/build/lib/lean/Zeta23/ResidueRank/ | sed 's/^/  /'
