# SHARED — claude-shaped-science-2026 (side-session 2026-10-03)

Evidence agents append dated blocks here as they work (KICKSTART 10(e)). Deliverables: `evidence/*.md`. Briefs: `BRIEFS.md`.

## B2 (time, grind, estimates) — 2026-10-03, batch 1
- Deliverable created: `evidence/B2-time-grind-estimates.md` (plan + Table 5, Sessions 19–41, 24 rows incl. Session 35 second close).
- Note for all agents: LOG.md is now 2317 lines (BRIEFS.md says 2309); session headings at the brief's line numbers still hold (Session 36 at l. 2061, Session 41 closing at l. 2272). A side-session heading was added at l. 2311.
- The local `grep` is ugrep and rejects `.{0,N}` windows above a complexity limit; a short Python window script works (re.finditer over lines).
- Session 19's closing entry has no "Agents:" field; Sessions 20–41 do (l. 1511, 1548, 1599, 1627, 1663, 1700, 1724, 1749, 1778, 1811, 1835, 1864, 1898, 1993, 2014, 2038, 2054, 2086, 2120, 2150, 2185, 2215, 2275).

### 2026-10-03 — agent C (units S36–S41), batch 1
- Deliverable created: `evidence/C-units-s36-s41.md` (plan + yardstick + Table 1 rows 1–4, wave 1 N1–N4).
- Fact for all agents: KICKSTART 10(g) is at `rh-program/KICKSTART.md` l. 74 ("every brief names the clause it discharges"); `novel-wave-s36/WAVE-CHARTER.md` has 0 hits for `clause`.
- Wave-1 closes: N1 K, N2 K, N3 K (seed mechanism), N4 N; all four upheld by read-F (no read-O in wave 1). Wave 3 has no unit subfolders: its units are the separate folders `*-s39`.

### D (outside readers) — 2026-10-03, batch 1
- Deliverable created: `evidence/D-outside-readers-significance.md` (plan + Table 1 rows 1–5).
- Fact for all: the three public papers went out by the SPONSOR's act (Zenodo + x67.ai), none on arXiv (endorsement gate open): `results/arxiv/README.md` l. 49, 63–64, 66; `LOG.md` l. 603–608 (first two, reported 2026-09-02), l. 2166/2252/2265 (Haglund, Sessions 39/41). Landing page x67.ai live `LOG.md` l. 2270.
- Note for agents sharing the scratchpad: a file `scratchpad/win.py` was overwritten by another agent with a different argument order; D now uses `scratchpad/agentD/`.

## A (closes and corrections) — 2026-10-03, block 1
- Deliverable started: `evidence/A-closes-and-corrections.md` (plan on disk).
- Verified at the line: Conjecture U "NUMERICAL COUNTEREXAMPLE" = STATUS.md l. 26 (Session 39 block, char ≈ 9706) and LOG.md l. 2178 ("A CANDIDATE COUNTEREXAMPLE TO CONJECTURE U, numerical"); withdrawn LOG.md l. 2208. First caught by the orchestrator's read-F (LOG l. 2196), decided by unit `s5-multiplicity-s40` (LOG l. 2206).
- Tool note for other agents: `grep` here is ugrep and rejects `.{0,200}X.{0,300}` windows ("exceeds complexity limits"); a Python window works. The shared scratchpad `win.py` was rewritten by another agent mid-run; agent A uses its own `agentA_win.py`.

## B2 — 2026-10-03, batch 2
- Table 3 (waste lines) written: 38 matches of `[Ss]pent for nothing` in LOG.md (l. 1550 → l. 2304): 23 session-close lines + 15 in-line. Whole agent runs named as spent for nothing: two (Session 36 N4 first agent, l. 2088; Session 41 U3 first agent, "77 minutes, nothing on disk", l. 2268/2277), both label (ii) output ceiling. Label (iii) never used.
- KICKSTART l. 81 (10(m)) defines the labels (i)/(ii)/(iii); l. 83 (10(o)) defines the waste line.
- Sessions 34 and 35 have extra closes (l. 2026 "second close", l. 2057 "third close") with their own agent counts.

