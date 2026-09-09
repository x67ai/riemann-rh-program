# KICKSTART — how to run RH-program sessions (operations guide)

**What this file is:** the operating manual for launching sessions — where to run them, the exact prompt to paste, and the environment rules. **It contains no program state.** All research state lives in `STATUS.md` (the resume point) and `LOG.md`; this file only tells the sponsor and Claude how to boot a session, which then follows STATUS.md.

Written 2026-08-16 after the infrastructure side-session (64k→128k output-ceiling fix verified). **Revised the same day, sponsor directive: the cloud path is RETIRED — every session runs locally on the sponsor's MacBook.** Rationale: the PDF corpus (`fetched/` + `fetched-r2/`, 336 files) is local-only/gitignored and invisible to cloud clones, and Wolfram/Mathematica is local-only too; running locally removes both gaps at once. The old reasons for preferring the cloud (overnight sleep-deaths, heat) are handled directly by the keep-awake and batching rules in Part 2.

---

## Part 1 — For the sponsor (plain language, no tech skills needed)

### Starting the next RH session

1. Open **Terminal** in the `riemann` folder, type `claude`, press Enter.
2. Paste exactly this (kept as a plain code block so it copies clean — no leading bars; sponsor formatting rule, 2026-08-26):

```
Read rh-program/KICKSTART.md and follow its "Part 2 — session bootstrap". Then proceed with the program.
```

3. Keep the laptop **plugged in with the lid open** for the entire run. That's the whole job. The session keeps the machine awake on its own (`caffeinate`), and it paces heavy computations so the laptop shouldn't run hot for long stretches — warm is normal, sustained roaring fans should now be rare.

The same one-line prompt works for **every** session — the bootstrap below figures out the rest from STATUS.md.

### Why local-only (what changed on 2026-08-16)

- Cloud sessions (claude.ai/code) work from the GitHub copy of this folder, which **does not contain the PDF corpus** (`fetched/` and `fetched-r2/` are deliberately kept off GitHub) and cannot reach Mathematica. Running on the MacBook gives every session the full corpus *and* Mathematica — no more splitting work between "cloud sessions" and a "Wolfram queue".
- The two old local problems are solved differently now: sleep-deaths are prevented automatically (see Part 2 step 4), and heat is controlled by a pacing policy sized to this exact machine (M5, 10 cores, 24 GB) — the work is batched, never reduced.

### Things NOT to do

- Don't start program sessions at claude.ai/code — that copy can't see the PDF corpus or Mathematica. (If one is ever started there by mistake, it will detect this and stop safely.)
- Don't close the lid or unplug the power during a run.
- Don't sync or move `~/.claude` or Claude's tmp folders between machines (login credentials live there; syncing can corrupt sessions and gives no benefit).
- Don't route this program through Claude Cowork — it's a separate product with no access to these workflows.

### Known issues — fixed and standing

