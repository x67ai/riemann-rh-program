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
import Mathlib.Algebra.Order.Chebyshev

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

/-! ## 4. Prop. 4.5 (paper §4.2 = pair-channel.md Prop. 3.1): the vacancy lattice plus one pair at the hole, every `n`, `d`, `μ` -/

/-- on the band `|s| ≤ 2n` the residue `(s : ZMod (2n+1))` vanishes only at `s = 0`. -/
lemma intCast_zmod_eq_zero_iff (n : ℕ) (s : ℤ) (hs : s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ))) :
    ((s : ZMod (2 * n + 1)) = 0) ↔ s = 0 := by
  rw [Finset.mem_Icc] at hs
  constructor
  · intro h
    rw [ZMod.intCast_zmod_eq_zero_iff_dvd] at h
    exact int_eq_zero_of_dvd_of_bounds (by positivity) h (by push_cast; omega) (by push_cast; omega)
  · rintro rfl
    simp

/-- the atom form factor of the vacancy lattice (paper §4.2: "φ₀(s) = 64 at s ≡ 0 and −1 otherwise" at n = 32): on the band it is
`2n` at `s = 0` and `−1` elsewhere — character orthogonality minus the missing hole. -/
lemma dftMarkQ_vacancy (n : ℕ) (s : ℤ) (hs : s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ))) :
    dftMarkQ (zetaM (2 * n + 1)) (vacancyMark n) (s : ZMod (2 * n + 1))
      = (((if s = 0 then 2 * (n : ℝ) else -1) : ℝ) : ℂ) := by
  have hζ := isPrimitiveRoot_zetaM (2 * n + 1)
  unfold dftMarkQ vacancyMark
  have hterm : ∀ k : ZMod (2 * n + 1),
      (((if k = 0 then (0 : ℚ) else 1) : ℚ) : ℂ) * chi (zetaM (2 * n + 1)) ((s : ZMod (2 * n + 1)) * k)
        = chi (zetaM (2 * n + 1)) (k * (s : ZMod (2 * n + 1))) - (if k = 0 then 1 else 0) := by
    intro k
    by_cases hk : k = 0
    · subst hk
      simp
    · simp only [hk, if_false, Rat.cast_one, one_mul, sub_zero, mul_comm]
  rw [Finset.sum_congr rfl fun k _ => hterm k, Finset.sum_sub_distrib, sum_chi_mul hζ,
    Finset.sum_ite_eq', if_pos (Finset.mem_univ _)]
  by_cases hs0 : s = 0
  · rw [if_pos ((intCast_zmod_eq_zero_iff n s hs).2 hs0), if_pos hs0]
    push_cast
    ring
  · rw [if_neg (fun h => hs0 ((intCast_zmod_eq_zero_iff n s hs).1 h)), if_neg hs0]
    push_cast
    ring

/-- `W2(0) = 1/M`: at `s = 0` the filter is the whole band. -/
lemma W2_zero (n : ℕ) : W2 n 0 = 1 / (2 * (n : ℝ) + 1) := by
  rw [W2_eq n 0 (by rw [Finset.mem_Icc]; omega), Int.cast_zero, abs_zero, sub_zero,
    div_eq_div_iff (by positivity) (by positivity)]
  ring

/-- `ā(0) = 1`: the flat weights sum to `1`. -/
lemma abar_zero (n : ℕ) : abar n 0 = 1 := by
  unfold abar
  have h : ∀ j : ℤ, (1 / (2 * (n : ℝ) + 1)) * Real.cosh (2 * Real.pi * (j : ℝ) * 0 / (2 * (n : ℝ)))
      = 1 / (2 * (n : ℝ) + 1) := by
    intro j
    rw [show 2 * Real.pi * (j : ℝ) * 0 / (2 * (n : ℝ)) = 0 by ring, Real.cosh_zero, mul_one]
  rw [Finset.sum_congr rfl fun j _ => h j, Finset.sum_const, card_band, nsmul_eq_mul]
  have hM : (2 * (n : ℝ) + 1) ≠ 0 := by positivity
  push_cast
  field_simp

/-- the vacancy lattice has `Σ_k m_k² = 2n` (`M − 1` unit atoms). -/
lemma sum_vacancyMark_sq (n : ℕ) :
    (∑ k : ZMod (2 * n + 1), (vacancyMark n k) ^ 2 : ℚ) = 2 * (n : ℚ) := by
  unfold vacancyMark
  have h : ∀ k : ZMod (2 * n + 1), ((if k = 0 then (0 : ℚ) else 1)) ^ 2 = 1 - (if k = 0 then 1 else 0) := by
    intro k
    split_ifs <;> norm_num
  rw [Finset.sum_congr rfl fun k _ => h k, Finset.sum_sub_distrib, Finset.sum_const, Finset.card_univ,
    ZMod.card, Finset.sum_ite_eq', if_pos (Finset.mem_univ _), nsmul_eq_mul, mul_one]
  push_cast
  ring

/-- the atom part of Prop. 4.5's row: `Σ_s W2(s) φ₀(s)² = 2n` — the agreement lemma, rational Parseval, and the count of atoms. -/
lemma sum_W2_vacancy_sq (n : ℕ) :
    ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)), W2 n s * (if s = 0 then 2 * (n : ℝ) else -1) ^ 2
      = 2 * (n : ℝ) := by
  have h : ∀ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)),
      W2 n s * (if s = 0 then 2 * (n : ℝ) else -1) ^ 2
        = W2 n s * Complex.normSq (pairFormFactor n (vacancyMark n) ∅ s) := by
    intro s hs
    unfold pairFormFactor
    rw [Finset.sum_empty, add_zero, dftMarkQ_vacancy n s hs, Complex.normSq_ofReal]
    ring
  rw [Finset.sum_congr rfl h]
  change pairRow n (vacancyMark n) ∅ = _
  rw [pairRow_eq_gridRowQ, gridRowQ_eq, sum_vacancyMark_sq]
  push_cast
  ring

