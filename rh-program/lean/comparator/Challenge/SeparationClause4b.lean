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
comparator/Challenge/SeparationClause4b.lean — CHALLENGE for the rung of Unit A (Session 24 item 3): clause 4 of
Theorem M2 (the in-window on-line noise; separation note §5) over the class 𝒞(C₁) with the noise constant b₁ PROVED in
symbolic form — MODULO the one displayed hypothesis H-B‴.  Trusted vocabulary: ChallengeDeps.Separation (`B`, `ft`, `Z`),
ChallengeDeps.SepConfig (`SepConfig`, `inWindowNoise`, `ftest`, `HB3`), ChallengeDeps.Separation6b (`b1sym`), all over
Mathlib alone.  Solution/SeparationClause4b.lean (untrusted) proves exactly this statement by delegating to
Zeta23/Separation/Assembly2.lean; github.com/leanprover/comparator checks statement equality, that only the axioms
propext, Classical.choice, Quot.sound are used, and replays the proof through the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  For every C₁ ≥ 1, t ≥ 3, L ≥ 50, R ≥ 1 and every Z ∈ 𝒞(C₁), the in-window on-line
noise N_Z := Σ_{ρ ∈ Z, Re ρ = 1/2, |Im ρ − t| ≤ R} m_ρ·‖h_f(γ_ρ)‖², f = f_{t,L}, satisfies
    0 ≤ N_Z ≤ 2·b₁sym·C₁·log(4 + t + R)/L²,   b₁sym = (2e^{−1}/Z)² = ‖B′‖₁²,
PROVIDED the displayed H-B‴ holds (∫ ‖B‴‖ ≤ 64231/100, the note's ‖B‴‖₁ = 642.301: a computed constant).  Compared with
the M4 (iii) rung (Challenge/SeparationClause4.lean, frozen): H-b₁ (b₁ ≤ 87/10) is NO LONGER a hypothesis — the bound
b₁ ≤ ‖B′‖₁² is a theorem of the solution — and the constant in the conclusion is the real number b₁sym rather than the
digit 87/10 (the L-hypothesis of the assembly is stronger by log(10.984/8.70) = 0.233 nats; nothing else changes).
Label, binding: "clause 4 of Theorem M2 is kernel-checked modulo H-B‴, with b₁ = ‖B′‖₁² proved" — never "clause 4 is
formalized" and never "Theorem M2 is formalized".  Nothing is claimed about ζ or RH.

The `sorry` below is deliberate (this is the challenge side); expect a "declaration uses 'sorry'" warning when building
this module.
-/
import ChallengeDeps.Separation6b

noncomputable section

/-- **Theorem M2, clause 4, with b₁ proved** (separation note §5): for Z ∈ 𝒞(C₁), t ≥ 3, L ≥ 50, R ≥ 1,
0 ≤ N_Z ≤ 2·b₁sym·C₁·log(4 + t + R)/L² with b₁sym = (2e^{−1}/Z)² — modulo the displayed H-B‴. -/
theorem separation_clause4_in_window_noise_b (C₁ t L R : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hL : 50 ≤ L) (hR : 1 ≤ R)
    (Z : Separation.SepConfig C₁) (hB3 : Separation.HB3) :
    0 ≤ Z.inWindowNoise t L R ∧
      Z.inWindowNoise t L R ≤ 2 * Separation.b1sym * C₁ * Real.log (4 + t + R) / L ^ 2 := by
  sorry
