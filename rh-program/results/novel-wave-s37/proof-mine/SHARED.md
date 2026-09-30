# SHARED — seed M2 `proof-mine` (dated blocks, newest last)

## 2026-09-30 block 0 — launch
Read: WAVE-CHARTER.md (whole), tournament NOTE §2.1, tournament read-F.md. Folder created: NOTE.md skeleton, verify/, sources/.
Sources located on disk so far: Milne, "The Riemann hypothesis over finite fields: from Weil to the present day" (arXiv:1509.00797),
at `results/e3-borger-rung1/sources/milne-1509.00797.{pdf,txt}`; CCM 2009 at `fetched/y-07-…`. To fetch: Bombieri Bourbaki 430
(numdam), Deligne Weil I (numdam), Laumon 1987 (numdam), Weil 1949 (AMS), Kedlaya math/0210149, Hrushovski math/0406514,
a free Hasse-theorem text. Plan: baseline computations first (V, its formal twist, the control), then rows in batches of <= 5.

## 2026-09-30 block 1 — sources on disk, baseline and line computations
Fetched to `sources/` (log `verify/fetch_sources.log`): Bombieri Bourbaki 430 (numdam), Deligne Weil I (numdam), Laumon 1987 (numdam),
Kedlaya math/0210149v3, Hrushovski math/0406514v2, Sutherland 18.783 L7 + L8 (Hasse), Milne 1509.00797 (copied from e3), CCM math/0703392
(copied from fetched/y-07). NOT obtained: Weil 1949 BAMS (Cloudflare wall), Tao's blog (bad URL, dropped), Katz Weil II lectures, Stepanov 1969,
Mattuck-Tate 1958, Grothendieck 1958, Weil 1948a/b (all read only through Milne's survey at the page).
Computed (`verify/baseline.log`, `verify/lines.log`): V's N_n, b_d to 60; the control E0: y^2 = x^3 + 2x over F_5 (the unique short
Weierstrass curve with trace 4), counts to F_625 by brute force, twist checks over F_5 and F_25. The line numbers (NOTE §1 table):
deg(pi - 2) = -1; def(Gamma_pi - 2 Delta) = -2; formal index (2,2); Rosati trace -2; alpha^2 = 13.09 > q^{3/2}; twist over F_25 has 41 > 40.
Finding at the page: Bombieri 1973 p. 239 prints an RH-false formal example (omega1 = q, omega2 = 1, nu_r = 0) and says the upper bound
alone does NOT give RH; the lower bound needs a Galois cover and its twists (pp. 239-240). This contradicts the G-line of tournament
row T24 ("the tower over F_{q^n} upgrades the bound to RH") — flagged for the orchestrator; T24's verdict (DEAD) is not affected.

