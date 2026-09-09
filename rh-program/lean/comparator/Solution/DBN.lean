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
comparator/Solution/DBN.lean — the UNTRUSTED comparator solution module for the topic `DBN`: the seven statements of
Challenge/DBN.lean, byte-identical, each PROVED by delegating to the program's Zeta23 additions
(Zeta23/DBN/{Defs,BarrierCert,Asym,BtFacts,Instance02}.lean and the emitted literal modules under Zeta23/DBN/Instance02/).

THE BRIDGE (namespace `DBNBridge`, nothing of it in the root namespace).  The challenge's nine definitions of the trusted
layer, `windowIdx`, and every helper `def` of ChallengeDeps.DBN are character-for-character Zeta23's, so each is
definitionally equal to its Zeta23 namesake (`rfl`: §1).  The challenge's STRUCTURES (`W1Row`, `W1Data`, `PrismData`,
`RectData`, `BarrierData`, `AsymRow`, `TailRow`, `AsymData`) are re-declared and therefore DISTINCT TYPES from Zeta23's, so
they are transported field-wise (`toZRow`, `toZPrism`, …; §2) and the checkers and enclosure Props are shown to commute with
the transport (§3, by induction on the row/mesh lists for the recursive helpers, `rfl` for the rest).  The trusted literal
copies transport to Zeta23's literals — decided by the kernel on the two copies (`decide +kernel`, no `native_decide`; §4).
(I) then delegates to Zeta23's `lambda_le_point2` / `lambda_le_point2_arb`; (K) to the emitted kernel facts; (G) to a NEW
generic lemma `ray_of_certificates` (§5) which repeats the proof of Zeta23's `row2_ray_mp` with the barrier and asymptotic
data generic under the constraints that proof actually uses — Zeta23 itself proves only the instance form (recorded as
fidelity divergence (f) in formalization.yaml / FIDELITY.md).

Nothing in this file is part of the trusted base: comparator re-checks that every root-namespace theorem below has exactly
the statement of its Challenge namesake and uses only the permitted axioms.  Label (SPEC §3.7): "kernel-checked modulo
H1, H2 (H2-B, H2-A, H-TAIL), H3" — never "fully machine-checked".
-/
import ChallengeDeps.DBN
import ChallengeDeps.DBN.Instance02
import Zeta23.DBN.Instance02

open DBN

noncomputable section

namespace DBNBridge

/-! ### 1. Definitions with identical bodies are definitionally equal -/

theorem Phi_eq : DBN.Phi = Zeta23.DBN.Phi := rfl
theorem Ht_eq : DBN.Ht = Zeta23.DBN.Ht := rfl
theorem ZeroVerification_eq : DBN.ZeroVerification = Zeta23.DBN.ZeroVerification := rfl
theorem alpha_eq : DBN.alpha = Zeta23.DBN.alpha := rfl
theorem M0_eq : DBN.M0 = Zeta23.DBN.M0 := rfl
theorem Mt_eq : DBN.Mt = Zeta23.DBN.Mt := rfl
theorem Bt_eq : DBN.Bt = Zeta23.DBN.Bt := rfl
theorem HtEntire_eq : DBN.HtEntire = Zeta23.DBN.HtEntire := rfl
theorem Polymath15Bridge'_eq : DBN.Polymath15Bridge' = Zeta23.DBN.Polymath15Bridge' := rfl
theorem windowIdx_eq : DBN.windowIdx = Zeta23.DBN.windowIdx := rfl

/-! ### 2. Transport of the re-declared structures (field-wise) -/

def toZRow (r : DBN.W1.W1Row) : Zeta23.W1.W1Row :=
  ⟨r.reLo, r.reHi, r.imLo, r.imHi, r.argLo, r.argHi⟩
def toZPrism (p : DBN.PrismData) : Zeta23.DBN.PrismData :=
  ⟨p.tn, p.td, p.K, p.A, p.bottom, p.right, p.top, p.left, p.rows.map toZRow, p.Fn, p.Fd, p.E, p.D⟩
def toZRect (r : DBN.RectData) : Zeta23.DBN.RectData :=
  ⟨r.xn1, r.xd1, r.xn2, r.xd2, r.yn1, r.yd1, r.yn2, r.yd2⟩
