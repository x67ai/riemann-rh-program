/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: it imports Mathlib and the trusted
modules ChallengeDeps.Separation, ChallengeDeps.SepConfig only.
-/
/-
comparator/ChallengeDeps/Separation6.lean — the TRUSTED definition layer for the comparator topic `Separation6` (the
clause-6 assembly of Theorem M2 over the class 𝒞(C₁), MODULO displayed hypotheses; rh-program/results/c2-m2/separation-note.md
§0.1–§0.2, §4, §6, §7.1 and the addendum A1–A3 of 2026-09-17; contract rh-program/results/c2-m2/followups/PRICING.md §1(b)
candidate (iii); build record rh-program/results/c2-m4/BUILD-NOTES-iii.md).  Kept separate from ChallengeDeps/SepConfig.lean
so that the rung's trusted file stays byte for byte what its Comparator run checked.

Everything the assembly's challenge mentions beyond ChallengeDeps.Separation and ChallengeDeps.SepConfig is defined
HERE, from Mathlib alone, in the namespace `Separation`:
  orbit t δ            the four points ρ = 1/2 ± δ ± it of the defect's orbit (γ_ρ = ±t ± iδ; note §0.2);
  edge λ               the edge function c(λ) := ∫ B(v)·cosh(λv) dv (note §0.1; c(λ) = B̂(±iλ) is a solution-side lemma);
  Hedge                H-edge (DISPLAYED): clause 2's LOWER bound, c(λ) ≥ exp(λ/2 − √λ − (3/4)log λ + κ₋) for every
                       λ ≥ 25 with κ₋ = 148088/100000 (the note's κ_∞ = 1.48088… as a rational; §3.2).  The upper bound of
                       the two-sided law (κ₊) is not consumed by the assembly and is not displayed;
  outWindow, Hout      the out-window part of the datum (the points with |Im ρ − t| > R) and H-out (DISPLAYED; the
                       note's clause 5): for f = f_{t,L}, the out-window sum of m_ρ h_f(γ_ρ) conj(h_f(conj γ_ρ)) converges
                       absolutely and has norm ≤ e^{−L}.  Clause 5 is a THEOREM of the note (§6, addendum A3 with R₀ = 73);
                       its proof (incomplete-gamma integrals, the Laurent polynomial P, the one-point check F̃(50; 73) ≤ −0.32)
                       is not formalized here and the clause is displayed whole — the "fails" close of PRICING §5(e) / the
                       brief's rule 5, recorded as such;
  Rstar t δ L          clause 1′, the reflection condition (R*) of the addendum A1, in the note's logarithmic form
                       2c_B s − 2log(1 + (c_B/2)s) ≥ δL/2 + log((4t² + δ²)C_B²/(1.35δ²)), s = √(2tL); 1.35 = 27/20.
                       (R*) is a HYPOTHESIS of the theorem (the note's), not an "H-": t ≥ 21L implies it (A1), a fact
                       computed in the note and not derived here.
The constants of the theorem's L-hypothesis are the record's, as rationals: λ₀ = 25, C₀ = 4, b₁ = 87/10, R₀ = 73, c₀ = 1/2.
A reader who wants to know WHAT is claimed reads this file, ChallengeDeps/Separation.lean, ChallengeDeps/SepConfig.lean
and Challenge/Separation6.lean only.
-/
import Mathlib
import ChallengeDeps.Separation
import ChallengeDeps.SepConfig

namespace Separation

noncomputable section

open Complex

/-- the orbit {1/2 ± δ ± it} of the defect (γ_ρ = ±t ± iδ; note §0.2), as points ρ = β + iτ. -/
def orbit (t δ : ℝ) : Set ℂ :=
  {(⟨1 / 2 + δ, t⟩ : ℂ), (⟨1 / 2 - δ, t⟩ : ℂ), (⟨1 / 2 + δ, -t⟩ : ℂ), (⟨1 / 2 - δ, -t⟩ : ℂ)}

/-- the edge function c(λ) := ∫ B(v)·cosh(λv) dv (note §0.1). -/
def edge (l : ℝ) : ℝ := ∫ v, B v * Real.cosh (l * v)

/-- **H-edge** (displayed): clause 2's lower bound, c(λ) ≥ exp(λ/2 − √λ − (3/4)·log λ + κ₋) for λ ≥ 25,
κ₋ = 148088/100000 (note §3.2). -/
def Hedge : Prop :=
  ∀ l : ℝ, 25 ≤ l → Real.exp (l / 2 - Real.sqrt l - 3 / 4 * Real.log l + 148088 / 100000) ≤ edge l

/-- clause 1′, the reflection condition (R*) (note addendum A1), with s = √(2tL) and 1.35 = 27/20. -/
def Rstar (t δ L : ℝ) : Prop :=
  δ * L / 2 + Real.log ((4 * t ^ 2 + δ ^ 2) * CB ^ 2 / (27 / 20 * δ ^ 2))
    ≤ 2 * cB * Real.sqrt (2 * t * L) - 2 * Real.log (1 + cB / 2 * Real.sqrt (2 * t * L))

namespace SepConfig

variable {C₁ : ℝ} (Z : SepConfig C₁)

/-- the out-window points: |Im ρ − t| > R. -/
def outWindow (t R : ℝ) : Set ℂ := Z.carrier ∩ {ρ | R < |ρ.im - t|}

/-- **H-out** (displayed; the note's clause 5): for f = f_{t,L}, the out-window sum converges absolutely and
‖Σ_{|Im ρ − t| > R} m_ρ h_f(γ_ρ) conj(h_f(conj γ_ρ))‖ ≤ e^{−L}. -/
def Hout (t L R : ℝ) : Prop :=
  Summable (fun ρ : Z.outWindow t R => ‖Z.Wsummand (ftest t L) (ftest t L) ρ‖) ∧
    ‖∑' ρ : Z.outWindow t R, Z.Wsummand (ftest t L) (ftest t L) ρ‖ ≤ Real.exp (-L)

end SepConfig

end

end Separation
