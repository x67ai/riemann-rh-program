import Zeta23.W1.FDH
import Zeta23.W1.Ledger
import Zeta23.W1.Soundness
import Zeta23.W1.ArgPrincipleBridge

-- Job 2 (Opus) independent #print axioms probe over EVERY top-level declaration of
-- FDH.lean, Ledger.lean, Soundness.lean, plus cert_of_checkW1_ap and the checker literals.

#print axioms Zeta23.W1.kappaDH
#print axioms Zeta23.W1.fDH
#print axioms Zeta23.W1.differentiable_fDH
#print axioms Zeta23.W1.hasSum_hurwitzZeta_one_fifth
#print axioms Zeta23.W1.cert_of_checkW1_fDH
#print axioms Zeta23.W1.mpDH_T1
#print axioms Zeta23.W1.mpDH_T2
#print axioms Zeta23.W1.arbDH_T1
#print axioms Zeta23.W1.arbDH_T2
#print axioms Zeta23.W1.mpDH_zero
#print axioms Zeta23.W1.arbDH_zero
#print axioms Zeta23.W1.mpNullT100_exclusion
#print axioms Zeta23.W1.arbNullT100_exclusion
#print axioms Zeta23.W1.mpNullT1000_exclusion
#print axioms Zeta23.W1.arbNullT1000_exclusion
#print axioms Zeta23.W1.mpNullT10000_exclusion
#print axioms Zeta23.W1.arbNullT10000_exclusion
#print axioms Zeta23.W1.mpNullDeepT100_exclusion
#print axioms Zeta23.W1.arbNullDeepT100_exclusion
#print axioms Zeta23.W1.ratVal
#print axioms Zeta23.W1.sigma1
#print axioms Zeta23.W1.sigma2
#print axioms Zeta23.W1.T1
#print axioms Zeta23.W1.T2
#print axioms Zeta23.W1.cpt
#print axioms Zeta23.W1.cpt_re
#print axioms Zeta23.W1.cpt_im
#print axioms Zeta23.W1.rectClosed
#print axioms Zeta23.W1.rectOpen
#print axioms Zeta23.W1.rectBdry
#print axioms Zeta23.W1.W1Rect
#print axioms Zeta23.W1.W1RectOpen
#print axioms Zeta23.W1.W1Bdry
#print axioms Zeta23.W1.consecPairs
#print axioms Zeta23.W1.segPt
#print axioms Zeta23.W1.bottomPts
#print axioms Zeta23.W1.rightPts
#print axioms Zeta23.W1.topPts
#print axioms Zeta23.W1.leftPts
#print axioms Zeta23.W1.segs
#print axioms Zeta23.W1.logDerivSegIntegral
#print axioms Zeta23.W1.argIncrement
#print axioms Zeta23.W1.RowEnclOK
#print axioms Zeta23.W1.W1EnclOK
#print axioms Zeta23.W1.RectArgPrinciple
#print axioms Zeta23.W1.ratVal_le_of_cross
#print axioms Zeta23.W1.ratVal_lt_of_cross
#print axioms Zeta23.W1.ratVal_eq_of_cross
#print axioms Zeta23.W1.checksOK_of_checkW1
#print axioms Zeta23.W1.edgeOK_inc_spec
#print axioms Zeta23.W1.edgeOK_dec_spec
#print axioms Zeta23.W1.densPos_cons
#print axioms Zeta23.W1.rowsOK_mem
#print axioms Zeta23.W1.rowOK_C6
#print axioms Zeta23.W1.consecPairs_map
#print axioms Zeta23.W1.map_congr_fn
#print axioms Zeta23.W1.chainLt_spec
#print axioms Zeta23.W1.chainGt_spec
#print axioms Zeta23.W1.firstOK_spec
#print axioms Zeta23.W1.lastOK_spec
#print axioms Zeta23.W1.consecPairs_tail_subset
#print axioms Zeta23.W1.head_le_of_consec_le
#print axioms Zeta23.W1.getLast_ge_of_consec_le
#print axioms Zeta23.W1.head?_lt_getLast?
#print axioms Zeta23.W1.cover_chain
#print axioms Zeta23.W1.cover_chain_dec
#print axioms Zeta23.W1.segPt_mk_horiz
#print axioms Zeta23.W1.segPt_mk_vert
#print axioms Zeta23.W1.exists_t_inc
#print axioms Zeta23.W1.exists_t_dec
#print axioms Zeta23.W1.bdry_cover
#print axioms Zeta23.W1.forall₂_mem_right
#print axioms Zeta23.W1.row_box_excludes_zero
#print axioms Zeta23.W1.boundary_nonvanishing
#print axioms Zeta23.W1.im_list_sum
#print axioms Zeta23.W1.sum_arg_encl
#print axioms Zeta23.W1.segPt_zero
#print axioms Zeta23.W1.segPt_one
#print axioms Zeta23.W1.segPt_comp
#print axioms Zeta23.W1.segPt_horiz_tau
#print axioms Zeta23.W1.segPt_vert_tau
#print axioms Zeta23.W1.smul_comp_integral
#print axioms Zeta23.W1.logDerivSegIntegral_affine
#print axioms Zeta23.W1.sum_integral_consecPairs
#print axioms Zeta23.W1.consec_map_forall
#print axioms Zeta23.W1.tau_facts_inc
#print axioms Zeta23.W1.tau_facts_dec
#print axioms Zeta23.W1.edge_sum_eq
#print axioms Zeta23.W1.continuousOn_logDeriv_seg_of_diffOn
#print axioms Zeta23.W1.differentiableOn_riemannZeta_re_lt_one
#print axioms Zeta23.W1.continuousOn_zeta_logDeriv_seg
#print axioms Zeta23.W1.pin_m
#print axioms Zeta23.W1.cert_of_checkW1_of_diffOn
#print axioms Zeta23.W1.cert_of_checkW1
#print axioms Zeta23.W1.checkW1Floor_spec
#print axioms Zeta23.W1.floorRowsOK_mem
#print axioms Zeta23.W1.mdist_sq_le
#print axioms Zeta23.W1.floor_of_checkW1Floor
#print axioms Zeta23.W1.cert_of_checkW1_ap
#print axioms Zeta23.W1.rectArgPrinciple_riemannZeta
#print axioms Zeta23.W1.mpDH_check
#print axioms Zeta23.W1.arbDH_check
#print axioms Zeta23.W1.mpNullT100_check
#print axioms Zeta23.W1.arbNullT100_check
#print axioms Zeta23.W1.mpNullT1000_check
#print axioms Zeta23.W1.arbNullT1000_check
#print axioms Zeta23.W1.mpNullT10000_check
#print axioms Zeta23.W1.arbNullT10000_check
#print axioms Zeta23.W1.mpNullDeepT100_check
#print axioms Zeta23.W1.arbNullDeepT100_check
#print axioms Zeta23.W1.mpDH
#print axioms Zeta23.W1.arbDH