### D (outside readers) — 2026-10-03, batch 2
- Table 1 rows 6–12 written (public repo; accidental publications + three purges; ÁLKL note SENT; arXiv NOT posted; m0/m1 kept internal; X post drafts PREPARED, no sending line found; Prove2Me "nothing was posted").
- Fact for all: the ONLY human outside reader found so far is J. A. Álvarez López (first author of [ÁLKL23]): note SENT 2026-09-07 (`LOG.md` l. 1516), reply 2026-09-18 — about half of the arguments read and found in order so far, by the program's own summary at `LOG.md` l. 1634 (`results/c3-r/s14/correspondence/2026-09-18-alvarez-lopez-reply.md` l. 9; `LOG.md` l. 1634); watch item still OPEN in later queues (`LOG.md` l. 2043). The drafted answer of 2026-09-18 is marked "as sent or to be sent by the sponsor" (correspondence l. 23): no line found saying it was sent.

### 2026-10-03 — agent C, batch 2
- Table 1 rows 5–11 written: `d4-infty-s36`, `theoremR-lean-s36`, `beta-shapes-s35` (S35, in scope list), wave 2 M1a/M1b/M2 (all close T), `haglund-cert-s37` (certificate; no T/K/G/N letter).
- Facts: `novel-wave-s37/WAVE-CHARTER.md` 0 hits for `clause`. d4-infty BRIEF l. 39 is the only brief so far that mentions a C3 frontier clause ("Compare with C3's frontier (S4′ + clause (0))"), as a comparison, not as the clause discharged.
- For A (closes): M2 `proof-mine/read-O.md` l. 7–8 F3: "the partition is by inequality, not by input" — the charter (WC37 l. 88) asked for a partition "by separating input".

## B2 — 2026-10-03, batch 3
- Table 4 (deaths and walls) written, 18 rows. Usage-limit deaths: Session 8 (l. 295, four agents), Session 14 (four in one day, l. 669, 766, 837, 1005; summary l. 1215), Session 18 (l. 1429). Output-ceiling deaths: A4 designer ×5 (l. 113, 64k cap → `CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000`), N4 Session 36 (l. 2081), the orchestrator itself Session 41 (l. 2246), U3 Session 41 (l. 2268, 77 min, nothing on disk). Sleep deaths: l. 80, l. 177 → `caffeinate` rule l. 195.
- Rules that followed, in order: 128k env (l. 113), caffeinate (l. 195), RULE ONE + autocommit watchdog (l. 648–652), sequential streams (l. 900–902), HARD OUTPUT RULE / KICKSTART item 16 (l. 2092), item 16 binds the orchestrator (l. 2246), plan-first + write-each-attempt lines (l. 2268).
- Session 9 has no LOG entry; l. 300 says its two deliverables "died with the previous session", cause not stated.

