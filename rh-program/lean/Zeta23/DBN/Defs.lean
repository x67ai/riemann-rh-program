/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
/-
Zeta23/DBN/Defs.lean — the TRUSTED DEFINITION LAYER of the de Bruijn–Newman milestone M2a.

Binding design document: rh-program/results/d1-m0/m2a-m2b-design.md (the D-R2 repair note,
2026-08-26), §1.2–1.3 and §5.  This file realizes that note's Lean skeleton verbatim up to
current-Mathlib API; any forced deviation carries a dated comment here and a dated addendum
in the design note.

CONTENTS — by design exactly four definitions and NOTHING else (trusted-thin on purpose):
  * `Phi`               — the heat-kernel density Φ(u) (Polymath15 eq. (2));
  * `Ht`                — H_t(z) = ∫₀^∞ e^{tu²} Φ(u) cos(zu) du (Bochner integral on (0,∞));
  * `ZeroVerification`  — the (H1) hypothesis shape: zero-freeness of `riemannZeta` in a
                          box [σ₀,1] × [0,T₀];
  * `Polymath15Bridge`  — the (H3) hypothesis: Polymath15 Theorem 1.2 (upper bound
                          criterion), quantified over its parameters, in the merged
                          barrier + asymptotic "canopy" form.
The checker vocabulary for (H2) (`BarrierCertData`, `BarrierEnclOK`), the instance data, and
the target theorem live in later files (BarrierCert.lean, Instance02.lean, after the M1 v1
checker); the comparator mirror of this layer follows the ChallengeDeps pattern at packaging
time.  Nothing in this file is proved: it is statement vocabulary, part of the audit surface.

TRUST MODEL (fixed by the design note; the honest label, verbatim, for any publication):
the M2a target theorem is "kernel-checked modulo three displayed hypotheses: (H1) a
producer-certified zero verification, (H2) producer-certified H_t enclosures, (H3) the
Polymath15 upper-bound criterion (Theorem 1.2) as an analytic hypothesis — with two
independent producers for (H2)."  This extends the PairCeiling trust model (sole displayed
hypothesis `EnclOK`) from one displayed computation to two displayed computations plus one
displayed ANALYTIC implication.

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
anywhere (this file happens to contain no numeric parameters at all — they enter with the
instance data).
-/
-- Import note, 2026-08-26: the design note's import list says
-- `Mathlib.MeasureTheory.Integral.Bochner`; in current Mathlib that module is a directory
-- and the Bochner integral lives in `Mathlib.MeasureTheory.Integral.Bochner.Basic`.
-- Same content, path fixed; dated addendum appended to the design note.
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.NumberTheory.LSeries.RiemannZeta

noncomputable section

open scoped Real
open Real (exp)
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

/-- (H3) THE DISPLAYED ANALYTIC HYPOTHESIS: Polymath15 Theorem 1.2 (upper bound criterion),
quantified over the parameters (t₀, X, y₀).  Hypotheses, in order: parameter ranges; (i) the
zero verification at initial time (via `ZeroVerification`); (ii)+(iii) merged into one
"canopy" nonvanishing statement — no zeros of H_t with x ≥ X, y₀ ≤ y ≤ 1, 0 ≤ t ≤ t₀
(the design's merged form of the paper's barrier region at X and asymptotic region beyond
it, so that no unstated analytic step exists outside a displayed hypothesis).  Conclusion:
every H_t with t ≥ t₀ + y₀²/2 has only real zeros.  This Prop is stated, named, and NOT
proved in M2a; discharging it is M2b (explicitly not scheduled). -/
def Polymath15Bridge : Prop :=
  ∀ t₀ X y₀ : ℝ, 0 < t₀ → 0 < X → 0 < y₀ → y₀ ≤ 1 →
    ZeroVerification ((1 + y₀) / 2) (X / 2) →
    (∀ x y : ℝ, X ≤ x → y₀ ≤ y → y ≤ 1 → ∀ t : ℝ, 0 ≤ t → t ≤ t₀ →
        Ht t (x + y * Complex.I) ≠ 0) →
    ∀ t : ℝ, t₀ + y₀ ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0

end DBN
end Zeta23
