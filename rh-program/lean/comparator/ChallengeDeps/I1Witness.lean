/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and does NOT import it: it imports Mathlib only.
-/
/-
comparator/ChallengeDeps/I1Witness.lean — the TRUSTED definition layer for the comparator topics `EpsteinWitnessSix` (rung 1:
the Epstein value at n = 6) and `I1Witness` (the witness table) of the barrier-zoo item I.1, the Davenport–Heilbronn / Epstein
filter (rh-program/BARRIER-ZOO.md I.1 and formalization-queue item 6, line 666; the record rh-program/results/c3-r/m0-axiom-note.md
§6.1–§6.2 and rh-program/results/c3-m0-epstein/n1_epstein_witness.json; build record
rh-program/results/i1-witness-lean-s32/BUILD-NOTES.md).

Everything the challenge statements mention is defined HERE, from Mathlib alone, in the namespace `I1Witness`:
  lambdaVec b n p    the coefficient of log p in Λ_b(n), for a coefficient array b : ℕ → R (R a commutative ring, b 1 = 1 in the
                     record's normalization) — the von Mangoldt recursion "a_n log n = Σ_{d|n} Λ(d) a_{n/d}" of the record, solved
                     for Λ(n), with log n replaced by the exponent vector (log n = Σ_p e_p(n) log p, e_p(n) = padicValNat p n):
                         lambdaVec b n p = b n · e_p(n) − Σ_{d | n, d < n} lambdaVec b d p · b (n / d)   for n ≥ 2,
                         lambdaVec b 1 p = 0,  lambdaVec b 0 p = 0.
                     It is written as a FUEL-structural recursion (`lambdaVecAux`, fuel := n) so that the kernel can evaluate it
                     under `decide`; that the defined object satisfies the displayed recursion is itself a shipped theorem
                     (`lambdaVec_rec` in Challenge/I1Witness.lean), so a reader need not trust the fuel;
  LambdaReal b n     := Σ_{p ≤ n prime} lambdaVec b n p · Real.log p, the real number Λ_b(n) of the record (b : ℕ → ℝ);
  epsteinB n         := r_Q(n)/2 for Q = x² + 5y² (D = −20, h = 2), the record's normalization "F(s) = ζ_Q(s)/2, b_n = r_Q(n)/2,
                     b₁ = 1"; r_Q(n) is DEFINED as the count of (x, y) with x² + 5y² = n over the box |x|, |y| ≤ n, which
                     contains every solution (x² ≤ n and 5y² ≤ n force |x|, |y| ≤ √n ≤ n; at n = 0 the box is {(0, 0)});
  kappa              := (√(10 − 2√5) − 2)/(√5 − 1), the record's Gauss-sum surd κ = 0.28407904384…;
  dhA n              := (1, κ, −κ, −1, 0) at n ≡ 1, 2, 3, 4, 0 (mod 5), the Davenport–Heilbronn coefficients "a_n periodic mod 5,
                     (a₁,…,a₅) = (1, κ, −κ, −1, 0)" of the record.
What is NOT defined here: no Dirichlet series, no −F′/F, no analytic continuation, no functional equation, no zero of anything.
The identification "LambdaReal b is the coefficient sequence of −F′/F for F(s) = Σ b_n n^{−s}" is the classical identity
(Σ Λ(n) n^{−s})(Σ b_n n^{−s}) = Σ b_n log n · n^{−s} and is NOT formalized (FIDELITY row (F-a)); what is formalized is the recursion
and its values.  A reader who wants to know WHAT is claimed reads this file and the challenge files only.
-/
import Mathlib

namespace I1Witness

variable {R : Type*} [CommRing R]

/-- the von Mangoldt recursion with a fuel: `lambdaVecAux b p fuel n` is the coefficient of `log p` in `Λ_b(n)` computed with
`fuel` levels of recursion (enough as soon as `fuel ≥ n`, since every recursive call descends to a proper divisor). At
`n < 2` the value is `0`; at `n ≥ 2` it is `b n · padicValNat p n − Σ_{d ∈ properDivisors n} (value at d) · b (n / d)`. -/
def lambdaVecAux (b : ℕ → R) (p : ℕ) : ℕ → ℕ → R
  | 0, _ => 0
  | fuel + 1, n => if n < 2 then 0 else
      b n * (padicValNat p n : R) - ∑ d ∈ n.properDivisors, lambdaVecAux b p fuel d * b (n / d)

/-- the coefficient of `log p` in `Λ_b(n)`: the von Mangoldt recursion `a_n log n = Σ_{d|n} Λ(d) a_{n/d}` of the record, solved
for `Λ(n)` with `log n = Σ_p (padicValNat p n) · log p`, on the coefficient array `b` (with `b 1 = 1`); fuel `n`. -/
def lambdaVec (b : ℕ → R) (n p : ℕ) : R := lambdaVecAux b p n n

noncomputable section

/-- the real number `Λ_b(n) = Σ_{p ≤ n prime} lambdaVec b n p · log p` for a real coefficient array `b`. -/
def LambdaReal (b : ℕ → ℝ) (n : ℕ) : ℝ :=
  ∑ p ∈ (Finset.range (n + 1)).filter Nat.Prime, lambdaVec b n p * Real.log p

/-- the Epstein coefficient `b_n = r_Q(n)/2` for `Q = x² + 5y²`: half the number of `(x, y) ∈ ℤ²` with `x² + 5y² = n`, counted over
the box `|x|, |y| ≤ n` (which contains every solution). The record's normalization `F(s) = ζ_Q(s)/2`, `b₁ = 1`. -/
def epsteinB (n : ℕ) : ℚ :=
  (((Finset.Icc (-(n : ℤ)) n ×ˢ Finset.Icc (-(n : ℤ)) n).filter
      (fun xy : ℤ × ℤ => xy.1 ^ 2 + 5 * xy.2 ^ 2 = n)).card : ℚ) / 2

/-- the record's Gauss-sum surd `κ = (√(10 − 2√5) − 2)/(√5 − 1) = 0.28407904384…`. -/
def kappa : ℝ := (Real.sqrt (10 - 2 * Real.sqrt 5) - 2) / (Real.sqrt 5 - 1)

/-- the Davenport–Heilbronn coefficients `a_n`, periodic mod 5: `(a₁, …, a₅) = (1, κ, −κ, −1, 0)` at `n ≡ 1, 2, 3, 4, 0 (mod 5)`. -/
def dhA (n : ℕ) : ℝ :=
  if n % 5 = 1 then 1 else if n % 5 = 2 then kappa else if n % 5 = 3 then -kappa
  else if n % 5 = 4 then -1 else 0

end

end I1Witness
