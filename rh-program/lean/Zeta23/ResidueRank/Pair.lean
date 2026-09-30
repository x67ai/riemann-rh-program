/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and imports nothing from it beyond Zeta23/ResidueRank/LogPrimes.lean (this unit's own module).
-/
/-
Zeta23/ResidueRank/Pair.lean — LEMMA F and THEOREM R ON THE ABSTRACT PAIR (rh-program/results/beta-shapes-s35/NOTE.md §2.0
Lemma F (a), (b); §2.3 Theorem R and T3 at B = Spec Z; read-O.md §2.2, §2.5).  Unit brief
rh-program/results/theoremR-lean-s36/UNIT-BRIEF.md (items 4–6); build record rh-program/results/theoremR-lean-s36/BUILD-NOTES.md.

THE ABSTRACT PAIR.  `cls : ℕ → ι` is the map n ↦ c(Γ_n) on the ghost components (Γ_1 the diagonal), `v : ι → ℝ` is the
diagonal row D ↦ (Δ · D)_Y of the target's real pairing, and A5 is built in: the weight of Γ_1 ∩ Γ_m is von Mangoldt's
Λ(m).  A9, with ONE real κ: for every n ≥ 2 the fiber sum Σ_{m ≥ 2, cls m = cls n} Λ(m) converges (unconditionally) to
κ · v(cls n).  A7's graph structure is not used (NOTE §2.3's converse paragraph); Lemma F(b) uses only that the class map
is multiplicative into a monoid.

  `lemmaF_finite_fiber`   — (4) Lemma F(a): each fiber holds finitely many prime powers (a prime power weighs ≥ log 2, and a
                             summable family of nonnegative reals has finitely many terms ≥ log 2);
  `fiber_sum_eq_log`      — Lemma F(a), second clause: κ · v(cls n) = log N, N the product of the primes of the prime powers
                             of the fiber (the HasSum collapses to a finite sum);
  `lemmaF_infinite_order` — (5) Lemma F(b): φ(p^a) ≠ φ(p^{a+k}) for k ≥ 1 (else p^{a+jk}, j ≥ 0, lie in one fiber);
  `theoremR_of_A9`        — Theorem R at B = Spec Z from A9 alone, with NO hypothesis on κ: N_p := the fiber product at p has
                             p ∣ N_p and log N_p = κ · v(cls p), so the ℚ-linear map x ↦ κx carries (a subspace of) the
                             diagonal-row span onto span{log N_p}, which is infinite-dimensional by LogPrimes.lean (2);
  `theoremR`              — (6) the brief's statement, κ > 0 displayed (the SPEC's) and unused (PREDERIVATION-ERRATA E1);
  `lemmaF_finite_fiber_all`, `lemmaF_infinite_order_all` — the errata's E2 and E3 kernel-checked: item (4) needs no `2 ≤ n`,
                             item (5) needs no `1 ≤ a`.  Program side only; not statements of the Comparator topic.

WHAT IS NOT HERE.  The SPEC's geometric clauses A6–A8 (the base β, the factorization of Sp_B, dimension two, the canonical
class, adjunction), the existence or non-existence of a target Y, the general-base Theorem R (any base with its residue
characteristics), Lemma F(c); nothing about ζ or its zeros.

Trust model: proved from Mathlib alone and LogPrimes.lean; the three standard axioms only (program-axioms.log).
-/
import Zeta23.ResidueRank.LogPrimes

namespace Zeta23.ResidueRank

/-! ## §1 Lemma F(a): finite fibers, and the fiber sum as a logarithm -/

/-- A prime power has von Mangoldt weight at least `log 2`. -/
theorem log_two_le_vonMangoldt {m : ℕ} (hm : IsPrimePow m) :
    Real.log 2 ≤ ArithmeticFunction.vonMangoldt m := by
  rw [ArithmeticFunction.vonMangoldt_apply, if_pos hm]
  apply Real.log_le_log (by norm_num)
  exact_mod_cast (Nat.minFac_prime hm.ne_one).two_le

