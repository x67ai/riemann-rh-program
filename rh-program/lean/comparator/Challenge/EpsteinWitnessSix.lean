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
comparator/Challenge/EpsteinWitnessSix.lean — CHALLENGE for rung 1 of the I.1 witness unit (Session 32; KICKSTART 10(l): one value
as a complete Comparator pair before the table): the Epstein value Λ_Q(6) = 2 log 2 + 2 log 3 for Q = x² + 5y², the record's
"support off prime powers" witness (rh-program/results/c3-r/m0-axiom-note.md §6.2; n1_epstein_witness.json `witness_i`).
Trusted vocabulary: ChallengeDeps.I1Witness (`I1Witness.{lambdaVec, LambdaReal, epsteinB}`, defined over Mathlib alone).
Solution/EpsteinWitnessSix.lean (untrusted) proves exactly these statements; github.com/leanprover/comparator checks statement
equality, that only the axioms propext, Classical.choice, Quot.sound are used, and replays the proofs through the Lean kernel and
nanoda.

WHAT IS CLAIMED, and what is NOT.  Three kernel facts about the coefficient array b_n = r_Q(n)/2 of x² + 5y² (b₁ = 1): the
normalization `epsteinB 1 = 1`; the two coefficients of the von Mangoldt recursion at n = 6, `lambdaVec epsteinB 6 2 = 2` and
`lambdaVec epsteinB 6 3 = 2`; and the real value `LambdaReal (epsteinB cast to ℝ) 6 = 2·log 2 + 2·log 3 > 0` (the coefficient at the
remaining prime 5 ≤ 6 vanishes because 5 ∤ 6).  "Λ_Q" here means the recursion's coefficient sequence on the array with b₁ = 1
(ChallengeDeps.I1Witness); its identification with the coefficients of −F′/F for F(s) = Σ b_n n^{−s} is the classical identity and
is NOT formalized.  Nothing is said about the Euler product, the zeros, the functional equation or the analytic continuation of
any Epstein zeta function; nothing about ζ or RH.  The value 6 = 2·3 is not a prime power; the reading "support off prime powers"
is the zoo's, not a theorem here.

The `sorry`s below are deliberate (this is the challenge side); expect "declaration uses 'sorry'" warnings when building this module.
-/
import ChallengeDeps.I1Witness

noncomputable section

open I1Witness

/-- **the normalization**: `b₁ = r_Q(1)/2 = 1` (the two solutions `(±1, 0)`, halved). -/
theorem epsteinB_one : epsteinB 1 = 1 := by
  sorry

/-- **the two coefficients at n = 6**: `Λ_Q(6) = 2·log 2 + 2·log 3` in the exponent-vector form. -/
theorem epstein_six_coeff : lambdaVec epsteinB 6 2 = 2 ∧ lambdaVec epsteinB 6 3 = 2 := by
  sorry

/-- **the real value**: `Λ_Q(6) = 2·log 2 + 2·log 3 = 2·log 6 > 0`, support off prime powers. -/
theorem epstein_witness_6 :
    LambdaReal (fun n => (epsteinB n : ℝ)) 6 = 2 * Real.log 2 + 2 * Real.log 3 ∧
      LambdaReal (fun n => (epsteinB n : ℝ)) 6 = 2 * Real.log 6 ∧
      0 < LambdaReal (fun n => (epsteinB n : ℝ)) 6 := by
  sorry
