# RH Research Program — Master Tracker (dashboard)

**Goal:** Building on `zeta-23-lean-main` (the 2026 "more than two thirds of zeta zeros are simple and on the critical line" theorem + Lean formalization), devise novel methods — advancing the existing machinery AND building wholly new machinery, up to and including a new mathematical field — toward proving or refuting RH. The 2/3 effort itself did not and provably cannot decide RH within its certificate class; the program is designed around its formalized obstructions.

**Horizon:** MONTHS, run in on/off sessions as the sponsor's usage allows, continuing until RH is decided or the program is retired. Documentation is the program's persistent brain: every session starts by reading it and ends by updating it. Refutations and dead ends are first-class results — record them as carefully as successes.

## Documentation protocol (read me first, every session)

Files and their roles:
- `STATUS.md` (this file) — always-current dashboard: phase state, live tasks, constraints, next actions. Overwrite freely; keep lean.
- `LOG.md` — append-only session journal, one entry per working session (template inside). Never edit past entries. When STATUS and LOG disagree, LOG explains why.
- `directions/<ID>-<name>.md` — one living document per research direction (see `directions/README.md` for template and lifecycle). The long-term substance accumulates HERE.
- `results/` — immutable phase outputs (maps, literature, proposals, verdicts, prospectus snapshots).
- `sources-extracted/` — plain-text pages of the three zeta PDFs; grep these, never re-parse the PDFs.

