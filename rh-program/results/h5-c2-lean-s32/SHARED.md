# H5 — SHARED log (builder Fable 5.1, then checker Opus 5); Session 32, 2026-09-29

Brief `BRIEF.md` SHA-256 `1a2e8a3acb4c6ba0623a9cf91ac515952490d49767717dd4b09af45f5c4e49ab`. Every block dated by `date`.

## [builder] Tue Sep 29 06:30:41 IST 2026 — deliverable 1 landed: `PREDERIVATION-ERRATA.md`
Verdict: the pre-derivation is correct in substance; statement shape unchanged; stop lines (i) and (iv) do not fire. Items: E1 (gap:
the split L < log 2 / otherwise misses L = log 2, where I = ∅ and (P3)'s "nonempty" fails — repaired by splitting on I = ∅), E2 (the
evenness of g is unused; kept as displayed, recorded), E3 (design: one bump at 0 with rIn = log(max I), rOut = L, times the Lagrange
interpolant in u² replaces the δ-separated bumps; still an interpolant at ±log n), E4–E7 checks with no error (the closed-set argument
for g = 0 on Ici L; distinctness; the rpow identity; the ContDiff index type). ContDiffBump lemmas present at the brief's line numbers.
SHA-256 `PREDERIVATION-ERRATA.md` = bf31def42315df09f2ee1a03376a48744883a317750d41e3a6951f10399898a7.
Next: the rung-1 files (`WeilContainmentC2One`) in `lean/comparator/`, mirrored to `~/rh-lean-work/checker-clone-s21`, built, print-axioms, comparator.