def toZBarrier (d : DBN.BarrierData) : Zeta23.DBN.BarrierData :=
  ⟨toZRect d.rect, d.t0n, d.t0d, d.prisms.map toZPrism⟩
def toZARow (r : DBN.AsymRow) : Zeta23.DBN.AsymRow := ⟨r.Nlo, r.Nhi, r.T, r.E⟩
def toZTail (r : DBN.TailRow) : Zeta23.DBN.TailRow := ⟨r.N1, r.Q1, r.Q2, r.Q3, r.Q4, r.E1⟩
def toZAsym (a : DBN.AsymData) : Zeta23.DBN.AsymData :=
  ⟨a.K, a.t0n, a.t0d, a.y0n, a.y0d, a.yAn, a.yAd, a.rows.map toZARow, toZTail a.tail⟩

/-! ### 3. The checkers and the enclosure Props commute with the transport -/

theorem densPos_eq : ∀ l : List (ℤ × ℤ), DBN.W1.densPos l = Zeta23.W1.densPos l
  | [] => rfl
  | r :: l => by simp [DBN.W1.densPos, Zeta23.W1.densPos, densPos_eq l]

theorem chainLt_eq : ∀ l : List (ℤ × ℤ), DBN.W1.chainLt l = Zeta23.W1.chainLt l
  | [] => rfl
  | [_] => rfl
  | r :: s :: l => by simp [DBN.W1.chainLt, Zeta23.W1.chainLt, chainLt_eq (s :: l)]

theorem chainGt_eq : ∀ l : List (ℤ × ℤ), DBN.W1.chainGt l = Zeta23.W1.chainGt l
  | [] => rfl
  | [_] => rfl
  | r :: s :: l => by simp [DBN.W1.chainGt, Zeta23.W1.chainGt, chainGt_eq (s :: l)]

theorem firstOK_eq (t : ℤ × ℤ) : ∀ l : List (ℤ × ℤ), DBN.W1.firstOK t l = Zeta23.W1.firstOK t l
  | [] => rfl
  | _ :: _ => rfl

theorem lastOK_eq (t : ℤ × ℤ) : ∀ l : List (ℤ × ℤ), DBN.W1.lastOK t l = Zeta23.W1.lastOK t l
  | [] => rfl
  | [_] => rfl
  | _ :: s :: l => by simp [DBN.W1.lastOK, Zeta23.W1.lastOK, lastOK_eq t (s :: l)]

theorem edgeOK_eq (a b : ℤ × ℤ) (inc : Bool) (l : List (ℤ × ℤ)) :
    DBN.W1.edgeOK a b inc l = Zeta23.W1.edgeOK a b inc l := by
  simp only [DBN.W1.edgeOK, Zeta23.W1.edgeOK, firstOK_eq, lastOK_eq, chainLt_eq, chainGt_eq]

theorem rowOK_eq (A : ℤ) (r : DBN.W1.W1Row) : DBN.W1.rowOK A r = Zeta23.W1.rowOK A (toZRow r) := rfl

theorem rowsOK_eq (A : ℤ) : ∀ l : List DBN.W1.W1Row, DBN.W1.rowsOK A l = Zeta23.W1.rowsOK A (l.map toZRow)
  | [] => rfl
  | r :: l => by simp [DBN.W1.rowsOK, Zeta23.W1.rowsOK, rowsOK_eq A l, rowOK_eq]

theorem sumArgLo_eq : ∀ l : List DBN.W1.W1Row, DBN.W1.sumArgLo l = Zeta23.W1.sumArgLo (l.map toZRow)
  | [] => rfl
  | r :: l => by simp [DBN.W1.sumArgLo, Zeta23.W1.sumArgLo, sumArgLo_eq l, toZRow]

theorem sumArgHi_eq : ∀ l : List DBN.W1.W1Row, DBN.W1.sumArgHi l = Zeta23.W1.sumArgHi (l.map toZRow)
  | [] => rfl
  | r :: l => by simp [DBN.W1.sumArgHi, Zeta23.W1.sumArgHi, sumArgHi_eq l, toZRow]

theorem mdist_eq (lo hi : ℤ) : DBN.W1.mdist lo hi = Zeta23.W1.mdist lo hi := rfl

