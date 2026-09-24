/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it (through Solution.Separation6b).
-/
/-
comparator/PrintAxioms/Separation6b.lean — quick axiom audit of the Separation6b topic WITHOUT the comparator tool:
  lake build Solution.Separation6b && lake env lean comparator/PrintAxioms/Separation6b.lean
The three lines must each print 'depends on axioms: [propext, Classical.choice, Quot.sound]'.  No sorryAx, no
Lean.ofReduceBool (= no native_decide), no other axiom.  The comparator run (config-separation6b.json) is the stronger
check: it also verifies that each statement coincides with the trusted one in Challenge/Separation6b.lean.
-/
import Solution.Separation6b

#print axioms separation_clause6_assembly_b
#print axioms separation_clause7_tight_pair
#print axioms rstar_of_21L
