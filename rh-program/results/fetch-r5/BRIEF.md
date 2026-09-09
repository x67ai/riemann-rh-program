# Round-5 fetch ingest — agent brief (Session 20, 2026-09-10)

**Scope (Session 20 queue item 0, modeled on the Session-18 ingest `results/fetch-r4/BRIEF.md`):** verify each sponsor-delivered file in `fetched-r5/` against its citation in `FETCH-LIST-ROUND5.md` (standing order 5), extract the specific thing the list says the program needs from it, and record it durably. This is an INGEST: no new mathematics, no verdict changes, no edits to direction files, adjudications, the ledger or the zoo. If a source contradicts something the program has on record, WRITE THAT DOWN in your report with page references — do not fix the record yourself. The Q-S4⁗ verdict (`results/c3-r/s19/qs4quad/adjudication.md` §0, §6) stands whatever you find: rows 1–2 cannot flip face (b) (Warsaw 2002 postdates them and prints "unknown in general"); rows 3 / 7b could at most NAME branch (P∞). Say so plainly if you find something that looks decisive — it goes to the next program stream, not into the record by your hand.

**Files:** `fetched-r5/` (gitignored, local-only; 13 files). Filenames start with `r5-<list row>`. Never commit a PDF. Page counts and text-layer health as measured by the orchestrator (chars = `pdftotext` of pp. 1–3):