theorem floorRowOK_eq (K Fn Fd : ℤ) (r : DBN.W1.W1Row) :
    DBN.W1.floorRowOK K Fn Fd r = Zeta23.W1.floorRowOK K Fn Fd (toZRow r) := rfl

theorem floorRowsOK_eq (K Fn Fd : ℤ) : ∀ l : List DBN.W1.W1Row,
    DBN.W1.floorRowsOK K Fn Fd l = Zeta23.W1.floorRowsOK K Fn Fd (l.map toZRow)
  | [] => rfl
  | r :: l => by simp [DBN.W1.floorRowsOK, Zeta23.W1.floorRowsOK, floorRowsOK_eq K Fn Fd l, floorRowOK_eq]

theorem consecPairs_eq {α : Type*} : ∀ l : List α, DBN.W1.consecPairs l = Zeta23.W1.consecPairs l
  | [] => rfl
  | [_] => rfl
  | x :: y :: l => by simp [DBN.W1.consecPairs, Zeta23.W1.consecPairs, consecPairs_eq (y :: l)]

theorem segs_eq (r : DBN.RectData) (p : DBN.PrismData) :
    DBN.W1.segs (DBN.toW1 r p) = Zeta23.W1.segs (Zeta23.DBN.toW1 (toZRect r) (toZPrism p)) := by
  simp only [DBN.W1.segs, Zeta23.W1.segs, consecPairs_eq]
  rfl

theorem checkPrismW1_eq (r : DBN.RectData) (p : DBN.PrismData) :
    DBN.checkPrismW1 (DBN.toW1 r p) = Zeta23.DBN.checkPrismW1 (Zeta23.DBN.toW1 (toZRect r) (toZPrism p)) := by
  simp only [DBN.checkPrismW1, Zeta23.DBN.checkPrismW1, DBN.toW1, Zeta23.DBN.toW1, toZRect, toZPrism, densPos_eq,
    edgeOK_eq, rowsOK_eq, sumArgLo_eq, sumArgHi_eq, List.length_map]
  rfl

theorem checkPrism_eq (r : DBN.RectData) (p : DBN.PrismData) :
    DBN.checkPrism r p = Zeta23.DBN.checkPrism (toZRect r) (toZPrism p) := by
  unfold DBN.checkPrism Zeta23.DBN.checkPrism
  rw [checkPrismW1_eq, floorRowsOK_eq]
  rfl

theorem seams_eq (d : DBN.BarrierData) : Zeta23.DBN.seams (toZBarrier d) = DBN.seams d := by
  simp only [Zeta23.DBN.seams, DBN.seams, toZBarrier, List.map_map]
  rfl

theorem checkBarrierChain_eq (d : DBN.BarrierData) :
    DBN.checkBarrierChain d = Zeta23.DBN.checkBarrierChain (toZBarrier d) := by
  unfold DBN.checkBarrierChain Zeta23.DBN.checkBarrierChain
  rw [seams_eq, densPos_eq, firstOK_eq, chainLt_eq]
  rfl

theorem checkBarrier_eq (d : DBN.BarrierData) : DBN.checkBarrier d = Zeta23.DBN.checkBarrier (toZBarrier d) := by
  unfold DBN.checkBarrier Zeta23.DBN.checkBarrier
  rw [checkBarrierChain_eq]
  have hp : (toZBarrier d).prisms = d.prisms.map toZPrism := rfl
  have hr : (toZBarrier d).rect = toZRect d.rect := rfl
  rw [hp, hr, List.all_map]
  have hc : Zeta23.DBN.checkPrism (toZRect d.rect) ∘ toZPrism = DBN.checkPrism d.rect :=
    funext fun p => (checkPrism_eq d.rect p).symm
  rw [hc]

theorem consecutive_eq : ∀ l : List DBN.AsymRow, DBN.consecutive l = Zeta23.DBN.consecutive (l.map toZARow)
  | [] => rfl
  | [_] => rfl
  | r :: s :: l => by simp [DBN.consecutive, Zeta23.DBN.consecutive, consecutive_eq (s :: l), toZARow]

