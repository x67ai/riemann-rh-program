# haglund-conj4 / A-track — NOTE (branch census for F_k(z,t) = Xi_k + t Phi_{k+1})

Unit A-track of the stream haglund-conj4 (writer). Brief: ../BRIEF-A-track.md. Code: code/, data: data/, figures: figures/, logs: logs/.
Status: in progress — rows are added to the tables of §0 as each k is final; the close block ends §0.

## §0 Results

### §0-P1 Census table (P1: W_k = [0, X_k] x [0, Y_k], X_k = 2 pi (k+2)^2 + 30) — rows added as each k is final

Columns: R_k / R_{k+1} = real zeros of Xi_k / Xi_{k+1} in (0, X_k] (sign changes of S_k - 1 and S_k on a grid of
spacing/20, roots refined; Haglund p. 4 in brackets); NR = non-real zeros of Xi_k / Xi_{k+1} in W_k; B = branches
followed (= NR of Xi_k); L = landings; E = ends at a non-real zero of Xi_{k+1}; X = exits through Re z = X_k;
dy+ = largest step increase of Im z over all branches (negative = Im z decreased at every step); m = smallest margin
-Im S'/|S'| above height 1e-6; checks: A = argument-principle count of Xi_k and Xi_{k+1} on [0,X_k] x [-Y_k,Y_k] equals
R + 2 NR (floating point; "A4" = same count at 4 Y_k; "W" = rigorous hag_core winding — not affordable at this size, §2 T2), C1 = every non-real zero of
Xi_{k+1} in W_k is a branch end, C2 = L = (R_{k+1} - R_k)/2, C3 = landings = local maxima of S_k in (0,1) one to one,
D = no local minimum of S_k in (0,1) on [0, X_k] and every (0,1)-interval consistent, H = hygiene (half-step re-trace
of one branch in ten agrees, routes L/T agree at 5 points per branch for k <= 6, every S value has Arb relative radius
<= 2^-40).

