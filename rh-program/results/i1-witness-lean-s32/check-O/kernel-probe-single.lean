-- CHECK-O single-theorem probe (checker-written): is the profiler line cumulative?
import ChallengeDeps.I1Witness
open I1Witness
set_option profiler true
set_option profiler.threshold 0
theorem probe36_three : lambdaVec epsteinB 36 3 = -4 := by decide +kernel
