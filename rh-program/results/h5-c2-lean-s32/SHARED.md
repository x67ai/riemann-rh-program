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

## [builder] Tue Sep 29 06:37:47 IST 2026 — rung 1 (topic `WeilContainmentC2One`, L = log 3) is a complete Comparator pair: PASS
Files (source of truth `lean/comparator/`, mirrored to `~/rh-lean-work/checker-clone-s21` by `cp`): `Challenge/WeilContainmentC2One.lean`
(1 statement, `weilContainment_c2_interpolant_log3`, `sorry`), `Solution/WeilContainmentC2One.lean` (the general proof `interpolant` for
every band L in namespace `WeilContainmentC2One.Proof` — one `ContDiffBump (0:ℝ)` with rIn = log (max I), rOut = L, times Mathlib's
`Lagrange.interpolate` in u² — instantiated at L = log 3), `PrintAxioms/WeilContainmentC2One.lean`, `config-weil-containment-c2-one.json`.
`lake build Solution.WeilContainmentC2One`: first try 4 errors (an instance-path mismatch under `simpa` in the polynomial lemma, the
explicit `r` argument of `Lagrange.eval_interpolate_at_node`, and `tsupport 0` versus `tsupport fun _ => 0`), second try *Build completed
successfully (8698 jobs)*, 0 errors, 0 warnings. `rung1-print-axioms.log`: [propext, Classical.choice, Quot.sound]. `rung1-prerun-cleanup.log`:
the topic's artifacts removed. `rung1-comparator.log` (runner `tools/run.sh`, the D5 runner byte for byte but for its comment line):
Built ChallengeDeps.WeilContainment (2.9s), Built Challenge.WeilContainmentC2One (2.9s) with its one deliberate `sorry` (41:8), Built
Solution.WeilContainmentC2One (3.3s), `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`, `Your solution is
okay!`, `--- comparator exit code: 0 ---`, 68.70 s wall. `statement-identity.log` first section: IDENTICAL on the tree and on the mirror.
Next: the family (topic `WeilContainmentC2`, general L).

## [builder] Tue Sep 29 06:40:55 IST 2026 — the family (topic `WeilContainmentC2`, every band L) is a complete Comparator pair: PASS
Files: `Challenge/WeilContainmentC2.lean` (1 statement, `weilContainment_c2_interpolant`, `sorry`), `Solution/WeilContainmentC2.lean` (its own
copy of the general proof, namespace `WeilContainmentC2.Proof`), `PrintAxioms/WeilContainmentC2.lean`, `config-weil-containment-c2.json`;
mirrored by `cp`, cmp-identical. `lake build Solution.WeilContainmentC2`: *Build completed successfully (8698 jobs)*, 0 errors, 0 warnings,
first try. `print-axioms.log`: [propext, Classical.choice, Quot.sound]. `statement-identity.log` second section: IDENTICAL on the tree and
on the mirror. `trust-greps.log` (RERUN section after a zsh word-splitting slip, kept in the log): exactly the 2 deliberate challenge
`sorry`s (C2One 46, C2 50); imports Mathlib / `ChallengeDeps.WeilContainment` / `Solution.*` only; tree = mirror for the 7 topic files and 2
configs; `ChallengeDeps/WeilContainment.lean` SHA-256 47c9a508… = the D5 record (unchanged). `prerun-cleanup.log`: the topic's artifacts removed.
`comparator-run.log`: Built ChallengeDeps.WeilContainment (2.9s), Built Challenge.WeilContainmentC2 (2.9s) with its one deliberate `sorry`
(46:8), Built Solution.WeilContainmentC2 (3.3s), `Nanoda kernel accepts the solution`, `Lean default kernel accepts the solution`, `Your
solution is okay!`, `--- comparator exit code: 0 ---`, 68.13 s wall, max RSS 5.9 GB.
Next: FIDELITY.md, BUILD-NOTES.md, the yaml rows, the README section, the D5 (N2) correction, hashes.txt.

## [builder] Tue Sep 29 06:46:25 IST 2026 — closing block: every deliverable on disk; label earned; no stop line fired
Written this stage: `FIDELITY.md`, `BUILD-NOTES.md`, the yaml rows (description paragraph, status sentence, main_results entry, row (x), the
FORMALIZED pointer inside row (u), two alignment rows; validator PASS, `yaml-validation.log`), the README section "WeilContainmentC2
(Session 32, 2026-09-29)", the dated FORMALIZED correction appended to `results/d5-lean-s30/FIDELITY.md` (N2) — the only edit outside
this folder and `lean/` — `lint-10g.log` (PASS), `hashes.txt`.
Theorems shipped: `weilContainment_c2_interpolant_log3` (topic `WeilContainmentC2One`) and `weilContainment_c2_interpolant` (topic
`WeilContainmentC2`), each `[propext, Classical.choice, Quot.sound]`; comparator exit 0 with nanoda on both configs.
Label (verbatim, earned): "IV.1 formalized-in-Lean — prime-side containment into Zeta23's C² test class for continuous g (prime-side
values; the C² witness is an interpolant at ±log n, not the tilted test; zero side untouched)". Fidelity divergences (a hypothesis
beyond the three): none. Stop lines: none fired.
SHA-256: BUILD-NOTES.md 421db9a63aa787663a2f727037ceaaa5c3ce1b961f4d119b56052e069eeba44e; FIDELITY.md bb499197be2d8ce5f3c870ed7439c2d542da6b025ebd90be37bf09bb92c4c4d1; hashes.txt 2deb306d25d5508ab91419eb8832c76bb87b945f82f1de73bac8120e52c4d0d1; PREDERIVATION-ERRATA.md bf31def42315df09f2ee1a03376a48744883a317750d41e3a6951f10399898a7.
Next: the Opus 5 clean-clone CHECKER (BRIEF §3) — `CHECK-O.md` in this folder; nothing committed by the builder.
