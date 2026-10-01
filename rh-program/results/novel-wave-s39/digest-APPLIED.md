# digest-APPLIED — the five Session-39 units' Instruments rows and Untried entries applied to the direction files (SESSION 40 QUEUE item 0(c))

Bookkeeping agent (Opus 5.5), Session 40, 2026-10-01. Brief: `results/novel-wave-s39/APPLIER-BRIEF.md`. Model, method reproduced:
`results/novel-wave-s37/digest-APPLIED.md` (pristine copies, guarded programmatic copy, check script, actual diff, bar counts).
Sources: the CURRENT dual-read NOTEs (never `NOTE.pre-reader.md`) of `fejer-form-s39`, `dz-half-s39`, `u-offsurgery-s39`, `qtwin-s39`,
`lemmaG-s39`, plus three entries drafted from their read-O files. Insertion-only; rows and NOTE entries copied byte-for-byte (one
declared escape, §2); no git command run. Written: `directions/C2-rigidity-conservation.md`, `directions/B2-refutation-program.md`,
this record, `SHARED.md` (this folder, blocks 0–10). Not touched: the other 11 `directions/*.md`, every NOTE and read-O file, STATUS, LOG.
Line numbers are in the files as they stand after ALL insertions (final state), unless a line says otherwise.

## 0. SHA-256 before any insertion; routing (taken 2026-10-01 12:20 IST)

```
0ab5f19ed976a72ed507b271b40eb698d5b9cbfabad319214fc9eb4c406893c0  results/fejer-form-s39/NOTE.md      (source, read only)
51e062e9ddc3bb0edd092d1e9357e0f1c232df377c98554a826712b7d53bac3b  results/dz-half-s39/NOTE.md         (source, read only)
ef143a4354b75580c17d619024d779de4484b0688fe886d7fce1cae9fddfc668  results/u-offsurgery-s39/NOTE.md    (source, read only; dual-read 12:17)
0a7ea6be2449adf8f8a5cb5cf248e04d7c2317d6e0b9526b9fbaf2f1fa206af5  results/qtwin-s39/NOTE.md           (source, read only)
41f195d40705ae77819b9a3805cd1323f0e5b7f3468e447c4db04b9e93b65d61  results/lemmaG-s39/NOTE.md          (source, read only)
04496dce0b444d480e460d35aae3eaa78f90a1beaaaf58b85506afb524afc7bb  directions/C2-rigidity-conservation.md
fba5d0daaa69a1a943a883e76f0e5e1934cc053128d6fbf3b770c5a8c53a49c1  directions/B2-refutation-program.md
```

Pristine copies of all 13 `directions/*.md` (12:20:11 IST) and start copies of the five NOTEs and five read-O files are in the agent's
scratchpad (`before/`, `notes-at-start/`), not in the program tree. A script found none of the 17 rows in any pristine direction file
(nothing pre-applied). Every section the brief names is present (no stop): fejer-form §8 (rows at NOTE 281–288) and §9 (292–304);
dz-half §6.2 (386) and §6.3 (389–399); u-offsurgery §6 (215–216) and §7 (220–230); qtwin §10.1 (376–378) and §10.2 (381–393); lemmaG §6
(364–366) and UT-L1 … UT-L5 (369–385, found by grep, inside §6); read-O §7 of u-offsurgery (A5, A8), qtwin (A4), dz-half (A2).

Routing, read from the NOTEs (not chosen): fejer-form §8 and qtwin §10.1 say their rows are in C2's column shape; dz-half §6.2,
u-offsurgery §6 and lemmaG §6 say B2's. Entries with a "Target:" line follow it — fejer-form's three (C2), UT-U1, U2, U4, U5 (B2), UT-U3
("Target: B2, C2": quoted in both), UT-QT1 and UT-QT2 (C2). Entries with no Target line go to the file their NOTE's rows are written
for: U-1 … U-5 and UT-L1 … UT-L5 → B2; UT-QT3, UT-QT4 → C2; fejer-form's fourth bullet, a "Closed by this unit" record, → C2, where both
bullets it closes stand. Drafts: (a) u-offsurgery → B2, (b) qtwin → C2, (c) dz-half → B2. Both targets already had an Instruments table
and an Untried section; both headers are "| Quantity | Current best value | Result file | Dated |" (5 bars = 4 cells).

## 1. C2 Instruments — eleven NOTE rows + two ↳ Session-40 provenance rows (applied 2026-10-01 12:30:15 IST)

