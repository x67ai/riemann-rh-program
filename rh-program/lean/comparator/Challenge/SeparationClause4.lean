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
comparator/Challenge/SeparationClause4.lean — CHALLENGE for the dress-rehearsal rung of M4 (iii): clause 4 of Theorem M2
(the in-window on-line noise) of the separation note (rh-program/results/c2-m2/separation-note.md §5), stated over the
class 𝒞(C₁) MODULO two displayed hypotheses.  Trusted vocabulary: ChallengeDeps.Separation (`Separation.B`, `ft`) and
ChallengeDeps.SepConfig (`Separation.SepConfig`, `inWindowNoise`, `ftest`, `Hb1`, `HB3`), all over Mathlib alone.
Solution/SeparationClause4.lean (untrusted) proves exactly this statement by delegating to Zeta23/Separation/Clause4.lean;
github.com/leanprover/comparator checks statement equality, that only the axioms propext, Classical.choice, Quot.sound
are used, and replays the proof through the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  For every C₁ ≥ 1, t ≥ 3, L ≥ 50, R ≥ 1 and every configuration Z of the class 𝒞(C₁)
(a `Separation.SepConfig C₁`: distinct points of the closed strip 0 ≤ Re ρ ≤ 1 with multiplicities, invariant under
ρ ↦ 1 − conj ρ and ρ ↦ conj ρ, locally finite in the ordinate, with the local count
Σ_{|Im ρ − x| ≤ 1} m_ρ ≤ C₁·log(3 + |x|) for every real x), the in-window on-line noise
    N_Z := Σ_{ρ ∈ Z, Re ρ = 1/2, |Im ρ − t| ≤ R} m_ρ · ‖h_f(γ_ρ)‖²,   f = f_{t,L}(u) = i·(B_L)′(u)·e^{−itu},
satisfies 0 ≤ N_Z ≤ 2·(87/10)·C₁·log(4 + t + R)/L² — PROVIDED the two DISPLAYED hypotheses hold:
    H-b₁ : (|η|·‖B̂(η)‖)² ≤ 87/10 for every real η    (the note's b₁ = sup|ηB̂|² ≤ 8.70: a computed constant),
    H-B‴ : ∫ ‖B‴‖ ≤ 64231/100                          (the note's ‖B‴‖₁ = 642.301: a computed constant).
Nothing else is displayed.  Label, binding: "clause 4 of Theorem M2 is kernel-checked modulo H-b₁, H-B‴" — never
"clause 4 is formalized" and never "Theorem M2 is formalized".  Nothing is claimed about the orbit, the out-window
sum, the datum W_Z(f) as a whole, ζ, or RH; the hypothesis of the note's clause 4 that the window is on-line except for
the orbit is not needed for this bound and is not stated (the sum is over the on-line points by definition).

The `sorry` below is deliberate (this is the challenge side); expect a "declaration uses 'sorry'" warning when building
this module.
-/
import ChallengeDeps.SepConfig

noncomputable section

/-- **Theorem M2, clause 4** (separation note §5): for Z ∈ 𝒞(C₁), t ≥ 3, L ≥ 50, R ≥ 1,
0 ≤ N_Z ≤ 2·b₁·C₁·log(4 + t + R)/L² with b₁ = 87/10 — modulo the displayed H-b₁ and H-B‴. -/
theorem separation_clause4_in_window_noise (C₁ t L R : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hL : 50 ≤ L) (hR : 1 ≤ R)
    (Z : Separation.SepConfig C₁) (hb1 : Separation.Hb1) (hB3 : Separation.HB3) :
    0 ≤ Z.inWindowNoise t L R ∧
      Z.inWindowNoise t L R ≤ 2 * (87 / 10) * C₁ * Real.log (4 + t + R) / L ^ 2 := by
  sorry