| id | file | PDF pages | text layer |
|---|---|---|---|
| r5-01 | Cantwell–Conlon 1989, Publ. Mat. 33, Markov LMS | 24 | present |
| r5-02 | Cantwell–Conlon 1988, Tôhoku 40, Foliations and subshifts | 24 | present |
| r5-03 | Cantwell–Conlon 1981, TAMS 265, Poincaré–Bendixson theory | 29 | present |
| r5-04 | Cantwell–Conlon 1998, CMH 73, Generic leaves | 31 | present |
| r5-05 | Dippolito 1978, Annals 107 (JSTOR) | 52 | present (JSTOR scan — verify by vision) |
| r5-06 | Cantwell–Conlon 1987, Topology 26, Every surface is a leaf | 21 | present |
| r5-07 | *A Fête of Topology* (Academic Press 1988), WHOLE VOLUME; Inaba's article printed pp. 95–100 ≈ PDF 101–106 (Nishimori's article starts PDF 107) | 588 | present but thin — verify by vision |
| r5-07b | Contemp. Math. 70 (AMS 1988), WHOLE VOLUME, **IMAGE-ONLY**; *The theory of levels* begins PDF p. 12 = printed p. 1 (vision-confirmed by the orchestrator) | 334 | none — vision only |
| r5-07c | Cantwell–Conlon 1982, TAMS 269, Nonexponential leaves at finite level | 25 | present |
| r5-08 | Schweitzer 1978, LNM 652, Some problems in foliation theory | 13 | present |
| r5-09 | Cantwell–Conlon 1982, Topology 21, Endsets of leaves | 20 | present |
| r5-10 | Cantwell–Conlon 1983, Math. Ann. 265, Analytic foliations and the theory of levels (the sponsor's find for row 10) | 9 | present |
| r5-11 | Cass 1985, TAMS 287 (JSTOR), Minimal leaves in foliations | 14 | present (JSTOR scan — verify by vision) |

**Ground rules (corpus-routing.md caveats 1–3, binding):**
1. **No third-party OCR, ever.** Image-only or scanned pages are read by rendering them and reading them with your own vision: `pdftoppm -r 110 -f N -l M -png "<file>" <scratch>/pg` then the Read tool on the PNGs. Use text layers where they exist (`pdftotext -f N -l M "<file>" -`), but **verify any formula-critical quotation by vision** — text layers garble math (script letters, bars, subscripts).
2. **Locate before you read.** For a volume, find the article's PDF page range first (table of contents / grep / vision) and record the PDF-page ↔ printed-folio offset in your report. For every file record the offset.
3. **Quote exactly.** Where the list asks for an exact statement (a theorem, a definition, a hypothesis), transcribe it verbatim with the printed page and the theorem/definition number. Mark anything you could not read with [illegible]. Never paraphrase a hypothesis.
4. **Write to disk as you go.** Your deliverable is `results/fetch-r5/<your-id>.md`. Create it at the start with a header and the file list, then append sections as you finish each file. An auto-commit watchdog commits every ten minutes; the session can die at any moment, and what is on disk is what survives.
5. **Read the "where it was flagged" pointer first.** Each row of `FETCH-LIST-ROUND5.md` names the scout section that asked for it (`results/c3-r/s19/qs4quad/scout-O.md`, `scout-F.md`) and the adjudication (`adjudication.md`, esp. §2, §3, §6). Read that passage so you answer the question that was actually asked, then answer it from the source. The contract objects (D1)–(D6) and the Warsaw pp. 225–227 statements are quoted in `results/fetch-r4/a01-12-warsaw.md` and `results/c3-r/s19/insights-digest.md` §G/§I — read those before judging "does this bear on the contract".
6. Paths contain spaces: quote every path. Use U.S. English. Do not use MathSciNet (closed). Do not go to the network for anything except a citation check via Crossref/zbMATH if a page range is in doubt.
7. Budget: your output ceiling is 128k tokens per response; write in chunks to disk rather than one huge response. Do not summarize the whole paper — extract what the row asks for, then §4 one-liners.

**Report format (`results/fetch-r5/<id>.md`):**
- §1 Identity verification, per file: what the file is (author, title, venue, volume, pages as printed on the file itself), page count, PDF-page ↔ printed-page offset, text-layer health (clean / garbled / image-only), edition caveats, whether it matches the list's citation EXACTLY (flag any mismatch: volume, year, page range).
- §2 What the program asked for, quoted from the list row and the flagged scout/adjudication passage.
- §3 The answer from the source: verbatim statements with page/theorem/definition numbers, then a short plain-English reading of what it settles or does not settle for the question in §2. Distinguish "the source says" from "I infer".
- §4 Anything else in the source that a future session should know exists (one line each, with page).
- §5 Caveats for `corpus-routing.md` (one line each: file id, the trap, the fix).
- §6 SHA-256 of each file you read (`shasum -a 256`).

## Assignments (two agents at a time — sponsor's sequential rule)

**a01 — rows 1, 2 (P1): the Markov apparatus.** Files r5-01, r5-02.
- r5-02 (Tôhoku 1988): transcribe verbatim the printed DEFINITION of a Markov local minimal set (and of the subshift-of-finite-type condition on the holonomy pseudogroup, with every hypothesis: differentiability class, codimension, compactness, orientation), the main theorems' statements, and whatever the paper says about ends of leaves in a Markov LMS. Record where Warsaw p. 257's "these are theorems for Markov LMS's [3]" points.
- r5-01 (Publ. Mat. 1989): transcribe verbatim the theorem under which the semiproperness hypothesis of Duminy's theorem is dropped for Markov LMS (Warsaw p. 226: "This is true for Markov LMS [4]"), with its exact hypotheses, and the definition of Markov LMS as used THERE (check it agrees with r5-02's; flag any difference). Record whether the paper says anything about leaves at infinite level or about a leaf whose closure contains a Markov LMS but which is not in it.
- Then answer, from the pages only: what would a future program theorem about K have to establish for either paper's theorem to apply? List the hypotheses as a checklist; do not judge whether the contract meets them (that is the next program stream's job) — but note in §3 which hypotheses are visibly NOT among (D1)–(D6).

