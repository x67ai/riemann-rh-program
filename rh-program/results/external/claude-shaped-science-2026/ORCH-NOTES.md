# ORCH-NOTES — the orchestrator's working notes for the Claude-shaped-science study (side-session 2026-10-03)

Working notes, written as the work goes (KICKSTART item 16 as amended: think in files). Nothing here is adopted; the study is `process-lessons.md`.

## N1 (written about 01:40 IST 2026-10-03; the stamp was typed, not read from the clock) — candidate rules, and what each still waits for

The test for every candidate, as in the Cogentic study: is the failure on THIS program's record, and is the remedy a file, a line, or one agent?

| # | candidate | from | evidence in hand | still waits for |
|---|---|---|---|---|
| u | The plan file is bounded: STATUS keeps the live state under a cap; superseded text moves verbatim to an archive in the same commit; the resume checklist is true today | P5 | complete (sizes by `git cat-file`; the queue under "SESSION 8 CLOSED"; the stale "How to resume") | — |
| v | A NUMERICAL claim ships its picture (points, law, residuals or local slope); the orchestrator's read looks at it; data words join the 10(g) lint list | P7 | complete (0 plotting calls; 76 images all scans or screenshots; digest §E l. 465–513; the Session-39 announcement and its withdrawal) | ev. A for the count of announcements corrected |
| w | "Done" is written before launch; a conditional result names its open hypothesis first and says whether that hypothesis is the hard part | P6 | STATUS l. 26: "a conditional theorem whose single missing lemma is the next session's target", then seven units and "NO upper bound on E proved"; "Lemma G is Conjecture O restated" | ev. A Table 2; ev. C (success lines in briefs) |
| x | A tools register; before a long leg, one written line on whether a tool would make it short | P2, P3 | `scripts/` has no library and no index; 779 `.py` under `results/` | ev. B1 (reuse, duplicates, bugs); ev. B2 (long legs) |
| y | Clock, not feel: stamps and effort lines come from the machine; a stream states its budget before launch | P4, P3 | the orchestrator's own stamps of this session ran 5–11 minutes ahead of the clock; the `lemmaB-s41` stop line "try to break it for an hour" gives an agent a duration it cannot measure | ev. B2 (estimates against actuals; deaths) |
| z | Significance is asked separately from novelty; who outside has read anything | P8, P9 | Cogentic study P10: "The program has no reader of that kind in its loop" | ev. D; ev. C |
| + | After a positive close, the next brief asks for the stronger statement and names what the unit restricted itself to | P10 | — | ev. C Tables 3, 4 |

## N2 — things to keep straight while writing

- The post's sentence on Millennium problems is reported once, in §0 and P12, as what the post says. Standing orders 10 and 12 fix the program's target and are the sponsor's; standing order 14 forbids ritual lines about the problem's status. The study draws only the operational part (which unit shapes the record shows closing with checked results).
- W3 applies to this note: no absolute about the record without the search that earns it. "Never drawn its data" is earned by the six-pattern grep and the listing of all image folders; say exactly that.
- The time-stamp slip of this session goes into P4 as an instance, with the LOG correction line.

## N3 (written about 01:41 IST 2026-10-03; first typed as "01:44", ahead of the clock) — candidate (u): what is live in STATUS.md, and how a split is checked

Looked at l. 56–70 and l. 112–131 (previews) and the per-section byte counts.