File `directions/C2-rigidity-conservation.md`. Appended after the table's last row (old and new line 165, the Session-38 ↳ PROVENANCE
row), above the blank line and the Session-38 "[Renderer repair …]" note (old 167, now 180). fejer-form §8 rows (NOTE 281–288) at
166–173 — the eighth (173) is the NOTE's own "↳ provenance" row, copied as a row; 174 is this agent's ↳ row. qtwin §10.1 rows (NOTE
376–378) at 175–177; 178 is this agent's ↳ row. Each ↳ row is "↳ [PROVENANCE 2026-10-01, Session 40 — Session-39 unit `<unit>`, applied
insertion-only by the bookkeeping agent]" + the rows' first words, NOTE path, lines and full SHA-256, the NOTE's heading words (verbatim
where quoted; the script found each quote in its NOTE) and a marked bookkeeping note on abbreviated paths. Copy = programmatic slice of
the NOTE lines, applied by a guarded copy of the dry run (`cmp`: byte-identical).

```
sha256 before 04496dce0b444d480e460d35aae3eaa78f90a1beaaaf58b85506afb524afc7bb
sha256 after  e4999ca778df277804607284d4a323dd38b22d425c7d60d45e1db91f8210eb08   (after §3 as well; line 5 changed in §6)
166	header 5 bars / row 5 bars	| Rung-1 exit degree from the Weil (Toeplitz / Hodge-index Gram) region, RH-fa
167	header 5 bars / row 5 bars	| V's least Toeplitz eigenvalue λ_min(T_M(V)) (closed form (M + 1) − (Σφ^{2k}·
168	header 5 bars / row 5 bars	| Positions-side Fejér defect on q^Z, D_k = h(q^{g−1+k} − 1) (M1a's Step 1 on 
169	header 5 bars / row 5 bars	| Class-number window (√q − 1)^{2g} ≤ h ≤ (√q + 1)^{2g} (two Weil tests after 
170	header 5 bars / row 5 bars	| Class-summed Clifford N_1 ≤ h at g = 2 (non-free, non-Weil positions inequal
171	header 5 bars / row 5 bars	| Z3: zeros-side Weil–Fejér form, g_T = 2(1 − \|x\|/L)₊cos(Tx), L = 20 | ζ (10
172	header 5 bars / row 5 bars	| Z1: M1a's (C_Q) on RH-false controls | F_{2.9,2}: 2.95 = 2.95 (exact for eve
173	header 5 bars / row 5 bars	| ↳ provenance | the rung-1 LP is Oesterlé's program (Howe–Lauter 1202.6308 p.
174	header 5 bars / row 5 bars	| ↳ [PROVENANCE 2026-10-01, Session 40 — Session-39 unit `fejer-form-s39`, app
175	header 5 bars / row 5 bars	| Q_cond's last corner — weighted / clustering Beurling systems with Riemann's
176	header 5 bars / row 5 bars	| Thick-mixture probe (truncations of 𝒯 at q = 4): best attainable min_{x ≤ 64
177	header 5 bars / row 5 bars	| Weighted genus-1 admissibility over F₅ (L = 1 − tu + 5u², t real; rung 1 of 
178	header 5 bars / row 5 bars	| ↳ [PROVENANCE 2026-10-01, Session 40 — Session-39 unit `qtwin-s39`, applied 
```

## 2. B2 Instruments — six NOTE rows + three ↳ Session-40 provenance rows (applied 2026-10-01 12:30:32 IST)

