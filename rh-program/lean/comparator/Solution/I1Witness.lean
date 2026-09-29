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
comparator/Solution/I1Witness.lean — the UNTRUSTED comparator solution module for the topic `I1Witness` (the I.1 witness unit,
Session 32): the fourteen statements of Challenge/I1Witness.lean, byte-identical, PROVED over Mathlib alone.
(R) The recursion lemmas are proved from the fuel-structural definition: the fuel is irrelevant once it is at least n (strong
induction on n), which gives the record's recursion; the not-dividing-prime lemma is a strong induction through it.
(E) The two Epstein coefficients at 36 and the normalization are decided in the kernel (`decide +kernel`, about 3.6 s each —
results/i1-witness-lean-s32/typing.log); the other primes' coefficients vanish by the (R) lemma (a prime dividing 36 = 2²·3² is 2
or 3); the real value uses the commutation of `lambdaVec` with the cast ℚ → ℝ and `Real.log_pos`.
(D) `kappa_pos` from `Real.lt_sqrt` and `Real.sqrt_lt'`; the Davenport–Heilbronn coefficients at 2, 3, 4, 6, 12 are computed
symbolically through the (R) recursion over the proper divisors (`Nat.properDivisors 12 = {1, 2, 3, 4, 6}` decided), the array values
`dhA n` by `n % 5`, and closed by `ring` — polynomial identities in κ, no numerics.  The sums over the primes p ≤ n are reduced to
their surviving terms with `Finset.sum_eq_add_of_mem` / `Finset.sum_eq_single` and the not-dividing-prime lemma.
The general lemmas live in the namespace `I1WitnessProof`; nothing in this file is part of the trusted base: comparator re-checks
that each theorem below has exactly the statement of its Challenge namesake and uses only the permitted axioms.  This module never
imports the challenge and never imports Solution.EpsteinWitnessSix (each topic is self-contained).
-/
import ChallengeDeps.I1Witness

noncomputable section

open I1Witness

namespace I1WitnessProof

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

theorem rec' (b : ℕ → R) (p n : ℕ) (hn : 2 ≤ n) :
    lambdaVec b n p = b n * (padicValNat p n : R)
      - ∑ d ∈ n.properDivisors, lambdaVec b d p * b (n / d) := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  simp only [lambdaVec, lambdaVecAux, show ¬ m + 1 < 2 by omega, if_false]
  congr 1
  refine Finset.sum_congr rfl fun d hd => ?_
  have hd' := Nat.mem_properDivisors.1 hd
  rw [lambdaVecAux_stable b p d m d (by omega) le_rfl]

theorem one' (b : ℕ → R) (p : ℕ) : lambdaVec b 1 p = 0 := by
  simp [lambdaVec, lambdaVecAux]

theorem zero' (b : ℕ → R) (p : ℕ) : lambdaVec b 0 p = 0 := by
  simp [lambdaVec, lambdaVecAux]

theorem not_dvd' (b : ℕ → R) (p : ℕ) : ∀ n, ¬ p ∣ n → lambdaVec b n p = 0 := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro hp
    rcases lt_or_ge n 2 with hn | hn
    · interval_cases n
      · exact zero' b p
      · exact one' b p
    · rw [rec' b p n hn, padicValNat.eq_zero_of_not_dvd hp]
      rw [Finset.sum_eq_zero, Nat.cast_zero, mul_zero, sub_zero]
      intro d hd
      have hd' := Nat.mem_properDivisors.1 hd
      rw [ih d hd'.2 (fun h => hp (h.trans hd'.1)), zero_mul]

/-- `lambdaVec` commutes with the cast `ℚ → ℝ` of the array. -/
theorem ratCast' (b : ℕ → ℚ) (n p : ℕ) :
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

/-! (E) the kernel facts at 36 -/

theorem e36_two : lambdaVec epsteinB 36 2 = -4 := by decide +kernel
theorem e36_three : lambdaVec epsteinB 36 3 = -4 := by decide +kernel

theorem e36_other (p : ℕ) (hp : p.Prime) (h2 : p ≠ 2) (h3 : p ≠ 3) : lambdaVec epsteinB 36 p = 0 := by
  apply not_dvd'
  intro hdvd
  have : p ∣ 2 ^ 2 * 3 ^ 2 := by norm_num; exact hdvd
  rcases prime_dvd_two_three hp this with h | h
  · exact h2 h
  · exact h3 h

