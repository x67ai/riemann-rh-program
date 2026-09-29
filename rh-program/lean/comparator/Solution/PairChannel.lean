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
comparator/Solution/PairChannel.lean — the UNTRUSTED comparator solution module for the topic `PairChannel` (barrier-zoo
IV.17's pair channel): the eight statements of Challenge/PairChannel.lean, byte-identical, PROVED by delegating to
Zeta23/PairCeiling/PairRow.lean (`W2_eq`, `sum_W2_mul`, `pairRow_eq_gridRowQ`, `sum_W2_cosh`, `prop45`, `abar_sq_le`,
`floor_holds_integer`) and Zeta23/PairCeiling/PairCert.lean (`floor_fails_anchor`).  The challenge's
`PairChannel.{chi, dftMarkQ, zetaM, gridRowQ, W2, pairFormFactor, pairRow, abar, vacancyMark}` are character for character the
Zeta23 definitions, so each delegation typechecks by definitional unfolding in the kernel.  This module never imports the
challenge.  Nothing in this file is part of the trusted base: comparator re-checks that each theorem below has exactly the
statement of its Challenge namesake and uses only the permitted axioms.
-/
import ChallengeDeps.PairChannel
import Zeta23.PairCeiling.PairCert

noncomputable section

open Finset PairChannel

/-- **(1) the closed-form weight** of pair-channel.md line 39: `W2(s) = (M − |s|)/M²` for `|s| ≤ 2n`, `M = 2n + 1`. -/
theorem W2_eq (n : ℕ) (s : ℤ) (hs : s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ))) :
    W2 n s = ((2 * (n : ℝ) + 1) - |(s : ℝ)|) / (2 * (n : ℝ) + 1) ^ 2 :=
  Zeta23.PairCeiling.PairRow.W2_eq n s hs

/-- **(1) the generic regrouping**: the single sum over the frequency weighted by `W2` is the double sum over the band. -/
theorem sum_W2_mul (n : ℕ) (g : ℤ → ℝ) :
    ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)), W2 n s * g s
      = ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) * g (j1 + j2) :=
  Zeta23.PairCeiling.PairRow.sum_W2_mul n g

/-- **(1) the agreement lemma**: with no pair the unreduced row IS the shipped rational grid row. -/
theorem pairRow_eq_gridRowQ (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) :
    pairRow n m ∅ = gridRowQ n m :=
  Zeta23.PairCeiling.PairRow.pairRow_eq_gridRowQ n m

/-- **(1) the generating identity (T1)** at imaginary argument: `Σ_s W2(s) cosh(2πsx/N) = ā(x)²`. -/
theorem sum_W2_cosh (n : ℕ) (x : ℝ) :
    ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)),
        W2 n s * Real.cosh (2 * Real.pi * (s : ℝ) * x / (2 * (n : ℝ))) = abar n x ^ 2 :=
  Zeta23.PairCeiling.PairRow.sum_W2_cosh n x

/-- **(2) Prop. 4.5 for every `n`, depth and real mark**: `F1 − S2 = 2μ²ā(2d)² − 4μ(ā(d)² − 1)`, `S2 = 2n + 2μ²`. -/
theorem prop45 (n : ℕ) (d μ : ℝ) :
    pairRow n (vacancyMark n) {((0 : ZMod (2 * n + 1)), μ, d)} - (2 * (n : ℝ) + 2 * μ ^ 2)
      = 2 * μ ^ 2 * abar n (2 * d) ^ 2 - 4 * μ * (abar n d ^ 2 - 1) :=
  Zeta23.PairCeiling.PairRow.prop45 n d μ

/-- **(3) the log-convexity step** (pair-channel.md (T3)): `ā(d)² ≤ (1 + ā(2d))/2`. -/
theorem abar_sq_le (n : ℕ) (d : ℝ) : abar n d ^ 2 ≤ (1 + abar n (2 * d)) / 2 :=
  Zeta23.PairCeiling.PairRow.abar_sq_le n d

/-- **(3) the integer-mark safety chain**: for an INTEGER mark `m ≥ 1` the expression of `prop45` is positive. -/
theorem floor_holds_integer (n : ℕ) (d : ℝ) (m : ℕ) (hm : 1 ≤ m) :
    0 < 2 * (m : ℝ) ^ 2 * abar n (2 * d) ^ 2 - 4 * (m : ℝ) * (abar n d ^ 2 - 1) :=
  Zeta23.PairCeiling.PairRow.floor_holds_integer n d m hm

/-- **(4) the floor `F1 ≥ S2` FAILS at the anchor** `n = 32`, `(d, μ) = (1/4, 1/20)`, for the REAL mark `1/20`:
`pairRow < 64 + 2·(1/20)²`. -/
theorem floor_fails_anchor :
    pairRow 32 (vacancyMark 32) {((0 : ZMod 65), (1 / 20 : ℝ), (1 / 4 : ℝ))} < 64 + 2 * (1 / 20 : ℝ) ^ 2 :=
  Zeta23.PairCeiling.PairCert.floor_fails_anchor
