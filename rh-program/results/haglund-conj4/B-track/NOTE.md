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
