/- SCRATCH type-check of the M2a barrier-certificate contract's Lean shapes (SPEC.md §§3,7,8).
   Not a program file.  `sorry` appears ONLY in theorem statements used to fix the shapes. -/
import Zeta23.DBN.Defs
import Zeta23.W1.Soundness

open scoped Real
open Complex (I)

noncomputable section

namespace Zeta23
namespace DBN
namespace M2aScratch

/-! ## A. Trusted-layer additions proposed for Defs.lean v1.1 (SPEC §3.4, §3.6) -/

/-- α(s) = 1/(2s) + 1/(s−1) + ½·Log(s/(2π))   (Polymath15 eq. (9), second line, p4). -/
def alpha (s : ℂ) : ℂ := 1 / (2 * s) + 1 / (s - 1) + (1 / 2 : ℂ) * Complex.log (s / (2 * π))

/-- M₀(s) = ⅛ · s(s−1)/2 · π^{−s/2} · √(2π) · exp((s/2 − ½)·Log(s/2) − s/2)   (eq. (6), p4). -/
def M0 (s : ℂ) : ℂ :=
  (1 / 8 : ℂ) * (s * (s - 1) / 2) * (π : ℂ) ^ (-s / 2) * (Real.sqrt (2 * π) : ℂ)
    * Complex.exp ((s / 2 - 1 / 2) * Complex.log (s / 2) - s / 2)

/-- M_t(s) = exp(t/4 · α(s)²) · M₀(s)   (eq. (10), p4). -/
def Mt (t : ℝ) (s : ℂ) : ℂ := Complex.exp ((t : ℂ) / 4 * alpha s ^ 2) * M0 s

/-- B_t(z) = M_t((1 + y − ix)/2) for z = x + iy, i.e. M_t((1 − iz)/2)   (eq. (11), p4). -/
def Bt (t : ℝ) (z : ℂ) : ℂ := Mt t ((1 - I * z) / 2)

/-- the entirety of every H_t (analytic-package component of H3; SPEC §3.6). -/
def HtEntire : Prop := ∀ t : ℝ, Differentiable ℂ (Ht t)

/-- **Amended (H3)**: Polymath15 Theorem 1.2 with hypothesis (ii) at the FINAL time only and the
simplified barrier box for (iii) — the instantiable form (SPEC §3.2; replaces the merged canopy
of `Polymath15Bridge`, which quantifies (ii) over all t ∈ [0, t₀] and is not dischargeable). -/
def Polymath15Bridge' : Prop :=
  ∀ t₀ X y₀ : ℝ, 0 < t₀ → 0 < X → 0 < y₀ → y₀ ≤ 1 →
    ZeroVerification ((1 + y₀) / 2) (X / 2) →
    (∀ x y : ℝ, X + 1 ≤ x → y₀ ≤ y → y ^ 2 ≤ 1 - 2 * t₀ →
        Ht t₀ (x + y * I) ≠ 0) →
    (∀ x y : ℝ, X ≤ x → x ≤ X + 1 → y₀ ≤ y → y ≤ 1 → ∀ t : ℝ, 0 ≤ t → t ≤ t₀ →
        Ht t (x + y * I) ≠ 0) →
    ∀ t : ℝ, t₀ + y₀ ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0

/-! ## B. Barrier-lane data (SPEC §7.1) -/

/-- one time prism: seam time τ = tn/td (its left endpoint), the seam transcript (W1 exclusion
rows for the approximant f at time τ on the common rectangle), the floor |f| ≥ Fn/Fd on ∂R,
the approximation defect E (|g_τ − f| ≤ E/K on ∂R) and the displacement D
(|g_t − g_τ| ≤ D/K on ∂R for τ ≤ t ≤ τ⁺). -/
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

/-- the barrier certificate: the rectangle, the final time t₀, the prisms in time order. -/
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

def seams (d : BarrierData) : List (ℤ × ℤ) := d.prisms.map fun p => (p.tn, p.td)

/-! ### the checker (SPEC §7.3) -/

/-- W1's C1, C3–C9 with C2 replaced by C2′ (x₁ < x₂, y₁ < y₂ — no strip constraint) and
C10 replaced by m = 0. -/
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

/-- per-prism check: the seam exclusion transcript, the floor (C11), and the prism gate
C12: (E + D)·Fd < Fn·K, i.e. E/K + D/K < Fn/Fd. -/
def checkPrism (r : RectData) (p : PrismData) : Bool :=
  checkPrismW1 (toW1 r p)
    && decide (1 ≤ p.td) && decide (0 ≤ p.tn)
    && decide (0 ≤ p.Fn) && decide (1 ≤ p.Fd) && W1.floorRowsOK p.K p.Fn p.Fd p.rows
    && decide (0 ≤ p.E) && decide (0 ≤ p.D) && decide ((p.E + p.D) * p.Fd < p.Fn * p.K)

