/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
/-
Zeta23/W1/Checker.lean — the W1 INTEGER CHECKER: `checkW1 : W1Data → Bool` implementing the
normative check list C1–C10 of rh-program/results/d1-m1/FORMAT.md §7 (and C11 for the optional
modulus floor, `checkW1Floor`), in PURE INTEGER ARITHMETIC — only +, ·, |·|, min on ℤ and ℕ
comparisons on list lengths; every rational comparison by cross-multiplication (FORMAT.md D7);
no floats, no division, no transcendental constants anywhere.

The checker mirrors `RowCert.checkRows` (Zeta23/PairCeiling/RowCert.lean): a Bool-valued pure
function on literal data, evaluated by `decide +kernel` in instance files (NumericCert
discipline — NO `native_decide`), plus a soundness theorem (Soundness.lean) turning
`checkW1 d = true` and the two displayed hypotheses H-ENCL and H-AP into the analytic
conclusion.  The checker is a conjunction: order is fixed only for failure reporting, and
short-circuiting does not affect the accepted set.

CHECK LIST (FORMAT.md §7, normative; the comment on each clause names the check):
  C1  scales and denominators: K ≥ 1, A ≥ 1; every rational's d ≥ 1.
  C2  rectangle: q₁ < 2p₁; p₁q₂ ≤ p₂q₁; p₂ < q₂; a₁b₂ < a₂b₁  (½ < σ₁ ≤ σ₂ < 1, T₁ < T₂).
  C3  mesh walk: each edge has ≥ 2 breakpoints, endpoint equalities to the rectangle
      parameters, and strict monotonicity in the traversal direction (bottom/right increasing,
      top/left decreasing), all cross-multiplied.
  C4  row count: |rows| = (|bottom|−1) + (|right|−1) + (|top|−1) + (|left|−1).
  C5  box validity: reLo ≤ reHi ∧ imLo ≤ imHi, every row.
  C6  nonvanishing/admissibility: reLo > 0 ∨ reHi < 0 ∨ imLo > 0 ∨ imHi < 0, every row.
  C7  argument rows: argLo ≤ argHi ∧ −A ≤ 2·argLo ∧ 2·argHi ≤ A, every row.
  C8  sum width: 2·(S_hi − S_lo) < A,  S_lo = Σ argLo, S_hi = Σ argHi.
  C9  containment: S_lo ≤ A·m ≤ S_hi.
  C10 (Lean remnant) 0 ≤ m: the JSON mode field is implicit here (FORMAT.md §12.5); the
      refutation/exclusion split is `1 ≤ m` vs `m = 0` at the theorem level.
  C11 (floor variant only): (mre² + mim²)·Fd² ≥ Fn²·K², every row, with mre/mim the §5.2
      coordinate distances of the box from 0.

Trust model: definitions only, no proofs; kernel-decidable on literal data.  A transcript can
be schema-valid and checker-rejected; acceptance means C1–C10 (C11) and NOTHING analytic —
the analytic content enters only through the displayed hypotheses (Soundness.lean).
-/
import Mathlib.Algebra.Order.Ring.Int
import Zeta23.W1.Format

namespace Zeta23
namespace W1

/-! ## Rational comparisons by cross-multiplication (FORMAT.md D7)

A mesh entry `(n, d)` means n/d with d ≥ 1 checked by C1 (`densPos`); under d₁, d₂ ≥ 1,
n₁/d₁ < n₂/d₂ ⟺ n₁·d₂ < n₂·d₁ and likewise for =, ≤.  No division anywhere. -/

/-- rational equality by cross-multiplication: r = s as fractions. -/
def ratEqB (r s : ℤ × ℤ) : Bool := decide (r.1 * s.2 = s.1 * r.2)

/-- every denominator in the list is ≥ 1 (the C1 clause for a mesh edge). -/
def densPos : List (ℤ × ℤ) → Bool
  | [] => true
  | r :: l => decide (1 ≤ r.2) && densPos l

/-- adjacent strict INcrease along a list of rationals (cross-multiplied). -/
def chainLt : List (ℤ × ℤ) → Bool
  | [] => true
  | [_] => true
  | r :: s :: l => decide (r.1 * s.2 < s.1 * r.2) && chainLt (s :: l)

/-- adjacent strict DEcrease along a list of rationals (cross-multiplied). -/
def chainGt : List (ℤ × ℤ) → Bool
  | [] => true
  | [_] => true
  | r :: s :: l => decide (s.1 * r.2 < r.1 * s.2) && chainGt (s :: l)

/-- the first breakpoint equals the target rational (false on an empty edge). -/
def firstOK (t : ℤ × ℤ) : List (ℤ × ℤ) → Bool
  | [] => false
  | r :: _ => ratEqB r t

/-- the last breakpoint equals the target rational (false on an empty edge). -/
def lastOK (t : ℤ × ℤ) : List (ℤ × ℤ) → Bool
  | [] => false
  | [r] => ratEqB r t
  | _ :: s :: l => lastOK t (s :: l)

/-- the full C3 clause for one edge: ≥ 2 breakpoints, endpoints pinned to the rectangle
parameters, strict monotonicity in the traversal direction (`inc = true` for increasing). -/
def edgeOK (start stop : ℤ × ℤ) (inc : Bool) (l : List (ℤ × ℤ)) : Bool :=
  decide (2 ≤ l.length) && firstOK start l && lastOK stop l
    && (if inc then chainLt l else chainGt l)

