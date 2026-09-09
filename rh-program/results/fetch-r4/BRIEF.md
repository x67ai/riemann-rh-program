# Round-4 fetch ingest — agent brief (Session 18, 2026-09-09)

**Session scope (sponsor directive):** the RH program is NOT resumed this session. This is an INGEST-ONLY session, exactly like Session 4.5: verify each sponsor-delivered file against its citation (standing order 5), extract the specific thing `FETCH-LIST-ROUND4.md` says the program needs from it, and record it durably. No new mathematics, no verdict changes, no edits to direction files, adjudications or the zoo. If a source contradicts something the program has on record, WRITE THAT DOWN in your report with page references — do not fix the record yourself.

**Files:** `fetched-r4/` (gitignored, local-only). Filenames start with `r4-<list item number>`. `fetched-r4/duplicates-of-r3/` holds re-deliveries of r3s-32 and r3s-34 (already on disk, ignore). `fetched-r4/not-on-list/` holds one stray download (a math.GM "proof of RH" preprint; ignore).

**Ground rules (corpus-routing.md caveats 1–3, binding):**
1. **No third-party OCR, ever.** Image-only files (`r4-04` Contemp. Math. 387, `r4-06a` Farber, `r4-11` Wengenroth scan, `r4-15a` Candel–Conlon I, `r4-15a2` Candel–Conlon II) are read by rendering pages and reading them with your own vision: `pdftoppm -r 110 -f N -l M -png <file> <scratch>/pg` then the Read tool on the PNGs. Use text layers where they exist (`pdftotext -f N -l M`), but **verify any formula-critical quotation by vision** — text layers garble math.
2. **Locate before you read.** For a volume, find the article's PDF page range first (table of contents / grep) and record the PDF-page ↔ printed-folio offset in your report.
3. **Quote exactly.** Where the list asks for an exact statement (a theorem, a definition, a hypothesis), transcribe it verbatim with the printed page and the theorem/definition number. Mark anything you could not read with [illegible]. Never paraphrase a hypothesis.
4. **Write to disk as you go.** Your deliverable is `results/fetch-r4/<your-id>.md`. Create it at the start with a header and the file list, then append sections as you finish them. An auto-commit watchdog commits every ten minutes; a session can die at any moment, and what is on disk is what survives.
5. **Read the "where it was flagged" pointer first.** Each list item names the adjudication section that asked for it (`results/c3-r/s16/novelty/adjudication.md` §4, `results/c3-r/s16/qs4prime/adjudication.md` §4/§5, `results/c3-r/s14/novelty/adjudication.md` §4, `results/c3-r/referee-s14/novelty-adjudication.md`). Read that passage so you answer the question that was actually asked, then answer it from the source.
6. Use U.S. English. Do not use MathSciNet (closed). Do not go to the network for anything except a citation check via Crossref/zbMATH if a page range is in doubt.

**Report format (`results/fetch-r4/<id>.md`):**
- §1 Identity verification, per file: what the file is (author, title, venue, volume, pages as printed on the file itself), page count, PDF-page ↔ printed-page offset, text-layer health (clean / garbled / image-only), edition caveats, whether it matches the list's citation EXACTLY (flag any mismatch: volume number, year, page range, edition).
- §2 What the program asked for, quoted from the flagged adjudication passage.
- §3 The answer from the source: verbatim statements with page/theorem numbers, then a short plain-English reading of what it settles or does not settle for the question in §2. Distinguish "the source says" from "I infer".
- §4 Anything else in the source that a future session should know exists (one line each, with page).
- §5 Caveats for `corpus-routing.md` (one line each: file id, the trap, the fix).
