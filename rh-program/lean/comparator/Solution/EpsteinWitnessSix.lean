/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does not import it: it imports Mathlib only
(through ChallengeDeps.I1Witness).
-/
/-
comparator/Solution/EpsteinWitnessSix.lean — the UNTRUSTED comparator solution module for the topic `EpsteinWitnessSix` (rung 1
of the I.1 witness unit, Session 32): the three statements of Challenge/EpsteinWitnessSix.lean, byte-identical, PROVED over
Mathlib alone.  The two coefficients and the normalization are decided in the kernel (`decide +kernel`: the recursion is
fuel-structural and the box count is a `Finset` card, both of which the kernel evaluates; measured 77 ms for the pair of
coefficients, results/i1-witness-lean-s32/typing.log).  The real value follows from the two coefficients, the vanishing of the
coefficient at the prime 5 (5 ∤ 6, lemma `lambdaVec_eq_zero_of_not_dvd`), the commutation of `lambdaVec` with the cast ℚ → ℝ, and
`Real.log_pos`.  The general lemmas (namespace `EpsteinWitnessSix.Proof`) are proved from the trusted definition by induction on
the fuel; nothing in this file is part of the trusted base: comparator re-checks that each theorem below has exactly the statement
of its Challenge namesake and uses only the permitted axioms.  This module never imports the challenge.
-/
import ChallengeDeps.I1Witness

noncomputable section

open I1Witness

namespace EpsteinWitnessSix.Proof

variable {R : Type*} [CommRing R]

/-- the fuel does not matter once it is at least `n`. -/
theorem lambdaVecAux_stable (b : ℕ → R) (p : ℕ) :
    ∀ n f g, n ≤ f → n ≤ g → lambdaVecAux b p f n = lambdaVecAux b p g n := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro f g hf hg
    rcases lt_or_ge n 2 with hn | hn
    · cases f <;> cases g <;> simp [lambdaVecAux, hn]
    · obtain ⟨f', rfl⟩ : ∃ f', f = f' + 1 := ⟨f - 1, by omega⟩
      obtain ⟨g', rfl⟩ : ∃ g', g = g' + 1 := ⟨g - 1, by omega⟩
      simp only [lambdaVecAux, show ¬ n < 2 by omega, if_false]
      congr 1
      refine Finset.sum_congr rfl fun d hd => ?_
      have hd' := Nat.mem_properDivisors.1 hd
      rw [ih d hd'.2 f' g' (by omega) (by omega)]

/-- the record's recursion, as a theorem about the fuel-defined object. -/
theorem lambdaVec_rec (b : ℕ → R) (p n : ℕ) (hn : 2 ≤ n) :
    lambdaVec b n p = b n * (padicValNat p n : R)
      - ∑ d ∈ n.properDivisors, lambdaVec b d p * b (n / d) := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  simp only [lambdaVec, lambdaVecAux, show ¬ m + 1 < 2 by omega, if_false]
  congr 1
  refine Finset.sum_congr rfl fun d hd => ?_
  have hd' := Nat.mem_properDivisors.1 hd
  rw [lambdaVecAux_stable b p d m d (by omega) le_rfl]

theorem lambdaVec_one (b : ℕ → R) (p : ℕ) : lambdaVec b 1 p = 0 := by
  simp [lambdaVec, lambdaVecAux]

theorem lambdaVec_zero (b : ℕ → R) (p : ℕ) : lambdaVec b 0 p = 0 := by
  simp [lambdaVec, lambdaVecAux]

/-- a prime that does not divide `n` has coefficient `0` at `n` (no `log p` in `log d` for any divisor `d`). -/
theorem lambdaVec_eq_zero_of_not_dvd (b : ℕ → R) (p : ℕ) :
    ∀ n, ¬ p ∣ n → lambdaVec b n p = 0 := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro hp
    rcases lt_or_ge n 2 with hn | hn
    · interval_cases n
      · exact lambdaVec_zero b p
      · exact lambdaVec_one b p
    · rw [lambdaVec_rec b p n hn, padicValNat.eq_zero_of_not_dvd hp]
      rw [Finset.sum_eq_zero, Nat.cast_zero, mul_zero, sub_zero]
      intro d hd
      have hd' := Nat.mem_properDivisors.1 hd
      rw [ih d hd'.2 (fun h => hp (h.trans hd'.1)), zero_mul]

