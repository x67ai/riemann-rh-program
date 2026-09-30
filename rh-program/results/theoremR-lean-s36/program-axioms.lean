/- program-side axiom probe (theoremR-lean-s36 builder, Session 36): every declaration of Zeta23/ResidueRank/{LogPrimes,Pair,GenusBound}.lean
(27 names).  Run from the Lean tree root: lake env lean <this file>.  Expected: each line a subset of [propext, Classical.choice, Quot.sound]. -/
import Zeta23.ResidueRank.Pair
import Zeta23.ResidueRank.GenusBound

open Zeta23.ResidueRank

-- LogPrimes.lean (16)
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
#print axioms rank_span_log_le_of_supp
#print axioms rank_span_log_le
-- Pair.lean (8)
#print axioms log_two_le_vonMangoldt
#print axioms lemmaF_finite_fiber
#print axioms fiber_sum_eq_log
#print axioms lemmaF_infinite_order
#print axioms theoremR_of_A9
#print axioms theoremR
#print axioms lemmaF_finite_fiber_all
#print axioms lemmaF_infinite_order_all
-- GenusBound.lean (3)
#print axioms theoremS_bound
#print axioms theoremS
#print axioms theoremS_abs