**a02 — rows 3, 7b, 7c: the level theory and the bounded question of adjudication §6 item 1.** Files r5-03, r5-07b (vision only, PDF 12–21 ≈ printed 1–10), r5-07c.
- The bounded question, verbatim from `adjudication.md` §6 item 1: "Does Cantwell–Conlon 1981/1988 print any relation between the endset (or the existence of an exceptional LMS in the closure) of a leaf at infinite level and its level?" Expected answer "none". Answer it from r5-03 (all 29 pages — use the text layer, vision-check the statements) and from r5-07b (all ten printed pages by vision). Transcribe verbatim every printed statement about (i) leaves at infinite level, (ii) endsets, (iii) local minimal sets / exceptional local minimal sets in the closure of a leaf, (iv) the definition of level and of "local minimal set" (with hypotheses). If any statement relates endset to level, transcribe it in full with hypotheses and say which branch (P0)/(P1)/(P∞) of adjudication §3 it would name.
- r5-07c (TAMS 1982, nonexponential leaves at finite level): identity check, the main theorem verbatim, and one paragraph on whether anything there constrains a leaf at infinite level or its ends (expected: no; it constrains growth at finite level).

**a03 — rows 4, 5, 6 (P2): the sharpening sources.** Files r5-04, r5-05, r5-06.
- r5-04 (CMH 1998, Generic leaves): transcribe verbatim the theorem(s) behind Warsaw p. 227's "the generic leaf has one end or a Cantor set of ends" — statement, the meaning of "generic" used there (Baire? measure? which measure?), and every hypothesis. Record whether "one end" is realized by an example in the paper and under what conditions.
- r5-05 (Annals 1978, Dippolito): identity by vision (JSTOR); transcribe verbatim the semistability theorem (the one Candel–Conlon quote as Theorem 5.3.4) and the octopus/structure theorem statement with hypotheses; record the definition of "border leaf" if printed. Then one paragraph, from the pages: what the structure theory says about a leaf that is a border leaf of an open saturated set (the reduction of (S) in Candel–Conlon Lemma 5.3.2 p. 133). Do not attempt to apply it to the contract.
- r5-06 (Topology 1987, Every surface is a leaf): main theorem verbatim with hypotheses (differentiability class, which 3-manifolds, level of the leaf); the construction's statement about the leaf's level and whether the leaf's closure is described (does it contain an exceptional minimal set?); Candel–Conlon I Example 8.3.20 p. 194 cites this — record what exactly the paper proves that the example uses.

**a04 — rows 7, 8, 9, 10, 11 (P3): completeness.** Files r5-07 (Inaba only, ≈ PDF 101–106), r5-08, r5-09, r5-10, r5-11.
- r5-07 Inaba: identity of the volume (title page, editors, publisher, year, ISBN by vision) and of the article (printed pp. 95–100); list every example of an exceptional minimal set catalogued, one line each with page, and for each say whether the paper states the number of ends of its leaves (verbatim if so). Answer: does any published example there have a one-ended leaf?
- r5-08 Schweitzer: identity; transcribe verbatim the problem(s) on ends of leaves and on semi-proper leaves of exceptional minimal sets (Hector's question, Warsaw p. 258 = Hurder Problem 5.2) with their problem numbers and attributions.
- r5-09 Endsets of leaves: identity; main theorems verbatim (which leaves — totally proper? finite level?) and whether any statement concerns a non-semiproper leaf (expected: none).
- r5-10 Analytic foliations (the sponsor's find): identity; main theorem verbatim with hypotheses; then decide from the page whether it is the printed source of the Candel–Conlon I p. 199 remark ("For real analytic foliations, the proof is much easier and extends to every leaf of the exceptional minimal set") — quote the p. 199 remark from `fetched-r4/r4-15a` by vision (locate by printed folio; the PDF↔printed offset drifts) and compare.
- r5-11 Cass: identity by vision (JSTOR); main theorem verbatim; what "minimal leaf" means there; one line on whether it says anything about ends of a named leaf (expected: no).

**On completion, the orchestrator:** mechanical sweep (`results/fetch-r5/sweep-2026-09-10.json`: SHA-256, pages, text-layer health), `FETCH-RESPONSE-ROUND5.md` (delivery table + findings by row, each citing a report), caveat 22 in `results/corpus-routing.md`, the delivery header of `FETCH-LIST-ROUND5.md`, STATUS/LOG, commit. Then the bounded §6-item-1 answer is recorded as a dated block in the adjudication and ledger by the NEXT program stream (item 3's C3-r digest), not by the ingest agents.
