# THEOREM R in Lean — the Comparator topic `ResidueRank` — SHARED log (builder Opus 5.5, then the checker); Session 36, 2026-09-30

Unit brief `results/theoremR-lean-s36/UNIT-BRIEF.md` SHA-256 `60b131b3353f944b101bca54609cd07f591fad4c20618fab5387b6a03d42068e`; typing probe
`results/theoremR-lean-s36/typing-probe.lean` SHA-256 `881e024a9184e9e4aab0976e42a31f1d8f8f5f01b3cec10c773a00f236601a81` (byte-identical to the
orchestrator's run copy `~/rh-lean-work/checker-clone-s33-h4/probe_s36.lean`, `diff` empty). Record read against: `results/beta-shapes-s35/NOTE.md`
(SHA-256 `49eb8e12…`) §1.1, §2.0, §2.3; `results/beta-shapes-s35/read-O.md` (SHA-256 `1614bcbb…`) §2.5. Every block dated by `date`. Label:
barrier hardening. Nothing about ζ's zeros or RH follows from anything in this unit (Theorem R is RH-blind, NOTE §2.3 DH CHECK).

## [builder] Wed Sep 30 17:19:00 IST 2026 — start
Brief, probe, NOTE §1.1/§2.0/§2.3, read-O §2.5 read; the packaging template `results/h4-pair-lean-s33/` (BUILD-NOTES, FIDELITY, hashes, logs, tools),
`lean/comparator/{Challenge,ChallengeDeps,Solution,PrintAxioms}/PairChannel.lean`, `config-pair-channel.json`, `results/d1-m2a/packaging/COMPARATOR-RUN.md`
and the runner `results/h5-c2-lean-s32/tools/run.sh` read. Build tree: `~/rh-lean-work/checker-clone-s33-h4` (Lean v4.33.0-rc2, Mathlib
`51e6992efd06126df61a496bebf8f49482a4e129`, checked by `git -C .lake/packages/mathlib rev-parse HEAD`). Pin facts checked by a scratch `#check` probe:
the unused-variable linter DOES fire on an unused hypothesis in a theorem signature at this pin; `HasSum` carries a `SummationFilter` argument
(default unconditional) at 51e6992e; `Infinite.exists_not_mem_finset` is named `Infinite.exists_notMem_finset`; no Mathlib lemma states the
ℚ-linear independence of the logarithms of the primes (grep of `Mathlib/` for `LinearIndependent` near `log`: one hit, the regulator of a number
field — unrelated). Next: deliverable 1, `PREDERIVATION-ERRATA.md`.

## [builder] Wed Sep 30 17:21:33 IST 2026 — deliverable 1 landed: `PREDERIVATION-ERRATA.md` (+ `tools/errata_numbers.py`, `tools/errata_numbers.log`)
Verdict: all eight statements TRUE and faithful (abstractions listed, none adds a hypothesis); **stop line (i) does not fire**. One erratum
against the brief's sketches: **E1** — "for κ ≤ 0 the hypothesis is contradictory at n = 2" holds for κ = 0 only; for κ < 0 the hypotheses are
satisfiable (cls = id, v = Λ/κ) and the theorem still holds; Theorem R's proof uses no hypothesis on κ (the ℚ-linear map x ↦ κx pushes finiteness
from the diagonal-row span to span{log N_p}, against item 2), so `hκ` is kept and UNUSED. Removable displayed hypotheses (kept, recorded):
item 4's `2 ≤ n` (E2 — answers the brief's question: not needed), item 5's `1 ≤ a` (E3), item 3's `hpos` (E4), item 8's `hg` (E5). Needed:
item 2's `hpos` and `hdvd`, item 7's `hg` (g = −1 counterexample), item 8's `hκ` (κ = 0 counterexample). Item 7 re-derived at every step,
g = 0 and x < 0 included; its bound is ATTAINED at x = r², L = 1 + r² + 2gr (E7, exact). No ChallengeDeps module (E9). No Mathlib lemma for
item 1 (grep recorded). SHA-256 `PREDERIVATION-ERRATA.md` = ef565ba553eb30e6cac660391da5496500a58f50596c7951adbdcf0033869f12; `tools/errata_numbers.py` = a847a63ce5089efbcdccd50d3930d74c9fa35cf95d14a40790d9a069be55091f; `tools/errata_numbers.log` = 874bff745f14a910aa97ec990971cdba54e6caecad69007db9ee09b4193b9831.
Next: rung 1 — `lean/Zeta23/ResidueRank/LogPrimes.lean` (items 1–3) in the build tree, `lake build Zeta23.ResidueRank.LogPrimes`, `rung1-print-axioms.log`.

