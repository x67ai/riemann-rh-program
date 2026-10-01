# read-O — lemmaB-s41/U3-firstbound

Reader: Opus (claude-opus-5-5), second model of the dual-model check. Opened 18:49 IST 2026-10-01.
Target: `results/lemmaB-s41/U3-firstbound/NOTE.md`, SHA-256 f3dfc4539a5a58c879bb50de475450f7bd7c09ca6f94f6709edc67da1022d2b2,
243 lines (all line numbers below refer to this hash). Claim: N(x) = O(x) for S8(rho), every rho in (0, 1/2); Theorem T1':
E(x) <= 0.196413 (x - 1) for rho = pi/16 and E(x) <= 0.098198 (x - 1) for rho = pi/32, all x > 1.
Also read: READ-BRIEF-O.md (generic rules); lemmaB-s41/CHARTER.md (the unit's brief: there is no BRIEF.md in the folder);
free-greedy-s40/CHARTER.md §1; free-greedy-s40/theory/NOTE.md Lemmas 1.0-1.5, Prop. 2.1; ORCH-NOTES.md O9 and its correction
block; the unit's verify/ scripts and logs (read only, never imported). `read-F.md` and `verify-F/` not opened.
Re-run: `U3-firstbound/verify-O/` (own C generator, double-double arithmetic with certified ordering margins; own Python checks).

Status: IN PROGRESS (sections are appended as each check closes).

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
