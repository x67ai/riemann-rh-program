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
comparator/Challenge/WeilContainmentOne.lean — CHALLENGE for rung 1 of the D5 unit (KICKSTART 10(l): one tilt level as a
complete Comparator pair before the family): the C1 containment identity at the level a = 1, C1's proven ray.
Trusted vocabulary: ChallengeDeps.WeilContainment (`WeilContainment.{tilt, weilTestOf, primeSide, tiltedPrimeSide}`, defined
over Mathlib alone).  Solution/WeilContainmentOne.lean (untrusted) proves exactly this statement;
github.com/leanprover/comparator checks statement equality, that only the axioms propext, Classical.choice, Quot.sound are
used, and replays the proof through the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  For every even g : ℝ → ℂ,
    Σ_n Λ(n) n^{−1} g(log n) = Σ_n (Λ(n)/√n) (k(log n) + k(−log n)),   k(u) = (1/2) g(u) e^{−|u|/2}:
the prime side of C1's tilted explicit formula at level 1 is the classical Weil-EF prime datum at the test k = weilTestOf 1 g.
NO displayed hypothesis: the statement is concrete, and it holds with no summability assumption (it is a term-by-term identity
of `tsum`s).  Nothing is claimed about the zero side of any explicit formula, about the Zeta23 test class (k is in general not
C¹ at u = 0), about the archimedean term, or about ζ.

The `sorry` below is deliberate (this is the challenge side); expect a "declaration uses 'sorry'" warning when building this
module.
-/
import ChallengeDeps.WeilContainment

noncomputable section

open WeilContainment

/-- **IV.1 at level a = 1**: the tilted prime side at level 1 equals the classical prime datum at the test weilTestOf 1 g. -/
theorem weilContainment_identity_one :
    ∀ g : ℝ → ℂ, (∀ u, g (-u) = g u) → tiltedPrimeSide 1 g = primeSide (weilTestOf 1 g) := by
  sorry
