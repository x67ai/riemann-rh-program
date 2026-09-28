/- CHECKER probe: each trusted definition of ChallengeDeps/IntegralityGap.lean is, as a constant, equal to its Zeta23 original
(same binder telescope, same body) — checked by `rfl` on the two `@`-constants (no unfolding by a tactic). -/
import ChallengeDeps.IntegralityGap
import Zeta23.PairCeiling.GridGap

example : @IntegralityGap.chi = @Zeta23.PairCeiling.GridParseval.chi := rfl
example : @IntegralityGap.dftMark = @Zeta23.PairCeiling.GridParseval.dftMark := rfl
example : @IntegralityGap.dftMarkQ = @Zeta23.PairCeiling.GridParsevalRat.dftMarkQ := rfl
example : @IntegralityGap.zetaM = @Zeta23.PairCeiling.GridParseval.zetaM := rfl
example : @IntegralityGap.gridRow = @Zeta23.PairCeiling.GridCorner.gridRow := rfl
example : @IntegralityGap.gridRowQ = @Zeta23.PairCeiling.GridParsevalRat.gridRowQ := rfl
example : @IntegralityGap.fracMark = @Zeta23.PairCeiling.GridGap.fracMark := rfl
#check @IntegralityGap.dftMarkQ
#check @Zeta23.PairCeiling.GridParsevalRat.dftMarkQ
