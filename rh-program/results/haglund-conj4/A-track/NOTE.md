# haglund-conj4 / A-track — NOTE (branch census for F_k(z,t) = Xi_k + t Phi_{k+1})

## Plan (unit A-track; written before reading the brief in full — refined below)
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

## Plan refined after reading the brief (16:20 IST 2026-10-03)
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

## §0 Census table (P1: W_k = [0, X_k] x [0, Y_k], X_k = 2 pi (k+2)^2 + 30) — rows added as each k is final
Columns: R_k / R_{k+1} = real zeros of Xi_k / Xi_{k+1} in (0, X_k] (sign changes of S_k - 1 and S_k on a grid of
spacing/20, roots refined; Haglund p. 4 in brackets); NR = non-real zeros of Xi_k / Xi_{k+1} in W_k; B = branches
followed (= NR of Xi_k); L = landings; E = ends at a non-real zero of Xi_{k+1}; X = exits through Re z = X_k;
dy+ = largest step increase of Im z over all branches (negative = Im z decreased at every step); m = smallest margin
-Im S'/|S'| above height 1e-6; checks: A = argument-principle count of Xi_k and Xi_{k+1} on [0,X_k] x [-Y_k,Y_k] equals
R + 2 NR (floating point; "A4" = same count at 4 Y_k; "W" = rigorous hag_core winding), C1 = every non-real zero of
Xi_{k+1} in W_k is a branch end, C2 = L = (R_{k+1} - R_k)/2, C3 = landings = local maxima of S_k in (0,1) one to one,
D = no local minimum of S_k in (0,1) on [0, X_k] and every (0,1)-interval consistent, H = hygiene (half-step re-trace
of one branch in ten agrees, routes L/T agree at 5 points per branch for k <= 6, every S value has Arb relative radius
<= 2^-40).

| k | X_k | Y_k | R_k / R_{k+1} [Haglund] | NR k / k+1 | B | L | E | X | dy+ | m | checks passed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 86.55 | 41 | 1 / 7 [1 / 7] | 15 / 11 | 15 | 3 | 11 | 1 | -3.7e-7 | 0.719 | A, A4, C1, C2, C3, D, H (re-trace 2/2: landing x to 1.0e-12, end z to 0; L/T 75 pts, max rel diff 3.0e-13; max Arb rel radius 9.0e-13) |
| 2 | 130.53 | 50 | 7 / 15 [7 / 15] | 23 / 18 | 23 | 4 | 18 | 1 | -3.1e-07 | 0.806 | A, A4, C1, C2, C3, D, H; re-trace 3/3 (ends to 7.6e-12); L/T 115 pts max rel 1.3e-13; Arb rel radius <= 9.0e-13 |
| 3 | 187.08 | 59 | 15 / 31 [15 / 32] | 35 / 25 | 35 | 8 | 25 | 2 | -3.3e-07 | 0.812 | A, A4, C1, C2, C3, D, H; re-trace 4/4 (ends to 1.2e-12); L/T 172 pts max rel 1.8e-13; Arb rel radius <= 8.3e-13 |
| 4 | 256.19 | 68 | 31 / 53 [32 / 53] | 47 / 34 | 47 | 11 | 34 | 2 | -3.2e-07 | 0.797 | A, A4, C1, C2, C3, D, H; re-trace 5/5 (ends to 5.1e-12); L/T 235 pts max rel 3.0e-13; Arb rel radius <= 8.7e-13 |

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
