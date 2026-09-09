/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it (through Solution.DBN).
-/
/-
comparator/PrintAxioms/DBN.lean — quick axiom audit of the DBN topic WITHOUT the comparator tool:
  lake build Solution.DBN && lake env lean comparator/PrintAxioms/DBN.lean
Every line must print exactly '<name>' depends on axioms: [propext, Classical.choice, Quot.sound] (the three ray
statements) or a subset of it (the four kernel facts (K) are integer facts on literals; [propext] or fewer).
No sorryAx, no Lean.ofReduceBool (= no native_decide), no other axiom.  The comparator run (config-dbn.json) is the
stronger check: it also verifies that these statements coincide with the trusted ones in Challenge/DBN.lean.
Label (SPEC §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3" — never "fully machine-checked".
-/
import Solution.DBN

#print axioms dbn_ray_le_point2_of_certificates
#print axioms dbn_ray_le_point2_mp
#print axioms dbn_ray_le_point2_arb
#print axioms dbn_row2BarrierMP_checked
#print axioms dbn_row2BarrierARB_checked
#print axioms dbn_row2AsymMP_checked
#print axioms dbn_row2AsymARB_checked
