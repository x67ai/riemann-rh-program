# Brief warnings — the kinds of error that repeat, one line for writers and one for readers

**What this file is.** The standing list that KICKSTART Part 2 item 10(p) requires: every kind of error that the reads have caught in two or more units, turned into one line a WRITER follows and one line a READER checks. Every charter's rules and every reader brief open with "read `BRIEF-WARNINGS.md` first". It is a list of habits, not of mathematics: nothing here says what is true or which route to take.

**Who writes it.** At each reconciliation the orchestrator tags every upheld FIX-FIRST with its kind; the reconciliation that brings a kind to two units enters its line here, with the evidence (read file and item, or digest section) and the waves in which it fired. The consolidation digest (10(a), 10(p)) reconciles the file: it adds the waves in which each line fired and proposes new lines. At most FORTY live lines; a line that no read has fired in three consecutive waves moves to "History" at the foot of the file with the date. A kind seen in one unit only is not a line yet.

**Seeded 2026-10-03 (side-session; source: `results/external/cogentic-2026/process-lessons.md` P6, P1, dual-read).** Evidence abbreviations: "w3 §E.x" = `results/novel-wave-s39/insights-digest.md` §E item x (the wave-3 digest); "s41" = the reads of the stream `results/lemmaB-s41/`.

## Live lines

**W1 — A printed core missed.**
- WRITER: before any label "new", open the papers your stream's `SOURCES.md` names (10(s)) and search the on-disk corpus (`fetched*/`, `sources-extracted/`, every `results/*/sources/`) for the statement's objects; when a core is found the label is "new as a statement on a printed core: <paper, page>".
- READER: for every result labeled new, open the papers of `SOURCES.md` at the page before searching anywhere else.
- Evidence: on disk and missed in five cases — w3 §E.1 F2, §E.4 F5, §E.6 F2 (Hilberdink 2012, three units of one wave), §E.10 F2 (Olofsson 2010), s41 `U3-firstbound/read-F.md` (Diamond–Zhang 2016 Thm 6.13, on disk since Session 39 under `results/dz-half-s39/sources/`); in print in two more — w3 R4 (Bateman–Grosswald 1964), s41 `U5-obstruction/read-O.md` F7 (Hilberdink 2011). Fired: waves 3, 4.

**W2 — A fit stated as an exponent, or a finite scan stated as a fact about the limit object.**
- WRITER: a slope fitted on [a, b] is reported as "slope on [a, b]", never as an exponent; a computation at finite X is a statement about the truncation at X, never about the limit object; no close and no stop line rests on a fit (10(r)).
- READER: for every exponent or asymptotic claim, find its proof; where there is none, the claim is rewritten as a range statement (FIX-FIRST).
- Evidence: w3 §E.3 (rF F1 = rO F1 …: "β ≈ 0.30" is a slope on [10³, 10⁹]), §E.2 F4, §E.9 F2, §E.11 F1, §E.12 (a brief's stop trigger accepted a pre-asymptotic fit); the Session-39 numerical counterexample, withdrawn in Session 40. Fired: wave 3.

**W3 — A label stronger than the check behind it.**
- WRITER: "certified", "proved", "unconditional", "exact", and absolutes such as "nothing", "every", "never", are written only where the check that earns the word is on disk and named in the same sentence (the script and its log; the proof; the full list of inputs; the search that was run).
- READER: for each such word, open the named check; where it establishes less than the word says, FIX-FIRST.
- Evidence: w3 §E.9 F1 ("certified" on an error bound the code never proves), §E.4 F1 ("uncond."), §E.8 F2 (an audit that omitted one of two decision classes), §E.10 F1 (a headline asserting a barrier the NOTE lists as open); `results/external/cogentic-2026/read-O.md` F4, F6, F12 (three absolutes about the record that the record contradicts). Fired: wave 3; the side-session of 2026-10-03.

**W4 — A printed theorem applied without checking its hypotheses for the object.**
- WRITER: when a printed theorem is applied to one of the program's objects, list its hypotheses and verify each one for that object in the text; a hypothesis that is itself the open statement is named as such.
- READER: open the theorem at the page and test each hypothesis against the object.
- Evidence: w3 §E.11 F2 (Axiom A is the open hypothesis), §E.6 F5; s41 `U5-obstruction/read-O.md` F5–F6 (a localization that uses ζ ≠ 0 on Re s ≥ 1). Fired: waves 3, 4.

**W5 — The record left inconsistent after corrections.**
- ORCHESTRATOR / APPLIER: after applying pairs, compare the script's printed count with the reads' totals; a corrected block occurs once; every label the reads changed (novelty labels, producer counts, "unrefuted") is searched for in the NOTE and brought into line — and once the unit's rows are in `THEOREM-LEDGER.md`, the row is the record of status, not the NOTE's label.
- READER (digest): list as residues every label in a NOTE that disagrees with the read that closed it.
- Evidence: w3 §E R1 (a corrected block five times, a sentence cut), R2, R4 (stale novelty labels), R3 (record lag), R5, R6 (stale producer counts). Fired: wave 3.

**W6 — Mathematics in a brief or charter that the units had to correct.**
- ORCHESTRATOR: every identity, dichotomy, lemma or expectation of your own in a charter stands under a heading that marks it unverified; stop lines carry none of it and never trigger on a fit (10(r)).
- WRITER: treat the charter's mathematics as claims; the first one you cannot confirm goes into `SHARED.md` at once, before you build on it.
- Evidence: w3 §E.12 (five errors caught by units, and a stop trigger caught only by the reads); the errata sections of the wave-1 and wave-2 digests (`results/novel-wave-s36/insights-digest.md` §E, `results/novel-wave-s37/insights-digest.md` §E) list the charter errors their units caught. Fired: waves 1, 2, 3.

## History (retired lines, with dates)

(none)
