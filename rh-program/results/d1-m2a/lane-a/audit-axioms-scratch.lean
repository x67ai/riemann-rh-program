-- audit-axioms-scratch.lean — AUDITOR's own `#print axioms` / `#check` probe (Job 2, BRIEF-3d.md).
-- Written independently of final-axioms-scratch.lean; run from ~/rh-lean-work/zeta-23-lean-main:
--     lake env lean "<this file>"
-- Expected: the six theorems [propext, Classical.choice, Quot.sound]; the two kernel facts [propext];
-- no sorryAx, no Lean.ofReduceBool (native_decide), no project-local axiom anywhere.
import Zeta23.DBN.Instance02

open Zeta23.DBN.Instance02

-- the eight names of BRIEF-3d.md item 5
#print axioms Zeta23.DBN.Instance02.lambda_le_point2
#print axioms Zeta23.DBN.Instance02.lambda_le_point2_arb
#print axioms Zeta23.DBN.Instance02.row2_ray_mp
#print axioms Zeta23.DBN.Instance02.row2_ray_arb
#print axioms Zeta23.DBN.Instance02.row2_laneA_mp
#print axioms Zeta23.DBN.Instance02.row2_laneA_arb
#print axioms Zeta23.DBN.Instance02.row2AsymMP_check
#print axioms Zeta23.DBN.Instance02.row2AsymARB_check

-- the soundness theorem the glue lemmas rest on, and the three simp facts (auditor's additions)
#print axioms Zeta23.DBN.cert_of_checkAsym
#print axioms Zeta23.DBN.Instance02.row2AsymMP_t0
#print axioms Zeta23.DBN.Instance02.row2AsymMP_y0
#print axioms Zeta23.DBN.Instance02.row2AsymMP_yA
#print axioms Zeta23.DBN.Instance02.row2AsymARB_t0
#print axioms Zeta23.DBN.Instance02.row2AsymARB_y0
#print axioms Zeta23.DBN.Instance02.row2AsymARB_yA
#print axioms Zeta23.DBN.Instance02.row2_windowIdx_ge

-- displayed statements: the auditor compares these against H1, H2-B, hAsym, hTail, H3 and nothing else
#check @Zeta23.DBN.Instance02.lambda_le_point2
#check @Zeta23.DBN.Instance02.lambda_le_point2_arb
#check @Zeta23.DBN.Instance02.row2_ray_mp
#check @Zeta23.DBN.Instance02.row2_ray_arb
#check @Zeta23.DBN.Instance02.row2_laneA_mp
#check @Zeta23.DBN.Instance02.row2_laneA_arb
#check @Zeta23.DBN.cert_of_checkAsym

-- the literals themselves, as the kernel sees them
#print Zeta23.DBN.Instance02.row2AsymMP
#print Zeta23.DBN.Instance02.row2AsymARB
