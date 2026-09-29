# H4 — SHARED log (builder Fable 5.1, then checker Opus 5); Session 33, 2026-09-29

Unit brief `results/h4-pair-typing-s32/UNIT-BRIEF.md` SHA-256 `2d80f9db8ccf04765840b041189dc771813f5fdbb77767c40d471e8b9908cb94`. Every block dated by `date`. Nothing about ζ or RH
follows from anything in this unit.

## [builder] Tue Sep 29 11:21:44 IST 2026 — deliverable 1 landed: `PREDERIVATION-ERRATA.md` (+ `tools/h4_numbers.py`, `tools/h4_numbers.log`)
Verdict: the note's §2–§4 derivations are correct in substance; every anchor number reproduces (ā(1/4) = 1.10944370, ā(1/2) =
1.48140550, F1 − S2 = −0.0352002534 by closed form AND by the integer-frequency row; the reduced row gives −0.0144817; power sums
22880 / 14492192 / 10924353440 / 8964042662432; certified bound −0.033682 with L(3.141592) = 1.1060211, U(3.141593) = 1.4815182,
margin spent 0.001518; (MI) holds at the anchor, F1 − T = +3.67). Errata: E7 (the note's dyadic bracket 3294198/2²⁰ < π does not
follow from pi_gt_d6 — unused here), E5 (0.021 is an upper estimate of the per-cosh error at π/4, the value is 0.0162), E9 (the
Cauchy–Schwarz name is `sq_sum_le_card_mul_sum_sq`, Chebyshev.lean 136), E1/E10 design routes. No stop line fires.
SHA-256 `PREDERIVATION-ERRATA.md` = fb2a0683a8afef858c7f350d5cac26c729cf67dff341db765acb0c8fc99e154d.
Next: rung 1 — `lean/Zeta23/PairCeiling/PairRow.lean` items 1–4 (W2_eq, sum_W2_mul, pairRow_eq_gridRowQ, sum_W2_cosh), mirrored
to `~/rh-lean-work/checker-clone-s21`, `lake build Zeta23.PairCeiling.PairRow`, `rung1-print-axioms.log`.

## [builder] Tue Sep 29 11:29:57 IST 2026 — rung 1 landed: `lean/Zeta23/PairCeiling/PairRow.lean` items 1–4 built alone, axioms clean
`W2`, `pairFormFactor`, `pairRow`, `abar`, `vacancyMark` (the probe's forms; the one deviation: the unused summation binder of `W2`
is written `_j` so the module builds with 0 warnings — recorded for FIDELITY); `card_band`, `W2_eq`, `sum_W2_mul` (the inner reindex
+ `sum_comm` route, errata E1), `pairRow_eq_gridRowQ`, `sum_sinh_band`, `sum_W2_cosh`. Mirrored by `cp` to
`~/rh-lean-work/checker-clone-s21/Zeta23/PairCeiling/PairRow.lean`. `lake build Zeta23.PairCeiling.PairRow`: first try 2 errors (an
extra `ring`, a no-op `beta_reduce`), second try *Built (1.6s), Build completed successfully (2274 jobs)*, 0 errors, 0 warnings.
`rung1-print-axioms.log` (probe `rung1-axioms.lean`): 6 names × `[propext, Classical.choice, Quot.sound]`. Stop line (i) did not fire
(`sum_W2_mul`: one build attempt, 33 lines). SHA-256 of the rung-1 `PairRow.lean` (will change when §4–§5 are appended): f5cff1349fc1f2b83129d6f671586c1b81c8542ec0440b91d4cdf35637b8cbfe.
Next: §4 Prop. 4.5 for every n (`dftMarkQ_vacancy`, `W2_zero`, `abar_zero`, the three sums, `prop45`), §5 the chain (`one_le_abar`,
`abar_sq_le`, `floor_holds_integer`).

## [builder] Tue Sep 29 11:37:08 IST 2026 — §4–§5 of `PairRow.lean` and the certificate `PairCert.lean` built and TIMED
`PairRow.lean` (now complete; SHA-256 133f04a2c74e28c87007d9228d2132e40117924c2ca3ba7caa72dc97a1a04722): `intCast_zmod_eq_zero_iff`, `dftMarkQ_vacancy`, `W2_zero`, `abar_zero`, `sum_vacancyMark_sq`,
`sum_W2_vacancy_sq`, `sum_W2_vacancy_cosh`, `sum_W2_cosh_sq`, **`prop45` for every n, d, μ** (stop line (ii) did NOT fire: general n, 250-line
budget not approached, no hypothesis), `one_le_abar`, `abar_sq_le` (Cauchy–Schwarz `sq_sum_le_card_mul_sum_sq`, import
`Mathlib.Algebra.Order.Chebyshev` added), `floor_holds_integer`. Two build rounds of fixes (a decidable-instance rewrite inside an `if`
replaced by a case split; `Finset.sum_div` is not a name at 51e6992e — the 1/2 is folded out with `mul_sum`; two extra `ring`s after
`field_simp`), then *Built (1.9s), 2282 jobs, 0 errors, 0 warnings*.
`PairCert.lean` (SHA-256 9c9691b5c3d2178394308203a9766858a8f7422a963a4154d28f5e1027314c8e): `one_add_sq_half_le_cosh`, `exp_sub_sum_le` (the ℝ transfer of `Complex.exp_bound'` at n = 8, 12 lines —
stop line (iv) did NOT fire), `cosh_le_poly8`, `sum_pow2/4/6/8` (`decide +kernel`), their ℝ casts, `card_band32`, `sum_poly2`, `sum_poly8`,
`abar32`, `abar_quarter_ge`, `abar_half_le`, `abar_quarter_ge_L`, `abar_half_le_U`, `cert_numeric` (one `norm_num`), **`floor_fails_anchor`**.
First try built with one linter nit (fixed). TIMED (`cert-build.log`): `lake build Zeta23.PairCeiling.PairCert` — Built (1.8s), 2.72 s wall
for the lake call, max RSS 2.57 GB; `lake env lean` of the file alone 2.38 s wall; the four power sums alone: kernel type checking 58 ms.
Stop line (iii) (ten minutes) is under by a factor of about 200. Next: the Comparator topic `PairChannel` (five files + config), tools, build,
axioms, identity, greps, cleanup, the run with nanoda.

