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
comparator/Solution/IntegralityGap.lean — the UNTRUSTED comparator solution module for the topic `IntegralityGap`
(barrier-zoo IV.17): the sixteen statements of Challenge/IntegralityGap.lean, byte-identical, PROVED by delegating to
Zeta23/PairCeiling/GridCorner.lean (`gridRow_eq`), GridParsevalRat.lean (`trace_sq_grid_rat`, `gridRowQ_eq`,
`gridRow_eq_gridRowQ`) and GridGap.lean (everything else).  The challenge's `IntegralityGap.{chi, dftMark, dftMarkQ, zetaM,
gridRow, gridRowQ, fracMark}` are character for character the Zeta23 definitions, so each delegation typechecks by
definitional unfolding in the kernel.  This module never imports the challenge.  Nothing in this file is part of the
trusted base: comparator re-checks that each theorem below has exactly the statement of its Challenge namesake and uses
only the permitted axioms.
-/
import ChallengeDeps.IntegralityGap
import Zeta23.PairCeiling.GridGap

noncomputable section

open Finset IntegralityGap

/-- **(1) grid Parseval with rational marks, normalized**: the literal Frobenius row equals `Σ_k m_k²`. -/
theorem trace_sq_grid_rat :
    ∀ (n : ℕ) (m : ZMod (2 * n + 1) → ℚ),
      ∑ j1 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ), ∑ j2 ∈ Finset.Icc (-(n : ℤ)) (n : ℤ),
          (1 / (2 * (n : ℝ) + 1)) * (1 / (2 * (n : ℝ) + 1)) *
            Complex.normSq (dftMarkQ (zetaM (2 * n + 1)) m
              ((j1 : ZMod (2 * n + 1)) + (j2 : ZMod (2 * n + 1))))
        = ∑ k : ZMod (2 * n + 1), (m k : ℝ) ^ 2 :=
  fun n m => Zeta23.PairCeiling.GridParsevalRat.trace_sq_grid_rat n m

/-- **(1) the rational row as a named quantity**: `gridRowQ n m = Σ_k m_k²` (cast to ℝ). -/
theorem gridRowQ_eq :
    ∀ (n : ℕ) (m : ZMod (2 * n + 1) → ℚ),
      gridRowQ n m = ((∑ k : ZMod (2 * n + 1), (m k) ^ 2 : ℚ) : ℝ) :=
  fun n m => Zeta23.PairCeiling.GridParsevalRat.gridRowQ_eq n m

/-- **(1) the integer row** (GridCorner's `gridRow_eq`): `gridRow n m = Σ_k m_k²` (cast to ℝ). -/
theorem gridRow_eq :
    ∀ (n : ℕ) (m : ZMod (2 * n + 1) → ℤ),
      gridRow n m = ((∑ k : ZMod (2 * n + 1), (m k) ^ 2 : ℤ) : ℝ) :=
  fun n m => Zeta23.PairCeiling.GridCorner.gridRow_eq n m

/-- **(1) one row**: the integer row is the rational row of the cast marks. -/
theorem gridRow_eq_gridRowQ :
    ∀ (n : ℕ) (m : ZMod (2 * n + 1) → ℤ),
      gridRow n m = gridRowQ n (fun k => (m k : ℚ)) :=
  fun n m => Zeta23.PairCeiling.GridParsevalRat.gridRow_eq_gridRowQ n m

/-- **(2) instance data, kernel-checked**: mass `Σ m = 64`. -/
theorem fracMark_mass : ∑ k : ZMod 65, fracMark k = 64 :=
  Zeta23.PairCeiling.GridGap.fracMark_mass

/-- **(2) instance data, kernel-checked**: `Σ m² = 256/3`. -/
theorem fracMark_sq : ∑ k : ZMod 65, (fracMark k) ^ 2 = 256 / 3 :=
  Zeta23.PairCeiling.GridGap.fracMark_sq

/-- **(2) instance data, kernel-checked**: `N_d = 48` occupied sites. -/
theorem fracMark_Nd :
    (Finset.univ.filter (fun k : ZMod 65 => fracMark k ≠ 0)).card = 48 :=
  Zeta23.PairCeiling.GridGap.fracMark_Nd

/-- **(2) the instance's grid row is exactly the budget at `ε = 0`**: `gridRowQ 32 fracMark = (4/3)·64·(1 + 0)`. -/
theorem fracMark_row : gridRowQ 32 fracMark = 4 / 3 * 64 * (1 + 0) :=
  Zeta23.PairCeiling.GridGap.fracMark_row

/-- **(3) (MI) is FALSE over rational marks**: the integer theorem's statement with `ℚ` for `ℤ` fails on the 65-site grid. -/
theorem mi_fails_rational :
    ¬ ∀ (m : ZMod 65 → ℚ), (∀ k, 0 ≤ m k) →
      3 * (∑ k : ZMod 65, m k) - (∑ k : ZMod 65, (m k) ^ 2)
        ≤ 2 * ((Finset.univ.filter (fun k : ZMod 65 => m k ≠ 0)).card : ℚ) :=
  Zeta23.PairCeiling.GridGap.mi_fails_rational

/-- **(3) the 5/6 corner fails for fractional marks on the grid at `ε = 0`**: `fracMark` has nonnegative marks, mass 64,
grid row `≤ (4/3)·64·(1 + 0)`, and `N_d = 48 < 64·(5/6 − (2/3)·0)`. -/
theorem corner_fails_rational :
    (∀ k, 0 ≤ fracMark k) ∧
    ∑ k : ZMod 65, fracMark k = 64 ∧
    gridRowQ 32 fracMark ≤ 4 / 3 * 64 * (1 + 0) ∧
    ((Finset.univ.filter (fun k : ZMod 65 => fracMark k ≠ 0)).card : ℝ) < 64 * (5 / 6 - 2 / 3 * 0) :=
  Zeta23.PairCeiling.GridGap.corner_fails_rational

/-- **(3) the corner bound, stated for rational marks at `N = 64`, `ε = 0`, is FALSE.** -/
theorem corner_bound_fails_rational :
    ¬ ∀ (m : ZMod 65 → ℚ), (∀ k, 0 ≤ m k) → ∑ k : ZMod 65, m k = 64 →
      gridRowQ 32 m ≤ 4 / 3 * 64 * (1 + 0) →
      (64 : ℝ) * (5 / 6 - 2 / 3 * 0)
        ≤ ((Finset.univ.filter (fun k : ZMod 65 => m k ≠ 0)).card : ℝ) :=
  Zeta23.PairCeiling.GridGap.corner_bound_fails_rational

/-- **(4) (MI) HOLDS over integer marks** on every grid: `3·Σm − Σm² ≤ 2·N_d` for nonnegative integer marks. -/
theorem mi_holds_integer :
    ∀ (M : ℕ) [NeZero M] (m : ZMod M → ℤ), (∀ k, 0 ≤ m k) →
      3 * (∑ k : ZMod M, m k) - (∑ k : ZMod M, (m k) ^ 2)
        ≤ 2 * ((Finset.univ.filter (fun k : ZMod M => m k ≠ 0)).card : ℤ) :=
  fun _ _ m hm => Zeta23.PairCeiling.GridGap.mi_holds_integer m hm

/-- **(4) the per-atom slack** — the line where integrality is consumed: `(m − 1)(m − 2) ≥ 0` for every integer `m`. -/
theorem per_atom_slack : ∀ m : ℤ, 0 ≤ (m - 1) * (m - 2) :=
  Zeta23.PairCeiling.GridGap.per_atom_slack

/-- **(4) the per-atom slack is FALSE over ℚ** (at `m = 4/3`). -/
theorem per_atom_slack_fails_rational : ¬ ∀ q : ℚ, 0 ≤ q → 0 ≤ (q - 1) * (q - 2) :=
  Zeta23.PairCeiling.GridGap.per_atom_slack_fails_rational

/-- **(4) the mark-1 floor**: `m ≤ m²` for every integer `m`. -/
theorem per_atom_floor : ∀ m : ℤ, m ≤ m ^ 2 :=
  Zeta23.PairCeiling.GridGap.per_atom_floor

/-- **(4) the mark-1 floor is FALSE over ℚ** (at `m = 1/2`). -/
theorem per_atom_floor_fails_rational : ¬ ∀ q : ℚ, 0 ≤ q → q ≤ q ^ 2 :=
  Zeta23.PairCeiling.GridGap.per_atom_floor_fails_rational