| Issue | Status |
|---|---|
| Agents dying while writing large JSON (the "64k" failures) | **FIXED & VERIFIED 2026-08-16** — the repo's `.claude/settings.json` raises the per-response ceiling to 128k; a probe emitted 97,505 output tokens in one response cleanly (old ceiling 64k). |
| Long runs dying overnight / "orphaned" | Cause: the Mac going to **sleep** kills the run (reproduced 2026-08-16). Now handled: every session starts `caffeinate` so the machine can't sleep mid-run; sponsor keeps the lid open and power plugged in. |
| MacBook running hot, fans on | Handled by the Part 2 batching policy: at most 4 heavy local computations at once (matched to the M5's 4 performance cores); big sweeps run as back-to-back batches. Throughput is kept in full — work is paced, never shrunk. |

---

## Part 2 — For Claude: session bootstrap (binding)

Every session in this repo starts here:

1. **Sync first:** run `git pull` (the local repo may be behind). Check `git log --oneline -5` for where history left off.
2. **State:** read `rh-program/STATUS.md` top to bottom — it is the sole authority on program state, sponsor standing orders, and next actions (its "How to resume" checklist). Then read the latest `LOG.md` entry. This file adds only environment rules; where they seem to conflict, STATUS.md wins.
3. **Environment — always local (sponsor directive 2026-08-16):** every session runs on the sponsor's MacBook Pro (Apple M5: 4 performance + 6 efficiency CPU cores, 24 GB RAM). Wolfram MCP is available — work through any `## Wolfram queue` items early. The full PDF corpus is on disk (`fetched/` 174 files, `fetched-r2/` 162 files, both gitignored/local-only). **Sanity check:** if those directories are missing, you are in a corpus-less clone (e.g. a stray cloud session) — STOP and tell the sponsor to relaunch in Terminal on the MacBook; never improvise around the missing corpus.
4. **Keep-awake + the two watchdogs (sponsor directive 2026-09-02, top priority — see STATUS.md standing order 0):** at session top start `nohup caffeinate -dimsu &`, `nohup ~/.claude/push-watchdog.sh "<repo root>" &` and `nohup ~/.claude/autocommit-watchdog.sh "<repo root>" "Session N" &` (the latter commits whatever agents have written every ten minutes, so a usage-limit death loses at most ten minutes; check all three with `pgrep`). Before any long-running work, make sure `caffeinate` is running so the machine cannot idle-sleep mid-run, and remind the sponsor once at session start: lid open, plugged in. (Sleep mid-response is the proven killer of long runs — the 2026-08-16 probe and the Session-3 orphans.)
5. **Thermal & RAM batching policy (binding — sized to this machine; replaces the retired "prefer cloud for heavy runs" rule):**
   - **SEQUENTIAL STREAMS (sponsor directive 2026-09-02, overrides the fan-out sentence below): one workflow at a time, at most two agents in flight, the next stream after the previous one is harvested** — a usage-limit death then costs one agent, not a dozen. The thermal notes below still hold for local compute.
   - **Agent fan-out is NOT the heat source.** Subagents run on Anthropic's servers; their local footprint is I/O. Use the harness's full concurrency — min(16, cores−2) = **8 concurrent agents** on this machine — whenever the work warrants it. Standing order 3 (full parallelism) stands; do NOT undershoot fan-out for thermal reasons.
   - **Local CPU-heavy processes ARE the heat source.** Cap at **4 concurrent** heavy local jobs — "heavy" = anything that pegs a core for minutes (long mpmath/numpy/sympy sweeps, batch PDF/vision prep, compiles). Four matches the M5's performance cores; a 5th+ job spills onto efficiency cores, sustains all-core load, and buys little throughput for a lot of heat.
   - **Batch, don't shrink.** Chunk large compute sweeps into slices of ≤4 jobs and run slices back-to-back (`pipeline()` paces this naturally; in plain Bash: launch 4, `wait`, launch the next 4). The full computation always runs — bounded concurrency, zero reduction in scope. Sponsor calibration, in writing: **"do not undershoot — have as many computations as this M5 machine can handle."** 8-wide agents + 4-wide heavy compute is the operating point, not a ceiling to creep below.
   - **Wolfram:** one kernel, strictly serial queue (the MCP is single-kernel and Mathematica kernels are RAM-heavy).
   - **RAM (24 GB):** chunked write-to-disk for large intermediates (also the 128k-safe delivery pattern); never hold multi-GB arrays in several concurrent processes; one Mathematica kernel at a time.
   - **Escalation:** if `pmset -g therm` shows `CPU_Speed_Limit` sustained below 100 (actual throttling, not mere fan noise), drop heavy-compute concurrency to 3. Never below 3, and never reduce the total amount of work.
6. **Output budget:** `.claude/settings.json` sets `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000` — verified reaching workflow subagents (97,505-token single StructuredOutput response, 2026-08-16, run wf_15eb682f-dd9). Keep the Session-4 lessons regardless: pin heavy agents' `effort`, prefer chunked write-to-disk for very large deliverables, and state the 128k budget explicitly in any brief that demands a huge single response (an unbriefed subagent self-rations to ~57k).
7. **Sponsor fetch items (sponsor rule 2026-09-06):** anything the sponsor must fetch goes into the current `FETCH-LIST-ROUND<n>.md` at the harvest that surfaces it — full citation, priority, reason — and NOWHERE else (STATUS, LOG and direction files carry a one-line pointer at most).
8. **Persistence (document as you go — standing order 0):** commit after EVERY landed unit, not only at phase harvests; write the live-task entry in STATUS.md at launch; append LOG.md as things land; harvest a completed run before starting anything new; ALWAYS push to origin: GitHub is the program's off-machine backup and history. (The corpus itself is deliberately NOT pushed — `fetched/`/`fetched-r2/` stay local-only per the sponsor's Session-4.5 decision; the sponsor keeps their own backup of those.)
9. **Close-out:** standing order 2 — all learnings on disk (LOG.md entry + STATUS.md update + touched `directions/` files), committed and pushed, before the session ends.
10. **Direction-selection discipline under a lean budget (sponsor, 2026-09-09; source: `results/external/openai-ns-2026/process-lessons.md`).** The sponsor's constraint: "we don't have that many resources, we must be really smart about directions to pursue." (The sponsor is willing to keep going as long as it takes; that is a constraint on us, not a schedule — the program moves as fast as the mathematics allows and never paces itself to a horizon.) Six rules, each a one-agent cost or free; none assumes scale:
   - **(a) Consolidation step between phases.** Before writing the next round's briefs, run ONE consolidation agent whose input is every stream's on-disk intermediate results and whose output is `results/<phase>/insights-digest.md`: per stream, the three most useful findings, the most useful failure, and what another stream should borrow. The next briefs must quote it. (OpenAI's cross-pollination step; ours was implicit and lossy.)
   - **(b) Ladder rule for new machinery.** Any new instrument (S1–S5 spec) is first run on the rungs where the answer is KNOWN — function fields (RH true), Epstein / Davenport–Heilbronn (RH false), then Dirichlet L — and the write-ups are fed verbatim into the ζ brief. A brief that skips the ladder is returned. (OpenAI solved Euler first and prompted NS with it; C3-r's mapping-torus-first order is the program's own precedent.)
   - **(c) Refutation-shaped output is every lane's default deliverable.** B2 and D1 exist as refutation directions; the change is that EVERY lane, including proof-shaped ones, must close each unit with a stated theorem of the form "proof class X cannot yield Y because Z" or "Y holds" — never a narrative. The A4 no-go paper is the template. Barrier-zoo entries are extracted from these statements, not from prose. (OpenAI won on the disproof variants C/D; for this program the disproof shape is the zoo.)
   - **(d) Reallocation rule.** A result graded above threshold (a new zoo Group-IV barrier, a lemma surviving two blind referees, or a Lean-checked statement) pulls the NEXT session's full agent budget into its follow-ups; other lanes pause and are noted as paused in STATUS. Fixed per-lane budgets are the default only while nothing has signal.
   - **(e) Shared stream scratch.** Every multi-agent stream gets `results/<stream>/SHARED.md`; each agent appends its partial results as they land and reads the file at start. Poor man's intra-group channel; harvests read it too.
   - **(f) Formalization downstream, with an independent checker.** Lean is never a gate on exploration. When something is formalized, a second agent rebuilds it from a clean clone and reports `#print axioms` for every top-level theorem; the report is filed next to the proof. (OpenAI's Comparator step; detail in `results/external/openai-ns-2026/lean-repos.md`.) The checker compares against a human-reviewed statement file (`Challenge.lean`-style: the theorem as the sponsor's referee would state it, nothing else), and a fidelity ledger records where the formal statement differs from the prose one — the Alpöge–Buckmaster practice.
   - **(g) Contract theorems and discharge maps (from the paper, `ns-paper-read.md`).** A direction's "Current frontier" is written as a contract theorem with numbered clauses; every brief names the clause it discharges; constants carry a written dependency chain checked for cycles; margins carry a slack ledger. Briefs and notes are linted for "clearly / obviously / easy to see / well known" — the 166-page proof contains none of them.
   - **(h) Free design parameter first.** When choosing between statement shapes, prefer the one with a free design parameter (the paper's force; our certificates' test functions and kernels), and record in the zoo where each proof class's parameter is pinned and by what cone/positivity condition.
   - **(j) Lean shipping standard (from `lean-repos.md`).** Every formalized unit ships as a Comparator-style pair — a challenge file holding only the reviewed statement with `sorry`, and a solution that never imports it — plus a `formalization.yaml` with honest `automation` and `review` fields and a `fidelity.divergences` paragraph; trust greps (`axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`, `sorry`) on every merge; numerics as many small certificate modules with dyadic integers; keep the program's two-producer back-parse cross-check, which neither public repo has.
   - **(i) Hash early.** When a unit lands (a note, a certificate, a Lean file), record its SHA-256 in LOG.md at the commit; the public GitHub history is the timestamp. (Alpöge–Buckmaster's lesson from the credit dispute.)
   And one rule about what NOT to copy: width. Ten thousand agents is not a technique, it is a budget. The concurrent Alpöge–Buckmaster result (two people, Claude and Codex, about a year, Lean-verified) is the regime this program is in; invest in steering artifacts — direction files, briefs, the zoo, the digest — not in fan-out.
