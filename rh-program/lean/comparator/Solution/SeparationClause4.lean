/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it.
-/
/-
comparator/Solution/SeparationClause4.lean — the UNTRUSTED comparator solution module for the topic `SeparationClause4`:
the statement of Challenge/SeparationClause4.lean, byte-identical, PROVED by delegating to
Zeta23/Separation/Clause4.lean (`Zeta23.Separation.inWindowNoise_le`, stated there for any carrier and multiplicity
function with the local count; the fields of the trusted `Separation.SepConfig` are passed one by one).  The trusted
`Separation.{B, ft, gammaOf, ftest, BL, Hb1, HB3}` are character for character `Zeta23.Separation.{B, ftest, BL, Hb1,
HB3}`, `Zeta23.paperFT` and `Zeta23.gammaOf`, so the delegation typechecks by definitional unfolding in the kernel.  This
module never imports the challenge.  Nothing in this file is part of the trusted base: comparator re-checks that the
theorem below has exactly the statement of its Challenge namesake and uses only the permitted axioms.
-/
import ChallengeDeps.SepConfig
import Zeta23.Separation.Clause4

noncomputable section

/-- **Theorem M2, clause 4** (separation note §5): for Z ∈ 𝒞(C₁), t ≥ 3, L ≥ 50, R ≥ 1,
0 ≤ N_Z ≤ 2·b₁·C₁·log(4 + t + R)/L² with b₁ = 87/10 — modulo the displayed H-b₁ and H-B‴. -/
theorem separation_clause4_in_window_noise (C₁ t L R : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hL : 50 ≤ L) (hR : 1 ≤ R)
    (Z : Separation.SepConfig C₁) (hb1 : Separation.Hb1) (hB3 : Separation.HB3) :
    0 ≤ Z.inWindowNoise t L R ∧
      Z.inWindowNoise t L R ≤ 2 * (87 / 10) * C₁ * Real.log (4 + t + R) / L ^ 2 :=
  Zeta23.Separation.inWindowNoise_le Z.carrier Z.mult Z.finite_window Z.localCount hC ht hL hR hb1 hB3