## [builder] Wed Sep 30 17:27:58 IST 2026 — rung 1 landed: `lean/Zeta23/ResidueRank/LogPrimes.lean` (items 1–3) built alone, axioms clean
`logP`, `expVec` (+ `_apply`, `_one`, `_mul`, `_prime`), `linearCombination_expVec_prime`, `linearCombination_expVec` (Σ_q v_q(n) log q = log n,
induction on primes), `log_mem_span_logP`, `padicValRat_finset_prod`, `padicValRat_prime`, `linearIndependent_logP`, **`log_primes_linearIndependent`**
(item 1: over ℤ by `LinearIndependent.iff_fractionRing ℤ ℚ`, then Π p^{m_p} = 1 and the q-adic valuation), **`span_log_not_finite`** (item 2: coordinates by
`LinearIndependent.repr`, `Module.Finite.exists_fin`, a prime outside the finite union of supports), **`rank_span_log_le`** (item 3: `Submodule.rank_mono` +
`rank_span_finset_le`). One design point: rewriting under the coercion `Nat.Primes → ℕ` fails at this pin (`Nat.Primes` is a def; `rw`/`simp` refuse a target
"not type-correct under the implicit transparency level" when an anonymous constructor ⟨p, hp⟩ meets α = Nat.Primes), so the internal work uses the named
family `logP` and variables of type `Nat.Primes`; item 1's statement is `logP`'s by definitional unfolding. Build: first elaboration 4 errors (all that
coercion issue, and one un-beta-reduced goal), second elaboration clean; `lake build Zeta23.ResidueRank.LogPrimes` *Built (10s), 8697 jobs*, 13.23 s real,
0 warnings (`rung1-build.log`). `rung1-print-axioms.log` (probe `rung1-axioms.lean`): 15 names × `[propext, Classical.choice, Quot.sound]`. Stop line (ii)
does not fire: item 1 with its two valuation helpers is 54 lines, lines 103–156 (the whole module 234 lines, header included). Mirrored by `cp`, `cmp` identical.
SHA-256 `LogPrimes.lean` = 9a76d1311a2bc33b795caa8ded3bcde9477208a001c6e367499de27f98a55893.
Next: `lean/Zeta23/ResidueRank/Pair.lean` (items 4–6).

