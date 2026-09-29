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
comparator/Challenge/PairChannel.lean — CHALLENGE for the H4 unit: barrier-zoo IV.17's PAIR CHANNEL as ONE topic — the
pair-containing bandwidth-one Frobenius row of the A4 no-go paper §2.3, Prop. 4.5 of §4.2 (= pair-channel.md Prop. 3.1) for
every n, depth and REAL mark, the integer-mark safety chain, and the floor F1 ≥ S2's FAILURE for a real mark at the record's
anchor (d, μ) = (1/4, 1/20) — kernel-checked (unit brief rh-program/results/h4-pair-typing-s32/UNIT-BRIEF.md; formalization-queue
item 10's pair-channel sub-item; paper.md §2.3, §4.2; pair-channel.md §0–§4).  Trusted vocabulary: ChallengeDeps.PairChannel
(`PairChannel.{chi, dftMark, dftMarkQ, zetaM, gridRow, gridRowQ, fracMark, W2, pairFormFactor, pairRow, abar, vacancyMark}`,
defined over Mathlib alone).  Solution/PairChannel.lean (untrusted) proves exactly these statements; github.com/leanprover/comparator
checks statement equality, that only the axioms propext, Classical.choice, Quot.sound are used, and replays the proofs through
the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  On the (2n+1)-site uniform grid, circle length N = 2n, flat harmonics u_j = 1/(2n+1) on the
band {−n, …, n}, with the row `pairRow` over the UNREDUCED integer frequency s ∈ [−2n, 2n] (the pair's factor 2μ cosh(2πsd/N)
is not periodic mod 2n+1, so the shipped reduced rows `gridRow`/`gridRowQ` cannot hold a pair):
  (1) `W2_eq` — the assembly weight is the closed form (2n+1 − |s|)/(2n+1)² on the band (pair-channel.md line 39);
      `sum_W2_mul` — the generic regrouping Σ_s W2(s) g(s) = Σ_{j₁,j₂} (1/M)² g(j₁+j₂);
      `pairRow_eq_gridRowQ` — with NO pair the new row IS the shipped rational grid row (the agreement lemma);
      `sum_W2_cosh` — the generating identity (T1) of pair-channel.md line 71 at q = e^{β}: Σ_s W2(s) cosh(2πsx/N) = ā(x)².
  (2) `prop45` — Prop. 4.5 for EVERY n, EVERY depth d and EVERY real mark μ: on the vacancy lattice (unit atoms on the 2n sites
      k ≠ 0) plus one pair at the hole 0, F1 − S2 = 2μ²ā(2d)² − 4μ(ā(d)² − 1) exactly, S2 = 2n + 2μ² (paper §4.2's display).
  (3) `abar_sq_le` — the log-convexity step ā(d)² ≤ (1 + ā(2d))/2 (pair-channel.md (T3), Cauchy–Schwarz on the flat weights);
      `floor_holds_integer` — the integer-mark safety chain: for an INTEGER mark m ≥ 1 the expression of `prop45` is > 0
      (paper §4.2 "For integer marks the same family is safe").  Integrality enters here, as 1 ≤ m, and nowhere else.
  (4) `floor_fails_anchor` — at n = 32 (N = 64), (d, μ) = (1/4, 1/20): pairRow < 64 + 2·(1/20)², i.e. the floor F1 ≥ S2 FAILS for
      this real mark (the record's F1 − S2 = −3.520·10⁻²; the certificate's bound −0.0336), kernel-checked through two generic
      cosh bounds, four integer power sums and Mathlib's π bracket (Solution side: Zeta23/PairCeiling/PairCert.lean).
NO displayed hypothesis beyond what the statements carry (`n : ℕ`, `d μ : ℝ`, `1 ≤ m`, the band membership of `W2_eq`).
What is NOT claimed: nothing about (MI) F1 ≥ 3M − 2N_d at any anchor — at THIS anchor (MI) HOLDS (T = 60.3, F1 − T = +3.67) and
`floor_fails_anchor` is the failure of the floor F1 ≥ S2 for a real mark, nothing more; nothing about Theorems 4.6–4.9 of the
paper (the pair channel's closure stays at paper grade); nothing about laws, the LP, pairs at general (off-grid) positions, any
budget other than the bandwidth-one row; nothing about ζ or RH.

The `sorry`s below are deliberate (this is the challenge side); expect "declaration uses 'sorry'" warnings when building this
module.
-/
import ChallengeDeps.PairChannel

noncomputable section

open Finset PairChannel

/-- **(1) the closed-form weight** of pair-channel.md line 39: `W2(s) = (M − |s|)/M²` for `|s| ≤ 2n`, `M = 2n + 1`. -/
theorem W2_eq (n : ℕ) (s : ℤ) (hs : s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ))) :
    W2 n s = ((2 * (n : ℝ) + 1) - |(s : ℝ)|) / (2 * (n : ℝ) + 1) ^ 2 := by
  sorry

/-- **(1) the generic regrouping**: the single sum over the frequency weighted by `W2` is the double sum over the band. -/
theorem sum_W2_mul (n : ℕ) (g : ℤ → ℝ) :
    ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)), W2 n s * g s
      = ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) * g (j1 + j2) := by
  sorry

