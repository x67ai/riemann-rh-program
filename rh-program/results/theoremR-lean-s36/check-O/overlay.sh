#!/bin/bash
# CHECK-O overlay (checker-written, Session 36): ONLY the three program modules and the four topic files of the unit, each
# cp then cmp-verified against rh-program/lean/. Nothing else (the modules import only Mathlib and each other).
RP="/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/lean"
C="$HOME/rh-lean-work/checker-clone-s36-residue"
cd "$C" || exit 99
echo "== overlay $(date)"
for f in Zeta23/ResidueRank/LogPrimes.lean Zeta23/ResidueRank/Pair.lean Zeta23/ResidueRank/GenusBound.lean \
         comparator/Challenge/ResidueRank.lean comparator/Solution/ResidueRank.lean \
         comparator/PrintAxioms/ResidueRank.lean comparator/config-residue-rank.json; do
  [ -e "$f" ] && echo "PRE-EXISTING in v1.0: $f"
  mkdir -p "$(dirname "$f")"; cp "$RP/$f" "$f" && cmp "$RP/$f" "$f" && echo "OK $f $(shasum -a 256 "$f" | cut -d' ' -f1)"
done
echo "== git status --short"
git status --short
echo "== imports of the seven files"
grep -n '^import' Zeta23/ResidueRank/*.lean comparator/Challenge/ResidueRank.lean comparator/Solution/ResidueRank.lean comparator/PrintAxioms/ResidueRank.lean
