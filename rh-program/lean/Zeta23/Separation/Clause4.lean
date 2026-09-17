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
Zeta23/Separation/Clause4.lean — clause 4 of Theorem M2 (the in-window on-line noise) of the separation note
(rh-program/results/c2-m2/separation-note.md §0.1, §5), the dress-rehearsal rung of M4 (iii) (contract
rh-program/results/c2-m2/followups/PRICING.md §1(b) candidate (iii); build record rh-program/results/c2-m4/BUILD-NOTES-iii.md).

WHAT IS PROVED, modulo WHAT.  For any set `carrier` of points of ℂ with multiplicities `mult`, locally finite in the
ordinate and satisfying the local count Σ_{ρ ∈ carrier, |Im ρ − x| ≤ 1} m_ρ ≤ C₁·log(3 + |x|) for every real x
(the class 𝒞(C₁) of the note), and for t ≥ 3, L ≥ 50, R ≥ 1, the in-window on-line noise
    N := Σ_{ρ ∈ carrier, Re ρ = 1/2, |Im ρ − t| ≤ R} m_ρ · ‖h_f(γ_ρ)‖²,   f = f_{t,L}(u) = i·(B_L)′(u)·e^{−itu},
satisfies 0 ≤ N ≤ 2·(87/10)·C₁·log(4 + t + R)/L² — MODULO the two DISPLAYED hypotheses
    H-b₁ : ∀ η, (|η|·‖B̂(η)‖)² ≤ 87/10        (the note's b₁ = sup|ηB̂|² ≤ 8.70, a computed constant),
    H-B‴ : ∫ ‖B‴‖ ≤ 64231/100                (the note's ‖B‴‖₁ = 642.301, a computed constant).
Label: "clause 4 is kernel-checked modulo H-b₁, H-B‴" — never "clause 4 is formalized".

The route is the note's (§5), step for step: (0.1) h_f(r) = (r − t)·B̂(L(r − t)) by one integration by parts
(`paperFT_deriv`) and the scaling B̂_L(z) = B̂(Lz) (`integral_comp_mul_left`); for a real point γ the term is
(γ − t)²·‖B̂(L(γ − t))‖², bounded by b₁/L² for every γ (H-b₁) and, when k ≤ |γ − t| with k ≥ 1, by ‖B‴‖₁²/(L⁶k⁴)
(three integrations by parts, `paperFT_iteratedDeriv` at k = 3, and H-B‴); the finite in-window set is partitioned by
the shell index k = ⌊|γ − t|⌋₊ (`Finset.sum_fiberwise_of_maps_to`), shell 0 holding at most C₁·log(3 + t) ≤ C₁·ℓ_R
points and shell k ≥ 1 at most 2C₁·ℓ_R (two windows of the class definition centered at t ± (k + 1/2)), and
Σ_{k ≥ 1} k⁻⁴ ≤ 2 closes: N ≤ C₁ℓ_R (b₁/L² + 4‖B‴‖₁²/L⁶) ≤ 2b₁C₁ℓ_R/L² for L ≥ 50 (the note's L₁ = 17.9 is not needed:
the cruder Σ k⁻⁴ ≤ 2 and L ≥ 50 leave room).  The tsum over the in-window subtype is a finite sum (`finite_window`).

Divergences from the note's text, recorded in formalization.yaml fidelity (p): the constants 8.70 and 642.31 are the
rationals 87/10 and 64231/100; the shell sum uses Σ k⁻⁴ ≤ 2 in place of 2ζ(4); the local count is stated as a finite
`∑ᶠ` with multiplicity over the closed window |Im ρ − x| ≤ 1 (the note's #{γ : |Re γ − x| ≤ 1}, Re γ_ρ = Im ρ).
-/
import Zeta23.Separation.LemmaG

namespace Zeta23
namespace Separation

open Complex MeasureTheory
open scoped ContDiff

noncomputable section

/-! ### §1 The test f_{t,L}, the two displayed hypotheses, and the identity (0.1) -/

/-- B_L(u) := B(u/L)/L (separation note §0.1). -/
def BL (L : ℝ) (u : ℝ) : ℝ := B (u / L) / L

/-- the test f_{t,L}(u) := i·(B_L)′(u)·e^{−itu} (separation note §0.1), with Mathlib's `deriv` of the real function B_L. -/
def ftest (t L : ℝ) (u : ℝ) : ℂ := Complex.I * ((deriv (BL L) u : ℝ) : ℂ) * Complex.exp (-(Complex.I * t * u))

/-- **H-b₁** (displayed): (|η|·‖B̂(η)‖)² ≤ 87/10 for every real η — the note's b₁ = sup_η |ηB̂(η)|² ≤ 8.70 (§5, §12.2). -/
def Hb1 : Prop := ∀ η : ℝ, (|η| * ‖paperFT (fun v => (B v : ℂ)) η‖) ^ 2 ≤ 87 / 10

/-- **H-B‴** (displayed): ∫ ‖B‴‖ ≤ 64231/100 — the note's ‖B‴‖₁ = 642.301 (§5). -/
def HB3 : Prop := ∫ u, ‖iteratedDeriv 3 (fun v => (B v : ℂ)) u‖ ≤ 64231 / 100

theorem BL_contDiff {L : ℝ} {n : ℕ∞} : ContDiff ℝ n (BL L) :=
  (B_contDiff.comp (contDiff_id.div_const L)).div_const L

theorem BL_eq_zero_of_le {L : ℝ} (hL : 0 < L) {u : ℝ} (h : L / 2 ≤ |u|) : BL L u = 0 := by
  unfold BL
  rw [B_eq_zero_of_half_le, zero_div]
  rw [abs_div, abs_of_pos hL, le_div_iff₀ hL]
  linarith

theorem BLc_contDiff {L : ℝ} : ContDiff ℝ ∞ (fun u => (BL L u : ℂ)) :=
  Complex.ofRealCLM.contDiff.comp (BL_contDiff (n := ⊤))

theorem BLc_support {L : ℝ} (hL : 0 < L) : ∀ u : ℝ, (fun u => (BL L u : ℂ)) u ≠ 0 → |u| ≤ L / 2 :=
  fun u hu => by
    by_contra h
    exact hu (by simp [BL_eq_zero_of_le hL (not_le.mp h).le])

theorem hasCompactSupport_BLc {L : ℝ} (hL : 0 < L) : HasCompactSupport (fun u => (BL L u : ℂ)) :=
  hasCompactSupport_of_support_subset_abs (BLc_support hL)

theorem hasDerivAt_BLc {L : ℝ} (u : ℝ) :
    HasDerivAt (fun u => (BL L u : ℂ)) ((deriv (BL L) u : ℝ) : ℂ) u :=
  ((BL_contDiff (n := 1)).differentiable (by norm_num) u).hasDerivAt.ofReal_comp

theorem deriv_BLc {L : ℝ} : deriv (fun u => (BL L u : ℂ)) = fun u => ((deriv (BL L) u : ℝ) : ℂ) :=
  funext fun u => (hasDerivAt_BLc u).deriv

/-- the scaling B̂_L(z) = B̂(Lz) (note §0.1), by the substitution u = Lv. -/
theorem paperFT_BLc {L : ℝ} (hL : 0 < L) (z : ℂ) :
    paperFT (fun u => (BL L u : ℂ)) z = paperFT (fun v => (B v : ℂ)) ((L : ℂ) * z) := by
  have hL0 : L ≠ 0 := hL.ne'
  have hLc : (L : ℂ) ≠ 0 := Complex.ofReal_ne_zero.mpr hL0
  let g : ℝ → ℂ := fun v => (B v : ℂ) * cexp (I * ((L : ℂ) * z) * v)
  have hpt : ∀ u : ℝ, (BL L u : ℂ) * cexp (I * z * u) = (L⁻¹ : ℝ) • g (L⁻¹ * u) := by
    intro u
    have e1 : ((L⁻¹ * u : ℝ) : ℂ) = (L : ℂ)⁻¹ * u := by push_cast; ring
    have e2 : I * ((L : ℂ) * z) * ((L : ℂ)⁻¹ * u) = I * z * u := by field_simp
    simp only [g, BL, div_eq_inv_mul, Complex.ofReal_mul, Complex.ofReal_inv, Complex.real_smul, e1, e2]
    ring
  have hcomp := Measure.integral_comp_mul_left g L⁻¹
  rw [inv_inv, abs_of_pos hL] at hcomp
  rw [paperFT_def, paperFT_def]
  simp_rw [hpt]
  rw [integral_smul, hcomp, smul_smul, inv_mul_cancel₀ hL0, one_smul]

/-- **(0.1)**: h_f(r) = (r − t)·B̂(L(r − t)) for f = f_{t,L} and every complex r (note §0.1). -/
theorem paperFT_ftest {t L : ℝ} (hL : 0 < L) (r : ℂ) :
    paperFT (ftest t L) r = (r - t) * paperFT (fun v => (B v : ℂ)) ((L : ℂ) * (r - t)) := by
  have hpt : ∀ u : ℝ, ftest t L u * cexp (I * r * u)
      = I * (deriv (fun u => (BL L u : ℂ)) u * cexp (I * (r - t) * u)) := by
    intro u
    rw [deriv_BLc]
    have e : cexp (-(I * t * u)) * cexp (I * r * u) = cexp (I * (r - t) * u) := by
      rw [← Complex.exp_add]; congr 1; ring
    simp only [ftest]
    calc I * ((deriv (BL L) u : ℝ) : ℂ) * cexp (-(I * t * u)) * cexp (I * r * u)
        = I * (((deriv (BL L) u : ℝ) : ℂ) * (cexp (-(I * t * u)) * cexp (I * r * u))) := by ring
      _ = _ := by rw [e]
  have hd : paperFT (deriv (fun u => (BL L u : ℂ))) (r - t)
      = -(I * (r - t)) * paperFT (fun u => (BL L u : ℂ)) (r - t) :=
    paperFT_deriv ((BLc_contDiff (L := L)).of_le (by exact_mod_cast le_top)) (hasCompactSupport_BLc hL) (r - t)
  rw [paperFT_def]
  simp_rw [hpt]
  rw [integral_const_mul, ← paperFT_def (deriv fun u => (BL L u : ℂ)) (r - t), hd, paperFT_BLc hL]
  linear_combination (-(r - t) * paperFT (fun v => (B v : ℂ)) ((L : ℂ) * (r - t))) * Complex.I_sq

/-- for a point on the line, γ_ρ = Im ρ is real. -/
theorem gammaOf_of_re_eq_half {ρ : ℂ} (h : ρ.re = 1 / 2) : gammaOf ρ = (ρ.im : ℂ) := by
  unfold gammaOf
  rw [div_eq_iff Complex.I_ne_zero]
  apply Complex.ext <;> simp [h]

/-! ### §2 The two pointwise term bounds -/

/-- three integrations by parts and H-B‴: |η|³·‖B̂(η)‖ ≤ ∫‖B‴‖ ≤ 64231/100. -/
theorem abs_cube_mul_norm_paperFT_Bc_le (hB3 : HB3) (η : ℝ) :
    |η| ^ 3 * ‖paperFT (fun v => (B v : ℂ)) η‖ ≤ 64231 / 100 := by
  have hint' : ∀ k : ℕ, Integrable (iteratedDeriv k (fun v => (B v : ℂ))) := fun k =>
    (Bc_contDiff.continuous_iteratedDeriv k (by exact_mod_cast le_top)).integrable_of_hasCompactSupport
      (hasCompactSupport_iteratedDeriv hasCompactSupport_Bc k)
  have hint : Integrable (iteratedDeriv 3 (fun v => (B v : ℂ))) := hint' 3
  have hsupp : ∀ u, iteratedDeriv 3 (fun v => (B v : ℂ)) u ≠ 0 → |u| ≤ 1 / 2 := fun u hu => by
    by_contra h
    exact hu (iteratedDeriv_Bc_eq_zero (not_le.mp h))
  have h := norm_paperFT_le hint hsupp (η : ℂ)
  rw [paperFT_iteratedDeriv Bc_contDiff hasCompactSupport_Bc (η : ℂ) 3, norm_mul, norm_pow, norm_neg,
    norm_mul, Complex.norm_I, one_mul, Complex.ofReal_im, abs_zero, zero_mul, Real.exp_zero, one_mul,
    Complex.norm_real, Real.norm_eq_abs] at h
  exact h.trans hB3

/-- the term of a real point, every shell: d²·‖B̂(Ld)‖² ≤ b₁/L² (H-b₁). -/
theorem term_le_b1 (hb1 : Hb1) {L : ℝ} (hL : 0 < L) (d : ℝ) :
    d ^ 2 * ‖paperFT (fun v => (B v : ℂ)) ((L * d : ℝ) : ℂ)‖ ^ 2 ≤ (87 / 10) / L ^ 2 := by
  have h := hb1 (L * d)
  rw [abs_mul, abs_of_pos hL] at h
  rw [le_div_iff₀ (by positivity)]
  have e : (L * |d| * ‖paperFT (fun v => (B v : ℂ)) ((L * d : ℝ) : ℂ)‖) ^ 2
      = d ^ 2 * ‖paperFT (fun v => (B v : ℂ)) ((L * d : ℝ) : ℂ)‖ ^ 2 * L ^ 2 := by
    rw [mul_pow, mul_pow, sq_abs]; ring
  rw [e] at h
  exact h

/-- the term of a real point in shell k ≥ 1 (k ≤ |d|): d²·‖B̂(Ld)‖² ≤ ‖B‴‖₁²/(L⁶k⁴) (H-B‴). -/
theorem term_le_B3 (hB3 : HB3) {L : ℝ} (hL : 0 < L) {d k : ℝ} (hk : 1 ≤ k) (hd : k ≤ |d|) :
    d ^ 2 * ‖paperFT (fun v => (B v : ℂ)) ((L * d : ℝ) : ℂ)‖ ^ 2 ≤ (64231 / 100) ^ 2 / (L ^ 6 * k ^ 4) := by
  have h := abs_cube_mul_norm_paperFT_Bc_le hB3 (L * d)
  set X := ‖paperFT (fun v => (B v : ℂ)) ((L * d : ℝ) : ℂ)‖ with hX
  have hX0 : 0 ≤ X := norm_nonneg _
  rw [abs_mul, abs_of_pos hL] at h
  have hk4 : k ^ 4 ≤ |d| ^ 4 := pow_le_pow_left₀ (by linarith) hd 4
  have h2 : (L ^ 3 * |d| ^ 3 * X) ^ 2 ≤ (64231 / 100) ^ 2 := by
    have : L ^ 3 * |d| ^ 3 * X = (L * |d|) ^ 3 * X := by ring
    rw [this]; exact pow_le_pow_left₀ (by positivity) h 2
  rw [le_div_iff₀ (by positivity)]
  calc d ^ 2 * X ^ 2 * (L ^ 6 * k ^ 4) ≤ d ^ 2 * X ^ 2 * (L ^ 6 * |d| ^ 4) := by gcongr
    _ = (L ^ 3 * |d| ^ 3 * X) ^ 2 := by rw [← sq_abs d]; ring
    _ ≤ _ := h2

/-! ### §3 The shell sum over the finite in-window set -/

/-- Σ_{k<K} (k+1)⁻⁴ ≤ 2 − 1/K for K ≥ 1 (telescoping through (k+1)⁻⁴ ≤ k⁻¹ − (k+1)⁻¹). -/
theorem sum_inv_pow_four_le : ∀ K : ℕ, 1 ≤ K →
    ∑ k ∈ Finset.range K, 1 / ((k : ℝ) + 1) ^ 4 ≤ 2 - 1 / (K : ℝ) := by
  intro K hK
  induction K, hK using Nat.le_induction with
  | base => norm_num
  | succ n hn ih =>
    rw [Finset.sum_range_succ]
    have hn' : (1 : ℝ) ≤ n := by exact_mod_cast hn
    have h1 : 1 / ((n : ℝ) + 1) ^ 4 ≤ 1 / (n : ℝ) - 1 / ((n : ℝ) + 1) := by
      rw [div_sub_div _ _ (by positivity) (by positivity), div_le_div_iff₀ (by positivity) (by positivity)]
      have h2 : ((n : ℝ) + 1) ^ 2 ≤ ((n : ℝ) + 1) ^ 4 := pow_le_pow_right₀ (by linarith) (by norm_num)
      nlinarith [h2]
    push_cast
    linarith

/-- Σ_{k<K} (k+1)⁻⁴ ≤ 2 for every K. -/
theorem sum_inv_pow_four_le' (K : ℕ) : ∑ k ∈ Finset.range K, 1 / ((k : ℝ) + 1) ^ 4 ≤ 2 := by
  rcases Nat.eq_zero_or_pos K with h | h
  · simp [h]
  · exact (sum_inv_pow_four_le K h).trans (by
      have : (0 : ℝ) < K := by exact_mod_cast h
      have : 0 < 1 / (K : ℝ) := by positivity
      linarith)

/-- the local count of 𝒞(C₁), applied to any finite family of points of the carrier inside a window |Im ρ − x| ≤ 1. -/
theorem window_count_le {C₁ : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (x : ℝ) (F : Finset ℂ) (hF : ∀ ρ ∈ F, ρ ∈ carrier ∧ |ρ.im - x| ≤ 1) :
    ((∑ ρ ∈ F, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|) := by
  have hWfin : (carrier ∩ {ρ | |ρ.im - x| ≤ 1}).Finite := (hfin (x - 2) (x + 1)).subset (by
    rintro ρ ⟨h1, h2⟩
    have := abs_le.mp (show |ρ.im - x| ≤ 1 from h2)
    exact ⟨h1, by linarith [this.1], by linarith [this.2]⟩)
  refine le_trans ?_ (hcount x)
  rw [finsum_mem_eq_finite_toFinset_sum _ hWfin]
  exact_mod_cast Finset.sum_le_sum_of_subset_of_nonneg
    (fun ρ hρ => hWfin.mem_toFinset.mpr (hF ρ hρ)) (fun _ _ _ => Nat.zero_le _)

/-- **The shell sum.**  For a term g bounded by m_ρ·a on every in-window on-line point and by m_ρ·b/k⁴
on the points with k ≤ |Im ρ − t| (k ≥ 1), the sum over the in-window on-line points is at most
C₁·log(4 + t + R)·(a + 4b): shell 0 holds ≤ C₁·log(3 + t) points, shell k ≥ 1 at most 2C₁·log(4 + t + R)
(two windows of the class definition centered at t ± (k + 1/2)), and Σ_{k≥1} k⁻⁴ ≤ 2. -/
theorem shell_sum_le {C₁ t R a b : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hC : 0 ≤ C₁) (ht : 0 ≤ t) (hR : 1 ≤ R) (ha : 0 ≤ a) (hb : 0 ≤ b) (g : ℂ → ℝ)
    (hA : ∀ ρ ∈ carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R}, g ρ ≤ mult ρ * a)
    (hB : ∀ ρ ∈ carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R}, ∀ k : ℕ, 1 ≤ k → (k : ℝ) ≤ |ρ.im - t| →
      g ρ ≤ mult ρ * (b / (k : ℝ) ^ 4)) :
    ∑' ρ : ↥(carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R}), g ρ
      ≤ C₁ * Real.log (4 + t + R) * (a + 4 * b) := by
  classical
  set S := carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R} with hS
  have hSfin : S.Finite := (hfin (t - R - 1) (t + R)).subset (by
    rintro ρ ⟨h1, _, h2⟩
    have := abs_le.mp (show |ρ.im - t| ≤ R from h2)
    exact ⟨h1, by linarith [this.1], by linarith [this.2]⟩)
  set F := hSfin.toFinset with hF
  have hmemF : ∀ ρ, ρ ∈ F ↔ ρ ∈ S := fun ρ => hSfin.mem_toFinset
  -- the tsum over the finite subtype is the finite sum
  have htsum : ∑' ρ : S, g ρ = ∑ ρ ∈ F, g ρ := by
    rw [tsum_subtype S g, tsum_eq_sum (s := F) ?_]
    · exact Finset.sum_congr rfl fun ρ hρ => Set.indicator_of_mem ((hmemF ρ).mp hρ) g
    · intro ρ hρ; exact Set.indicator_of_notMem (fun h => hρ ((hmemF ρ).mpr h)) g
  rw [htsum]
  -- ℓ_R and the window logs
  set ℓ := Real.log (4 + t + R) with hℓ
  have hℓ0 : 0 ≤ ℓ := Real.log_nonneg (by linarith)
  have hlog : ∀ x : ℝ, |x| ≤ 1 + t + R → C₁ * Real.log (3 + |x|) ≤ C₁ * ℓ := fun x hx =>
    mul_le_mul_of_nonneg_left (Real.log_le_log (by positivity) (by linarith)) hC
  -- the shell index and the per-shell weight
  let shell : ℂ → ℕ := fun ρ => ⌊|ρ.im - t|⌋₊
  let ψ : ℕ → ℝ := fun k => if k = 0 then a else b / (k : ℝ) ^ 4
  have hψ : ∀ ρ ∈ F, g ρ ≤ mult ρ * ψ (shell ρ) := by
    intro ρ hρ
    have hρS := (hmemF ρ).mp hρ
    by_cases h0 : shell ρ = 0
    · rw [show ψ (shell ρ) = a from by rw [h0]; exact if_pos rfl]
      exact hA ρ hρS
    · rw [show ψ (shell ρ) = b / (shell ρ : ℝ) ^ 4 from if_neg h0]
      exact hB ρ hρS (shell ρ) (Nat.one_le_iff_ne_zero.mpr h0) (Nat.floor_le (abs_nonneg _))
  set K := ⌊R⌋₊ with hK
  have hKR : (K : ℝ) ≤ R := Nat.floor_le (by linarith)
  have hmaps : ∀ ρ ∈ F, shell ρ ∈ Finset.range (K + 1) := by
    intro ρ hρ
    obtain ⟨_, _, h2⟩ := (hmemF ρ).mp hρ
    exact Finset.mem_range.mpr (Nat.lt_succ_of_le (Nat.floor_mono h2))
  -- the fiber counts
  have hfiber0 : ((∑ ρ ∈ F with shell ρ = 0, mult ρ : ℕ) : ℝ) ≤ C₁ * ℓ := by
    refine le_trans (window_count_le carrier mult hfin hcount t _ ?_)
      (hlog t (by rw [abs_of_nonneg ht]; linarith))
    intro ρ hρ
    obtain ⟨hρF, hρ0⟩ := Finset.mem_filter.mp hρ
    obtain ⟨h1, _, _⟩ := (hmemF ρ).mp hρF
    exact ⟨h1, (Nat.floor_eq_zero.mp hρ0).le⟩
  have hfiberk : ∀ k : ℕ, 1 ≤ k → k ≤ K →
      ((∑ ρ ∈ F with shell ρ = k, mult ρ : ℕ) : ℝ) ≤ 2 * (C₁ * ℓ) := by
    intro k hk1 hkK
    have hkR : (k : ℝ) ≤ R := le_trans (by exact_mod_cast hkK) hKR
    have hk1' : (1 : ℝ) ≤ k := by exact_mod_cast hk1
    set Fp := F.filter (fun ρ => |ρ.im - (t + ((k : ℝ) + 1 / 2))| ≤ 1) with hFp
    set Fm := F.filter (fun ρ => |ρ.im - (t - ((k : ℝ) + 1 / 2))| ≤ 1) with hFm
    have hsub : F.filter (fun ρ => shell ρ = k) ⊆ Fp ∪ Fm := by
      intro ρ hρ
      obtain ⟨hρF, hρk⟩ := Finset.mem_filter.mp hρ
      have hlo : ((shell ρ : ℕ) : ℝ) ≤ |ρ.im - t| := Nat.floor_le (abs_nonneg _)
      have hhi : |ρ.im - t| < ((shell ρ : ℕ) : ℝ) + 1 := Nat.lt_floor_add_one _
      rw [hρk] at hlo hhi
      rw [Finset.mem_union, hFp, hFm, Finset.mem_filter, Finset.mem_filter]
      rcases le_or_gt 0 (ρ.im - t) with hs | hs
      · left
        rw [abs_of_nonneg hs] at hlo hhi
        exact ⟨hρF, abs_le.mpr ⟨by linarith, by linarith⟩⟩
      · right
        rw [abs_of_neg hs] at hlo hhi
        exact ⟨hρF, abs_le.mpr ⟨by linarith, by linarith⟩⟩
    have hp : ((∑ ρ ∈ Fp, mult ρ : ℕ) : ℝ) ≤ C₁ * ℓ := by
      refine le_trans (window_count_le carrier mult hfin hcount (t + ((k : ℝ) + 1 / 2)) _ ?_)
        (hlog (t + ((k : ℝ) + 1 / 2)) ?_)
      · intro ρ hρ
        obtain ⟨hρF, h⟩ := Finset.mem_filter.mp hρ
        exact ⟨((hmemF ρ).mp hρF).1, h⟩
      · rw [abs_of_nonneg (by linarith)]; linarith
    have hm : ((∑ ρ ∈ Fm, mult ρ : ℕ) : ℝ) ≤ C₁ * ℓ := by
      refine le_trans (window_count_le carrier mult hfin hcount (t - ((k : ℝ) + 1 / 2)) _ ?_)
        (hlog (t - ((k : ℝ) + 1 / 2)) ?_)
      · intro ρ hρ
        obtain ⟨hρF, h⟩ := Finset.mem_filter.mp hρ
        exact ⟨((hmemF ρ).mp hρF).1, h⟩
      · exact abs_le.mpr ⟨by linarith, by linarith⟩
    have hunion : (∑ ρ ∈ F.filter (fun ρ => shell ρ = k), mult ρ)
        ≤ (∑ ρ ∈ Fp, mult ρ) + ∑ ρ ∈ Fm, mult ρ := by
      have h1 : (∑ ρ ∈ F.filter (fun ρ => shell ρ = k), mult ρ) ≤ ∑ ρ ∈ Fp ∪ Fm, mult ρ :=
        Finset.sum_le_sum_of_subset hsub
      have h2 := Finset.sum_union_inter (s₁ := Fp) (s₂ := Fm) (f := mult)
      omega
    calc ((∑ ρ ∈ F with shell ρ = k, mult ρ : ℕ) : ℝ)
        ≤ ((∑ ρ ∈ Fp, mult ρ : ℕ) : ℝ) + ((∑ ρ ∈ Fm, mult ρ : ℕ) : ℝ) := by exact_mod_cast hunion
      _ ≤ C₁ * ℓ + C₁ * ℓ := add_le_add hp hm
      _ = 2 * (C₁ * ℓ) := by ring
  -- assemble
  calc ∑ ρ ∈ F, g ρ ≤ ∑ ρ ∈ F, (mult ρ : ℝ) * ψ (shell ρ) := Finset.sum_le_sum hψ
    _ = ∑ k ∈ Finset.range (K + 1), ∑ ρ ∈ F with shell ρ = k, (mult ρ : ℝ) * ψ (shell ρ) :=
        (Finset.sum_fiberwise_of_maps_to hmaps _).symm
    _ = ∑ k ∈ Finset.range (K + 1), ψ k * ((∑ ρ ∈ F with shell ρ = k, mult ρ : ℕ) : ℝ) := by
        refine Finset.sum_congr rfl fun k _ => ?_
        rw [Nat.cast_sum, Finset.mul_sum]
        refine Finset.sum_congr rfl fun ρ hρ => ?_
        rw [(Finset.mem_filter.mp hρ).2]; ring
    _ ≤ ∑ k ∈ Finset.range K, ψ (k + 1) * (2 * (C₁ * ℓ)) + ψ 0 * (C₁ * ℓ) := by
        rw [Finset.sum_range_succ']
        refine add_le_add (Finset.sum_le_sum fun k hk => ?_) (mul_le_mul_of_nonneg_left hfiber0 ?_)
        · have hk := Finset.mem_range.mp hk
          refine mul_le_mul_of_nonneg_left (hfiberk (k + 1) (by omega) (by omega)) ?_
          rw [show ψ (k + 1) = b / ((k + 1 : ℕ) : ℝ) ^ 4 from if_neg (Nat.succ_ne_zero k)]
          positivity
        · rw [show ψ 0 = a from if_pos rfl]; exact ha
    _ = 2 * (C₁ * ℓ) * b * (∑ k ∈ Finset.range K, 1 / ((k : ℝ) + 1) ^ 4) + a * (C₁ * ℓ) := by
        rw [Finset.mul_sum, show ψ 0 = a from if_pos rfl]
        congr 1
        refine Finset.sum_congr rfl fun k _ => ?_
        rw [show ψ (k + 1) = b / ((k + 1 : ℕ) : ℝ) ^ 4 from if_neg (Nat.succ_ne_zero k)]
        push_cast; ring
    _ ≤ 2 * (C₁ * ℓ) * b * 2 + a * (C₁ * ℓ) := by
        gcongr
        exact sum_inv_pow_four_le' K
    _ = C₁ * ℓ * (a + 4 * b) := by ring

/-! ### §4 Clause 4 -/

/-- **Theorem M2, clause 4** (separation note §5), library form: for any carrier with multiplicities, locally finite in
the ordinate and satisfying the local count of 𝒞(C₁), and t ≥ 3, L ≥ 50, R ≥ 1: the in-window on-line noise
N = Σ_{ρ ∈ carrier, Re ρ = 1/2, |Im ρ − t| ≤ R} m_ρ‖h_f(γ_ρ)‖² satisfies 0 ≤ N ≤ 2·(87/10)·C₁·log(4 + t + R)/L² —
modulo the displayed H-b₁ and H-B‴. -/
theorem inWindowNoise_le {C₁ t L R : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hL : 50 ≤ L) (hR : 1 ≤ R) (hb1 : Hb1) (hB3 : HB3) :
    0 ≤ ∑' ρ : ↥(carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R}),
        (mult ρ : ℝ) * ‖paperFT (ftest t L) (gammaOf ρ)‖ ^ 2 ∧
      ∑' ρ : ↥(carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R}),
        (mult ρ : ℝ) * ‖paperFT (ftest t L) (gammaOf ρ)‖ ^ 2
      ≤ 2 * (87 / 10) * C₁ * Real.log (4 + t + R) / L ^ 2 := by
  have hL0 : 0 < L := by linarith
  have hLne : L ≠ 0 := hL0.ne'
  refine ⟨tsum_nonneg fun ρ => by positivity, ?_⟩
  -- the term of an on-line point, by (0.1)
  have hterm : ∀ ρ : ℂ, ρ.re = 1 / 2 →
      ‖paperFT (ftest t L) (gammaOf ρ)‖ ^ 2
        = (ρ.im - t) ^ 2 * ‖paperFT (fun v => (B v : ℂ)) ((L * (ρ.im - t) : ℝ) : ℂ)‖ ^ 2 := by
    intro ρ hρ
    rw [gammaOf_of_re_eq_half hρ, paperFT_ftest hL0, norm_mul, mul_pow,
      show ((L : ℂ) * ((ρ.im : ℂ) - (t : ℂ))) = ((L * (ρ.im - t) : ℝ) : ℂ) by push_cast; ring,
      ← Complex.ofReal_sub, Complex.norm_real, Real.norm_eq_abs, sq_abs]
  have key := shell_sum_le (t := t) (R := R) (a := (87 / 10) / L ^ 2) (b := (64231 / 100) ^ 2 / L ^ 6)
    carrier mult hfin hcount
    (by linarith) (by linarith) hR (by positivity) (by positivity)
    (fun ρ => (mult ρ : ℝ) * ‖paperFT (ftest t L) (gammaOf ρ)‖ ^ 2)
    (fun ρ hρ => by
      rw [hterm ρ hρ.2.1]
      exact mul_le_mul_of_nonneg_left (term_le_b1 hb1 hL0 _) (Nat.cast_nonneg _))
    (fun ρ hρ k hk hkd => by
      rw [hterm ρ hρ.2.1, div_div]
      exact mul_le_mul_of_nonneg_left (term_le_B3 hB3 hL0 (by exact_mod_cast hk) hkd) (Nat.cast_nonneg _))
  refine key.trans ?_
  have hℓ0 : 0 ≤ Real.log (4 + t + R) := Real.log_nonneg (by linarith)
  have hC0 : 0 ≤ C₁ := by linarith
  have hL4 : (50 : ℝ) ^ 4 ≤ L ^ 4 := pow_le_pow_left₀ (by norm_num) hL 4
  have hb : 4 * ((64231 / 100 : ℝ) ^ 2 / L ^ 6) ≤ (87 / 10) / L ^ 2 := by
    have e : 4 * ((64231 / 100 : ℝ) ^ 2 / L ^ 6) = (4 * (64231 / 100) ^ 2 / L ^ 4) / L ^ 2 := by
      field_simp
    rw [e]
    refine div_le_div_of_nonneg_right ?_ (by positivity)
    rw [div_le_iff₀ (by positivity)]
    nlinarith [hL4]
  calc C₁ * Real.log (4 + t + R) * ((87 / 10) / L ^ 2 + 4 * ((64231 / 100) ^ 2 / L ^ 6))
      ≤ C₁ * Real.log (4 + t + R) * ((87 / 10) / L ^ 2 + (87 / 10) / L ^ 2) := by gcongr
    _ = 2 * (87 / 10) * C₁ * Real.log (4 + t + R) / L ^ 2 := by ring

end

end Separation
end Zeta23