| block of `STATUS.md` | bytes | live or history |
|---|---|---|
| l. 1–25 title, files and roles, session discipline | ~4 k | live |
| l. 26 header: the newest state | first ~2 k of 27 k | live; the "Previous:" chain is history |
| l. 28–52 standing orders 0–14, the resume-point line | ~17 k | live |
| l. 56–69 "Program plan (phases)" — the August phases 1–5, the Grossmann sweep | 16 k | history (one pointer line stays) |
| Key artifacts; Hard constraints; S1–S5 specification | ~5 k | live ("reuse in every future brief") |
| Verified numerics; Designer briefs | ~3 k | history |
| l. 112–123 the Session 19 / 18 / 7 / 8 blocks | ~7 k | history |
| l. 124–130 SESSION 42 QUEUE | ~11 k | live |
| l. 132–400 the superseded queues, Sessions 41 → 9 | ~225 k | history |
| "Live/completed background tasks": entries in flight | varies | live |
| the same section: completed entries | ~257 k | history |
| "How to resume" | 2 k | to be REWRITTEN (it describes August's phases 3–5) |
| "Findings log (append-only)" | 2 k | to look at before deciding |

So the live core is of the order of 45–50 kB against 578 kB. The queue's own item 4 (l. 129) already lists "STATUS housekeeping (move the older 'Previous:' header entries and …" as small bookkeeping: the trim is re-listed by hand each time, no rule repeats it.

**How a split is made checkable.** One script, kept under `rh-program/scripts/`: it takes the line ranges that are history, appends them VERBATIM to `rh-program/STATUS-ARCHIVE.md` under a dated heading, removes them from `STATUS.md`, and cuts the header line at its first "Previous:" (the tail goes to the archive). Check, by the script itself: the multiset of lines of the old file equals the multiset of lines of the new file plus the lines appended to the archive, except for (a) the header line, where old = kept part + moved part as strings, and (b) lines the script itself writes (pointer lines, the new resume checklist), which it lists. Nothing is restated. The SHA-256 of the old file and of both new files goes into LOG.

**Order.** Nothing is moved before the study has had its Opus read and rule (u) stands. If it stands, the first split is done in this side-session, so that Session 42 boots from the short file.

## N4 (01:42 IST 2026-10-03, from `date`) — the stamp slip happened twice

The LOG correction of 01:36 said that stamps would come from `date`. Five minutes later N1 and N3 of this file were stamped by hand again, and N3's stamp was three minutes in the future. An intention to use the clock did not hold; what holds is a stamp produced by the command that writes the line (as this one is). This goes into P4 as the session's own instance, and into the wording of any rule there: the stamp is generated, never typed.

## N5 (01:42 IST 2026-10-03, from `date`) — cut points for the split, by anchor

- Header line (starts `**Started:**`): keep up to the first " Previous: **Last updated:**"; the tail is history.
- Section under the heading "## SESSION 8 CLOSED …": the live queue is the block from the first line starting `**SESSION nn QUEUE` to the line before the next such line (today l. 124–130, SESSION 42 QUEUE); the rest (the superseded queues, Sessions 41 → 9) is history.
- "Live/completed background tasks" (l. 401–617, 165 entries, newest first): the live queue item 0 names Session 41 entries as the ones to harvest, so entries of the newest session and the side-sessions stay (today l. 403–425); from the first entry of an older session (today l. 427, Session 40) everything is history.
- "Findings log (append-only)": three lines of August 2026 (last 13 Aug) — history, with a pointer.
- "Program plan (phases)", "Verified numerics", "Designer briefs", the Session 19 / 18 / 7 blocks: history, with a pointer.
- "How to resume": the old text is history; the new text is written by the orchestrator in a separate file and inserted by the script, listed as written.

## N6 (01:43 IST 2026-10-03, from `date`) — the split script, dry run

`scripts/status-split.py` written (dry run by default; `--apply` writes). Dry run on the current file: 578,150 bytes / 636 lines → 57,648 bytes / 148 lines kept; 522 kB in 11 blocks to the archive (header chain 26 kB; superseded queues 225 kB; completed task entries 245 kB; the August phase plan 16 kB; the rest small); 21 lines written by the script (pointers, one heading); CHECK PASS (multisets of lines; the header as kept + moved = old). With `--resume NEW-RESUME.md` the stale checklist is replaced by a seven-step one that is true today (drafted beside this file). Nothing applied: it waits for the read of the study.

## N7 (01:54 IST 2026-10-03, by `scripts/stamp.py`) — the stamp helper, tested on this session

`scripts/stamp.py` written: prints the clock stamp; `--fill FILE` replaces the placeholder in a brief or header; `--append FILE TEXT` appends a stamped line; `--check REV` fails if a stamp in a line added since REV is later than the commit that introduced it. Run on this session's commits (`--check c6fd319a`): 20 stamps of the day in added lines, 5 ahead of their commit — exactly the orchestrator's hand-typed ones (01:40 ×3 in lines committed 01:34; 01:46 in a line committed 01:36; 01:44 in a line committed 01:41). Exit 1. So the check catches the slip the record names in eleven sessions; it waits for the read of the study before it is made a rule.

## N8 (02:03 IST 2026-10-03, by `scripts/stamp.py`) — the plotting helper, tested on nine points from the record

`scripts/plot_claim.py` written (two panels: the points with candidate laws on log-log axes; the local slope between consecutive points with the slope each law has there). Test: the nine running-sup values of S8(π/4) at x = 10³ … 10¹¹ (`results/free-greedy-s40/compute/NOTE.md` l. 11), with 0.2·log²x and two power laws through the first point; picture `figures/s8-pi4-supE.png` (local; the CSV beside it is tracked). What the orchestrator sees in it: the local slope runs 0.21, 0.30, 0.17, 0.08, 0.30, 0.00, 0.07, 0.04 — no horizontal line, so no single power law; the running sup moves in steps (flat from 10⁸ to 10⁹, a jump from 10⁷ to 10⁸), so eight slopes cannot tell a slowly falling curve from scatter; x^0.25 through the first point is far above the last points, x^0.15 meets the last point and misses the middle. That is what the Session-41 reader had to write out ("β = 0, no power law fits" cut back to "β < ¼ on the observed range"); the picture puts it in front of the writer first. It proves nothing and decides no rule; it shows the helper does its job.

## N9 (02:05 IST 2026-10-03, by `scripts/stamp.py`) — the brief checker, tested on three files

`scripts/check-brief.py` written: it checks that a charter or brief HAS the lines the manual says it is returned without — the pointer to BRIEF-WARNINGS (10(p)), a SOURCES.md beside a charter (10(s)), the stop line (10(m)), a bearing line (10(g) as rule (z) would amend it), the output clause (item 16; unit and reader briefs), a filled stamp and no duration of effort (rule (w)); a line "WAIVED name: reason" turns a check off. It checks presence, not truth. Tests: `results/lemmaB-s41/CHARTER.md` fails four (no pointer, no SOURCES.md, no bearing line — all three rules postdate it — and "try to break it for an hour"); `results/free-greedy-s40/theory/BRIEF.md` fails two (pointer, bearing); this session's `READ-BRIEF-O.md` passes. Staged; nothing adopted.
