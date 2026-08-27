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
Zeta23/W1/Examples.lean — the FORMAT.md §11 worked micro-examples as kernel-checked checker
instances: the refutation example (w1-example-refutation.json) and its exclusion twin
(w1-example-exclusion.json), transcribed literally from rh-program/results/d1-m1/, and the
theorems `exampleRefutation_accepted` / `exampleExclusion_accepted` proved by `decide +kernel`
(kernel evaluation; NO `native_decide` — the NumericCert discipline).

HONESTY LABEL (FORMAT.md §11, binding): the numbers are ARTIFICIAL — invented to exercise every
check with small integers.  No producer certified H-ENCL for them; "the checker accepts" means
exactly and only that C1–C11 pass.  These theorems assert NOTHING about ζ: they are the
cross-validation that the Lean checker and the untrusted reference implementation
(reference_checker.py, run transcript reference-checker-run.txt) accept the same transcripts —
the checker-level acceptance tests of the architecture, not mathematical claims.

Cross-validated integer facts (FORMAT.md §11, digit for digit): refutation example
S_lo = 925, S_hi = 1083, width check 2·158 = 316 < 1000 = A, A·m = 1000 ∈ [925, 1083];
exclusion twin S_lo = −92, S_hi = 148, 2·240 = 480 < 1000, A·0 = 0 ∈ [−92, 148].
-/
import Zeta23.W1.Checker

namespace Zeta23
namespace W1

/-- FORMAT.md §11 / w1-example-refutation.json: mode refutation (m = 1), K = 100, A = 1000,
R = [3/5, 7/10] × [10, 11], two segments per edge (M = 8).  ARTIFICIAL data. -/
def exampleRefutation : W1Data where
  p1 := 3;  q1 := 5
  p2 := 7;  q2 := 10
  a1 := 10; b1 := 1
  a2 := 11; b2 := 1
  K := 100
  A := 1000
  m := 1
  bottom := [(3, 5), (13, 20), (7, 10)]
  right  := [(10, 1), (21, 2), (11, 1)]
  top    := [(7, 10), (13, 20), (3, 5)]
  left   := [(11, 1), (21, 2), (10, 1)]
  rows := [
    ⟨50, 90, -25, 25, 110, 140⟩,
    ⟨20, 70, 20, 70, 120, 130⟩,
    ⟨-25, 25, 50, 90, 115, 135⟩,
    ⟨-70, -20, 20, 70, 120, 140⟩,
    ⟨-90, -50, -25, 25, 105, 130⟩,
    ⟨-70, -20, -70, -20, 125, 145⟩,
    ⟨-25, 25, -90, -50, 110, 125⟩,
    ⟨20, 70, -70, -20, 120, 138⟩]

/-- the §11 example's optional modulus floor Fn/Fd = 1/4. -/
def exampleFloor : W1Floor where
  Fn := 1
  Fd := 4

/-- w1-example-exclusion.json: the m = 0 twin (same rectangle and mesh; all boxes in the right
half-plane, argument rows straddling 0).  ARTIFICIAL data. -/
def exampleExclusion : W1Data where
  p1 := 3;  q1 := 5
  p2 := 7;  q2 := 10
  a1 := 10; b1 := 1
  a2 := 11; b2 := 1
  K := 100
  A := 1000
  m := 0
  bottom := [(3, 5), (13, 20), (7, 10)]
  right  := [(10, 1), (21, 2), (11, 1)]
  top    := [(7, 10), (13, 20), (3, 5)]
  left   := [(11, 1), (21, 2), (10, 1)]
  rows := [
    ⟨60, 95, -30, 30, -15, 20⟩,
    ⟨55, 90, -25, 35, -10, 18⟩,
    ⟨62, 98, -28, 22, -12, 15⟩,
    ⟨58, 92, -35, 25, -8, 22⟩,
    ⟨61, 99, -20, 30, -14, 16⟩,
    ⟨57, 94, -30, 28, -9, 19⟩,
    ⟨63, 97, -26, 33, -11, 17⟩,
    ⟨59, 93, -31, 24, -13, 21⟩]

/-- the §11 refutation example is ACCEPTED (C1–C10), kernel-checked.  Asserts nothing about ζ
(H-ENCL was never certified for this artificial data). -/
theorem exampleRefutation_accepted : checkW1 exampleRefutation = true := by decide +kernel

/-- the §11 example with its modulus floor 1/4 is ACCEPTED (C1–C11), kernel-checked. -/
theorem exampleRefutation_floor_accepted :
    checkW1Floor exampleRefutation exampleFloor = true := by decide +kernel

/-- the exclusion twin is ACCEPTED (C1–C10, m = 0), kernel-checked. -/
theorem exampleExclusion_accepted : checkW1 exampleExclusion = true := by decide +kernel

/-! Negative controls (FORMAT.md §11): mutations of the example must be REJECTED.  Two are
kernel-checked here as checker-hardness witnesses (the full six-control suite lives in the
untrusted reference run, reference-checker-run.txt). -/

/-- negative control: a box containing 0 (row 0's value box widened to straddle 0) fails C6. -/
theorem exampleRefutation_C6_control :
    checkW1 { exampleRefutation with
      rows := ⟨-50, 90, -25, 25, 110, 140⟩ :: exampleRefutation.rows.tail } = false := by
  decide +kernel

/-- negative control: claimed m = 2 fails C9 (A·2 = 2000 ∉ [925, 1083]). -/
theorem exampleRefutation_C9_control :
    checkW1 { exampleRefutation with m := 2 } = false := by decide +kernel

end W1
end Zeta23
