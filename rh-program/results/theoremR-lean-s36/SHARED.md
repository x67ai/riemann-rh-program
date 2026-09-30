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
