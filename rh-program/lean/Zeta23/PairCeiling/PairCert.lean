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
Zeta23/PairCeiling/PairCert.lean — the DYADIC CERTIFICATE at the anchor of paper §4.2 / pair-channel.md Prop. 3.1:
at `n = 32` (N = 64, M = 65), depth `d = 1/4` and REAL mark `μ = 1/20`, the floor `F1 ≥ S2` FAILS on the vacancy lattice
plus one pair at the hole — `floor_fails_anchor : pairRow 32 (vacancyMark 32) {(0, 1/20, 1/4)} < 64 + 2·(1/20)²`
(the record: F1 − S2 = −3.520·10⁻²; the certificate proves F1 − S2 ≤ −0.0336 < 0, spending 0.0015 of the margin).
Unit brief rh-program/results/h4-pair-typing-s32/UNIT-BRIEF.md; typing note TYPING-NOTE.md §4; build record
rh-program/results/h4-pair-lean-s33/BUILD-NOTES.md (with the module's kernel time).

WHAT IS CERTIFIED AND HOW (Route P of the typing note).  By `prop45` (PairRow.lean) the quantity is
`2μ²ā(1/2)² − 4μ(ā(1/4)² − 1)`, increasing in ā(1/2) and decreasing in ā(1/4).  Two generic bounds on cosh,
  `one_add_sq_half_le_cosh :  1 + x²/2 ≤ cosh x`                                              (every x),
  `cosh_le_poly8           :  cosh x ≤ 1 + x²/2 + x⁴/24 + x⁶/720 + x⁸/20160`                  (|x| ≤ 9/2;
                              the ℝ transfer of Mathlib's `Complex.exp_bound'` at n = 8, applied at x and −x),
pass through the flat average ā(x) = (1/65) Σ_{|j| ≤ 32} cosh(2πjx/64) symbolically, leaving the four INTEGER power sums
S₂ = 22880, S₄ = 14492192, S₆ = 10924353440, S₈ = 8964042662432 over j ∈ [−32, 32] (each `decide +kernel`), so that
  ā(1/4) ≥ 1 + (π/128)² S₂/(2·65)         and        ā(1/2) ≤ 1 + Σ_{k=1}^{4} (π/64)^{2k} S_{2k}/((2k)!·65);
Mathlib's `Real.pi_gt_d6 : 3.141592 < π` and `Real.pi_lt_d6 : π < 3.141593` replace π by decimals in the right direction
(monotone even powers), and one `norm_num` decides the final rational inequality
`2·(1/20)²·U² − 4·(1/20)·(L² − 1) < 0` with L = L(3.141592) = 1.10602…, U = U(3.141593) = 1.48152….  Nine kernel-checked
cells, no per-term enclosure, no `native_decide`, no new axiom.

WHAT IS NOT CLAIMED.  Nothing about (MI): at this anchor (MI) HOLDS — T = 3M − 2N_d = 60.3 and F1 − T = +3.67 > 0 — and
`floor_fails_anchor` is the failure of the FLOOR F1 ≥ S2 for a real mark, nothing more (for integer marks the floor holds:
`floor_holds_integer`).  Nothing about Theorems 4.6–4.9 of the paper, laws, the LP, general positions, or ζ.
-/
import Zeta23.PairCeiling.PairRow
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp

noncomputable section

open Finset

namespace Zeta23
namespace PairCeiling
namespace PairCert

open PairRow

/-! ## 1. The two generic cosh bounds -/

/-- **the lower bound** `1 + x²/2 ≤ cosh x` for every real `x`: `cosh x = 1 + 2 sinh²(x/2)` and `|sinh y| = sinh |y| ≥ |y|`. -/
theorem one_add_sq_half_le_cosh (x : ℝ) : 1 + x ^ 2 / 2 ≤ Real.cosh x := by
  have h1 : Real.cosh x = Real.cosh (2 * (x / 2)) := by
    congr 1
    ring
  have h4 : |x / 2| ≤ Real.sinh |x / 2| := Real.self_le_sinh_iff.2 (abs_nonneg _)
  have h5 : Real.sinh |x / 2| = |Real.sinh (x / 2)| := (Real.abs_sinh _).symm
  have h6 : (x / 2) ^ 2 ≤ Real.sinh (x / 2) ^ 2 := by
    rw [← sq_abs (x / 2), ← sq_abs (Real.sinh (x / 2))]
    exact pow_le_pow_left₀ (abs_nonneg _) (h5 ▸ h4) 2
  have h7 : (x / 2) ^ 2 = x ^ 2 / 4 := by ring
  rw [h1, Real.cosh_two_mul, Real.cosh_sq]
  rw [h7] at h6
  linarith

/-- the ℝ transfer of `Complex.exp_bound'` at `n = 8`: for `|x| ≤ 9/2`, `|exp x − Σ_{m<8} xᵐ/m!| ≤ |x|⁸/8! · 2`. -/
lemma exp_sub_sum_le (x : ℝ) (hx : |x| ≤ 9 / 2) :
    |Real.exp x - ∑ m ∈ Finset.range 8, x ^ m / (m.factorial : ℝ)|
      ≤ |x| ^ 8 / (Nat.factorial 8 : ℝ) * 2 := by
  have hxc : ‖(x : ℂ)‖ / ((8 : ℕ).succ : ℝ) ≤ 1 / 2 := by
    rw [Complex.norm_real, Real.norm_eq_abs]
    norm_num
    linarith
  have h := Complex.exp_bound' (x := (x : ℂ)) (n := 8) hxc
  have hsum : (∑ m ∈ Finset.range 8, (x : ℂ) ^ m / (m.factorial : ℂ))
      = ((∑ m ∈ Finset.range 8, x ^ m / (m.factorial : ℝ) : ℝ) : ℂ) := by
    push_cast
    rfl
  rw [← Complex.ofReal_exp, hsum, ← Complex.ofReal_sub, Complex.norm_real, Real.norm_eq_abs,
    Complex.norm_real, Real.norm_eq_abs] at h
  exact h

/-- **the upper bound** `cosh x ≤ 1 + x²/2 + x⁴/24 + x⁶/720 + x⁸/20160` for `|x| ≤ 9/2`: the degree-7 Taylor bound of `exp`
at `x` and at `−x` (the odd terms cancel; the two remainders `2x⁸/8!` average to `x⁸/20160`). -/
theorem cosh_le_poly8 (x : ℝ) (hx : |x| ≤ 9 / 2) :
    Real.cosh x ≤ 1 + x ^ 2 / 2 + x ^ 4 / 24 + x ^ 6 / 720 + x ^ 8 / 20160 := by
  have h1 := exp_sub_sum_le x hx
  have h2 := exp_sub_sum_le (-x) (by rwa [abs_neg])
  have e1 : ∑ m ∈ Finset.range 8, x ^ m / (m.factorial : ℝ)
      = 1 + x + x ^ 2 / 2 + x ^ 3 / 6 + x ^ 4 / 24 + x ^ 5 / 120 + x ^ 6 / 720 + x ^ 7 / 5040 := by
    simp only [Finset.sum_range_succ, Finset.sum_range_zero, Nat.factorial]
    push_cast
    ring
  have e2 : ∑ m ∈ Finset.range 8, (-x) ^ m / (m.factorial : ℝ)
      = 1 - x + x ^ 2 / 2 - x ^ 3 / 6 + x ^ 4 / 24 - x ^ 5 / 120 + x ^ 6 / 720 - x ^ 7 / 5040 := by
    simp only [Finset.sum_range_succ, Finset.sum_range_zero, Nat.factorial]
    push_cast
    ring
  have e3 : (Nat.factorial 8 : ℝ) = 40320 := by
    simp only [Nat.factorial]
    norm_num
  have h8 : |x| ^ 8 = x ^ 8 := by
    rw [show (8 : ℕ) = 2 * 4 from rfl, pow_mul, sq_abs, ← pow_mul]
  rw [e1, e3, h8] at h1
  rw [e2, e3, abs_neg, h8] at h2
  have h1' := (abs_sub_le_iff.1 h1).1
  have h2' := (abs_sub_le_iff.1 h2).1
  rw [Real.cosh_eq]
  linarith

/-! ## 2. The four integer power sums over the band, kernel-checked -/

theorem sum_pow2 : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, j ^ 2) = 22880 := by decide +kernel
theorem sum_pow4 : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, j ^ 4) = 14492192 := by decide +kernel
theorem sum_pow6 : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, j ^ 6) = 10924353440 := by decide +kernel
theorem sum_pow8 : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, j ^ 8) = 8964042662432 := by decide +kernel

