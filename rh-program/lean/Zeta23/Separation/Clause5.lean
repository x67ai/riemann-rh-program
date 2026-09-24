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

end

end Separation
end Zeta23
