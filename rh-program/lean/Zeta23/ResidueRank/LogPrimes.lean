/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and imports nothing from it: its only import is Mathlib.
-/
/-
Zeta23/ResidueRank/LogPrimes.lean — the ARITHMETIC CORE of Theorem R (rh-program/results/beta-shapes-s35/NOTE.md §2.3,
H3.3(b) and the proof of Theorem R; read-O.md §2.5, the reader's converse): the logarithms of the rational primes are
linearly independent over ℚ, a family of positive integers N_p with p ∣ N_p has logarithms spanning an
infinite-dimensional ℚ-space, and logarithms of integers whose prime factors lie in a finite set S span a ℚ-space of
dimension at most #S.  Unit brief rh-program/results/theoremR-lean-s36/UNIT-BRIEF.md (items 1–3, rung 1 of 10(l)); build
record rh-program/results/theoremR-lean-s36/BUILD-NOTES.md.

  `expVec n`                        — the exponent vector q ↦ v_q(n) of n on the primes, with rational entries;
  `linearCombination_expVec`        — for n ≠ 0, Σ_q v_q(n) · log q = log n (induction on prime factors);
  `log_primes_linearIndependent`    — (1) NOTE H3.3(b): {log p : p prime} is ℚ-linearly independent.  Route: over ℤ first
                                       (Mathlib's `LinearIndependent.iff_fractionRing ℤ ℚ` clears the denominators), then an
                                       integer relation Σ m_p log p = 0 makes x = Π p^{m_p} ∈ ℚ equal to 1, and the q-adic
                                       valuation of x is m_q (unique factorization in the form of `padicValRat`);
  `span_log_not_finite`             — (2) the core of Theorem R: if p ∣ N p and N p > 0 for every prime p, the ℚ-span of
                                       {log N p} is not finite-dimensional (finitely many generators have coordinates on a
                                       finite set of primes; a prime q outside it has coordinate v_q(N q) ≥ 1 on log N q);
  `rank_span_log_le`                — (3) the reader's converse: prime factors in a finite S ⟹ rank ≤ #S (the displayed
                                       positivity of the N i is not used: `rank_span_log_le_of_supp`, errata E4).

WHAT IS NOT HERE.  Nothing about the pair's geometry (the SPEC's A6–A8), no target Y, nothing about ζ or its zeros.

Trust model: proved from Mathlib alone; the three standard axioms only (rung1-print-axioms.log).
-/
import Mathlib

namespace Zeta23.ResidueRank

open Finsupp

/-! ## §1 The exponent vector of `n` on the primes -/

/-- `logP p = log p` for a prime `p`: the family of item (1), as a named function (so that rewriting never has to see
the coercion `Nat.Primes → ℕ` under a binder). -/
noncomputable def logP (p : Nat.Primes) : ℝ := Real.log ((p : ℕ) : ℝ)

/-- `expVec n`: the exponent vector of `n` on the primes, `q ↦ v_q(n)` (the factorization of `n` restricted to
`Nat.Primes`), with rational entries. -/
noncomputable def expVec (n : ℕ) : Nat.Primes →₀ ℚ :=
  Finsupp.mapRange (fun k : ℕ => (k : ℚ)) Nat.cast_zero
    (Finsupp.comapDomain (fun p : Nat.Primes => (p : ℕ)) n.factorization
      Subtype.val_injective.injOn)

theorem expVec_apply (n : ℕ) (q : Nat.Primes) :
    expVec n q = ((n.factorization (q : ℕ) : ℕ) : ℚ) :=
  rfl

theorem expVec_one : expVec 1 = 0 := by
  ext q
  rw [expVec_apply, Nat.factorization_one]
  rfl

theorem expVec_mul {a b : ℕ} (ha : a ≠ 0) (hb : b ≠ 0) :
    expVec (a * b) = expVec a + expVec b := by
  ext q
  rw [Finsupp.add_apply, expVec_apply, expVec_apply, expVec_apply, Nat.factorization_mul ha hb,
    Finsupp.add_apply, Nat.cast_add]

