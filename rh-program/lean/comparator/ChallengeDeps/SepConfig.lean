/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: it imports Mathlib and the trusted
module ChallengeDeps.Separation only.
-/
/-
comparator/ChallengeDeps/SepConfig.lean — the TRUSTED definition layer for the comparator topics `SeparationClause4`
(the dress-rehearsal rung of M4 (iii): clause 4 of Theorem M2, the in-window on-line noise) and `Separation6` (the
clause-6 assembly) of Theorem M2's separation note (rh-program/results/c2-m2/separation-note.md §0.1, §5, §7.1 and the
addendum of 2026-09-17; contract rh-program/results/c2-m2/followups/PRICING.md §1(b) candidate (iii); build record
rh-program/results/c2-m4/BUILD-NOTES-iii.md).

Everything the challenge statements mention beyond ChallengeDeps.Separation (Braw, Z, B, ft, cB, CB) is defined HERE,
from Mathlib alone, in the namespace `Separation`:
  gammaOf ρ := (ρ − 1/2)/i,  reflect ρ := 1 − conj ρ        character for character `Zeta23.gammaOf`, `Zeta23.reflect`
                                                              (Zeta23/Defs.lean): γ_ρ is the ordinate coordinate, real iff
                                                              Re ρ = 1/2, and Re γ_ρ = Im ρ;
  SepConfig C₁                                                the class 𝒞(C₁) of the note (§0.1): the seven fields of
                                                              `Zeta23.ZeroConfig` character for character (distinct points
                                                              with multiplicity ≥ 1, the closed strip 0 ≤ Re ρ ≤ 1,
                                                              invariance under ρ ↦ 1 − conj ρ with equal multiplicity, local
                                                              finiteness in the ordinate), PLUS invariance under ρ ↦ conj ρ
                                                              with equal multiplicity, PLUS the explicit local count
                                                              Σ_{ρ ∈ carrier, |Im ρ − x| ≤ 1} m_ρ ≤ C₁·log(3 + |x|) for every
                                                              real x, counted WITH multiplicity as a finite sum (`∑ᶠ`; the
                                                              set is finite by `finite_window`).  The docstring of
                                                              `Zeta23.ZeroConfig` says the local count is deliberately not a
                                                              field of that structure; this structure adds it;
  Wsummand, W                                                 the datum W_Z(f, g) = Σ_ρ m_ρ h_f(γ_ρ) conj(h_g(conj γ_ρ)) as a
                                                              tsum over the subtype of the carrier — character for character
                                                              `Zeta23.ZeroConfig.Wsummand` / `.W` with `ft` for `paperFT`;
  BL L u := B(u/L)/L,  ftest t L u := i·(B_L)′(u)·e^{−itu}    the note's B_L and the test f_{t,L} (§0.1), with Mathlib's
                                                              `deriv` of the real function B_L;
  inWindowReal, inWindowNoise                                 the on-line points of the carrier with |Im ρ − t| ≤ R, and
                                                              N_Z := Σ over them of m_ρ·‖h_f(γ_ρ)‖² (the note's clause 4);
  Hb1, HB3                                                    the two DISPLAYED hypotheses of the rung, as Props:
                                                              H-b₁: (|η|·‖B̂(η)‖)² ≤ 87/10 for every real η (the note's
                                                              b₁ = sup|ηB̂|² ≤ 8.70, the certified upper end of the
                                                              enclosure [8.64613, 8.6981], §5 and §12.2 — a COMPUTED
                                                              constant, not a theorem here);
                                                              H-B‴: ∫ ‖B‴‖ ≤ 64231/100 (the note's ‖B‴‖₁ = 642.301,
                                                              computed by quadrature — likewise displayed, not proved).
The constants 87/10 and 64231/100 are the note's decimals as rationals; every digit of them is a design choice recorded in
the fidelity ledger (formalization.yaml, fidelity (p)).  A reader who wants to know WHAT is claimed reads this file,
ChallengeDeps/Separation.lean and the challenge files only.
-/
import Mathlib
import ChallengeDeps.Separation

namespace Separation

noncomputable section

open Complex

/-- γ_ρ := (ρ − 1/2)/i — character for character `Zeta23.gammaOf`. -/
def gammaOf (ρ : ℂ) : ℂ := (ρ - 1 / 2) / Complex.I

/-- The reflection ρ ↦ 1 − ρ̄ — character for character `Zeta23.reflect`. -/
def reflect (ρ : ℂ) : ℂ := 1 - (starRingEnd ℂ) ρ

/-- The class 𝒞(C₁) (separation note §0.1): a `Zeta23.ZeroConfig` (its seven fields, character for character) that is
in addition invariant under ρ ↦ conj ρ with equal multiplicities and satisfies the explicit local count
Σ_{ρ ∈ carrier, |Im ρ − x| ≤ 1} m_ρ ≤ C₁·log(3 + |x|) for every real x (with multiplicity; the set is finite by
`finite_window`, so the `∑ᶠ` is the honest finite sum). -/
structure SepConfig (C₁ : ℝ) where
  /-- the set 𝒵 of distinct zeros -/
  carrier : Set ℂ
  /-- multiplicity m_ρ (value irrelevant off carrier) -/
  mult : ℂ → ℕ
  one_le_mult : ∀ ρ ∈ carrier, 1 ≤ mult ρ
  strip : ∀ ρ ∈ carrier, 0 ≤ ρ.re ∧ ρ.re ≤ 1
  reflect_mem : ∀ ρ ∈ carrier, reflect ρ ∈ carrier
  mult_reflect : ∀ ρ ∈ carrier, mult (reflect ρ) = mult ρ
  /-- local finiteness in the ordinate: finitely many zeros with T₁ < γ ≤ T₂ -/
  finite_window : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite
  /-- invariance under ρ ↦ conj ρ (the note's second symmetry; ζ's configuration has it) -/
  conj_mem : ∀ ρ ∈ carrier, (starRingEnd ℂ) ρ ∈ carrier
  mult_conj : ∀ ρ ∈ carrier, mult ((starRingEnd ℂ) ρ) = mult ρ
  /-- the local count of 𝒞(C₁): #{γ ∈ Z : |Re γ − x| ≤ 1} ≤ C₁ log(3 + |x|), with multiplicity, Re γ_ρ = Im ρ -/
  localCount : ∀ x : ℝ,
    ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|)

