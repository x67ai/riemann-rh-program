# read-O — lemmaB-s41/U3-firstbound

Reader: Opus (claude-opus-5-5), second model of the dual-model check. Opened 18:49 IST 2026-10-01.
Target: `results/lemmaB-s41/U3-firstbound/NOTE.md`, SHA-256 f3dfc4539a5a58c879bb50de475450f7bd7c09ca6f94f6709edc67da1022d2b2,
243 lines (all line numbers below refer to this hash). Claim: N(x) = O(x) for S8(rho), every rho in (0, 1/2); Theorem T1':
E(x) <= 0.196413 (x - 1) for rho = pi/16 and E(x) <= 0.098198 (x - 1) for rho = pi/32, all x > 1.
Also read: READ-BRIEF-O.md (generic rules); lemmaB-s41/CHARTER.md (the unit's brief: there is no BRIEF.md in the folder);
free-greedy-s40/CHARTER.md §1; free-greedy-s40/theory/NOTE.md Lemmas 1.0-1.5, Prop. 2.1; ORCH-NOTES.md O9 and its correction
block; the unit's verify/ scripts and logs (read only, never imported). `read-F.md` and `verify-F/` not opened.
Re-run: `U3-firstbound/verify-O/` (own C generator, double-double arithmetic with certified ordering margins; own Python checks).

**VERDICT LINE: AGREES-WITH-CORRECTIONS.** The close stands as mathematics: identity (*), Lemmas B1, C1, D1, Corollary D2,
Lemmas E1, E1' and Theorems T1, T1' are re-derived at the line with no circularity (only (*), E > −1/2, E = +1/2 at g-primes,
lattice spacing and infinitude of g-primes are used; rho < 1/2 enters only in C1, and in D2 for T1); T1' holds for ALL x > 1,
the initial range being covered by a finite run whose every placement decision I certified independently (own double-double
generator); every number reproduces (rho + 2eps0/D0 = 0.19641319 for pi/16, 0.09819826 for pi/32). Corrections: the
qualitative T1 is in print once D2 is known — Diamond–Zhang Thm 6.13, p. 61 (psi1(x) <= log x + O(1) ⇒ N ≪ x) — so the new
content is the Mertens bound D2 for S8 and the sharp explicit constant of T1' (F1); Cor. 1.9's lower half is DZ Thm 4.7 /
Cor. 8.7 (F2); §2's "class R cannot yield T2" rests in part (c) on data (F3); the headline constants are printed rounded DOWN
below what is proved (F4); §1.6 with early placement needs pi(x) = O(x), one-line fix given (F5). Total: 5 FIX-FIRST items
(8 pairs) and 6 minor items (7 pairs), 15 pairs in all.

## §1 Re-derivations at the line

**1.A Identity (A1) and (*) (NOTE l. 61-74) — ✓.** For a multiset n of g-primes, log n = Σ_p a_p log p = Σ over pairs (p, j),
1 <= j <= a_p, of log p = Σ_{d | n} Λ(d) (d = p^j as a sub-multiset). Swapping sums, Σ_{n<=x} log n = Σ_d Λ(d)·#{m : d·m <= x} =
Σ_d Λ(d) N(x/d) (n = d ∪ m is a bijection of multisets; no freeness of real values used, ties and coincident values allowed).
LHS by Stieltjes = N(x) log x − ∫_1^x N du/u; with N = rho(u−1) + 1 + E: ∫_1^x N du/u = rho(x−1) − rho log x + log x + ∫E du/u,
so LHS = rho x log x − rho(x−1) + E(x) log x − ∫_1^x E du/u. RHS = rho x S + (1−rho) psi + Σ Λ(d)E(x/d), and S = psi/x + Psi~
(Stieltjes; psi = 0 on [1, p1)), so rho x S + (1−rho)psi = psi + rho x Psi~. Equating gives (*) exactly as at l. 72. Delta-form
(l. 74): psi + rho x Psi~ − rho x(log x − 1) = (1−rho)psi − rho x Delta ✓; and with Psi~ = log x − 1 − D it is psi − rho x D.
Numerical check with my own generator at three x: §2.

**1.B Lemma B1 (l. 77-84) — ✓.** At a g-prime y: E(y) = 1/2 (s40 Lemma 1.0(ii); holds for every rho, ties included, since by
1.0(i) no element of G_k sits at p_{k+1}). E > −1/2 everywhere (s40 Lemma 1.1) gives −∫_1^y E du/u < (1/2) log y, so
LHS(*) < log y; and E(y/d) > −1/2 for all d <= y gives Σ Λ(d)E(y/d) > −psi(y)/2, so RHS(*) > psi/2 + rho y Psi~ −
rho y(log y − 1) − rho = y F(y) − rho. Hence F(y) < (log y + rho)/y (strict). Delta-form: F = (1/2 − rho)psi/x − rho Delta ✓
(ρPsi~ = rho(log x − 1 − Delta − psi/x)). Also F = psi/(2x) − rho D (used in T1'). Both one-sided facts enter, as the NOTE says.

**1.C Lemma C1 (l. 88-99) — ✓.** Between prime powers dF/dx = −psi/(2x²) + rho psi/x² − rho/x = −(1/2 − rho)psi/x² − rho/x < 0
(this is the first use of rho < 1/2); F jumps by Λ(d)/(2d) at each prime power (Psi~ is continuous). On (P, x], P the last g-prime
<= x, the prime powers are p^j, j >= 2, p^j > P, so F(x) <= F(P) + T(P)/2 <= eta(P) + T(P)/2 by B1 at P. T(0) <= Σ_k log x_k/(x_k(x_k−1))
< ∞ because S8's g-primes are DISTINCT lattice points (s40 Lemma 1.2); T(z) decreases to 0. eta' < 0 iff log z > 1 − rho; the
three-interval check p1 = 1 + 1/(2rho) > e^{1−rho} on (0, 1/2) is right (both sides decrease in rho; the endpoint values
e, 2.25, 2 against e^{1−rho} <= e, e^{.709} = 2.032, e^{.6} = 1.822 hold on the stated pieces). So eps(x) = eta(P(x)) + T(P(x))/2 is
nonincreasing and → 0 (infinitely many g-primes: s40 1.0(i) gives p_{k+1} < ∞ for every k; the NOTE's (L4) argument is also fine).
(L4) uses N_k(x) <= Π(1 + log x/log p_i): ✓ (each exponent e_i of a product <= x has p_i^{e_i} <= x, p_i > 1).

**1.D Lemma D1 and Corollary D2 (l. 101-113) — ✓.** g(t) = Psi~(e^t) is continuous, piecewise C¹, g' = psi(e^t)/e^t, and
F = g'/2 + rho g − rho(t − 1); C1 gives (e^{2rho t}g)' <= 2rho e^{2rho t}(t − 1) + 2e^{2rho t}eps a.e.; g is absolutely continuous, so
integration on [t0, t] is legitimate; d/ds[e^{2rho s}(s − 1 − 1/(2rho))] = 2rho e^{2rho s}(s − 1) ✓; D = t − 1 − g turns the result
into the display at l. 103 (g(t0) − t0 + 1 = −D(t0)) ✓. Liminf: split at t/2, ✓ (needs sqrt x >= p1, true eventually). The
"convex combination" form used in §1.7-1.8 is also right: with lambda = (X0/x)^{2rho} and 2∫_{t0}^t e^{2rho(s−t)}eps <= (1 − lambda)eps0/rho,
D(x) >= lambda D(X0) + (1 − lambda)(1/(2rho) − eps0/rho) >= min{D(X0), 1/(2rho) − eps0/rho}. D2: Delta = D − psi/x and (C2) give
Delta(1 + rho/(1/2 − rho)) >= D − eps/(1/2 − rho); 1 + rho/(1/2 − rho) = 1/(1 − 2rho) ✓ (no sign condition on Delta is needed).
Hence S <= log x − 1/(2rho) + o(1) ✓. No circularity: only (*), (L1), (L2), lattice spacing and infinitude of g-primes are used.

**1.E Lemma E1, "records exist", Theorem T1 (l. 116-132) — ✓.** E(u) <= A u on [1, x] gives LHS(*) >= A x log x − A(x − 1) and
Σ Λ(d)E(x/d) <= A x S (all x/d in [1, x]; the bound is lossy at x/d < p1, where E < 0, but valid). Cancelling gives
(A + rho)x Delta <= (1 − rho)psi − rho − A, i.e. l. 117 ✓. Records: E(u) + rho u = N(u) − 1 + rho > 0, so E(u)/u (and, for
u >= p1, E(u)/(u − 1), since E(u) + rho(u − 1) = N(u) − 1 >= 1) is strictly decreasing on every piece between g-integers: the sup
over [1, x] is a maximum over finitely many left ends ✓. T1: at a record u* > X0 with A > 0, eps(u*) <= eps0 (eps
nonincreasing), Delta(u*) >= Delta0 > 0 (D2 + D1), and (A + rho)Delta <= (1 − rho)(rho Delta + eps0)/(1/2 − rho) gives
A <= rho/(1 − 2rho) + 2(1 − rho)eps0/((1 − 2rho)Delta0) (2rho(1 − rho)/(1 − 2rho) − rho = rho/(1 − 2rho) ✓). The constant in the
table (0.32346 for pi/16 = 0.32332 + 1.4·10⁻⁴) is consistent with the formula.

**1.F Lemma E1' and Theorem T1' (l. 169-184) — ✓ with one missing hypothesis (minor m1).** E(u) <= A(u − 1) on [1, x]:
LHS(*) >= A(x − 1)log x − A(x − 1 − log x) = A x log x − A(x − 1) ✓; Σ Λ(d)E(x/d) <= A(xS − psi) ✓; first part of RHS(*) =
psi − rho x D − rho ✓; with xS = x(log x − 1 − Delta) and x Delta + psi = x D: A(1 + xD) <= psi − rho x D − rho ✓ (l. 170).
The displayed consequence "A <= max{0, psi/(xD) − rho}" (l. 171) needs D(x) > 0: if D(x) < 0 < 1 + xD it would assert A <= 0,
which does not follow. With D > 0 and A > 0: A xD < A(1 + xD) <= psi − rho x D − rho, so A < psi/(xD) − rho ✓. T1' applies it
only where D >= D0 > 0, so the theorem is unaffected. In T1' the Mertens corollary D2 is not needed: C1 in the form
psi/x <= 2rho D + 2eps (F = psi/(2x) − rho D) gives psi/(xD) − rho <= rho + 2eps/D <= rho + 2eps0/D0 ✓. So T1' is proved for
every rho in (0, 1/2), for ALL x > 1, given (i) the exact value sup_{1<u<=X0} E(u)/(u − 1) and (ii) a valid eps0 and D(X0).
Where rho < 1/2 is used: only in C1 (F decreasing between prime powers; eta decreasing from p1) and, for T1, in D2.
Where E = +1/2 at a g-prime is used: only in B1. Where E > −1/2 is used: B1 (twice). Nothing assumes N = O(x), a bound on psi,
or convergence of an integral of E: every quantity is a finite sum at finite x. The initial range is covered by (i) exactly
(T1' is "for all x > 1", not "for x >= X0").

## §2 Independent re-run (verify-O/s8gen.c; logs verify-O/logs/s8gen_*.log)
Own C generator written from the s40 charter definition (no unit script imported or copied). Double-double arithmetic (fma
two-product), SEGMENTED exact sweep: all composites in (B(Ma), B(Mb)] are generated before any decision in that range, which is
legitimate because B(Mb) < p1·B(Ma) forces every factor below B(Ma); B(M) = 1 + M t are lattice MIDPOINTS (no boundary
ambiguity). Each composite c is located against the lattice by u(c) = (c − 1)rho + 1/2 in double-double; the minimum distance
of any composite to a lattice point is 9.4·10⁻⁸ lattice units (pi/16, 4.10·10⁶ composites) and 2.3·10⁻⁶ (pi/32), against a
double-double error below 10⁻²² units: every placement decision to 3·10⁷ is certified, and no two composites coincide
(0 pairs closer than 10⁻²² relative). Rule: a g-prime at x_k iff N(x_k−) = k (with an assertion that N(x_k−) < k never occurs).
Generator control: rho = pi/4, X = 10⁶ gives N = 785,400, pi_P = 78,134, sup E = 39.53, first g-primes 1.6366, 4.1831, 6.7296,
10.5493, 15.6423, 16.9155 — the s40 charter's and theory NOTE's values. Runtime 0.6 s, 254 MB, for pi/16 to 3·10⁷.

| quantity | NOTE (pi/16) | read-O (pi/16) | NOTE (pi/32) | read-O (pi/32) |
|---|---|---|---|---|
| sup_{1<u<=3e7} E/(u−1), at | rho at p1 = 3.5465 | 0.1963495408 = rho at 3.546479 | rho at p1 = 6.0930 | 0.0981747704 = rho at 6.092958 |
| next largest, at | 0.0655 (u = 8.64) | 0.065450 (8.6394) | 0.0402 (37.1) | 0.040237 (37.1241) |
| sup_{u<=3e7} E/u | 0.14099 | 0.140985 | 0.08206 | 0.082062 |
| max over g-primes of F(y) − eta(y) (B1) | −0.221 | −0.221148 | −0.155 | −0.155243 |
| D(X0) | 4.596 | 4.595645 | 7.741 | 7.740841 |
| eps0 = eta(P0) + T(P0)/2 | 8.1·10⁻⁵ | 8.10261·10⁻⁵ (P0 = 29999951.4685) | 6.0·10⁻⁵ | 5.98115·10⁻⁵ (P0 = 29999984.5728) |
| Delta0 | 1.546 | 1.546066 | 4.092 | 4.092349 |
| T1 record bound | 0.32346 | 0.323454 | 0.12220 | 0.122194 |
| T1' constant rho + 2eps0/D0 | 0.196413 | 0.19641319 | 0.098198 | 0.09819826 |
| N(x) <= (.)(x − 1) + 1 | 0.392763 | 0.39276273 | 0.196373 | 0.19637303 |

Also reproduced: N(10⁶) = 196,350 and sup E = 9.6362, 12.8385 at 10⁶, 10⁷ (pi/16); 6.3931, 8.9279 (pi/32) — O7's values;
Σ_{p<=x}1/p − log log x = −0.867, −0.995, −1.054, −1.082, −1.096, −1.103 (pi/16, 10²…10⁷) and −1.170 … −1.687 (pi/32), as at
NOTE l. 222-223. Every number the close rests on reproduces to the digits printed, EXCEPT that two printed constants are
rounded DOWN below what the proof gives (0.098198 < 0.09819826; 0.196413 < 0.19641319; "rho + 6.3·10⁻⁵" for 6.365·10⁻⁵, "rho
+ 2.3·10⁻⁵" for 2.349·10⁻⁵; "+ 0.80", "+ 0.90" for 1 − rho = 0.8037, 0.9018 in the §1.7 table): minor m2, m3.

**Identity (*) at three x with my generator (target (a)).** LHS − RHS = −4.6·10⁻¹⁴, −4.4·10⁻¹¹, −1.2·10⁻⁷ at x = 1000.5,
123456.7, 9876543.21 (pi/16; terms of size x log x ≈ 1.6·10⁸, so relative 10⁻¹⁵), and 5.0·10⁻¹⁴, −1.5·10⁻¹¹, −2.0·10⁻⁸
(pi/32); (A1) Σ log n = Σ Λ(d)N(x/d) to 10⁻¹³ at all six points. ∫E du/u computed exactly piece by piece.

**Robustness of the certificate.** The finite run enters T1' only through sup_{1<u<=X0} E/(u − 1) (attained at p1, where
nothing depends on the run), P0, D(X0) (it enters only through D0 = min{D(X0), 1/(2rho) − eps0/rho}, and D(X0) exceeds the
second entry by 2.05 and 2.65) and T(P0). Replacing T(P0) by the same sum over ALL lattice points (a bound valid for any set
of g-primes on the lattice) gives eps0 <= 1.766·10⁻⁴ and 8.85·10⁻⁵ and T1' constants rho + 1.39·10⁻⁴ and rho + 3.48·10⁻⁵:
the theorem's constants do not hinge on fine details of the 3·10⁷ run.

**1.G §1.6, threshold-tau variants with early placement (l. 139-152) — ✓ with one unproved input (minor m4).** (L1') E > −tau:
D reaches tau only at a placement instant, after which it is tau − 1, so D < tau at every point ✓. (L2') E(y) <= 1 − tau + rho w:
at a placement at y the deficit time y* <= y + w has D(y*−) = tau in the continuation, and D rises at most at slope rho, so
D(y−) >= tau − rho w; this survives SEVERAL placements at one point (each needs the current D >= tau − rho w), so
E(y) = 1 − D(y−) + (k − 1) <= 1 − tau + rho w ✓. B1_tau, C1_tau (dF_tau/dx = −(1 − tau − rho)psi/x² − rho/x, jumps (1 − tau)Λ(d)/d),
D1_tau (kappa = rho/(1 − tau), particular solution t − 1 − (1 − tau)/rho), D2_tau (Delta >= (r0/(1 − tau))D − eps/(1 − tau)) and the
final constant rho tau/(1 − rho − tau) all re-derived ✓; T1'_tau: rho tau/(1 − tau) + eps0/((1 − tau)D0) ✓ (l. 179). The unproved
input: C1 needs T(0) = Σ_p log p/(p(p − 1)) < ∞, which the NOTE gets from "distinct lattice points" (l. 90-91) — false for early
placement (positions leave the lattice; if rho w >= 1 several g-primes may sit at one point). Fix (proved here): between two
placements D must climb from <= tau − 1 back to >= tau − rho w, and composites only lower D, so m placements in [a, b] force
tau − rho w <= tau − (m − 1) + rho(b − a): pi(b) − pi(a−) <= rho(b − a) + rho w + 1. Hence pi(x) = O(x) and T(0) < ∞ by partial
summation. Also eta_w is decreasing only for log z > 1 − rho/(1 + rho w) (p1 = 1 + tau/rho can lie below that, e.g. 1.509 for
tau = 0.1, rho = pi/16), so "eps nonincreasing" holds from such z on — enough for T1 at large X0, which is how §1.7 uses it.
Numerics: my generator with tau = 0.1, rho = pi/16, X = 10⁷ (logs/s8gen_pi16_tau01_1e7.log) gives sup E/u = 0.767818 at
u = 2.277974 (= p1²), eps0 = 1.6105·10⁻⁴, D(X0) = 8.024009, Delta0 = 3.582842, record bound 0.027956, early sup E/(u − 1) =
1.7671459 at 1.509296, large-record bound 0.021856 — the NOTE's row and §2.4 values (0.76782, 1.6·10⁻⁴, 8.024, 3.583, 0.02796;
1.7671, ≤ 0.0219) ✓.

**1.H Corollary 1.9 (l. 209-226) — ✓.** (a) D1 started at p1 and D2 give Delta >= −K on [p1, ∞), so S <= log y + c2 for all
y >= 1; Σ_{p<=x}1/p <= ∫_{[p1,x]} dS/log u by partial summation ✓. (b) Σ_{n<=X} n^{−σ} >= σ∫_1^X N u^{−σ−1}du, so
zeta_P(σ) >= rho/(σ − 1) + 1/2 in [0, ∞] without any a-priori convergence (T1 is not needed); the Euler product holds in [0, ∞]
for a free monoid of multisets (Tonelli), Σ_p p^{−σ} < ∞ by the lattice; p^{−kσ}/k <= p^{−k} gives log zeta <= Σ p^{−σ} + T2 ✓;
the tail: p^{−σ} = (log p/p) f(p), f decreasing, −f(x)S(x) <= 0, ∫_x^∞ S(−f') <= (log x + c2)f(x) + ∫_x^∞ f du/u ✓, f(x)log x = 1/e,
∫_x^∞ f du/u = E1(1) at σ = 1 + 1/log x ✓. My floor: T2 <= 0.135614 (pi/16), 0.040153 (pi/32), so log rho − T2 − 1/e − E1(1) =
−2.3507, −2.9484; the NOTE's −2.354, −2.951 are slightly lower, hence also valid. Both halves are in print once D2 is known (§3).

**1.I §2, the class theorem (l. 186-207, 228-242) — (a) ✓ but tautological; (b) GAP, closable (my A2); (c) not proved.**
Class R is defined at l. 32-33 as "(*) at a point, with scale-proportional upper bounds A(v − 1) or Av at the lower scales and
ANY information on psi, S" — not precise: it does not say whether the comparison must hold on all of [1, x] (it must, for (a))
or only on [X, x] with true values below X (the restart of (c), §2.5(i)). (a) A bound E(v) <= A(v − 1) valid at v = p1 forces
A >= rho (E(p1) = 1/2, p1 − 1 = 1/(2rho)) ✓ — but this says only that a UNIFORM linear bound from v = 1 cannot be o(x); it is
a statement about the global supremum, not about the method's reach. (b) §2.3(i) ✓ given psi(x) > x^theta log x, which the NOTE
supports by data ("on data psi(x) ≈ 0.93x", l. 203); it is provable for every theta < 1 and all large x (addition A2). (c) "R stops at
psi/(xD) − rho = −W/D + O(log x/x) ≈ +0.010-0.014" is data: the identity Q(y) = (1/2)log y − ∫E du/u + rho − Σ Λ(d)E(y/d) at a
g-prime (l. 188) is exact ✓ (and Q' = −rho(Delta + 1) between prime powers ✓), but "−W(y) + O(log y/y)" needs ∫_1^y E du/u =
O(log y), which is not proved (only −∫E/u < (1/2)log y and, by T1', ∫E/u <= (rho + δ)y are); and the sign of W at large scales
needs the distribution of psi in (y/2, y], which the NOTE itself calls unknown (l. 151). So §0's "proof class R cannot yield it
(§2) ... Because (a) ..., (b) ..., (c) ..." overstates: (a), (b) are proved (b after A2), (c) is an observation [computed].
My re-run reproduces the data in (c): psi/(xD) − rho = 0.019170, 0.013484, 0.013293 and W = −0.0585, −0.0569, −0.0605 at
x = 10³, 1.2·10⁵, 9.9·10⁶ (pi/16); 0.0053, 0.0074, 0.0073 and −0.024, −0.047, −0.055 (pi/32). §2.3(ii) "b < 0 is beaten at
u = 1" holds only for b < −A (b in [−A, 0) is admissible; b = −A is (iii)) — minor m5.

## §3 Prior art at the page
Source on disk: Diamond–Zhang, *Beurling Generalized Numbers*, AMS Surveys 213 (2016), text at
`results/dz-half-s39/sources/t-50-diamond-zhang-2016-book.txt` (grep "Chebyshev": 134 hits, "Mertens": 43). Opened at the line.
- **Theorem 6.13, p. 61 (l. 3633-3680) [quoted]:** "Suppose that the Chebyshev function ψ(x) of a g-number system satisfies the
  one-sided Mertens-type inequality (6.13) ψ1(x) := ∫_1^x u^{−1}dψ(u) <= log x + O(1). Then the associated g-integers satisfy
  N(x) ≪ x." Proof: if psi = 0 below A >= 3 and ∫_A^x u^{−1}dψ <= log x − 1, Chebyshev's identity L dN = dψ ∗ dN and induction on
  [A^n, A^{n+1}) give N(x) <= x for all x; the general case removes the g-primes below a suitable A and uses Prop. 6.3 (non-explicit
  constant). ψ1 is the NOTE's S. Since Cor. D2 with D1 started at X0 = p1 gives S(x) <= log x + c2 for every x >= 1 (as the NOTE
  itself uses in Cor. 1.9(a), l. 212), **N(x) = O(x) for S8(rho), 0 < rho < 1/2, is D2 + DZ Thm 6.13; Step E is not needed for the
  qualitative T1.** DZ's induction and the NOTE's record inequality E1 are two forms of the same Chebyshev-identity bootstrap.
  What DZ does not give: the Mertens bound D2 for S8 (its proof, B1 → C1 → D1, is where the greedy rule enters), and the sharp
  constant of T1' (records of E(u)/(u − 1) beyond X0 are <= rho + 2eps0/D0; DZ's general case gives no usable constant).
- **Theorem 6.5, p. 57 (l. 3389-3405) [quoted]:** finite upper residue + Chebyshev upper bound pi(x) ≪ x/log x ⇒ N ≪ x. Not
  applicable to S8 with what is proved (psi = O(x) is open, NOTE l. 226).
- **Theorem 4.7, p. 33 (l. 2039-2046) [quoted]:** positive lower log density ⇒ ∫_1^x u^{−1}dΠ >= log log ex − M; **Corollary 8.7,
  p. 81 (l. 4785-4800) [quoted]:** for discrete g-primes with positive lower log density and ∫u^{−2}dΠ < ∞, Σ_{p<=x}1/p >=
  log log x + O(1). S8 has positive lower log density (E > −1/2 gives N >= rho(x − 1) + 1/2) and ∫u^{−2}dΠ < ∞ (lattice): the
  lower half of Cor. 1.9 is in print; the upper half is partial summation from D2. **Prop. 4.5, p. 31 (l. 1944-1950) [quoted]:**
  ∫dΠ/u <= log log ex + O(1) ⇒ O-log density.
- **Proposition 9.8, p. 90 (l. 5312-5316) [quoted]:** O-log density ⇒ liminf pi(x)log x/x <= 1; positive lower log density ⇒
  limsup >= 1. Applies to S8 (addition A3).
- Diamond 1970 / DZ Thm 9.9-Cor. 9.10 (p. 91, l. 5340-5360) [quoted]: Chebyshev bounds from N(x) = Ax + O(x log^{−γ}x), γ > 1 —
  hypotheses far beyond what S8 is known to satisfy; not relevant to T1.
- The greedy rule itself: not in print per the s40 prior-art log (`free-greedy-s40/theory/sources/prior-art-log.txt` Q1, l. 507;
  arXiv "all:Beurling AND all:greedy" → 0). So statements ABOUT S8 are new as statements; their cores are as above.
- Is T1 a consequence of a printed theorem "once E > −1/2 is known" (target f)? No: E > −1/2 alone is a LOWER bound and is
  compatible with N(x)/x → ∞ (any system with N(x) >= rho(x − 1) + 1/2, e.g. one with more g-primes); every printed O-density
  criterion in DZ Ch. 6 needs an upper bound on the primes. The upper bound needed by DZ 6.13 is exactly D2, which the NOTE
  proves from E = +1/2 at g-primes AND E > −1/2. So: T1 = (NOTE's D2) + (DZ Thm 6.13).
- arXiv (API, 3 queries, results in `verify-O/sources/q1-q3.xml`): abs:Beurling AND abs:"O-density" → 0; abs:Beurling AND
  abs:Mertens → 1 (2511.14736, bounded arithmetic functions; off-topic); abs:Beurling AND abs:Chebyshev → 5, of which Vindas
  1201.1405 and 1205.4281 and Tranoy–Vindas 2602.07690 give Chebyshev bounds (psi ≪ x) from L¹ / O(x/log x) conditions on
  N − ax (abstracts read) — the opposite direction, with hypotheses S8 is not known to satisfy. Nothing closer than DZ 6.13.

## §4 FIX-FIRST pairs (5 items, 8 pairs)
**F1 — missed prior art changes the novelty label of T1 (l. 20).**
OLD: **(T1) holds, proof in §1 (Theorem T1 §1.5, sharper Theorem T1' §1.8) [proved here; novelty: single-check, prior art not searched].**
NEW: **(T1) holds, proof in §1 (Theorem T1 §1.5, sharper Theorem T1' §1.8) [proved here; novelty: the qualitative N(x) = O(x) is new as a statement on a printed core — it follows from Corollary D2 (S(x) ≤ log x + O(1) for all x ≥ 1) and Diamond–Zhang, Beurling Generalized Numbers (2016), Thm 6.13, p. 61 (ψ1(x) ≤ log x + O(1) ⇒ N(x) ≪ x); new here: the Mertens upper bound D2 for S8 (Lemmas B1, C1, D1, where the greedy rule enters) and the explicit constant of T1' (records ≤ rho + 2eps0/D0), which DZ's proof does not give].**

**F2 — missed prior art for Corollary 1.9 (l. 31).**
OLD: **Corollary (§1.9):** Σ_{p≤x} 1/p = log log x + O(1) for S8(rho), rho < 1/2.
NEW: **Corollary (§1.9):** Σ_{p≤x} 1/p = log log x + O(1) for S8(rho), rho < 1/2 [lower half in print: Diamond–Zhang Thm 4.7 p. 33 and Cor. 8.7 p. 81, whose hypotheses S8 meets (positive lower log density from E > −1/2; ∫u^{−2}dΠ < ∞ from the lattice); upper half: partial summation from D2].

**F3 — the class statement of §0 rests on data in part (c) (l. 32, l. 37).**
OLD: **(T2) is not obtained; proof class R cannot yield it (§2):** class R = "the Chebyshev identity (*) at a point, with scale-
NEW: **(T2) is not obtained; a uniform linear comparison cannot yield it, and the restarted record method stops at a positive ceiling on data (§2):** class R = "the Chebyshev identity (*) at a point, with scale-
OLD: which is dominated by the bounded scales where E(v) = −rho(v − 1) < 0 (≈ +0.010–0.014 on data for π/16). GAP (T2), exact: a lower
NEW: which is dominated by the bounded scales where E(v) = −rho(v − 1) < 0 (≈ +0.010–0.014 on data for π/16) [computed, not proved: it needs ∫_1^x E du/u = O(log x) and the distribution of psi in (x/2, x], neither of which is proved; (a) is proved, and (b) for all large x via Cor. 1.9 (read-O A2)]. GAP (T2), exact: a lower

**F4 — the headline constants are rounded DOWN below what the proof gives (l. 23, l. 24, l. 182).** Proved values (read-O §2,
reproducing the unit's own logs): rho + 2eps0/D0 = 0.19641319 (pi/16), 0.09819826 (pi/32).
OLD:   **S8(π/16): E(x) ≤ 0.196413·(x − 1), i.e. N(x) ≤ 0.392763·(x − 1) + 1, for all x > 1;**
NEW:   **S8(π/16): E(x) ≤ 0.1964132·(x − 1), i.e. N(x) ≤ 0.3927628·(x − 1) + 1, for all x > 1;**
OLD:   **S8(π/32): E(x) ≤ 0.098198·(x − 1), i.e. N(x) ≤ 0.196373·(x − 1) + 1, for all x > 1**
NEW:   **S8(π/32): E(x) ≤ 0.0981983·(x − 1), i.e. N(x) ≤ 0.1963731·(x − 1) + 1, for all x > 1**
OLD (l. 182, from "Hence"): Hence **E(x) ≤ (rho + 6.3·10⁻⁵)(x − 1) for S8(π/16), E(x) ≤ (rho + 2.3·10⁻⁵)(x − 1) for
NEW: Hence **E(x) ≤ (rho + 6.37·10⁻⁵)(x − 1) for S8(π/16), E(x) ≤ (rho + 2.35·10⁻⁵)(x − 1) for

**F5 — §1.6's T1 for early placement uses T(0) < ∞ from the lattice, which early placement leaves (l. 148).**
OLD: So T1 holds for every S8_{tau,w} with rho + tau < 1, and the bound on large records is proportional to tau.
NEW: So T1 holds for every S8_{tau,w} with rho + tau < 1, and the bound on large records is proportional to tau. (For w > 0 the g-primes leave the lattice, and if rho w ≥ 1 several may coincide; T(0) < ∞ still holds: m placements in [a, b] force tau − rho w ≤ tau − (m − 1) + rho(b − a), so pi(b) − pi(a−) ≤ rho(b − a) + rho w + 1, pi(x) = O(x), and T(0) < ∞ by partial summation. eps is nonincreasing from the point where eta_w decreases, log z > 1 − rho/(1 + rho w).)

## §5 Minor pairs (6 items, 7 pairs)
**m1 — E1' needs D(x) > 0 for its displayed consequence (l. 171).**
OLD:   A ≤ max{0, psi(x)/(x D(x)) − rho}.
NEW:   A ≤ max{0, psi(x)/(x D(x)) − rho}   whenever D(x) > 0 (the only case T1' uses: D ≥ D0 > 0 on [X0, ∞)).

**m2 — the §1.7 table rounds the additive constant 1 − rho down (l. 161, l. 162).**
OLD: | S8(π/16) | 3·10⁷ | 0.14099 (p1 = 3.5465) | 8.1·10⁻⁵ | 4.596 | 1.546 | 0.32346 | c = 0.32346 | 0.51981 x + 0.80 |
NEW: | S8(π/16) | 3·10⁷ | 0.14099 (p1 = 3.5465) | 8.1·10⁻⁵ | 4.596 | 1.546 | 0.32346 | c = 0.32346 | 0.51981 x + 0.8037 |
OLD: | S8(π/32) | 3·10⁷ | 0.08206 (p1 = 6.0930) | 6.0·10⁻⁵ | 7.741 | 4.092 | 0.12220 | c = 0.12220 | 0.22037 x + 0.90 |
NEW: | S8(π/32) | 3·10⁷ | 0.08206 (p1 = 6.0930) | 6.0·10⁻⁵ | 7.741 | 4.092 | 0.12220 | c = 0.12220 | 0.22037 x + 0.9019 |

**m3 — the drift identity's error term is one-sided as proved (l. 189).**
OLD: so psi(y)/y − rho D(y) = −W(y) + O(log y/y), W(y) := (1/y)Σ_{d≤y}Λ(d)E(y/d) (the Lambda-weighted mean of E over the lower scales).
NEW: so psi(y)/y − rho D(y) = −W(y) + ((1/2)log y − ∫_1^y E(u)du/u + rho)/y ≤ −W(y) + (log y + rho)/y (the remainder is O(log y/y) only if ∫_1^y E du/u = O(log y), which is not proved), W(y) := (1/y)Σ_{d≤y}Λ(d)E(y/d) (the Lambda-weighted mean of E over the lower scales).

**m4 — §2.3(ii) (l. 206).**
OLD: (ii) A u + b, b ≠ 0: shifts the effective constant (b > 0 worsens it by 2b rho/(1 − 2rho); b < 0 is beaten at u = 1).
NEW: (ii) A u + b, b ≠ 0: shifts the effective constant (b > 0 worsens it by 2b rho/(1 − 2rho); b < −A is beaten at u = 1, and −A ≤ b < 0 interpolates toward (iii)).

**m5 — the ordering of the 3·10⁷ run is now certified independently (l. 164).**
OLD: Rounding: the run is in double precision; the ordering of S8 in double precision is exact below 5·10⁷ (π/16) and 7.1·10⁷ (π/32)
NEW: Rounding: the run is in double precision; the ordering of S8 in double precision is exact below 5·10⁷ (π/16) and 7.1·10⁷ (π/32), and every composite-versus-lattice decision to 3·10⁷ is certified independently by read-O (double-double, minimum distance 9.4·10⁻⁸ (π/16) and 2.3·10⁻⁶ (π/32) lattice units against an error below 10⁻²², verify-O/logs/s8gen_*.log)

**m6 — the rho = 0.3 and 0.45 side runs cross lattice ties (l. 85-86).**
OLD: −0.276 (0.45); logs/t1_*.log.]
NEW: −0.276 (0.45); logs/t1_*.log. For rho = 0.3 and 0.45, t = 10/3 and 20/9 have even numerators, so composites can sit exactly on the lattice (s40 Lemma 1.4; e.g. rho = 0.3: 6 = x_2 is a g-prime and (8/3)·6 = 16 = x_5), and a double-precision event loop decides such ties by rounding; these two rows are not certified, and no theorem uses them.]

## §6 Novelty per result
| result | verdict |
|---|---|
| (A1) and (*) | in print as Chebyshev's identity L dN = dψ ∗ dN (DZ eq. (3.3), used at p. 57 l. 3393-3396); the (E, psi, Psi~) rearrangement is routine |
| Lemma B1 (Chebyshev–Mertens inequality at every g-prime) | new (S8-specific: uses E = +1/2 at g-primes) [single-check → second check here ✓] |
| Lemmas C1, D1, Cor. D2 (S <= log x − 1/(2rho) + o(1)) | new for S8; D2 is exactly the hypothesis of DZ Thm 6.13 |
| Lemma E1, E1' (record inequality) | new as a statement; same Chebyshev-identity bootstrap as DZ Thm 6.13's induction (p. 61-62) |
| Theorem T1 (N = O(x)) | new as a statement on a printed core: D2 + DZ Thm 6.13 p. 61 (F1) |
| Theorem T1' and the constants of §1.7-1.8 | new (explicit sharp constant, not in DZ); reproduced here independently |
| §1.6 variants | new as statements on the same core (F5 fix needed for w > 0) |
| Cor. 1.9 | lower half in print (DZ Thm 4.7 p. 33, Cor. 8.7 p. 81); upper half routine from D2 (F2) |
| §2 (a) | elementary; (b) new, closed unconditionally by A2 below; (c) observation on data, not a theorem (F3) |

## §7 Additions (single-check)
**A1 (a second proof of T1).** For x >= p1, D1 (X0 = p1) and D2 give Delta(x) >= (1 − 2rho)(min{D(p1), 1/(2rho)} − eps(p1)/rho)
− 2eps(p1) =: −K, so psi1(x) = S(x) <= log x − 1 + K for all x >= 1, and DZ Thm 6.13 gives N(x) ≪ x. Step E is needed only for
the constants.
**A2 (§2.3(i) without data).** For every theta < 1 there is x_theta with Σ_{d<=x}Λ(d)d^{−theta} > log x for x >= x_theta, so
the bracket of §2.3(i) is negative and sub-linear comparison functions give no upper bound, unconditionally. Proof: Cor. 1.9
gives log log x − K1 <= Σ_{p<=x}1/p <= log log x + K2; with a := exp(−(K1 + K2 + 1)), Σ_{x^a<p<=x}1/p >= 1, so
S(x) − S(x^a) >= Σ_{x^a<p<=x} log p/p >= a log x; then Σ_{d<=x}Λ(d)d^{−theta} >= Σ_{x^a<d<=x}(Λ(d)/d)d^{1−theta} >=
x^{a(1−theta)}·a log x > log x once x^{a(1−theta)} > 1/a.
**A3 (Chebyshev-type corollary from print).** By DZ Prop. 9.8 (p. 90), O-log density (from D2, or from T1) gives
liminf pi_P(x) log x/x <= 1, and positive lower log density (from E > −1/2, every rho) gives limsup pi_P(x) log x/x >= 1. So for
S8(rho), rho < 1/2: liminf pi_P(x) log x/x <= 1 <= limsup pi_P(x) log x/x. (Data at 3·10⁷, pi/16: pi_P log x/x = 1.026.)
**A4 (robust certificate).** The T1' constant can be certified with a lattice-uniform bound for T(P0) (any g-prime set on the
lattice): rho + 1.39·10⁻⁴ (pi/16), rho + 3.48·10⁻⁵ (pi/32) (§2), so the theorem's constants survive any error in the fine
structure of the 3·10⁷ run other than P0 and D(X0) — and D(X0) enters only through a minimum it exceeds by more than 2.

## §8 What I could not check, and why
- rho = 0.3 and 0.45 rows (side data, no theorem uses them): not reproduced; my generator takes a decimal rho as a double, which
  does not reproduce exact lattice ties (m6).
- s40 Lemmas 1.0-1.2 are used as dual-read in Session 40; I re-derived only the parts T1 uses (E(p) = +1/2, E > −1/2, spacing).
- DZ page numbers are read from the running heads of the on-disk text, not from page images.
- My certification of the run needs no transcendence (it bounds every composite away from the lattice directly); the
  "no ties" count for pi/16, pi/32 is a finite check to 3·10⁷ only.

Closed 19:18 IST 2026-10-01. Files: read-O.md; verify-O/s8gen.c (build: clang -O2 -ffp-contract=off s8gen.c -lm; run: s8gen 16 3e7, s8gen 32 3e7, s8gen 16 1e7 0.1, s8gen 4 1e6); verify-O/logs/s8gen_*.log; verify-O/sources/q1-q3.xml (arXiv queries). Nothing over 50 MB written.