/-! (D) the Davenport–Heilbronn coefficients, symbolically -/

theorem kpos : 0 < kappa := by
  unfold kappa
  apply div_pos
  · have h5 : Real.sqrt 5 < 3 := by
      rw [Real.sqrt_lt' (by norm_num)]; norm_num
    have : (2 : ℝ) < Real.sqrt (10 - 2 * Real.sqrt 5) := by
      rw [Real.lt_sqrt (by norm_num)]; nlinarith
    linarith
  · have : (1 : ℝ) < Real.sqrt 5 := by
      rw [Real.lt_sqrt (by norm_num)]; norm_num
    linarith

theorem d2 : lambdaVec dhA 2 2 = kappa := by
  rw [rec' dhA 2 2 (by norm_num), show Nat.properDivisors 2 = {1} by decide]
  simp [one', dhA]

theorem d3 : lambdaVec dhA 3 3 = -kappa := by
  rw [rec' dhA 3 3 (by norm_num), show Nat.properDivisors 3 = {1} by decide]
  simp [one', dhA]

theorem d4 : lambdaVec dhA 4 2 = -(2 + kappa ^ 2) := by
  rw [rec' dhA 2 4 (by norm_num), show Nat.properDivisors 4 = {1, 2} by decide]
  rw [Finset.sum_insert (by decide), Finset.sum_singleton]
  simp only [one', d2, show padicValNat 2 4 = 2 by decide +kernel]
  simp [dhA]; ring

theorem d6_two : lambdaVec dhA 6 2 = 1 + kappa ^ 2 := by
  rw [rec' dhA 2 6 (by norm_num), show Nat.properDivisors 6 = {1, 2, 3} by decide]
  rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_singleton]
  simp only [one', d2, not_dvd' dhA 2 3 (by decide), show padicValNat 2 6 = 1 by decide +kernel]
  simp [dhA]; ring

theorem d6_three : lambdaVec dhA 6 3 = 1 + kappa ^ 2 := by
  rw [rec' dhA 3 6 (by norm_num), show Nat.properDivisors 6 = {1, 2, 3} by decide]
  rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_singleton]
  simp only [one', d3, not_dvd' dhA 3 2 (by decide), show padicValNat 3 6 = 1 by decide +kernel]
  simp [dhA]; ring

theorem d12_two : lambdaVec dhA 12 2 = -kappa * (1 + kappa ^ 2) * 2 := by
  rw [rec' dhA 2 12 (by norm_num), show Nat.properDivisors 12 = {1, 2, 3, 4, 6} by decide]
  rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_singleton]
  simp only [one', d2, d4, d6_two, not_dvd' dhA 2 3 (by decide), show padicValNat 2 12 = 2 by decide +kernel]
  simp [dhA]; ring

theorem d12_three : lambdaVec dhA 12 3 = -kappa * (1 + kappa ^ 2) := by
  rw [rec' dhA 3 12 (by norm_num), show Nat.properDivisors 12 = {1, 2, 3, 4, 6} by decide]
  rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide), Finset.sum_insert (by decide),
    Finset.sum_insert (by decide), Finset.sum_singleton]
  simp only [one', d3, d6_three, not_dvd' dhA 3 2 (by decide), not_dvd' dhA 3 4 (by decide),
    show padicValNat 3 12 = 1 by decide +kernel]
  simp [dhA]; ring

/-- the sum over the primes `p ≤ n` collapses to the terms at 2 and 3 when `n = 2^a·3^b`. -/
theorem sum_two_three (b : ℕ → ℝ) {n a c : ℕ} (hn : n = 2 ^ a * 3 ^ c) (h3 : 3 ≤ n) :
    LambdaReal b n = lambdaVec b n 2 * Real.log 2 + lambdaVec b n 3 * Real.log 3 := by
  unfold LambdaReal
  rw [Finset.sum_eq_add_of_mem 2 3 (by simp [Nat.prime_two]; omega) (by simp [Nat.prime_three]; omega) (by norm_num)]
  · push_cast; ring
  · intro p hp hne
    have hp' := (Finset.mem_filter.1 hp).2
    rw [not_dvd' b p n ?_, zero_mul]
    intro hdvd
    rw [hn] at hdvd
    rcases prime_dvd_two_three hp' hdvd with h | h
    · exact hne.1 h
    · exact hne.2 h

theorem log6 : Real.log 6 = Real.log 2 + Real.log 3 := by
  rw [show (6 : ℝ) = 2 * 3 by norm_num, Real.log_mul (by norm_num) (by norm_num)]

theorem log12 : Real.log 12 = 2 * Real.log 2 + Real.log 3 := by
  rw [show (12 : ℝ) = 2 * 2 * 3 by norm_num, Real.log_mul (by norm_num) (by norm_num),
    Real.log_mul (by norm_num) (by norm_num)]; ring

theorem log2_pos : 0 < Real.log 2 := Real.log_pos (by norm_num)
theorem log3_pos : 0 < Real.log 3 := Real.log_pos (by norm_num)

end I1WitnessProof

open I1WitnessProof

/-- **(R) the record's recursion holds for the trusted object**: `Λ(n) = b_n·e_p(n) − Σ_{d | n, d < n} Λ(d)·b_{n/d}` for `n ≥ 2`. -/
theorem lambdaVec_rec {R : Type*} [CommRing R] (b : ℕ → R) (p n : ℕ) (hn : 2 ≤ n) :
    lambdaVec b n p = b n * (padicValNat p n : R)
      - ∑ d ∈ n.properDivisors, lambdaVec b d p * b (n / d) := by
  exact rec' b p n hn

/-- **(R) the base case**: `Λ(1) = 0`. -/
theorem lambdaVec_one {R : Type*} [CommRing R] (b : ℕ → R) (p : ℕ) : lambdaVec b 1 p = 0 := by
  exact one' b p

/-- **(R) a prime not dividing `n` has coefficient `0` at `n`.** -/
theorem lambdaVec_eq_zero_of_not_dvd {R : Type*} [CommRing R] (b : ℕ → R) (p n : ℕ) (h : ¬ p ∣ n) :
    lambdaVec b n p = 0 := by
  exact not_dvd' b p n h

/-- **(E) the normalization**: `b₁ = r_Q(1)/2 = 1`. -/
theorem epsteinB_one : epsteinB 1 = 1 := by
  decide +kernel

/-- **(E) the coefficients at n = 36**: `−4` at `p = 2`, `−4` at `p = 3`, `0` at every other prime. -/
theorem epstein_thirtysix_coeff :
    lambdaVec epsteinB 36 2 = -4 ∧ lambdaVec epsteinB 36 3 = -4 ∧
      ∀ p, p.Prime → p ≠ 2 → p ≠ 3 → lambdaVec epsteinB 36 p = 0 := by
  exact ⟨e36_two, e36_three, e36_other⟩

/-- **(E) the witness**: `Λ_Q(36) = −4·log 2 − 4·log 3 = −4·log 6 < 0`. -/
theorem epstein_witness_36 :
    LambdaReal (fun n => (epsteinB n : ℝ)) 36 = -4 * Real.log 2 - 4 * Real.log 3 ∧
      LambdaReal (fun n => (epsteinB n : ℝ)) 36 = -4 * Real.log 6 ∧
      LambdaReal (fun n => (epsteinB n : ℝ)) 36 < 0 := by
  have hval : LambdaReal (fun n => (epsteinB n : ℝ)) 36 = -4 * Real.log 2 - 4 * Real.log 3 := by
    rw [sum_two_three _ (show 36 = 2 ^ 2 * 3 ^ 2 by norm_num) (by norm_num), ratCast', ratCast',
      e36_two, e36_three]
    push_cast; ring
  refine ⟨hval, ?_, ?_⟩
  · rw [hval, log6]; ring
  · rw [hval]; linarith [log2_pos, log3_pos]

/-- **(D) `κ > 0`** from the closed form `(√(10 − 2√5) − 2)/(√5 − 1)`: `√5 < 3` and `1 < √5`. -/
theorem kappa_pos : 0 < kappa := by
  exact kpos

/-- **(D) the normalization**: `a₁ = 1`. -/
theorem dhA_one : dhA 1 = 1 := by
  simp [dhA]

/-- **(D) the coefficient at the prime 3**: `Λ_DH(3) = a₃·log 3 = −κ·log 3`. -/
theorem dh_three_coeff : lambdaVec dhA 3 3 = -kappa := by
  exact d3

/-- **(D) the cheapest witness**: `Λ_DH(3) = −κ·log 3 < 0`. -/
theorem dh_witness_3 : LambdaReal dhA 3 = -kappa * Real.log 3 ∧ LambdaReal dhA 3 < 0 := by
  have hval : LambdaReal dhA 3 = -kappa * Real.log 3 := by
    rw [sum_two_three dhA (show 3 = 2 ^ 0 * 3 ^ 1 by norm_num) le_rfl, d3,
      not_dvd' dhA 2 3 (by decide)]
    ring
  refine ⟨hval, ?_⟩
  rw [hval]; nlinarith [mul_pos kpos log3_pos]

/-- **(D) the coefficients at n = 12**: `−2κ(1 + κ²)` at `p = 2`, `−κ(1 + κ²)` at `p = 3`. -/
theorem dh_twelve_coeff :
    lambdaVec dhA 12 2 = -kappa * (1 + kappa ^ 2) * 2 ∧ lambdaVec dhA 12 3 = -kappa * (1 + kappa ^ 2) := by
  exact ⟨d12_two, d12_three⟩

/-- **(D) I.1's one-line witness**: `Λ_DH(12) = −κ(1 + κ²)(2 log 2 + log 3) = −κ(1 + κ²)·log 12 < 0`. -/
theorem dh_witness_12 :
    LambdaReal dhA 12 = -kappa * (1 + kappa ^ 2) * (2 * Real.log 2 + Real.log 3) ∧
      LambdaReal dhA 12 = -kappa * (1 + kappa ^ 2) * Real.log 12 ∧
      LambdaReal dhA 12 < 0 := by
  have hval : LambdaReal dhA 12 = -kappa * (1 + kappa ^ 2) * (2 * Real.log 2 + Real.log 3) := by
    rw [sum_two_three dhA (show 12 = 2 ^ 2 * 3 ^ 1 by norm_num) (by norm_num), d12_two, d12_three]
    ring
  have hA : 0 < kappa * (1 + kappa ^ 2) := mul_pos kpos (by positivity)
  have hB : 0 < 2 * Real.log 2 + Real.log 3 := by linarith [log2_pos, log3_pos]
  refine ⟨hval, ?_, ?_⟩
  · rw [hval, log12]
  · rw [hval]; nlinarith [mul_pos hA hB]

/-- **(D) the table row n = 4**: `Λ_DH(4) = −(2 + κ²)·log 2 < 0` (negativity at a prime power). -/
theorem dh_four :
    lambdaVec dhA 4 2 = -(2 + kappa ^ 2) ∧ LambdaReal dhA 4 = -(2 + kappa ^ 2) * Real.log 2 ∧
      LambdaReal dhA 4 < 0 := by
  have hval : LambdaReal dhA 4 = -(2 + kappa ^ 2) * Real.log 2 := by
    rw [sum_two_three dhA (show 4 = 2 ^ 2 * 3 ^ 0 by norm_num) (by norm_num), d4,
      not_dvd' dhA 3 4 (by decide)]
    ring
  have hA : 0 < (2 + kappa ^ 2) * Real.log 2 := mul_pos (by positivity) log2_pos
  refine ⟨d4, hval, ?_⟩
  rw [hval]; linarith

/-- **(D) the table row n = 6**: `Λ_DH(6) = (1 + κ²)·log 6 > 0` (support off prime powers). -/
theorem dh_six :
    lambdaVec dhA 6 2 = 1 + kappa ^ 2 ∧ lambdaVec dhA 6 3 = 1 + kappa ^ 2 ∧
      LambdaReal dhA 6 = (1 + kappa ^ 2) * Real.log 6 ∧ 0 < LambdaReal dhA 6 := by
  have hval : LambdaReal dhA 6 = (1 + kappa ^ 2) * Real.log 6 := by
    rw [sum_two_three dhA (show 6 = 2 ^ 1 * 3 ^ 1 by norm_num) (by norm_num), d6_two, d6_three, log6]
    ring
  refine ⟨d6_two, d6_three, hval, ?_⟩
  rw [hval]
  exact mul_pos (by positivity) (Real.log_pos (by norm_num))
