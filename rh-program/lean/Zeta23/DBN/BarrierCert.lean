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
Zeta23/DBN/BarrierCert.lean — the BARRIER-CERTIFICATE layer of the de Bruijn–Newman milestone
M2a (Lane B of rh-program/results/d1-m2a/SPEC.md v1.0, 2026-09-02): the transcript data types
(SPEC §7.1, §8.2), the integer checker `checkBarrier` (SPEC §7.3) in the RowCert/W1 architecture,
the displayed enclosure hypothesis H2-B (`BarrierEnclOK`, SPEC §8.1), and the soundness theorem
`cert_of_checkBarrier` (SPEC §8.3, proof plan §4.6 D-B1…D-B9).

WHAT THE CERTIFICATE CERTIFIES (SPEC §1.3, Lane B).  For a normalized family G : ℝ → ℂ → ℂ
(instance: G t z = H_t(z)/B_t(z)), a rectangle R = [x₁,x₂] × [y₁,y₂] and a final time t₀ > 0, a
list of consecutive time prisms [τ_j, τ_{j+1}] covering [0, t₀] (τ_J := t₀).  Each prism carries a
W1 EXCLUSION transcript at its seam τ_j for a holomorphic approximant f of G τ_j (winding 0, boundary
nonvanishing, a modulus floor Fn/Fd), plus two integers: the approximation defect E
(|G τ_j − f| ≤ E/K on ∂R) and the displacement D (|G t − G τ_j| ≤ D/K on ∂R for t in the prism).
The checker's one new gate is C-B12: (E + D)·Fd < Fn·K.  Conclusion:

    ∀ t ∈ [0, t₀], ∀ z ∈ R (closed),  G t z ≠ 0.