/-! ## Row checks (C5, C6, C7) and the argument sums (C8, C9) -/

/-- the per-row conjunction C5 ∧ C6 ∧ C7. -/
def rowOK (A : ℤ) (r : W1Row) : Bool :=
  -- C5 (box validity; producer-bug tripwire)
  decide (r.reLo ≤ r.reHi) && decide (r.imLo ≤ r.imHi)
    -- C6 (nonvanishing / mesh admissibility: the box excludes 0 — FORMAT.md D1)
    && (decide (0 < r.reLo) || decide (r.reHi < 0) || decide (0 < r.imLo) || decide (r.imHi < 0))
    -- C7 (argument-row validity + the D3 half-turn clamp; tripwire)
    && decide (r.argLo ≤ r.argHi) && decide (-A ≤ 2 * r.argLo) && decide (2 * r.argHi ≤ A)

/-- C5–C7 over all rows. -/
def rowsOK (A : ℤ) : List W1Row → Bool
  | [] => true
  | r :: l => rowOK A r && rowsOK A l

/-- S_lo := Σ argLo (FORMAT.md C8). -/
def sumArgLo : List W1Row → ℤ
  | [] => 0
  | r :: l => r.argLo + sumArgLo l

/-- S_hi := Σ argHi. -/
def sumArgHi : List W1Row → ℤ
  | [] => 0
  | r :: l => r.argHi + sumArgHi l

/-! ## The checker -/

/-- **the W1 checker** (FORMAT.md §7, checks C1–C10): pure integer arithmetic, kernel-decidable
on literal data.  Acceptance means exactly that the listed integer comparisons hold. -/
def checkW1 (d : W1Data) : Bool :=
  -- C1: scales ≥ 1; every denominator ≥ 1 (rectangle parameters and all four mesh edges)
  decide (1 ≤ d.K) && decide (1 ≤ d.A)
    && decide (1 ≤ d.q1) && decide (1 ≤ d.q2) && decide (1 ≤ d.b1) && decide (1 ≤ d.b2)
    && densPos d.bottom && densPos d.right && densPos d.top && densPos d.left
    -- C2: ½ < σ₁;  σ₁ ≤ σ₂;  σ₂ < 1;  T₁ < T₂
    && decide (d.q1 < 2 * d.p1) && decide (d.p1 * d.q2 ≤ d.p2 * d.q1)
    && decide (d.p2 < d.q2) && decide (d.a1 * d.b2 < d.a2 * d.b1)
    -- C3: the four edge walks (bottom/right increasing; top/left DEcreasing)
    && edgeOK (d.p1, d.q1) (d.p2, d.q2) true d.bottom
    && edgeOK (d.a1, d.b1) (d.a2, d.b2) true d.right
    && edgeOK (d.p2, d.q2) (d.p1, d.q1) false d.top
    && edgeOK (d.a2, d.b2) (d.a1, d.b1) false d.left
    -- C4: |rows| = M = Σ_edges (breakpoints − 1)  (written +4 to avoid ℕ-subtraction)
    && decide (d.rows.length + 4
        = d.bottom.length + d.right.length + d.top.length + d.left.length)
    -- C5, C6, C7: per-row checks
    && rowsOK d.A d.rows
    -- C8: winding-enclosure width < ½ turn
    && decide (2 * (sumArgHi d.rows - sumArgLo d.rows) < d.A)
    -- C9: S_lo ≤ A·m ≤ S_hi
    && decide (sumArgLo d.rows ≤ d.A * d.m) && decide (d.A * d.m ≤ sumArgHi d.rows)
    -- C10 (Lean remnant): m ≥ 0
    && decide (0 ≤ d.m)

/-! ## The optional modulus floor (C11, FORMAT.md §5.2) -/

/-- the coordinate distance-from-0 of the interval [lo, hi]: 0 if the interval contains 0,
else min(|lo|, |hi|)  (FORMAT.md §5.2's mre/mim). -/
def mdist (lo hi : ℤ) : ℤ := if lo ≤ 0 ∧ 0 ≤ hi then 0 else min |lo| |hi|

/-- the C11 clause for one row: (mre² + mim²)·Fd² ≥ Fn²·K². -/
def floorRowOK (K Fn Fd : ℤ) (r : W1Row) : Bool :=
  decide (Fn ^ 2 * K ^ 2 ≤ (mdist r.reLo r.reHi ^ 2 + mdist r.imLo r.imHi ^ 2) * Fd ^ 2)

/-- C11 over all rows. -/
def floorRowsOK (K Fn Fd : ℤ) : List W1Row → Bool
  | [] => true
  | r :: l => floorRowOK K Fn Fd r && floorRowsOK K Fn Fd l

/-- **the floor-variant checker**: `checkW1` plus C11 (with Fn ≥ 0, Fd ≥ 1).  Certifies the
by-product |f| ≥ Fn/Fd on ∂R under H-ENCL(a); never load-bearing for the W1 conclusion. -/
def checkW1Floor (d : W1Data) (fl : W1Floor) : Bool :=
  checkW1 d && decide (0 ≤ fl.Fn) && decide (1 ≤ fl.Fd) && floorRowsOK d.K fl.Fn fl.Fd d.rows

end W1
end Zeta23
