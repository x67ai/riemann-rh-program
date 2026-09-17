/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it (through Solution.SeparationClause4).
-/
/-
comparator/PrintAxioms/SeparationClause4.lean — quick axiom audit of the SeparationClause4 topic WITHOUT the comparator tool:
  lake build Solution.SeparationClause4 && lake env lean comparator/PrintAxioms/SeparationClause4.lean
The line must print exactly 'separation_clause4_in_window_noise' depends on axioms: [propext, Classical.choice, Quot.sound].
No sorryAx, no Lean.ofReduceBool (= no native_decide), no other axiom.  The comparator run (config-separation-clause4.json)
is the stronger check: it also verifies that the statement coincides with the trusted one in Challenge/SeparationClause4.lean.
-/
import Solution.SeparationClause4

#print axioms separation_clause4_in_window_noise
