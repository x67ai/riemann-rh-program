# State of the Art on 12 RH Fronts (as of mid-August 2026)
(Compiled by a web-research agent, 2026-08-11. Verify arXiv ids marked as flagged.)

**Anchor context:** the Anthropic/Claude paper "More Than Two Thirds of the Zeros of the Riemann Zeta Function Are Simple and on the Critical Line" (released Aug 10, 2026) proves >= 67.250% of nontrivial zeros are simple and on the critical line, via Weil explicit formula -> Hermitian Gram-matrix compression -> Sylvester inertia -> rank-trace inequality with pair-correlation input; Lean 4 formalization with no sorrys; proven "bandwidth-one ceiling" ~0.68185 for the certificate class, with Fourier support ~1.04 / 1.26 / 1.70 needed to certify 70% / 80% / 90%. Validation: internal (Sumner, Alpoge, Furman) plus short-notice comments from Conrey and Goldston; no conventional peer review yet.

## 1. Proportion of zeros on the critical line / simple zeros
- Lineage: Selberg 1942 (positive proportion) -> Levinson 1974 (1/3) -> Conrey 1989 (2/5) -> Bui-Conrey-Young 2011 (41.05%) -> Feng 2012 (41.28%; debated) -> Pratt-Robles-Zaharescu-Zeindler 2020 (> 5/12 ~ 41.67% on line, > 40.7% on-line-and-simple; arXiv:1802.10521 flagged-from-memory). Stood until Aug 2026.
- Current best: the Anthropic 67.250% result (Aug 10, 2026). No published follow-up yet (one day old).
- Adjacent: Conrey, Farmer, Kwan, Lin, Turnage-Butterbaugh, "Short mollifiers of the Riemann zeta-function" (arXiv:2508.11108, Aug 2025) — variational optimization over combinations of derivatives; positive proportion regardless of mollifier length; more than doubles critical-line proportions for GL(2).
- Known pre-2026: >= 1/3 simple and on the line (per arXiv:2501.14545).

## 2. Zero-density estimates
- Guth-Maynard (arXiv:2405.20552, Annals 2025): N(sigma,T) << T^{30(1-sigma)/13+o(1)}; first improvement at sigma=3/4 in ~80 years; primes in intervals x^{17/30+o(1)}. Maynard-Pratt "Half-isolated zeros and zero-density estimates".
- Successors: Tao-Trudgian-Yang (arXiv:2501.16779) + ANTEDB exponent database (GitHub); Tao arXiv:2505.24017; arXiv:2509.04883 (beyond 17/30 for progressions); Guth survey arXiv:2503.07410; Turnage-Butterbaugh expository arXiv:2607.04632.
- Density Hypothesis (exponent 2(1-sigma)) open. Zero-density methods cannot certify 100%-on-line structurally.

## 3. Pair correlation / Montgomery's conjecture
- Montgomery 1973: under RH, F(alpha,T)=|alpha|+o(1) for |alpha|<=1; conjecturally F=1 for |alpha|>=1; RH+PCC => almost all zeros simple. Gallagher-Mueller 1978.
- Unconditional form factor: Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh, "An unconditional Montgomery Theorem for Pair Correlation of Zeros" (arXiv:2306.04799, 2023) — removes RH for |alpha|<1 (complex-zero form factor). Follow-ups: arXiv:2501.14545 (narrow-vertical-box hypothesis => 2/3 simple, 2/3 on line); Goldston-Suriajaya arXiv:2511.20059; arXiv:2603.28104 (zeta zeros in a narrow vertical box).
- PCC-only: Goldston-Lee-Schettler-Suriajaya arXiv:2503.15449 (Mar 2025): PCC alone, WITHOUT RH, implies 100% of zeros simple and on the line. Part II arXiv:2507.06823 (July 2025): the Alternative Hypothesis (AH) analysis.
- Conditional quantitative support: Carneiro-Milinovich-Ramos arXiv:2310.01913 (Math. Comp. 2024): under RH, long-interval average of F in [0.9303, 1.3208] via Cohn-Elkies (sphere-packing) Fourier optimization beyond bandlimited classes; sequel arXiv:2502.05106.

## 4. De Bruijn-Newman constant
- Rodgers-Tao (arXiv:1801.05914; Forum Math Pi 2020): Lambda >= 0. Polymath15: Lambda <= 0.22; Platt-Trudgian 2021: Lambda <= 0.2. Current interval: 0 <= Lambda <= 0.2, RH <=> Lambda = 0. No improvement 2023-2026.
- Adjacent: arXiv:2211.17269; arXiv:2602.20313 (Feb 2026, Polya frequency order of dBN kernel, certified failure at order five) — no new bound.
- Takeaway: Lambda >= 0 = "RH, if true, is barely true": no margin below criticality for smoothing/heat-flow shortcuts.

