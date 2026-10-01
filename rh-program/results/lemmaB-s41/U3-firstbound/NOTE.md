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

## §0 Result (filled at the end)
(pending)

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
weighted mean dominated by the SMALL scales y/d = O(1) (half the weight of psi(y) sits at y/d ≤ 2); a threshold that falls with
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
= rho exactly at u = p1 for π/16 and π/32. Hence **E(x) ≤ (rho + 6.3·10⁻⁵)(x − 1) for S8(π/16), E(x) ≤ (rho + 2.3·10⁻⁵)(x − 1) for
S8(π/32), for all x > 1; i.e. N(x) ≤ (2rho + 10⁻⁴)(x − 1) + 1: the count never exceeds twice its target slope.** For general
rho ∈ (0, 1/2): every record of E(u)/(u − 1) beyond X0 is ≤ rho + o(1) as X0 → ∞.

