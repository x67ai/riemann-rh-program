/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it.
-/
/-
Zeta23/PairCeiling/PairRow.lean — the PAIR-CONTAINING bandwidth-one Frobenius row at the UNREDUCED integer frequency
(A4 no-go paper §2.3, line "tr Ĝ² = Σ_s W2(s) |c_s|²" with a conjugate pair contributing 2m cosh(2πsd/N) e^{−2πisθ/N}),
its agreement with the shipped grid row on pair-free columns, the generating identity (T1) of pair-channel.md at
imaginary argument, Prop. 4.5 of the paper (= pair-channel.md Prop. 3.1) for every n, depth and real mark, and the
integer-mark safety chain.  Barrier-zoo IV.17's pair channel; formalization-queue item 10's sub-item; unit brief
rh-program/results/h4-pair-typing-s32/UNIT-BRIEF.md, typing note TYPING-NOTE.md there, build record
rh-program/results/h4-pair-lean-s33/BUILD-NOTES.md.

WHY A NEW ROW.  The shipped rows `gridRow` / `gridRowQ` (GridCorner.lean, GridParsevalRat.lean) index the form factor at
the REDUCED residue `(j₁ : ZMod M) + (j₂ : ZMod M)`, which is right for grid atoms (their DFT is periodic mod M) and wrong
for a pair: the pair's factor 2μ cosh(2πsd/N) grows with |s| and is not periodic mod M = 2n + 1.  So this file defines the
paper's single-convolution row `pairRow` over the integer frequency s ∈ [−2n, 2n] with the flat-weight autocorrelation
`W2 n s = Σ_{j ∈ B, s − j ∈ B} (1/M)²` (u_j = 1/M substituted; the paper's W2 for general u is not needed), and proves
  `pairRow_eq_gridRowQ` — with no pair the new row IS the shipped rational row (the agreement lemma);
  `W2_eq`           — the closed form (M − |s|)/M² of pair-channel.md line 39;
  `sum_W2_mul`      — the generic regrouping of the single s-sum into the double band sum;
  `sum_W2_cosh`     — (T1) at q = e^{β}: Σ_s W2(s) cosh(2πsx/N) = ā(x)², ā(x) = Σ_j (1/M) cosh(2πjx/N);
  `prop45`          — F1 − S2 = 2μ²ā(2d)² − 4μ(ā(d)² − 1) on the vacancy lattice plus one pair at the hole, every n, d, μ;
  `abar_sq_le`      — ā(d)² ≤ (1 + ā(2d))/2 (Cauchy–Schwarz with the flat weights and cosh² = (1 + cosh 2x)/2);
  `floor_holds_integer` — for an INTEGER mark m ≥ 1 the expression of `prop45` is > 0: integrality enters here, as 1 ≤ m.
The certificate at the anchor (d, μ) = (1/4, 1/20), n = 32 — the floor F1 ≥ S2 FAILS for this real mark — is the separate
module PairCert.lean.  Conventions: M = 2n + 1 grid sites, circle length N = 2n (GridParseval.lean line "Even period N = 2n");
pairs sit on grid sites (a restriction of the paper's row, which allows any real θ_p; Prop. 4.5 needs only the hole g₀ = 0);
atom marks ℚ (the shipped vocabulary), pair marks ℝ (Prop. 4.5's "REAL mark μ").

WHAT IS NOT HERE.  Nothing about (MI) at any anchor (at the anchor of PairCert.lean (MI) HOLDS: F1 − T = +3.67 with
T = 3M − 2N_d; only the floor F1 ≥ S2 fails); nothing about Theorems 4.6–4.9 of the paper (the pair channel's closure at
paper grade); no law, no LP, no general-position pair; nothing about ζ.

Trust model: everything is proved from Mathlib with no `sorry` and no `native_decide`; the transcendental objects are
`Complex.exp` through `zetaM` (as in GridParseval.lean), `Real.cosh`/`Real.sinh` and `Real.pi`.
-/
import Zeta23.PairCeiling.GridParsevalRat
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp

noncomputable section

open Finset

namespace Zeta23
namespace PairCeiling
namespace PairRow

open GridParseval GridParsevalRat

/-! ## 1. The row -/

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

/-! ## 2. The weight: closed form, and the regrouping of the single sum into the double band sum -/

/-- the band has `2n + 1` harmonics. -/
lemma card_band (n : ℕ) : (Finset.Icc (-(n : ℤ)) (n : ℤ)).card = 2 * n + 1 := by
  rw [Int.card_Icc]
  omega

/-- **the closed-form weight** of pair-channel.md line 39: `W2(s) = (M − |s|)/M²` for `|s| ≤ 2n`, `M = 2n + 1` — the
number of ordered pairs `(j, s − j)` in `B × B` is `M − |s|`. -/
theorem W2_eq (n : ℕ) (s : ℤ) (hs : s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ))) :
    W2 n s = ((2 * (n : ℝ) + 1) - |(s : ℝ)|) / (2 * (n : ℝ) + 1) ^ 2 := by
  rw [Finset.mem_Icc] at hs
  have hcard : ((Finset.Icc (-(n : ℤ)) (n : ℤ)).filter
      (fun j : ℤ => s - j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ))).card = (2 * (n : ℤ) + 1 - |s|).toNat := by
    rcases (by omega : 0 ≤ s ∨ s < 0) with h | h
    · have hset : (Finset.Icc (-(n : ℤ)) (n : ℤ)).filter
          (fun j : ℤ => s - j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ)) = Finset.Icc (s - n) n := by
        ext j
        simp only [Finset.mem_filter, Finset.mem_Icc]
        omega
      rw [hset, Int.card_Icc, abs_of_nonneg h]
      omega
    · have hset : (Finset.Icc (-(n : ℤ)) (n : ℤ)).filter
          (fun j : ℤ => s - j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ)) = Finset.Icc (-(n : ℤ)) (s + n) := by
        ext j
        simp only [Finset.mem_filter, Finset.mem_Icc]
        omega
      rw [hset, Int.card_Icc, abs_of_neg h]
      omega
  have hnonneg : 0 ≤ 2 * (n : ℤ) + 1 - |s| := by
    rcases abs_cases s with ⟨h1, _⟩ | ⟨h1, _⟩ <;> omega
  have hcast : (((2 * (n : ℤ) + 1 - |s|).toNat : ℕ) : ℝ) = 2 * (n : ℝ) + 1 - |(s : ℝ)| := by
    have h1 : (((2 * (n : ℤ) + 1 - |s|).toNat : ℕ) : ℤ) = 2 * (n : ℤ) + 1 - |s| :=
      Int.toNat_of_nonneg hnonneg
    have h2 := congrArg (Int.cast : ℤ → ℝ) h1
    push_cast at h2
    exact h2
  unfold W2
  rw [Finset.sum_const, hcard, nsmul_eq_mul, hcast]
  have hM : (2 * (n : ℝ) + 1) ≠ 0 := by positivity
  field_simp

