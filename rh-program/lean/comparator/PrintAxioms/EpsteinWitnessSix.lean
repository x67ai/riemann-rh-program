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
comparator/PrintAxioms/EpsteinWitnessSix.lean — quick axiom audit of the EpsteinWitnessSix topic WITHOUT the comparator tool:
  lake build Solution.EpsteinWitnessSix && lake env lean comparator/PrintAxioms/EpsteinWitnessSix.lean
Each line must print '<name>' depends on axioms: [propext, Classical.choice, Quot.sound] (or a subset).
No sorryAx, no Lean.ofReduceBool (= no native_decide), no other axiom.  The comparator run (config-epstein-witness-six.json)
is the stronger check: it also verifies that each statement coincides with the trusted one in Challenge/EpsteinWitnessSix.lean.
-/
import Solution.EpsteinWitnessSix

#print axioms epsteinB_one
#print axioms epstein_six_coeff
#print axioms epstein_witness_6
