-- CHECK-O kernel-time probe (checker-written). Run from the clean clone with `lake env lean <this file>`.
import ChallengeDeps.I1Witness
open I1Witness
set_option profiler true
set_option profiler.threshold 0
theorem probe36_two : lambdaVec epsteinB 36 2 = -4 := by decide +kernel
theorem probe36_three : lambdaVec epsteinB 36 3 = -4 := by decide +kernel
theorem probe36_five : lambdaVec epsteinB 36 5 = 0 := by decide +kernel
theorem probe_b36 : epsteinB 36 = 3 := by decide +kernel
theorem probe_b9 : epsteinB 9 = 3 := by decide +kernel
-- negative control: must FAIL (the kernel evaluates the proposition to false)
theorem probe36_wrong : lambdaVec epsteinB 36 2 = -3 := by decide +kernel
