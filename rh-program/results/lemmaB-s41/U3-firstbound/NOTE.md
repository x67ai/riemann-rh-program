# U3-firstbound — first unconditional upper bound for the integer error E of S8(rho)

Stream: lemmaB-s41. Unit: U3-firstbound (second agent; the first died without writing a file).
Opened: 18:08 IST 2026-10-01

## Plan (at most 20 lines)
1. Read briefly: CHARTER (s41), free-greedy-s40 CHARTER §1 + theory NOTE §1, Prop 2.1, §3.3;
   ORCH-NOTES (O9 + correction); U7 §4.1, §5; U5 §0; U1 §0. Record only what is load-bearing.
2. verify/: copy the event loop of orch-verify/s8_meansq.py; log N(x)/x, E(x)/x, max E,
   queue e_k, gaps between g-primes, and every candidate inequality before trying to prove it.
3. ATTEMPT 1 (T1): "no g-prime while queue positive" + lattice spacing 1/rho -> bound on the
   length of excess stretches -> N(x) <= C x.
4. ATTEMPT 2 (T1/T2): identity (I1) (multiples of p1 = system one scale down) + Cor 5.4
   (queue of arrivals coprime to p1) -> recursive inequality for sup E(x)/x.
5. ATTEMPT 3 (T2/T3) only if T1 lands.
6. If a class of arguments provably cannot give (T1), state that theorem with the control.
7. Close §0 with the theorem-shaped statement.