File `directions/B2-refutation-program.md`. Appended after the table's last row (old and new line 128, the Session-38 ↳ PROVENANCE
row), above the blank line and the renderer note (old 130, now 139). dz-half §6.2 row (NOTE 386) at 129, ↳ 130 (with a marked note:
the row's "Untried U-1" is line 155). u-offsurgery §6 rows (NOTE 215–216, the dual-read text) at 131–132, ↳ 133, which quotes the NOTE's
line 13 verbatim ("THE CLOSE IS CHANGED: the numerical crossing of Conjecture U's line by S5(0.8) is WITHDRAWN.") and expands the
`u-offsurgery-s39/` and `…/` path abbreviations. lemmaG §6 rows (NOTE 364–366) at 134–136, ↳ 137.
The one byte change of the unit, required by the brief's escape rule: NOTE row 364 carries the absolute value `|E(n)|` unescaped
inside its second cell (7 bars against the header's 5); in line 134 its two bars are written `\|` (the substring "at |E(n)| ≍"
became "at \|E(n)\| ≍"; nothing else differs; the ↳ row 137 states it). Rows 131–132 already arrive with escaped bars.

```
sha256 before fba5d0daaa69a1a943a883e76f0e5e1934cc053128d6fbf3b770c5a8c53a49c1
sha256 after  eacc4794a5cbeefc456104184d5c34565fd22542bccef8fdf14b6d0a77dfc0d6   (after §4 as well; line 5 changed in §6)
129	header 5 bars / row 5 bars	| Integer-error exponent β of the Diamond–Zhang random systems (DZ book Thms 1
130	header 5 bars / row 5 bars	| ↳ [PROVENANCE 2026-10-01, Session 40 — Session-39 unit `dz-half-s39`, applie
131	header 5 bars / row 5 bars	| (α, β) of the integer-greedy ℕ-supported system S5(ρ) (candidate non-surgery
132	header 5 bars / row 5 bars	| Off-line zero of S5(0.8)'s ζ_P (route 2 for α; the zero behind Theorem K′) |
133	header 5 bars / row 5 bars	| ↳ [PROVENANCE 2026-10-01, Session 40 — Session-39 unit `u-offsurgery-s39`, a
134	header 5 bars / row 5 bars	| Conjecture O at the function-field rung (degree-wise; F_q[T], RH true) | FAL
135	header 5 bars / row 5 bars	| Deterministic deletions with O (β₂ ≥ α_R/2) a theorem beyond Cor. Z.1 | unco
136	header 5 bars / row 5 bars	| Exact dyadic mean square of deterministic deletions at X = 10¹⁰ | sq = {next
137	header 5 bars / row 5 bars	| ↳ [PROVENANCE 2026-10-01, Session 40 — Session-39 unit `lemmaG-s39`, applied
```

## 3. C2 Untried — ten entries (applied 2026-10-01 12:30:24 IST)

File `directions/C2-rigidity-conservation.md`, Untried section, after its last bullet (old 182, now 195: Session 38's UT-5). Bullet
shape, as the Session-38 applier's: the dated tag "**[2026-10-01, Session 40 — Session-39 unit NOTE, `results/<unit>/NOTE.md` §N]**",
then the NOTE entry verbatim (list marker dropped, wrapped lines joined with one space; the script finds the joined text exactly once in
each target file and in no other direction file), then a bracketed note marked "not NOTE text" (NOTE lines; for an entry without a
Target line, the placement reason). The qtwin entries keep their own Session-39 tag after the Session-40 tag. Notes beyond that:
fejer-form's fourth bullet (199) is a closure record, not a new entry — its note says "UT-4" is this file's line 194 and that the NOTE's
"C2 Untried line 176" (the wave-1 bullet "Extremal characterization of ξ") is line 189 after this insertion; neither bullet was edited.
UT-U3 (200) names the B2 copy (B2 163). Draft (b) (205) is §5's.

```
sha256 before 1516b6c99c1a8c14e84fb6a535aa512237bdeff9239954796e489f2adb2b2ea1   (= after §1)
sha256 after  e4999ca778df277804607284d4a323dd38b22d425c7d60d45e1db91f8210eb08
196	Z3-Epstein (NOTE 292–293)	**Z3 on Epstein x² + 5y²** (NOTE §6). Fit: none of S1–S5 (Z3 is We
197	nonfree-g3 (NOTE 294–298)	**A non-free positions inequality at g ≥ 3** (NOTE §7: class-summe
198	HP19 (NOTE 299–300)	**HP19 at the page** (Trans. AMS 372 (2019) 5409–5451; cited here 
199	closed-UT4 (NOTE 301–304)	Closed by this unit: **UT-4** (digest §F.3) — K (NOTE §0); and, as
200	UT-U3 (NOTE 224–226)	**UT-U3 Why β ≈ 0.3.** The scatter is horizontal (§2.3): explain t
201	UT-QT1 (NOTE 381–384)	**[2026-10-01, Session 39 — `qtwin-s39`]** **UT-QT1 The one-condit
202	UT-QT2 (NOTE 385–388)	**[2026-10-01, Session 39 — `qtwin-s39`]** **UT-QT2 Route (ii)'s h
203	UT-QT3 (NOTE 389–391)	**[2026-10-01, Session 39 — `qtwin-s39`]** **UT-QT3 Mixed systems 
204	UT-QT4 (NOTE 392–393)	**[2026-10-01, Session 39 — `qtwin-s39`]** **UT-QT4 Infinitely man
205	D-b (draft, read-O §7 A4)	**A limit-periodic Hilberdink Prop. 3.4** (from read-O, single-che
```

## 4. B2 Untried — seventeen entries (applied 2026-10-01 12:30:44 IST)

File `directions/B2-refutation-program.md`, Untried section, after its last bullet (old 145, now 154: Session 38's UT-13). Same bullet
shape as §3; each unit's block in NOTE order, its draft after it. U-2 (156) carries the reader's answer (read-O §7 A1) as the dual
read amended it, and its note says so. UT-U3 (163) names the C2 copy (C2 200). Drafts (c) (160) and (a) (166) are §5's.

```
sha256 before a91114750d65decd2eff839c24a460f6540804b72f8907541a94f3f5d3079a76   (= after §2)
sha256 after  eacc4794a5cbeefc456104184d5c34565fd22542bccef8fdf14b6d0a77dfc0d6
155	U-1 (NOTE 389–391)	**U-1 The exceptional null set.** Does every subsequence of Γ sati
156	U-2 (NOTE 392–394)	**U-2 The sharp order.** lim sup |E|/(x/log x)^{1/2} = ∞ a.s. (rea
157	U-3 (NOTE 395–396)	**U-3 Remark 5.1 at the page.** Check that Broucke's ζ_c (2507.137
158	U-4 (NOTE 397–398)	**U-4 Natural boundary.** Is σ = ½ a natural boundary of ζ_B a.s. 
159	U-5 (NOTE 399–399)	**U-5 DMV's system.** Check (H1) for DMV's dΠ_C at the page; then 
160	D-c (draft, read-O §7 A2)	**Is N − ρx = O(x^{1/2}) for the Diamond–Zhang systems?** (from re
161	UT-U1 (NOTE 220–221)	**UT-U1 Decide Lemma H** for S5(0.8): sup_{u≤x}|N(u) − 0.8⌊u⌋| ≪ x
162	UT-U2 (NOTE 222–223)	**UT-U2 The 30-digit zero.** Certify ρ₁ by interval arithmetic (py
163	UT-U3 (NOTE 224–226)	**UT-U3 Why β ≈ 0.3.** The scatter is horizontal (§2.3): explain t
164	UT-U4 (NOTE 227–228)	**UT-U4 S3 and S4 (not run).** The planted pseudo-character twist 
165	UT-U5 (NOTE 229–230)	**UT-U5 What survives of U.** Conjecture O (surgery class) is unto
166	D-a (draft, read-O §7 A5, A8)	**S5(0.95): its zero and its exact multiplicity ascent** (from rea
167	UT-L1 (NOTE 369–372)	**UT-L1 The ℚ-limit of the rung-1 counterexample.** A continuous f
168	UT-L2 (NOTE 373–376)	**UT-L2 Pair-correlation input for pseudo-random deletions.** Prov
169	UT-L3 (NOTE 377–380)	**UT-L3 Membership test for 𝒞_self.** Given R, search for a model 
170	UT-L4 (NOTE 381–383)	**UT-L4 The stop-line trigger, recalibrated twice.** Restate cO's 
171	UT-L5 (NOTE 384–385)	**UT-L5 T3's Bessel law across a full period.** nsq to 10¹¹ (the n
```

## 5. The three drafted entries — each labeled "(from read-O, single-check)" (in §3–§4's insertions)

House format (idea; S1–S5 fit reason; first ladder rung; Target), tag "**[2026-10-01, Session 40 — drafted by the bookkeeping agent
from `results/<unit>/read-O.md` §7 …]**". Content is the reader's; quotations are verbatim; nothing is claimed beyond read-O.
- (a) B2 line 166, "**S5(0.95): its zero and its exact multiplicity ascent**" — from u-offsurgery read-O §7 A5 (exponent near 0.27 at
  ρ = 0.95 to 10^{38.8}, flat; A5's two sentences "If the program pursues S5 … own accumulation analysis." quoted) and A8 (the
  crossing needs β < Re ρ₁/2). Fit: S2 (whether one off-line zero of a discrete system is seen by N − ρx, Conjecture U's question);
  the entry says that "S5" there is the NOTE's design name, not the S5 fit class. First rung: the route-2 zero search for S5(0.95)'s
  ζ_P as NOTE §2.1–2.2 did for ρ = 0.8, then the ascent against Re ρ₁/2.
- (b) C2 line 205, "**A limit-periodic Hilberdink Prop. 3.4**" — from qtwin read-O §7 A4: Hilberdink 2012, Acta Arith. 152,
  Prop. 3.4 (on disk: `results/novel-wave-s37/beurling-fe/sources/p3-22c2-…`, lines 632–660, as the NOTE cites it) rules out every
  finite rational design with a non-integer atom; only infinitely many rational atoms escape; the limit-periodic version "would close
  the rational part of 𝒯" (verbatim). Fit: S1, as UT-QT1. First rung: Props. 3.2–3.4 at the page, then the atoms (p + 1)/p.
- (c) B2 line 160, "**Is N − ρx = O(x^{1/2}) for the Diamond–Zhang systems?**" — from dz-half read-O §7 A2 (DZ p. 196, θ = ½; why the
  Mellin route cannot decide it; "so O(x^{1/2}) may well hold" verbatim). The entry notes that read-O proposed it to replace U-2, while
  the NOTE kept U-2 (answer added, this question as its "still open" clause) — so the question now appears in U-2 and, stated on its
  own, here. Fit: instrument, as U-2. First rung: max_{x≤X}|E(x)|/x^{1/2} on the 10 runs on disk.

## 6. Last-touched lines — new text prepended in both files (2026-10-01 12:31:08 IST)

Line 5 of each file, changed in place (no line added), as the Session-38 applier did: "2026-10-01 (Session 40 — Session-39 units … applied
insertion-only from their dual-read NOTEs: <what>; record `results/novel-wave-s39/digest-APPLIED.md`); previously " is PREPENDED after
"**Last touched:** " and the old text follows unchanged. The script refused to write unless each file's SHA-256 equalled the
post-insertion hash of §3/§4, and checked that the new line ends with the old text byte-for-byte. The only non-insertion change.

```
directions/C2-rigidity-conservation.md
sha256 before e4999ca778df277804607284d4a323dd38b22d425c7d60d45e1db91f8210eb08
sha256 after  614e59e4740df4dfe85c264feab751162a96f6e44858ea6ca15b18f584d30db4
  prefix-only: new line ends with the old text after the label byte-for-byte = True | fields 225 -> 225
directions/B2-refutation-program.md
sha256 before eacc4794a5cbeefc456104184d5c34565fd22542bccef8fdf14b6d0a77dfc0d6
sha256 after  b9f37f495703b823e5cc17c2ff20ff719becdcbe61e9e34cf0549e439a699d14
  prefix-only: new line ends with the old text after the label byte-for-byte = True | fields 179 -> 179
```

## 7. Verification (1) — an actual `diff` against the pristine copies (2026-10-01 12:34:26 IST)

`$SCRATCH` = this agent's scratchpad; `before/` holds the copies taken at 12:20:11 IST (§0). Run from the program root, per file:
`diff "$SCRATCH/before/<file>" "directions/<file>"`; the summary keeps diff's change-command lines (`NaM,K` = lines M–K of the new file
appended after old line N; `5c5` = line 5 changed) and counts its `<` and `>` lines. Output verbatim:

```
$ diff "$SCRATCH/before/C2-rigidity-conservation.md" "directions/C2-rigidity-conservation.md"
  exit 1; change commands: 5c5 165a166,178 182a196,205 
  lines removed/changed (<): 1; lines added (>): 24; wc -l: 201 -> 224
$ diff "$SCRATCH/before/B2-refutation-program.md" "directions/B2-refutation-program.md"
  exit 1; change commands: 5c5 128a129,137 145a155,171 
  lines removed/changed (<): 1; lines added (>): 27; wc -l: 152 -> 178
$ diff -q (the other 11 direction files): 11 of 11 identical
```

Reading: in C2 and B2 every change is an append (`a`) except one `5c5`, whose single `<` line is the old Last-touched line (§6; §8 shows
the new line ends with it byte-for-byte). `>` = inserted lines + 1 (the new line 5): C2 23 + 1, B2 26 + 1.

## 8. Verification (2) — insertion-only, column counts, verbatim placement, SHA-256 (script output verbatim) (2026-10-01 12:34:38 IST)

Script `verify.py` (agent scratchpad) against the pristine copies and the 12:20 start copies. (1) difflib opcodes: only insertions, plus
the one prefix-only change of line 5 per file. (2) Every row of both Instruments tables: unescaped bars counted by the GFM rule (a bar
preceded by an odd run of backslashes is escaped) and, for comparison, by the Session-38 applier's rule (any bar directly after a
backslash); every new row has 5 bars = the header and splits into 4 cells. One pre-existing row per file is off-count under the GFM
rule only (C2 142: 11; B2 120: 7) — compared by content before and after, untouched (§10). (3) Each NOTE row (lemmaG 364 after its
declared escape) is an exact line of exactly one direction file, its target, searched across all `directions/*.md`. (4) Each NOTE
entry, wrapped lines joined with one space, is a substring of exactly the file(s) it was routed to; each draft is an exact line of its
target at the planned line, with the label. (5) The quotations the ↳ rows call verbatim occur in their NOTEs. (6) The other 11
direction files, the five NOTEs and the five read-O files are byte-identical to the copies of §0.

