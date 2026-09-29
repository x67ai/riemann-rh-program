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
comparator/Solution/WeilContainmentC2One.lean — the UNTRUSTED comparator solution module for the topic `WeilContainmentC2One`
(rung 1 of the H5 unit, Session 32): the statement of Challenge/WeilContainmentC2One.lean, byte-identical, PROVED over Mathlib
alone.  The proof is the general one (every band L, namespace `WeilContainmentC2One.Proof`, theorem `interpolant`), instantiated
at L = log 3.  Construction (results/h5-c2-lean-s32/PREDERIVATION-ERRATA.md E3): with I the interior indices
{n : 2 ≤ n ≤ ⌊e^L⌋, log n < L}, if I is empty the witness is k = 0; otherwise the witness is k(u) = P(u²)·φ(u), where φ is one
Mathlib bump `ContDiffBump (0 : ℝ)` with rIn = log (max I) and rOut = L (so φ = 1 at every ±log n, n ∈ I, and φ = 0 wherever
|u| ≥ L) and P is Mathlib's Lagrange interpolant with nodes (log n)² and values (1/2)·n^{1/2−a}·g(log n), n ∈ I.  k is even
because u² and φ are; C² because a polynomial, ofReal, u ↦ u² and φ are C^∞; supported in [−L, L] because φ is; and its prime side
is the tilted one term by term (n ∈ I by the rpow identity Λ/√n · n^{1/2−a} = Λ n^{−a}; n ∉ I by Λ(0) = Λ(1) = 0 or by φ(±log n) = 0
together with g(log n) = 0 for log n ≥ L, which uses only the continuity of g and its support).  The evenness of g is not used.
This module never imports the challenge and never imports Solution.WeilContainment (the D5 cutoff is re-proved here, so the topic
is self-contained).  Nothing in this file is part of the trusted base: comparator re-checks that the theorem below has exactly the
statement of its Challenge namesake and uses only the permitted axioms.
-/
import ChallengeDeps.WeilContainment

noncomputable section

open WeilContainment

namespace WeilContainmentC2One.Proof

/-- a polynomial over ℂ is C^n as a function ℂ → ℂ, for every n. -/
theorem contDiff_poly_eval {n : WithTop ℕ∞} (p : Polynomial ℂ) :
    ContDiff ℂ n (fun z : ℂ => p.eval z) := by
  refine Polynomial.induction_on' p ?_ ?_
  · intro p q hp hq
    simpa only [Polynomial.eval_add] using hp.add hq
  · intro k c
    simpa only [Polynomial.eval_monomial] using (contDiff_const (c := c)).mul (contDiff_id.pow k)

/-- a continuous g with tsupport in [−L, L] vanishes on [L, ∞): the zero set is closed and contains (L, ∞). -/
theorem eq_zero_of_le (L : ℝ) (g : ℝ → ℂ) (hc : Continuous g) (hs : tsupport g ⊆ Set.Icc (-L) L)
    (u : ℝ) (hu : L ≤ u) : g u = 0 := by
  have hcl : IsClosed {x : ℝ | g x = 0} := isClosed_eq hc continuous_const
  have hsub : Set.Ioi L ⊆ {x : ℝ | g x = 0} := by
    intro x hx
    apply image_eq_zero_of_notMem_tsupport
    intro hmem
    exact absurd (hs hmem).2 (not_le.mpr hx)
  have hIci : Set.Ici L ⊆ {x : ℝ | g x = 0} := by
    rw [← closure_Ioi L]
    exact hcl.closure_subset_iff.mpr hsub
  exact hIci (Set.mem_Ici.mpr hu)

/-- the D5 cutoff (`weilContainment_cutoff`), re-proved so that this module imports only the trusted vocabulary. -/
theorem cutoff (a L : ℝ) (g : ℝ → ℂ) (hg : tsupport g ⊆ Set.Icc (-L) L) :
    tiltedPrimeSide a g = ∑ n ∈ Finset.range (⌊Real.exp L⌋₊ + 1),
        ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) * g (Real.log n) := by
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

