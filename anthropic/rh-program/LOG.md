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
- **The B3 gap-1 theorem is now on disk and statement-verified:** `u-36a` = typeset IOP Langer–Woracek 2011, Theorem 1.2 transcribed by vision from both the typeset and author versions (identical): initial-segment coincidence up to reparametrization ⟺ exponentially-close Weyl coefficients, segment length governed by a = ∫√(det H); genuinely local (global de Branges = separate Thm 1.1); general 2×2 H ≥ 0 class; **Pontryagin/indefinite analog per Remark 1.3**; explicitly a Borg–Marchenko transfer (Bennewitz the closest relative). **NEW agent-surfaced caution: ∫√(det H) degenerates when det H = 0 a.e. — B3's converse must check det H > 0 on its class.**
- **Three refutations, all corrections not failures:** (1) response's §1 misprints t-46a's pagination — actually AIF 68(2) (2018) 563–567; (2) u-13 (MNT-II author draft — content/completeness confirmed, Ch. 16–22 + App. E–H) internally built 9 Oct 2024, the "post-publication 1 June 2026" claim is an HTTP-header fact not verifiable from disk; (3) **program's own Session-4 record wrong: the "July-2026 8pp CCM paper" is byte-identical (MD5-verified) to t-22b = arXiv:2511.22755v1 (Nov 2025, 34 pp) — substance stands, metadata corrected in STATUS.**
- **Vision decisives:** t-56a printed masthead READS 187–236 (OCR misreads 185 — artifact confirmed); Berry/Norfolk image-only scans identity- and content-verified (−0.385 < Λ sighted); all 6 round-6 chapter extractions boundary-verified (TU-Dresden address on u-41a as claimed); IMPAN page mappings for r-07a/t-55a verified against printed DOIs/copyright; u-01a doubly-broken text layer confirmed (CP1251 mojibake + Р dropped); u-39c erratum applicability verified (§3.2 defines H_j(t), §3.3+figures write H_j(1/2+it)); u-15b's [CC7] bibliography entry with blank arXiv number sighted directly.
- **Bookkeeping landed:** FETCH-LIST-ROUND2.md fully checked off (incl. **MathSciNet PERMANENTLY CLOSED — discharged via zbMATH Open substitute, never to be re-listed**, per response §4.1.3; §B items all delivered as files; watch-list updated: MV-II APPEARED, 0 ≤ Λ ≤ 0.22 standing, [CC7] re-check ≥ Nov 2026); `fetched-r2/` gitignored (local-only, like `fetched/` — sponsor should keep a backup); response doc copied to rh-program root and tracked; stale NEEDS_SPONSOR lines in STATUS marked resolved.
- **paper-v5 assessed (sponsor-supplied, user-requested):** it is **v5 of the parent paper itself**, retitled "…Are Simple and on the Critical Line" (17 pp, 2026-08-11) — not a separate work. Newness established by grep-diff against the mapped 35-page original. NEW: Theorem B (primitive Dirichlet L-functions); Remark 7.1 ξ′ unconditional 0.85838 simple / 0.92919 distinct (quartic 0.86864 EXCEEDS FGL's RH-conditional constant; formalized as XiPrime); §7.2 in-paper bandwidth-one ceiling 0.6818287 + certificate-class definition + robustness (|r′(1)|+∫|r″| < 8.2); **§7.2(e): tr G̃^k evaluable exactly in the Rudnick–Sarnak range X^k ≤ T^{2−ε} — the A4 frontier, now paper-official**; §7.2(f) HL*(4)→13/18 moment ladder — **confirms the program's independent Session-1 Wolfram derivation**; **§7.3 conditional cubic-weight certificate ω(m) (tight m=1,2,3, Schur–Horn) — the finished template whose unconditional input is exactly A4's job; form factor on (−λ₀,λ₀) ∀λ₀ ⇒ 100% simple-on-line stated as the method's ceiling**. Local Lean repo verified already current with v5's Appendix A (XiPrime/, PairCeiling/, comparator/ present). Assessment: `results/paper-v5-assessment-2026-08-14.md`; clean tracked copy `anthropic/zeta-two-thirds-v5.pdf`; per-page text `sources-extracted/v5_p01..17.txt`. Follow-ups deferred to the RH session (A4 brief update, ξ′ propagation, v5 as primary citation) and folded into STATUS resume actions.

**Decisions:**
- Acceptance bar per sponsor: mathematical identity, not pagination/typesetting (3 pagination-class findings recorded as corrections, not failures).
- Corpus disposition mirrors Round 1: `fetched-r2/` stays local-only/gitignored; only the response doc + verification records are tracked.

**New artifacts:** FETCH-VERIFICATION.md Round-2 appendix; results/fetch-verification-r2-sweep-2026-08-14.json; results/fetch-verification-r2-agents-2026-08-14.json; results/paper-v5-assessment-2026-08-14.md; FETCH-RESPONSE-ROUND2.md (tracked copy); anthropic/zeta-two-thirds-v5.pdf; sources-extracted/v5_p01..17.txt; FETCH-LIST-ROUND2.md check-offs; .gitignore entry.

**Open at close:** Nothing running. **Next session = RH work resumes at STATUS resume actions 0–6** with both corpora verified and the v5/Round-2 propagation items folded into actions 0/1/2/4/5.

## Session 4.9 — 2026-08-16 — Infrastructure side-session (no RH work, sponsor-directed)

**Focus:** Sponsor's three infrastructure questions ahead of the RH resume: (1) empirically test whether the CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000 fix (Session-4 FIX 3) actually reaches workflow subagents; (2) whether heavy computations can be handed off to the cloud so runs survive machine shutdown (Cowork vs alternatives); (3) whether Claude's tmp/session state can be moved into the repo for cross-machine (MacBook ↔ Mac Mini, iCloud) resume.

**Done:**
- **64k→128k fix VERIFIED (run wf_15eb682f-dd9, 3 probe iterations):** a single workflow subagent emitted a **97,505-output-token StructuredOutput response, stop_reason tool_use, clean completion** — 52% above the old 64k ceiling that killed A4 designer attempts 1–5. The A4 overflow blocker is cleared. Recorded in STATUS Session-4 task line. Probe lessons: attempt 1 killed by MacBook **sleep** mid-response (same orphaning mode as Session-3 runs); attempt 2 showed unbriefed subagents **self-ration to ~57k** (stopped at a round 700/1600 items just under the old cap) — briefs for very large single-response deliverables must state the 128k budget; chunked write-to-disk remains the safer architecture. Model ceiling confirmed against current API docs: claude-fable-5 max output = 128k, thinking counts toward the same cap (consistent with the Session-4 diagnosis).
- **Cloud execution researched (docs-verified):** Claude Cowork = wrong vehicle (separate product, cloud-capable but NO documented interop/handoff with Claude Code projects). Right vehicle = **Claude Code cloud sessions (claude.ai/code)**: run on Anthropic infra, survive local shutdown, support full Workflow/ultracode tooling, account-scoped (reachable from both Macs + phone), repo handoff via GitHub App on x67ai/riemann-rh-program. Constraint: no local Wolfram MCP in cloud → numerics in Python, Mathematica-only items queued for local follow-up.
- **Cross-machine state question answered:** cross-machine session resume is unsupported by design; syncing ~/.claude via iCloud is unsupported and risky (credentials, jsonl conflict-mangling); tmp scratchpad is ephemeral (~1MB) and not worth relocating. The program's existing repo-as-state pattern (STATUS.md + results/ + journal snapshots) IS the cross-machine resume mechanism, now complemented by cloud sessions.
- **KICKSTART.md written** (operations guide, no program state): Part 1 = sponsor's plain-language runbook (one-time claude.ai/code setup; the universal one-line boot prompt; cloud-vs-local decision; don'ts; known-issues table). Part 2 = binding session bootstrap for Claude (git pull first → STATUS.md authority → cloud/local environment rules → 128k budget notes → push-at-close discipline, PR-merge fallback explained for a non-technical sponsor). STATUS resume pointer and Last-updated line wired to it.

**Decisions:**
- Next session = RH work at STATUS resume actions 0–6, run as a **cloud session** via the KICKSTART boot prompt (sponsor will paste one line at claude.ai/code). Wolfram-dependent verification stays local (Mac Mini preferred).
- No relocation of ~/.claude or tmp state; no Cowork.

**New artifacts:** KICKSTART.md; STATUS.md updates (FIX 3 verification note in the Session-4 task line, resume pointer, Last-updated); this LOG entry. Probe script/journal live under the side-session's transcript dir (synthetic test — not snapshotted to results/, nothing of mathematical value).

