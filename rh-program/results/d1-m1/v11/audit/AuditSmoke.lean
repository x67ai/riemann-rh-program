import Zeta23.W1.ArgPrincipleBridge
import Zeta23.W1.Examples

namespace Zeta23
namespace W1

-- The refutation example: modulo H-ENCL ALONE (no H-AP), an accepted m = 1 transcript
-- yields an off-critical-line zero of zeta.  Non-vacuous: checkW1 = true is kernel-proved.
theorem auditSmoke_refutation (hE : W1EnclOK riemannZeta exampleRefutation) :
    ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1
      ∧ T1 exampleRefutation < ρ.im ∧ ρ.im < T2 exampleRefutation :=
  (cert_of_checkW1_ap exampleRefutation exampleRefutation_accepted hE).1 (by norm_num [exampleRefutation, exampleExclusion])

-- The exclusion example: modulo H-ENCL ALONE, an accepted m = 0 transcript excludes zeros.
theorem auditSmoke_exclusion (hE : W1EnclOK riemannZeta exampleExclusion) :
    ∀ s ∈ W1Rect exampleExclusion, riemannZeta s ≠ 0 :=
  (cert_of_checkW1_ap exampleExclusion exampleExclusion_accepted hE).2 (by norm_num [exampleRefutation, exampleExclusion])

end W1
end Zeta23

#print axioms Zeta23.W1.auditSmoke_refutation
#print axioms Zeta23.W1.auditSmoke_exclusion
