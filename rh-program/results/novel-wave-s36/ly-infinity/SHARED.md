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
