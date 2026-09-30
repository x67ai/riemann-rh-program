# digest-APPLIED — wave-2 digest §D and §F.3 applied to the direction files (KICKSTART 10(k), 10(m))

Bookkeeping agent (Opus 5.5), Session 38, 2026-10-01. Source: `results/novel-wave-s37/insights-digest.md` §D (14 Instruments rows) and §F.3
(thirteen Untried entries UT-1 … UT-13). Insertion-only; the digest's text is quoted verbatim; no git commands. Model: `results/novel-wave-s36/digest-APPLIED.md`.
Not touched: `directions/D1-certified-refutation-arm.md` and `directions/B3-arithmetic-debranges.md` (the digest routes nothing to them — §D: "No D1 row: nothing in the wave is interval-certified"; no §D block and no UT "Target:" names B3), `BARRIER-ZOO.md`, `STATUS.md`, `LOG.md`, every NOTE.md, the charter, the tournament NOTE.
Line numbers are in the file as it stands after ALL insertions of this report (final state), unless a block says otherwise.

## 0. SHA-256 before any insertion (taken 2026-10-01 04:44:00 IST)

```
e86f642a47cf4bdedad83efd61cd307b34fa55b87e60501faca2a9b3b0c6c981  results/novel-wave-s37/insights-digest.md   (source, read only; matches the expected prefix e86f642a…)
2d2e7d15a3f3af2be050361166d0f3607e21c711988ddda318f79294ad821084  directions/C2-rigidity-conservation.md
041d3410087e251dfb561936aef13ea026701a4bc96028449b4ebbc4cdcad7d8  directions/B2-refutation-program.md
03f3a544bff69702f23f16689656e1922488162b08ed5b3c850837bff2d6e612  directions/C3-geometric-substrate.md
d70138667bdceb285bfc3ae9b59d437e7acf6a3eb66c7b23d84ea65fbae344ae  directions/B3-arithmetic-debranges.md      (not touched; = wave-1 applier's "after")
6108a2102eb6194f5b53580a1aeca705df380fa6a9fe3f3b089a1a19d703643f  directions/D1-certified-refutation-arm.md   (not touched; = wave-1 applier's "after")
```

Pristine copies for the insertion-only diff check are kept in the agent's scratchpad (`before/`), not in the program tree. Before any edit, a
scan found none of the 14 rows in any `directions/*.md` and no direction file citing `novel-wave-s37` (nothing was pre-applied).

Routing, read from the digest (not chosen): §D "→ `directions/C2-…`" block = digest lines 230–235 (6 rows), "→ `directions/B2-…`" = 241–245
(5 rows), "→ `directions/C3-…`" = 251–253 (3 rows); no row's own text names another direction. §F.3 "Target:" fields: C2 ← UT-1, UT-2, UT-3,
UT-4, UT-5; B2 ← UT-3, UT-6, UT-7, UT-8, UT-9, UT-10, UT-13; C3 ← UT-11, UT-12. UT-3's Target names two files ("Target: C2 (controls); B2
(the zero as a live-fire target)"), so UT-3 is quoted in both. Every target file already has an "Instruments" table and an "Untried" section,
so no new section was created. Column shape: every §D row has 5 unescaped bars = 4 cells; every target header
("| Quantity | Current best value | Result file | Dated |") has 5 bars = 4 cells; the rows' absolute-value bars already arrive escaped as `\|`
(digest rows 233, 242, 244, 245, 251, 252), so the byte-for-byte copy already satisfies the Session-38 renderer rule and no byte was altered.

## 1. C2 Instruments — six §D rows + one ↳ provenance row (2026-10-01 04:49:21 IST)

