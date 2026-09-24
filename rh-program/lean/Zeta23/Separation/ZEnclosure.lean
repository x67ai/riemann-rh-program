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
Zeta23/Separation/ZEnclosure.lean — Piece 8 of the M4 residue (rh-program/results/c2-m4/PRICING-RESIDUE.md): a two-sided
rational enclosure of Z = ∫_{−1/2}^{1/2} B_raw, Z_lo ≤ Z ≤ Z_hi, by monotone Riemann sums on n = 16 cells per half —
B_raw is antitone on [0, 1/2] (`Braw_antitoneOn`), so with g(x) := B_raw(x/32) on [0, 16],
    Σ_{i<16} g(i + 1) ≤ ∫_0^{16} g = 32·∫_0^{1/2} B_raw = 16·Z ≤ Σ_{i<16} g(i)
(`AntitoneOn.sum_le_integral`, `AntitoneOn.integral_le_sum`, `intervalIntegral.integral_comp_div`, B_raw even), and per
cell a rational bound on exp(−x_i), x_i = 1/(1 − 4(i/32)²) = 256/(256 − i²):
    upper  exp(−x) ≤ 1/Σ_{k<8} x^k/k!                                     (`Real.sum_le_exp_of_nonneg`)
    lower  exp(−x) ≥ 1/(Σ_{m<8} y^m/m! + y⁸·9/(8!·8))^q,  y = x/q ≤ 1    (`Real.exp_bound'`, `Real.exp_nat_mul`),
q = ⌈x_i⌉ (1, 2, …, 2, 3, 3, 5, 9 for i = 0, 1, …, 11, 12, 13, 14, 15).  The bridging lemmas are generic; the 16-cell
data is checked by `norm_num` over ℚ (the `NumericCert` discipline: proved rational bounds at rational points, one finite
inequality).  Result (`Z_enclosure`): 421/2000 ≤ Z ≤ 233651/1000000 (Z = 0.221997; −5.2 % / +5.2 %; the exact Riemann
sums are 0.2105014 and 0.2336502, rh-program/results/c2-m4/verify-B/cert-numbers.log).  Consumed by Clause5Cert.lean
(C_B ≤ e²/Z_lo and b₁sym ≥ (2/(e·Z_hi))² in the one-point check F₁₃(50; 73) ≤ 0).  Nothing here is about ζ or RH.
-/
import Mathlib.Analysis.SumIntegralComparisons
import Zeta23.Separation.B1Sym

namespace Zeta23
namespace Separation

open MeasureTheory

noncomputable section

/-! ### §1 B_raw is antitone on [0, 1/2], and Z as an integral over [0, 1/2] -/

