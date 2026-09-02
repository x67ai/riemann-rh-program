/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library; it imports it.

Portions ported from the Lean development in
github.com/judegomila/dbn-lambda-01787854-candidate-audit (branch
lean/certificate-and-argument-principle, commit ea09b2f), Copyright (c) 2026 Jude Gomila,
MIT License, generated with Harmonic Aristotle; ported and adapted here.
The MIT license text is reproduced in the program's NOTICE file.
-/
/-
Zeta23/W1/ArgPrincipleBridge.lean — DISCHARGE of H-AP (D1 milestone v1.1, D-R3).

`Soundness.lean` proves the W1 checker soundness theorem `cert_of_checkW1` modulo two displayed
hypotheses, H-ENCL (`W1EnclOK riemannZeta d`) and H-AP (`RectArgPrinciple riemannZeta`).  This
file PROVES `RectArgPrinciple f` for EVERY `f : ℂ → ℂ` (`rectArgPrinciple_of_local`) and
restates the soundness theorem without H-AP (`cert_of_checkW1_ap`).  Nothing in
`Soundness.lean` is rewritten; it is imported.

Route.  H-AP is stated in `Soundness.lean` for an arbitrary open set `U` containing the closed
rectangle and takes `DifferentiableOn ℂ f U` as a hypothesis, so the only analytic input it
needs is the argument principle for a function analytic on a neighborhood of the rectangle.
The ported theorem `ArgPrinciple.windingRect_eq_sum_analyticOrder` (Rect.lean / General.lean)
is stated for ENTIRE functions; §1 below generalizes the six entire-only lemmas of the port to
`DifferentiableOn ℂ H U`, `U` open with `Rect z w ⊆ U` (route B of the v1.1 task; the proofs
are those of the port with `hH.analyticAt` replaced by `hH.analyticAt (hU.mem_nhds _)` and the
identity theorem applied on the preconnected closed rectangle instead of on `Set.univ`).  No
ζ-specific fact is consumed anywhere in this file: the entire-surrogate route A was not needed.

§2 bridges the two vocabularies: `ArgPrinciple.Rect`/`RectFrontier` (Mathlib's
`[[·,·]] ×ℂ [[·,·]]` convention) against `rectClosed`/`rectBdry`, and the port's four-edge
`rectIntegral (logDeriv f)` against the four affine-parameterized `logDerivSegIntegral`s of the
§4 traversal (bottom, right, top, left).  §3 proves `RectArgPrinciple f` — nondegenerate
rectangles via §1 + §2, the degenerate case `σ₁ = σ₂` (which clause C2b allows) directly: the
horizontal edges have zero length and the two vertical edges cancel, so `Z = 0` — and states
`cert_of_checkW1_ap`.

HONEST LABEL after this file (binding): an accepted ζ transcript is
"kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)".
Never "fully machine-checked": H-ENCL is where the untrusted producers enter, and it stays.
-/
import Mathlib.Analysis.Analytic.Order
import Mathlib.Analysis.Complex.CauchyIntegral
import Zeta23.W1.ArgPrinciple.General
import Zeta23.W1.Soundness

open Set Complex Filter Topology MeasureTheory
open scoped Real BigOperators Interval

noncomputable section

namespace Zeta23
namespace W1

/-! ## 1. The ported argument principle for functions analytic on a neighborhood of the rectangle

The port's `analyticOrderAt_ne_top`, `exists_factor_pow_sub`, `exists_factor_prod`,
`finite_zeros_of_isCompact`, `continuousOn_logDeriv`, `rectIntegral_logDeriv_eq_zero` and
`windingRect_eq_sum_analyticOrder` assume `Differentiable ℂ H`.  Each is restated here with
`DifferentiableOn ℂ H U` for an open `U ⊇ Rect z w` (suffix `_on`).  Statements and proofs
otherwise follow the port. -/

namespace ArgPrinciple

