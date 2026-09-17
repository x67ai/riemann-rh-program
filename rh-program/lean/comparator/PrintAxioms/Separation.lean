/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it (through Solution.Separation).
-/
/-
comparator/PrintAxioms/Separation.lean — quick axiom audit of the Separation topic WITHOUT the comparator tool:
  lake build Solution.Separation && lake env lean comparator/PrintAxioms/Separation.lean
Every line must print exactly '<name>' depends on axioms: [propext, Classical.choice, Quot.sound].
No sorryAx, no Lean.ofReduceBool (= no native_decide), no other axiom.  The comparator run (config-separation.json) is the
stronger check: it also verifies that these statements coincide with the trusted ones in Challenge/Separation.lean.
-/
import Solution.Separation

#print axioms separation_bump_fourier_decay
#print axioms separation_bump_fourier_decay_complex
#print axioms separation_bump_fourier_decay_pure_exp