namespace SepConfig

variable {C₁ : ℝ} (Z : SepConfig C₁)

/-- Summand of Weil's form: m_ρ h_f(γ_ρ) conj(h_g(conj γ_ρ)) — character for character `Zeta23.ZeroConfig.Wsummand`. -/
def Wsummand (f g : ℝ → ℂ) (ρ : ℂ) : ℂ :=
  (Z.mult ρ : ℂ) * ft f (gammaOf ρ) * (starRingEnd ℂ) (ft g ((starRingEnd ℂ) (gammaOf ρ)))

/-- W(f,g) := Σ_ρ m_ρ h_f(γ_ρ) conj(h_g(conj γ_ρ)), a tsum over the subtype of the carrier — character for character
`Zeta23.ZeroConfig.W`. -/
def W (f g : ℝ → ℂ) : ℂ := ∑' ρ : Z.carrier, Z.Wsummand f g ρ

/-- the on-line points of the carrier within the window |Im ρ − t| ≤ R (γ_ρ real with |γ_ρ − t| ≤ R). -/
def inWindowReal (t R : ℝ) : Set ℂ := Z.carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R}

end SepConfig

/-- B_L(u) := B(u/L)/L (separation note §0.1). -/
def BL (L : ℝ) (u : ℝ) : ℝ := B (u / L) / L

/-- the test f_{t,L}(u) := i·(B_L)′(u)·e^{−itu} (separation note §0.1), with Mathlib's `deriv` of the real function B_L. -/
def ftest (t L : ℝ) (u : ℝ) : ℂ := Complex.I * ((deriv (BL L) u : ℝ) : ℂ) * Complex.exp (-(Complex.I * t * u))

/-- N_Z := Σ_{γ ∈ Z real, |γ − t| ≤ R} m_γ ‖h_f(γ)‖² for f = f_{t,L} (separation note §5, clause 4). -/
def SepConfig.inWindowNoise {C₁ : ℝ} (Z : SepConfig C₁) (t L R : ℝ) : ℝ :=
  ∑' ρ : Z.inWindowReal t R, (Z.mult ρ : ℝ) * ‖ft (ftest t L) (gammaOf ρ)‖ ^ 2

/-- **H-b₁** (displayed): (|η|·‖B̂(η)‖)² ≤ 87/10 for every real η — the note's b₁ = sup_η |ηB̂(η)|² ≤ 8.70 (§5, §12.2). -/
def Hb1 : Prop := ∀ η : ℝ, (|η| * ‖ft (fun v => (B v : ℂ)) η‖) ^ 2 ≤ 87 / 10

/-- **H-B‴** (displayed): ∫ ‖B‴‖ ≤ 64231/100 — the note's ‖B‴‖₁ = 642.301 (§5). -/
def HB3 : Prop := ∫ u, ‖iteratedDeriv 3 (fun v => (B v : ℂ)) u‖ ≤ 64231 / 100

end

end Separation