theorem lastNhi_eq : ∀ l : List DBN.AsymRow, DBN.lastNhi l = Zeta23.DBN.lastNhi (l.map toZARow)
  | [] => rfl
  | [_] => rfl
  | _ :: s :: l => by simp [DBN.lastNhi, Zeta23.DBN.lastNhi, lastNhi_eq (s :: l)]

theorem checkAsymRow_eq (r : DBN.AsymRow) : DBN.checkAsymRow r = Zeta23.DBN.checkAsymRow (toZARow r) := rfl

theorem all_checkAsymRow_eq (l : List DBN.AsymRow) :
    l.all DBN.checkAsymRow = (l.map toZARow).all Zeta23.DBN.checkAsymRow := by
  rw [List.all_map]
  rfl

theorem checkAsym_eq (a : DBN.AsymData) : DBN.checkAsym a = Zeta23.DBN.checkAsym (toZAsym a) := by
  unfold DBN.checkAsym Zeta23.DBN.checkAsym
  have hr : (toZAsym a).rows = a.rows.map toZARow := rfl
  rw [hr, ← consecutive_eq, ← lastNhi_eq, ← all_checkAsymRow_eq, List.length_map]
  rfl

theorem BarrierRect_eq (d : DBN.BarrierData) : Zeta23.DBN.BarrierRect (toZBarrier d) = DBN.BarrierRect d := rfl
theorem BarrierBdry_eq (d : DBN.BarrierData) : Zeta23.DBN.BarrierBdry (toZBarrier d) = DBN.BarrierBdry d := rfl
theorem seamTime_eq (p : DBN.PrismData) : Zeta23.DBN.seamTime (toZPrism p) = DBN.seamTime p := rfl
theorem t0_eq (d : DBN.BarrierData) : Zeta23.DBN.t0 (toZBarrier d) = DBN.t0 d := rfl
theorem At0_eq (a : DBN.AsymData) : Zeta23.DBN.At0 (toZAsym a) = DBN.At0 a := rfl
theorem Ay0_eq (a : DBN.AsymData) : Zeta23.DBN.Ay0 (toZAsym a) = DBN.Ay0 a := rfl
theorem AyA_eq (a : DBN.AsymData) : Zeta23.DBN.AyA (toZAsym a) = DBN.AyA a := rfl

theorem nextSeams_eq (d : DBN.BarrierData) : Zeta23.DBN.nextSeams (toZBarrier d) = DBN.nextSeams d := by
  have hp : (toZBarrier d).prisms = d.prisms.map toZPrism := rfl
  simp only [Zeta23.DBN.nextSeams, DBN.nextSeams, hp, t0_eq, ← List.map_tail, List.map_map]
  rfl

theorem PrismEnclOK_iff (G : ℝ → ℂ → ℂ) (d : DBN.BarrierData) (p : DBN.PrismData) (τ : ℝ) :
    DBN.PrismEnclOK G d p τ ↔ Zeta23.DBN.PrismEnclOK G (toZBarrier d) (toZPrism p) τ := by
  unfold DBN.PrismEnclOK Zeta23.DBN.PrismEnclOK
  rw [BarrierRect_eq, BarrierBdry_eq, seamTime_eq]
  have hK : (toZPrism p).K = p.K := rfl
  have hA : (toZPrism p).A = p.A := rfl
  have hE : (toZPrism p).E = p.E := rfl
  have hD : (toZPrism p).D = p.D := rfl
  have hrows : (toZPrism p).rows = p.rows.map toZRow := rfl
  have hrect : (toZBarrier d).rect = toZRect d.rect := rfl
  rw [hK, hA, hE, hD, hrows, hrect]
  simp only [List.forall₂_map_left_iff, ← segs_eq]
  exact Iff.rfl

theorem BarrierEnclOK_iff (G : ℝ → ℂ → ℂ) (d : DBN.BarrierData) :
    DBN.BarrierEnclOK G d ↔ Zeta23.DBN.BarrierEnclOK G (toZBarrier d) := by
  unfold DBN.BarrierEnclOK Zeta23.DBN.BarrierEnclOK
  have hp : (toZBarrier d).prisms = d.prisms.map toZPrism := rfl
  rw [nextSeams_eq, hp, List.forall₂_map_left_iff]
  constructor
  · exact List.Forall₂.imp (fun p τ h => (PrismEnclOK_iff G d p τ).mp h)
  · exact List.Forall₂.imp (fun p τ h => (PrismEnclOK_iff G d p τ).mpr h)

