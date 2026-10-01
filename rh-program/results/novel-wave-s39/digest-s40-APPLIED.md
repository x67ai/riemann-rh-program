# digest-s40-APPLIED — the wave-3 digest's §D rows, §G Untried entries and record residues R1–R6 applied (Session 41)

Applier agent (Opus 5.5), Session 41, started 17:35 IST 2026-10-01. Source of truth: `results/novel-wave-s39/insights-digest.md`
(SHA-256 f6464e2e…, read only): §D (16 Instruments rows, digest lines 426–441), §G (22 Untried entries, 595–681), §E's residues R1–R6.
Model: `results/novel-wave-s39/digest-APPLIED.md` (pristine copies, guarded programmatic copy, bar counts, prefix-only Last-touched).
Rows and entries are copied byte-for-byte from the digest by script (never retyped). No git command run except the read-only
`git diff --numstat` / `git status --short` of §6. Not touched: BARRIER-ZOO.md, STATUS.md, LOG.md, the digest, `results/lemmaB-s41/`,
`results/purge-s41/`, every other direction file. Line numbers are in the files as they stand after all edits, unless a line says otherwise.

## 0. SHA-256 before any edit (taken 17:30 IST 2026-10-01; pristine copies in the agent's scratchpad `before/`)

```
fe95057ff8809f60e1655598cc1d37077fbe27514a8cd7bce66e7dc867be29d4  directions/B2-refutation-program.md
8a055953cb39420d903b087d0dff4a1c931fede5b798e845b7bc707ff91d6248  directions/C2-rigidity-conservation.md
579f22e3e8114d0468cc4de559d4c739970cb8202f03e31af2e88e20cef87bdd  results/qcond-s38/NOTE.md
9c5a8886183aff933597d6962fc304c9b64c0a3c69960ad809c95643ebe50d1d  results/free-greedy-s40/theory/NOTE.md   (= digest's fgT hash)
ef143a4354b75580c17d619024d779de4484b0688fe886d7fce1cae9fddfc668  results/u-offsurgery-s39/NOTE.md
ca102d858fd71faff5282896cfed6ab8f91be0de183b5b9c145ad6b764b560af  results/s5-multiplicity-s40/NOTE.md      (= digest's s5m hash)
e8dc8e876d83de522c34d173948c012c2286c331e17f5c49619a803209b60e97  results/local-greedy-s40/NOTE.md          (= digest's lg hash)
445cfe96dcb7d4ca4a7887cbbc0c2ea3dd033a8cdf4c3932123bfd63115fb54f  results/qcond-s38/NOTE.pre-reader.md     (read only)
```

Routing, read from the digest (not chosen): §D's "Target:" line sends all 16 rows to B2's Instruments (header
"| Quantity | Current best value | Result file | Dated |", 5 bars = 4 cells). §G's per-entry "Target:" lines send 19 entries to B2
and 3 (UT-F5, UT-M5, UT-LG5) to C2, matching the digest's count line (682). §D gives no ↳ rows, so none were added. Duplicate check
(grep, before any edit): none of the 22 names UT-F1…F5, UT-C1…C4, UT-M1…M5, UT-LG0…LG7, nor `free-greedy-s40`,
`s5-multiplicity-s40`, `local-greedy-s40`, `S8(`, `S7(`, occurs in B2 or C2 — nothing was pre-applied.

## 1. B2 Instruments — 16 rows (§D) appended after the last row (old line 137), applied 17:36:48 IST 2026-10-01

Inserted at B2 lines 138–153 (one pure-add hunk `137a138,153`), byte-identical to digest 426–441 (script check). Bar count:
header (B2 line 102) = 5 unescaped bars; every inserted row = 5 (4 cells). Escaped `\|` (absolute values) kept as in the digest.

