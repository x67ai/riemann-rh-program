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
comparator/ChallengeDeps/DBN.lean — the TRUSTED definition layer for the comparator topic `DBN`
(the de Bruijn–Newman milestone M2a; see comparator/README.md, "Layout convention: one topic per file", and
rh-program/results/d1-m2a/packaging/BUILD-NOTES.md).

Everything the challenge statements in Challenge/DBN.lean mention is defined HERE, from Mathlib alone:
  §1 the nine definitions of Zeta23/DBN/Defs.lean v1.1 (`Phi`, `Ht`, `ZeroVerification`, `alpha`, `M0`, `Mt`, `Bt`,
     `HtEntire`, `Polymath15Bridge'`);
  §2 the W1 transcript vocabulary the barrier lane reuses (Zeta23/W1/{Format,Checker,Soundness}.lean: `W1Row`,
     `W1Data`, the integer checker helpers, the real/complex reading of a transcript, `segs`, `RowEnclOK`);
  §3 the barrier lane (Zeta23/DBN/BarrierCert.lean §1–§3: `PrismData`, `RectData`, `BarrierData`, `checkPrismW1`,
     `checkPrism`, `checkBarrierChain`, `checkBarrier`, the rational accessors, `PrismEnclOK`, `BarrierEnclOK`);
  §4 the asymptotic lane (Zeta23/DBN/Asym.lean: `windowIdx`, `AsymRow`, `TailRow`, `AsymData`, `checkAsymRow`,
     `consecutive`, `lastNhi`, `checkAsym`, `At0`, `Ay0`, `AyA`, `AsymEnclOK`, `TailOK`).
This module imports NOTHING from Zeta23/.  Every `def`/`structure` block below is CHARACTER FOR CHARACTER the block of
the named Zeta23 source (docstrings included; extracted mechanically by
rh-program/results/d1-m2a/packaging/gen_challengedeps_dbn.py, source lines recorded in BUILD-NOTES.md §1), re-wrapped
under the root-style namespace `DBN` (the W1 vocabulary under `DBN.W1`, so that the copied text `W1.densPos`,
`W1.RowEnclOK`, … resolves unchanged).  Zeta23's live in `Zeta23.DBN` / `Zeta23.W1`, so that Solution/DBN.lean can
import both without name clashes.  The copied structures are DISTINCT TYPES from Zeta23's (a re-declared structure is
never definitionally equal to the original); the solution side bridges them by transport lemmas, never by import.

A reader auditing WHAT is claimed needs to read only this file, ChallengeDeps/DBN/Instance02.lean (the instance
literals) and Challenge/DBN.lean, trusting Mathlib and the Lean kernel.  Nothing here is proved: this is statement
vocabulary, the audit surface.

TRUST MODEL (SPEC §3.7, verbatim, for any publication): the M2a target theorem is "kernel-checked modulo the displayed
hypotheses: (H1) a producer-certified zero verification — `ZeroVerification (116733/200000) 2500000097429`, discharged
by Platt–Trudgian Theorem 1; (H2) producer-certified enclosures — the barrier prisms (H2-B), the final-time window rows
(H2-A) and the tail (H-TAIL), from two independent producers; (H3) the Polymath15 analytic package — Theorem 1.2 in the
form `Polymath15Bridge'` and the entirety of H_t — as hypotheses."  Short label: "kernel-checked modulo H1, H2 (H2-B,
H2-A, H-TAIL), H3" — never "fully machine-checked".  Λ ≤ 0.2 is NOT proved: the bracket of record stays 0 ≤ Λ ≤ 0.2 on
the literature.  The word Λ never appears in a formal statement (design note §1.2; the conclusion is the ray form
∀ t ≥ 1/5, every zero of H_t is real).  ANTI-CHEAT NOTE (Defs.lean): `Ht` is a Bochner integral; if the integrand were
not integrable the definition would collapse to 0, making EVERY z a zero and the target conclusion FALSE, not vacuous.
-/
import Mathlib

open scoped Real
open Real (exp)
open Complex (I)
open MeasureTheory

noncomputable section

namespace DBN

/-! ## 1. The trusted definition layer — Zeta23/DBN/Defs.lean v1.1 (nine definitions, nothing else) -/

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

/-! ## 2. The W1 vocabulary reused by the barrier lane (namespace `DBN.W1`) -/

namespace W1

/-! ### 2a. W1 transcript data — Zeta23/W1/Format.lean -/

