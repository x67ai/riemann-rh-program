# BRIEFS — evidence readers for the "Claude-shaped science" study (side-session 2026-10-03)

Five evidence questions, one Opus agent each (default effort, standing order 11). The agents report FACTS FROM THE PROGRAM'S OWN RECORD; the orchestrator writes the study (`process-lessons.md`) from them and from its own reads. If the session dies: any evidence file missing or unfinished under `evidence/` is relaunched from its section here with "resume from your deliverable file and SHARED.md".

## Common rules (every agent)

Repository root (the path contains a SPACE — quote every path in every shell command):
`/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann`
Program directory: `rh-program/` under it. Study folder: `rh-program/results/external/claude-shaped-science-2026/`.

1. Read `rh-program/BRIEF-WARNINGS.md` first. Its kind "a label stronger than the check behind it" applies to you: state nothing about the record that you have not seen at the line.
2. What this is. The orchestrator is studying a blog post about running research with AI agents. For each failure mode the post describes, it needs to know whether THIS program's record shows it. You answer one evidence question. You do not recommend rules, you do not judge the mathematics, and you do not need the post.
3. Citations. Every table row cites file and line (for example `rh-program/LOG.md` l. 2212) and quotes the deciding words verbatim, at most about 40 words per quote. No paraphrase stands without its quote. If you did not find something, write "not found in <scope searched, patterns used>", never "there is none".
4. Long lines. `rh-program/LOG.md` (808 kB, 2309 lines) and `rh-program/STATUS.md` (576 kB) have single lines of up to 26 kB. Never `cat` them and never Read them whole. Work in windows: `grep -n -o -E ".{0,200}PATTERN.{0,300}" FILE`, `awk 'NR==N' FILE | cut -c A-B`, or a short Python snippet. STATUS.md l. 26 is the header chain (the current state, then "Previous:" entries back to Session 32); LOG.md l. 1922–1988 holds the older header chain; LOG session entries: Session 36 starts at l. 2061, Session 41 closes at l. 2272–2288.
5. Read-only. You write ONLY your deliverable file and your blocks in `SHARED.md` of the study folder. Do not edit, move or delete anything else; no git command that changes state; do not launch agents; no heavy computation (reading, grep, `shasum`, `wc` only).
6. U.S. English.
7. HARD OUTPUT RULE: never write more than about 6 kB of text in a single response or tool call. Build every deliverable incrementally on disk — create the file, then append one section (or five table rows) at a time — and append a dated block to SHARED.md after each batch. Keep reasoning between tool calls short; think in the files, not in long messages. Your final report is under 60 lines.
8. Your FIRST tool call after reading the warnings creates the deliverable file with a plan of at most 20 lines.
9. Final message (under 60 lines): the deliverable's path, the row counts per table, the three most important findings with their citations, and what you could not check.

## A — Closes and their corrections

**Question.** Which results did the program announce with a positive label and later withdraw, narrow, downgrade or relabel? And which results announced as "conditional on one missing lemma" had a missing lemma that later proved to be the hard part, false, or a restatement of the target?

**Scope.** Sessions 36–41 at full resolution: `rh-program/LOG.md` l. 2061–2309; `rh-program/STATUS.md` l. 26; the wave digests `rh-program/results/novel-wave-s36/insights-digest.md`, `…/novel-wave-s37/insights-digest.md`, `…/novel-wave-s39/insights-digest.md` (their §E errata); every `read-O.md` and `read-F.md` under `rh-program/results/` in folders of Sessions 36–41. Earlier sessions at lower resolution: grep LOG.md for `WITHDRAWN|withdrawn|retracted|RETRACTED|narrowed|relabel|pre-empted|downgrad|demoted|record correction|repair`.

**Starting points to verify at the line (the list may be incomplete or wrong; find the rest):** Session 39 "A NUMERICAL COUNTEREXAMPLE TO CONJECTURE U", withdrawn in Session 40; `conj-O-s38` "Lemma G the exact missing lemma" (Session 38), then "Lemma G is Conjecture O restated" and "Conjecture O FALSE AT RUNG 1" (Session 39); Theorem 1.6, "a conditional theorem whose single missing lemma is the next session's target" (Session 40), then seven units on Lemma B_ρ and "NO upper bound on E proved" (Session 41); "β = 0" narrowed to "β < ¼ on the observed range"; novelty relabels (Theorem 1.6 "new as a statement on a printed core"; T1's core in Olofsson 2010; the seed no-go's Theorems 1–3 = Winkelmann 2002; "(T1) unrecorded" = Bertrand 1997); Session 7's "C3-r FULLY CLOSED" and the later repairs of the alkl23 note (Sessions 14–17).

