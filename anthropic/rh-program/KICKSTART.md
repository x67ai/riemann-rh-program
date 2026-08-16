# KICKSTART — how to run RH-program sessions (operations guide)

**What this file is:** the operating manual for launching sessions — where to run them (cloud vs local), the exact prompt to paste, and the environment rules. **It contains no program state.** All research state lives in `STATUS.md` (the resume point) and `LOG.md`; this file only tells the sponsor and Claude how to boot a session, which then follows STATUS.md.

Written 2026-08-16, after the infrastructure side-session that (a) empirically verified the 64k→128k output-ceiling fix and (b) established cloud sessions as the recommended way to run heavy multi-agent work.

---

## Part 1 — For the sponsor (plain language, no tech skills needed)

### One-time setup (~10 minutes, do once)

1. In a browser, go to **claude.ai/code** and sign in with your usual Claude account.
2. When it asks to connect GitHub, approve it and grant access to **`x67ai/riemann-rh-program`** (the repo is already on GitHub — nothing to upload).

### Starting the next RH session (recommended: in the cloud)

1. On claude.ai/code, start a **new session** on `x67ai/riemann-rh-program`.
2. Paste exactly this:

   > Read anthropic/rh-program/KICKSTART.md and follow its "Part 2 — session bootstrap". Then proceed with the program.

3. That's all. You can close the laptop or shut it down — the session keeps running on Anthropic's computers. Check progress any time from the Claude phone app or any browser (same account).

The same one-line prompt works for **every** session type, cloud or local — the bootstrap below figures out the rest from STATUS.md.

### When a cloud session finishes

- It will have saved and pushed its results to GitHub. If it says it opened a **pull request** instead, open the link it gives you and click the green **Merge** button — that's the whole job.
- Your Macs catch up automatically: every session starts with `git pull` (step 1 of the bootstrap below), so the next session on either machine sees the cloud session's work.

### Local sessions (mainly for the Wolfram/Mathematica queue)

Cloud sessions cannot reach Mathematica on your Macs. When STATUS.md lists items under a "Wolfram queue" heading, run a local session:

1. Prefer the **Mac Mini** (stays awake, runs cooler). If using the MacBook: keep it **plugged in with the lid open** for the entire run.
2. Open Terminal in the `riemann` folder, type `claude`, and paste the same one-line prompt from above.

### Things NOT to do

- Don't sync or move `~/.claude` or Claude's tmp folders between machines (login credentials live there; syncing can corrupt sessions and gives no benefit — the repo plus cloud sessions already provide cross-machine resume).
- Don't route this program through Claude Cowork — it's a separate product with no access to these workflows.

### Known issues — fixed and standing

| Issue | Status |
|---|---|
| Agents dying while writing large JSON (the "64k" failures) | **FIXED & VERIFIED 2026-08-16** — the repo's `.claude/settings.json` raises the per-response ceiling to 128k; a probe emitted 97,505 output tokens in one response cleanly (old ceiling 64k). |
| Long local runs dying overnight / "orphaned" | Cause: the Mac going to **sleep** kills the run (reproduced 2026-08-16). Cloud sessions are immune; locally, keep the lid open and plugged in. |
| MacBook running hot, fans on | Many parallel agents running on the laptop. Cloud sessions are immune; otherwise prefer the Mac Mini. |

---

## Part 2 — For Claude: session bootstrap (binding)

Every session in this repo — cloud or local — starts here:

1. **Sync first:** run `git pull` (a cloud clone may be stale; a local repo may be behind a cloud session's pushes). Check `git log --oneline -5` for where history left off.
2. **State:** read `anthropic/rh-program/STATUS.md` top to bottom — it is the sole authority on program state, sponsor standing orders, and next actions (its "How to resume" checklist). Then read the latest `LOG.md` entry. This file adds only environment rules; where they seem to conflict, STATUS.md wins.
3. **Detect the environment:**
   - **Cloud session** (claude.ai/code): the sponsor's local Wolfram MCP is unavailable. Do all numerics in Python (mpmath/sympy/numpy — standing order 5's computational verification remains mandatory). Anything that genuinely requires Mathematica goes under a `## Wolfram queue` heading in STATUS.md for a local follow-up session — never silently skipped.
   - **Local session:** Wolfram MCP available; work through any `## Wolfram queue` items early. Before long runs, remind the sponsor the machine must stay awake (lid open, plugged in). Check for orphaned runs per STATUS.
4. **Output budget:** `.claude/settings.json` sets `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000` — verified reaching workflow subagents (97,505-token single StructuredOutput response, 2026-08-16, run wf_15eb682f-dd9). Keep the Session-4 lessons regardless: pin heavy agents' `effort`, prefer chunked write-to-disk for very large deliverables, and state the 128k budget explicitly in any brief that demands a huge single response (an unbriefed subagent self-rations to ~57k).
5. **Persistence:** per STATUS git discipline — commit after each phase harvest and at session close, and ALWAYS push to origin. In a cloud session, pushing is the ONLY way work reaches the sponsor's machines; if direct push is blocked, open a PR and tell the sponsor in plain language to click **Merge** (the sponsor is non-technical — give the exact link and button, no jargon).
6. **Close-out:** standing order 2 — all learnings on disk (LOG.md entry + STATUS.md update + touched `directions/` files), committed and pushed, before the session ends.
