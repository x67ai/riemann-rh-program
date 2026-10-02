# READ-BRIEF-O — the second read of the Claude-shaped-science study

**Written 02:01 IST 2026-10-03 (orchestrator Fable 5.1; stamp filled by `scripts/stamp.py`). Reader: one Opus agent, default effort (standing order 11).** Deliverable: `rh-program/results/external/claude-shaped-science-2026/read-O.md`.

Repository root (the path contains a SPACE — quote every path): `/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann`. Study folder: `rh-program/results/external/claude-shaped-science-2026/`.

## What you are reading

A process study, not mathematics. The program's sponsor asked whether a guest post on Anthropic's research pages (M. Schwartz, "Claude-shaped science", 1 Oct 2026) has anything to teach about HOW this program is run. The orchestrator wrote `process-lessons.md`: twelve practices of the post (P1–P12), each set against the program's own record, and six proposed rules (§A, letters (u)–(z)) that are NOT yet applied. Your read decides what is adopted. Nothing in this study is to be judged on the program's mathematics.

## Rules

1. Read `rh-program/BRIEF-WARNINGS.md` first. Kind W3 (a label stronger than the check behind it) is the kind a study like this commits: the previous study's first version carried three absolutes about the record that the record contradicted.
2. Labels in the study are claims to test, not facts. Every quotation is wrong until you have found it; every count is wrong until you have recounted it.
3. Private correspondence — anything under a `correspondence/` folder, any e-mail from a person outside the program — is NEVER quoted verbatim in your file: paraphrase and cite file and line. The program's own summary lines in tracked files may be quoted.
4. Long lines: `rh-program/LOG.md` and `rh-program/STATUS.md` have single lines of up to 27 kB. Never `cat` them or Read them whole; use short Python windows (the local `grep` is ugrep and rejects long `.{0,N}` windows).
5. Read-only: you write ONLY `read-O.md` (and may append dated blocks to the folder's `SHARED.md`). No git command that changes state; do not launch agents; do not run the program's research code. You MAY run `rh-program/scripts/status-split.py` WITHOUT `--apply` (a dry run that writes nothing) and `rh-program/scripts/stamp.py --check c6fd319a` to test the two scripts the study relies on.
6. U.S. English. Time stamps in your file come from `date '+%H:%M IST %Y-%m-%d'`, never from estimate.

## The read, in this order

**Step 1 — BLIND PASS, before you open `process-lessons.md` or anything under `evidence/`.** Read the post (`page.txt` in the study folder; about 4,700 words; local-only, do not copy it into your file beyond short quotations). Read `rh-program/KICKSTART.md` Part 2 (item 10 in full) and the standing orders in `rh-program/STATUS.md` l. 28–52. Then write into `read-O.md` your own table: every practice, tip or failure mode of the post that bears on how a research program is run | already in the program's rules? (cite the rule) | if not, does the program's record show the failure it prevents? (say where you would look) | your verdict: transfer / already ours / does not transfer. Write this table BEFORE you read the study, and say in the file that you did.

**Step 2 — every quotation from the post.** For each passage the study puts in quotation marks and attributes to the post (the tags [I], [W], [K], [T], [O]), find it in `page.txt`. Report every mismatch, and every place where the study's own wording misstates what the post says or leaves out something the post says that changes the lesson (in particular §0's "What the post does not contain" and the block P12).

**Step 3 — every citation of the record.** The study cites the record in two ways: directly (file and line) and through the five evidence files (`evidence/A…D`, written by five Opus readers; "ev. C Table 2"). (a) Check EVERY direct citation at the line. (b) For each number the study takes from an evidence file (for example: 43 corrections and 28 that held; 32 of 43 caught by read-O; 0 of 29 briefs naming a clause; 18 of 29 follow-ups; 11 generator programs; eleven sessions of estimated stamps; 7 of 12 estimates overstated; one human outside reader), open the evidence file, see whether the table supports the number, and re-derive at least THREE rows of each evidence file from the record itself, chosen by you. Report what you sampled. An evidence file that fails your sample is a FIX-FIRST against every block that leans on it.

**Step 4 — each "Already adopted here?" verdict.** For each of P1–P12: is the verdict right? Does the record hold a practice, a rule or a counter-example the study missed? Is any "the record shows" stronger than what the record shows? Three verdicts deserve particular suspicion: P3 (that the record shows no grinding), P7 ("the program has never drawn its own data"), P8 (that no step asks whether a result matters).

**Step 5 — the rules (u)–(z) of §A.** For each: ADOPT AS WRITTEN / AMEND (give the amended text) / DECLINE (give the reason). Hold each to the standard of the earlier studies: a rule is adopted only if the failure it answers is on THIS program's record, and if its cost is a file, a line, a script or one agent. Say plainly where a rule is forced, where it duplicates an existing rule (10(a)–(t), items 1–18, the standing orders), where it conflicts with a standing order, and where a rule that the study proposes as text would be better as a script or a file shape — or the reverse. Test the two scripts as rule 5 allows and report what they print. Six new rules in a manual that already has twenty lettered ones is itself a cost: say which of the six you would drop first, and whether any two should be one.

**Step 6 — what the study does not say.** Practices of the post the study missed; refusals (§C) that are wrong; anything in §D or §E that overstates; and whether the study's account of this session's own two slips (hand-typed time stamps; a private e-mail quoted into tracked files by an evidence reader, `LOG.md` entries of 01:36 and 01:49–01:51 IST 2026-10-03) is accurate.

## Shape of `read-O.md`

Verdict line at the top (AGREES / AGREES-WITH-CORRECTIONS / DISAGREES). Then the blind table; then findings numbered F1, F2, … each marked FIX-FIRST (the study says something the source contradicts, or a rule rests on it) or minor, each with its evidence at the line and an OLD/NEW pair that can be applied by exact string replacement (OLD must occur exactly once in `process-lessons.md`); then the rule verdicts table; then "What I could not check".

HARD OUTPUT RULE: never write more than about 6 kB of text in a single response or tool call. Build every deliverable incrementally on disk — create the file, then append one section (or five table rows) at a time — and append a dated block to SHARED.md after each batch. Keep reasoning between tool calls short; think in the files, not in long messages. Your final report is under 60 lines.

Your FIRST tool call after reading the warnings creates `read-O.md` with a plan of at most 20 lines.