theorem AsymEnclOK_iff (g : ℂ → ℂ) (a : DBN.AsymData) :
    DBN.AsymEnclOK g a ↔ Zeta23.DBN.AsymEnclOK g (toZAsym a) := by
  unfold DBN.AsymEnclOK Zeta23.DBN.AsymEnclOK
  have hr : (toZAsym a).rows = a.rows.map toZARow := rfl
  rw [hr, At0_eq, Ay0_eq, AyA_eq, List.forall_mem_map]
  exact Iff.rfl

theorem TailOK_iff (g : ℂ → ℂ) (a : DBN.AsymData) : DBN.TailOK g a ↔ Zeta23.DBN.TailOK g (toZAsym a) := by
  unfold DBN.TailOK Zeta23.DBN.TailOK
  rw [At0_eq, Ay0_eq, AyA_eq]
  exact Iff.rfl

/-! ### 4. The trusted literal copies transport to Zeta23's literals (decided by the kernel on the two copies) -/

deriving instance DecidableEq for Zeta23.W1.W1Row
deriving instance DecidableEq for Zeta23.DBN.RectData
deriving instance DecidableEq for Zeta23.DBN.PrismData
deriving instance DecidableEq for Zeta23.DBN.BarrierData
deriving instance DecidableEq for Zeta23.DBN.AsymRow
deriving instance DecidableEq for Zeta23.DBN.TailRow
deriving instance DecidableEq for Zeta23.DBN.AsymData

set_option maxRecDepth 100000

theorem row2Rect_toZ : toZRect DBN.row2Rect = Zeta23.DBN.Instance02.row2Rect := rfl
theorem row2BarrierMP_toZ : toZBarrier DBN.row2BarrierMP = Zeta23.DBN.Instance02.row2BarrierMP := by
  decide +kernel
theorem row2BarrierARB_toZ : toZBarrier DBN.row2BarrierARB = Zeta23.DBN.Instance02.row2BarrierARB := by
  decide +kernel
theorem row2AsymMP_toZ : toZAsym DBN.row2AsymMP = Zeta23.DBN.Instance02.row2AsymMP := by
  decide +kernel
theorem row2AsymARB_toZ : toZAsym DBN.row2AsymARB = Zeta23.DBN.Instance02.row2AsymARB := by
  decide +kernel

/-! ### 5. The generic ray statement in Zeta23's vocabulary — a NEW lemma (Zeta23 proves only the instance form):
the proof of `Zeta23.DBN.Instance02.row2_ray_mp` + `lambda_le_point2` with `d`, `a` generic under exactly the
constraints that proof uses (the rectangle's four reals, t₀, the checker facts; t₀, y₀, yA of the asymptotic data and a
row starting at or below N_start = 630783 for L-A1). -/

