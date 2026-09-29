/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: its imports are Mathlib-only.
-/
/-
comparator/Challenge/I1Witness.lean — CHALLENGE for the I.1 witness unit (Session 32): the barrier-zoo item I.1's one-line
witnesses as kernel-checked VALUES of the von Mangoldt recursion (rh-program/BARRIER-ZOO.md I.1 and line 666; the record
rh-program/results/c3-r/m0-axiom-note.md §6.1 (the DH table) and §6.2 (Epstein, x² + 5y²); n1_epstein_witness.json `witness_ii`).
Trusted vocabulary: ChallengeDeps.I1Witness (`I1Witness.{lambdaVec, LambdaReal, epsteinB, kappa, dhA}`, defined over Mathlib
alone).  Solution/I1Witness.lean (untrusted) proves exactly these statements; github.com/leanprover/comparator checks statement
equality, that only the axioms propext, Classical.choice, Quot.sound are used, and replays the proofs through the Lean kernel and
nanoda.

WHAT IS CLAIMED, and what is NOT.  (R) The trusted object satisfies the record's recursion: for every commutative ring R, array b
and prime index p, `lambdaVec b n p = b n · padicValNat p n − Σ_{d | n, d < n} lambdaVec b d p · b (n / d)` for n ≥ 2, with
`lambdaVec b 1 p = 0`, and `lambdaVec b n p = 0` whenever p ∤ n.  (E) Epstein, Q = x² + 5y² (D = −20, h = 2), b_n = r_Q(n)/2, b₁ = 1:
`lambdaVec epsteinB 36 2 = −4`, `lambdaVec epsteinB 36 3 = −4`, every other prime's coefficient at 36 is 0, and
`LambdaReal (epsteinB cast to ℝ) 36 = −4·log 2 − 4·log 3 = −4·log 6 < 0` — the record's "Λ_Q(36) = −4·log 2 − 4·log 3 = −4·log 6".
(D) Davenport–Heilbronn, a_n = (1, κ, −κ, −1, 0) mod 5 with κ = (√(10 − 2√5) − 2)/(√5 − 1): `0 < kappa` (from the closed form:
√5 < 3 and 1 < √5); `lambdaVec dhA 3 3 = −κ` and `LambdaReal dhA 3 = −κ·log 3 < 0` (the record's "cheapest witness");
`lambdaVec dhA 12 2 = −κ(1 + κ²)·2`, `lambdaVec dhA 12 3 = −κ(1 + κ²)` and `LambdaReal dhA 12 = −κ(1 + κ²)(2 log 2 + log 3) =
−κ(1 + κ²)·log 12 < 0` (the record's one-line witness Λ_DH(12) = −0.7629…); and the two further table rows Λ_DH(4) = −(2 + κ²) log 2 < 0,
Λ_DH(6) = (1 + κ²) log 6 > 0.  "Λ_f" throughout means the recursion's coefficient sequence on the array with b₁ = 1
(ChallengeDeps.I1Witness); its identification with the coefficients of −F′/F for F(s) = Σ b_n n^{−s} is the classical identity and is
NOT formalized.  NOT claimed: anything about the Euler product of either function (the witness is a value; "DH has no Euler product"
is the zoo's reading, not a theorem here); the analytic continuation, functional equation or off-line zero of the Davenport–Heilbronn
function; anything about the zeros of any Epstein zeta function; anything about ζ or RH.  Nothing here is an attack on RH; it is a
hardening of I.1's witness table from "computationally-verified" to kernel-checked.

The `sorry`s below are deliberate (this is the challenge side); expect "declaration uses 'sorry'" warnings when building this module.
-/
import ChallengeDeps.I1Witness

noncomputable section

open I1Witness

/-- **(R) the record's recursion holds for the trusted object**: `Λ(n) = b_n·e_p(n) − Σ_{d | n, d < n} Λ(d)·b_{n/d}` for `n ≥ 2`. -/
theorem lambdaVec_rec {R : Type*} [CommRing R] (b : ℕ → R) (p n : ℕ) (hn : 2 ≤ n) :
    lambdaVec b n p = b n * (padicValNat p n : R)
      - ∑ d ∈ n.properDivisors, lambdaVec b d p * b (n / d) := by
  sorry

/-- **(R) the base case**: `Λ(1) = 0`. -/
theorem lambdaVec_one {R : Type*} [CommRing R] (b : ℕ → R) (p : ℕ) : lambdaVec b 1 p = 0 := by
  sorry

/-- **(R) a prime not dividing `n` has coefficient `0` at `n`.** -/
theorem lambdaVec_eq_zero_of_not_dvd {R : Type*} [CommRing R] (b : ℕ → R) (p n : ℕ) (h : ¬ p ∣ n) :
    lambdaVec b n p = 0 := by
  sorry

/-- **(E) the normalization**: `b₁ = r_Q(1)/2 = 1`. -/
theorem epsteinB_one : epsteinB 1 = 1 := by
  sorry

/-- **(E) the coefficients at n = 36**: `−4` at `p = 2`, `−4` at `p = 3`, `0` at every other prime. -/
theorem epstein_thirtysix_coeff :
    lambdaVec epsteinB 36 2 = -4 ∧ lambdaVec epsteinB 36 3 = -4 ∧
      ∀ p, p.Prime → p ≠ 2 → p ≠ 3 → lambdaVec epsteinB 36 p = 0 := by
  sorry

/-- **(E) the witness**: `Λ_Q(36) = −4·log 2 − 4·log 3 = −4·log 6 < 0`. -/
theorem epstein_witness_36 :
    LambdaReal (fun n => (epsteinB n : ℝ)) 36 = -4 * Real.log 2 - 4 * Real.log 3 ∧
      LambdaReal (fun n => (epsteinB n : ℝ)) 36 = -4 * Real.log 6 ∧
      LambdaReal (fun n => (epsteinB n : ℝ)) 36 < 0 := by
  sorry

/-- **(D) `κ > 0`** from the closed form `(√(10 − 2√5) − 2)/(√5 − 1)`: `√5 < 3` and `1 < √5`. -/
theorem kappa_pos : 0 < kappa := by
  sorry

/-- **(D) the normalization**: `a₁ = 1`. -/
theorem dhA_one : dhA 1 = 1 := by
  sorry

/-- **(D) the coefficient at the prime 3**: `Λ_DH(3) = a₃·log 3 = −κ·log 3`. -/
theorem dh_three_coeff : lambdaVec dhA 3 3 = -kappa := by
  sorry

/-- **(D) the cheapest witness**: `Λ_DH(3) = −κ·log 3 < 0`. -/
theorem dh_witness_3 : LambdaReal dhA 3 = -kappa * Real.log 3 ∧ LambdaReal dhA 3 < 0 := by
  sorry

/-- **(D) the coefficients at n = 12**: `−2κ(1 + κ²)` at `p = 2`, `−κ(1 + κ²)` at `p = 3`. -/
theorem dh_twelve_coeff :
    lambdaVec dhA 12 2 = -kappa * (1 + kappa ^ 2) * 2 ∧ lambdaVec dhA 12 3 = -kappa * (1 + kappa ^ 2) := by
  sorry

/-- **(D) I.1's one-line witness**: `Λ_DH(12) = −κ(1 + κ²)(2 log 2 + log 3) = −κ(1 + κ²)·log 12 < 0`. -/
theorem dh_witness_12 :
    LambdaReal dhA 12 = -kappa * (1 + kappa ^ 2) * (2 * Real.log 2 + Real.log 3) ∧
      LambdaReal dhA 12 = -kappa * (1 + kappa ^ 2) * Real.log 12 ∧
      LambdaReal dhA 12 < 0 := by
  sorry

/-- **(D) the table row n = 4**: `Λ_DH(4) = −(2 + κ²)·log 2 < 0` (negativity at a prime power). -/
theorem dh_four :
    lambdaVec dhA 4 2 = -(2 + kappa ^ 2) ∧ LambdaReal dhA 4 = -(2 + kappa ^ 2) * Real.log 2 ∧
      LambdaReal dhA 4 < 0 := by
  sorry

/-- **(D) the table row n = 6**: `Λ_DH(6) = (1 + κ²)·log 6 > 0` (support off prime powers). -/
theorem dh_six :
    lambdaVec dhA 6 2 = 1 + kappa ^ 2 ∧ lambdaVec dhA 6 3 = 1 + kappa ^ 2 ∧
      LambdaReal dhA 6 = (1 + kappa ^ 2) * Real.log 6 ∧ 0 < LambdaReal dhA 6 := by
  sorry
