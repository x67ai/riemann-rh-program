# Process lessons from the OpenAI Navier–Stokes release — what transfers to the RH program

**v0, Session 18, 2026-09-09 18:15 IST, written from the announcement page only** (`openai-announcement-2026-09-08.md`); to be revised once the three reader reports (`ns-paper-read.md`, `euler-and-context.md`, `lean-repos.md`) are in. Sponsor's framing: "I just wanted you to look at problem-solving techniques if those could be used in our program too." So this note is about METHOD. The fluid mechanics is recorded elsewhere in this folder and is not the point.

**Scale disclaimer first.** OpenAI: ~10,000 concurrent agents, 88 hours, 2.7 million messages, ~130 billion output tokens on the one problem, an internal model "significantly more capable than GPT-6 Astra", plus 17 hours of Lean formalization. This program: one MacBook, 8-wide agents, sessions bounded by a usage cap. Nothing below assumes their scale. What transfers is the SHAPE of the search, which costs nothing to copy.

## The eight techniques the page describes, and the program's counterpart

### 1. Fan out over EVERY variant of the problem statement — proof and disproof — to separate groups.
*The page says:* "we prompted different groups of agents with different variants of the problem statement, covering all variants of the problem. For the Navier–Stokes problem, we suggested versions A and B (… a proof) and versions C and D (… a disproof) to separate groups." The win came from the DISPROOF side (C and D).
*The program today:* every direction file attacks RH as a statement to be PROVED; the barrier zoo records why proof strategies fail. There is no lane whose brief is the refutation-shaped statement.
*Transfer:* add a standing lane whose brief is the disproof shape — "produce an off-line zero, or a certified obstruction to a stated proof class" — with the same rigor. RH itself has no cheap disproof variant, but its NEIGHBORS do, and the program already touches them: the Davenport–Heilbronn counterexamples to RH for Epstein zeta functions (r3 corpus), the de Bruijn–Newman constant Λ ≥ 0 (RH is exactly Λ ≤ 0, and Λ ≥ 0 is Rodgers–Tao), the Selberg-class analogues, function-field analogues where RH is a theorem. A "C/D group" on the RH program means: for each proof-class the zoo certifies as blocked, state the obstruction as a theorem and prove it (the program's A4 no-go paper IS this, done once; make it the default output shape of a lane, not an exception).

### 2. Solve the easier neighbor first, then feed its solution to the harder problem as a prompt.
*The page says:* the "easier" problem list included Euler (viscosity removed); ~100 agents resolved unforced Euler in ~50 h; "we shifted agents away from the other Millennium Problems and prompted these agents with the Euler resolution."
*Transfer:* the program's ladder should be explicit and ordered by difficulty with the same statement shape at each rung: (i) function fields (RH known), (ii) Epstein / Davenport–Heilbronn (RH false), (iii) Selberg class degree 1 (Dirichlet L, RH open), (iv) ζ. For any new machinery (the S1–S5 specification) the brief should demand the rung-(i) and rung-(ii) versions FIRST and feed the write-ups verbatim into the rung-(iv) brief. C3-r's foliated-dynamical-system work is the one place the program has done this (function-field / mapping-torus first); make it the rule.

### 3. Diversity of approaches per group, then cross-pollination by a consolidation step.
*The page says:* "We encouraged different groups of agents to explore a diversity of approaches. After some time, we cross-pollinated the agent groups by using Codex to consolidate the most useful insights from each agent group. These follow-up prompts drew on the agents' own intermediate results."
*The program today:* streams run in parallel and are harvested by the orchestrator into STATUS/LOG; the next brief is written by the orchestrator from memory of the harvest. Cross-stream insight transfer is implicit and lossy.
*Transfer:* insert a named CONSOLIDATION agent between phases: input = every stream's intermediate results on disk; output = one "insights digest" per stream that the NEXT round's briefs must quote. This is a one-agent cost per phase and is the single cheapest thing on this list.

### 4. Reallocate the whole fleet the moment one line shows signal.
*The page says:* "Once we saw the Euler solution, we thought that Navier–Stokes was the most promising problem to work on. Thus, we decided to devote our resources to Navier–Stokes."
*Transfer:* the program runs several directions with fixed budgets per session. Add a written reallocation rule to KICKSTART: when a stream returns a result graded above a stated threshold (e.g. a new certified obstruction, or a lemma that survives two referees), the next session's full agent budget goes to that stream's follow-ups and the other lanes pause. The Lane-A / D1 queue already behaves this way informally.

### 5. Groups with internal communication, tools = cached corpus + code execution.
*The page says:* "Agents were subdivided into groups with the ability to communicate within the group … access to tools such as the ability to read from a cached version of the internet and the ability to run code."
*Transfer:* the program's Workflow scripts already give agents the local corpus and code. What it does not use is intra-group messaging: agents in one stream cannot see each other's partial results until harvest. The Workflow tool supports `pipeline()`; a shared scratch file per stream, appended to by every agent and read at every agent's start, is the poor man's group channel and costs nothing.

### 6. Upgrade the model mid-effort without restarting.
*The page says:* "When a further trained version of our internal model became available over the course of the effort, we updated our agents to that model."
*Transfer:* trivially available here (Fable 5.1 today). The lesson is the durable-state discipline that makes a mid-effort swap possible: every intermediate result on disk, briefs that a fresh agent can pick up. The program has that (RULE ONE); keep it.

### 7. Prove first, formalize second, with a weaker model, as a separate phase.
*The page says:* the analytical proof came at 88 h; "Lean formalization and verification took an additional 17 hours via GPT-6 Astra" — a lesser model than the one that found the proof. The repository ships a `ComparatorChallenges/` directory for independent proof checking.
*Transfer:* the program formalizes as it goes (grid law, Asym.lean). Keep formalization as a downstream phase with its own budget, never as a gate on exploration; and adopt an "independent checker" step — a second toolchain or a second agent that rebuilds from a clean clone and reports axioms — as the program's Comparator analogue. (What Comparator is exactly is pending the `lean-repos` report.)

### 8. Report the pace, decline the prize, publish everything.
*The page says:* proof PDF, Euler PDF, Lean repo, prompts offered to the concurrent authors; "We do not intend to claim the Millennium Prize."
*Transfer:* the program's circulation prep already follows this shape (arXiv packages, dual referees, prior-art sweeps). The one addition: publish the PROMPTS and BRIEFS alongside results. The program's briefs are already on disk; include them in the arXiv package's ancillary files.

## Two things the page does NOT say, which matter more for us
- It does not say how the agents were kept from converging on the same idea, nor how false proofs were filtered before the Lean phase. The 166-page paper's 18-page "Proof outline" (§3) is the visible artifact of that process; the `ns-paper` reader is reading it for exactly this.
- It does not say what the 9,900 agents that did NOT find the proof produced, or whether their negative results were kept. For a program whose main durable asset is a barrier zoo, that is the more important half; nothing in the release suggests they kept it.

## Concurrent human-led work (Alpöge–Buckmaster) — the other model of the same week
Two people with Claude and Codex over about a year, Lean-verified, on forced Euler / Boussinesq / porous medium. Pending the `euler-context` reader, the contrast to draw is: year-long human-steered iteration produced a proof of comparable depth with roughly four orders of magnitude fewer tokens. That is the regime this program is actually in, and it argues for investing in STEERING artifacts (direction files, briefs, the zoo) rather than in width.

## Lean-budget adoption (sponsor, 18:25 IST: "we don't have to overindex on their exact workflow … we don't have that many resources, we must be really smart about directions to pursue")

Adopted into `KICKSTART.md` Part 2 item 10 as six binding rules — (a) consolidation step between phases, (b) ladder rule for new machinery, (c) refutation-shaped output as every lane's default, (d) reallocation rule on signal, (e) shared stream scratch file, (f) formalization downstream with an independent checker — plus the explicit non-adoption of width. What the sponsor's framing changes relative to v0: the value of the OpenAI release for us is not the swarm; it is that a proof of this size was found by SEARCH SHAPE (variant fan-out, easy-neighbor-first, consolidation, reallocation), and every one of those shapes is available at width 8 as long as the state lives on disk. What "smart about directions" means concretely: the zoo's Group IV (program-discovered barriers) is the compounding asset — each session should leave it strictly larger, and a direction that cannot add to it in one session is the one to pause. (The sponsor's willingness to continue as long as needed is a constraint we are allowed to rely on, not a pace to plan for; the program never stretches to fill a horizon.)

*(v0.1; §9 "What the readers add" to follow once `ns-paper-read.md`, `euler-and-context.md`, `lean-repos.md` land.)*
