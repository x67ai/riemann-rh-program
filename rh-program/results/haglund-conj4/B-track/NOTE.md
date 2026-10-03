# B-track NOTE — haglund-conj4 (independent second producer)

## Plan (written before any computation)
1. Read BRIEF-B-track.md, BRIEF-WARNINGS.md, CHARTER.md, SOURCES.md, ORCH-NOTES N0-N1; Haglund (1)-(14).
2. Write own evaluator (mpmath only; no flint/Arb; no A-track/orch-probe/producer-A files).
3. Ladder: pass every rung named in the brief before any census.
4. Q1 for k = 1, 2, 3: follow every zero of F_k(z,t) = Xi_k(z) + t Phi_{k+1}(z) in the window by
   Newton continuation on a tau-grid, tau = -ln(1-t), tau in [0, pi(2k+3)+12], then t = 1.
5. Q3 (real axis) for k = 1..12: real-zero counts along t, landings (x*, tau*), any exits.
6. Q2: the N = 27 site in detail.
7. Q1 for k = 4, 5.
8. After each finished k: table row here + dated block in SHARED.md; close block at end.

## Log of attempts and results (appended as work proceeds)

### Evaluator (written 16:22 IST 2026-10-03)
`code/hb.py`, mpmath 1.3.0 (pure-Python backend), no python-flint, no Arb, no code of A-track / orch-probe / producer-A.
- Phi_n by Haglund (14) with G from (10) (`hb.Phi`), and by the relation form of main.tex Lemma relation,
  Phi_n = (1/2)s(s-1)g_n(s) + (4 pi n^2 - 1)e^{-pi n^2} (`hb.Phi_rel`, two incomplete gammas instead of four; the engine).
- Xi(z) = xi(1/2 + iz) from mpmath zeta/gamma, evaluated at s = 1/2 - iz when Im z > 0 (Xi even).
- Route T: Xi_N = Xi - sum_{n>N} Phi_n (main.tex Thm sandwich), tail summed until a term < 2^-(prec+12) x running scale.
- Pencil: F_k(z,t) = A(z) - u B(z), A = Xi_{k+1} (route T), B = Phi_{k+1}, u = 1 - t = e^{-tau}.
- Incomplete gamma: mpmath.gammainc, checked against my own Legendre continued fraction (modified Lentz,
  stop when |delta-1| < 2^-(prec+8) three times running) and my own lower series Gamma(w) - gamma(w,a).

### Ladder (KICKSTART 10(b)) — rungs L0, L1, L2, L5 (log `data/ladder-L0L2.log`, `data/ladder-L3L5.log`; JSON `data/ladder*.json`)
- L0 gammainc vs own CF at dps 40, 8 points with |Im w| up to 1572 and a = pi n^2 up to 784 pi: max rel. diff 1.1e-37.
  (The series route is accurate only where |w| > a; where |w| < a it cancels 133 bits and the code flags it.)
- L1 Haglund's 19 appendix zeros of Xi_1 (p. 16, 25 printed digits): Newton at dps 40 from each printed value, by (14)
  and by route T; my zero is within 6.9e-22 of his printed value for all 19 (both routes agree to 1e-36). PASS (20 digits).
- L2 largest real zeros of Xi_1..Xi_4 (table p. 4): 14.04543957882982, 39.53248107978795, 65.03207377198914,
  103.3679880094135 (literal sum at dps 60 = route T at dps 30 to 4e-27); each within 3.0e-11 of the 10-decimal table
  entry. PASS for the values; that each is the LARGEST real zero is checked by the real-axis scans below.
- L5 route T (dps 30) vs the literal sum (13)-(14) at dps 80, N = 1..4, 24 points incl. complex z up to 150+60i:
  max rel. diff 2.7e-27. PASS.
- Phi by (14) vs Phi by the relation form, n in {1,2,5,6,7,13,27,28}, |z| up to 3143+60i, dps 30 vs dps 60:
  agree to <= 6e-28 relative wherever the pencil uses them (n >= k+1 in its window); Phi_1 at x = 3143 loses
  digits in the relation form (5e-18) but route T never uses Phi_1 there.

### Independence incident (16:24 IST 2026-10-03)
A `ps aux` listing I ran to find my own ladder process printed the full command lines of other units' running
processes (A-track `axis.py`/`a_core` fragments and orch-probe `rcrit.py`). I did not open their folders; my
evaluator (`hb.py`) and real-axis scanner (`realaxis.py`) were written before the listing and were not changed
because of it; nothing from those lines is used. From here on I query only my own processes by script name.
- L3 Xi_27 at 3144.8946 and 3144.8947 by route T at dps 30 and dps 60: -1.76019463128e-1070 and +1.06871649226e-1070
  (sign change, both precisions); the LITERAL sum (13) at dps 1100 gives the same two values to 12 digits
  (-1.76019463127752e-1070, +1.06871649226171e-1070; 97 s and 102 s). Real zeros 3144.8946622186467569 and
  3145.5998495764871408 (dps 30 = dps 60). PASS (main.tex Thm main (a)).
- L4 Newton on Xi_27 (route T) from 3143.2206824215 + 0.3152587994i: dps 30 -> distance 8.0e-29 from the paper's z*,
  dps 60 -> 3.9e-37. PASS (Thm main (b)).
- Argument principle (code/argp.py, adaptive arg sampling, pi/6 per sample, max spacing 0.25): Xi_1 on
  (0, 86.55) x (-45, 45) counts 31.0 = 1 real + 2 x 15; recursive bisection + Newton finds exactly Haglund's 15
  non-real zeros with Re <= 86.55. Ladder complete (16:27 IST 2026-10-03).

## §0 Census table (one row per pencil k; filled as each k becomes final)
Window W_k = [0, X_k] x [0, Y_k], X_k = 2 pi (k+2)^2 + 30. tau = -ln(1 - t), grid tau_j = 0.1 j up to
pi(2k+3) + 12, then t = 1. Counts are NUMERICAL (mpmath, dps 30; argument principle by adaptive sampling,
not interval-rigorous). Columns: real zeros of Xi_k / Xi_{k+1} in (0, X_k) [argument principle | real-axis scan];
non-real zeros of Xi_k / Xi_{k+1} in W_k; landings (x*, tau*); non-real ends in W_k; exits / entries;
worst increase of Im z between consecutive grid values (negative = every step descended); grid values with
Im(dz/dt) > 0.

| k | X_k | Y_k | real Xi_k / Xi_k+1 | non-real Xi_k / Xi_k+1 | landings | non-real ends | exits / entries | worst dIm | Im dz/dt > 0 |
|---|---|---|---|---|---|---|---|---|---|