```
C2-rigidity-conservation.md: opcodes = 2 insert blocks [(166, 178), (196, 205)] + replace of line 5 (prefix-only = True); only insertions otherwise = True
   header bars 5; table rows 65 -> 78; new rows (line, bars): [(166, 5), (167, 5), (168, 5), (169, 5), (170, 5), (171, 5), (172, 5), (173, 5), (174, 5), (175, 5), (176, 5), (177, 5), (178, 5)]
   pre-existing off-count rows (line, GFM bars, simple bars): before [(142, 11, 5)] after [(142, 11, 5)] unchanged = True
   cells per new row: [4]
B2-refutation-program.md: opcodes = 2 insert blocks [(129, 137), (155, 171)] + replace of line 5 (prefix-only = True); only insertions otherwise = True
   header bars 5; table rows 25 -> 34; new rows (line, bars): [(129, 5), (130, 5), (131, 5), (132, 5), (133, 5), (134, 5), (135, 5), (136, 5), (137, 5)]
   pre-existing off-count rows (line, GFM bars, simple bars): before [(120, 7, 5)] after [(120, 7, 5)] unchanged = True
   cells per new row: [4]
row fejer-form-s39:281 -> [('C2', 166)] (exact-line match; directions-wide hits = 1)
row fejer-form-s39:282 -> [('C2', 167)] (exact-line match; directions-wide hits = 1)
row fejer-form-s39:283 -> [('C2', 168)] (exact-line match; directions-wide hits = 1)
row fejer-form-s39:284 -> [('C2', 169)] (exact-line match; directions-wide hits = 1)
row fejer-form-s39:285 -> [('C2', 170)] (exact-line match; directions-wide hits = 1)
row fejer-form-s39:286 -> [('C2', 171)] (exact-line match; directions-wide hits = 1)
row fejer-form-s39:287 -> [('C2', 172)] (exact-line match; directions-wide hits = 1)
row fejer-form-s39:288 -> [('C2', 173)] (exact-line match; directions-wide hits = 1)
row qtwin-s39:376 -> [('C2', 175)] (exact-line match; directions-wide hits = 1)
row qtwin-s39:377 -> [('C2', 176)] (exact-line match; directions-wide hits = 1)
row qtwin-s39:378 -> [('C2', 177)] (exact-line match; directions-wide hits = 1)
row dz-half-s39:386 -> [('B2', 129)] (exact-line match; directions-wide hits = 1)
row u-offsurgery-s39:215 -> [('B2', 131)] (exact-line match; directions-wide hits = 1)
row u-offsurgery-s39:216 -> [('B2', 132)] (exact-line match; directions-wide hits = 1)
row lemmaG-s39:364 -> [('B2', 134)] (exact-line match; directions-wide hits = 1) (escape applied)
row lemmaG-s39:365 -> [('B2', 135)] (exact-line match; directions-wide hits = 1)
row lemmaG-s39:366 -> [('B2', 136)] (exact-line match; directions-wide hits = 1)
Z3-Epstein NOTE fejer-form-s39 lines 292-293 -> [('C2', 196)] (verbatim substring, wrapped lines joined)
nonfree-g3 NOTE fejer-form-s39 lines 294-298 -> [('C2', 197)] (verbatim substring, wrapped lines joined)
HP19 NOTE fejer-form-s39 lines 299-300 -> [('C2', 198)] (verbatim substring, wrapped lines joined)
closed-UT4 NOTE fejer-form-s39 lines 301-304 -> [('C2', 199)] (verbatim substring, wrapped lines joined)
U-1 NOTE dz-half-s39 lines 389-391 -> [('B2', 155)] (verbatim substring, wrapped lines joined)
U-2 NOTE dz-half-s39 lines 392-394 -> [('B2', 156)] (verbatim substring, wrapped lines joined)
U-3 NOTE dz-half-s39 lines 395-396 -> [('B2', 157)] (verbatim substring, wrapped lines joined)
U-4 NOTE dz-half-s39 lines 397-398 -> [('B2', 158)] (verbatim substring, wrapped lines joined)
U-5 NOTE dz-half-s39 lines 399-399 -> [('B2', 159)] (verbatim substring, wrapped lines joined)
UT-U1 NOTE u-offsurgery-s39 lines 220-221 -> [('B2', 161)] (verbatim substring, wrapped lines joined)
UT-U2 NOTE u-offsurgery-s39 lines 222-223 -> [('B2', 162)] (verbatim substring, wrapped lines joined)
UT-U3 NOTE u-offsurgery-s39 lines 224-226 -> [('B2', 163), ('C2', 200)] (verbatim substring, wrapped lines joined)
UT-U4 NOTE u-offsurgery-s39 lines 227-228 -> [('B2', 164)] (verbatim substring, wrapped lines joined)
UT-U5 NOTE u-offsurgery-s39 lines 229-230 -> [('B2', 165)] (verbatim substring, wrapped lines joined)
UT-QT1 NOTE qtwin-s39 lines 381-384 -> [('C2', 201)] (verbatim substring, wrapped lines joined)
UT-QT2 NOTE qtwin-s39 lines 385-388 -> [('C2', 202)] (verbatim substring, wrapped lines joined)
UT-QT3 NOTE qtwin-s39 lines 389-391 -> [('C2', 203)] (verbatim substring, wrapped lines joined)
UT-QT4 NOTE qtwin-s39 lines 392-393 -> [('C2', 204)] (verbatim substring, wrapped lines joined)
UT-L1 NOTE lemmaG-s39 lines 369-372 -> [('B2', 167)] (verbatim substring, wrapped lines joined)
UT-L2 NOTE lemmaG-s39 lines 373-376 -> [('B2', 168)] (verbatim substring, wrapped lines joined)
UT-L3 NOTE lemmaG-s39 lines 377-380 -> [('B2', 169)] (verbatim substring, wrapped lines joined)
UT-L4 NOTE lemmaG-s39 lines 381-383 -> [('B2', 170)] (verbatim substring, wrapped lines joined)
UT-L5 NOTE lemmaG-s39 lines 384-385 -> [('B2', 171)] (verbatim substring, wrapped lines joined)
draft D-a (u-offsurgery-s39 read-O §7 A5, A8) -> [('B2', 166)] (exact line; label present = True)
draft D-b (qtwin-s39 read-O §7 A4) -> [('C2', 205)] (exact line; label present = True)
draft D-c (dz-half-s39 read-O §7 A2) -> [('B2', 160)] (exact line; label present = True)
verbatim quote in ↳ row found in qtwin-s39 NOTE: True
verbatim quote in ↳ row found in dz-half-s39 NOTE: True
verbatim quote in ↳ row found in u-offsurgery-s39 NOTE: True
verbatim quote in ↳ row found in u-offsurgery-s39 NOTE: True
verbatim quote in ↳ row found in fejer-form-s39 NOTE: True
A1-break-bandwidth.md untouched = True
A2-richer-functionals.md untouched = True
A3-families-derivatives.md untouched = True
A4-lindelof-lock.md untouched = True
B1-mult-positivity.md untouched = True
B3-arithmetic-debranges.md untouched = True
B4-zero-dynamics.md untouched = True
C1-requirements-first-field.md untouched = True
C3-geometric-substrate.md untouched = True
D1-certified-refutation-arm.md untouched = True
README.md untouched = True
NOTE fejer-form-s39 sha256 0ab5f19ed976a72ed507b271b40eb698d5b9cbfabad319214fc9eb4c406893c0 (unchanged since 12:20 = True)
NOTE dz-half-s39 sha256 51e062e9ddc3bb0edd092d1e9357e0f1c232df377c98554a826712b7d53bac3b (unchanged since 12:20 = True)
NOTE u-offsurgery-s39 sha256 ef143a4354b75580c17d619024d779de4484b0688fe886d7fce1cae9fddfc668 (unchanged since 12:20 = True)
NOTE qtwin-s39 sha256 0a7ea6be2449adf8f8a5cb5cf248e04d7c2317d6e0b9526b9fbaf2f1fa206af5 (unchanged since 12:20 = True)
NOTE lemmaG-s39 sha256 41f195d40705ae77819b9a3805cd1323f0e5b7f3468e447c4db04b9e93b65d61 (unchanged since 12:20 = True)
five NOTEs and five read-O files byte-identical to the 12:20 start copies (checked above; silent = identical)
C2-rigidity-conservation.md sha256 before 04496dce0b444d480e460d35aae3eaa78f90a1beaaaf58b85506afb524afc7bb after 614e59e4740df4dfe85c264feab751162a96f6e44858ea6ca15b18f584d30db4
B2-refutation-program.md sha256 before fba5d0daaa69a1a943a883e76f0e5e1934cc053128d6fbf3b770c5a8c53a49c1 after b9f37f495703b823e5cc17c2ff20ff719becdcbe61e9e34cf0549e439a699d14
ALL CHECKS PASS
```