-- statements
#check @Zeta23.W1.cert_of_checkW1_fDH
#check @Zeta23.W1.mpDH_zero
#check @Zeta23.W1.arbDH_zero
#check @Zeta23.W1.cert_of_checkW1_ap
#check @Zeta23.W1.cert_of_checkW1
#check @Zeta23.W1.cert_of_checkW1_of_diffOn
#check @Zeta23.W1.differentiable_fDH
#check @Zeta23.W1.hasSum_hurwitzZeta_one_fifth
#check @Zeta23.W1.continuousOn_logDeriv_seg_of_diffOn
#check @Zeta23.W1.continuousOn_zeta_logDeriv_seg
#check @Zeta23.W1.W1Rect
#check @Zeta23.W1.T1
#check @Zeta23.W1.T2
#check @Zeta23.W1.mpNullT100_exclusion
#check @Zeta23.W1.arbNullT100_exclusion
#check @Zeta23.W1.mpNullT1000_exclusion
#check @Zeta23.W1.arbNullT1000_exclusion
#check @Zeta23.W1.mpNullT10000_exclusion
#check @Zeta23.W1.arbNullT10000_exclusion
#check @Zeta23.W1.mpNullDeepT100_exclusion
#check @Zeta23.W1.arbNullDeepT100_exclusion
#print Zeta23.W1.kappaDH
#print Zeta23.W1.fDH