/-- the global chain: denominators, y₁ > 0, t₀ > 0, seams start at 0 and increase, last seam < t₀. -/
def checkBarrierChain (d : BarrierData) : Bool :=
  decide (1 ≤ d.rect.xd1) && decide (1 ≤ d.rect.xd2) && decide (1 ≤ d.rect.yd1)
    && decide (1 ≤ d.rect.yd2) && decide (1 ≤ d.t0d) && decide (0 < d.rect.yn1) && decide (0 < d.t0n)
    -- C-B2′: x₁ < x₂ and y₁ < y₂ (also re-checked per prism through `checkPrismW1`)
    && decide (d.rect.xn1 * d.rect.xd2 < d.rect.xn2 * d.rect.xd1)
    && decide (d.rect.yn1 * d.rect.yd2 < d.rect.yn2 * d.rect.yd1)
    && W1.densPos (seams d) && W1.firstOK (0, 1) (seams d)
    && W1.chainLt (seams d ++ [(d.t0n, d.t0d)])

/-- the monolithic checker (equivalent to the chain check plus every prism check). -/
def checkBarrier (d : BarrierData) : Bool :=
  checkBarrierChain d && d.prisms.all (checkPrism d.rect)

/-! ### the displayed hypothesis (SPEC §8.1) -/

def seamTime (p : PrismData) : ℝ := (p.tn : ℝ) / p.td
def t0 (d : BarrierData) : ℝ := (d.t0n : ℝ) / d.t0d
def RectClosedOf (r : RectData) : Set ℂ :=
  W1.rectClosed ((r.xn1 : ℝ) / r.xd1) ((r.xn2 : ℝ) / r.xd2) ((r.yn1 : ℝ) / r.yd1) ((r.yn2 : ℝ) / r.yd2)
def RectBdryOf (r : RectData) : Set ℂ :=
  W1.rectBdry ((r.xn1 : ℝ) / r.xd1) ((r.xn2 : ℝ) / r.xd2) ((r.yn1 : ℝ) / r.yd1) ((r.yn2 : ℝ) / r.yd2)
def BarrierRect (d : BarrierData) : Set ℂ := RectClosedOf d.rect
def BarrierBdry (d : BarrierData) : Set ℂ := RectBdryOf d.rect

/-- the right endpoints of the prisms: the next seam, or t₀ for the last prism. -/
def nextSeams (d : BarrierData) : List ℝ := (d.prisms.tail.map seamTime) ++ [t0 d]

