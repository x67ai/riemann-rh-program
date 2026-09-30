# SHARED — seed N1 `ly-infinity` (novel-approach wave, Session 36)

Agent: Opus 5.5 (default effort). Folder: `results/novel-wave-s36/ly-infinity/`. Nothing here is committed by this agent.

---

## 2026-09-30 17:45 IST — unit 0: bootstrap

Read: WAVE-CHARTER.md (whole); STATUS.md 72–103; BARRIER-ZOO.md §0, I.1, III.15 (with riders), IV.1, IV.9, V.4, V.5; KICKSTART Part 2 items 10, 12; `results/ccm-dh-test/dh.py`.

First-pass derivation notes (to be checked by computation and at the page):
- Seed (1) re-derived: with z_p = p^{1/2-s}, Q(z) = prod(1 - p^{-1/2} z_p) restricts to E_S(s) = prod_{p in S}(1 - p^{-s}); Qtilde = prod(z_p - p^{-1/2}) restricts to P^{1/2-s} E_S(1-s). So f_pm(s) = E_S(s) pm P^{1/2-s} E_S(1-s) = E_S(s)(1 pm B(s)), B = prod of Blaschke factors b_p. Zeros on Re s = 1/2: yes. But the Lee-Yang lift adds nothing for product type: a product of one-variable Hermite-Biehler factors is Hermite-Biehler.
- Suspected ERRATUM (sign): E_S is the partial product of 1/zeta; the phase of B carries +2 pi S_X(t) while zeta's zeros sit at 2 theta(t) + 2 pi S(t) = pi mod 2 pi; the prime fluctuation enters with the OPPOSITE sign (anti-aligned). The zeta-aligned Lee-Yang product is prod(1 + p^{-s}) (Blaschke zero at -p^{-1/2}) or truncated geometric series per prime.
- Suspected no-go (to prove carefully): for ANY Lee-Yang polynomial p of multidegree m in prime variables, the restriction t -> p(p^{-it}) has |N(a,b) - W (b-a)/2pi| < |m|, W = sum m_p log p >= |m| log 2. So every nonconstant restriction has a zero in every interval of length > 2 pi / log 2 = 9.0647; Xi has none in (-14.13, 14.13). Hurwitz then forbids locally uniform convergence to Xi.

## 2026-09-30 18:20 IST — unit 1: prior art read at the page (on-disk corpus) + gap/discrepancy check

Sources extracted with `pdftotext -layout` into `sources/` from the corpus copies (fetched-r2 u-20b, u-24b, u-25a, u-27b, u-28b, u-30b, u-34b; fetched p2-18, p2-19b, y-33, y-34).
- Kurasov-Sarnak (arXiv:2004.05678v1, p.1): Guinand's explicit-formula example "does not give a Fourier quasicrystal, even assuming the Riemann hypothesis". => ERRATUM to seed step (4).
- Kurasov-Sarnak p.2: stable pairs; spectral pairs det(I - diag(P_j(z)) S), S unitary (their eq. (5)); p.6 Thm 1; p.6 eq (30) |arg P(z)| <= pi deg P.
- Alon-Vinzant (gap distributions), Thm 1.9 p.5: mu_{p,l}([x,x+T]) = <d,l>T/(2pi) + err, |err| <= |d|; every gap <= 2 pi |d|/<d,l>; tight (Remark 1.10). => the lemma of my no-go is PRIOR ART; the application to Xi is mine [novelty: single-check pending arXiv].
- Favorov arXiv:2311.02728 pp.1-3: zero sets of absolutely convergent Dirichlet series are almost periodic sets; almost periodic sets have a positive asymptotic density (Prop. 3). => infinite-rank density obstruction is prior art in substance.
- Goncalves arXiv:2312.11185v3 (26 Jan 2026): classification of Fourier summation pairs via Hermite-Biehler functions E with A/B almost periodic (Thm 3, Thm 4); Remark 6 p.11: under GRH the DIFFERENCE of the zero measures of two even primitive L-functions (same Gamma factor) is an FS-pair with spectrum {0} u {+-log n/2pi}, a(0) = log(N1/N2): the archimedean term cancels. Nearest published object for task (f).
- Goncalves p.2 quotes Dyson 2009's quasicrystal suggestion for RH (the seed's step (4) is Dyson's programme).

Computation `verify/k1_gap_theorem.py` (+ .log, 8.9 s): 33 Haar-random det(I - Z(t)U) in prime variables (1-8 variables, repeated primes allowed): worst |N - W L/2pi| <= 3.13 < |d| in every case; max gap <= 2 pi |d|/W in every case (one prime attains 9.0647 = 2 pi/log 2 exactly). Product-type seed and aligned combinations: same. Xi: gamma_1 = 14.1347251417347; interval (-gamma_1, gamma_1) length 28.2694 forces >= 3 zeros of EVERY nonconstant prime-variable LY restriction (N > |d|(L log2/2pi - 1) = 2.1186|d|). => no Hurwitz limit to Xi (theorem K1 in NOTE).

## 2026-09-30 19:05 IST — unit 2: arXiv prior-art search (export API, sequential, 3 s apart) + downloads + alignment numerics

