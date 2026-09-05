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
Zeta23/DBN/Defs.lean — the TRUSTED DEFINITION LAYER of the de Bruijn–Newman milestone M2a.
VERSION 1.1 (2026-09-06).  v1.0 was 2026-08-26 (design note §7).

Binding design document: rh-program/results/d1-m0/m2a-m2b-design.md (the D-R2 repair note,
2026-08-26), §1.2–1.3 and §5, AS AMENDED by the M2a contract
rh-program/results/d1-m2a/SPEC.md §3 (2026-09-02; the defect D-3.2 and the amended bridge).
Any forced deviation carries a dated comment here and a dated addendum in the design note.

CONTENTS — by design exactly nine definitions and NOTHING else (trusted-thin on purpose):
  * `Phi`                — the heat-kernel density Φ(u) (Polymath15 eq. (2));
  * `Ht`                 — H_t(z) = ∫₀^∞ e^{tu²} Φ(u) cos(zu) du (Bochner integral on (0,∞));
  * `ZeroVerification`   — the (H1) hypothesis shape: zero-freeness of `riemannZeta` in a
                           box [σ₀,1] × [0,T₀];
  * `alpha`, `M0`, `Mt`, `Bt` — the explicit nowhere-vanishing normalizer B_t(z) = M_t((1 − iz)/2)
                           of Polymath15 eqs. (9), (6), (10), (11) (p4); the barrier transcripts
                           enclose the NORMALIZED function g_t = H_t/B_t (SPEC §3.4);
  * `HtEntire`           — the entirety of every H_t (SPEC §3.5), the second component of H3;
  * `Polymath15Bridge'`  — the (H3) hypothesis: Polymath15 Theorem 1.2 (upper bound criterion),
                           quantified over its parameters, with hypothesis (ii) at the FINAL time
                           only and the paper's simplified barrier box for (iii) (SPEC §3.3).
The checker vocabulary for (H2) (`BarrierData`, `BarrierEnclOK`), the instance data, and the
target theorem live in later files (BarrierCert.lean, Instance02.lean, after the M1 v1 checker);
the comparator mirror of this layer follows the ChallengeDeps pattern at packaging time.
Nothing in this file is proved: it is statement vocabulary, part of the audit surface.

