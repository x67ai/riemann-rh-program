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
Zeta23/Separation/LemmaG1.lean — Theorem M2's bump B and Lemmas G0–G1 of the separation note
(rh-program/results/c2-m2/separation-note.md §2): the derivative bounds for B_raw, transported from
Zeta23's `Taper.gevrey_expNegInvGlue`.  Session 23, M4 (i), the dress-rehearsal rung
(rh-program/results/c2-m4/BUILD-NOTES.md).

DEFINITIONS (§1).  The comparator's trusted layer comparator/ChallengeDeps/Separation.lean carries
character-for-character copies of these five definitions under the namespace `Separation`; the
solution modules bridge the two by definitional unfolding.
  Braw v := if |v| < 1/2 then exp (−1/(1 − 4v²)) else 0          (the note's B_raw)
  Z      := ∫ v in −1/2..1/2, Braw v                              (the normalization; no digit of it is asserted)
  B      := Braw / Z
  cB     := 2/√(72e),   CB := e²/Z                                (Lemma G's constants)

RESULTS.
  (G0)  Braw_eq_mul : Braw v = expNegInvGlue (4v + 2) · expNegInvGlue (2 − 4v).  The note's remark
        "B_raw = θ(v + ½)^{1/4}" (θ the Gevrey.lean bump) is deliberately NOT stated: a quarter power
        transfers no derivative bound, and nothing below mentions θ.
  (G1)  abs_iteratedDeriv_Braw_le : ∀ k, ∀ v, |iteratedDeriv k Braw v| ≤ (k + 1)·(72/e)^k·k^{2k}
        (stated for every k; the note states k ≥ 1, and k = 0 reads |B_raw| ≤ 1).  Route:
        (i) the affine chain rule — Mathlib's `iteratedDeriv_comp_const_mul`, `iteratedDeriv_comp_add_const`,
            `iteratedDeriv_comp_const_sub` — gives |d^k/dv^k g(±4v + 2)| ≤ 4^k · gb k, where
            Taper.gb k = (18/e)^k k^{2k} is the (P1) bound `Taper.abs_iteratedDeriv_g_le` (gb 0 = 1);
        (ii) Leibniz — `norm_iteratedFDeriv_mul_le`, the pattern of `Taper.abs_iteratedDeriv_theta_le`;
        (iii) the note's improvement over the on-disk route: C(k,i)·i^i·(k−i)^{k−i} ≤ k^k (one term of the
            binomial expansion of (i + (k − i))^k over ℕ, `add_pow`) and i^i(k−i)^{k−i} ≤ k^i k^{k−i} = k^k, so
            each of the k + 1 Leibniz terms is ≤ (72/e)^k k^{2k}.  (`Taper.gb_mul_gb_le` + Σ_i C(k,i) = 2^k
            would give 2^k in place of k + 1, i.e. A = 144/e and the decay constant 1/(6√e).)
  Also (§4): Braw_nonneg, Braw_le_one, Braw_pos, Braw_eq_zero_of_half_le, Braw_contDiff, Braw_continuous,
  Z_pos, Z_le_one — the facts Lemma G (Zeta23/Separation/LemmaG.lean) consumes.
Conventions: 0^0 = 1 (Lean's `pow_zero`), which is the note's convention for the k = 0 factor bounds.
-/
import Zeta23.Taper.Gevrey

noncomputable section

namespace Zeta23
namespace Separation

open Real Set Finset

/-! ### §1 Definitions (copied character for character into comparator/ChallengeDeps/Separation.lean) -/

/-- the note's B_raw: exp(−1/(1 − 4v²)) on |v| < 1/2, 0 elsewhere. -/
def Braw (v : ℝ) : ℝ := if |v| < 1 / 2 then Real.exp (-1 / (1 - 4 * v ^ 2)) else 0

/-- the normalization Z = ∫_{−1/2}^{1/2} B_raw (a real number defined by an integral; ≈ 0.222). -/
def Z : ℝ := ∫ v in (-1 / 2 : ℝ)..(1 / 2), Braw v

/-- the bump B = B_raw / Z (so that ∫ B = 1). -/
def B (v : ℝ) : ℝ := Braw v / Z

/-- c_B = 2/√(72e). -/
def cB : ℝ := 2 / Real.sqrt (72 * Real.exp 1)

/-- C_B = e²/Z. -/
def CB : ℝ := Real.exp 1 ^ 2 / Z

/-! ### §2 (G0) the factorization through Mathlib's `expNegInvGlue` -/

/-- **(G0)** B_raw(v) = g(4v + 2)·g(2 − 4v) with g = expNegInvGlue, for every real v. -/
theorem Braw_eq_mul (v : ℝ) :
    Braw v = expNegInvGlue (4 * v + 2) * expNegInvGlue (2 - 4 * v) := by
  unfold Braw
  split_ifs with h
  · have hv := abs_lt.mp h
    have h1 : 0 < 4 * v + 2 := by linarith [hv.1]
    have h2 : 0 < 2 - 4 * v := by linarith [hv.2]
    have h3 : 0 < 1 - 4 * v ^ 2 := by nlinarith
    unfold expNegInvGlue
    rw [if_neg (not_le.mpr h1), if_neg (not_le.mpr h2), ← Real.exp_add]
    congr 1
    field_simp
    ring
  · have hv : 1 / 2 ≤ |v| := not_lt.mp h
    rcases le_abs.mp hv with hv | hv
    · rw [expNegInvGlue.zero_of_nonpos (show 2 - 4 * v ≤ 0 by linarith), mul_zero]
    · rw [expNegInvGlue.zero_of_nonpos (show 4 * v + 2 ≤ 0 by linarith), zero_mul]

/-- the left factor v ↦ g(4v + 2). -/
def gL (v : ℝ) : ℝ := expNegInvGlue (4 * v + 2)

/-- the right factor v ↦ g(2 − 4v). -/
def gR (v : ℝ) : ℝ := expNegInvGlue (2 - 4 * v)

theorem Braw_eq_gL_mul_gR : Braw = fun v => gL v * gR v := funext fun v => Braw_eq_mul v

theorem gL_contDiff {n : ℕ∞} : ContDiff ℝ n gL :=
  expNegInvGlue.contDiff.comp ((contDiff_const.mul contDiff_id).add contDiff_const)

theorem gR_contDiff {n : ℕ∞} : ContDiff ℝ n gR :=
  expNegInvGlue.contDiff.comp (contDiff_const.sub (contDiff_const.mul contDiff_id))

/-! ### §3 (G1) the derivative bounds -/

/-- the affine chain rule on the left factor: |d^k/dv^k g(4v + 2)| ≤ 4^k · gb k. -/
theorem abs_iteratedDeriv_gL_le (k : ℕ) (v : ℝ) :
    |iteratedDeriv k gL v| ≤ 4 ^ k * Taper.gb k := by
  have hshift : ContDiff ℝ k (fun w : ℝ => expNegInvGlue (w + 2)) :=
    expNegInvGlue.contDiff.comp (contDiff_id.add contDiff_const)
  have h1 : gL = fun v => (fun w : ℝ => expNegInvGlue (w + 2)) (4 * v) := by
    funext v; simp only [gL]
  rw [h1, iteratedDeriv_comp_const_mul hshift 4]
  simp only []
  rw [iteratedDeriv_comp_add_const]
  simp only [abs_mul, abs_pow, abs_of_pos (show (0:ℝ) < 4 by norm_num)]
  exact mul_le_mul_of_nonneg_left (Taper.abs_iteratedDeriv_g_le k _) (by positivity)

/-- the affine chain rule on the right factor: |d^k/dv^k g(2 − 4v)| ≤ 4^k · gb k. -/
theorem abs_iteratedDeriv_gR_le (k : ℕ) (v : ℝ) :
    |iteratedDeriv k gR v| ≤ 4 ^ k * Taper.gb k := by
  have hflip : ContDiff ℝ k (fun w : ℝ => expNegInvGlue (2 - w)) :=
    expNegInvGlue.contDiff.comp (contDiff_const.sub contDiff_id)
  have h1 : gR = fun v => (fun w : ℝ => expNegInvGlue (2 - w)) (4 * v) := by
    funext v; simp only [gR]
  rw [h1, iteratedDeriv_comp_const_mul hflip 4]
  simp only []
  rw [iteratedDeriv_comp_const_sub]
  simp only [smul_eq_mul, abs_mul, abs_pow, abs_neg, abs_one, one_pow, one_mul,
    abs_of_pos (show (0:ℝ) < 4 by norm_num)]
  exact mul_le_mul_of_nonneg_left (Taper.abs_iteratedDeriv_g_le k _) (by positivity)

/-- the note's step (iii), first half: C(k,i)·i^i·(k−i)^{k−i} ≤ k^k — one term of the binomial
expansion of (i + (k − i))^k over ℕ, all of whose terms are nonnegative. -/
theorem choose_mul_pow_mul_pow_le (k i : ℕ) (hi : i ≤ k) :
    k.choose i * (i ^ i * (k - i) ^ (k - i)) ≤ k ^ k := by
  have h := add_pow i (k - i) k
  rw [Nat.add_sub_cancel' hi] at h
  rw [h]
  have hmem : i ∈ Finset.range (k + 1) := Finset.mem_range.mpr (Nat.lt_succ_of_le hi)
  calc k.choose i * (i ^ i * (k - i) ^ (k - i)) = i ^ i * (k - i) ^ (k - i) * k.choose i := by ring
    _ ≤ ∑ m ∈ Finset.range (k + 1), i ^ m * (k - i) ^ (k - m) * k.choose m :=
        Finset.single_le_sum (f := fun m => i ^ m * (k - i) ^ (k - m) * k.choose m)
          (fun m _ => Nat.zero_le _) hmem

/-- the note's step (iii), second half: i^i·(k−i)^{k−i} ≤ k^i·k^{k−i} = k^k. -/
theorem pow_mul_pow_le (k i : ℕ) (hi : i ≤ k) : i ^ i * (k - i) ^ (k - i) ≤ k ^ k := by
  calc i ^ i * (k - i) ^ (k - i) ≤ k ^ i * k ^ (k - i) :=
        Nat.mul_le_mul (Nat.pow_le_pow_left hi i) (Nat.pow_le_pow_left (Nat.sub_le k i) (k - i))
    _ = k ^ k := by rw [← pow_add, Nat.add_sub_cancel' hi]

/-- the note's step (iii) assembled: C(k,i)·i^{2i}·(k−i)^{2(k−i)} ≤ k^{2k}. -/
theorem choose_mul_sq_le (k i : ℕ) (hi : i ≤ k) :
    k.choose i * (i ^ (2 * i) * (k - i) ^ (2 * (k - i))) ≤ k ^ (2 * k) := by
  rw [pow_mul' i, pow_mul' (k - i), pow_mul' k]
  calc k.choose i * ((i ^ i) ^ 2 * ((k - i) ^ (k - i)) ^ 2)
      = (k.choose i * (i ^ i * (k - i) ^ (k - i))) * (i ^ i * (k - i) ^ (k - i)) := by ring
    _ ≤ k ^ k * k ^ k := Nat.mul_le_mul (choose_mul_pow_mul_pow_le k i hi) (pow_mul_pow_le k i hi)
    _ = (k ^ k) ^ 2 := by ring

/-- one Leibniz term: C(k,i)·(4^i gb i)·(4^{k−i} gb (k−i)) ≤ (72/e)^k k^{2k}. -/
theorem choose_mul_gb_le {k i : ℕ} (hi : i ≤ k) :
    (k.choose i : ℝ) * (4 ^ i * Taper.gb i) * (4 ^ (k - i) * Taper.gb (k - i))
      ≤ (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) := by
  unfold Taper.gb
  have hcast : (k.choose i : ℝ) * ((i : ℝ) ^ (2 * i) * ((k - i : ℕ) : ℝ) ^ (2 * (k - i)))
      ≤ (k : ℝ) ^ (2 * k) := by
    exact_mod_cast choose_mul_sq_le k i hi
  have h4 : (4 : ℝ) ^ i * 4 ^ (k - i) = 4 ^ k := by rw [← pow_add, Nat.add_sub_cancel' hi]
  have h18 : (18 / Real.exp 1) ^ i * (18 / Real.exp 1) ^ (k - i) = (18 / Real.exp 1) ^ k := by
    rw [← pow_add, Nat.add_sub_cancel' hi]
  have h72 : (72 / Real.exp 1) ^ k = 4 ^ k * (18 / Real.exp 1) ^ k := by
    rw [← mul_pow]; congr 1; ring
  have h4k : (0 : ℝ) ≤ 4 ^ k * (18 / Real.exp 1) ^ k := by positivity
  calc (k.choose i : ℝ) * (4 ^ i * ((18 / Real.exp 1) ^ i * (i : ℝ) ^ (2 * i)))
        * (4 ^ (k - i) * ((18 / Real.exp 1) ^ (k - i) * ((k - i : ℕ) : ℝ) ^ (2 * (k - i))))
      = (4 ^ i * 4 ^ (k - i)) * ((18 / Real.exp 1) ^ i * (18 / Real.exp 1) ^ (k - i))
          * ((k.choose i : ℝ) * ((i : ℝ) ^ (2 * i) * ((k - i : ℕ) : ℝ) ^ (2 * (k - i)))) := by ring
    _ = 4 ^ k * (18 / Real.exp 1) ^ k
          * ((k.choose i : ℝ) * ((i : ℝ) ^ (2 * i) * ((k - i : ℕ) : ℝ) ^ (2 * (k - i)))) := by
        rw [h4, h18]
    _ ≤ 4 ^ k * (18 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) := mul_le_mul_of_nonneg_left hcast h4k
    _ = (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) := by rw [h72]

/-- **(G1)** |B_raw^{(k)}(v)| ≤ (k + 1)·(72/e)^k·k^{2k} for every k and every real v
(Leibniz on the (G0) factorization, each of the k + 1 terms bounded by `choose_mul_gb_le`). -/
theorem abs_iteratedDeriv_Braw_le (k : ℕ) (v : ℝ) :
    |iteratedDeriv k Braw v| ≤ ((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) := by
  have hf : ContDiff ℝ k gL := gL_contDiff
  have hg : ContDiff ℝ k gR := gR_contDiff
  have h := norm_iteratedFDeriv_mul_le hf hg v (n := k) le_rfl
  rw [norm_iteratedFDeriv_eq_norm_iteratedDeriv] at h
  simp only [norm_iteratedFDeriv_eq_norm_iteratedDeriv, Real.norm_eq_abs] at h
  rw [Braw_eq_gL_mul_gR]
  refine h.trans ?_
  calc ∑ i ∈ Finset.range (k + 1), (k.choose i : ℝ) * |iteratedDeriv i gL v|
        * |iteratedDeriv (k - i) gR v|
      ≤ ∑ i ∈ Finset.range (k + 1), (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) := by
        refine Finset.sum_le_sum fun i hi => ?_
        have hik : i ≤ k := Nat.lt_succ_iff.mp (Finset.mem_range.mp hi)
        calc (k.choose i : ℝ) * |iteratedDeriv i gL v| * |iteratedDeriv (k - i) gR v|
            ≤ (k.choose i : ℝ) * (4 ^ i * Taper.gb i) * (4 ^ (k - i) * Taper.gb (k - i)) := by
              refine mul_le_mul (mul_le_mul_of_nonneg_left (abs_iteratedDeriv_gL_le i v)
                (Nat.cast_nonneg _)) (abs_iteratedDeriv_gR_le (k - i) v) (abs_nonneg _) ?_
              exact mul_nonneg (Nat.cast_nonneg _) (mul_nonneg (by positivity)
                ((abs_nonneg _).trans (Taper.abs_iteratedDeriv_g_le i v)))
          _ ≤ (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) := choose_mul_gb_le hik
    _ = ((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) := by
        rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]; push_cast; ring

/-! ### §4 Elementary facts about B_raw and Z consumed by Lemma G -/

theorem Braw_nonneg (v : ℝ) : 0 ≤ Braw v := by
  unfold Braw; split_ifs
  · exact (Real.exp_pos _).le
  · exact le_rfl

theorem Braw_le_one (v : ℝ) : Braw v ≤ 1 := by
  unfold Braw; split_ifs with h
  · have hv := abs_lt.mp h
    have h3 : 0 < 1 - 4 * v ^ 2 := by nlinarith
    rw [Real.exp_le_one_iff, div_le_iff₀ h3]
    linarith
  · exact zero_le_one

theorem Braw_pos {v : ℝ} (h : |v| < 1 / 2) : 0 < Braw v := by
  unfold Braw; rw [if_pos h]; exact Real.exp_pos _

theorem Braw_eq_zero_of_half_le {v : ℝ} (h : 1 / 2 ≤ |v|) : Braw v = 0 := by
  unfold Braw; rw [if_neg (not_lt.mpr h)]

theorem Braw_contDiff {n : ℕ∞} : ContDiff ℝ n Braw := by
  rw [Braw_eq_gL_mul_gR]; exact gL_contDiff.mul gR_contDiff

theorem Braw_continuous : Continuous Braw := (Braw_contDiff (n := 0)).continuous

/-- Z > 0 (B_raw is continuous and positive on (−1/2, 1/2)). -/
theorem Z_pos : 0 < Z := by
  unfold Z
  refine intervalIntegral.intervalIntegral_pos_of_pos_on (Braw_continuous.intervalIntegrable _ _)
    (fun x hx => Braw_pos (abs_lt.mpr ⟨by linarith [hx.1], hx.2⟩)) (by norm_num)

/-- Z ≤ 1 (B_raw ≤ 1 on an interval of length 1). -/
theorem Z_le_one : Z ≤ 1 := by
  unfold Z
  calc (∫ v in (-1 / 2 : ℝ)..(1 / 2), Braw v) ≤ ∫ _ in (-1 / 2 : ℝ)..(1 / 2), (1 : ℝ) :=
        intervalIntegral.integral_mono_on (by norm_num) (Braw_continuous.intervalIntegrable _ _)
          (continuous_const.intervalIntegrable _ _) (fun x _ => Braw_le_one x)
    _ = 1 := by rw [intervalIntegral.integral_const]; norm_num

end Separation
end Zeta23