## 9. Summary and SHA-256 of every file, before and after

| File | Inserted (final line numbers) | SHA-256 before | SHA-256 after |
|---|---|---|---|
| `directions/C2-rigidity-conservation.md` | rows 166–173 (fejer-form §8) + 174 (↳), 175–177 (qtwin §10.1) + 178 (↳); Untried 196–205 (fejer-form §9 ×4, UT-U3, UT-QT1 … QT4, draft (b)); line 5 prefixed | `04496dce0b444d480e460d35aae3eaa78f90a1beaaaf58b85506afb524afc7bb` | `614e59e4740df4dfe85c264feab751162a96f6e44858ea6ca15b18f584d30db4` |
| `directions/B2-refutation-program.md` | rows 129 (dz-half §6.2) + 130 (↳), 131–132 (u-offsurgery §6) + 133 (↳), 134–136 (lemmaG §6) + 137 (↳); Untried 155–171 (U-1 … U-5, draft (c), UT-U1 … U5, draft (a), UT-L1 … L5); line 5 prefixed | `fba5d0daaa69a1a943a883e76f0e5e1934cc053128d6fbf3b770c5a8c53a49c1` | `b9f37f495703b823e5cc17c2ff20ff719becdcbe61e9e34cf0549e439a699d14` |
| the other 11 `directions/*.md` | nothing (nothing routed) | as in the scratchpad copies of 12:20:11 | unchanged |
| the five NOTEs (§0) and five read-O files | read only (sources) | §0 | unchanged |