/-- the pair–hole coupling of Prop. 4.5: `Σ_s W2(s) φ₀(s) cosh(βs) = 1 − ā(d)²` (φ₀ = −1 + M·[s = 0]; (T1); W2(0) = 1/M). -/
lemma sum_W2_vacancy_cosh (n : ℕ) (d : ℝ) :
    ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)),
        W2 n s * (if s = 0 then 2 * (n : ℝ) else -1) * Real.cosh (2 * Real.pi * (s : ℝ) * d / (2 * (n : ℝ)))
      = 1 - abar n d ^ 2 := by
  have hφ : ∀ s : ℤ,
      W2 n s * (if s = 0 then 2 * (n : ℝ) else -1) * Real.cosh (2 * Real.pi * (s : ℝ) * d / (2 * (n : ℝ)))
        = -(W2 n s * Real.cosh (2 * Real.pi * (s : ℝ) * d / (2 * (n : ℝ))))
          + (if s = 0 then (2 * (n : ℝ) + 1) * W2 n s * Real.cosh (2 * Real.pi * (s : ℝ) * d / (2 * (n : ℝ))) else 0) := by
    intro s
    split_ifs <;> ring
  have h0 : (0 : ℤ) ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)) := by
    rw [Finset.mem_Icc]
    omega
  rw [Finset.sum_congr rfl fun s _ => hφ s, Finset.sum_add_distrib, Finset.sum_neg_distrib, sum_W2_cosh n d,
    Finset.sum_ite_eq', if_pos h0, W2_zero, Int.cast_zero]
  rw [show 2 * Real.pi * (0 : ℝ) * d / (2 * (n : ℝ)) = 0 by ring, Real.cosh_zero]
  have hM : (2 * (n : ℝ) + 1) ≠ 0 := by positivity
  field_simp
  ring

/-- the pair's own term of Prop. 4.5: `Σ_s W2(s) cosh²(βs) = (1 + ā(2d)²)/2` — `cosh² y = (1 + cosh 2y)/2` and (T1) at `0` and `2d`. -/
lemma sum_W2_cosh_sq (n : ℕ) (d : ℝ) :
    ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)),
        W2 n s * Real.cosh (2 * Real.pi * (s : ℝ) * d / (2 * (n : ℝ))) ^ 2
      = (1 + abar n (2 * d) ^ 2) / 2 := by
  have hc2 : ∀ s : ℤ, W2 n s * Real.cosh (2 * Real.pi * (s : ℝ) * d / (2 * (n : ℝ))) ^ 2
      = (1 / 2) * (W2 n s * Real.cosh (2 * Real.pi * (s : ℝ) * 0 / (2 * (n : ℝ)))
          + W2 n s * Real.cosh (2 * Real.pi * (s : ℝ) * (2 * d) / (2 * (n : ℝ)))) := by
    intro s
    have h2 : 2 * Real.pi * (s : ℝ) * (2 * d) / (2 * (n : ℝ))
        = 2 * (2 * Real.pi * (s : ℝ) * d / (2 * (n : ℝ))) := by ring
    have h0 : 2 * Real.pi * (s : ℝ) * 0 / (2 * (n : ℝ)) = 0 := by ring
    rw [h2, h0, Real.cosh_two_mul, Real.cosh_sq, Real.cosh_zero]
    ring
  rw [Finset.sum_congr rfl fun s _ => hc2 s, ← Finset.mul_sum, Finset.sum_add_distrib, sum_W2_cosh n 0,
    sum_W2_cosh n (2 * d), abar_zero]
  ring

