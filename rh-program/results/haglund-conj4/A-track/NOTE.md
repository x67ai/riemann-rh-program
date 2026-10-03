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