Totals: 17 NOTE rows + 5 ↳ provenance rows = 22 table rows; 23 NOTE Untried bullets in 24 lines (UT-U3 in both files) + 3 drafts =
27 Untried lines; 49 inserted lines in all; 2 Last-touched lines prefixed in place. `wc -l`: C2 201 → 224, B2 152 → 178. Diff verdict:
INSERTION-ONLY VERIFIED (§7, §11). Column check: every inserted row 5 bars = header, 4 cells (§1, §2, §8). Nothing left unplaced.

## 10. Judgment calls, what was not placed, and notes for the orchestrator

Judgment calls, stated: (a) one ↳ provenance row per source block (five), each directly under its rows, rather than one per file:
each names its own NOTE, lines and SHA-256; fejer-form's own "↳ provenance" row is NOTE content and was copied as a row, with this
agent's ↳ row after it. (b) fejer-form §9's fourth bullet ("Closed by this unit: UT-4 … 'Extremal characterization of ξ' …") has no
Target line and is a closure record, not an idea; it was copied into C2's Untried list — the brief names §9 whole, and insertion-only
leaves no other way to show next to those two C2 bullets that they are closed; its note marks it as a closure record and gives both
bullets' new line numbers (the NOTE's "C2 Untried line 176" is 189 after the insertion; the copied text keeps 176 verbatim). (c) Entries
with no Target line go to the file their NOTE's rows are written for (dz-half, lemmaG → B2; qtwin → C2). (d) UT-QT2's "Target: C2 (and
the BSS §8 classification problem)" names one file. (e) Each unit's draft sits after that unit's block. (f) The qtwin entries keep
their Session-39 tags after the Session-40 tag. (g) The one byte change: lemmaG row 364's `|E(n)|` → `\|E(n)\|` (§2), required by
the brief's escape rule; it changes no content (GFM renders `\|` as `|`).