/-- **Prop. 4.5 (paper §4.2; pair-channel.md Prop. 3.1), for every `n`, every depth `d` and every REAL mark `μ`**: on the vacancy
lattice (unit atoms on the `2n` sites `k ≠ 0`) plus one pair at the hole `0` with mark `μ` and depth `d`,

    `F1 − S2 = 2μ² ā(2d)² − 4μ (ā(d)² − 1)`,   `S2 = 2n + 2μ²`,

exactly.  Proof: the form factor is the real number `φ₀(s) + 2μ cosh(βs)` (`dftMarkQ_vacancy`, the pair's phase at the hole is `1`),
and the three sums of its square are `sum_W2_vacancy_sq`, `sum_W2_vacancy_cosh`, `sum_W2_cosh_sq`.  No hypothesis on `n`, `d`, `μ`;
the sign of the right side for real marks is the certificate's business (PairCert.lean), the integer-mark sign is
`floor_holds_integer` below. -/
theorem prop45 (n : ℕ) (d μ : ℝ) :
    pairRow n (vacancyMark n) {((0 : ZMod (2 * n + 1)), μ, d)} - (2 * (n : ℝ) + 2 * μ ^ 2)
      = 2 * μ ^ 2 * abar n (2 * d) ^ 2 - 4 * μ * (abar n d ^ 2 - 1) := by
  have hsummand : ∀ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)),
      W2 n s * Complex.normSq (pairFormFactor n (vacancyMark n) {((0 : ZMod (2 * n + 1)), μ, d)} s)
        = W2 n s * (if s = 0 then 2 * (n : ℝ) else -1) ^ 2
          + 4 * μ * (W2 n s * (if s = 0 then 2 * (n : ℝ) else -1)
              * Real.cosh (2 * Real.pi * (s : ℝ) * d / (2 * (n : ℝ))))
          + 4 * μ ^ 2 * (W2 n s * Real.cosh (2 * Real.pi * (s : ℝ) * d / (2 * (n : ℝ))) ^ 2) := by
    intro s hs
    unfold pairFormFactor
    rw [Finset.sum_singleton]
    dsimp only
    rw [dftMarkQ_vacancy n s hs, mul_zero, chi_zero, mul_one, ← Complex.ofReal_add, Complex.normSq_ofReal]
    ring
  unfold pairRow
  rw [Finset.sum_congr rfl hsummand, Finset.sum_add_distrib, Finset.sum_add_distrib, ← Finset.mul_sum,
    ← Finset.mul_sum, sum_W2_vacancy_sq, sum_W2_vacancy_cosh, sum_W2_cosh_sq]
  ring

/-! ## 5. The integer-mark safety chain (pair-channel.md (T3); paper §4.2 "For integer marks the same family is safe") -/

/-- `1 ≤ ā(x)`: every `cosh` is `≥ 1` and the flat weights sum to `1`. -/
lemma one_le_abar (n : ℕ) (x : ℝ) : 1 ≤ abar n x := by
  have h : ∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), (1 / (2 * (n : ℝ) + 1)) ≤ abar n x := by
    unfold abar
    refine Finset.sum_le_sum fun j _ => ?_
    have hu : 0 ≤ 1 / (2 * (n : ℝ) + 1) := by positivity
    calc 1 / (2 * (n : ℝ) + 1) = 1 / (2 * (n : ℝ) + 1) * 1 := (mul_one _).symm
      _ ≤ _ := mul_le_mul_of_nonneg_left (Real.one_le_cosh _) hu
  rw [Finset.sum_const, card_band, nsmul_eq_mul] at h
  have hM : (2 * (n : ℝ) + 1) ≠ 0 := by positivity
  calc (1 : ℝ) = ((2 * n + 1 : ℕ) : ℝ) * (1 / (2 * (n : ℝ) + 1)) := by
        push_cast
        field_simp
    _ ≤ abar n x := h

