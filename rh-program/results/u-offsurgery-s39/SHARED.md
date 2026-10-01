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

## 11:21 IST 2026-10-01 — read-O block 1 (Opus reader, Session 40): own generator reproduces the 10⁹ run; C1 confirmed

- `verify-O/gen.c` (my own code from NOTE l. 54–56; exact integers for ρ = P/Q; push sieve; uint16 counts with overflow check). Control ρ = 1 to 10⁶: π(x) sites, no composites, N(n) = n.
- ρ = 4/5, X = 10⁹ (19 s, 2.06 GB; `verify-O/logs/gen_r08_1e9.log`): N(10⁹) = 800,000,008 (C(10⁹) = 8); 50,829,666 g-primes, all multiplicity 1; 46,758,777 composite; 4,070,889 of π(10⁹) = 50,847,534 primes accepted (92.0% refused); sup E = 274.8 at n = 902,538,000 = 2⁴·3²·5³·7·13·19·29, a_n = 276, E(n − 1) = −0.4; sup|ψ − x| = 7.35·10⁵; min E(n) = −0.4 at integers.
- C1's record list reproduces exactly (a_n = 124 @ 90,253,800; 155; 170; 178; 215; 209; 244; 276). Max a_n per decade 10⁴…10⁹: 8, 14, 27, 59, 124, 276 (local log₁₀ ratios 0.24, 0.29, 0.34, 0.32, 0.35).
- First composite g-primes: ρ = 4/5: 20, 30, 38, 57, 58, 82, 87, 110, 133, 150, 158, 178; ρ = 3/4: 15, 26, 35, 39, 51, 55, 74, 75, 87, 91, 95, 111. The NOTE's §0 list "15, 26, 35" (l. 15) belongs to ρ = 3/4, not 0.8.
- Observed and proved (single-check): at ρ = 4/5, m_n ≥ 1 forces A(n) = 0 and m_n = 1 (since E(n) ≥ −½ at every integer). Next: second generator by a different algorithm; carriers (C2); exact factorization counts (C3); the zero.

## 11:44 IST 2026-10-01 — read-O block 2: second generator agrees; C2, C3 (explicit values) confirmed exactly; the zero reproduces

- `verify-O/gen2.c` (pull recursion on the Ω-derivation identity Ω(n)a_n = Σ_{d|n} L(d)a_{n/d}, exact integers; a different algorithm from gen.c): identical sequence and g-prime hashes at every decade to 10⁸; every A(n) an integer.
- C2: refused primes < 200 at ρ = 4/5: 5, 19, 29, 41, 59, 61, 79, 89, 109, 139, 149, 163, 179, 181, 199; carriers of 5: 20, 30, 110, 150, 200, 245, 355, 370, 380, 455; of 19: 38, 57, 133, 247, 323, 380, … (C2's lists exact). No composite g-prime has only accepted prime factors (forced: such n has A(n) ≥ 1).
- C3 (`verify-O/fcount.c`, exact uint64 DP on the divisor lattice, g-primes ≤ 10⁹ from my own list): f(2⁵·3³·5⁴·7·11·13·19²·29·41) = 20,390 exactly (exp. 0.29998); f(2⁷·3⁵·5⁹·7²·11·13·17·19³·23·29²·37·41²·47) = 13,461,378,553 exactly (log₁₀ n = 30.4482, exp. 0.33267). Consequence (rigorous given the list): H_θ is FALSE for every θ ≤ 0.3227 (a_n − 0.8 > 2n^θ), in particular H_0.32; not for θ = 0.35 (2n^0.35 = 9.08·10¹⁰). The NOTE's envelope sup E ≤ 0.61x^0.30 extrapolated to that n is exceeded 16.2-fold.
- ρ = 21/20 at 10⁹: sup E = 475.05, sup|ψ − x| = 2.17·10⁶ (NOTE matches); max a_n = 174 there, so for ρ > 1 the sup of E is accumulated, not a single burst. ρ = 19/20: sup E = 177.45.
- Route 2 (`verify-O/zmom.c` Taylor moments at s₀ = 0.7659 + 30.326i, K = 28, + Euler–Maclaurin tail; validated against direct sums to 8·10⁻¹⁴): zero of F_X = 0.7658596 + 30.3260636i (3·10⁷), 0.7658709 + 30.3260583i (10⁸), 0.7658696 + 30.3260661i (3·10⁸), 0.7658722 + 30.3260650i (10⁹); |F′| = 2.032; winding 1 on ∂B (1600 pts/side, max phase step 0.0013 rad), min|F_X| = 0.039357 (10⁹), 0.039359 (10⁸). All digit-for-digit with the NOTE.

## 11:53 IST 2026-10-01 — read-O block 3: citations at the line; my own ascent; §1 written

- Citations opened at the line: Hilberdink 2005 (w-18a) Thm 1 l. 195, Cor. 2(b) l. 207–209, Remark B(ii) l. 228–232, Remark C l. 494–500 (faithful; Greek lost in extraction, reconstructs unambiguously); BDR z-02 l. 84–86 and l. 169–181 (faithful); BDR Thm 1.3 covers only ½ < α < ⅔, so NOTE l. 200 "needs β ≥ 2α/(α + 2) ≈ 0.55 at α = 0.77" applies it outside its range (minor); DMV p1-02 l. 203–207 (faithful); Hilberdink 2012 p3-22c2 abstract is at l. 42–50 of the extracted text (NOTE says l. 30–40; content faithful). Révész's "Ramanujan condition" (t-14b l. 464–476, Condition G) is an average moment condition; S5's membership in Révész–Pintz's class needs Axiom A + Condition G, both unproved (NOTE l. 204 "exactly S5's class" overstates; minor).
- My greedy ascent (`verify-O/ascent.c`, exact uint64 DP, the 3717 g-primes ≤ 10⁹ smooth over primes ≤ 61; start 902,538,000): exponent log f/log n = 0.2991 (log₁₀ n 14.30), 0.3139 (20.53), 0.3324 (30.32), 0.3333 (32.25), 0.3357 (34.45, f = 3.64·10¹¹ vs 2n^0.35 = 2.27·10¹²); marginal exponents 0.30–0.49 (the ×41 step: 0.4875). Still running.
- Frozen-bound tightness: at n₃ the count with g-primes ≤ B grows ×2.37, 1.31, 1.079, 1.020 per decade of B (10⁵ → 10⁹): the ≤ 10⁹ bound is plausibly within ~1% of a_{n₃}.
- 47-smooth census to 10⁹ (`verify-O/smooth_census.py`): smooth g-primes per decade 3, 15, 25, 66, 158, 239, 322, 438, 528 (still growing); admitted fraction of irreducible smooth integers 0.17 → 0.078.
- arXiv queries (https; one at a time, 7 s apart): Beurling ∧ greedy, Beurling ∧ integers ∧ prescribed, Beurling ∧ inverse ∧ primes: 0 hits each. Remaining queries running.
