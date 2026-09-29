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
comparator/PrintAxioms/WeilContainmentC2One.lean — quick axiom audit of the WeilContainmentC2One topic WITHOUT the comparator tool:
  lake build Solution.WeilContainmentC2One && lake env lean comparator/PrintAxioms/WeilContainmentC2One.lean
The line must print 'weilContainment_c2_interpolant_log3' depends on axioms: [propext, Classical.choice, Quot.sound] (or a subset).
No sorryAx, no Lean.ofReduceBool (= no native_decide), no other axiom.  The comparator run (config-weil-containment-c2-one.json)
is the stronger check: it also verifies that the statement coincides with the trusted one in Challenge/WeilContainmentC2One.lean.
-/
import Solution.WeilContainmentC2One

#print axioms weilContainment_c2_interpolant_log3
