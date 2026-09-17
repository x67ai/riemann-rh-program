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

end

end Separation
end Zeta23