lemma sum_pow2_real : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, (j : ℝ) ^ 2) = 22880 := by exact_mod_cast sum_pow2
lemma sum_pow4_real : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, (j : ℝ) ^ 4) = 14492192 := by exact_mod_cast sum_pow4
lemma sum_pow6_real : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, (j : ℝ) ^ 6) = 10924353440 := by
  exact_mod_cast sum_pow6
lemma sum_pow8_real : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, (j : ℝ) ^ 8) = 8964042662432 := by
  exact_mod_cast sum_pow8

lemma card_band32 : (Finset.Icc (-32 : ℤ) 32).card = 65 := by
  rw [Int.card_Icc]
  rfl

/-! ## 3. The bounds pass through the flat average symbolically -/

/-- the flat average of the degree-2 lower polynomial over the band: `1 + c² S₂/(2·65)`. -/
lemma sum_poly2 (c : ℝ) :
    ∑ j ∈ Finset.Icc (-32 : ℤ) 32, (1 / 65 : ℝ) * (1 + (c * j) ^ 2 / 2) = 1 + c ^ 2 * 22880 / (2 * 65) := by
  have h : ∀ j : ℤ, (1 / 65 : ℝ) * (1 + (c * j) ^ 2 / 2) = 1 / 65 + (c ^ 2 / (2 * 65)) * (j : ℝ) ^ 2 := by
    intro j
    ring
  rw [Finset.sum_congr rfl fun j _ => h j]
  simp only [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_const, card_band32, nsmul_eq_mul]
  rw [sum_pow2_real]
  push_cast
  ring

