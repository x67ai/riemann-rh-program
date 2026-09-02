import Zeta23.DBN.Instance02
namespace Zeta23.DBN.Instance02
-- kernel timing of the MONOLITHIC checker on each full transcript (SPEC section 7.6 item 5 said "serial hours";
-- measured here); the program modules prove the same facts from the per-prism kernel theorems instead.
set_option maxRecDepth 100000
set_option maxHeartbeats 4000000
theorem row2BarrierMP_check_kernel : checkBarrier row2BarrierMP = true := by decide +kernel
theorem row2BarrierARB_check_kernel : checkBarrier row2BarrierARB = true := by decide +kernel
#print axioms row2BarrierMP_check_kernel
#print axioms row2BarrierARB_check_kernel
end Zeta23.DBN.Instance02
