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
comparator/ChallengeDeps/WeilContainment.lean — the TRUSTED definition layer for the comparator topics
`WeilContainmentOne` (rung 1: the tilt level a = 1) and `WeilContainment` (the whole family) of the barrier-zoo item IV.1,
the C1 containment theorem (rh-program/BARRIER-ZOO.md IV.1; source: results/adjudication-C1.json, fatal 2 and its mandatory
repair; build record rh-program/results/d5-lean-s30/BUILD-NOTES.md).

Everything the challenge statements mention is defined HERE, from Mathlib alone, in the namespace `WeilContainment`:
  tilt a u          := exp (−(a − 1/2) · |u|)                 the multiplier m_a(u) of the record ("bounded below on the
                                                              compact band");
  weilTestOf a g u  := (1/2) · g u · tilt a u                 the classical Weil test k_{a,g}(u) = (1/2) ĝ(u) e^{−(a−1/2)|u|}
                                                              of the record, with g standing for the cos-transform ĝ of C1's
                                                              window (the record's "(1/2) ŵ(u) e^{−(a−1/2)|u|}");
  primeSide k       := Σ'_{n : ℕ} (Λ(n)/√n) · (k (log n) + k (−log n))
                                                              the prime term of Zeta23's `literatureRHS`
                                                              (Zeta23/ExplicitFormula.lean, `literatureRHS`, the second line),
                                                              character for character, re-declared so that this module imports
                                                              nothing from Zeta23/ — the classical Weil-EF prime datum;
  tiltedPrimeSide a g := Σ'_{n : ℕ} Λ(n) · n^{−a} · g (log n)  the prime side of C1's tilted explicit formula
                                                              (directions/C1-requirements-first-field.md, MASTER FORMULA:
                                                              "Σ_{n ≤ X} Λ(n) n^{−a} (cos-transform of w)(log n)"), written as a
                                                              sum over ALL n : ℕ — Λ(0) = Λ(1) = 0, and for a band-limited g
                                                              the n > X terms vanish (theorem `weilContainment_cutoff`).
`Λ` is Mathlib's `ArithmeticFunction.vonMangoldt` (Λ(0) = 0), `√` is `Real.sqrt` (√0 = 0), `log` is `Real.log` (log 0 = 0),
`n^{−a}` is `Real.rpow` on the cast (n : ℝ), and the sums are `tsum` (0 when not summable; with a band-limited test both sums are
finite, so no summability question arises for the data the record speaks of).  Evenness of a test is spelled out in the
challenge statements as `∀ u, g (−u) = g u`.  A reader who wants to know WHAT is claimed reads this file and the challenge
files only.
-/
import Mathlib

namespace WeilContainment

noncomputable section

/-- the multiplier m_a(u) = exp(−(a − 1/2)·|u|). -/
def tilt (a u : ℝ) : ℝ := Real.exp (-(a - 1 / 2) * |u|)

/-- the classical Weil test attached to the level a and the even function g: k_{a,g}(u) = (1/2)·g(u)·m_a(u). -/
def weilTestOf (a : ℝ) (g : ℝ → ℂ) (u : ℝ) : ℂ := (1 / 2 : ℂ) * g u * (tilt a u : ℂ)

/-- the classical Weil-EF prime datum of a test k — the prime term of Zeta23's `literatureRHS`, character for character:
Σ_{n : ℕ} (Λ(n)/√n)·(k(log n) + k(−log n)). -/
def primeSide (k : ℝ → ℂ) : ℂ :=
  ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ)
      * (k (Real.log n) + k (-Real.log n))

/-- the prime side of C1's tilted explicit formula at level a: Σ_{n : ℕ} Λ(n)·n^{−a}·g(log n). -/
def tiltedPrimeSide (a : ℝ) (g : ℝ → ℂ) : ℂ :=
  ∑' n : ℕ, ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) * g (Real.log n)

end

end WeilContainment
