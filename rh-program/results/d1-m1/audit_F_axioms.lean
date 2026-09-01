import Zeta23.W1.Soundness
import Zeta23.W1.Examples
import Zeta23.DBN.Defs

-- AUDIT F scratch: axiom audit of the W1 layer (not part of the library)
#print axioms Zeta23.W1.cert_of_checkW1
#print axioms Zeta23.W1.floor_of_checkW1Floor
#print axioms Zeta23.W1.exampleRefutation_accepted
#print axioms Zeta23.W1.exampleRefutation_floor_accepted
#print axioms Zeta23.W1.exampleExclusion_accepted
#print axioms Zeta23.W1.exampleRefutation_C6_control
#print axioms Zeta23.W1.exampleRefutation_C9_control
#print axioms Zeta23.W1.RectArgPrinciple
#print axioms Zeta23.W1.W1EnclOK
#print axioms Zeta23.DBN.Polymath15Bridge
#check @Zeta23.W1.cert_of_checkW1
#print Zeta23.W1.RectArgPrinciple
#print Zeta23.W1.RowEnclOK
