/- rung-1 axiom probe (theoremR-lean-s36 builder, Session 36): every declaration of Zeta23/ResidueRank/LogPrimes.lean.
Run from the Lean tree root: lake env lean <this file>.  Expected: each line lists a subset of [propext, Classical.choice, Quot.sound]. -/
import Zeta23.ResidueRank.LogPrimes

open Zeta23.ResidueRank

#print axioms logP
#print axioms expVec
#print axioms expVec_apply
#print axioms expVec_one
#print axioms expVec_mul
#print axioms expVec_prime
#print axioms linearCombination_expVec_prime
#print axioms linearCombination_expVec
#print axioms log_mem_span_logP
#print axioms padicValRat_finset_prod
#print axioms padicValRat_prime
#print axioms linearIndependent_logP
#print axioms log_primes_linearIndependent
#print axioms span_log_not_finite
#print axioms rank_span_log_le