Session discipline:
- START: read STATUS.md fully; read the latest LOG.md entry; read any `directions/` file you are about to work on. Check "Live/completed background tasks" for orphaned runs and harvest their journals. Check `git log --oneline -5` for where history left off.
- DURING: new durable results go under `results/` or the relevant `directions/` file immediately (session scratchpads in /tmp die with the session).
- GIT (sponsor directive, Session 2): the repo root is `/Users/jaytyagi/Documents/Work/2026/Math/riemann` (branch `main`). Commit after every phase harvest or meaningful state change (e.g. "Phase 4 verdicts harvested", "prospectus v1"), and ALWAYS at session end. Message style: what landed + program state. Remote: PENDING — gh is authenticated (account x67ai) but repo creation is blocked for the agent; the sponsor will run `gh repo create riemann-rh-program --private --source . --remote origin --push` at the next break. Once `origin` exists, push at every session end (and after phase-harvest commits).
- END (or when the user says they're stopping, or context runs long): update STATUS.md (phases, live tasks, next actions), append a LOG.md entry, update touched `directions/` files' "Current frontier", commit.
- The persistent memory entry `rh-research-program` points here; keep it pointing here and nothing else — all content lives in these files, not in memory.

**Started:** 2026-08-11. **Last updated:** 2026-08-11 ~15:10, Session 2 close (update this line on every edit).

**SPONSOR DIRECTIVE (2026-08-11):** The user's priority is WHOLLY NEW MACHINERY — potentially a new mathematical field — over extension of existing machinery. Their stated position: existing machinery has provable limitations (that is why RH stands); low trust that existing machinery can decide RH. Program response: Track C added (2 new-field designers, C1 requirements-first field construction, C2 rigidity/conservation-laws); in verification and synthesis, Track B/C directions are the headline and Track A is reframed as supporting infrastructure (instruments, specification-writing, proportion progress) — not a competing bet on proving RH with old tools.
**This file is the resume point.** A fresh session should read this file top to bottom, then follow "How to resume" at the end.

---

## Program plan (phases)

1. ✅ **Understand** — map the paper + Lean repo: method, exact constants, formalized no-go theorems, extension hooks. (6-agent workflow, done.)
2. ✅ **Literature** — verified state of the art on 12 fronts, Aug 2026. (web agent, done.)
3. 🔶 **Design** — 9 of 10 DONE (A1-A3, B1-B4, C1-C2 in `results/design-proposals.json`; direction files under `directions/`). **A4:lindelof-lock was stopped mid-run at user pause (no result journaled) — must be RE-RUN on resume**: its full prompt is in `scripts/rh-design-wf_30287ea4-643.js` under label 'A4:lindelof-lock'; run it as a SINGLE agent (do NOT relaunch the whole 8-agent script — the other 7 are already harvested).
4. 🔶 **Adversarial verify** — Session-2 relaunch got **12 of 18** killer/referee verdicts before the Session-2 pause (harvested to `results/verdicts-partial.json`). Missing: kill:A2, kill:B4, kill+ref:C1, kill+ref:C2, completeness critic — all covered by the reduced script `scripts/rh-verify-remaining.js` (launch on resume). A4's kill+ref are inside `scripts/rh-a4-design-verify.js`. NOTE for adjudication: killers say REFUTED on A1 (1.5) and B1 (1.5) while referees say survives-with-repairs (6.5 / 5) — resolve these conflicts in synthesis (possibly a tie-breaker agent reading both verdicts).
5. ⬜ **Synthesize** — rank surviving directions, write the research prospectus, publish as artifact; optionally add numerics per direction (Wolfram) and Lean statement sketches.

## Key artifacts (all durable, in this directory)

- `results/full-map.md` — the six-reader technical map of paper + Lean repo (method pipeline, constants, formalized ceilings, extension hooks). THE core context document.
- `results/map-hooks.txt` — condensed limitations + extension hooks per reader.
- `results/literature.md` — 12-front state of the art + no-go results + campaign residue (from the 95-page transcript).
- `results/design-proposals.json` — (to be written when phase 3 completes; if missing, recover from journal, see below)
- `sources-extracted/` — plain-text page extractions: `full_p1..35.txt` (main paper), `condensed_p1..5.txt`, `tx_001..095.txt` (discovery-transcript volume). Grep these instead of re-reading PDFs.
- Original sources (parent dir): `../zeta-two-thirds.pdf`, `../zeta-two-thirds-condensed.pdf`, `../zeta-transcript-explanation.pdf`, `../zeta-23-lean-main/`.

## Hard constraints every proposal must respect (distilled)

- **DH/Epstein filter:** Davenport–Heilbronn & Epstein (class no. >1) satisfy functional equation + explicit formula + L² mean values yet violate RH ⇒ any FULL-RH route must consume Euler-product/multiplicativity input beyond L²-means. Proportion-improvement routes are exempt but must say so.
- **Formalized ceilings (in Lean, in the repo):** bandwidth-one certificate ceiling **0.6818287**; `lemmaR_tight` (two-moment rank–trace certificate exhausted; on-line double ≡ off-line pair); dimension cap d = λN; κ(λ)=1/λ+λ/3 ≥ 2/√3 ⇒ trace+Frobenius certificates cap at **2−2/√3 ≈ 0.8453 at ANY bandwidth**.
- **Bandwidth-1 wall location:** single lemma chain `O1_bound → prop_PP → tr2` (PrimeSideB): off-diagonal prime pairs bounded via Montgomery–Vaughan in absolute value, zero cancellation used. λ>1 needs Hardy–Littlewood-strength pair correlations.
- **Literature no-gos:** Alternative Hypothesis consistent with all bandwidth-1 data (arXiv:2507.06823); Bombieri small-support Weil positivity unconditional (small cones prove nothing); Bombieri–Garrett ~94% pseudo-Laplacian cap (arXiv:2002.07929); parity problem; Conrey–Li vs de Branges positivity; Rodgers–Tao Λ≥0 (RH ⟺ Λ=0; certified Λ>0 would DISPROVE RH); Radziwiłł mollifier limits.
- **Campaign residue (transcript):** ~30 refuted routes; per-pair quadratic integrality pricing FALSE; Pontryagin negative-index counting route structurally empty; "every route's first substantive step was Weil positivity in disguise".

## Verified numerics (Wolfram, this session)

- c₁\* = 0.7532960678560707 (Montgomery–Taylor), Theorem D proportion 2−1/c₁\* = 0.6725007036794117. ✓
- Payoff targets (paper Remark 1.1): pair-correlation support 1.043→70%, 1.265→80% independently reproduced from the unconstrained cosine-window formula c\*_λ = √2 tan(λ/√2)/(1+(λ/√2)tan(λ/√2)); the 1.70→90% figure is NOT reproduced by that formula (formula valid only λ ≲ π/√2 ≈ 2.22 and, more importantly, for λ>1 the form-factor input changes: F conj ≡ 1 beyond the band, not |α|) — use the paper's numbers, present the formula curve only for λ≤1.
- Flat-window two-moment cap: max_λ H(λ)=2−1/λ−λ/3 at λ=√3: **0.84530**. ✓
- HL\*(4) chain: Christoffel Λ₂(0;1)=5/36 ⇒ n₊/d ≥ 31/36 ⇒ s₁ ≥ 2·(31/36)−1 = **13/18 = 0.7222**. ✓ Exact.
- Optimal-window curve 2−1/c\*_λ grid (λ≤1 valid): 0.6→0.135, 0.7→0.340, 0.8→0.486, 0.9→0.593, 1.0→0.6725.

## Designer briefs (phase 3, for reference / re-launch)

Track A (advance machinery): A1 break-bandwidth (evaluate O1 off-diagonal beyond MV; HL*(4,λ)→13/18; edge-constraint LP), A2 richer-functionals (escape ceiling format: close 0.6725→0.6818 gap, depth pricing/λ_max, commutator traces, 3-correlation ceiling LP), A3 families-derivatives (q-averaging with Gevrey taper, GL(2) families, ξ^(k) escalation, hybrid uniformity), A4 lindelof-lock (short-window P_X bounds via Guth–Maynard/ANTEDB large-value technology; unlock tr R³ + orthonormalization + λ_max pricing).
Track B (new machinery): B1 mult-positivity (multiplicativity-sensitive Weil positivity; Connes–Consani prolate; amplified vectors; e^{−4πX} margin law), B2 refutation-program (Λ>0 channel, distinguishing statistics, "wanted poster" constraints on any off-line zero, killing AH), B3 arithmetic-debranges (K_a multiplicity-visible kernel made prime-computable via δ-tilt; Suzuki 2301.00421), B4 zero-dynamics (feed new unconditional statistics into de Bruijn–Newman flow; dynamical certificates for H_t; Polymath15 pipeline).
Track C (new-field construction, added on sponsor directive): C1 requirements-first-field (work backwards from spec S1–S5; skeletons: Hodge-index over Spec Z via Connes–Consani Riemann-Roch/Jacobian/absolute curve; Osterwalder–Schrader reflection positivity on the adele class space with a prime transfer operator; Lorentzian/log-concavity technology), C2 rigidity-conservation (Ghosh–Peres number rigidity made deterministic via explicit-formula sum-rule systems; single-defect exponential visibility e^{L·depth}; the overlooked Λ(n) ≥ 0 pointwise-positivity input — DH violates it and L²/Weil-form methods never use it; Boas–Kac/Cohn–Elkies double-positivity cone vs the explicit formula unconditionally).
Full prompts: in the workflow scripts (paths below).

## The specification for new machinery (S1–S5, distilled from all obstructions — reuse in every future brief)

- S1 Euler-product sensitivity: consume an input DH/Epstein violate (multiplicativity at every prime beyond L²-means; Ramanujan; note Λ(n) ≥ 0 pointwise is itself such an input).
- S2 o(N)-sensitivity: must see a SINGLE off-line zero; all density/proportion methods are structurally blind to o(N) exceptions.
- S3 Multiplicity-visibility: on-line double vs off-line pair must be distinguishable (Weil-form signature is not; K_a de Branges kernels are).
- S4 A new positivity GENERATOR, not just a bigger Weil-positivity cone (algebraic: Hodge index/ampleness; analytic: reflection positivity/complete monotonicity; combinatorial: Lorentzian polynomials; probabilistic: determinantal/negative association).
- S5 Survive the named no-gos: AH world, Bombieri–Garrett 94%, parity, Conrey–Li, Λ ≥ 0, bandwidth/two-moment ceilings.

## PAUSED 2026-08-11 ~15:10 (Session-2 close, user break). Nothing is running. Resume actions, in order:

1. Launch BOTH in parallel (self-contained, cross-session safe):
   - `Workflow({scriptPath: "<rh-program>/scripts/rh-a4-design-verify.js"})` — A4:lindelof-lock designer → its killer+referee (3 agents; the Session-2 attempt died mid-designer with 0 results journaled).
   - `Workflow({scriptPath: "<rh-program>/scripts/rh-verify-remaining.js"})` — the 6 missing verdicts (kill:A2, kill:B4, kill+ref:C1, kill+ref:C2) + completeness critic (7 agents). Do NOT relaunch the full `rh-verify-wf_eb8254d0-341.js` — 12/18 verdicts are already harvested in `results/verdicts-partial.json`.
2. Merge `results/verdicts-partial.json` + both new runs → `results/verdicts.json` (delete the -partial file). A4 design → merge into `results/design-proposals.json`, create `directions/A4-lindelof-lock.md` (template: any sibling).
3. Write each verdict pair into its directions/ file ("Verification verdicts" section); flip direction statuses. Adjudicate the killer-vs-referee conflicts (A1, B1 — see phase 4 note; consider a tie-breaker agent fed both verdicts + the direction file).
4. Phase 5 synthesis: rank per sponsor directive (Track B/C headline; A = instruments), write prospectus, load artifact-design skill BEFORE writing the page, publish artifact, save source copy into rh-program/, append LOG.md entry.
5. Git: commit after each harvest and at session end. Remote pending — sponsor will run `gh repo create riemann-rh-program --private --source . --remote origin --push` at a break; after that exists, push too.

## Live/completed background tasks (session-specific paths — data persists on disk after session death)

- Session 2: Phase-4 verify relaunch `rh-verify`: task w5nv06qz1, run wf_a2389ed4-3f1. **STOPPED at Session-2 close with 12/18 verdicts** — harvested to `results/verdicts-partial.json`; journal snapshot `results/journals/wf_a2389ed4-3f1.journal.jsonl`. Remaining 6+critic covered by `scripts/rh-verify-remaining.js`.
- Session 2: A4 design+verify `rh-a4-design-verify`: task w5rp1heki, run wf_89b075e1-f64. **STOPPED at Session-2 close, 0 results** (designer died mid-run). Relaunch whole script next session.

- Phase 1 workflow `rh-understand`: task wz8rup87t, run wf_2a6a86ee-92c. DONE. Results distilled into results/full-map.md.
  Journal (raw per-agent results): `~/.claude/projects/-Users-jaytyagi-Documents-Work-2026-Math-riemann-anthropic/e8c24f5f-4faf-41e1-962d-7ba16dbd457a/subagents/workflows/wf_2a6a86ee-92c/journal.jsonl`
- Phase 2 literature agent: task a7144a5623a6dd106. DONE. Result saved as results/literature.md.
- Phase 3 supplement `rh-design-supplement` (Track C, 2 new-field designers): task w4dxvhdce, run wf_2d492d18-6bd. **RUNNING at last update.**
  Script: `~/.claude/projects/-Users-jaytyagi-Documents-Work-2026-Math-riemann-anthropic/e8c24f5f-4faf-41e1-962d-7ba16dbd457a/workflows/scripts/rh-design-supplement-wf_2d492d18-6bd.js`
  Journal: `~/.claude/projects/-Users-jaytyagi-Documents-Work-2026-Math-riemann-anthropic/e8c24f5f-4faf-41e1-962d-7ba16dbd457a/subagents/workflows/wf_2d492d18-6bd/journal.jsonl`
  On completion: append results into `results/design-proposals.json` alongside A1-B4.
- Phase 3 workflow `rh-design`: task wd7790w3z, run wf_30287ea4-643. **RUNNING at last update.**
  Script: `~/.claude/projects/-Users-jaytyagi-Documents-Work-2026-Math-riemann-anthropic/e8c24f5f-4faf-41e1-962d-7ba16dbd457a/workflows/scripts/rh-design-wf_30287ea4-643.js`
  Journal: `~/.claude/projects/-Users-jaytyagi-Documents-Work-2026-Math-riemann-anthropic/e8c24f5f-4faf-41e1-962d-7ba16dbd457a/subagents/workflows/wf_30287ea4-643/journal.jsonl`
  Full result on completion: `/private/tmp/claude-501/-Users-jaytyagi-Documents-Work-2026-Math-riemann-anthropic/e8c24f5f-4faf-41e1-962d-7ba16dbd457a/tasks/wd7790w3z.output` (NOTE: /tmp may be wiped on reboot — copy `result` JSON into `results/design-proposals.json` as soon as available; the journal.jsonl under ~/.claude is the durable copy).

## How to resume (fresh session checklist)

0. Follow the Documentation protocol above (STATUS → latest LOG entry → relevant directions/ files).
1. Read this file. Read `results/full-map.md` (skim `results/map-hooks.txt`) and `results/literature.md`.
2. Check whether `results/design-proposals.json` exists.
   - If yes → go to step 4.
   - If no → extract the 8 designer results from the phase-3 journal.jsonl (one `{"type":"result",...}` line per agent, labels A1:…B4:…) and save to `results/design-proposals.json`. If the journal is incomplete (session died mid-run), relaunch the design workflow from its script file (path above; it is self-contained) or reconstruct from the briefs summarized above.
3. If any designer failed/missing, re-run just that brief as a single agent.
4. Phase 4 (adversarial verify): for each proposal spawn critics — (a) obstruction check against the "Hard constraints" section above + barrier-zoo thinking (does an RH-false model satisfy all the proposal's inputs?), (b) novelty check against results/literature.md, (c) tractability check of first_theorem (are the inputs really proven? is the first step a known-hard problem in disguise?). One completeness critic across all 8 (what direction is missing?). Save verdicts to `results/verdicts.json`.
5. Phase 5: synthesize prospectus (rank by: soundness, novelty, tractability, payoff; keep refutation channels separate from proof channels), publish as an artifact (title ~ "RH Research Prospectus: Beyond the Two-Thirds Certificate"), save the HTML/MD source into this directory too (`prospectus.md`/`.html`). Include: the verified numerics table above, the constraint map, per-direction pages (thesis/mechanism/first theorem/milestones/Lean hook/numerics/risks), and an honest framing section (no claim of proving RH; what "success" means for each direction).
6. Wolfram numerics session id (this session, likely dead later): re-derive from the "Verified numerics" section rather than resuming the kernel.
7. Keep this file updated after each phase (flip ✅, update paths, append findings).

## Findings log (append-only)

- 2026-08-11: Phase 1+2 complete. Headline discovery: the repo formalizes its own impossibility results — the 2/3 method is *provably* saturated at every layer except its arithmetic input (bandwidth), and the single lemma chain `O1_bound → prop_PP → tr2` is where all further proportion progress must enter. Two-moment certificates cap at 0.845 at any bandwidth ⇒ proportion-1 (RH-strength) needs functionals beyond {tr, ‖·‖_F²} regardless of prime-correlation progress. PCC alone (no RH) already ⇒ 100% simple-on-line (arXiv:2503.15449) ⇒ the marginal value of *all* bandwidth->∞ pair data is exactly "100% but not RH": o(N) exceptional zeros remain invisible to every density-type method — full RH requires a qualitatively different input (DH/Epstein filter).
- 2026-08-11: Λ-channel insight for the refutation track: Rodgers–Tao Λ≥0 + RH ⟺ Λ=0 means a *certified strictly positive lower bound* on Λ is a legitimate, well-defined disproof channel — apparently unexplored as a search program (no serious counterexample-search program exists per Farmer arXiv:2211.11671).
