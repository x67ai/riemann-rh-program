import Mathlib.Data.Int.Interval
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
set_option profiler true in
theorem sum_pow2 : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, j ^ 2) = 22880 := by decide +kernel
set_option profiler true in
theorem sum_pow4 : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, j ^ 4) = 14492192 := by decide +kernel
set_option profiler true in
theorem sum_pow6 : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, j ^ 6) = 10924353440 := by decide +kernel
set_option profiler true in
theorem sum_pow8 : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, j ^ 8) = 8964042662432 := by decide +kernel
