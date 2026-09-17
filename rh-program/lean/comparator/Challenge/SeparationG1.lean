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
comparator/Challenge/SeparationG1.lean — CHALLENGE for the dress-rehearsal rung of M4 (i): Lemma G1 of Theorem M2's
separation note (rh-program/results/c2-m2/separation-note.md §2), the derivative bounds for the bump B_raw.
Trusted vocabulary: ChallengeDeps.Separation (`Separation.Braw`, defined by the exp formula over Mathlib alone) and
Mathlib's `iteratedDeriv`.  Solution/SeparationG1.lean (untrusted) proves exactly this statement by delegating to
Zeta23/Separation/LemmaG1.lean; github.com/leanprover/comparator checks statement equality, that only the axioms
propext, Classical.choice, Quot.sound are used, and replays the proof through the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  For every k ≥ 1 and every real v,
    |B_raw^{(k)}(v)| ≤ (k + 1) · (72/e)^k · k^{2k},
with B_raw(v) = exp(−1/(1 − 4v²)) on |v| < 1/2 and 0 elsewhere, and `iteratedDeriv` Mathlib's k-th derivative of a
real function (for a C^∞ function it is the classical k-th derivative).  NO displayed hypothesis: the statement is
concrete.  Nothing is claimed about the Fourier transform of B (that is the topic `Separation`, Challenge/Separation.lean),
about the numerical size of any derivative (the bound is generous by design — the note records factors 10²–10⁸ at k ≤ 6),
or about ζ.  The constant 72/e is 4·(18/e): the Cauchy-estimate constant of Zeta23's `gevrey_expNegInvGlue` times the
affine factor 4 of the factorization B_raw(v) = g(4v + 2)·g(2 − 4v); that provenance is a solution-side fact, not part
of this statement.

The `sorry` below is deliberate (this is the challenge side); expect a "declaration uses 'sorry'" warning when building
this module.
-/
import ChallengeDeps.Separation

noncomputable section

/-- **Lemma G1** (separation note §2): |B_raw^{(k)}(v)| ≤ (k + 1)·(72/e)^k·k^{2k} for every k ≥ 1 and every real v. -/
theorem separation_braw_iteratedDeriv_le :
    ∀ k : ℕ, 1 ≤ k → ∀ v : ℝ,
      |iteratedDeriv k Separation.Braw v| ≤ ((k : ℝ) + 1) * (72 / Real.exp 1) ^ k * (k : ℝ) ^ (2 * k) := by
  sorry