### D (outside readers) — 2026-10-03, batch 3
- Table 2 written (7 rows). One human outside reader on the whole record: Álvarez López (reply 2026-09-18, about half read, "seem to be OK" in the wording of `LOG.md` l. 1634. His "final word" is not on the record; the watch item last appears in the SESSION 39 QUEUE (`STATUS.md` l. 150) and is absent from the SESSION 40–42 queues and LOG Sessions 36–41 (searched). No reader, download, citation or reply recorded for the three public papers; no arXiv endorser asked; no contact with Haglund, Alpöge–Furman, Connes–Consani, Winkelmann or Lamzouri found.

### 2026-10-03 — agent C, batch 3
- Table 1 rows 12–13 (S38: `qcond-s38` T+G, `conj-O-s38` G with T-parts). Both launched "on the program's own questions" (LOG l. 2149) before the wave-2 digest's ranking existed (qcond NOTE l. 15–16: digest "absent at this unit's start").
- STATUS queue blocks: S42 l. 124–130, S41 l. 132–137, S40 l. 139–144, S39 l. 146–151, S38 l. 153–158, S37 l. 160–165, S36 l. 167–174.

## A — 2026-10-03, block 2
- Table 1 rows 1–15 on disk (S35–S40 announcements; corrections S35–S41). Most corrections in S36–S41 were caught by the Opus read-O (FIX-FIRST items), several missed by the orchestrator's read-F (LOG l. 2203: "two of them REAL ERRORS THE ORCHESTRATOR'S READ MISSED").
- A chain worth noting for B2/C: M1b (S37, LOG l. 2127) "excluded by > 4σ at 0.6 and 0.75" → softened by read-O (l. 2141 F5) → `conj-O-s38` (l. 2158) "TENSION DISSOLVED" → overturned by its read-O (l. 2176 F3, "undecided").
- Earlier sessions (lower resolution): S7 seed no-go "NOVEL-WITH-CITATIONS … circulation-ready" (l. 262) → S10 "Theorems 1–3 are Winkelmann 2002", "(T1) … not \"unrecorded\"" (l. 308–315); alkl23 note S16 (l. 1314, 1322) → S16 post-close rereads "Two ERRORS" (l. 1403) → S17 external assessment HOLDS-WITH-REPAIR (l. 1418).

### D (outside readers) — 2026-10-03, batch 4
- Table 3 written (9 rows). Every referee of every outgoing text is an AI agent of the program (record: "wf_… 7 agents", "Two independent referee agents", "Blind referee (Opus, ≈ 443k, 42 min)"). The only non-program reader of any text besides Álvarez López was an AI: "an external (ChatGPT) assessment … relayed by the sponsor" (`LOG.md` l. 1414). The Haglund paper's posted text was changed after its referee on the sponsor's instruction (`LOG.md` l. 2165); no second read of the posted text found (LOG l. 2160–2192).

## B1 (tools inventory) — 2026-10-03, block 1
- Census done: 1081 code files under `results/` + `scripts/` (799 .py, 126 .sh, 57 .c, 55 .lean, 33 .js, 4 .h, 3 .rs, 3 .cpp, 1 .go), excluding `.lake/` and `sources/`. Roles W 612, R 371, I 82, C 16 (packaging copies). Per-folder table in `evidence/B1-tools-inventory.md`.
- Early reuse signals (to verify by hash): Lean comparator runners and trust-grep / statement-identity tools copied byte-for-byte unit to unit (c2-m4 → d5 → h5 → h4 → i1, iv17, theoremR); `conj-O-s38/verify/thin_fr.c` declared a verbatim copy of the M1b frontier `thin.c`; `lemmaB-s41/CHARTER.md` l. 28 names earlier generators "to cross-check against (never to import)".

### D (outside readers) — 2026-10-03, batch 5
- Table 4 written (9 rows). Every internal funding criterion on the record is a correctness or form test (two reads, a control, a barrier, Lean, "beyond the ground the zoo marks as covered", "a NEW mechanism"); the only written test of value to outside readers is CIRCULATION-PREP STEP 5, "Would anyone otherwise have tried this?" (`CIRCULATION-PREP.md` l. 253–258), applied to the four August papers only.

### 2026-10-03 — agent C, batch 4
- Table 1 rows 14–18 (wave 3, S39): u-offsurgery (pre-reader "K-conditional + T + G" → after reads "T + obstruction + open exponent", crossing WITHDRAWN, NOTE l. 13), lemmaG G+T, dz-half T, qtwin G, fejer-form K ("found nothing new, correctly").
- Fact: all five S39 briefs carry a heading "## Contract clause" (l. 8), but its text is the unit's own T/K/G closes, not a numbered clause of a direction's contract theorem. LOG l. 2167: "FIVE NEW-MECHANISM UNITS on the program's own questions".

## B2 — 2026-10-03, batch 4
- Table 1 (long compute legs) written, 8 rows + notes. Rehearsal-first is on the record for 5 of the 7 legs where it applies (Lane A pricing batch; campaign at 10³; D4 rehearsal + Opus gate before scale; E5 rung 0; S8 C port vs prototype).
- Algorithm changes that replaced grinding, with the record's own figures: Lane A row design (projection "≈ 18.6 h single-process" l. 1451 → "Arb 14 s, mp 7.4 min" l. 1459); campaign k-optimized radius ("overstated the compute ×20–50" l. 1601; per-height 118–458 s, CAMPAIGN.md l. 17–20, vs "6.5 h" at 10⁶ for the contract radius, CAMPAIGN.md l. 8); S8 `s8win` "3× faster" (free-greedy-s40/compute/NOTE.md l. 49).
- GPU/Colab port for D4 priced (LOG l. 1691, STATUS l. 262), made CONDITIONAL (l. 1693), never run (no GPU|Colab|cuda|numba in LOG.md after l. 1705).
- E5 writer has two records: l. 1801 "≈ 390k tokens, 3.2 h" and l. 1811 "396k / 3.6 h".

## A — 2026-10-03, block 3
- Table 1 rows 16–25 on disk. The wave-3 digest §E (`results/novel-wave-s39/insights-digest.md` l. 447–531) is the most complete single list of FIX-FIRST items for S38–S40 units; its E.12 (l. 523–531) lists five brief/charter errors caught by units (W6), one "caught by the reads, not by the unit" (uoff stop trigger).
- Prior art on disk before it was missed: Olofsson 2010 sat in `results/novel-wave-s37/beurling-fe/sources/` (S37) and was first flagged by the u-offsurgery read-O in S40 (LOG l. 2208) — passed to the S8 stream, then found again by the s5m read-O in S41 (read-O l. 214).

### D (outside readers) — 2026-10-03, batch 6
- Table 5 written (15 rows). Every "known" finding was made by an agent (novelty-check adversaries, read-O, the Opus reader, a digest) or the orchestrator; none by an outside human. Two of the three posted papers carry a relabel: the Tate-products paper's Theorems 1–3 = Winkelmann 2002 and (T1) = Bertrand (found before posting, STEP 2). Waves 3–4: seven results relabeled "on a printed core" (Hilberdink 2011/2012 ×4, Olofsson 2010, Bateman–Grosswald 1964, Diamond–Zhang 2016).

### 2026-10-03 — agent C, batch 5
- Table 1 rows 19–22 (S40): FG theory T+G (G = Lemma B_ρ), FG compute numerical record (no letter), s5-multiplicity K+T, local-greedy K-candidate + K-conditional + G.
- For B2/A: LOG l. 2240 — FG compute read: "'β = 0, no power law fits' → 'β < ¼ on the observed range'" and "ordering 'certified' → estimated". Stop lines fired on numerical triggers: u-offsurgery (LOG l. 2178), local-greedy BRIEF l. 13 "+ 0.05 numerically over two decades".

## B1 (tools inventory) — 2026-10-03, block 2
- Table 2 written: 30 byte-identical groups (69 files; 29 cross-folder), plus 5 near-identical groups after stripping comments. Biggest copy families: the Lean comparator runner / statement-identity / trust-grep tools (Session 23 c2-m4 → d5, h5, h4, i1, iv17, theoremR), the haglund-cert-s37 packaging copy, `thin.c` → `conj-O-s38/thin_fr.c`, `dyadic_ms.py` → `lemmaG-s39`.
- Cross-unit Python imports: `ccm-dh-test/dh.py` (Davenport–Heilbronn) imported by c2-m2, c2-m6, d1-m0, novel-wave-s36 (fingerprint, ly-infinity); `ccm-dh-test/weilform.py` by d1-m0; `d1-m1/ball.py` by d1-m2a. The S8 generators of free-greedy-s40 and the lemmaB-s41 units share at most 25% of lines with one another (rewritten, not adapted).

## B2 — 2026-10-03, batch 5
- Table 2 (estimate vs actual) written, 12 pairs: 7 overstated (Lane A projection "≈ 18.6 h" → "mp 7.4 min", l. 1451/1459; campaign "×20–50", l. 1591; M6 "X·50 ns overestimated ×30", l. 1592; SPEC "serial hours" → "280× smaller", d1-m2a/RUN-REPORT.md l. 89; D4 ceiling 10²⁰ → 6.63·10¹⁹, STATUS l. 497; zoo tokens 400–560k → 373k, l. 2015/2024; D1 "exponential" → "polynomial", l. 263), 2 understated (zetazero 0.28 → 0.344 s/zero; D4 "cost model 4 % low"), 3 on target or under (Lane A planner ≈ 8 min → 7.4 min; D4 1½ slots; H4 1¾ of 2¼ slots).
- Timestamps-by-estimate slips recorded in seven sessions (21, 24, 26, 38, 39, 40, 41).

## B2 — 2026-10-03, batch 6
- "Counts and medians" written. Sessions 26–34 (Fable writers, Opus readers, sequential): zoo writer 236k / 14.5 min; zoo reader 186k / 9 min; digest writer 707k / 25 min; digest reader 317k / 16 min; unit writer 358k / 27 min; unit reader 270.5k / 22 min; Lean builder 272k / 31 min; Lean checker 203k / 13 min (medians). Sessions 36–41 (all Opus, parallel): unit writer 439k / 47.5 min; read-O 383.5k / 43 min.
- Context at close: 9–56 % in Sessions 19–35; 62–70 % in Sessions 36–41 (all RULE ZERO handovers, five of six with agents in flight).
D: private-reply quotes replaced by paraphrase (01:49)

## A — 2026-10-03, block 4
- Table 1 complete for S35–S41 (43 rows) plus Table 1b (18 rows, S7–S35, lower resolution). Next: Table 2 (conditionals), Table 3 (held), counts, wording.
- Verdict pattern in the read files of S35–S41 (first verdict word per file): every Opus read-O returned AGREES-WITH-CORRECTIONS (20 files) or DISAGREES (1: `u-offsurgery-s39/read-O.md` l. 8); the orchestrator's read-F returned AGREES in 14 of 21 files. Useful for C/D.
- A, correction to block 4's counts (recounted file by file): 19 read-O files — 17 AGREES-WITH-CORRECTIONS, 1 DISAGREES (`u-offsurgery-s39`), 1 CONFIRMED (`lemmaB-s41/U6-certificate`, a second producer); 22 read-F files — 13 AGREES (including `u-offsurgery-s39/read-F.md` l. 5, "AGREES on every finite fact … DISAGREES WITH THE CLOSE'S WEIGHT"), 7 AGREES-WITH-CORRECTIONS, 2 with ✓ marks only (U6, U7).

## B1 (tools inventory) — 2026-10-03, block 3
- Table 1 written (per class). Classes with three or more WRITER implementations of the same object: S8 generator (11 programs in free-greedy-s40 and lemmaB-s41), thinning/deletion generators (4), the F_X zero finder (u-offsurgery-s39, local-greedy-s40, free-greedy-s40, lemmaB-s41), arXiv query helpers (≥ 11 folders), linters, zoo-insert scripts (18). `lemmaB-s41/CHARTER.md` l. 28 forbade importing the existing S8 generators.
- Next: Table 3 (recorded tool bugs) from LOG.md, digests §E, read-O files; then the index question.

### 2026-10-03 — agent C, batch 6
- Table 1 complete: 29 rows (rows 1–29; row 7 is S35 `beta-shapes-s35`). lemmaB U1–U7: no T/K/G/N letters; closes are prose ("No rule with a proved (B) was found", "stop condition (ii)", "the obstruction is NOT proved", "Y holds: two proved finite certificates").
- Fact for all: `lemmaB-s41/CHARTER.md` has 0 hits for `clause`/`contract`; the B2 frontier "CONTRACT, clause by clause" (C1)–(C5) is at `directions/B2-refutation-program.md` l. 264, dated 18:24 IST 2026-10-01, after the charter (16:45 IST). Its (C4): "OPEN — the single missing clause".
- U2-structured has no read file on disk.

## B2 — 2026-10-03, batch 7 (final)
- Deliverable complete and reordered (Plan, Tables 1–5, Counts and medians, limits): `evidence/B2-time-grind-estimates.md`, about 48 kB. Rows: T1 8, T2 12, T3a 23 + T3b 9 (38 matches), T4 18, T5 23, medians 9 + 7 kinds.
- Correction to batch 5: clock-stamp slips are recorded in eleven sessions (21, 24, 26, 28, 29, 30, 31, 38, 39, 40, 41), not seven.

### D (outside readers) — 2026-10-03, batch 7 (final)
- Deliverable COMPLETE: Tables 1–5 (14 / 7 / 9 / 9 / 15 rows), Counts, the closing paragraph, "Not checked". Closing finding: the only written "who would care" test is CIRCULATION-PREP STEP 5 ("Would anyone otherwise have tried this?", `CIRCULATION-PREP.md` l. 258), applied once, to the four August papers; "what would a specialist ask instead" not found in 814 `.md` files (patterns in the deliverable). Table 2 row 2 now paraphrases the private reply and quotes only `LOG.md` l. 1634.

## B1 (tools inventory) — 2026-10-03, block 4
- Table 3 written: 15 recorded tool bugs. 8 caught by the tool's author or its own self-test, 5 by an independent reader or audit (S8 "certified" ordering the code never bounded; float audit margins 9–21× too large; the block-edge bug that changed Session-40 numbers; two MAJOR bugs in the d1-m1 mpmath leg), 1 by the sponsor's Linux run (the Session-30 comparator script's brace-group `exit`), 1 by the next agent to run the orchestrator's prototype (drift beyond 10^8, a charter count off by one event).
- Next: the index question (README/INDEX, STATUS "Key artifacts", directions Instruments tables), then Counts.

## A — 2026-10-03, block 5
- Tables 2 (10 rows) and 3 (28 rows; 15 marked † = held in statement, a part corrected) on disk. Next: Counts and Wording.
- Record inconsistency for D/B2: `STATUS.md` l. 26 (S41 block, updated 19:19) still says "NO upper bound on E proved" while the same block says "U3's first bound N(x) = O(x) is dual-read", and `LOG.md` l. 2287 says "THIS IS THE FIRST UNCONDITIONAL UPPER BOUND FOR THE SYSTEM" (U3's E(x) ≤ 0.1964132·(x − 1)); `LOG.md` l. 2281 (U4) "THE FIRST PROVED UPPER BOUNDS FOR E, on a finite range".

### 2026-10-03 — agent C, batch 7
- Table 2 (tallies) and Table 3 (14 follow-up rows) written. Headline tallies: 0 of 29 briefs name a numbered contract clause; all 4 plain-T closes are on PUBLISHED targets from digest rankings (M1a, M1b, M2, dz-half); 12 of 29 closes carry no T/K/G/N letter.
- For A: STATUS l. 126 (S42 queue, 18:23 IST) "NOT PROVED: any upper bound whatever for E (not N(x) = O(x))" predates U3's N(x) = O(x) (18:50 IST update, STATUS l. 125).
- Lean follow-ups queued for Theorem T (D37 l. 335, STATUS l. 155, l. 148) and U_q/L′/D (STATUS l. 141): no Lean folder after `theoremR-lean-s36`.

### 2026-10-03 — agent C, batch 8
- Table 4 written: 15 rows (13 unit results cut back or delivered as a special case; 2 brief claims holding only in a special case). Main sources: D39 §E (l. 447–531), D37 §E l. 292–317, read-O/read-F files.
- For A: D39 l. 467 (conj-O F2: Lemma G "a reformulation, not a weaker input"); D39 l. 530–531 (u-offsurgery stop trigger "accepted a pre-asymptotic fit … caught by the reads, not by the unit").

## B1 (tools inventory) — 2026-10-03, block 5 (closing)
- Index: no program-wide tool index, manual or register found. STATUS.md "Key artifacts" (l. 71–78) lists documents only; the directions' Instruments tables (defined in `directions/README.md` l. 34 as "quantity | current best value | result file | dated") name code only as result files; per-package READMEs exist (Linux check, Haglund certificate archive). The only written rule on code reuse is the lemmaB-s41 charter's "never to import" (l. 28).
- Counts: W 612, R 371, I 82, C 16. Cross-unit imports: 21 writer files in 5 units, from `ccm-dh-test` (dh.py, weilform.py, finisher_weilext.py) and `d1-m1/ball.py`. Deliverable complete: `evidence/B1-tools-inventory.md`.

### 2026-10-03 — agent C, DONE
- `evidence/C-units-s36-s41.md` complete: Table 1 29 rows, Table 2 tallies, Table 3 14 rows, Table 4 15 rows, plus "What this reader could not check".
- Correction applied in my own file: M1a/M1b are PUBLISHED object classes, but STATUS l. 156 calls their questions "the program's own and … not on any printed agenda" — both facts now in rows 8–9 and in Table 2.

## A — 2026-10-03, block 6 (final)
- Deliverable COMPLETE: `evidence/A-closes-and-corrections.md` (233 lines). Table 1: 43 rows (S35–S41); Table 1b: 19 rows (S7–S35); Table 2: 10 rows; Table 3: 28 rows (12 clean, 16 †), plus 3 unchecked S41 announcements.
- Correction to block 5: Table 3 has 16 † rows, not 15.
- Headline counts: Table 1 first catcher — Opus read-O 32 of 43; orchestrator's read-F 2; orchestrator's re-derivation or self-check 3; a later unit 3; the consolidation digest 2; a referee agent 1; the sponsor 0 (S35–S41). Lag: 0 sessions 7, 1 session 31, 2 sessions 4, untraced 1.
- Table 2: of the "missing piece" conditionals, Lemma G proved to be the target restated (LOG l. 2176), H_{0.35} was refuted within a session (l. 2208), Lemma B_ρ stayed open through a seven-unit stream (STATUS l. 26 S41 block).

## read-O (second read) — 02:05 IST 2026-10-03, block 1
- Blind pass done before opening the study or evidence/: `read-O.md` §1 holds 24 rows (B1–B24) from page.txt, KICKSTART Part 2 and STATUS l. 28–52. Blind expectations: time stamps by script (B3), STATUS file shape (B4), tool-before-grind line (B2), tools register (B15), qualitative-agreement lint (B9), outside human reader as practice (B11, B14). The post's "footgun" remark on Millennium Prize problems (page.txt l. 75) must appear in any faithful study.
- Next: Step 2, quotations against page.txt.

## read-O (second read) — 02:09 IST 2026-10-03, block 2
- Read process-lessons.md whole (165 lines; identical to process-lessons.pre-reader.md by cmp). Starting Step 2 (post quotations, with section tags) and Step 3 (record citations).
- Early flags to test, not yet findings: P4 "seven later sessions — eleven in all" vs its own list (nine sessions after 24); P6 "ten conditional results" broken down as 1+1+1+6 = 9; P2 "37 per cent of all code files" vs 371/1,081; P8 "not what the record shows" vs the sponsor's own trigger of standing order 12 (STATUS l. 44); P9 heading quote "correct, and a shrug" is not in the post; rule (u)'s "With the sponsor" list vs KICKSTART item 7 ("NOWHERE else") and standing order 9.

## read-O (second read) — 02:14 IST 2026-10-03, block 3
- Step 2 done: every passage tagged [I]/[W]/[K]/[T]/[O] is verbatim in page.txt and in the tagged section; problems are of framing only (§0/P12 "one sentence" on problems of this kind vs page.txt l. 8; P9 heading in quotation marks not from the post).
- Step 3(a) done: 60 direct citations hold at the line. Scripts tested: `stamp.py --check c6fd319a` prints 36 same-day stamps, 5 AHEAD (the five N7 names), exit 1; it is one-sided by construction (only stamps later than their commit). `status-split.py` dry run: 578,239 → 57,737 bytes kept, 522,312 bytes in 11 blocks, CHECK PASS, nothing written (no STATUS-ARCHIVE.md created).
- Next: Step 3(b), the five evidence files, three rows each re-derived from the record.

## read-O (second read) — 02:19 IST 2026-10-03, block 4
- Evidence A passes my sample (Table 1 rows 1–4, 11, 12; Table 2 c1, c10; catcher of rows 7, 17). The study drops A's "fate not traced: 1 (c9)" (nine conditionals listed as ten) and A's 3 orchestrator self-catches.
- Evidence B1 passes as a census (S8 files exist; imports 17 vs 21 in the same five units; 19 zoo-insert scripts over 18 sessions; Table 3 15 rows). Defects inherited by P2: "37%" is 34.3% (371/1081); the "eleven" S8 programs include one tool's deliberate evolution (proto → line-by-line port → s8gen → s8win) and one reuse (theory/verify/s8_check.py runs the prototype), which P3 praises.
- Private e-mail: no sentence of the third party's message is in any current study file, LOG or STATUS (7-gram comparison; only the program's own lines and a public title overlap). The sponsor ran the history rewrite at 02:14 (LOG l. 2329): §E.3(a) is stale. After the squash, `stamp.py --check c6fd319a` reports 4 AHEAD, not 5 — the N3 slip is no longer visible to it.

## read-O (second read) — 02:23 IST 2026-10-03, block 5
- Evidence B2, C, D pass my samples (B2 Table 2 rows 3, 5, 6, 7, 12, Table 5 rows 36, 41; C 2d by own grep, Table 3 rows 1, 3, 9; D Table 1 rows 3, 8, 9, Table 2 row 4, Table 3 Haglund referee). No evidence file fails.
- Study-side defects found: stamp slips are on record in at least 14 sessions (16, 20, 36 missing; remedy first written Session 16, LOG l. 1392), and P4 says "seven later — eleven in all"; "advance estimates wrong by one to two orders" holds for 4 of 10 advance pairs only (5 within ×1.5); P1 "refereed and published" (an Opus referee; a Zenodo deposit); P12 "three hours" (ledger opened 00:29, study ~02:00); P8 "not what the record shows" vs STATUS l. 44.
- Next: Step 4 verdicts P1–P12, then findings with OLD/NEW pairs, then rules.

## read-O (second read) — 02:29 IST 2026-10-03, block 6
- Findings written: 17 (FIX-FIRST 7: F1 "one sentence" vs page.txt l. 8; F3 stamp slips ≥ 14 sessions, remedy first in S16; F4 advance-estimate overreach in P4/(w); F6 "eleven separate" S8 programs; F7 "refereed and published"; F12 P8 vs STATUS l. 44 and (z)'s published-object clause; F15 (z)'s outside-user cell vs §C.4). Minor 10. Each with OLD/NEW pairs, OLDs unique.
- Next: Step 4 table (P1–P12), Step 5 rule verdicts, Step 6, could-not-check, verdict line.

## read-O (second read) — 02:31 IST 2026-10-03, block 7
- Rule verdicts: (u) AMEND (sponsor items into standing order 9's list per item 7; pre-split commit named for old line citations); (v) AMEND into two W2 lines, no new letter; (w) AMEND (check two-sided via a stamp log, run before any squash; 10(l) sentence narrowed to formula-priced compute legs); (x) AMEND into W3 + the NOTE §0 close block, no new letter; (y) AMEND evidence line only; (z) AMEND (drop the published-object clause and the outside-user prediction; check-brief.py tests the bearing line's form). Drop first: (x), then (v), as letters. "18 of 29 follow-ups" is 10(d) obeyed, not momentum.

## read-O (second read) — 02:33 IST 2026-10-03, block 8
- Step 6 written. Main omission: the private-e-mail kind has fired in two units (Session 41's purge of the tracked reply, LOG l. 2262; tonight's evidence D, LOG l. 2321) — at the 10(p) threshold for a BRIEF-WARNINGS line; a WRITER/READER pair is proposed in read-O.md §8. Pairs now 39, all apply in sequence.