/-- **the generic regrouping**: the single sum over the frequency `s` weighted by `W2` is the double sum over the band,
`Σ_s W2(s) g(s) = Σ_{j₁, j₂ ∈ B} (1/M)² g(j₁ + j₂)` — for every `g`.  (For fixed `j₁` the inner sum is reindexed by
`s = j₁ + j₂`; then the two sums are swapped and the inner one is `W2 n s` by definition.) -/
theorem sum_W2_mul (n : ℕ) (g : ℤ → ℝ) :
    ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)), W2 n s * g s
      = ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) * g (j1 + j2) := by
  have hinner : ∀ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
      ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) * g (j1 + j2)
        = ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)),
            if s - j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ) then
              (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) * g s else 0 := by
    intro j1 hj1
    rw [Finset.mem_Icc] at hj1
    rw [← Finset.sum_filter]
    refine Finset.sum_nbij' (fun j2 => j1 + j2) (fun s => s - j1) ?_ ?_ ?_ ?_ ?_
    · intro j2 hj2
      rw [Finset.mem_Icc] at hj2
      simp only [Finset.mem_filter, Finset.mem_Icc]
      omega
    · intro s hs
      simp only [Finset.mem_filter, Finset.mem_Icc] at hs
      rw [Finset.mem_Icc]
      omega
    · intro j2 _
      simp
    · intro s _
      simp
    · intro j2 _
      rfl
  rw [Finset.sum_congr rfl hinner, Finset.sum_comm]
  refine Finset.sum_congr rfl fun s _ => ?_
  rw [← Finset.sum_filter]
  unfold W2
  rw [Finset.sum_mul]

/-! ## 3. The agreement lemma and (T1) -/

/-- **the agreement lemma**: with no pair, the unreduced row IS the shipped rational grid row, `pairRow n m ∅ = gridRowQ n m`
(the regrouping, then `((j₁ + j₂ : ℤ) : ZMod M) = (j₁ : ZMod M) + (j₂ : ZMod M)`).  With `gridRowQ_eq` this is the
atom-only Parseval `pairRow n m ∅ = Σ_k m_k²` on the new row. -/
theorem pairRow_eq_gridRowQ (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) :
    pairRow n m ∅ = gridRowQ n m := by
  unfold pairRow pairFormFactor
  simp only [Finset.sum_empty, add_zero]
  rw [sum_W2_mul n (fun s : ℤ => Complex.normSq (dftMarkQ (zetaM (2 * n + 1)) m (s : ZMod (2 * n + 1))))]
  unfold gridRowQ
  refine Finset.sum_congr rfl fun j1 _ => Finset.sum_congr rfl fun j2 _ => ?_
  simp only [Int.cast_add]

