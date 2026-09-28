import Zeta23.PairCeiling.GridCorner

open Finset

-- (a) rational marks over a general commutative ring: no cast exists (expected to FAIL)
section
variable {K : Type*} [CommRing K] {M : ℕ} [NeZero M]
#check fun (m : ZMod M → ℚ) (k : ZMod M) => ((m k : ℚ) : K)
end

-- (a') over a Field it typechecks
section
variable {K : Type*} [Field K] {M : ℕ} [NeZero M]
#check fun (m : ZMod M → ℚ) (k : ZMod M) => ((m k : ℚ) : K)
end

-- (b) the cast lemmas the ℂ specialization needs
#check @map_ratCast
#check @Complex.ofReal_ratCast
#check @Rat.cast_intCast
example (q : ℚ) : (starRingEnd ℂ) (q : ℂ) = (q : ℂ) := map_ratCast _ q
example (q : ℚ) : ((q : ℝ) : ℂ) = (q : ℂ) := Complex.ofReal_ratCast q

-- (c) kernel evaluation over ℚ on ZMod 65
def fracMarkProbe : ZMod 65 → ℚ := fun k => if k.val < 48 then 4/3 else 0
set_option maxHeartbeats 400000 in
theorem probe_mass : ∑ k : ZMod 65, fracMarkProbe k = 64 := by decide +kernel
set_option maxHeartbeats 400000 in
theorem probe_sq : ∑ k : ZMod 65, (fracMarkProbe k) ^ 2 = 256 / 3 := by decide +kernel
set_option maxHeartbeats 400000 in
theorem probe_Nd : (Finset.univ.filter (fun k : ZMod 65 => fracMarkProbe k ≠ 0)).card = 48 := by decide +kernel
#print axioms probe_mass
#print axioms probe_sq
#print axioms probe_Nd