/-- **(4) Lemma F(a)**: under A9's real-valued fiber sums, each fiber holds finitely many prime powers. -/
theorem lemmaF_finite_fiber {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (cls n)))
    (n : ℕ) (hn : 2 ≤ n) :
    {m : ℕ | IsPrimePow m ∧ cls m = cls n}.Finite := by
  have hfin : {x : {m : ℕ // 2 ≤ m ∧ cls m = cls n} |
      ¬ ArithmeticFunction.vonMangoldt (x : ℕ) < Real.log 2}.Finite :=
    Filter.eventually_cofinite.mp
      ((hA9 n hn).summable.tendsto_cofinite_zero.eventually (gt_mem_nhds (Real.log_pos one_lt_two)))
  refine (hfin.image Subtype.val).subset ?_
  rintro m ⟨hpp, hcls⟩
  exact ⟨⟨m, hpp.two_le, hcls⟩, not_lt.mpr (log_two_le_vonMangoldt hpp), rfl⟩

/-- **Lemma F(a), second clause**: the fiber sum is `log N` with `N` the product of the smallest prime factors of the
prime powers of the fiber: `κ · v(cls n) = log (Π_{m ∈ F_n} minFac m)`. -/
theorem fiber_sum_eq_log {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (cls n)))
    (n : ℕ) (hn : 2 ≤ n) :
    κ * v (cls n)
      = Real.log ((∏ m ∈ (lemmaF_finite_fiber cls v κ hA9 n hn).toFinset, m.minFac : ℕ) : ℝ) := by
  classical
  have hmemF : ∀ m, m ∈ (lemmaF_finite_fiber cls v κ hA9 n hn).toFinset ↔ IsPrimePow m ∧ cls m = cls n :=
    fun m => Set.Finite.mem_toFinset _
  have hsum : HasSum
      (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
      (∑ m ∈ (lemmaF_finite_fiber cls v κ hA9 n hn).toFinset, ArithmeticFunction.vonMangoldt m) := by
    have h := hasSum_sum_of_ne_finset_zero
      (s := (lemmaF_finite_fiber cls v κ hA9 n hn).toFinset.subtype (fun m => 2 ≤ m ∧ cls m = cls n))
      (f := fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
      (L := SummationFilter.unconditional _) ?_
    · rwa [Finset.sum_subtype_eq_sum_filter, Finset.filter_true_of_mem] at h
      intro m hm
      rw [hmemF] at hm
      exact ⟨hm.1.two_le, hm.2⟩
    · intro b hb
      rw [ArithmeticFunction.vonMangoldt_eq_zero_iff]
      intro hpp
      apply hb
      rw [Finset.mem_subtype, hmemF]
      exact ⟨hpp, b.prop.2⟩
  rw [(hA9 n hn).unique hsum, Nat.cast_prod, Real.log_prod]
  · refine Finset.sum_congr rfl fun m hm => ?_
    rw [ArithmeticFunction.vonMangoldt_apply, if_pos ((hmemF m).mp hm).1]
  · intro m _
    exact_mod_cast (Nat.minFac_pos m).ne'

/-! ## §2 Lemma F(b): the prime endomorphisms have infinite order -/

/-- **(5) Lemma F(b)**: if the class map is multiplicative into a monoid, every prime has infinite order. -/
theorem lemmaF_infinite_order {E : Type} [Monoid E] (φ : ℕ → E)
    (hmul : ∀ a b : ℕ, φ (a * b) = φ a * φ b) (v : E → ℝ) (κ : ℝ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ φ m = φ n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (φ n)))
    (p : ℕ) (hp : p.Prime) (a k : ℕ) (ha : 1 ≤ a) (hk : 1 ≤ k) :
    φ (p ^ a) ≠ φ (p ^ (a + k)) := by
  intro heq
  -- the powers p ^ (a + j k), j ≥ 0, all lie in the fiber of φ (p ^ a)
  have hj : ∀ j : ℕ, φ (p ^ (a + j * k)) = φ (p ^ a) := by
    intro j
    induction j with
    | zero => simp
    | succ j ih =>
      calc φ (p ^ (a + (j + 1) * k)) = φ (p ^ (a + j * k) * p ^ k) := by
            rw [← pow_add]
            congr 2
            ring
        _ = φ (p ^ a) * φ (p ^ k) := by rw [hmul, ih]
        _ = φ (p ^ (a + k)) := by rw [← hmul, ← pow_add]
        _ = φ (p ^ a) := heq.symm
  have hfin := lemmaF_finite_fiber φ v κ hA9 (p ^ a)
    (le_trans hp.two_le (Nat.le_self_pow (by omega) p))
  refine Set.not_infinite.mpr hfin
    (Set.infinite_of_injective_forall_mem (f := fun j : ℕ => p ^ (a + j * k)) ?_ ?_)
  · intro i j hij
    have h1 : a + i * k = a + j * k := Nat.pow_right_injective hp.two_le hij
    exact Nat.eq_of_mul_eq_mul_right (by omega) (Nat.add_left_cancel h1)
  · intro j
    exact ⟨hp.isPrimePow.pow (by omega), hj j⟩

/-! ## §3 Theorem R on the abstract pair -/

/-- **Theorem R at B = Spec Z from A9 alone** (no hypothesis on κ): the ℚ-span of the diagonal row is not
finite-dimensional. -/
theorem theoremR_of_A9 {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (cls n))) :
    ¬ Module.Finite ℚ
      (Submodule.span ℚ (Set.range fun n : {n : ℕ // 2 ≤ n} => v (cls (n : ℕ)))) := by
  intro hfin
  -- N p: the product of the primes of the prime powers in the fiber of cls p
  let N : Nat.Primes → ℕ := fun p =>
    ∏ m ∈ (lemmaF_finite_fiber cls v κ hA9 p p.prop.two_le).toFinset, m.minFac
  have hNpos : ∀ p, 0 < N p := fun p => Finset.prod_pos fun m _ => Nat.minFac_pos m
  have hNdvd : ∀ p : Nat.Primes, (p : ℕ) ∣ N p := by
    intro p
    have hmem : (p : ℕ) ∈ (lemmaF_finite_fiber cls v κ hA9 p p.prop.two_le).toFinset := by
      rw [Set.Finite.mem_toFinset]
      exact ⟨p.prop.isPrimePow, rfl⟩
    have hd := Finset.dvd_prod_of_mem (fun m : ℕ => m.minFac) hmem
    rwa [p.prop.minFac_eq] at hd
  have hlog : ∀ p : Nat.Primes, Real.log ((N p : ℕ) : ℝ) = κ * v (cls p) := fun p =>
    (fiber_sum_eq_log cls v κ hA9 p p.prop.two_le).symm
  apply span_log_not_finite N hNpos hNdvd
  -- span{log N_p} lies in the image of the diagonal-row span under the ℚ-linear map x ↦ κ x
  let f : ℝ →ₗ[ℚ] ℝ := (LinearMap.mulLeft ℝ κ).restrictScalars ℚ
  have hle : Submodule.span ℚ (Set.range fun p : Nat.Primes => Real.log ((N p : ℕ) : ℝ))
      ≤ (Submodule.span ℚ (Set.range fun n : {n : ℕ // 2 ≤ n} => v (cls (n : ℕ)))).map f := by
    rw [Submodule.map_span, Submodule.span_le]
    rintro _ ⟨p, rfl⟩
    refine Submodule.subset_span ⟨v (cls p), ⟨⟨p, p.prop.two_le⟩, rfl⟩, ?_⟩
    show κ * v (cls p) = Real.log ((N p : ℕ) : ℝ)
    rw [hlog p]
  have : Module.Finite ℚ
      ((Submodule.span ℚ (Set.range fun n : {n : ℕ // 2 ≤ n} => v (cls (n : ℕ)))).map f) :=
    Module.Finite.map _ f
  exact Submodule.finiteDimensional_of_le hle

/-- **(6) Theorem R on the abstract pair** (the brief's statement): A5 (the weights are von Mangoldt's Λ) and A9 (every
fiber sum is `κ` times a real number `v`, one fixed `κ > 0`) force the ℚ-span of the diagonal row to be
infinite-dimensional.  The displayed `κ > 0` is the SPEC's and is not used (`theoremR_of_A9`). -/
theorem theoremR {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ) (_hκ : 0 < κ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (cls n))) :
    ¬ Module.Finite ℚ
      (Submodule.span ℚ (Set.range fun n : {n : ℕ // 2 ≤ n} => v (cls (n : ℕ)))) :=
  theoremR_of_A9 cls v κ hA9

/-! ## §4 The errata's E2 and E3, kernel-checked (program side only) -/

/-- PREDERIVATION-ERRATA E2: Lemma F(a) holds at every `n`, with no `2 ≤ n`. -/
theorem lemmaF_finite_fiber_all {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (cls n)))
    (n : ℕ) :
    {m : ℕ | IsPrimePow m ∧ cls m = cls n}.Finite := by
  by_cases h : ∃ m₀, IsPrimePow m₀ ∧ cls m₀ = cls n
  · obtain ⟨m₀, hpp, hc⟩ := h
    have hfin := lemmaF_finite_fiber cls v κ hA9 m₀ hpp.two_le
    rwa [hc] at hfin
  · rw [Set.eq_empty_of_forall_notMem fun m hm => h ⟨m, hm⟩]
    exact Set.finite_empty

/-- PREDERIVATION-ERRATA E3: Lemma F(b) holds with no `1 ≤ a` (only `1 ≤ k` is needed). -/
theorem lemmaF_infinite_order_all {E : Type} [Monoid E] (φ : ℕ → E)
    (hmul : ∀ a b : ℕ, φ (a * b) = φ a * φ b) (v : E → ℝ) (κ : ℝ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ φ m = φ n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (φ n)))
    (p : ℕ) (hp : p.Prime) (a k : ℕ) (hk : 1 ≤ k) :
    φ (p ^ a) ≠ φ (p ^ (a + k)) := by
  rcases Nat.eq_zero_or_pos a with rfl | ha
  · intro h
    have h1 : φ 1 = φ (p ^ k) := by simpa using h
    apply lemmaF_infinite_order φ hmul v κ hA9 p hp k k hk hk
    calc φ (p ^ k) = φ (1 * p ^ k) := by rw [one_mul]
      _ = φ 1 * φ (p ^ k) := hmul _ _
      _ = φ (p ^ k) * φ (p ^ k) := by rw [h1]
      _ = φ (p ^ (k + k)) := by rw [← hmul, ← pow_add]
  · exact lemmaF_infinite_order φ hmul v κ hA9 p hp a k ha hk

end Zeta23.ResidueRank
