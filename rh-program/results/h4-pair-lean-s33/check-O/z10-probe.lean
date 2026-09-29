-- checker probe (Session 33): where do the axioms of the `decide +kernel` power sums come from?  (FIDELITY (z10))
import Mathlib.Order.Interval.Finset.Defs
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Order.Interval.Finset.Basic
import Mathlib.Data.Int.Interval
def stmtS2 : Prop := (∑ j ∈ Finset.Icc (-32 : ℤ) 32, j ^ 2) = 22880
def icc32 : Finset ℤ := Finset.Icc (-32 : ℤ) 32
theorem s2 : (∑ j ∈ Finset.Icc (-32 : ℤ) 32, j ^ 2) = 22880 := by decide +kernel
#print axioms stmtS2
#print axioms icc32
#print axioms s2