/-- **the log-convexity step** (pair-channel.md (T3), paper §4.2 "Cauchy–Schwarz on the positive weights"):
`ā(d)² ≤ (1 + ā(2d))/2` — `(Σ u_j C_j)² ≤ (Σ u_j)(Σ u_j C_j²)` with the flat weights and `cosh² = (1 + cosh 2x)/2`. -/
theorem abar_sq_le (n : ℕ) (d : ℝ) : abar n d ^ 2 ≤ (1 + abar n (2 * d)) / 2 := by
  have hM : (2 * (n : ℝ) + 1) ≠ 0 := by positivity
  have hsq : ∀ j : ℤ, Real.cosh (2 * Real.pi * (j : ℝ) * d / (2 * (n : ℝ))) ^ 2
      = (1 / 2) * (1 + Real.cosh (2 * Real.pi * (j : ℝ) * (2 * d) / (2 * (n : ℝ)))) := by
    intro j
    have h2 : 2 * Real.pi * (j : ℝ) * (2 * d) / (2 * (n : ℝ))
        = 2 * (2 * Real.pi * (j : ℝ) * d / (2 * (n : ℝ))) := by ring
    rw [h2, Real.cosh_two_mul, Real.cosh_sq]
    ring
  have hCS := sq_sum_le_card_mul_sum_sq (s := Finset.Icc (-(n : ℤ)) (n : ℤ))
    (f := fun j : ℤ => Real.cosh (2 * Real.pi * (j : ℝ) * d / (2 * (n : ℝ))))
  rw [card_band] at hCS
  have h1 : abar n d = (1 / (2 * (n : ℝ) + 1))
      * ∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), Real.cosh (2 * Real.pi * (j : ℝ) * d / (2 * (n : ℝ))) := by
    unfold abar
    rw [Finset.mul_sum]
  have h2 : abar n (2 * d) = (1 / (2 * (n : ℝ) + 1))
      * ∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), Real.cosh (2 * Real.pi * (j : ℝ) * (2 * d) / (2 * (n : ℝ))) := by
    unfold abar
    rw [Finset.mul_sum]
  have h3 : ∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), Real.cosh (2 * Real.pi * (j : ℝ) * d / (2 * (n : ℝ))) ^ 2
      = (1 / 2) * (((2 * n + 1 : ℕ) : ℝ)
        + ∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), Real.cosh (2 * Real.pi * (j : ℝ) * (2 * d) / (2 * (n : ℝ)))) := by
    rw [Finset.sum_congr rfl fun j _ => hsq j, ← Finset.mul_sum, Finset.sum_add_distrib, Finset.sum_const, card_band,
      nsmul_eq_mul, mul_one]
  rw [h1, h2]
  rw [h3] at hCS
  set S := ∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), Real.cosh (2 * Real.pi * (j : ℝ) * d / (2 * (n : ℝ))) with hS
  set S2 := ∑ j ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), Real.cosh (2 * Real.pi * (j : ℝ) * (2 * d) / (2 * (n : ℝ))) with hS2
  push_cast at hCS
  have hkey : (1 / (2 * (n : ℝ) + 1) * S) ^ 2 = (1 / (2 * (n : ℝ) + 1)) ^ 2 * S ^ 2 := by ring
  rw [hkey]
  calc (1 / (2 * (n : ℝ) + 1)) ^ 2 * S ^ 2
      ≤ (1 / (2 * (n : ℝ) + 1)) ^ 2 * ((2 * (n : ℝ) + 1) * ((1 / 2) * ((2 * (n : ℝ) + 1) + S2))) := by
        gcongr
    _ = (1 + 1 / (2 * (n : ℝ) + 1) * S2) / 2 := by
        field_simp

/-- **the integer-mark safety chain, a theorem** (paper §4.2: "For integer marks the same family is safe … F1 − S2 ≥
2m²ā(2d)² − 2m(ā(2d) − 1) > 0"): for an INTEGER mark `m ≥ 1`, the right side of `prop45` is positive — with `A = ā(2d) ≥ 1` and
`ā(d)² ≤ (1 + A)/2` it is `≥ 2m(mA² − A + 1) > 0`.  This is where integrality enters, as `1 ≤ m`; nothing else about the
marks is used, and the atom theorems `per_atom_slack` / `mi_holds_integer` (GridGap.lean) are not involved. -/
theorem floor_holds_integer (n : ℕ) (d : ℝ) (m : ℕ) (hm : 1 ≤ m) :
    0 < 2 * (m : ℝ) ^ 2 * abar n (2 * d) ^ 2 - 4 * (m : ℝ) * (abar n d ^ 2 - 1) := by
  have hmR : (1 : ℝ) ≤ m := by exact_mod_cast hm
  have hA : 1 ≤ abar n (2 * d) := one_le_abar n (2 * d)
  have hCS : abar n d ^ 2 ≤ (1 + abar n (2 * d)) / 2 := abar_sq_le n d
  have h1 : 4 * (m : ℝ) * (abar n d ^ 2 - 1) ≤ 2 * (m : ℝ) * (abar n (2 * d) - 1) := by
    nlinarith
  have hc : 0 < abar n (2 * d) ^ 2 - abar n (2 * d) + 1 := by
    nlinarith [sq_nonneg (abar n (2 * d) - 1 / 2)]
  have hmc := mul_pos (by linarith : (0 : ℝ) < m) hc
  have h2 : 2 * (m : ℝ) * (abar n (2 * d) - 1) < 2 * (m : ℝ) ^ 2 * abar n (2 * d) ^ 2 := by
    nlinarith [mul_nonneg (mul_nonneg (by linarith : (0 : ℝ) ≤ m) (sub_nonneg.2 hmR)) (sq_nonneg (abar n (2 * d)))]
  linarith

end PairRow
end PairCeiling
end Zeta23
