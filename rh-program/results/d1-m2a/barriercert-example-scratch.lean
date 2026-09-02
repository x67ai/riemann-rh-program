/- SCRATCH: the SPEC.md §12 micro-example (ARTIFICIAL data, all integers) as kernel-checked
   instances of the PROGRAM checker `Zeta23.DBN.checkBarrier` (M2a item (b), 2026-09-02).
   Same literals as lean-shapes-scratch.lean §E, now against the built module.  Not a program file.
   Every fact is `decide +kernel` (no `native_decide`); `#print axioms` of each is listed at the end. -/
import Zeta23.DBN.BarrierCert

namespace Zeta23.DBN.M2aExample

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

/-- the global chain check (C-B0 global, C-B2′, C-B13). -/
theorem exBarrier_chain : checkBarrierChain exBarrier = true := by decide +kernel
/-- per-prism checks (the per-module kernel facts of SPEC §7.6). -/
theorem exPrism0_check : checkPrism exRect exPrism0 = true := by decide +kernel
theorem exPrism1_check : checkPrism exRect exPrism1 = true := by decide +kernel
/-- the monolithic checker on the whole certificate. -/
theorem exBarrier_check : checkBarrier exBarrier = true := by decide +kernel

/-- negative control: C-B12 fails when D = 400 (E + D = 420; 420·2 = 840 ≥ 5·100). -/
theorem exPrism0_bad_D : checkPrism exRect { exPrism0 with D := 400 } = false := by decide +kernel
/-- negative control: C-B13 fails when the first seam is not 0. -/
theorem exBarrier_bad_seam :
    checkBarrierChain { exBarrier with prisms := [{ exPrism0 with tn := 1 }, exPrism1] } = false := by
  decide +kernel
/-- negative control: C-B13 fails when the last seam is not below t₀ (seam 1/20 vs t₀ = 1/20). -/
theorem exBarrier_bad_t0 : checkBarrierChain { exBarrier with t0n := 1, t0d := 20 } = false := by
  decide +kernel
/-- negative control: C-B6 fails when a row's box contains 0 (both the Re and the Im interval
straddle 0; a box with one interval clear of 0 still passes C-B6 — e.g. reHi = 10 with imLo = 280
is ACCEPTED, as it should be). -/
theorem exPrism1_bad_row :
    checkPrism exRect { exPrism1 with rows := [⟨-70,-40,250,330,-8,9⟩, ⟨-60,-30,260,340,-7,8⟩,
      ⟨-50,-20,270,350,-9,7⟩, ⟨-40,10,-5,360,-6,10⟩, ⟨-50,-20,270,350,-8,8⟩,
      ⟨-60,-30,260,340,-10,6⟩, ⟨-70,-40,250,330,-7,9⟩] } = false := by
  decide +kernel

/-- the split-form assembly of SPEC §7.6: the per-prism facts feed `hprisms` of
`cert_of_checkBarrier` directly. -/
theorem exBarrier_prisms : ∀ p ∈ exBarrier.prisms, checkPrism exBarrier.rect p = true := by
  intro p hp
  simp only [exBarrier, List.mem_cons, List.not_mem_nil, or_false] at hp
  rcases hp with rfl | rfl
  · exact exPrism0_check
  · exact exPrism1_check

/-- the soundness theorem instantiates on the example (its analytic hypotheses stay displayed;
this checks only that the shapes fit). -/
example (G : ℝ → ℂ → ℂ)
    (hHol : ∀ t : ℝ, 0 ≤ t → t ≤ t0 exBarrier →
      ∃ U : Set ℂ, IsOpen U ∧ BarrierRect exBarrier ⊆ U ∧ DifferentiableOn ℂ (G t) U)
    (hEncl : BarrierEnclOK G exBarrier) :
    ∀ t : ℝ, 0 ≤ t → t ≤ t0 exBarrier → ∀ z ∈ BarrierRect exBarrier, G t z ≠ 0 :=
  cert_of_checkBarrier G exBarrier exBarrier_chain exBarrier_prisms hHol hEncl

end Zeta23.DBN.M2aExample

#print axioms Zeta23.DBN.M2aExample.exBarrier_chain
#print axioms Zeta23.DBN.M2aExample.exPrism0_check
#print axioms Zeta23.DBN.M2aExample.exPrism1_check
#print axioms Zeta23.DBN.M2aExample.exBarrier_check
#print axioms Zeta23.DBN.M2aExample.exPrism0_bad_D
#print axioms Zeta23.DBN.M2aExample.exBarrier_bad_seam
#print axioms Zeta23.DBN.M2aExample.exBarrier_bad_t0
#print axioms Zeta23.DBN.M2aExample.exPrism1_bad_row
#print axioms Zeta23.DBN.M2aExample.exBarrier_prisms