| k | X_k | Y_k | R_k / R_{k+1} [Haglund] | NR k / k+1 | B | L | E | X | dy+ | m | checks passed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 86.55 | 41 | 1 / 7 [1 / 7] | 15 / 11 | 15 | 3 | 11 | 1 | -3.7e-07 | 0.708 | A, A4, C1, C2, C3, D, H; re-trace 2/2 (ends to 1.0e-12); L/T 75 pts max rel 3.0e-13; Arb rel radius <= 9.0e-13 |
| 2 | 130.53 | 50 | 7 / 15 [7 / 15] | 23 / 18 | 23 | 4 | 18 | 1 | -3.1e-07 | 0.806 | A, A4, C1, C2, C3, D, H; re-trace 3/3 (ends to 7.6e-12); L/T 115 pts max rel 1.3e-13; Arb rel radius <= 9.0e-13 |
| 3 | 187.08 | 59 | 15 / 31 [15 / 32] | 35 / 25 | 35 | 8 | 25 | 2 | -3.3e-07 | 0.812 | A, A4, C1, C2, C3, D, H; re-trace 4/4 (ends to 1.2e-12); L/T 172 pts max rel 1.8e-13; Arb rel radius <= 8.3e-13 |
| 4 | 256.19 | 68 | 31 / 53 [32 / 53] | 47 / 34 | 47 | 11 | 34 | 2 | -3.2e-07 | 0.797 | A, A4, C1, C2, C3, D, H; re-trace 5/5 (ends to 5.1e-12); L/T 235 pts max rel 3.0e-13; Arb rel radius <= 8.7e-13 |
| 5 | 337.88 | 79 | 53 / 79 [53 / 79] | 63 / 47 | 63 | 13 | 47 | 3 | -3.0e-07 | 0.828 | A, A4, C1, C2, C3, D, H; re-trace 7/7 (ends to 3.1e-11); L/T 315 pts max rel 2.2e-13; Arb rel radius <= 9.1e-13 |
| 6 | 432.12 | 90 | 79 / 113 [79 / 113] | 82 / 62 | 82 | 17 | 62 | 3 | -3.0e-07 | 0.832 | A, A4, C1, C2, C3, D, H; re-trace 9/9 (ends to 1.1e-11); L/T 410 pts max rel 2.6e-13; Arb rel radius <= 9.0e-13 |
  (k = 6: one branch, from 425.6801 + 82.8913i, reaches u = 0 at the zero 432.1548 + 63.0618i of Xi_7, just beyond X_6 = 432.1239; counted as an exit.)
  (Haglund column: arXiv v1 / journal table; the author's 2011 web copy prints 31 at N = 4 (L-lit, SHARED 16:18), as found here.)
<!-- P1 rows -->

### §0-P2 Frontier windows (window [4(k+1)^2 - 40, 4(k+2)^2 + 40] x [0, Y]; branches that start in it; same columns)
| k | window | Y | R_k / R_{k+1} | NR k / k+1 | B | L | E | X | dy+ | m | checks passed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 26 | [2876, 3176] | 69 | 45 / 263 | 133 / 17 | 133 | 109 | 17 | 7 | -3.0e-07 | 0.868 | A, A4, C1, C2, C3, D, H; re-trace 14/14 (ends to 3.6e-10); Arb rel radius <= 9.0e-13 |
| 27 | [3096, 3404] | 70 | 48 / 276 | 137 / 16 | 137 | 114 | 16 | 7 | -3.0e-07 | 0.851 | A, A4, C1, C2, C3, D, H; re-trace 14/14 (ends to 4.3e-10); Arb rel radius <= 9.1e-13 |
<!-- P2 rows -->

### §0-P3 The real-axis test (d) alone, k = 1..50, on [0, 4(k+2)^2 + 40]
Grid of spacing/20 (spacing = 2 pi / log(x / 2 pi)) on the whole interval; every discrete extremum whose parabola value
is in (-10, 11) refined to a zero of S_k' (Arb central difference); the frontier part [4(k+1)^2 - 40, end] scanned again
at spacing/40 and compared. Columns: R_k / R_{k+1} real zeros of Xi_k / Xi_{k+1}; max / min = local maxima / minima of
S_k with value in (0,1); "half" = (#max - #min) = (R_{k+1} - R_k)/2; "int" = every maximal interval where 0 < S_k < 1 has
the extrema its end types require ([0,0]: one more max than min; [1,1]: one more min; mixed: equal); "re" = the finer
frontier rescan finds the same zeros and extrema; u_min = smallest landing value; last = largest real zero of Xi_{k+1}
(Haglund's table, N = k+1 <= 10: 39.5324810798, 65.0320737720, 103.3679880094, 149.0026994921, 197.9575955732,
258.5304836632, 327.3794646017, 406.8174206801, 489.3900649445). PASS = no minimum, all of half/int/re, S_k(0) > 1, S_k(end) < 0.
| k | end | R_k / R_{k+1} | max | min | half | int | re | u_min | last | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 76 | 1 / 7 | 3 | 0 | yes | yes | yes | 7.0e-07 | 39.5325 | PASS |
| 2 | 104 | 7 / 15 | 4 | 0 | yes | yes | yes | 1.1e-07 | 65.0321 | PASS |
| 3 | 140 | 15 / 31 | 8 | 0 | yes | yes | yes | 6.1e-12 | 103.3680 | PASS |
| 4 | 184 | 31 / 53 | 11 | 0 | yes | yes | yes | 1.4e-15 | 149.0027 | PASS |
| 5 | 236 | 53 / 79 | 13 | 0 | yes | yes | yes | 1.9e-17 | 197.9576 | PASS |
| 6 | 296 | 79 / 113 | 17 | 0 | yes | yes | yes | 1.6e-19 | 258.5305 | PASS |
| 7 | 364 | 113 / 155 | 21 | 0 | yes | yes | yes | 4.7e-22 | 327.3795 | PASS |
| 8 | 440 | 155 / 207 | 26 | 0 | yes | yes | yes | 1.3e-26 | 406.8174 | PASS |
| 9 | 524 | 207 / 263 | 28 | 0 | yes | yes | yes | 3.6e-29 | 489.3901 | PASS |
| 10 | 616 | 263 / 327 | 32 | 0 | yes | yes | yes | 2.5e-31 | 580.0556 | PASS |
| 11 | 716 | 327 / 401 | 37 | 0 | yes | yes | yes | 5.3e-34 | 681.6374 | PASS |
| 12 | 824 | 401 / 483 | 41 | 0 | yes | yes | yes | 1.1e-36 | 789.8537 | PASS |
| 13 | 940 | 483 / 575 | 46 | 0 | yes | yes | yes | 3.6e-40 | 907.0997 | PASS |
| 14 | 1064 | 575 / 673 | 49 | 0 | yes | yes | yes | 1.0e-42 | 1029.0743 | PASS |
| 15 | 1196 | 673 / 781 | 54 | 0 | yes | yes | yes | 8.1e-45 | 1161.3203 | PASS |
| 16 | 1336 | 781 / 899 | 59 | 0 | yes | yes | yes | 2.1e-48 | 1301.2536 | PASS |
| 17 | 1484 | 899 / 1027 | 64 | 0 | yes | yes | yes | 7.8e-51 | 1450.5619 | PASS |
| 18 | 1640 | 1027 / 1163 | 68 | 0 | yes | yes | yes | 4.1e-54 | 1606.0765 | PASS |
| 19 | 1804 | 1163 / 1307 | 72 | 0 | yes | yes | yes | 6.8e-55 | 1768.2781 | PASS |
| 20 | 1976 | 1307 / 1463 | 78 | 0 | yes | yes | yes | 1.4e-57 | 1940.9312 | PASS |
<!-- P3 rows -->

<!-- close block -->

## §1 Checks of the charter's and ORCH-NOTES' mathematics used here (as made)
- C1 (N1, the u-form). F_k(z,t) = Xi_k + t Phi_{k+1} = Xi_{k+1} - (1-t) Phi_{k+1}, so where Phi_{k+1}(z) != 0 the zeros at
  parameter t are the solutions of S_k(z) = u, u = 1 - t. Confirmed (one line of algebra). Along a branch dz/du = 1/S_k';
  dz/dt = -1/S_k' = -conj(S_k')/|S_k'|^2, so Im(dz/dt) = Im S_k'/|S_k'|^2 and (D) <=> Im S_k' <= 0 on the branch.
  The brief's margin -Im S_k'/|S_k'| is the sine of the descent angle (1 = straight down). Confirmed.
- C2 (integral form). hag_core's Phi_n equals int_0^oo phi_n(t) cos(zt) dt, phi_n(t) = exp(-n^2 pi e^{2t})(8 pi^2 n^4 e^{4.5t}
  - 12 pi n^2 e^{2.5t}) (Riemann's term): mpmath quadrature against hag_core at z = 5, 2+i, 3i for n = 1, 2 agrees to
  12 digits (NUMERICAL). ORCH-NOTES N1 writes 2 int phi~_n cos; consistent with main.tex, where phi~_n is one half of
  phi_n. No discrepancy.
- C3 (left edge). phi_n(t) = 4 pi n^2 e^{2.5t} exp(-n^2 pi e^{2t}) (2 pi n^2 e^{2t} - 3) > 0 for t >= 0, so
  Phi_n(iy) = int phi_n cosh(yt) dt > 0 and Xi_N(iy) > 0 for every real y, N >= 1. PROVED (from C2's representation,
  which is Haglund's derivation of (14); checked numerically in C2).
- C4 (count formula). Xi_N(conj z) = conj Xi_N(z); for a rectangle [a,b] x [-Y,Y] with Xi_N(a), Xi_N(b) != 0 the zero
  count is (arg change of Xi_N along (b,0)->(b,Y)->(a,Y)->(a,0))/pi. With a = 0 the left edge contributes nothing (C3).
- C5 (real axis). Phi_{k+1} > 0 on R (main.tex sandwich, termwise, n >= 2), so S_k is real-analytic on R; real zeros of the
  pencil at u are S_k(x) = u; a local max of S_k with value u* in (0,1) is a landing at u*, a local min a departure. The
  real count changes only there (S_k(0) > 1 and S_k < 0 near X_k are checked in every scan), so
  #landings - #departures = (R_{k+1} - R_k)/2. Confirmed.

## §2 Tool notes and attempts (as made)
- T1. Arb degeneracy on the imaginary axis: for x = 0 exactly, b +- i z/2 = b - y/2 is real, and python-flint's
  gamma_upper at the points b - y/2 = 0, -1, -2, ... (y = 4.5 + 2n for b = 9/4) drove the adaptive precision loop
  into a runaway (observed: a strip count with left edge on x = 0 hung > 2 min in acb_hypgeom / acb_calc_integrate).
  Fix: the left edge x = 0 is not sampled (its arg change is 0 by C3); seeds start at x >= 0.01; precision cap 20000 bits.
- T2. ATTEMPT 1 — rigorous count by hag_core.winding (route L on boxes) on [-X_1, X_1] x [-41, 41] (Xi_N even, so the
  count there is twice the count on [0, X_1] x [-41, 41]) — breaks at: the box enclosures. A box 86.5 + [10, 10.2]i
  gives Xi_1 in a ball of radius 0.02 around values of size 1e-5 (route T boxes give nan at y = 41), so pieces need
  bisection far below depth 14; stopped after 3.5 min CPU for N = 1 at the first side. Not affordable at the size of W_k
  with these enclosures; every count in this NOTE is the floating-point argument principle, labeled as such.
- T3. Floating-point argument principle (zeros.argpath): arg of the exact midpoint of the Arb value (24 bits relative),
  adaptive bisection until every increment is below pi/4 (minimum segment 1e-9; a segment that cannot reach it is
  counted as a flag; flags = 0 in every count reported); total rounded, deviation from an integer reported (< 1e-12
  in every P1 count so far).

- T4. Margin bookkeeping fix (17:10 IST): the first runs (P1 k = 1..6, P2 k = 26, 27) recorded -Im S'/|S'| at the
  accepted interior nodes only. code/endmargins.py added the margin at every start (zero of Xi_k) and every u = 0 end
  (zero of Xi_{k+1}) and re-summarized; the tracer now includes both. Only k = 1 changed in the table (0.719 -> 0.708,
  at the start 20.6253 + 2.6972i); the largest change of a branch minimum was 0.039 (k = 6).
- T5. Positive controls (code/controls.py, data/controls_lam5e-05.json): the pencil built on Xi + lam, lam = 5e-5
  (S^lam_k = (Xi_{k+1} + lam)/Phi_{k+1}, route L). (i) The axis scan finds, for k = 1 on [0, 76], a local maximum at
  22.54201999 (value 0.62819) and a local MINIMUM at 24.34012104 with value 0.6119951561613 — the reader read-O's
  independent value is 0.611995156161 (SHARED 16:46). (ii) At the zero near beta = 28.6324463545 + 8.5242688193i the
  margin is negative: -0.874 (k = 2), -0.831 (k = 3), -0.811 (k = 5), -0.806 (k = 8); for k = 2 the trace records a
  step increase of Im z of +8.4e-7; for k >= 3 the whole branch is shorter than double precision (the pencil zero moves
  by ~ Phi_{k+1}/|Xi_k'|), so the margin, not the step increase, is the detector there. Both detectors fire.

## §3 P2 sites (k = 26, 27)

### P2 site, k = 26 (the Conjecture-1 violation of Xi_27)
- The branch from the zero 3130.2619 + 52.4297i of Xi_26 ends at u = 0 at 3143.2206824215 + 0.3152587994i (Newton on
  Xi_27 from the brief's value converges to 3143.2206824215364 + 0.3152587993782i; S_26 there 1e-88, S_27 = 1 to 1e-13).
  Im z decreased at every step (largest step change -6.3e-2; 216 steps), smallest margin 0.970.
- Its right neighbor, from 3132.1660 + 52.9056i, lands at x* = 3145.2290390026 at u* = 3.32e-76 (a local maximum of S_26);
  as u -> 0 the pair separates into the two real zeros of Xi_27 at 3144.8946622175 and 3145.5998495774 (in the brief's
  intervals). Its left neighbor, from 3128.3576 + 51.9536i, lands at 3141.3370957 at u* = 1.44e-75 (real zeros 3141.0818,
  3141.6310 of Xi_27). The branch between them is the one that does not land: S_26 has no local maximum in (0,1) on
  (3141.6310, 3144.8947) (the axis scan's extrema list on [3140, 3150] is exactly the two maxima above).
- Landings in the window happen at u between ~1e-69 and ~1e-76 near the site: t within 1e-69 of 1.

### P2 site, k = 27 (the continuation)
- The zero 3143.2206824215 + 0.3152587994i of Xi_27, followed in the pencil k = 27, lands at x* = 3143.2466268840 at
  u* = 0.41051 (t = 0.58949): Im z decreased at every step (36 steps), smallest margin 0.993. The pair it becomes
  separates, as u -> 0, into the real zeros 3142.979457 and 3143.567499 of Xi_28 (the positive lobe (3142.98, 3143.57)
  of Xi named in main.tex §5).
- The two real zeros of Xi_27 at 3144.8946622 and 3145.5998496 (S_27 = 1) stay real for 0 <= t <= 1: S_27 has no local
  extremum with value in (0,1) on [3144.49, 3146.29] (axis scan: the only extrema in (0,1) on [3138, 3150] are the
  maxima at 3143.2466, 3147.7040, 3149.3067), and they move monotonically to the real zeros 3144.490488 and 3146.283528
  of Xi_28 at u = 0.
- The next branches land at 3147.7040 (u* = 0.0302) and 3149.3067 (u* = 0.00527): in pencil 27 the landings near
  3143-3150 happen at u of order 1e-1..1e-3, against 1e-69..1e-76 in pencil 26 at the same heights.

## §4 Plan (as written at the start; history)

### Plan (unit A-track; written before reading the brief in full — refined below)
1. Read BRIEF-A-track.md, BRIEF-WARNINGS.md, CHARTER.md, SOURCES.md, ORCH-NOTES.md.
2. Run orch-probe/t2.py (k = 1 ladder) and read hag_core.py, c4probe.py, trace.py.
3. Build census tool: zeros of S_k(z) = u along u: 1 -> 0, branch tracking on Im S_k = 0,
   certified counts (argument principle / real sign changes), step hygiene.
4. P1 for k = 1..6: per-k row (real counts, non-real zeros in window, landings,
   non-real ends, exits, worst step increase of Im z, smallest margin, completeness).
5. P2 frontier windows for k = 26, 27.
6. P3 real-axis test k = 1..50.
7. P1 k = 7..12; P2 k = 15, 20, 35, 50.
8. P4 pictures (matplotlib).
9. Close block.
Each k's row goes here and a dated block to SHARED.md as soon as it is final.

### Plan refined after reading the brief (16:20 IST 2026-10-03)
- Evaluator `code/a_core.py`: S_k = Xi_{k+1}/Phi_{k+1} by routes T (adaptive M: tail < 2^-(bits+8)|value|) and L,
  precision raised until relative radius <= 2^-40 (2^-90 for the central-difference derivative, h = 1e-9).
- Real axis: one scan of S_k gives the real zeros of Xi_k (S=1) and Xi_{k+1} (S=0); extrema with value in (0,1)
  live only in maximal intervals where 0 < S < 1: a [0,0] interval holds a max (landing), a [1,1] interval a min (witness).
- Counts: Xi_N real on R, Xi_N(iy) > 0 (phi~_n > 0), so the zero count in [0,X]x[-Y,Y] is (arg change of Xi_N along
  right edge (X,0)->(X,Y) and top edge (X,Y)->(0,Y))/pi; rigorous `winding` of hag_core where affordable.
- Zeros of Xi_N off the axis: Haglund's appendix (N = 1), pencil ends, a march along the zero curve; complete when the
  located count equals (N_tot - R)/2.
- Tracer: arc-length predictor along -conj(S')/|S'|, chord-Newton corrector on Im S = 0, step control by corrector size
  and turning angle; ends: u = 0 (zero of Xi_{k+1}), landing (critical point of S on the axis), right edge.