## 5. Weil positivity / explicit-formula positivity
- RH <=> positivity of Weil's quadratic functional. Bombieri (Lincei 2000): positivity unconditional for small support; genuine negativity once support reaches (1/p, p) — small-support cones can never certify RH.
- Connes-Consani, "Weil positivity and trace formula, the archimedean place" (arXiv:2006.13771; Selecta 2021): positivity at archimedean place via scaling action, prolate functions, Sonin space, Toeplitz control; full semilocal case would give RH. Connes-Moscovici arXiv:2112.05500 (PNAS 2022: UV prolate spectrum matches zeta zeros). Connes-Consani-Moscovici arXiv:2310.18423 (semilocal prolate wave operator). Connes survey arXiv:2602.04022 (Feb 2026).
- Computational: Groskin arXiv:2605.20224 (truncated Weil form Galerkin, first 10 zeros to 300+ digits), arXiv:2607.02828 (finite Guinand-Weil dictionary) — single-author, unrefereed.
- Bombieri-Garrett (arXiv:2002.07929): pseudo-Laplacian discrete spectra can contain at most ~94% of zeros (pair correlation + zeta(1+it) growth) — sharp no-go for that spectral route.
- Newest quantitative no-go: the Anthropic bandwidth-one ceiling (~0.68185).

## 6. Nyman-Beurling / Baez-Duarte
- RH <=> d_N^2 -> 0. Lower bound: d_N^2 >= (C+o(1))/log N (Baez-Duarte-Balazard-Landreau-Saias, Burnol). Bettin-Conrey-Farmer arXiv:1211.5191: under RH + zeta'(rho) moment bound, d_N^2 ~ (2+gamma-log 4pi)/log N. No unconditional upper bound o(1) known at all; 1/log N decay makes numerical certification hopeless.
- Recent: Alouges-Darses-Hillion (JTNB 2022); Darses-Hillion arXiv:2004.10086; Ehm arXiv:2405.06349 (closed-form NB Gram-matrix structure); arXiv:2606.16097 (unexamined). No breakthrough 2023-2026.

## 7. Hilbert-Polya spectral constructions
- Berry-Keating xp; Connes trace formula (Selecta 1999). Rigorous frontier: Connes-Consani-Moscovici prolate operator program (PNAS 2022 spectral realization).
- Bender-Brody-Mueller (PRL 2017): refuted as non-rigorous by Bellissard arXiv:1704.02644. Yakaboylu arXiv:2309.00405, arXiv:2408.15135: concedes key stage non-rigorous. Bagarello-Kuzel arXiv:2606.24405: rigorous operator theory, RH connection remains not understood. arXiv:2511.18309 (chiral adelic Dirac operator, unexamined).
- de Branges: Conrey-Li (IMRN 2000, arXiv:math/9812166) numerical counterexamples to the positivity conditions his approach requires. Suzuki arXiv:2301.00421 (2023): under RH the Weil-form Hilbert space IS a de Branges space (new RH equivalences).

## 8. Function-field / arithmetic-geometry transfer
- Weil 1948; Deligne 1974. Missing over Z: Hodge-index/Castelnuovo negativity on "Spec Z x Spec Z".
- Connes-Consani active: "Riemann-Roch for the ring Z" (CRAS 2024); "On the Jacobian of Spec Z" (JNCG 2026); "On the Absolute Geometry of Spec Z" (arXiv:2606.06604, June 2026) — absolute F1-curve as common origin of p-adic Hodge theory, the adelic scaling site, and the Fargues-Fontaine curve; GRR over Spec Z claimed.
- No global number-field shtuka theory; no credible IUT-adjacent progress.

## 9. Computational verification frontier
- Rigorous record: Platt-Trudgian arXiv:2004.09765 (Bull. LMS 2021): RH true up to height 3*10^12 (12,363,153,437,138 zeros, all simple, on line). Gourdon-Demichel 10^13 non-rigorous. "Twenty trillion" claims in 2026 secondary sources unverified — do not cite.
- Odlyzko sampling near 10^20-10^22; Bober-Hiary arXiv:1607.00709 (extreme heights ~10^30+). GUE discrepancies at finite height explained by arithmetic lower-order terms (Bogomolny-Bohigas-Leboeuf-Monastra; Berry) — understood, not RH-threatening.
- Lehmer pairs: first at t~7005.06/7005.10; Stopple arXiv:1508.05870; arXiv:2509.00906. Fed pre-Rodgers-Tao lower bounds on Lambda (Csordas-Smith-Varga).
- No serious counterexample-search program exists. Farmer, "Currently there are no reasons to doubt the Riemann Hypothesis" (arXiv:2211.11671, to appear Bull. AMS): rebuts doubt-arguments; computation cannot probe heights ~10^10000 where carrier-wave-driven near-failures would live.

