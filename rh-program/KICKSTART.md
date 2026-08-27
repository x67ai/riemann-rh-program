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
4. **Keep-awake:** before any long-running work, start `caffeinate -is` as a background Bash task so the machine cannot idle-sleep mid-run, and remind the sponsor once at session start: lid open, plugged in. (Sleep mid-response is the proven killer of long runs — the 2026-08-16 probe and the Session-3 orphans.)
5. **Thermal & RAM batching policy (binding — sized to this machine; replaces the retired "prefer cloud for heavy runs" rule):**
   - **Agent fan-out is NOT the heat source.** Subagents run on Anthropic's servers; their local footprint is I/O. Use the harness's full concurrency — min(16, cores−2) = **8 concurrent agents** on this machine — whenever the work warrants it. Standing order 3 (full parallelism) stands; do NOT undershoot fan-out for thermal reasons.
   - **Local CPU-heavy processes ARE the heat source.** Cap at **4 concurrent** heavy local jobs — "heavy" = anything that pegs a core for minutes (long mpmath/numpy/sympy sweeps, batch PDF/vision prep, compiles). Four matches the M5's performance cores; a 5th+ job spills onto efficiency cores, sustains all-core load, and buys little throughput for a lot of heat.
   - **Batch, don't shrink.** Chunk large compute sweeps into slices of ≤4 jobs and run slices back-to-back (`pipeline()` paces this naturally; in plain Bash: launch 4, `wait`, launch the next 4). The full computation always runs — bounded concurrency, zero reduction in scope. Sponsor calibration, in writing: **"do not undershoot — have as many computations as this M5 machine can handle."** 8-wide agents + 4-wide heavy compute is the operating point, not a ceiling to creep below.
   - **Wolfram:** one kernel, strictly serial queue (the MCP is single-kernel and Mathematica kernels are RAM-heavy).
   - **RAM (24 GB):** chunked write-to-disk for large intermediates (also the 128k-safe delivery pattern); never hold multi-GB arrays in several concurrent processes; one Mathematica kernel at a time.
   - **Escalation:** if `pmset -g therm` shows `CPU_Speed_Limit` sustained below 100 (actual throttling, not mere fan noise), drop heavy-compute concurrency to 3. Never below 3, and never reduce the total amount of work.
6. **Output budget:** `.claude/settings.json` sets `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000` — verified reaching workflow subagents (97,505-token single StructuredOutput response, 2026-08-16, run wf_15eb682f-dd9). Keep the Session-4 lessons regardless: pin heavy agents' `effort`, prefer chunked write-to-disk for very large deliverables, and state the 128k budget explicitly in any brief that demands a huge single response (an unbriefed subagent self-rations to ~57k).
7. **Persistence:** per STATUS git discipline — commit after each phase harvest and at session close, and ALWAYS push to origin: GitHub is the program's off-machine backup and history. (The corpus itself is deliberately NOT pushed — `fetched/`/`fetched-r2/` stay local-only per the sponsor's Session-4.5 decision; the sponsor keeps their own backup of those.)
8. **Close-out:** standing order 2 — all learnings on disk (LOG.md entry + STATUS.md update + touched `directions/` files), committed and pushed, before the session ends.
