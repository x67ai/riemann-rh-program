/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and imports nothing from it beyond this unit's modules (through Solution.ResidueRank).
-/
/-
comparator/PrintAxioms/ResidueRank.lean — quick axiom audit of the ResidueRank topic WITHOUT the comparator tool:
  lake build Solution.ResidueRank && lake env lean comparator/PrintAxioms/ResidueRank.lean
Every line must print '<name>' depends on axioms: [propext, Classical.choice, Quot.sound] (or a subset).
No sorryAx, no Lean.ofReduceBool, no other axiom.  The comparator run (config-residue-rank.json) is the stronger check: it also
verifies that each statement coincides with the trusted one in Challenge/ResidueRank.lean.
-/
import Solution.ResidueRank

#print axioms ResidueRank.log_primes_linearIndependent
#print axioms ResidueRank.span_log_not_finite
#print axioms ResidueRank.rank_span_log_le
#print axioms ResidueRank.lemmaF_finite_fiber
#print axioms ResidueRank.lemmaF_infinite_order
#print axioms ResidueRank.theoremR
#print axioms ResidueRank.theoremS_bound
#print axioms ResidueRank.theoremS