/-- the interior indices: 2 ≤ n ≤ ⌊e^L⌋ with log n < L. -/
def interior (L : ℝ) : Finset ℕ :=
  (Finset.range (⌊Real.exp L⌋₊ + 1)).filter (fun n => 2 ≤ n ∧ Real.log n < L)

theorem mem_interior {L : ℝ} {n : ℕ} :
    n ∈ interior L ↔ n < ⌊Real.exp L⌋₊ + 1 ∧ (2 ≤ n ∧ Real.log n < L) := by
  simp only [interior, Finset.mem_filter, Finset.mem_range]

/-- for n ≥ 2 outside the interior set, L ≤ log n. -/
theorem le_log_of_notMem {L : ℝ} {n : ℕ} (h2 : 2 ≤ n) (hn : n ∉ interior L) : L ≤ Real.log n := by
  rw [mem_interior] at hn
  by_cases hr : n < ⌊Real.exp L⌋₊ + 1
  · by_contra hlt
    exact hn ⟨hr, h2, not_le.mp hlt⟩
  · have hn' : ⌊Real.exp L⌋₊ < n := by omega
    have hlt : Real.exp L < n := Nat.lt_of_floor_lt hn'
    exact ((Real.lt_log_iff_exp_lt (lt_trans (Real.exp_pos L) hlt)).mpr hlt).le

/-- the tilted summand vanishes at every n ≤ ⌊e^L⌋ outside the interior set (n ≤ 1 by Λ = 0; otherwise by g = 0 on [L, ∞)). -/
theorem tilted_term_zero (a L : ℝ) (g : ℝ → ℂ) (hc : Continuous g) (hs : tsupport g ⊆ Set.Icc (-L) L)
    (n : ℕ) (hnI : n ∉ interior L) :
    ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) * g (Real.log n) = 0 := by
  by_cases h2 : 2 ≤ n
  · rw [eq_zero_of_le L g hc hs _ (le_log_of_notMem h2 hnI), mul_zero]
  · have : n = 0 ∨ n = 1 := by omega
    rcases this with rfl | rfl
    · simp
    · simp [ArithmeticFunction.vonMangoldt_apply_one]

/-- the tilted prime side is the finite sum over the interior indices. -/
theorem tilted_eq_sum_interior (a L : ℝ) (g : ℝ → ℂ) (hc : Continuous g)
    (hs : tsupport g ⊆ Set.Icc (-L) L) :
    tiltedPrimeSide a g = ∑ n ∈ interior L,
        ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) * g (Real.log n) := by
  rw [cutoff a L g hs]
  symm
  apply Finset.sum_subset (Finset.filter_subset _ _)
  intro n _ hnI
  exact tilted_term_zero a L g hc hs n hnI

/-- the interpolation nodes (log n)², as complex numbers. -/
def node (n : ℕ) : ℂ := (((Real.log n) ^ 2 : ℝ) : ℂ)

/-- the interpolated values (1/2)·n^{1/2−a}·g(log n). -/
def value (a : ℝ) (g : ℝ → ℂ) (n : ℕ) : ℂ :=
  (1 / 2 : ℂ) * (((n : ℝ) ^ (1 / 2 - a) : ℝ) : ℂ) * g (Real.log n)

/-- the nodes are pairwise distinct on the interior set (log is injective on [1, ∞) and squaring on [0, ∞)). -/
theorem node_injOn (L : ℝ) : Set.InjOn node (interior L : Set ℕ) := by
  intro n hn m hm h
  rw [Finset.mem_coe, mem_interior] at hn hm
  obtain ⟨-, hn2, -⟩ := hn
  obtain ⟨-, hm2, -⟩ := hm
  have hn' : (1 : ℝ) ≤ n := by exact_mod_cast (by omega : 1 ≤ n)
  have hm' : (1 : ℝ) ≤ m := by exact_mod_cast (by omega : 1 ≤ m)
  have h' : (Real.log n) ^ 2 = (Real.log m) ^ 2 := by
    unfold node at h
    exact_mod_cast h
  have hlog : Real.log n = Real.log m :=
    (pow_left_inj₀ (Real.log_nonneg hn') (Real.log_nonneg hm') two_ne_zero).mp h'
  have hnm : (n : ℝ) = m :=
    Real.log_injOn_pos (Set.mem_Ioi.mpr (by linarith)) (Set.mem_Ioi.mpr (by linarith)) hlog
  exact_mod_cast hnm

