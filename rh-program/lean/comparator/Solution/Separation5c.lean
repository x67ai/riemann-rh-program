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
comparator/Solution/Separation5c.lean — the UNTRUSTED comparator solution module for the topic `Separation5c`: the two
statements of Challenge/Separation5c.lean, byte-identical, PROVED by delegating to Zeta23/Separation/Clause5.lean
(`clause5_out_window`, `clause6_assembly_c`) with H-R₀ supplied by the theorem `Zeta23.Separation.F13_50_neg`
(Zeta23/Separation/Clause5Cert.lean: the 16-cell enclosure 421/2000 ≤ Z ≤ 233651/10⁶ of ZEnclosure.lean, the rational
enclosures of e, c_B, √73, and one finite inequality over ℚ checked by `norm_num`).  The trusted `Separation.{B, Z, ft,
gammaOf, ftest, BL, cB, CB, b1sym, HB3, Hedge, Rstar, orbit}`, `Separation.SepConfig.{Wsummand, W, outWindow, Hout}` are
character for character `Zeta23.Separation.{…}`, `Zeta23.paperFT`, `Zeta23.gammaOf` and `Zeta23.Separation.wsum` over
the raw fields, so the delegation typechecks by definitional unfolding in the kernel.  This module never imports the
challenge.  Nothing in this file is part of the trusted base: comparator re-checks that each theorem below has exactly
the statement of its Challenge namesake and uses only the permitted axioms.
Label, binding: "Theorem M2's clause-6 assembly is a Comparator-checked theorem over `SepConfig`, modulo the displayed
H-edge and H-B‴, on the three standard axioms, replayed by nanoda" — never "Theorem M2 is formalized".
-/
import ChallengeDeps.Separation6b
import Zeta23.Separation.Clause5Cert

noncomputable section

/-- **Theorem M2, clause 5** (separation note §6, addendum A3, R₀ = 73), no displayed hypothesis: for Z ∈ 𝒞(C₁),
C₁ ≥ 1, t ≥ 3, L ≥ 50 and 8(log log(3 + t) + log(2b₁C₁)) ≤ L, the out-window sum beyond 73L converges absolutely and
has norm ≤ e^{−L} — `Z.Hout t L (73 * L)`. -/
theorem separation_clause5_out_window_c (C₁ t L : ℝ) (Z : Separation.SepConfig C₁) (hC : 1 ≤ C₁) (ht : 3 ≤ t)
    (hL : 50 ≤ L) (hL8 : 8 * (Real.log (Real.log (3 + t)) + Real.log (2 * Separation.b1sym * C₁)) ≤ L) :
    Z.Hout t L (73 * L) :=
  Zeta23.Separation.clause5_out_window Z.carrier Z.mult Z.finite_window Z.localCount Z.strip hC ht hL hL8
    Zeta23.Separation.F13_50_neg

/-- **Theorem M2, clause 6, with clause 5 proved** (separation note §7.1 with the addendum's hypotheses):
`separation_clause6_assembly_b` with `houtZ`, `houtZ'` deleted — modulo the displayed H-B‴ and H-edge only. -/
theorem separation_clause6_assembly_d (C₁ t δ L : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
    (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * Separation.b1sym * C₁)) ≤ L)
    (hRstar : Separation.Rstar t δ L)
    (Z Z' : Separation.SepConfig C₁)
    (hZorb : Separation.orbit t δ ⊆ Z.carrier) (hZmult : ∀ ρ ∈ Separation.orbit t δ, Z.mult ρ = 1)
    (hZ : ∀ ρ ∈ Z.carrier, |ρ.im - t| ≤ 73 * L → ρ ∉ Separation.orbit t δ → ρ.re = 1 / 2)
    (hZ' : ∀ ρ ∈ Z'.carrier, |ρ.im - t| ≤ 73 * L → ρ.re = 1 / 2)
    (hB3 : Separation.HB3) (hedge : Separation.Hedge) :
    δ ^ 2 * Real.exp (δ * L / 2)
        ≤ ‖Z.W (Separation.ftest t L) (Separation.ftest t L) - Z'.W (Separation.ftest t L) (Separation.ftest t L)‖ ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) :=
  Zeta23.Separation.clause6_assembly_c hC ht hδ0 hδ hL1 hL2 hRstar
    Z.carrier Z.mult Z.finite_window Z.localCount Z.strip Z'.carrier Z'.mult Z'.finite_window Z'.localCount Z'.strip
    hZorb hZmult hZ hZ' hB3 hedge Zeta23.Separation.F13_50_neg