/-- **(1) the agreement lemma**: with no pair the unreduced row IS the shipped rational grid row. -/
theorem pairRow_eq_gridRowQ (n : ℕ) (m : ZMod (2 * n + 1) → ℚ) :
    pairRow n m ∅ = gridRowQ n m := by
  sorry

/-- **(1) the generating identity (T1)** at imaginary argument: `Σ_s W2(s) cosh(2πsx/N) = ā(x)²`. -/
theorem sum_W2_cosh (n : ℕ) (x : ℝ) :
    ∑ s ∈ Finset.Icc (-(2 * (n : ℤ))) (2 * (n : ℤ)),
        W2 n s * Real.cosh (2 * Real.pi * (s : ℝ) * x / (2 * (n : ℝ))) = abar n x ^ 2 := by
  sorry

/-- **(2) Prop. 4.5 for every `n`, depth and real mark**: `F1 − S2 = 2μ²ā(2d)² − 4μ(ā(d)² − 1)`, `S2 = 2n + 2μ²`. -/
theorem prop45 (n : ℕ) (d μ : ℝ) :
    pairRow n (vacancyMark n) {((0 : ZMod (2 * n + 1)), μ, d)} - (2 * (n : ℝ) + 2 * μ ^ 2)
      = 2 * μ ^ 2 * abar n (2 * d) ^ 2 - 4 * μ * (abar n d ^ 2 - 1) := by
  sorry

/-- **(3) the log-convexity step** (pair-channel.md (T3)): `ā(d)² ≤ (1 + ā(2d))/2`. -/
theorem abar_sq_le (n : ℕ) (d : ℝ) : abar n d ^ 2 ≤ (1 + abar n (2 * d)) / 2 := by
  sorry

/-- **(3) the integer-mark safety chain**: for an INTEGER mark `m ≥ 1` the expression of `prop45` is positive. -/
theorem floor_holds_integer (n : ℕ) (d : ℝ) (m : ℕ) (hm : 1 ≤ m) :
    0 < 2 * (m : ℝ) ^ 2 * abar n (2 * d) ^ 2 - 4 * (m : ℝ) * (abar n d ^ 2 - 1) := by
  sorry

/-- **(4) the floor `F1 ≥ S2` FAILS at the anchor** `n = 32`, `(d, μ) = (1/4, 1/20)`, for the REAL mark `1/20`:
`pairRow < 64 + 2·(1/20)²`. -/
theorem floor_fails_anchor :
    pairRow 32 (vacancyMark 32) {((0 : ZMod 65), (1 / 20 : ℝ), (1 / 4 : ℝ))} < 64 + 2 * (1 / 20 : ℝ) ^ 2 := by
  sorry
