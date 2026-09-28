/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does not import it: it imports Mathlib only
(through ChallengeDeps.WeilContainment).
-/
/-
comparator/Solution/WeilContainment.lean — the UNTRUSTED comparator solution module for the topic `WeilContainment` (the D5
unit, barrier-zoo IV.1): the twelve statements of Challenge/WeilContainment.lean, byte-identical, PROVED over Mathlib alone.
No Zeta23 import is needed and none is used: every object is defined in the trusted ChallengeDeps.WeilContainment from
Mathlib, and every proof is elementary (rpow algebra for (T1), monotonicity of exp for (T2), support and continuity lemmas
and `exp_add` for (T3), `tsum_eq_sum` for the cutoff, the two containments assembled into the set equality, and
`not_differentiableAt_abs_zero` for the negative witness).  The helper
lemmas live in the namespace `WeilContainment.Proof`; the rung-1 module Solution/WeilContainmentOne.lean carries its own copy
of the (T1) computation so that each topic is self-contained.  This module never imports the challenge.  Nothing in this file
is part of the trusted base: comparator re-checks that each theorem below has exactly the statement of its Challenge namesake
and uses only the permitted axioms.
-/
import ChallengeDeps.WeilContainment

noncomputable section

open WeilContainment

namespace WeilContainment.Proof

theorem tilt_even (a u : ℝ) : tilt a (-u) = tilt a u := by
  simp [tilt, abs_neg]

theorem tilt_pos (a u : ℝ) : 0 < tilt a u := Real.exp_pos _

theorem tilt_of_nonneg (a u : ℝ) (hu : 0 ≤ u) : tilt a u = Real.exp (-(a - 1 / 2) * u) := by
  simp [tilt, abs_of_nonneg hu]

theorem tilt_mul_tilt (a u : ℝ) : tilt a u * tilt (1 - a) u = 1 := by
  unfold tilt
  rw [← Real.exp_add]
  have h : -(a - 1 / 2) * |u| + -(1 - a - 1 / 2) * |u| = 0 := by ring
  rw [h, Real.exp_zero]

