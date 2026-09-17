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
comparator/Challenge/Separation6.lean — CHALLENGE for M4 (iii): the clause-6 assembly of Theorem M2 (Gevrey-localized
single-defect separation, α = 2) of the separation note (rh-program/results/c2-m2/separation-note.md §7.1, with the
hypotheses as the addendum A1–A3 of 2026-09-17 restates them: (R*) as clause 1′, R₀ = 73), stated over the class 𝒞(C₁)
MODULO DISPLAYED HYPOTHESES.  Trusted vocabulary: ChallengeDeps.Separation, ChallengeDeps.SepConfig,
ChallengeDeps.Separation6, all over Mathlib alone.  Solution/Separation6.lean (untrusted) proves exactly this statement by
delegating to Zeta23/Separation/Assembly.lean; github.com/leanprover/comparator checks statement equality, that only the
axioms propext, Classical.choice, Quot.sound are used, and replays the proof through the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  Let C₁ ≥ 1, t ≥ 3, 0 < δ ≤ 1/2, and L with L ≥ 25/δ and
L ≥ (4/δ)(log log(3 + t) + 2 log(1/δ) + log(2·(87/10)·C₁)) (the note's L-hypothesis with λ₀ = 25, C₀ = 4, b₁ = 87/10), and let
(R*) hold (clause 1′: 2c_B√(2tL) − 2log(1 + (c_B/2)√(2tL)) ≥ δL/2 + log((4t² + δ²)C_B²/(1.35δ²)); t ≥ 21L implies it).
Let Z, Z′ ∈ 𝒞(C₁) with, for R = 73L: every point of Z′ with |Im ρ − t| ≤ R on the line Re ρ = 1/2; the four orbit points
1/2 ± δ ± it in Z with multiplicity one, and every other point of Z with |Im ρ − t| ≤ R on the line.  Then, for the test
f = f_{t,L} = i(B_L)′e^{−itu},
    ‖W_Z(f) − W_{Z′}(f)‖ ≥ δ²·e^{δL/2} ≥ 1,
PROVIDED the DISPLAYED hypotheses hold: H-b₁ (sup|ηB̂|² ≤ 87/10), H-B‴ (∫|B‴| ≤ 64231/100), H-edge (clause 2's lower
bound with κ₋ = 1.48088), and H-out for Z and for Z′ (clause 5: the out-window sum beyond 73L converges absolutely and is
≤ e^{−L} in norm).  Label, binding: "Theorem M2's clause-6 assembly is kernel-checked modulo H-edge, H-b₁, H-B‴, H-out"
— never "Theorem M2 is formalized".  What is PROVED inside: clause 4 (the rung), the orbit's four-point accounting
(−2δ²c(δL)² from the pair at +t), clause 1's explicit bound on the reflected pair from Lemma G's complex form, its
absorption under (R*), the decomposition W = (in-window off-line) + (in-window on-line) + (out-window), the L-hypothesis
absorptions, and the final chain.  What is NOT claimed: anything about ζ or RH (the theorem is about two abstract
configurations and one test; clause 8 of the note is scope, not content), clause 5 (displayed), clause 2 (displayed),
the numerical values b₁, ‖B‴‖₁ (displayed), that t ≥ 21L implies (R*) (computed in the note, not derived here), clause 7.

The `sorry` below is deliberate (this is the challenge side); expect a "declaration uses 'sorry'" warning when building
this module.
-/
import ChallengeDeps.Separation6

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
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) := by
  sorry
