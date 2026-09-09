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
Zeta23/DBN/Instance02/Asym_arb.lean — the LANE A (asymptotic-region, final time t₀) literal of the Arb/FLINT leg
of the Instance02 certificate for Polymath15 Table 1 row 2 (X = 5 000 000 194 858, t₀ = 93/500, y₀ = 16733/100000;
SPEC.md §5, §9; the stream plan results/d1-m2a/lane-a/PLAN.md), as an `AsymData` literal `row2AsymARB` with its
kernel fact `row2AsymARB_check : checkAsym row2AsymARB = true` (`decide +kernel`; no `native_decide`), the three real-parameter
facts `row2AsymARB_t0` / `_y0` / `_yA`, and the glue lemma `row2_laneA_arb` (PLAN.md §1.5) that turns `cert_of_checkAsym`
on the literal into exactly the statement hypothesis (ii′) of `Polymath15Bridge'` consumes in Instance02.lean.

TRANSCRIPT (results/d1-m2a/lane-a/asym-arb.json; producer Arb/FLINT (p9_arb.py, python-flint 0.6.0), prec 320, N_c 10000, m 2000 panels;
producer stamp 2026-09-09 21:36:43 IST; UNTRUSTED).  K = 10¹²; t₀ = 93/500; y₀ = 16733/100000; yA = 3962323/5000000;
3 window rows covering N ∈ [630783, 5140999] consecutively (4510217 windows); tail row at N₁ = 5141000:
  row 0: N ∈ [630783, 746495] (115713 windows), T/K ≈ 0.01202311, E/K ≈ 1.059e-07 (E/T ≈ 8.81e-06)
  row 1: N ∈ [746496, 1469440] (722945 windows), T/K ≈ 0.01202211, E/K ≈ 8.504e-08 (E/T ≈ 7.07e-06)
  row 2: N ∈ [1469441, 5140999] (3671559 windows), T/K ≈ 0.1544291, E/K ≈ 2.686e-08 (E/T ≈ 1.74e-07)
  tail: Q₁ + Q₂ + Q₃ + Q₄ + E₁ = 1996999372834 < 2K, i.e. Σ/K ≈ 1.9969993728 (margin (2K − Σ)/K ≈ 3.001e-03);
  Q₁/K ≈ 1.780739, Q₂/K ≈ 0.1786072, Q₃/K ≈ 0.01863847, Q₄/K ≈ 0.01901499, E₁/K ≈ 1.823e-09.
Every integer is the JSON's decimal string written verbatim (floors ⌊K·lower⌋ for T, ceilings ⌈K·upper⌉ for E, Q, E₁,
taken on exact rationals by the producer; nothing here is computed).  Mechanically emitted by the UNTRUSTED
results/d1-m2a/lane-a/emit_lean_lane_a.py and back-parse-verified against the JSON, integer by integer, by
backparse_lane_a.py (results/d1-m2a/lane-a/backparse.log).

WHAT THE KERNEL CHECKS HERE (integers only; SPEC.md §7.4): C-A1 (K ≥ 1, denominators ≥ 1, t₀ > 0, y₀ > 0, yA ≥ 0,
yA² ≥ 1 − 2t₀ cross-multiplied), C-A2 (a nonempty row list), C-A3 (per row Nlo ≤ Nhi and 0 ≤ E < T), C-A4
(consecutive rows), C-A5 (N₁ = last Nhi + 1), C-A6 (Q₁ … Q₄, E₁ ≥ 0 and Q₁ + Q₂ + Q₃ + Q₄ + E₁ < 2K).  Nothing
analytic is asserted here: H2-A (`AsymEnclOK`, the window-row floors ‖g(x + iy)‖ ≥ (T − E)/K for N(x) ∈ [Nlo, Nhi],
y ∈ [y₀, yA]) and H-TAIL (`TailOK`, g(x + iy) ≠ 0 for N(x) ≥ N₁, y ∈ [y₀, yA]) stay DISPLAYED (SPEC.md §6, §8.1).

