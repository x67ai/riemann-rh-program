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

## 2026-10-01 — block 3: route 2 confirms; close K-conditional + T + G; STOP and report

- Route 2 for α (S5, ρ = 0.8): zero ρ₁ = 0.76587 + 30.32606i of ζ_P = 0.8ζ + Σ(a_n − 0.8)n^{−s}, stable to 10⁻⁵ from X = 3·10⁷ to 10⁹;
  winding number 1 on a box at X = 10⁹ (min|F_X| 0.0394 vs tail ≤ 0.021 if |N(u) − 0.8⌊u⌋| ≤ u^{0.35} beyond 10⁹). Strip counts to t = 60:
  zeros in σ ∈ [0.60, 0.65], [0.65, 0.70], [0.75, 0.80].
- Robustness: 9 tie-break variants (ρ = 0.8, 0.95, 1.05; δ = −0.3, 0.3, 0.45) all on or above α = 2β; ρ = 0.95, 1.05 at 10⁹ also 0.10–0.19 above.
- Theorem K′ (NOTE §4): Lemma H (|N(u) − 0.8⌊u⌋| ≪ u^{0.35}) ⇒ U false. T: design (i) tracking ⇒ β ≥ ½ (Hilberdink Remark C);
  periodic design (ii) ⇒ abelian field or off-line Dirichlet zero. G: Lemma H; smallest undecided class S5(ρ), ρ ∈ (0.5, 1.3).
- Stopped per the brief (stop condition met; report before proving). Not run: S3, S4, 30-digit certification, proof of Lemma H (Untried UT-U1…U5).
