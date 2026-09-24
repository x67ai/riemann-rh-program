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
Zeta23/Separation/Clause5.lean — clause 5 of Theorem M2 (the out-window contamination, uniform over the depth
|Im γ| ≤ 1/2) of the separation note (rh-program/results/c2-m2/separation-note.md §6 and addendum A3, R₀ = 73 with
the L-hypothesis spent once), Unit B of the M4 residue (contract rh-program/results/c2-m4/PRICING-RESIDUE.md §1
Piece 1; build record rh-program/results/c2-m4/BUILD-NOTES-B.md).

WHAT IS PROVED, modulo WHAT.  For any set `carrier` of points of ℂ with multiplicities `mult`, locally finite in
the ordinate, inside the closed strip 0 ≤ Re ρ ≤ 1, and satisfying the local count Σ_{ρ ∈ carrier, |Im ρ − x| ≤ 1}
m_ρ ≤ C₁·log(3 + |x|) for every real x (the class 𝒞(C₁) of the note):
  §1–§3 (the rung): for t ≥ 3 and L > 0 the out-window sum Σ_{|Im ρ − t| > 73L} ‖m_ρ h_f(γ_ρ) conj(h_f(conj γ_ρ))‖,
        f = f_{t,L}, is summable (`clause5_summable`) — no numerics, no displayed hypothesis;
  §4–§9 (clause 5 modulo H-R₀): for t ≥ 3, L ≥ 50, 8·(log log(3 + t) + log(2b₁C₁)) ≤ L and the one-point check
        H-R₀ (F₁₃(50) ≤ 0 with 5/(2c_B√73 − 13/8) ≤ 50, `HR0`), the same sum is summable and its norm is ≤ e^{−L}
        (`clause5_out_window`) — exactly the two conjuncts of the trusted `Hout` at R = 73L.
Label: "clause 5 is kernel-checked modulo H-R₀" — never "clause 5 is formalized".

The route is the note's, step for step.  (a) The pointwise bound: for ρ = x + iy in the strip, γ_ρ = x′ + iy′ with
x′ = Im ρ, y′ = 1/2 − Re ρ, |y′| ≤ 1/2, and h_f(γ) = (γ − t)B̂(L(γ − t)) (`paperFT_ftest`), so by Lemma G's complex
form (`norm_paperFT_Bc_le`) ‖h_f(γ_ρ)‖ ≤ (u + 1/2)e^{L/4}G(Lu), u := |Im ρ − t|, and the same at conj γ_ρ;
multiplied, ‖m_ρ h_f(γ_ρ)conj(h_f(conj γ_ρ))‖ ≤ m_ρ(u + 1/2)²e^{L/2}G(Lu)² (`norm_wsum_le_strip`) — the depth enters
only through e^{L|y′|/2} ≤ e^{L/4}, which is the uniformity over the depth.  (b) The shell device on the INFINITE
out-window set: every finite sub-family F is fibered by the shell index k = ⌊|Im ρ − t|⌋₊ ≥ ⌊73L⌋₊
(`Finset.sum_fiberwise_of_maps_to`), shell k holds at most 2C₁·log(7/2 + t + k) points (two windows of the class
definition centered at t ± (k + 1/2), `window_count_le`), and a uniform bound c on the shell series over every
initial segment gives Σ_F ≤ c (`out_finset_sum_le`); summability then follows from `summable_of_sum_le`, the
tsum bound from `Summable.tsum_le_of_sum_le`, and the norm of the sum from `norm_tsum_le_tsum_norm`
(`out_window_norm_le`).  (c) The rung's crude majorant: (u + 1)⁷G(Lu)² ≤ M_L (from (1 + w)e^{−w/8} ≤ 8), so the
shell weight is e^{L/2}M_L/(k + 1)⁵ and Σ_k log(7/2 + t + k)/(k + 1)⁵ ≤ (9/2 + t)·Σ(k + 1)⁻⁴ ≤ 2(9/2 + t)
(`sum_inv_pow_four_le'` of Clause4.lean).  (d) The tail bound (§4–§9) is documented at its sections.