/-- Per-segment transcript row (FORMAT.md §2, §7.1): the value box at scale K
(`reLo ≤ K·Re f ≤ reHi`, `imLo ≤ K·Im f ≤ imHi`, for ALL points of the closed segment) and the
argument-increment enclosure at scale A in turn units (`argLo ≤ A·(Δ/2π) ≤ argHi`). -/
structure W1Row where
  reLo : ℤ
  reHi : ℤ
  imLo : ℤ
  imHi : ℤ
  argLo : ℤ
  argHi : ℤ

/-- The W1 rectangle transcript (FORMAT.md §7.1).  All numbers are flat ℤ literals; every
constraint on them (C1–C10) is the checker's, and every analytic assertion about them is a
displayed hypothesis. -/
structure W1Data where
  /-- σ₁ = p1/q1 (left abscissa). -/
  p1 : ℤ
  q1 : ℤ
  /-- σ₂ = p2/q2 (right abscissa). -/
  p2 : ℤ
  q2 : ℤ
  /-- T₁ = a1/b1 (bottom ordinate). -/
  a1 : ℤ
  b1 : ℤ
  /-- T₂ = a2/b2 (top ordinate). -/
  a2 : ℤ
  b2 : ℤ
  /-- value scale K ≥ 1. -/
  K : ℤ
  /-- argument scale A ≥ 1 (turn units). -/
  A : ℤ
  /-- claimed winding number m ≥ 0; the refutation/exclusion mode split is at the theorem level. -/
  m : ℤ
  /-- bottom-edge breakpoints: Re values, σ₁ → σ₂ strictly increasing. -/
  bottom : List (ℤ × ℤ)
  /-- right-edge breakpoints: Im values, T₁ → T₂ strictly increasing. -/
  right : List (ℤ × ℤ)
  /-- top-edge breakpoints: Re values, σ₂ → σ₁ strictly DEcreasing. -/
  top : List (ℤ × ℤ)
  /-- left-edge breakpoints: Im values, T₂ → T₁ strictly DEcreasing. -/
  left : List (ℤ × ℤ)
  /-- per-segment rows, global traversal order (bottom, right, top, left segments). -/
  rows : List W1Row

/-! ### 2b. W1 checker helpers — Zeta23/W1/Checker.lean -/

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

/-! ### 2c. W1 real/complex reading and the row enclosure — Zeta23/W1/Soundness.lean §1–§2 -/

/-- the real value n/d of a transcript rational (n, d). -/
def ratVal (r : ℤ × ℤ) : ℝ := (r.1 : ℝ) / r.2

/-- σ₁ = p1/q1. -/
def sigma1 (d : W1Data) : ℝ := (d.p1 : ℝ) / d.q1

/-- σ₂ = p2/q2. -/
def sigma2 (d : W1Data) : ℝ := (d.p2 : ℝ) / d.q2

/-- T₁ = a1/b1. -/
def T1 (d : W1Data) : ℝ := (d.a1 : ℝ) / d.b1

/-- T₂ = a2/b2. -/
def T2 (d : W1Data) : ℝ := (d.a2 : ℝ) / d.b2

/-- the complex point x + iy. -/
def cpt (x y : ℝ) : ℂ := ⟨x, y⟩

/-- the closed rectangle [σ₁,σ₂] × [t₁,t₂] ⊂ ℂ. -/
def rectClosed (s₁ s₂ t₁ t₂ : ℝ) : Set ℂ :=
  {s | s₁ ≤ s.re ∧ s.re ≤ s₂ ∧ t₁ ≤ s.im ∧ s.im ≤ t₂}

/-- the open rectangle (σ₁,σ₂) × (t₁,t₂). -/
def rectOpen (s₁ s₂ t₁ t₂ : ℝ) : Set ℂ :=
  {s | s₁ < s.re ∧ s.re < s₂ ∧ t₁ < s.im ∧ s.im < t₂}

/-- the rectangle boundary ∂R (closed minus open; for the nondegenerate rectangles the checker
certifies this is the topological frontier). -/
def rectBdry (s₁ s₂ t₁ t₂ : ℝ) : Set ℂ :=
  rectClosed s₁ s₂ t₁ t₂ \ rectOpen s₁ s₂ t₁ t₂

/-- consecutive pairs of a list: [x₀, x₁, x₂, …] ↦ [(x₀,x₁), (x₁,x₂), …]. -/
def consecPairs {α : Type*} : List α → List (α × α)
  | [] => []
  | [_] => []
  | x :: y :: l => (x, y) :: consecPairs (y :: l)

