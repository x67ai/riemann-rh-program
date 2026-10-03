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

### Method statements used by the census (each with its proof)
**M1 (velocity).** Along a branch z(t) of zeros of F_k(z,t) = Xi_k(z) + t Phi_{k+1}(z) with F_z := dF/dz != 0,
dz/dt = -Phi_{k+1}(z)/F_z(z,t), and with u = 1 - t = e^{-tau}, dz/dtau = u dz/dt = -u B/(A' - uB').
Proof: differentiate F(z(t),t) = 0 (implicit function theorem; F is entire in z, affine in t). []

**M2 (landings and lift-offs are the critical points of S_k on the line).** Put A = Xi_{k+1}, B = Phi_{k+1}, so
F = A - uB, and S = A/B on the real axis, where B > 0 (N1: Phi_n > 0 on R for n >= 2, termwise kernel argument
of main.tex Thm sandwich). The real zeros at parameter u are the solutions of S(x) = u. A non-real conjugate pair
can meet the axis at (x*, u*) only at a real double zero: F(x*) = F'(x*) = 0, i.e. S(x*) = u*, S'(x*) = 0.
If S''(x*) < 0 (local max) then for u slightly above u* the zeros near x* are x* +- i sqrt(2(u - u*)/|S''(x*)|)
(1 + o(1)) and for u slightly below u* two real ones: as t increases (u decreases) the pair LANDS at x*, at
tau* = -ln u*. If S''(x*) > 0 (local min) the same expansion with the sign reversed: two real zeros merge at x*
and LEAVE the axis as t increases (a witness against (R), and against (D) just after).
Proof: S(z) - u = (S''(x*)/2)(z - x*)^2 (1 + O(z - x*)) - (u - u*) near x*; take square roots (Rouche /
implicit function theorem in w = z - x*). Since B > 0 and real on R, F(x) = B(x)(S(x) - u) has the same real
zeros with the same multiplicities as S - u. []
Consequence used in Q1/Q3: every landing in (0, X) occurs at a local maximum of S_k on (0, X) with value in (0,1),
every lift-off at a local minimum with value in (0,1); a real zero can leave the axis only through such a minimum
(a simple real zero of a real function stays real under a real perturbation).