DEVIATION RECORD, 2026-09-06 (Session 16) — v1.0 → v1.1 (format: design note §7):
  1. `Polymath15Bridge` (v1.0, the merged "canopy" form: no zeros of H_t for ALL x ≥ X,
     y₀ ≤ y ≤ 1 and ALL t ∈ [0, t₀]) is REMOVED and NOT kept under the old name.  Reason
     (SPEC §3.2, derivation D-3.2): at t = 0, H₀(x + iy) = ⅛·ξ((1 − y)/2 + ix/2), so the
     canopy's t = 0 slice asserts that ζ has no zeros with (1 + y₀)/2 ≤ Re s ≤ 1 at ANY height
     ≥ X/2 — the Riemann hypothesis in a half-strip above the verified height, unproved and not
     the object of any finite computation.  The Prop is true as a mathematical statement (its
     hypotheses are stronger than Theorem 1.2's), which is why it elaborated in v1.0; but no
     transcript plus H1 can discharge it, so the instance theorem was unprovable.
  2. `Polymath15Bridge'` REPLACES it, exactly as SPEC §3.3 prints it.  Justification D-H3
     (SPEC §3.3): it is implied by Theorem 1.2 together with the paper's own remark (p3) that
     the barrier region may be replaced by the larger box X ≤ x ≤ X + 1, y₀ ≤ y ≤ 1,
     0 ≤ t ≤ t₀; (ii′) restricts (ii) to x ≥ X + 1 (the strip X + √(1 − y₀²) ≤ x ≤ X + 1 is
     covered by (iii′) at t = t₀), and (ii′)'s y-range is written as y² ≤ 1 − 2t₀ to avoid a
     square root in the trusted layer.
  3. `alpha`, `M0`, `Mt`, `Bt` and `HtEntire` ADDED (SPEC §3.4–3.5), with the shapes type-checked
     in results/d1-m2a/lean-shapes-scratch.lean §A (2026-09-02).  `Bt` is stated concretely
     (not existentially) so that a reader of this layer sees which function the rows are about.
     Transcription notes: Mathlib's `Complex.log` is the principal branch (P15's "Log");
     `(π : ℂ) ^ (-s / 2)` is `Complex.cpow` with the positive real base π (P15's π^{−s/2});
     (1 − iz)/2 = (1 + y − ix)/2 for z = x + iy.
  4. Imports: `Mathlib.Analysis.SpecialFunctions.Complex.Log` and
     `Mathlib.Analysis.SpecialFunctions.Pow.Complex` added for `Complex.log` and `cpow`;
     `open Complex (I)` added so the source reads as SPEC §3.3–3.4 print it (elaborated terms
     unchanged: `I` is `Complex.I`).

TRUST MODEL (SPEC §3.7, the honest label, verbatim, for any publication): the M2a target
theorem is "kernel-checked modulo the displayed hypotheses: (H1) a producer-certified zero
verification — `ZeroVerification (116733/200000) 2500000097429`, discharged by Platt–Trudgian
Theorem 1; (H2) producer-certified enclosures — the barrier prisms (H2-B), the final-time window
rows (H2-A) and the tail (H-TAIL), from two independent producers; (H3) the Polymath15 analytic
package — Theorem 1.2 in the form `Polymath15Bridge'` and the entirety of H_t — as hypotheses."
Never "fully machine-checked".  This extends the PairCeiling trust model (sole displayed
hypothesis `EnclOK`) from one displayed computation to displayed computations plus one displayed
ANALYTIC package.

RAY FORM (design §1.2).  The target conclusion is stated as
    ∀ t, 1/5 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0,
the ray form of the de Bruijn–Newman bound Λ ≤ 0.2.  The constant Λ itself
(sInf {t | H_t has only real zeros}) is deliberately NOT defined: a Lean `sInf` on a set not
known nonempty/bounded-below has junk-value pitfalls, and making the definition meaningful
would drag de Bruijn monotonicity and Hurwitz closure into the trusted layer.  The ray
statement is equivalent given the ray structure {t | H_t real-zeroed} = [Λ, ∞), and the
word Λ never appears in any formal statement — prose and comments only.

ANTI-CHEAT NOTE (design §1.2, recorded here as required): `Ht` is defined by a Bochner
integral; if the integrand were NOT integrable the definition would collapse to the junk
value 0 everywhere, making EVERY z a zero and the target conclusion FALSE, not vacuous.
The statement cannot be satisfied by a degenerate definition — integrability is forced onto
the solution side, where it belongs.

Numeric-literal discipline: exact rationals only in this layer; no floating-point literals
anywhere (this file contains no numeric parameters at all beyond the constants of P15's
formulas — they enter with the instance data).
-/
-- Import note, 2026-08-26: the design note's import list says
-- `Mathlib.MeasureTheory.Integral.Bochner`; in current Mathlib that module is a directory
-- and the Bochner integral lives in `Mathlib.MeasureTheory.Integral.Bochner.Basic`.
-- Same content, path fixed; dated addendum appended to the design note.
-- Import note, 2026-09-06 (v1.1): `Complex.Log` and `Pow.Complex` added for `alpha`/`M0`.
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Complex
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.NumberTheory.LSeries.RiemannZeta

noncomputable section

open scoped Real
open Real (exp)
open Complex (I)
open MeasureTheory

namespace Zeta23
namespace DBN

/-- Φ(u) = Σ_{n≥1} (2π²n⁴e^{9u} − 3πn²e^{5u})·exp(−πn²e^{4u})  (the heat-kernel density;
Polymath15 eq. (2), with the normalization H₀(z) = ⅛·ξ(½ + iz/2)).  A `tsum` over `ℕ+`:
the sum converges (super-exponentially) for every real u, but no convergence fact is part
of this definition — integrability/summability facts belong to the solution side. -/
def Phi (u : ℝ) : ℝ :=
  ∑' n : ℕ+, (2 * π ^ 2 * (n : ℝ) ^ 4 * exp (9 * u) - 3 * π * (n : ℝ) ^ 2 * exp (5 * u))
    * exp (-π * (n : ℝ) ^ 2 * exp (4 * u))

/-- H_t(z) = ∫₀^∞ e^{tu²} Φ(u) cos(zu) du  (Bochner integral over (0,∞) with Lebesgue
measure; junk value 0 if the integrand is not integrable — see the anti-cheat note in the
file header: junk makes the target statement false, not vacuous). -/
def Ht (t : ℝ) (z : ℂ) : ℂ :=
  ∫ u in Set.Ioi (0 : ℝ), Complex.exp (t * u ^ 2) * (Phi u : ℂ) * Complex.cos (z * u)

/-- (H1) Producer-certified zero verification to ζ-height T₀, in the exact shape Polymath15
Theorem 1.2(i) consumes: no zeros of ζ with real part in [σ₀, 1] and imaginary part in
[0, T₀].  Displayed hypothesis; discharged in prose by Platt–Trudgian Theorem 1
(σ₀ = (1+y₀)/2, T₀ = X/2 ≤ 3·10¹²).  Stated in the weak box form so that any future partial
verification weaker than full RH-to-height could also discharge it; monotone in σ₀ (larger
σ₀ is weaker), so instances may round σ₀ DOWN safely. -/
def ZeroVerification (σ₀ T₀ : ℝ) : Prop :=
  ∀ s : ℂ, riemannZeta s = 0 → σ₀ ≤ s.re → s.re ≤ 1 → 0 ≤ s.im → s.im ≤ T₀ → False

/-- α(s) = 1/(2s) + 1/(s−1) + ½·Log(s/(2π))   (Polymath15 eq. (9), second line, p4). -/
def alpha (s : ℂ) : ℂ := 1 / (2 * s) + 1 / (s - 1) + (1 / 2 : ℂ) * Complex.log (s / (2 * π))

/-- M₀(s) = ⅛ · s(s−1)/2 · π^{−s/2} · √(2π) · exp((s/2 − ½)·Log(s/2) − s/2)   (eq. (6), p4). -/
def M0 (s : ℂ) : ℂ :=
  (1 / 8 : ℂ) * (s * (s - 1) / 2) * (π : ℂ) ^ (-s / 2) * (Real.sqrt (2 * π) : ℂ)
    * Complex.exp ((s / 2 - 1 / 2) * Complex.log (s / 2) - s / 2)

/-- M_t(s) = exp(t/4 · α(s)²) · M₀(s)   (eq. (10), p4). -/
def Mt (t : ℝ) (s : ℂ) : ℂ := Complex.exp ((t : ℂ) / 4 * alpha s ^ 2) * M0 s

/-- B_t(z) = M_t((1 + y − ix)/2) for z = x + iy, i.e. M_t((1 − iz)/2)   (eq. (11), p4).
The explicit normalizer: the barrier transcripts enclose g_t = H_t/B_t (SPEC §3.4).  Its
holomorphy and nonvanishing off the imaginary axis are PROVED (BtFacts.lean, L-B3), not
displayed. -/
def Bt (t : ℝ) (z : ℂ) : ℂ := Mt t ((1 - I * z) / 2)

/-- the entirety of every H_t (analytic-package component of H3; SPEC §3.5).  `Ht` is a
Bochner integral whose holomorphy (differentiation under the integral against the
super-exponentially decaying Φ) is M2b-class analysis; it is therefore DISPLAYED. -/
def HtEntire : Prop := ∀ t : ℝ, Differentiable ℂ (Ht t)

/-- (H3) THE DISPLAYED ANALYTIC HYPOTHESIS: Polymath15 Theorem 1.2 (upper bound criterion),
quantified over the parameters (t₀, X, y₀), with hypothesis (ii) at the FINAL time only and
the paper's simplified barrier box for (iii) — the instantiable form (SPEC §3.3; replaces the
v1.0 merged canopy, which is not dischargeable by any finite certificate, SPEC §3.2).
Hypotheses, in order: parameter ranges; (i) the zero verification at initial time (via
`ZeroVerification`); (ii′) no zeros of H_{t₀}(x + iy) with x ≥ X + 1, y ≥ y₀, y² ≤ 1 − 2t₀;
(iii′) no zeros of H_t(x + iy) with X ≤ x ≤ X + 1, y₀ ≤ y ≤ 1, 0 ≤ t ≤ t₀.  Conclusion:
every H_t with t ≥ t₀ + y₀²/2 has only real zeros.  Derivation D-H3 (SPEC §3.3): implied by
Theorem 1.2 with the p3 simplified barrier region.  This Prop is stated, named, and NOT
proved in M2a; discharging it is M2b (explicitly not scheduled). -/
def Polymath15Bridge' : Prop :=
  ∀ t₀ X y₀ : ℝ, 0 < t₀ → 0 < X → 0 < y₀ → y₀ ≤ 1 →
    ZeroVerification ((1 + y₀) / 2) (X / 2) →
    (∀ x y : ℝ, X + 1 ≤ x → y₀ ≤ y → y ^ 2 ≤ 1 - 2 * t₀ →
        Ht t₀ (x + y * I) ≠ 0) →
    (∀ x y : ℝ, X ≤ x → x ≤ X + 1 → y₀ ≤ y → y ≤ 1 → ∀ t : ℝ, 0 ≤ t → t ≤ t₀ →
        Ht t (x + y * I) ≠ 0) →
    ∀ t : ℝ, t₀ + y₀ ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0

end DBN
end Zeta23
