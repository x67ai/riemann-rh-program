#!/bin/bash
# CHECK-O overlay (checker-written, Session 33): the unit's seven files, the Zeta23 import closure of PairCert that v1.0 lacks
# (GridParseval, GridCorner, GridParsevalRat — earlier checked units), ChallengeDeps/IntegralityGap.lean (for the 7/7 diff only),
# and the root Zeta23.lean as every prior overlay copied it. Nothing else.
RP="/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/lean"
C="$HOME/rh-lean-work/checker-clone-s33-h4"
cd "$C" || exit 99
echo "== overlay $(date)"
for f in Zeta23/PairCeiling/PairRow.lean Zeta23/PairCeiling/PairCert.lean \
         Zeta23/PairCeiling/GridParseval.lean Zeta23/PairCeiling/GridCorner.lean Zeta23/PairCeiling/GridParsevalRat.lean \
         comparator/ChallengeDeps/PairChannel.lean comparator/Challenge/PairChannel.lean comparator/Solution/PairChannel.lean \
         comparator/PrintAxioms/PairChannel.lean comparator/config-pair-channel.json comparator/ChallengeDeps/IntegralityGap.lean \
         Zeta23.lean; do
  mkdir -p "$(dirname "$f")"; cp "$RP/$f" "$f" && cmp "$RP/$f" "$f" && echo "OK $f $(shasum -a 256 "$f" | cut -c1-16)"
done
git status --short