### Q1, k = 1 (main run finished 16:44 IST 2026-10-03; data `data/k1-*.json`, logs `data/k1-*.log`)
W_1 = [0, 86.549] x [0, 45]; the argument-principle count is the same with the top edge at 60.
- Xi_1: 31 zeros in (0, 86.549) x (-45, 45) = 1 real + 2 x 15 (AP); real-axis scan on [0, 98.55]: 1 real zero
  (14.0454), so 14.0454395788 is the largest real zero up to 98.55. Non-real zeros found by bisection + Newton:
  exactly 15 in W_1 (Haglund's appendix list) and 3 more up to Re 98.55 (followed as well).
- Xi_2: 29 zeros = 7 real + 2 x 11 (AP); scan: 7 real zeros, largest 39.5325 (so the largest up to 98.55).
- S_1 on [0, 98.55] (8292 points, step 0.05, refined to 0.01 where S is in (-0.5, 1.5)): 9 local extrema,
  3 with value in (0,1), all local MAXIMA: x* = 22.142378 (u* = 0.0837083, tau* = 2.48042), 31.254957
  (u* = 1.32607e-4, tau* = 8.92812), 38.516854 (u* = 7.02803e-7, tau* = 14.16819). No local minimum in (0,1).
- Branches (tau-grid 0.1 to 27.8, then t = 1): the 3 lowest land, each at one of the 3 maxima above; the last
  computed point of each lies on the M2 model (Im z_c = 0.0089427 / 0.0069870 / 0.0046975 against the model
  0.0089427 / 0.0069871 / 0.0046975). 11 end at non-real zeros of Xi_2 in W_1, matching the 11 found
  independently to 5.7e-16. 1 exit: 85.2022 + 35.8750i ends at 88.6268 + 27.5501i (Re > X_1). No entry:
  the 3 branches started at Re 89.15, 93.05, 96.91 end at Re 92.48, 96.30, 100.09.
  Balance: 15 = 3 + 11 + 1; real: 1 + 2 x 3 = 7.
- Im z decreased between every pair of consecutive grid values on every branch (largest increase -3.3e-8, i.e.
  the smallest decrease, at the end of the tau-range where the motion has converged); Im(dz/dt) < 0 at every
  one of the 3,605 recorded grid values of the 15 branches in W_1 (largest value -0.632); at the last step (tau = 27.8 -> t = 1) Im z
  also decreased on every branch.
| # | start z (t=0) | end | x* | tau* | worst dIm | #grid Im(dz/dt)>0 | grid pts |
|---|---|---|---|---|---|---|---|
| 0 | 20.625346 + 2.697152i | landed | 22.142378 | 2.48042 | -7.610e-02 | 0 | 25 |
| 1 | 26.056167 + 7.125360i | landed | 31.254957 | 8.92812 | -6.293e-02 | 0 | 90 |
| 2 | 31.501431 + 10.729150i | landed | 38.516854 | 14.16819 | -5.876e-02 | 0 | 142 |
| 3 | 36.727023 + 13.759614i | Xi_k+1 zero 43.138908 + 3.280971i |  |  | -6.586e-08 | 0 | 279 |
| 4 | 41.737035 + 16.440127i | Xi_k+1 zero 47.522756 + 6.252509i |  |  | -5.846e-08 | 0 | 279 |
| 5 | 46.566229 + 18.881870i | Xi_k+1 zero 51.828315 + 8.958574i |  |  | -5.422e-08 | 0 | 279 |
| 6 | 51.244566 + 21.147504i | Xi_k+1 zero 56.112003 + 11.479609i |  |  | -5.000e-08 | 0 | 279 |
| 7 | 55.795254 + 23.276257i | Xi_k+1 zero 60.350292 + 13.841617i |  |  | -4.642e-08 | 0 | 279 |
| 8 | 60.236214 + 25.294585i | Xi_k+1 zero 64.539068 + 16.070563i |  |  | -4.341e-08 | 0 | 279 |
| 9 | 64.581505 + 27.221336i | Xi_k+1 zero 68.676113 + 18.186820i |  |  | -4.090e-08 | 0 | 279 |
| 10 | 68.842357 + 29.070496i | Xi_k+1 zero 72.761784 + 20.206670i |  |  | -3.880e-08 | 0 | 279 |
| 11 | 73.027899 + 30.852792i | Xi_k+1 zero 76.797531 + 22.143225i |  |  | -3.704e-08 | 0 | 279 |
| 12 | 77.145673 + 32.576663i | Xi_k+1 zero 80.785405 + 24.007108i |  |  | -3.554e-08 | 0 | 279 |
| 13 | 81.201991 + 34.248893i | Xi_k+1 zero 84.727702 + 25.807016i |  |  | -3.426e-08 | 0 | 279 |
| 14 | 85.202203 + 35.875031i | Xi_k+1 zero 88.626777 + 27.550132i (outside W) |  |  | -3.315e-08 | 0 | 279 |
| 15 | 89.150893 + 37.459690i (start outside W) | Xi_k+1 zero 92.484940 + 29.242452i (outside W) |  |  | -3.218e-08 | 0 | 279 |
| 16 | 93.052023 + 39.006751i (start outside W) | Xi_k+1 zero 96.304398 + 30.889023i (outside W) |  |  | -3.133e-08 | 0 | 279 |
| 17 | 96.909049 + 40.519517i (start outside W) | Xi_k+1 zero 100.087229 + 32.494132i (outside W) |  |  | -3.058e-08 | 0 | 279 |

### Q1, k = 2 (main run finished 16:58 IST 2026-10-03; data `data/k2-*.json`)
W_2 = [0, 130.531] x [0, 45] (AP count unchanged with the top edge at 60).
- Xi_2: 53 = 7 real + 2 x 23 (AP); scan on [0, 142.5]: 7 real zeros, largest 39.5325.
- Xi_3: 51 = 15 real + 2 x 18 (AP); scan: 15 real zeros, largest 65.0321 (largest up to 142.5).
- S_2 on [0, 142.5] (11208 points): 19 extrema; 4 with value in (0,1), all MAXIMA: x* = 44.560600 (tau* 3.24730),
  50.852817 (8.29249), 57.272541 (13.06910), 62.128208 (15.97922). No local minimum in (0,1).
- 23 branches in W_2 (+3 started beyond X_2, all ending beyond it): 4 land at the 4 maxima (last points on the
  M2 model: Im 0.0081700 / 0.0075351 / 0.0056521 / 0.0068053 vs model 0.0081701 / 0.0075351 / 0.0056521 /
  0.0068053); 18 end at the 18 non-real zeros of Xi_3 in W_2 (matched to 4.8e-15); 1 exit
  (129.2369 + 44.1967i -> 133.7312 + 32.7765i). Balance 23 = 4 + 18 + 1; real 7 + 2 x 4 = 15. No entry.
- Im z decreased at every grid step of every branch (largest increase -7.9e-8); Im(dz/dt) < 0 at all 6,886 grid
  values of the 23 branches (largest -0.563); the last step to t = 1 decreased Im z on every branch.
| # | start z (t=0) | end | x* | tau* | worst dIm | #grid Im(dz/dt)>0 | grid pts |
|---|---|---|---|---|---|---|---|
| 0 | 43.138908 + 3.280971i | landed | 44.560600 | 3.24730 | -7.180e-02 | 0 | 33 |
| 1 | 47.522756 + 6.252509i | landed | 50.852817 | 8.29249 | -6.519e-02 | 0 | 83 |
| 2 | 51.828315 + 8.958574i | landed | 57.272541 | 13.06910 | -5.906e-02 | 0 | 131 |
| 3 | 56.112003 + 11.479609i | landed | 62.128208 | 15.97922 | -6.419e-02 | 0 | 160 |
| 4 | 60.350292 + 13.841617i | Xi_k+1 zero 67.880190 + 0.477344i |  |  | -2.302e-07 | 0 | 341 |
| 5 | 64.539068 + 16.070563i | Xi_k+1 zero 71.893569 + 2.803764i |  |  | -1.270e-07 | 0 | 341 |
| 6 | 68.676113 + 18.186820i | Xi_k+1 zero 75.694358 + 5.102453i |  |  | -1.172e-07 | 0 | 341 |
| 7 | 72.761784 + 20.206670i | Xi_k+1 zero 79.461016 + 7.225401i |  |  | -1.156e-07 | 0 | 341 |
| 8 | 76.797531 + 22.143225i | Xi_k+1 zero 83.226871 + 9.287337i |  |  | -1.119e-07 | 0 | 341 |
| 9 | 80.785405 + 24.007108i | Xi_k+1 zero 86.971197 + 11.275670i |  |  | -1.086e-07 | 0 | 341 |
| 10 | 84.727702 + 25.807016i | Xi_k+1 zero 90.697290 + 13.198710i |  |  | -1.053e-07 | 0 | 341 |
| 11 | 88.626777 + 27.550132i | Xi_k+1 zero 94.402402 + 15.062584i |  |  | -1.022e-07 | 0 | 341 |
| 12 | 92.484940 + 29.242452i | Xi_k+1 zero 98.085906 + 16.872149i |  |  | -9.924e-08 | 0 | 341 |
| 13 | 96.304398 + 30.889023i | Xi_k+1 zero 101.747341 + 18.632047i |  |  | -9.646e-08 | 0 | 341 |
| 14 | 100.087229 + 32.494132i | Xi_k+1 zero 105.386545 + 20.346292i |  |  | -9.385e-08 | 0 | 341 |
| 15 | 103.835373 + 34.061455i | Xi_k+1 zero 109.003590 + 22.018477i |  |  | -9.142e-08 | 0 | 341 |
| 16 | 107.550633 + 35.594163i | Xi_k+1 zero 112.598697 + 23.651800i |  |  | -8.916e-08 | 0 | 341 |
| 17 | 111.234679 + 37.095012i | Xi_k+1 zero 116.172195 + 25.249115i |  |  | -8.705e-08 | 0 | 341 |
| 18 | 114.889055 + 38.566417i | Xi_k+1 zero 119.724492 + 26.812979i |  |  | -8.509e-08 | 0 | 341 |
| 19 | 118.515192 + 40.010505i | Xi_k+1 zero 123.256046 + 28.345684i |  |  | -8.326e-08 | 0 | 341 |
| 20 | 122.114411 + 41.429158i | Xi_k+1 zero 126.767348 + 29.849295i |  |  | -8.156e-08 | 0 | 341 |
| 21 | 125.687939 + 42.824054i | Xi_k+1 zero 130.258906 + 31.325674i |  |  | -7.998e-08 | 0 | 341 |
| 22 | 129.236912 + 44.196693i | Xi_k+1 zero 133.731239 + 32.776508i (outside W) |  |  | -7.851e-08 | 0 | 341 |
| 23 | 132.762384 + 45.548423i (start outside W) | Xi_k+1 zero 137.184864 + 34.203325i (outside W) |  |  | -7.713e-08 | 0 | 341 |
| 24 | 136.265339 + 46.880464i (start outside W) | Xi_k+1 zero 140.620297 + 35.607518i (outside W) |  |  | -7.584e-08 | 0 | 341 |
| 25 | 139.746691 + 48.193917i (start outside W) | Xi_k+1 zero 144.038042 + 36.990356i (outside W) |  |  | -7.464e-08 | 0 | 341 |
