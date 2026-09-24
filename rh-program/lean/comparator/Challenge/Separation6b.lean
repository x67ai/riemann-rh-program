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
comparator/Challenge/Separation6b.lean — CHALLENGE for Unit A of the M4 residue (Session 24 item 3): the clause-6 assembly
of Theorem M2 (Gevrey-localized single-defect separation, α = 2; separation note §7.1 with the addendum A1–A3's
hypotheses: (R*) as clause 1′, R₀ = 73) over the class 𝒞(C₁) MODULO DISPLAYED HYPOTHESES, now with the noise constant b₁
PROVED; the clause-7 tight pair (note §7.2) folded in as a second theorem; and "t ≥ 21L ⟹ (R*)" (addendum A1) as a third.
Trusted vocabulary: ChallengeDeps.Separation, ChallengeDeps.SepConfig, ChallengeDeps.Separation6 (the frozen M4 (iii)
files, untouched) and ChallengeDeps.Separation6b (one definition, b1sym), all over Mathlib alone.  Solution/Separation6b.lean
(untrusted) proves exactly these statements by delegating to Zeta23/Separation/Assembly2.lean;
github.com/leanprover/comparator checks statement equality, that only the axioms propext, Classical.choice, Quot.sound
are used, and replays the proofs through the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.
(1) `separation_clause6_assembly_b`: let C₁ ≥ 1, t ≥ 3, 0 < δ ≤ 1/2, and L with L ≥ 25/δ and
    L ≥ (4/δ)(log log(3 + t) + 2 log(1/δ) + log(2·b₁sym·C₁)), b₁sym = (2e^{−1}/Z)² = ‖B′‖₁² (the note's L-hypothesis with
    λ₀ = 25, C₀ = 4 and the PROVED b₁ in place of the displayed digit 87/10 — stronger by log(10.984/8.70) = 0.233 nats),
    and let (R*) hold.  Let Z, Z′ ∈ 𝒞(C₁) with, for R = 73L: every point of Z′ with |Im ρ − t| ≤ R on the line; the
    four orbit points 1/2 ± δ ± it in Z with multiplicity one, every other point of Z with |Im ρ − t| ≤ R on the line.
    Then, for f = f_{t,L}, ‖W_Z(f) − W_{Z′}(f)‖ ≥ δ²·e^{δL/2} ≥ 1, PROVIDED the DISPLAYED hypotheses hold: H-B‴
    (∫|B‴| ≤ 64231/100), H-edge (clause 2's lower bound with κ₋ = 1.48088), H-out for Z and for Z′ (clause 5 whole).
    H-b₁ is NOT a hypothesis any more: (|η|·‖B̂(η)‖)² ≤ b₁sym is a theorem of the solution (B1Sym.lean), with no digit
    of b₁ and no lower bound on Z stated anywhere in this topic's statements.
(2) `separation_clause7_tight_pair`: the same, with Z′ carrying the on-line double at ±t (1/2 ± it, multiplicity 2) —
    the tight pair of note §7.2 (the S3 clause: the defect's orbit against the double on the line).  Its proof is (1)
    applied: Z′ is already arbitrary on-line inside the window.  The double's accounting (h_f(t) = 0; the point at −t
    contributes 2·(2t)²‖B̂(−2tL)‖² = 8t²B̂(2tL)², check-O §12.3, not the note body's 16t²) is a solution-side lemma
    (Assembly2.lean §4), on the standard axioms, not part of this statement.
(3) `rstar_of_21L`: t ≥ 3, L ≥ 50, 25/L ≤ δ ≤ 1/2, 21L ≤ t ⟹ (R*).  The record's "t ≥ 21L implies (R*)" (addendum A1,
    a computed fact there) becomes a proved corollary; the constant 21 enters Lean here only, as this corollary's
    hypothesis, never as the assembly's.
Label, binding: "Theorem M2's clause-6 assembly is a Comparator-checked theorem over `SepConfig`, modulo the displayed
H-edge, H-B‴ and H-out, on the three standard axioms, replayed by nanoda — with b₁ = ‖B′‖₁² proved, clause 7 folded, and
(R*) implied by t ≥ 21L as a proved corollary" — never "Theorem M2 is formalized".  What is NOT claimed: anything about
ζ or RH (the theorems are about abstract configurations and one test; clause 8 of the note is scope, not content),
clause 5 (displayed as H-out), clause 2 (displayed as H-edge), the numerical value ‖B‴‖₁ (displayed), any digit of b₁.

The `sorry`s below are deliberate (this is the challenge side); expect three "declaration uses 'sorry'" warnings when
building this module.
-/
import ChallengeDeps.Separation6b

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
  by
  sorry

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
  by
  sorry

/-- **"t ≥ 21L implies (R*)"** (separation note addendum A1): for t ≥ 3, L ≥ 50, 25/L ≤ δ ≤ 1/2 and 21L ≤ t, the
reflection condition `Rstar t δ L` (clause 1′, the hypothesis of the assembly) holds. -/
theorem rstar_of_21L (t δ L : ℝ) (ht : 3 ≤ t) (hL : 50 ≤ L) (hδ1 : 25 / L ≤ δ) (hδ : δ ≤ 1 / 2)
    (h21 : 21 * L ≤ t) : Separation.Rstar t δ L :=
  by
  sorry