**Deliverable** `evidence/A-closes-and-corrections.md`:
- Table 1 "Announced, then corrected": # | session announced | the announcement (verbatim, file:line) | label used (CLOSED, PROVED, COUNTEREXAMPLE, NEW, CERTIFIED, …) | the qualifier attached at announcement, if any (verbatim, for example "certification is the next session's first unit", "single-check", "interim numbers") | session corrected | the correction (verbatim, file:line) | caught by (read-F / read-O / a later unit / the orchestrator's recount / a referee agent / the sponsor) | kind (withdrawn / narrowed / novelty relabeled / hypothesis found false / record defect).
- Table 2 "Conditional results and their missing piece": # | the conditional statement as announced (verbatim, file:line) | the missing hypothesis | what the record later shows about it (proved / refuted / a restatement of the target / still open after N units), with citations | units and sessions spent on it after the announcement.
- Table 3 "Announcements that held" (the denominator): positive announcements of Sessions 36–41 that passed their later checks unchanged; one citation each.
- "Counts": totals per table; for Table 1, the split by who caught it and by lag in sessions.
- "Wording at announcement": for each Table 1 row, was the open part (unverified, single-check, numerical only) stated in the same sentence as the claim, later in the same paragraph, or not at all? One word per row and the quote.

## B1 — Tools inventory

**Question.** What reusable computational tools has the program built, where do they live, and how often did a later unit REUSE an earlier unit's code rather than write its own?