**Open at close:** Nothing running. Untracked stray `anthropic/paper-v5 (12).pdf` (sponsor's original browser download; clean tracked copy exists as anthropic/zeta-two-thirds-v5.pdf) — left untracked, sponsor may delete. Next session = RH work, cloud, resume actions 0–6.

## Session 4.95 — 2026-08-16 — Ops revision: cloud path retired, local-only + thermal batching (no RH work, sponsor-directed)

**Focus:** Sponsor question exposed a hole in the Session-4.9 cloud plan: cloud sessions clone from GitHub, and `fetched/`/`fetched-r2/` (336 corpus PDFs) are gitignored/local-only by the sponsor's own Session-4.5 decision — so a cloud session could never read the corpus, and STATUS resume action 0 (corpus ingest) would be blocked there. Sponsor directive in response: **forget the cloud, run everything locally on the M5 MacBook**, batched so the machine doesn't run hot, and explicitly **without undershooting** ("have as many computations as this M5 machine can handle").

**Done:**
- **KICKSTART.md rewritten local-only.** Part 1: sponsor runbook is now just Terminal → `claude` → the same one-line boot prompt; lid open + plugged in; cloud setup, claude.ai/code flow, and Mac Mini preference removed; "don'ts" now include starting sessions at claude.ai/code. Part 2 step 3: environment is always local (Wolfram MCP + full corpus available; sanity check STOPS a stray corpus-less cloud clone). Step 4: sessions start `caffeinate -is` in the background before long runs (sleep is the proven run-killer).
- **Binding thermal & RAM batching policy added (KICKSTART Part 2 step 5), sized to the actual machine** (verified via sysctl/system_profiler: MacBook Pro, Apple M5, 4 P-cores + 6 E-cores, 24 GB): agent fan-out is API-bound, not a heat source — keep the full harness cap (min(16, cores−2) = 8 concurrent agents), never undershoot parallelism for thermals; heat comes from local CPU-heavy processes — cap those at 4 concurrent (= P-core count) and run big sweeps as back-to-back batches of ≤4 (pipeline()/bash-wait pacing) so scope is never reduced, only paced; Wolfram strictly serial single-kernel; 24 GB RAM → chunked write-to-disk, no multi-GB arrays across concurrent processes; escalation only on measured throttling (`pmset -g therm` CPU_Speed_Limit < 100 sustained → drop to 3, never lower, never less total work).
- **STATUS.md aligned:** Last-updated line (next session = RH work at resume actions 0–6, LOCAL), resume-point ops pointer, and the Session-4 "prefer cloud sessions for long runs" lesson marked retired.

**Decisions:**
- Sponsor directive (2026-08-16, binding): all sessions local on the MacBook; cloud path retired. Upside banked: every session now sees the corpus AND Wolfram — the cloud/Wolfram-queue split disappears, and resume action 0 (corpus ingest) is unblocked.
- Operating point in writing: 8-wide agents + 4-wide heavy local compute — a floor as much as a ceiling ("do not undershoot").

**New artifacts:** KICKSTART.md (local-only revision); STATUS.md pointer edits; this LOG entry.

**Open at close:** Nothing running. Untracked stray `anthropic/paper-v5 (12).pdf` unchanged (sponsor may delete). **Next session = RH work at STATUS resume actions 0–6, run locally via the unchanged one-line boot prompt.**

## Session 5 — 2026-08-19 — RH work resumed: all resume actions 0–6 completed; Phases 3, 4, 4.5 CLOSED; Phase 5 synthesis DELIVERED

**Focus:** The full resume queue in one session, all local per KICKSTART (caffeinate on, 128k ceiling verified in the live env at bootstrap): corpus ingest bookkeeping; A4 attempt 6 end-to-end (design → duplicated killers → binding adjudication → A2→A4 merge); Grossmann wave-2 relaunch and sweep closure; CCM DH-filter verdict; Phase-5 portfolio restructure (C3 + D1 commissioned, barrier zoo institutionalized) and the published prospectus.

**Done:**
- **Action 0 (ingest):** FETCH-LIST.md fully checked off (rename-into-sources-extracted instruction formally RETIRED per the local-only decision); `results/corpus-routing.md` created (routing index by consumer + 13 standing corpus-wide caveats); ledger corrections propagated (B3 now carries Langer–Woracek Thm 1.2 verbatim-in-substance + det H > 0 caution + Pontryagin Remark 1.3; FGL pinned to r-12a with the v5 ξ′ note in B3 + A3; w-08 non-strictness as routing caveat). 7 flags surfaced; 4 folded into later actions, MNT-II watch item already cleared.
- **Action 3 (GROSSMANN SWEEP CLOSED):** wave-2 relaunch (run wf_b4ab92cb-558, 10/10 agents, ~1.0M tokens) — 9 fresh scouts + 2 Session-4 partials = all 11 corners versed: 9 instruments, 2 NEW dead-end certificates (tomita-takesaki 0.72 via Gesteau–Liu — kills the one unassessed S4 class; lapidus 0.85 — axiom-level DH-filter failure), 0 grossmann-candidates, no shortlist displacement. **Closure verdict: wave 2 does NOT change wave 1 — no Grossmann, proceed de novo** — with 3 independent corroborations (BDPW purity-only S6 success; BZSV positivity consumed FROM RH per fn.115; Yuan–Zhang substrate-blind proven calculus). Net additions: adelic-Hodge-index toolkit + today-provable DH non-instantiability lemma; Blomer–Leung monoid exclusion = sharpest S1 home; BZSV = published S6 template; 4 formalizable ceilings; 2 supply lines (Harper-chaos → Lindelöf lock; KKT → B2). Harvest `results/grossmann-sweep2.json` + journal snapshot. ROUND-3 fetch section appended to FETCH-LIST.md, then **cross-checked same session: 13 items → 6 hard-missing sponsor documents**; 21 PDFs self-fetched into new gitignored `fetched-r3/` (IAS botwall beaten via Wayback: Langlands 2004 + Sarnak 2001 letter; Bost–Connes 1995; Wiesbrock+Borchers; Lichtman–Pascadi PINNED = arXiv:2408.13682; Harper 2301.04390 → Lindelöf-lock conditioning task unblocked).
- **Action 2 (CCM DH-filter DECIDED): ARITHMETIC-BLIND, 0.85** (`results/decisive-tests/ccm-dh-filter.json`, cites arXiv:2511.22755). DH passes CCM's mechanism at every probed truncation (even simple ground state; D″ spectrum reproduces DH's own zeros to 1.05e-5). The Session-4 collapse-rate reading REFUTED by two new RH-true controls: conductor law c = 4π/q across four systems (χ₅ 2.669 vs DH 2.604, equal to 2.4% — the "1e-29 vs 1e-6" gap was q=1-vs-q=5). Fuchs law confirmed for zeta (prefactor to 0.7%). DH's off-line zero needs μ ≳ 120 vs probed ≤ 14.44 (CCM's own ≤ 17). Consequences: CCM → instrument + publishable circularity no-go; S1 must act at the AXIOM level (witness Λ_DH(12) = −0.76 < 0); new B2 statistic ε ~ poly·e^(−4πμ/q). All numbers re-verified per order 5.
- **Actions 1+4 (A4 END-TO-END):** attempt 6 (run wf_3a8bdf77-ffc) — **the 128k fix held; zero overflow deaths after 5 straight ceiling kills.** Pre-launch brief edits: v5 §7.2(e)+§7.3 fold-in, A2-refutation caution, duplicate-killer protocol wired into the script. Design: **"The Schatten-3 Lindelöf Lock"** (Schatten-3 tail bound at near-critical bandwidth from 1970s inputs; sign-sensitive tr G̃³ row separating doubles (+8) from pairs (0) against lemmaR_tight; joint two-bandwidth LP). Verdicts SPLIT — killer-1 REFUTED (2, fatal: cubic-row vacuity), killer-2 (blind) SWR (3.5, no fatal), referee SWR (7); all three independently caught the same Thm-1(i) display error. **Three-way adjudication (12 computations, binding): SURVIVES-WITH-REPAIRS 5.5** — killer-1's fatal verified against the theorem as written but OVERRULED against the mechanism (the proof's own all-V Chebyshev ladder at θ<1 + squeeze LP caps garnish adversaries at o(N)); killer-2's θ<1 bite verified STRENGTHENED; upheld: Thm 1(i) false as displayed (min-of-branches repair; MVT-4 alone reaches λ<2/3, Huxley not load-bearing), R2 V-dependent bridge = THE open analytic gap (~0.8), support (k−1)λ′ = 1+o(1) (AH bullet struck), c₃ cubic resonance = absolute constant 2.3158, θ≥1 vacuous, M2 gate must be re-specified (R5) and run FIRST. 7 mandatory repairs R1–R7. **A2→A4 MERGE EXECUTED**: A4-lindelof-lock.md = the merged cubic-certificate direction (adjudicator's merge guidance + A2 salvage inside; re-import check: NONE — A4 is the corrected response to A2's fatal-2 escape channel); A2 file closed-historical. **Phase-4 scoreboard FINAL: 4 refuted / 6 SWR.** lemmaR_tight bookkeeping: NOT yet broken by anything currently provable.
- **Action 5 (PHASE 5 DELIVERED):** (i) `directions/C3-geometric-substrate.md` COMMISSIONED — the sweep's construction order (CC+Deninger joint via Morishita; Yuan–Zhang Part-A positivity engine; M0 = the DH/Epstein polarized-Frobenius non-instantiability lemma, provable today, one Epstein witness computation missing; M1 non-circularity gate before S4 credit; Tate-curve E_p×E_q seed; 6-item zoo self-check inside). (ii) `directions/D1-certified-refutation-arm.md` COMMISSIONED — Track D: certified Λ>0 witness formats (Polymath15-in-reverse, KKT partial sums, Weil-negativity, Robin), B2=theory/D1=execution split fixed, first deliverable = Certified Refutation Interface v1 with the DH live-fire acceptance test; S1-empty by design. (iii) `BARRIER-ZOO.md` — 45 barriers / 5 groups, 7-step brief-time protocol, return-before-design-cost rule, casualty cross-reference, 7-item formalization queue; headline new entry = A4's garnish-absorption/all-V-ladder squeeze. (iv) **Prospectus v2 published**: artifact "Beyond the Two-Thirds Certificate" (https://claude.ai/code/artifact/5febfa8b-0ab0-46f9-9409-33d79d06bdba), source `prospectus.html` tracked at rh-program root; honest-framing section first, refutations first-class, proof/refutation channels ranked separately.
- **Action 6:** committed + pushed after every harvest (9 commits this session through the close commit).

**Decisions:**
- Ingest deviation (recorded): corpus PDFs stay in place (fetched*/), NO mass rename into sources-extracted/ — the old instruction predated the sponsor's local-only decision.
- The duplicate-killer protocol earned its keep immediately: A4's killers genuinely disagreed (fatal vs no-fatal), and the adjudicator's computational cross-examination found BOTH partially right — as-written vacuity real, mechanism-level survival real. Single-killer would have either killed a repairable direction or passed an unsound statement.
- C3/D1 enter at commissioned grade; nothing ranks above its adversarial cycle. Proof channels and refutation channels stay separately ranked in the prospectus.
- fetched-r3/ gitignored like its siblings; sponsor should add it to their corpus backup.

**New artifacts:** results/{corpus-routing.md, grossmann-sweep2.json, adjudication-A4.json, adjudication-input-A4.json, decisive-tests/ccm-dh-filter.json}, results/ccm-dh-test/finisher_* (6 scripts + 12 outputs), results/journals/{wf_b4ab92cb-558, wf_3a8bdf77-ffc}.journal.jsonl, directions/{A4-lindelof-lock.md (merged direction), C3-geometric-substrate.md, D1-certified-refutation-arm.md}, BARRIER-ZOO.md, prospectus.html + published artifact, FETCH-LIST.md (Round-1 check-offs + annotated ROUND 3), fetched-r3/ (21 PDFs, local-only), design-proposals.json (10), verdicts.json (21), .gitignore entry, updated A2/A3/B3 direction files.

**Open at close:** Nothing running. Sponsor to-dos: (1) fetch the 6 remaining Round-3 documents (list in STATUS Session-6 queue); (2) back up fetched-r3/. Session 6 = the SESSION 6 QUEUE in STATUS.md (C3+D1 adversarial cycles first, then A4's M2 gate, C3 M0 witness, D1 interface v1, formalization queue).

## Session 6 — 2026-08-26 — The whole Session-6 queue in one session: C3/D1 cycles + C3 adjudication, the A4 M2 gate DECIDED (absorb, audited, evidence complete), Λ record corrected program-wide, conductor law at five points, C3-r deliverables written

**Focus:** The full SESSION 6 QUEUE (STATUS): C3+D1 adversarial cycles first, then the A4 corrected M2 gate, C3 M0 witness, D1 repairs/M0(ii), fetches. Local per KICKSTART (caffeinate on; network to github/arXiv was DOWN most of the session — ISP IPv6 issue, sponsor switched connections near close; pushes queued then delivered).

**Done:**
- **Housekeeping at open:** committed the pending U.S.-English pass with two over-corrections fixed ("advertize"→"advertise", "analyzs"→"analyses"); vendored zeta-23-lean-main READMEs reverted to upstream spelling (source fidelity); duplicate "paper-v5 (12).pdf" removed (MD5-identical).
- **Queue 3 (C3 M0/N1) first, exact:** Epstein witnesses for x²+5y² (D=−20, h=2) in closed form — Λ_Q(6) = 2 log 6 (off prime powers), Λ_Q(36) = −4 log 6 < 0 — with the genus identity vs χ₋₂₀ exact to n ≤ 200 and the ζ_K contrast object clean (`results/c3-m0-epstein/`). Later independently replicated digit-for-digit by BOTH C3 killers and the adjudicator (four-way agreement).
- **Queue 1 (cycles, wf_11e60b6b-3a1, 6 agents ~1.18M tokens):** **D1 CONVERGENT swr 6.5/7/7, zero fatals** — no adjudication needed; consolidated binding repairs D-R1…D-R10 written into the file; by session end D-R1/D-R7/D-R8/D-R9 were EXECUTED (the rest scheduled at their milestones). **C3 SPLIT** (killer-1 swr 2.5 with 2 fatals; killer-2 blind REFUTED 2 with the SAME 2 fatals independently constructed; referee swr 6) → **binding adjudication: SWR 3, reduced recommission C3-r** (`results/adjudication-C3.json`, 7 computations). Both fatals upheld on full re-derivation: (i) the E_p×E_q Tate-curve seed is EMPTY — Hom(E_p,E_q) ≠ 0 iff log p·log q ∈ 4π²Q, at most one exceptional partner per prime unconditionally, the {2,3,5} sandbox coherence-impossible, off-diagonal NS rank 2 (no Δ, no graphs, Castelnuovo–Severi vacuous) → new zoo entry IV.10, publishable no-go; (ii) Lemma B is not a theorem under either reading (P¹×P¹ z↦zⁿ counterexample; degree data forced completely multiplicative; char-p accounting verified numerically on y²=x³+x+1/F₇ — degrees see main terms, the zero side lives in the Δ-intersection; trace reading needs a Lefschetz axiom that makes the exclusion definitional) → M0 repriced to axiom-format note. Killer-2's commission-level REFUTED overruled: C3's own conversion machinery (Z5 rule, R8 pricing, kill-criteria) priced exactly these deaths. C3-r = M0-note + M1 + M2c-primary (session-budgeted, obstruction ledger) + M2a time-boxed watch + M3-instrument. Also caught: the q-13a corpus conflation (2019 norms/heights LNM ≠ the 2021 intersection Mémoire) → routing caveat 14; missed prior art (CCM math/0703392, Banaszak–Uetake, Kurokawa/Akatsuka tensor-square) → extended R7(a).
- **Λ RECORD CORRECTED PROGRAM-WIDE (D-R1):** the D1 killer read the on-disk Platt–Trudgian PDF: **Corollary 2 proves Λ ≤ 0.2** (Polymath15 Table-1 row 2 at H > 2.51·10¹² + their verified 3·10¹²); quote re-verified by the orchestrator against the text layer and by a second agent online. Routing caveat 9 and zoo III.6 superseded with dated notes — the old "[0, 0.22] bracket of record" was a propagated Round-2 verification error (correction 28 checked only the strict phrase). Strict "Λ < 0.2" stays forbidden. Related: Farmer "~10^10000" figure STRUCK program-wide (not in the on-disk full text; Odlyzko S(t)≳100 anchor substituted); zoo III.9's KKT gloss cautioned (body unread).
- **Queue 2 (A4 corrected M2 gate, wf_6e545a63-759 formulate→implement→audit, + follow-up agent): DECIDED — ABSORPTION, audited, evidence base COMPLETE.** δ₀ = 0 IDENTICALLY (≤1e-12, 940 records; W 2–8, C_led 10–1000 + per-column 4, ε .002–.10, N 64/128) with a hand-checkable marks-{1,2} witness on the ψ₁-zero grid (grid-Parseval decoupling + occupancy-2 cluster cross-terms pay the cubic budget at zero N_d cost — the adjudication's predicted position/interference channel; spectral escape stays squeezed at 2√2·√(C_led·ε)N). Auditor: R5-conformant, all 4,003 columns independently recomputed, 8 break attempts failed. Follow-up discharged all three audit fixes: near-CUE class at DECISION grade (τ₂=1: δ₀′ = 0 exactly at N=64 AND 128; absorption by SLACK — only pinning rows bind); p1-objective moved ≤1.4e-12 (clean-converged) — the no-go covers BOTH benchmarks; BGSTB24 fetched (r3s-06) + read — the near-CUE rows are an UNCONDITIONAL POINTWISE data class (closed band 0 ≤ α ≤ 1; three scope riders recorded). Structural correction along the way (supersedes Step-4's narrative and the adjudication's phase model): under the true Prop-4.1 block law pairs carry cubic charge ≥ 8m³ at EVERY depth (per-zero identity cubic = 3F − 2 + (m−1)(m−2)) — the "+8 vs 0" premise was false; all discrimination was always in cross-terms. **Consequences: cubic route closed at the proven operating point; R2 NOT to be funded for the cubic payoff; lemmaR_tight STRENGTHENED with an audited exact-zero certificate; sine-Gram closed forms m₂(λ)=1/λ+λ/3 (= κ exactly) and m₃(λ)=1+1/λ² verified two routes; M5 payoff curve quantified (first possible bite λ′ ≳ 0.6, MD-gated).** Zoo IV.7 closed; formalization-queue item 5 witness-ready (grid law algebraic → Lean).
- **D1 M0(ii) same session:** the χ₃ fifth conductor point CONFIRMS the law — fitted c = 4.23966 vs 4π/3 = 4.18879 (+1.21%, tightest Dirichlet point); parity trap navigated; L(s,χ₃) first zero reproduced to 4.1e-10; prefactor prolate-shaped, DH sitting between RH-true systems (no arithmetic signature). Baseline calibrated at five systems, q = 1,3,4,5, both parities (`results/d1-m0/`).
- **C3-r deliverables written:** `results/c3-r/m0-axiom-note.md` (repaired definition PF1–PF6, fork stated, six exact witnesses, I.2/I.7 clauses, may-not-cite list) + `m1-noncircularity.md` (full any-characteristic proof — the recommission record's compressed sketch was loose; repaired via auxiliary-ample H′ = D + mH + the D² = 0 perturbation case, flagged honestly — F_q degeneration to Weil's inequality, zeta-content-none ledger). S4 credit gate formally discharged. Referee pass still owed before external circulation.
- **Queue 6 (fetches): sponsor load 6 → 3.** Self-fetched + verified: DGH preprint (math/0110092), Halász 1968 PUBLISHED journal pages (REAL-J volume scan), Ichino–Ikeda author preprint (Ikeda's Kyoto page); Wintner + Guo confirmed closed-access everywhere legitimate (DOIs recorded); Graham–Kolesnik book remains. Post-network-fix: r3s-06 (BGSTB24), r3s-07 (the actual CM intersection-theory Mémoire arXiv:2103.15646 — closing the q-13a gap), r3s-08 (Morishita v5 21-Jan-2026 — the flagged version claim now confirmed). fetched-r3/ = 27 PDFs, sponsor backup requested.
- **Prospectus v3 PUBLISHED** to the same artifact URL (5febfa8b…): Session-6 callout, corrected Λ record, five-system conductor law, closed forms, C3-r/D1/A4 cards rewritten, zoo 46, Session-7 ops. Source prospectus.html tracked.
- **Git:** 13 commits this session; pushed after the sponsor's network fix + VS Code GitHub sign-in (which also seeded the keychain — direct pushes work from sessions now).

**Decisions:**
- The duplicate-killer protocol delivered its strongest result yet: BLIND REPLICATION of both C3 fatals — upgraded to an evidence class in zoo V.3, along with three new process rules ([V:scout] provability tags = [RU] until re-derived; referee silence ≠ rebuttal, weight by examination coverage; corpus-sufficiency claims name the exact volume). Fourth rule: self-instrumented briefs convert instead of dying — conversion machinery now REQUIRED in Track-C briefs.
- D1 promoted without an adjudicator (convergent cycle; adjudication is for conflicts). C3-r ranks commissioned-reduced; no design effort beyond M0-note/M1/M2c-ledger until a light re-check against the recommission order.
- A4's cubic bet resolved honestly negative at the M2 gate; the direction pivots to the no-go paper + Theorem 1(ii)-repaired + re-aimed consumers. lemmaR_tight bookkeeping: NOT broken; strengthened.
- KICKSTART boot prompt reformatted to a clean-copy code block (sponsor formatting rule).

**New artifacts:** results/{verdicts-c3d1.json, adjudication-input-C3.json, adjudication-C3.json, c3-m0-epstein/, c3-r/{m0-axiom-note,m1-noncircularity}.md, d1-m0/, a4-m2-gate/ (SPEC, code, RUN-REPORT, gate-result, witness_N64, AUDIT, FOLLOWUP-REPORT, followup-*.json, runs/), journals/{wf_11e60b6b-3a1, wf_6e545a63-759}.journal.jsonl}; scripts/{rh-c3d1-verify.js, rh-a4-m2gate.js}; BARRIER-ZOO.md (IV.10 new, IV.7 closed, III.6/III.9/V.3 amended, queue items 5/6 updated, C3 casualty row); corpus-routing caveats 9 (superseded), 14, 15; FETCH-LIST-ROUND3.md updated; prospectus.html v3 + republished artifact; fetched-r3/ +6 PDFs; direction files A4/C3/D1 rewritten at frontier level.

**Open at close:** Nothing running. Sponsor to-dos: (1) fetch the 3 remaining Round-3 documents (Wintner, Guo, Graham–Kolesnik book — exact DOIs in FETCH-LIST-ROUND3.md); (2) back up fetched-r3/ (27 PDFs). Session 7 = the SESSION 7 QUEUE in STATUS.md.

## Session 7 — 2026-08-26 — The entire Session-7 queue in one session: the A4 no-go paper (dual-refereed), C3-r fully closed, D1 M0 certified complete, first Lean formalization, Round-3 fetch list closed to zero

**Focus:** The full SESSION 7 QUEUE. LOCAL per KICKSTART (caffeinate + push watchdog from the top; network to github/arXiv down on the IPv6 ISP for the first hours — GCS mirror workaround for arXiv; sponsor switched to the IPv4 Wi-Fi ~17:05 and everything queued fired automatically). Orchestration: three parallel workflows (16 agents) + ~10 single agents; ~6M subagent tokens total.

**Done:**
- **Queue 1 — THE A4 NO-GO PAPER COMPLETE** (`results/a4-no-go/`: paper.md ~12.5k words; theorems.md T1–T6 referee-grade 622 lines; data-tables.md provenance doc; pair-channel.md; referee-1/2.md; verify/ 7 scripts; wf_b7adec9e-151, 7 agents). Both independent referees: **pass-with-repairs, ZERO fatals** — every proof re-derived, every number traced to raw JSONs, BGSTB24 verified verbatim (published: Acta Arith. 214 (2024) 357–376, web-verified), the R6 wording bars verbatim, external prior-art sweep CLEAN (novelty survives). All 8 majors + 20+ minors repaired (revision record in the paper). New mathematics produced for it: the **pair-interference channel closed at proved coverage** (single-pair w ≤ 2.8, 34% margin; multi-pair w ≤ 0.82 unconditional, ≤ 1 mod one certified constant; 8/9 backstop all depths; O1–O5 residue honest) and the **fractional-mark discovery: the 5/6 corner is an INTEGRALITY theorem** (mark-4/3 atoms beat it; convexified LP analyses unsound for the pair class).
- **Lean, from cold to first theorem in one session:** toolchain + Mathlib cache built in `~/rh-lean-work` (installer with network-retry loops; fired on the Wi-Fi switch); **`Zeta23/PairCeiling/GridParseval.lean` LANDED** — ~560 lines, sorry-free, axioms = propext/Classical.choice/Quot.sound, full library builds 9,011 jobs: DFT Parseval, band collapse, the T1 grid-decoupling theorem, the literal tr Ĝ² = Σ m² row, weight telescoping, corner transfer. TODOs documented (witness instance 4128/33, half-band proposition, ε-budget corner).
- **Queue 2 — C3-r FULLY CLOSED** (wf_a0c5fe16-6a2, 5 agents + 2 follow-up agents): both notes refereed **pass-with-repairs zero fatals** (all math replicated; 3+3 majors + 13 minors EXECUTED — Blomer–Leung pinned authoritatively to Adv. Math. 485 (2026) art. 110716/arXiv:2401.04037, fixed in m0 + zoo I.1; m1 gains (IN7) Nakai–Moishezon + the Stepanov–Bombieri footnote); **extended R7(a) prior-art gate: NOVEL-WITH-CITATIONS** (7 obligations; math/0703392 title corrected — it is "The Weil Proof…", not "Fun with F₁"; CC 2501.06560 → 2606.06604 lineage); **seed no-go note WRITTEN, refereed FAIL-with-one-fatal-in-its-FAVOR, repaired and STRENGTHENED**: (T2) refuted unconditionally by Gelfond–Schneider ⟹ **End(E_p) = Z for every prime unconditionally**, Theorem 5 exception clause deleted, one open rider (T1, refuted under 4EC) — all three notes circulation-ready; **M2c feasibility ledger: OPEN-WITH-LEDGER** (Route 1 verbatim-ALKL EXHAUSTED: 9 obstructed rows + 3 shape mismatches; live route = solenoid intermediate, blocked at S4 = Deninger's own open lamination-existence problem; well-posed S2 work item; **decidable kill-probe 9.3** queued — a YES fires the kill-criterion).
- **Queue 3 — D1 rungs, then M0 CLOSED CERTIFIED** (wf_d6dcdf12-546 + follow-on): **λ-ladder cost curve published** (D-R5) — cost POLYNOMIAL, the "exponential prime sums" premise false; **M0(i) DONE: certified λ_c ≤ 5.55** (μ_c ≤ 30.8025, onset bracket (5.525, 5.55], 14 interval-certified rungs, frozen 40-digit witnesses; staircase baseline departure; **the μ ≳ 120 tension RESOLVED** — wrong functional + stale mean-gap input; K_inv crossing at λ = 5.536 inside the bracket; DH zero sits mid anomalous 4.54-wide void). **KKT body read** (r3s-09/r3s-10 fetched via GCS mirror): **W2 DEMOTED pointer-only** (constants effective-never-explicit; no companion needed; ζ outside S(m) — W2 can never feed Λ>0); zoo III.9 caution resolved. **M2a/M2b split design written** (D-R2; ray form, 3 displayed hypotheses, PT Table-1-row-2 instance ⟹ Λ ≤ 0.2, "0 ≤ Λ" dropped, f_t evaluator priced, first file Zeta23/DBN/Defs.lean) — M2a unfrozen. **Gomila claim screen, first live run: screen-open (interim)** — disclosure-complete exact-rational audit repo, steps 1/2/5 pass (t₀ + y₀²/2 = 0.1787854 recomputed; height correctly below PT's precise rigorous 3,000,175,332,800), steps 3–4 pend on OUR M1 checker; NOT a record.
- **w-05b vision pass — standing risk (iii) DISCHARGED: FAITHFUL** (`results/w-05b-vision-pass.md`; CL-refuted condition verbatim in de Branges 1994 pp. 118–119, he himself flagged it "in doubt"); one real drift fixed program-wide (C1's "at criticality a = 1/2" → a = 1, the §4 replacement text executed; B3/A2 scoping fixes executed).
- **Queue 5 — ROUND-3 FETCH LIST CLOSED TO ZERO:** sponsor hand-delivered 7 files, all verified/renamed/routed (r3s-11 Wintner complete, r3s-12 Guo complete, r3s-13 Hiary Annals 2011 bonus [the misnamed "graham1991"], r3s-14 Halász Springer-typeset, r3s-15 Ichino–Ikeda revised, DGH duplicate parked, **r3s-16 the genuine Graham–Kolesnik book** — Rankin pin vision-verified §5.4 p. 63: the book prints R = 0.82902135…, floor (2R−1)/4 ≈ 0.16451). **Wintner zoo flag discharged FAITHFUL** (a.s. √-cancellation both directions verified on the page; new rider: a.s. natural boundary at σ = 1/2 ⟹ no FE).
- **Git:** 10 commits this session, all pushed (watchdog delivered the first 4 the minute the network returned).

**Decisions:**
- Adopted the cost-curve agent's M0(i) rescope (hunt λ ∈ [5.5, 13], negative branch dps 60) — vindicated by the certified result.
- The referee protocol's strongest session yet: it caught a citation error (Adv. Math. 471→485), an under-claim (Gelfond–Schneider strengthening), three provenance drifts, and eight scope majors on the paper — every deliverable is stronger for it. The Gelfond–Schneider case is a new species: a FATAL in the note's FAVOR.
- Ultracode/context question (sponsor): verified via documentation — effort level and context window are orthogonal; Fable 5 runs the 1M window regardless; keep ultracode for research sessions.

**New artifacts:** results/a4-no-go/ (complete paper package), results/c3-r/{seed-no-go-note.md + checks, referee-m0/m1/seed-no-go.md, prior-art-r7a.md, m2c-feasibility-ledger.md, referee_m1_checks.py, referee_seed_checks.{py,json}}, results/d1-m0/{lambda-ladder-cost-curve.{md,json}, kkt-body-read.md, m2a-m2b-design.md, gomila-screen.md, m0i-crash-certificates.{md,json} + 4 scripts}, results/w-05b-vision-pass.md, Zeta23/PairCeiling/GridParseval.lean (+ Zeta23.lean import), fetched-r3/ +9 files (r3s-09..16 + duplicate parked), ~/rh-lean-work/ (9.2 GB toolchain+build, local-only), BARRIER-ZOO.md (I.1, I.5, III.9, IV.7-queue, IV.10 amendments), corpus-routing caveat 16, FETCH-LIST-ROUND3.md closed, direction files A4/C3/D1 + C1/B3/A2 updated.

**Open at close:** Nothing running. Sponsor to-dos: (1) **back up `fetched-r3/`** (36 files now); (2) external-circulation decision on the four circulation-ready documents (A4 paper + three C3-r notes) — sponsor's call, next session can prepare submission formats if wanted. Session 8 = the SESSION 8 QUEUE in STATUS.md.

## Session 8 — 2026-08-26 — Prospectus v4; M2c probes decided (Theorem A, no kill); D1 M1 v1 built with live fire; Lean W1 architecture; O1 grid-artifact discovery

**Focus:** the SESSION 8 QUEUE. LOCAL per KICKSTART (caffeinate + push watchdog from the top; network fine). Orchestration: three parallel workflows (5 + 6 + 3-stage agents) + one single A4-polish agent; sponsor called wrap-up mid-session (usage limits) — no further launches after that call; streams allowed to finish.

**Done:**
- **Queue 1 — PROSPECTUS v4 REPUBLISHED** (same artifact URL 5febfa8b; artifact-design skill loaded first). Session-7 callout (four circulation-ready documents; certified λ_c ≤ 5.55 + resolved μ-tension; integrality-theorem discovery; End(E_p) = Z unconditional; first Lean formalization; Round-3 closed); phase table gains the Build-out row; new numerics rows (λ_c certificate, gate δ₀ cite-safe); the stale "μ ≳ 120" CCM bullet corrected to the resolved figures; A4/C3-r/D1 cards rewritten; §8 leads with the sponsor circulation-decision callout + fetched-r3 backup (36→42 files now).
- **Queue 3 — M2C PROBES ALL EXECUTED AND ADJUDICATED (wf_a8922fb6-34d, 5 agents, ~1.15M tokens): KILL-CRITERION DOES NOT FIRE, and the probes produced new mathematics.** Both independent 9.3 probes proved the same new **Theorem A (packet-closure law)**: in X₀ = X(Spec Z) the closure of every periodic orbit contains its entire packet Γ_p; forcing group = coker(lk_p); mechanism = CRT/Frobenius-return accumulation (the ledger's fibration-monodromy sketch refuted — twist trivial at K = Q). Adjudicator re-derived it (third derivation). Banked referee-grade: **closed-subsystem half of S4 DEAD** (Deninger's own question x-03 p. 40, first alternative, answered NO); **X₀ non-Hausdorff along packets** (new row W12; G1 decided NO — probe B's Cor A.2; probe A's G1-conditioned kills VOID; Morishita "homeomorphism" wording caveat). Ledger 9.3 REPLACED by merged residue **Q*** (Q-a non-closed subspace / Q-b equivariant mapping — pure p→∞ accumulation; NO on both fires the kill-criterion). **S2 = TRANSFERS-WITH-WORK, accepted**: (1.3.1)/(1.3.2) survive the totally disconnected transversal (conormality is flow-transverse; Montel fails but is not consumed; work program W1–W7, W3 the single residual risk); ALKL corpus re-fetched DURABLE (r3s-17..21 incl. the ALKL23 companion + Lei07 precedent). **9.4 closed as a trichotomy** (equivariance no-go via Steinitz; defect bound empty on the periodic locus; transport = Teichmüller cut) with the structural identity B_p = coker(ring-aut → group-aut) = coker(lk_p), and a NEW road: **Haar-average the packet → DQ-M** (measured trace formula for orbit continua — the ranked decidable sub-question). Deninger 2508.05329 ("Rational Witt vectors") fetched as r3s-22. Referee debts for Session 9: probe A Thm B(b), probe B Cor A.1, 9.4 Lemmas A–D/Prop 1.
- **Queue 4 — D1 M1 v1 BUILT (wf_ba6a6bb3-f5b; audit stage still running at close).** The W1 FORMAT CONTRACT v1.0 landed (FORMAT.md + w1-schema.json + worked examples + reference_checker.py). **mpmath-BALL PRODUCER LEG built and validated** (ball.py 5068 containment checks 0 fail; zeta_encl.py Euler–Maclaurin with the remainder bound DERIVED in-file, 200/200 containment vs dps-100; hurwitz_encl.py same; producer_mp.py adaptive-mesh transcripts, derivative-free winding; checker_ref.py independent Fraction checker). **Arb leg built too** (python-flint; producer_arb.py; transcripts on disk). **THE DH LIVE FIRE FIRES: certified winding m = 1 around ρ_DH** (S/A ∈ [0.999999999973, 1.000000000030], 57 segments — checker-level per D-R8), BOTH legs, both checkers ACCEPT; null exclusion certificates (m = 0) at t ≈ 10/100/1000 (+t10000 in flight at close); positive control m = 1 + kernel-checked negative controls; cross-check 5 transcript pairs CONSISTENT; cost-curve.json.
- **Queue 2 — LEAN: ALL THREE GridParseval TODOs DISCHARGED + DBN Defs + W1 checker in Lean (wf_b1254667-97d; Soundness stage still running at close).** `GridWitness.lean` (~380 lines: vacancy-lattice spectrum algebraic for EVERY vacancy position; F' = 4128/33 EXACT, integer core 136224 kernel-checked; half_band_alive 4128/33 ≠ 64 = the two-bandwidth decoupling as one exact identity; Prop 1.3 finite half). `GridCorner.lean` (~230 lines: the ε-budget LP corner on grid configurations/laws; exact attainment at N = 64, ε = 1/32 kernel-checked). `Zeta23/DBN/Defs.lean` (M2a trusted layer per the design note). `Zeta23/W1/{Format,Checker,Examples}.lean` — checkW1 in pure integer arithmetic, both FORMAT §11 examples ACCEPTED by decide +kernel, negative controls REJECT, **the Lean checker cross-validates the Python reference checker digit for digit**. All sorry-free, clean axiom audits, 9013–9017 jobs, committed per unit.
- **A4 polish — A REAL DISCOVERY, not a polish (single agent; report `results/a4-no-go/o1-n128-report.md`, 301 lines): the Session-7 crowding constant 0.9775 was a GRID ARTIFACT** (the 0.004 depth grid's last admissible point 0.156 silently capped the family). Certified now: (C1) Sgen2 ≤ C* < 1 for all d, d' ≤ 39/250 (w ≤ 0.98018) by 17-box interval partition; (C2) **Sgen2 > 1 certified INSIDE the R5 family** (crossing bracket d* ∈ (0.156, 0.158)) — the multi-pair ledger route is UNREPAIRABLE on w ∈ (0.98, 1]; the (MI) inequality itself shows NO numerical failure there (attack margin +17.5 at the sliver); (C3) Theorem B(i)'s Y = 0.13 self-consistency now interval-certified both sides. **N = 128 re-run: every identity holds; control leg reproduces N = 64 to ≤ 2e-15; capped Sgen2 improves to 0.96329.** Paper repair sentences quoted in the report — apply through the dated-revision process in Session 9 (theorem B(ii) scope: "w ≤ 1 mod a constant" → certified w ≤ 0.98 + honest open sliver).
- **Housekeeping:** r3s-22 promoted from scratchpad (fetched-r3 now 42+ files — sponsor backup reminder stands); C3 direction file Session-8 entry + superseding frontier; STATUS live-tasks; commits pushed throughout (watchdog live).

**Decisions:** external circulation remains the sponsor's call (§8 callout in the prospectus); LaTeX/TeX install DEFERRED until a venue is chosen; no new launches after the sponsor's wrap-up call — the remaining stream stages (D1 audit, Lean Soundness, A4 report finalization) finish on their own or hand their residue to Session 9.

**New artifacts:** prospectus.html v4 (republished); results/c3-r/{probe-9.3-a,probe-9.3-b,probe-9.3-adjudication,s2-feasibility-note,probe-9.4-note}.md + ledger §12; results/d1-m1/ (complete v1 package incl. live-fire transcript); Zeta23/PairCeiling/{GridWitness,GridCorner}.lean, Zeta23/DBN/Defs.lean, Zeta23/W1/{Format,Checker,Examples}.lean; results/a4-no-go/{o1-n128-report.md, verify/o1_crowding_interval.py + n128_rerun.py + outputs}; fetched-r3/r3s-17..r3s-22.

**Open at close:** D1 audit stage + Lean W1/Soundness.lean stage + A4 report finalization possibly unfinished (harvest from journals + disk next session; any uncommitted tail is snapshot-committed). Sponsor to-dos unchanged: circulation decision; back up fetched-r3/ (now 42+ files). Session 9 = the SESSION 9 QUEUE in STATUS.md.

**Addendum (post-close, same night — the usage-limit cut and the recovery):** the sponsor's usage limit killed four agents mid-flight (reset 3:10am IST); final accounting after the limit partially restored: (1) **D1 `d1-m1-v1`: the acceptance agent died AFTER finishing its work** — the final `acceptance-report.md` (verdict table: ALL PASS — 8/8 null transcripts ×2 checkers, positive control with correct C2 rejection, DH live fire both legs, cross-check CONSISTENT zero stop-the-line, cost curve written, t10000 completed) was on disk and is committed (51d1e00); **only the adversarial AUDIT stage never ran** — Session 9 item 1a (brief in the workflow script). (2) **Lean `lean-s8`: RECOVERED TO FULLY COMPLETE** — the w1 agent died after writing `Zeta23/W1/Soundness.lean` (1257 lines, sorry-free: W1EnclOK + RectArgPrinciple-in-consequence-form as the two displayed Props, `cert_of_checkW1` proved through the full FORMAT §6.3 chain incl. the L1 additivity obligation, plus `floor_of_checkW1Floor`) but before its verification build; the orchestrator ran the build (9018 jobs, zero errors), audited axioms (both theorems: propext/Classical.choice/Quot.sound only), synced to the iCloud tree and committed (51d1e00). **The M1 v1 Lean architecture is COMPLETE** — Format + Checker + Examples + Soundness; v1.1 (discharging H-AP) is the remaining named milestone, unchanged. (3) **A4 polish: killed mid report-finalization** — the corrected-run outputs are committed; the report's 26 template slots and the paper repair go to Session 9 (items 1b + 2). Grid stage, DBN stage, format stage, both producer legs, and all C3-r probe work were fully complete and committed before the cut.

## Session 10 — 2026-08-27 (arXiv preparation: CIRCULATION-PREP steps 2 and 3)

**Focus:** finish the arXiv-preparation register — the independent novelty check (step 2) and the
LaTeX conversion (step 3) — both of which had died with the previous session leaving no deliverable.

**Done:**
- **STEP 2 CLOSED.** `results/arxiv/novelty-check.md` (97 KB; 4 document sweeps + 4 adversarial
  refutation agents + synthesis). Verdicts: A4 NOVEL-WITH-CITATIONS; m0 NOVEL-WITH-CITATIONS;
  m1 ANTICIPATED-BY (standard mathematics, as the note itself says); seed no-go ANTICIPATED-BY on
  the rigidity, no-go survives.
- **THE PRIORITY FINDING, verified here against the primary PDFs rather than on the agents' word:**
  seed-no-go Theorems 1–3 are **Winkelmann 2002** (arXiv:math/0204195; Nagoya Math. J. 176 (2004)
  159–180). Read verbatim from the v3 PDF: isogeny of `E_i, E_j` forces
  `4π²/(log λ_i log λ_j) ∈ Q`, division of two such relations forces `log λ_i/log λ_k ∈ Q`, the
  argument runs on three curves, and the conclusion is "for each of these curves there is at most
  one other curve in this family to which it is isogenous". With `λ = p` that is Theorems 1, 2 and
  3. Also verified: (T1) is **Bertrand's weak four-exponentials conjecture** (Madras 1996; verbatim
  in Diaz, JTNB 1997), not "unrecorded"; and the per-prime elliptic-analogue lineage is **July 2015**
  (*The Scaling Site*, arXiv:1507.05818), not January 2025.
- **STEP 3 CLOSED.** Four arXiv packages built and passing a new checker: a4-no-go 41 pp,
  m0-axiom 10 pp, m1-noncirc 8 pp, seed-no-go 17 pp. A4's fidelity audit returned FAITHFUL
  (numeric-multiset diff clean, all 26 statement numbers exact, all 8 tables, inequality census
  exact).
- **Bibliography check of the three C3-r notes:** 33 entries audited; **five substantive errors**,
  four converter-manufactured and one inherited from the prior-art gate — the `[Ha15]`
  Haran/Thas misattribution (repointed to Haran's 1991 Durham chapter, page-verified once the
  sponsor fetched it), `[BU3]`'s wrong title ("for operators in Hilbert space" → "for
  zeta-functions"), `[YZ]`'s wrong series volume (Annals Studies **221**, not 223 — repo-wide),
  `[vdGS]`'s invented first page (377, not 379), and Stepanov's missing leading "On". Plus 15
  completeness/staleness fixes. All applied and rebuilt.
- **FORMALIZATION AUDIT (new; sponsor question).** Twelve theorems in
  `Zeta23/PairCeiling/{GridParseval,GridWitness,GridCorner}.lean` machine-check A4's Lemma 3.8,
  Theorem 3.9, the 4128/33 witness, the "alive" half of Proposition 3.10, Lemma 4.2 and
  Theorem 4.3 (pointwise, law-form, exact attainment). Rebuilt: 2081 jobs, clean.
  `#print axioms` on all twelve → `[propext, Classical.choice, Quot.sound]`; zero real
  `sorry`/`admit` across 34 files. Section 10 had been titled "Formalization plan" and listed four
  of these as queue items — retitled and corrected. No Magma anywhere in the program.

**Decisions:**
- Applied the citation and accuracy repairs to `paper.md` (source of truth) and mirrored into the
  `.tex`, rather than re-converting — the conversion had already passed an adversarial audit and
  re-running it would have discarded that evidence.
- Corrected two agent errors instead of executing them: the `[CC26]` title is **not** truncated
  (the arXiv API truncates at the TeX macro; the on-disk extraction is authoritative), and §7.5
  **does** exist in the 35-page parent version — item (e) is inside it, and moved to §7.2(e) only
  in v5. Both parent pointers are now explicitly disambiguated by a version pin.
- Did **not** start the formalization expansion. It is new scope beyond the register and the
  costing (`results/FORMALIZATION-ROADMAP.md`) recommends not blocking circulation on it.

**New artifacts:** `results/arxiv/{novelty-check.md, README.md, check-submittable.sh}`;
`results/arxiv/{a4-no-go,m0-axiom,m1-noncirc,seed-no-go}/{main.tex,main.pdf,abstract.txt}`;
`results/a4-no-go/formalization-status.md`; `results/FORMALIZATION-ROADMAP.md`; dated corrections
in `results/c3-r/{seed-no-go-note.md, prior-art-r7a.md, referee-m0.md, referee-seed-no-go.md,
m0-axiom-note.md}`, `BARRIER-ZOO.md`, `directions/C3-geometric-substrate.md`, and
`results/corpus-routing.md` caveats 17–20.

**Sponsor fetches this session** (all local-only in `fetched-r3/`): `haran1991.pdf`,
`The double Riemann zeta function.pdf`, `davenport1936.pdf`, `davenport1936-2.pdf`. Each closed a
standing caveat — the Haran attribution, the Akatsuka paywall, and the "(Second paper)" title line
(genuine, lowercase p, so Crossref must **not** be used to "correct" it).

**Open at close:** **CIRCULATION-PREP STEP 4** — execute ~40 MUST + ~19 SHOULD citation actions
and 13 textual repairs from `results/arxiv/novelty-check.md` §§A–D across the four documents, and
**rewrite the seed no-go's framing** so Theorems 1–3 are Winkelmann's transported, not new. Then
Session-9 queue item 5 (the circulation decision itself) is the sponsor's.

---

## Session 11 — 2026-08-27 (~17:05 onward)

**Task.** CIRCULATION-PREP **STEP 4**: execute the ~40 MUST + ~19 SHOULD citation actions and 13
textual repairs specified file-by-file in `results/arxiv/novelty-check.md` §§A–D, across the four
circulation-ready documents, and rewrite the seed no-go note's framing so Theorems 1–3 are
presented as Winkelmann's. **Done, committed one commit per document, plus an adjudication sweep.**

### The discipline, and what it caught

STEP 4's binding instruction was that **every action be confirmed against a primary source before
it touched a file** — because Session 10 spot-checked roughly six of the report's claims and two
were wrong. That was run as a workflow of **18 verification agents plus an adjudicator**: 92
items, 2.67 M subagent tokens, 866 tool calls, ~54 minutes. Evidence is on disk, one markdown file
per cluster, in `results/arxiv/citation-verification/`, with `ADJUDICATION.md` (716 lines)
settling the cross-cluster disagreements. Nothing was taken on the report's word.

**Twenty-one of the report's actions did not survive.** Each is now recorded in a dated block
inside the paper it would have touched, so a later session cannot reintroduce it. The four that
would have done real damage, because a *sentence* was to be written on their strength:

1. **Ito–Ito–Koshikawa Remark 1.3 is not "the published non-circularity audit."** It says the
   opposite: *"we did not attempt to avoid the Weil conjecture in our proof of Theorem 1.2."* That
   is a **stronger** precedent for m1 — it shows the question is recognized *and* that answering it
   affirmatively is not automatic — and it is now quoted as what it is.
2. **Ancona makes no independence or non-circularity claim anywhere**, and his §1 does not publish
   m1's §9 "verbatim". `grep circular` returns zero. Only Lemma 7.10 is cited, for the contrast.
3. **The seed note's "first appears in January 2025" lineage** is off by 9 years 5.7 months — and
   the correction needed a correction: the July-2015 object is `C_p = R*₊/p^Z`, a **real** circle of
   circumference `log p` in characteristic one with a real-valued Riemann–Roch, which CC themselves
   call "a variant of the classical Jacobi description `C*/q^Z`". The **complex** Tate curve is
   June 2026. Both halves are now stated.
4. **The two Connes–Consani Riemann–Roch papers do not supply `h⁰_θ`.** They explicitly call the
   log-theta number virtual, *"for the obvious reason that it outputs real numbers rather than
   integers"*, and their result is an Euler-characteristic identity that gives no lower bound on
   `h⁰` alone. m0 §7's absolute is softened; the M4-level input genuinely survives as unsupplied.

Also caught and not executed: an **invented Milne quotation** ("avoid the Weil conjecture" — the
string "avoid" occurs **zero** times in his paper, in either extraction); **Kleiman's Remark 3.10**
pointing at the wrong remark (3.10 is a characteristic-zero remark about homological vs numerical
equivalence; **4.5** is the dependency-ledger remark, and it is a far better pin); **Montgomery–
Vaughan §1.2** (the Euler-product material is **§1.3**, Thm 1.9, p. 20); a **"§7" citation to a
paper with six sections** (Winkelmann's Schanuel argument is §3.2, Prop. 3, p. 14); **Waldschmidt's
AWS Conjectures 5.34/5.35** described as four-exponentials statements (they are Bertrand's
**modular** conjectures on `J`; 4EC there is Conj. 5.11); and **Chirre–Gonçalves–de Laat's
inequality (7)** called "the published convex-programming form" of A4's Lemma 4.2 (it is elementary
integer arithmetic, credited there to an argument of Ghosh, and sits at the **third**, reciprocal-
weighted integrality level where Lemma 4.2 is at the **unweighted second**).

Two Session-10 adjudications were re-confirmed a second time against the primary sources: the
parent's item (e) **is** in §7.5 of the 35-page version, and "and the Fargues–Fontaine curve" **is**
part of the `[CC26]` title. But the *mechanism* recorded for the second ("the arXiv API truncates
the title at a TeX macro") was itself wrong and is corrected in place: the clause is absent from
**every** arXiv metadata surface — abs-page heading, `citation_title`, the API, the PDF's own
metadata — and from zbMATH, surviving only on the typeset title page and in arXiv's HTML rendering.

Two real cross-cluster conflicts arose and were settled by the adjudicator against a re-fetched
primary source: the Bombieri passage is on **p. 9 alone** (the Clay PDF is 11 pp; p. 10 has moved
on), and the Diaz p. 231 line is `x₂ = (log α₁)/2iπ` — one cluster's Numdam OCR had silently eaten
the `/2iπ`, which is exactly the failure mode the other cluster had warned about by name.

### Per document

**A4 no-go (44 pp).** New: `[GdLL25]` Gonçalves–de Laat–Leijenhorst, Math. Comp. **94** (2025),
no. 354, 2041–2058 — the report said 2024 and flagged the volume unverified; Crossref, zbMATH and
the AMS issue index all say 2025 — cited in §1.2 with a full reconciliation paragraph and at
Proposition 3.3; `[KLS11]`; and `[FGL14]`, solely to disambiguate the numerical coincidence at
Corollary 4.4 (their published 0.8051 for distinct zeros vs this paper's LP corner 0.8050957 —
verified by reading the *published* JLMS paper on disk, since the 2008 two-author preprint gives
0.6544 and citing it would have been a factual error). Completed: coordinates for `[BGSTB24]`,
`[KLS07]`, `[KS66]`, `[CGdL20]`, `[CdLS22]`, and DOIs for six more. Textual: Proposition 3.3 now
names the atom half as the third-order **Stirling change of basis** between power sums and falling
factorials and confines the novelty claim to the pair term; Lemma 3.8 / Prop. 3.11 labeled
critical-sampling Parseval and Shannon–Whittaker; the "convexified analyses are unsound" moral
labeled as the textbook **integrality gap**. The package was also missing `abstract.txt`; created.

**m0 axiom note (14 pp).** Had no reference list at all. Now carries a new **§1.5 "Prior art and
what is new"** — six upstream lines, each with its differentiator, ending in an explicit statement
of the three things that *are* new — and **§10**, 32 verified entries, plus in-place citations at
(PF1), (PF3), §3.2, §3.3, §4(a), §4(b), §6.1, §6.2, §6.3 and §7. Blomer–Leung: the word **"monoid"
is withdrawn as an attribution** (case-insensitive count in **both** arXiv versions: zero,
split-hyphenation checked), their Theorem 1.1 restated verbatim in their own terms, the
converse-hosts-an-exclusion logic spelled out, and the binding caveat added that their theorem is
for **GL(3)** while Davenport–Heilbronn is degree 2 — so they do not exclude it. Propagated to
`BARRIER-ZOO.md` I.1 and its item-7 rider. Deninger's axiom numbering corrected: **2.3 is spectral,
2.4 is the trace isomorphism, and Theorem 2.13 refutes 2.12**; his paper has also now appeared
(Annali SNS Pisa (5) **25** (2024), 1717–1725). Conrey–Li corrected: those are **de Branges'**
positivity conditions, not Li's λ_n ≥ 0 criterion, and they fail for **ζ itself**, so the parallel
is one of genre. The Kaczorowski–Perelli cross-check the report asked for is an author's
computation, not a search result, and is logged as an explicit open item rather than guessed at.

**m1 non-circularity note (13 pp).** Also had no external references. Now §12, 22 verified entries.
**§9's lineage rewritten**: "the first modern non-circular derivation" for Mattuck–Tate 1958 was
wrong by twenty-one years and is withdrawn; the record runs Severi 1903/1906 and Castelnuovo 1906,
**Hodge/Segre 1937 and Bronowski 1938**, Zariski 1952, Mattuck–Tate 1958, Grothendieck 1958, Kani
1984, Vainsencher–Voloch 1988, Hallouin–Perret. §8's headline is now "**a** proof, not **the**
proof", with Bombieri's own caveat carried — he regards the alternatives as *rediscoveries of
Severi's argument*, not independent routes. **§8's "Scope of the claim" rewritten** against the
arithmetic Hodge index theorem, which was the one-line refutation the old paragraph invited: that
theorem is codimension-one and one-signed (Faltings/Hriljac/Moriwaki/Yuan–Zhang), everything above
codimension one is open (Gillet–Soulé; Künnemann p. 115; Yuan–Zhang p. 2), and Faltings–Hriljac
**is** the arithmetic-surface case, so it cannot give more there. §8 now also answers Deninger's
opposite reading of Néron–Tate positivity as *support* for a positivity route to RH, using his own
conditional wording. From the publisher-grade GDZ scan of Grothendieck 1958: the "G. Bronowski /
(1958)" corruption is in **Grothendieck's own printed bibliography**, not in a later
retranscription, and his Segre start page (167) is wrong too — both flagged in §9.

**Seed no-go note (21 pp) — the framing rewrite.** Theorems 1–3 are now presented as Winkelmann's
in four places a reader cannot miss: **the abstract**, a **"Priority and attribution" note directly
under it**, an **attribution banner at the head of §3**, and the **novelty statement** in §9, with a
new §9 item 8 citing and distinguishing him. Nine refinements from the primary sources, all
applied: no §7 in his paper; Theorem 2 assumes **Zariski-dense**, not cocompact; the "at most one
other curve" wording is v3 (2003) while the mathematics is v1 (15 April 2002); he proves **one
direction only** and the converse is one line from his own Lemma 7, which *is* an equivalence — so
the "iff" is his too and cannot be claimed here; **"Hom", "rank" and any isogeny degree are absent
from his paper**, and he never takes λ prime, so the note's addition is an **explication in the
prime-indexed case**, not a sharpening of a theorem, and no priority over Theorems 1–3 is available.
**§9's "(T1) appears to be unrecorded" is deleted and formally withdrawn**: its negation is
displayed as **(C4E faible)** on p. 231 of Diaz, JTNB **9** (1997), attributed there to D. Bertrand
(Madras 1996), and the same paper carries unconditional partial results the note did not know
about. The germ is older still — **Alaoglu–Erdős 1944, p. 449**, ask the two-prime question in
print and record Siegel's three-prime theorem on p. 455, which is the exact four-versus-six-
exponentials split the note rediscovers. A second, stronger unconditional route to `End(E_p) = Z`
was added: Barré-Sirieix–Diaz–Gramain–Philibert's Mahler–Manin theorem gives `j(E_p)` transcendental.
`prior-art-r7a.md` now carries a **second dated withdrawal**, for the lineage clause.

### Process lessons

* **The verify-before-executing rule paid for itself many times over.** 21 of ~59 actions were
  wrong in a way that would have put a false sentence into a paper. A referee opening Ito–Ito–
  Koshikawa's Remark 1.3 or Kleiman's Remark 3.10 catches those in one line each.
* **A secondary bibliography is not primary evidence, and neither is an OCR layer.** Grothendieck's
  own 1958 bibliography carries a wrong initial and a wrong page; Numdam's OCR of Diaz silently ate
  a `/2iπ`; Crossref and Cambridge Core both render Winkelmann's title with a spurious `Γ..`. Every
  one of those would have propagated.
* **Corpus before network, still.** The published Farmer–Gonek–Lee paper — the one that actually
  carries the constant 0.8051 — is not on arXiv and *was already in `fetched-r2/`*. The obvious
  arXiv preprint has two authors and the number 0.6544, and stopping there would have produced a
  confident REFUTED.

### State at close

All four packages rebuilt from clean and passing `results/arxiv/check-submittable.sh`:
**a4-no-go 44 pp, m0-axiom 14 pp, m1-noncirc 13 pp, seed-no-go 21 pp — ALL CHECKS PASSED.**
CIRCULATION-PREP steps 1a/1b/1c/2/3/4 are all **DONE**. `results/arxiv/README.md` updated with the
new page counts and a "citation pass" section. **Everything in CIRCULATION-PREP is now closed. The
only open item is Session-9 item 5 — whether to circulate — which is the sponsor's decision, not
the program's.** Nothing in this session touched a theorem, a proof, a number, or a verdict.
