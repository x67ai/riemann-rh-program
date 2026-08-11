# RH Program — Session Log (append-only)

Chronological journal of the research program. One entry per working session. Never edit past entries; append corrections as new entries. STATUS.md is the always-current dashboard; this file is the historical record — when they disagree, this file explains why.

Entry template:
```
## Session N — YYYY-MM-DD
**Focus:** ...
**Done:** ...
**Decisions:** ... (and why)
**New artifacts:** ... (paths)
**Open at close:** ... (running tasks with journal paths, unanswered questions)
**Next session should:** ...
```

---

## Session 1 — 2026-08-11

**Focus:** Program launch. Ingest the zeta-2/3 artifact (paper + condensed + 95-page transcript + 103k-line Lean repo), establish state of the art, launch design phase.

**Done:**
- Phase 1 (Understand): 6-agent deep-read → `results/full-map.md`, `results/map-hooks.txt`. All 135 PDF pages extracted to `sources-extracted/`.
- Phase 2 (Literature): 12-front web reconnaissance → `results/literature.md`.
- Verified key numerics in Wolfram (Montgomery–Taylor constant, payoff curve λ≤1, two-moment cap 0.8453, HL*(4)→13/18 chain). Recorded in STATUS.md.
- Phase 3 (Design) launched: 8 designers (Tracks A1–A4, B1–B4), then +2 (Track C1–C2) after sponsor directive.
- Durable archive created (`rh-program/`), persistent memory pointer written.

**Decisions:**
- Two-track → three-track structure. Sponsor directive (recorded in STATUS.md): prioritize wholly new machinery (Tracks B/C); Track A reframed as instruments + specification-writing + proportion progress, not a competing bet on deciding RH with existing tools. Rationale: the repo formalizes its own no-go theorems; campaign post-mortem shows ~30 refuted routes all collapsing to Weil positivity; DH/Epstein filter implies the missing input is structural.
- Canonized the new-machinery specification S1–S5 in STATUS.md; every future design brief must cite it.
- Payoff-curve caveat: the unconstrained cosine-window formula is valid only for λ ≤ 1 (and ≲ π/√2); paper's 1.70→90% uses the constrained problem — use paper numbers beyond the band.

**New artifacts:** `STATUS.md`, `LOG.md` (this file), `results/{full-map.md, map-hooks.txt, literature.md}`, `sources-extracted/` (135 files), memory file `rh-research-program.md`.

**Open at close:**
- RUNNING: rh-design (8 designers), task wd7790w3z, run wf_30287ea4-643 — journal under `~/.claude/projects/-Users-jaytyagi-Documents-Work-2026-Math-riemann-anthropic/e8c24f5f-4faf-41e1-962d-7ba16dbd457a/subagents/workflows/wf_30287ea4-643/journal.jsonl`.
- RUNNING: rh-design-supplement (2 Track-C designers), task w4dxvhdce, run wf_2d492d18-6bd — journal `.../wf_2d492d18-6bd/journal.jsonl`.
- When they land: save all 10 proposals to `results/design-proposals.json`, create `directions/` files, update STATUS.md, append Session-1 addendum or Session-2 entry.

**Next session should (if this session ends before the workflows do):** follow STATUS.md "How to resume" step 2 — recover the 10 proposals from the two journals, then run Phase 4 (adversarial verification).

### Session 1 close — 2026-08-11 ~14:10 (user-requested pause)

**State at close:** Phases 1-2 ✅. Phase 3: 9/10 proposals done and durable (A4:lindelof-lock designer stopped mid-run, must re-run). Phase 4: launched then stopped ~12 min in, 0 verdicts journaled — relaunch from `scripts/rh-verify-wf_eb8254d0-341.js`. Phase 5 not started.

**Session-1 headline findings (beyond the phase artifacts):**
1. The zeta-2/3 artifact formalizes its own no-gos: two-moment certificates cap at 0.845 at ANY bandwidth; bandwidth-1 ceiling 0.6818; certificate cannot distinguish on-line double from off-line pair. All proportion progress must enter through one lemma chain (O1_bound → prop_PP → tr2); full RH cannot enter through this machinery at all (DH/Epstein filter).
2. Specification S1-S5 for new machinery canonized (STATUS.md).
3. INDEPENDENT CONVERGENCE: both Track-C designers, briefed differently, converged on Λ(n) ≥ 0 pointwise (positive prime measure) as the overlooked S1 input — violated by Davenport-Heilbronn, invisible to all L²-mean-value machinery. C1 = tilted reflection positivity ladder quasi-RH(a) with Krein-Langer multiplicity-visible indices (conf 0.6); C2 = explicit-formula conservation-law system with defect-cost rigidity (conf 0.55). B3 (tilt-jets arithmetic de Branges, conf 0.8) lands in the same basin from the B-track brief — three of ten designers, mutually blind.
4. Wolfram-verified: c₁* = 0.75329607, Thm D = 0.6725007; support targets 1.043→70%, 1.265→80% reproduced; 1.70→90% needs the constrained (CCLM17) problem; two-moment cap 2−2/√3 = 0.84530; HL*(4) chain 5/36 → 31/36 → 13/18 exact.

**Next session:** follow STATUS.md "PAUSED ... Resume actions" 1-5 verbatim.