/-- H2-B for one prism [τ, τ⁺]: some holomorphic approximant f on an open U ⊇ R is enclosed by
the seam rows (W1's H-ENCL, verbatim), approximates G_τ on ∂R to E/K, and G moves by at most
D/K on ∂R during the prism. -/
def PrismEnclOK (G : ℝ → ℂ → ℂ) (d : BarrierData) (p : PrismData) (τ' : ℝ) : Prop :=
  ∃ (U : Set ℂ) (f : ℂ → ℂ), IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ f U ∧
    List.Forall₂ (W1.RowEnclOK f p.K p.A) p.rows (W1.segs (toW1 d.rect p)) ∧
    (∀ z ∈ BarrierBdry d, ‖G (seamTime p) z - f z‖ ≤ (p.E : ℝ) / p.K) ∧
    (∀ t : ℝ, seamTime p ≤ t → t ≤ τ' →
      ∀ z ∈ BarrierBdry d, ‖G t z - G (seamTime p) z‖ ≤ (p.D : ℝ) / p.K)

/-- **H2-B** (barrier enclosure hypothesis), for the normalized family G. -/
def BarrierEnclOK (G : ℝ → ℂ → ℂ) (d : BarrierData) : Prop :=
  List.Forall₂ (PrismEnclOK G d) d.prisms (nextSeams d)

/-- the generic barrier soundness theorem (statement only here; SPEC §8.3, Lean item (b)). -/
theorem cert_of_checkBarrier (G : ℝ → ℂ → ℂ) (d : BarrierData)
    (hchain : checkBarrierChain d = true)
    (hprisms : ∀ p ∈ d.prisms, checkPrism d.rect p = true)
    (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 d →
      ∃ U : Set ℂ, IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ (G t) U)
    (hEncl : BarrierEnclOK G d) :
    ∀ t : ℝ, 0 ≤ t → t ≤ t0 d → ∀ z ∈ BarrierRect d, G t z ≠ 0 := by
  sorry

/-! ## C. Asymptotic-lane data (SPEC §7.2) -/

/-- the Riemann–Siegel window index N(x) = ⌊√(x/(4π) + t/16)⌋   (Polymath15 eq. (19), p6). -/
def windowIdx (t x : ℝ) : ℕ := ⌊Real.sqrt (x / (4 * π) + t / 16)⌋₊

/-- one window row: for N(x) ∈ [Nlo, Nhi] and y ∈ [y₀, yA], |f_{t₀}| ≥ T/K and the Theorem-1.3
defect is ≤ E/K, hence |g_{t₀}| ≥ (T − E)/K. -/
structure AsymRow where
  Nlo : ℤ
  Nhi : ℤ
  T : ℤ
  E : ℤ

/-- the Lemma-T tail row (SPEC §5.4): integer upper bounds, at scale K, of the five finite
quantities whose sum must stay below 2. -/
structure TailRow where
  N1 : ℤ
  Q1 : ℤ
  Q2 : ℤ
  Q3 : ℤ
  Q4 : ℤ
  E1 : ℤ

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

def checkAsymRow (r : AsymRow) : Bool :=
  decide (r.Nlo ≤ r.Nhi) && decide (0 ≤ r.E) && decide (r.E < r.T)

def consecutive : List AsymRow → Bool
  | [] => true
  | [_] => true
  | r :: s :: l => decide (s.Nlo = r.Nhi + 1) && consecutive (s :: l)

def lastNhi : List AsymRow → ℤ
  | [] => 0
  | [r] => r.Nhi
  | _ :: s :: l => lastNhi (s :: l)

def checkAsym (d : AsymData) : Bool :=
  decide (1 ≤ d.K) && decide (1 ≤ d.t0d) && decide (0 < d.t0n) && decide (1 ≤ d.y0d)
    && decide (0 < d.y0n) && decide (1 ≤ d.yAd) && decide (0 ≤ d.yAn)
    -- yA² ≥ 1 − 2t₀  ⟺  yAn²·t0d ≥ (t0d − 2·t0n)·yAd²
    && decide ((d.t0d - 2 * d.t0n) * d.yAd ^ 2 ≤ d.yAn ^ 2 * d.t0d)
    && decide (0 < d.rows.length)
    && d.rows.all checkAsymRow && consecutive d.rows
    && decide (d.tail.N1 = lastNhi d.rows + 1)
    && decide (0 ≤ d.tail.Q1) && decide (0 ≤ d.tail.Q2) && decide (0 ≤ d.tail.Q3)
    && decide (0 ≤ d.tail.Q4) && decide (0 ≤ d.tail.E1)
    && decide (d.tail.Q1 + d.tail.Q2 + d.tail.Q3 + d.tail.Q4 + d.tail.E1 < 2 * d.K)

def At0 (d : AsymData) : ℝ := (d.t0n : ℝ) / d.t0d
def Ay0 (d : AsymData) : ℝ := (d.y0n : ℝ) / d.y0d
def AyA (d : AsymData) : ℝ := (d.yAn : ℝ) / d.yAd

/-- **H2-A**: every window row's floor holds for the normalized function at time t₀. -/
def AsymEnclOK (g : ℂ → ℂ) (d : AsymData) : Prop :=
  ∀ r ∈ d.rows, ∀ x y : ℝ, (r.Nlo : ℝ) ≤ windowIdx (At0 d) x → (windowIdx (At0 d) x : ℝ) ≤ r.Nhi →
    Ay0 d ≤ y → y ≤ AyA d → ((r.T : ℝ) - r.E) / d.K ≤ ‖g (x + y * I)‖

/-- **H-TAIL** (displayed, conclusion form): nonvanishing beyond the last window. -/
def TailOK (g : ℂ → ℂ) (d : AsymData) : Prop :=
  ∀ x y : ℝ, (d.tail.N1 : ℝ) ≤ windowIdx (At0 d) x → Ay0 d ≤ y → y ≤ AyA d → g (x + y * I) ≠ 0

theorem cert_of_checkAsym (g : ℂ → ℂ) (d : AsymData) (hc : checkAsym d = true)
    (hEncl : AsymEnclOK g d) (hTail : TailOK g d) :
    ∀ x y : ℝ, ∀ r ∈ d.rows, (r.Nlo : ℝ) ≤ windowIdx (At0 d) x →
      Ay0 d ≤ y → y ≤ AyA d → g (x + y * I) ≠ 0 := by
  sorry

/-! ## D. The instance theorem shape (SPEC §9), row 2 -/

/-- the normalized family g_t = H_t / B_t. -/
def G (t : ℝ) (z : ℂ) : ℂ := Ht t z / Bt t z

structure Row2Cert where
  barrier : BarrierData
  asym : AsymData

/-- H2 for the instance: the barrier enclosures for G, the window enclosures and the tail at t₀. -/
def M2aEnclOK (c : Row2Cert) : Prop :=
  BarrierEnclOK G c.barrier ∧ AsymEnclOK (G (At0 c.asym)) c.asym ∧ TailOK (G (At0 c.asym)) c.asym

theorem lambda_le_point2_shape (c : Row2Cert)
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hH2 : M2aEnclOK c)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  sorry

/-- arithmetic glue the instance file must discharge (exact rationals). -/
example : (186 / 1000 : ℝ) + (16733 / 100000 : ℝ) ^ 2 / 2 ≤ 1 / 5 := by norm_num
example : ((1 : ℝ) + 16733 / 100000) / 2 = 116733 / 200000 := by norm_num
example : ((5 * 10 ^ 12 + 194858 : ℝ)) / 2 = 2500000097429 := by norm_num
example : (2500000097429 : ℝ) ≤ 3000175332800 := by norm_num

end M2aScratch
end DBN
end Zeta23

/-! ## E. The SPEC §12 micro-example as kernel-checked checker instances (artificial data) -/
namespace Zeta23.DBN.M2aScratch

def exPrism0 : PrismData :=
  { tn := 0, td := 1, K := 100, A := 1000,
    bottom := [(10,1),(21,2),(11,1)], right := [(1,5),(3,5),(1,1)],
    top := [(11,1),(21,2),(10,1)], left := [(1,1),(3,5),(1,5)],
    rows := [⟨300,420,-60,60,-12,15⟩, ⟨310,430,-50,70,-10,14⟩, ⟨320,440,-40,80,-11,13⟩,
             ⟨330,450,-30,90,-13,12⟩, ⟨340,460,-20,100,-14,11⟩, ⟨330,450,-30,90,-12,16⟩,
             ⟨320,440,-40,80,-15,10⟩, ⟨310,430,-50,70,-9,17⟩],
    Fn := 5, Fd := 2, E := 20, D := 100 }

def exPrism1 : PrismData :=
  { tn := 1, td := 20, K := 100, A := 1000,
    bottom := [(10,1),(41,4),(43,4),(11,1)], right := [(1,5),(1,1)],
    top := [(11,1),(21,2),(10,1)], left := [(1,1),(1,5)],
    rows := [⟨-70,-40,250,330,-8,9⟩, ⟨-60,-30,260,340,-7,8⟩, ⟨-50,-20,270,350,-9,7⟩,
             ⟨-40,-10,280,360,-6,10⟩, ⟨-50,-20,270,350,-8,8⟩, ⟨-60,-30,260,340,-10,6⟩,
             ⟨-70,-40,250,330,-7,9⟩],
    Fn := 12, Fd := 5, E := 20, D := 150 }

def exRect : RectData :=
  { xn1 := 10, xd1 := 1, xn2 := 11, xd2 := 1, yn1 := 1, yd1 := 5, yn2 := 1, yd2 := 1 }

def exBarrier : BarrierData :=
  { rect := exRect, t0n := 1, t0d := 10, prisms := [exPrism0, exPrism1] }

theorem exBarrier_chain : checkBarrierChain exBarrier = true := by decide +kernel
theorem exPrism0_check : checkPrism exRect exPrism0 = true := by decide +kernel
theorem exPrism1_check : checkPrism exRect exPrism1 = true := by decide +kernel
theorem exBarrier_check : checkBarrier exBarrier = true := by decide +kernel

/-- negative control: C12 fails when D = 400 (E + D = 420; 420·2 = 840 ≥ 5·100). -/
theorem exPrism0_bad : checkPrism exRect { exPrism0 with D := 400 } = false := by decide +kernel
/-- the monolithic check follows from the chain check and the per-prism checks (the packaging
pattern of SPEC §7.6: per-prism facts proved in separate modules, assembled here). -/
theorem exBarrier_check' : checkBarrier exBarrier = true := by
  unfold checkBarrier
  rw [exBarrier_chain]
  show List.all [exPrism0, exPrism1] (checkPrism exRect) = true
  simp only [List.all_cons, List.all_nil, exPrism0_check, exPrism1_check, Bool.and_self]

def exAsym : AsymData :=
  { K := 1000, t0n := 1, t0d := 10, y0n := 1, y0d := 5, yAn := 9, yAd := 10,
    rows := [⟨5,5,400,30⟩, ⟨6,9,350,25⟩, ⟨10,20,300,20⟩],
    tail := ⟨21, 1500, 100, 50, 20, 5⟩ }

theorem exAsym_check : checkAsym exAsym = true := by decide +kernel
/-- negative control: yA = 8/10 has yA² = 0.64 < 1 − 2t₀ = 0.8, so C-A1 fails. -/
theorem exAsym_bad : checkAsym { exAsym with yAn := 8 } = false := by decide +kernel

end Zeta23.DBN.M2aScratch