/-- the point of the directed segment z → w at parameter t ∈ [0,1]. -/
def segPt (z w : ℂ) (t : ℝ) : ℂ := z + (t : ℂ) * (w - z)

/-- bottom-edge breakpoints as complex points (Im = T₁). -/
def bottomPts (d : W1Data) : List ℂ := d.bottom.map fun r => cpt (ratVal r) (T1 d)

/-- right-edge breakpoints (Re = σ₂). -/
def rightPts (d : W1Data) : List ℂ := d.right.map fun r => cpt (sigma2 d) (ratVal r)

/-- top-edge breakpoints (Im = T₂). -/
def topPts (d : W1Data) : List ℂ := d.top.map fun r => cpt (ratVal r) (T2 d)

/-- left-edge breakpoints (Re = σ₁). -/
def leftPts (d : W1Data) : List ℂ := d.left.map fun r => cpt (sigma1 d) (ratVal r)

/-- the boundary segments (endpoint pairs) in global traversal order (FORMAT.md §4):
bottom segments, then right, top, left.  `d.rows` indexes this list. -/
def segs (d : W1Data) : List (ℂ × ℂ) :=
  consecPairs (bottomPts d) ++ consecPairs (rightPts d)
    ++ consecPairs (topPts d) ++ consecPairs (leftPts d)

/-- the log-derivative contour integral along the directed segment z → w (FORMAT.md §6.1):
∫₀¹ (f′/f)(γ(t))·(w−z) dt, γ(t) = z + t(w−z).  (Bochner/interval integral; junk value 0 if the
integrand is not integrable — on the soundness path integrability is PROVED, see the header.) -/
def logDerivSegIntegral (f : ℂ → ℂ) (z w : ℂ) : ℂ :=
  ∫ t in (0:ℝ)..1, (deriv f (segPt z w t) / f (segPt z w t)) * (w - z)

/-- the argument increment Δ along the directed segment z → w: the imaginary part of the
log-derivative integral (FORMAT.md §6.1, derivation D2). -/
def argIncrement (f : ℂ → ℂ) (z w : ℂ) : ℝ := (logDerivSegIntegral f z w).im

/-- H-ENCL for one row/segment pair (FORMAT.md §8.1): (a) the value box encloses K·f at EVERY
point of the closed segment; (b) the argument row encloses A·(Δ/2π) (turn units). -/
def RowEnclOK (f : ℂ → ℂ) (K A : ℤ) (row : W1Row) (zw : ℂ × ℂ) : Prop :=
  (∀ t : ℝ, 0 ≤ t → t ≤ 1 →
      ((row.reLo : ℝ) ≤ K * (f (segPt zw.1 zw.2 t)).re
        ∧ (K : ℝ) * (f (segPt zw.1 zw.2 t)).re ≤ row.reHi)
      ∧ ((row.imLo : ℝ) ≤ K * (f (segPt zw.1 zw.2 t)).im
        ∧ (K : ℝ) * (f (segPt zw.1 zw.2 t)).im ≤ row.imHi))
  ∧ ((row.argLo : ℝ) ≤ A * (argIncrement f zw.1 zw.2 / (2 * π))
      ∧ (A : ℝ) * (argIncrement f zw.1 zw.2 / (2 * π)) ≤ row.argHi)

end W1

open W1

/-! ## 3. Lane B: barrier data, checker, H2-B — Zeta23/DBN/BarrierCert.lean §1–§3 -/

/-- one time prism: seam time τ = tn/td (its left endpoint), the seam transcript (W1 exclusion
rows for the approximant f at time τ on the common rectangle), the floor |f| ≥ Fn/Fd on ∂R,
the approximation defect E (|g_τ − f| ≤ E/K on ∂R) and the displacement D
(|g_t − g_τ| ≤ D/K on ∂R for τ ≤ t ≤ τ⁺).  All fields flat ℤ; every constraint is the
checker's (SPEC §7.3) and every analytic assertion is `PrismEnclOK`. -/
structure PrismData where
  tn : ℤ
  td : ℤ
  K : ℤ
  A : ℤ
  bottom : List (ℤ × ℤ)
  right : List (ℤ × ℤ)
  top : List (ℤ × ℤ)
  left : List (ℤ × ℤ)
  rows : List W1.W1Row
  Fn : ℤ
  Fd : ℤ
  E : ℤ
  D : ℤ

