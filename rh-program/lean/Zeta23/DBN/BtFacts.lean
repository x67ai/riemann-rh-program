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
Zeta23/DBN/BtFacts.lean — Lean obligation L-B3 of the M2a contract (SPEC §3.4, §8.3): the
explicit normalizer `Bt` of Defs.lean v1.1 is holomorphic and nowhere vanishing off the
imaginary axis, hence on an open neighborhood of every barrier rectangle with x₁ > 0.

PROVED HERE (sorry-free; `#print axioms` = propext, Classical.choice, Quot.sound):
  * `Bt_ne_zero`          — Bt t z ≠ 0 whenever Re z ≠ 0;
  * `differentiableAt_Bt` — Bt t is complex-differentiable at every z with Re z ≠ 0;
  * `isOpen_rightHalfPlane`, `differentiableOn_Ht_div_Bt` — the packaged form the instance's
    `hHol` consumes: given the displayed `HtEntire`, g_t = Ht t / Bt t is differentiable on the
    open right half-plane {z | 0 < Re z}, which contains R = [X, X+1] × [y₀, 1] for X > 0.

MECHANISM (SPEC §3.4, verbatim in spirit): with s = (1 − iz)/2 one has Im s = −Re z / 2, so
Re z ≠ 0 puts s, s/2 and s/(2π) in Mathlib's `slitPlane` (the complement of (−∞, 0]) — both
principal logarithms are off the cut — and gives s ≠ 0 and s ≠ 1; exp never vanishes; the
complex power π^{−s/2} has the positive real base π ≠ 0; √(2π) > 0.  The hypothesis is only
Re z ≠ 0: SPEC §3.4's "x₁ > 1, y₁ > 0" is more than is needed and is not assumed.

Nothing here is displayed: L-B3 is discharged, so the glue in Instance02.lean carries no `hBt`.
-/
import Zeta23.DBN.Defs
import Mathlib.Analysis.SpecialFunctions.Complex.LogDeriv
import Mathlib.Analysis.SpecialFunctions.Pow.Deriv
import Mathlib.Analysis.SpecialFunctions.ExpDeriv

open scoped Real
open Complex (I slitPlane)

noncomputable section

namespace Zeta23
namespace DBN

/-! ## 1. The point s = (1 − iz)/2 and its imaginary part -/

/-- Im((1 − iz)/2) = −Re z / 2. -/
theorem im_half_one_sub_I_mul (z : ℂ) : ((1 - I * z) / 2).im = -z.re / 2 := by
  simp [Complex.div_ofNat_im, Complex.sub_im, Complex.mul_im, Complex.I_re, Complex.I_im]

/-- a complex number with nonzero imaginary part lies in the slit plane. -/
theorem mem_slitPlane_of_im_ne_zero' {s : ℂ} (hs : s.im ≠ 0) : s ∈ slitPlane :=
  Complex.mem_slitPlane_iff.mpr (Or.inr hs)

theorem ne_zero_of_im_ne_zero {s : ℂ} (hs : s.im ≠ 0) : s ≠ 0 := by
  intro h; apply hs; rw [h]; simp

theorem sub_one_ne_zero_of_im_ne_zero {s : ℂ} (hs : s.im ≠ 0) : s - 1 ≠ 0 := by
  intro h; apply hs
  have : s = 1 := sub_eq_zero.mp h
  rw [this]; simp

theorem half_im_ne_zero {s : ℂ} (hs : s.im ≠ 0) : (s / 2).im ≠ 0 := by
  rw [Complex.div_ofNat_im]; exact div_ne_zero hs two_ne_zero

theorem div_two_pi_im_ne_zero {s : ℂ} (hs : s.im ≠ 0) : (s / (2 * (π : ℂ))).im ≠ 0 := by
  have h : (2 * (π : ℂ)) = ((2 * π : ℝ) : ℂ) := by push_cast; ring
  rw [h, Complex.div_ofReal_im]
  exact div_ne_zero hs (by positivity)

/-! ## 2. Differentiability of α, M₀, M_t at points with Im s ≠ 0 -/