WHAT THE KERNEL DOES NOT USE (PLAN-REVIEW.md F-6; SPEC §5.1).  `cert_of_checkAsym` consumes only K ≥ 1, C-A3, C-A4
and C-A5.  C-A2, C-A6 (the tail row's Σ < 2K) and C-A1's yA² ≥ 1 − 2t₀ are kernel-checked on this literal but
never consumed by any proof: they are recorded evidence for the prose discharge of Lemma T (SPEC §5.4) and of the
y-band condition.  "C-A6 is kernel-checked" must not be read as "the tail reduction is kernel-checked".

THE GLUE (PLAN.md §1.5) AND WHAT IT BUYS (PLAN-REVIEW.md §6).  `row2_laneA_arb hAsym hTail` has the conclusion
∀ x y, X + 1 ≤ x → y₀ ≤ y → y² ≤ 1 − 2t₀ → Ht t₀ (x + y·I) ≠ 0 — character for character the former `hLaneA`
binder of Instance02.lean — from `cert_of_checkAsym` on this literal, L-A1 (`row2_windowIdx_ge`: x ≥ X + 1 ⟹
N(x) ≥ 630783 = the first row's Nlo) and y ≤ yA from y² ≤ 157/250 < yA² (yA² − 157/250 = 3556329/(25·10¹²)).
Before the replacement the whole region x ≥ X + 1 was a DISPLAYED nonvanishing claim; now the window range
N ∈ [630783, 5140999] (x from ≈ 5.0·10¹² up to x_{N₁} ≈ 3.32·10¹⁴) is a displayed FLOOR ENCLOSURE (`AsymEnclOK`)
plus the kernel-checked coverage argument (C-A3, C-A4, C-A5 + L-A1 + L-A2), and the displayed nonvanishing
CONCLUSION that remains is `TailOK` only: N(x) ≥ 5 141 000, i.e. x ≳ 3.32·10¹⁴, on the y-band [y₀, yA].  One
asymmetry, stated not glossed: yA = 0.7924646 is 1.5·10⁻⁷ WIDER than the conclusion's y ≤ √(157/250) = 0.79246451…,
so `TailOK` (and `AsymEnclOK`) are hypotheses on the y-band [y₀, yA], a hair wider than the conclusion's y-range —
"the tail region N ≥ N₁, y ∈ [y₀, yA]", not "part of what `hLaneA` said".

The two producer legs are never merged (D-R3): this module is the Arb/FLINT leg's; Asym_mp.lean is the mpmath-ball leg's (K = 10²⁴), and each
leg pairs its own Lane A literal with its own Lane B literal in Instance02.lean.  The two-producer cross-check
(results/d1-m2a/lane-a/crosscheck-full.txt, CONSISTENT: T_lo and Q₁ … Q₄ agree to ≤ 5·10⁻⁷⁹ relative; the E upper
bounds are hull bounds, Arb's the larger on every row, Arb/mp = 1.027, 1.124, 1.261 on rows 0–2 and 1.000000 on E₁,
recorded not gated, etol 0.3) is producer-side evidence, not a proof.
Trust label (SPEC.md §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3" — never "fully machine-checked".
-/
import Zeta23.DBN.Asym

open Complex (I)

namespace Zeta23
namespace DBN
namespace Instance02

/-- the Arb/FLINT leg's Lane A transcript (asym-arb.json, producer stamp 2026-09-09 21:36:43 IST), integers as written:
K = 10¹², t₀ = 93/500, y₀ = 16733/100000, yA = 3962323/5000000; rows ⟨Nlo, Nhi, T, E⟩ with
T/K ≈ 0.01202311, 0.01202211, 0.1544291; tail ⟨N₁, Q₁, Q₂, Q₃, Q₄, E₁⟩ with Σ/K ≈ 1.9969993728 < 2. -/
def row2AsymARB : AsymData :=
  { K := 1000000000000,
    t0n := 93,
    t0d := 500,
    y0n := 16733,
    y0d := 100000,
    yAn := 3962323,
    yAd := 5000000,
    rows := [
      ⟨630783, 746495, 12023114801, 105892⟩,
      ⟨746496, 1469440, 12022114003, 85041⟩,
      ⟨1469441, 5140999, 154429052431, 26856⟩],
    tail := ⟨5141000, 1780738683686, 178607231320, 18638466998, 19014989007, 1823⟩ }

/-- kernel fact: C-A1 … C-A6 (SPEC.md §7.4) hold for the literal — integer relations only, `decide +kernel`. -/
theorem row2AsymARB_check : checkAsym row2AsymARB = true := by decide +kernel

/-- the transcript's t₀, y₀, yA as reals are the instance parameters (SPEC.md §9), exactly. -/
theorem row2AsymARB_t0 : At0 row2AsymARB = 93 / 500 := by simp [At0, row2AsymARB]
theorem row2AsymARB_y0 : Ay0 row2AsymARB = 16733 / 100000 := by simp [Ay0, row2AsymARB]
theorem row2AsymARB_yA : AyA row2AsymARB = 3962323 / 5000000 := by simp [AyA, row2AsymARB]

/-- **The glue (PLAN.md §1.5), Arb/FLINT leg.**  From the DISPLAYED H2-A (`hAsym`, the window-row floors) and H-TAIL
(`hTail`) for g = Ht t₀ / Bt t₀ on this literal: hypothesis (ii′) of `Polymath15Bridge'` at row 2, character for
character the former `hLaneA` — `cert_of_checkAsym` on the kernel fact `row2AsymARB_check`, applied at the first row
(Nlo = 630783 = L-A1's constant, `row2_windowIdx_ge`), with y ≤ yA from y² ≤ 157/250 < yA²; Ht ≠ 0 from Ht/Bt ≠ 0 is
`div_ne_zero_iff`.  Kernel-checked modulo `hAsym` and `hTail` (producers untrusted). -/
theorem row2_laneA_arb
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymARB)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymARB) :
    ∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →
      y ^ 2 ≤ 1 - 2 * (93 / 500) → Ht (93 / 500) (x + y * I) ≠ 0 := by
  intro x y hx hy0 hy2
  have hyA : y ≤ 3962323 / 5000000 := by
    apply le_of_sq_le_sq _ (by norm_num)
    nlinarith
  have hg := cert_of_checkAsym _ row2AsymARB row2AsymARB_check hAsym hTail x y
    ⟨630783, 746495, 12023114801, 105892⟩ (by simp [row2AsymARB])
    (by rw [row2AsymARB_t0]; exact row2_windowIdx_ge x hx)
    (by rw [row2AsymARB_y0]; exact hy0) (by rw [row2AsymARB_yA]; exact hyA)
  exact (div_ne_zero_iff.mp hg).1

end Instance02
end DBN
end Zeta23
