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
Zeta23/Separation/LemmaG.lean — Lemma G of Theorem M2's separation note (rh-program/results/c2-m2/separation-note.md
§2): the Fourier decay of the bump B = B_raw/Z, proved from the derivative bounds of Zeta23/Separation/LemmaG1.lean and
the one-step integration by parts `Zeta23.paperFT_deriv` (Zeta23/Poisson/PaperFT.lean).  Session 23, M4 (i)
(rh-program/results/c2-m4/BUILD-NOTES.md).  No displayed hypothesis: every object is concrete.

STATEMENTS (the transform is the paper's h_f(z) = ∫ f(u) e^{izu} du, `Zeta23.paperFT`; c_B = 2/√(72e), C_B = e²/Z):
  norm_paperFT_Bc_le (z : ℂ)        ‖B̂(z)‖ ≤ e^{|Im z|/2} · C_B (1 + (c_B/2)√|Re z|) e^{−c_B√|Re z|}   (the complex form)
  norm_paperFT_Bc_ofReal_le (η : ℝ) ‖B̂(η)‖ ≤ C_B (1 + (c_B/2)√|η|) e^{−c_B√|η|}                          (G1)
  norm_paperFT_Bc_ofReal_le' (η : ℝ) ‖B̂(η)‖ ≤ 4e^{−3/4} C_B · e^{−(7/8)c_B√|η|}                          (G2)
where B̂ = paperFT (fun v => (B v : ℂ)).

ROUTE (the note's proof, step for step).
  §1  B is C^∞ with support in [−1/2, 1/2]; ‖D^k(B : ℝ → ℂ)‖ = |D^k B| (Complex.ofRealLI, a linear isometry) and
      |D^k B| ≤ (k + 1)(72/e)^k k^{2k}/Z (Lemma G1); D^k(B : ℝ → ℂ) vanishes off [−1/2, 1/2] (tsupport of iteratedFDeriv).
  §2  k-fold integration by parts: paperFT (D^k f) z = (−iz)^k · paperFT f z for f ∈ C^∞_c (induction on `paperFT_deriv`),
      so ‖B̂(z)‖ ‖z‖^k ≤ e^{|Im z|/2} ∫|D^k B| ≤ e^{|Im z|/2} (k + 1)(72/e)^k k^{2k}/Z  (`norm_paperFT_le` with Λ = 1/2,
      and ∫ over the unit-length support).  Also ∫ B = 1, so ‖B̂(z)‖ ≤ e^{|Im z|/2}.
  §3  With s = |Re z| and κ = (c_B/2)√s (so (72/e)κ² = s/e² and c_B√s = 2κ): if κ < 1 use ‖B̂‖ ≤ e^{|Im z|/2} and
      C_B e^{−2κ} ≥ C_B e^{−2} = 1/Z ≥ 1; if κ ≥ 1 take k = ⌊κ⌋ ≥ 1, then (72/e)^k k^{2k} ≤ (s/e²)^k, k + 1 ≤ 1 + κ,
      e^{−2k} ≤ e² e^{−2κ}, and divide by s^k > 0.  (G2): (1 + x/2)e^{−x} ≤ 4e^{−3/4}e^{−7x/8} from e^t ≥ 1 + t at
      t = (x − 6)/8.
FIDELITY (PRICING §1(b)(i) (a)–(g); formalization.yaml / FIDELITY.md (o)): B is the exp formula (a); Z and C_B are reals
defined by an integral, no digit asserted (b); the transform is `paperFT` re-declared in the trusted layer as `ft` (c);
the prefactor (1 + (c_B/2)√|η|) is kept and (G2) is a separate theorem (d); the number 2/√(72e) is stated, its provenance
is not a theorem (e); the complex form's strip weight is e^{|Im z|/2} for the support [−1/2, 1/2] — the note's clause-5
use at L(x − t) − iLy is an instance by scaling, not stated here (f); `iteratedDeriv` = the classical derivative for C^∞
functions (g).
-/
import Zeta23.Separation.LemmaG1
import Zeta23.Poisson.PaperFT

noncomputable section

namespace Zeta23
namespace Separation

open Real Set MeasureTheory Complex Filter Topology
open scoped ContDiff

/-! ### §1 The bump as a complex-valued function: smoothness, support, derivative bounds -/

theorem B_contDiff {n : ℕ∞} : ContDiff ℝ n B := Braw_contDiff.div_const Z

theorem B_nonneg (v : ℝ) : 0 ≤ B v := div_nonneg (Braw_nonneg v) Z_pos.le

theorem B_eq_zero_of_half_le {v : ℝ} (h : 1 / 2 ≤ |v|) : B v = 0 := by
  rw [B, Braw_eq_zero_of_half_le h, zero_div]

theorem Bc_contDiff : ContDiff ℝ ∞ (fun v => (B v : ℂ)) :=
  Complex.ofRealCLM.contDiff.comp (B_contDiff (n := ⊤))

theorem Bc_support : ∀ u : ℝ, (fun v => (B v : ℂ)) u ≠ 0 → |u| ≤ 1 / 2 := fun u hu => by
  by_contra h
  exact hu (by simp [B_eq_zero_of_half_le (not_le.mp h).le])

theorem hasCompactSupport_Bc : HasCompactSupport (fun v => (B v : ℂ)) :=
  hasCompactSupport_of_support_subset_abs Bc_support

theorem Bc_integrable : Integrable (fun v => (B v : ℂ)) :=
  Bc_contDiff.continuous.integrable_of_hasCompactSupport hasCompactSupport_Bc

/-- ‖D^k (B : ℝ → ℂ)‖ = |D^k B| — the real embedding is a linear isometry. -/
theorem norm_iteratedDeriv_Bc (k : ℕ) (u : ℝ) :
    ‖iteratedDeriv k (fun v => (B v : ℂ)) u‖ = |iteratedDeriv k B u| := by
  rw [← norm_iteratedFDeriv_eq_norm_iteratedDeriv, ← Real.norm_eq_abs,
    ← norm_iteratedFDeriv_eq_norm_iteratedDeriv]
  exact Complex.ofRealLI.norm_iteratedFDeriv_comp_left (f := B) (B_contDiff (n := ⊤)).contDiffAt
    (by exact_mod_cast le_top)

/-- |D^k B| ≤ (k + 1)(72/e)^k k^{2k} / Z (Lemma G1 divided by Z). -/
theorem abs_iteratedDeriv_B_le (k : ℕ) (u : ℝ) :
    |iteratedDeriv k B u| ≤ ((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) / Z := by
  have hZ := Z_pos
  unfold B
  rw [iteratedDeriv_div_const, abs_div, abs_of_pos hZ]
  gcongr
  exact abs_iteratedDeriv_Braw_le k u

/-- D^k (B : ℝ → ℂ) vanishes off [−1/2, 1/2]. -/
theorem iteratedDeriv_Bc_eq_zero {k : ℕ} {u : ℝ} (hu : 1 / 2 < |u|) :
    iteratedDeriv k (fun v => (B v : ℂ)) u = 0 := by
  have hts : tsupport (fun v => (B v : ℂ)) ⊆ Icc (-(1 / 2)) (1 / 2) :=
    tsupport_subset_of_support_subset_abs Bc_support
  have hnot : u ∉ tsupport (iteratedFDeriv ℝ k (fun v => (B v : ℂ))) := fun h => by
    have hmem := hts (tsupport_iteratedFDeriv_subset k h)
    have : |u| ≤ 1 / 2 := abs_le.mpr ⟨hmem.1, hmem.2⟩
    linarith
  rw [iteratedDeriv_eq_iteratedFDeriv, image_eq_zero_of_notMem_tsupport hnot]
  rfl

theorem hasCompactSupport_iteratedDeriv {f : ℝ → ℂ} (hs : HasCompactSupport f) :
    ∀ k : ℕ, HasCompactSupport (iteratedDeriv k f)
  | 0 => by rw [iteratedDeriv_zero]; exact hs
  | k + 1 => by rw [iteratedDeriv_succ]; exact (hasCompactSupport_iteratedDeriv hs k).deriv

theorem contDiff_iteratedDeriv {f : ℝ → ℂ} (hf : ContDiff ℝ ∞ f) (k : ℕ) :
    ContDiff ℝ ∞ (iteratedDeriv k f) := by
  rw [iteratedDeriv_eq_iterate]; exact hf.iterate_deriv k

/-- ∫ ‖D^k (B : ℝ → ℂ)‖ ≤ (k + 1)(72/e)^k k^{2k} / Z: the support has length 1. -/
theorem integral_norm_iteratedDeriv_Bc_le (k : ℕ) :
    ∫ u, ‖iteratedDeriv k (fun v => (B v : ℂ)) u‖
      ≤ ((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) / Z := by
  have hZ := Z_pos
  set M : ℝ := ((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) / Z with hM
  have hM0 : 0 ≤ M := by positivity
  have hind : Integrable ((Icc (-(1 / 2 : ℝ)) (1 / 2)).indicator (fun _ => M)) := by
    rw [integrable_indicator_iff measurableSet_Icc]
    exact integrableOn_const (by rw [Real.volume_Icc]; exact ENNReal.ofReal_ne_top)
  calc ∫ u, ‖iteratedDeriv k (fun v => (B v : ℂ)) u‖
      ≤ ∫ u, (Icc (-(1 / 2 : ℝ)) (1 / 2)).indicator (fun _ => M) u := by
        refine integral_mono_of_nonneg (Eventually.of_forall fun u => norm_nonneg _) hind
          (Eventually.of_forall ?_)
        intro u
        show ‖iteratedDeriv k (fun v => (B v : ℂ)) u‖ ≤ _
        by_cases hu : u ∈ Icc (-(1 / 2 : ℝ)) (1 / 2)
        · rw [indicator_of_mem hu, norm_iteratedDeriv_Bc]
          exact abs_iteratedDeriv_B_le k u
        · rw [indicator_of_notMem hu]
          have hu' : 1 / 2 < |u| := by
            rw [mem_Icc, not_and_or] at hu
            rcases hu with h | h
            · have h1 := not_le.mp h
              have h2 := neg_le_abs u
              linarith
            · exact lt_of_lt_of_le (not_le.mp h) (le_abs_self u)
          rw [iteratedDeriv_Bc_eq_zero hu', norm_zero]
    _ = M := by
        rw [integral_indicator_const _ measurableSet_Icc, smul_eq_mul, Real.volume_real_Icc]
        norm_num

/-! ### §2 k-fold integration by parts and the two basic bounds -/

/-- paperFT (D^k f) z = (−iz)^k · paperFT f z for f ∈ C^∞_c — `paperFT_deriv` iterated. -/
theorem paperFT_iteratedDeriv {f : ℝ → ℂ} (hf : ContDiff ℝ ∞ f) (hs : HasCompactSupport f) (z : ℂ) :
    ∀ k : ℕ, paperFT (iteratedDeriv k f) z = (-(I * z)) ^ k * paperFT f z
  | 0 => by rw [iteratedDeriv_zero, pow_zero, one_mul]
  | k + 1 => by
    rw [iteratedDeriv_succ,
      paperFT_deriv ((contDiff_iteratedDeriv hf k).of_le (by exact_mod_cast le_top))
        (hasCompactSupport_iteratedDeriv hs k),
      paperFT_iteratedDeriv hf hs z k, pow_succ]
    ring

/-- ∫ B_raw over ℝ = Z (B_raw vanishes off (−1/2, 1/2]). -/
theorem integral_Braw : ∫ u, Braw u = Z := by
  have hzero : ∀ u, u ∉ Ioc (-1 / 2 : ℝ) (1 / 2) → Braw u = 0 := by
    intro u hu
    rw [mem_Ioc, not_and_or] at hu
    apply Braw_eq_zero_of_half_le
    rcases hu with h | h
    · exact le_abs.mpr (Or.inr (by linarith [not_lt.mp h]))
    · exact le_abs.mpr (Or.inl (by linarith [not_le.mp h]))
  rw [Z, intervalIntegral.integral_of_le (by norm_num),
    setIntegral_eq_integral_of_forall_compl_eq_zero hzero]

/-- ∫ ‖(B : ℝ → ℂ)‖ = 1. -/
theorem integral_norm_Bc : ∫ u, ‖(B u : ℂ)‖ = 1 := by
  have hZ := Z_pos
  have h1 : (fun u => ‖(B u : ℂ)‖) = fun u => Braw u / Z := by
    funext u
    rw [Complex.norm_real, Real.norm_eq_abs, B, abs_of_nonneg (div_nonneg (Braw_nonneg u) hZ.le)]
  rw [h1, integral_div, integral_Braw, div_self hZ.ne']

/-- ‖B̂(z)‖ ≤ e^{|Im z|/2}. -/
theorem norm_paperFT_Bc_le_exp (z : ℂ) :
    ‖paperFT (fun v => (B v : ℂ)) z‖ ≤ Real.exp (|z.im| / 2) := by
  have h := norm_paperFT_le Bc_integrable Bc_support z
  rw [integral_norm_Bc, mul_one, show |z.im| * (1 / 2) = |z.im| / 2 by ring] at h
  exact h

/-- ‖B̂(z)‖ · ‖z‖^k ≤ e^{|Im z|/2} · (k + 1)(72/e)^k k^{2k} / Z. -/
theorem norm_paperFT_Bc_mul_le (k : ℕ) (z : ℂ) :
    ‖paperFT (fun v => (B v : ℂ)) z‖ * ‖z‖ ^ k
      ≤ Real.exp (|z.im| / 2) * (((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) / Z) := by
  have hint : Integrable (iteratedDeriv k (fun v => (B v : ℂ))) :=
    (Bc_contDiff.continuous_iteratedDeriv k (by exact_mod_cast le_top)).integrable_of_hasCompactSupport
      (hasCompactSupport_iteratedDeriv hasCompactSupport_Bc k)
  have hsupp : ∀ u, iteratedDeriv k (fun v => (B v : ℂ)) u ≠ 0 → |u| ≤ 1 / 2 := fun u hu => by
    by_contra h
    exact hu (iteratedDeriv_Bc_eq_zero (not_le.mp h))
  have h := norm_paperFT_le hint hsupp z
  rw [paperFT_iteratedDeriv Bc_contDiff hasCompactSupport_Bc z k, norm_mul, norm_pow, norm_neg,
    norm_mul, Complex.norm_I, one_mul, show |z.im| * (1 / 2) = |z.im| / 2 by ring] at h
  calc ‖paperFT (fun v => (B v : ℂ)) z‖ * ‖z‖ ^ k
      = ‖z‖ ^ k * ‖paperFT (fun v => (B v : ℂ)) z‖ := by ring
    _ ≤ Real.exp (|z.im| / 2) * ∫ u, ‖iteratedDeriv k (fun v => (B v : ℂ)) u‖ := h
    _ ≤ Real.exp (|z.im| / 2) * (((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) / Z) := by
        gcongr
        exact integral_norm_iteratedDeriv_Bc_le k

/-! ### §3 The choice of k and the assembly -/

theorem cB_pos : 0 < cB := by unfold cB; positivity

theorem CB_pos : 0 < CB := by have := Z_pos; unfold CB; positivity

/-- the exponent bookkeeping for k = ⌊κ⌋: (k + 1)(72/e)^k k^{2k}/Z ≤ C_B (1 + κ) e^{−2κ} s^k when (72/e)κ² = s/e²,
k ≤ κ < k + 1. -/
theorem key_ineq {s κ : ℝ} (hs : 0 < s) (hκ0 : 0 ≤ κ)
    (hκs : (72 / Real.exp 1) * κ ^ 2 = s / Real.exp 1 ^ 2) (k : ℕ) (hkκ : (k : ℝ) ≤ κ)
    (hκk : κ < k + 1) :
    ((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) / Z
      ≤ CB * (1 + κ) * Real.exp (-(2 * κ)) * s ^ k := by
  have hZ := Z_pos
  have hE := Real.exp_pos 1
  have hA : (72 / Real.exp 1) * (k : ℝ) ^ 2 ≤ s / Real.exp 1 ^ 2 := by
    rw [← hκs]; gcongr
  have hpow : (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) ≤ (s / Real.exp 1 ^ 2) ^ k := by
    rw [pow_mul, ← mul_pow]; exact pow_le_pow_left₀ (by positivity) hA k
  have hexp : 1 ≤ Real.exp 1 ^ 2 * Real.exp (-(2 * κ)) * Real.exp 1 ^ (2 * k) := by
    have e1 : Real.exp 1 ^ 2 * Real.exp (-(2 * κ)) * Real.exp 1 ^ (2 * k)
        = Real.exp ((2 * k + 2 : ℕ)) * Real.exp (-(2 * κ)) := by
      rw [← Real.exp_one_pow]; ring
    rw [e1, ← Real.exp_add, Real.one_le_exp_iff]; push_cast; linarith
  have hinv : 1 / Real.exp 1 ^ (2 * k) ≤ Real.exp 1 ^ 2 * Real.exp (-(2 * κ)) := by
    rw [div_le_iff₀ (by positivity)]; exact hexp
  have hk1 : (k : ℝ) + 1 ≤ 1 + κ := by linarith
  calc ((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) / Z
      = ((k : ℝ) + 1) * ((72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k)) / Z := by ring
    _ ≤ (1 + κ) * (s / Real.exp 1 ^ 2) ^ k / Z := by gcongr
    _ = (1 + κ) * (s ^ k * (1 / Real.exp 1 ^ (2 * k))) / Z := by
        rw [div_pow, ← pow_mul]; ring
    _ ≤ (1 + κ) * (s ^ k * (Real.exp 1 ^ 2 * Real.exp (-(2 * κ)))) / Z := by gcongr
    _ = CB * (1 + κ) * Real.exp (-(2 * κ)) * s ^ k := by rw [CB]; ring

/-- **Lemma G, complex-argument form**: for every z ∈ ℂ,
‖B̂(z)‖ ≤ e^{|Im z|/2} · C_B (1 + (c_B/2)√|Re z|) e^{−c_B√|Re z|}. -/
theorem norm_paperFT_Bc_le (z : ℂ) :
    ‖paperFT (fun v => (B v : ℂ)) z‖
      ≤ Real.exp (|z.im| / 2)
        * (CB * (1 + cB / 2 * Real.sqrt |z.re|) * Real.exp (-(cB * Real.sqrt |z.re|))) := by
  have hZ := Z_pos
  have hZ1 := Z_le_one
  have hE := Real.exp_pos 1
  have hE0 : Real.exp 1 ≠ 0 := hE.ne'
  have hCB := CB_pos
  have hcB := cB_pos
  set s : ℝ := |z.re| with hs
  have hs0 : 0 ≤ s := abs_nonneg _
  set κ : ℝ := cB / 2 * Real.sqrt s with hκ
  have hκ0 : 0 ≤ κ := by positivity
  have key : cB * Real.sqrt s = 2 * κ := by rw [hκ]; ring
  rw [key]
  rcases lt_or_ge κ 1 with hlt | hge
  · -- κ < 1: the trivial bound ‖B̂‖ ≤ e^{|Im z|/2} and C_B e^{−2κ} ≥ C_B e^{−2} = 1/Z ≥ 1
    refine (norm_paperFT_Bc_le_exp z).trans (le_mul_of_one_le_right (Real.exp_pos _).le ?_)
    have hCBexp : 1 ≤ CB * Real.exp (-2) := by
      have e2 : Real.exp (-2) = 1 / Real.exp 1 ^ 2 := by
        rw [Real.exp_neg, Real.exp_one_pow]; norm_num
      have e3 : CB * (1 / Real.exp 1 ^ 2) = 1 / Z := by rw [CB]; field_simp
      rw [e2, e3, le_div_iff₀ hZ, one_mul]; exact hZ1
    calc (1 : ℝ) ≤ CB * Real.exp (-2) := hCBexp
      _ ≤ CB * Real.exp (-(2 * κ)) := by gcongr; linarith
      _ = CB * 1 * Real.exp (-(2 * κ)) := by ring
      _ ≤ CB * (1 + κ) * Real.exp (-(2 * κ)) := by gcongr; linarith
  · -- κ ≥ 1: k = ⌊κ⌋ ≥ 1 and the k-fold integration by parts
    set k : ℕ := ⌊κ⌋₊ with hk
    have hkκ : (k : ℝ) ≤ κ := Nat.floor_le hκ0
    have hκk : κ < k + 1 := Nat.lt_floor_add_one κ
    have hspos : 0 < s := by
      rcases hs0.lt_or_eq with h | h
      · exact h
      · exfalso
        have : κ = 0 := by rw [hκ, ← h, Real.sqrt_zero, mul_zero]
        linarith
    have hκs : (72 / Real.exp 1) * κ ^ 2 = s / Real.exp 1 ^ 2 := by
      have hsq := Real.sq_sqrt (show (0 : ℝ) ≤ 72 * Real.exp 1 by positivity)
      have hss := Real.sq_sqrt hs0
      have hκ2 : κ ^ 2 = cB ^ 2 / 4 * s := by rw [hκ, mul_pow, div_pow, hss]; ring
      have hcB2 : cB ^ 2 = 4 / (72 * Real.exp 1) := by rw [cB, div_pow, hsq]; norm_num
      rw [hκ2, hcB2]; field_simp
    have h1 : ‖paperFT (fun v => (B v : ℂ)) z‖ * s ^ k
        ≤ Real.exp (|z.im| / 2) * (((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) / Z) := by
      refine le_trans ?_ (norm_paperFT_Bc_mul_le k z)
      gcongr
      exact Complex.abs_re_le_norm z
    have h2 := key_ineq hspos hκ0 hκs k hkκ hκk
    have h3 : ‖paperFT (fun v => (B v : ℂ)) z‖ * s ^ k
        ≤ Real.exp (|z.im| / 2) * (CB * (1 + κ) * Real.exp (-(2 * κ))) * s ^ k := by
      calc ‖paperFT (fun v => (B v : ℂ)) z‖ * s ^ k
          ≤ Real.exp (|z.im| / 2) * (((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) / Z) := h1
        _ ≤ Real.exp (|z.im| / 2) * (CB * (1 + κ) * Real.exp (-(2 * κ)) * s ^ k) := by gcongr
        _ = Real.exp (|z.im| / 2) * (CB * (1 + κ) * Real.exp (-(2 * κ))) * s ^ k := by ring
    exact le_of_mul_le_mul_right h3 (pow_pos hspos k)

/-- **Lemma G, (G1)**: for every real η, ‖B̂(η)‖ ≤ C_B (1 + (c_B/2)√|η|) e^{−c_B√|η|}. -/
theorem norm_paperFT_Bc_ofReal_le (η : ℝ) :
    ‖paperFT (fun v => (B v : ℂ)) η‖
      ≤ CB * (1 + cB / 2 * Real.sqrt |η|) * Real.exp (-(cB * Real.sqrt |η|)) := by
  have h := norm_paperFT_Bc_le (η : ℂ)
  rwa [Complex.ofReal_im, Complex.ofReal_re, abs_zero, zero_div, Real.exp_zero, one_mul] at h

/-- the one-variable inequality behind (G2): (1 + x/2)e^{−x} ≤ 4e^{−3/4}e^{−7x/8}, from e^t ≥ 1 + t at t = (x − 6)/8. -/
theorem G2_aux (x : ℝ) :
    (1 + x / 2) * Real.exp (-x) ≤ 4 * Real.exp (-3 / 4) * Real.exp (-(7 / 8 * x)) := by
  have h := Real.add_one_le_exp ((x - 6) / 8)
  have e : 4 * Real.exp (-3 / 4) * Real.exp (-(7 / 8 * x)) = 4 * Real.exp ((x - 6) / 8) * Real.exp (-x) := by
    rw [mul_assoc, mul_assoc, ← Real.exp_add, ← Real.exp_add]; congr 2; ring
  rw [e]
  exact mul_le_mul_of_nonneg_right (by linarith) (Real.exp_pos _).le

/-- **Lemma G, (G2)**: for every real η, ‖B̂(η)‖ ≤ 4e^{−3/4} C_B · e^{−(7/8)c_B√|η|}. -/
theorem norm_paperFT_Bc_ofReal_le' (η : ℝ) :
    ‖paperFT (fun v => (B v : ℂ)) η‖
      ≤ 4 * Real.exp (-3 / 4) * CB * Real.exp (-(7 / 8 * cB * Real.sqrt |η|)) := by
  refine (norm_paperFT_Bc_ofReal_le η).trans ?_
  have hCB := CB_pos
  have h := G2_aux (cB * Real.sqrt |η|)
  calc CB * (1 + cB / 2 * Real.sqrt |η|) * Real.exp (-(cB * Real.sqrt |η|))
      = CB * ((1 + cB * Real.sqrt |η| / 2) * Real.exp (-(cB * Real.sqrt |η|))) := by ring
    _ ≤ CB * (4 * Real.exp (-3 / 4) * Real.exp (-(7 / 8 * (cB * Real.sqrt |η|)))) := by gcongr
    _ = 4 * Real.exp (-3 / 4) * CB * Real.exp (-(7 / 8 * cB * Real.sqrt |η|)) := by
        rw [show 7 / 8 * (cB * Real.sqrt |η|) = 7 / 8 * cB * Real.sqrt |η| by ring]; ring

end Separation
end Zeta23
