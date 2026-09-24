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
comparator/Solution/Separation6b.lean — the UNTRUSTED comparator solution module for the topic `Separation6b`: the three
statements of Challenge/Separation6b.lean, byte-identical, PROVED by delegating to Zeta23/Separation/Assembly2.lean
(`Zeta23.Separation.clause6_assembly_b`, `clause7_tight_pair`, `rstar_of_21L`, stated there over raw data: the two
carriers, multiplicity functions, local finiteness and local counts are passed field by field from the trusted
`Separation.SepConfig`).  The trusted `Separation.{orbit, edge, Hedge, Rstar, ftest, HB3, b1sym, SepConfig.W,
SepConfig.Wsummand, SepConfig.Hout, gammaOf, ft, Z}` are character for character `Zeta23.Separation.{orbit, edge, Hedge,
Rstar, ftest, HB3, b1sym, wsum, Z}`, `Zeta23.gammaOf`, `Zeta23.paperFT`, so the delegations typecheck by definitional
unfolding in the kernel.  This module never imports the challenge.  Nothing in this file is part of the trusted base:
comparator re-checks that each theorem below has exactly the statement of its Challenge namesake and uses only the
permitted axioms.
Label, binding: "kernel-checked modulo H-edge, H-B‴, H-out — with b₁ = ‖B′‖₁² proved, clause 7 folded, and (R*)
implied by t ≥ 21L as a proved corollary" — never "Theorem M2 is formalized".
-/
import ChallengeDeps.Separation6b
import Zeta23.Separation.Assembly2

noncomputable section

/-- **Theorem M2, clause 6, with b₁ proved** (separation note §7.1 with the addendum's hypotheses): for Z, Z′ ∈ 𝒞(C₁)
as in the header, ‖W_Z(f_{t,L}) − W_{Z′}(f_{t,L})‖ ≥ δ²e^{δL/2} ≥ 1 — modulo the displayed H-B‴, H-edge, H-out; the
L-hypothesis carries b₁sym = (2e^{−1}/Z)² in place of the digit 87/10, and H-b₁ is no longer a hypothesis. -/
theorem separation_clause6_assembly_b (C₁ t δ L : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
    (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * Separation.b1sym * C₁)) ≤ L)
    (hRstar : Separation.Rstar t δ L)
    (Z Z' : Separation.SepConfig C₁)
    (hZorb : Separation.orbit t δ ⊆ Z.carrier) (hZmult : ∀ ρ ∈ Separation.orbit t δ, Z.mult ρ = 1)
    (hZ : ∀ ρ ∈ Z.carrier, |ρ.im - t| ≤ 73 * L → ρ ∉ Separation.orbit t δ → ρ.re = 1 / 2)
    (hZ' : ∀ ρ ∈ Z'.carrier, |ρ.im - t| ≤ 73 * L → ρ.re = 1 / 2)
    (hB3 : Separation.HB3) (hedge : Separation.Hedge)
    (houtZ : Z.Hout t L (73 * L)) (houtZ' : Z'.Hout t L (73 * L)) :
    δ ^ 2 * Real.exp (δ * L / 2)
        ≤ ‖Z.W (Separation.ftest t L) (Separation.ftest t L) - Z'.W (Separation.ftest t L) (Separation.ftest t L)‖ ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) :=
  Zeta23.Separation.clause6_assembly_b hC ht hδ0 hδ hL1 hL2 hRstar
    Z.carrier Z.mult Z.finite_window Z.localCount Z'.carrier Z'.mult Z'.finite_window Z'.localCount
    hZorb hZmult hZ hZ' hB3 hedge houtZ houtZ'

set_option linter.unusedVariables false in
/-- **Theorem M2, clause 7 — the tight pair** (separation note §7.2, with check-O §12.3's accounting): the hypotheses of
`separation_clause6_assembly_b` with Z′ carrying the on-line double at ±t — the points 1/2 + it and 1/2 − it in Z′ with
multiplicity 2 — and the same conclusion: the pair (Z: the defect's orbit; Z′: the double on the line) is separated at
the same bandwidth.  The double's own accounting (0 at +t, 2·(2t)²‖B̂(−2tL)‖² at −t) is a solution-side lemma. -/
theorem separation_clause7_tight_pair (C₁ t δ L : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
    (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * Separation.b1sym * C₁)) ≤ L)
    (hRstar : Separation.Rstar t δ L)
    (Z Z' : Separation.SepConfig C₁)
    (hZorb : Separation.orbit t δ ⊆ Z.carrier) (hZmult : ∀ ρ ∈ Separation.orbit t δ, Z.mult ρ = 1)
    (hZ : ∀ ρ ∈ Z.carrier, |ρ.im - t| ≤ 73 * L → ρ ∉ Separation.orbit t δ → ρ.re = 1 / 2)
    (hZ' : ∀ ρ ∈ Z'.carrier, |ρ.im - t| ≤ 73 * L → ρ.re = 1 / 2)
    (hZ'plus : (⟨1 / 2, t⟩ : ℂ) ∈ Z'.carrier) (hZ'minus : (⟨1 / 2, -t⟩ : ℂ) ∈ Z'.carrier)
    (hZ'plus2 : Z'.mult ⟨1 / 2, t⟩ = 2) (hZ'minus2 : Z'.mult ⟨1 / 2, -t⟩ = 2)
    (hB3 : Separation.HB3) (hedge : Separation.Hedge)
    (houtZ : Z.Hout t L (73 * L)) (houtZ' : Z'.Hout t L (73 * L)) :
    δ ^ 2 * Real.exp (δ * L / 2)
        ≤ ‖Z.W (Separation.ftest t L) (Separation.ftest t L) - Z'.W (Separation.ftest t L) (Separation.ftest t L)‖ ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) :=
  Zeta23.Separation.clause7_tight_pair hC ht hδ0 hδ hL1 hL2 hRstar
    Z.carrier Z.mult Z.finite_window Z.localCount Z'.carrier Z'.mult Z'.finite_window Z'.localCount
    hZorb hZmult hZ hZ' hZ'plus hZ'minus hZ'plus2 hZ'minus2 hB3 hedge houtZ houtZ'

/-- **"t ≥ 21L implies (R*)"** (separation note addendum A1): for t ≥ 3, L ≥ 50, 25/L ≤ δ ≤ 1/2 and 21L ≤ t, the
reflection condition `Rstar t δ L` (clause 1′, the hypothesis of the assembly) holds. -/
theorem rstar_of_21L (t δ L : ℝ) (ht : 3 ≤ t) (hL : 50 ≤ L) (hδ1 : 25 / L ≤ δ) (hδ : δ ≤ 1 / 2)
    (h21 : 21 * L ≤ t) : Separation.Rstar t δ L :=
  Zeta23.Separation.rstar_of_21L ht hL hδ1 hδ h21