/-- the summand identity, for every n : ℕ (n = 0 by Λ 0 = 0; n ≥ 1 by the rpow computation). -/
theorem summand_eq (a : ℝ) (g : ℝ → ℂ) (hg : ∀ u, g (-u) = g u) (n : ℕ) :
    ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) * g (Real.log n)
      = ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ)
          * (weilTestOf a g (Real.log n) + weilTestOf a g (-Real.log n)) := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp
  · have hn' : (0 : ℝ) < n := by exact_mod_cast hn
    have hlog : 0 ≤ Real.log n := Real.log_nonneg (by exact_mod_cast hn)
    have h1 : weilTestOf a g (Real.log n) + weilTestOf a g (-Real.log n)
        = g (Real.log n) * (tilt a (Real.log n) : ℂ) := by
      simp only [weilTestOf, hg, tilt_even]; ring
    have h2 : tilt a (Real.log n) = (n : ℝ) ^ (1 / 2 - a) := by
      rw [tilt_of_nonneg _ _ hlog, Real.rpow_def_of_pos hn']; congr 1; ring
    have h3 : ArithmeticFunction.vonMangoldt n / Real.sqrt n * (n : ℝ) ^ (1 / 2 - a)
        = ArithmeticFunction.vonMangoldt n * (n : ℝ) ^ (-a) := by
      rw [Real.sqrt_eq_rpow, div_eq_mul_inv, ← Real.rpow_neg hn'.le, mul_assoc, ← Real.rpow_add hn']
      congr 2; ring
    have h3' : ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) * (((n : ℝ) ^ (1 / 2 - a) : ℝ) : ℂ)
        = ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) := by
      rw [← Complex.ofReal_mul, h3, Complex.ofReal_mul]
    rw [h1, h2, ← h3']; ring

/-- (T1). -/
theorem identity (a : ℝ) (g : ℝ → ℂ) (hg : ∀ u, g (-u) = g u) :
    tiltedPrimeSide a g = primeSide (weilTestOf a g) := by
  unfold tiltedPrimeSide primeSide
  exact tsum_congr (fun n => summand_eq a g hg n)

/-- the support of weilTestOf a g is the support of g (tilt never vanishes). -/
theorem support_weilTestOf (a : ℝ) (g : ℝ → ℂ) :
    Function.support (weilTestOf a g) = Function.support g := by
  ext u
  simp [weilTestOf, Function.mem_support, (tilt_pos a u).ne']

theorem tsupport_weilTestOf (a : ℝ) (g : ℝ → ℂ) : tsupport (weilTestOf a g) = tsupport g := by
  simp only [tsupport, support_weilTestOf]

theorem weilTestOf_even (a : ℝ) (g : ℝ → ℂ) (hg : ∀ u, g (-u) = g u) (u : ℝ) :
    weilTestOf a g (-u) = weilTestOf a g u := by
  simp only [weilTestOf, hg, tilt_even]

/-- the witness of the converse containment: g = 2 k · tilt (1 − a). -/
theorem exact (a L : ℝ) (k : ℝ → ℂ) (hk : ∀ u, k (-u) = k u) (hks : tsupport k ⊆ Set.Icc (-L) L) :
    ∃ g : ℝ → ℂ, (∀ u, g (-u) = g u) ∧ tsupport g ⊆ Set.Icc (-L) L ∧ primeSide k = tiltedPrimeSide a g := by
  set g : ℝ → ℂ := fun u => 2 * k u * (tilt (1 - a) u : ℂ) with hgdef
  have hgeven : ∀ u, g (-u) = g u := by
    intro u; simp only [hgdef, hk, tilt_even]
  have hsupp : Function.support g = Function.support k := by
    ext u; simp [hgdef, Function.mem_support, (tilt_pos (1 - a) u).ne']
  refine ⟨g, hgeven, ?_, ?_⟩
  · calc tsupport g = tsupport k := by simp only [tsupport, hsupp]
      _ ⊆ Set.Icc (-L) L := hks
  · rw [identity a g hgeven]
    congr 1
    funext u
    have hc : (tilt a u : ℂ) * (tilt (1 - a) u : ℂ) = 1 := by
      rw [← Complex.ofReal_mul, tilt_mul_tilt, Complex.ofReal_one]
    simp only [weilTestOf, hgdef]
    linear_combination (-(k u)) * hc

end WeilContainment.Proof

open WeilContainment.Proof

/-- **(T1) the containment identity**: for every real a and every even g, the level-a tilted prime side is the classical
prime datum at the test k_{a,g}. -/
theorem weilContainment_identity :
    ∀ (a : ℝ) (g : ℝ → ℂ), (∀ u, g (-u) = g u) →
      tiltedPrimeSide a g = primeSide (weilTestOf a g) :=
  fun a g hg => identity a g hg

/-- **(T1′) the cutoff**: for tsupport g ⊆ [−L, L] the tilted prime side is the finite sum over 0 ≤ n ≤ ⌊e^L⌋. -/
theorem weilContainment_cutoff :
    ∀ (a L : ℝ) (g : ℝ → ℂ), tsupport g ⊆ Set.Icc (-L) L →
      tiltedPrimeSide a g = ∑ n ∈ Finset.range (⌊Real.exp L⌋₊ + 1),
        ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) * g (Real.log n) := by
  intro a L g hg
  unfold tiltedPrimeSide
  apply tsum_eq_sum
  intro n hn
  have hn' : ⌊Real.exp L⌋₊ < n := by
    rw [Finset.mem_range, not_lt] at hn; omega
  have hlt : Real.exp L < n := Nat.lt_of_floor_lt hn'
  have hL : L < Real.log n := (Real.lt_log_iff_exp_lt (lt_trans (Real.exp_pos L) hlt)).mpr hlt
  have hg0 : g (Real.log n) = 0 := by
    apply image_eq_zero_of_notMem_tsupport
    intro hmem
    exact absurd (hg hmem).2 (not_le.mpr hL)
  rw [hg0, mul_zero]

/-- **(T2) the multiplier bounds** on the band |u| ≤ L: e^{−|a−1/2| L} ≤ m_a(u) ≤ e^{|a−1/2| L}. -/
theorem weilContainment_tilt_bounds :
    ∀ (a L u : ℝ), |u| ≤ L →
      Real.exp (-(|a - 1 / 2| * L)) ≤ tilt a u ∧ tilt a u ≤ Real.exp (|a - 1 / 2| * L) := by
  intro a L u hu
  unfold tilt
  have h0 : abs (-(a - 1 / 2) * |u|) ≤ |a - 1 / 2| * L := by
    rw [abs_mul, abs_neg, abs_abs]
    exact mul_le_mul_of_nonneg_left hu (abs_nonneg _)
  rw [abs_le] at h0
  exact ⟨Real.exp_le_exp.mpr h0.1, Real.exp_le_exp.mpr h0.2⟩

/-- **(T2) positivity**: m_a(u) > 0 for every a and u. -/
theorem weilContainment_tilt_pos : ∀ (a u : ℝ), 0 < tilt a u :=
  fun a u => tilt_pos a u

/-- **(T3) the inverse**: m_a(u)·m_{1−a}(u) = 1. -/
theorem weilContainment_tilt_inv : ∀ (a u : ℝ), tilt a u * tilt (1 - a) u = 1 :=
  fun a u => tilt_mul_tilt a u

/-- **(T3) evenness**: k_{a,g} is even when g is. -/
theorem weilContainment_even :
    ∀ (a : ℝ) (g : ℝ → ℂ), (∀ u, g (-u) = g u) → ∀ u, weilTestOf a g (-u) = weilTestOf a g u :=
  fun a g hg u => weilTestOf_even a g hg u

/-- **(T3) the band**: tsupport k_{a,g} ⊆ tsupport g. -/
theorem weilContainment_tsupport :
    ∀ (a : ℝ) (g : ℝ → ℂ), tsupport (weilTestOf a g) ⊆ tsupport g :=
  fun a g => (tsupport_weilTestOf a g).le

/-- **(T3) the band, exactly**: tsupport k_{a,g} = tsupport g. -/
theorem weilContainment_tsupport_eq :
    ∀ (a : ℝ) (g : ℝ → ℂ), tsupport (weilTestOf a g) = tsupport g :=
  fun a g => tsupport_weilTestOf a g

/-- **(T3) continuity**: k_{a,g} is continuous when g is. -/
theorem weilContainment_continuous :
    ∀ (a : ℝ) (g : ℝ → ℂ), Continuous g → Continuous (weilTestOf a g) := by
  intro a g hg
  have ht : Continuous (tilt a) := Real.continuous_exp.comp (continuous_const.mul continuous_abs)
  exact (continuous_const.mul hg).mul (Complex.continuous_ofReal.comp ht)

/-- **(T3) the converse containment**: every classical prime datum of an even test k on the band [−L, L] is the level-a
tilted datum of an even g on the same band. -/
theorem weilContainment_exact :
    ∀ (a L : ℝ) (k : ℝ → ℂ), (∀ u, k (-u) = k u) → tsupport k ⊆ Set.Icc (-L) L →
      ∃ g : ℝ → ℂ, (∀ u, g (-u) = g u) ∧ tsupport g ⊆ Set.Icc (-L) L ∧ primeSide k = tiltedPrimeSide a g :=
  fun a L k hk hks => exact a L k hk hks

/-- **IV.1, the record's sentence**: for every real a and L, the level-a tilted prime data over even band-[−L, L] tests are
EXACTLY the classical Weil-EF prime data over even band-[−L, L] tests. -/
theorem weilContainment_range_eq :
    ∀ (a L : ℝ),
      {x : ℂ | ∃ g : ℝ → ℂ, (∀ u, g (-u) = g u) ∧ tsupport g ⊆ Set.Icc (-L) L ∧ x = tiltedPrimeSide a g} =
      {x : ℂ | ∃ k : ℝ → ℂ, (∀ u, k (-u) = k u) ∧ tsupport k ⊆ Set.Icc (-L) L ∧ x = primeSide k} := by
  intro a L
  ext x
  constructor
  · rintro ⟨g, hg, hgs, rfl⟩
    exact ⟨weilTestOf a g, weilTestOf_even a g hg, (tsupport_weilTestOf a g).le.trans hgs, identity a g hg⟩
  · rintro ⟨k, hk, hks, rfl⟩
    obtain ⟨g, hg, hgs, hgk⟩ := exact a L k hk hks
    exact ⟨g, hg, hgs, hgk⟩

/-- **The C² class is not preserved** (witness): at a = 1 and g ≡ 1 the test k_{1,1}(u) = (1/2)·e^{−|u|/2} is not C² (it is not
even differentiable at u = 0). -/
theorem weilContainment_not_contDiff : ¬ ContDiff ℝ 2 (weilTestOf 1 (fun _ => (1 : ℂ))) := by
  intro h
  have hfun : weilTestOf 1 (fun _ => (1 : ℂ)) =
      fun u => ((1 / 2 * Real.exp (-(1 / 2) * |u|) : ℝ) : ℂ) := by
    funext u
    simp only [weilTestOf, tilt]
    push_cast
    ring_nf
  have hd : DifferentiableAt ℝ (weilTestOf 1 (fun _ => (1 : ℂ))) 0 :=
    (h.differentiable (by norm_num)).differentiableAt
  have hre : DifferentiableAt ℝ (Complex.reCLM ∘ weilTestOf 1 (fun _ => (1 : ℂ))) 0 :=
    Complex.reCLM.differentiableAt.comp 0 hd
  have hre' : DifferentiableAt ℝ (fun u : ℝ => 1 / 2 * Real.exp (-(1 / 2) * |u|)) 0 := by
    have : (Complex.reCLM ∘ weilTestOf 1 (fun _ => (1 : ℂ))) =
        fun u : ℝ => 1 / 2 * Real.exp (-(1 / 2) * |u|) := by
      rw [hfun]; funext u; simp only [Function.comp, Complex.reCLM_apply, Complex.ofReal_re]
    rwa [this] at hre
  have hlog : DifferentiableAt ℝ
      (fun u : ℝ => -2 * Real.log (2 * (1 / 2 * Real.exp (-(1 / 2) * |u|)))) 0 := by
    apply DifferentiableAt.const_mul
    apply DifferentiableAt.log
    · exact hre'.const_mul 2
    · have := Real.exp_pos (-(1 / 2) * |(0 : ℝ)|)
      positivity
  have habs : (fun u : ℝ => -2 * Real.log (2 * (1 / 2 * Real.exp (-(1 / 2) * |u|)))) =
      fun u : ℝ => |u| := by
    funext u
    rw [show 2 * (1 / 2 * Real.exp (-(1 / 2) * |u|)) = Real.exp (-(1 / 2) * |u|) by ring, Real.log_exp]
    ring
  rw [habs] at hlog
  exact not_differentiableAt_abs_zero hlog