**Scope.** All code under `rh-program/results/` (about 779 `.py`, 57 `.c`, 128 `.sh`, 55 `.lean` outside `.lake`, 3 `.rs`, 1 `.go`) and `rh-program/scripts/`. Method: list code files with sizes by folder; read the first 30 lines of each `.py`/`.c` (docstring, header comment) to classify by FUNCTION and by ROLE — WRITER (a unit's own producer), READER (an independent re-run written by a `read-O`, `read-F` or checker agent; by this program's rules a reader must not import the unit's scripts, so reader duplicates are by design and are counted separately), INFRA (zoo insertion, record editing, linting, packaging).

**Function classes to look for (add the ones you find):** generators of Beurling / greedy g-prime systems (S5, S8, necklaces, random Diamond–Zhang systems); counting functions N(x) and the integer error E(x); zeta / L-function values and zeros (mpmath, Arb, python-flint); interval-arithmetic certificate producers and checkers; explicit-formula or Weil-functional evaluators; fits, regressions, exponent estimates; sieves and prime tables; Lean build and axiom-print scripts; PDF / OCR / text-extraction helpers; linters and apply-pairs tools.

**Reuse.** grep imports across unit folders (`sys.path`, an `import` of a module that lives in another results folder, a `cp` of a script); compute `shasum -a 256` over all code files and report groups of identical files in different folders; grep NOTE files and briefs for "reused", "reuses", "adapted from", "from results/".

**Recorded tool bugs.** grep LOG.md, the digests' §E and the read-O files for `bug|float|drift|block-edge|off-by-one|overflow|precision loss|wrong window`: tool, unit, what the bug changed, who caught it.

**Index.** Is there any index, manual or register of tools (a README or INDEX, a section of STATUS.md "Key artifacts", Instruments tables in `rh-program/directions/*.md` that name code)? Report what exists.

**Deliverable** `evidence/B1-tools-inventory.md`:
- Table 1, per function class: class | writer implementations (count; folders) | reader/checker implementations (count) | languages | the most validated one, if the record says what it was validated against | reused by a later unit? (which; by import, by copy, or rewritten).
- Table 2: duplicate-hash groups.
- Table 3: recorded tool bugs.
- "Index or manual": what exists.
- "Counts": code files by role; function classes with three or more WRITER implementations; cross-unit imports found.

## B2 — Time, grind, estimates

**Question.** What does the record show about (a) long computations, and whether a better tool or algorithm replaced grinding; (b) estimates made in advance against the actuals; (c) work the record itself calls wasted; (d) deaths at usage or output limits?

**Scope.** `rh-program/LOG.md`, all sessions, grep-driven; `rh-program/STATUS.md` "Live/completed background tasks" (from l. 401); `rh-program/directions/*.md` (Instruments tables, work logs); `rh-program/results/d1-m2a/`, `results/d1-m3/`, `results/c2-m2/campaign/`, `results/free-greedy-s40/compute/`, `results/lemmaB-s41/U7-patterns/`; Colab / GPU notes (grep `Colab|T4|GPU`). Patterns: `h wall|hours| min[ ,;)]|tokens|priced|slots|overstated|understated|estimate|feasib|rate|speed-?up|faster|rewrote|vectoriz|ported to C|Spent for nothing|usage|128k|ceiling|died|relaunch`.

**Deliverable** `evidence/B2-time-grind-estimates.md`:
- Table 1 "Long compute legs" (30 minutes of wall time or more, or called heavy): leg | session | what was computed | wall time (verbatim) | algorithm or tool change before or during the leg (verbatim; the speed-up if stated) | was a smaller dress rehearsal run first (KICKSTART 10(l))? | the later use of the result.
- Table 2 "Estimate against actual": every place the record prices or estimates in advance (time, slots, tokens, data cost, feasibility) and later records the actual: the estimate (verbatim) | the actual (verbatim) | direction and ratio.
- Table 3 "Waste lines": every "Spent for nothing" line of LOG.md (trimmed to 60 words), its session, its cause label.
- Table 4 "Deaths and walls": usage-limit deaths, output-ceiling deaths, sleep deaths: date and session | what died | what was lost | the rule that followed.
- Table 5 "Sessions 19–41": session | wall time | context % at close | agents launched | tokens where recorded (from the session headings and closing entries).
- "Counts and medians": run minutes and tokens by kind of agent (writer unit / reader / digest / zoo / Lean), from the entries that record them.

## C — The units of Sessions 36–41: source, link, shape, close

**Question.** For every research unit launched in Sessions 36–41, where did the idea come from, what did its brief say about how the unit bears on the program's main target, what shape was its deliverable, and how did it close after the reads?

**Scope.** `rh-program/results/novel-wave-s36/` (WAVE-CHARTER.md, units N1–N4, insights-digest.md); wave 2 `results/novel-wave-s37/` (M1a, M1b, M2); wave 3 `results/novel-wave-s39/` and the units `u-offsurgery-s39`, `lemmaG-s39`, `dz-half-s39`, `qtwin-s39`, `fejer-form-s39`; Session 38 `qcond-s38`, `conj-O-s38`; Session 40 `free-greedy-s40/theory`, `free-greedy-s40/compute`, `s5-multiplicity-s40`, `local-greedy-s40`; Session 41 `results/lemmaB-s41/` (CHARTER.md, U1–U7, ORCH-NOTES.md); `haglund-cert-s37`, `d4-infty-s36`, `theoremR-lean-s36`, `beta-shapes-s35`; the SESSION 37–42 QUEUE texts in STATUS.md (grep `SESSION (3[6-9]|4[0-2]) QUEUE`); LOG.md l. 2061–2288. Folder names may differ slightly: `ls rh-program/results | grep -E "s3[5-9]|s4[01]"` first.

**Deliverable** `evidence/C-units-s36-s41.md`:
- Table 1, one row per unit: unit | session | idea source, verbatim from the charter, brief or queue (the orchestrator's construction / a digest's ranking, with its § / a published conjecture or paper / the sponsor) | the brief's statement of how the unit bears on the program's contract theorem or target (verbatim, or "none found in <file>") — KICKSTART 10(g) requires every brief to name the contract clause it discharges: does this one? (yes, with the quote / no) | origin of the target: a PUBLISHED object (cite) or the PROGRAM'S OWN object (for example Conjecture U, Conjecture O, S5, S8) | deliverable shape, one of: certificate or exact computation checkable by a rerun; Lean-checked; proof in prose; construction; numerical exploration or pattern search; literature pricing or partition | close label as the record uses it (T / K / G / N; verbatim) | novelty label after the reads (verbatim) | the stop condition as written in the brief (verbatim) | the success criterion as written in the brief, if any (verbatim, or "none found").
- Table 2, tallies: deliverable shape × close label; target origin × close label; idea source × close label; the count of briefs that name a contract clause; the count that state a success criterion in advance.
- Table 3 "Follow-ups": for each unit that closed with a positive result, what the next queue funded after it (verbatim): the same result strengthened, generalized to a next class, a different question, or nothing.
- Table 4 "Narrowing found by a read": cases where a read or a digest says the unit proved or computed less than its brief asked, or a special case of it (grep the read-O files and digests for `restricted|only for|special case|narrow|weaker than|not the brief`), with quotes.

## D — Outside readers and significance

**Question.** What has the program sent outside, which humans other than the sponsor have read any of it, and how does the record judge whether a result MATTERS — as distinct from whether it is correct or new?

**Scope.** `rh-program/CIRCULATION-PREP.md`; `rh-program/results/arxiv/` (README.md, POSTING.md, DE-INTERNALIZATION.md, referee reports); `public/`, `README.md`, `CITATION.cff` at the repository root; `rh-program/results/x67-landing-s41/`; `rh-program/results/external/prove2me/NOTE.md`; LOG.md and STATUS.md by grep: `circulat|arXiv|endors|Zenodo|DOI|x67|e-?mail|wrote to|repl(y|ied)|referee|expert|mathematician|courtesy note|alkl23|Lamzouri|sponsor's decision|prove2me`. For ranking: the digests `rh-program/results/*/insights-digest.md` and the queue texts — sections named "survivor filter", "merit", "ranking", "funding". For results that were correct but already known: `pre-empted|printed core|in print since|folklore|well known|standard|trivial|of no interest`.

**Deliverable** `evidence/D-outside-readers-significance.md`:
- Table 1 "What went out": item | date and session | where (a Zenodo DOI, the x67.ai page, GitHub, arXiv, e-mail) | who decided (the sponsor / the program) | citation.
- Table 2 "Human readers": every instance of a human other than the sponsor reading, answering, or being sent program output — or "not found", with the scope searched. Include courtesy notes that were prepared, and say for each whether the record shows it SENT or not sent, with the line.
- Table 3 "Agent referees": which outgoing texts had a blind referee agent, and the verdicts.
- Table 4 "Ranking criteria as written": digest or queue | the criteria, verbatim.
- Table 5 "Correct but known": unit | what was found in print | who found it (the writer / read-F / read-O / a digest) | how the label changed.
- One paragraph: does any step on the record ask "would a specialist in this object care about this result, and what would they ask instead?" Quote it if it exists; otherwise "not found", with the patterns searched.