/-- the common rectangle R = [x₁,x₂] × [y₁,y₂] as exact rationals (its own structure, so that each
per-prism instance module can name it without importing the prism list — SPEC §7.6). -/
structure RectData where
  xn1 : ℤ
  xd1 : ℤ
  xn2 : ℤ
  xd2 : ℤ
  yn1 : ℤ
  yd1 : ℤ
  yn2 : ℤ
  yd2 : ℤ

/-- the barrier certificate: the rectangle, the final time t₀ = t0n/t0d, the prisms in time order. -/
structure BarrierData where
  rect : RectData
  t0n : ℤ
  t0d : ℤ
  prisms : List PrismData

/-- the prism's seam transcript as a W1 rectangle transcript (m = 0), so that W1's mesh, segment
and enclosure vocabulary is reused verbatim (`W1.segs`, `W1.RowEnclOK`, `W1.W1Rect`, …). -/
def toW1 (r : RectData) (p : PrismData) : W1.W1Data :=
  { p1 := r.xn1, q1 := r.xd1, p2 := r.xn2, q2 := r.xd2,
    a1 := r.yn1, b1 := r.yd1, a2 := r.yn2, b2 := r.yd2,
    K := p.K, A := p.A, m := 0,
    bottom := p.bottom, right := p.right, top := p.top, left := p.left, rows := p.rows }

/-- the seam rationals (tn, td) of the prisms, in order. -/
def seams (d : BarrierData) : List (ℤ × ℤ) := d.prisms.map fun p => (p.tn, p.td)

/-- W1's C1, C3–C9 with C2 replaced by C2′ (x₁ < x₂, y₁ < y₂ — no strip constraint) and
C10 replaced by m = 0.  The body is W1's helper functions, unchanged. -/
def checkPrismW1 (w : W1.W1Data) : Bool :=
  decide (1 ≤ w.K) && decide (1 ≤ w.A)
    && decide (1 ≤ w.q1) && decide (1 ≤ w.q2) && decide (1 ≤ w.b1) && decide (1 ≤ w.b2)
    && W1.densPos w.bottom && W1.densPos w.right && W1.densPos w.top && W1.densPos w.left
    && decide (w.p1 * w.q2 < w.p2 * w.q1) && decide (w.a1 * w.b2 < w.a2 * w.b1)
    && W1.edgeOK (w.p1, w.q1) (w.p2, w.q2) true w.bottom
    && W1.edgeOK (w.a1, w.b1) (w.a2, w.b2) true w.right
    && W1.edgeOK (w.p2, w.q2) (w.p1, w.q1) false w.top
    && W1.edgeOK (w.a2, w.b2) (w.a1, w.b1) false w.left
    && decide (w.rows.length + 4
        = w.bottom.length + w.right.length + w.top.length + w.left.length)
    && W1.rowsOK w.A w.rows
    && decide (2 * (W1.sumArgHi w.rows - W1.sumArgLo w.rows) < w.A)
    && decide (W1.sumArgLo w.rows ≤ 0) && decide (0 ≤ W1.sumArgHi w.rows)
    && decide (w.m = 0)

/-- per-prism check: the seam exclusion transcript (C-B0..C-B9), the seam denominator and
numerator (C-B0), the floor (C-B11), and the prism gate
C-B12: (E + D)·Fd < Fn·K, i.e. E/K + D/K < Fn/Fd. -/
def checkPrism (r : RectData) (p : PrismData) : Bool :=
  checkPrismW1 (toW1 r p)
    && decide (1 ≤ p.td) && decide (0 ≤ p.tn)
    && decide (0 ≤ p.Fn) && decide (1 ≤ p.Fd) && W1.floorRowsOK p.K p.Fn p.Fd p.rows
    && decide (0 ≤ p.E) && decide (0 ≤ p.D) && decide ((p.E + p.D) * p.Fd < p.Fn * p.K)

/-- the global chain (C-B0 global, C-B2′, C-B13): denominators ≥ 1, y₁ > 0, t₀ > 0, x₁ < x₂,
y₁ < y₂, seam denominators ≥ 1, first seam = 0, seams strictly increasing, last seam < t₀. -/
def checkBarrierChain (d : BarrierData) : Bool :=
  decide (1 ≤ d.rect.xd1) && decide (1 ≤ d.rect.xd2) && decide (1 ≤ d.rect.yd1)
    && decide (1 ≤ d.rect.yd2) && decide (1 ≤ d.t0d) && decide (0 < d.rect.yn1)
    && decide (0 < d.t0n)
    -- C-B2′: x₁ < x₂ and y₁ < y₂ (also re-checked per prism through `checkPrismW1`)
    && decide (d.rect.xn1 * d.rect.xd2 < d.rect.xn2 * d.rect.xd1)
    && decide (d.rect.yn1 * d.rect.yd2 < d.rect.yn2 * d.rect.yd1)
    && W1.densPos (seams d) && W1.firstOK (0, 1) (seams d)
    && W1.chainLt (seams d ++ [(d.t0n, d.t0d)])

