# SHARED — unit `u-offsurgery-s39` (Conjecture U off the surgery class; UT-9)

Dated blocks, appended as the work lands. Writer: Opus 5.5 (agent). U.S. English. No git.

## 2026-10-01 — block 1: record read, plan

- Read at the line: BRIEF.md; `novel-wave-s37/beurling-frontier/NOTE.md` (all 482 lines); `read-O.md` §3–§4 (A1–A11);
  `read-F.md` §1, §4(b), P2; digest §B2, §F.1(c), §F.3 UT-9; `directions/B2-refutation-program.md` Instruments/Untried shape.
- Sibling unit `results/dz-half-s39/` is proving the DZ β₀ = ½ lemma (digest U5a); this unit only runs a numerical DZ-type rung and cites it.
- Plan: (0) rung 1 over F_q; (1) DZ random system with a planted zero; (2) candidates — (i) greedy (deterministic) discretization of a
  planted-zero continuous template, (ii) twisted-integer systems on N (periodic and non-periodic multiplicities), (iii) real-quadratic
  ideal systems thinned by the unit angle. Two routes for every exponent. Then theorems: a relative Hilberdink wall for discretizations,
  and rigidity of the periodic twisted class.

## 2026-10-01 — block 2: S5 (integer-greedy systems) crosses U's line numerically

- S5 defined in NOTE §2; generator `verify/pseudoN.c`, independent re-derivation `verify/pseudoN_check.py` (0 mismatches to 10⁶, ρ = 0.8, 1.05).
- ρ = 0.8 at X = 10⁹: β ≈ 0.30 (running sup of |E|, stable over windows 10³…10⁶ → 10⁹), α ≈ 0.74–0.76 (running sup of |ψ − x|).
  α − 2β ≈ 0.14 over six decades. Sweep over 19 densities at 10⁸: several ρ (0.8, 0.95, 1.05) above the line by ≥ 0.12.
- STOP CONDITION of the brief met numerically. Next: route 2 for α (argument principle on ζ_P = ρζ + Σ(a_n − ρ)n^{−s}), then report.
- Design (i) in tracking form is forbidden in print: Hilberdink 2005 Remark C (w-18a l. 496–500) + Remark B(ii): finitely many zeros
  in σ > η with η ∈ (β, α) forces η ≥ ½; a tracking discretization of a rational template has only the template's zeros, so β ≥ ½.
