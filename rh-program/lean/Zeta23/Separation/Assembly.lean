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
Zeta23/Separation/Assembly.lean — the clause-6 assembly of Theorem M2 (the separation note
rh-program/results/c2-m2/separation-note.md §0.2, §4, §7.1 and the addendum A1–A3 of 2026-09-17), M4 (iii) (contract
rh-program/results/c2-m2/followups/PRICING.md §1(b) candidate (iii); build record rh-program/results/c2-m4/BUILD-NOTES-iii.md).

WHAT IS PROVED, modulo WHAT.  Over any carrier with multiplicities, locally finite in the ordinate, with the local count of
𝒞(C₁): for t ≥ 3, 0 < δ ≤ 1/2, L ≥ 25/δ, L ≥ (4/δ)(log log(3 + t) + 2log(1/δ) + log(2·(87/10)·C₁)) and (R*), for Z with the
orbit 1/2 ± δ ± it (multiplicity one) and otherwise on-line within |Im ρ − t| ≤ 73L, and Z′ on-line there,
    ‖W_Z(f) − W_{Z′}(f)‖ ≥ δ²e^{δL/2} ≥ 1,   f = f_{t,L},
MODULO the DISPLAYED H-b₁, H-B‴ (clause 4, from Clause4.lean), H-edge (clause 2's lower bound with κ₋ = 148088/100000) and
H-out for Z and Z′ (clause 5, displayed whole: absolute convergence of the out-window sum beyond 73L and its bound e^{−L}).
Label: "kernel-checked modulo H-edge, H-b₁, H-B‴, H-out" — never "Theorem M2 is formalized".

Proved here: the edge function c(λ) = ∫B cosh(λv) equals B̂(±iλ) (evenness of B); the orbit's four-point accounting
(each point of the pair at +t contributes −δ²c(δL)²; note §0.2); clause 1's explicit bound on each reflected point,
‖m h_f(γ) conj(h_f(conj γ))‖ ≤ (4t² + δ²)e^{δL}G(2tL)², from Lemma G's complex form (note §4); (R*) exponentiated:
2(4t² + δ²)e^{δL}G(2tL)² ≤ 2.7δ²e^{δL/2} (addendum A1); the decomposition W = Σ_{in-window off-line} + N + O of the tsum
over the carrier (a genuine partition — the reflected pair lies in the first or in the third part according to 2t ≤ 73L,
referee O's MINOR (d)); H-edge to the margin c(λ)² ≥ 1.88e^{λ/2} for λ ≥ 25 (clause 3 with the slack the addendum A2
uses); the L-hypothesis absorptions N ≤ (6/100)δ²e^{δL/2}, 2e^{−L} ≤ (1/1000)δ²e^{δL/2}, δ²e^{δL/2} ≥ 1; the chain
Re(W_{Z′} − W_Z) ≥ 2δ²c² − 2.7δ²e^{δL/2} − N − 2e^{−L} ≥ δ²e^{δL/2} (addendum A1's displayed inequality, one noise term, D8).
-/
import Zeta23.Separation.Clause4

namespace Zeta23
namespace Separation

open Complex MeasureTheory
open scoped ContDiff

noncomputable section

/-! ### §1 The trusted vocabulary, character for character (namespace `Zeta23.Separation`) -/

/-- the orbit {1/2 ± δ ± it} of the defect (γ_ρ = ±t ± iδ; note §0.2), as points ρ = β + iτ. -/
def orbit (t δ : ℝ) : Set ℂ :=
  {(⟨1 / 2 + δ, t⟩ : ℂ), (⟨1 / 2 - δ, t⟩ : ℂ), (⟨1 / 2 + δ, -t⟩ : ℂ), (⟨1 / 2 - δ, -t⟩ : ℂ)}

/-- the edge function c(λ) := ∫ B(v)·cosh(λv) dv (note §0.1). -/
def edge (l : ℝ) : ℝ := ∫ v, B v * Real.cosh (l * v)

/-- **H-edge** (displayed): clause 2's lower bound, c(λ) ≥ exp(λ/2 − √λ − (3/4)·log λ + κ₋) for λ ≥ 25,
κ₋ = 148088/100000 (note §3.2). -/
def Hedge : Prop :=
  ∀ l : ℝ, 25 ≤ l → Real.exp (l / 2 - Real.sqrt l - 3 / 4 * Real.log l + 148088 / 100000) ≤ edge l

/-- clause 1′, the reflection condition (R*) (note addendum A1), with s = √(2tL) and 1.35 = 27/20. -/
def Rstar (t δ L : ℝ) : Prop :=
  δ * L / 2 + Real.log ((4 * t ^ 2 + δ ^ 2) * CB ^ 2 / (27 / 20 * δ ^ 2))
    ≤ 2 * cB * Real.sqrt (2 * t * L) - 2 * Real.log (1 + cB / 2 * Real.sqrt (2 * t * L))

/-- the Weil summand m_ρ h_f(γ_ρ) conj(h_f(conj γ_ρ)) for raw data (character for character `Zeta23.ZeroConfig.Wsummand`
and the trusted `Separation.SepConfig.Wsummand`). -/
def wsum (mult : ℂ → ℕ) (f : ℝ → ℂ) (ρ : ℂ) : ℂ :=
  (mult ρ : ℂ) * paperFT f (gammaOf ρ) * (starRingEnd ℂ) (paperFT f ((starRingEnd ℂ) (gammaOf ρ)))

/-- Lemma G's majorant G(x) = C_B(1 + (c_B/2)√x)e^{−c_B√x}. -/
def Gmaj (x : ℝ) : ℝ := CB * (1 + cB / 2 * Real.sqrt x) * Real.exp (-(cB * Real.sqrt x))

/-! ### §2 The edge function is B̂(±iλ) -/

theorem B_even (v : ℝ) : B (-v) = B v := by
  simp only [B, Braw, abs_neg, neg_sq]

theorem hasCompactSupport_B : HasCompactSupport B :=
  hasCompactSupport_of_support_subset_abs (Λ := 1 / 2) fun u hu => by
    by_contra h
    exact hu (B_eq_zero_of_half_le (not_le.mp h).le)

theorem B_continuous : Continuous B := (B_contDiff (n := 0)).continuous

theorem integrable_B_mul_exp (l : ℝ) : Integrable (fun u => B u * Real.exp (l * u)) :=
  (B_continuous.mul (by fun_prop)).integrable_of_hasCompactSupport hasCompactSupport_B.mul_right

/-- evenness: ∫ B(u)e^{lu} du = ∫ B(u)e^{−lu} du. -/
theorem integral_B_exp_symm (l : ℝ) :
    ∫ u, B u * Real.exp (l * u) = ∫ u, B u * Real.exp (-(l * u)) := by
  have h := Measure.integral_comp_mul_left (fun u => B u * Real.exp (-(l * u))) (-1)
  simp only [neg_mul, one_mul, mul_neg, neg_neg, inv_neg, inv_one, abs_neg, abs_one, one_smul, B_even] at h
  exact h

/-- c(λ) = ∫ B(u) e^{−λu} du. -/
theorem edge_eq (l : ℝ) : edge l = ∫ u, B u * Real.exp (-(l * u)) := by
  unfold edge
  have : (fun v => B v * Real.cosh (l * v)) = fun v => (1 / 2 : ℝ) * (B v * Real.exp (l * v) + B v * Real.exp (-(l * v))) := by
    funext v; rw [Real.cosh_eq]; ring
  rw [this, integral_const_mul, integral_add (integrable_B_mul_exp l) (by simpa using integrable_B_mul_exp (-l)),
    integral_B_exp_symm]
  ring

theorem edge_nonneg (l : ℝ) : 0 ≤ edge l := by
  rw [edge_eq]
  exact integral_nonneg fun u => mul_nonneg (B_nonneg u) (Real.exp_pos _).le

/-- B̂(iλ) = c(λ). -/
theorem paperFT_Bc_I_mul (l : ℝ) : paperFT (fun v => (B v : ℂ)) (I * l) = (edge l : ℂ) := by
  rw [edge_eq, paperFT_def]
  have hint : Integrable (fun u => B u * Real.exp (-(l * u))) := by
    simpa only [neg_mul] using integrable_B_mul_exp (-l)
  have e : (fun u : ℝ => (B u : ℂ) * cexp (I * (I * l) * u)) = fun u => ((B u * Real.exp (-(l * u)) : ℝ) : ℂ) := by
    funext u
    rw [show I * (I * (l : ℂ)) * (u : ℂ) = ((-(l * u) : ℝ) : ℂ) by
        push_cast; linear_combination (l * u : ℂ) * Complex.I_sq, ← Complex.ofReal_exp]
    push_cast; ring
  rw [e]
  simpa only [Complex.ofRealCLM_apply] using Complex.ofRealCLM.integral_comp_comm hint

/-- B̂(−iλ) = c(λ). -/
theorem paperFT_Bc_neg_I_mul (l : ℝ) : paperFT (fun v => (B v : ℂ)) (-(I * l)) = (edge l : ℂ) := by
  rw [edge_eq, ← integral_B_exp_symm, paperFT_def]
  have hint : Integrable (fun u => B u * Real.exp (l * u)) := integrable_B_mul_exp l
  have e : (fun u : ℝ => (B u : ℂ) * cexp (I * -(I * l) * u)) = fun u => ((B u * Real.exp (l * u) : ℝ) : ℂ) := by
    funext u
    rw [show I * -(I * (l : ℂ)) * (u : ℂ) = ((l * u : ℝ) : ℂ) by
        push_cast; linear_combination (-(l * u : ℂ)) * Complex.I_sq, ← Complex.ofReal_exp]
    push_cast; ring
  rw [e]
  simpa only [Complex.ofRealCLM_apply] using Complex.ofRealCLM.integral_comp_comm hint

theorem edge_neg (l : ℝ) : edge (-l) = edge l := by
  simp only [edge, neg_mul, Real.cosh_neg]

theorem Gmaj_nonneg (x : ℝ) : 0 ≤ Gmaj x := by
  unfold Gmaj; have := CB_pos; have := cB_pos; positivity

/-! ### §3 The orbit: γ-coordinates, the main term at +t, the reflected pair at −t, (R*) exponentiated -/

theorem gammaOf_mk (a b : ℝ) : gammaOf ⟨a, b⟩ = (b : ℂ) - ((a - 1 / 2 : ℝ) : ℂ) * I := by
  unfold gammaOf
  rw [div_eq_iff Complex.I_ne_zero]
  apply Complex.ext <;> simp

/-- h_f(t − si) = −si·c(sL). -/
theorem paperFT_ftest_sub_I {t L s : ℝ} (hL : 0 < L) :
    paperFT (ftest t L) ((t : ℂ) - (s : ℂ) * I) = -((s : ℂ) * I) * (edge (s * L) : ℂ) := by
  rw [paperFT_ftest hL]
  congr 1
  · ring
  · rw [← paperFT_Bc_neg_I_mul]; congr 1; push_cast; ring

/-- h_f(t + si) = si·c(sL). -/
theorem paperFT_ftest_add_I {t L s : ℝ} (hL : 0 < L) :
    paperFT (ftest t L) ((t : ℂ) + (s : ℂ) * I) = ((s : ℂ) * I) * (edge (s * L) : ℂ) := by
  rw [paperFT_ftest hL]
  congr 1
  · ring
  · rw [← paperFT_Bc_I_mul]; congr 1; push_cast; ring

/-- **the main term** (note §0.2): a point of multiplicity one with γ_ρ = t − si contributes −s²c(sL)². -/
theorem wsum_of_gammaOf_eq {mult : ℂ → ℕ} {t L s : ℝ} (hL : 0 < L) {ρ : ℂ} (hm : mult ρ = 1)
    (hγ : gammaOf ρ = (t : ℂ) - (s : ℂ) * I) :
    wsum mult (ftest t L) ρ = -((s ^ 2 * edge (s * L) ^ 2 : ℝ) : ℂ) := by
  have hconj : (starRingEnd ℂ) ((t : ℂ) - (s : ℂ) * I) = (t : ℂ) + (s : ℂ) * I := by
    simp only [map_sub, map_mul, Complex.conj_ofReal, Complex.conj_I]; ring
  rw [wsum, hm, hγ, hconj, paperFT_ftest_sub_I hL, paperFT_ftest_add_I hL, map_mul, map_mul,
    Complex.conj_ofReal, Complex.conj_ofReal, Complex.conj_I, Nat.cast_one, one_mul]
  push_cast
  linear_combination ((s : ℂ) ^ 2 * (edge (s * L) : ℂ) ^ 2) * Complex.I_sq

/-- the two orbit points at +t: γ = t − δi and γ = t + δi. -/
theorem gammaOf_orbit_plus (t δ : ℝ) :
    gammaOf (⟨1 / 2 + δ, t⟩ : ℂ) = (t : ℂ) - (δ : ℂ) * I ∧
      gammaOf (⟨1 / 2 - δ, t⟩ : ℂ) = (t : ℂ) - ((-δ : ℝ) : ℂ) * I := by
  constructor
  · rw [gammaOf_mk, show (1 / 2 + δ - 1 / 2 : ℝ) = δ by ring]
  · rw [gammaOf_mk, show (1 / 2 - δ - 1 / 2 : ℝ) = -δ by ring]

/-- the two orbit points at −t: γ = −t − δi and γ = −t + δi. -/
theorem gammaOf_orbit_minus (t δ : ℝ) :
    gammaOf (⟨1 / 2 + δ, -t⟩ : ℂ) = -(t : ℂ) - (δ : ℂ) * I ∧
      gammaOf (⟨1 / 2 - δ, -t⟩ : ℂ) = -(t : ℂ) - ((-δ : ℝ) : ℂ) * I := by
  constructor
  · rw [gammaOf_mk, show (1 / 2 + δ - 1 / 2 : ℝ) = δ by ring]; push_cast; try ring
  · rw [gammaOf_mk, show (1 / 2 - δ - 1 / 2 : ℝ) = -δ by ring]; push_cast; try ring

/-- each of the two points at +t contributes −δ²c(δL)² (multiplicity one). -/
theorem wsum_orbit_plus {mult : ℂ → ℕ} {t δ L : ℝ} (hL : 0 < L)
    (h1 : mult (⟨1 / 2 + δ, t⟩ : ℂ) = 1) (h2 : mult (⟨1 / 2 - δ, t⟩ : ℂ) = 1) :
    wsum mult (ftest t L) (⟨1 / 2 + δ, t⟩ : ℂ) = -((δ ^ 2 * edge (δ * L) ^ 2 : ℝ) : ℂ) ∧
      wsum mult (ftest t L) (⟨1 / 2 - δ, t⟩ : ℂ) = -((δ ^ 2 * edge (δ * L) ^ 2 : ℝ) : ℂ) := by
  refine ⟨wsum_of_gammaOf_eq hL h1 (gammaOf_orbit_plus t δ).1, ?_⟩
  rw [wsum_of_gammaOf_eq hL h2 (gammaOf_orbit_plus t δ).2, neg_sq, neg_mul, edge_neg]

/-- **clause 1's explicit bound, one factor**: ‖h_f(−t − si)‖ ≤ √(4t² + δ²)·e^{δL/2}·G(2tL) for |s| = δ (note §4). -/
theorem norm_paperFT_ftest_reflected {t δ L : ℝ} (ht : 0 ≤ t) (hL : 0 < L) (s : ℝ) (hs : |s| = δ) :
    ‖paperFT (ftest t L) (-(t : ℂ) - (s : ℂ) * I)‖
      ≤ Real.sqrt (4 * t ^ 2 + δ ^ 2) * Real.exp (δ * L / 2) * Gmaj (2 * t * L) := by
  have hδ : 0 ≤ δ := hs ▸ abs_nonneg s
  have hs2 : s ^ 2 = δ ^ 2 := by rw [← hs, sq_abs]
  rw [paperFT_ftest hL, norm_mul]
  have h1 : ‖-(t : ℂ) - (s : ℂ) * I - t‖ = Real.sqrt (4 * t ^ 2 + δ ^ 2) := by
    rw [← Real.sqrt_sq (norm_nonneg _), Complex.sq_norm, Complex.normSq_apply]
    congr 1
    simp only [Complex.sub_re, Complex.neg_re, Complex.ofReal_re, Complex.mul_re, Complex.ofReal_im,
      Complex.I_re, Complex.I_im, Complex.sub_im, Complex.neg_im, Complex.mul_im]
    linear_combination hs2
  have h2 : ‖paperFT (fun v => (B v : ℂ)) ((L : ℂ) * (-(t : ℂ) - (s : ℂ) * I - t))‖
      ≤ Real.exp (δ * L / 2) * Gmaj (2 * t * L) := by
    have h := norm_paperFT_Bc_le ((L : ℂ) * (-(t : ℂ) - (s : ℂ) * I - t))
    have hre : ((L : ℂ) * (-(t : ℂ) - (s : ℂ) * I - t)).re = -(2 * t * L) := by simp; ring
    have him : ((L : ℂ) * (-(t : ℂ) - (s : ℂ) * I - t)).im = -(L * s) := by simp
    rw [hre, him, abs_neg, abs_neg, abs_mul, abs_of_pos hL, hs, abs_of_nonneg (by positivity)] at h
    rw [Gmaj, mul_comm δ L]
    exact h
  calc ‖-(t : ℂ) - (s : ℂ) * I - t‖ * ‖paperFT (fun v => (B v : ℂ)) ((L : ℂ) * (-(t : ℂ) - (s : ℂ) * I - t))‖
      = Real.sqrt (4 * t ^ 2 + δ ^ 2) * ‖paperFT (fun v => (B v : ℂ)) ((L : ℂ) * (-(t : ℂ) - (s : ℂ) * I - t))‖ := by
        rw [h1]
    _ ≤ Real.sqrt (4 * t ^ 2 + δ ^ 2) * (Real.exp (δ * L / 2) * Gmaj (2 * t * L)) := by gcongr
    _ = _ := by ring

/-- **clause 1's explicit bound**: a reflected point (multiplicity one, γ_ρ = −t − si, |s| = δ) contributes at most
(4t² + δ²)·e^{δL}·G(2tL)² in norm (note §4). -/
theorem norm_wsum_reflected {mult : ℂ → ℕ} {t δ L : ℝ} (ht : 0 ≤ t) (hL : 0 < L) {ρ : ℂ} (hm : mult ρ = 1)
    (s : ℝ) (hs : |s| = δ) (hγ : gammaOf ρ = -(t : ℂ) - (s : ℂ) * I) :
    ‖wsum mult (ftest t L) ρ‖ ≤ (4 * t ^ 2 + δ ^ 2) * Real.exp (δ * L) * Gmaj (2 * t * L) ^ 2 := by
  have hconj : (starRingEnd ℂ) (-(t : ℂ) - (s : ℂ) * I) = -(t : ℂ) - ((-s : ℝ) : ℂ) * I := by
    simp only [map_sub, map_neg, map_mul, Complex.conj_ofReal, Complex.conj_I]; push_cast; ring
  rw [wsum, hm, hγ, hconj, norm_mul, norm_mul, Complex.norm_conj, Nat.cast_one, norm_one, one_mul]
  have h1 := norm_paperFT_ftest_reflected ht hL s hs
  have h2 := norm_paperFT_ftest_reflected ht hL (-s) (by rw [abs_neg, hs])
  have hsq : Real.sqrt (4 * t ^ 2 + δ ^ 2) * Real.sqrt (4 * t ^ 2 + δ ^ 2) = 4 * t ^ 2 + δ ^ 2 :=
    Real.mul_self_sqrt (by positivity)
  have hex : Real.exp (δ * L / 2) * Real.exp (δ * L / 2) = Real.exp (δ * L) := by
    rw [← Real.exp_add]; ring_nf
  have hG := Gmaj_nonneg (2 * t * L)
  calc ‖paperFT (ftest t L) (-(t : ℂ) - (s : ℂ) * I)‖ * ‖paperFT (ftest t L) (-(t : ℂ) - ((-s : ℝ) : ℂ) * I)‖
      ≤ (Real.sqrt (4 * t ^ 2 + δ ^ 2) * Real.exp (δ * L / 2) * Gmaj (2 * t * L))
          * (Real.sqrt (4 * t ^ 2 + δ ^ 2) * Real.exp (δ * L / 2) * Gmaj (2 * t * L)) :=
        mul_le_mul h1 h2 (norm_nonneg _) (by positivity)
    _ = (Real.sqrt (4 * t ^ 2 + δ ^ 2) * Real.sqrt (4 * t ^ 2 + δ ^ 2))
          * (Real.exp (δ * L / 2) * Real.exp (δ * L / 2)) * Gmaj (2 * t * L) ^ 2 := by ring
    _ = _ := by rw [hsq, hex]

/-- **(R*) exponentiated** (addendum A1): 2(4t² + δ²)e^{δL}G(2tL)² ≤ (27/10)δ²e^{δL/2}. -/
theorem rstar_exp {t δ L : ℝ} (hδ : 0 < δ) (h : Rstar t δ L) :
    2 * (4 * t ^ 2 + δ ^ 2) * Real.exp (δ * L) * Gmaj (2 * t * L) ^ 2 ≤ 27 / 10 * δ ^ 2 * Real.exp (δ * L / 2) := by
  unfold Rstar at h
  unfold Gmaj
  set s := Real.sqrt (2 * t * L) with hs
  set X := Real.exp (δ * L / 2) with hX
  set E := Real.exp (2 * cB * s) with hE
  set P := 1 + cB / 2 * s with hP
  set A := (4 * t ^ 2 + δ ^ 2) * CB ^ 2 / (27 / 20 * δ ^ 2) with hA
  have hs0 : 0 ≤ s := Real.sqrt_nonneg _
  have hcB := cB_pos
  have hCB := CB_pos
  have hA0 : 0 < A := by positivity
  have hP0 : 0 < P := by positivity
  have hX0 : 0 < X := Real.exp_pos _
  have hE0 : 0 < E := Real.exp_pos _
  have hA' : 27 / 20 * δ ^ 2 * A = (4 * t ^ 2 + δ ^ 2) * CB ^ 2 := by
    rw [hA]; field_simp
  -- exponentiate (R*): X * A ≤ E / P²
  have h' := Real.exp_le_exp.mpr h
  rw [Real.exp_add, Real.exp_log hA0, Real.exp_sub,
    show 2 * Real.log P = Real.log (P ^ 2) by rw [Real.log_pow]; push_cast; ring,
    Real.exp_log (by positivity)] at h'
  have h'' : X * A * P ^ 2 ≤ E := by
    rw [le_div_iff₀ (by positivity)] at h'; exact h'
  have h3 : X * ((4 * t ^ 2 + δ ^ 2) * CB ^ 2) * P ^ 2 ≤ 27 / 20 * δ ^ 2 * E := by
    have := mul_le_mul_of_nonneg_left h'' (by positivity : (0 : ℝ) ≤ 27 / 20 * δ ^ 2)
    calc X * ((4 * t ^ 2 + δ ^ 2) * CB ^ 2) * P ^ 2 = 27 / 20 * δ ^ 2 * (X * A * P ^ 2) := by
          rw [← hA']; ring
      _ ≤ 27 / 20 * δ ^ 2 * E := this
  have hX2 : Real.exp (δ * L) = X ^ 2 := by
    rw [hX, ← Real.exp_nat_mul]; congr 1; push_cast; ring
  have hEinv : Real.exp (-(cB * s)) ^ 2 = E⁻¹ := by
    rw [hE, ← Real.exp_neg, ← Real.exp_nat_mul]; congr 1; push_cast; ring
  rw [hX2, mul_pow, mul_pow, hEinv,
    show 2 * (4 * t ^ 2 + δ ^ 2) * X ^ 2 * (CB ^ 2 * P ^ 2 * E⁻¹)
      = (2 * (4 * t ^ 2 + δ ^ 2) * X ^ 2 * (CB ^ 2 * P ^ 2)) / E by rw [div_eq_mul_inv]; ring,
    div_le_iff₀ hE0]
  have := mul_le_mul_of_nonneg_left h3 (by positivity : (0 : ℝ) ≤ 2 * X)
  linear_combination this

/-! ### §4 The decomposition of the datum: in-window off-line + in-window on-line + out-window -/

/-- W = Σ_{in-window, off-line} + Σ_{in-window, on-line} + Σ_{out-window}: a genuine partition of the carrier (the
window is |Im ρ − t| ≤ R, its complement |Im ρ − t| > R); the two in-window parts are finite (`finite_window`), the
out-window part is summable by H-out. -/
theorem W_decomp {carrier : Set ℂ} {mult : ℂ → ℕ} {f : ℝ → ℂ} {t R : ℝ}
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hout : Summable (fun ρ : ↥(carrier ∩ {ρ | R < |ρ.im - t|}) => ‖wsum mult f ρ‖)) :
    ∑' ρ : carrier, wsum mult f ρ
      = (∑' ρ : ↥(carrier ∩ {ρ | |ρ.im - t| ≤ R ∧ ρ.re ≠ 1 / 2}), wsum mult f ρ)
        + (∑' ρ : ↥(carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R}), wsum mult f ρ)
        + ∑' ρ : ↥(carrier ∩ {ρ | R < |ρ.im - t|}), wsum mult f ρ := by
  classical
  set S := wsum mult f with hS
  set A := carrier ∩ {ρ | |ρ.im - t| ≤ R ∧ ρ.re ≠ 1 / 2} with hA
  set In := carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R} with hIn
  set Out := carrier ∩ {ρ | R < |ρ.im - t|} with hOut
  have hAfin : A.Finite := (hfin (t - R - 1) (t + R)).subset (by
    rintro ρ ⟨h1, h2, _⟩
    have := abs_le.mp (show |ρ.im - t| ≤ R from h2)
    exact ⟨h1, by linarith [this.1], by linarith [this.2]⟩)
  have hInfin : In.Finite := (hfin (t - R - 1) (t + R)).subset (by
    rintro ρ ⟨h1, _, h2⟩
    have := abs_le.mp (show |ρ.im - t| ≤ R from h2)
    exact ⟨h1, by linarith [this.1], by linarith [this.2]⟩)
  have hsA : Summable (A.indicator S) :=
    summable_of_ne_finset_zero (s := hAfin.toFinset) fun ρ hρ =>
      Set.indicator_of_notMem (fun h => hρ (hAfin.mem_toFinset.mpr h)) S
  have hsIn : Summable (In.indicator S) :=
    summable_of_ne_finset_zero (s := hInfin.toFinset) fun ρ hρ =>
      Set.indicator_of_notMem (fun h => hρ (hInfin.mem_toFinset.mpr h)) S
  have hsOut : Summable (Out.indicator S) := summable_subtype_iff_indicator.mp (Summable.of_norm hout)
  have hpart : ∀ ρ, carrier.indicator S ρ = A.indicator S ρ + In.indicator S ρ + Out.indicator S ρ := by
    intro ρ
    by_cases hc : ρ ∈ carrier
    · rw [Set.indicator_of_mem hc]
      by_cases hR : R < |ρ.im - t|
      · rw [Set.indicator_of_notMem (fun h : ρ ∈ A => by
            obtain ⟨_, h2, _⟩ := h; exact absurd h2 (not_le.mpr hR)),
          Set.indicator_of_notMem (fun h : ρ ∈ In => by
            obtain ⟨_, _, h2⟩ := h; exact absurd h2 (not_le.mpr hR)),
          Set.indicator_of_mem (show ρ ∈ Out from ⟨hc, hR⟩)]
        ring
      · have hR' : |ρ.im - t| ≤ R := not_lt.mp hR
        rw [Set.indicator_of_notMem (fun h : ρ ∈ Out => by obtain ⟨_, h2⟩ := h; exact hR h2)]
        by_cases hre : ρ.re = 1 / 2
        · rw [Set.indicator_of_notMem (fun h : ρ ∈ A => by obtain ⟨_, _, h3⟩ := h; exact h3 hre),
            Set.indicator_of_mem (show ρ ∈ In from ⟨hc, hre, hR'⟩)]
          ring
        · rw [Set.indicator_of_mem (show ρ ∈ A from ⟨hc, hR', hre⟩),
            Set.indicator_of_notMem (fun h : ρ ∈ In => by obtain ⟨_, h2, _⟩ := h; exact hre h2)]
          ring
    · rw [Set.indicator_of_notMem hc, Set.indicator_of_notMem (fun h : ρ ∈ A => hc h.1),
        Set.indicator_of_notMem (fun h : ρ ∈ In => hc h.1), Set.indicator_of_notMem (fun h : ρ ∈ Out => hc h.1)]
      ring
  rw [tsum_subtype carrier S, tsum_subtype A S, tsum_subtype In S, tsum_subtype Out S]
  simp_rw [hpart]
  rw [(hsA.add hsIn).tsum_add hsOut, hsA.tsum_add hsIn]

/-- on the line, γ_ρ is real and the Weil summand is m_ρ‖h_f(γ_ρ)‖². -/
theorem wsum_real {mult : ℂ → ℕ} {f : ℝ → ℂ} {ρ : ℂ} (hρ : ρ.re = 1 / 2) :
    wsum mult f ρ = (((mult ρ : ℝ) * ‖paperFT f (gammaOf ρ)‖ ^ 2 : ℝ) : ℂ) := by
  have hγ : (starRingEnd ℂ) (gammaOf ρ) = gammaOf ρ := by
    rw [gammaOf_of_re_eq_half hρ, Complex.conj_ofReal]
  rw [wsum, hγ, mul_assoc, Complex.mul_conj, Complex.normSq_eq_norm_sq]
  push_cast; ring

/-- the in-window on-line part of the datum is the rung's N_Z (real). -/
theorem tsum_inWindow_eq {carrier : Set ℂ} {mult : ℂ → ℕ} {f : ℝ → ℂ} {t R : ℝ} :
    ∑' ρ : ↥(carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R}), wsum mult f ρ
      = ((∑' ρ : ↥(carrier ∩ {ρ | ρ.re = 1 / 2 ∧ |ρ.im - t| ≤ R}),
          (mult ρ : ℝ) * ‖paperFT f (gammaOf ρ)‖ ^ 2 : ℝ) : ℂ) := by
  rw [Complex.ofReal_tsum]
  exact tsum_congr fun ρ => wsum_real ρ.2.2.1

/-- **the orbit's contribution**: the in-window off-line part of Z is contained in the orbit and contains the pair at
+t, so its real part is at most −2δ²c(δL)² + 2·(4t² + δ²)e^{δL}G(2tL)² (the reflected pair, when it is in the window —
if 2t > 73L it belongs to the out-window part instead, and the bound holds with 0 in its place). -/
theorem re_tsum_offline_le {carrier : Set ℂ} {mult : ℂ → ℕ} {t δ L : ℝ} (ht : 0 < t) (hδ : 0 < δ) (hL : 0 < L)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hZorb : orbit t δ ⊆ carrier) (hZmult : ∀ ρ ∈ orbit t δ, mult ρ = 1)
    (hZ : ∀ ρ ∈ carrier, |ρ.im - t| ≤ 73 * L → ρ ∉ orbit t δ → ρ.re = 1 / 2) :
    (∑' ρ : ↥(carrier ∩ {ρ | |ρ.im - t| ≤ 73 * L ∧ ρ.re ≠ 1 / 2}), wsum mult (ftest t L) ρ).re
      ≤ -(2 * δ ^ 2 * edge (δ * L) ^ 2)
        + 2 * ((4 * t ^ 2 + δ ^ 2) * Real.exp (δ * L) * Gmaj (2 * t * L) ^ 2) := by
  classical
  have horb : ∀ ρ, ρ ∈ orbit t δ ↔
      ρ = (⟨1 / 2 + δ, t⟩ : ℂ) ∨ ρ = (⟨1 / 2 - δ, t⟩ : ℂ) ∨ ρ = (⟨1 / 2 + δ, -t⟩ : ℂ) ∨ ρ = (⟨1 / 2 - δ, -t⟩ : ℂ) :=
    fun ρ => by simp only [orbit, Set.mem_insert_iff, Set.mem_singleton_iff]
  have h12 : (⟨1 / 2 + δ, t⟩ : ℂ) ≠ (⟨1 / 2 - δ, t⟩ : ℂ) := fun h => by
    have := congrArg Complex.re h; simp at this; linarith
  have h34 : (⟨1 / 2 + δ, -t⟩ : ℂ) ≠ (⟨1 / 2 - δ, -t⟩ : ℂ) := fun h => by
    have := congrArg Complex.re h; simp at this; linarith
  have hAfin : (carrier ∩ {ρ | |ρ.im - t| ≤ 73 * L ∧ ρ.re ≠ 1 / 2}).Finite :=
    (hfin (t - 73 * L - 1) (t + 73 * L)).subset (by
      rintro ρ ⟨h1, h2, _⟩
      have := abs_le.mp (show |ρ.im - t| ≤ 73 * L from h2)
      exact ⟨h1, by linarith [this.1], by linarith [this.2]⟩)
  have hmemF : ∀ ρ, ρ ∈ hAfin.toFinset ↔ ρ ∈ carrier ∩ {ρ | |ρ.im - t| ≤ 73 * L ∧ ρ.re ≠ 1 / 2} :=
    fun ρ => hAfin.mem_toFinset
  have htsum : ∑' ρ : ↥(carrier ∩ {ρ | |ρ.im - t| ≤ 73 * L ∧ ρ.re ≠ 1 / 2}), wsum mult (ftest t L) ρ
      = ∑ ρ ∈ hAfin.toFinset, wsum mult (ftest t L) ρ := by
    rw [tsum_subtype _ (wsum mult (ftest t L)), tsum_eq_sum (s := hAfin.toFinset) ?_]
    · exact Finset.sum_congr rfl fun ρ hρ => Set.indicator_of_mem ((hmemF ρ).mp hρ) _
    · intro ρ hρ; exact Set.indicator_of_notMem (fun h => hρ ((hmemF ρ).mpr h)) _
  have hp1A : (⟨1 / 2 + δ, t⟩ : ℂ) ∈ carrier ∩ {ρ | |ρ.im - t| ≤ 73 * L ∧ ρ.re ≠ 1 / 2} :=
    ⟨hZorb ((horb _).mpr (Or.inl rfl)), by
      show |t - t| ≤ 73 * L; rw [sub_self, abs_zero]; positivity, by
      show (1 / 2 + δ : ℝ) ≠ 1 / 2; intro h; linarith⟩
  have hp2A : (⟨1 / 2 - δ, t⟩ : ℂ) ∈ carrier ∩ {ρ | |ρ.im - t| ≤ 73 * L ∧ ρ.re ≠ 1 / 2} :=
    ⟨hZorb ((horb _).mpr (Or.inr (Or.inl rfl))), by
      show |t - t| ≤ 73 * L; rw [sub_self, abs_zero]; positivity, by
      show (1 / 2 - δ : ℝ) ≠ 1 / 2; intro h; linarith⟩
  have hsub12 : ({(⟨1 / 2 + δ, t⟩ : ℂ), (⟨1 / 2 - δ, t⟩ : ℂ)} : Finset ℂ) ⊆ hAfin.toFinset := by
    intro ρ hρ
    rw [Finset.mem_insert, Finset.mem_singleton] at hρ
    rcases hρ with rfl | rfl
    · exact (hmemF _).mpr hp1A
    · exact (hmemF _).mpr hp2A
  have hsub34 : hAfin.toFinset \ {(⟨1 / 2 + δ, t⟩ : ℂ), (⟨1 / 2 - δ, t⟩ : ℂ)}
      ⊆ ({(⟨1 / 2 + δ, -t⟩ : ℂ), (⟨1 / 2 - δ, -t⟩ : ℂ)} : Finset ℂ) := by
    intro ρ hρ
    rw [Finset.mem_sdiff, Finset.mem_insert, Finset.mem_singleton] at hρ
    obtain ⟨hρF, hρ12⟩ := hρ
    obtain ⟨hρc, hρw, hρre⟩ := (hmemF ρ).mp hρF
    have hρorb : ρ ∈ orbit t δ := by
      by_contra h
      exact hρre (hZ ρ hρc hρw h)
    rw [Finset.mem_insert, Finset.mem_singleton]
    rcases (horb ρ).mp hρorb with h | h | h | h
    · exact absurd (Or.inl h) hρ12
    · exact absurd (Or.inr h) hρ12
    · exact Or.inl h
    · exact Or.inr h
  obtain ⟨hS1, hS2⟩ := wsum_orbit_plus (mult := mult) hL (hZmult _ ((horb _).mpr (Or.inl rfl)))
    (hZmult _ ((horb _).mpr (Or.inr (Or.inl rfl))))
  have hS3 := norm_wsum_reflected (mult := mult) ht.le hL (hZmult _ ((horb _).mpr (Or.inr (Or.inr (Or.inl rfl)))))
    δ (abs_of_pos hδ) (gammaOf_orbit_minus t δ).1
  have hS4 := norm_wsum_reflected (mult := mult) ht.le hL (hZmult _ ((horb _).mpr (Or.inr (Or.inr (Or.inr rfl)))))
    (-δ) (by rw [abs_neg, abs_of_pos hδ]) (gammaOf_orbit_minus t δ).2
  rw [htsum, ← Finset.union_sdiff_of_subset hsub12, Finset.sum_union Finset.disjoint_sdiff, Finset.sum_pair h12,
    Complex.add_re, Complex.add_re, hS1, hS2, Complex.neg_re, Complex.ofReal_re]
  have hrest : (∑ ρ ∈ hAfin.toFinset \ {(⟨1 / 2 + δ, t⟩ : ℂ), (⟨1 / 2 - δ, t⟩ : ℂ)}, wsum mult (ftest t L) ρ).re
      ≤ 2 * ((4 * t ^ 2 + δ ^ 2) * Real.exp (δ * L) * Gmaj (2 * t * L) ^ 2) := by
    calc (∑ ρ ∈ hAfin.toFinset \ {(⟨1 / 2 + δ, t⟩ : ℂ), (⟨1 / 2 - δ, t⟩ : ℂ)}, wsum mult (ftest t L) ρ).re
        = ∑ ρ ∈ hAfin.toFinset \ {(⟨1 / 2 + δ, t⟩ : ℂ), (⟨1 / 2 - δ, t⟩ : ℂ)}, (wsum mult (ftest t L) ρ).re :=
          Complex.re_sum _ _
      _ ≤ ∑ ρ ∈ hAfin.toFinset \ {(⟨1 / 2 + δ, t⟩ : ℂ), (⟨1 / 2 - δ, t⟩ : ℂ)}, ‖wsum mult (ftest t L) ρ‖ :=
          Finset.sum_le_sum fun ρ _ => Complex.re_le_norm _
      _ ≤ ∑ ρ ∈ ({(⟨1 / 2 + δ, -t⟩ : ℂ), (⟨1 / 2 - δ, -t⟩ : ℂ)} : Finset ℂ), ‖wsum mult (ftest t L) ρ‖ :=
          Finset.sum_le_sum_of_subset_of_nonneg hsub34 fun _ _ _ => norm_nonneg _
      _ = ‖wsum mult (ftest t L) (⟨1 / 2 + δ, -t⟩ : ℂ)‖ + ‖wsum mult (ftest t L) (⟨1 / 2 - δ, -t⟩ : ℂ)‖ :=
          Finset.sum_pair h34
      _ ≤ _ := by linarith [hS3, hS4]
  linarith [hrest]

/-! ### §5 Numerics: log 25, log 1.875; H-edge to the margin c(λ)² ≥ 1.875·e^{λ/2} -/

theorem log25_le : Real.log 25 ≤ 3221173 / 1000000 := by
  rw [Real.log_le_iff_le_exp (by norm_num)]
  have e1 := Real.exp_one_gt_d9
  have e3 : (2.7182818283 : ℝ) ^ 3 ≤ Real.exp 1 ^ 3 := pow_le_pow_left₀ (by norm_num) e1.le 3
  have t4 := Real.sum_le_exp_of_nonneg (show (0 : ℝ) ≤ 221173 / 1000000 by norm_num) 5
  rw [show (3221173 / 1000000 : ℝ) = ((3 : ℕ) : ℝ) * 1 + 221173 / 1000000 by norm_num, Real.exp_add,
    Real.exp_nat_mul]
  calc (25 : ℝ) ≤ (2.7182818283 : ℝ) ^ 3 * ∑ i ∈ Finset.range 5, (221173 / 1000000 : ℝ) ^ i / (i.factorial : ℝ) := by
        norm_num [Finset.sum_range_succ, Nat.factorial_succ, Nat.factorial_zero]
    _ ≤ Real.exp 1 ^ 3 * Real.exp (221173 / 1000000) := mul_le_mul e3 t4 (by positivity) (by positivity)

theorem log_1875_le : Real.log (1875 / 1000) ≤ 63 / 100 := by
  rw [Real.log_le_iff_le_exp (by norm_num),
    show (63 / 100 : ℝ) = ((2 : ℕ) : ℝ) * (315 / 1000) by norm_num, Real.exp_nat_mul]
  have t5 := Real.sum_le_exp_of_nonneg (show (0 : ℝ) ≤ 315 / 1000 by norm_num) 6
  calc (1875 / 1000 : ℝ) ≤ (∑ i ∈ Finset.range 6, (315 / 1000 : ℝ) ^ i / (i.factorial : ℝ)) ^ 2 := by
        norm_num [Finset.sum_range_succ, Nat.factorial_succ, Nat.factorial_zero]
    _ ≤ Real.exp (315 / 1000) ^ 2 := pow_le_pow_left₀ (by positivity) t5 2

/-- **H-edge to the margin** (clause 3 with the slack of addendum A2): c(λ)² ≥ 1.875·e^{λ/2} for λ ≥ 25, through
√λ ≤ λ/10 + 5/2, log λ ≤ log 25 + λ/25 − 1, log 25 ≤ 3.221173 and log 1.875 ≤ 0.63 (m(25) = 0.6335 in the note). -/
theorem edge_sq_ge (hedge : Hedge) {l : ℝ} (hl : 25 ≤ l) : 1875 / 1000 * Real.exp (l / 2) ≤ edge l ^ 2 := by
  have h := hedge l hl
  have h0 : 0 ≤ Real.exp (l / 2 - Real.sqrt l - 3 / 4 * Real.log l + 148088 / 100000) := (Real.exp_pos _).le
  have hsq := pow_le_pow_left₀ h0 h 2
  refine le_trans ?_ hsq
  rw [← Real.exp_nat_mul]
  have hsqrt : Real.sqrt l ≤ l / 10 + 5 / 2 := by
    have h1 := Real.sqrt_nonneg l
    have h2 := Real.sq_sqrt (show (0 : ℝ) ≤ l by linarith)
    nlinarith [sq_nonneg (Real.sqrt l - 5)]
  have hlog : Real.log l ≤ Real.log 25 + (l / 25 - 1) := by
    have e : Real.log l = Real.log 25 + Real.log (l / 25) := by
      rw [← Real.log_mul (by norm_num) (by positivity)]; congr 1; field_simp
    rw [e]
    linarith [Real.log_le_sub_one_of_pos (by positivity : (0 : ℝ) < l / 25)]
  have hm : Real.log (1875 / 1000) + l / 2
      ≤ ((2 : ℕ) : ℝ) * (l / 2 - Real.sqrt l - 3 / 4 * Real.log l + 148088 / 100000) := by
    push_cast
    linarith [hsqrt, hlog, log25_le, log_1875_le]
  calc 1875 / 1000 * Real.exp (l / 2) = Real.exp (Real.log (1875 / 1000) + l / 2) := by
        rw [Real.exp_add, Real.exp_log (by norm_num)]
    _ ≤ _ := Real.exp_le_exp.mpr hm

/-! ### §6 The L-hypothesis absorptions -/

/-- from L ≥ 25/δ and L ≥ (4/δ)(log log(3 + t) + 2log(1/δ) + log(2b₁C₁)), with U := δ²e^{δL/2}:
N = 2b₁C₁ℓ_R/L² ≤ 0.039·U, 2e^{−L} ≤ 0.001·U, and U ≥ 1 (note §7.1's chain, addendum A2, with cruder constants). -/
theorem absorb {C₁ t δ L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2) (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * (87 / 10) * C₁)) ≤ L) :
    2 * (87 / 10) * C₁ * Real.log (4 + t + 73 * L) / L ^ 2 ≤ 39 / 1000 * (δ ^ 2 * Real.exp (δ * L / 2)) ∧
      2 * Real.exp (-L) ≤ 1 / 1000 * (δ ^ 2 * Real.exp (δ * L / 2)) ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) := by
  have hL50 : 50 ≤ L := by
    have : (50 : ℝ) ≤ 25 / δ := by rw [le_div_iff₀ hδ0]; linarith
    linarith
  have hL0 : 0 < L := by linarith
  have hC0 : 0 ≤ C₁ := by linarith
  set ℓ := Real.log (3 + t) with hℓ
  have hℓ1 : 138 / 100 ≤ ℓ := by
    have h4 : Real.log 4 ≤ ℓ := Real.log_le_log (by norm_num) (by linarith)
    have : Real.log 4 = 2 * Real.log 2 := by
      rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow]; push_cast; ring
    have h2 : (69 : ℝ) / 100 < Real.log 2 := lt_trans (by norm_num) Real.log_two_gt_d9
    linarith
  have hℓ0 : 0 < ℓ := by linarith
  set Q := Real.log ℓ + 2 * Real.log (1 / δ) + Real.log (2 * (87 / 10) * C₁) with hQ
  have h4Q : 4 * Q ≤ δ * L := by
    have e : 4 / δ * Q * δ = 4 * Q := by field_simp
    calc 4 * Q = 4 / δ * Q * δ := e.symm
      _ ≤ L * δ := mul_le_mul_of_nonneg_right hL2 hδ0.le
      _ = δ * L := by ring
  set X := Real.exp (δ * L / 2) with hX
  have hX0 : 0 < X := Real.exp_pos _
  have hXge : ℓ ^ 2 * (1 / δ) ^ 4 * (2 * (87 / 10) * C₁) ^ 2 ≤ X := by
    have e : ℓ ^ 2 * (1 / δ) ^ 4 * (2 * (87 / 10) * C₁) ^ 2 = Real.exp (2 * Q) := by
      rw [hQ, mul_add, mul_add, Real.exp_add, Real.exp_add,
        show 2 * (2 * Real.log (1 / δ)) = ((4 : ℕ) : ℝ) * Real.log (1 / δ) by push_cast; ring,
        show 2 * Real.log ℓ = ((2 : ℕ) : ℝ) * Real.log ℓ by push_cast; ring,
        show 2 * Real.log (2 * (87 / 10) * C₁) = ((2 : ℕ) : ℝ) * Real.log (2 * (87 / 10) * C₁) by push_cast; ring,
        Real.exp_nat_mul, Real.exp_nat_mul, Real.exp_nat_mul, Real.exp_log hℓ0, Real.exp_log (by positivity),
        Real.exp_log (by positivity)]
    rw [e, hX]
    exact Real.exp_le_exp.mpr (by linarith)
  have hU : 4 * ℓ ^ 2 * (2 * (87 / 10) * C₁) ^ 2 ≤ δ ^ 2 * X := by
    have h1 : 4 ≤ (1 / δ) ^ 2 := by
      rw [div_pow, one_pow, le_div_iff₀ (by positivity)]
      nlinarith
    have e : δ ^ 2 * (ℓ ^ 2 * (1 / δ) ^ 4 * (2 * (87 / 10) * C₁) ^ 2)
        = (δ * (1 / δ)) ^ 2 * ((1 / δ) ^ 2 * ℓ ^ 2 * (2 * (87 / 10) * C₁) ^ 2) := by ring
    calc 4 * ℓ ^ 2 * (2 * (87 / 10) * C₁) ^ 2 ≤ (1 / δ) ^ 2 * ℓ ^ 2 * (2 * (87 / 10) * C₁) ^ 2 := by gcongr
      _ = δ ^ 2 * (ℓ ^ 2 * (1 / δ) ^ 4 * (2 * (87 / 10) * C₁) ^ 2) := by
          rw [e, mul_one_div_cancel hδ0.ne', one_pow, one_mul]
      _ ≤ δ ^ 2 * X := by gcongr
  have hU1 : 1 ≤ δ ^ 2 * X := by
    have : (1 : ℝ) ≤ 4 * ℓ ^ 2 * (2 * (87 / 10) * C₁) ^ 2 := by
      calc (1 : ℝ) ≤ 4 * (138 / 100) ^ 2 * (2 * (87 / 10)) ^ 2 * 1 ^ 2 := by norm_num
        _ ≤ 4 * ℓ ^ 2 * (2 * (87 / 10)) ^ 2 * C₁ ^ 2 := by gcongr
        _ = 4 * ℓ ^ 2 * (2 * (87 / 10) * C₁) ^ 2 := by ring
    linarith
  refine ⟨?_, ?_, hU1⟩
  · have hℓR : Real.log (4 + t + 73 * L) ≤ ℓ + 73 * L := by
      have h1 : 4 + t + 73 * L ≤ (3 + t) * Real.exp (73 * L) := by
        have := Real.add_one_le_exp (73 * L)
        calc 4 + t + 73 * L ≤ (3 + t) * (73 * L + 1) := by nlinarith
          _ ≤ (3 + t) * Real.exp (73 * L) := by gcongr
      calc Real.log (4 + t + 73 * L) ≤ Real.log ((3 + t) * Real.exp (73 * L)) :=
            Real.log_le_log (by positivity) h1
        _ = ℓ + 73 * L := by rw [Real.log_mul (by positivity) (Real.exp_pos _).ne', Real.log_exp]
    have ha : 50 * ℓ ≤ L * ℓ := mul_le_mul_of_nonneg_right hL50 hℓ0.le
    have hb : 138 / 100 * L ≤ L * ℓ := by
      have := mul_le_mul_of_nonneg_left hℓ1 hL0.le; linarith
    have hLℓ : 69 ≤ L * ℓ := by nlinarith only [ha, hℓ1]
    have hsq : 69 * (L * ℓ) ≤ (L * ℓ) ^ 2 := by
      nlinarith only [mul_nonneg (sub_nonneg.mpr hLℓ) (by positivity : (0 : ℝ) ≤ L * ℓ)]
    have hkey : ℓ + 73 * L ≤ 271 / 100 * (L ^ 2 * ℓ ^ 2) := by
      have e : L ^ 2 * ℓ ^ 2 = (L * ℓ) ^ 2 := by ring
      rw [e]; linarith only [hsq, ha, hb, hLℓ]
    have hprod : C₁ * (L ^ 2 * ℓ ^ 2) * 1 ≤ C₁ * (L ^ 2 * ℓ ^ 2) * C₁ :=
      mul_le_mul_of_nonneg_left hC (by positivity)
    rw [div_le_iff₀ (by positivity)]
    calc 2 * (87 / 10) * C₁ * Real.log (4 + t + 73 * L) ≤ 2 * (87 / 10) * C₁ * (ℓ + 73 * L) := by gcongr
      _ ≤ 2 * (87 / 10) * C₁ * (271 / 100 * (L ^ 2 * ℓ ^ 2)) := by gcongr
      _ ≤ 39 / 1000 * (4 * ℓ ^ 2 * (2 * (87 / 10) * C₁) ^ 2) * L ^ 2 := by
          have hnn : 0 ≤ C₁ * (L ^ 2 * ℓ ^ 2) := by positivity
          linarith only [hprod, hnn]
      _ ≤ 39 / 1000 * (δ ^ 2 * X) * L ^ 2 := by gcongr
  · have h1 : Real.exp (-L) ≤ Real.exp (-50) := Real.exp_le_exp.mpr (by linarith)
    have h25 : (338 : ℝ) ≤ Real.exp 25 := by
      have := Real.quadratic_le_exp_of_nonneg (show (0 : ℝ) ≤ 25 by norm_num)
      linarith
    have h2 : (114244 : ℝ) ≤ Real.exp 50 := by
      rw [show (50 : ℝ) = ((2 : ℕ) : ℝ) * 25 by norm_num, Real.exp_nat_mul]
      calc (114244 : ℝ) = 338 ^ 2 := by norm_num
        _ ≤ Real.exp 25 ^ 2 := pow_le_pow_left₀ (by norm_num) h25 2
    have h3 : Real.exp (-50) ≤ 1 / 114244 := by
      rw [Real.exp_neg, one_div]
      exact inv_anti₀ (by norm_num) h2
    have h4 : 1 / 1000 ≤ 1 / 1000 * (δ ^ 2 * X) := by
      have := mul_le_mul_of_nonneg_left hU1 (by norm_num : (0 : ℝ) ≤ 1 / 1000); linarith
    linarith

/-! ### §7 The assembly -/

/-- **Theorem M2, clause 6** (separation note §7.1 with the addendum's hypotheses), library form over raw data —
modulo the displayed H-b₁, H-B‴, H-edge and H-out (for Z and for Z′). -/
theorem clause6_assembly {C₁ t δ L : ℝ} (hC : 1 ≤ C₁) (ht : 3 ≤ t) (hδ0 : 0 < δ) (hδ : δ ≤ 1 / 2)
    (hL1 : 25 / δ ≤ L)
    (hL2 : 4 / δ * (Real.log (Real.log (3 + t)) + 2 * Real.log (1 / δ) + Real.log (2 * (87 / 10) * C₁)) ≤ L)
    (hRstar : Rstar t δ L)
    (carrier : Set ℂ) (mult : ℂ → ℕ)
    (hfin : ∀ T₁ T₂ : ℝ, (carrier ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier ∩ {ρ | |ρ.im - x| ≤ 1}, mult ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (carrier' : Set ℂ) (mult' : ℂ → ℕ)
    (hfin' : ∀ T₁ T₂ : ℝ, (carrier' ∩ {ρ | T₁ < ρ.im ∧ ρ.im ≤ T₂}).Finite)
    (hcount' : ∀ x : ℝ, ((∑ᶠ ρ ∈ carrier' ∩ {ρ | |ρ.im - x| ≤ 1}, mult' ρ : ℕ) : ℝ) ≤ C₁ * Real.log (3 + |x|))
    (hZorb : orbit t δ ⊆ carrier) (hZmult : ∀ ρ ∈ orbit t δ, mult ρ = 1)
    (hZ : ∀ ρ ∈ carrier, |ρ.im - t| ≤ 73 * L → ρ ∉ orbit t δ → ρ.re = 1 / 2)
    (hZ' : ∀ ρ ∈ carrier', |ρ.im - t| ≤ 73 * L → ρ.re = 1 / 2)
    (hb1 : Hb1) (hB3 : HB3) (hedge : Hedge)
    (houtZ : Summable (fun ρ : ↥(carrier ∩ {ρ | 73 * L < |ρ.im - t|}) => ‖wsum mult (ftest t L) ρ‖) ∧
      ‖∑' ρ : ↥(carrier ∩ {ρ | 73 * L < |ρ.im - t|}), wsum mult (ftest t L) ρ‖ ≤ Real.exp (-L))
    (houtZ' : Summable (fun ρ : ↥(carrier' ∩ {ρ | 73 * L < |ρ.im - t|}) => ‖wsum mult' (ftest t L) ρ‖) ∧
      ‖∑' ρ : ↥(carrier' ∩ {ρ | 73 * L < |ρ.im - t|}), wsum mult' (ftest t L) ρ‖ ≤ Real.exp (-L)) :
    δ ^ 2 * Real.exp (δ * L / 2)
        ≤ ‖(∑' ρ : carrier, wsum mult (ftest t L) ρ) - ∑' ρ : carrier', wsum mult' (ftest t L) ρ‖ ∧
      1 ≤ δ ^ 2 * Real.exp (δ * L / 2) := by
  obtain ⟨hN, hexp, hU1⟩ := absorb hC ht hδ0 hδ hL1 hL2
  refine ⟨?_, hU1⟩
  have hL50 : 50 ≤ L := by
    have : (50 : ℝ) ≤ 25 / δ := by rw [le_div_iff₀ hδ0]; linarith
    linarith
  have hL0 : 0 < L := by linarith
  have ht0 : 0 < t := by linarith
  have hδL : 25 ≤ δ * L := by
    have := (div_le_iff₀ hδ0).mp hL1; linarith
  rw [W_decomp hfin houtZ.1, W_decomp hfin' houtZ'.1, tsum_inWindow_eq, tsum_inWindow_eq]
  have hA' : (∑' ρ : ↥(carrier' ∩ {ρ | |ρ.im - t| ≤ 73 * L ∧ ρ.re ≠ 1 / 2}), wsum mult' (ftest t L) ρ) = 0 := by
    have : IsEmpty ↥(carrier' ∩ {ρ | |ρ.im - t| ≤ 73 * L ∧ ρ.re ≠ 1 / 2}) :=
      ⟨fun ρ => by obtain ⟨hc, hw, hre⟩ := ρ.2; exact hre (hZ' ρ hc hw)⟩
    exact tsum_empty
  rw [hA']
  have hAre := re_tsum_offline_le ht0 hδ0 hL0 hfin hZorb hZmult hZ
  have hbnd := rstar_exp hδ0 hRstar
  obtain ⟨hNz0, hNzle⟩ := inWindowNoise_le (R := 73 * L) carrier mult hfin hcount hC ht hL50 (by linarith) hb1 hB3
  obtain ⟨hNz0', _⟩ := inWindowNoise_le (R := 73 * L) carrier' mult' hfin' hcount' hC ht hL50 (by linarith) hb1 hB3
  have hOre := (abs_le.mp ((Complex.abs_re_le_norm _).trans houtZ.2)).2
  have hOre' := (abs_le.mp ((Complex.abs_re_le_norm _).trans houtZ'.2)).1
  have hc2 := edge_sq_ge hedge hδL
  have hc2' := mul_le_mul_of_nonneg_left hc2 (sq_nonneg δ)
  set X := Real.exp (δ * L / 2) with hX
  rw [norm_sub_rev]
  refine le_trans ?_ (Complex.re_le_norm _)
  simp only [Complex.sub_re, Complex.add_re, Complex.ofReal_re, Complex.zero_re]
  linarith [hAre, hbnd, hNzle, hN, hNz0', hOre, hOre', hc2', hexp]

end

end Separation
end Zeta23
