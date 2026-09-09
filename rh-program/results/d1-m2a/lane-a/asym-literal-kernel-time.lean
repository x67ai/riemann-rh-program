-- asym-literal-kernel-time.lean — the wall time of each `decide +kernel` on the two Lane A literals (Session 19 emitter, 2026-09-09).
-- NOT a program file.  Run from ~/rh-lean-work/zeta-23-lean-main against the BUILT literal modules:
--     lake env lean "<this file>"     (one lean process; tree untouched)
-- `profiler true` with threshold 0 prints, per declaration, the elaboration time (the `decide +kernel` tactic hands the
-- closed term to the kernel; the kernel's evaluation of `checkAsym <literal>` is the "type checking" line).  The two
-- re-elaborations below are exactly the kernel facts of Instance02/Asym_mp.lean and Asym_arb.lean, on the built literals.
import Zeta23.DBN.Instance02.Asym_mp
import Zeta23.DBN.Instance02.Asym_arb

open Zeta23.DBN Zeta23.DBN.Instance02

set_option profiler true
set_option profiler.threshold 0

theorem row2AsymMP_check_timed : checkAsym row2AsymMP = true := by decide +kernel

theorem row2AsymARB_check_timed : checkAsym row2AsymARB = true := by decide +kernel

#print axioms row2AsymMP_check_timed
#print axioms row2AsymARB_check_timed