```
B2 line  digest  bars  esc  first cell (truncated)
    138     426     5    0  Real zero of ζ_P for the free greedy system S8(ρ) (Theor
    139     427     5    0  Integer error of S8(ρ) in the U-relevant range ρ < ¼ (Le
    140     428     5    0  Law of E of S8 vs the Poisson-queue heuristic (tail e^{−
    141     429     5    0  Mertens law and Legendre remainder of S8 (the sieve marg
    142     430     5    0  S8(π/4) integer error sup_{u≤x}E(u) (numerical; not an e
    143     431     5    0  S8(π/4) rightmost zero of F_X, t ≤ 5000
    144     432     5   10  Rouché margin for ρ₁ as a zero of ζ_P(S8(π/4)) (box \|σ 
    145     433     5    0  α(S8(π/4)) by the explicit formula
    146     434     5    0  S8 generator capacity and ordering proof
    147     435     5    0  Certified multiplicity of S5(0.8) beyond the computed ra
    148     436     5    0  Exact S5(0.8) beyond 10⁹
    149     437     5    0  Growth of max a_n (S5(0.8)): exponent of the exact lower
    150     438     5    4  (α, β) of the prime-local integer-greedy system S7(ρ) (g
    151     439     5    2  Off-line zeros of S7(0.6)'s F_X (route 2; the zeros behi
    152     440     5    4  (α, β) of the capped prime-local system S7^{≤2}(ρ) (m_n 
    153     441     5    2  Lemma H₇ on the computed range (the one hypothesis of Th
```

## 2. Untried — 22 entries (§G), applied 17:36:48 IST 2026-10-01

Copied verbatim with the digest's names and line wrapping (bullet + two-space continuation lines; renders as one list item),
in the digest's order, after the last existing entry of each "Untried" section. Script check: B2 188–261 equal the 74 §G lines
outside the three C2 blocks; C2 206–218 equal those 13 lines. Pure-add hunks: B2 `171a188,261` (old numbering), C2 `205a206,218`.
These are list bullets, not table rows: their 18 absolute-value bars need no escape and were left as in the digest.

```
B2-refutation-program.md (19, after old line 171 = line 187 after §1):
  UT-F1 d595→188–193;  UT-F2 d601→194–198;  UT-F3 d606→199–203;  UT-F4 d611→204–206
  UT-C1 d619→207–212;  UT-C2 d625→213–215;  UT-C3 d628→216–218;  UT-C4 d631→219–221
  UT-M1 d634→222–225;  UT-M2 d638→226–229;  UT-M3 d642→230–232;  UT-M4 d645→233–236
  UT-LG0 d653→237–241;  UT-LG1 d658→242–244;  UT-LG2 d661→245–248;  UT-LG3 d665→249–252
  UT-LG4 d669→253–255;  UT-LG6 d676→256–258;  UT-LG7 d679→259–261
C2-rigidity-conservation.md (3, after line 205):
  UT-F5 d614→206–210;  UT-M5 d649→211–214;  UT-LG5 d672→215–218
```
(dNNN = digest line where the entry starts; a–b = its lines in the direction file.)

## 3. Last-touched lines — new text prepended (the one permitted replacement per file), 17:37 IST 2026-10-01

Line 5 of each file, changed in place (no line added): "17:37 IST 2026-10-01 (Session 41 — … ; record
`results/novel-wave-s39/digest-s40-APPLIED.md`); previously " is inserted after "**Last touched:** " and the old text follows
byte-for-byte (script-checked). The script refused to write unless each file still had its post-§1/§2 SHA-256.

```
directions/B2-refutation-program.md 
  sha256 before 92b1c30a54b4dbc9576558915170e9e85dfc1da5395e5ef1fd9f691da353ad13 
  sha256 after  5cbd0110876d3849aa498e5425aa4335849b1484d2f031d08599fb663204bc47 
  prefix-only = True; lines 269 ; prepended chars 509
directions/C2-rigidity-conservation.md 
  sha256 before 6f4783411abf5764f0191e5ad2f03e22a239b346dd2a50d7329e73da71a5fcd8 
  sha256 after  fc3af79c6c5c2e2fa99da9901680bd66185647d3356e86ad8929848ef65d9d7d 
  prefix-only = True; lines 238 ; prepended chars 323
stamp 17:37 IST 2026-10-01
```

## 4. R1 and R2 — `results/qcond-s38/NOTE.md` (copy first: `NOTE.pre-repair-s41.md`, SHA-256 579f22e3…), applied 17:38:37 IST

Script-checked before writing: the 7-line block "THEOREM D. A discrete Beurling system … (2) §2.6(b): the classes [x] (x ∈ 𝒩)
form a finite group" starts exactly at old lines 219, 252, 335, 351, 451, and the five copies are byte-identical. NOTE 472 → 445 lines
(trailing newline counted). `diff NOTE.pre-repair-s41.md NOTE.md`: `219,225c219` `252,258d245` `351,357d337` `439c419` `451,457d430`.

