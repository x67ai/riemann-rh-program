/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean.
-/
/-
Zeta23/Separation/B1Sym.lean — the noise constant b₁ of Theorem M2 PROVED in symbolic form (Session 24 item 3, Unit A,
piece "3-sym" of rh-program/results/c2-m4/PRICING-RESIDUE.md §1; separation note §5, the hand-proved bound
b₁ = sup_η |ηB̂(η)|² ≤ ‖B′‖₁², and check-O §12.2's substitution sentence).

What is proved here, over the library's B = B_raw/Z (LemmaG1.lean) and paperFT (Defs.lean):
  §2  |η|·‖B̂(η)‖ ≤ ∫ ‖D¹(B : ℝ → ℂ)‖          one integration by parts with the L¹ norm KEPT (the k = 1 case of
                                               `paperFT_iteratedDeriv`, as `norm_paperFT_Bc_mul_le` up to its last step);
  §3  ∫ ‖D¹(B : ℝ → ℂ)‖ = 2·B(0) = 2e^{−1}/Z     B′ = B_raw′/Z with B_raw′(u) = B_raw(u)·(−8u)/(1 − 4u²)² on |u| < 1/2
                                               (`HasDerivAt.exp`, `HasDerivAt.inv`), B′ ≥ 0 on [−1/2, 0], B′ ≤ 0 on
                                               [0, 1/2], B′ = 0 off (−1/2, 1/2) (one-sided derivatives at ±1/2), and the
                                               fundamental theorem of calculus on the two halves;
  §4  b₁sym := (2e^{−1}/Z)²,  4 ≤ b₁sym          from Z ≤ e^{−1} (B_raw ≤ e^{−1}: the `Z_le_one` pattern), and
      (|η|·‖B̂(η)‖)² ≤ b₁sym for every real η    the displayed H-b₁ of M4 (iii) (`Hb1`, 87/10) REPLACED by a theorem.
NO digit of b₁ and NO lower bound on Z appears in this file: b₁sym is a real number defined from Z, and the consumers
(Assembly2.lean) need it from below only, which Z ≤ e^{−1} gives (pricing observation §0 (i) of PRICING-RESIDUE.md,
verified here). The note's 8.70 and the hand computation's 10.984 are not stated.
-/
import Zeta23.Separation.LemmaG

namespace Zeta23
namespace Separation

open Complex MeasureTheory Set
open scoped ContDiff

noncomputable section

/-! ### §1 b₁ as a real number (copied character for character into comparator/ChallengeDeps/Separation6b.lean) -/

/-- b₁ as the real number (2e^{−1}/Z)² = ‖B′‖₁² (separation note §5; no digit). -/
def b1sym : ℝ := (2 * Real.exp (-1) / Z) ^ 2

/-! ### §2 One integration by parts with the L¹ norm kept -/

/-- |η|·‖B̂(η)‖ ≤ ∫ ‖D¹(B : ℝ → ℂ)‖ (the k = 1 case of `paperFT_iteratedDeriv`, the integral kept). -/
theorem abs_mul_norm_paperFT_Bc_le_integral (η : ℝ) :
    |η| * ‖paperFT (fun v => (B v : ℂ)) η‖ ≤ ∫ u, ‖iteratedDeriv 1 (fun v => (B v : ℂ)) u‖ := by
  have hint : Integrable (iteratedDeriv 1 (fun v => (B v : ℂ))) :=
    (Bc_contDiff.continuous_iteratedDeriv 1 (by exact_mod_cast le_top)).integrable_of_hasCompactSupport
      (hasCompactSupport_iteratedDeriv hasCompactSupport_Bc 1)
  have hsupp : ∀ u, iteratedDeriv 1 (fun v => (B v : ℂ)) u ≠ 0 → |u| ≤ 1 / 2 := fun u hu => by
    by_contra h
    exact hu (iteratedDeriv_Bc_eq_zero (not_le.mp h))
  have h := norm_paperFT_le hint hsupp (η : ℂ)
  rw [paperFT_iteratedDeriv Bc_contDiff hasCompactSupport_Bc (η : ℂ) 1, norm_mul, norm_pow, norm_neg,
    norm_mul, Complex.norm_I, one_mul, Complex.ofReal_im, abs_zero, zero_mul, Real.exp_zero, one_mul,
    Complex.norm_real, Real.norm_eq_abs, pow_one] at h
  exact h

/-! ### §3 The derivative of B on the two halves and ∫ |B′| = 2B(0) -/

/-- B_raw on |u| < 1/2, by its definition. -/
theorem Braw_of_abs_lt {u : ℝ} (hu : |u| < 1 / 2) : Braw u = Real.exp (-1 / (1 - 4 * u ^ 2)) := if_pos hu

/-- on |u| < 1/2, B_raw′(u) = B_raw(u)·(−8u)/(1 − 4u²)². -/
theorem hasDerivAt_Braw {u : ℝ} (hu : |u| < 1 / 2) :
    HasDerivAt Braw (Braw u * (-(8 * u) / (1 - 4 * u ^ 2) ^ 2)) u := by
  have hv := abs_lt.mp hu
  have hg : 0 < 1 - 4 * u ^ 2 := by nlinarith
  have h1 : HasDerivAt (fun v : ℝ => 1 - 4 * v ^ 2) (-(4 * (2 * u))) u := by
    have := ((hasDerivAt_pow 2 u).const_mul 4).const_sub 1
    simpa using this
  have h2 : HasDerivAt (fun v : ℝ => -(1 - 4 * v ^ 2)⁻¹)
      (-(-(-(4 * (2 * u))) / (1 - 4 * u ^ 2) ^ 2)) u := (h1.inv hg.ne').neg
  have h3 := h2.exp
  have heq : Braw =ᶠ[nhds u] fun v : ℝ => Real.exp (-(1 - 4 * v ^ 2)⁻¹) := by
    have hopen : IsOpen {v : ℝ | |v| < 1 / 2} := isOpen_lt continuous_abs continuous_const
    filter_upwards [hopen.mem_nhds hu] with v hv
    rw [Braw_of_abs_lt hv, neg_div, one_div]
  have h4 := h3.congr_of_eventuallyEq heq
  refine h4.congr_deriv ?_
  rw [Braw_of_abs_lt hu, show (-1 : ℝ) / (1 - 4 * u ^ 2) = -(1 - 4 * u ^ 2)⁻¹ by rw [neg_div, one_div]]
  ring

theorem deriv_Braw_of_abs_lt {u : ℝ} (hu : |u| < 1 / 2) :
    deriv Braw u = Braw u * (-(8 * u) / (1 - 4 * u ^ 2) ^ 2) :=
  (hasDerivAt_Braw hu).deriv

/-- B′ = B_raw′/Z. -/
theorem deriv_B (u : ℝ) : deriv B u = deriv Braw u / Z := by
  unfold B; exact deriv_div_const Z

/-- B is differentiable everywhere (it is C¹). -/
theorem hasDerivAt_B (u : ℝ) : HasDerivAt B (deriv B u) u :=
  ((B_contDiff (n := 1)).differentiable (by norm_num) u).hasDerivAt

theorem continuous_deriv_B : Continuous (deriv B) := (B_contDiff (n := 1)).continuous_deriv_one

/-- B′ = 0 on |u| ≥ 1/2 (B vanishes on [1/2, ∞) and on (−∞, −1/2]; one-sided derivatives at the endpoints). -/
theorem deriv_B_eq_zero_of_half_le {u : ℝ} (hu : 1 / 2 ≤ |u|) : deriv B u = 0 := by
  rcases le_abs'.mp hu with h | h
  · -- u ≤ −1/2: B = 0 on Iic u
    have h1 : HasDerivWithinAt B (deriv B u) (Iic u) u := (hasDerivAt_B u).hasDerivWithinAt
    have h2 : HasDerivWithinAt B 0 (Iic u) u :=
      (hasDerivWithinAt_const u (Iic u) (0 : ℝ)).congr_of_mem
        (fun y hy => B_eq_zero_of_half_le (le_abs.mpr (Or.inr (by linarith [mem_Iic.mp hy]))))
        (mem_Iic.mpr le_rfl)
    exact (uniqueDiffWithinAt_Iic u).eq_deriv _ h1 h2
  · -- 1/2 ≤ u: B = 0 on Ici u
    have h1 : HasDerivWithinAt B (deriv B u) (Ici u) u := (hasDerivAt_B u).hasDerivWithinAt
    have h2 : HasDerivWithinAt B 0 (Ici u) u :=
      (hasDerivWithinAt_const u (Ici u) (0 : ℝ)).congr_of_mem
        (fun y hy => B_eq_zero_of_half_le (le_abs.mpr (Or.inl (by linarith [mem_Ici.mp hy]))))
        (mem_Ici.mpr le_rfl)
    exact (uniqueDiffWithinAt_Ici u).eq_deriv _ h1 h2

/-- B′ ≤ 0 on [0, 1/2]. -/
theorem deriv_B_nonpos {u : ℝ} (h0 : 0 ≤ u) (h1 : u ≤ 1 / 2) : deriv B u ≤ 0 := by
  rcases eq_or_lt_of_le h1 with h | h
  · rw [deriv_B_eq_zero_of_half_le (by rw [h]; norm_num)]
  · have hu : |u| < 1 / 2 := abs_lt.mpr ⟨by linarith, h⟩
    have hZ := Z_pos
    have hB := Braw_nonneg u
    have hg1 : 0 < 1 - 4 * u ^ 2 := by have := abs_lt.mp hu; nlinarith
    have hg : 0 < (1 - 4 * u ^ 2) ^ 2 := pow_pos hg1 2
    have key : deriv B u = -(8 * u * Braw u / ((1 - 4 * u ^ 2) ^ 2 * Z)) := by
      rw [deriv_B, deriv_Braw_of_abs_lt hu]; field_simp
    rw [key]
    have : 0 ≤ 8 * u * Braw u / ((1 - 4 * u ^ 2) ^ 2 * Z) := by positivity
    linarith

/-- B′ ≥ 0 on [−1/2, 0]. -/
theorem deriv_B_nonneg {u : ℝ} (h0 : -1 / 2 ≤ u) (h1 : u ≤ 0) : 0 ≤ deriv B u := by
  rcases eq_or_lt_of_le h0 with h | h
  · rw [deriv_B_eq_zero_of_half_le (by rw [← h]; norm_num)]
  · have hu : |u| < 1 / 2 := abs_lt.mpr ⟨by linarith, by linarith⟩
    have hZ := Z_pos
    have hB := Braw_nonneg u
    have hg1 : 0 < 1 - 4 * u ^ 2 := by have := abs_lt.mp hu; nlinarith
    have hg : 0 < (1 - 4 * u ^ 2) ^ 2 := pow_pos hg1 2
    have hu0 : 0 ≤ -u := by linarith
    have key : deriv B u = 8 * (-u) * Braw u / ((1 - 4 * u ^ 2) ^ 2 * Z) := by
      rw [deriv_B, deriv_Braw_of_abs_lt hu]; field_simp
    rw [key]
    positivity

/-- B(0) = e^{−1}/Z. -/
theorem B_zero : B 0 = Real.exp (-1) / Z := by
  unfold B Braw; rw [if_pos (by norm_num)]; norm_num

/-- ∫ ‖D¹(B : ℝ → ℂ)‖ = 2B(0) = 2e^{−1}/Z: the fundamental theorem of calculus on [−1/2, 0] and [0, 1/2]. -/
theorem integral_norm_deriv_Bc : ∫ u, ‖iteratedDeriv 1 (fun v => (B v : ℂ)) u‖ = 2 * Real.exp (-1) / Z := by
  have hcont := continuous_deriv_B
  have hII : ∀ a b : ℝ, IntervalIntegrable (fun u => |deriv B u|) volume a b := fun a b =>
    hcont.abs.intervalIntegrable a b
  have hpt : (fun u => ‖iteratedDeriv 1 (fun v => (B v : ℂ)) u‖) = fun u => |deriv B u| := by
    funext u; rw [norm_iteratedDeriv_Bc, iteratedDeriv_one]
  rw [hpt]
  have hzero : ∀ u, u ∉ Icc (-1 / 2 : ℝ) (1 / 2) → |deriv B u| = 0 := by
    intro u hu
    rw [abs_eq_zero]
    apply deriv_B_eq_zero_of_half_le
    rw [mem_Icc, not_and_or] at hu
    rcases hu with h | h
    · exact le_abs.mpr (Or.inr (by linarith [not_le.mp h]))
    · exact le_abs.mpr (Or.inl (by linarith [not_le.mp h]))
  rw [← setIntegral_eq_integral_of_forall_compl_eq_zero hzero, integral_Icc_eq_integral_Ioc,
    ← intervalIntegral.integral_of_le (by norm_num : (-1 / 2 : ℝ) ≤ 1 / 2),
    ← intervalIntegral.integral_add_adjacent_intervals (hII (-1 / 2) 0) (hII 0 (1 / 2))]
  have hl : ∫ u in (-1 / 2 : ℝ)..0, |deriv B u| = ∫ u in (-1 / 2 : ℝ)..0, deriv B u := by
    refine intervalIntegral.integral_congr fun x hx => ?_
    rw [uIcc_of_le (by norm_num)] at hx
    exact abs_of_nonneg (deriv_B_nonneg hx.1 hx.2)
  have hr : ∫ u in (0 : ℝ)..(1 / 2), |deriv B u| = ∫ u in (0 : ℝ)..(1 / 2), -deriv B u := by
    refine intervalIntegral.integral_congr fun x hx => ?_
    rw [uIcc_of_le (by norm_num)] at hx
    exact abs_of_nonpos (deriv_B_nonpos hx.1 hx.2)
  rw [hl, hr, intervalIntegral.integral_neg,
    intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => hasDerivAt_B x) (hcont.intervalIntegrable _ _),
    intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => hasDerivAt_B x) (hcont.intervalIntegrable _ _),
    B_eq_zero_of_half_le (v := 1 / 2) (by norm_num), B_eq_zero_of_half_le (v := -1 / 2) (by norm_num), B_zero]
  ring