/-- the flat average of the degree-8 upper polynomial over the band: `1 + Σ_k c^{2k} S_{2k}/((2k)!·65)`. -/
lemma sum_poly8 (c : ℝ) :
    ∑ j ∈ Finset.Icc (-32 : ℤ) 32,
        (1 / 65 : ℝ) * (1 + (c * j) ^ 2 / 2 + (c * j) ^ 4 / 24 + (c * j) ^ 6 / 720 + (c * j) ^ 8 / 20160)
      = 1 + c ^ 2 * 22880 / (2 * 65) + c ^ 4 * 14492192 / (24 * 65) + c ^ 6 * 10924353440 / (720 * 65)
          + c ^ 8 * 8964042662432 / (20160 * 65) := by
  have h : ∀ j : ℤ,
      (1 / 65 : ℝ) * (1 + (c * j) ^ 2 / 2 + (c * j) ^ 4 / 24 + (c * j) ^ 6 / 720 + (c * j) ^ 8 / 20160)
        = 1 / 65 + (c ^ 2 / (2 * 65)) * (j : ℝ) ^ 2 + (c ^ 4 / (24 * 65)) * (j : ℝ) ^ 4
            + (c ^ 6 / (720 * 65)) * (j : ℝ) ^ 6 + (c ^ 8 / (20160 * 65)) * (j : ℝ) ^ 8 := by
    intro j
    ring
  rw [Finset.sum_congr rfl fun j _ => h j]
  simp only [Finset.sum_add_distrib, ← Finset.mul_sum, Finset.sum_const, card_band32, nsmul_eq_mul]
  rw [sum_pow2_real, sum_pow4_real, sum_pow6_real, sum_pow8_real]
  push_cast
  ring

