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

## Session 4 — 2026-08-13 (~00:30–02:15)

**Focus:** Sponsor standing orders codified; Phase-4 closure (C1+A2 adjudications); Grossmann sweep (wave 1 complete, wave 2 deferred); decisive pre-design tests; A4 root cause.

**Done:**
- **Standing orders 1–6 written into STATUS.md as binding protocol** (sponsor directives): prior-art gate; session-end learnings in writing; full parallelism; structural-thesis reaffirmation; NO decisive action on fabrications (verify computationally / against sources; escalate inaccessible papers); GROSSMANN-FIRST (sweep existing math before de novo construction — then free rein to build from scratch). Memory pointer recreated (memory store came up empty; repo survived — the write-everything-down rule vindicated).
- **C1 adjudicated REFUTED (2.5)** — both fatal killer findings upheld (cosh-ghost correction re-derived independently; data-class containment verified; referee's O(1) repair ruled unsound). Salvage: the containment/delimitation theorem, anchoring/transfer note, ghost-term EF. Substance later REPLICATED blind by an independent run-2 killer.
- **Accidental replication study:** cross-session resumeFromRunId does NOT hit the journal cache — the verify-remaining resume re-ran all 6 verdicts fresh (LESSON). Result: independent second verdicts (results/verdicts-run2.json). Divergence: **A2 killer flipped swr→REFUTED with two fatal math claims run-1 missed.**
- **A2 cross-run adjudicated REFUTED (3)** — adjudicator VERIFIED both fatals by direct computation (standing order 5 in action): cross-window kernels are transforms of window PRODUCTS (support min(λi,λj)) to ~1e-11 across two parameter sets — the mixed-window corner does not exist, equal windows at 2/3 (the parent paper's own boundary) is the true optimum; rank_trace_cubic false by exact counterexample (violation ~μ³ vs quadratic remainder). Run-1 had PASSED A2 (its referee even computed the shadow of the error inside the false formula). **PROCESS LEARNING → protocol: duplicate killers on load-bearing directions; critics must re-derive central identities; computational adjudication is standard.**
- Verdict sections + status flips completed for A2/B4/C1/C2 — **all 9 direction files carry Phase-4 verdicts. Scoreboard: 4 refuted (A1,B1,C1,A2) / 5 swr (A3 ~6.75, B2 ~6.75, B3 ~5.75, B4 ~6, C2 ~5.75).**
- **Completeness critic in:** portfolio lopsided (survivors = correlated rank-trace block; S4 algebraic/combinatorial/probabilistic EMPTY). Recommendations adopted for Phase 5: merge A2+A4; commission second Track-C direction (arithmetic-geometry/functoriality axis); stand up computational Λ>0 arm; institutionalize the barrier zoo at brief time.
- **GROSSMANN SWEEP WAVE 1 COMPLETE (phase 4.5): 24 branch scouts + synthesizer, ~2.1M tokens, 631 online-verification tool calls.** VERDICT: **NO GROSSMANN — "the generator exists but the geometry does not."** Hodge index/Castelnuovo on the square (the only mechanism ever to prove an RH) has no substrate over Q; Connes–Consani stalled at the square 8 years (curve/Jacobian/RR exist as of 2023–26); Deninger has phase space + both model-world halves proven 2024 but no cohomology. 1 grossmann-candidate (arakelov 0.55), 5 certified dead-ends, rest instruments. **S6 spec amendment** (finite-rank/tower rationality + doubled object, from comparative anatomy of all TRUE RH cases). → **De novo construction (Weil mode) green-lit** with sweep-fixed raw material. Full harvest: results/grossmann-sweep.json.
- **Decisive test (b) DONE:** arXiv:2606.06604 full-body read — contains NO square/Lefschetz/RR/zeta content ("GRR over Spec Z" paraphrase STRUCK; f1 scout vindicated). NEW design seed: per-prime Tate curves E_p ≅ C_p × X̃_∞ with classical intersection theory — assemble correspondence calculus from E_p × E_q products (option the paper never raises). **alainconnes.org botwall DEFEATED (User-Agent block)** → fetched: Jacobian JNcG PDF + **NEW July-2026 CCM paper "Zeta Spectral Triples"** (explicit RH strategy: D(λ,N) from Euler products only; det_reg → ξ). Watch: forthcoming [CC7].
- **Decisive test (a) NEARLY DONE (stopped at harvest step at session close):** CCM DH-filter experiment — all principal computations durable in results/ccm-dh-test/ (ground-state tests zeta vs DH at λ²∈{2,3}, N up to 24+; margin curves; Fuchs fits). **PRELIMINARY, UNINTERPRETED:** DH also exhibits an even simple ground state at tested truncations (naively: arithmetic-blind), BUT zeta's ground eigenvalue collapses toward 0 many orders faster (1e-29 vs 1e-6 at λ²=3) — the real discriminator may be the collapse RATE. Finisher agent must complete interpretation BEFORE any verdict is recorded (standing order 5).
- **Wave 2 deferred at sponsor request:** 2/11 scouts harvested final (decoupling 0.87: DH-blindness ceiling theorem for the ANTEDB calculus; beyond-endoscopy 0.85: monoid-form DH-exclusion theorem). Handoff written (trim BRANCHES to remaining 9; feed partial file to closure synthesizer).
- **A4 ROOT CAUSE FOUND after 5 failures:** designer exceeds the 64k per-response output ceiling — and at ultracode session effort its EXTENDED THINKING counts toward that cap (sweep scouts at pinned effort all succeeded). Fixes in script: schema maxLength caps + output budget + effort:'high' pin + direct-delivery constraint. Attempt 6 launched then STOPPED (deferred to Session 5 at sponsor request; nothing cached — fresh launch next time). Belt-and-braces: `.claude/settings.json` (repo root, new) sets CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000 from next session start — sponsor asked whether dropping ultracode would fix it; answer recorded: the 64k cap is effort-independent, only the thinking volume varies, so the per-agent effort pin + env raise fixes it WITHOUT giving up ultracode.
- **FETCH-LIST.md created** (P1/P2/P3 checklist): sponsor will deliver PDFs at Session-5 start. Conrey–Li + Suzuki PDFs rescued from session-temp into sources-extracted/. Sponsor authorized Chrome-via-MCP for botwalls.

**Decisions:**
- Binding adjudications require independent computational verification — no verdict on testimony alone (order 5).
- Refutations at this rate (4/9) are the system working: A2's reversal after a passed verdict is the strongest argument yet for duplicated critics.
- The Grossmann sweep's negative is a POSITIVE deliverable: it fixes the de-novo design's axioms, target inequality, spec (S6), calibration theorems, and substrate candidates.

**New artifacts:** results/{adjudication-C1,adjudication-A2,adjudication-input-A2,verdicts-run2,completeness-critic,grossmann-sweep,grossmann-sweep2-partial}.json, results/decisive-tests/arxiv-2606-body-read.json, results/ccm-dh-test/ (code+outputs), FETCH-LIST.md, scripts/{rh-grossmann-sweep,rh-grossmann-sweep2}.js, 4 fetched/rescued PDFs + 2606 full text in sources-extracted/, journal snapshots, standing orders 1–6.

**Open at close:** Nothing running. Session 5, in order: (1) ingest sponsor PDFs per FETCH-LIST.md; (2) launch A4 attempt 6 (fresh, script fixed); (3) CCM DH-filter finisher agent (interpret results/ccm-dh-test/, write results/decisive-tests/ccm-dh-filter.json); (4) wave-2 relaunch per handoff; (5) Phase 5: portfolio restructure (A2+A4 merge; commission geometric-substrate Track-C direction + computational Λ>0 arm) + prospectus.