## [builder] Wed Sep 30 17:34:12 IST 2026 — deliverable 3 landed: `Pair.lean` (items 4–6) and `GenusBound.lean` (items 7–8) built and timed; `LogPrimes.lean` amended
**`Pair.lean`** (221 lines): `log_two_le_vonMangoldt`, **`lemmaF_finite_fiber`** (item 4: `Summable.tendsto_cofinite_zero`, finitely many terms ≥ log 2),
`fiber_sum_eq_log` (Lemma F(a)'s second clause: κ·v(cls n) = log Π minFac over the fiber's prime powers — `hasSum_sum_of_ne_finset_zero` + `HasSum.unique`),
**`lemmaF_infinite_order`** (item 5: the injective family j ↦ p^{a+jk} in one fiber), `theoremR_of_A9` (Theorem R with NO hypothesis on κ: N_p := fiber product,
p ∣ N_p, log N_p = κ·v(cls p), so span{log N_p} ≤ (diagonal-row span).map (x ↦ κx), finite if the latter is — against item 2), **`theoremR`** (item 6, the brief's
binders, `_hκ` unused — errata E1), and the errata's E2/E3 kernel-checked: `lemmaF_finite_fiber_all` (no `2 ≤ n`), `lemmaF_infinite_order_all` (no `1 ≤ a`).
**`GenusBound.lean`** (132 lines): **`theoremS_bound`** (item 7, 62 lines with its statement — stop line (iv), 120 lines, does not fire; the errata-E7 route,
`nlinarith` with explicit product hints), **`theoremS`** (item 8: a prime above exp(κ·bound) by `Nat.exists_infinite_primes`), `theoremS_abs` (E5: no `0 ≤ g`).
**`LogPrimes.lean`** amended after rung 1 (246 lines): `rank_span_log_le_of_supp` (E4 kernel-checked: no positivity; an N i = 0 contributes Real.log 0 = 0) and
`rank_span_log_le` now its corollary with `_hpos`; nothing else changed (the rung-1 record `rung1-print-axioms.log` is of the pre-amendment file,
SHA-256 9a76d131…; the amended file's names are all in `program-axioms.log`). Elaboration: Pair.lean first try 1 error (`hasSum_sum_of_ne_finset_zero`'s
`SummationFilter` argument had to be given: `(L := SummationFilter.unconditional _)`) + 2 deprecation warnings (`push_neg`, `Set.mem_setOf_eq` — the step rewritten
with `Set.eq_empty_of_forall_notMem`), second try clean; GenusBound.lean clean at the first elaboration. **Builds** (`program-build.log`, one lake at a time,
`/usr/bin/time -l`): LogPrimes *Built (3.2s)* 6.05 s real; Pair *Built (3.1s)* 5.09 s real; GenusBound *Built (7.3s)* 9.39 s real; 8697/8698/8697 jobs; 0 warnings;
max RSS ≈ 5.9 GB (Mathlib's oleans mapped). **`program-axioms.log`** (probe `program-axioms.lean`): 27 names × `[propext, Classical.choice, Quot.sound]`, no `sorryAx`,
no `Lean.ofReduceBool`. Mirrored by `cp`, `cmp` identical. SHA-256: LogPrimes.lean 1d5f4e28a9612ec0d0dc5849ddf7ba907de166dbaea159fbd9f8252f152f050d;
Pair.lean 4fc07998bf03dd0c20150b82d7b9a79fd35170609cbd561a5d817aeac32c87e0; GenusBound.lean d24145eb8a19cb08ac87bc32bff5cde64d4635d685501908161f80f08c1df7d6.
Next: the Comparator topic `ResidueRank` (challenge, solution, print-axioms, config), statement identity, trust greps, the comparator run with nanoda.

## [builder] Wed Sep 30 17:37:37 IST 2026 — deliverable 4 in progress: the Comparator topic `ResidueRank` written, built once, checked; the comparator run launched
Files (build tree → `cp` → `rh-program/lean/`, `cmp` identical, `trust-greps.log` last section): `comparator/Challenge/ResidueRank.lean` (header with the WHAT IS
CLAIMED / NOT paragraph, then from `import Mathlib` to the end the typing probe character for character — `statement-identity.log` [D]: 3536 bytes IDENTICAL),
`comparator/Solution/ResidueRank.lean` (the eight statements byte-identical, each proof the program theorem of the same name applied to the same arguments;
imports `Zeta23.ResidueRank.Pair`, `Zeta23.ResidueRank.GenusBound`; never the challenge), `comparator/PrintAxioms/ResidueRank.lean`,
`comparator/config-residue-rank.json` (ONE topic, the eight names `ResidueRank.*` in the challenge's order, `propext`/`Quot.sound`/`Classical.choice`,
`enable_nanoda: true`). **No ChallengeDeps module** (errata E9: no definitions needed; the challenge imports Mathlib, as the probe does). No root import added to
`lean/Zeta23.lean`: the H4 precedent added none for its program modules (`PairRow`/`PairCert` are absent from it), and the root there imports modules that the
build tree lacks. `build-comparator-topic.log`: `lake build Challenge.ResidueRank Solution.ResidueRank` — Solution *Built (3.5s)* 0 warnings, Challenge *Built (3.5s)* with
exactly the 8 deliberate `sorry` warnings, 8701 jobs, 5.61 s real. `print-axioms.log`: 8 × `[propext, Classical.choice, Quot.sound]`. `statement-identity.log`
(`tools/statement_identity_s36.py`, the H4 extraction): [A] challenge vs solution 8/8 IDENTICAL on the build tree AND on `rh-program/lean`; [B] challenge vs probe 8/8;
[C] config order = challenge order PASS; [D] whole-text identity PASS; RESULT PASS. `trust-greps.log` (`tools/trust_greps_s36.py`, comments stripped, nine words): on
both roots exactly the 8 challenge `sorry`s, nothing in the three program modules, the solution, the print-axioms file; no `set_option`, no attribute. 
`prerun-cleanup.log` (`tools/prerun-cleanup.sh`): the 16 artifacts of `Challenge/ResidueRank` and `Solution/ResidueRank` under `.lake/build/{lib/lean,ir}` removed,
0 remaining; the program modules stay built. Comparator run launched with `tools/run.sh` (the H4 runner; only the comment line and the `cd` target
`~/rh-lean-work/checker-clone-s33-h4` differ — `diff` shown in the session) → `comparator-run.log`.

## [builder] Wed Sep 30 17:38:25 IST 2026 — deliverable 4 landed: **the comparator run PASSES** (`comparator-run.log`)
17:37:22–17:37:55 IST, `32.26 real`, max RSS 5.85 GB; runner `tools/run.sh` from `~/rh-lean-work/checker-clone-s33-h4`; comparator v4.33.0, lean4export
v4.33.0-rc2, nanoda 0.4.17, the fake-landrun shim — NOT sandboxed, as in every macOS record (COMPARATOR-RUN.md §2); the four tool SHA-256s printed in the log
equal COMPARATOR-RUN.md §1's (fe1222e2…, de4ffedf…, d6c87133…, 167507c8…). Steps: `Building Challenge.ResidueRank` → *Built (2.0s)* with the 8 deliberate
`sorry` warnings, 8697 jobs; the export of the 8 names (+ the comparator's primitives) from the challenge; `Building Solution.ResidueRank` → *Built (3.0s)*,
0 warnings, 8700 jobs; the same export from the solution; then verbatim: `Running nanoda kernel on solution` / `Nanoda kernel accepts the solution` /
`Running Lean default kernel on solution.` / `Lean default kernel accepts the solution` / `Your solution is okay!`; `--- comparator exit code: 0 ---`. What the run
established: each solution statement coincides constant for constant with its challenge namesake (the constants are Mathlib's — there is no trusted
definition layer); the proofs use no axiom outside the three; nanoda re-checked the solution export and Lean's kernel replayed it. SHA-256
`comparator-run.log` = ea685bae7d4e4415d7a72fd25e1ec24f4c8beed7deca9a31c1002ed9bf835602.
Next: BUILD-NOTES.md, FIDELITY.md, the yaml rows, the README section, the lint, hashes.txt.

## [builder] Wed Sep 30 17:45:14 IST 2026 — deliverable 5 landed; the BUILDER's work is complete (hand-off to the orchestrator, then the clean-clone CHECKER)
`BUILD-NOTES.md` (SHA-256 f882e480d764c2f554d042f6903fe28b9e2cef0f15d7d8544e579c99af56ab25), `FIDELITY.md` (b25f4f45c9df01145ff83921ccc55c4ea9690451c155c2c7ff7732ce100df3c2; covered: the eight statements; NOT covered: A6–A8 and A7's graphs, the target Y, the
general-base Theorem R, Lemma F(a)'s second clause as a topic statement and Lemma F(c), the rung-1 side, the geometric reading of items 7–8, ζ, RH;
fidelity divergences in the brief's sense: NONE; **item 6's `hκ` is NOT used by the proof**), `lean/formalization.yaml` (status.scope sentence,
main_results entry, automation model "Claude Opus 5.5", fidelity row (aa), review.notes paragraph, two namespaces, three alignment rows;
`yaml-validation.log`: the D5/H5/H4 validator — VALIDATION errors 0, undeclared names 0, RESULT PASS), `lean/README.md` section "ResidueRank (Session
36, 2026-09-30)" (its quick-check commands re-run as written: RESULT PASS, 8 hits), `lint-10g.log` (`tools/lint_10g.py`: the four banned phrases 0
everywhere, the brief's forbidden phrasings 0 everywhere — read from the brief, not quoted —, British forms 0, five RH/zeros lines without an
on-line negation reviewed by hand: disclaimers and the Lean case name `zero`; PASS), `hashes.txt` (SHA-256 2badc8cfa545c73b9973a611bb7f4cfe1501a539444568fba50c6554053b8073; 33 files).
PREDERIVATION-ERRATA.md final SHA-256 d0431cb5213a8d51d31deb1d67d5c030d144538d1c47a56642a062adb97383a0 (after its §4 addendum).
**Outcome.** All eight statements PROVED; the Comparator run with nanoda PASSES; every name at `[propext, Classical.choice, Quot.sound]`; the label of
UNIT-BRIEF §1(3) is earned verbatim; no stop line fired. For the orchestrator: ERRATUM **E1** against the brief's item-6 parenthetical (κ < 0 is not
contradictory; the proof needs no hypothesis on κ); the removable displayed hypotheses E2–E5 (kept verbatim; removals kernel-checked program-side);
item 7's bound is attained (E7). Nothing committed. Nothing about ζ's zeros or RH follows.
