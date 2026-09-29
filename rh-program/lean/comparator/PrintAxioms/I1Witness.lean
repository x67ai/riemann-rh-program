/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: its imports are Mathlib-only.
-/
/-
comparator/PrintAxioms/I1Witness.lean — quick axiom audit of the I1Witness topic WITHOUT the comparator tool:
  lake build Solution.I1Witness && lake env lean comparator/PrintAxioms/I1Witness.lean
Each of the fourteen lines must print '<name>' depends on axioms: [propext, Classical.choice, Quot.sound] (or a subset).
No sorryAx, no Lean.ofReduceBool (= no native_decide), no other axiom.  The comparator run (config-i1-witness.json) is the
stronger check: it also verifies that each statement coincides with the trusted one in Challenge/I1Witness.lean.
-/
import Solution.I1Witness

#print axioms lambdaVec_rec
#print axioms lambdaVec_one
#print axioms lambdaVec_eq_zero_of_not_dvd
#print axioms epsteinB_one
#print axioms epstein_thirtysix_coeff
#print axioms epstein_witness_36
#print axioms kappa_pos
#print axioms dhA_one
#print axioms dh_three_coeff
#print axioms dh_witness_3
#print axioms dh_twelve_coeff
#print axioms dh_witness_12
#print axioms dh_four
#print axioms dh_six
