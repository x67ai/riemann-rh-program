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
comparator/ChallengeDeps/PairChannel.lean — the TRUSTED definition layer for the comparator topic `PairChannel`
(barrier-zoo IV.17's PAIR CHANNEL: Prop. 4.5 of the A4 no-go paper §4.2 = pair-channel.md Prop. 3.1, the integer-mark safety
chain, and the floor's failure at the anchor; unit brief rh-program/results/h4-pair-typing-s32/UNIT-BRIEF.md; build record
rh-program/results/h4-pair-lean-s33/BUILD-NOTES.md).

Everything the challenge statements mention is defined HERE, from Mathlib alone, in the namespace `PairChannel`.  The first
seven definitions are CHARACTER FOR CHARACTER those of comparator/ChallengeDeps/IntegralityGap.lean (namespace `IntegralityGap`),
themselves character for character the Zeta23/PairCeiling/{GridParseval, GridCorner, GridParsevalRat}.lean originals; the
statements of this topic mention `chi`, `dftMarkQ`, `zetaM`, `gridRowQ` of them, and `dftMark`, `gridRow`, `fracMark` are
restated only so that the trusted layer of the two IV.17 topics is one and the same vocabulary.  The five new definitions are
character for character those of Zeta23/PairCeiling/PairRow.lean (so that the untrusted solution can delegate to that file
and to PairCert.lean by definitional unfolding):
  W2 n s              := Σ_{j ∈ B, s−j ∈ B} (1/M)²         the flat-weight autocorrelation w = u ∗ u of paper §2.3 at u_j = 1/M,
                                                            B = {−n, …, n}, M = 2n + 1 (pair-channel.md line 39: (65 − |s|)/65²);
  pairFormFactor n m pairs s := c_s                        the form factor at the UNREDUCED integer frequency s: the atoms' DFT
                                                            at the reduced residue (s : ZMod M) plus, per pair (θ, μ, d) on the
                                                            grid site θ with REAL mark μ and depth d, 2μ cosh(2π s d / N) χ(s·θ)
                                                            at the unreduced (s : ℝ), N = 2n (paper §2.3: "a conjugate pair at
                                                            θ ± id contributes 2m cosh(2πsd/N) e^{−2πisθ/N}");
  pairRow n m pairs   := Σ_{s ∈ [−2n, 2n]} W2 n s |c_s|²   the bandwidth-one Frobenius row F1 of paper §2.3 with pairs;
  abar n x            := Σ_{j ∈ B} (1/M) cosh(2π j x / N)  ā(x) = ψ(ix) of pair-channel.md line 69;
  vacancyMark n       := (k ↦ if k = 0 then 0 else 1)      the vacancy lattice of Prop. 4.5: unit atoms off the hole 0.
The quantity S2 = 2n + 2μ² and the pair at the hole `{(0, μ, d)}` are written out in the challenge statements themselves.
A reader who wants to know WHAT is claimed reads this file and the challenge file only.
-/
import Mathlib

namespace PairChannel

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

/-- the assembly weight of paper §2.3 at the flat harmonics `u_j = 1/(2n+1)`: `W2(s) = Σ_{j ∈ B, s−j ∈ B} u_j u_{s−j}`,
the autocorrelation `w = u ∗ u` on the band `B = {−n, …, n}` (pair-channel.md line 39: `w_s = (65 − |s|)/65²`, `W2_eq`). -/
def W2 (n : ℕ) (s : ℤ) : ℝ :=
  ∑ _j ∈ (Finset.Icc (-(n : ℤ)) (n : ℤ)).filter (fun j : ℤ => s - j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ)),
    (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1))

/-- the pair-containing form factor at the UNREDUCED integer frequency `s`: grid atoms with rational marks `m` (their DFT
at the reduced residue `(s : ZMod (2n+1))` — periodic, so harmless) plus, per pair `(θ, μ, d)` on the grid site `θ` with
real mark `μ` and real depth `d`, the factor `2μ cosh(2π s d / N)` at the unreduced `(s : ℝ)` times the character
`χ(s·θ)` (paper §2.3: "a conjugate pair at θ ± id contributes 2m cosh(2πsd/N) e^{−2πisθ/N}"; the sign of the character is
immaterial under `normSq`). -/
def pairFormFactor (n : ℕ) (m : ZMod (2 * n + 1) → ℚ)
    (pairs : Finset (ZMod (2 * n + 1) × ℝ × ℝ)) (s : ℤ) : ℂ :=
  dftMarkQ (zetaM (2 * n + 1)) m (s : ZMod (2 * n + 1))
    + ∑ p ∈ pairs,
        ((2 * p.2.1 * Real.cosh (2 * Real.pi * (s : ℝ) * p.2.2 / (2 * (n : ℝ))) : ℝ) : ℂ)
          * chi (zetaM (2 * n + 1)) ((s : ZMod (2 * n + 1)) * p.1)

/-- the bandwidth-one Frobenius row of paper §2.3 over the unreduced frequencies `s ∈ [−2n, 2n]`:
`F1 = Σ_s W2(s) |c_s|²`. -/
def pairRow (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) (pairs : Finset (ZMod (2 * n + 1) × ℝ × ℝ)) : ℝ :=
  ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)), W2 n s * Complex.normSq (pairFormFactor n m pairs s)

/-- `ā(x) = ψ(ix) = Σ_j u_j cosh(2π j x / N)` of pair-channel.md line 69, with `u_j = 1/(2n+1)`, `N = 2n`. -/
def abar (n : ℕ) (x : ℝ) : ℝ :=
  ∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), (1 / (2 * (n : ℝ) + 1)) * Real.cosh (2 * Real.pi * (j : ℝ) * x / (2 * (n : ℝ)))

/-- the vacancy lattice of Prop. 4.5: unit atoms on every grid site except the hole `0`. -/
def vacancyMark (n : ℕ) : ZMod (2 * n + 1) → ℚ := fun k => if k = 0 then 0 else 1

end

end PairChannel
