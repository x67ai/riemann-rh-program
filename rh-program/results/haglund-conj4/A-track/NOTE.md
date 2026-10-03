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
