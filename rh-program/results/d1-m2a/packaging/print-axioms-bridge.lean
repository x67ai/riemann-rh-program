-- packaging/print-axioms-bridge.lean — a second probe (not part of the comparator topic): the bridge lemmas of
-- comparator/Solution/DBN.lean, the kernel-decided literal identities, and the Zeta23 theorems delegated to.
--   lake env lean "<this file>"   (from ~/rh-lean-work/zeta-23-lean-main)
import Solution.DBN

#print axioms DBNBridge.ray_of_certificates
#print axioms DBNBridge.row2BarrierMP_toZ
#print axioms DBNBridge.row2BarrierARB_toZ
#print axioms DBNBridge.row2AsymMP_toZ
#print axioms DBNBridge.row2AsymARB_toZ
#print axioms DBNBridge.checkBarrier_eq
#print axioms DBNBridge.checkAsym_eq
#print axioms DBNBridge.BarrierEnclOK_iff
#print axioms DBNBridge.AsymEnclOK_iff
#print axioms DBNBridge.TailOK_iff
#print axioms DBNBridge.Ht_eq
#print axioms Zeta23.DBN.Instance02.lambda_le_point2
#print axioms Zeta23.DBN.Instance02.lambda_le_point2_arb
#print axioms Zeta23.DBN.Instance02.row2BarrierMP_check
#print axioms Zeta23.DBN.Instance02.row2AsymMP_check
#check @dbn_ray_le_point2_mp
#check @dbn_ray_le_point2_of_certificates
