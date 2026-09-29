/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it (through Solution.PairChannel).
-/
/-
comparator/PrintAxioms/PairChannel.lean — quick axiom audit of the PairChannel topic WITHOUT the comparator tool:
  lake build Solution.PairChannel && lake env lean comparator/PrintAxioms/PairChannel.lean
Every line must print '<name>' depends on axioms: [propext, Classical.choice, Quot.sound] (or a subset).
No sorryAx, no Lean.ofReduceBool (= no native_decide), no other axiom.  The comparator run (config-pair-channel.json)
is the stronger check: it also verifies that each statement coincides with the trusted one in Challenge/PairChannel.lean.
-/
import Solution.PairChannel

#print axioms W2_eq
#print axioms sum_W2_mul
#print axioms pairRow_eq_gridRowQ
#print axioms sum_W2_cosh
#print axioms prop45
#print axioms abar_sq_le
#print axioms floor_holds_integer
#print axioms floor_fails_anchor
