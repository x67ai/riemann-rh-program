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
comparator/Solution/Separation6.lean — the UNTRUSTED comparator solution module for the topic `Separation6`: the statement
of Challenge/Separation6.lean, byte-identical, PROVED by delegating to Zeta23/Separation/Assembly.lean
(`Zeta23.Separation.clause6_assembly`, stated there over raw data: the two carriers, multiplicity functions, local
finiteness and local counts are passed field by field from the trusted `Separation.SepConfig`).  The trusted
`Separation.{orbit, edge, Hedge, Rstar, ftest, Hb1, HB3, SepConfig.W, SepConfig.Wsummand, SepConfig.Hout, gammaOf, ft}`
are character for character `Zeta23.Separation.{orbit, edge, Hedge, Rstar, ftest, Hb1, HB3, wsum}`, `Zeta23.gammaOf`,
`Zeta23.paperFT`, so the delegation typechecks by definitional unfolding in the kernel.  This module never imports the
challenge.  Nothing in this file is part of the trusted base: comparator re-checks that the theorem below has exactly the
statement of its Challenge namesake and uses only the permitted axioms.
Label, binding: "kernel-checked modulo H-edge, H-b₁, H-B‴, H-out" — never "Theorem M2 is formalized".
-/
import ChallengeDeps.Separation6
import Zeta23.Separation.Assembly

noncomputable section

/-- **Theorem M2, clause 6** (separation note §7.1 with the addendum's hypotheses): for Z, Z′ ∈ 𝒞(C₁) as in the header,
‖W_Z(f_{t,L}) − W_{Z′}(f_{t,L})‖ ≥ δ²e^{δL/2} ≥ 1 — modulo the displayed H-b₁, H-B‴, H-edge, H-out. -/
theorem separation_clause6_assembly (C₁ t δ L : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
    (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * (87 / 10) * C₁)) ≤ L)
    (hRstar : Separation.Rstar t δ L)
    (Z Z' : Separation.SepConfig C₁)
    (hZorb : Separation.orbit t δ ⊆ Z.carrier) (hZmult : ∀ ρ ∈ Separation.orbit t δ, Z.mult ρ = 1)
    (hZ : ∀ ρ ∈ Z.carrier, |ρ.im - t| ≤ 73 * L → ρ ∉ Separation.orbit t δ → ρ.re = 1 / 2)
    (hZ' : ∀ ρ ∈ Z'.carrier, |ρ.im - t| ≤ 73 * L → ρ.re = 1 / 2)
    (hb1 : Separation.Hb1) (hB3 : Separation.HB3) (hedge : Separation.Hedge)
    (houtZ : Z.Hout t L (73 * L)) (houtZ' : Z'.Hout t L (73 * L)) :
    δ ^ 2 * Real.exp (δ * L / 2)
        ≤ ‖Z.W (Separation.ftest t L) (Separation.ftest t L) - Z'.W (Separation.ftest t L) (Separation.ftest t L)‖ ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) :=
  Zeta23.Separation.clause6_assembly hC ht hδ0 hδ hL1 hL2 hRstar
    Z.carrier Z.mult Z.finite_window Z.localCount Z'.carrier Z'.mult Z'.finite_window Z'.localCount
    hZorb hZmult hZ hZ' hb1 hB3 hedge houtZ houtZ'
