-- final-axioms-scratch.lean — `#print axioms` on the eight names of BRIEF-3d.md item 5 after the hLaneA replacement
-- (Session 19 emitter, 2026-09-09).  NOT a program file.  Run from ~/rh-lean-work/zeta-23-lean-main against the BUILT tree:
--     lake env lean "<this file>"     (one lean process; tree untouched)
-- Expected: the six theorems [propext, Classical.choice, Quot.sound]; the two kernel facts [propext].  No sorryAx, no
-- Lean.ofReduceBool (no native_decide) anywhere.
import Zeta23.DBN.Instance02

#print axioms Zeta23.DBN.Instance02.lambda_le_point2
#print axioms Zeta23.DBN.Instance02.lambda_le_point2_arb
#print axioms Zeta23.DBN.Instance02.row2_ray_mp
#print axioms Zeta23.DBN.Instance02.row2_ray_arb
#print axioms Zeta23.DBN.Instance02.row2_laneA_mp
#print axioms Zeta23.DBN.Instance02.row2_laneA_arb
#print axioms Zeta23.DBN.Instance02.row2AsymMP_check
#print axioms Zeta23.DBN.Instance02.row2AsymARB_check

-- the displayed statements, elaborated (the auditor compares these against H1, H2-B, hAsym, hTail, H3 and nothing else)
#check @Zeta23.DBN.Instance02.lambda_le_point2
#check @Zeta23.DBN.Instance02.lambda_le_point2_arb
#check @Zeta23.DBN.Instance02.row2_ray_mp
#check @Zeta23.DBN.Instance02.row2_ray_arb
#check @Zeta23.DBN.Instance02.row2_laneA_mp
#check @Zeta23.DBN.Instance02.row2_laneA_arb