File `directions/C2-rigidity-conservation.md`. Digest lines 230–235 copied byte-for-byte (programmatic copy, not retyped), appended after the
table's last row (old line 158, the Session-37 wave-1 ↳ PROVENANCE row) and above the Session-38 "[Renderer repair …]" note (old 159, now 166),
which stays directly under the table. Line 165 is this agent's ↳ PROVENANCE row: it names the digest with its full SHA-256 and carries,
verbatim, the block heading's parenthetical ("(positive prime data with an exact FE: Theorem T, Theorem C, Q_cond)") and the whole §D preamble
(paths relative to `results/`; status words are the sources'; "No D1 row … read-O R1's zero (C2 row 4) becomes a D1 candidate only after an
Arb/interval producer."), plus a marked bookkeeping note ("C2 row 4" = line 162 here; the seed-folder key from the digest header, verbatim).
The dry run on a scratch copy produced a byte-identical file (`cmp`). Numbers are final (every later insertion in this file lies below the table).

```
sha256 before 2d2e7d15a3f3af2be050361166d0f3607e21c711988ddda318f79294ad821084
sha256 after  e793244b858b8d29c03e7e6bbc8d2708d6d1bcea70cc8b352733b256b0c2d4a7
159	header 5 bars / row 5 bars	| Fejér defect S_F = Σ_k c_k·sinc²(λ_k) of a positive Dirichlet series (Theore
160	header 5 bars / row 5 bars	| Conductor identity (C_q): ρ_q(1 − q^{−1/2}) = 2q^{−1/2}∫sinc²(t/q)dN(t), ρ_q
161	header 5 bars / row 5 bars	| Λ-sign of the known positive-coefficient solutions at conductor q > 1 (the Q
162	header 5 bars / row 5 bars	| Signed RH-false solution of Riemann's exact FE at conductor 1 with every fre
163	header 5 bars / row 5 bars	| Continuous RH-false systems with Riemann's FE and extra poles (the orchestra
164	header 5 bars / row 5 bars	| Genus-1 admissibility over F₅ (L = 1 − tu + 5u²; the rung-1 calibration of a
165	header 5 bars / row 5 bars	| ↳ [PROVENANCE 2026-10-01, Session 38 — wave-2 digest §D, applied insertion-o
```

## 2. B2 Instruments — five §D rows + one ↳ provenance row (2026-10-01 04:49:51 IST)

File `directions/B2-refutation-program.md`. Digest lines 241–245 copied byte-for-byte, appended after the table's last row (old line 122, the
Session-37 wave-1 ↳ PROVENANCE row) and above the Session-38 "[Renderer repair …]" note (old 123, now 129). Line 128 is the ↳ PROVENANCE row:
digest path and full SHA-256; the block heading's parenthetical, verbatim ("(the visibility price of an off-line zero in the integer counting
function of a Beurling world — the IV.9 shape)"); the §D preamble's first two sentences, verbatim ("Paths relative to `results/`. Status words
are the sources'." — the third sentence concerns C2 and D1 and is carried in C2's row); the seed-folder key as a marked bookkeeping note.
Rows 124, 126 and 127 carry escaped absolute-value bars (`\|`) exactly as the digest has them. Dry run byte-identical (`cmp`). Numbers are final.

```
sha256 before 041d3410087e251dfb561936aef13ea026701a4bc96028449b4ebbc4cdcad7d8
sha256 after  c9fd84e83cb153c1b423e3e28d9c5512e011c4e90c42db9867c5dac7cc549aa8
123	header 5 bars / row 5 bars	| Integer-error exponent β of Bernoulli thinning T_α (delete p with probabilit
124	header 5 bars / row 5 bars	| Integer-error exponent of structured (greedy, \|π_R − F\| < 1) deletions of 
125	header 5 bars / row 5 bars	| Proved bounds on the frontier {α > ½, β < ½} (surgery on ℙ) | Unconditional:
126	header 5 bars / row 5 bars	| Mean-system error T(y) = Σ_{n≤y}Π_{p\|n}(1 − p^{α−1}) − y/ζ(2 − α) (gap G1 o
127	header 5 bars / row 5 bars	| Exact mean square of the integer error for a FINITE deletion R (Prop. 5.1; t
128	header 5 bars / row 5 bars	| ↳ [PROVENANCE 2026-10-01, Session 38 — wave-2 digest §D, applied insertion-o
```

## 3. C3 Instruments — three §D rows + one ↳ provenance row (2026-10-01 04:50:09 IST)

