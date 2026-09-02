import Zeta23.W1.ArgPrincipleBridge

namespace Zeta23
namespace W1
open Complex

/-- Adversarial NON-VACUITY / ORIENTATION witness for the discharged H-AP: a concrete analytic
`f` with one zero inside a checker-admissible rectangle (1/2 < 3/5 <= 7/10 < 1, 10 < 11) forces
`Z >= 1`, hence the four §4 edge increments sum to `2*pi*Z > 0` — so the increments are NOT the
junk value, and the counterclockwise traversal gives a POSITIVE winding. -/
theorem auditWitness :
    ∃ Z : ℕ, 1 ≤ Z ∧
      2 * Real.pi * Z
        = argIncrement (fun s => s - cpt (13/20) (21/2)) (cpt (3/5) 10) (cpt (7/10) 10)
          + argIncrement (fun s => s - cpt (13/20) (21/2)) (cpt (7/10) 10) (cpt (7/10) 11)
          + argIncrement (fun s => s - cpt (13/20) (21/2)) (cpt (7/10) 11) (cpt (3/5) 11)
          + argIncrement (fun s => s - cpt (13/20) (21/2)) (cpt (3/5) 11) (cpt (3/5) 10) := by
  set c : ℂ := cpt (13/20) (21/2) with hc
  have hcOpen : c ∈ rectOpen (3/5) (7/10) 10 11 := by
    refine ⟨?_, ?_, ?_, ?_⟩ <;> simp [hc, cpt] <;> norm_num
  have hbd : ∀ s ∈ rectBdry (3/5 : ℝ) (7/10) 10 11, (fun s : ℂ => s - c) s ≠ 0 := by
    intro s hs h0
    have hsc : s = c := by simpa [sub_eq_zero] using h0
    exact hs.2 (by rw [hsc]; exact hcOpen)
  obtain ⟨Z, h1, h2, _h3⟩ :=
    rectArgPrinciple_of_local (fun s : ℂ => s - c) (3/5) (7/10) 10 11
      (by norm_num) (by norm_num) (by norm_num) (by norm_num)
      Set.univ isOpen_univ (Set.subset_univ _) (by fun_prop) hbd
  have hZ : Z ≠ 0 := fun h => h2 h c hcOpen (by simp)
  exact ⟨Z, Nat.one_le_iff_ne_zero.mpr hZ, h1⟩

end W1
end Zeta23

#print axioms Zeta23.W1.auditWitness
