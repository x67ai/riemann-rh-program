# SHARED — Session-40 digest applier (SESSION 40 QUEUE item 0(c)), `results/novel-wave-s39/` (dated blocks, newest last)

Agent: digest applier, Opus 5.5 (default effort). Brief: `APPLIER-BRIEF.md` (this folder). Model: `results/novel-wave-s37/digest-APPLIED.md`.
Writes only: `directions/*.md` (insertions + Last-touched lines), this folder (`digest-APPLIED.md`, this file). Git is not run.

## 2026-10-01 12:20 IST block 0 — START: brief and model read; sources hashed; pristine copies taken

- Brief read in full (3 591 B); model report read in full (28 324 B; method: pristine copies, check script, diff verdict, bar counts).
- Source NOTEs (current files, not `NOTE.pre-reader.md`), SHA-256 at 12:20:02 IST:
  fejer-form-s39 0ab5f19e…; dz-half-s39 51e062e9…; u-offsurgery-s39 ef143a43…; qtwin-s39 0a7ea6be…; lemmaG-s39 41f195d4….
- Pristine copies of all 13 `directions/*.md` taken 12:20:11 IST (agent scratchpad `before/`), plus start copies of the five NOTEs and
  read-O files (scratchpad `notes-at-start/`), so a NOTE that changes mid-work is detected at the close.
- Running now: reading each NOTE's named sections and the target tables. Resume here: if this block is the last one, nothing has been
  inserted yet; restart from the brief.

## 2026-10-01 12:24 IST block 1 — sources read; routing fixed (nothing inserted yet)

- Every named section is present (no stop): fejer-form §8 (lines 279–288: header + 8 rows, the 8th its own "↳ provenance" row) and §9
  (292–304: 3 entries with "Target: C2" + 1 "Closed by this unit" record); dz-half §6.2 (386: 1 row) and §6.3 (389–399: U-1 … U-5, no
  Target lines); u-offsurgery §6 (215–216: 2 rows) and §7 (220–230: UT-U1 … UT-U5, UT-U3 "Target: B2, C2"); qtwin §10.1 (376–378: 3 rows)
  and §10.2 (381–393: UT-QT1 … UT-QT4); lemmaG §6 (364–366: 3 rows) and UT-L1 … UT-L5 (369–385, no Target lines). read-O §7 items for the
  three drafts: u-offsurgery A5 (+A8), qtwin A4, dz-half A2.