TRUST MODEL (D-R3 / D-R8, binding; SPEC §3.7, §6).  The honest label for an accepted barrier
transcript is, verbatim: "kernel-checked modulo the displayed hypotheses" — here H2-B
(`BarrierEnclOK G d`) and the holomorphy hypothesis `hHol` of the theorem (for the instance,
discharged from H3's `HtEntire` and L-B3, Instance02.lean).  Never "fully machine-checked".  The
producers are UNTRUSTED by design: their interval arithmetic enters the trusted statement ONLY
through `PrismEnclOK` (the seam rows via W1's `RowEnclOK`, verbatim; the two integer clauses E
and D).  The kernel checks integer relations (`decide +kernel` on the literals, the NumericCert
discipline, no `native_decide`); it does not see t, f, or any real number.

WHAT IS PROVED HERE (all sorry-free; `#print axioms` = propext, Classical.choice, Quot.sound):
  * L-B0  `rectArgPrincipleGen` — the rectangle argument principle in consequence form for a
          general nondegenerate rectangle (W1's `RectArgPrinciple` without its strip clauses; the
          proof is that of `rectArgPrinciple_of_local`, nondegenerate branch), and the strip-free
          restatement of W1's mesh chain (`MeshOK`, `bdry_cover_gen`, `boundary_nonvanishing_gen`,
          `exclusion_of_checkPrismW1` = D-B1, `floor_of_meshOK` = D-B2);
  * D-B3  `re_div_pos_of_norm_sub_lt` — the boundary perturbation: |g − f| < |f| ⟹ g ≠ 0 and
          Re(g/f) > 0;
  * L-B2  `logDerivSegIntegral_div_add` — log-derivative additivity g = (g/f)·f on a segment
          (D-B5), integrability PROVED from continuity (no junk-value path);
  * L-B1  `logDerivSegIntegral_eq_log_sub` — THE ONE NEW ANALYTIC LEMMA (D-B6): if h is holomorphic
          near a segment and Re h > 0 on it, ∫ h′/h = Log h(w) − Log h(z) (principal Log; chain
          rule + FTC).  D-B7 (telescoping over the four edges) is `ring`;
  * `prism_nonvanishing` — D-B8: one prism, one time t, G t ≠ 0 on the closed rectangle;
  * L-B4  `cover_prisms` — D-B9: every t ∈ [0, t₀] lies in some prism (list induction on the
          `Forall₂` of H2-B; C-B13's monotonicity is a reject-more check, not a soundness input);
  * `cert_of_checkBarrier` — Lane B soundness, exactly the SPEC §8.3 shape (checker facts in the
          split form `hchain`/`hprisms` so that per-prism kernel facts live in per-prism modules,
          SPEC §7.6); and `cert_of_checkBarrier_xy`, the same conclusion in the coordinate form
          that `Polymath15Bridge`'s hypothesis (iii) consumes, for H = G·B.

WHAT IS DISPLAYED (not proved here; D-R3 vocabulary):
  * H2-B `BarrierEnclOK G d` — the producers' claims: per prism, SOME f holomorphic on an open
    U ⊇ R is enclosed by the seam rows (W1 H-ENCL), approximates G τ_j on ∂R to E/K, and G moves
    by at most D/K on ∂R during the prism.  f is deliberately NOT defined in Lean (SPEC §4.2:
    defining P15's f_t would move eqs. (14)–(19) into the trusted layer; M2b replaces the
    existential by it).
  * `hHol` — G t is holomorphic on an open neighborhood of R for every t ∈ [0, t₀] (for the
    instance, from H3's `HtEntire` and L-B3 `Bt` ≠ 0 near R; Instance02.lean).
No Rouché theorem, no homotopy invariance and no zero-continuity in t is used or assumed (SPEC
§4.6): the time step reduces to the fixed-t argument principle applied twice (to f, to G t) plus
L-B1.  Nothing in `W1/` is modified (SPEC §8.4); the W1 helpers are called on `toW1 rect prism`.

Numeric-literal discipline: the checker is +, ·, ^2 and comparisons on ℤ and list lengths; every
rational comparison by cross-multiplication (FORMAT.md D7); no floats, no division, no
transcendental constants in checked data.
-/
import Zeta23.DBN.Defs
import Zeta23.W1.ArgPrincipleBridge

open scoped Real
open Complex (I)
open MeasureTheory

noncomputable section

namespace Zeta23
namespace DBN

open W1 W1.ArgPrinciple

/-! ## 1. Barrier-lane data (SPEC §7.1, §8.2) -/

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

/-! ## 2. The checker (SPEC §7.3) -/

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

/-! ## 3. The real reading of the data and the displayed hypothesis H2-B (SPEC §8.1) -/

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

/-! ### definitional bridges to the W1 vocabulary (all `rfl`) -/

lemma sigma1_toW1 (r : RectData) (p : PrismData) : sigma1 (toW1 r p) = r.x1 := rfl
lemma sigma2_toW1 (r : RectData) (p : PrismData) : sigma2 (toW1 r p) = r.x2 := rfl
lemma T1_toW1 (r : RectData) (p : PrismData) : T1 (toW1 r p) = r.y1 := rfl
lemma T2_toW1 (r : RectData) (p : PrismData) : T2 (toW1 r p) = r.y2 := rfl
lemma W1Rect_toW1 (r : RectData) (p : PrismData) : W1Rect (toW1 r p) = RectClosedOf r := rfl
lemma W1Bdry_toW1 (r : RectData) (p : PrismData) : W1Bdry (toW1 r p) = RectBdryOf r := rfl

/-! ## 4. Unpacking the checker -/

/-- the semantic content of `checkPrismW1 w = true` — W1's `ChecksOK` minus its strip clauses
(hC2a, hC2c), with C2′ (`hC2x`, `hC2y`) and m = 0 (`hC9a`, `hC9b`, `hm`). -/
structure MeshOK (w : W1Data) : Prop where
  hK : 1 ≤ w.K
  hA : 1 ≤ w.A
  hq1 : 1 ≤ w.q1
  hq2 : 1 ≤ w.q2
  hb1 : 1 ≤ w.b1
  hb2 : 1 ≤ w.b2
  hdb : densPos w.bottom = true
  hdr : densPos w.right = true
  hdt : densPos w.top = true
  hdl : densPos w.left = true
  hC2x : w.p1 * w.q2 < w.p2 * w.q1
  hC2y : w.a1 * w.b2 < w.a2 * w.b1
  hEb : edgeOK (w.p1, w.q1) (w.p2, w.q2) true w.bottom = true
  hEr : edgeOK (w.a1, w.b1) (w.a2, w.b2) true w.right = true
  hEt : edgeOK (w.p2, w.q2) (w.p1, w.q1) false w.top = true
  hEl : edgeOK (w.a2, w.b2) (w.a1, w.b1) false w.left = true
  hC4 : w.rows.length + 4 = w.bottom.length + w.right.length + w.top.length + w.left.length
  hRows : rowsOK w.A w.rows = true
  hC8 : 2 * (sumArgHi w.rows - sumArgLo w.rows) < w.A
  hC9a : sumArgLo w.rows ≤ 0
  hC9b : 0 ≤ sumArgHi w.rows
  hm : w.m = 0

lemma meshOK_of_checkPrismW1 {w : W1Data} (hc : checkPrismW1 w = true) : MeshOK w := by
  simp only [checkPrismW1, Bool.and_eq_true, decide_eq_true_eq] at hc
  obtain ⟨hc, hm⟩ := hc
  obtain ⟨hc, hC9b⟩ := hc
  obtain ⟨hc, hC9a⟩ := hc
  obtain ⟨hc, hC8⟩ := hc
  obtain ⟨hc, hRows⟩ := hc
  obtain ⟨hc, hC4⟩ := hc
  obtain ⟨hc, hEl⟩ := hc
  obtain ⟨hc, hEt⟩ := hc
  obtain ⟨hc, hEr⟩ := hc
  obtain ⟨hc, hEb⟩ := hc
  obtain ⟨hc, hC2y⟩ := hc
  obtain ⟨hc, hC2x⟩ := hc
  obtain ⟨hc, hdl⟩ := hc
  obtain ⟨hc, hdt⟩ := hc
  obtain ⟨hc, hdr⟩ := hc
  obtain ⟨hc, hdb⟩ := hc
  obtain ⟨hc, hb2⟩ := hc
  obtain ⟨hc, hb1⟩ := hc
  obtain ⟨hc, hq2⟩ := hc
  obtain ⟨hK, hq1⟩ := hc
  exact ⟨hK.1, hK.2, hq1, hq2, hb1, hb2, hdb, hdr, hdt, hdl, hC2x, hC2y, hEb, hEr, hEt, hEl,
    hC4, hRows, hC8, hC9a, hC9b, hm⟩

/-- the semantic content of `checkPrism r p = true`. -/
lemma checkPrism_spec {r : RectData} {p : PrismData} (hc : checkPrism r p = true) :
    checkPrismW1 (toW1 r p) = true ∧ 1 ≤ p.td ∧ 0 ≤ p.tn ∧ 0 ≤ p.Fn ∧ 1 ≤ p.Fd
      ∧ floorRowsOK p.K p.Fn p.Fd p.rows = true ∧ 0 ≤ p.E ∧ 0 ≤ p.D
      ∧ (p.E + p.D) * p.Fd < p.Fn * p.K := by
  simp only [checkPrism, Bool.and_eq_true, decide_eq_true_eq] at hc
  obtain ⟨hc, hC12⟩ := hc
  obtain ⟨hc, hD⟩ := hc
  obtain ⟨hc, hE⟩ := hc
  obtain ⟨hc, hrows⟩ := hc
  obtain ⟨hc, hFd⟩ := hc
  obtain ⟨hc, hFn⟩ := hc
  obtain ⟨hc, htn⟩ := hc
  obtain ⟨hc1, htd⟩ := hc
  exact ⟨hc1, htd, htn, hFn, hFd, hrows, hE, hD, hC12⟩

/-- the semantic content of `checkBarrierChain d = true`. -/
lemma checkBarrierChain_spec {d : BarrierData} (hc : checkBarrierChain d = true) :
    1 ≤ d.rect.xd1 ∧ 1 ≤ d.rect.xd2 ∧ 1 ≤ d.rect.yd1 ∧ 1 ≤ d.rect.yd2 ∧ 1 ≤ d.t0d
      ∧ 0 < d.rect.yn1 ∧ 0 < d.t0n
      ∧ d.rect.xn1 * d.rect.xd2 < d.rect.xn2 * d.rect.xd1
      ∧ d.rect.yn1 * d.rect.yd2 < d.rect.yn2 * d.rect.yd1
      ∧ densPos (seams d) = true ∧ firstOK (0, 1) (seams d) = true
      ∧ chainLt (seams d ++ [(d.t0n, d.t0d)]) = true := by
  simp only [checkBarrierChain, Bool.and_eq_true, decide_eq_true_eq] at hc
  obtain ⟨hc, h12⟩ := hc
  obtain ⟨hc, h11⟩ := hc
  obtain ⟨hc, h10⟩ := hc
  obtain ⟨hc, h9⟩ := hc
  obtain ⟨hc, h8⟩ := hc
  obtain ⟨hc, h7⟩ := hc
  obtain ⟨hc, h6⟩ := hc
  obtain ⟨hc, h5⟩ := hc
  obtain ⟨hc, h4⟩ := hc
  obtain ⟨hc, h3⟩ := hc
  obtain ⟨h1, h2⟩ := hc
  exact ⟨h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12⟩

/-! ## 5. L-B0: W1's mesh chain, strip-free (the proofs are those of Soundness.lean §6 with
`ChecksOK` replaced by `MeshOK`; nothing in `W1/` is modified) -/

/-- every boundary point lies on some transcript segment (W1 `bdry_cover`, strip-free). -/
lemma bdry_cover_gen {d : W1Data} (hchk : MeshOK d) :
    ∀ s ∈ W1Bdry d, ∃ zw ∈ segs d, ∃ t : ℝ, 0 ≤ t ∧ t ≤ 1 ∧ segPt zw.1 zw.2 t = s := by
  intro s hs
  obtain ⟨hcl, hno⟩ := hs
  obtain ⟨h1, h2, h3, h4⟩ := hcl
  obtain ⟨h2b, hfb, hlb, hcb⟩ := edgeOK_inc_spec hchk.hEb
  obtain ⟨h2r, hfr, hlr, hcr⟩ := edgeOK_inc_spec hchk.hEr
  obtain ⟨h2t, hft, hlt', hct⟩ := edgeOK_dec_spec hchk.hEt
  obtain ⟨h2l, hfl, hll, hclf⟩ := edgeOK_dec_spec hchk.hEl
  rcases eq_or_lt_of_le h3 with e3 | l3
  · -- bottom edge: s.im = T₁
    obtain ⟨ra, hra, hva⟩ := firstOK_spec hfb hchk.hdb hchk.hq1
    obtain ⟨rb, hrb, hvb⟩ := lastOK_spec hchk.hq2 hlb hchk.hdb
    have hpairs := chainLt_spec hchk.hdb hcb
    obtain ⟨q, hqm, hq1, hq2⟩ := cover_chain ratVal d.bottom ra rb s.re hra hrb hpairs h2b
      (by rw [hva]; exact h1) (by rw [hvb]; exact h2)
    obtain ⟨t, ht0, ht1, hteq⟩ := exists_t_inc (hpairs q hqm) hq1 hq2
    refine ⟨(cpt (ratVal q.1) (T1 d), cpt (ratVal q.2) (T1 d)), ?_, t, ht0, ht1, ?_⟩
    · have : (cpt (ratVal q.1) (T1 d), cpt (ratVal q.2) (T1 d))
          ∈ consecPairs (bottomPts d) := by
        unfold bottomPts
        rw [consecPairs_map]
        exact List.mem_map.mpr ⟨q, hqm, rfl⟩
      simp [segs, List.mem_append, this]
    · rw [segPt_mk_horiz, hteq]
      exact Complex.ext rfl (by simpa using e3)
  rcases eq_or_lt_of_le h4 with e4 | l4
  · -- top edge: s.im = T₂
    obtain ⟨ra, hra, hva⟩ := firstOK_spec hft hchk.hdt hchk.hq2
    obtain ⟨rb, hrb, hvb⟩ := lastOK_spec hchk.hq1 hlt' hchk.hdt
    have hpairs := chainGt_spec hchk.hdt hct
    obtain ⟨q, hqm, hq1, hq2⟩ := cover_chain_dec ratVal d.top ra rb s.re hra hrb hpairs h2t
      (by rw [hvb]; exact h1) (by rw [hva]; exact h2)
    obtain ⟨t, ht0, ht1, hteq⟩ := exists_t_dec (hpairs q hqm) hq1 hq2
    refine ⟨(cpt (ratVal q.1) (T2 d), cpt (ratVal q.2) (T2 d)), ?_, t, ht0, ht1, ?_⟩
    · have : (cpt (ratVal q.1) (T2 d), cpt (ratVal q.2) (T2 d))
          ∈ consecPairs (topPts d) := by
        unfold topPts
        rw [consecPairs_map]
        exact List.mem_map.mpr ⟨q, hqm, rfl⟩
      simp [segs, List.mem_append, this]
    · rw [segPt_mk_horiz, hteq]
      exact Complex.ext rfl (by simpa using e4.symm)
  rcases eq_or_lt_of_le h1 with e1 | l1
  · -- left edge: s.re = σ₁
    obtain ⟨ra, hra, hva⟩ := firstOK_spec hfl hchk.hdl hchk.hb2
    obtain ⟨rb, hrb, hvb⟩ := lastOK_spec hchk.hb1 hll hchk.hdl
    have hpairs := chainGt_spec hchk.hdl hclf
    obtain ⟨q, hqm, hq1, hq2⟩ := cover_chain_dec ratVal d.left ra rb s.im hra hrb hpairs h2l
      (by rw [hvb]; exact l3.le) (by rw [hva]; exact l4.le)
    obtain ⟨t, ht0, ht1, hteq⟩ := exists_t_dec (hpairs q hqm) hq1 hq2
    refine ⟨(cpt (sigma1 d) (ratVal q.1), cpt (sigma1 d) (ratVal q.2)), ?_, t, ht0, ht1, ?_⟩
    · have : (cpt (sigma1 d) (ratVal q.1), cpt (sigma1 d) (ratVal q.2))
          ∈ consecPairs (leftPts d) := by
        unfold leftPts
        rw [consecPairs_map]
        exact List.mem_map.mpr ⟨q, hqm, rfl⟩
      simp [segs, List.mem_append, this]
    · rw [segPt_mk_vert, hteq]
      exact Complex.ext (by simpa using e1) rfl
  rcases eq_or_lt_of_le h2 with e2 | l2
  · -- right edge: s.re = σ₂
    obtain ⟨ra, hra, hva⟩ := firstOK_spec hfr hchk.hdr hchk.hb1
    obtain ⟨rb, hrb, hvb⟩ := lastOK_spec hchk.hb2 hlr hchk.hdr
    have hpairs := chainLt_spec hchk.hdr hcr
    obtain ⟨q, hqm, hq1, hq2⟩ := cover_chain ratVal d.right ra rb s.im hra hrb hpairs h2r
      (by rw [hva]; exact l3.le) (by rw [hvb]; exact l4.le)
    obtain ⟨t, ht0, ht1, hteq⟩ := exists_t_inc (hpairs q hqm) hq1 hq2
    refine ⟨(cpt (sigma2 d) (ratVal q.1), cpt (sigma2 d) (ratVal q.2)), ?_, t, ht0, ht1, ?_⟩
    · have : (cpt (sigma2 d) (ratVal q.1), cpt (sigma2 d) (ratVal q.2))
          ∈ consecPairs (rightPts d) := by
        unfold rightPts
        rw [consecPairs_map]
        exact List.mem_map.mpr ⟨q, hqm, rfl⟩
      simp [segs, List.mem_append, this]
    · rw [segPt_mk_vert, hteq]
      exact Complex.ext (by simpa using e2.symm) rfl
  · exact absurd ⟨l1, l2, l3, l4⟩ hno

/-- f ≠ 0 on all of ∂R (W1 `boundary_nonvanishing`, strip-free; FORMAT.md D1). -/
lemma boundary_nonvanishing_gen {f : ℂ → ℂ} {d : W1Data} (hchk : MeshOK d)
    (hE : W1EnclOK f d) : ∀ s ∈ W1Bdry d, f s ≠ 0 := by
  intro s hs
  obtain ⟨zw, hzw, t, ht0, ht1, hpt⟩ := bdry_cover_gen hchk s hs
  obtain ⟨row, hrow, hR⟩ := forall₂_mem_right hE zw hzw
  have hOK := rowsOK_mem hchk.hRows row hrow
  have := row_box_excludes_zero hR (rowOK_C6 hOK) t ht0 ht1
  rw [hpt] at this
  exact this

/-- **D-B2**, the C11 floor for a strip-free mesh (W1 `floor_of_checkW1Floor`, same derivation
D6): |f| ≥ Fn/Fd on ∂R under H-ENCL(a). -/
theorem floor_of_meshOK {f : ℂ → ℂ} {d : W1Data} (hchk : MeshOK d) (hEncl : W1EnclOK f d)
    {Fn Fd : ℤ} (hFn : 0 ≤ Fn) (hFd : 1 ≤ Fd) (hrows : floorRowsOK d.K Fn Fd d.rows = true) :
    ∀ s ∈ W1Bdry d, (Fn : ℝ) / Fd ≤ ‖f s‖ := by
  intro s hs
  obtain ⟨zw, hzw, t, ht0, ht1, hpt⟩ := bdry_cover_gen hchk s hs
  obtain ⟨row, hrow, hR⟩ := forall₂_mem_right hEncl zw hzw
  have hOK := floorRowsOK_mem hrows row hrow
  simp only [floorRowOK, decide_eq_true_eq] at hOK
  obtain ⟨⟨hre1, hre2⟩, him1, him2⟩ := hR.1 t ht0 ht1
  rw [hpt] at hre1 hre2 him1 him2
  have hmre := mdist_sq_le (lo := row.reLo) (hi := row.reHi)
    (x := (d.K : ℝ) * (f s).re) hre1 hre2
  have hmim := mdist_sq_le (lo := row.imLo) (hi := row.imHi)
    (x := (d.K : ℝ) * (f s).im) him1 him2
  have hKpos : (0 : ℝ) < (d.K : ℝ) := by
    have : (1 : ℝ) ≤ (d.K : ℝ) := by exact_mod_cast hchk.hK
    linarith
  have hFdpos : (0 : ℝ) < (Fd : ℝ) := by
    have : (1 : ℝ) ≤ (Fd : ℝ) := by exact_mod_cast hFd
    linarith
  have hFnn : (0 : ℝ) ≤ (Fn : ℝ) := by exact_mod_cast hFn
  have hnormsq : ‖f s‖ ^ 2 = (f s).re ^ 2 + (f s).im ^ 2 := by
    rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
    ring
  have hC11 : (Fn : ℝ) ^ 2 * (d.K : ℝ) ^ 2
      ≤ (((mdist row.reLo row.reHi : ℤ) : ℝ) ^ 2 + ((mdist row.imLo row.imHi : ℤ) : ℝ) ^ 2)
        * (Fd : ℝ) ^ 2 := by exact_mod_cast hOK
  have hsum : ((mdist row.reLo row.reHi : ℤ) : ℝ) ^ 2 + ((mdist row.imLo row.imHi : ℤ) : ℝ) ^ 2
      ≤ (d.K : ℝ) ^ 2 * ‖f s‖ ^ 2 := by
    rw [hnormsq]
    nlinarith [hmre, hmim]
  have hK2 : (0 : ℝ) < (d.K : ℝ) ^ 2 := by positivity
  have hkey : (Fn : ℝ) ^ 2 ≤ ‖f s‖ ^ 2 * (Fd : ℝ) ^ 2 := by
    have hcomb : (Fn : ℝ) ^ 2 * (d.K : ℝ) ^ 2
        ≤ ((d.K : ℝ) ^ 2 * ‖f s‖ ^ 2) * (Fd : ℝ) ^ 2 := by
      calc (Fn : ℝ) ^ 2 * (d.K : ℝ) ^ 2
          ≤ (((mdist row.reLo row.reHi : ℤ) : ℝ) ^ 2
              + ((mdist row.imLo row.imHi : ℤ) : ℝ) ^ 2) * (Fd : ℝ) ^ 2 := hC11
        _ ≤ ((d.K : ℝ) ^ 2 * ‖f s‖ ^ 2) * (Fd : ℝ) ^ 2 :=
            mul_le_mul_of_nonneg_right hsum (sq_nonneg _)
    have hcomb' : (d.K : ℝ) ^ 2 * (Fn : ℝ) ^ 2
        ≤ (d.K : ℝ) ^ 2 * (‖f s‖ ^ 2 * (Fd : ℝ) ^ 2) := by
      nlinarith [hcomb]
    exact le_of_mul_le_mul_left hcomb' hK2
  rw [div_le_iff₀ hFdpos]
  by_contra hlt
  rw [not_le] at hlt
  nlinarith [hkey, mul_nonneg (norm_nonneg (f s)) hFdpos.le]

/-! ## 6. L-B0: the argument principle on a general nondegenerate rectangle -/

/-- **L-B0.**  The rectangle argument principle in consequence form for a GENERAL nondegenerate
rectangle: W1's `RectArgPrinciple` without the strip clauses ½ < σ₁, σ₂ < 1 (which W1's C2 imposes
for ζ and which the proof of `rectArgPrinciple_of_local` never uses).  Same proof, nondegenerate
branch.  Traversal: bottom (σ₁+it₁ → σ₂+it₁), right (→ σ₂+it₂), top (→ σ₁+it₂), left (→ σ₁+it₁). -/
theorem rectArgPrincipleGen (f : ℂ → ℂ) (s₁ s₂ t₁ t₂ : ℝ) (hs : s₁ < s₂) (ht : t₁ < t₂)
    (U : Set ℂ) (hU : IsOpen U) (hRU : rectClosed s₁ s₂ t₁ t₂ ⊆ U)
    (hf : DifferentiableOn ℂ f U) (hbd : ∀ s ∈ rectBdry s₁ s₂ t₁ t₂, f s ≠ 0) :
    ∃ Z : ℕ,
      2 * π * Z
          = argIncrement f (cpt s₁ t₁) (cpt s₂ t₁) + argIncrement f (cpt s₂ t₁) (cpt s₂ t₂)
            + argIncrement f (cpt s₂ t₂) (cpt s₁ t₂) + argIncrement f (cpt s₁ t₂) (cpt s₁ t₁)
        ∧ (Z = 0 → ∀ s ∈ rectOpen s₁ s₂ t₁ t₂, f s ≠ 0)
        ∧ (1 ≤ Z → ∃ ρ ∈ rectOpen s₁ s₂ t₁ t₂, f ρ = 0) := by
  have hs12 : s₁ ≤ s₂ := hs.le
  have hre : (cpt s₁ t₁).re < (cpt s₂ t₂).re := hs
  have him : (cpt s₁ t₁).im < (cpt s₂ t₂).im := ht
  have hRect : Rect (cpt s₁ t₁) (cpt s₂ t₂) = rectClosed s₁ s₂ t₁ t₂ := Rect_cpt hs12 ht.le
  have hFr : RectFrontier (cpt s₁ t₁) (cpt s₂ t₂) = rectBdry s₁ s₂ t₁ t₂ :=
    RectFrontier_cpt hs12 ht.le
  have hRU' : Rect (cpt s₁ t₁) (cpt s₂ t₂) ⊆ U := hRect ▸ hRU
  have hbd' : ∀ c ∈ RectFrontier (cpt s₁ t₁) (cpt s₂ t₂), f c ≠ 0 := hFr ▸ hbd
  have hzR : cpt s₁ t₁ ∈ Rect (cpt s₁ t₁) (cpt s₂ t₂) :=
    RectFrontier_subset_Rect _ _ (mem_RectFrontier_left_corner _ _)
  have hne : ∃ x ∈ Rect (cpt s₁ t₁) (cpt s₂ t₂), f x ≠ 0 :=
    ⟨cpt s₁ t₁, hzR, hbd' _ (mem_RectFrontier_left_corner _ _)⟩
  have hAn : AnalyticOnNhd ℂ f (Rect (cpt s₁ t₁) (cpt s₂ t₂)) :=
    (hf.analyticOnNhd hU).mono hRU'
  have hfin := finite_zeros_Rect_on hU hRU' hf hne
  classical
  have hS : ∀ p, p ∈ hfin.toFinset ↔ (p ∈ Rect (cpt s₁ t₁) (cpt s₂ t₂) ∧ f p = 0) :=
    fun p => by simp [Set.Finite.mem_toFinset]
  have hW := windingRect_eq_sum_analyticOrder_on hre him hU hRU' hf hbd' hfin.toFinset hS
  refine ⟨∑ p ∈ hfin.toFinset, analyticOrderNatAt f p, ?_, ?_, ?_⟩
  · -- (i) the winding identity
    have h2πI : (2 * (π : ℂ) * I) ≠ 0 :=
      mul_ne_zero (mul_ne_zero two_ne_zero (Complex.ofReal_ne_zero.mpr Real.pi_ne_zero))
        Complex.I_ne_zero
    have hRI : rectIntegral (logDeriv f) (cpt s₁ t₁) (cpt s₂ t₂)
        = 2 * (π : ℂ) * I * ((∑ p ∈ hfin.toFinset, analyticOrderNatAt f p : ℕ) : ℂ) := by
      rw [windingRect] at hW
      push_cast
      exact (inv_mul_eq_iff_eq_mul₀ h2πI).mp hW
    have hcast : 2 * (π : ℂ) * I * ((∑ p ∈ hfin.toFinset, analyticOrderNatAt f p : ℕ) : ℂ)
        = ((2 * π * ((∑ p ∈ hfin.toFinset, analyticOrderNatAt f p : ℕ) : ℝ) : ℝ) : ℂ) * I := by
      push_cast
      ring
    simp only [argIncrement]
    rw [← Complex.add_im, ← Complex.add_im, ← Complex.add_im, edge_sum_eq_rectIntegral, hRI,
      hcast, Complex.mul_I_im, Complex.ofReal_re]
  · -- (ii) Z = 0 → no zero in the open rectangle
    intro hZ s hs' hfs
    have hsR : s ∈ Rect (cpt s₁ t₁) (cpt s₂ t₂) := by
      rw [hRect]
      exact ⟨hs'.1.le, hs'.2.1.le, hs'.2.2.1.le, hs'.2.2.2.le⟩
    have hsS : s ∈ hfin.toFinset := (hS s).mpr ⟨hsR, hfs⟩
    have h0 : analyticOrderNatAt f s = 0 := Finset.sum_eq_zero_iff.mp hZ s hsS
    rw [analyticOrderNatAt, ENat.toNat_eq_zero] at h0
    rcases h0 with h0 | h0
    · exact ((hAn s hsR).analyticOrderAt_eq_zero.mp h0) hfs
    · exact analyticOrderAt_ne_top_of_analyticOnNhd (isPreconnected_Rect _ _) hAn hne hsR h0
  · -- (iii) Z ≥ 1 → a zero in the open rectangle
    intro hZ
    have hne0 : ∑ p ∈ hfin.toFinset, analyticOrderNatAt f p ≠ 0 := by omega
    obtain ⟨p, hp⟩ := Finset.nonempty_of_sum_ne_zero hne0
    obtain ⟨hpR, hp0⟩ := (hS p).mp hp
    have hIoo := mem_Ioo_of_zero_mem_Rect hre him hbd' hpR hp0
    exact ⟨p, ⟨hIoo.1.1, hIoo.1.2, hIoo.2.1, hIoo.2.2⟩, hp0⟩