/-- `ā(x)` at `n = 32` with the argument written as `(πx/32)·j`. -/
lemma abar32 (x : ℝ) :
    abar 32 x = ∑ j ∈ Finset.Icc (-32 : ℤ) 32, (1 / 65 : ℝ) * Real.cosh ((Real.pi * x / 32) * j) := by
  unfold abar
  have hI : Finset.Icc (-((32 : ℕ) : ℤ)) ((32 : ℕ) : ℤ) = Finset.Icc (-32 : ℤ) 32 := by norm_num
  rw [hI]
  refine Finset.sum_congr rfl fun j _ => ?_
  have harg : 2 * Real.pi * (j : ℝ) * x / (2 * ((32 : ℕ) : ℝ)) = (Real.pi * x / 32) * j := by
    push_cast
    ring
  rw [harg]
  norm_num

/-- the lower bound on `ā(1/4)` in terms of `π`. -/
lemma abar_quarter_ge : 1 + (Real.pi / 128) ^ 2 * 22880 / (2 * 65) ≤ abar 32 (1 / 4) := by
  rw [abar32, show Real.pi * (1 / 4) / 32 = Real.pi / 128 by ring, ← sum_poly2 (Real.pi / 128)]
  refine Finset.sum_le_sum fun j _ => ?_
  exact mul_le_mul_of_nonneg_left (one_add_sq_half_le_cosh _) (by norm_num)

/-- the upper bound on `ā(1/2)` in terms of `π` (the arguments `πj/64` satisfy `|πj/64| ≤ π/2 < 9/2`). -/
lemma abar_half_le :
    abar 32 (1 / 2) ≤ 1 + (Real.pi / 64) ^ 2 * 22880 / (2 * 65) + (Real.pi / 64) ^ 4 * 14492192 / (24 * 65)
      + (Real.pi / 64) ^ 6 * 10924353440 / (720 * 65) + (Real.pi / 64) ^ 8 * 8964042662432 / (20160 * 65) := by
  rw [abar32, show Real.pi * (1 / 2) / 32 = Real.pi / 64 by ring, ← sum_poly8 (Real.pi / 64)]
  refine Finset.sum_le_sum fun j hj => ?_
  refine mul_le_mul_of_nonneg_left (cosh_le_poly8 _ ?_) (by norm_num)
  rw [Finset.mem_Icc] at hj
  have hj' : |(j : ℝ)| ≤ 32 := abs_le.2 ⟨by exact_mod_cast hj.1, by exact_mod_cast hj.2⟩
  rw [abs_mul, abs_of_pos (by positivity : (0 : ℝ) < Real.pi / 64)]
  calc Real.pi / 64 * |(j : ℝ)| ≤ Real.pi / 64 * 32 := by gcongr
    _ ≤ 9 / 2 := by linarith [Real.pi_lt_d6]

/-! ## 4. The π bracket and the final rational inequality -/

/-- `L ≤ ā(1/4)` with the rational `L = 1 + (3.141592/128)² S₂/(2·65)` (`Real.pi_gt_d6`). -/
lemma abar_quarter_ge_L : (1 : ℝ) + (3.141592 / 128) ^ 2 * 22880 / (2 * 65) ≤ abar 32 (1 / 4) := by
  refine le_trans ?_ abar_quarter_ge
  gcongr
  linarith [Real.pi_gt_d6]

/-- `ā(1/2) ≤ U` with the rational `U = 1 + Σ_k (3.141593/64)^{2k} S_{2k}/((2k)!·65)` (`Real.pi_lt_d6`). -/
lemma abar_half_le_U :
    abar 32 (1 / 2) ≤ (1 : ℝ) + (3.141593 / 64) ^ 2 * 22880 / (2 * 65) + (3.141593 / 64) ^ 4 * 14492192 / (24 * 65)
      + (3.141593 / 64) ^ 6 * 10924353440 / (720 * 65) + (3.141593 / 64) ^ 8 * 8964042662432 / (20160 * 65) := by
  refine le_trans abar_half_le ?_
  gcongr <;> linarith [Real.pi_lt_d6]

