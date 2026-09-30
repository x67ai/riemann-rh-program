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
pre-existing off-count rows (lines 228 and 233, older rows not repaired by the Session-38 renderer pass) are outside this unit and untouched.
Dry run byte-identical (`cmp`). Numbers are final.

```
sha256 before 03f3a544bff69702f23f16689656e1922488162b08ed5b3c850837bff2d6e612
sha256 after  f1045aec865e4acf26e3b0d7496dde37b0004794733197189947cbbe9e4bfbae
241	header 5 bars / row 5 bars	| The virtual curve V = (5, 5) against each positivity inequality of Theorem P
242	header 5 bars / row 5 bars	| V₂ — the rung-1 twin for ONE-SIDED mechanisms (genus 2, non-real off-line ro
243	header 5 bars / row 5 bars	| Chebyshev-type auxiliary integers F_x = Π_k(⌊x/k⌋!)^{c_k} (Lemma Z4; class C
244	header 5 bars / row 5 bars	| ↳ [PROVENANCE 2026-10-01, Session 38 — wave-2 digest §D, applied insertion-o
```