theorem differentiableAt_alpha {s : ℂ} (hs : s.im ≠ 0) : DifferentiableAt ℂ alpha s := by
  have hs0 : s ≠ 0 := ne_zero_of_im_ne_zero hs
  have hs1 : s - 1 ≠ 0 := sub_one_ne_zero_of_im_ne_zero hs
  have h1 : DifferentiableAt ℂ (fun s : ℂ => 1 / (2 * s)) s :=
    (differentiableAt_const _).div (differentiableAt_id.const_mul 2) (mul_ne_zero two_ne_zero hs0)
  have h2 : DifferentiableAt ℂ (fun s : ℂ => 1 / (s - 1)) s :=
    (differentiableAt_const _).div (differentiableAt_id.sub_const 1) hs1
  have h3 : DifferentiableAt ℂ (fun s : ℂ => (1 / 2 : ℂ) * Complex.log (s / (2 * π))) s :=
    ((differentiableAt_id.div_const _).clog
      (mem_slitPlane_of_im_ne_zero' (div_two_pi_im_ne_zero hs))).const_mul _
  exact (h1.add h2).add h3

theorem differentiableAt_M0 {s : ℂ} (hs : s.im ≠ 0) : DifferentiableAt ℂ M0 s := by
  have hπ : (π : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr Real.pi_ne_zero
  have hpoly : DifferentiableAt ℂ (fun s : ℂ => (1 / 8 : ℂ) * (s * (s - 1) / 2)) s :=
    ((differentiableAt_id.mul (differentiableAt_id.sub_const 1)).div_const 2).const_mul _
  have hpow : DifferentiableAt ℂ (fun s : ℂ => (π : ℂ) ^ (-s / 2)) s :=
    (differentiableAt_id.neg.div_const 2).const_cpow (Or.inl hπ)
  have hexp : DifferentiableAt ℂ
      (fun s : ℂ => Complex.exp ((s / 2 - 1 / 2) * Complex.log (s / 2) - s / 2)) s :=
    (((differentiableAt_id.div_const 2).sub_const _).mul
      ((differentiableAt_id.div_const 2).clog
        (mem_slitPlane_of_im_ne_zero' (half_im_ne_zero hs)))
      |>.sub (differentiableAt_id.div_const 2)).cexp
  exact ((hpoly.mul hpow).mul_const _).mul hexp

theorem differentiableAt_Mt (t : ℝ) {s : ℂ} (hs : s.im ≠ 0) : DifferentiableAt ℂ (Mt t) s := by
  have hexp : DifferentiableAt ℂ (fun s : ℂ => Complex.exp ((t : ℂ) / 4 * alpha s ^ 2)) s :=
    (((differentiableAt_alpha hs).pow 2).const_mul _).cexp
  exact hexp.mul (differentiableAt_M0 hs)

/-! ## 3. Nonvanishing of M₀, M_t at points with Im s ≠ 0 -/

theorem M0_ne_zero {s : ℂ} (hs : s.im ≠ 0) : M0 s ≠ 0 := by
  have hs0 : s ≠ 0 := ne_zero_of_im_ne_zero hs
  have hs1 : s - 1 ≠ 0 := sub_one_ne_zero_of_im_ne_zero hs
  have hπ : (π : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr Real.pi_ne_zero
  have hpow : (π : ℂ) ^ (-s / 2) ≠ 0 := by
    rw [Ne, Complex.cpow_eq_zero_iff]
    exact fun h => hπ h.1
  have hsqrt : (Real.sqrt (2 * π) : ℂ) ≠ 0 :=
    Complex.ofReal_ne_zero.mpr (Real.sqrt_ne_zero'.mpr (by positivity))
  unfold M0
  exact mul_ne_zero (mul_ne_zero (mul_ne_zero (mul_ne_zero (by norm_num)
    (div_ne_zero (mul_ne_zero hs0 hs1) two_ne_zero)) hpow) hsqrt) (Complex.exp_ne_zero _)

theorem Mt_ne_zero (t : ℝ) {s : ℂ} (hs : s.im ≠ 0) : Mt t s ≠ 0 :=
  mul_ne_zero (Complex.exp_ne_zero _) (M0_ne_zero hs)

/-! ## 4. L-B3 for `Bt`: off the imaginary axis -/

/-- **L-B3 (nonvanishing).**  B_t(z) ≠ 0 whenever Re z ≠ 0. -/
theorem Bt_ne_zero (t : ℝ) {z : ℂ} (hz : z.re ≠ 0) : Bt t z ≠ 0 := by
  unfold Bt
  apply Mt_ne_zero
  rw [im_half_one_sub_I_mul]
  exact div_ne_zero (neg_ne_zero.mpr hz) two_ne_zero

/-- **L-B3 (holomorphy).**  B_t is complex-differentiable at every z with Re z ≠ 0. -/
theorem differentiableAt_Bt (t : ℝ) {z : ℂ} (hz : z.re ≠ 0) : DifferentiableAt ℂ (Bt t) z := by
  have hinner : DifferentiableAt ℂ (fun z : ℂ => (1 - I * z) / 2) z :=
    ((differentiableAt_const _).sub (differentiableAt_id.const_mul I)).div_const 2
  have him : ((1 - I * z) / 2).im ≠ 0 := by
    rw [im_half_one_sub_I_mul]
    exact div_ne_zero (neg_ne_zero.mpr hz) two_ne_zero
  exact (differentiableAt_Mt t him).comp z hinner

/-! ## 5. The packaged neighborhood form the instance's `hHol` consumes -/

/-- the open right half-plane. -/
theorem isOpen_rightHalfPlane : IsOpen {z : ℂ | 0 < z.re} :=
  isOpen_lt continuous_const Complex.continuous_re

/-- given the displayed `HtEntire`, the normalized g_t = H_t/B_t is differentiable on the open
right half-plane (which contains every rectangle with x₁ > 0). -/
theorem differentiableOn_Ht_div_Bt (hEnt : HtEntire) (t : ℝ) :
    DifferentiableOn ℂ (fun z => Ht t z / Bt t z) {z : ℂ | 0 < z.re} := by
  intro z hz
  have hz' : z.re ≠ 0 := ne_of_gt hz
  exact ((hEnt t).differentiableAt.div (differentiableAt_Bt t hz') (Bt_ne_zero t hz')).differentiableWithinAt

end DBN
end Zeta23

end
