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

