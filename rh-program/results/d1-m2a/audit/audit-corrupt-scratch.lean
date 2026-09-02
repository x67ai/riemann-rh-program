-- AUDIT SCRATCH (not a program file): corrupted Instance02 literals must be REJECTED by the Lean checker.
import Zeta23.DBN.Instance02.mp_0017
import Zeta23.DBN.Instance02.arb_0040
import Zeta23.DBN.Instance02.mp_Barrier
import Zeta23.DBN.Instance02.arb_Barrier

namespace Zeta23
namespace DBN
namespace Instance02

set_option maxRecDepth 100000

-- sanity: the untouched literals are accepted (re-evaluated here by the kernel)
theorem audit_mp0017_ok : checkPrism row2Rect mp0017 = true := by decide +kernel
theorem audit_arb0040_ok : checkPrism row2Rect arb0040 = true := by decide +kernel

-- (1) C-B6: row 7's value box made to straddle 0
def audit_bad_box : PrismData := { mp0017 with rows := mp0017.rows.set 7 ⟨-1, 1, -1, 1, 0, 0⟩ }
theorem audit_bad_box_rejected : checkPrism row2Rect audit_bad_box = false := by decide +kernel

-- (2) C-B12: E := Fn * K / Fd (here Fd = K, so E := Fn) -- E + D >= floor
def audit_bad_E : PrismData := { mp0017 with E := mp0017.Fn }
theorem audit_bad_E_rejected : checkPrism row2Rect audit_bad_E = false := by decide +kernel

-- (3) C-B3: a bottom-edge breakpoint of arb0040 moved onto its predecessor (walk no longer strictly increasing)
def audit_bad_mesh : PrismData := { arb0040 with bottom := arb0040.bottom.set 5 (80000003117729, 16) }
theorem audit_bad_mesh_rejected : checkPrism row2Rect audit_bad_mesh = false := by decide +kernel

-- (4) C-B11: floor numerator x 10
def audit_bad_floor : PrismData := { arb0040 with Fn := 10 * arb0040.Fn }
theorem audit_bad_floor_rejected : checkPrism row2Rect audit_bad_floor = false := by decide +kernel

-- (5) C-B9: every argument row shifted by +1 (S_lo = -108 + 184 > 0)
def audit_bad_arg : PrismData := { mp0017 with rows := mp0017.rows.map fun r => { r with argLo := r.argLo + 1, argHi := r.argHi + 1 } }
theorem audit_bad_arg_rejected : checkPrism row2Rect audit_bad_arg = false := by decide +kernel

-- (6) C-B4: one row deleted
def audit_bad_count : PrismData := { mp0017 with rows := mp0017.rows.tail }
theorem audit_bad_count_rejected : checkPrism row2Rect audit_bad_count = false := by decide +kernel

-- (7) C-B13: t0 lowered to the last seam of the mp chain (3719/20000)
def audit_bad_t0 : BarrierData := { row2BarrierMP with t0n := 3719, t0d := 20000 }
theorem audit_bad_t0_rejected : checkBarrierChain audit_bad_t0 = false := by decide +kernel

-- (8) C-B13: first prism dropped (chain no longer starts at 0)
def audit_bad_first : BarrierData := { row2BarrierARB with prisms := row2BarrierARB.prisms.tail }
theorem audit_bad_first_rejected : checkBarrierChain audit_bad_first = false := by decide +kernel

-- (9) C-B13: two prisms swapped (seams not increasing)
def audit_bad_order : BarrierData := { row2BarrierMP with prisms := (row2BarrierMP.prisms.set 5 mp0017).set 17 mp0005 }
theorem audit_bad_order_rejected : checkBarrierChain audit_bad_order = false := by decide +kernel

-- (10) C-B2': degenerate rectangle x2 := x1
def audit_bad_rect : BarrierData := { row2BarrierMP with rect := { row2Rect with xn2 := 5000000194858 } }
theorem audit_bad_rect_rejected : checkBarrierChain audit_bad_rect = false := by decide +kernel
theorem audit_bad_rect_prism_rejected : checkPrism audit_bad_rect.rect mp0017 = false := by decide +kernel

end Instance02
end DBN
end Zeta23

-- audit harness control: a FALSE claim must be refused by the kernel (this line is EXPECTED to error)
namespace Zeta23.DBN.Instance02
theorem audit_control_must_fail : checkPrism row2Rect audit_bad_E = true := by decide +kernel
#print axioms audit_bad_box_rejected
#print axioms audit_bad_E_rejected
#print axioms audit_bad_mesh_rejected
#print axioms audit_bad_floor_rejected
#print axioms audit_bad_arg_rejected
#print axioms audit_bad_count_rejected
#print axioms audit_bad_t0_rejected
#print axioms audit_bad_first_rejected
#print axioms audit_bad_order_rejected
#print axioms audit_bad_rect_rejected
#print axioms audit_bad_rect_prism_rejected
#print axioms audit_mp0017_ok
end Zeta23.DBN.Instance02