/-! ## 7. Edge geometry: the four directed edges lie on ∂R; the edge integrand is continuous -/

lemma bottom_seg_mem {s₁ s₂ t₁ t₂ : ℝ} (hs : s₁ ≤ s₂) (ht : t₁ < t₂) (t : ℝ)
    (h0 : 0 ≤ t) (h1 : t ≤ 1) :
    segPt (cpt s₁ t₁) (cpt s₂ t₁) t ∈ rectBdry s₁ s₂ t₁ t₂ := by
  rw [segPt_mk_horiz]
  simp only [rectBdry, rectClosed, rectOpen, Set.mem_sdiff, Set.mem_ofPred_eq, cpt_re, cpt_im]
  refine ⟨⟨by nlinarith, by nlinarith, le_rfl, ht.le⟩, ?_⟩
  rintro ⟨-, -, hlt, -⟩
  exact lt_irrefl _ hlt

lemma right_seg_mem {s₁ s₂ t₁ t₂ : ℝ} (hs : s₁ ≤ s₂) (ht : t₁ < t₂) (t : ℝ)
    (h0 : 0 ≤ t) (h1 : t ≤ 1) :
    segPt (cpt s₂ t₁) (cpt s₂ t₂) t ∈ rectBdry s₁ s₂ t₁ t₂ := by
  rw [segPt_mk_vert]
  simp only [rectBdry, rectClosed, rectOpen, Set.mem_sdiff, Set.mem_ofPred_eq, cpt_re, cpt_im]
  refine ⟨⟨hs, le_rfl, by nlinarith, by nlinarith⟩, ?_⟩
  rintro ⟨-, hlt, -, -⟩
  exact lt_irrefl _ hlt

