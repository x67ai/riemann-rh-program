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
Zeta23/PairCeiling/GridGap.lean — the INTEGRALITY GAP of barrier-zoo IV.17 on the grid Frobenius row: the master
inequality (MI) `3·Σm − Σm² ≤ 2·N_d` HOLDS over integer marks (`mi_holds_integer` = GridParseval's
`two_mul_distinct_ge`, re-exported) and FAILS over rational marks on the SAME row (`mi_fails_rational`), witnessed by
the zoo's mark-4/3 instance (`fracMark`: 48 atoms of mark 4/3 on the 65-site grid; mass 64, Σm² = 256/3, N_d = 48,
3·64 − 2·48 = 96 > 256/3), and the 5/6 corner fails with it at ε = 0 (`corner_fails_rational`,
`corner_bound_fails_rational`).  Formalization-queue item 10; brief rh-program/results/iv17-lean-s30/BRIEF.md,
clauses (2)–(4).

Provenance: rh-program/BARRIER-ZOO.md IV.17 STATEMENT ("(MI) is FALSE for fractional marks, at the baseline itself:
mass N of mark-4/3 atoms on the (N+1)-site grid … has F1 = (3/4)N·(16/9) = (4/3)N, budget-tight, and
N_d = (3/4)N < (5/6)N, while (MI) would demand F1 ≥ 3N − (3/2)N = (3/2)N") and EXECUTABLE TEST (1), (3);
results/a4-no-go/paper.md §2.4 (the mark-4/3 baseline failure), §4.2 ((MI), the "textbook integrality gap" Reading);
results/a4-no-go/theorems.md Lemma 2.2 (the two integrality levels), Theorem 2.3.

THE LINE WHERE INTEGRALITY IS CONSUMED (IV.17 TEST (3)).  `per_atom_slack : ∀ m : ℤ, 0 ≤ (m − 1)(m − 2)` — the
per-atom slack of Lemma 2.2(a) — is the whole content of (MI): summed over sites it is `Σ (3m − m²) ≤ 2·#{m ≠ 0}`
(the step `nlinarith [(m − 1)(m − 2) ≥ 0]` inside `two_mul_distinct_ge`).  It is an INTEGER statement: over ℚ it is
false at `m = 4/3` (value −2/9; `per_atom_slack_fails_rational`), and that single failure, 48 times over, is the whole
counterexample.  The mark-1 floor `m ≤ m²` (the second device TEST (3) names) is `per_atom_floor`, false over ℚ at
`m = 1/2` (`per_atom_floor_fails_rational`).

WHAT IS AND IS NOT HERE.  Here: the bandwidth-one grid Frobenius row (GridParseval Theorem 1.2 / paper Theorem 3.9,
`gridRow`/`gridRowQ`), integer versus rational marks on it, the corner at ε = 0.  NOT here: laws (probability mixtures
of columns) — the pointwise failure of the corner bound implies the failure of its law form, but no law-form negation
is stated; the pair channel (paper Prop. 4.5 — "paper-certificate grade", item 10); the two-sided band; anything about
ζ.  The instance sits at ε = 0 (budget-tight, the zoo's "F1 = (4/3)N") — the corner theorem `grid_corner_pointwise`
of GridCorner.lean holds for every ε, and its ε = 0 case is the one contradicted.

Trust model: everything is proved from Mathlib with no `sorry` and no `native_decide`; the five column-data facts of
the instance (`fracMark_mass`, `fracMark_sq`, `fracMark_Nd`, and the two used through them) are kernel-checked
(`decide +kernel`, NumericCert discipline); the transcendental object is `Complex.exp` through `zetaM`, as in
GridParseval.lean.
-/
import Zeta23.PairCeiling.GridParsevalRat

noncomputable section

open Finset

namespace Zeta23
namespace PairCeiling
namespace GridGap

open GridParseval GridCorner GridParsevalRat

/-! ## 1. The two integrality devices, and their failure over ℚ -/

/-- **theorems.md Lemma 2.2(a), the per-atom slack**: `(m − 1)(m − 2) ≥ 0` for EVERY integer `m` — the product of
two consecutive integers is nonnegative.  This is the line where the master inequality consumes integrality
(IV.17 TEST (3)); equality iff `m ∈ {1, 2}`. -/
theorem per_atom_slack (m : ℤ) : 0 ≤ (m - 1) * (m - 2) := by
  rcases (by omega : m ≤ 1 ∨ 2 ≤ m) with h | h
  · have h1 : 0 ≤ 1 - m := by omega
    have h2 : 0 ≤ 2 - m := by omega
    nlinarith [mul_nonneg h1 h2]
  · have h1 : 0 ≤ m - 1 := by omega
    have h2 : 0 ≤ m - 2 := by omega
    nlinarith [mul_nonneg h1 h2]

/-- the per-atom slack is FALSE over the rationals: at `m = 4/3`, `(m − 1)(m − 2) = −2/9 < 0`. -/
theorem per_atom_slack_fails_rational : ¬ ∀ q : ℚ, 0 ≤ q → 0 ≤ (q - 1) * (q - 2) := by
  intro h
  have := h (4 / 3) (by norm_num)
  norm_num at this

/-- **the mark-1 floor** `m ≤ m²` for every integer `m` (the second integrality device IV.17 TEST (3) names). -/
theorem per_atom_floor (m : ℤ) : m ≤ m ^ 2 := by
  rcases (by omega : m ≤ 0 ∨ 1 ≤ m) with h | h
  · nlinarith [sq_nonneg m]
  · nlinarith

/-- the mark-1 floor is FALSE over the rationals: at `m = 1/2`, `m² = 1/4 < m`. -/
theorem per_atom_floor_fails_rational : ¬ ∀ q : ℚ, 0 ≤ q → q ≤ q ^ 2 := by
  intro h
  have := h (1 / 2) (by norm_num)
  norm_num at this

/-! ## 2. The master inequality over integer marks (re-export) -/

/-- **(MI) over integer marks** (barrier-zoo IV.17, paper §4.2): for nonnegative integer marks on any grid,
`3·Σm − Σm² ≤ 2·N_d`, `N_d` the number of occupied sites — GridParseval's `two_mul_distinct_ge` re-exported under the
topic's name.  Its proof consumes integrality at exactly `per_atom_slack`. -/
theorem mi_holds_integer {M : ℕ} [NeZero M] (m : ZMod M → ℤ) (hm : ∀ k, 0 ≤ m k) :
    3 * (∑ k : ZMod M, m k) - (∑ k : ZMod M, (m k) ^ 2)
      ≤ 2 * ((Finset.univ.filter (fun k : ZMod M => m k ≠ 0)).card : ℤ) :=
  two_mul_distinct_ge m hm

/-! ## 3. The instance: 48 atoms of mark 4/3 on the 65-site grid (N = 64) -/

/-- the zoo's mark-4/3 column at `N = 64`: 48 atoms of mark `4/3` on distinct sites of the `(N+1) = 65`-site grid,
the other 17 sites empty (BARRIER-ZOO.md item 10: "N = 64: 48 atoms of mark 4/3 on distinct grid sites"). -/
def fracMark : ZMod 65 → ℚ := fun k => if k.val < 48 then 4 / 3 else 0

/-- the column's marks are nonnegative. -/
theorem fracMark_nonneg : ∀ k : ZMod 65, 0 ≤ fracMark k := by
  intro k
  simp only [fracMark]
  split_ifs <;> norm_num

/-- kernel-checked column data: mass `Σ m = 64` (`= (3/4)·64 · 4/3`). -/
theorem fracMark_mass : ∑ k : ZMod 65, fracMark k = 64 := by decide +kernel

/-- kernel-checked column data: `Σ m² = 256/3 = (4/3)·64` — the budget-tight `F1 = (4/3)N`. -/
theorem fracMark_sq : ∑ k : ZMod 65, (fracMark k) ^ 2 = 256 / 3 := by decide +kernel

/-- kernel-checked column data: `N_d = 48 = (3/4)·64` occupied sites. -/
theorem fracMark_Nd :
    (Finset.univ.filter (fun k : ZMod 65 => fracMark k ≠ 0)).card = 48 := by decide +kernel

/-- the column's grid Frobenius row is EXACTLY the budget at `ε = 0`: `gridRowQ 32 fracMark = 256/3 = (4/3)·64·(1 + 0)`
(rational grid Parseval, `gridRowQ_eq`, plus the kernel fact `fracMark_sq`). -/
theorem fracMark_row : gridRowQ 32 fracMark = 4 / 3 * 64 * (1 + 0) := by
  rw [gridRowQ_eq 32 fracMark, fracMark_sq]
  norm_num

/-! ## 4. The negations -/

/-- **(MI) is FALSE over rational marks** (IV.17 STATEMENT, EXECUTABLE TEST (1)): the statement of `mi_holds_integer`
with `ℚ` in place of `ℤ` fails on the 65-site grid, witnessed by `fracMark` — there `3·Σm − Σm² = 192 − 256/3 = 320/3`
while `2·N_d = 96`, i.e. (MI) would demand `F1 ≥ 3·64 − 2·48 = 96 > 256/3 = F1`. -/
theorem mi_fails_rational :
    ¬ ∀ (m : ZMod 65 → ℚ), (∀ k, 0 ≤ m k) →
      3 * (∑ k : ZMod 65, m k) - (∑ k : ZMod 65, (m k) ^ 2)
        ≤ 2 * ((Finset.univ.filter (fun k : ZMod 65 => m k ≠ 0)).card : ℚ) := by
  intro h
  have hmi := h fracMark fracMark_nonneg
  rw [fracMark_mass, fracMark_sq, fracMark_Nd] at hmi
  norm_num at hmi

/-- **the 5/6 corner fails for fractional marks on the grid at `ε = 0`** (IV.17 STATEMENT, verbatim numbers): the
column `fracMark` has nonnegative marks, mass `64`, grid row `≤ (4/3)·64·(1 + 0)` (budget-tight), and
`N_d = 48 < 64·(5/6 − (2/3)·0)` — every hypothesis of `grid_corner_pointwise` (GridCorner.lean) at `N = 64`, `ε = 0`,
and the negation of its first conclusion. -/
theorem corner_fails_rational :
    (∀ k, 0 ≤ fracMark k) ∧
    ∑ k : ZMod 65, fracMark k = 64 ∧
    gridRowQ 32 fracMark ≤ 4 / 3 * 64 * (1 + 0) ∧
    ((Finset.univ.filter (fun k : ZMod 65 => fracMark k ≠ 0)).card : ℝ) < 64 * (5 / 6 - 2 / 3 * 0) := by
  refine ⟨fracMark_nonneg, fracMark_mass, le_of_eq fracMark_row, ?_⟩
  rw [fracMark_Nd]
  norm_num

/-- the corner bound of `grid_corner_pointwise` (first conclusion), stated for RATIONAL marks at `N = 64`, `ε = 0`, is
FALSE: no theorem of that shape exists over ℚ. -/
theorem corner_bound_fails_rational :
    ¬ ∀ (m : ZMod 65 → ℚ), (∀ k, 0 ≤ m k) → ∑ k : ZMod 65, m k = 64 →
      gridRowQ 32 m ≤ 4 / 3 * 64 * (1 + 0) →
      (64 : ℝ) * (5 / 6 - 2 / 3 * 0)
        ≤ ((Finset.univ.filter (fun k : ZMod 65 => m k ≠ 0)).card : ℝ) := by
  intro h
  have hc := h fracMark fracMark_nonneg fracMark_mass (le_of_eq fracMark_row)
  rw [fracMark_Nd] at hc
  norm_num at hc

end GridGap
end PairCeiling
end Zeta23