## Session 2 — 2026-08-11 (~14:40–15:10)

**Focus:** Resume after Session-1 pause: relaunch Phase-4 verification + A4 re-run; put the program under git.

**Done:**
- Relaunched Phase-4 verify (19 agents, run wf_a2389ed4-3f1) and a new chained A4 design→verify workflow (`scripts/rh-a4-design-verify.js`, run wf_89b075e1-f64; A4 prompts repointed at durable rh-program paths — the Session-1 scratchpad was wiped, as predicted).
- Harvested **12/18 verdicts** at close → `results/verdicts-partial.json`; journals snapshotted. A4 designer died mid-run again (0 results) — pure relaunch next time.
- Wrote `scripts/rh-verify-remaining.js` (6 missing verdicts + completeness critic) so the done 12 are never re-run.
- **Git initialized** at the `riemann/` root (branch `main`), everything committed; git discipline added to the documentation protocol (commit per phase harvest + session end). gh authenticated as `x67ai`; repo creation blocked for the agent by permissions — sponsor will run `gh repo create riemann-rh-program --private --source . --remote origin --push` at a break.

**Decisions:**
- Stopped both workflows at the user's break request rather than letting them die with the session — frozen state is documented state.
- Early verdict signal recorded for adjudication: killers REFUTE A1 (1.5) and B1 (1.5); referees say survives-with-repairs (6.5/5). Both C-track pairs, kill:A2, kill:B4, completeness, and all of A4 still missing.

**New artifacts:** `results/verdicts-partial.json`, `scripts/rh-a4-design-verify.js`, `scripts/rh-verify-remaining.js`, journal snapshots `results/journals/wf_{a2389ed4-3f1,89b075e1-f64}.journal.jsonl`, git history (root commit d23a9ae).

**Open at close:** Nothing running. Killer-vs-referee conflicts on A1/B1 unadjudicated.

**Next session should:** follow STATUS.md "PAUSED ... Resume actions" 1–5 (launch the two scripts in parallel, merge verdicts, adjudicate conflicts, then Phase-5 synthesis).

## Session 3 — 2026-08-11 ~23:20 – 2026-08-12 ~00:15

**Focus:** Phase-4 completion push: the 6 missing verdicts, A4 re-run, A1/B1 conflict adjudication.

**Done:**
- Relaunched `rh-verify-remaining` + `rh-a4-design-verify`; both were orphaned mid-run when the machine slept (~23:26) and the session process died — relaunched again with `resumeFromRunId` from the background fork. Second attempt delivered **all 6 missing verdicts** (journal-cached for future resumes).
- **Phase 4 verdict matrix complete: 18/18** killer/referee verdicts → `results/verdicts.json` (single file; `-partial` deleted, subsumed).
- **Adjudicated A1 and B1 (binding): both REFUTED, final score 2.** A1: sieve envelope of the resonant block is X-sized, not second-order — proving the first theorem would BE averaged-HL below the Mikawa threshold (M5 smuggled into M1); adjudicator re-derived the scaling and the "deceptive dip" independently; zero killer findings overruled. B1: Möbius-mollifier fourth moment diverges (θ log T)² — confirmed independently by BOTH critics; Regime II is HL prime-pair input in disguise; S4 failure (same Weil cone, reweighted). Salvage lists recorded in `results/adjudication-{A1,B1}.json`.
- Wrote Phase-4 verdict sections + flipped statuses in 5 direction files: A1 (REFUTED), B1 (REFUTED), A3/B2/B3 (survive-with-repairs, no conflicts).
- New verdicts summary: A2 killer 4 swr; B4 killer 5 swr; C2 killer 5 / referee 6.5 swr; **C1 CONFLICT: killer REFUTED 2 vs referee swr 5.5 — unadjudicated**, input file + reusable adjudicator prompt template staged (`results/adjudication-input-C1.json`, `scripts/adjudicator-prompt-template.md`).
- Journals snapshotted to `results/journals/*.session3.journal.jsonl`; pushed to origin throughout.

**Decisions:**
- Pulled A1/B1 adjudication forward (parallel with the verify workflows) instead of waiting for synthesis — conflicts only needed already-harvested data. Worked well; C1 next.
- Adjudication standard recorded in the prompt template: refuted requires a specific checkable technical argument left unrebutted; Track-A scope ≠ full-RH scope; Track-B/C must meet S1–S5.
- At user pause request, stopped workflows mid-critic rather than waiting — the 6 verdicts were already journaled (cached on resume); only the completeness critic and A4 chain re-run.

**New artifacts:** `results/verdicts.json` (18/18), `results/adjudication-{A1,B1}.json`, `results/adjudication-input-{A1,B1,C1}.json`, `scripts/adjudicator-prompt-template.md`, journal snapshots, 5 updated direction files.

**Open at close:** Nothing running. Pending: C1 adjudication; completeness critic (cached resume); A4 design+kill+ref (3rd designer death — pure relaunch); verdict write-ups for A2/B4/C1/C2; then Phase-5 synthesis.

**Next session should:** follow STATUS.md "PAUSED 2026-08-12 ... Resume actions" 1–5 (three parallel launches, then write-ups, then synthesis).