lemma top_seg_mem {s₁ s₂ t₁ t₂ : ℝ} (hs : s₁ ≤ s₂) (ht : t₁ < t₂) (t : ℝ)
    (h0 : 0 ≤ t) (h1 : t ≤ 1) :
    segPt (cpt s₂ t₂) (cpt s₁ t₂) t ∈ rectBdry s₁ s₂ t₁ t₂ := by
  rw [segPt_mk_horiz]
  simp only [rectBdry, rectClosed, rectOpen, Set.mem_sdiff, Set.mem_ofPred_eq, cpt_re, cpt_im]
  refine ⟨⟨by nlinarith, by nlinarith, ht.le, le_rfl⟩, ?_⟩
  rintro ⟨-, -, -, hlt⟩
  exact lt_irrefl _ hlt

lemma left_seg_mem {s₁ s₂ t₁ t₂ : ℝ} (hs : s₁ ≤ s₂) (ht : t₁ < t₂) (t : ℝ)
    (h0 : 0 ≤ t) (h1 : t ≤ 1) :
    segPt (cpt s₁ t₂) (cpt s₁ t₁) t ∈ rectBdry s₁ s₂ t₁ t₂ := by
  rw [segPt_mk_vert]
  simp only [rectBdry, rectClosed, rectOpen, Set.mem_sdiff, Set.mem_ofPred_eq, cpt_re, cpt_im]
  refine ⟨⟨le_rfl, hs, by nlinarith, by nlinarith⟩, ?_⟩
  rintro ⟨hlt, -, -, -⟩
  exact lt_irrefl _ hlt

/-- the edge integrand t ↦ (f′/f)(γ(t))·(w − z) is continuous on [0,1] when f is holomorphic on
an open set containing the segment and nonvanishing on it (the generic form of W1's
`continuousOn_zeta_logDeriv_seg`; this is the PROVED integrability input of every integral
identity below — no junk-value path). -/
lemma continuousOn_logDeriv_seg {f : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hf : DifferentiableOn ℂ f U) {z w : ℂ}
    (hseg : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → segPt z w t ∈ U)
    (hnz : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → f (segPt z w t) ≠ 0) :
    ContinuousOn (fun t : ℝ => (deriv f (segPt z w t) / f (segPt z w t)) * (w - z))
      (Set.Icc 0 1) := by
  have hAn : AnalyticOnNhd ℂ f U := hf.analyticOnNhd hU
  have hdC : ContinuousOn (deriv f) U := hAn.deriv.continuousOn
  have hfC : ContinuousOn f U := hAn.continuousOn
  have hsegC : Continuous fun t : ℝ => segPt z w t := by
    unfold segPt
    exact continuous_const.add (Complex.continuous_ofReal.mul continuous_const)
  have hmaps : Set.MapsTo (fun t : ℝ => segPt z w t) (Set.Icc 0 1) U :=
    fun t ht => hseg t ht.1 ht.2
  exact ((hdC.comp hsegC.continuousOn hmaps).div (hfC.comp hsegC.continuousOn hmaps)
    fun t ht => hnz t ht.1 ht.2).mul continuousOn_const

/-! ## 8. D-B1: the seam exclusion for f (the W1 chain, strip-free, generic in f) -/