Queries and hits: `verify/arxiv_search.py`, `verify/arxiv_search.log`, raw Atom in `sources/arxiv-queries/`. Zero hits for: "Fourier quasicrystal" AND (zeta OR Riemann); "crystalline measure" AND zeta; "stable polynomial" AND "Dirichlet series"; "Riemann hypothesis" AND "stable polynomials"; "Euler product" AND "Hermite-Biehler"; "real zeros" AND "Dirichlet polynomial" AND "functional equation". [novelty: single-check; V.5: absence is not evidence]
Downloaded + text (`sources/arxiv-*.txt`): Gonek 0704.3448; Burnol 1106.4749; Kuipers-Hummel-Richter 1307.6055; Favorov 2411.07190; Nakamura 2008.02570; Alon-Kummer 2507.16029.
Read at the page:
- Gonek 0704.3448 p.16: zeta_X(s) = P_X(s) + chi(s) conj(P_X(s)) is NON-ANALYTIC (bar lost in pdftotext; confirmed by p.17 proof of Thm 6.2 "zeros ... only occur ... where |chi(s)| = 1"); his "RH for zeta_X" (Thm 6.2) is by construction; p.16: the analytic version (35) zeta ~ P_X(s) + chi(s)P_X(1-s) "is not a good guess". Thm 8.1 p.27: under RH, if X < exp(C3 log t/Phi(t)) all zeros simple and phase monotone; Thm 9.1 p.33: under RH zeros of zeta_X converge to zeta's.
- Burnol 1106.4749 p.2: Hamburger's theorem verbatim (French): f meromorphic, finite order (=> finitely many poles), f = sum a_n n^-s abs. conv. Re s > 1, g = chi(s) f(1-s) a convergent Dirichlet series sum b_n n^-s for Re s >> 1 => f = c zeta.
- Nakamura 2008.02570 abstract p.1: f(s,chi) = q^s L(s,chi) + i^{-kappa} G(chi) L(s, conj chi) satisfies Riemann's FE (the one in Hamburger's theorem) for even chi; for NON-REAL chi it has infinitely many zeros OFF the line. Its frequencies are log(n/q), not log n => the RH-false control for the orchestrator's Hamburger acceptance test: the integer-lattice support is sharp.
- Kuipers-Hummel-Richter 1307.6055: quantum graphs with prime edge lengths reproducing zeta's oscillating density; the MINUS SIGN (Maslov phase) problem = my alignment erratum; "The smooth part is completely different, and hence also the spectrum" = the density obstruction, stated physically.

Alignment numerics `verify/b_alignment.py` (+ .log/.json): see log for T* = 1319.47 and 14514.16 (mean |nearest model zero - zeta zero| / mean spacing): gram 0.237/0.211; LY-seed 0.361/0.282 (WORSE than prime-free); LY-aligned 0.144/0.168 (better); arch-euler X=1000: 0.020/0.039, X=10^4: -/0.024; arch-anti and arch-sqfree at large X acquire EXTRA real zeros (non-monotone phase).

## 2026-09-30 19:50 IST — unit 3: alignment third height; Hamburger addendum checks; RH-false/RH-true controls

- `verify/b_alignment.log` third height T* = 188684.05 (S = {2..13}, 493 zeta zeros): gram 0.230; LY-seed 0.272 (worse); LY-aligned 0.183 (better); arch-euler X = 10^4: 0.037. Run stopped before the 4th height (T* ~ 3.2e6) to respect the 10-minute rule (noted in the log).
- `verify/f_hamburger_checks.py` (+ .log, 183 s): Nakamura's f(s,chi) = 7^s L(s,chi) + G(chi) L(s, conj chi), chi cubic mod 7 (even, non-real): Riemann's FE f(s) = chi(s) f(1-s) holds to 1.0e-30; 31 zeros with Re s != 1/2 in 0 < t < 45, e.g. 0.633567396172 + 1.601081706 i, 1.063645710 + 4.263045566 i, 0.863910648 + 8.705613632 i (|f| ~ 1e-31 at 30 digits). Support log(n/7): hypothesis (i) (integer lattice) fails. => the integer-lattice support in the acceptance test is sharp: relaxing it to a rescaled lattice admits RH-false functions with EXACTLY zeta's FE.
  Lee-Yang finite model: own FE (conductor P, no Gamma) residual 2e-32; Riemann FE residual 0.67 / 6.0 => (ii) fails. Archimedean analytic model A(s) + chi(s)A(1-s): Riemann FE residual 1e-31, but poles at s = 3, 5, 7 (|F(3 + 1e-6)| = 2.6e12, A(-2) = 65000 != 0: no trivial zeros) => (iii) fails.
- `verify/e_controls.py` (+ .log, 53 s): DH = c L(chi) + conj(c) L(conj chi), c = (1 - i kappa)/2 (check 6.4e-11 at 2+3i). Lift of the S-part: stable for S2 = {2,3} (reach 2 arctan sum 2.278 < pi - 2 arctan(kappa) = 2.588), UNSTABLE for S2 = {2,3,7} (zero at polyradius ~0.84). S-truncated DH has zeros with sigma > 1/2 already at X = 7 (0.633 + 85.780 i) converging to DH's off-line zero 0.808517 + 85.699348 i: distance 0.193 (X=7), 0.075 (30), 0.016 (1000), 0.0081 (X=10^4; zero 0.808501 + 85.707440 i). zeta's S-parts never vanish. => I.1 passed at the axiom level (the consumed input "the Bohr lift of every S-part is a product of one-variable stable factors" fails for DH at S2 = {2,3,7}), but the detector is blind to zeta's own zeros (its S-parts are zero-free for all S).
  F_{a,q}: local factor 1 + (a/sqrt q) z + z^2 Lee-Yang iff a <= 2 sqrt q; q=5,a=5 zeros at sigma = 0.2010, 0.7990; q=2,a=3 at sigma = 0, 1. RH-true: E/F_5 all a in [-4,4] Lee-Yang (rank 1, exact); genus-2 example Lee-Yang; non-curve (13, 8) not.
- Correction to my own preliminary estimate: the maximal argument of each Cayley factor over the disc is 2 arctan(p^{-1/2}) (not 2 arcsin); first unstable small S2 is {2,3,7}, not {2,3}.