## 2026-09-30 block 2 — NOTE §1 and table rows R1–R5 written
§1: baseline + the six recurring numbers (for g = 1 the Hasse / Castelnuovo-Severi / Rosati numbers are ONE binary form, m^2 + tmn + qn^2,
= the norm form of Q(pi); V's is the norm form of Q(sqrt5) and takes -1 at pi - 2 = golden ratio). Rows: R1 Hasse (D), R2 Weil-Rosati (D;
V supplies Thm 1.30's Weil-pairing input, fails Thm 1.27), R3 Weil 1941/48a (A; fails at effectivity + the rational function Phi),
R4 Mattuck-Tate/Grothendieck (A; formal index (2,2)), R5 Stepanov/Schmidt (C; not read at the page -> carries no verdict; line = R6's).

## 2026-09-30 block 3 — table rows R6–R10 written
R6 Bombieri (C): Theorem 1 never separates V (a_r > 0 => N_r < 5^r + 1); the line is §III (separable t, Galois closure, twists): V's
formal twist over F_25 has 41 points vs (5) "< 41" and (7) "<= 40" — violated at the first admissible field; (8) as printed fails at 5^4.
R7 Deligne Weil I (B): (7.1) at X = C x C violated both sides (13.090 > 11.180; 1.910 < 2.236); family form: Rankin passes 2k=2, fails 2k=4.
R8 Laumon/Weil II (B): first object = a function to P^1 (Prop 4.3.2.1), then the Fourier family + purity criterion 4.2.1.3; number = the
conclusion of Cor 4.3.1.1 only (labeled). R9 Kedlaya (B): complete p-adic proof in print (abstract, at the page) = R8 transcribed;
Dwork = rationality only (V passes; not a proof of RH). R10 Davenport-Hasse/Weil 1949 (C, special curves): Gauss sums |g|^2 = 5 computed.
Bookkeeping: an append had landed after the §3/§4 placeholders; the placeholders were removed and §3/§4 will be appended at the end.

## 2026-09-30 block 4 — table rows R11–R14 written (table complete)
R11: modular/automorphic methods CONSUME RH for curves (Milne pp. 45-49 at the page: Hasse-Weil continuation for CM/modular curves over Q;
Ramanujan deduced from Weil); CM over F_q is class D. R12 CCM: Weil restated (A), Prop 6.2 = Weil's criterion. R13 Hrushovski: for curves
Weil's positivity (Ex. 11.4, p. 114), else consumes Deligne; e = -5 vs 4.472. R14: named-not-read list (Manin 1956, Igusa, Quigley, Roquette,
Kani, Weil II 1980, Stark, Stohr-Voloch). No proof found that V passes. Next: §3 (Z-analogs on the record), §4 (partition theorem, close).

## 2026-09-30 block 5 — §3 table (Z-analogs) written; Z-side computations
`verify/z_side.{py,log}`: Z1 zeta(sigma) < 0 at 99 grid points of (0,1) (proof elementary: eta alternating); Z2 #{n mod p^2: n^p = n} = p
for all 29 primes < 110 (Frobenius identity holds to FIRST order only over Z); Z3 log C(2n,n) / sum_{n<p<=2n} log p -> 2 log 2 = 1.386
(n = 10^3..10^6). Source added: Pritsker 2013 arXiv:1307.5361 (Gelfond-Schnirelman; t_Z[0,1] > 0.4213 > 1/e, Gorshkov 1956; Nair-Chudnovsky
0.99035; PNT by a sequence of weights OPEN, p. 4). Z-analog statuses: A refuted/RH-restated; B refuted/RH-restated; D refuted/RH-restated;
C: twists exist (and are unnecessary over Z), Frobenius-identity form refuted to first order, weak auxiliary integers exist, sharp form unbuilt.

## 2026-09-30 block 6 — CLOSE T
Theorem P (partition: A surface / B family / C coordinates / D group; each inequality violated by V at an explicit place, passed by E0;
hence no input is a function of the zeta datum) with proof, NOTE §4. Lemma Z4 (finite-support Chebyshev auxiliary integers have
kappa = A T/(T-1) > 1 strictly; c = mu gives lcm(1..x), RH restated): proved on the page, checked (Chebyshev 1.105550; C(2n,n) 1.386294).
One input not dead over Z: class C's integer-polynomial auxiliary object (Pritsker 2013 p. 4, PNT-strength open); cheapest unit: compute
Pritsker's B(w) for products of integer Chebyshev factors on [0,1]^n, n <= 6, and fit 1 - B(w_n); prior-art gate first.
`verify/twin_g2.{py,log}`: 111 genus-2 virtual curves over F_5 with NON-REAL off-line roots (N_n, b_d >= 0 to 40, h >= 1); V2 =
1 - u + 11u^2 - 5u^3 + 25u^4 violates Bombieri's one-sided Theorem 1 at Q = 5^6 (693 > 625) — caveat for the rung-1 twin rule: test
one-sided mechanisms on V2, not V. Flags for the orchestrator: T24 G-line (Bombieri p. 239); V sharpens Bombieri's example; twin-rule caveat.
Files: NOTE.md, SHARED.md, verify/{baseline,lines,z_side,twin_g2}.{py,log}, verify/fetch_sources.{sh,log}, sources/ (10 texts + PDFs).
