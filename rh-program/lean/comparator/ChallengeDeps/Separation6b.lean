/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: it imports Mathlib and the trusted
modules ChallengeDeps.Separation, ChallengeDeps.SepConfig, ChallengeDeps.Separation6 only.
-/
/-
comparator/ChallengeDeps/Separation6b.lean — the TRUSTED definition layer for the comparator topics `SeparationClause4b`
(clause 4 of Theorem M2 with b₁ PROVED) and `Separation6b` (the clause-6 assembly with b₁ proved, the clause-7 tight pair,
and "t ≥ 21L ⟹ (R*)"); Session 24 item 3, Unit A (rh-program/results/c2-m4/PRICING-RESIDUE.md §1 Pieces 2, 3 (3-sym), 6,
§2 row A; build record rh-program/results/c2-m4/BUILD-NOTES-A.md).  It IMPORTS the frozen trusted files of M4 (iii)
(ChallengeDeps/SepConfig.lean and ChallengeDeps/Separation6.lean, untouched — so `SepConfig`, `Wsummand`, `W`,
`inWindowNoise`, `ftest`, `HB3`, `orbit`, `edge`, `Hedge`, `Rstar`, `outWindow`, `Hout` are the SAME declarations the
M4 (iii) runs checked) and adds ONE definition:
  b1sym := (2·e^{−1}/Z)²        the noise constant b₁ of the note (§5) as a REAL NUMBER defined from Z = ∫ B_raw — the
                                hand-proved bound b₁ ≤ ‖B′‖₁² with ‖B′‖₁ = 2B(0) = 2e^{−1}/Z.  No digit: neither the
                                note's 8.70 (the displayed `Hb1` of M4 (iii), 87/10, which the new statements no longer
                                take) nor the computation's 10.984 appears.  The solution proves (|η|·‖B̂(η)‖)² ≤ b1sym
                                for every real η (Zeta23/Separation/B1Sym.lean), so H-b₁ is no longer displayed.
The displayed `Hb1` of SepConfig.lean stays defined there (frozen) and is consumed by no statement of this unit.
A reader who wants to know WHAT is claimed reads this file, ChallengeDeps/Separation.lean, ChallengeDeps/SepConfig.lean,
ChallengeDeps/Separation6.lean and the two challenge files only.
-/
import Mathlib
import ChallengeDeps.Separation6

namespace Separation

noncomputable section

/-- b₁ as the real number (2e^{−1}/Z)² = ‖B′‖₁² (separation note §5; no digit) — character for character
`Zeta23.Separation.b1sym`. -/
def b1sym : ℝ := (2 * Real.exp (-1) / Z) ^ 2

end

end Separation
