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
comparator/Challenge/SeparationClause5Sum.lean — CHALLENGE for the dress-rehearsal rung of Unit B (Session 25 item 2):
clause 5's SUMMABILITY — the first conjunct of the displayed H-out (`Separation.SepConfig.Hout`, ChallengeDeps/Separation6.lean)
at R = 73L, with no numerics.  Trusted vocabulary: ChallengeDeps.Separation (`B`, `ft`), ChallengeDeps.SepConfig
(`SepConfig`, `Wsummand`, `ftest`), ChallengeDeps.Separation6 (`outWindow`), reached through ChallengeDeps.Separation6b,
all over Mathlib alone.  Solution/SeparationClause5Sum.lean (untrusted) proves exactly this statement by delegating to
Zeta23/Separation/Clause5.lean; github.com/leanprover/comparator checks statement equality, that only the axioms propext,
Classical.choice, Quot.sound are used, and replays the proof through the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  For every C₁, t ≥ 3, L > 0 and every Z ∈ 𝒞(C₁), the out-window family
    ρ ↦ ‖m_ρ·h_f(γ_ρ)·conj(h_f(conj γ_ρ))‖,  ρ ∈ Z with |Im ρ − t| > 73L,  f = f_{t,L},
is summable (absolute convergence of the out-window part of W_Z(f_{t,L})).  This is the summability that
`separation_clause6_assembly_b` (frozen) takes from its hypothesis `Hout`; the SIZE of the out-window sum (the second
conjunct of `Hout`, ‖Σ‖ ≤ e^{−L}) is NOT claimed here — it is the topic `Separation5` (clause 5 modulo H-R₀).  No
displayed hypothesis: the proof uses the strip 0 ≤ Re ρ ≤ 1 (the `strip` field of `SepConfig`, consumed for the first
time), the local count, and Lemma G's complex form, which is a theorem of the library.  Label, binding: "clause 5's
summability is Comparator-checked" — never "clause 5 is formalized" and never "Theorem M2 is formalized".  Nothing is
claimed about ζ or RH.

The `sorry` below is deliberate (this is the challenge side); expect a "declaration uses 'sorry'" warning when building
this module.
-/
import ChallengeDeps.Separation6b

noncomputable section

/-- **Theorem M2, clause 5 — summability** (separation note §6 (b), absolute convergence): for Z ∈ 𝒞(C₁), t ≥ 3 and
L > 0, the out-window family ‖m_ρ h_f(γ_ρ) conj(h_f(conj γ_ρ))‖ over |Im ρ − t| > 73L is summable — the first conjunct
of `Separation.SepConfig.Hout` at R = 73L, with no numerics and no displayed hypothesis. -/
theorem separation_clause5_summable (C₁ t L : ℝ) (Z : Separation.SepConfig C₁) (ht : 3 ≤ t) (hL : 0 < L) :
    Summable (fun ρ : Z.outWindow t (73 * L) =>
      ‖Z.Wsummand (Separation.ftest t L) (Separation.ftest t L) ρ‖) :=
  by
  sorry
