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
comparator/ChallengeDeps/IntegralityGap.lean — the TRUSTED definition layer for the comparator topic `IntegralityGap`
(barrier-zoo IV.17, the fractional-mark integrality barrier; formalization-queue item 10; build record
rh-program/results/iv17-lean-s30/BUILD-NOTES.md).

Everything the challenge statements mention is defined HERE, from Mathlib alone, in the namespace `IntegralityGap`,
CHARACTER FOR CHARACTER as in Zeta23/PairCeiling/GridParseval.lean, GridCorner.lean and GridParsevalRat.lean (so that the
untrusted solution can delegate to those files by definitional unfolding):
  chi ζ x            := ζ ^ x.val                          the additive character of ZMod M attached to an M-th root of unity;
  dftMark ζ m r      := Σ_k (m k : K) · chi ζ (r·k)         the form factor (DFT) of an INTEGER mark vector on the M-site grid;
  dftMarkQ ζ m r     := Σ_k (m k : F) · chi ζ (r·k)         the same for a RATIONAL mark vector, over a field F (the cast ℚ → F
                                                            needs a division ring: item 10's typing fact);
  zetaM M            := exp (2πi / M)                       the standard primitive M-th root of unity in ℂ;
  gridRow n m        := Σ_{j₁,j₂ ∈ [−n, n]} (1/(2n+1))² |c_{j₁+j₂}|²   the literal SPEC-1.4 bandwidth-one Frobenius row of a grid
                                                            configuration with integer marks, M = 2n + 1 sites, band {−n, …, n};
  gridRowQ n m       := the same row with rational marks;
  fracMark k         := if k.val < 48 then 4/3 else 0       the zoo's mark-4/3 column at N = 64: 48 atoms of mark 4/3 on the
                                                            65-site grid (BARRIER-ZOO.md item 10).
The master inequality (MI) `3·Σm − Σm² ≤ 2·N_d` and the corner `N_d ≥ N(5/6 − (2/3)ε)` are written out in the challenge
statements themselves with `Finset.sum` and `Finset.card` — no further vocabulary.  A reader who wants to know WHAT is claimed
reads this file and the challenge file only.
-/
import Mathlib

namespace IntegralityGap

noncomputable section

open Finset

variable {K : Type*} [CommRing K] {M : ℕ} [NeZero M]

/-- the additive character of `ZMod M` attached to an `M`-th root of unity `ζ`: `x ↦ ζ ^ x.val`. -/
def chi (ζ : K) (x : ZMod M) : K := ζ ^ x.val

/-- the form factor (DFT) of an integer mark vector on the `M`-site grid: `c_r = Σ_k m_k ζ^{(r·k).val}`. -/
def dftMark (ζ : K) (m : ZMod M → ℤ) (r : ZMod M) : K :=
  ∑ k : ZMod M, (m k : K) * chi ζ (r * k)

/-- the form factor (DFT) of a RATIONAL mark vector on the `M`-site grid, over a field `F`. -/
def dftMarkQ {F : Type*} [Field F] (ζ : F) (m : ZMod M → ℚ) (r : ZMod M) : F :=
  ∑ k : ZMod M, (m k : F) * chi ζ (r * k)

/-- the standard primitive `M`-th root of unity `e^{2πi/M}` in `ℂ`. -/
def zetaM (M : ℕ) : ℂ := Complex.exp (2 * Real.pi * Complex.I / M)

/-- the literal SPEC-1.4 bandwidth-one Frobenius row of a grid configuration with INTEGER marks:
`tr Ĝ² = Σ_{j₁,j₂ ∈ B} (1/M)² |c_{j₁+j₂}|²`, `M = 2n+1`, `B = {−n, …, n}`. -/
def gridRow (n : ℕ) (m : ZMod (2 * n + 1) → ℤ) : ℝ :=
  ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
    (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) *
      Complex.normSq (dftMark (zetaM (2 * n + 1)) m
        ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1))))

/-- the same Frobenius row of a grid configuration with RATIONAL marks. -/
def gridRowQ (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) : ℝ :=
  ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
    (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) *
      Complex.normSq (dftMarkQ (zetaM (2 * n + 1)) m
        ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1))))

/-- the zoo's mark-4/3 column at `N = 64`: 48 atoms of mark `4/3` on distinct sites of the 65-site grid. -/
def fracMark : ZMod 65 → ℚ := fun k => if k.val < 48 then 4 / 3 else 0

end

end IntegralityGap