theorem Braw_antitoneOn : AntitoneOn Braw (Set.Icc 0 (1 / 2)) := by
  intro u hu v hv huv
  by_cases hv2 : v < 1 / 2
  · have hu2 : |u| < 1 / 2 := abs_lt.mpr ⟨by linarith [hu.1], lt_of_le_of_lt huv hv2⟩
    have hv2' : |v| < 1 / 2 := abs_lt.mpr ⟨by linarith [hv.1], hv2⟩
    rw [Braw_of_abs_lt hu2, Braw_of_abs_lt hv2']
    apply Real.exp_le_exp.mpr
    have h1 : 0 < 1 - 4 * v ^ 2 := by nlinarith [hv.1]
    have h2 : 1 - 4 * v ^ 2 ≤ 1 - 4 * u ^ 2 := by nlinarith [hu.1]
    rw [neg_div, neg_div]
    exact neg_le_neg (one_div_le_one_div_of_le h1 h2)
  · have hv' : v = 1 / 2 := le_antisymm hv.2 (not_lt.mp hv2)
    rw [hv', Braw_eq_zero_of_half_le (by rw [abs_of_pos (by norm_num)])]
    exact Braw_nonneg u

theorem Braw_even (v : ℝ) : Braw (-v) = Braw v := by
  unfold Braw; rw [abs_neg, neg_sq]

/-- Z = 2·∫_0^{1/2} B_raw (B_raw even). -/
theorem Z_eq_two_mul : Z = 2 * ∫ v in (0 : ℝ)..(1 / 2), Braw v := by
  unfold Z
  have hint : ∀ a b : ℝ, IntervalIntegrable Braw volume a b := fun a b => Braw_continuous.intervalIntegrable a b
  rw [← intervalIntegral.integral_add_adjacent_intervals (hint (-1 / 2) 0) (hint 0 (1 / 2))]
  have h : ∫ v in (-1 / 2 : ℝ)..0, Braw v = ∫ v in (0 : ℝ)..(1 / 2), Braw v := by
    have := intervalIntegral.integral_comp_neg (a := (0 : ℝ)) (b := 1 / 2) Braw
    simp only [neg_zero] at this
    rw [show (-1 / 2 : ℝ) = -(1 / 2) by norm_num, ← this]
    exact intervalIntegral.integral_congr fun v _ => Braw_even v
  rw [h]; ring

/-- 16·Z = ∫_0^{16} B_raw(x/32) dx. -/
theorem sixteen_mul_Z : 16 * Z = ∫ x in (0 : ℝ)..(0 + (16 : ℕ)), Braw (x / 32) := by
  rw [intervalIntegral.integral_comp_div (f := Braw) (c := 32) (by norm_num), Z_eq_two_mul, smul_eq_mul]
  norm_num
  ring

theorem g_antitoneOn : AntitoneOn (fun x : ℝ => Braw (x / 32)) (Set.Icc 0 (0 + (16 : ℕ))) := by
  intro u hu v hv huv
  simp only at hu hv ⊢
  refine Braw_antitoneOn ⟨by linarith [hu.1], ?_⟩ ⟨by linarith [hv.1], ?_⟩ (by linarith)
  · have := hu.2; push_cast at this; linarith
  · have := hv.2; push_cast at this; linarith

/-- the two Riemann sums bracket 16·Z: Σ_{i<16} B_raw((i + 1)/32) ≤ 16·Z ≤ Σ_{i<16} B_raw(i/32). -/
theorem riemann_bracket :
    (∑ i ∈ Finset.range 16, Braw (((i + 1 : ℕ) : ℝ) / 32)) ≤ 16 * Z ∧
      16 * Z ≤ ∑ i ∈ Finset.range 16, Braw ((i : ℝ) / 32) := by
  have h1 := AntitoneOn.sum_le_integral g_antitoneOn
  have h2 := AntitoneOn.integral_le_sum g_antitoneOn
  simp only [zero_add] at h1 h2
  rw [sixteen_mul_Z]
  simp only [zero_add]
  exact ⟨h1, h2⟩

/-! ### §2 The cells: x_i = 256/(256 − i²), and the two generic exp bounds -/

/-- x_i := 256/(256 − i²) = 1/(1 − 4(i/32)²). -/
def cellx (i : ℕ) : ℝ := 256 / (256 - (i : ℝ) ^ 2)

/-- q_i := ⌈x_i⌉: 1, 2 (i = 1..11), 3 (i = 12, 13), 5 (i = 14), 9 (i = 15). -/
def qcell (i : ℕ) : ℕ := if i = 0 then 1 else if i ≤ 11 then 2 else if i ≤ 13 then 3 else if i = 14 then 5 else 9

theorem Braw_cell {i : ℕ} (hi : i ≤ 15) : Braw ((i : ℝ) / 32) = Real.exp (-(cellx i)) := by
  have hi' : (i : ℝ) ≤ 15 := by exact_mod_cast hi
  have hi0 : (0 : ℝ) ≤ i := Nat.cast_nonneg i
  rw [Braw_of_abs_lt (by rw [abs_of_nonneg (by positivity)]; linarith [show (i : ℝ) / 32 ≤ 15 / 32 by linarith])]
  congr 1
  unfold cellx
  have h' : (1 : ℝ) - 4 * ((i : ℝ) / 32) ^ 2 = (256 - (i : ℝ) ^ 2) / 256 := by ring
  rw [h', neg_div, one_div_div]

theorem Braw_sixteen : Braw ((16 : ℝ) / 32) = 0 :=
  Braw_eq_zero_of_half_le (by rw [abs_of_pos (by norm_num)]; norm_num)

/-- exp(−x) ≤ 1/Σ_{k<8} x^k/k! for x ≥ 0. -/
theorem exp_neg_le_inv_taylor {x : ℝ} (hx : 0 ≤ x) :
    Real.exp (-x) ≤ 1 / ∑ k ∈ Finset.range 8, x ^ k / (k.factorial : ℝ) := by
  have h := Real.sum_le_exp_of_nonneg hx 8
  have hpos : 0 < ∑ k ∈ Finset.range 8, x ^ k / (k.factorial : ℝ) := by
    rw [Finset.sum_range_succ']
    have : 0 ≤ ∑ k ∈ Finset.range 7, x ^ (k + 1) / ((k + 1).factorial : ℝ) := by positivity
    simp only [pow_zero, Nat.factorial_zero, Nat.cast_one, div_one]
    linarith
  rw [Real.exp_neg, ← one_div]
  exact one_div_le_one_div_of_le hpos h

/-- 1/S^q ≤ exp(−(q·y)) whenever exp y ≤ S. -/
theorem one_div_pow_le_exp_neg {y S : ℝ} (hS : Real.exp y ≤ S) (q : ℕ) : 1 / S ^ q ≤ Real.exp (-(q * y)) := by
  have he := Real.exp_pos y
  rw [Real.exp_neg, Real.exp_nat_mul, one_div]
  exact inv_anti₀ (pow_pos he q) (pow_le_pow_left₀ he.le hS q)

/-- the Taylor upper bound at y ∈ [0, 1] with n = 8: T(y) := Σ_{m<8} y^m/m! + y⁸·9/(8!·8). -/
def taylorT (y : ℝ) : ℝ :=
  (∑ m ∈ Finset.range 8, y ^ m / (m.factorial : ℝ)) + y ^ 8 * ((8 : ℕ) + 1) / (((8 : ℕ).factorial : ℝ) * (8 : ℕ))

theorem exp_le_taylorT {y : ℝ} (h0 : 0 ≤ y) (h1 : y ≤ 1) : Real.exp y ≤ taylorT y := by
  have h := Real.exp_bound' h0 h1 (n := 8) (by norm_num)
  unfold taylorT
  exact h

/-- the lower cell bound: for x ≥ 0, x ≤ q, 1/T(x/q)^q ≤ exp(−x). -/
theorem cell_lo {x : ℝ} {q : ℕ} (hq : 0 < q) (hx : 0 ≤ x) (hxq : x ≤ q) :
    1 / taylorT (x / q) ^ q ≤ Real.exp (-x) := by
  have hq' : (0 : ℝ) < q := by exact_mod_cast hq
  have hy0 : 0 ≤ x / q := by positivity
  have hy1 : x / q ≤ 1 := by rw [div_le_one hq']; exact hxq
  have h := one_div_pow_le_exp_neg (exp_le_taylorT hy0 hy1) q
  rwa [mul_div_cancel₀ _ hq'.ne'] at h

/-- the cells' data: 0 ≤ x_i ≤ q_i for i ≤ 15 (checked cell by cell). -/
theorem cellx_le_qcell {i : ℕ} (hi : i ≤ 15) : 0 ≤ cellx i ∧ cellx i ≤ qcell i ∧ 0 < qcell i := by
  interval_cases i <;> norm_num [cellx, qcell]

/-! ### §3 The enclosure -/

/-- **Z_lo ≤ Z ≤ Z_hi** with Z_lo = 421/2000, Z_hi = 233651/1000000, from the 16-cell Riemann sums and the per-cell
rational exp bounds, evaluated by `norm_num` over ℚ. -/
theorem Z_enclosure : 421 / 2000 ≤ Z ∧ Z ≤ 233651 / 1000000 := by
  obtain ⟨hlo, hhi⟩ := riemann_bracket
  constructor
  · -- lower: Σ_{i<16} Braw((i+1)/32) = Σ_{i<15} exp(−x_{i+1}) + 0 ≥ Σ_{i<15} 1/T(x_{i+1}/q_{i+1})^{q_{i+1}}
    have hsum : (∑ i ∈ Finset.range 15, 1 / taylorT (cellx (i + 1) / qcell (i + 1)) ^ qcell (i + 1))
        ≤ ∑ i ∈ Finset.range 16, Braw (((i + 1 : ℕ) : ℝ) / 32) := by
      rw [Finset.sum_range_succ (n := 15), show ((15 + 1 : ℕ) : ℝ) = 16 by norm_num, Braw_sixteen, add_zero]
      refine Finset.sum_le_sum fun i hi => ?_
      have hi' : i + 1 ≤ 15 := by have := Finset.mem_range.mp hi; omega
      rw [Braw_cell hi']
      obtain ⟨h0, hq, hqpos⟩ := cellx_le_qcell hi'
      exact cell_lo hqpos h0 hq
    have hnum : (421 / 2000 : ℝ) * 16 ≤ ∑ i ∈ Finset.range 15, 1 / taylorT (cellx (i + 1) / qcell (i + 1)) ^ qcell (i + 1) := by
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, taylorT, cellx, qcell]
      norm_num [Nat.factorial]
    linarith
  · -- upper: Σ_{i<16} Braw(i/32) = Σ_{i<16} exp(−x_i) ≤ Σ_{i<16} 1/Σ_{k<8} x_i^k/k!
    have hsum : (∑ i ∈ Finset.range 16, Braw ((i : ℝ) / 32))
        ≤ ∑ i ∈ Finset.range 16, 1 / ∑ k ∈ Finset.range 8, cellx i ^ k / (k.factorial : ℝ) := by
      refine Finset.sum_le_sum fun i hi => ?_
      have hi' : i ≤ 15 := by have := Finset.mem_range.mp hi; omega
      rw [Braw_cell hi']
      exact exp_neg_le_inv_taylor (cellx_le_qcell hi').1
    have hnum : (∑ i ∈ Finset.range 16, 1 / ∑ k ∈ Finset.range 8, cellx i ^ k / (k.factorial : ℝ))
        ≤ (233651 / 1000000 : ℝ) * 16 := by
      simp only [Finset.sum_range_succ, Finset.sum_range_zero, cellx]
      norm_num [Nat.factorial]
    linarith

end

end Separation
end Zeta23