/-- the flat-weight sinh sum vanishes on the symmetric band (the involution `j ↦ −j`). -/
lemma sum_sinh_band (n : ℕ) (x : ℝ) :
    ∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
      (1 / (2 * (n : ℝ) + 1)) * Real.sinh (2 * Real.pi * (j : ℝ) * x / (2 * (n : ℝ))) = 0 := by
  refine Finset.sum_involution (fun j _ => -j) ?_ ?_ ?_ ?_
  · intro j _
    have h : 2 * Real.pi * ((-j : ℤ) : ℝ) * x / (2 * (n : ℝ))
        = -(2 * Real.pi * (j : ℝ) * x / (2 * (n : ℝ))) := by
      push_cast
      ring
    rw [h, Real.sinh_neg]
    ring
  · intro j _ hne hj
    apply hne
    have h0 : j = 0 := by omega
    subst h0
    simp
  · intro j hj
    rw [Finset.mem_Icc] at hj ⊢
    omega
  · intro j _
    simp

/-- **(T1) at imaginary argument** (pair-channel.md line 71 at `q = e^{β}`, `β = 2πx/N`):
`Σ_s W2(s) cosh(2πsx/N) = ā(x)²` — the regrouping, `cosh(a + b) = cosh a cosh b + sinh a sinh b`, and the vanishing sinh sum. -/
theorem sum_W2_cosh (n : ℕ) (x : ℝ) :
    ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)),
        W2 n s * Real.cosh (2 * Real.pi * (s : ℝ) * x / (2 * (n : ℝ))) = abar n x ^ 2 := by
  rw [sum_W2_mul n (fun s : ℤ => Real.cosh (2 * Real.pi * (s : ℝ) * x / (2 * (n : ℝ))))]
  have hadd : ∀ j1 j2 : ℤ,
      (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1))
          * Real.cosh (2 * Real.pi * ((j1 + j2 : ℤ) : ℝ) * x / (2 * (n : ℝ)))
        = ((1 / (2 * (n : ℝ) + 1)) * Real.cosh (2 * Real.pi * (j1 : ℝ) * x / (2 * (n : ℝ))))
            * ((1 / (2 * (n : ℝ) + 1)) * Real.cosh (2 * Real.pi * (j2 : ℝ) * x / (2 * (n : ℝ))))
          + ((1 / (2 * (n : ℝ) + 1)) * Real.sinh (2 * Real.pi * (j1 : ℝ) * x / (2 * (n : ℝ))))
            * ((1 / (2 * (n : ℝ) + 1)) * Real.sinh (2 * Real.pi * (j2 : ℝ) * x / (2 * (n : ℝ)))) := by
    intro j1 j2
    have h : 2 * Real.pi * ((j1 + j2 : ℤ) : ℝ) * x / (2 * (n : ℝ))
        = 2 * Real.pi * (j1 : ℝ) * x / (2 * (n : ℝ)) + 2 * Real.pi * (j2 : ℝ) * x / (2 * (n : ℝ)) := by
      push_cast
      ring
    rw [h, Real.cosh_add]
    ring
  have key : (∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (1 / (2 * (n : ℝ) + 1)) * Real.cosh (2 * Real.pi * (j : ℝ) * x / (2 * (n : ℝ))))
        * (∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (1 / (2 * (n : ℝ) + 1)) * Real.cosh (2 * Real.pi * (j : ℝ) * x / (2 * (n : ℝ))))
      + (∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (1 / (2 * (n : ℝ) + 1)) * Real.sinh (2 * Real.pi * (j : ℝ) * x / (2 * (n : ℝ))))
        * (∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (1 / (2 * (n : ℝ) + 1)) * Real.sinh (2 * Real.pi * (j : ℝ) * x / (2 * (n : ℝ))))
      = ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (((1 / (2 * (n : ℝ) + 1)) * Real.cosh (2 * Real.pi * (j1 : ℝ) * x / (2 * (n : ℝ))))
            * ((1 / (2 * (n : ℝ) + 1)) * Real.cosh (2 * Real.pi * (j2 : ℝ) * x / (2 * (n : ℝ))))
          + ((1 / (2 * (n : ℝ) + 1)) * Real.sinh (2 * Real.pi * (j1 : ℝ) * x / (2 * (n : ℝ))))
            * ((1 / (2 * (n : ℝ) + 1)) * Real.sinh (2 * Real.pi * (j2 : ℝ) * x / (2 * (n : ℝ))))) := by
    rw [Finset.sum_mul_sum, Finset.sum_mul_sum, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun j1 _ => ?_
    rw [← Finset.sum_add_distrib]
  rw [Finset.sum_congr rfl fun j1 _ => Finset.sum_congr rfl fun j2 _ => hadd j1 j2, ← key,
    sum_sinh_band n x, mul_zero, add_zero]
  unfold abar
  ring

end PairRow
end PairCeiling
end Zeta23