File `directions/C3-geometric-substrate.md` (not touched by the wave-1 applier; wave 2 routes rows here). Digest lines 251–253 copied
byte-for-byte, appended after the table's last row (old line 240, the Session-36 "(D4) priced" row); the blank line and the Untried heading
follow (old 241–242, now 245–246). Line 244 is the ↳ PROVENANCE row: digest path and full SHA-256; the block heading's parenthetical, verbatim
("(the rung-1 anatomy: where each proof of RH for curves separates the virtual curve from a curve)"); the §D preamble's first two sentences,
verbatim; the seed-folder key as a marked bookkeeping note. Rows 241–242 carry escaped `\|` exactly as the digest has them. The table's two
pre-existing off-count rows (lines 228 and 233, older rows; cause stated in §10) are outside this unit and untouched.
Dry run byte-identical (`cmp`). Numbers are final.

```
sha256 before 03f3a544bff69702f23f16689656e1922488162b08ed5b3c850837bff2d6e612
sha256 after  f1045aec865e4acf26e3b0d7496dde37b0004794733197189947cbbe9e4bfbae
241	header 5 bars / row 5 bars	| The virtual curve V = (5, 5) against each positivity inequality of Theorem P
242	header 5 bars / row 5 bars	| V₂ — the rung-1 twin for ONE-SIDED mechanisms (genus 2, non-real off-line ro
243	header 5 bars / row 5 bars	| Chebyshev-type auxiliary integers F_x = Π_k(⌊x/k⌋!)^{c_k} (Lemma Z4; class C
244	header 5 bars / row 5 bars	| ↳ [PROVENANCE 2026-10-01, Session 38 — wave-2 digest §D, applied insertion-o
```

## 4. C2 Untried — five §F.3 entries, UT-1 … UT-5 (2026-10-01 04:51:46 IST)