## [builder] Tue Sep 29 11:42:15 IST 2026 — the Comparator topic `PairChannel` PASS with nanoda (exit 0); the Lean files are now FROZEN (no edit after the run)
Files (source of truth `lean/comparator/`, mirrored to the clone by `cp`, `cmp`-identical): `ChallengeDeps/PairChannel.lean` (Mathlib only,
namespace `PairChannel`: the seven IntegralityGap definitions + the five of PairRow.lean, all character for character — `trust-greps.log`),
`Challenge/PairChannel.lean` (the eight statements, byte-identical to the probe's — `statement-identity.log`), `Solution/PairChannel.lean`
(eight one-line delegations to PairRow/PairCert), `PrintAxioms/PairChannel.lean`, `config-pair-channel.json` (8 names, three axioms,
nanoda). `build-comparator-topic.log`: ChallengeDeps 18 s, Challenge 3.0 s (8 deliberate sorry warnings), Solution 4.0 s with 0 warnings,
8704 jobs, first try. `print-axioms.log`: 8 × [propext, Classical.choice, Quot.sound]; `program-axioms.log`: the 34 program-side names
likewise. `statement-identity.log`: 8/8 IDENTICAL on clone and tree; 8/8 IDENTICAL against the probe; config order = challenge order.
`trust-greps.log`: the 8 challenge sorrys only; imports as designed; tree = mirror ×7; 7/7 and 5/5 definitions character for character; the
one deviation from the probe is W2's binder `_j`. `prerun-cleanup.log`: 25 artifacts removed. **`comparator-run.log`: 11:40:58–11:41:45
IST, 46.93 s real, max RSS 5.8 GB; Built ChallengeDeps.PairChannel (5.2s), Challenge.PairChannel (3.0s), Solution.PairChannel (3.0s);
Nanoda kernel accepts the solution; Lean default kernel accepts the solution; Your solution is okay!; --- comparator exit code: 0 ---.**
The fake-landrun shim (NOT sandboxed) as in every prior macOS record; the four tool SHA-256s in the log equal COMPARATOR-RUN.md §1's.
Stop lines (i)–(vi): none fired; no displayed hypothesis beyond the statements' own → the label of §1(3) is earned verbatim.
Next: BUILD-NOTES.md, FIDELITY.md, the yaml rows, the README section, the formalization-status addendum, validation, lint, hashes.

## [builder] Tue Sep 29 11:50:19 IST 2026 — packaging done; BUILDER DONE. Label earned verbatim; the Opus 5 clean-clone check is the next job
Written: `BUILD-NOTES.md` (SHA-256 11d0dca35019fb7411f8ea5401e0065c7cd72da074bf42c5c34ad998f36f1955), `FIDELITY.md` (covered: the eight statements; NOT covered: (MI) at any anchor — it HOLDS at
this one, a Python fact; Theorems 4.6–4.9; laws/LP; general positions; Prop. 4.1's ledger; the value −0.0352; ζ, RH; rows (z1)–(z12)),
`lean/formalization.yaml` (scope sentence, main_results entry, fidelity row (z), review paragraph, 3 namespaces, 2 statements rows;
`yaml-validation.log`: PASS, errors 0, undeclared names 0, 32 main_results, 40 alignment.statements), `lean/README.md` (section
"PairChannel (Session 33, 2026-09-29)" before "What these build against"), `results/a4-no-go/formalization-status.md` (a dated Session-33
addendum; earlier records untouched), `lint-10g.log` (the four banned phrases: 0 everywhere; British spellings: none; the three
FORBIDDEN phrasings: absent from every file, comments included; the looser 'formalized/closed near IV.17/pair channel' net hits only the
FIDELITY sentence that states the rule and the status addendum's quotation of the Session-30 record "Still NOT formalized: the pair
channel" — both quotations of the rule/record, neither an application), `hashes.txt` (SHA-256 f33f488eca4e95f374cbb96977cc7fb0182c1873730d3db54f84f8462fdd1fe4; 32 files).
Corrections to earlier blocks of this log, measured at the file (BUILD-NOTES carries the measured figures): `sum_W2_mul` is 34 lines
(statement and proof), not 33; `exp_sub_sum_le` is 16 lines, not 12; `prop45` is 20 lines and §4 with its eight helpers 153 lines.
Not done, by the brief: no commit, no push, no edit of any Lean file after the comparator run, nothing outside this folder and
`lean/` except the status addendum. Stop lines: none fired. Nothing about ζ or RH follows.
