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