File `directions/C2-rigidity-conservation.md`, Untried section, after its last bullet (old line 169, now 176: the wave-1 "Krein–Langer transport
as a theorem (lemma L2)" bullet). Entries UT-1 … UT-5 (digest lines 404–421); each "Target:" names C2 (UT-3's names C2 and B2 — quoted in both).
Each bullet: the dated tag "[2026-10-01, Session 38 — wave-2 digest, `results/novel-wave-s37/insights-digest.md` §F.3]", then the digest entry
verbatim with its UT number (list marker dropped, wrapped lines joined with one space; checked by script: the joined text occurs exactly once in
the file), then a bracketed note marked "not digest text": the digest lines, the §F.3 preface "the fit reasons are this digest's reading of the
cited lines, not new claims", the seed-folder key; UT-3 adds the two-file note; UT-4 adds the pointer to wave-1's "Extremal characterization
of ξ" bullet (line 175 here) and the digest's §F.3 closing line verbatim ("… UT-4 is the concrete instance of the first."). Dry run
byte-identical (`cmp`). Numbers are final.

```
sha256 before e793244b858b8d29c03e7e6bbc8d2708d6d1bcea70cc8b352733b256b0c2d4a7
sha256 after  98d789784d1514f393aca0ecabadb2b8bb01d8d4eae773f10c1d7c085eb6597b
inserted after line 176 (- **[2026-09-30, Session 37 — wave-1 digest, `resu)
177	UT-1 (digest 404–407)	**UT-1 Discrete Beurling systems with Riemann's FE and finitely many e
178	UT-2 (digest 408–410)	**UT-2 Can (G′) be dropped for dN ≥ 0?** (read-O R4(2); fe/NOTE.md §5(
179	UT-3 (digest 411–414)	**UT-3 Classify the signed solutions with the gap** (fe/NOTE.md:247–25
180	UT-4 (digest 415–419)	**UT-4 The Fejér defect as a positive form, transported to the zeros**
181	UT-5 (digest 420–421)	**UT-5 Double pole at s = 1 with Riemann's Γ-factor** (fe/NOTE.md §8(f
```

## 5. B2 Untried — seven §F.3 entries: UT-3, UT-6, UT-7, UT-8, UT-9, UT-10, UT-13 (2026-10-01 04:52:09 IST)

File `directions/B2-refutation-program.md`, Untried section, after its last bullet (old line 131, now 137: "M5 restated distributionally or
demoted to a remark"). Order = the digest's order. Each "Target:" names B2 (UT-3's names C2 and B2; the C2 copy is §4's line 179). Same bullet
shape as §4. Added notes (marked "not digest text"): UT-3 the two-file note; UT-6 "ranked unit U5b is the digest's §F.2 item 6 (digest lines
396–399)"; UT-10 "ranked unit U5a is the digest's §F.2 item 4 (digest lines 383–387)" — the two one-line entries point into §F.2 and carry no
fit reason of their own, so the note says where the content is; UT-13 "`conj-O-s38` is `results/conj-O-s38/`". Dry run byte-identical (`cmp`).
Numbers are final.

```
sha256 before c9fd84e83cb153c1b423e3e28d9c5512e011c4e90c42db9867c5dac7cc549aa8
sha256 after  9263eab6c31d85fcc9fad126fe1fdabf83ca2d532df6f46e8bae051502720de1
inserted after line 137 (- **M5 restated distributionally or demoted to a r)
138	UT-3 (digest 411–414)	**UT-3 Classify the signed solutions with the gap** (fe/NOTE.md:247–25
139	UT-6 (digest 422–422)	**UT-6 Gap G1 under RH** = ranked unit U5b (§F.2 item 6). Target: B2. 
140	UT-7 (digest 423–424)	**UT-7 Gap G2 — moments of the Bernoulli chaos Σ_d μ_η(d)T_d(x/d)** (f
141	UT-8 (digest 425–428)	**UT-8 Conjecture R's unconditional form as a zero detector** (fr/NOTE
142	UT-9 (digest 429–432)	**UT-9 Conjecture U off the surgery class** (fr/NOTE.md:480–482; fr re
143	UT-10 (digest 433–433)	**UT-10 The A3 lemma** = ranked unit U5a (§F.2 item 4). Target: B2. [B
144	UT-13 (digest 442–443)	**UT-13 Prior art for Prop. 5.1** (a Franel-type exact mean square for
```

## 6. C3 Untried — two §F.3 entries, UT-11 and UT-12 (2026-10-01 04:52:29 IST)

File `directions/C3-geometric-substrate.md`, Untried section, after its last non-blank line (old line 254, now 258: the Session-36 "(D4)
priced" bullet). UT-11's "Target:" reads "C3 (nearest; no direction owns class C — open a direction file only if U-C1 returns a candidate)"
and is quoted whole; UT-12's reads "C3". Same bullet shape as §4. Added note on UT-11 (marked "not digest text"): "U4 and its rung U-C1 are
the digest's §F.2 item 3 (digest lines 374–382); "class C" is the class of that name in Theorem P's partition (digest §A.3), not a
direction". Dry run byte-identical (`cmp`). Numbers are final.

```
sha256 before f1045aec865e4acf26e3b0d7496dde37b0004794733197189947cbbe9e4bfbae
sha256 after  da92237131126a5e2c84223cdc17e8d8759589f14c257648f4f871fdccc777d6
inserted after line 258 (- **[2026-09-30, Session 36 — (D4) priced, `result)
259	UT-11 (digest 434–437)	**UT-11 Is there any finite auxiliary-integer certificate of a zero-fr
260	UT-12 (digest 438–441)	**UT-12 The unread rows of Theorem P** (pm/NOTE.md:220–224, R14; R5; R
```

## 7. Last-touched lines — new date prepended in all three files (2026-10-01 04:53:03 IST)

Line 5 of each file, changed in place (no line added), exactly as the wave-1 applier did (its §8): the new text "2026-10-01 (Session 38 — wave-2
digest `results/novel-wave-s37/insights-digest.md` §D/§F.3 applied, insertion-only: <what>; record `results/novel-wave-s37/digest-APPLIED.md`);
previously " is PREPENDED after "**Last touched:** " and the old text follows unchanged (checked by script: the line ends with the old text
byte-for-byte). The script refused to write unless each file's SHA-256 equalled the hash left by §4–§6. Its "lines N -> N" counts newline-split
fields (= `wc -l` + 1). This is the only non-insertion change of the unit; §8 checks it.

```
directions/C2-rigidity-conservation.md
sha256 before 98d789784d1514f393aca0ecabadb2b8bb01d8d4eae773f10c1d7c085eb6597b
sha256 after  7de98cc7d33562518ebc85174d4fcad54f5c07b0858961d677854fba93527be9
5	**Last touched:** 2026-10-01 (Session 38 — wave-2 digest `results/novel-wave-s37/insights-digest.md` §D/§F.3 applied, insertion-only: six §D Instrumen …
	prefix-only: new line ends with the old text after "**Last touched:** " byte-for-byte = True; lines 201 -> 201
directions/B2-refutation-program.md
sha256 before 9263eab6c31d85fcc9fad126fe1fdabf83ca2d532df6f46e8bae051502720de1
sha256 after  a7d7aa48565e466747a93bbc0dd003cc4a563a0cc125262b69899eb1961431d9
5	**Last touched:** 2026-10-01 (Session 38 — wave-2 digest `results/novel-wave-s37/insights-digest.md` §D/§F.3 applied, insertion-only: five §D Instrume …
	prefix-only: new line ends with the old text after "**Last touched:** " byte-for-byte = True; lines 152 -> 152
directions/C3-geometric-substrate.md
sha256 before da92237131126a5e2c84223cdc17e8d8759589f14c257648f4f871fdccc777d6
sha256 after  988ccdf3ab4d5f1af298f6e9cd80a150c7bb85c28f00c5f4d55cd1e8d2fc3ce7
5	**Last touched:** 2026-10-01 (Session 38 — wave-2 digest `results/novel-wave-s37/insights-digest.md` §D/§F.3 applied, insertion-only: three §D Instrum …
	prefix-only: new line ends with the old text after "**Last touched:** " byte-for-byte = True; lines 300 -> 300
```

## 8. Verification (1) — an actual `diff` against the pristine copies (2026-10-01 04:53:32 IST)

`$SCRATCH` = this agent's scratchpad; `before/` holds the copies taken at 04:44:00 IST (§0). Command, run from the program root, per file:
`diff "$SCRATCH/before/<file>" "directions/<file>"`; the summary keeps diff's change-command lines (`NaM,K` = lines M–K of the new file appended
after old line N; `5c5` = line 5 changed) and counts its `<` and `>` lines. Output verbatim:

```
$ diff "$SCRATCH/before/C2-rigidity-conservation.md" "directions/C2-rigidity-conservation.md"
  exit 1; change commands: 5c5 158a159,165 169a177,181 
  lines removed/changed (<): 1; lines added (>): 13; wc -l: 188 -> 200
$ diff "$SCRATCH/before/B2-refutation-program.md" "directions/B2-refutation-program.md"
  exit 1; change commands: 5c5 122a123,128 131a138,144 
  lines removed/changed (<): 1; lines added (>): 14; wc -l: 138 -> 151
$ diff "$SCRATCH/before/C3-geometric-substrate.md" "directions/C3-geometric-substrate.md"
  exit 1; change commands: 5c5 240a241,244 254a259,260 
  lines removed/changed (<): 1; lines added (>): 7; wc -l: 293 -> 299
$ diff "$SCRATCH/before/B3-arithmetic-debranges.md" "directions/B3-arithmetic-debranges.md"
  exit 0; change commands: 
  lines removed/changed (<): 0; lines added (>): 0; wc -l: 104 -> 104
$ diff "$SCRATCH/before/D1-certified-refutation-arm.md" "directions/D1-certified-refutation-arm.md"
  exit 0; change commands: 
  lines removed/changed (<): 0; lines added (>): 0; wc -l: 237 -> 237
```

Reading: in C2, B2 and C3 every change is an append (`a`) except one `5c5`, whose single `<` line is the old Last-touched line (§7; §9 shows
the new line ends with it byte-for-byte). `>` = inserted lines + 1 (the new line 5): C2 12 + 1, B2 13 + 1, C3 6 + 1. B3 and D1: exit 0, identical.

## 9. Verification (2) — insertion-only, column counts, verbatim placement, SHA-256 (script output verbatim) (2026-10-01 04:53:56 IST)

Script `verify.py` (agent scratchpad) against the pristine copies. (1) difflib opcodes: only insertions, plus the one prefix-only change of
line 5 per file. (2) Every row of every touched Instruments table: cell count by unescaped `|` (GFM: `\|` is a literal pipe); every new row has
5 bars = the header. C3 carries two PRE-EXISTING off-count rows (line 228, 6 bars; line 233, 4 bars — older rows; cause stated in
§10); they are compared by content before and after and are untouched. (3) Each §D row is an exact line of exactly one direction file —
the one the digest names — searched across all of `directions/*.md`; each UT entry (wrapped lines joined with one space) is a substring of
exactly the file(s) its "Target:" names, once per file. (4) The digest, B3 and D1 are byte-identical to §0.

```
C2-rigidity-conservation.md: opcodes = 2 insert blocks [(159, 165), (177, 181)] + replace of line 5 (prefix-only = True); only insertions otherwise = True
   header bars 5; table rows 60 -> 67; new rows (line, bars): [(159, 5), (160, 5), (161, 5), (162, 5), (163, 5), (164, 5), (165, 5)]
   pre-existing off-count rows (bars): before [] after [] unchanged = True
   sha256 before 2d2e7d15a3f3af2be050361166d0f3607e21c711988ddda318f79294ad821084
   sha256 after  7de98cc7d33562518ebc85174d4fcad54f5c07b0858961d677854fba93527be9
B2-refutation-program.md: opcodes = 2 insert blocks [(123, 128), (138, 144)] + replace of line 5 (prefix-only = True); only insertions otherwise = True
   header bars 5; table rows 21 -> 27; new rows (line, bars): [(123, 5), (124, 5), (125, 5), (126, 5), (127, 5), (128, 5)]
   pre-existing off-count rows (bars): before [] after [] unchanged = True
   sha256 before 041d3410087e251dfb561936aef13ea026701a4bc96028449b4ebbc4cdcad7d8
   sha256 after  a7d7aa48565e466747a93bbc0dd003cc4a563a0cc125262b69899eb1961431d9
C3-geometric-substrate.md: opcodes = 2 insert blocks [(241, 244), (259, 260)] + replace of line 5 (prefix-only = True); only insertions otherwise = True
   header bars 5; table rows 24 -> 28; new rows (line, bars): [(241, 5), (242, 5), (243, 5), (244, 5)]
   pre-existing off-count rows (bars): before [4, 6] after [(228, 6), (233, 4)] unchanged = True
   sha256 before 03f3a544bff69702f23f16689656e1922488162b08ed5b3c850837bff2d6e612
   sha256 after  988ccdf3ab4d5f1af298f6e9cd80a150c7bb85c28f00c5f4d55cd1e8d2fc3ce7
§D row digest line 230 -> [('C2', 159)] (exact-line match; directions-wide hits = 1)
§D row digest line 231 -> [('C2', 160)] (exact-line match; directions-wide hits = 1)
§D row digest line 232 -> [('C2', 161)] (exact-line match; directions-wide hits = 1)
§D row digest line 233 -> [('C2', 162)] (exact-line match; directions-wide hits = 1)
§D row digest line 234 -> [('C2', 163)] (exact-line match; directions-wide hits = 1)
§D row digest line 235 -> [('C2', 164)] (exact-line match; directions-wide hits = 1)
§D row digest line 241 -> [('B2', 123)] (exact-line match; directions-wide hits = 1)
§D row digest line 242 -> [('B2', 124)] (exact-line match; directions-wide hits = 1)
§D row digest line 243 -> [('B2', 125)] (exact-line match; directions-wide hits = 1)
§D row digest line 244 -> [('B2', 126)] (exact-line match; directions-wide hits = 1)
§D row digest line 245 -> [('B2', 127)] (exact-line match; directions-wide hits = 1)
§D row digest line 251 -> [('C3', 241)] (exact-line match; directions-wide hits = 1)
§D row digest line 252 -> [('C3', 242)] (exact-line match; directions-wide hits = 1)
§D row digest line 253 -> [('C3', 243)] (exact-line match; directions-wide hits = 1)
UT-1 digest lines 404-407 -> [('C2', 177)] (verbatim substring, wrapped lines joined)
UT-2 digest lines 408-410 -> [('C2', 178)] (verbatim substring, wrapped lines joined)
UT-3 digest lines 411-414 -> [('B2', 138), ('C2', 179)] (verbatim substring, wrapped lines joined)
UT-4 digest lines 415-419 -> [('C2', 180)] (verbatim substring, wrapped lines joined)
UT-5 digest lines 420-421 -> [('C2', 181)] (verbatim substring, wrapped lines joined)
UT-6 digest lines 422-422 -> [('B2', 139)] (verbatim substring, wrapped lines joined)
UT-7 digest lines 423-424 -> [('B2', 140)] (verbatim substring, wrapped lines joined)
UT-8 digest lines 425-428 -> [('B2', 141)] (verbatim substring, wrapped lines joined)
UT-9 digest lines 429-432 -> [('B2', 142)] (verbatim substring, wrapped lines joined)
UT-10 digest lines 433-433 -> [('B2', 143)] (verbatim substring, wrapped lines joined)
UT-11 digest lines 434-437 -> [('C3', 259)] (verbatim substring, wrapped lines joined)
UT-12 digest lines 438-441 -> [('C3', 260)] (verbatim substring, wrapped lines joined)
UT-13 digest lines 442-443 -> [('B2', 144)] (verbatim substring, wrapped lines joined)
digest sha256 e86f642a47cf4bdedad83efd61cd307b34fa55b87e60501faca2a9b3b0c6c981 (read only)
B3-arithmetic-debranges.md untouched = True
D1-certified-refutation-arm.md untouched = True
ALL CHECKS PASS
```

## 10. Summary and SHA-256 of every file, before and after (hashes re-taken 2026-10-01 04:54:34 IST)

| File | Inserted (final line numbers) | SHA-256 before | SHA-256 after |
|---|---|---|---|
| `directions/C2-rigidity-conservation.md` | rows 159–164 (§D, digest 230–235) + 165 (↳ provenance); Untried 177–181 (UT-1 … UT-5); line 5 prefixed | `2d2e7d15a3f3af2be050361166d0f3607e21c711988ddda318f79294ad821084` | `7de98cc7d33562518ebc85174d4fcad54f5c07b0858961d677854fba93527be9` |
| `directions/B2-refutation-program.md` | rows 123–127 (§D, digest 241–245) + 128 (↳ provenance); Untried 138–144 (UT-3, UT-6, UT-7, UT-8, UT-9, UT-10, UT-13); line 5 prefixed | `041d3410087e251dfb561936aef13ea026701a4bc96028449b4ebbc4cdcad7d8` | `a7d7aa48565e466747a93bbc0dd003cc4a563a0cc125262b69899eb1961431d9` |
| `directions/C3-geometric-substrate.md` | rows 241–243 (§D, digest 251–253) + 244 (↳ provenance); Untried 259–260 (UT-11, UT-12); line 5 prefixed | `03f3a544bff69702f23f16689656e1922488162b08ed5b3c850837bff2d6e612` | `988ccdf3ab4d5f1af298f6e9cd80a150c7bb85c28f00c5f4d55cd1e8d2fc3ce7` |
| `directions/B3-arithmetic-debranges.md` | nothing (nothing routed) | `d70138667bdceb285bfc3ae9b59d437e7acf6a3eb66c7b23d84ea65fbae344ae` | unchanged |
| `directions/D1-certified-refutation-arm.md` | nothing (§D: "No D1 row") | `6108a2102eb6194f5b53580a1aeca705df380fa6a9fe3f3b089a1a19d703643f` | unchanged |
| `results/novel-wave-s37/insights-digest.md` | read only (source) | `e86f642a47cf4bdedad83efd61cd307b34fa55b87e60501faca2a9b3b0c6c981` | unchanged |

Totals: 14 §D rows + 3 ↳ provenance rows (one per table) + 14 §F.3 Untried bullets (13 entries; UT-3 in two files) = 31 inserted lines;
3 Last-touched lines prefixed in place. Line counts (`wc -l`): C2 188 → 200, B2 138 → 151, C3 293 → 299. No new section was created
(all three files already had "Instruments" and "Untried"). Also written by this agent: this record, and blocks 9–14 of `SHARED.md` (this folder).

Judgment calls, stated: (a) UT-3's "Target:" names two files ("C2 (controls); B2 (the zero as a live-fire target)"), so the entry is quoted
verbatim in both, each copy naming the other; (b) the three ↳ PROVENANCE rows are this agent's addition in the house ↳ convention — they name
the digest with its full SHA-256 and carry, verbatim, the §D framing the rows lose when moved (the block heading's parenthetical; the preamble
"Paths relative to `results/`. Status words are the sources'." — for C2 the whole preamble, whose third sentence is about "C2 row 4"), plus a
marked bookkeeping note with the digest header's seed-folder key (rows after the first in each block abbreviate paths to `beurling-fe/`,
`beurling-frontier/`, `proof-mine/`); (c) each Untried bullet ends with a bracketed note marked "not digest text" (digest lines, the §F.3 preface,
the folder key; UT-6 and UT-10 — one-line entries that defer to §F.2 — point to the §F.2 item's digest lines; UT-4 points to wave-1's
"Extremal characterization of ξ" bullet and quotes §F.3's closing line; UT-11 says where U4/U-C1 are and that "class C" is Theorem P's class,
not a direction; UT-13 expands `conj-O-s38`); (d) the Last-touched prefix (§7) follows the wave-1 applier's §8 — it is the one change that is
not an insertion, and §8–§9 prove it prefix-only; (e) in C2 and B2 the rows go after the table's last `|` row, above the Session-38
"[Renderer repair …]" note.

Not applied, why: no §D row was left out — all 14 matched their target header (5 bars / 5 bars) and none needed a byte changed. Outside the
unit by its terms: §F.3's two trailing lines — 444 "Folded, not listed separately: …" (folds into ranked units U2 and U1, not Untried entries)
and 445 "Wave-1's six Untried entries … remain Untried …" (a status line; quoted inside UT-4's note, not entered as an entry); §F.1–§F.2 (the
funding ranking) and §A–§C, §E, §G. `BARRIER-ZOO.md`, `STATUS.md`, `LOG.md`, the NOTEs, the charter and the tournament NOTE were not opened
for writing. No git command was run (the watchdogs commit).

For the orchestrator (pre-existing, not changed — outside this unit): in C2 (line 166) and B2 (line 129) the Session-38 "[Renderer repair …]"
note sits directly under the table with no blank line between; under GFM a non-blank line right after a table row is read as one more table
row, so each note renders as a one-cell row. One blank line inserted above each note would end the table where intended. C3 (no renderer
note) has two off-count rows: 228 has an unescaped divisibility bar inside a cell ("gcd{d | n, d > 1}", 6 bars), and 233 has 3 cells, one
separator short (its absolute-value bars are already escaped).

## 11. Closing — insertion-only verified by an actual diff (2026-10-01 04:55:46 IST)

Run from the program root; `$SCRATCH/before/` = the pristine copies of §0. The verdict line is printed by the shell only if the diff has no
change command other than appends and `5c5`, exactly three `<` lines, and all three are the old Last-touched lines.

```
$ for f in C2-rigidity-conservation.md B2-refutation-program.md C3-geometric-substrate.md; do diff "$SCRATCH/before/$f" "directions/$f"; done > all.diff
$ grep -E '^[0-9]' all.diff | tr '\n' ' '
5c5 158a159,165 169a177,181 5c5 122a123,128 131a138,144 5c5 240a241,244 254a259,260 
change commands other than appends and 5c5: 0; '<' lines: 3, of which old Last-touched lines: 3
INSERTION-ONLY VERIFIED: every change is an append, except line 5 of each file, whose old text survives byte-for-byte as the tail of the new line (§9: prefix-only = True).
```

Insertion-only verified: 31 lines inserted (14 §D rows, 3 ↳ provenance rows, 14 Untried bullets) and three Last-touched lines prefixed, in
`directions/C2-rigidity-conservation.md`, `directions/B2-refutation-program.md` and `directions/C3-geometric-substrate.md`; B3, D1 and the
digest byte-identical to §0. No git command was run.
