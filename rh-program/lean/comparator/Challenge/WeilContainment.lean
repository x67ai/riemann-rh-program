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
comparator/Challenge/WeilContainment.lean — CHALLENGE for the D5 unit: the C1 containment theorem, barrier-zoo item IV.1
(rh-program/BARRIER-ZOO.md IV.1; results/adjudication-C1.json fatal 2: "the family spans exactly bandwidth-log X Weil-EF data").
Trusted vocabulary: ChallengeDeps.WeilContainment (`WeilContainment.{tilt, weilTestOf, primeSide, tiltedPrimeSide}`, defined
over Mathlib alone).  Solution/WeilContainment.lean (untrusted) proves exactly these statements;
github.com/leanprover/comparator checks statement equality, that only the axioms propext, Classical.choice, Quot.sound are
used, and replays the proofs through the Lean kernel and nanoda.

WHAT IS CLAIMED, and what is NOT.  With m_a(u) = e^{−(a−1/2)|u|} and k_{a,g}(u) = (1/2) g(u) m_a(u):
  (T1) `weilContainment_identity`  — for every real a and every even g, the level-a tilted prime side
        Σ_n Λ(n) n^{−a} g(log n) equals the classical Weil-EF prime datum Σ_n (Λ(n)/√n)(k(log n) + k(−log n)) at k = k_{a,g};
        `weilContainment_cutoff` — for tsupport g ⊆ [−L, L] the tilted prime side is the FINITE sum over n ≤ e^L
        (the record's "n ≤ X" cutoff, X = e^L, is a theorem, not a convention).
  (T2) `weilContainment_tilt_bounds`, `weilContainment_tilt_pos` — on |u| ≤ L, e^{−|a−1/2| L} ≤ m_a(u) ≤ e^{|a−1/2| L};
        m_a > 0 everywhere (the record's "bounded below on the compact band", with the explicit constants).
  (T3) `weilContainment_even`, `weilContainment_tsupport`, `weilContainment_tsupport_eq`, `weilContainment_continuous` —
        k_{a,g} is even when g is, has EXACTLY the support of g (so the same band), and is continuous when g is;
        `weilContainment_tilt_inv` — m_a · m_{1−a} = 1 (the level-(1−a) tilt inverts the level-a tilt);
        `weilContainment_exact` — every classical prime datum of an even test on the band [−L, L] is a level-a tilted datum
        of an even g on the same band, for every a;
        `weilContainment_range_eq` — the record's sentence as one statement: for every real a and L, the SET of level-a tilted
        prime data over even band-[−L, L] tests EQUALS the set of classical Weil-EF prime data over even band-[−L, L] tests.
NO displayed hypothesis anywhere: every statement is concrete, and (T1) holds with no summability assumption (it is a
term-by-term identity of `tsum`s; with a band-limited test both sums are finite).  What is NOT claimed: nothing about the ZERO
side of any explicit formula at any level (the record's fatal 1, the in-window "cosh ghost", is untouched); nothing about the
Zeta23 test class — k_{a,g} is in general not C¹ at u = 0 when a ≠ 1/2 and g(0) ≠ 0, so no statement here feeds k_{a,g} into
`EF_lit` (the witness `weilContainment_not_contDiff`: at a = 1 and g ≡ 1 the test k_{1,1}(u) = (1/2)e^{−|u|/2} is NOT C², so the
C² class is not preserved by the tilt — the one NEGATIVE statement of the topic, stated so that the ledger's "not covered" is a
theorem and not a remark); nothing about nonlinear functions of the band (the μ-band, IV.4); nothing about ζ or RH.  The classical data class
here is "even, band-limited" with no regularity; the refinement into the C² class (by finite interpolation at the points ±log n)
is not formalized.

The `sorry`s below are deliberate (this is the challenge side); expect "declaration uses 'sorry'" warnings when building this
module.
-/
import ChallengeDeps.WeilContainment

noncomputable section

open WeilContainment

/-- **(T1) the containment identity**: for every real a and every even g, the level-a tilted prime side is the classical
prime datum at the test k_{a,g}. -/
theorem weilContainment_identity :
    ∀ (a : ℝ) (g : ℝ → ℂ), (∀ u, g (-u) = g u) →
      tiltedPrimeSide a g = primeSide (weilTestOf a g) := by
  sorry

/-- **(T1′) the cutoff**: for tsupport g ⊆ [−L, L] the tilted prime side is the finite sum over 0 ≤ n ≤ ⌊e^L⌋. -/
theorem weilContainment_cutoff :
    ∀ (a L : ℝ) (g : ℝ → ℂ), tsupport g ⊆ Set.Icc (-L) L →
      tiltedPrimeSide a g = ∑ n ∈ Finset.range (⌊Real.exp L⌋₊ + 1),
        ((ArithmeticFunction.vonMangoldt n : ℝ) : ℂ) * (((n : ℝ) ^ (-a) : ℝ) : ℂ) * g (Real.log n) := by
  sorry

/-- **(T2) the multiplier bounds** on the band |u| ≤ L: e^{−|a−1/2| L} ≤ m_a(u) ≤ e^{|a−1/2| L}. -/
theorem weilContainment_tilt_bounds :
    ∀ (a L u : ℝ), |u| ≤ L →
      Real.exp (-(|a - 1 / 2| * L)) ≤ tilt a u ∧ tilt a u ≤ Real.exp (|a - 1 / 2| * L) := by
  sorry

/-- **(T2) positivity**: m_a(u) > 0 for every a and u. -/
theorem weilContainment_tilt_pos : ∀ (a u : ℝ), 0 < tilt a u := by
  sorry

/-- **(T3) the inverse**: m_a(u)·m_{1−a}(u) = 1. -/
theorem weilContainment_tilt_inv : ∀ (a u : ℝ), tilt a u * tilt (1 - a) u = 1 := by
  sorry

/-- **(T3) evenness**: k_{a,g} is even when g is. -/
theorem weilContainment_even :
    ∀ (a : ℝ) (g : ℝ → ℂ), (∀ u, g (-u) = g u) → ∀ u, weilTestOf a g (-u) = weilTestOf a g u := by
  sorry

/-- **(T3) the band**: tsupport k_{a,g} ⊆ tsupport g. -/
theorem weilContainment_tsupport :
    ∀ (a : ℝ) (g : ℝ → ℂ), tsupport (weilTestOf a g) ⊆ tsupport g := by
  sorry

/-- **(T3) the band, exactly**: tsupport k_{a,g} = tsupport g. -/
theorem weilContainment_tsupport_eq :
    ∀ (a : ℝ) (g : ℝ → ℂ), tsupport (weilTestOf a g) = tsupport g := by
  sorry

/-- **(T3) continuity**: k_{a,g} is continuous when g is. -/
theorem weilContainment_continuous :
    ∀ (a : ℝ) (g : ℝ → ℂ), Continuous g → Continuous (weilTestOf a g) := by
  sorry

/-- **(T3) the converse containment**: every classical prime datum of an even test k on the band [−L, L] is the level-a
tilted datum of an even g on the same band. -/
theorem weilContainment_exact :
    ∀ (a L : ℝ) (k : ℝ → ℂ), (∀ u, k (-u) = k u) → tsupport k ⊆ Set.Icc (-L) L →
      ∃ g : ℝ → ℂ, (∀ u, g (-u) = g u) ∧ tsupport g ⊆ Set.Icc (-L) L ∧ primeSide k = tiltedPrimeSide a g := by
  sorry

/-- **IV.1, the record's sentence**: for every real a and L, the level-a tilted prime data over even band-[−L, L] tests are
EXACTLY the classical Weil-EF prime data over even band-[−L, L] tests. -/
theorem weilContainment_range_eq :
    ∀ (a L : ℝ),
      {x : ℂ | ∃ g : ℝ → ℂ, (∀ u, g (-u) = g u) ∧ tsupport g ⊆ Set.Icc (-L) L ∧ x = tiltedPrimeSide a g} =
      {x : ℂ | ∃ k : ℝ → ℂ, (∀ u, k (-u) = k u) ∧ tsupport k ⊆ Set.Icc (-L) L ∧ x = primeSide k} := by
  sorry

/-- **The C² class is not preserved** (witness): at a = 1 and g ≡ 1 the test k_{1,1}(u) = (1/2)·e^{−|u|/2} is not C² (it is not
even differentiable at u = 0). -/
theorem weilContainment_not_contDiff : ¬ ContDiff ℝ 2 (weilTestOf 1 (fun _ => (1 : ℂ))) := by
  sorry
