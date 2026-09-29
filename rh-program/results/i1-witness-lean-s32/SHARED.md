# I.1 witness table — SHARED log (builder Fable 5.1, then checker Opus 5); Session 32, 2026-09-29

Brief `BRIEF.md` SHA-256 `54ad13fb0b6197d241bae84de43942d6e1e7396bc0050eb965cc503f62aa3b69`. Every block dated by `date`.

## [builder] Tue Sep 29 07:37:22 IST 2026 — deliverable 1 landed: `PREDERIVATION-ERRATA.md`; rung 0 typing facts in `typing.log`
Verdict: no error that changes a value; stop line (iv) does not fire. Every (D2) coefficient, every a_n, every Epstein count re-derived
by hand against the record (E1–E6, E10, E12); two presentation gaps closed inside the proofs (E7: the ∀ p clause of (E2) is a lemma,
not a decide; E13: the "hence" needs the non-dividing primes' coefficients to vanish); typing notes E8 (LambdaReal over ℝ, the
Epstein array cast, commutation lemma), E9 (padicValNat reduces in the kernel — kept as the brief wrote); cost note E11 (n = 36
coefficient 3.6 s of kernel time each; no split; stop line (i) does not fire). Rung 0: lambdaVec is a fuel-structural recursion with
fuel n; the record's recursion is shipped as a theorem. SHA-256 PREDERIVATION-ERRATA.md = 6aea75b50fa424484808fd84f6b9b35004fca0d9aefadcca203dcfd86708c22c.
Next: the trusted file and the rung-1 pair (EpsteinWitnessSix) in lean/comparator/, mirrored to the tree, built, print-axioms, comparator.

## [builder] Tue Sep 29 07:42:51 IST 2026 — rung 1 (topic `EpsteinWitnessSix`, Λ_Q(6)) is a complete Comparator pair: PASS
Files (source of truth `lean/comparator/`, mirrored to `~/rh-lean-work/checker-clone-s21` by `cp`, cmp-identical): `ChallengeDeps/I1Witness.lean`
(the trusted layer: `lambdaVecAux`, `lambdaVec`, `LambdaReal`, `epsteinB`, `kappa`, `dhA`), `Challenge/EpsteinWitnessSix.lean` (3 statements, `sorry`:
`epsteinB_one`, `epstein_six_coeff`, `epstein_witness_6`), `Solution/EpsteinWitnessSix.lean`, `PrintAxioms/EpsteinWitnessSix.lean`,
`config-epstein-witness-six.json`. `lake build Solution.EpsteinWitnessSix`: first try, *Build completed successfully (8698 jobs)*, 0 errors,
0 warnings (9.4 s wall). `rung1-print-axioms.log`: three lines, each [propext, Classical.choice, Quot.sound]. `rung1-statement-identity.log`:
3 IDENTICAL on tree and mirror. `rung1-trust-greps.log` (RERUN section; the first section is the zsh one-argument slip, kept): the 3
deliberate challenge sorrys only; imports Mathlib / ChallengeDeps.I1Witness / Solution.* only. `rung1-prerun-cleanup.log`: 16 artifacts
removed. `rung1-comparator.log`: comparator with nanoda, `Built ChallengeDeps.I1Witness (2.9s)`, `Built Challenge.EpsteinWitnessSix` with its
3 sorry warnings, `Built Solution.EpsteinWitnessSix (3.2s)`, `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`,
`Your solution is okay!`, exit 0, 30.45 s real. Kernel time of the n = 6 decide: 77 ms (typing.log). Next: the unit `I1Witness`.