- Routing (from the NOTEs' own shape lines; entries without a Target line go to the file their NOTE writes rows for):
  C2 ← fejer-form rows + qtwin rows; fejer-form §9, UT-U3 (2nd copy), UT-QT1 … QT4, draft (b).
  B2 ← dz-half row, u-offsurgery rows, lemmaG rows; U-1 … U-5, draft (c), UT-U1 … UT-U5, draft (a), UT-L1 … UT-L5.
- One byte change foreseen (brief's escape rule): lemmaG row 364 has an unescaped `|E(n)|` inside a cell (7 bars against 5); the two
  bars become `\|`. Every other row: to be counted by script.
- Running now: building the insertion script on scratch copies. Resume here: no direction file has been edited yet.

## 2026-10-01 12:27 IST block 2 — specs checked by script; the three read-O drafts written (scratch only)

- Script check of the specs against the current NOTEs: all 17 rows have the header's 5 unescaped bars except lemmaG 364 (7: the
  `|E(n)|` pair inside the second cell); all 23 NOTE entries are cleanly bounded (first line "- ", continuation lines indented, no
  trailing spaces); Target lines present for the fejer-form three and UT-U1 … U5, UT-QT1, UT-QT2; absent for the rest.
- Drafts (scratch `drafts.py`), each labeled "(from read-O, single-check)": (a) "S5(0.95): its zero and its exact multiplicity
  ascent" → B2; (b) "A limit-periodic Hilberdink Prop. 3.4" → C2; (c) "Is N − ρx = O(x^{1/2}) for the Diamond–Zhang systems?" → B2.
- Running now: provenance texts and the build script. Resume here: no direction file has been edited yet.

## 2026-10-01 12:30 IST block 3 — C2 Instruments: 11 NOTE rows + 2 ↳ Session-40 provenance rows inserted (lines 166–178)

- `directions/C2-rigidity-conservation.md`, after the table's last row (165, the Session-38 ↳ PROVENANCE row), above the blank line
  and the Session-38 renderer note: fejer-form §8 rows 166–173 (NOTE 281–288; 173 is the NOTE's own "↳ provenance" row), ↳ 174;
  qtwin §10.1 rows 175–177 (NOTE 376–378), ↳ 178. Every row 5 bars = header. Applied 12:30:15 by guarded copy of the dry run
  (byte-identical). SHA-256 04496dce… → 1516b6c9…; wc -l 201 → 214.
- Running now: C2 Untried. Resume here: C2 rows are in; C2 Untried, B2 and the Last-touched lines are not.

## 2026-10-01 12:30 IST block 4 — C2 Untried: 10 entries inserted (lines 196–205)

- After the Untried section's last bullet (old 182, now 195: UT-5 of Session 38): fejer-form §9 ×4 (196–199; 199 is the "Closed by
  this unit" record, with a note giving the closed bullets' new lines 194 (UT-4) and 189 ("Extremal characterization of ξ", old 176)),
  UT-U3 (200; B2 copy to follow), UT-QT1 … UT-QT4 (201–204), draft (b) "A limit-periodic Hilberdink Prop. 3.4" (205). Applied
  12:30:24 (byte-identical to the dry run). SHA-256 1516b6c9… → e4999ca7…; wc -l 214 → 224.
- Running now: B2 Instruments. Resume here: C2 insertions complete (Last-touched not yet); B2 untouched.

## 2026-10-01 12:30 IST block 5 — B2 Instruments: 6 NOTE rows + 3 ↳ Session-40 provenance rows inserted (lines 129–137)

- `directions/B2-refutation-program.md`, after the table's last row (128, the Session-38 ↳ PROVENANCE row): dz-half §6.2 row 129
  (NOTE 386), ↳ 130; u-offsurgery §6 rows 131–132 (NOTE 215–216, dual-read text), ↳ 133 (quotes the NOTE's WITHDRAWN line 13);
  lemmaG §6 rows 134–136 (NOTE 364–366; row 134 with the two bars of `\|E(n)\|` escaped, the one byte change), ↳ 137. Every row
  5 bars. Applied 12:30:32 (byte-identical to the dry run). SHA-256 fba5d0da… → a9111475…; wc -l 152 → 161.
- Running now: B2 Untried. Resume here: C2 complete, B2 rows in; B2 Untried and both Last-touched lines remain.

## 2026-10-01 12:30 IST block 6 — B2 Untried: 17 entries inserted (lines 155–171); all insertions in

- After the Untried section's last bullet (old 145, now 154: UT-13 of Session 38): U-1 … U-5 (155–159), draft (c) "Is N − ρx =
  O(x^{1/2}) for the Diamond–Zhang systems?" (160), UT-U1 … UT-U5 (161–165; UT-U3 at 163, C2 copy at 200), draft (a) "S5(0.95): its
  zero and its exact multiplicity ascent" (166), UT-L1 … UT-L5 (167–171). Applied 12:30:44 (byte-identical to the dry run).
  SHA-256 a9111475… → eacc4794…; wc -l 161 → 178.
- Running now: the Last-touched lines (C2, B2). Resume here: every row and entry is in; Last-touched, verification, report remain.

## 2026-10-01 12:31 IST block 7 — Last-touched lines prefixed (C2, B2)

- Line 5 of each file changed in place: the Session-40 text is prepended after "**Last touched:** "; the old text follows byte-for-byte
  (script check = True for both); no line added. Guarded on the post-insertion hashes. C2 e4999ca7… → 614e59e4…; B2 eacc4794… →
  b9f37f49….
- Running now: verification (script + actual diff against the pristine copies). Resume here: all edits done; verify, then report.

## 2026-10-01 12:32 IST block 8 — verification: ALL CHECKS PASS; INSERTION-ONLY VERIFIED

- `verify.py` (scratchpad) 12:31:57: difflib opcodes = 2 insert blocks per file + the prefix-only line 5; every new row 4 cells / 5
  bars; each of the 17 rows an exact line of exactly its target (lemmaG 364 after the declared escape); each NOTE entry (wrapped
  lines joined) a substring of exactly its Target file(s) (UT-U3 in B2 163 and C2 200); each draft an exact line of its target with
  the label; the five quotes in the ↳ rows found verbatim in their NOTEs; the other 11 direction files byte-identical; the five
  NOTEs and five read-O files byte-identical to the 12:20 start copies.
- `diff` 12:32:22: C2 `5c5 165a166,178 182a196,205`; B2 `5c5 128a129,137 145a155,171`; the only `<` lines are the two old
  Last-touched lines. Verdict line printed by the shell: INSERTION-ONLY VERIFIED.
- Found, pre-existing, not changed: C2 row 142 and B2 row 120 carry `\\|` (escaped backslash + live bar), so under GFM they have 11
  and 7 bars against 5. For the orchestrator.
- Running now: writing `digest-APPLIED.md`. Resume here: the direction files are final; only the report remains.

## 2026-10-01 12:34 IST block 9 — report: header, §0–§4 written to `digest-APPLIED.md`

- §0 hashes and routing; §1–§2 the 22 table rows with line and bar counts (listing generated from the live files); §3–§4 the 27
  Untried lines with key, source lines and first words (generated). Remaining: §5 drafts, §6 Last-touched, §7–§8 verification output,
  §9 summary, §10 judgment calls and notes for the orchestrator, §11 verdict.
- Resume here: the direction files are final; finish the report from §5.

## 2026-10-01 12:36 IST block 10 — CLOSE: all rows and entries applied, insertion-only verified; report complete; nothing running

- `digest-APPLIED.md` complete (340 lines, §0–§11): per-file insertions with first words, SHA-256 before/after, the diff verdict
  (INSERTION-ONLY VERIFIED, re-run 12:35), the column check (every inserted row 5 bars / 4 cells), verify.py output verbatim (ALL CHECKS
  PASS), judgment calls, notes for the orchestrator. Final: C2 614e59e4…, B2 b9f37f49…; NOTEs unchanged at 12:35:58.
- Totals: 22 table rows (17 NOTE + 5 ↳), 27 Untried lines (24 copied incl. UT-U3 twice + 3 drafts), 2 Last-touched lines prefixed.
  Nothing left unplaced. For the orchestrator: pre-existing `\\|` bars in C2 row 142 and B2 row 120 (GFM off-count; not changed).
- No git command run. Nothing running. Resume here: nothing to resume — the unit is done.

## 2026-10-01 16:58 IST block 11 — CONSOLIDATION START (Session 41, KICKSTART 10(a)); brief read; inputs hashed

- Agent: consolidation, Opus 5.5. Brief: `DIGEST-BRIEF.md` (this folder, 6 175 B, read in full). Outputs: `insights-digest.md`,
  `ZOO-LINES-STAGED.md` (this folder), and these dated blocks. No git; no NOTE, zoo, direction, STATUS or LOG file is edited.
- Stop check: all 33 files present (NOTE, read-F, read-O for each of the eleven units). No stop.
- SHA-256 prefixes at 16:57:43 IST (NOTE / read-F / read-O): qcond-s38 579f22e3 / 5695b73f / 4ab28867; conj-O-s38 e897b844 /
  0f5bd889 / 3e67be7e; u-offsurgery-s39 ef143a43 / c30a9ee3 / f25749d7; lemmaG-s39 41f195d4 / 1766f908 / daafc8bf; dz-half-s39
  51e062e9 / 766eeafa / 26241c2f; qtwin-s39 0a7ea6be / d487577b / 885ee374; fejer-form-s39 0ab5f19e / e323d3d6 / 6d598b76;
  free-greedy-s40/theory 9c5a8886 / 148f9dbf / 9c8a5eec; free-greedy-s40/compute 25a78d32 / 5fdd0da4 / f723ac3f; s5-multiplicity-s40
  ca102d85 / ebca8c39 / 23092da4; local-greedy-s40 e8dc8e87 / 2045e251 / 459c85e2. Others: lemmaB-s41/CHARTER 4596b371;
  free-greedy-s40/CHARTER 4ae44bd3; BARRIER-ZOO 0a0a832d (788 lines); directions/README e7d22586; B2 b9f37f49 (178); C2 614e59e4 (224);
  digest-APPLIED a414302b; s37 digest e86f642a; s37 ZOO-LINES-STAGED 93e7e394.
- Baseline read: s37 digest §B (B1–B10), §F (F.1–F.3, UT-1 … UT-13), §G; s37 staged-lines format (blocks, insertion map, Block C).
- Running now: reading the eleven units (§0 close, read-F, read-O verdict/FIX-FIRST/additions). Resume here: no deliverable written yet.

## 2026-10-01 17:01 IST block 12 — digest header + §A.1–A.3 written (qcond, conjO, uoff)

- `insights-digest.md` created: header, conventions, A.1 qcond, A.2 conjO, A.3 uoff.
- Found for §E (consolidator, not in either read): (1) qcond NOTE carries the corrected Theorem D block FIVE times (lines 219, 252,
  335, 351, 451; the pre-reader NOTE has one) — at 218–219 it cuts L′'s COVERAGE sentence after "It strengthens BFE" (pre-reader 215–216
  continues "§11(i) (finite Euler factors) to all finite Dirichlet-polynomial multipliers"); an application slip of F1, no theorem
  changes. (2) uoff NOTE:22 ("at exponent 0.35 unrefuted") lags s5m NOTE:15/101 (H_θ false for θ ≤ 0.35, c < 1.88).
- Disagreements noted: conjO α = 0.75 mean square (read-F accepted at report level; read-O re-ran, undecided); qcond Meyer subtraction
  (read-F ρ_q·Leb, read-O (ρ_q − 1)·Leb — both valid).
- Running now: lemG, dzh, qtw, fej. Resume here: append §A.4 onward.

## 2026-10-01 17:04 IST block 13 — §A.4–A.7 written (lemG, dzh, qtw, fej): the seven Session-38/39 units are done

- Each from §0/close + read-F + read-O verdict/FIX-FIRST/novelty/additions; NOTE bodies opened only at the cited lines.
- Read-F/read-O differences recorded: lemG F1–F2 missed by read-F (its §4 says so; read-O re-derives); fej wording F1–F2 (read-F
  accepted, verified by hand at reconciliation); qtw F1 credit (Lemma M first in qcond's read). No contradiction on a theorem's validity.
- Running now: the four Session-40 units (fgT, fgC, s5m, lg) + the free-greedy charter. Resume here: append §A.8 onward.