theorem ray_of_certificates (d : Zeta23.DBN.BarrierData)
    (hx1 : d.rect.x1 = 5000000194858) (hx2 : d.rect.x2 = 5000000194858 + 1)
    (hy1 : d.rect.y1 = 16733 / 100000) (hy2 : d.rect.y2 = 1) (ht0 : Zeta23.DBN.t0 d = 93 / 500)
    (hchk : Zeta23.DBN.checkBarrier d = true)
    (a : Zeta23.DBN.AsymData) (ha0 : Zeta23.DBN.At0 a = 93 / 500) (hay0 : Zeta23.DBN.Ay0 a = 16733 / 100000)
    (hayA : Zeta23.DBN.AyA a = 3962323 / 5000000) (hrow : ∃ r ∈ a.rows, r.Nlo ≤ 630783)
    (hachk : Zeta23.DBN.checkAsym a = true)
    (hH1 : Zeta23.DBN.ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : Zeta23.DBN.BarrierEnclOK (fun t z => Zeta23.DBN.Ht t z / Zeta23.DBN.Bt t z) d)
    (hAsym : Zeta23.DBN.AsymEnclOK (fun z => Zeta23.DBN.Ht (93 / 500) z / Zeta23.DBN.Bt (93 / 500) z) a)
    (hTail : Zeta23.DBN.TailOK (fun z => Zeta23.DBN.Ht (93 / 500) z / Zeta23.DBN.Bt (93 / 500) z) a)
    (hH3 : Zeta23.DBN.Polymath15Bridge' ∧ Zeta23.DBN.HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Zeta23.DBN.Ht t z = 0 → z.im = 0 := by
  have hchk' := hchk
  simp only [Zeta23.DBN.checkBarrier, Bool.and_eq_true, List.all_eq_true] at hchk'
  obtain ⟨hchain, hprisms⟩ := hchk'
  have hHol : ∀ t : ℝ, 0 ≤ t → t ≤ Zeta23.DBN.t0 d →
      ∃ U : Set ℂ, IsOpen U ∧ Zeta23.DBN.BarrierRect d ⊆ U
        ∧ DifferentiableOn ℂ (fun z => Zeta23.DBN.Ht t z / Zeta23.DBN.Bt t z) U := by
    intro t _ _
    refine ⟨{z : ℂ | 0 < z.re}, Zeta23.DBN.isOpen_rightHalfPlane, ?_,
      Zeta23.DBN.differentiableOn_Ht_div_Bt hH3.2 t⟩
    intro z hz
    have h1 : d.rect.x1 ≤ z.re := hz.1
    rw [hx1] at h1
    show 0 < z.re
    linarith
  have hiii := Zeta23.DBN.cert_of_checkBarrier_xy Zeta23.DBN.Ht Zeta23.DBN.Bt d hchain hprisms hHol hEncl
  have hii : ∀ x y : ℝ, 5000000194858 + 1 ≤ x → 16733 / 100000 ≤ y →
      y ^ 2 ≤ 1 - 2 * (93 / 500) → Zeta23.DBN.Ht (93 / 500) (x + y * Complex.I) ≠ 0 := by
    intro x y hx hy0 hy2
    have hyA : y ≤ 3962323 / 5000000 := by
      apply le_of_sq_le_sq _ (by norm_num)
      nlinarith
    obtain ⟨r, hr, hrN⟩ := hrow
    have hlo : (r.Nlo : ℝ) ≤ Zeta23.DBN.windowIdx (Zeta23.DBN.At0 a) x := by
      rw [ha0]
      have h1 := Zeta23.DBN.row2_windowIdx_ge x hx
      have h2 : (r.Nlo : ℝ) ≤ 630783 := by exact_mod_cast hrN
      linarith
    have hg := Zeta23.DBN.cert_of_checkAsym _ a hachk hAsym hTail x y r hr hlo
      (by rw [hay0]; exact hy0) (by rw [hayA]; exact hyA)
    exact (div_ne_zero_iff.mp hg).1
  have hray : ∀ t : ℝ, 93 / 500 + (16733 / 100000) ^ 2 / 2 ≤ t → ∀ z : ℂ, Zeta23.DBN.Ht t z = 0 → z.im = 0 := by
    refine hH3.1 (93 / 500) 5000000194858 (16733 / 100000) (by norm_num) (by norm_num) (by norm_num)
      (by norm_num) (Zeta23.DBN.Instance02.hH1_row2 hH1) hii ?_
    intro x y hx1' hx2' hy1' hy2' t ht0' ht1'
    exact hiii x y (by rw [hx1]; exact hx1') (by rw [hx2]; exact hx2') (by rw [hy1]; exact hy1')
      (by rw [hy2]; exact hy2') t ht0' (by rw [ht0]; exact ht1')
  intro t ht
  exact hray t (le_trans Zeta23.DBN.Instance02.row2_bound_le_point2 ht)

end DBNBridge

/-! ## The seven challenge statements, byte-identical to Challenge/DBN.lean, proved -/

/-- **(G) Generic soundness of the two-lane certificate at Polymath15 Table 1 row 2.**  For ANY barrier data `d` on the
instance rectangle R = [X, X+1] × [y₀, 1] (X = 5 000 000 194 858, y₀ = 16733/100000) with final time t₀ = 93/500 that the
integer checker `checkBarrier` accepts, and ANY asymptotic data `a` with t₀ = 93/500, y₀ = 16733/100000, yA = 3962323/5000000
and some window row starting at or below N_start = 630783 that `checkAsym` accepts: modulo the displayed hypotheses (H1)
`hH1`, (H2-B) `hEncl`, (H2-A) `hAsym`, (H-TAIL) `hTail`, (H3) `hH3`, every H_t with t ≥ 1/5 has only real zeros — Λ ≤ 0.2 in
ray form.  Label (SPEC §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3" — never "fully machine-checked".  The
window range N ∈ [Nlo, …] is a displayed floor enclosure plus kernel-checked coverage; the only displayed nonvanishing
conclusion is `TailOK` on N(x) ≥ N₁ with the y-band [y₀, yA]. -/
theorem dbn_ray_le_point2_of_certificates
    (d : BarrierData) (hx1 : d.rect.x1 = 5000000194858) (hx2 : d.rect.x2 = 5000000194858 + 1)
    (hy1 : d.rect.y1 = 16733 / 100000) (hy2 : d.rect.y2 = 1) (ht0 : t0 d = 93 / 500)
    (hchk : checkBarrier d = true)
    (a : AsymData) (ha0 : At0 a = 93 / 500) (hay0 : Ay0 a = 16733 / 100000)
    (hayA : AyA a = 3962323 / 5000000) (hrow : ∃ r ∈ a.rows, r.Nlo ≤ 630783)
    (hachk : checkAsym a = true)
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) d)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) a)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) a)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  rw [DBNBridge.Ht_eq]
  rw [DBNBridge.ZeroVerification_eq] at hH1
  rw [DBNBridge.Ht_eq, DBNBridge.Bt_eq] at hEncl hAsym hTail
  rw [DBNBridge.Polymath15Bridge'_eq, DBNBridge.HtEntire_eq] at hH3
  rw [DBNBridge.BarrierEnclOK_iff] at hEncl
  rw [DBNBridge.AsymEnclOK_iff] at hAsym
  rw [DBNBridge.TailOK_iff] at hTail
  rw [DBNBridge.checkBarrier_eq] at hchk
  rw [DBNBridge.checkAsym_eq] at hachk
  refine DBNBridge.ray_of_certificates (DBNBridge.toZBarrier d) hx1 hx2 hy1 hy2 ht0 hchk
    (DBNBridge.toZAsym a) ha0 hay0 hayA ?_ hachk hH1 hEncl hAsym hTail hH3
  obtain ⟨r, hr, hrN⟩ := hrow
  exact ⟨DBNBridge.toZARow r, List.mem_map_of_mem hr, hrN⟩

/-- **(I) Λ ≤ 0.2 in ray form, mpmath-ball leg** (the referee's statement of Zeta23's `lambda_le_point2`, over the trusted
copies `row2BarrierMP`, `row2AsymMP` of the mpmath-ball producer's two transcripts).  Every H_t with t ≥ 1/5 has only real
zeros — kernel-checked modulo the displayed hypotheses: (H1) `hH1`, the producer-certified zero verification
`ZeroVerification (116733/200000) 2500000097429` (Platt–Trudgian Theorem 1, prose); (H2-B) `hEncl`, the producer-certified
barrier enclosures for the kernel-checked mpmath-ball transcript (39 prisms, 7 176 rows); (H2-A) `hAsym`, the producer-certified
final-time window-row floors on N ∈ [630783, 5140999] (the step from the floors to nonvanishing there is kernel-checked
coverage); (H-TAIL) `hTail`, nonvanishing for N(x) ≥ N₁ = 5 141 000 on y ∈ [y₀, yA] — the one displayed nonvanishing
CONCLUSION (Lemma T's reduction is prose; C-A6 is kernel-checked evidence, never consumed); (H3) `hH3`, the Polymath15
analytic package `Polymath15Bridge' ∧ HtEntire`.  Label (SPEC §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL),
H3" — never "fully machine-checked".  Λ ≤ 0.2 is not proved; the word Λ appears in prose only. -/
theorem dbn_ray_le_point2_mp
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierMP)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymMP)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  rw [DBNBridge.Ht_eq]
  rw [DBNBridge.ZeroVerification_eq] at hH1
  rw [DBNBridge.Ht_eq, DBNBridge.Bt_eq] at hEncl hAsym hTail
  rw [DBNBridge.Polymath15Bridge'_eq, DBNBridge.HtEntire_eq] at hH3
  rw [DBNBridge.BarrierEnclOK_iff, DBNBridge.row2BarrierMP_toZ] at hEncl
  rw [DBNBridge.AsymEnclOK_iff, DBNBridge.row2AsymMP_toZ] at hAsym
  rw [DBNBridge.TailOK_iff, DBNBridge.row2AsymMP_toZ] at hTail
  exact Zeta23.DBN.Instance02.lambda_le_point2 hH1 hEncl hAsym hTail hH3

/-- **(I) Λ ≤ 0.2 in ray form, Arb/FLINT leg** — the same statement from the independent producer's transcripts
(`row2BarrierARB`: 72 prisms, 10 771 rows; `row2AsymARB`), the referee's statement of Zeta23's `lambda_le_point2_arb`.
The two legs are two theorems, never merged (D-R3).  Label (SPEC §3.7): "kernel-checked modulo H1, H2 (H2-B, H2-A,
H-TAIL), H3" — never "fully machine-checked". -/
theorem dbn_ray_le_point2_arb
    (hH1 : ZeroVerification (116733 / 200000) 2500000097429)
    (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) row2BarrierARB)
    (hAsym : AsymEnclOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymARB)
    (hTail : TailOK (fun z => Ht (93 / 500) z / Bt (93 / 500) z) row2AsymARB)
    (hH3 : Polymath15Bridge' ∧ HtEntire) :
    ∀ t : ℝ, (1 / 5 : ℝ) ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0 := by
  rw [DBNBridge.Ht_eq]
  rw [DBNBridge.ZeroVerification_eq] at hH1
  rw [DBNBridge.Ht_eq, DBNBridge.Bt_eq] at hEncl hAsym hTail
  rw [DBNBridge.Polymath15Bridge'_eq, DBNBridge.HtEntire_eq] at hH3
  rw [DBNBridge.BarrierEnclOK_iff, DBNBridge.row2BarrierARB_toZ] at hEncl
  rw [DBNBridge.AsymEnclOK_iff, DBNBridge.row2AsymARB_toZ] at hAsym
  rw [DBNBridge.TailOK_iff, DBNBridge.row2AsymARB_toZ] at hTail
  exact Zeta23.DBN.Instance02.lambda_le_point2_arb hH1 hEncl hAsym hTail hH3

/-- **(K) The mpmath-ball barrier transcript passes the integer checker** (C-B0…C-B13 for the chain and all 39 prisms).
An integer fact about the literal; nothing analytic — H2-B stays displayed. -/
theorem dbn_row2BarrierMP_checked : checkBarrier row2BarrierMP = true := by
  rw [DBNBridge.checkBarrier_eq, DBNBridge.row2BarrierMP_toZ]
  exact Zeta23.DBN.Instance02.row2BarrierMP_check

/-- **(K) The Arb/FLINT barrier transcript passes the integer checker** (all 72 prisms).  Integer fact only. -/
theorem dbn_row2BarrierARB_checked : checkBarrier row2BarrierARB = true := by
  rw [DBNBridge.checkBarrier_eq, DBNBridge.row2BarrierARB_toZ]
  exact Zeta23.DBN.Instance02.row2BarrierARB_check

/-- **(K) The mpmath-ball Lane A transcript passes the integer checker** (C-A1…C-A6).  Integer fact only; C-A6 is
checked here but consumed by no proof (the tail reduction is prose). -/
theorem dbn_row2AsymMP_checked : checkAsym row2AsymMP = true := by
  rw [DBNBridge.checkAsym_eq, DBNBridge.row2AsymMP_toZ]
  exact Zeta23.DBN.Instance02.row2AsymMP_check

/-- **(K) The Arb/FLINT Lane A transcript passes the integer checker** (C-A1…C-A6).  Integer fact only. -/
theorem dbn_row2AsymARB_checked : checkAsym row2AsymARB = true := by
  rw [DBNBridge.checkAsym_eq, DBNBridge.row2AsymARB_toZ]
  exact Zeta23.DBN.Instance02.row2AsymARB_check

end