/-- **the barrier checker** (monolithic form; equivalent to the chain check plus every prism
check — the soundness theorem takes the split form, SPEC §7.6). -/
def checkBarrier (d : BarrierData) : Bool :=
  checkBarrierChain d && d.prisms.all (checkPrism d.rect)

/-- x₁ = xn1/xd1. -/
def RectData.x1 (r : RectData) : ℝ := (r.xn1 : ℝ) / r.xd1

/-- x₂ = xn2/xd2. -/
def RectData.x2 (r : RectData) : ℝ := (r.xn2 : ℝ) / r.xd2

/-- y₁ = yn1/yd1. -/
def RectData.y1 (r : RectData) : ℝ := (r.yn1 : ℝ) / r.yd1

/-- y₂ = yn2/yd2. -/
def RectData.y2 (r : RectData) : ℝ := (r.yn2 : ℝ) / r.yd2

/-- the seam time τ = tn/td. -/
def seamTime (p : PrismData) : ℝ := (p.tn : ℝ) / p.td

/-- the final time t₀ = t0n/t0d. -/
def t0 (d : BarrierData) : ℝ := (d.t0n : ℝ) / d.t0d

/-- the closed rectangle R of a `RectData` (W1's `rectClosed` of its rationals). -/
def RectClosedOf (r : RectData) : Set ℂ := W1.rectClosed r.x1 r.x2 r.y1 r.y2

/-- the boundary ∂R of a `RectData` (W1's `rectBdry`). -/
def RectBdryOf (r : RectData) : Set ℂ := W1.rectBdry r.x1 r.x2 r.y1 r.y2

/-- the barrier's closed rectangle R. -/
def BarrierRect (d : BarrierData) : Set ℂ := RectClosedOf d.rect

/-- the barrier's boundary ∂R. -/
def BarrierBdry (d : BarrierData) : Set ℂ := RectBdryOf d.rect

/-- the right endpoints of the prisms: the next seam, or t₀ for the last prism. -/
def nextSeams (d : BarrierData) : List ℝ := (d.prisms.tail.map seamTime) ++ [t0 d]

/-- H2-B for one prism [τ, τ⁺]: some holomorphic approximant f on an open U ⊇ R is enclosed by
the seam rows (W1's H-ENCL, verbatim), approximates G τ on ∂R to E/K, and G moves by at most
D/K on ∂R during the prism. -/
def PrismEnclOK (G : ℝ → ℂ → ℂ) (d : BarrierData) (p : PrismData) (τ' : ℝ) : Prop :=
  ∃ (U : Set ℂ) (f : ℂ → ℂ), IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ f U ∧
    List.Forall₂ (W1.RowEnclOK f p.K p.A) p.rows (W1.segs (toW1 d.rect p)) ∧
    (∀ z ∈ BarrierBdry d, ‖G (seamTime p) z - f z‖ ≤ (p.E : ℝ) / p.K) ∧
    (∀ t : ℝ, seamTime p ≤ t → t ≤ τ' →
      ∀ z ∈ BarrierBdry d, ‖G t z - G (seamTime p) z‖ ≤ (p.D : ℝ) / p.K)

/-- **H2-B** (the barrier enclosure hypothesis, displayed), for the normalized family G: every
prism, paired with its right endpoint, satisfies `PrismEnclOK`.  This is where the untrusted
producers enter the trusted statement. -/
def BarrierEnclOK (G : ℝ → ℂ → ℂ) (d : BarrierData) : Prop :=
  List.Forall₂ (PrismEnclOK G d) d.prisms (nextSeams d)

/-! ## 4. Lane A: window data, checker, H2-A, H-TAIL — Zeta23/DBN/Asym.lean -/

/-- the window index N(x) = ⌊√(x/(4π) + t/16)⌋ (Polymath15 (19), p6). -/
def windowIdx (t x : ℝ) : ℕ := ⌊Real.sqrt (x / (4 * π) + t / 16)⌋₊

/-- a window row (SPEC §5.2): windows N ∈ [Nlo, Nhi], modulus floor T/K, defect bound E/K. -/
structure AsymRow where
  Nlo : ℤ
  Nhi : ℤ
  T : ℤ
  E : ℤ

/-- the tail row (SPEC §5.4, Lemma T): N₁ and the five parts Q₁ … Q₄, E₁ (each ⌈K·⌉). -/
structure TailRow where
  N1 : ℤ
  Q1 : ℤ
  Q2 : ℤ
  Q3 : ℤ
  Q4 : ℤ
  E1 : ℤ

/-- the Lane A transcript data: scale K, t₀ = t0n/t0d, y₀ = y0n/y0d, yA = yAn/yAd, rows, tail. -/
structure AsymData where
  K : ℤ
  t0n : ℤ
  t0d : ℤ
  y0n : ℤ
  y0d : ℤ
  yAn : ℤ
  yAd : ℤ
  rows : List AsymRow
  tail : TailRow

/-- C-A3 per row: Nlo ≤ Nhi and 0 ≤ E < T. -/
def checkAsymRow (r : AsymRow) : Bool :=
  decide (r.Nlo ≤ r.Nhi) && decide (0 ≤ r.E) && decide (r.E < r.T)

/-- C-A4: consecutive rows (next.Nlo = Nhi + 1). -/
def consecutive : List AsymRow → Bool
  | [] => true
  | [_] => true
  | r :: s :: l => decide (s.Nlo = r.Nhi + 1) && consecutive (s :: l)

/-- the last row's Nhi (0 on the empty list, which C-A2 excludes). -/
def lastNhi : List AsymRow → ℤ
  | [] => 0
  | [r] => r.Nhi
  | _ :: s :: l => lastNhi (s :: l)

/-- **`checkAsym`** — C-A1 … C-A6 (SPEC §7.4).  Integer arithmetic only: `decide +kernel` on a literal. -/
def checkAsym (d : AsymData) : Bool :=
  decide (1 ≤ d.K) && decide (1 ≤ d.t0d) && decide (0 < d.t0n) && decide (1 ≤ d.y0d)
    && decide (0 < d.y0n) && decide (1 ≤ d.yAd) && decide (0 ≤ d.yAn)
    -- C-A1: yA² ≥ 1 − 2t₀  ⟺  (t0d − 2·t0n)·yAd² ≤ yAn²·t0d
    && decide ((d.t0d - 2 * d.t0n) * d.yAd ^ 2 ≤ d.yAn ^ 2 * d.t0d)
    && decide (0 < d.rows.length)                                        -- C-A2
    && d.rows.all checkAsymRow && consecutive d.rows                      -- C-A3, C-A4
    && decide (d.tail.N1 = lastNhi d.rows + 1)                            -- C-A5
    && decide (0 ≤ d.tail.Q1) && decide (0 ≤ d.tail.Q2) && decide (0 ≤ d.tail.Q3)
    && decide (0 ≤ d.tail.Q4) && decide (0 ≤ d.tail.E1)
    && decide (d.tail.Q1 + d.tail.Q2 + d.tail.Q3 + d.tail.Q4 + d.tail.E1 < 2 * d.K)   -- C-A6

/-- t₀ of the transcript as a real. -/
def At0 (d : AsymData) : ℝ := (d.t0n : ℝ) / d.t0d

/-- y₀ of the transcript as a real. -/
def Ay0 (d : AsymData) : ℝ := (d.y0n : ℝ) / d.y0d

/-- yA of the transcript as a real. -/
def AyA (d : AsymData) : ℝ := (d.yAn : ℝ) / d.yAd

/-- **H2-A** (SPEC §8.1): every window row's floor holds for the normalized function at time t₀. -/
def AsymEnclOK (g : ℂ → ℂ) (d : AsymData) : Prop :=
  ∀ r ∈ d.rows, ∀ x y : ℝ, (r.Nlo : ℝ) ≤ windowIdx (At0 d) x → (windowIdx (At0 d) x : ℝ) ≤ r.Nhi →
    Ay0 d ≤ y → y ≤ AyA d → ((r.T : ℝ) - r.E) / d.K ≤ ‖g (x + y * I)‖

/-- **H-TAIL** (SPEC §8.1, conclusion form): nonvanishing beyond the last window. -/
def TailOK (g : ℂ → ℂ) (d : AsymData) : Prop :=
  ∀ x y : ℝ, (d.tail.N1 : ℝ) ≤ windowIdx (At0 d) x → Ay0 d ≤ y → y ≤ AyA d → g (x + y * I) ≠ 0

end DBN

end