Not placed: nothing. Outside the unit by the brief's terms: the NOTEs' waste lines, zoo riders, distance-from-upstream lines, and
read-O additions other than the three named (u-offsurgery A1–A4, A6, A7; qtwin A1–A3, A5, A6; dz-half A1 — already in U-2 — A3, A4).

For the orchestrator (pre-existing, not changed — outside this unit): C2 row 142 carries `\\|D\\|` (twice) and `\\|u\\|` (twice), and
B2 row 120 carries `\\|ρ\\|`. Under GFM `\\` is an escaped backslash and the bar after it is a live cell separator, so these rows have
11 and 7 bars against the header's 5 and render split (the Session-38 applier's simpler count read them as 5). Writing each `\\|` as
`\|` would fix both. Also: a scan of the pristine direction files, STATUS.md and KICKSTART.md found no pointer to a C2 line after 165
or a B2 line after 128, so these insertions move no existing pointer; the one stale number is inside copied text — fejer-form's
"C2 Untried line 176" (now 189), noted in its entry. Earlier ↳ rows that count "rows above" are unaffected (all insertions lie below).

## 11. Closing — insertion-only verified by an actual diff (2026-10-01 12:35:43 IST)

Run from the program root; `$SCRATCH/before/` = the pristine copies of §0. The verdict line is printed by the shell only if the diff has
no change command other than appends and `5c5`, exactly two `<` lines, and both are the old Last-touched lines.

```
$ for f in C2-rigidity-conservation.md B2-refutation-program.md; do diff "$SCRATCH/before/$f" "directions/$f"; done > all.diff
$ grep -E '^[0-9]' all.diff | tr '\n' ' '
5c5 165a166,178 182a196,205 5c5 128a129,137 145a155,171 
change commands other than appends and 5c5: 0; '<' lines: 2, of which old Last-touched lines: 2
INSERTION-ONLY VERIFIED: every change is an append, except line 5 of each file, whose old text survives byte-for-byte as the tail of the new line (§8: prefix-only = True).
```

Insertion-only verified: 49 lines inserted (17 NOTE rows, 5 ↳ provenance rows, 24 copied Untried lines, 3 drafts) and two Last-touched
lines prefixed, in `directions/C2-rigidity-conservation.md` and `directions/B2-refutation-program.md`; the other 11 direction files, the
five NOTEs and the five read-O files byte-identical to §0. No git command was run (the watchdogs commit).
