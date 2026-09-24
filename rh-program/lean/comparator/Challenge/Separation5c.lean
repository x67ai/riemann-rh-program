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
comparator/Challenge/Separation5c.lean — CHALLENGE for Unit B, leg 1(b) (Session 25 item 2): clause 5 of Theorem M2
with NO displayed hypothesis, and the clause-6 assembly modulo H-edge and H-B‴ only.  These are the two statements of
Challenge/Separation5.lean with the hypothesis `hR0 : Separation.HR0` REMOVED — H-R₀ (the one-point check
F₁₃(50; 73) ≤ 0) is a theorem of the solution side (Zeta23/Separation/Clause5Cert.lean, from a 16-cell rational
enclosure of Z, Zeta23/Separation/ZEnclosure.lean, and one finite inequality over ℚ).  Trusted vocabulary: ONLY the frozen
ChallengeDeps.{Separation, SepConfig, Separation6, Separation6b} (`SepConfig`, `Hout`, `ftest`, `W`, `orbit`, `Rstar`,
`HB3`, `Hedge`, `b1sym`), all over Mathlib alone — this topic adds no trusted definition at all.
Solution/Separation5c.lean (untrusted) proves exactly these statements by delegating to Zeta23/Separation/
{Clause5, Clause5Cert}.lean; github.com/leanprover/comparator checks statement equality, that only the axioms propext,
Classical.choice, Quot.sound are used, and replays the proofs through the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  (1) `separation_clause5_out_window_c`: for every Z ∈ 𝒞(C₁), C₁ ≥ 1, t ≥ 3, L ≥ 50
with 8(log log(3 + t) + log(2b₁C₁)) ≤ L, `Z.Hout t L (73L)`: the out-window sum beyond 73L of m_ρ h_f(γ_ρ) conj(h_f(conj γ_ρ)),
f = f_{t,L}, converges absolutely and its norm is ≤ e^{−L} — the note's clause 5 with R₀ = 73 (addendum A3), with b₁ the
proved b₁sym; no displayed hypothesis.  (2) `separation_clause6_assembly_d`: the Unit A assembly
`separation_clause6_assembly_b` (frozen) with `houtZ`, `houtZ'` DELETED — the same conclusion ‖W_Z(f) − W_{Z′}(f)‖ ≥
δ²e^{δL/2} ≥ 1, modulo the displayed H-B‴ and H-edge only.  Label, binding: "Theorem M2's clause-6 assembly is a
Comparator-checked theorem over `SepConfig`, modulo the displayed H-edge and H-B‴, on the three standard axioms, replayed
by nanoda" — never "clause 5 is formalized" and never "Theorem M2 is formalized" (clause 8's ζ instance and the fidelity
ledger's rows remain what they are).  Nothing is claimed about ζ or RH.

The two `sorry`s below are deliberate (this is the challenge side); expect "declaration uses 'sorry'" warnings when
building this module.
-/
import ChallengeDeps.Separation6b

noncomputable section

/-- **Theorem M2, clause 5** (separation note §6, addendum A3, R₀ = 73), no displayed hypothesis: for Z ∈ 𝒞(C₁),
C₁ ≥ 1, t ≥ 3, L ≥ 50 and 8(log log(3 + t) + log(2b₁C₁)) ≤ L, the out-window sum beyond 73L converges absolutely and
has norm ≤ e^{−L} — `Z.Hout t L (73 * L)`. -/
theorem separation_clause5_out_window_c (C₁ t L : ℝ) (Z : Separation.SepConfig C₁) (hC : 1 ≤ C₁) (ht : 3 ≤ t)
    (hL : 50 ≤ L) (hL8 : 8 * (Real.log (Real.log (3 + t)) + Real.log (2 * Separation.b1sym * C₁)) ≤ L) :
    Z.Hout t L (73 * L) :=
  by
  sorry

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
  by
  sorry