/-- `lambdaVec` commutes with the cast `ℚ → ℝ` of the array (it is built from ring operations). -/
theorem lambdaVec_ratCast (b : ℕ → ℚ) (n p : ℕ) :
    lambdaVec (fun m => (b m : ℝ)) n p = ((lambdaVec b n p : ℚ) : ℝ) := by
  suffices h : ∀ f m, lambdaVecAux (fun m => (b m : ℝ)) p f m = ((lambdaVecAux b p f m : ℚ) : ℝ) from h n n
  intro f
  induction f with
  | zero => intro m; simp [lambdaVecAux]
  | succ f ih =>
    intro m
    simp only [lambdaVecAux]
    split_ifs
    · simp
    · push_cast
      congr 1
      refine Finset.sum_congr rfl fun d _ => ?_
      rw [ih d]

/-- a prime dividing `2^a · 3^b` is `2` or `3`. -/
theorem prime_dvd_two_three {p a b : ℕ} (hp : p.Prime) (h : p ∣ 2 ^ a * 3 ^ b) : p = 2 ∨ p = 3 := by
  rcases (Nat.Prime.dvd_mul hp).1 h with h2 | h3
  · exact Or.inl ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_two).1 (hp.dvd_of_dvd_pow h2))
  · exact Or.inr ((Nat.prime_dvd_prime_iff_eq hp Nat.prime_three).1 (hp.dvd_of_dvd_pow h3))

theorem coeff_two : lambdaVec epsteinB 6 2 = 2 := by decide +kernel
theorem coeff_three : lambdaVec epsteinB 6 3 = 2 := by decide +kernel

end EpsteinWitnessSix.Proof

open EpsteinWitnessSix.Proof

/-- **the normalization**: `b₁ = r_Q(1)/2 = 1` (the two solutions `(±1, 0)`, halved). -/
theorem epsteinB_one : epsteinB 1 = 1 := by
  decide +kernel

/-- **the two coefficients at n = 6**: `Λ_Q(6) = 2·log 2 + 2·log 3` in the exponent-vector form. -/
theorem epstein_six_coeff : lambdaVec epsteinB 6 2 = 2 ∧ lambdaVec epsteinB 6 3 = 2 := by
  exact ⟨coeff_two, coeff_three⟩

/-- **the real value**: `Λ_Q(6) = 2·log 2 + 2·log 3 = 2·log 6 > 0`, support off prime powers. -/
theorem epstein_witness_6 :
    LambdaReal (fun n => (epsteinB n : ℝ)) 6 = 2 * Real.log 2 + 2 * Real.log 3 ∧
      LambdaReal (fun n => (epsteinB n : ℝ)) 6 = 2 * Real.log 6 ∧
      0 < LambdaReal (fun n => (epsteinB n : ℝ)) 6 := by
  have h2 := Real.log_pos (by norm_num : (1 : ℝ) < 2)
  have h3 := Real.log_pos (by norm_num : (1 : ℝ) < 3)
  have hval : LambdaReal (fun n => (epsteinB n : ℝ)) 6 = 2 * Real.log 2 + 2 * Real.log 3 := by
    unfold LambdaReal
    rw [Finset.sum_eq_add_of_mem 2 3 (by simp [Nat.prime_two]) (by simp [Nat.prime_three]) (by norm_num)]
    · rw [lambdaVec_ratCast, lambdaVec_ratCast, coeff_two, coeff_three]; push_cast; ring
    · intro c hc hne
      have hc' := (Finset.mem_filter.1 hc).2
      rw [lambdaVec_ratCast, lambdaVec_eq_zero_of_not_dvd epsteinB c 6 ?_]
      · simp
      · intro hdvd
        have : c ∣ 2 ^ 1 * 3 ^ 1 := by norm_num; exact hdvd
        rcases prime_dvd_two_three hc' this with h | h
        · exact hne.1 h
        · exact hne.2 h
  refine ⟨hval, ?_, ?_⟩
  · rw [hval, show (6 : ℝ) = 2 * 3 by norm_num, Real.log_mul (by norm_num) (by norm_num)]; ring
  · rw [hval]; linarith