/-- The closed rectangle is preconnected (the continuous image of a product of intervals; the
set identity is the one used in the port's `isCompact_Rect`). -/
lemma isPreconnected_Rect (z w : ℂ) : IsPreconnected (Rect z w) := by
  have h : Rect z w =
      (fun p : ℝ × ℝ => (p.1 : ℂ) + (p.2 : ℂ) * I) '' ([[z.re, w.re]] ×ˢ [[z.im, w.im]]) := by
    ext c
    simp only [Rect, Complex.mem_reProdIm, Set.mem_image, Set.mem_prod]
    constructor
    · rintro ⟨h1, h2⟩
      exact ⟨(c.re, c.im), ⟨h1, h2⟩, by simp⟩
    · rintro ⟨⟨x, y⟩, ⟨h1, h2⟩, rfl⟩
      simpa using ⟨h1, h2⟩
  rw [h]
  exact (isPreconnected_uIcc.prod isPreconnected_uIcc).image _ (by fun_prop : Continuous _).continuousOn

/-- On a preconnected set where `H` is analytic and not identically zero, the order of
vanishing at every point is finite (Mathlib's `analyticOrderAt_ne_top_of_isPreconnected`
transported from a nonvanishing point).  Replaces the port's `analyticOrderAt_ne_top`. -/
lemma analyticOrderAt_ne_top_of_analyticOnNhd {H : ℂ → ℂ} {K : Set ℂ} (hK : IsPreconnected K)
    (hH : AnalyticOnNhd ℂ H K) (hne : ∃ x ∈ K, H x ≠ 0) {p : ℂ} (hp : p ∈ K) :
    analyticOrderAt H p ≠ ⊤ := by
  obtain ⟨x, hxK, hx⟩ := hne
  have h0 : analyticOrderAt H x ≠ ⊤ := by
    rw [(hH x hxK).analyticOrderAt_eq_zero.mpr hx]
    exact ENat.zero_ne_top
  exact hH.analyticOrderAt_ne_top_of_isPreconnected hK hxK hp h0

/-- The port's `exists_factor_pow_sub` for `H` differentiable on an open set `U ∋ p`: the
cofactor `G` is differentiable on `U` and the factorization holds everywhere. -/
lemma exists_factor_pow_sub_on {H : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hH : DifferentiableOn ℂ H U) {p : ℂ} (hp : p ∈ U) (htop : analyticOrderAt H p ≠ ⊤) :
    ∃ G : ℂ → ℂ, DifferentiableOn ℂ G U ∧ G p ≠ 0 ∧
      ∀ ζ, H ζ = (ζ - p) ^ (analyticOrderNatAt H p) * G ζ := by
  classical
  obtain ⟨g, hg, hgp, hHg⟩ := (hH.analyticAt (hU.mem_nhds hp)).analyticOrderAt_ne_top.mp htop
  set n := analyticOrderNatAt H p with hn
  set G : ℂ → ℂ := fun ζ => if ζ = p then g p else H ζ / (ζ - p) ^ n with hG
  have hGg : G =ᶠ[𝓝 p] g := by
    filter_upwards [hHg] with x hx
    by_cases hxp : x = p
    · simp [hG, hxp]
    · have hne : (x - p) ^ n ≠ 0 := pow_ne_zero _ (sub_ne_zero.mpr hxp)
      simp only [hG, if_neg hxp, hx, smul_eq_mul]
      field_simp
  refine ⟨G, ?_, by simp [hG, hgp], ?_⟩
  · intro ζ hζ
    by_cases h : ζ = p
    · subst h
      exact (hg.differentiableAt.congr_of_eventuallyEq hGg).differentiableWithinAt
    · have hev : G =ᶠ[𝓝 ζ] fun x => H x / (x - p) ^ n := by
        filter_upwards [isOpen_ne.mem_nhds h] with x hx
        simp [hG, hx]
      have hd : DifferentiableAt ℂ (fun x : ℂ => (x - p) ^ n) ζ := by fun_prop
      exact (((hH.differentiableAt (hU.mem_nhds hζ)).div hd
        (pow_ne_zero n (sub_ne_zero.mpr h))).congr_of_eventuallyEq hev).differentiableWithinAt
  · intro ζ
    by_cases h : ζ = p
    · subst h
      simpa [hG, hn, smul_eq_mul] using hHg.self_of_nhds
    · have hne : (ζ - p) ^ n ≠ 0 := pow_ne_zero _ (sub_ne_zero.mpr h)
      simp only [hG, if_neg h]
      field_simp

/-- The port's `exists_factor_prod` for `H` differentiable on an open `U`: the finite set `S`
lies in a preconnected `K ⊆ U` on which `H` is not identically zero. -/
lemma exists_factor_prod_on {U K : Set ℂ} (hU : IsOpen U) (hKU : K ⊆ U)
    (hK : IsPreconnected K) (S : Finset ℂ) (hSK : ∀ p ∈ S, p ∈ K)
    {H : ℂ → ℂ} (hH : DifferentiableOn ℂ H U) (hne : ∃ x ∈ K, H x ≠ 0) :
    ∃ G : ℂ → ℂ, DifferentiableOn ℂ G U ∧ (∀ p ∈ S, G p ≠ 0) ∧
      ∀ ζ, H ζ = (∏ p ∈ S, (ζ - p) ^ (analyticOrderNatAt H p)) * G ζ := by
  classical
  induction S using Finset.induction_on generalizing H with
  | empty => exact ⟨H, hH, by simp, by simp⟩
  | insert q T hq ih =>
      have hqK : q ∈ K := hSK q (Finset.mem_insert_self q T)
      have hTK : ∀ p ∈ T, p ∈ K := fun p hp => hSK p (Finset.mem_insert_of_mem hp)
      have htop : analyticOrderAt H q ≠ ⊤ :=
        analyticOrderAt_ne_top_of_analyticOnNhd hK ((hH.analyticOnNhd hU).mono hKU) hne hqK
      obtain ⟨G₁, hG₁, hG₁q, hHfac⟩ := exists_factor_pow_sub_on hU hH (hKU hqK) htop
      obtain ⟨G, hG, hGT, hG₁fac⟩ := ih hTK hG₁ ⟨q, hqK, hG₁q⟩
      have horder : ∀ p ∈ T, analyticOrderNatAt G₁ p = analyticOrderNatAt H p := by
        intro p hp
        have hpq : p ≠ q := fun h => hq (h ▸ hp)
        have hHeq : H = (fun ζ : ℂ => (ζ - q) ^ (analyticOrderNatAt H q)) * G₁ := by
          funext ζ; simpa using hHfac ζ
        have h1 : AnalyticAt ℂ (fun ζ : ℂ => (ζ - q) ^ (analyticOrderNatAt H q)) p := by fun_prop
        have h0 : analyticOrderAt (fun ζ : ℂ => (ζ - q) ^ (analyticOrderNatAt H q)) p = 0 := by
          rw [h1.analyticOrderAt_eq_zero]
          exact pow_ne_zero _ (sub_ne_zero.mpr hpq)
        have hmul := analyticOrderAt_mul h1 (hG₁.analyticAt (hU.mem_nhds (hKU (hTK p hp))))
        rw [← hHeq, h0, zero_add] at hmul
        rw [analyticOrderNatAt, analyticOrderNatAt, hmul]
      refine ⟨G, hG, ?_, ?_⟩
      · intro p hp
        rcases Finset.mem_insert.mp hp with rfl | hp
        · intro h0
          exact hG₁q (by rw [hG₁fac p, h0, mul_zero])
        · exact hGT p hp
      · intro ζ
        rw [Finset.prod_insert hq, hHfac ζ, hG₁fac ζ, mul_assoc]
        congr 2
        exact Finset.prod_congr rfl fun p hp => by rw [horder p hp]

/-- The port's `finite_zeros_of_isCompact` for `H` differentiable on an open `U ⊇ K`, `K`
compact and preconnected, `H` not identically zero on `K`. -/
lemma finite_zeros_of_isCompact_on {H : ℂ → ℂ} {U K : Set ℂ} (hU : IsOpen U) (hKU : K ⊆ U)
    (hK : IsCompact K) (hKc : IsPreconnected K) (hH : DifferentiableOn ℂ H U)
    (hne : ∃ x ∈ K, H x ≠ 0) : {p | p ∈ K ∧ H p = 0}.Finite := by
  by_contra hinf
  rw [Set.not_finite] at hinf
  obtain ⟨x, hxK, hx⟩ := hinf.exists_accPt_of_subset_isCompact hK fun p hp => hp.1
  rw [accPt_iff_frequently_nhdsNE] at hx
  have hfreq : ∃ᶠ y in 𝓝[≠] x, H y = 0 := hx.mono fun y hy => hy.2
  have hAn : AnalyticOnNhd ℂ H K := (hH.analyticOnNhd hU).mono hKU
  obtain ⟨y, hyK, hy⟩ := hne
  exact hy (hAn.eqOn_zero_of_preconnected_of_frequently_eq_zero hKc hxK hfreq hyK)

/-- The zeros of `H` in the closed rectangle form a finite set, `H` differentiable on an open
set containing the rectangle and not identically zero there. -/
lemma finite_zeros_Rect_on {z w : ℂ} {H : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hRU : Rect z w ⊆ U) (hH : DifferentiableOn ℂ H U) (hne : ∃ x ∈ Rect z w, H x ≠ 0) :
    {p | p ∈ Rect z w ∧ H p = 0}.Finite :=
  finite_zeros_of_isCompact_on hU hRU (isCompact_Rect z w) (isPreconnected_Rect z w) hH hne

/-- The port's `continuousOn_logDeriv` for `F` differentiable on an open `U ⊇ Rect z w`. -/
lemma continuousOn_logDeriv_on {z w : ℂ} {F : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hRU : Rect z w ⊆ U) (hF : DifferentiableOn ℂ F U) (hF0 : ∀ c ∈ Rect z w, F c ≠ 0) :
    ContinuousOn (logDeriv F) (RectFrontier z w) := by
  have hAn : AnalyticOnNhd ℂ F (Rect z w) := (hF.analyticOnNhd hU).mono hRU
  have h : ContinuousOn (fun c => deriv F c / F c) (Rect z w) :=
    hAn.deriv.continuousOn.div hAn.continuousOn hF0
  exact h.mono (RectFrontier_subset_Rect z w)

/-- The port's `rectIntegral_logDeriv_eq_zero` (Cauchy–Goursat for `F'/F`) for `F`
differentiable on an open `U ⊇ Rect z w` and nonvanishing on the closed rectangle. -/
lemma rectIntegral_logDeriv_eq_zero_on {z w : ℂ} {F : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hRU : Rect z w ⊆ U) (hF : DifferentiableOn ℂ F U) (hF0 : ∀ c ∈ Rect z w, F c ≠ 0) :
    rectIntegral (logDeriv F) z w = 0 := by
  have hAn : AnalyticOnNhd ℂ F (Rect z w) := (hF.analyticOnNhd hU).mono hRU
  refine rectIntegral_eq_zero_of_differentiableOn ?_
  intro c hc
  have h : DifferentiableAt ℂ (fun c => deriv F c / F c) c :=
    (hAn.deriv c hc).differentiableAt.div (hAn c hc).differentiableAt (hF0 c hc)
  exact (h.congr_of_eventuallyEq (by filter_upwards with x using rfl)).differentiableWithinAt

/-- **The argument principle on a rectangle, local form.**  The port's
`windingRect_eq_sum_analyticOrder` with `Differentiable ℂ H` weakened to
`DifferentiableOn ℂ H U` for an open `U` containing the closed rectangle: if `H` is
nonvanishing on the boundary and `S` is the set of zeros of `H` in the closed rectangle, the
winding number `W (H; z, w)` is the number of zeros inside, counted with multiplicity. -/
theorem windingRect_eq_sum_analyticOrder_on {z w : ℂ} (hre : z.re < w.re) (him : z.im < w.im)
    {H : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U) (hRU : Rect z w ⊆ U) (hH : DifferentiableOn ℂ H U)
    (hbd : ∀ c ∈ RectFrontier z w, H c ≠ 0)
    (S : Finset ℂ) (hS : ∀ p, p ∈ S ↔ (p ∈ Rect z w ∧ H p = 0)) :
    windingRect H z w = ∑ p ∈ S, (analyticOrderNatAt H p : ℂ) := by
  have hzR : z ∈ Rect z w := RectFrontier_subset_Rect z w (mem_RectFrontier_left_corner z w)
  have hne : ∃ x ∈ Rect z w, H x ≠ 0 := ⟨z, hzR, hbd z (mem_RectFrontier_left_corner z w)⟩
  obtain ⟨G, hG, hGS, hfac⟩ := exists_factor_prod_on hU hRU (isPreconnected_Rect z w) S
    (fun p hp => ((hS p).mp hp).1) hH hne
  have hG0 : ∀ c ∈ Rect z w, G c ≠ 0 := by
    intro c hc
    by_cases h : H c = 0
    · exact hGS c ((hS c).mpr ⟨hc, h⟩)
    · intro h0
      exact h (by rw [hfac c, h0, mul_zero])
  have ha : ∀ p ∈ S, (p : ℂ).re ∈ Ioo z.re w.re ∧ (p : ℂ).im ∈ Ioo z.im w.im := by
    intro p hp
    obtain ⟨hp1, hp2⟩ := (hS p).mp hp
    exact mem_Ioo_of_zero_mem_Rect hre him hbd hp1 hp2
  have hHfun : H = fun c => (∏ p ∈ S, (c - p) ^ (analyticOrderNatAt H p)) * G c := funext hfac
  conv_lhs => rw [hHfun]
  exact windingRect_prod_mul (continuousOn_logDeriv_on hU hRU hG hG0)
    (rectIntegral_logDeriv_eq_zero_on hU hRU hG hG0) (fun c hc => hG0 c hc.1)
    (fun c hc => hG.differentiableAt (hU.mem_nhds (hRU hc.1))) ha

end ArgPrinciple

/-! ## 2. Vocabulary bridge: `Rect`/`RectFrontier`/`rectIntegral` ↔ `rectClosed`/`rectBdry`/edge
integrals -/

open ArgPrinciple

/-- `cpt x y` in the `x + y·I` form the port's edge parameterizations use. -/
lemma cpt_eq (x y : ℝ) : cpt x y = (x : ℂ) + (y : ℂ) * I := by
  apply Complex.ext <;> simp [cpt]

/-- For `σ₁ ≤ σ₂`, `t₁ ≤ t₂`, the port's closed rectangle with corners `σ₁ + it₁`, `σ₂ + it₂`
is `rectClosed σ₁ σ₂ t₁ t₂`. -/
lemma Rect_cpt {s₁ s₂ t₁ t₂ : ℝ} (hs : s₁ ≤ s₂) (ht : t₁ ≤ t₂) :
    Rect (cpt s₁ t₁) (cpt s₂ t₂) = rectClosed s₁ s₂ t₁ t₂ := by
  ext c
  simp only [Rect, Complex.mem_reProdIm, cpt_re, cpt_im, Set.uIcc_of_le hs, Set.uIcc_of_le ht,
    Set.mem_Icc, rectClosed, Set.mem_ofPred_eq]
  tauto

/-- For `σ₁ ≤ σ₂`, `t₁ ≤ t₂`, the port's rectangle boundary is `rectBdry σ₁ σ₂ t₁ t₂`
(closed minus open). -/
lemma RectFrontier_cpt {s₁ s₂ t₁ t₂ : ℝ} (hs : s₁ ≤ s₂) (ht : t₁ ≤ t₂) :
    RectFrontier (cpt s₁ t₁) (cpt s₂ t₂) = rectBdry s₁ s₂ t₁ t₂ := by
  ext c
  simp only [RectFrontier, Rect_cpt hs ht, rectBdry, Set.mem_sdiff, rectClosed,
    rectOpen, Set.mem_ofPred_eq, cpt_re, cpt_im]
  constructor
  · rintro ⟨hc, h⟩
    refine ⟨hc, fun ho => ?_⟩
    obtain ⟨o1, o2, o3, o4⟩ := ho
    rcases h with h | h | h | h <;> linarith
  · rintro ⟨hc, ho⟩
    refine ⟨hc, ?_⟩
    by_contra h
    push Not at h
    obtain ⟨h1, h2, h3, h4⟩ := h
    obtain ⟨c1, c2, c3, c4⟩ := hc
    exact ho ⟨lt_of_le_of_ne c1 (Ne.symm h1), lt_of_le_of_ne c2 h2,
      lt_of_le_of_ne c3 (Ne.symm h3), lt_of_le_of_ne c4 h4⟩

/-- A horizontal directed segment `u + iT → v + iT`: the affine-parameterized log-derivative
integral is the interval integral of `logDeriv f` over `[u, v]`.  Unconditional (junk-value
safe): the change of variables is `Soundness.lean`'s `smul_comp_integral` (Mathlib's
`smul_integral_comp_mul_add`). -/
lemma logDerivSegIntegral_horiz (f : ℂ → ℂ) (u v T : ℝ) :
    logDerivSegIntegral f (cpt u T) (cpt v T)
      = ∫ x in u..v, logDeriv f ((x : ℂ) + (T : ℂ) * I) := by
  unfold logDerivSegIntegral
  have hpt : ∀ t : ℝ, segPt (cpt u T) (cpt v T) t
      = (((v - u) * t + u : ℝ) : ℂ) + (T : ℂ) * I := by
    intro t
    rw [segPt_mk_horiz]
    apply Complex.ext
    · simp [cpt]; ring
    · simp [cpt]
  have hdiff : cpt v T - cpt u T = ((v - u : ℝ) : ℂ) := by
    apply Complex.ext <;> simp [cpt]
  have hfun : (fun t : ℝ => (deriv f (segPt (cpt u T) (cpt v T) t)
        / f (segPt (cpt u T) (cpt v T) t)) * (cpt v T - cpt u T))
      = fun t : ℝ => (v - u) • (fun x : ℝ => logDeriv f ((x : ℂ) + (T : ℂ) * I))
          ((v - u) * t + u) := by
    funext t
    rw [hpt, hdiff, Complex.real_smul]
    simp only [logDeriv_apply]
    ring
  have key := smul_comp_integral (fun x : ℝ => logDeriv f ((x : ℂ) + (T : ℂ) * I)) (v - u) u
  have hb : v - u + u = v := by ring
  rw [hb] at key
  rw [hfun]
  exact key

/-- A vertical directed segment `S + iu → S + iv`: the affine-parameterized log-derivative
integral is `I` times the interval integral of `logDeriv f` over `[u, v]`.  Unconditional. -/
lemma logDerivSegIntegral_vert (f : ℂ → ℂ) (S u v : ℝ) :
    logDerivSegIntegral f (cpt S u) (cpt S v)
      = I * ∫ y in u..v, logDeriv f ((S : ℂ) + (y : ℂ) * I) := by
  unfold logDerivSegIntegral
  have hpt : ∀ t : ℝ, segPt (cpt S u) (cpt S v) t
      = (S : ℂ) + (((v - u) * t + u : ℝ) : ℂ) * I := by
    intro t
    rw [segPt_mk_vert]
    apply Complex.ext
    · simp [cpt]
    · simp [cpt]; ring
  have hdiff : cpt S v - cpt S u = I * ((v - u : ℝ) : ℂ) := by
    apply Complex.ext <;> simp [cpt]
  have hfun : (fun t : ℝ => (deriv f (segPt (cpt S u) (cpt S v) t)
        / f (segPt (cpt S u) (cpt S v) t)) * (cpt S v - cpt S u))
      = fun t : ℝ => I * ((v - u) • (fun y : ℝ => logDeriv f ((S : ℂ) + (y : ℂ) * I))
          ((v - u) * t + u)) := by
    funext t
    rw [hpt, hdiff, Complex.real_smul]
    simp only [logDeriv_apply]
    ring
  have key := smul_comp_integral (fun y : ℝ => logDeriv f ((S : ℂ) + (y : ℂ) * I)) (v - u) u
  have hb : v - u + u = v := by ring
  rw [hb] at key
  rw [hfun, intervalIntegral.integral_const_mul, key]

/-- The §4 traversal (bottom, right, top, left) of the rectangle `[σ₁, σ₂] × [t₁, t₂]` sums to
the port's four-edge boundary integral of `logDeriv f`.  Unconditional. -/
lemma edge_sum_eq_rectIntegral (f : ℂ → ℂ) (s₁ s₂ t₁ t₂ : ℝ) :
    logDerivSegIntegral f (cpt s₁ t₁) (cpt s₂ t₁) + logDerivSegIntegral f (cpt s₂ t₁) (cpt s₂ t₂)
      + logDerivSegIntegral f (cpt s₂ t₂) (cpt s₁ t₂)
      + logDerivSegIntegral f (cpt s₁ t₂) (cpt s₁ t₁)
    = rectIntegral (logDeriv f) (cpt s₁ t₁) (cpt s₂ t₂) := by
  rw [logDerivSegIntegral_horiz, logDerivSegIntegral_vert, logDerivSegIntegral_horiz,
    logDerivSegIntegral_vert, intervalIntegral.integral_symm s₁ s₂,
    intervalIntegral.integral_symm t₁ t₂]
  simp only [rectIntegral, cpt_re, cpt_im]
  ring

/-! ## 3. H-AP discharged, and the soundness theorem without it -/

/-- **H-AP holds for every `f`.**  The rectangle argument principle in the consequence form of
`Soundness.lean` (`RectArgPrinciple`), proved from the local argument principle
`ArgPrinciple.windingRect_eq_sum_analyticOrder_on` and the §2 vocabulary bridge.  The
degenerate rectangle `σ₁ = σ₂` (allowed by clause C2b) is handled directly with `Z = 0`: the
horizontal edges have zero length and the two vertical edges are reverses of each other. -/
theorem rectArgPrinciple_of_local (f : ℂ → ℂ) : RectArgPrinciple f := by
  intro s₁ s₂ t₁ t₂ _hhalf hs12 _hs2 ht12 U hU hRU hf hbd
  rcases hs12.lt_or_eq with hs | hs
  · -- nondegenerate rectangle: the local argument principle
    have hre : (cpt s₁ t₁).re < (cpt s₂ t₂).re := hs
    have him : (cpt s₁ t₁).im < (cpt s₂ t₂).im := ht12
    have hRect : Rect (cpt s₁ t₁) (cpt s₂ t₂) = rectClosed s₁ s₂ t₁ t₂ := Rect_cpt hs12 ht12.le
    have hFr : RectFrontier (cpt s₁ t₁) (cpt s₂ t₂) = rectBdry s₁ s₂ t₁ t₂ :=
      RectFrontier_cpt hs12 ht12.le
    have hRU' : Rect (cpt s₁ t₁) (cpt s₂ t₂) ⊆ U := hRect ▸ hRU
    have hbd' : ∀ c ∈ RectFrontier (cpt s₁ t₁) (cpt s₂ t₂), f c ≠ 0 := hFr ▸ hbd
    have hzR : cpt s₁ t₁ ∈ Rect (cpt s₁ t₁) (cpt s₂ t₂) :=
      RectFrontier_subset_Rect _ _ (mem_RectFrontier_left_corner _ _)
    have hne : ∃ x ∈ Rect (cpt s₁ t₁) (cpt s₂ t₂), f x ≠ 0 :=
      ⟨cpt s₁ t₁, hzR, hbd' _ (mem_RectFrontier_left_corner _ _)⟩
    have hAn : AnalyticOnNhd ℂ f (Rect (cpt s₁ t₁) (cpt s₂ t₂)) :=
      (hf.analyticOnNhd hU).mono hRU'
    have hfin := finite_zeros_Rect_on hU hRU' hf hne
    classical
    have hS : ∀ p, p ∈ hfin.toFinset ↔ (p ∈ Rect (cpt s₁ t₁) (cpt s₂ t₂) ∧ f p = 0) :=
      fun p => by simp [Set.Finite.mem_toFinset]
    have hW := windingRect_eq_sum_analyticOrder_on hre him hU hRU' hf hbd' hfin.toFinset hS
    refine ⟨∑ p ∈ hfin.toFinset, analyticOrderNatAt f p, ?_, ?_, ?_⟩
    · -- (i) the winding identity
      have h2πI : (2 * (π : ℂ) * I) ≠ 0 :=
        mul_ne_zero (mul_ne_zero two_ne_zero (ofReal_ne_zero.mpr Real.pi_ne_zero)) I_ne_zero
      have hRI : rectIntegral (logDeriv f) (cpt s₁ t₁) (cpt s₂ t₂)
          = 2 * (π : ℂ) * I * ((∑ p ∈ hfin.toFinset, analyticOrderNatAt f p : ℕ) : ℂ) := by
        rw [windingRect] at hW
        push_cast
        exact (inv_mul_eq_iff_eq_mul₀ h2πI).mp hW
      have hcast : 2 * (π : ℂ) * I * ((∑ p ∈ hfin.toFinset, analyticOrderNatAt f p : ℕ) : ℂ)
          = ((2 * π * ((∑ p ∈ hfin.toFinset, analyticOrderNatAt f p : ℕ) : ℝ) : ℝ) : ℂ) * I := by
        push_cast
        ring
      simp only [argIncrement]
      rw [← Complex.add_im, ← Complex.add_im, ← Complex.add_im, edge_sum_eq_rectIntegral, hRI,
        hcast, Complex.mul_I_im, Complex.ofReal_re]
    · -- (ii) Z = 0 → no zero in the open rectangle
      intro hZ s hs hfs
      have hsR : s ∈ Rect (cpt s₁ t₁) (cpt s₂ t₂) := by
        rw [hRect]
        exact ⟨hs.1.le, hs.2.1.le, hs.2.2.1.le, hs.2.2.2.le⟩
      have hsS : s ∈ hfin.toFinset := (hS s).mpr ⟨hsR, hfs⟩
      have h0 : analyticOrderNatAt f s = 0 := Finset.sum_eq_zero_iff.mp hZ s hsS
      rw [analyticOrderNatAt, ENat.toNat_eq_zero] at h0
      rcases h0 with h0 | h0
      · exact ((hAn s hsR).analyticOrderAt_eq_zero.mp h0) hfs
      · exact analyticOrderAt_ne_top_of_analyticOnNhd (isPreconnected_Rect _ _) hAn hne hsR h0
    · -- (iii) Z ≥ 1 → a zero in the open rectangle
      intro hZ
      have hne0 : ∑ p ∈ hfin.toFinset, analyticOrderNatAt f p ≠ 0 := by omega
      obtain ⟨p, hp⟩ := Finset.nonempty_of_sum_ne_zero hne0
      obtain ⟨hpR, hp0⟩ := (hS p).mp hp
      have hIoo := mem_Ioo_of_zero_mem_Rect hre him hbd' hpR hp0
      exact ⟨p, ⟨hIoo.1.1, hIoo.1.2, hIoo.2.1, hIoo.2.2⟩, hp0⟩
  · -- degenerate rectangle σ₁ = σ₂ (clause C2b): Z = 0
    subst hs
    refine ⟨0, ?_, ?_, ?_⟩
    · have hB : logDerivSegIntegral f (cpt s₁ t₁) (cpt s₁ t₁) = 0 := by
        simp [logDerivSegIntegral]
      have hT : logDerivSegIntegral f (cpt s₁ t₂) (cpt s₁ t₂) = 0 := by
        simp [logDerivSegIntegral]
      have hL : logDerivSegIntegral f (cpt s₁ t₂) (cpt s₁ t₁)
          = -logDerivSegIntegral f (cpt s₁ t₁) (cpt s₁ t₂) := by
        rw [logDerivSegIntegral_vert, logDerivSegIntegral_vert, intervalIntegral.integral_symm t₁ t₂]
        ring
      simp only [argIncrement, hB, hT, hL, Complex.zero_im, Complex.neg_im]
      simp
    · intro _ s hs
      exact absurd (lt_trans hs.1 hs.2.1) (lt_irrefl _)
    · intro h
      omega

/-- H-AP for ζ, the instance `cert_of_checkW1` consumes. -/
theorem rectArgPrinciple_riemannZeta : RectArgPrinciple riemannZeta :=
  rectArgPrinciple_of_local riemannZeta

/-- **W1 checker soundness with H-AP discharged.**  Same conclusion and same hypotheses as
`cert_of_checkW1`, minus `RectArgPrinciple riemannZeta`, which is now a theorem.  The single
remaining displayed hypothesis is H-ENCL (`W1EnclOK riemannZeta d`): the honest label for an
accepted ζ transcript is "kernel-checked modulo the displayed hypothesis H-ENCL (producers
untrusted)". -/
theorem cert_of_checkW1_ap (d : W1Data) (hc : checkW1 d = true)
    (hEncl : W1EnclOK riemannZeta d) :
    (1 ≤ d.m → ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1
        ∧ T1 d < ρ.im ∧ ρ.im < T2 d)
    ∧ (d.m = 0 → ∀ s ∈ W1Rect d, riemannZeta s ≠ 0) :=
  cert_of_checkW1 d hc hEncl rectArgPrinciple_riemannZeta

end W1
end Zeta23

end