/-- **D-B1.**  An accepted seam transcript (`checkPrismW1`, m = 0) with its rows enclosing f
(H-ENCL) certifies, for f holomorphic on an open U ⊇ R: f ≠ 0 on the closed rectangle, AND the
four-edge argument increment of f around ∂R is exactly 0 (the winding pinned by C8/C9,
FORMAT.md D4).  The second clause is what D-B8 consumes. -/
theorem exclusion_of_checkPrismW1 {f : ℂ → ℂ} (d : W1Data) (hc : checkPrismW1 d = true)
    (hEncl : W1EnclOK f d) {U : Set ℂ} (hU : IsOpen U) (hRU : W1Rect d ⊆ U)
    (hf : DifferentiableOn ℂ f U) :
    (∀ s ∈ W1Rect d, f s ≠ 0)
    ∧ argIncrement f (cpt (sigma1 d) (T1 d)) (cpt (sigma2 d) (T1 d))
        + argIncrement f (cpt (sigma2 d) (T1 d)) (cpt (sigma2 d) (T2 d))
        + argIncrement f (cpt (sigma2 d) (T2 d)) (cpt (sigma1 d) (T2 d))
        + argIncrement f (cpt (sigma1 d) (T2 d)) (cpt (sigma1 d) (T1 d)) = 0 := by
  have hchk := meshOK_of_checkPrismW1 hc
  have hs12 : sigma1 d < sigma2 d :=
    ratVal_lt_of_cross (r := (d.p1, d.q1)) (s := (d.p2, d.q2)) hchk.hq1 hchk.hq2 hchk.hC2x
  have hT12 : T1 d < T2 d :=
    ratVal_lt_of_cross (r := (d.a1, d.b1)) (s := (d.a2, d.b2)) hchk.hb1 hchk.hb2 hchk.hC2y
  -- boundary nonvanishing (D1)
  have hbnz := boundary_nonvanishing_gen hchk hEncl
  -- edge data
  obtain ⟨h2b, hfb, hlb, hcb⟩ := edgeOK_inc_spec hchk.hEb
  obtain ⟨h2r, hfr, hlr, hcr⟩ := edgeOK_inc_spec hchk.hEr
  obtain ⟨h2t, hft, hlt', hct⟩ := edgeOK_dec_spec hchk.hEt
  obtain ⟨h2l, hfl, hll, hclf⟩ := edgeOK_dec_spec hchk.hEl
  -- real breakpoint chains, heads and lasts
  obtain ⟨rba, hrba, hvba⟩ := firstOK_spec hfb hchk.hdb hchk.hq1
  obtain ⟨rbb, hrbb, hvbb⟩ := lastOK_spec hchk.hq2 hlb hchk.hdb
  have hheadb : (d.bottom.map ratVal).head? = some (sigma1 d) := by
    rw [List.head?_map, hrba, Option.map_some]
    exact congrArg some hvba
  have hlastb : (d.bottom.map ratVal).getLast? = some (sigma2 d) := by
    rw [List.getLast?_map, hrbb, Option.map_some]
    exact congrArg some hvbb
  have hpairsb : ∀ p ∈ consecPairs (d.bottom.map ratVal), p.1 < p.2 :=
    consec_map_forall fun q hq => chainLt_spec hchk.hdb hcb q hq
  obtain ⟨rra, hrra, hvra⟩ := firstOK_spec hfr hchk.hdr hchk.hb1
  obtain ⟨rrb, hrrb, hvrb⟩ := lastOK_spec hchk.hb2 hlr hchk.hdr
  have hheadr : (d.right.map ratVal).head? = some (T1 d) := by
    rw [List.head?_map, hrra, Option.map_some]
    exact congrArg some hvra
  have hlastr : (d.right.map ratVal).getLast? = some (T2 d) := by
    rw [List.getLast?_map, hrrb, Option.map_some]
    exact congrArg some hvrb
  have hpairsr : ∀ p ∈ consecPairs (d.right.map ratVal), p.1 < p.2 :=
    consec_map_forall fun q hq => chainLt_spec hchk.hdr hcr q hq
  obtain ⟨rta, hrta, hvta⟩ := firstOK_spec hft hchk.hdt hchk.hq2
  obtain ⟨rtb, hrtb, hvtb⟩ := lastOK_spec hchk.hq1 hlt' hchk.hdt
  have hheadt : (d.top.map ratVal).head? = some (sigma2 d) := by
    rw [List.head?_map, hrta, Option.map_some]
    exact congrArg some hvta
  have hlastt : (d.top.map ratVal).getLast? = some (sigma1 d) := by
    rw [List.getLast?_map, hrtb, Option.map_some]
    exact congrArg some hvtb
  have hpairst : ∀ p ∈ consecPairs (d.top.map ratVal), p.2 < p.1 :=
    consec_map_forall fun q hq => chainGt_spec hchk.hdt hct q hq
  obtain ⟨rla, hrla, hvla⟩ := firstOK_spec hfl hchk.hdl hchk.hb2
  obtain ⟨rlb, hrlb, hvlb⟩ := lastOK_spec hchk.hb1 hll hchk.hdl
  have hheadl : (d.left.map ratVal).head? = some (T2 d) := by
    rw [List.head?_map, hrla, Option.map_some]
    exact congrArg some hvla
  have hlastl : (d.left.map ratVal).getLast? = some (T1 d) := by
    rw [List.getLast?_map, hrlb, Option.map_some]
    exact congrArg some hvlb
  have hpairsl : ∀ p ∈ consecPairs (d.left.map ratVal), p.2 < p.1 :=
    consec_map_forall fun q hq => chainGt_spec hchk.hdl hclf q hq
  -- the four edges lie on ∂R ⊆ R ⊆ U, and f ≠ 0 there: the edge integrands are continuous
  have hmemB : ∀ t : ℝ, 0 ≤ t → t ≤ 1 →
      segPt (cpt (sigma1 d) (T1 d)) (cpt (sigma2 d) (T1 d)) t ∈ W1Bdry d :=
    fun t h0 h1 => bottom_seg_mem hs12.le hT12 t h0 h1
  have hmemR : ∀ t : ℝ, 0 ≤ t → t ≤ 1 →
      segPt (cpt (sigma2 d) (T1 d)) (cpt (sigma2 d) (T2 d)) t ∈ W1Bdry d :=
    fun t h0 h1 => right_seg_mem hs12.le hT12 t h0 h1
  have hmemT : ∀ t : ℝ, 0 ≤ t → t ≤ 1 →
      segPt (cpt (sigma2 d) (T2 d)) (cpt (sigma1 d) (T2 d)) t ∈ W1Bdry d :=
    fun t h0 h1 => top_seg_mem hs12.le hT12 t h0 h1
  have hmemL : ∀ t : ℝ, 0 ≤ t → t ≤ 1 →
      segPt (cpt (sigma1 d) (T2 d)) (cpt (sigma1 d) (T1 d)) t ∈ W1Bdry d :=
    fun t h0 h1 => left_seg_mem hs12.le hT12 t h0 h1
  have hcontB := continuousOn_logDeriv_seg hU hf (fun t h0 h1 => hRU (hmemB t h0 h1).1)
    (fun t h0 h1 => hbnz _ (hmemB t h0 h1))
  have hcontR := continuousOn_logDeriv_seg hU hf (fun t h0 h1 => hRU (hmemR t h0 h1).1)
    (fun t h0 h1 => hbnz _ (hmemR t h0 h1))
  have hcontT := continuousOn_logDeriv_seg hU hf (fun t h0 h1 => hRU (hmemT t h0 h1).1)
    (fun t h0 h1 => hbnz _ (hmemT t h0 h1))
  have hcontL := continuousOn_logDeriv_seg hU hf (fun t h0 h1 => hRU (hmemL t h0 h1).1)
    (fun t h0 h1 => hbnz _ (hmemL t h0 h1))
  -- the four edge sums (W1's L1 per edge)
  have hsumB : ((consecPairs (bottomPts d)).map
      fun p => logDerivSegIntegral f p.1 p.2).sum
      = logDerivSegIntegral f (cpt (sigma1 d) (T1 d)) (cpt (sigma2 d) (T1 d)) := by
    obtain ⟨hgh, hgl, hgle⟩ := tau_facts_inc hs12 hheadb hlastb hpairsb
    have hbp : bottomPts d = (d.bottom.map ratVal).map
        fun y => segPt (cpt (sigma1 d) (T1 d)) (cpt (sigma2 d) (T1 d))
          ((y - sigma1 d) / (sigma2 d - sigma1 d)) := by
      unfold bottomPts
      rw [List.map_map]
      exact map_congr_fn (fun r => (segPt_horiz_tau hs12.ne (T1 d) (ratVal r)).symm) d.bottom
    rw [hbp]
    exact edge_sum_eq _ _ hgh hgl hgle hcontB
  have hsumR : ((consecPairs (rightPts d)).map
      fun p => logDerivSegIntegral f p.1 p.2).sum
      = logDerivSegIntegral f (cpt (sigma2 d) (T1 d)) (cpt (sigma2 d) (T2 d)) := by
    obtain ⟨hgh, hgl, hgle⟩ := tau_facts_inc hT12 hheadr hlastr hpairsr
    have hbp : rightPts d = (d.right.map ratVal).map
        fun y => segPt (cpt (sigma2 d) (T1 d)) (cpt (sigma2 d) (T2 d))
          ((y - T1 d) / (T2 d - T1 d)) := by
      unfold rightPts
      rw [List.map_map]
      exact map_congr_fn (fun r => (segPt_vert_tau hT12.ne (sigma2 d) (ratVal r)).symm) d.right
    rw [hbp]
    exact edge_sum_eq _ _ hgh hgl hgle hcontR
  have hsumT : ((consecPairs (topPts d)).map
      fun p => logDerivSegIntegral f p.1 p.2).sum
      = logDerivSegIntegral f (cpt (sigma2 d) (T2 d)) (cpt (sigma1 d) (T2 d)) := by
    obtain ⟨hgh, hgl, hgle⟩ := tau_facts_dec hs12 hheadt hlastt hpairst
    have hbp : topPts d = (d.top.map ratVal).map
        fun y => segPt (cpt (sigma2 d) (T2 d)) (cpt (sigma1 d) (T2 d))
          ((y - sigma2 d) / (sigma1 d - sigma2 d)) := by
      unfold topPts
      rw [List.map_map]
      exact map_congr_fn (fun r => (segPt_horiz_tau hs12.ne' (T2 d) (ratVal r)).symm) d.top
    rw [hbp]
    exact edge_sum_eq _ _ hgh hgl hgle hcontT
  have hsumL : ((consecPairs (leftPts d)).map
      fun p => logDerivSegIntegral f p.1 p.2).sum
      = logDerivSegIntegral f (cpt (sigma1 d) (T2 d)) (cpt (sigma1 d) (T1 d)) := by
    obtain ⟨hgh, hgl, hgle⟩ := tau_facts_dec hT12 hheadl hlastl hpairsl
    have hbp : leftPts d = (d.left.map ratVal).map
        fun y => segPt (cpt (sigma1 d) (T2 d)) (cpt (sigma1 d) (T1 d))
          ((y - T2 d) / (T1 d - T2 d)) := by
      unfold leftPts
      rw [List.map_map]
      exact map_congr_fn (fun r => (segPt_vert_tau hT12.ne' (sigma1 d) (ratVal r)).symm) d.left
    rw [hbp]
    exact edge_sum_eq _ _ hgh hgl hgle hcontL
  -- the argument principle for f (L-B0)
  obtain ⟨Z, hZeq, hZ0, -⟩ := rectArgPrincipleGen f (sigma1 d) (sigma2 d) (T1 d) (T2 d)
    hs12 hT12 U hU hRU hf hbnz
  -- total winding: the segment sum equals 2πZ
  have hsegsum : ((segs d).map fun p => logDerivSegIntegral f p.1 p.2).sum
      = logDerivSegIntegral f (cpt (sigma1 d) (T1 d)) (cpt (sigma2 d) (T1 d))
        + logDerivSegIntegral f (cpt (sigma2 d) (T1 d)) (cpt (sigma2 d) (T2 d))
        + logDerivSegIntegral f (cpt (sigma2 d) (T2 d)) (cpt (sigma1 d) (T2 d))
        + logDerivSegIntegral f (cpt (sigma1 d) (T2 d)) (cpt (sigma1 d) (T1 d)) := by
    unfold segs
    rw [List.map_append, List.map_append, List.map_append, List.sum_append, List.sum_append,
      List.sum_append, hsumB, hsumR, hsumT, hsumL]
  have htot : ((segs d).map fun p => argIncrement f p.1 p.2).sum = 2 * π * Z := by
    have h1 : ((segs d).map fun p => argIncrement f p.1 p.2)
        = ((segs d).map fun p => logDerivSegIntegral f p.1 p.2).map Complex.im := by
      rw [List.map_map]
      rfl
    rw [h1, ← im_list_sum, hsegsum]
    simp only [Complex.add_im]
    exact hZeq.symm
  -- the winding enclosure pins Z = 0 (D4 with m = 0)
  obtain ⟨hlo, hhi⟩ := sum_arg_encl hEncl
  rw [htot] at hlo hhi
  have h2π : (2:ℝ) * π ≠ 0 := Real.two_pi_pos.ne'
  rw [mul_div_cancel_left₀ _ h2π] at hlo hhi
  have hloZ : sumArgLo d.rows ≤ d.A * (Z:ℤ) := by exact_mod_cast hlo
  have hhiZ : d.A * (Z:ℤ) ≤ sumArgHi d.rows := by exact_mod_cast hhi
  have hZ0' : (Z:ℤ) = 0 := pin_m (m := 0) hchk.hA hchk.hC8 (by rw [mul_zero]; exact hchk.hC9a)
    (by rw [mul_zero]; exact hchk.hC9b) hloZ hhiZ
  have hZ : Z = 0 := by exact_mod_cast hZ0'
  constructor
  · intro s hsmem
    by_cases hop : s ∈ rectOpen (sigma1 d) (sigma2 d) (T1 d) (T2 d)
    · exact hZ0 hZ s hop
    · exact hbnz s ⟨hsmem, hop⟩
  · rw [← hZeq, hZ]
    simp

/-! ## 9. D-B3: the boundary perturbation -/

/-- **D-B3.**  If |g − f| < |f| at a point then g ≠ 0 there and g/f lies in the open right
half-plane (|g/f − 1| < 1). -/
lemma re_div_pos_of_norm_sub_lt {a b : ℂ} (h : ‖a - b‖ < ‖b‖) : a ≠ 0 ∧ 0 < (a / b).re := by
  have hb : b ≠ 0 := by
    intro hb
    rw [hb, norm_zero] at h
    exact absurd h (not_lt.mpr (norm_nonneg _))
  have hbpos : 0 < ‖b‖ := norm_pos_iff.mpr hb
  constructor
  · intro ha
    rw [ha, zero_sub, norm_neg] at h
    exact lt_irrefl _ h
  · have h1 : ‖a / b - 1‖ < 1 := by
      rw [div_sub_one hb, norm_div, div_lt_one hbpos]
      exact h
    have h2 : |(a / b - 1).re| ≤ ‖a / b - 1‖ := Complex.abs_re_le_norm _
    have h3 : -(a / b - 1).re ≤ |(a / b - 1).re| := neg_le_abs _
    rw [Complex.sub_re, Complex.one_re] at h2 h3
    linarith

/-! ## 10. L-B2 (D-B5) and L-B1 (D-B6): the two segment identities -/

/-- **L-B2 (D-B5).**  Log-derivative additivity on a directed segment: for f, g holomorphic on an
open U containing the segment and both nonvanishing on it,
∫ g′/g = ∫ (g/f)′/(g/f) + ∫ f′/f.  Integrability is proved (continuity of the integrands). -/
lemma logDerivSegIntegral_div_add {f g : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hf : DifferentiableOn ℂ f U) (hg : DifferentiableOn ℂ g U) {z w : ℂ}
    (hseg : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → segPt z w t ∈ U)
    (hf0 : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → f (segPt z w t) ≠ 0)
    (hg0 : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → g (segPt z w t) ≠ 0) :
    logDerivSegIntegral g z w
      = logDerivSegIntegral (fun x => g x / f x) z w + logDerivSegIntegral f z w := by
  have hV : IsOpen (U ∩ f ⁻¹' {x | x ≠ 0}) :=
    hf.continuousOn.isOpen_inter_preimage hU isOpen_ne
  have hhV : DifferentiableOn ℂ (fun x => g x / f x) (U ∩ f ⁻¹' {x | x ≠ 0}) :=
    (hg.mono Set.inter_subset_left).div (hf.mono Set.inter_subset_left) fun x hx => hx.2
  have hsegV : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → segPt z w t ∈ U ∩ f ⁻¹' {x | x ≠ 0} :=
    fun t h0 h1 => ⟨hseg t h0 h1, hf0 t h0 h1⟩
  have hh0 : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → (fun x => g x / f x) (segPt z w t) ≠ 0 :=
    fun t h0 h1 => div_ne_zero (hg0 t h0 h1) (hf0 t h0 h1)
  have hcf := continuousOn_logDeriv_seg hU hf hseg hf0
  have hch := continuousOn_logDeriv_seg hV hhV hsegV hh0
  have hIf : IntervalIntegrable
      (fun t : ℝ => (deriv f (segPt z w t) / f (segPt z w t)) * (w - z)) volume 0 1 :=
    hcf.intervalIntegrable_of_Icc (by norm_num)
  have hIh : IntervalIntegrable
      (fun t : ℝ => (deriv (fun x => g x / f x) (segPt z w t)
        / (fun x => g x / f x) (segPt z w t)) * (w - z)) volume 0 1 :=
    hch.intervalIntegrable_of_Icc (by norm_num)
  unfold logDerivSegIntegral
  rw [← intervalIntegral.integral_add hIh hIf]
  apply intervalIntegral.integral_congr
  intro t ht
  rw [Set.uIcc_of_le (by norm_num : (0:ℝ) ≤ 1)] at ht
  obtain ⟨h0, h1⟩ := ht
  have hfd : DifferentiableAt ℂ f (segPt z w t) :=
    hf.differentiableAt (hU.mem_nhds (hseg t h0 h1))
  have hgd : DifferentiableAt ℂ g (segPt z w t) :=
    hg.differentiableAt (hU.mem_nhds (hseg t h0 h1))
  have hf0' := hf0 t h0 h1
  have hg0' := hg0 t h0 h1
  have hdh : deriv (fun x => g x / f x) (segPt z w t)
      = (deriv g (segPt z w t) * f (segPt z w t) - g (segPt z w t) * deriv f (segPt z w t))
        / f (segPt z w t) ^ 2 :=
    (hgd.hasDerivAt.div hfd.hasDerivAt hf0').deriv
  show (deriv g (segPt z w t) / g (segPt z w t)) * (w - z)
      = (deriv (fun x => g x / f x) (segPt z w t) / (g (segPt z w t) / f (segPt z w t)))
          * (w - z)
        + (deriv f (segPt z w t) / f (segPt z w t)) * (w - z)
  rw [hdh]
  field_simp
  ring

/-- **L-B1 (D-B6), the half-plane lemma — the one new analytic lemma of Lane B.**  If h is
holomorphic on an open U containing the directed segment z → w and Re h > 0 on the segment, then
∫₀¹ (h′/h)(γ(s))·γ′(s) ds = Log h(w) − Log h(z) for the principal `Complex.log`: s ↦ Log h(γ(s)) is
differentiable on [0,1] with that derivative (chain rule; `Complex.log` is differentiable on the
slit plane, which contains the right half-plane), and the fundamental theorem of calculus for the
interval integral applies (integrability from continuity). -/
lemma logDerivSegIntegral_eq_log_sub {h : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hh : DifferentiableOn ℂ h U) {z w : ℂ}
    (hseg : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → segPt z w t ∈ U)
    (hre : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → 0 < (h (segPt z w t)).re) :
    logDerivSegIntegral h z w = Complex.log (h w) - Complex.log (h z) := by
  have hne : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → h (segPt z w t) ≠ 0 := by
    intro t h0 h1 hz0
    have := hre t h0 h1
    rw [hz0] at this
    simp at this
  have hcont := continuousOn_logDeriv_seg hU hh hseg hne
  have hInt : IntervalIntegrable
      (fun t : ℝ => (deriv h (segPt z w t) / h (segPt z w t)) * (w - z)) volume 0 1 :=
    hcont.intervalIntegrable_of_Icc (by norm_num)
  have hγ : ∀ t : ℝ, HasDerivAt (fun s : ℝ => segPt z w s) (w - z) t := by
    intro t
    have h1 : HasDerivAt (fun s : ℝ => ((s : ℝ) : ℂ)) ((1 : ℝ) : ℂ) t :=
      (hasDerivAt_id t).ofReal_comp
    have h2 := (h1.mul_const (w - z)).const_add z
    simpa [segPt] using h2
  have hderiv : ∀ t ∈ Set.uIcc (0:ℝ) 1,
      HasDerivAt (fun s : ℝ => Complex.log (h (segPt z w s)))
        ((deriv h (segPt z w t) / h (segPt z w t)) * (w - z)) t := by
    intro t ht
    rw [Set.uIcc_of_le (by norm_num : (0:ℝ) ≤ 1)] at ht
    have hhd : HasDerivAt h (deriv h (segPt z w t)) (segPt z w t) :=
      (hh.differentiableAt (hU.mem_nhds (hseg t ht.1 ht.2))).hasDerivAt
    have hcomp := hhd.scomp t (hγ t)
    have hslit : (h ∘ fun s : ℝ => segPt z w s) t ∈ Complex.slitPlane :=
      Complex.mem_slitPlane_iff.mpr (Or.inl (hre t ht.1 ht.2))
    refine (hcomp.clog_real hslit).congr_deriv ?_
    simp only [smul_eq_mul, Function.comp_apply]
    ring
  unfold logDerivSegIntegral
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hInt, segPt_one, segPt_zero]

/-- the two identities combined on one edge whose points lie in a set S ⊆ W on which f ≠ 0,
g ≠ 0 and Re(g/f) > 0:  ∫ g′/g = (Log(g/f)(w) − Log(g/f)(z)) + ∫ f′/f. -/
lemma edge_decomp {f g : ℂ → ℂ} {W : Set ℂ} (hW : IsOpen W) (hf : DifferentiableOn ℂ f W)
    (hg : DifferentiableOn ℂ g W) {z w : ℂ} {S : Set ℂ} (hSW : S ⊆ W)
    (hf0 : ∀ x ∈ S, f x ≠ 0) (hg0 : ∀ x ∈ S, g x ≠ 0 ∧ 0 < (g x / f x).re)
    (hseg : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → segPt z w t ∈ S) :
    logDerivSegIntegral g z w
      = (Complex.log (g w / f w) - Complex.log (g z / f z)) + logDerivSegIntegral f z w := by
  have hsegW : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → segPt z w t ∈ W := fun t h0 h1 => hSW (hseg t h0 h1)
  have hf0' : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → f (segPt z w t) ≠ 0 :=
    fun t h0 h1 => hf0 _ (hseg t h0 h1)
  have hg0' : ∀ t : ℝ, 0 ≤ t → t ≤ 1 → g (segPt z w t) ≠ 0 :=
    fun t h0 h1 => (hg0 _ (hseg t h0 h1)).1
  rw [logDerivSegIntegral_div_add hW hf hg hsegW hf0' hg0']
  congr 1
  have hW' : IsOpen (W ∩ f ⁻¹' {x | x ≠ 0}) :=
    hf.continuousOn.isOpen_inter_preimage hW isOpen_ne
  have hh : DifferentiableOn ℂ (fun x => g x / f x) (W ∩ f ⁻¹' {x | x ≠ 0}) :=
    (hg.mono Set.inter_subset_left).div (hf.mono Set.inter_subset_left) fun x hx => hx.2
  exact logDerivSegIntegral_eq_log_sub hW' hh (fun t h0 h1 => ⟨hsegW t h0 h1, hf0' t h0 h1⟩)
    (fun t h0 h1 => (hg0 _ (hseg t h0 h1)).2)

/-! ## 11. D-B8: one prism, one time -/

/-- **D-B8 (one prism, one time).**  For an accepted prism (`checkPrism r p`), a holomorphic f on
an open U ⊇ R enclosed by the seam rows, a holomorphic g on an open V ⊇ R, and the perturbation
bound ‖g − f‖ ≤ (E + D)/K on ∂R: g ≠ 0 on the closed rectangle R.  The chain: D-B1 (f ≠ 0 on R,
four-edge winding of f = 0) → D-B2 (floor) → C-B12 → D-B3 (g ≠ 0 and Re(g/f) > 0 on ∂R) →
L-B2 + L-B1 on the four edges → D-B7 (`ring`) → the argument principle for g (L-B0) pins its
winding to 0 → g ≠ 0 on R° ∪ ∂R. -/
theorem prism_nonvanishing {f g : ℂ → ℂ} (r : RectData) (p : PrismData)
    (hc : checkPrism r p = true) (hEncl : W1EnclOK f (toW1 r p))
    {U V : Set ℂ} (hU : IsOpen U) (hRU : RectClosedOf r ⊆ U) (hf : DifferentiableOn ℂ f U)
    (hV : IsOpen V) (hRV : RectClosedOf r ⊆ V) (hg : DifferentiableOn ℂ g V)
    (hpert : ∀ z ∈ RectBdryOf r, ‖g z - f z‖ ≤ ((p.E : ℝ) + p.D) / p.K) :
    ∀ z ∈ RectClosedOf r, g z ≠ 0 := by
  obtain ⟨hc1, -, -, hFn, hFd, hrows, -, -, hC12⟩ := checkPrism_spec hc
  have hchk := meshOK_of_checkPrismW1 hc1
  have hs12 : r.x1 < r.x2 :=
    ratVal_lt_of_cross (r := (r.xn1, r.xd1)) (s := (r.xn2, r.xd2)) hchk.hq1 hchk.hq2 hchk.hC2x
  have hT12 : r.y1 < r.y2 :=
    ratVal_lt_of_cross (r := (r.yn1, r.yd1)) (s := (r.yn2, r.yd2)) hchk.hb1 hchk.hb2 hchk.hC2y
  -- D-B1: the seam exclusion for f
  obtain ⟨hf0, hfsum⟩ := exclusion_of_checkPrismW1 (toW1 r p) hc1 hEncl hU hRU hf
  simp only [sigma1_toW1, sigma2_toW1, T1_toW1, T2_toW1] at hfsum
  -- D-B2: the floor
  have hfloor : ∀ z ∈ RectBdryOf r, (p.Fn : ℝ) / p.Fd ≤ ‖f z‖ :=
    floor_of_meshOK hchk hEncl hFn hFd hrows
  -- C-B12 at the real level: (E + D)/K < Fn/Fd
  have hKpos : (0 : ℝ) < p.K := by
    have : (1 : ℝ) ≤ p.K := by exact_mod_cast hchk.hK
    linarith
  have hFdpos : (0 : ℝ) < p.Fd := by
    have : (1 : ℝ) ≤ p.Fd := by exact_mod_cast hFd
    linarith
  have hC12' : ((p.E : ℝ) + p.D) / p.K < (p.Fn : ℝ) / p.Fd := by
    rw [div_lt_div_iff₀ hKpos hFdpos]
    exact_mod_cast hC12
  -- D-B3: on ∂R, ‖g − f‖ < ‖f‖, hence g ≠ 0 and Re(g/f) > 0
  have hgbd : ∀ z ∈ RectBdryOf r, g z ≠ 0 ∧ 0 < (g z / f z).re := fun z hz =>
    re_div_pos_of_norm_sub_lt (lt_of_le_of_lt (hpert z hz) (lt_of_lt_of_le hC12' (hfloor z hz)))
  -- D-B4: the open set W ⊇ R on which f, g and g/f are holomorphic and f ≠ 0
  have hW : IsOpen (V ∩ (U ∩ f ⁻¹' {x | x ≠ 0})) :=
    hV.inter (hf.continuousOn.isOpen_inter_preimage hU isOpen_ne)
  have hRW : RectClosedOf r ⊆ V ∩ (U ∩ f ⁻¹' {x | x ≠ 0}) :=
    fun z hz => ⟨hRV hz, hRU hz, hf0 z hz⟩
  have hfW : DifferentiableOn ℂ f (V ∩ (U ∩ f ⁻¹' {x | x ≠ 0})) := hf.mono fun x hx => hx.2.1
  have hgW : DifferentiableOn ℂ g (V ∩ (U ∩ f ⁻¹' {x | x ≠ 0})) := hg.mono fun x hx => hx.1
  have hSW : RectBdryOf r ⊆ V ∩ (U ∩ f ⁻¹' {x | x ≠ 0}) := fun z hz => hRW hz.1
  have hf0S : ∀ z ∈ RectBdryOf r, f z ≠ 0 := fun z hz => hf0 z hz.1
  -- L-B2 + L-B1 on the four edges (D-B5, D-B6)
  have hB := edge_decomp hW hfW hgW hSW hf0S hgbd (bottom_seg_mem hs12.le hT12)
  have hR := edge_decomp hW hfW hgW hSW hf0S hgbd (right_seg_mem hs12.le hT12)
  have hT := edge_decomp hW hfW hgW hSW hf0S hgbd (top_seg_mem hs12.le hT12)
  have hL := edge_decomp hW hfW hgW hSW hf0S hgbd (left_seg_mem hs12.le hT12)
  -- the argument principle for g (L-B0), and D-B7 (the Logs telescope)
  obtain ⟨Z, hZeq, hZ0, -⟩ := rectArgPrincipleGen g r.x1 r.x2 r.y1 r.y2 hs12 hT12 V hV hRV hg
    (fun z hz => (hgbd z hz).1)
  have hsum0 : (2 : ℝ) * π * Z = 0 := by
    rw [hZeq]
    simp only [argIncrement] at hfsum ⊢
    rw [hB, hR, hT, hL]
    simp only [Complex.add_im, Complex.sub_im]
    linarith
  have hZ : Z = 0 := by
    have hZr : (Z : ℝ) = 0 := by
      rcases mul_eq_zero.mp hsum0 with h | h
      · exact absurd h Real.two_pi_pos.ne'
      · exact h
    exact_mod_cast hZr
  intro z hz
  by_cases hop : z ∈ rectOpen r.x1 r.x2 r.y1 r.y2
  · exact hZ0 hZ z hop
  · exact (hgbd z ⟨hz, hop⟩).1

/-! ## 12. L-B4 (D-B9): coverage in t, and the soundness theorem -/

/-- **L-B4 (D-B9).**  A `Forall₂` relation between the prisms p :: ps and their right endpoints
(the later seams, then τ′) yields, for every t with seamTime p ≤ t ≤ τ′, a prism q in the list and
its right endpoint τ″ with P q τ″ and seamTime q ≤ t ≤ τ″.  Pure list induction: C-B13's
monotonicity is a reject-more check (it keeps the chain honest), not a soundness input. -/
lemma cover_prisms (P : PrismData → ℝ → Prop) (τ' : ℝ) :
    ∀ (p : PrismData) (ps : List PrismData),
      List.Forall₂ P (p :: ps) (ps.map seamTime ++ [τ']) →
      ∀ t : ℝ, seamTime p ≤ t → t ≤ τ' →
      ∃ q ∈ p :: ps, ∃ τ'' : ℝ, P q τ'' ∧ seamTime q ≤ t ∧ t ≤ τ'' := by
  intro p ps
  induction ps generalizing p with
  | nil =>
    intro hF t hpt htτ
    simp only [List.map_nil, List.nil_append, List.forall₂_cons] at hF
    exact ⟨p, by simp, τ', hF.1, hpt, htτ⟩
  | cons q qs ih =>
    intro hF t hpt htτ
    simp only [List.map_cons, List.cons_append, List.forall₂_cons] at hF
    obtain ⟨hP, hF'⟩ := hF
    by_cases hq : t ≤ seamTime q
    · exact ⟨p, by simp, seamTime q, hP, hpt, hq⟩
    · rw [not_le] at hq
      obtain ⟨q', hq', τ'', hP', h1, h2⟩ := ih q hF' t hq.le htτ
      exact ⟨q', List.mem_cons_of_mem p hq', τ'', hP', h1, h2⟩

/-- the first seam is 0 (C-B13's `firstOK (0,1)`): for the head prism, `seamTime p = 0`. -/
lemma seamTime_head_eq_zero {p : PrismData} {ps : List PrismData}
    (hfirst : firstOK (0, 1) ((p :: ps).map fun q => (q.tn, q.td)) = true) :
    seamTime p = 0 := by
  simp only [List.map_cons, firstOK, ratEqB, decide_eq_true_eq] at hfirst
  have htn : p.tn = 0 := by omega
  simp [seamTime, htn]

/-- **Lane B soundness** (SPEC §8.3; proof plan §4.6 D-B1…D-B9).  Modulo the displayed
hypotheses H2-B (`BarrierEnclOK G d`) and `hHol` (G t holomorphic near R for t ∈ [0, t₀]), an
accepted barrier certificate — the global chain check `hchain` and the per-prism checks `hprisms`
(split so that per-prism kernel facts can live in per-prism modules, SPEC §7.6) — certifies
that G t has no zero in the closed rectangle R for any t ∈ [0, t₀].  For the instance,
G t z = Ht t z / Bt t z, and `cert_of_checkBarrier_xy` below gives the coordinate form. -/
theorem cert_of_checkBarrier (G : ℝ → ℂ → ℂ) (d : BarrierData)
    (hchain : checkBarrierChain d = true)
    (hprisms : ∀ p ∈ d.prisms, checkPrism d.rect p = true)
    (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 d →
      ∃ U : Set ℂ, IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ (G t) U)
    (hEncl : BarrierEnclOK G d) :
    ∀ t : ℝ, 0 ≤ t → t ≤ t0 d → ∀ z ∈ BarrierRect d, G t z ≠ 0 := by
  intro t ht0 ht1
  obtain ⟨-, -, -, -, -, -, -, -, -, -, hfirst, -⟩ := checkBarrierChain_spec hchain
  unfold BarrierEnclOK nextSeams at hEncl
  unfold seams at hfirst
  rcases hp : d.prisms with _ | ⟨p, ps⟩
  · rw [hp] at hfirst
    simp [firstOK] at hfirst
  · rw [hp] at hEncl hfirst
    have hseam0 : seamTime p = 0 := seamTime_head_eq_zero hfirst
    have hF : List.Forall₂ (PrismEnclOK G d) (p :: ps) (ps.map seamTime ++ [t0 d]) := hEncl
    obtain ⟨q, hq, τ'', hP, hq1, hq2⟩ :=
      cover_prisms (PrismEnclOK G d) (t0 d) p ps hF t (by rw [hseam0]; exact ht0) ht1
    have hqmem : q ∈ d.prisms := by rw [hp]; exact hq
    have hcq := hprisms q hqmem
    obtain ⟨U, f, hU, hRU, hf, hrows, hE, hD⟩ := hP
    obtain ⟨V, hV, hRV, hg⟩ := hHol t ht0 ht1
    have hpert : ∀ z ∈ BarrierBdry d, ‖G t z - f z‖ ≤ ((q.E : ℝ) + q.D) / q.K := by
      intro z hz
      calc ‖G t z - f z‖
          = ‖(G t z - G (seamTime q) z) + (G (seamTime q) z - f z)‖ := by
            congr 1
            ring
        _ ≤ ‖G t z - G (seamTime q) z‖ + ‖G (seamTime q) z - f z‖ := norm_add_le _ _
        _ ≤ (q.D : ℝ) / q.K + (q.E : ℝ) / q.K := add_le_add (hD t hq1 hq2 z hz) (hE z hz)
        _ = ((q.E : ℝ) + q.D) / q.K := by ring
    exact prism_nonvanishing d.rect q hcq hrows hU hRU hf hV hRV hg hpert

/-- **The conclusion in the coordinate form `Polymath15Bridge`'s hypothesis (iii) consumes.**
For H = G·B (instance: H = Ht, B = Bt, G = Ht/Bt): if the checker accepts and the displayed
hypotheses hold for G = H/B, then H t (x + iy) ≠ 0 for x₁ ≤ x ≤ x₂, y₁ ≤ y ≤ y₂, 0 ≤ t ≤ t₀.
(No nonvanishing of B is needed for THIS direction: H = 0 forces H/B = 0.  B ≠ 0 near R is what
discharges `hHol` from the entirety of H in the instance, L-B3.) -/
theorem cert_of_checkBarrier_xy (H B : ℝ → ℂ → ℂ) (d : BarrierData)
    (hchain : checkBarrierChain d = true)
    (hprisms : ∀ p ∈ d.prisms, checkPrism d.rect p = true)
    (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 d →
      ∃ U : Set ℂ, IsOpen U ∧ BarrierRect d ⊆ U
        ∧ DifferentiableOn ℂ (fun z => H t z / B t z) U)
    (hEncl : BarrierEnclOK (fun t z => H t z / B t z) d) :
    ∀ x y : ℝ, d.rect.x1 ≤ x → x ≤ d.rect.x2 → d.rect.y1 ≤ y → y ≤ d.rect.y2 →
      ∀ t : ℝ, 0 ≤ t → t ≤ t0 d → H t (x + y * I) ≠ 0 := by
  intro x y hx1 hx2 hy1 hy2 t ht0 ht1 hH
  have hmem : (x + y * I : ℂ) ∈ BarrierRect d := by
    simp only [BarrierRect, RectClosedOf, rectClosed, Set.mem_ofPred_eq, Complex.add_re,
      Complex.add_im, Complex.ofReal_re, Complex.ofReal_im, Complex.mul_I_re, Complex.mul_I_im]
    refine ⟨?_, ?_, ?_, ?_⟩ <;> linarith
  have := cert_of_checkBarrier (fun t z => H t z / B t z) d hchain hprisms hHol hEncl t ht0 ht1
    _ hmem
  apply this
  simp [hH]

end DBN
end Zeta23

end