Divergences from the note's text, recorded in formalization.yaml fidelity (r): (r3) the `strip` field of `SepConfig`
is consumed here for the first time (the pointwise bound); (r4) the out-window shell index starts at ⌊73L⌋₊ ≥ 73L − 1
(the note's u₀ := R − 1) and every shell, including shell 0, is counted by the two windows at t ± (k + 1/2).
-/
import Mathlib.Analysis.SumIntegralComparisons
import Zeta23.Separation.Assembly2

namespace Zeta23
namespace Separation

open Complex MeasureTheory
open scoped ContDiff

noncomputable section

/-! ### §1 The pointwise bound (note §6 (a)) -/

/-- G is antitone (in x ≤ y; √ is monotone on ℝ): for 0 ≤ w₁ ≤ w₂, (1 + w₂/2)e^{−w₂} ≤ (1 + w₁/2)e^{−w₁}, because
1 + w₂/2 ≤ (1 + w₁/2)(1 + (w₂ − w₁)) ≤ (1 + w₁/2)e^{w₂ − w₁}. -/
theorem Gmaj_antitone {x y : ℝ} (hxy : x ≤ y) : Gmaj y ≤ Gmaj x := by
  have hCB := CB_pos
  have hcB := cB_pos
  have hsx : 0 ≤ Real.sqrt x := Real.sqrt_nonneg x
  have hsxy : Real.sqrt x ≤ Real.sqrt y := Real.sqrt_le_sqrt hxy
  set w₁ := cB * Real.sqrt x with hw₁
  set w₂ := cB * Real.sqrt y with hw₂
  have hw₁0 : 0 ≤ w₁ := by positivity
  have hle : w₁ ≤ w₂ := by rw [hw₁, hw₂]; exact mul_le_mul_of_nonneg_left hsxy hcB.le
  have h1 : 1 + w₂ / 2 ≤ (1 + w₁ / 2) * Real.exp (w₂ - w₁) := by
    have he := Real.add_one_le_exp (w₂ - w₁)
    have : 1 + w₂ / 2 ≤ (1 + w₁ / 2) * (w₂ - w₁ + 1) := by nlinarith
    calc 1 + w₂ / 2 ≤ (1 + w₁ / 2) * (w₂ - w₁ + 1) := this
      _ ≤ (1 + w₁ / 2) * Real.exp (w₂ - w₁) := by gcongr
  have he2 : Real.exp (-w₂) * Real.exp (w₂ - w₁) = Real.exp (-w₁) := by
    rw [← Real.exp_add]; ring_nf
  have e1 : Gmaj y = CB * (1 + w₂ / 2) * Real.exp (-w₂) := by rw [Gmaj, hw₂]; ring
  have e2 : Gmaj x = CB * (1 + w₁ / 2) * Real.exp (-w₁) := by rw [Gmaj, hw₁]; ring
  rw [e1, e2]
  calc CB * (1 + w₂ / 2) * Real.exp (-w₂)
      ≤ CB * ((1 + w₁ / 2) * Real.exp (w₂ - w₁)) * Real.exp (-w₂) := by gcongr
    _ = CB * (1 + w₁ / 2) * (Real.exp (-w₂) * Real.exp (w₂ - w₁)) := by ring
    _ = CB * (1 + w₁ / 2) * Real.exp (-w₁) := by rw [he2]

/-- h_f at a point x + iy with |y| ≤ 1/2: ‖h_f(x + iy)‖ ≤ (|x − t| + 1/2)·e^{L/4}·G(L|x − t|) — (0.1) and Lemma G's
complex form; the depth y enters only through e^{L|y|/2} ≤ e^{L/4}. -/
theorem norm_paperFT_ftest_le_strip {t L : ℝ} (hL : 0 < L) (x y : ℝ) (hy : |y| ≤ 1 / 2) :
    ‖paperFT (ftest t L) ((x : ℂ) + (y : ℂ) * I)‖
      ≤ (|x - t| + 1 / 2) * Real.exp (L / 4) * Gmaj (L * |x - t|) := by
  rw [paperFT_ftest hL, norm_mul]
  have hre : ((x : ℂ) + (y : ℂ) * I - t).re = x - t := by simp
  have him : ((x : ℂ) + (y : ℂ) * I - t).im = y := by simp
  have h1 : ‖(x : ℂ) + (y : ℂ) * I - t‖ ≤ |x - t| + 1 / 2 := by
    refine (Complex.norm_le_abs_re_add_abs_im _).trans ?_
    rw [hre, him]; linarith
  have h2 : ‖paperFT (fun v => (B v : ℂ)) ((L : ℂ) * ((x : ℂ) + (y : ℂ) * I - t))‖
      ≤ Real.exp (L / 4) * Gmaj (L * |x - t|) := by
    have h := norm_paperFT_Bc_le ((L : ℂ) * ((x : ℂ) + (y : ℂ) * I - t))
    have hre' : ((L : ℂ) * ((x : ℂ) + (y : ℂ) * I - t)).re = L * (x - t) := by
      rw [Complex.mul_re, hre, him]; simp
    have him' : ((L : ℂ) * ((x : ℂ) + (y : ℂ) * I - t)).im = L * y := by
      rw [Complex.mul_im, hre, him]; simp
    rw [hre', him', abs_mul, abs_mul, abs_of_pos hL] at h
    refine h.trans ?_
    rw [Gmaj]
    have hG : 0 ≤ CB * (1 + cB / 2 * Real.sqrt (L * |x - t|)) * Real.exp (-(cB * Real.sqrt (L * |x - t|))) := by
      have := CB_pos; have := cB_pos; positivity
    refine mul_le_mul_of_nonneg_right (Real.exp_le_exp.mpr ?_) hG
    nlinarith [abs_nonneg y]
  have hG := Gmaj_nonneg (L * |x - t|)
  calc ‖(x : ℂ) + (y : ℂ) * I - t‖ * ‖paperFT (fun v => (B v : ℂ)) ((L : ℂ) * ((x : ℂ) + (y : ℂ) * I - t))‖
      ≤ (|x - t| + 1 / 2) * (Real.exp (L / 4) * Gmaj (L * |x - t|)) :=
        mul_le_mul h1 h2 (norm_nonneg _) (by positivity)
    _ = _ := by ring

/-- **clause 5 (a), the pointwise bound** (note §6 (a)): for ρ in the strip 0 ≤ Re ρ ≤ 1 and u := |Im ρ − t|,
‖m_ρ h_f(γ_ρ) conj(h_f(conj γ_ρ))‖ ≤ m_ρ·(u + 1/2)²·e^{L/2}·G(Lu)² — uniform over the depth |Im γ_ρ| = |Re ρ − 1/2|
≤ 1/2 (this is where the `strip` field of `SepConfig` is consumed). -/
theorem norm_wsum_le_strip {mult : ℂ → ℕ} {t L : ℝ} (hL : 0 < L) {ρ : ℂ} (hρ : 0 ≤ ρ.re ∧ ρ.re ≤ 1) :
    ‖wsum mult (ftest t L) ρ‖
      ≤ (mult ρ : ℝ) * ((|ρ.im - t| + 1 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * |ρ.im - t|) ^ 2) := by
  have hg : gammaOf ρ = (ρ.im : ℂ) + ((1 / 2 - ρ.re : ℝ) : ℂ) * I := by
    have := gammaOf_mk ρ.re ρ.im
    rw [Complex.eta] at this
    rw [this]; push_cast; ring
  have hconj : (starRingEnd ℂ) (gammaOf ρ) = (ρ.im : ℂ) + ((-(1 / 2 - ρ.re) : ℝ) : ℂ) * I := by
    rw [hg]; simp only [map_add, map_mul, Complex.conj_ofReal, Complex.conj_I]; push_cast; ring
  have hy : |1 / 2 - ρ.re| ≤ 1 / 2 := abs_le.mpr ⟨by linarith [hρ.1], by linarith [hρ.2]⟩
  have hy' : |-(1 / 2 - ρ.re)| ≤ 1 / 2 := by rw [abs_neg]; exact hy
  have h1 := norm_paperFT_ftest_le_strip (t := t) hL ρ.im (1 / 2 - ρ.re) hy
  have h2 := norm_paperFT_ftest_le_strip (t := t) hL ρ.im (-(1 / 2 - ρ.re)) hy'
  have hG := Gmaj_nonneg (L * |ρ.im - t|)
  have hex : Real.exp (L / 4) * Real.exp (L / 4) = Real.exp (L / 2) := by rw [← Real.exp_add]; ring_nf
  rw [wsum, norm_mul, norm_mul, Complex.norm_conj, Complex.norm_natCast, hconj, hg]
  calc (mult ρ : ℝ) * ‖paperFT (ftest t L) ((ρ.im : ℂ) + ((1 / 2 - ρ.re : ℝ) : ℂ) * I)‖
        * ‖paperFT (ftest t L) ((ρ.im : ℂ) + ((-(1 / 2 - ρ.re) : ℝ) : ℂ) * I)‖
      ≤ (mult ρ : ℝ) * ((|ρ.im - t| + 1 / 2) * Real.exp (L / 4) * Gmaj (L * |ρ.im - t|))
        * ((|ρ.im - t| + 1 / 2) * Real.exp (L / 4) * Gmaj (L * |ρ.im - t|)) := by
        gcongr
    _ = (mult ρ : ℝ) * ((|ρ.im - t| + 1 / 2) ^ 2 * (Real.exp (L / 4) * Real.exp (L / 4))
        * Gmaj (L * |ρ.im - t|) ^ 2) := by ring
    _ = _ := by rw [hex]

/-! ### §2 The shell device on the out-window set (an infinite set: every finite sub-family) -/

/-- shell k of the carrier (⌊|Im ρ − t|⌋₊ = k) holds at most 2C₁·log(7/2 + t + k) points: the shell lies in the two
windows |Im ρ − (t ± (k + 1/2))| ≤ 1 of the class definition, and 3 + |t ± (k + 1/2)| ≤ 7/2 + t + k. -/
theorem shell_count_le {C₁ t : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hC : 0 ≤ C₁) (ht : 0 ≤ t) (k : ℕ) (F : Finset ℂ)
    (hF : ∀ ρ ∈ F, ρ ∈ carrier ∧ ⌊|ρ.im - t|⌋₊ = k) :
    ((∑ ρ ∈ F, mult ρ : ℕ) : ℝ) ≤ 2 * C₁ * Real.log (7 / 2 + t + k) := by
  classical
  have hk0 : (0 : ℝ) ≤ k := Nat.cast_nonneg k
  set Fp := F.filter (fun ρ => |ρ.im - (t + ((k : ℝ) + 1 / 2))| ≤ 1) with hFp
  set Fm := F.filter (fun ρ => |ρ.im - (t - ((k : ℝ) + 1 / 2))| ≤ 1) with hFm
  have hsub : F ⊆ Fp ∪ Fm := by
    intro ρ hρ
    obtain ⟨_, hρk⟩ := hF ρ hρ
    have hlo : ((⌊|ρ.im - t|⌋₊ : ℕ) : ℝ) ≤ |ρ.im - t| := Nat.floor_le (abs_nonneg _)
    have hhi : |ρ.im - t| < ((⌊|ρ.im - t|⌋₊ : ℕ) : ℝ) + 1 := Nat.lt_floor_add_one _
    rw [hρk] at hlo hhi
    rw [Finset.mem_union, hFp, hFm, Finset.mem_filter, Finset.mem_filter]
    rcases le_or_gt 0 (ρ.im - t) with hs | hs
    · left
      rw [abs_of_nonneg hs] at hlo hhi
      exact ⟨hρ, abs_le.mpr ⟨by linarith, by linarith⟩⟩
    · right
      rw [abs_of_neg hs] at hlo hhi
      exact ⟨hρ, abs_le.mpr ⟨by linarith, by linarith⟩⟩
  have hℓ : ∀ x : ℝ, |x| ≤ t + k + 1 / 2 → C₁ * Real.log (3 + |x|) ≤ C₁ * Real.log (7 / 2 + t + k) :=
    fun x hx => mul_le_mul_of_nonneg_left (Real.log_le_log (by positivity) (by linarith)) hC
  have hp : ((∑ ρ ∈ Fp, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (7 / 2 + t + k) := by
    refine le_trans (window_count_le carrier mult hfin hcount (t + ((k : ℝ) + 1 / 2)) _ ?_) (hℓ _ ?_)
    · intro ρ hρ
      obtain ⟨hρF, h⟩ := Finset.mem_filter.mp hρ
      exact ⟨(hF ρ hρF).1, h⟩
    · rw [abs_of_nonneg (by positivity)]; linarith
  have hm : ((∑ ρ ∈ Fm, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (7 / 2 + t + k) := by
    refine le_trans (window_count_le carrier mult hfin hcount (t - ((k : ℝ) + 1 / 2)) _ ?_) (hℓ _ ?_)
    · intro ρ hρ
      obtain ⟨hρF, h⟩ := Finset.mem_filter.mp hρ
      exact ⟨(hF ρ hρF).1, h⟩
    · exact abs_le.mpr ⟨by linarith, by linarith⟩
  have hunion : (∑ ρ ∈ F, mult ρ) ≤ (∑ ρ ∈ Fp, mult ρ) + ∑ ρ ∈ Fm, mult ρ := by
    have h1 : (∑ ρ ∈ F, mult ρ) ≤ ∑ ρ ∈ Fp ∪ Fm, mult ρ := Finset.sum_le_sum_of_subset hsub
    have h2 := Finset.sum_union_inter (s₁ := Fp) (s₂ := Fm) (f := mult)
    omega
  calc ((∑ ρ ∈ F, mult ρ : ℕ) : ℝ)
      ≤ ((∑ ρ ∈ Fp, mult ρ : ℕ) : ℝ) + ((∑ ρ ∈ Fm, mult ρ : ℕ) : ℝ) := by exact_mod_cast hunion
    _ ≤ C₁ * Real.log (7 / 2 + t + k) + C₁ * Real.log (7 / 2 + t + k) := add_le_add hp hm
    _ = 2 * C₁ * Real.log (7 / 2 + t + k) := by ring

/-- **the shell device on the out-window set.**  For a term g bounded by m_ρ·ψ(k) on the points of shell k
(k = ⌊|Im ρ − t|⌋₊ ≥ ⌊R⌋₊ beyond the window), and a bound c on the shell series Σ_{⌊R⌋₊ ≤ k < K} 2C₁·log(7/2 + t + k)·ψ(k)
uniform in K, every finite family F of points of the carrier beyond R has Σ_F g ≤ c. -/
theorem out_finset_sum_le {C₁ t R : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hC : 0 ≤ C₁) (ht : 0 ≤ t) (g : ℂ → ℝ) (ψ : ℕ → ℝ) (hψ : ∀ k, 0 ≤ ψ k)
    (hg : ∀ ρ ∈ carrier ∩ {ρ | R < |ρ.im - t|}, g ρ ≤ mult ρ * ψ ⌊|ρ.im - t|⌋₊)
    (c : ℝ) (hc : ∀ K : ℕ, ∑ k ∈ Finset.Ico ⌊R⌋₊ K, 2 * C₁ * Real.log (7 / 2 + t + k) * ψ k ≤ c)
    (F : Finset ℂ) (hF : ∀ ρ ∈ F, ρ ∈ carrier ∩ {ρ | R < |ρ.im - t|}) :
    ∑ ρ ∈ F, g ρ ≤ c := by
  classical
  let shell : ℂ → ℕ := fun ρ => ⌊|ρ.im - t|⌋₊
  set K := F.sup shell + 1 with hK
  have hmaps : ∀ ρ ∈ F, shell ρ ∈ Finset.Ico ⌊R⌋₊ K := by
    intro ρ hρ
    obtain ⟨_, hρR⟩ := hF ρ hρ
    refine Finset.mem_Ico.mpr ⟨Nat.floor_mono (le_of_lt hρR), ?_⟩
    exact Nat.lt_succ_of_le (Finset.le_sup (f := shell) hρ)
  calc ∑ ρ ∈ F, g ρ ≤ ∑ ρ ∈ F, (mult ρ : ℝ) * ψ (shell ρ) := Finset.sum_le_sum fun ρ hρ => hg ρ (hF ρ hρ)
    _ = ∑ k ∈ Finset.Ico ⌊R⌋₊ K, ∑ ρ ∈ F with shell ρ = k, (mult ρ : ℝ) * ψ (shell ρ) :=
        (Finset.sum_fiberwise_of_maps_to hmaps _).symm
    _ = ∑ k ∈ Finset.Ico ⌊R⌋₊ K, ψ k * ((∑ ρ ∈ F with shell ρ = k, mult ρ : ℕ) : ℝ) := by
        refine Finset.sum_congr rfl fun k _ => ?_
        rw [Nat.cast_sum, Finset.mul_sum]
        refine Finset.sum_congr rfl fun ρ hρ => ?_
        rw [(Finset.mem_filter.mp hρ).2]; ring
    _ ≤ ∑ k ∈ Finset.Ico ⌊R⌋₊ K, ψ k * (2 * C₁ * Real.log (7 / 2 + t + k)) := by
        refine Finset.sum_le_sum fun k _ => mul_le_mul_of_nonneg_left ?_ (hψ k)
        refine shell_count_le carrier mult hfin hcount hC ht k _ fun ρ hρ => ?_
        obtain ⟨hρF, hρk⟩ := Finset.mem_filter.mp hρ
        exact ⟨(hF ρ hρF).1, hρk⟩
    _ = ∑ k ∈ Finset.Ico ⌊R⌋₊ K, 2 * C₁ * Real.log (7 / 2 + t + k) * ψ k := by
        refine Finset.sum_congr rfl fun k _ => ?_; ring
    _ ≤ c := hc K

/-- the out-window sum of a nonnegative term is summable, and its tsum is ≤ c, under the shell-device hypotheses
(`summable_of_sum_le`, `Summable.tsum_le_of_sum_le`). -/
theorem out_window_summable_tsum_le {C₁ t R : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hC : 0 ≤ C₁) (ht : 0 ≤ t) (g : ℂ → ℝ) (hg0 : ∀ ρ, 0 ≤ g ρ) (ψ : ℕ → ℝ) (hψ : ∀ k, 0 ≤ ψ k)
    (hg : ∀ ρ ∈ carrier ∩ {ρ | R < |ρ.im - t|}, g ρ ≤ mult ρ * ψ ⌊|ρ.im - t|⌋₊)
    (c : ℝ) (hc : ∀ K : ℕ, ∑ k ∈ Finset.Ico ⌊R⌋₊ K, 2 * C₁ * Real.log (7 / 2 + t + k) * ψ k ≤ c) :
    Summable (fun ρ : ↥(carrier ∩ {ρ | R < |ρ.im - t|}) => g ρ) ∧
      ∑' ρ : ↥(carrier ∩ {ρ | R < |ρ.im - t|}), g ρ ≤ c := by
  classical
  have hpart : ∀ u : Finset ↥(carrier ∩ {ρ | R < |ρ.im - t|}), ∑ x ∈ u, g x ≤ c := by
    intro u
    have hmap := Finset.sum_map u (Function.Embedding.subtype _) g
    simp only [Function.Embedding.coe_subtype] at hmap
    rw [← hmap]
    refine out_finset_sum_le carrier mult hfin hcount hC ht g ψ hψ hg c hc _ ?_
    intro ρ hρ
    obtain ⟨x, _, rfl⟩ := Finset.mem_map.mp hρ
    exact x.2
  have hsum : Summable (fun ρ : ↥(carrier ∩ {ρ | R < |ρ.im - t|}) => g ρ) :=
    summable_of_sum_le (fun ρ => hg0 ρ) hpart
  exact ⟨hsum, hsum.tsum_le_of_sum_le hpart⟩

/-- the two conjuncts of `Hout` from the shell device: summability of the norms and ‖Σ‖ ≤ c
(`norm_tsum_le_tsum_norm`). -/
theorem out_window_norm_le {C₁ t R : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hC : 0 ≤ C₁) (ht : 0 ≤ t) (f : ℝ → ℂ) (ψ : ℕ → ℝ) (hψ : ∀ k, 0 ≤ ψ k)
    (hg : ∀ ρ ∈ carrier ∩ {ρ | R < |ρ.im - t|}, ‖wsum mult f ρ‖ ≤ mult ρ * ψ ⌊|ρ.im - t|⌋₊)
    (c : ℝ) (hc : ∀ K : ℕ, ∑ k ∈ Finset.Ico ⌊R⌋₊ K, 2 * C₁ * Real.log (7 / 2 + t + k) * ψ k ≤ c) :
    Summable (fun ρ : ↥(carrier ∩ {ρ | R < |ρ.im - t|}) => ‖wsum mult f ρ‖) ∧
      ‖∑' ρ : ↥(carrier ∩ {ρ | R < |ρ.im - t|}), wsum mult f ρ‖ ≤ c := by
  obtain ⟨hs, hle⟩ := out_window_summable_tsum_le carrier mult hfin hcount hC ht
    (fun ρ => ‖wsum mult f ρ‖) (fun ρ => norm_nonneg _) ψ hψ hg c hc
  exact ⟨hs, (norm_tsum_le_tsum_norm hs).trans hle⟩

/-! ### §3 The rung: a crude majorant, and clause 5's summability with no numerics -/

/-- (1 + w)¹⁶·e^{−2w} ≤ 8¹⁶ for w ≥ 0, from 1 + w ≤ 8·e^{w/8}. -/
theorem pow16_mul_exp_le {w : ℝ} (hw : 0 ≤ w) : (1 + w) ^ 16 * Real.exp (-(2 * w)) ≤ 8 ^ 16 := by
  have h1 : 1 + w ≤ 8 * Real.exp (w / 8) := by
    have := Real.add_one_le_exp (w / 8); linarith
  have h2 : (1 + w) ^ 16 ≤ 8 ^ 16 * Real.exp (2 * w) := by
    calc (1 + w) ^ 16 ≤ (8 * Real.exp (w / 8)) ^ 16 := pow_le_pow_left₀ (by linarith) h1 16
      _ = 8 ^ 16 * Real.exp (w / 8) ^ 16 := by rw [mul_pow]
      _ = 8 ^ 16 * Real.exp (2 * w) := by
          rw [← Real.exp_nat_mul]; congr 2; push_cast; ring
  rw [Real.exp_neg, ← div_eq_mul_inv, div_le_iff₀ (Real.exp_pos _)]
  exact h2

/-- the rung's constant M_L := C_B²(1 + c_B²L)⁷·8¹⁶/(c_B²L)⁷, with (u + 1)⁷G(Lu)² ≤ M_L for all u ≥ 0. -/
def crudeM (L : ℝ) : ℝ := CB ^ 2 * (1 + cB ^ 2 * L) ^ 7 * 8 ^ 16 / (cB ^ 2 * L) ^ 7

theorem crudeM_nonneg {L : ℝ} (hL : 0 < L) : 0 ≤ crudeM L := by
  unfold crudeM; have := CB_pos; have := cB_pos; positivity

/-- the crude majorant: (u + 1)⁷·G(Lu)² ≤ M_L for u ≥ 0 (with w = c_B√(Lu): u + 1 = (w² + a)/a, a = c_B²L,
w² + a ≤ (1 + a)(1 + w)², 1 + w/2 ≤ 1 + w, and (1 + w)¹⁶e^{−2w} ≤ 8¹⁶). -/
theorem crude_bound {L : ℝ} (hL : 0 < L) {u : ℝ} (hu : 0 ≤ u) :
    (u + 1) ^ 7 * Gmaj (L * u) ^ 2 ≤ crudeM L := by
  have hcB := cB_pos
  have hCB := CB_pos
  set a := cB ^ 2 * L with ha
  have ha0 : 0 < a := by positivity
  set w := cB * Real.sqrt (L * u) with hw
  have hw0 : 0 ≤ w := by positivity
  have hw2 : w ^ 2 = a * u := by
    rw [hw, mul_pow, Real.sq_sqrt (by positivity), ha]; ring
  have hu1 : u + 1 = (w ^ 2 + a) / a := by rw [hw2]; field_simp
  have hG : Gmaj (L * u) = CB * (1 + w / 2) * Real.exp (-w) := by rw [Gmaj, hw]; ring
  have hpoly : (w ^ 2 + a) ^ 7 * (1 + w / 2) ^ 2 ≤ (1 + a) ^ 7 * (1 + w) ^ 16 := by
    have h1 : w ^ 2 + a ≤ (1 + a) * (1 + w) ^ 2 := by nlinarith
    have h2 : 1 + w / 2 ≤ 1 + w := by linarith
    calc (w ^ 2 + a) ^ 7 * (1 + w / 2) ^ 2 ≤ ((1 + a) * (1 + w) ^ 2) ^ 7 * (1 + w) ^ 2 := by gcongr
      _ = (1 + a) ^ 7 * (1 + w) ^ 16 := by ring
  have hexp := pow16_mul_exp_le hw0
  have hexp2 : Real.exp (-w) ^ 2 = Real.exp (-(2 * w)) := by
    rw [← Real.exp_nat_mul]; congr 1; push_cast; ring
  have hcrude : crudeM L = CB ^ 2 * (1 + a) ^ 7 * 8 ^ 16 / a ^ 7 := by rw [crudeM, ha]
  clear_value w a
  rw [hu1, hG, hcrude, div_pow, mul_pow, mul_pow, hexp2, div_mul_eq_mul_div,
    div_le_div_iff_of_pos_right (by positivity)]
  calc (w ^ 2 + a) ^ 7 * (CB ^ 2 * (1 + w / 2) ^ 2 * Real.exp (-(2 * w)))
      = CB ^ 2 * ((w ^ 2 + a) ^ 7 * (1 + w / 2) ^ 2) * Real.exp (-(2 * w)) := by ring
    _ ≤ CB ^ 2 * ((1 + a) ^ 7 * (1 + w) ^ 16) * Real.exp (-(2 * w)) := by gcongr
    _ = CB ^ 2 * (1 + a) ^ 7 * ((1 + w) ^ 16 * Real.exp (-(2 * w))) := by ring
    _ ≤ CB ^ 2 * (1 + a) ^ 7 * 8 ^ 16 := by gcongr

/-- the pointwise bound of a point in shell k = ⌊u⌋₊, majorized by the rung's shell weight e^{L/2}M_L/(k + 1)⁵. -/
theorem crude_shell_bound {L : ℝ} (hL : 0 < L) {u : ℝ} (hu : 0 ≤ u) :
    (u + 1 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * u) ^ 2
      ≤ Real.exp (L / 2) * crudeM L / ((⌊u⌋₊ : ℝ) + 1) ^ 5 := by
  have hk : ((⌊u⌋₊ : ℝ) + 1) ≤ u + 1 := by linarith [Nat.floor_le hu]
  have hk0 : (0 : ℝ) ≤ (⌊u⌋₊ : ℝ) + 1 := by positivity
  have hG := Gmaj_nonneg (L * u)
  have h := crude_bound hL hu
  rw [le_div_iff₀ (by positivity)]
  calc (u + 1 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * u) ^ 2 * ((⌊u⌋₊ : ℝ) + 1) ^ 5
      ≤ (u + 1) ^ 2 * Real.exp (L / 2) * Gmaj (L * u) ^ 2 * (u + 1) ^ 5 := by gcongr; linarith
    _ = Real.exp (L / 2) * ((u + 1) ^ 7 * Gmaj (L * u) ^ 2) := by ring
    _ ≤ Real.exp (L / 2) * crudeM L := by gcongr

/-- the rung's shell series is bounded uniformly in K: Σ_{K₀ ≤ k < K} 2C₁·log(7/2 + t + k)·e^{L/2}M_L/(k + 1)⁵
≤ 2C₁e^{L/2}M_L(9/2 + t)·2, from log(7/2 + t + k) ≤ (9/2 + t)(k + 1) and Σ(k + 1)⁻⁴ ≤ 2. -/
theorem crude_series_le {C₁ t L : ℝ} (hC : 0 ≤ C₁) (ht : 0 ≤ t) (hL : 0 < L) (K₀ K : ℕ) :
    ∑ k ∈ Finset.Ico K₀ K, 2 * C₁ * Real.log (7 / 2 + t + k) * (Real.exp (L / 2) * crudeM L / ((k : ℝ) + 1) ^ 5)
      ≤ 2 * C₁ * Real.exp (L / 2) * crudeM L * (9 / 2 + t) * 2 := by
  have hM := crudeM_nonneg hL
  have hterm : ∀ k : ℕ,
      2 * C₁ * Real.log (7 / 2 + t + k) * (Real.exp (L / 2) * crudeM L / ((k : ℝ) + 1) ^ 5)
        ≤ 2 * C₁ * Real.exp (L / 2) * crudeM L * (9 / 2 + t) * (1 / ((k : ℝ) + 1) ^ 4) := by
    intro k
    have hk0 : (0 : ℝ) ≤ k := Nat.cast_nonneg k
    have hlog : Real.log (7 / 2 + t + k) ≤ (9 / 2 + t) * ((k : ℝ) + 1) := by
      have := Real.log_le_sub_one_of_pos (show 0 < 7 / 2 + t + (k : ℝ) by positivity)
      nlinarith
    have hlog0 : 0 ≤ Real.log (7 / 2 + t + k) := Real.log_nonneg (by linarith)
    have e : 2 * C₁ * Real.exp (L / 2) * crudeM L * (9 / 2 + t) * (1 / ((k : ℝ) + 1) ^ 4)
        = 2 * C₁ * ((9 / 2 + t) * ((k : ℝ) + 1)) * (Real.exp (L / 2) * crudeM L / ((k : ℝ) + 1) ^ 5) := by
      field_simp
    rw [e]
    gcongr
  calc ∑ k ∈ Finset.Ico K₀ K, 2 * C₁ * Real.log (7 / 2 + t + k) * (Real.exp (L / 2) * crudeM L / ((k : ℝ) + 1) ^ 5)
      ≤ ∑ k ∈ Finset.Ico K₀ K, 2 * C₁ * Real.exp (L / 2) * crudeM L * (9 / 2 + t) * (1 / ((k : ℝ) + 1) ^ 4) :=
        Finset.sum_le_sum fun k _ => hterm k
    _ ≤ ∑ k ∈ Finset.range K, 2 * C₁ * Real.exp (L / 2) * crudeM L * (9 / 2 + t) * (1 / ((k : ℝ) + 1) ^ 4) :=
        Finset.sum_le_sum_of_subset_of_nonneg
          (fun k hk => Finset.mem_range.mpr (Finset.mem_Ico.mp hk).2) (fun k _ _ => by positivity)
    _ = 2 * C₁ * Real.exp (L / 2) * crudeM L * (9 / 2 + t) * ∑ k ∈ Finset.range K, 1 / ((k : ℝ) + 1) ^ 4 := by
        rw [Finset.mul_sum]
    _ ≤ 2 * C₁ * Real.exp (L / 2) * crudeM L * (9 / 2 + t) * 2 :=
        mul_le_mul_of_nonneg_left (sum_inv_pow_four_le' K) (by positivity)

/-- C₁ ≥ 0 is implied by the local count (at x = 0: 0 ≤ count ≤ C₁·log 3). -/
theorem C1_nonneg_of_count {C₁ : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|)) :
    0 ≤ C₁ := by
  have h := hcount 0
  have h0 : (0 : ℝ) ≤ ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - 0| ≤ 1}, mult ρ : ℕ) : ℝ) := Nat.cast_nonneg _
  have hl : 0 < Real.log (3 + |(0 : ℝ)|) := by
    rw [abs_zero, add_zero]; exact Real.log_pos (by norm_num)
  exact le_of_mul_le_mul_right (by rw [zero_mul]; linarith) hl

/-- **clause 5's summability (the rung, no numerics)**: for any carrier of 𝒞(C₁) inside the strip, t ≥ 3 and L > 0,
the out-window sum beyond 73L of ‖m_ρ h_f(γ_ρ)conj(h_f(conj γ_ρ))‖, f = f_{t,L}, is summable — the first conjunct of
`Hout` at R = 73L. -/
theorem clause5_summable {C₁ t L : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hstrip : ∀ ρ ∈ carrier, 0 ≤ ρ.re ∧ ρ.re ≤ 1) (ht : 3 ≤ t) (hL : 0 < L) :
    Summable (fun ρ : ↥(carrier ∩ {ρ | 73 * L < |ρ.im - t|}) => ‖wsum mult (ftest t L) ρ‖) := by
  have hC : 0 ≤ C₁ := C1_nonneg_of_count carrier mult hcount
  have hM := crudeM_nonneg hL
  exact (out_window_norm_le (R := 73 * L) carrier mult hfin hcount hC (by linarith) (ftest t L)
    (fun k => Real.exp (L / 2) * crudeM L / ((k : ℝ) + 1) ^ 5) (fun k => by positivity)
    (fun ρ hρ => (norm_wsum_le_strip hL (hstrip ρ hρ.1)).trans
      (mul_le_mul_of_nonneg_left (crude_shell_bound hL (abs_nonneg _)) (Nat.cast_nonneg _)))
    _ (fun K => crude_series_le hC (by linarith) hL _ K)).1

/-! ### §4 The tail incomplete-gamma integrals (Piece 1 item 4 — absent from Mathlib): γ_n(a, s) := Σ_{j≤n} (n!/j!)s^j/a^{n+1−j}
and ∫_{s₀}^∞ sⁿe^{−as}ds = e^{−as₀}γ_n(a, s₀), through the antiderivative −e^{−as}γ_n(a, s) — the identity
d/ds[e^{−as}γ_n(s)] = −sⁿe^{−as} is proved for EVERY n at once by induction through the recursion
γ_{n+1}(s) = s^{n+1}/a + ((n + 1)/a)γ_n(s), so the n = 9 instance of stop line (c) is the general case. -/

/-- γ_n(a, s) := Σ_{j=0}^{n} (n!/j!)·s^j/a^{n+1−j} — `r0_73_check.py` lines 22–23 (`gamma_poly`), term for term
(= e^{as}∫_s^∞ xⁿe^{−ax}dx, `integral_pow_mul_exp_Ioi`). -/
def gammaPoly (n : ℕ) (a s : ℝ) : ℝ :=
  ∑ j ∈ Finset.range (n + 1), (n.factorial : ℝ) / (j.factorial : ℝ) * s ^ j / a ^ (n + 1 - j)

theorem gammaPoly_zero (a s : ℝ) : gammaPoly 0 a s = 1 / a := by
  simp [gammaPoly]

/-- the recursion γ_{n+1}(s) = s^{n+1}/a + ((n + 1)/a)·γ_n(s), read off the Finset sum. -/
theorem gammaPoly_succ (n : ℕ) {a : ℝ} (ha : a ≠ 0) (s : ℝ) :
    gammaPoly (n + 1) a s = s ^ (n + 1) / a + ((n : ℝ) + 1) / a * gammaPoly n a s := by
  unfold gammaPoly
  rw [Finset.sum_range_succ, Finset.mul_sum]
  have hlast : ((n + 1).factorial : ℝ) / ((n + 1).factorial : ℝ) * s ^ (n + 1) / a ^ (n + 1 + 1 - (n + 1))
      = s ^ (n + 1) / a := by
    rw [div_self (by positivity), one_mul, show n + 1 + 1 - (n + 1) = 1 by omega, pow_one]
  rw [hlast, add_comm]
  congr 1
  refine Finset.sum_congr rfl fun j hj => ?_
  have hj' : j ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
  rw [show n + 1 + 1 - j = (n + 1 - j) + 1 by omega, pow_succ, Nat.factorial_succ]
  push_cast
  field_simp

theorem gammaPoly_nonneg (n : ℕ) {a s : ℝ} (ha : 0 ≤ a) (hs : 0 ≤ s) : 0 ≤ gammaPoly n a s := by
  unfold gammaPoly; positivity

/-- γ_n is monotone in s (nonnegative coefficients). -/
theorem gammaPoly_mono (n : ℕ) {a s s' : ℝ} (ha : 0 ≤ a) (hs : 0 ≤ s) (hss' : s ≤ s') :
    gammaPoly n a s ≤ gammaPoly n a s' := by
  unfold gammaPoly
  refine Finset.sum_le_sum fun j _ => ?_
  gcongr

/-- the monomial comparison γ_n(a, s·r) ≤ rⁿ·γ_n(a, s) for r ≥ 1 (every monomial has degree ≤ n). -/
theorem gammaPoly_mul_le (n : ℕ) {a s r : ℝ} (ha : 0 ≤ a) (hs : 0 ≤ s) (hr : 1 ≤ r) :
    gammaPoly n a (s * r) ≤ r ^ n * gammaPoly n a s := by
  unfold gammaPoly
  rw [Finset.mul_sum]
  refine Finset.sum_le_sum fun j hj => ?_
  have hj' : j ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hj)
  have hrj : r ^ j ≤ r ^ n := pow_le_pow_right₀ hr hj'
  have e : (n.factorial : ℝ) / (j.factorial : ℝ) * (s * r) ^ j / a ^ (n + 1 - j)
      = r ^ j * ((n.factorial : ℝ) / (j.factorial : ℝ) * s ^ j / a ^ (n + 1 - j)) := by
    rw [mul_pow]; ring
  rw [e]
  gcongr

/-- d/ds[e^{−as}γ_n(a, s)] = −sⁿe^{−as}, every n, by induction through `gammaPoly_succ`. -/
theorem hasDerivAt_exp_mul_gammaPoly {a : ℝ} (ha : 0 < a) (n : ℕ) (s : ℝ) :
    HasDerivAt (fun s => Real.exp (-(a * s)) * gammaPoly n a s) (-(s ^ n * Real.exp (-(a * s)))) s := by
  have hd : ∀ s : ℝ, HasDerivAt (fun s => Real.exp (-(a * s))) (Real.exp (-(a * s)) * (-a)) s := by
    intro s
    have := (((hasDerivAt_id s).const_mul a).neg).exp
    simp only [Pi.neg_apply, id_eq, mul_one] at this
    exact this
  induction n generalizing s with
  | zero =>
    have h : (fun s => Real.exp (-(a * s)) * gammaPoly 0 a s) = fun s => Real.exp (-(a * s)) * (1 / a) := by
      funext s; rw [gammaPoly_zero]
    rw [h]
    refine ((hd s).mul_const (1 / a)).congr_deriv ?_
    rw [pow_zero, one_mul]
    field_simp
  | succ n ih =>
    have h : (fun s => Real.exp (-(a * s)) * gammaPoly (n + 1) a s)
        = fun s => Real.exp (-(a * s)) * s ^ (n + 1) / a
          + ((n : ℝ) + 1) / a * (Real.exp (-(a * s)) * gammaPoly n a s) := by
      funext s; rw [gammaPoly_succ n ha.ne' s]; ring
    rw [h]
    have h1 : HasDerivAt (fun s => Real.exp (-(a * s)) * s ^ (n + 1) / a)
        ((Real.exp (-(a * s)) * (-a) * s ^ (n + 1)
          + Real.exp (-(a * s)) * (((n + 1 : ℕ) : ℝ) * s ^ (n + 1 - 1))) / a) s :=
      ((hd s).mul (hasDerivAt_pow (n + 1) s)).div_const a
    have h2 := (ih s).const_mul (((n : ℝ) + 1) / a)
    refine (h1.add h2).congr_deriv ?_
    rw [show n + 1 - 1 = n by omega]
    push_cast
    field_simp
    ring

/-- e^{−as}γ_n(a, s) → 0 as s → ∞ (each monomial s^j e^{−as} → 0). -/
theorem tendsto_exp_mul_gammaPoly {a : ℝ} (ha : 0 < a) (n : ℕ) :
    Filter.Tendsto (fun s => Real.exp (-(a * s)) * gammaPoly n a s) Filter.atTop (nhds 0) := by
  have hterm : ∀ j : ℕ, Filter.Tendsto (fun s => s ^ j * Real.exp (-(a * s))) Filter.atTop (nhds 0) := by
    intro j
    have h1 : Filter.Tendsto (fun s => (a * s) ^ j * Real.exp (-(a * s))) Filter.atTop (nhds 0) :=
      (Real.tendsto_pow_mul_exp_neg_atTop_nhds_zero j).comp (Filter.tendsto_id.const_mul_atTop ha)
    have h2 := h1.div_const (a ^ j)
    rw [zero_div] at h2
    refine h2.congr fun s => ?_
    rw [mul_pow]; field_simp
  have hj : ∀ j : ℕ, Filter.Tendsto
      (fun s => Real.exp (-(a * s)) * ((n.factorial : ℝ) / (j.factorial : ℝ) * s ^ j / a ^ (n + 1 - j)))
      Filter.atTop (nhds 0) := by
    intro j
    have := (hterm j).const_mul ((n.factorial : ℝ) / (j.factorial : ℝ) / a ^ (n + 1 - j))
    rw [mul_zero] at this
    refine this.congr fun s => ?_
    ring
  have hsum := tendsto_finsetSum (Finset.range (n + 1)) (fun j _ => hj j)
  simp only [Finset.sum_const_zero] at hsum
  refine hsum.congr fun s => ?_
  unfold gammaPoly
  rw [Finset.mul_sum]

/-- **the tail incomplete-gamma integral** (Piece 1 item 4): for a > 0 and s₀ ≥ 0,
∫_{s₀}^∞ sⁿe^{−as}ds = e^{−as₀}·γ_n(a, s₀) — the note's ∫_{s₀}^∞sⁿe^{−as}ds = e^{−as₀}Σ_j(n!/j!)s₀^j a^{−(n+1−j)}. -/
theorem integral_pow_mul_exp_Ioi {a : ℝ} (ha : 0 < a) (n : ℕ) {s₀ : ℝ} (hs₀ : 0 ≤ s₀) :
    ∫ s in Set.Ioi s₀, s ^ n * Real.exp (-(a * s)) = Real.exp (-(a * s₀)) * gammaPoly n a s₀ := by
  have hd : ∀ s ∈ Set.Ici s₀,
      HasDerivAt (fun s => -(Real.exp (-(a * s)) * gammaPoly n a s)) (s ^ n * Real.exp (-(a * s))) s := by
    intro s _
    have := (hasDerivAt_exp_mul_gammaPoly ha n s).neg
    rwa [neg_neg] at this
  have hpos : ∀ s ∈ Set.Ioi s₀, 0 ≤ s ^ n * Real.exp (-(a * s)) := by
    intro s hs
    have : 0 ≤ s := le_trans hs₀ (le_of_lt hs)
    positivity
  have hlim := (tendsto_exp_mul_gammaPoly ha n).neg
  rw [neg_zero] at hlim
  rw [integral_Ioi_of_hasDerivAt_of_nonneg' hd hpos hlim]
  ring

/-- Γ_m(s) := γ_{2m+1}(2c_B, s) + c_B·γ_{2m+2}(2c_B, s) + (c_B²/4)·γ_{2m+3}(2c_B, s) — the bracket of
`r0_73_check.py` line 28 (a = 2c_B; the coefficients 1, c_B, c_B²/4 of (1 + (c_B/2)s)²). -/
def GammaM (m : ℕ) (s : ℝ) : ℝ :=
  gammaPoly (2 * m + 1) (2 * cB) s + cB * gammaPoly (2 * m + 2) (2 * cB) s
    + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) s

theorem GammaM_nonneg (m : ℕ) {s : ℝ} (hs : 0 ≤ s) : 0 ≤ GammaM m s := by
  have := cB_pos
  unfold GammaM
  have h1 := gammaPoly_nonneg (2 * m + 1) (a := 2 * cB) (by positivity) hs
  have h2 := gammaPoly_nonneg (2 * m + 2) (a := 2 * cB) (by positivity) hs
  have h3 := gammaPoly_nonneg (2 * m + 3) (a := 2 * cB) (by positivity) hs
  positivity

theorem GammaM_mono (m : ℕ) {s s' : ℝ} (hs : 0 ≤ s) (hss' : s ≤ s') : GammaM m s ≤ GammaM m s' := by
  have := cB_pos
  unfold GammaM
  have h1 := gammaPoly_mono (2 * m + 1) (a := 2 * cB) (by positivity) hs hss'
  have h2 := gammaPoly_mono (2 * m + 2) (a := 2 * cB) (by positivity) hs hss'
  have h3 := gammaPoly_mono (2 * m + 3) (a := 2 * cB) (by positivity) hs hss'
  have hc2 : 0 ≤ cB ^ 2 / 4 := by positivity
  nlinarith [mul_le_mul_of_nonneg_left h2 this.le, mul_le_mul_of_nonneg_left h3 hc2]

/-- d/ds[e^{−2c_Bs}Γ_m(s)] = −s^{2m+1}(1 + (c_B/2)s)²e^{−2c_Bs} (the three instances n = 2m+1, 2m+2, 2m+3 of
`hasDerivAt_exp_mul_gammaPoly`, and (1 + (c_B/2)s)² = 1 + c_Bs + (c_B²/4)s²). -/
theorem hasDerivAt_exp_mul_GammaM (m : ℕ) (s : ℝ) :
    HasDerivAt (fun s => Real.exp (-(2 * cB * s)) * GammaM m s)
      (-(s ^ (2 * m + 1) * (1 + cB / 2 * s) ^ 2 * Real.exp (-(2 * cB * s)))) s := by
  have ha : 0 < 2 * cB := by have := cB_pos; positivity
  have h1 := hasDerivAt_exp_mul_gammaPoly ha (2 * m + 1) s
  have h2 := (hasDerivAt_exp_mul_gammaPoly ha (2 * m + 2) s).const_mul cB
  have h3 := (hasDerivAt_exp_mul_gammaPoly ha (2 * m + 3) s).const_mul (cB ^ 2 / 4)
  have h := (h1.add h2).add h3
  refine (h.congr_of_eventuallyEq (Filter.Eventually.of_forall fun s => ?_)).congr_deriv ?_
  · simp only [Pi.add_apply]; unfold GammaM; ring
  · ring

theorem tendsto_exp_mul_GammaM (m : ℕ) :
    Filter.Tendsto (fun s => Real.exp (-(2 * cB * s)) * GammaM m s) Filter.atTop (nhds 0) := by
  have ha : 0 < 2 * cB := by have := cB_pos; positivity
  have h1 := tendsto_exp_mul_gammaPoly ha (2 * m + 1)
  have h2 := (tendsto_exp_mul_gammaPoly ha (2 * m + 2)).const_mul cB
  have h3 := (tendsto_exp_mul_gammaPoly ha (2 * m + 3)).const_mul (cB ^ 2 / 4)
  have h := (h1.add h2).add h3
  simp only [mul_zero, add_zero] at h
  refine h.congr fun s => ?_
  unfold GammaM; ring

/-! ### §5 The substitution u = s²/L, folded into the antiderivative: φ_m(u) := u^m(1 + (c_B/2)√(Lu))²e^{−2c_B√(Lu)}
has the antiderivative Φ_m(u) := −(2/L^{m+1})e^{−2c_B√(Lu)}Γ_m(√(Lu)) (chain rule through √(Lu)), so
∫_{u₀}^∞φ_m = (2/L^{m+1})e^{−2c_Bs₀}Γ_m(s₀), s₀ = √(Lu₀) — the note's ∫_{u₀}^∞φ_m(u)du = (2/L^{m+1})∫_{s₀}^∞ s^{2m+1}(1 + (c_B/2)s)²e^{−2c_Bs}ds. -/

/-- φ_m(u) := u^m(1 + (c_B/2)√(Lu))²e^{−2c_B√(Lu)} (note §6 "The sums"). -/
def phi (m : ℕ) (L u : ℝ) : ℝ :=
  u ^ m * (1 + cB / 2 * Real.sqrt (L * u)) ^ 2 * Real.exp (-(2 * cB * Real.sqrt (L * u)))

/-- Φ_m(u) := −(2/L^{m+1})e^{−2c_B√(Lu)}Γ_m(√(Lu)), the antiderivative of φ_m. -/
def Phi (m : ℕ) (L u : ℝ) : ℝ :=
  -(2 / L ^ (m + 1) * (Real.exp (-(2 * cB * Real.sqrt (L * u))) * GammaM m (Real.sqrt (L * u))))

theorem phi_nonneg (m : ℕ) {L u : ℝ} (hu : 0 ≤ u) : 0 ≤ phi m L u := by
  have := cB_pos; unfold phi; positivity

/-- φ_m in the s-variable: φ_m(u) = s^{2m}(1 + (c_B/2)s)²e^{−2c_Bs}/L^m, s = √(Lu). -/
theorem phi_eq (m : ℕ) {L u : ℝ} (hL : 0 < L) (hu : 0 ≤ u) :
    phi m L u = Real.sqrt (L * u) ^ (2 * m) * (1 + cB / 2 * Real.sqrt (L * u)) ^ 2
      * Real.exp (-(2 * cB * Real.sqrt (L * u))) / L ^ m := by
  unfold phi
  have hs2 : Real.sqrt (L * u) ^ (2 * m) = L ^ m * u ^ m := by
    rw [pow_mul, Real.sq_sqrt (by positivity), mul_pow]
  rw [hs2]
  field_simp

theorem hasDerivAt_Phi (m : ℕ) {L u : ℝ} (hL : 0 < L) (hu : 0 < u) : HasDerivAt (Phi m L) (phi m L u) u := by
  have hLu : 0 < L * u := by positivity
  have hs : 0 < Real.sqrt (L * u) := Real.sqrt_pos.mpr hLu
  have hsq : HasDerivAt (fun u => Real.sqrt (L * u)) (L / (2 * Real.sqrt (L * u))) u := by
    have := ((hasDerivAt_id u).const_mul L).sqrt (by simpa only [id_eq] using hLu.ne')
    simpa only [id_eq, mul_one] using this
  have hE := (hasDerivAt_exp_mul_GammaM m (Real.sqrt (L * u))).comp u hsq
  have h := (hE.const_mul (2 / L ^ (m + 1))).neg
  refine (h.congr_of_eventuallyEq (Filter.Eventually.of_forall fun u => ?_)).congr_deriv ?_
  · rfl
  unfold phi
  set s := Real.sqrt (L * u) with hs_def
  have hs2 : s ^ (2 * m + 1) = L ^ m * u ^ m * s := by
    rw [pow_succ, pow_mul, hs_def, Real.sq_sqrt hLu.le, mul_pow]
  rw [hs2]
  field_simp
  ring

theorem tendsto_Phi (m : ℕ) {L : ℝ} (hL : 0 < L) : Filter.Tendsto (Phi m L) Filter.atTop (nhds 0) := by
  have hsqrt : Filter.Tendsto (fun u : ℝ => Real.sqrt (L * u)) Filter.atTop Filter.atTop :=
    Real.tendsto_sqrt_atTop.comp (Filter.tendsto_id.const_mul_atTop hL)
  have h := ((tendsto_exp_mul_GammaM m).comp hsqrt).const_mul (2 / L ^ (m + 1))
  rw [mul_zero] at h
  have h' := h.neg
  rw [neg_zero] at h'
  exact h'

/-- **∫_{u₀}^∞ φ_m = (2/L^{m+1})e^{−2c_Bs₀}Γ_m(s₀)**, s₀ = √(Lu₀) (Piece 1 items 4–5 together). -/
theorem integral_phi_Ioi (m : ℕ) {L u₀ : ℝ} (hL : 0 < L) (hu₀ : 0 < u₀) :
    ∫ u in Set.Ioi u₀, phi m L u
      = 2 / L ^ (m + 1) * (Real.exp (-(2 * cB * Real.sqrt (L * u₀))) * GammaM m (Real.sqrt (L * u₀))) := by
  have hd : ∀ u ∈ Set.Ici u₀, HasDerivAt (Phi m L) (phi m L u) u :=
    fun u hu => hasDerivAt_Phi m hL (lt_of_lt_of_le hu₀ hu)
  have hpos : ∀ u ∈ Set.Ioi u₀, 0 ≤ phi m L u := fun u hu => phi_nonneg m (le_trans hu₀.le (le_of_lt hu))
  rw [integral_Ioi_of_hasDerivAt_of_nonneg' hd hpos (tendsto_Phi m hL)]
  unfold Phi; ring

theorem integrableOn_phi_Ioi (m : ℕ) {L u₀ : ℝ} (hL : 0 < L) (hu₀ : 0 < u₀) :
    IntegrableOn (phi m L) (Set.Ioi u₀) := by
  have hd : ∀ u ∈ Set.Ici u₀, HasDerivAt (Phi m L) (phi m L u) u :=
    fun u hu => hasDerivAt_Phi m hL (lt_of_lt_of_le hu₀ hu)
  have hpos : ∀ u ∈ Set.Ioi u₀, 0 ≤ phi m L u := fun u hu => phi_nonneg m (le_trans hu₀.le (le_of_lt hu))
  exact integrableOn_Ioi_deriv_of_nonneg' hd hpos (tendsto_Phi m hL)

/-! ### §6 The tail sum is at most the first term plus the tail integral (Piece 1 item 3): φ_m is antitone on
[u₀, ∞) once c_B√(Lu₀) ≥ 2m (the s-form g_m(s) = s^{2m}(1 + (c_B/2)s)²e^{−2c_Bs} decreases from s = 2m/c_B on,
by the ratio bound g(s₂)/g(s₁) ≤ e^{d(2m/s₁ − c_B)}, d = s₂ − s₁ — the integrated form of the note's
(log φ_m)′ ≤ (m + 1)/u − c_B√L/√u < 0), and `AntitoneOn.sum_le_integral`. -/

/-- g_m(s) := s^{2m}(1 + (c_B/2)s)²e^{−2c_Bs} is antitone on [s₁, ∞) when 2m ≤ c_Bs₁. -/
theorem gpow_antitone (m : ℕ) {s₁ s₂ : ℝ} (h1 : 0 < s₁) (hm : 2 * m ≤ cB * s₁) (h12 : s₁ ≤ s₂) :
    s₂ ^ (2 * m) * (1 + cB / 2 * s₂) ^ 2 * Real.exp (-(2 * cB * s₂))
      ≤ s₁ ^ (2 * m) * (1 + cB / 2 * s₁) ^ 2 * Real.exp (-(2 * cB * s₁)) := by
  have hc := cB_pos
  set d := s₂ - s₁ with hd
  have hd0 : 0 ≤ d := by linarith
  have hA : s₂ ≤ s₁ * Real.exp (d / s₁) := by
    have h := Real.add_one_le_exp (d / s₁)
    have h' : s₁ * (d / s₁ + 1) ≤ s₁ * Real.exp (d / s₁) := by gcongr
    rw [mul_add, mul_div_cancel₀ _ h1.ne', mul_one] at h'
    linarith
  have hA' : s₂ ^ (2 * m) ≤ s₁ ^ (2 * m) * Real.exp (d / s₁) ^ (2 * m) := by
    rw [← mul_pow]; exact pow_le_pow_left₀ (by linarith) hA _
  have hB : 1 + cB / 2 * s₂ ≤ (1 + cB / 2 * s₁) * Real.exp (cB * d / 2) := by
    have h := Real.add_one_le_exp (cB * d / 2)
    have h' : 1 + cB / 2 * s₂ ≤ (1 + cB / 2 * s₁) * (cB * d / 2 + 1) := by
      rw [hd]; nlinarith [mul_nonneg hc.le h1.le, mul_nonneg hc.le hd0, mul_nonneg (mul_nonneg hc.le h1.le) (mul_nonneg hc.le hd0)]
    calc 1 + cB / 2 * s₂ ≤ (1 + cB / 2 * s₁) * (cB * d / 2 + 1) := h'
      _ ≤ (1 + cB / 2 * s₁) * Real.exp (cB * d / 2) := by gcongr
  have hs2 : 0 ≤ s₂ := by linarith
  have hB' : (1 + cB / 2 * s₂) ^ 2 ≤ (1 + cB / 2 * s₁) ^ 2 * Real.exp (cB * d / 2) ^ 2 := by
    rw [← mul_pow]; exact pow_le_pow_left₀ (by positivity) hB 2
  have hC : Real.exp (-(2 * cB * s₂)) = Real.exp (-(2 * cB * s₁)) * Real.exp (-(2 * cB * d)) := by
    rw [← Real.exp_add]; congr 1; rw [hd]; ring
  have hE : Real.exp (d / s₁) ^ (2 * m) * Real.exp (cB * d / 2) ^ 2 * Real.exp (-(2 * cB * d)) ≤ 1 := by
    rw [← Real.exp_nat_mul, ← Real.exp_nat_mul, ← Real.exp_add, ← Real.exp_add, Real.exp_le_one_iff]
    push_cast
    have : (2 * m : ℝ) * (d / s₁) ≤ cB * d := by
      rw [mul_div_assoc', div_le_iff₀ h1]; nlinarith
    linarith
  calc s₂ ^ (2 * m) * (1 + cB / 2 * s₂) ^ 2 * Real.exp (-(2 * cB * s₂))
      ≤ (s₁ ^ (2 * m) * Real.exp (d / s₁) ^ (2 * m)) * ((1 + cB / 2 * s₁) ^ 2 * Real.exp (cB * d / 2) ^ 2)
          * (Real.exp (-(2 * cB * s₁)) * Real.exp (-(2 * cB * d))) := by
        rw [hC]; gcongr
    _ = s₁ ^ (2 * m) * (1 + cB / 2 * s₁) ^ 2 * Real.exp (-(2 * cB * s₁))
          * (Real.exp (d / s₁) ^ (2 * m) * Real.exp (cB * d / 2) ^ 2 * Real.exp (-(2 * cB * d))) := by ring
    _ ≤ s₁ ^ (2 * m) * (1 + cB / 2 * s₁) ^ 2 * Real.exp (-(2 * cB * s₁)) * 1 := by gcongr
    _ = _ := by ring

/-- φ_m is antitone on [u₀, b] when 2m ≤ c_B√(Lu₀). -/
theorem phi_antitoneOn (m : ℕ) {L u₀ : ℝ} (hL : 0 < L) (hu₀ : 0 < u₀) (hm : 2 * m ≤ cB * Real.sqrt (L * u₀))
    (b : ℝ) : AntitoneOn (phi m L) (Set.Icc u₀ b) := by
  intro u hu v hv huv
  have hc := cB_pos
  have hu0 : 0 < u := lt_of_lt_of_le hu₀ hu.1
  have hv0 : 0 < v := lt_of_lt_of_le hu0 huv
  have hs0 : Real.sqrt (L * u₀) ≤ Real.sqrt (L * u) :=
    Real.sqrt_le_sqrt (mul_le_mul_of_nonneg_left hu.1 hL.le)
  have hsu : 0 < Real.sqrt (L * u) := Real.sqrt_pos.mpr (by positivity)
  have hsuv : Real.sqrt (L * u) ≤ Real.sqrt (L * v) :=
    Real.sqrt_le_sqrt (mul_le_mul_of_nonneg_left huv hL.le)
  have hm' : 2 * m ≤ cB * Real.sqrt (L * u) := le_trans hm (by gcongr)
  have key := gpow_antitone m hsu hm' hsuv
  rw [phi_eq m hL hu0.le, phi_eq m hL hv0.le]
  exact div_le_div_of_nonneg_right key (by positivity)

/-- **Σ_{K₀ ≤ k < K} φ_m(k) ≤ φ_m(K₀) + ∫_{K₀}^∞ φ_m** (note §6 "The sums": Σ_m ≤ β^mC_B²[φ_m(u₀) + ∫_{u₀}^∞φ_m]). -/
theorem sum_phi_le (m : ℕ) {L : ℝ} (hL : 0 < L) {K₀ : ℕ} (hK₀ : 0 < K₀)
    (hm : 2 * m ≤ cB * Real.sqrt (L * K₀)) (K : ℕ) :
    ∑ k ∈ Finset.Ico K₀ K, phi m L k ≤ phi m L K₀ + ∫ u in Set.Ioi (K₀ : ℝ), phi m L u := by
  have hK₀' : (0 : ℝ) < K₀ := by exact_mod_cast hK₀
  have hint : IntegrableOn (phi m L) (Set.Ioi (K₀ : ℝ)) := integrableOn_phi_Ioi m hL hK₀'
  have hI0 : 0 ≤ ∫ u in Set.Ioi (K₀ : ℝ), phi m L u :=
    setIntegral_nonneg measurableSet_Ioi fun u hu => phi_nonneg m (le_trans hK₀'.le (le_of_lt hu))
  have hφ0 : 0 ≤ phi m L K₀ := phi_nonneg m hK₀'.le
  rw [Finset.sum_Ico_eq_sum_range]
  rcases Nat.eq_zero_or_pos (K - K₀) with h0 | hpos
  · rw [h0, Finset.sum_range_zero]; linarith
  · obtain ⟨a, ha⟩ : ∃ a, K - K₀ = a + 1 := ⟨K - K₀ - 1, by omega⟩
    rw [ha, Finset.sum_range_succ']
    have hanti : AntitoneOn (phi m L) (Set.Icc (K₀ : ℝ) ((K₀ : ℝ) + a)) := phi_antitoneOn m hL hK₀' hm _
    have h1 := AntitoneOn.sum_le_integral hanti
    have h2 : ∫ x in (K₀ : ℝ)..(K₀ : ℝ) + a, phi m L x ≤ ∫ u in Set.Ioi (K₀ : ℝ), phi m L u := by
      rw [intervalIntegral.integral_of_le (by linarith [Nat.cast_nonneg (α := ℝ) a])]
      refine setIntegral_mono_set hint ?_ (Filter.Eventually.of_forall fun x hx => Set.Ioc_subset_Ioi_self hx)
      exact (ae_restrict_iff' measurableSet_Ioi).mpr
        (Filter.Eventually.of_forall fun u hu => phi_nonneg m (le_trans hK₀'.le (le_of_lt hu)))
    push_cast at h1 ⊢
    rw [add_zero]
    linarith

/-! ### §7 The absorption spent once (Piece 1 item 6; addendum A3, check-O §12.8) and the relaxations (item 7) -/

/-- 5/3 ≤ log 6 (e⁵ < 216). -/
theorem five_thirds_le_log_six : 5 / 3 ≤ Real.log 6 := by
  have h5 : Real.exp 5 < 216 := by
    rw [show (5 : ℝ) = ((5 : ℕ) : ℝ) * 1 by norm_num, Real.exp_nat_mul]
    calc Real.exp 1 ^ 5 < 2.7182818286 ^ 5 := by
          gcongr; exact Real.exp_one_lt_d9
      _ < 216 := by norm_num
  have h53 : Real.exp (5 / 3) < 6 := by
    have h3 : Real.exp (5 / 3) ^ 3 = Real.exp 5 := by
      rw [← Real.exp_nat_mul]; congr 1; push_cast; ring
    have : Real.exp (5 / 3) ^ 3 < 6 ^ 3 := by rw [h3]; norm_num; exact h5
    exact lt_of_pow_lt_pow_left₀ 3 (by norm_num) this
  exact (Real.le_log_iff_exp_le (by norm_num)).mpr h53.le

/-- the absorption of the prefactors through the L-hypothesis, spent ONCE (A3): from
8(log log(3 + t) + log(2b₁C₁)) ≤ L, 2C₁log(3 + t) ≤ e^{L/8}/b₁ and 2C₁ ≤ e^{L/8}/b₁; and log(7/2 + t) ≤ 1.05·log(3 + t)
for t ≥ 3 (log(7/2 + t) − log(3 + t) ≤ 1/(2(3 + t)) ≤ 1/12 ≤ 0.05·log 6). -/
theorem absorb_once {C₁ t L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t)
    (hL8 : 8 * (Real.log (Real.log (3 + t)) + Real.log (2 * b1sym * C₁)) ≤ L) :
    2 * C₁ * Real.log (3 + t) ≤ Real.exp (L / 8) / b1sym ∧ 2 * C₁ ≤ Real.exp (L / 8) / b1sym ∧
      Real.log (7 / 2 + t) ≤ 105 / 100 * Real.log (3 + t) := by
  have hb4 := four_le_b1sym
  have hb0 : 0 < b1sym := by linarith
  have hlog6 : Real.log 6 ≤ Real.log (3 + t) := Real.log_le_log (by norm_num) (by linarith)
  have h53 := five_thirds_le_log_six
  have hℓ0 : 0 < Real.log (3 + t) := by linarith
  have hprod : Real.log (Real.log (3 + t)) + Real.log (2 * b1sym * C₁)
      = Real.log (Real.log (3 + t) * (2 * b1sym * C₁)) := by
    rw [Real.log_mul hℓ0.ne' (by positivity)]
  have hexp : Real.log (3 + t) * (2 * b1sym * C₁) ≤ Real.exp (L / 8) := by
    rw [← Real.log_le_iff_le_exp (by positivity), ← hprod]; linarith
  have h1 : 2 * C₁ * Real.log (3 + t) ≤ Real.exp (L / 8) / b1sym := by
    rw [le_div_iff₀ hb0]; nlinarith
  refine ⟨h1, ?_, ?_⟩
  · have : 2 * C₁ ≤ 2 * C₁ * Real.log (3 + t) := by nlinarith
    linarith
  · have hq : Real.log (7 / 2 + t) - Real.log (3 + t) ≤ 1 / 12 := by
      rw [← Real.log_div (by linarith) (by linarith)]
      have := Real.log_le_sub_one_of_pos (show 0 < (7 / 2 + t) / (3 + t) by positivity)
      have h' : (7 / 2 + t) / (3 + t) - 1 ≤ 1 / 12 := by
        rw [div_sub_one (by linarith), div_le_iff₀ (by linarith)]; linarith
      linarith
    nlinarith

/-- the relaxation of the exponential: with s₀ = √(LK₀) and K₀ ≥ 73L − 1, e^{−2c_Bs₀} ≤ e^{2c_B/√73}·e^{−2c_B√73·L}
(from s₀ ≥ √73·L − 1/√73, i.e. (√73L − 1/√73)² ≤ L(73L − 1) ≤ LK₀ for L ≥ 1/73). -/
theorem exp_neg_s0_le {L K₀ : ℝ} (hL : 1 ≤ L) (hK₀ : 73 * L - 1 ≤ K₀) :
    Real.exp (-(2 * cB * Real.sqrt (L * K₀)))
      ≤ Real.exp (2 * cB / Real.sqrt 73) * Real.exp (-(2 * cB * Real.sqrt 73 * L)) := by
  have hc := cB_pos
  have h73 : 0 < Real.sqrt 73 := Real.sqrt_pos.mpr (by norm_num)
  have hsq : Real.sqrt 73 ^ 2 = 73 := Real.sq_sqrt (by norm_num)
  have hmul : Real.sqrt 73 * Real.sqrt 73 = 73 := Real.mul_self_sqrt (by norm_num)
  have hx0 : 0 ≤ (73 * L - 1) / Real.sqrt 73 := div_nonneg (by linarith) h73.le
  have hs : (73 * L - 1) / Real.sqrt 73 ≤ Real.sqrt (L * K₀) := by
    rw [Real.le_sqrt hx0 (by nlinarith)]
    rw [div_pow, hsq, div_le_iff₀ (by norm_num)]
    nlinarith
  rw [← Real.exp_add, Real.exp_le_exp]
  have h1 : 2 * cB * ((73 * L - 1) / Real.sqrt 73) ≤ 2 * cB * Real.sqrt (L * K₀) := by gcongr
  have e2 : 2 * cB * Real.sqrt 73 * L - 2 * cB / Real.sqrt 73
      = 2 * cB * ((Real.sqrt 73 * Real.sqrt 73 * L - 1) / Real.sqrt 73) := by
    field_simp
  rw [hmul] at e2
  linarith

/-- (k + 3/2)^m·G(Lk)² ≤ β^m·C_B²·φ_m(k) for k ≥ 3649, β = 1 + 3/(2(73·50 − 1)) (note §6: (k + 3/2)^m ≤ β^mk^m). -/
theorem pow_mul_Gmaj_sq_le (m : ℕ) {L k : ℝ} (hL : 0 < L) (hk : 3649 ≤ k) :
    (k + 3 / 2) ^ m * Gmaj (L * k) ^ 2 ≤ (1 + 3 / (2 * (73 * 50 - 1))) ^ m * CB ^ 2 * phi m L k := by
  have hc := cB_pos
  have hC := CB_pos
  have hβ : k + 3 / 2 ≤ (1 + 3 / (2 * (73 * 50 - 1))) * k := by nlinarith
  have hG : Gmaj (L * k) ^ 2
      = CB ^ 2 * ((1 + cB / 2 * Real.sqrt (L * k)) ^ 2 * Real.exp (-(2 * cB * Real.sqrt (L * k)))) := by
    rw [Gmaj, mul_pow, mul_pow, ← Real.exp_nat_mul]; push_cast; ring_nf
  rw [hG]
  unfold phi
  calc (k + 3 / 2) ^ m * (CB ^ 2 * ((1 + cB / 2 * Real.sqrt (L * k)) ^ 2 * Real.exp (-(2 * cB * Real.sqrt (L * k)))))
      ≤ ((1 + 3 / (2 * (73 * 50 - 1))) * k) ^ m
          * (CB ^ 2 * ((1 + cB / 2 * Real.sqrt (L * k)) ^ 2 * Real.exp (-(2 * cB * Real.sqrt (L * k))))) := by
        gcongr
    _ = _ := by rw [mul_pow]; ring

/-! ### §8 P₂, P₃, F₁₃ and H-R₀ — `r0_73_check.py` lines 24–33 term for term — and the decrease of F₁₃ on [50, ∞) -/

/-- P_m(L) := β^m·C_B²·[(73L)^m(1 + (c_B/2)√73·L)² + (2/L^{m+1})(γ_{2m+1} + c_Bγ_{2m+2} + (c_B²/4)γ_{2m+3})(2c_B, √73·L)],
β = 1 + 3/(2(73·50 − 1)) — `r0_73_check.py` lines 24–29 (`P_relaxed(m, L, 73, 50)`), term for term. -/
def Prelax (m : ℕ) (L : ℝ) : ℝ :=
  (1 + 3 / (2 * (73 * 50 - 1))) ^ m * CB ^ 2 *
    ((73 * L) ^ m * (1 + cB / 2 * (Real.sqrt 73 * L)) ^ 2 +
      2 / L ^ (m + 1) * (gammaPoly (2 * m + 1) (2 * cB) (Real.sqrt 73 * L)
        + cB * gammaPoly (2 * m + 2) (2 * cB) (Real.sqrt 73 * L)
        + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) (Real.sqrt 73 * L)))

/-- P₂ := P_relaxed(2, L, 73, 50). -/
def P2 (L : ℝ) : ℝ := Prelax 2 L

/-- P₃ := P_relaxed(3, L, 73, 50). -/
def P3 (L : ℝ) : ℝ := Prelax 3 L

/-- F₁₃(L) := (13/8 − 2c_B√73)L + 2c_B/√73 + log((1.05P₂(L) + P₃(L))/b₁), with b₁ = b₁sym (Unit A's symbolic b₁) —
`r0_73_check.py` lines 31–33 (`Ftilde(L, 73, 50, 13/8)`), term for term. -/
def F13 (L : ℝ) : ℝ :=
  (13 / 8 - 2 * cB * Real.sqrt 73) * L + 2 * cB / Real.sqrt 73 + Real.log ((105 / 100 * P2 L + P3 L) / b1sym)

/-- **H-R₀** (displayed in 1(a); discharged in 1(b)): the one-point check of addendum A3 at L₀ = 50, R₀ = 73 —
F₁₃(50) ≤ 0 and 5/(2c_B√73 − 13/8) ≤ 50. -/
def HR0 : Prop := F13 50 ≤ 0 ∧ 5 / (2 * cB * Real.sqrt 73 - 13 / 8) ≤ 50

theorem Prelax_pos (m : ℕ) {L : ℝ} (hL : 0 < L) : 0 < Prelax m L := by
  have hc := cB_pos; have hC := CB_pos
  have h73 : 0 < Real.sqrt 73 := Real.sqrt_pos.mpr (by norm_num)
  have h1 := gammaPoly_nonneg (2 * m + 1) (a := 2 * cB) (s := Real.sqrt 73 * L) (by positivity) (by positivity)
  have h2 := gammaPoly_nonneg (2 * m + 2) (a := 2 * cB) (s := Real.sqrt 73 * L) (by positivity) (by positivity)
  have h3 := gammaPoly_nonneg (2 * m + 3) (a := 2 * cB) (s := Real.sqrt 73 * L) (by positivity) (by positivity)
  unfold Prelax; positivity

/-- the relaxation of the first term and the tail integral (item 7): with K₀ ≤ 73L, s₀ = √(LK₀) ≤ √73·L,
β^m·C_B²·(φ_m(K₀) + ∫_{K₀}^∞φ_m) ≤ e^{−2c_Bs₀}·P_m(L). -/
theorem phi_tail_le (m : ℕ) {L K₀ : ℝ} (hL : 0 < L) (hK₀ : 0 < K₀) (hK : K₀ ≤ 73 * L) :
    (1 + 3 / (2 * (73 * 50 - 1))) ^ m * CB ^ 2 * (phi m L K₀ + ∫ u in Set.Ioi K₀, phi m L u)
      ≤ Real.exp (-(2 * cB * Real.sqrt (L * K₀))) * Prelax m L := by
  have hc := cB_pos; have hC := CB_pos
  have h73 : 0 ≤ Real.sqrt 73 := Real.sqrt_nonneg _
  have hs0 : 0 ≤ Real.sqrt (L * K₀) := Real.sqrt_nonneg _
  have hsle : Real.sqrt (L * K₀) ≤ Real.sqrt 73 * L := by
    rw [show Real.sqrt 73 * L = Real.sqrt (73 * L ^ 2) by
      rw [Real.sqrt_mul (by norm_num), Real.sqrt_sq hL.le]]
    exact Real.sqrt_le_sqrt (by nlinarith)
  rw [integral_phi_Ioi m hL hK₀]
  unfold phi Prelax
  have hΓ : GammaM m (Real.sqrt (L * K₀)) ≤ GammaM m (Real.sqrt 73 * L) := GammaM_mono m hs0 hsle
  unfold GammaM at hΓ
  have hβ : 0 ≤ (1 + 3 / (2 * (73 * 50 - 1)) : ℝ) ^ m * CB ^ 2 := by positivity
  set E := Real.exp (-(2 * cB * Real.sqrt (L * K₀))) with hE
  have hE0 : 0 ≤ E := Real.exp_nonneg _
  have hA : K₀ ^ m * (1 + cB / 2 * Real.sqrt (L * K₀)) ^ 2 * E ≤ (73 * L) ^ m * (1 + cB / 2 * (Real.sqrt 73 * L)) ^ 2 * E := by
    gcongr
  have hB : 2 / L ^ (m + 1) * (E * (gammaPoly (2 * m + 1) (2 * cB) (Real.sqrt (L * K₀))
        + cB * gammaPoly (2 * m + 2) (2 * cB) (Real.sqrt (L * K₀))
        + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) (Real.sqrt (L * K₀))))
      ≤ 2 / L ^ (m + 1) * (E * (gammaPoly (2 * m + 1) (2 * cB) (Real.sqrt 73 * L)
        + cB * gammaPoly (2 * m + 2) (2 * cB) (Real.sqrt 73 * L)
        + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) (Real.sqrt 73 * L))) := by
    gcongr
  calc (1 + 3 / (2 * (73 * 50 - 1))) ^ m * CB ^ 2 * (K₀ ^ m * (1 + cB / 2 * Real.sqrt (L * K₀)) ^ 2 * E
        + 2 / L ^ (m + 1) * (E * (gammaPoly (2 * m + 1) (2 * cB) (Real.sqrt (L * K₀))
          + cB * gammaPoly (2 * m + 2) (2 * cB) (Real.sqrt (L * K₀))
          + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) (Real.sqrt (L * K₀)))))
      ≤ (1 + 3 / (2 * (73 * 50 - 1))) ^ m * CB ^ 2 * ((73 * L) ^ m * (1 + cB / 2 * (Real.sqrt 73 * L)) ^ 2 * E
        + 2 / L ^ (m + 1) * (E * (gammaPoly (2 * m + 1) (2 * cB) (Real.sqrt 73 * L)
          + cB * gammaPoly (2 * m + 2) (2 * cB) (Real.sqrt 73 * L)
          + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) (Real.sqrt 73 * L)))) :=
        mul_le_mul_of_nonneg_left (add_le_add hA hB) hβ
    _ = _ := by ring

/-- the monomial comparison P_m(50r) ≤ r^{m+2}·P_m(50) for r ≥ 1 (every monomial of P_m has degree ≤ m + 2). -/
theorem Prelax_mul_le (m : ℕ) {r : ℝ} (hr : 1 ≤ r) : Prelax m (50 * r) ≤ r ^ (m + 2) * Prelax m 50 := by
  have hc := cB_pos; have hC := CB_pos
  have hr0 : 0 < r := by linarith
  have h73 : 0 ≤ Real.sqrt 73 := Real.sqrt_nonneg _
  set s : ℝ := Real.sqrt 73 * 50 with hs
  have hs0 : 0 ≤ s := by positivity
  have hsr : Real.sqrt 73 * (50 * r) = s * r := by rw [hs]; ring
  have hβ : 0 ≤ (1 + 3 / (2 * (73 * 50 - 1)) : ℝ) ^ m * CB ^ 2 := by positivity
  have hA : (73 * (50 * r)) ^ m * (1 + cB / 2 * (s * r)) ^ 2
      ≤ r ^ (m + 2) * ((73 * 50) ^ m * (1 + cB / 2 * s) ^ 2) := by
    have h1 : 1 + cB / 2 * (s * r) ≤ r * (1 + cB / 2 * s) := by nlinarith [mul_nonneg hc.le hs0]
    calc (73 * (50 * r)) ^ m * (1 + cB / 2 * (s * r)) ^ 2
        ≤ (73 * (50 * r)) ^ m * (r * (1 + cB / 2 * s)) ^ 2 := by gcongr
      _ = r ^ (m + 2) * ((73 * 50) ^ m * (1 + cB / 2 * s) ^ 2) := by ring
  have hg : ∀ n : ℕ, n ≤ 2 * m + 3 →
      gammaPoly n (2 * cB) (s * r) ≤ r ^ (2 * m + 3) * gammaPoly n (2 * cB) s := by
    intro n hn
    have h0 := gammaPoly_nonneg n (a := 2 * cB) (by positivity) hs0
    calc gammaPoly n (2 * cB) (s * r) ≤ r ^ n * gammaPoly n (2 * cB) s :=
          gammaPoly_mul_le n (by positivity) hs0 hr
      _ ≤ r ^ (2 * m + 3) * gammaPoly n (2 * cB) s := by gcongr
  have hB : 2 / (50 * r) ^ (m + 1) * (gammaPoly (2 * m + 1) (2 * cB) (s * r)
        + cB * gammaPoly (2 * m + 2) (2 * cB) (s * r) + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) (s * r))
      ≤ r ^ (m + 2) * (2 / 50 ^ (m + 1) * (gammaPoly (2 * m + 1) (2 * cB) s
        + cB * gammaPoly (2 * m + 2) (2 * cB) s + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) s)) := by
    have hg1 := hg (2 * m + 1) (by omega)
    have hg2 := hg (2 * m + 2) (by omega)
    have hg3 := hg (2 * m + 3) (by omega)
    have hc2 : 0 ≤ cB ^ 2 / 4 := by positivity
    have hsum : gammaPoly (2 * m + 1) (2 * cB) (s * r) + cB * gammaPoly (2 * m + 2) (2 * cB) (s * r)
          + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) (s * r)
        ≤ r ^ (2 * m + 3) * (gammaPoly (2 * m + 1) (2 * cB) s + cB * gammaPoly (2 * m + 2) (2 * cB) s
          + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) s) := by
      nlinarith [mul_le_mul_of_nonneg_left hg2 hc.le, mul_le_mul_of_nonneg_left hg3 hc2]
    have hpos : 0 ≤ 2 / (50 * r) ^ (m + 1) := by positivity
    calc 2 / (50 * r) ^ (m + 1) * (gammaPoly (2 * m + 1) (2 * cB) (s * r)
          + cB * gammaPoly (2 * m + 2) (2 * cB) (s * r) + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) (s * r))
        ≤ 2 / (50 * r) ^ (m + 1) * (r ^ (2 * m + 3) * (gammaPoly (2 * m + 1) (2 * cB) s
          + cB * gammaPoly (2 * m + 2) (2 * cB) s + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) s)) :=
          mul_le_mul_of_nonneg_left hsum hpos
      _ = r ^ (m + 2) * (2 / 50 ^ (m + 1) * (gammaPoly (2 * m + 1) (2 * cB) s
          + cB * gammaPoly (2 * m + 2) (2 * cB) s + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) s)) := by
          rw [mul_pow]; field_simp; ring
  unfold Prelax
  rw [hsr]
  calc (1 + 3 / (2 * (73 * 50 - 1))) ^ m * CB ^ 2 * ((73 * (50 * r)) ^ m * (1 + cB / 2 * (s * r)) ^ 2
        + 2 / (50 * r) ^ (m + 1) * (gammaPoly (2 * m + 1) (2 * cB) (s * r)
          + cB * gammaPoly (2 * m + 2) (2 * cB) (s * r) + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) (s * r)))
      ≤ (1 + 3 / (2 * (73 * 50 - 1))) ^ m * CB ^ 2 * (r ^ (m + 2) * ((73 * 50) ^ m * (1 + cB / 2 * s) ^ 2)
        + r ^ (m + 2) * (2 / 50 ^ (m + 1) * (gammaPoly (2 * m + 1) (2 * cB) s
          + cB * gammaPoly (2 * m + 2) (2 * cB) s + cB ^ 2 / 4 * gammaPoly (2 * m + 3) (2 * cB) s))) :=
        mul_le_mul_of_nonneg_left (add_le_add hA hB) hβ
    _ = _ := by ring

/-- 2c_B√73 − 13/8 > 0 (c_B ≥ 0.1429, √73 ≥ 8). -/
theorem slope_pos : 0 < 2 * cB * Real.sqrt 73 - 13 / 8 := by
  have hc := cB_ge
  have h8 : (8 : ℝ) ≤ Real.sqrt 73 := by
    rw [Real.le_sqrt (by norm_num) (by norm_num)]; norm_num
  nlinarith

/-- **the decrease of F₁₃ on [50, ∞) from the one-point check** (note §6 "The relaxation …"; check-O §7.3 (i)): for
L = 50r, r ≥ 1, Q(L) ≤ r⁵Q(50) (every monomial of 1.05P₂ + P₃ has degree ≤ 5), so F₁₃(L) − F₁₃(50) ≤ −c(L − 50) + 5log r
≤ (L − 50)(1/10 − c) ≤ 0 with c := 2c_B√73 − 13/8 ≥ 1/10 (the second conjunct of H-R₀) — the integrated form of the
note's (log P)′ ≤ 5/L. -/
theorem F13_le_F13_50 (hR0 : HR0) {L : ℝ} (hL : 50 ≤ L) : F13 L ≤ F13 50 := by
  have hb4 := four_le_b1sym
  have hb0 : 0 < b1sym := by linarith
  have hslope := slope_pos
  have hc10 : 1 / 10 ≤ 2 * cB * Real.sqrt 73 - 13 / 8 := by
    have := hR0.2
    rw [div_le_iff₀ hslope] at this
    linarith
  set r := L / 50 with hr
  have hr1 : 1 ≤ r := by rw [hr, le_div_iff₀ (by norm_num)]; linarith
  have hLr : L = 50 * r := by rw [hr]; ring
  have hlogr : Real.log r ≤ r - 1 := Real.log_le_sub_one_of_pos (by linarith)
  have hQ50 : 0 < 105 / 100 * P2 50 + P3 50 := by
    have := Prelax_pos 2 (L := 50) (by norm_num); have := Prelax_pos 3 (L := 50) (by norm_num)
    unfold P2 P3; positivity
  have hQL : 0 < 105 / 100 * P2 L + P3 L := by
    have := Prelax_pos 2 (L := L) (by linarith); have := Prelax_pos 3 (L := L) (by linarith)
    unfold P2 P3; positivity
  have hQ : 105 / 100 * P2 L + P3 L ≤ r ^ 5 * (105 / 100 * P2 50 + P3 50) := by
    have h2 : P2 L ≤ r ^ 5 * P2 50 := by
      unfold P2
      rw [hLr]
      calc Prelax 2 (50 * r) ≤ r ^ (2 + 2) * Prelax 2 50 := Prelax_mul_le 2 hr1
        _ ≤ r ^ 5 * Prelax 2 50 :=
          mul_le_mul_of_nonneg_right (pow_le_pow_right₀ hr1 (by norm_num))
            (Prelax_pos 2 (L := 50) (by norm_num)).le
    have h3 : P3 L ≤ r ^ 5 * P3 50 := by
      unfold P3
      rw [hLr]
      exact Prelax_mul_le 3 hr1
    nlinarith
  have hlog : Real.log ((105 / 100 * P2 L + P3 L) / b1sym)
      ≤ Real.log ((105 / 100 * P2 50 + P3 50) / b1sym) + 5 * Real.log r := by
    have : Real.log ((105 / 100 * P2 L + P3 L) / b1sym) ≤ Real.log (r ^ 5 * ((105 / 100 * P2 50 + P3 50) / b1sym)) := by
      apply Real.log_le_log (by positivity)
      rw [mul_div_assoc']
      exact div_le_div_of_nonneg_right hQ hb0.le
    rw [Real.log_mul (by positivity) (by positivity), Real.log_pow] at this
    push_cast at this
    linarith
  unfold F13
  have h5 : 5 * Real.log r ≤ (2 * cB * Real.sqrt 73 - 13 / 8) * (L - 50) := by
    have : 5 * Real.log r ≤ 5 * (r - 1) := by linarith
    have e : 5 * (r - 1) = (L - 50) / 10 := by rw [hr]; ring
    nlinarith
  nlinarith

/-! ### §9 Clause 5 modulo H-R₀: the two conjuncts of `Hout` at R = 73L, and the assembly with H-out replaced by H-R₀ -/

/-- the shell weight of 1(a): the pointwise bound of a point in shell k = ⌊u⌋₊ is ≤ (k + 3/2)²e^{L/2}G(Lk)²
(u + 1/2 < k + 3/2; G antitone). -/
theorem shell_weight_le {L u : ℝ} (hL : 0 < L) (hu : 0 ≤ u) :
    (u + 1 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * u) ^ 2
      ≤ ((⌊u⌋₊ : ℝ) + 3 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * (⌊u⌋₊ : ℝ)) ^ 2 := by
  have hk1 : u < (⌊u⌋₊ : ℝ) + 1 := Nat.lt_floor_add_one u
  have hk0 : (⌊u⌋₊ : ℝ) ≤ u := Nat.floor_le hu
  have hG : Gmaj (L * u) ≤ Gmaj (L * (⌊u⌋₊ : ℝ)) := Gmaj_antitone (by gcongr)
  have hG0 := Gmaj_nonneg (L * u)
  have h : u + 1 / 2 ≤ (⌊u⌋₊ : ℝ) + 3 / 2 := by linarith
  calc (u + 1 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * u) ^ 2
      ≤ ((⌊u⌋₊ : ℝ) + 3 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * u) ^ 2 :=
        mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (by positivity) h 2)
          (Real.exp_nonneg _)) (by positivity)
    _ ≤ ((⌊u⌋₊ : ℝ) + 3 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * (⌊u⌋₊ : ℝ)) ^ 2 := by gcongr

/-- the shell series of 1(a) is bounded by e^{F₁₃(L) − L}, uniformly in K: the absorption spent once, the two sums
Σ₂, Σ₃ through φ₂, φ₃, the tail integrals, and the relaxations (note §6 (b) "The sums" and "The relaxation …",
addendum A3's chain S_Z ≤ e^{2c_B/√73}e^{(13/8 − 2c_B√73)L}(1.05P₂ + P₃)/b₁ · e^{−L}). -/
theorem shell_series_le {C₁ t L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hL : 50 ≤ L)
    (hL8 : 8 * (Real.log (Real.log (3 + t)) + Real.log (2 * b1sym * C₁)) ≤ L) (K : ℕ) :
    ∑ k ∈ Finset.Ico ⌊73 * L⌋₊ K, 2 * C₁ * Real.log (7 / 2 + t + k)
        * (((k : ℝ) + 3 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * k) ^ 2)
      ≤ Real.exp (F13 L - L) := by
  have hc := cB_pos; have hC0 := CB_pos
  have hb4 := four_le_b1sym
  have hb0 : 0 < b1sym := by linarith
  have hL0 : 0 < L := by linarith
  have hC0' : 0 ≤ C₁ := by linarith
  obtain ⟨hab1, hab2, hlog105⟩ := absorb_once hC ht hL8
  set K₀ := ⌊73 * L⌋₊ with hK₀
  have hK₀le : (K₀ : ℝ) ≤ 73 * L := Nat.floor_le (by positivity)
  have hK₀ge : 73 * L - 1 ≤ K₀ := by linarith [Nat.lt_floor_add_one (73 * L)]
  have hK₀3650 : 3650 ≤ K₀ := Nat.le_floor (by push_cast; linarith)
  have hK₀pos : 0 < K₀ := by omega
  have hK₀r : (3650 : ℝ) ≤ K₀ := by exact_mod_cast hK₀3650
  have hK₀r0 : (0 : ℝ) < K₀ := by linarith
  set A := Real.exp (L / 8) / b1sym with hA
  have hA0 : 0 ≤ A := by positivity
  set β : ℝ := 1 + 3 / (2 * (73 * 50 - 1)) with hβ
  have hβ0 : 0 ≤ β := by positivity
  have hℓ0 : 0 ≤ Real.log (7 / 2 + t) := Real.log_nonneg (by linarith)
  -- c_B√(LK₀) ≥ 6 (s₀ ≥ √(50·3650) ≥ 427, c_B ≥ 0.1429)
  have hs427 : (427 : ℝ) ≤ Real.sqrt (L * K₀) := by
    rw [Real.le_sqrt (by norm_num) (by positivity)]; nlinarith
  have hm2 : 2 * (2 : ℕ) ≤ cB * Real.sqrt (L * K₀) := by
    push_cast; nlinarith [cB_ge]
  have hm3 : 2 * (3 : ℕ) ≤ cB * Real.sqrt (L * K₀) := by
    push_cast; nlinarith [cB_ge]
  -- per-term bound
  have hterm : ∀ k ∈ Finset.Ico K₀ K,
      2 * C₁ * Real.log (7 / 2 + t + k) * (((k : ℝ) + 3 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * k) ^ 2)
        ≤ Real.exp (L / 2) * A * (105 / 100 * (β ^ 2 * CB ^ 2 * phi 2 L k) + β ^ 3 * CB ^ 2 * phi 3 L k) := by
    intro k hk
    have hkK₀ : K₀ ≤ k := (Finset.mem_Ico.mp hk).1
    have hkr : (3649 : ℝ) ≤ k := by
      have : (K₀ : ℝ) ≤ k := by exact_mod_cast hkK₀
      linarith
    have hk0 : (0 : ℝ) ≤ k := by linarith
    have hG0 := Gmaj_nonneg (L * k)
    -- log(7/2 + t + k) ≤ log(7/2 + t) + k
    have hlogk : Real.log (7 / 2 + t + k) ≤ Real.log (7 / 2 + t) + k := by
      have h := Real.log_le_sub_one_of_pos (show 0 < (7 / 2 + t + k) / (7 / 2 + t) by positivity)
      rw [Real.log_div (by linarith) (by linarith)] at h
      have : (7 / 2 + t + k) / (7 / 2 + t) - 1 ≤ k := by
        rw [div_sub_one (by linarith), div_le_iff₀ (by linarith)]; nlinarith
      linarith
    have hlog0 : 0 ≤ Real.log (7 / 2 + t + k) := Real.log_nonneg (by linarith)
    have h2 := pow_mul_Gmaj_sq_le 2 hL0 hkr
    have h3 := pow_mul_Gmaj_sq_le 3 hL0 hkr
    have hφ2 := phi_nonneg 2 (L := L) hk0
    have hφ3 := phi_nonneg 3 (L := L) hk0
    -- 2C₁ log(7/2 + t) ≤ 1.05 A, 2C₁ ≤ A
    have hc1 : 2 * C₁ * Real.log (7 / 2 + t) ≤ 105 / 100 * A := by nlinarith
    have hc2 : 2 * C₁ ≤ A := hab2
    calc 2 * C₁ * Real.log (7 / 2 + t + k) * (((k : ℝ) + 3 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * k) ^ 2)
        ≤ 2 * C₁ * (Real.log (7 / 2 + t) + k) * (((k : ℝ) + 3 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * k) ^ 2) := by
          gcongr
      _ = Real.exp (L / 2) * ((2 * C₁ * Real.log (7 / 2 + t)) * (((k : ℝ) + 3 / 2) ^ 2 * Gmaj (L * k) ^ 2)
          + (2 * C₁) * (k * ((k : ℝ) + 3 / 2) ^ 2 * Gmaj (L * k) ^ 2)) := by ring
      _ ≤ Real.exp (L / 2) * ((105 / 100 * A) * (((k : ℝ) + 3 / 2) ^ 2 * Gmaj (L * k) ^ 2)
          + A * (((k : ℝ) + 3 / 2) ^ 3 * Gmaj (L * k) ^ 2)) := by
          have hk3 : k * ((k : ℝ) + 3 / 2) ^ 2 * Gmaj (L * k) ^ 2 ≤ ((k : ℝ) + 3 / 2) ^ 3 * Gmaj (L * k) ^ 2 := by
            have : k * ((k : ℝ) + 3 / 2) ^ 2 ≤ ((k : ℝ) + 3 / 2) ^ 3 := by nlinarith
            exact mul_le_mul_of_nonneg_right this (by positivity)
          refine mul_le_mul_of_nonneg_left (add_le_add ?_ ?_) (Real.exp_nonneg _)
          · exact mul_le_mul_of_nonneg_right hc1 (by positivity)
          · exact mul_le_mul hc2 hk3 (by positivity) hA0
      _ ≤ Real.exp (L / 2) * ((105 / 100 * A) * (β ^ 2 * CB ^ 2 * phi 2 L k)
          + A * (β ^ 3 * CB ^ 2 * phi 3 L k)) := by
          gcongr
      _ = _ := by ring
  -- the sum
  have hsum2 := sum_phi_le 2 hL0 hK₀pos hm2 K
  have hsum3 := sum_phi_le 3 hL0 hK₀pos hm3 K
  have htail2 := phi_tail_le 2 hL0 hK₀r0 hK₀le
  have htail3 := phi_tail_le 3 hL0 hK₀r0 hK₀le
  have hexp := exp_neg_s0_le (L := L) (K₀ := K₀) (by linarith) hK₀ge
  set E := Real.exp (-(2 * cB * Real.sqrt (L * K₀))) with hE
  have hE0 : 0 ≤ E := Real.exp_nonneg _
  have hP2 := Prelax_pos 2 hL0
  have hP3 := Prelax_pos 3 hL0
  have hQ : 0 < 105 / 100 * P2 L + P3 L := by unfold P2 P3; positivity
  calc ∑ k ∈ Finset.Ico K₀ K, 2 * C₁ * Real.log (7 / 2 + t + k)
          * (((k : ℝ) + 3 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * k) ^ 2)
      ≤ ∑ k ∈ Finset.Ico K₀ K, Real.exp (L / 2) * A
          * (105 / 100 * (β ^ 2 * CB ^ 2 * phi 2 L k) + β ^ 3 * CB ^ 2 * phi 3 L k) :=
        Finset.sum_le_sum hterm
    _ = Real.exp (L / 2) * A * (105 / 100 * (β ^ 2 * CB ^ 2 * ∑ k ∈ Finset.Ico K₀ K, phi 2 L k)
          + β ^ 3 * CB ^ 2 * ∑ k ∈ Finset.Ico K₀ K, phi 3 L k) := by
        simp only [mul_add, Finset.mul_sum, Finset.sum_add_distrib]
    _ ≤ Real.exp (L / 2) * A * (105 / 100 * (β ^ 2 * CB ^ 2 * (phi 2 L K₀ + ∫ u in Set.Ioi (K₀ : ℝ), phi 2 L u))
          + β ^ 3 * CB ^ 2 * (phi 3 L K₀ + ∫ u in Set.Ioi (K₀ : ℝ), phi 3 L u)) := by
        gcongr
    _ ≤ Real.exp (L / 2) * A * (105 / 100 * (E * Prelax 2 L) + E * Prelax 3 L) := by
        gcongr
    _ = Real.exp (L / 2) * (Real.exp (L / 8) / b1sym) * E * (105 / 100 * P2 L + P3 L) := by
        unfold P2 P3; rw [hA]; ring
    _ ≤ Real.exp (L / 2) * (Real.exp (L / 8) / b1sym)
          * (Real.exp (2 * cB / Real.sqrt 73) * Real.exp (-(2 * cB * Real.sqrt 73 * L)))
          * (105 / 100 * P2 L + P3 L) := by
        gcongr
    _ = Real.exp (L / 2) * Real.exp (L / 8) * Real.exp (2 * cB / Real.sqrt 73)
          * Real.exp (-(2 * cB * Real.sqrt 73 * L)) * ((105 / 100 * P2 L + P3 L) / b1sym) := by ring
    _ = Real.exp (L / 2 + L / 8 + 2 * cB / Real.sqrt 73 + -(2 * cB * Real.sqrt 73 * L))
          * ((105 / 100 * P2 L + P3 L) / b1sym) := by
        rw [← Real.exp_add, ← Real.exp_add, ← Real.exp_add]
    _ = Real.exp (F13 L - L) := by
        unfold F13
        rw [show (13 / 8 - 2 * cB * Real.sqrt 73) * L + 2 * cB / Real.sqrt 73
            + Real.log ((105 / 100 * P2 L + P3 L) / b1sym) - L
            = (L / 2 + L / 8 + 2 * cB / Real.sqrt 73 + -(2 * cB * Real.sqrt 73 * L))
              + Real.log ((105 / 100 * P2 L + P3 L) / b1sym) by ring,
          Real.exp_add (L / 2 + L / 8 + 2 * cB / Real.sqrt 73 + -(2 * cB * Real.sqrt 73 * L)),
          Real.exp_log (by positivity)]

/-- **Theorem M2, clause 5, modulo H-R₀** (separation note §6, addendum A3), library form over raw data — exactly
the two conjuncts of the trusted `Hout` at R = 73L: for any carrier of 𝒞(C₁) inside the strip, C₁ ≥ 1, t ≥ 3,
L ≥ 50, 8(log log(3 + t) + log(2b₁C₁)) ≤ L (implied by the assembly's L-hypothesis) and the one-point check H-R₀,
the out-window sum beyond 73L is absolutely convergent and its norm is at most e^{−L}. -/
theorem clause5_out_window {C₁ t L : ℝ} (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hstrip : ∀ ρ ∈ carrier, 0 ≤ ρ.re ∧ ρ.re ≤ 1)
    (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hL : 50 ≤ L)
    (hL8 : 8 * (Real.log (Real.log (3 + t)) + Real.log (2 * b1sym * C₁)) ≤ L) (hR0 : HR0) :
    Summable (fun ρ : ↥(carrier ∩ {ρ | 73 * L < |ρ.im - t|}) => ‖wsum mult (ftest t L) ρ‖) ∧
      ‖∑' ρ : ↥(carrier ∩ {ρ | 73 * L < |ρ.im - t|}), wsum mult (ftest t L) ρ‖ ≤ Real.exp (-L) := by
  have hL0 : 0 < L := by linarith
  have hC0 : 0 ≤ C₁ := by linarith
  have hF := F13_le_F13_50 hR0 hL
  have hc : Real.exp (F13 L - L) ≤ Real.exp (-L) := by
    apply Real.exp_le_exp.mpr; linarith [hR0.1]
  obtain ⟨hs, hle⟩ := out_window_norm_le (R := 73 * L) carrier mult hfin hcount hC0 (by linarith) (ftest t L)
    (fun k => ((k : ℝ) + 3 / 2) ^ 2 * Real.exp (L / 2) * Gmaj (L * k) ^ 2)
    (fun k => by have := Gmaj_nonneg (L * k); positivity)
    (fun ρ hρ => (norm_wsum_le_strip hL0 (hstrip ρ hρ.1)).trans
      (mul_le_mul_of_nonneg_left (shell_weight_le hL0 (abs_nonneg _)) (Nat.cast_nonneg _)))
    (Real.exp (F13 L - L)) (fun K => shell_series_le hC ht hL hL8 K)
  exact ⟨hs, hle.trans hc⟩

/-- the assembly's L-hypothesis implies clause 5's: 4/δ ≥ 8, 2log(1/δ) ≥ 0, and both remaining summands are ≥ 0. -/
theorem hL8_of_hL2 {C₁ t δ L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * b1sym * C₁)) ≤ L) :
    8 * (Real.log (Real.log (3 + t)) + Real.log (2 * b1sym * C₁)) ≤ L := by
  have hb4 := four_le_b1sym
  have hlog6 : Real.log 6 ≤ Real.log (3 + t) := Real.log_le_log (by norm_num) (by linarith)
  have h53 := five_thirds_le_log_six
  have hll : 0 ≤ Real.log (Real.log (3 + t)) := Real.log_nonneg (by linarith)
  have hlb : 0 ≤ Real.log (2 * b1sym * C₁) := Real.log_nonneg (by nlinarith)
  have hlδ : 0 ≤ Real.log (1 / δ) := Real.log_nonneg (by rw [le_div_iff₀ hδ0]; linarith)
  have h8 : (8 : ℝ) ≤ 4 / δ := by rw [le_div_iff₀ hδ0]; linarith
  have hS : 0 ≤ Real.log (Real.log (3 + t)) + Real.log (2 * b1sym * C₁) := by linarith
  calc 8 * (Real.log (Real.log (3 + t)) + Real.log (2 * b1sym * C₁))
      ≤ 4 / δ * (Real.log (Real.log (3 + t)) + Real.log (2 * b1sym * C₁)) := by gcongr
    _ ≤ 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * b1sym * C₁)) := by
        gcongr; linarith
    _ ≤ L := hL2

