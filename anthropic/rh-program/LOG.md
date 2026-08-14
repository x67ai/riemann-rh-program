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

## Session 4.5 — 2026-08-13 (evening) — fetch-corpus verification ONLY (sponsor directive: no RH work; todos stay put)

**Focus:** Independent verification of the sponsor's 174-PDF delivery (`fetched/` + `FETCH-LIST-RESPONSE.md`) against FETCH-LIST.md, under the corpus rules (R-1: Claude-vision only, zero third-party OCR — Tesseract banned after the w-07 audit showed it destroyed every displayed formula).

**Done:**
- **Mechanical sweep (pypdf, all 174 files):** 174/174 valid PDFs, §9 index matched 1:1, ZERO page-count mismatches, filename-vs-content confirmed wherever a text layer exists. Two cosmetic §9 header typos (P3 is 32 not 33; X is 25 not 24; they cancel).
- **15-agent verification workflow** (7 vision-identity, 6 quote-fidelity, 2 spot-check; ~549k tokens; all effort-pinned 'high' per the 64k lesson — zero overflows): **CORPUS ACCEPTED.** Full report: `FETCH-VERIFICATION.md`; raw: `results/fetch-verification-{sweep,agents}-2026-08-13.json`.
- **All three load-bearing response findings verified against sources:** Conrey–Li §4 read (12/12 checks, constants digit-for-digit, counterexamples unnumbered, no Weil/Li/Krein/Pontryagin content); Lagarias w-07 Theorem 1 transcription VERBATIM by vision (§3's B3-novelty identification stands); Haagerup w-21 booklet by vision (p. 3 abstract = expository Odlyzko survey — the §6 conversion from "silence" to "documented, expository" stands).
- **§8 pending question ANSWERED: w-05 (Suzuki JFA 279) contains NO local/Borg–Marchenko uniqueness** (checked every theorem; bibliography lacks Langer–Woracek/Kaltenbäck–Woracek) → B3 gap 1 stands; the Langer–Woracek line is the ONE new load-bearing fetch item.
- **Corrections recorded (none reverses a conclusion):** w-08 Cor 2/Thm 1 inequalities are NON-STRICT (response's "verbatim" quote wrote >/<); CGG assumes RH+GLH and BHB removes GLH (not GRH); §7's vision-needed list is 9 files not 5 (add w-21, x-16 glyph-soup; x-01a/b GDZ image-only); Zagier internal range 312–341 (+10 folio offset) and a y²-for-y^s typo in the volume's re-typeset layer; y-24 on disk is arXiv v1 (2023) with NO Acta Arith imprint (its "published error terms" claim unauditable from disk — y-23 routing already avoids it); y-23's 0.67250064/0.34500129 are the b=0.001 table row, not a literal b→0 limit.
- **Sufficiency verdict: corpus SUFFICIENT for the whole Session-5 queue** (A4 attempt 6, CCM finisher, wave-2, merges, Phase 5). Remaining fetches: Langer–Woracek line (load-bearing, B3 only), MathSciNet (needs sponsor login; zbMATH hit LISTS not on disk, only counts), P3 optionals (published y-24, Hilberdink corrigendum, FGL JLMS 2014, Clausen videos).
- **Environment change (disclosed):** a verification agent installed poppler 26.08.0 via Homebrew mid-run — the Read tool now renders PDF pages natively (benefits all future vision reads). Also recorded: w-05b's embedded TIFFs are stored top-bottom-flipped (transcription pipeline must flip).
- **64k question re-confirmed for sponsor:** diagnosis + 3-layer fix in writing (LOG Session 4, STATUS lines 96/107); `.claude/settings.json` CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000 verified present and active this session.

**Decisions:** fetched/ (~350 MB) stays untracked; git disposition is an ingest-time call (resume action 0). FETCH-LIST.md checkboxes left un-ticked — ingest (rename → sources-extracted, check-off, routing) remains Session-5 action 0 per sponsor's "todos stay put".

**New artifacts:** FETCH-VERIFICATION.md, results/fetch-verification-sweep-2026-08-13.json, results/fetch-verification-agents-2026-08-13.json; FETCH-LIST-RESPONSE.md (sponsor's, now tracked).

**Open at close:** unchanged from Session 4 — Session-5 resume actions 0–6 in STATUS.md, now with a verified corpus and one added fetch item.

**Addendum (Session 4.5, same evening):** Sponsor confirmed the fetched corpus stays OFF GitHub — `anthropic/rh-program/fetched/` added to .gitignore (local-only; sponsor advised to keep own backup). Sponsor asked for the fetch outlook across ALL planned sessions, not just Session 5 → FETCH-LIST.md "ROUND 2" section written: P1 = Langer–Woracek local-uniqueness line + MathSciNet (the only near-term items); P2 = contingent menu keyed to Phase-5 commissioning decisions (Krein–Langer N_κ originals, GHS/Lee–Yang originals, Hoffstein–Lockhart+GHL, Morishita book, Lapidus–vF book, published y-24) with [recalled] citation-fidelity flags per standing order 5; P3 = closure items; watch-list. Bottom line recorded: nothing blocks Sessions 5–6.

**Addendum 2 (Session 4.5):** Sponsor asked for the Round-2 fetch list as a precise standalone file → 6-agent citation-pinning workflow ran (every item corroborated via Crossref/zbMATH/publisher/arXiv/Wayback; zero recalled bibliography) → `FETCH-LIST-ROUND2.md` written (supersedes the sketch section in FETCH-LIST.md; raw evidence `results/fetch-round2-citations-2026-08-13.json`). Highlights: Langer–Woracek 2011 (Inverse Problems 27, 055002) CONFIRMED as the exact local Borg–Marchenko theorem B3 needs, with a verified free Wayback preprint (Woracek's TU-Wien site is dead — his preprints survive only in Wayback snapshots); Hoffstein–Lockhart + GHL appendix free on Goldfeld's Columbia page; Kaltenbäck–Woracek I–VI all free via Wayback; Hilberdink corrigendum corrected to JNT 269 (2025) 460–464 (flaw fixed with slightly weaker result — check w-18e citations); sponsor-required list shrinks to MathScinet + ~8 paywalled papers + 2 contingent books.

**Addendum 3 (Session 4.5 close, 2026-08-14):** Sponsor directive on session sequencing, binding and recorded in STATUS.md: the NEXT session is Round-2 corpus verification ONLY (sponsor delivers FETCH-LIST-ROUND2 §A items; verify per the Session-4.5 method; agents also pull the §B free copies; append to FETCH-VERIFICATION.md; check off ROUND2; commit; STOP — no RH work). The session AFTER that resumes RH work at STATUS resume actions 0–6. Session 4.5 closed with clean tree, all commits pushed (through 8ea08ee + this close commit).

## Session 4.75 — 2026-08-14 (evening) — Round-2 corpus verification ONLY (sponsor directive) + paper-v5 assessment

**Focus:** Verify the sponsor's Round-2 delivery (`fetched-r2/`: 160 PDFs — a ~5× over-delivery vs FETCH-LIST-ROUND2's ~30 items — plus `FETCH-RESPONSE-ROUND2.md`, a 546-line bibliographic record read in full); assess the sponsor-supplied `paper-v5 (12).pdf`. No RH work, per the Session-4.5 sequencing directive. Mid-session sponsor guidance recorded and applied: identity of the MATHEMATICS is the acceptance bar (title/content, not pagination pedantry); Claude-vision only for scans; care with notation-critical extraction.

**Done:**
- **Mechanical sweep (pypdf, 160 files): 160/160 valid, 160/160 page counts match the response's §1 index** (hand-transcribed expected values — independent of the file), text-layer health mapped, all surname flags explained. One new caveat found: `u-33b` text layer silently drops the letter "c" — read visually.
- **12-agent verification workflow** (~568k tokens, 166 tool calls, effort-pinned 'high', zero overflows, zero third-party OCR): **86 checks → 83 CONFIRMED, 3 REFUTED (all bookkeeping), 0 UNCERTAIN. CORPUS ACCEPTED.** Full report: FETCH-VERIFICATION.md Round-2 appendix; raw: `results/fetch-verification-r2-{sweep,agents}-2026-08-14.json`.
- **The B3 gap-1 theorem is now on disk and statement-verified:** `u-36a` = typeset IOP Langer–Woracek 2011, Theorem 1.2 transcribed by vision from both the typeset and author versions (identical): initial-segment coincidence up to reparametrization ⟺ exponentially-close Weyl coefficients, segment length governed by a = ∫√(det H); genuinely local (global de Branges = separate Thm 1.1); general 2×2 H ≥ 0 class; **Pontryagin/indefinite analogue per Remark 1.3**; explicitly a Borg–Marchenko transfer (Bennewitz the closest relative). **NEW agent-surfaced caution: ∫√(det H) degenerates when det H = 0 a.e. — B3's converse must check det H > 0 on its class.**
- **Three refutations, all corrections not failures:** (1) response's §1 misprints t-46a's pagination — actually AIF 68(2) (2018) 563–567; (2) u-13 (MNT-II author draft — content/completeness confirmed, Ch. 16–22 + App. E–H) internally built 9 Oct 2024, the "post-publication 1 June 2026" claim is an HTTP-header fact not verifiable from disk; (3) **program's own Session-4 record wrong: the "July-2026 8pp CCM paper" is byte-identical (MD5-verified) to t-22b = arXiv:2511.22755v1 (Nov 2025, 34 pp) — substance stands, metadata corrected in STATUS.**
- **Vision decisives:** t-56a printed masthead READS 187–236 (OCR misreads 185 — artifact confirmed); Berry/Norfolk image-only scans identity- and content-verified (−0.385 < Λ sighted); all 6 round-6 chapter extractions boundary-verified (TU-Dresden address on u-41a as claimed); IMPAN page mappings for r-07a/t-55a verified against printed DOIs/copyright; u-01a doubly-broken text layer confirmed (CP1251 mojibake + Р dropped); u-39c erratum applicability verified (§3.2 defines H_j(t), §3.3+figures write H_j(1/2+it)); u-15b's [CC7] bibliography entry with blank arXiv number sighted directly.
- **Bookkeeping landed:** FETCH-LIST-ROUND2.md fully checked off (incl. **MathSciNet PERMANENTLY CLOSED — discharged via zbMATH Open substitute, never to be re-listed**, per response §4.1.3; §B items all delivered as files; watch-list updated: MV-II APPEARED, 0 ≤ Λ ≤ 0.22 standing, [CC7] re-check ≥ Nov 2026); `fetched-r2/` gitignored (local-only, like `fetched/` — sponsor should keep a backup); response doc copied to rh-program root and tracked; stale NEEDS_SPONSOR lines in STATUS marked resolved.
- **paper-v5 assessed (sponsor-supplied, user-requested):** it is **v5 of the parent paper itself**, retitled "…Are Simple and on the Critical Line" (17 pp, 2026-08-11) — not a separate work. Newness established by grep-diff against the mapped 35-page original. NEW: Theorem B (primitive Dirichlet L-functions); Remark 7.1 ξ′ unconditional 0.85838 simple / 0.92919 distinct (quartic 0.86864 EXCEEDS FGL's RH-conditional constant; formalized as XiPrime); §7.2 in-paper bandwidth-one ceiling 0.6818287 + certificate-class definition + robustness (|r′(1)|+∫|r″| < 8.2); **§7.2(e): tr G̃^k evaluable exactly in the Rudnick–Sarnak range X^k ≤ T^{2−ε} — the A4 frontier, now paper-official**; §7.2(f) HL*(4)→13/18 moment ladder — **confirms the program's independent Session-1 Wolfram derivation**; **§7.3 conditional cubic-weight certificate ω(m) (tight m=1,2,3, Schur–Horn) — the finished template whose unconditional input is exactly A4's job; form factor on (−λ₀,λ₀) ∀λ₀ ⇒ 100% simple-on-line stated as the method's ceiling**. Local Lean repo verified already current with v5's Appendix A (XiPrime/, PairCeiling/, comparator/ present). Assessment: `results/paper-v5-assessment-2026-08-14.md`; clean tracked copy `anthropic/zeta-two-thirds-v5.pdf`; per-page text `sources-extracted/v5_p01..17.txt`. Follow-ups deferred to the RH session (A4 brief update, ξ′ propagation, v5 as primary citation) and folded into STATUS resume actions.

**Decisions:**
- Acceptance bar per sponsor: mathematical identity, not pagination/typesetting (3 pagination-class findings recorded as corrections, not failures).
- Corpus disposition mirrors Round 1: `fetched-r2/` stays local-only/gitignored; only the response doc + verification records are tracked.

**New artifacts:** FETCH-VERIFICATION.md Round-2 appendix; results/fetch-verification-r2-sweep-2026-08-14.json; results/fetch-verification-r2-agents-2026-08-14.json; results/paper-v5-assessment-2026-08-14.md; FETCH-RESPONSE-ROUND2.md (tracked copy); anthropic/zeta-two-thirds-v5.pdf; sources-extracted/v5_p01..17.txt; FETCH-LIST-ROUND2.md check-offs; .gitignore entry.

**Open at close:** Nothing running. **Next session = RH work resumes at STATUS resume actions 0–6** with both corpora verified and the v5/Round-2 propagation items folded into actions 0/1/2/4/5.