**R1, kept copy.** Old 335–341 (now 322–328), §2.7 — Theorem D's home ("THEOREM D (§2.7)"), and the only copy continued by the rest
of the proof: old 342–350 (now 329–337), "Γ ⊂ R_{>0}/Q_{>0}. (3) … (6) Theorem L′: q = 1, P̃ ≡ 1; BFE Theorem T: the rational primes. ∎".
The digest's "complete proof is at 351–358ff" is a line slip: the 351 copy stops at step (2) and is followed by a blank line and §3.

**R1, removed copies.** Old 252–258 (§2.4, between Corollary U2 and §2.5); old 351–357 (§2.7, after the complete proof); old 451–457
(§5, between the T list and the G residue — the digest's "at 458 the G residue follows step (2)" is gone: now T list → line 431 G).

**R1, restored sentence (OLD/NEW at line 219).**
BEFORE (pre-repair 218–226):
```
218: measure m has finitely many atoms, all radical-frequency multipliers such as ζ(s)(1 + a·2^{−s/2} + √2·2^{−s}). It strengthens BFE
219: THEOREM D. A discrete Beurling system (multiset P of reals > 1, integer multiplicities) whose Λ_F
220–225: [the rest of the 7-line block, ending "(2) §2.6(b): the classes [x] (x ∈ 𝒩) form a finite group"]
226: [blank]   227: ### 2.4 THEOREM U_q — …
```
AFTER (218–221):
```
218: measure m has finitely many atoms, all radical-frequency multipliers such as ζ(s)(1 + a·2^{−s/2} + √2·2^{−s}). It strengthens BFE
219: §11(i) (finite Euler factors) to all finite Dirichlet-polynomial multipliers. `[novelty: single-check]`
220: [blank]   221: ### 2.4 THEOREM U_q — …
```
New line 219 is `NOTE.pre-reader.md` line 216 byte-for-byte (script-checked; pre-reader 215 ends "It strengthens BFE" like line 218).

**R2 (label; old 439, now line 419).** The digest names the conflict and its sources (NOTE:435 now 415 "`[novelty: dual-checked]`";
read-O:23–24's split labels); the NEW label quotes read-O:23–24 for the three theorems the T list holds.
```
OLD 439: T (unconditional, proved here; `[novelty: single-check]`):
NEW 419: T (unconditional, proved here; novelty as split by read-O:23–24 and §4(h) — U_q: new reduction on a printed core (Hilberdink
         2012 §4); L′: new in its real-frequency statement, method printed for integer divisor-supported multipliers; E2: not found in
         print, `[novelty: dual-checked]`):            [one line in the file; wrapped here]
```
SHA-256 after R1+R2: 1d43ab112e765690bf4e86aa4175c0b67d878c1b1fdf05d2c39f826685652020.

**Displaced text NOT restored (outside the brief; for the orchestrator).** The pre-reader diff shows the block stood in place of three
more passages, none named by R1: pre-reader 243–245 (U_q's "NEAREST PUBLISHED OBJECTS (10(n))" paragraph — Lagarias 1999, Hamburger,
`[novelty: single-check]`; its content now lives, updated, in §4(h), lines 410–415); pre-reader 334–335 (§2.7 "STATUS. Theorem D is
(P) GIVEN Q4 …" — obsolete since D is unconditional); pre-reader 427–430 (§5 "T given one printed theorem on disk only second-hand:
• THEOREM D (§2.7). Given Meyer's …" — obsolete framing). Consequence: §5's T list now names U_q, L′, E2 but not D; D's unconditional
status stands in the header (line 3) and line 440 ("by Theorem D (Meyer at the page), for all discrete systems"). A " • THEOREM D
(§2.7)" bullet in §5 would be a statement-level addition, so it was not made.

## 5. R3–R6 — label repairs, applied 17:40:22 IST 2026-10-01 (each NOTE first copied to `NOTE.pre-repair-s41.md` beside it, 17:38:01)

Each OLD string was script-checked to occur exactly once in its file and on the named line; each NEW = the line with OLD replaced
and nothing else (`diff` vs the pre-repair copy shows only the lines below); table rows keep their bar count (5 → 5). Wording is the
digest's; where the digest names a source instead of giving text, the source's own words are used (cited in the NEW text).

**R3** `results/u-offsurgery-s39/NOTE.md` (record lag; original words kept, the digest's correction inserted after them). Inserted
text R3* = ` [record lag, repaired Session 41 (wave-3 digest R3): since `s5-multiplicity-s40`'s n_K, H_θ is false for every θ ≤ 0.35
with any c < 1.88, in particular for K′'s stated c = 1 (`s5-multiplicity-s40/NOTE.md`:15, 101; read-F §7)]` (one line in the file;
"read-F §7" = this unit's read-F, whose §7 states "H_θ is false for θ ≤ 0.35 with any constant below 1.88").
```
line 22  OLD: … at exponent 0.35 unrefuted and unsupported — exact lower bounds grow at local exponent 0.367 on [10^{30}, 10^{38}]), …
         NEW: … at exponent 0.35 unrefuted and unsupported R3* — exact lower bounds grow at local exponent 0.367 …
line 170 OLD: … holds for some θ ≤ 0.35 (necessarily θ > 0.3227: read-O §2C), then ζ_P has
         NEW: … holds for some θ ≤ 0.35 (necessarily θ > 0.3227: read-O §2C) R3*, then ζ_P has
```
**R4** `results/free-greedy-s40/theory/NOTE.md` (label of Theorem 1.6; NEW quotes both reads, rF:35 and rO:221–224 checked at the line).
```
line 11  OLD: [proved here; novelty: single-check — not found in print, §5]
         NEW: [proved here; novelty: new as a statement on a printed core: Bateman–Grosswald 1964 p. 367; Phragmén (both reads: rF:35,
              rO:221–224; §5)]
line 103 OLD: [proved here] [novelty: single-check]. Let P
         NEW: [proved here] [novelty: new as a statement on a printed core: Bateman–Grosswald 1964 p. 367; Phragmén (both reads: rF:35,
              rO:221–224)]. Let P
```
(Line 5's general "**[novelty: single-check]**" is not named by R4 and was left.)

**R5** `results/s5-multiplicity-s40/NOTE.md`, Instruments row 1 (bars 5 → 5).
```
line 307 OLD: … dump re-certified by the Ω-identity, 0 failures to 10⁹. One producer | `s5-multiplicity-s40/NOTE.md` …
         NEW: … dump re-certified by the Ω-identity, 0 failures to 10⁹. Four code paths, three producers since the reads (digest R5) | …
```
**R6** `results/local-greedy-s40/NOTE.md`, Instruments rows (bars 5 → 5 each); P6 = `Two producers (read-O reproduced every number; digest R6)`.
```
line 327 OLD: … ρ = 1.5 runs away. One producer; generator re-derived independently …   NEW: … runs away. P6; generator re-derived …
line 328 OLD: … (X = 10⁸, not boxed). One producer. Scratch data: …                     NEW: … (X = 10⁸, not boxed). P6. Scratch data: …
line 329 OLD: … 0.10 in the top decade. One producer | `local-greedy-s40/NOTE.md` …     NEW: … 0.10 in the top decade. P6 | …
line 330 not changed: the row carries no producer phrase at all (OLD "One producer" not present), so there was nothing to correct.
```
SHA-256 after: uoff 6d409939d13de97f…, fgT 388ef5c1b773a30d…, s5m 6a8356bdf94f4584…, lg be86e0fd1a0a3b58… (full values in §6).

## 6. Verification — diff against the pristine copies, `git diff --numstat`, `git status --short`, SHA-256 after (17:41 IST 2026-10-01)

Own `diff` of each file against its 17:30 pristine copy: B2 `5c5 137a138,153 171a188,261`; C2 `5c5 205a206,218`; qcond as §4;
fgT `11c11 103c103`; uoff `22c22 170c170`; s5m `307c307`; lg `327,329c327,329` — nothing else changed in any file.

The autocommit watchdog had already committed part of this work when `git diff --numstat` ran (plain `git diff --numstat` listed only
fgT 2/2, lg 3/3, s5m 1/1, uoff 2/2; `git status --short` showed those four NOTEs and this record as M). The same read-only command
against HEAD as of 17:30, `git diff --numstat 'HEAD@{2026-10-01 17:30:00}' -- <paths>`, gives the whole change (equal to the own diff):

```
91	1	rh-program/directions/B2-refutation-program.md
14	1	rh-program/directions/C2-rigidity-conservation.md
2	2	rh-program/results/free-greedy-s40/theory/NOTE.md
427	0	rh-program/results/free-greedy-s40/theory/NOTE.pre-repair-s41.md
3	3	rh-program/results/local-greedy-s40/NOTE.md
356	0	rh-program/results/local-greedy-s40/NOTE.pre-repair-s41.md
2	29	rh-program/results/qcond-s38/NOTE.md
471	0	rh-program/results/qcond-s38/NOTE.pre-repair-s41.md
1	1	rh-program/results/s5-multiplicity-s40/NOTE.md
329	0	rh-program/results/s5-multiplicity-s40/NOTE.pre-repair-s41.md
2	2	rh-program/results/u-offsurgery-s39/NOTE.md
236	0	rh-program/results/u-offsurgery-s39/NOTE.pre-repair-s41.md
```
(this record itself is not counted; it is still being written.)

SHA-256 after all edits:
```
5cbd0110876d3849aa498e5425aa4335849b1484d2f031d08599fb663204bc47  directions/B2-refutation-program.md
fc3af79c6c5c2e2fa99da9901680bd66185647d3356e86ad8929848ef65d9d7d  directions/C2-rigidity-conservation.md
1d43ab112e765690bf4e86aa4175c0b67d878c1b1fdf05d2c39f826685652020  results/qcond-s38/NOTE.md
388ef5c1b773a30db3a5a753673eb70b9a0c1d1fbe5eb7736f0542d328ae82b3  results/free-greedy-s40/theory/NOTE.md
6d409939d13de97f14c05d3520d0c2779a715d72f19c7ba74f71d5b78b2ae3d3  results/u-offsurgery-s39/NOTE.md
6a8356bdf94f4584d47017a8346f89d57573df75a72141a238734ab3e4b3a3ae  results/s5-multiplicity-s40/NOTE.md
be86e0fd1a0a3b5886bbc6a0545561e1af20c6ad4592b527a86ddfb4aa3937ab  results/local-greedy-s40/NOTE.md
f6464e2ede46f3f5bf2a31f7dad61ed1ecc03c1f4a780daa7ed2bfefba937664  results/novel-wave-s39/insights-digest.md
```
(the digest hash is unchanged: f6464e2e…, read only.)

## 7. Not applied, judgment calls, and notes for the orchestrator

- **UT-M4's second target.** Its line reads "Target: B2, B4."; the digest's count (line 682) puts it among B2's 19 and says it "also
  names B4". Placed in B2 only: the brief confines the edits to B2/C2, and `directions/B4-zero-dynamics.md` was not touched. To
  quote it in B4's Untried too, copy digest lines 645–648.
- **R1, three more passages the block displaced** (pre-reader 243–245, 334–335, 427–430): not restored. The brief names only the
  line-219 sentence, and two of the three are obsolete since Theorem D became unconditional (§4). §5's T list therefore no longer names D.
- **R1, the digest's "complete proof is at 351–358ff"**: a line slip. The kept copy is old 335 (now 322), the only one followed by steps (2)–(6).
- **R2 and R4 wording**: the digest names the sources of the correct label instead of giving the text. The NEW labels quote those
  sources (read-O:23–24; read-F:35 and read-O:221–224), and the quotes were checked at those lines.
- **R3**: the digest's correction was inserted after the stale words, and no words were removed. Theorem K′ and its hypothesis read as before.
- **R6, row 330**: no producer phrase, so nothing to correct (OLD absent; skipped as the brief directs).
- **§D "Not rowed" items** (digest 443–445): the digest leaves them out of the table, so they were not inserted.
- **Observed, outside R1–R6, not changed**: the lg NOTE's Instruments row 328 still says "Off-line zeros of S7(0.6)'s ζ_P", where §D's
  corrected row (B2 line 151) says "F_X" (E.11 F1's distinction). The B2 row is the corrected one. The NOTE row may want the same label.
- No stop condition was met: both target tables were identified, and every R-repair OLD string was found exactly once.

## 8. Closing

All three tasks are done: 16 rows, 22 entries, and R1–R6, except the items in §7. Insertion-only in B2/C2 apart from the two
Last-touched prefixes, checked by an actual diff. The NOTE repairs are confined to the lines listed in §4–§5. Closed 17:41 IST 2026-10-01.
