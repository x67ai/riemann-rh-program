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

