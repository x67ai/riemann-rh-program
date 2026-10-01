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
