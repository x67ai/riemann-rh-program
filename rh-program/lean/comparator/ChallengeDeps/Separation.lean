/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: it imports Mathlib only.
-/
/-
comparator/ChallengeDeps/Separation.lean — the TRUSTED definition layer for the comparator topics
`SeparationG1` (the dress-rehearsal rung: Lemma G1) and `Separation` (Lemma G) of Theorem M2's separation note
(rh-program/results/c2-m2/separation-note.md §2; build record rh-program/results/c2-m4/BUILD-NOTES.md).

Everything the challenge statements mention is defined HERE, from Mathlib alone, in the namespace `Separation`:
  Braw v := if |v| < 1/2 then exp (−1/(1 − 4v²)) else 0     the note's B_raw — defined by the exp formula
                                                             (the note's factorization through expNegInvGlue and its
                                                             remark B_raw = θ(v + ½)^{1/4} are NOT part of the trusted text);
  Z      := ∫ v in −1/2..1/2, Braw v                         the normalization, a real number defined by an integral —
                                                             no digit of it (0.2219969…) is asserted anywhere in Lean;
  B      := Braw / Z                                         the bump of Theorem M2 (∫ B = 1 is a solution-side fact);
  ft f z := ∫ u, f u · exp (I z u)                           the paper's Fourier convention h_f(z) = ∫ f(u) e^{izu} du
                                                             (character for character Zeta23.paperFT, Zeta23/Defs.lean),
                                                             re-declared so that this module imports nothing from Zeta23/;
  cB     := 2/√(72e),  CB := e²/Z                            Lemma G's constants, as closed-form reals.
The five definitions are character for character those of Zeta23/Separation/LemmaG1.lean §1 (namespace
`Zeta23.Separation`) and `ft` is character for character `Zeta23.paperFT`, so that each is definitionally equal to its
Zeta23 namesake and the solution modules delegate by unfolding.  A reader who wants to know WHAT is claimed reads this
file and the challenge files only.
-/
import Mathlib

namespace Separation

noncomputable section

/-- the note's B_raw: exp(−1/(1 − 4v²)) on |v| < 1/2, 0 elsewhere. -/
def Braw (v : ℝ) : ℝ := if |v| < 1 / 2 then Real.exp (-1 / (1 - 4 * v ^ 2)) else 0

/-- the normalization Z = ∫_{−1/2}^{1/2} B_raw (a real number defined by an integral; ≈ 0.222). -/
def Z : ℝ := ∫ v in (-1 / 2 : ℝ)..(1 / 2), Braw v

/-- the bump B = B_raw / Z (so that ∫ B = 1). -/
def B (v : ℝ) : ℝ := Braw v / Z

/-- the paper's Fourier transform h_f(z) = ∫ f(u) e^{izu} du (sign +i, no 2π, complex argument) —
character for character `Zeta23.paperFT`. -/
def ft (f : ℝ → ℂ) (z : ℂ) : ℂ := ∫ u : ℝ, f u * Complex.exp (Complex.I * z * (u : ℂ))

/-- c_B = 2/√(72e). -/
def cB : ℝ := 2 / Real.sqrt (72 * Real.exp 1)

/-- C_B = e²/Z. -/
def CB : ℝ := Real.exp 1 ^ 2 / Z

end

end Separation