theorem expVec_prime (P : Nat.Primes) : expVec (P : ℕ) = Finsupp.single P 1 := by
  ext q
  rw [expVec_apply, P.prop.factorization]
  by_cases h : P = q
  · subst h
    rw [Finsupp.single_eq_same, Finsupp.single_eq_same, Nat.cast_one]
  · have h' : (P : ℕ) ≠ (q : ℕ) := fun e => h (Subtype.ext e)
    rw [Finsupp.single_eq_of_ne' h, Finsupp.single_eq_of_ne' h', Nat.cast_zero]

theorem linearCombination_expVec_prime (P : Nat.Primes) :
    Finsupp.linearCombination ℚ logP (expVec (P : ℕ)) = Real.log ((P : ℕ) : ℝ) := by
  rw [expVec_prime P, Finsupp.linearCombination_single, one_smul]
  rfl

/-- For `n ≠ 0`: `Σ_q v_q(n) · log q = log n`. -/
theorem linearCombination_expVec {n : ℕ} (hn : n ≠ 0) :
    Finsupp.linearCombination ℚ logP (expVec n) = Real.log (n : ℝ) := by
  induction n using induction_on_primes with
  | zero => exact absurd rfl hn
  | one => rw [expVec_one, map_zero, Nat.cast_one, Real.log_one]
  | prime_mul p a hp ih =>
    have ha : a ≠ 0 := by
      rintro rfl
      simp at hn
    have hP : Finsupp.linearCombination ℚ logP (expVec p) = Real.log (p : ℝ) :=
      linearCombination_expVec_prime ⟨p, hp⟩
    rw [expVec_mul hp.ne_zero ha, map_add, ih ha, hP, Nat.cast_mul,
      Real.log_mul (by exact_mod_cast hp.ne_zero) (by exact_mod_cast ha)]

/-- For `n ≠ 0`, `log n` lies in the ℚ-span of the logarithms of the primes. -/
theorem log_mem_span_logP {n : ℕ} (hn : n ≠ 0) :
    Real.log (n : ℝ) ∈ Submodule.span ℚ (Set.range logP) := by
  rw [← linearCombination_expVec hn, ← Finsupp.range_linearCombination]
  exact LinearMap.mem_range_self _ _

/-! ## §2 Item (1): the logarithms of the primes are ℚ-linearly independent -/

/-- The `q`-adic valuation of a finite product of nonzero rationals is the sum of the valuations. -/
theorem padicValRat_finset_prod {ι : Type*} (q : ℕ) [Fact q.Prime] (s : Finset ι) (f : ι → ℚ)
    (hf : ∀ i ∈ s, f i ≠ 0) :
    padicValRat q (∏ i ∈ s, f i) = ∑ i ∈ s, padicValRat q (f i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp
  | insert i s hi ih =>
    have hfi : f i ≠ 0 := hf i (Finset.mem_insert_self i s)
    have hfs : ∀ j ∈ s, f j ≠ 0 := fun j hj => hf j (Finset.mem_insert_of_mem hj)
    rw [Finset.prod_insert hi, Finset.sum_insert hi,
      padicValRat.mul hfi (Finset.prod_ne_zero_iff.mpr hfs), ih hfs]

/-- The `q`-adic valuation of a prime `p` is `1` if `p = q` and `0` otherwise. -/
theorem padicValRat_prime (q p : Nat.Primes) :
    padicValRat (q : ℕ) ((p : ℕ) : ℚ) = if p = q then 1 else 0 := by
  have : Fact (q : ℕ).Prime := ⟨q.prop⟩
  have : Fact (p : ℕ).Prime := ⟨p.prop⟩
  split_ifs with h
  · subst h
    exact padicValRat.self p.prop.one_lt
  · rw [← padicValRat_of_nat, padicValNat_primes (fun e => h (Subtype.ext e.symm))]
    simp

theorem linearIndependent_logP : LinearIndependent ℚ logP := by
  rw [← LinearIndependent.iff_fractionRing ℤ ℚ, linearIndependent_iff']
  intro s m hm q hq
  have hpos : ∀ p : Nat.Primes, (0 : ℚ) < ((p : ℕ) : ℚ) := fun p => by exact_mod_cast p.prop.pos
  have hne : ∀ p ∈ s, ((p : ℕ) : ℚ) ^ (m p) ≠ 0 := fun p _ => (zpow_pos (hpos p) _).ne'
  -- the rational number x = Π_{p ∈ s} p ^ m_p has logarithm Σ m_p log p = 0
  have hlog : Real.log (((∏ p ∈ s, ((p : ℕ) : ℚ) ^ (m p) : ℚ)) : ℝ) = 0 := by
    rw [Rat.cast_prod, Real.log_prod]
    · simp only [Rat.cast_zpow, Rat.cast_natCast, Real.log_zpow]
      simpa [zsmul_eq_mul, logP] using hm
    · intro p hp
      exact_mod_cast hne p hp
  have hx1 : (∏ p ∈ s, ((p : ℕ) : ℚ) ^ (m p) : ℚ) = 1 := by
    have hx0 : (0 : ℝ) < ((∏ p ∈ s, ((p : ℕ) : ℚ) ^ (m p) : ℚ) : ℝ) := by
      exact_mod_cast Finset.prod_pos fun p _ => zpow_pos (hpos p) _
    exact_mod_cast Real.eq_one_of_pos_of_log_eq_zero hx0 hlog
  -- its q-adic valuation is m_q
  have : Fact (q : ℕ).Prime := ⟨q.prop⟩
  have hval := padicValRat_finset_prod (q : ℕ) s (fun p => ((p : ℕ) : ℚ) ^ (m p)) hne
  rw [hx1, padicValRat.one] at hval
  simp only [padicValRat.zpow, padicValRat_prime, mul_ite, mul_one, mul_zero,
    Finset.sum_ite_eq', if_pos hq] at hval
  exact hval.symm

/-- **(1) NOTE H3.3(b)**: the logarithms of the rational primes are linearly independent over ℚ. -/
theorem log_primes_linearIndependent :
    LinearIndependent ℚ (fun p : Nat.Primes => Real.log ((p : ℕ) : ℝ)) :=
  linearIndependent_logP

/-! ## §3 Item (2): Theorem R's arithmetic core -/

/-- **(2) Theorem R, arithmetic core**: if every prime `p` divides a positive integer `N p`, the ℚ-span of the real
numbers `log (N p)` is not finite-dimensional. -/
theorem span_log_not_finite (N : Nat.Primes → ℕ) (hpos : ∀ p, 0 < N p)
    (hdvd : ∀ p : Nat.Primes, (p : ℕ) ∣ N p) :
    ¬ Module.Finite ℚ
      (Submodule.span ℚ (Set.range fun p : Nat.Primes => Real.log ((N p : ℕ) : ℝ))) := by
  intro hfin
  have hli := linearIndependent_logP
  have hMV : Submodule.span ℚ (Set.range fun p : Nat.Primes => Real.log ((N p : ℕ) : ℝ))
      ≤ Submodule.span ℚ (Set.range logP) := by
    rw [Submodule.span_le]
    rintro _ ⟨p, rfl⟩
    exact log_mem_span_logP (hpos p).ne'
  -- ψ: the coordinates on the primes of the elements of the span
  let ψ := hli.repr ∘ₗ Submodule.inclusion hMV
  obtain ⟨k, g, hg⟩ := Module.Finite.exists_fin (R := ℚ)
    (M := Submodule.span ℚ (Set.range fun p : Nat.Primes => Real.log ((N p : ℕ) : ℝ)))
  -- S: the primes met by the coordinates of the finitely many generators
  let S : Finset Nat.Primes := Finset.univ.biUnion fun j => (ψ (g j)).support
  have hS : ∀ y, ψ y ∈ Finsupp.supported ℚ ℚ (S : Set Nat.Primes) := by
    intro y
    have hy : y ∈ Submodule.span ℚ (Set.range g) := hg ▸ Submodule.mem_top
    have hmap : ψ y ∈ (Submodule.span ℚ (Set.range g)).map ψ := Submodule.mem_map_of_mem hy
    rw [Submodule.map_span] at hmap
    refine (Submodule.span_le.mpr ?_) hmap
    rintro _ ⟨_, ⟨j, rfl⟩, rfl⟩
    rw [SetLike.mem_coe, Finsupp.mem_supported]
    intro q hq
    exact Finset.mem_coe.mpr (Finset.mem_biUnion.mpr ⟨j, Finset.mem_univ _, hq⟩)
  -- a prime q outside S (there are infinitely many primes)
  obtain ⟨q, hq⟩ := Infinite.exists_notMem_finset S
  let y : Submodule.span ℚ (Set.range fun p : Nat.Primes => Real.log ((N p : ℕ) : ℝ)) :=
    ⟨Real.log ((N q : ℕ) : ℝ), Submodule.subset_span ⟨q, rfl⟩⟩
  have hψy : ψ y = expVec (N q) := by
    apply hli.repr_eq
    rw [linearCombination_expVec (hpos q).ne']
    rfl
  have h0 : ψ y q = 0 := by
    by_contra hne
    have hsub := (Finsupp.mem_supported ℚ (ψ y)).mp (hS y)
    exact hq (Finset.mem_coe.mp (hsub (Finsupp.mem_support_iff.mpr hne)))
  rw [hψy, expVec_apply] at h0
  have hv : 0 < (N q).factorization (q : ℕ) :=
    q.prop.factorization_pos_of_dvd (hpos q).ne' (hdvd q)
  have hv' : (((N q).factorization (q : ℕ) : ℕ) : ℚ) ≠ 0 := by exact_mod_cast hv.ne'
  exact hv' h0

/-! ## §4 Item (3): the converse rank bound -/

/-- The converse bound with no positivity hypothesis (PREDERIVATION-ERRATA E4, kernel-checked; program side only): an
`N i = 0` contributes `Real.log 0 = 0`. -/
theorem rank_span_log_le_of_supp {ι : Type} (S : Finset ℕ) (N : ι → ℕ)
    (hsupp : ∀ i p, p.Prime → p ∣ N i → p ∈ S) :
    Module.rank ℚ (Submodule.span ℚ (Set.range fun i => Real.log ((N i : ℕ) : ℝ)))
      ≤ (S.card : Cardinal) := by
  classical
  have hle : Submodule.span ℚ (Set.range fun i => Real.log ((N i : ℕ) : ℝ))
      ≤ Submodule.span ℚ ((S.image fun p : ℕ => Real.log (p : ℝ) : Finset ℝ) : Set ℝ) := by
    rw [Submodule.span_le]
    rintro _ ⟨i, rfl⟩
    show Real.log ((N i : ℕ) : ℝ) ∈ _
    rcases Nat.eq_zero_or_pos (N i) with h0 | hpos
    · rw [h0, Nat.cast_zero, Real.log_zero]
      exact Submodule.zero_mem _
    rw [← linearCombination_expVec hpos.ne', Finsupp.linearCombination_apply, Finsupp.sum]
    refine Submodule.sum_mem _ fun q hq => Submodule.smul_mem _ _ (Submodule.subset_span ?_)
    have hq' : (N i).factorization (q : ℕ) ≠ 0 := by
      rw [Finsupp.mem_support_iff, expVec_apply] at hq
      exact_mod_cast hq
    have hqS : (q : ℕ) ∈ S := hsupp i q q.prop (Nat.dvd_of_factorization_pos hq')
    exact Finset.mem_coe.mpr (Finset.mem_image.mpr ⟨q, hqS, rfl⟩)
  calc Module.rank ℚ (Submodule.span ℚ (Set.range fun i => Real.log ((N i : ℕ) : ℝ)))
      ≤ Module.rank ℚ (Submodule.span ℚ ((S.image fun p : ℕ => Real.log (p : ℝ) : Finset ℝ) : Set ℝ)) :=
        Submodule.rank_mono hle
    _ ≤ ((S.image fun p : ℕ => Real.log (p : ℝ)).card : Cardinal) := rank_span_finset_le _
    _ ≤ (S.card : Cardinal) := by exact_mod_cast Finset.card_image_le

/-- **(3) The converse bound**: logarithms of positive integers whose prime factors lie in a finite set `S` span a
ℚ-space of dimension at most `#S`.  The displayed positivity is not needed (`rank_span_log_le_of_supp`). -/
theorem rank_span_log_le {ι : Type} (S : Finset ℕ) (N : ι → ℕ) (_hpos : ∀ i, 0 < N i)
    (hsupp : ∀ i p, p.Prime → p ∣ N i → p ∈ S) :
    Module.rank ℚ (Submodule.span ℚ (Set.range fun i => Real.log ((N i : ℕ) : ℝ)))
      ≤ (S.card : Cardinal) :=
  rank_span_log_le_of_supp S N hsupp

end Zeta23.ResidueRank