## §0 Result (filled 18:45 IST 2026-10-01)
**(T1) holds, proof in §1 (Theorem T1 §1.5, sharper Theorem T1' §1.8) [proved here; novelty: single-check, prior art not searched].**
For every rho ∈ (0, 1/2), S8(rho) has N(x) = O(x): every record of E(u)/(u − 1) beyond X0 is ≤ rho + 2eps(X0)/D0 with
eps(X0) → 0, so sup_{x>1} E(x)/(x − 1) < ∞. Explicitly (finite run to 3·10⁷ for the initial range, §1.7–1.8):
  **S8(π/16): E(x) ≤ 0.196413·(x − 1), i.e. N(x) ≤ 0.392763·(x − 1) + 1, for all x > 1;**
  **S8(π/32): E(x) ≤ 0.098198·(x − 1), i.e. N(x) ≤ 0.196373·(x − 1) + 1, for all x > 1**
— the count never exceeds twice its target slope (plus 10⁻⁴). Threshold-tau variants with early placement by at most w (§1.6):
records ≤ rho tau/(1 − tau) + o(1). Inputs: only E > −1/2 everywhere, E = +1/2 at every g-prime, rho < 1/2, and the Chebyshev
identity (*) (= U7 Thm 5.5); no prime-gap, zero-free-region or PNT input.
Mechanism: (*) at each g-prime y gives psi(y)/(2y) + rho Psi~(y) ≤ rho(log y − 1) + (log y + rho)/y (Lemma B1); it persists between
g-primes (C1) and integrates to the Mertens bound S(x) ≤ log x − 1/(2rho) + o(1) (D2); at a record of E(u)/(u − 1), (*) forces
A ≤ psi/(xD) − rho ≤ rho + o(1) (E1').
**Corollary (§1.9):** Σ_{p≤x} 1/p = log log x + O(1) for S8(rho), rho < 1/2.
**(T2) is not obtained; proof class R cannot yield it (§2):** class R = "the Chebyshev identity (*) at a point, with scale-
proportional upper bounds A·(v − 1) or A·v at the lower scales and any information on psi, S". Because (a) R bounds the GLOBAL
supremum of E(u)/(u − 1), which equals rho exactly at u = p1 (E(p1) = 1/2, p1 − 1 = 1/(2rho)), and for every threshold tau the
output is ≥ max{rho(1−tau)/tau, rho tau/(1−tau)} ≥ rho (§2.4); (b) for sub-linear comparison functions (*) gives no inequality
(§2.3); (c) restarted at large scales, R stops at psi/(xD) − rho = −W/D + O(log x/x), W the Lambda-mean of E over lower scales,
which is dominated by the bounded scales where E(v) = −rho(v − 1) < 0 (≈ +0.010–0.014 on data for π/16). GAP (T2), exact: a lower
bound for g-primes in macroscopic windows (x/K, x], or a non-lossy control of z-rough composites in a prime gap (§2.5).
(T3) not attempted beyond §2.3(i) (sub-linear comparison functions are excluded from class R).
Data on disk: verify/t1_check.py, t1_const.py, mertens2.py; logs/t1_*.log, t1const_*.log, mertens2_*.log.

## §1. ATTEMPT 1 (T1) — the Chebyshev identity at a record of E(u)/u  (opened 18:17 IST 2026-10-01)

Notation (S8(rho), threshold 1/2, 0 < rho < 1/2). g-primes p, Lambda(p^j) = log p, psi(x) = sum_{d<=x} Lambda(d),
S(x) = sum_{d<=x} Lambda(d)/d, Psi~(x) = int_1^x psi(u) u^{-2} du (so S = psi/x + Psi~), E(u) = N(u) - rho(u-1) - 1.
Mertens deficit Delta(x) := log x - 1 - S(x).  D(x) := log x - 1 - Psi~(x) = Delta(x) + psi(x)/x.

Inputs re-derived here (not imported): (L1) E(u) > -1/2 for all u >= 1 [s40 Lemma 1.1]; (L2) E(p) = 1/2 exactly at every
g-prime p [s40 Lemma 1.0(ii)]; (L3) E(u) = -rho(u-1) on [1, p1), p1 = 1 + 1/(2 rho).

Plan of the argument (each step proved below or marked GAP):
 Step A. Exact identity (*):  E(x) log x - int_1^x E(u) du/u = psi(x) + rho x Psi~(x) - rho x (log x - 1) - rho
         + sum_{d<=x} Lambda(d) E(x/d).        [= U7 Thm 5.5 / O9, rearranged; re-derived in §1.1]
 Step B. (*) at a g-prime y with (L1), (L2):  F(y) := psi(y)/(2y) + rho Psi~(y) - rho(log y - 1) <= (log y + rho)/y.
 Step C. F decreases between prime powers; so F(x) <= eps(x) -> 0 for all x (eps explicit from the last g-prime <= x).
 Step D. Integrate B/C as an ODE in t = log x:  D(x) >= 1/(2 rho) - o(1)   (a Mertens upper bound S <= log x - 1/(2rho) + o(1)).
 Step E. At a record x of E(u)/u (value A > 0): (*) gives (A + rho) Delta(x) <= (1 - rho) psi(x)/x - rho/x;
         with C and D:  A <= rho/(1 - 2 rho) + o(1).
 Conclusion (target T1): limsup E(x)/x <= rho/(1-2rho); hence N(x) <= C x for all x, C finite; explicit C from a finite run.

### §1.1 Step A — the identity (*) [proved here; = U7 Thm 5.5 rearranged, re-derived]
G = the multiset of finite products of g-primes, N(x) = #(G ∩ [1, x]) with multiplicity. For n ∈ G, log n = Σ_{d | n} Λ(d), the
sum over the prime-power sub-multisets p^j ⊆ n (j ≥ 1): n = Π p^{a_p} gives Σ_p a_p log p = Σ_p Σ_{j=1}^{a_p} log p. For a fixed
prime power d, the n ∈ G with d | n and n ≤ x are in bijection with m ∈ G, m ≤ x/d (n = d·m, multiset union). No freeness of the
real values and no transcendence of t = 1/rho is used: N counts multisets. Hence
  (A1) Σ_{n∈G, n≤x} log n = Σ_{d≤x} Λ(d) N(x/d).
Left side: Stieltjes, log 1 = 0: = N(x) log x − ∫_1^x N(u) du/u. Insert N(u) = rho(u − 1) + 1 + E(u):
  ∫_1^x N(u)du/u = rho(x − 1) − rho log x + log x + ∫_1^x E(u)du/u,
  so LHS = rho x log x − rho(x − 1) + E(x) log x − ∫_1^x E(u) du/u.
Right side: N(x/d) = rho(x/d − 1) + 1 + E(x/d) for every d ≤ x (x/d ≥ 1), so RHS = rho x S(x) + (1 − rho) psi(x) + Σ_{d≤x} Λ(d)E(x/d).
Stieltjes again (psi = 0 on [1, p1)): S(x) = ∫_1^x dpsi(u)/u = psi(x)/x + Psi~(x). So rho x S + (1 − rho) psi = psi + rho x Psi~. Equate:
  (*)  E(x) log x − ∫_1^x E(u) du/u = psi(x) + rho x Psi~(x) − rho x (log x − 1) − rho + Σ_{d≤x} Λ(d) E(x/d).      ∎
[computed: verify/t1_check.py, logs/t1_*.log — both sides agree to ≤ 3·10⁻⁷ at x = 10³…10⁶ for rho = π/16, π/32, 0.3, 0.45.]
Equivalent form used in Step E: with Delta = log x − 1 − S, psi + rho x Psi~ − rho x(log x − 1) = x[(1 − rho) psi/x − rho Delta].

### §1.2 Step B — a Chebyshev–Mertens inequality at every g-prime [proved here]
**Lemma B1.** For 0 < rho < 1 and every g-prime y:  F(y) := psi(y)/(2y) + rho Psi~(y) − rho(log y − 1) ≤ (log y + rho)/y.
*Proof.* Apply (*) at x = y. Left side: E(y) = 1/2 by (L2), and −∫_1^y E(u)du/u < (1/2) log y by (L1); so LHS < log y.
Right side: E(y/d) > −1/2 for every d ≤ y by (L1) (y/d ≥ 1), so Σ_{d≤y} Λ(d)E(y/d) ≥ −psi(y)/2 and
RHS ≥ psi(y)/2 + rho y Psi~(y) − rho y(log y − 1) − rho = y F(y) − rho. Hence y F(y) − rho < log y. ∎
In Delta-form: (1/2 − rho) psi(y)/y ≤ rho Delta(y) + (log y + rho)/y   (F = (1/2 − rho) psi/x − rho Delta).
So at every g-prime the Mertens deficit Delta controls psi from above. This is where both one-sided facts of the construction
enter: E(y) = +1/2 exactly at y (a g-prime is placed only when the count is 1/2 behind the target, and then lifts it to 1/2
ahead), and E > −1/2 at every smaller scale y/d.
[computed: max over all g-primes of F(y) − (log y + rho)/y = −0.221 (π/16, 1.79·10⁶ primes to 3·10⁷), −0.155 (π/32), −0.274 (0.3),
−0.276 (0.45); logs/t1_*.log.]

### §1.3 Step C — F stays below a vanishing bound everywhere [proved here]
(L4) There are infinitely many g-primes: with only p1..pk, N(x) ≤ Π_{i≤k}(1 + log x/log p_i) (s40 1.0), so E(x) → −∞, against (L1).
Put eta(z) := (log z + rho)/z and T(z) := Σ_{g-primes p} Σ_{j≥2, p^j>z} log p/p^j. T(0) ≤ Σ_{k≥1} log x_k/(x_k(x_k − 1)) < ∞
(distinct g-primes are distinct lattice points x_k = 1 + (k − 1/2)/rho), so T(z) ↓ 0. eta is decreasing on [e^{1−rho}, ∞) ∋ p1
(p1 = 1 + 1/(2rho) > e^{1−rho} on (0, 1/2): check on (0, .291] where p1 ≥ e, on [.291, .4] where p1 ≥ 2.25 > e^{.709}, on [.4, .5)
where p1 > 2 > e^{.6}).
**Lemma C1.** For 0 < rho < 1/2 and x ≥ p1, with P = P(x) the largest g-prime ≤ x:  F(x) ≤ eps(x) := eta(P) + T(P)/2.
eps is nonincreasing in x and eps(x) → 0 (L4).
*Proof.* F = psi/(2x) + rho Psi~ − rho(log x − 1) is right-continuous; Psi~ is continuous; F jumps only at prime powers d, by
Lambda(d)/(2d) > 0. Between prime powers psi is constant and dF/dx = −psi/(2x²) + rho psi/x² − rho/x = −(1/2 − rho)psi/x² − rho/x < 0.
On (P, x] every prime power is p^j with j ≥ 2 and p^j > P. So F(x) ≤ F(P) + (1/2)Σ_{p^j∈(P,x], j≥2} log p/p^j ≤ F(P) + T(P)/2,
and F(P) ≤ eta(P) by Lemma B1. ∎   In Delta-form: (1/2 − rho) psi(x)/x ≤ rho Delta(x) + eps(x) for all x ≥ p1.   (C2)

### §1.4 Step D — integrating C1: a Mertens upper bound with the right shape [proved here]
**Lemma D1.** For 0 < rho < 1/2 and x ≥ X0 ≥ p1, with t = log x, t0 = log X0:
  D(x) ≥ 1/(2rho) + (X0/x)^{2rho} (D(X0) − 1/(2rho)) − 2 ∫_{t0}^{t} e^{2rho(s−t)} eps(e^s) ds,
and with X0 = p1 (D(p1) = log p1 − 1, Psi~(p1) = 0):  liminf_{x→∞} D(x) ≥ 1/(2rho).
*Proof.* g(t) := Psi~(e^t) is continuous, piecewise C¹, g'(t) = psi(e^t)/e^t, and F = g'/2 + rho g − rho(t − 1). Lemma C1:
g' + 2rho g ≤ 2rho(t − 1) + 2eps, i.e. (e^{2rho t} g)' ≤ 2rho e^{2rho t}(t − 1) + 2 e^{2rho t} eps a.e. Integrate on [t0, t], using
d/ds[e^{2rho s}(s − 1 − 1/(2rho))] = 2rho e^{2rho s}(s − 1):
  g(t) ≤ t − 1 − 1/(2rho) + e^{2rho(t0−t)}(g(t0) − t0 + 1 + 1/(2rho)) + 2∫_{t0}^t e^{2rho(s−t)} eps ds.
D = t − 1 − g gives the display. For the liminf split the integral at t/2: ≤ eps(p1) e^{−rho t}/rho + eps(√x)/rho → 0. ∎
**Corollary D2 (Mertens upper bound).** Delta(x) ≥ (1 − 2rho) D(x) − 2 eps(x); so S(x) = Σ_{d≤x}Λ(d)/d ≤ log x − 1/(2rho) + o(1).
*Proof.* Delta = D − psi/x and (C2) give psi/x ≤ (rho Delta + eps)/(1/2 − rho); so Delta ≥ D − (rho Delta + eps)/(1/2 − rho),
i.e. Delta·(1 + rho/(1/2 − rho)) = Delta/(1 − 2rho) ≥ D − 2eps/(1 − 2rho); multiply by 1 − 2rho > 0. ∎
(The template has S = log x − (1 − x^{−rho})/rho → log x − 1/rho; D2 is weaker by 1/(2rho), and unconditional.)
[computed: min D per decade (π/16) 3.29, 3.85, 4.20, 4.41, 4.55 on 10³…10⁷ against 1/(2rho) = 2.55; (π/32) 4.33 … 7.53 vs 5.09.]

### §1.5 Step E — the record inequality and Theorem T1 [proved here]
**Lemma E1.** If x ≥ 1 and A := E(x)/x = sup_{1≤u≤x} E(u)/u > 0, then (A + rho) Delta(x) ≤ (1 − rho) psi(x)/x − (A + rho)/x.
*Proof.* LHS(*) = A x log x − ∫_1^x E(u)du/u ≥ A x log x − A(x − 1), since E(u) ≤ A u on [1, x]. In RHS(*), E(x/d) ≤ A x/d for
every d ≤ x (1 ≤ x/d ≤ x), so Σ_{d≤x} Λ(d)E(x/d) ≤ A x S(x) = A x(log x − 1 − Delta). With Psi~ = log x − 1 − Delta − psi/x,
psi + rho x Psi~ − rho x(log x − 1) = (1 − rho)psi − rho x Delta. So A x log x − A x + A ≤ (1 − rho)psi − rho x Delta − rho
+ A x log x − A x − A x Delta; cancel and divide by x. ∎
*Records exist.* On [1, x], E is right-continuous with finitely many jumps, all upward, and affine of slope −rho between them; so
u ↦ E(u)/u attains its supremum over [1, x] at some u* ≤ x (on each closed piece the right-end value E(a−)/a is beaten by E(a)/a).
**Theorem T1.** Let 0 < rho < 1/2 and X0 ≥ p1. Put eps0 := eps(X0) (Lemma C1), let D0 be any lower bound for D on [X0, ∞)
(Lemma D1 gives one), and Delta0 := (1 − 2rho) D0 − 2 eps0. If Delta0 > 0, then for every x ≥ 1
  E(x)/x ≤ max{ sup_{1≤u≤X0} E(u)/u ,  rho/(1 − 2rho) + 2(1 − rho) eps0 / ((1 − 2rho) Delta0) },
and N(x) ≤ (rho + that max)·x + 1 − rho. Such X0 exist for every rho ∈ (0, 1/2) (eps → 0 and liminf D ≥ 1/(2rho) by D1), so
**N(x) = O(x) and sup_x E(x)/x < ∞ for every S8(rho), 0 < rho < 1/2; every record of E(u)/u beyond X0 is ≤ rho/(1−2rho) + o(1).**
*Proof.* Fix x; take u* ≤ x attaining A := sup_{u≤x} E(u)/u. If u* ≤ X0 the first entry bounds A. If u* > X0 and A > 0, E1 at u*
gives (A + rho)Delta ≤ (1 − rho) psi/u*; (C2) gives psi/u* ≤ (rho Delta + eps0)/(1/2 − rho); Corollary D2 gives Delta ≥ Delta0 > 0.
So A + rho ≤ (1 − rho)(rho + eps0/Delta)/(1/2 − rho) ≤ 2(1 − rho)(rho + eps0/Delta0)/(1 − 2rho), and 2rho(1 − rho)/(1 − 2rho) − rho
= rho/(1 − 2rho). ∎
*Where the construction enters.* Only (L1) E > −1/2 and (L2) E = +1/2 at g-primes (Lemma B1), plus rho < 1/2. Any variant with
E > −tau everywhere and E ≤ 1 − tau + rho w at every g-prime (threshold tau, early placement by at most w) gives the same
argument with constant rho tau/(1 − rho − tau) in place of rho/(1 − 2rho): §1.6. No input on prime gaps, zeros, or a PNT.
[computed: in every run (π/16, π/32 to 3·10⁷; 0.3, 0.45 to 10⁷) the residual of E1 at every record is ≤ −0.16; the records of
E(u)/u stop at u = p1 for π/16, π/32, 0.3 (E(p1)/p1 = 1/(2 p1) = rho/(1 + 2rho) = 0.1410 for π/16); logs/t1_*.log.]

### §1.6 The same for the threshold-tau variants, with early placement [proved here]
Variant S8_{tau,w}: a g-prime is placed at the deficit time (D = T − N reaches tau, 0 < tau < 1 − rho) or earlier by at most w,
never after it. Then (L1') E > −tau everywhere, (L2') E(y) ≤ 1 − tau + rho w at every g-prime y (just before y, D ≥ tau − rho w).
B1 becomes: LHS(*) at y ≤ (1 − tau + rho w) log y + tau log y; RHS ≥ (1 − tau)psi + rho y Psi~ − rho y(log y − 1) − rho, i.e.
  F_tau(y) := (1 − tau)psi/y + rho Psi~ − rho(log y − 1) ≤ eta_w(y) := ((1 + rho w) log y + rho)/y;  Delta-form (1 − tau − rho)psi/y ≤ rho Delta + eta_w.
C1: dF_tau/dx = −(1 − tau − rho)psi/x² − rho/x < 0 needs only r0 := 1 − rho − tau > 0. D1: the ODE (1 − tau)g' + rho g ≤ rho(t − 1) + eps
has the particular solution t − 1 − (1 − tau)/rho, so liminf D ≥ (1 − tau)/rho, and D2 reads Delta ≥ (r0/(1 − tau)) D − eps/(1 − tau)
→ liminf Delta ≥ r0/rho. E1 is unchanged (it never uses the rule). Final step: A + rho ≤ (1 − rho)(rho + eps/Delta)/r0, so
  **every record of E(u)/u at large u is ≤ rho·tau/(1 − rho − tau) + o(1)**;  for tau = 1/2: rho/(1 − 2rho).
So T1 holds for every S8_{tau,w} with rho + tau < 1, and the bound on large records is proportional to tau.
Caution (why tau → 0 with scale does not give T2): the tau in B1 enters through Σ_{d≤y}Λ(d)E(y/d) ≥ −Σ Λ(d) tau(y/d), a Lambda-
weighted mean dominated by the SMALL scales y/d = O(1) (on data about half the weight of psi(y) sits at y/d ≤ 2; unconditionally
the distribution of psi in (y/2, y] is not known); a threshold that falls with
scale leaves this mean at the early thresholds.

### §1.7 Explicit constants (18:24 IST 2026-10-01) [proved here, with a finite computation [computed]]
Inputs from one run to X0 (verify/t1_const.py; logs/t1const_*.log): sup_{u≤X0} E(u)/u; P0 = last g-prime ≤ X0; eps0 = eta(P0)
+ (1 − tau)T(P0), with T(P0) summed exactly over the g-primes ≤ X0 plus the lattice bound rho(log a + 1)/(a − 1), a = X0 − 1/rho,
for g-primes > X0; D(X0); then D0 = min{D(X0), (1 − tau)/rho − eps0/rho} (Lemma D1 as a convex combination), Delta0 =
(r0 D0 − eps0)/(1 − tau), record bound rho tau/r0 + (1 − rho)eps0/(r0 Delta0).
| system | X0 | sup_{u≤X0} E/u (at) | eps0 | D(X0) | Delta0 | records beyond X0 ≤ | **E(x) ≤ c x, all x ≥ 1** | N(x) ≤ |
|---|---|---|---|---|---|---|---|---|
| S8(π/16) | 3·10⁷ | 0.14099 (p1 = 3.5465) | 8.1·10⁻⁵ | 4.596 | 1.546 | 0.32346 | c = 0.32346 | 0.51981 x + 0.80 |
| S8(π/32) | 3·10⁷ | 0.08206 (p1 = 6.0930) | 6.0·10⁻⁵ | 7.741 | 4.092 | 0.12220 | c = 0.12220 | 0.22037 x + 0.90 |
| S8_{0.1}(π/16) | 10⁷ | 0.76782 (u = 2.2780) | 1.6·10⁻⁴ | 8.024 | 3.583 | 0.02796 | c = 0.76782 | 0.96417 x + 0.80 |
Rounding: the run is in double precision; the ordering of S8 in double precision is exact below 5·10⁷ (π/16) and 7.1·10⁷ (π/32)
[quoted: s40 theory NOTE §3.0 and the row "Integer error of S8" in §6, ordering margins 6.1·10⁻¹⁴ and 6.5·10⁻¹⁵ relative]; every
quantity above enters with a margin ≥ 10⁻² against rounding ≤ 10⁻⁸. U6/U7 exact generators reproduce N, π_P to 10¹⁰ [quoted, SHARED].
So **(T1) holds for S8(π/16) with C = 0.5199 and for S8(π/32) with C = 0.2204**: N(x) ≤ C x + 1 − rho for all x ≥ 1.

### §1.8 Sharper form: compare E with u − 1 instead of u (18:33 IST 2026-10-01) [proved here]
**Lemma E1'.** If x > 1 and A := E(x)/(x − 1) = sup_{1<u≤x} E(u)/(u − 1) > 0, then A(1 + x D(x)) ≤ psi(x) − rho x D(x) − rho, so
  A ≤ max{0, psi(x)/(x D(x)) − rho}.
*Proof.* E(u) ≤ A(u − 1) on [1, x] (at u = 1 both sides vanish). LHS(*) ≥ A(x − 1)log x − A∫_1^x(1 − 1/u)du = A x log x − A(x − 1).
RHS(*): Σ_d Λ(d)E(x/d) ≤ A Σ_d Λ(d)(x/d − 1) = A(x S − psi). With S = log x − 1 − Delta, D = Delta + psi/x and (*)'s first part
= psi − rho x D: A x log x − A x + A ≤ psi − rho x D − rho + A x log x − A x − A x Delta − A psi, i.e. A(1 + x D) ≤ psi − rho x D − rho.
If the right side is ≥ 0, A ≤ (psi − rho x D)/(x D). ∎
**Theorem T1'.** For 0 < rho < 1/2 and X0 ≥ p1 with D0 := min{D(X0), 1/(2rho) − eps0/rho} > 0 (eps0 = eps(X0)): for all x > 1,
  E(x) ≤ max{ sup_{1<u≤X0} E(u)/(u − 1),  rho + 2 eps0/D0 } · (x − 1).
*Proof.* As for T1, with E1' in place of E1 and (C1) in the form psi/x ≤ 2rho D + 2 eps (F = psi/(2x) − rho D ≤ eps), so
psi/(xD) − rho ≤ rho + 2eps0/D; D ≥ D0 on [X0, ∞) by D1. ∎  (Threshold tau: rho tau/(1 − tau) + eps0/((1 − tau)D0), same proof.)
On [1, p1), E(u)/(u − 1) = −rho; at p1 it equals (1/2)/(p1 − 1) = rho. [computed, logs/t1const_*.log]: sup_{1<u≤3·10⁷} E(u)/(u − 1)
= rho exactly at u = p1 for π/16 and π/32; the next largest value over all other events is 0.0655 (u = 8.64, π/16) and 0.0402
(u = 37.1, π/32), margins 0.13 and 0.058 below rho against rounding ≤ 10⁻¹² (verify/second_sup.py, logs/second_sup_*.log). Hence **E(x) ≤ (rho + 6.3·10⁻⁵)(x − 1) for S8(π/16), E(x) ≤ (rho + 2.3·10⁻⁵)(x − 1) for
S8(π/32), for all x > 1; i.e. N(x) ≤ (2rho + 10⁻⁴)(x − 1) + 1: the count never exceeds twice its target slope.** For general
rho ∈ (0, 1/2): every record of E(u)/(u − 1) beyond X0 is ≤ rho + o(1) as X0 → ∞.

## §2. ATTEMPT 2 (T2: E = o(x)) — breaks at: the record method is a linear-scale balance (18:35 IST 2026-10-01)
**2.1 The drift identity [proved here].** Put Q(x) := psi(x) − rho x D(x) (= x(psi/x − rho D)). At a g-prime y, (*) reads
  Q(y) = (1/2)log y − ∫_1^y E(u)du/u + rho − Σ_{d≤y} Λ(d)E(y/d),
so psi(y)/y − rho D(y) = −W(y) + O(log y/y), W(y) := (1/y)Σ_{d≤y}Λ(d)E(y/d) (the Lambda-weighted mean of E over the lower scales).
Between g-primes Q' = −rho(Delta + 1) plus jumps at prime powers, so the same holds up to rho(Delta + 1)·(gap)/x elsewhere.
**2.2 What every record bound reduces to.** E1' gives at a record: A ≤ psi/(xD) − rho = (psi/x − rho D)/D ≈ −W/D. So the record
method can give A → 0 only if W(x) ≥ −o(1) at the records. On data about half of the weight of Σ_d Λ(d) sits at d > x/2 (scales
x/d < 2), so W is dominated by E at bounded scales, where E is a fixed function: on [1, p1) E(v) = −rho(v − 1) < 0.
[computed, logs/t1_*.log and U7 §5.6(v) quoted]: psi/x − rho D = +0.060 (π/16, 10⁶), the U7-measured Lambda-mean of E is −0.064
(π/16), −0.070 (π/32); the record ceiling (psi/x − rho D)/D is +0.0137 at 10⁶ and +0.010 at 10⁷ (π/16) — positive, slowly
varying. So the record method fails twice: (a) it bounds the GLOBAL supremum of E(u)/(u − 1), which is rho, attained at u = p1
(no comparison A(u − 1) with A < rho dominates E at p1, where E(p1)/(p1 − 1) = rho); (b) restarted at large scales it would still
stop at the ceiling ≈ 0.01, not 0. **The record method's output for S8 is E(x) ≤ (rho + o(1))(x − 1), never o(x)**: the information it uses —
upper bounds proportional to the scale at every lower scale — cannot see that E is small, because the identity balances terms of
size x log x and the record comparison is only sensitive at order x (the term x·Delta).
**2.3 Other comparison functions do not help [proved here].** (i) A u^theta, 0 < theta < 1: at a record (*) gives
A·[x^theta log x − (x^theta − 1)/theta − Σ_{d≤x} Λ(d)(x/d)^theta] ≤ Q(x) − rho, and the bracket is negative as soon as
Σ_{d≤x}Λ(d)d^{−theta} > log x, which holds whenever psi(x) > x^theta log x (each term d^{−theta} ≥ x^{−theta}); on data psi(x) ≈ 0.93x.
So for sub-linear comparison functions the record inequality carries no information: the right side is dominated by the small
scales x/d = O(1), where (x/d)^theta is not small compared with E. Only linear comparison functions balance (*) at order x log x.
(ii) A u + b, b ≠ 0: shifts the effective constant (b > 0 worsens it by 2b rho/(1 − 2rho); b < 0 is beaten at u = 1).
(iii) A(u − 1): best of this family (§1.8), ceiling as in 2.2.

### §1.9 Corollary: Mertens' second theorem up to O(1) for S8 (18:42 IST 2026-10-01) [proved here]
**Corollary 1.9.** For 0 < rho < 1/2: Σ_{p≤x} 1/p = log log x + O(1) (sum over g-primes). Explicitly, as x → ∞,
  log log x + log rho − T2 − 1/e − E1(1) − o(1) ≤ Σ_{p≤x} 1/p ≤ log log x + O(1),   T2 := Σ_p 1/(p(p − 1)), E1(1) = 0.21938…
*Proof.* (a) S(y) ≤ log y + c2 for all y ≥ 1: for y ≥ p1, D2 with D1 started at X0 = p1 gives Delta(y) ≥ −K (K explicit from
eps(p1) and log p1); S = 0 below p1. Upper bound: the primes are part of the measure dS, so Σ_{p≤x}1/p ≤ ∫_{[p1,x]} dS(u)/log u
= S(x)/log x + ∫_{p1}^x S(u)du/(u log²u) ≤ 1 + c2/log p1 + ∫_{p1}^x (log u + c2)du/(u log²u) = log log x + O(1).
(b) Lower bound. For sigma > 1, E > −1/2 gives N(u) ≥ rho(u − 1) + 1/2, so zeta_P(sigma) = sigma ∫_1^∞ N(u)u^{−sigma−1}du ≥
rho sigma/(sigma − 1) − rho + 1/2 ≥ rho/(sigma − 1). The Euler product holds (free monoid of multisets, Σ_p p^{−sigma} < ∞ since
the g-primes are distinct lattice points), so log zeta_P(sigma) = Σ_p Σ_k p^{−k sigma}/k ≤ Σ_p p^{−sigma} + T2, whence
Σ_p p^{−sigma} ≥ log(1/(sigma − 1)) + log rho − T2. Take sigma = 1 + 1/log x. Tail: p^{−sigma} = (log p/p)·f(p), f(u) := u^{1−sigma}/log u
positive and decreasing, so Σ_{p>x} p^{−sigma} ≤ ∫_{(x,∞)} f dS = −f(x)S(x) + ∫_x^∞ S(u)(−f'(u))du ≤ f(x)(log x + c2) + ∫_x^∞ f(u)du/u
(using 0 ≤ S(u) ≤ log u + c2 and f S → 0), with f(x)log x = 1/e and ∫_x^∞ f(u)du/u = ∫_x^∞ u^{−sigma}du/log u = ∫_{log x}^∞ e^{−v/log x}dv/v = E1(1).
So Σ_{p≤x}1/p ≥ Σ_{p≤x}p^{−sigma} ≥ log log x + log rho − T2 − 1/e − E1(1) − c2/(e log x). ∎
[computed: verify/mertens2.py, logs/mertens2_*.log] Σ_{p≤x}1/p − log log x = −0.867, −0.995, −1.054, −1.082, −1.096, −1.103 at
10²…10⁷ (π/16; proved floor −2.354); −1.170 … −1.687 (π/32; floor −2.951). S(x) − log x = −4.60 (π/16), −7.73 (π/32) at 10⁷
(proved: ≤ −1/(2rho) + o(1) = −2.55, −5.09).
Remark. (b) uses only E > −1/2 and the upper half of Mertens' first theorem (D2). What is NOT obtained: S(x) ≥ log x − O(1)
(Mertens I lower bound) and the Chebyshev bound psi(x) = O(x); by (C2) the second follows from the first.

**2.4 The threshold does not rescue the method; tau = 1/2 is its optimum [proved here].** For S8_tau (no early placement) the
first g-prime is p1 = 1 + tau/rho with E(p1) = 1 − tau, so sup_{u>1} E(u)/(u − 1) ≥ rho(1 − tau)/tau, while §1.6/§1.8 bound the
large records by rho tau/(1 − tau) + o(1). The method's output max{rho(1 − tau)/tau, rho tau/(1 − tau)} is ≥ rho, with equality
only at tau = 1/2. [computed: tau = 0.1, π/16: early sup 1.7671 = rho·0.9/0.1 at u = 1.5093, large records ≤ 0.0219.] A threshold
that falls with scale does not help either: B1 sees the threshold through Σ_d Λ(d)E(y/d), dominated by the bounded scales.
**2.5 What T2 needs (exact form of the missing input).** Two routes were followed to their breaking line.
(i) Restarting the record at a scale X (sup over [X, x]) puts the bounded scales into Σ_d Λ(d)E(x/d) with their true values,
whose contribution is −(rho + A)Σ_{x/p1<d≤x}Λ(d)(x/d − 1) − … : it HELPS (E < 0 on [1, p1)) but only in proportion to the
g-primes in (x/p1, x] — a lower bound for primes in a macroscopic window next to x, which nothing here provides (records sit in
prime gaps). (ii) Inclusion–exclusion over the small g-primes (the inherited layer, U7 Thm 5.1–5.2): the alternating signs need
TWO-sided smallness of E at the scales x/d, so an a-priori bound E ≤ a·scale costs a·x·Σ_{d|P(z)} 1/d ≍ a x log z — larger than the
burst a x it should explain; with o(scale) as hypothesis the step is circular (it is T2 itself), and a rate does not close either:
φ(x) ≥ c log z · φ(x/P(z)) + c'/log z has no decaying solution. **GAP (T2):** a lower bound for the g-primes in macroscopic windows
(x/K, x] (a Chebyshev-type lower bound in short-in-log windows), or a non-lossy (sieve-quality) control of the z-rough composites in
a prime gap. Not obtained: S(x) ≥ log x − O(1) (Mertens I lower bound) and psi(x) = O(x) — the first would give the second by (C2).