/-- the real-power identity (Λ(n)/√n)·n^{1/2−a} = Λ(n)·n^{−a} for n ≥ 1, cast to ℂ. -/
theorem rpow_identity (a : ℝ) (n : ℕ) (hn : 0 < n) :
    ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) * (((n : ℝ) ^ (1 / 2 - a) : ℝ) : ℂ)
      = ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have h3 : ArithmeticFunction.vonMangoldt n / Real.sqrt n * (n : ℝ) ^ (1 / 2 - a)
      = ArithmeticFunction.vonMangoldt n * (n : ℝ) ^ (-a) := by
    rw [Real.sqrt_eq_rpow, div_eq_mul_inv, ← Real.rpow_neg hn'.le, mul_assoc, ← Real.rpow_add hn']
    congr 2; ring
  rw [← Complex.ofReal_mul, h3, Complex.ofReal_mul]

/-- the general theorem, for every band L: the evenness of g is not needed. -/
theorem interpolant (a L : ℝ) (g : ℝ → ℂ) (hc : Continuous g) (hs : tsupport g ⊆ Set.Icc (-L) L) :
    ∃ k : ℝ → ℂ, (∀ u, k (-u) = k u) ∧ ContDiff ℝ 2 k ∧
      tsupport k ⊆ Set.Icc (-L) L ∧ primeSide k = tiltedPrimeSide a g := by
  rw [tilted_eq_sum_interior a L g hc hs]
  by_cases hI : (interior L).Nonempty
  · -- the interior set is nonempty: one bump at 0 times the Lagrange interpolant in u²
    set M : ℕ := (interior L).max' hI with hMdef
    have hM : M ∈ interior L := Finset.max'_mem _ hI
    obtain ⟨-, hM2, hMlt⟩ := mem_interior.mp hM
    have hM1 : (1 : ℝ) < M := by exact_mod_cast (by omega : 1 < M)
    have hrIn : 0 < Real.log M := Real.log_pos hM1
    let φ : ContDiffBump (0 : ℝ) := ⟨Real.log M, L, hrIn, hMlt⟩
    set P : Polynomial ℂ := Lagrange.interpolate (interior L) node (value a g) with hPdef
    -- φ = 1 at log n for n in the interior set
    have hφ1 : ∀ n ∈ interior L, φ (Real.log n) = 1 := by
      intro n hn
      obtain ⟨-, hn2, -⟩ := mem_interior.mp hn
      apply φ.one_of_mem_closedBall
      rw [Metric.mem_closedBall, dist_zero_right, Real.norm_eq_abs]
      have hn1 : (1 : ℝ) ≤ n := by exact_mod_cast (by omega : 1 ≤ n)
      have hnM : (n : ℝ) ≤ M := by exact_mod_cast Finset.le_max' _ n hn
      rw [abs_of_nonneg (Real.log_nonneg hn1)]
      exact Real.log_le_log (by linarith) hnM
    -- φ = 0 at log n whenever L ≤ log n
    have hφ0 : ∀ n : ℕ, L ≤ Real.log n → φ (Real.log n) = 0 := by
      intro n hL
      apply φ.zero_of_le_dist
      rw [dist_zero_right, Real.norm_eq_abs]
      exact hL.trans (le_abs_self _)
    have hφeven : ∀ u : ℝ, φ (-u) = φ u := fun u => φ.neg u
    refine ⟨fun u => Polynomial.eval (((u ^ 2 : ℝ)) : ℂ) P * ((φ u : ℝ) : ℂ), ?_, ?_, ?_, ?_⟩
    · -- even
      intro u
      simp only [neg_sq, hφeven]
    · -- C²
      have hP : ContDiff ℝ 2 (fun z : ℂ => P.eval z) := (contDiff_poly_eval P).restrict_scalars ℝ
      have hsq : ContDiff ℝ 2 (fun u : ℝ => (((u ^ 2 : ℝ)) : ℂ)) :=
        Complex.ofRealCLM.contDiff.comp (contDiff_id.pow 2)
      have hφC : ContDiff ℝ 2 (fun u : ℝ => ((φ u : ℝ) : ℂ)) := by
        have h := φ.contDiff (n := 2)
        exact Complex.ofRealCLM.contDiff.comp (by exact_mod_cast h)
      exact (hP.comp hsq).mul hφC
    · -- the band
      have h1 : tsupport (fun u : ℝ => ((φ u : ℝ) : ℂ)) = tsupport φ := by
        unfold tsupport
        congr 1
        ext u
        simp only [Function.mem_support, ne_eq, Complex.ofReal_eq_zero]
      calc tsupport (fun u : ℝ => Polynomial.eval (((u ^ 2 : ℝ)) : ℂ) P * ((φ u : ℝ) : ℂ))
          ⊆ tsupport (fun u : ℝ => ((φ u : ℝ) : ℂ)) := tsupport_mul_subset_right
        _ = tsupport φ := h1
        _ = Metric.closedBall 0 L := φ.tsupport_eq
        _ = Set.Icc (-L) L := by rw [Real.closedBall_eq_Icc, zero_sub, zero_add]
    · -- the prime side
      unfold primeSide
      rw [tsum_eq_sum (s := interior L)]
      · apply Finset.sum_congr rfl
        intro n hn
        obtain ⟨-, hn2, -⟩ := mem_interior.mp hn
        have hval : Polynomial.eval (((Real.log n ^ 2 : ℝ)) : ℂ) P = value a g n :=
          Lagrange.eval_interpolate_at_node (node_injOn L) hn
        have hk : Polynomial.eval (((Real.log n ^ 2 : ℝ)) : ℂ) P * ((φ (Real.log n) : ℝ) : ℂ)
            = value a g n := by
          rw [hval, hφ1 n hn, Complex.ofReal_one, mul_one]
        simp only [neg_sq, hφeven, hk]
        rw [← rpow_identity a n (by omega)]
        unfold value
        ring
      · intro n hn
        by_cases h2 : 2 ≤ n
        · have h0 : φ (Real.log n) = 0 := hφ0 n (le_log_of_notMem h2 hn)
          simp only [neg_sq, hφeven, h0, Complex.ofReal_zero, mul_zero, add_zero]
        · have : n = 0 ∨ n = 1 := by omega
          rcases this with rfl | rfl
          · simp
          · simp [ArithmeticFunction.vonMangoldt_apply_one]
  · -- the interior set is empty: the witness is 0
    rw [Finset.not_nonempty_iff_eq_empty] at hI
    rw [hI, Finset.sum_empty]
    refine ⟨fun _ => 0, fun _ => rfl, contDiff_const, ?_, ?_⟩
    · rw [tsupport_eq_empty_iff.mpr rfl]
      exact Set.empty_subset _
    · unfold primeSide
      simp

end WeilContainmentC2One.Proof

open WeilContainmentC2One.Proof

/-- **the C² interpolant at the band L = log 3**: for every real a and every even continuous g supported in [−log 3, log 3],
some even C² k on the same band has `primeSide k = tiltedPrimeSide a g`. -/
theorem weilContainment_c2_interpolant_log3 :
    ∀ (a : ℝ) (g : ℝ → ℂ), (∀ u, g (-u) = g u) → Continuous g →
      tsupport g ⊆ Set.Icc (-(Real.log 3)) (Real.log 3) →
      ∃ k : ℝ → ℂ, (∀ u, k (-u) = k u) ∧ ContDiff ℝ 2 k ∧
        tsupport k ⊆ Set.Icc (-(Real.log 3)) (Real.log 3) ∧ primeSide k = tiltedPrimeSide a g :=
  fun a g _ hc hs => interpolant a (Real.log 3) g hc hs