/-! ### §4 b₁sym ≥ 4 from Z ≤ e^{−1}, and the proved H-b₁ -/

/-- B_raw ≤ e^{−1} (the exponent −1/(1 − 4v²) is ≤ −1 on |v| < 1/2). -/
theorem Braw_le_exp_neg_one (v : ℝ) : Braw v ≤ Real.exp (-1) := by
  unfold Braw; split_ifs with h
  · have hv := abs_lt.mp h
    have h3 : 0 < 1 - 4 * v ^ 2 := by nlinarith
    apply Real.exp_le_exp.mpr
    rw [div_le_iff₀ h3]; nlinarith [sq_nonneg v]
  · exact (Real.exp_pos _).le

/-- Z ≤ e^{−1} (B_raw ≤ e^{−1} on an interval of length 1; the `Z_le_one` pattern). -/
theorem Z_le_exp_neg_one : Z ≤ Real.exp (-1) := by
  unfold Z
  calc (∫ v in (-1 / 2 : ℝ)..(1 / 2), Braw v) ≤ ∫ _ in (-1 / 2 : ℝ)..(1 / 2), Real.exp (-1) :=
        intervalIntegral.integral_mono_on (by norm_num) (Braw_continuous.intervalIntegrable _ _)
          (continuous_const.intervalIntegrable _ _) (fun x _ => Braw_le_exp_neg_one x)
    _ = Real.exp (-1) := by rw [intervalIntegral.integral_const]; norm_num

/-- 4 ≤ b₁sym (every consumer of b₁ wants it from below; this is all they get, and all they need). -/
theorem four_le_b1sym : 4 ≤ b1sym := by
  have hZ := Z_pos
  have h := Z_le_exp_neg_one
  have h2 : (2 : ℝ) ≤ 2 * Real.exp (-1) / Z := by rw [le_div_iff₀ hZ]; linarith
  unfold b1sym
  calc (4 : ℝ) = 2 ^ 2 := by norm_num
    _ ≤ (2 * Real.exp (-1) / Z) ^ 2 := pow_le_pow_left₀ (by norm_num) h2 2

/-- **H-b₁, proved**: (|η|·‖B̂(η)‖)² ≤ b₁sym = (2e^{−1}/Z)² = ‖B′‖₁² for every real η (separation note §5). -/
theorem hb1sym (η : ℝ) : (|η| * ‖paperFT (fun v => (B v : ℂ)) η‖) ^ 2 ≤ b1sym := by
  unfold b1sym
  have h := abs_mul_norm_paperFT_Bc_le_integral η
  rw [integral_norm_deriv_Bc] at h
  exact pow_le_pow_left₀ (by positivity) h 2

end

end Separation
end Zeta23