/-- the certificate's rational inequality: `2μ²U² − 4μ(L² − 1) < 0` at `μ = 1/20` (value `−0.03368…`). -/
lemma cert_numeric :
    2 * (1 / 20 : ℝ) ^ 2
        * ((1 : ℝ) + (3.141593 / 64) ^ 2 * 22880 / (2 * 65) + (3.141593 / 64) ^ 4 * 14492192 / (24 * 65)
          + (3.141593 / 64) ^ 6 * 10924353440 / (720 * 65) + (3.141593 / 64) ^ 8 * 8964042662432 / (20160 * 65)) ^ 2
      - 4 * (1 / 20 : ℝ) * (((1 : ℝ) + (3.141592 / 128) ^ 2 * 22880 / (2 * 65)) ^ 2 - 1) < 0 := by
  norm_num

/-- **the floor `F1 ≥ S2` FAILS at the anchor `(d, μ) = (1/4, 1/20)`, `n = 32`, for the REAL mark `μ = 1/20`** (paper §4.2 /
pair-channel.md Prop. 3.1, "F1 − S2 = −3.520·10⁻²"): `pairRow 32 (vacancyMark 32) {(0, 1/20, 1/4)} < 64 + 2·(1/20)²`.
By `prop45` the difference is `2μ²ā(1/2)² − 4μ(ā(1/4)² − 1)`; with `L ≤ ā(1/4)`, `ā(1/2) ≤ U` and `1 ≤ ā` it is at most
`2μ²U² − 4μ(L² − 1) < 0` (`cert_numeric`).  This says nothing about (MI), which holds at this anchor. -/
theorem floor_fails_anchor :
    pairRow 32 (vacancyMark 32) {((0 : ZMod 65), (1 / 20 : ℝ), (1 / 4 : ℝ))} < 64 + 2 * (1 / 20 : ℝ) ^ 2 := by
  have h45 : pairRow 32 (vacancyMark 32) {((0 : ZMod 65), (1 / 20 : ℝ), (1 / 4 : ℝ))}
      - (2 * (32 : ℝ) + 2 * (1 / 20 : ℝ) ^ 2)
      = 2 * (1 / 20 : ℝ) ^ 2 * abar 32 (2 * (1 / 4)) ^ 2 - 4 * (1 / 20) * (abar 32 (1 / 4) ^ 2 - 1) := by
    have h := prop45 32 (1 / 4) (1 / 20)
    push_cast at h
    exact h
  rw [show (2 : ℝ) * (1 / 4) = 1 / 2 by norm_num] at h45
  have hL := abar_quarter_ge_L
  have hU := abar_half_le_U
  have hA2 : 1 ≤ abar 32 (1 / 2) := one_le_abar 32 (1 / 2)
  have hL2 : ((1 : ℝ) + (3.141592 / 128) ^ 2 * 22880 / (2 * 65)) ^ 2 ≤ abar 32 (1 / 4) ^ 2 :=
    pow_le_pow_left₀ (by norm_num) hL 2
  have hU2 : abar 32 (1 / 2) ^ 2
      ≤ ((1 : ℝ) + (3.141593 / 64) ^ 2 * 22880 / (2 * 65) + (3.141593 / 64) ^ 4 * 14492192 / (24 * 65)
          + (3.141593 / 64) ^ 6 * 10924353440 / (720 * 65) + (3.141593 / 64) ^ 8 * 8964042662432 / (20160 * 65)) ^ 2 :=
    pow_le_pow_left₀ (by linarith) hU 2
  have hc := cert_numeric
  linarith

end PairCert
end PairCeiling
end Zeta23
