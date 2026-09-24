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
comparator/Challenge/Separation5.lean — CHALLENGE for Unit B, leg 1(a) (Session 25 item 2): clause 5 of Theorem M2
(the out-window contamination, uniform over the depth |Im γ| ≤ 1/2; separation note §6, addendum A3 with R₀ = 73 and
the L-hypothesis spent once) MODULO the displayed one-point check H-R₀, and the clause-6 assembly with H-out REPLACED by
H-R₀.  Trusted vocabulary: ChallengeDeps.{Separation, SepConfig, Separation6, Separation6b} (frozen) and
ChallengeDeps.Separation5 (`gammaPoly`, `Prelax`, `P2`, `P3`, `F13`, `HR0` — transcriptions of r0_73_check.py lines
22–33), all over Mathlib alone.  Solution/Separation5.lean (untrusted) proves exactly these statements by delegating to
Zeta23/Separation/Clause5.lean; github.com/leanprover/comparator checks statement equality, that only the axioms
propext, Classical.choice, Quot.sound are used, and replays the proofs through the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  (1) `separation_clause5_out_window`: for every Z ∈ 𝒞(C₁), C₁ ≥ 1, t ≥ 3, L ≥ 50 with
8(log log(3 + t) + log(2b₁C₁)) ≤ L (implied by the assembly's L-hypothesis), PROVIDED the displayed H-R₀ holds
(F₁₃(50) ≤ 0 and 5/(2c_B√73 − 13/8) ≤ 50: the note's one-point check at L₀ = 50, R₀ = 73 — a real inequality about
explicitly defined reals, NOT proved here), `Z.Hout t L (73L)` holds: the out-window sum beyond 73L of
m_ρ h_f(γ_ρ) conj(h_f(conj γ_ρ)), f = f_{t,L}, converges absolutely and its norm is ≤ e^{−L} — the note's clause 5,
with its constant R₀ = 73 of addendum A3.  (2) `separation_clause6_assembly_c`: the Unit A assembly
`separation_clause6_assembly_b` (frozen) with the two hypotheses `houtZ : Z.Hout t L (73L)`, `houtZ' : Z'.Hout t L (73L)`
REPLACED by the single `hR0 : HR0` — the same conclusion ‖W_Z(f) − W_{Z′}(f)‖ ≥ δ²e^{δL/2} ≥ 1, modulo the displayed
H-B‴, H-edge and H-R₀; its proof is (1) applied to Z and to Z′ and then the frozen assembly.  Compared with Unit A, the
displayed clause-5 hypothesis (H-out, a whole clause) has become a displayed numeric one-point check (H-R₀); this is
the note's own reduction (§6, "The relaxation that makes 'for all L ≥ L₀' a one-point check").  Label, binding: "Theorem
M2's clause-6 assembly is a Comparator-checked theorem over `SepConfig`, modulo the displayed H-edge, H-B‴ and H-R₀ (the
one-point check F₁₃(50; 73) ≤ 0 as a displayed real inequality), on the three standard axioms, replayed by nanoda" —
never "clause 5 is formalized" and never "Theorem M2 is formalized".  Nothing is claimed about ζ or RH.

The two `sorry`s below are deliberate (this is the challenge side); expect "declaration uses 'sorry'" warnings when
building this module.
-/
import ChallengeDeps.Separation5

noncomputable section

/-- **Theorem M2, clause 5, modulo H-R₀** (separation note §6, addendum A3): for Z ∈ 𝒞(C₁), C₁ ≥ 1, t ≥ 3, L ≥ 50,
8(log log(3 + t) + log(2b₁C₁)) ≤ L and the displayed one-point check H-R₀, the out-window sum beyond 73L converges
absolutely and has norm ≤ e^{−L} — `Z.Hout t L (73 * L)`. -/
theorem separation_clause5_out_window (C₁ t L : ℝ) (Z : Separation.SepConfig C₁) (hC : 1 ≤ C₁) (ht : 3 ≤ t)
    (hL : 50 ≤ L) (hL8 : 8 * (Real.log (Real.log (3 + t)) + Real.log (2 * Separation.b1sym * C₁)) ≤ L)
    (hR0 : Separation.HR0) :
    Z.Hout t L (73 * L) :=
  by
  sorry

/-- **Theorem M2, clause 6, with clause 5 proved modulo H-R₀** (separation note §7.1 with the addendum's hypotheses):
`separation_clause6_assembly_b` with `houtZ`, `houtZ'` replaced by `hR0 : HR0` — modulo the displayed H-B‴, H-edge
and H-R₀. -/
theorem separation_clause6_assembly_c (C₁ t δ L : ℝ) (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
    (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * Separation.b1sym * C₁)) ≤ L)
    (hRstar : Separation.Rstar t δ L)
    (Z Z' : Separation.SepConfig C₁)
    (hZorb : Separation.orbit t δ ⊆ Z.carrier) (hZmult : ∀ ρ ∈ Separation.orbit t δ, Z.mult ρ = 1)
    (hZ : ∀ ρ ∈ Z.carrier, |ρ.im - t| ≤ 73 * L → ρ ∉ Separation.orbit t δ → ρ.re = 1 / 2)
    (hZ' : ∀ ρ ∈ Z'.carrier, |ρ.im - t| ≤ 73 * L → ρ.re = 1 / 2)
    (hB3 : Separation.HB3) (hedge : Separation.Hedge) (hR0 : Separation.HR0) :
    δ ^ 2 * Real.exp (δ * L / 2)
        ≤ ‖Z.W (Separation.ftest t L) (Separation.ftest t L) - Z'.W (Separation.ftest t L) (Separation.ftest t L)‖ ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) :=
  by
  sorry