## 10. Formal verification (Lean/Mathlib, 2026)
- PrimeNumberTheoremAnd (Kontorovich-Tao): PNT via Wiener-Ikehara done 2024; medium PNT stalled on complex-analysis infra.
- Math Inc "Gauss" agent (Sept 2025): Strong PNT (de la Vallee Poussin error term) in ~3 weeks, ~25k lines (math-inc/strongpnt).
- Mathlib: zeta continuation + functional equation, Dirichlet L-functions, Dirichlet's theorem. Zero-density and pair correlation NOT formalized anywhere except the Zeta23 artifact (largest RH-adjacent formalization ever).

## 11. No-go / obstruction results
- Parity problem (Selberg 1949; Tao 2007): sieve-only methods blocked from RH-strength (M(x) << x^{1/2+eps} <=> RH).
- Radziwill, "Limitations to mollifying zeta" (arXiv:1207.6583): intrinsic ceiling for Levinson-Conrey with one-piece arbitrary-length mollifiers; separately theta=4/7 mollifier-length barrier (Conrey via Deshouillers-Iwaniec).
- Bombieri-Garrett ~94% spectral cap (arXiv:2002.07929).
- Bandwidth barrier: F(alpha) known only on |alpha|<1 even under RH; the ALTERNATIVE HYPOTHESIS (zeros spaced in half-multiples of mean gap) is consistent with all bandwidth-1 data (arXiv:2507.06823) — pair-correlation-only methods cannot rule out a GUE-violating universe.
- Positivity-cone no-gos: Bombieri small-support; Conrey-Li vs de Branges; Lambda >= 0 (no margin).
- The Anthropic formalized no-gos: bandwidth-one ceiling 0.6818287; lemmaR_tight (two-moment certificate exhausted); dimension cap d = lambda*N; kappa(lambda) = 1/lambda + lambda/3 >= 2/sqrt(3) => two-moment certificates cap at 2 - 2/sqrt3 ~ 0.845 at ANY bandwidth; Davenport-Heilbronn/Epstein satisfy all the method's inputs with RH false => any RH-complete route needs input they violate (Euler product beyond L^2-means).

## 12. Claimed proofs/disproofs 2024-2026
- No claimed proof or disproof by an established analytic number theorist 2024-2026; consensus (Farmer BAMS) unchanged. Fringe claims: arXiv:2404.06306 (math.GM "disproof", no traction), arXiv:2509.16240, arXiv:2607.04338, assorted Zenodo/preprints.org — none refereed, none with traction.

## Additional campaign residue (from the 95-page transcript volume accompanying Zeta23)
- ~30 refuted attack routes; coordinator synthesis: "every attempted route's first substantive step turned out to be Weil positivity or an equivalent in disguise"; the only axiom set not barred by an explicit RH-false model is the full one (functional equation + Euler product at every prime + Ramanujan).
- Barrier-checker methodology: a zoo of RH-false model worlds (Epstein class number 2, Davenport-Heilbronn, Beurling systems with planted zeros, fake Weil polynomials) mechanically classifies proposed methods by which model kills them.
- Per-pair quadratic "integrality pricing" is FALSE (G1-G4 experiments); only the mass-linear rank-trace inequality survives. The (m-1)(m-2) spectral level is destroyed by interactions even under RH+GUE.
- Negative-index (Pontryagin) route to COUNTING off-line zeros is empty for structural reasons (visibility needs dim V >~ N(T)).
- Empirical e^{-4piX} Weil-positivity margin law, mechanism located in Connes-Consani prolate spheroidal eigenvalue leakage (positivity certified by interval arithmetic on supp [1/3,3], primes 2,3,5,7).
- Three thin-interval zero-density improvements from a dropped 1979 Heath-Brown lemma (confirmed by two internal referees, never written up).
- de Branges delta-tilt: K_a kernel has exactly kappa_a negative squares = N(beta>a) WITH multiplicity (multiplicity-visible, unlike the Weil form); identified d/da log|xi(a+it)/xi(1-a+it)| at a=1/2 with 2*pi*nu_X; making K_a compressions prime-computable is open.
- Lindelof lock: bounds for P_X on windows of length 1/log T would unlock the third moment and orthonormalization (sub-Lindelof short-window statement, never attacked directly).