/-- **Theorem M2, clause 6, with clause 5 proved modulo H-R₀** (separation note §7.1 with the addendum's hypotheses),
library form over raw data — modulo the displayed H-B‴, H-edge and H-R₀; the two `Hout` hypotheses of
`clause6_assembly_b` are derived by `clause5_out_window` (for Z and for Z′; the strip of each is consumed). -/
theorem clause6_assembly_c {C₁ t δ L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
    (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * b1sym * C₁)) ≤ L)
    (hRstar : Rstar t δ L)
    (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hstrip : ∀ ρ ∈ carrier, 0 ≤ ρ.re ∧ ρ.re ≤ 1)
    (carrier' : Set ℂ) (mult' : ℂ → ℕ)
    (hfin' : ∀ T₁ T₂ : ℝ, (carrier' ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount' : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier' ∩ {ρ | |ρ.im - x| ≤ 1}, mult' ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hstrip' : ∀ ρ ∈ carrier', 0 ≤ ρ.re ∧ ρ.re ≤ 1)
    (hZorb : orbit t δ ⊆ carrier) (hZmult : ∀ ρ ∈ orbit t δ, mult ρ = 1)
    (hZ : ∀ ρ ∈ carrier, |ρ.im - t| ≤ 73 * L → ρ ∉ orbit t δ → ρ.re = 1 / 2)
    (hZ' : ∀ ρ ∈ carrier', |ρ.im - t| ≤ 73 * L → ρ.re = 1 / 2)
    (hB3 : HB3) (hedge : Hedge) (hR0 : HR0) :
    δ ^ 2 * Real.exp (δ * L / 2)
        ≤ ‖(∑' ρ : carrier, wsum mult (ftest t L) ρ) - ∑' ρ : carrier', wsum mult' (ftest t L) ρ‖ ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) := by
  have hL50 : 50 ≤ L := by
    have : (50 : ℝ) ≤ 25 / δ := by rw [le_div_iff₀ hδ0]; linarith
    linarith
  have hL8 := hL8_of_hL2 hC ht hδ0 hδ hL2
  exact clause6_assembly_b hC ht hδ0 hδ hL1 hL2 hRstar carrier mult hfin hcount carrier' mult' hfin' hcount'
    hZorb hZmult hZ hZ' hB3 hedge
    (clause5_out_window carrier mult hfin hcount hstrip hC ht hL50 hL8 hR0)
    (clause5_out_window carrier' mult' hfin' hcount' hstrip' hC ht hL50 hL8 hR0)

end

end Separation
end Zeta23
