#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 39 zoo stream `zoo-s39` (2026-10-01): insert into BARRIER-ZOO.md the Group-I entry I.10 (rigidity at conductor 1),
the two I.2 riders (the (alpha, beta) frontier; thresholds and obstructions), the I.9 rider (the one-sided caveat, V2, E0), the
III.20 rider (Theorem P and class C, with the T24 record correction), the V.4 pointer, an in-line dated correction bracket on
I.2's clause (b), five cross-reference rows and a dated count paragraph. Entries 62 -> 63 (I 10, II 5, III 21, IV 22, V 5);
745 -> 765 lines (+20; the bracket adds none).

The nine blocks are read AT RUN TIME from results/zoo-s39/zoo-entries-proposed.md (<!-- BLOCK:name --> ... <!-- END:name -->):
  count     a blank line + the paragraph after the Session-37 count paragraph (line 39), before the blank line and '---' (+2);
  i2b       in-line, inside I.2's STATEMENT (line 80): one space + the bracket after clause (b)'s last words (+0);
  i2alpha   the rider after I.2's STATUS (line 84), I.2's last line (+1);   i2thresh  the rider after i2alpha (+1);
  i9        the rider after I.9's STATUS (line 142), I.9's last line (+1);
  i10       a blank line + heading, blank, five bullets after the i9 rider (+8);
  iii20     the rider after III.20's last line, the Kapranov-Smirnov NOTE (line 387) (+1);
  v4        the pointer after V.4's last line, its Session-24 rider (line 662) (+1);
  xref      five rows after the row "| novel wave s36 N4 `tournament` ..." (line 715) (+5).

Gates, in order, before anything is written:
  1. idempotence: the input carries none of this stream's markers;
  2. full SHA-256 of the input zoo (fa0d7293...), of results/novel-wave-s37/ZOO-LINES-STAGED.md (93e7e394...), of the digest
     results/novel-wave-s37/insights-digest.md (e86f642a...) and of results/novel-wave-s37/beurling-fe/NOTE.md (c3e46d12...);
  3. every block but i2b re-derived from the staged file with only the sanctioned pairs (H1 H2 L1 D1 E1 C1-C5, see the
     proposed file's finding 3), plus any whole subset of the optional pairs O1-O3 (finding 5); <ENTRY-DATE> -> "2026-10-01" or
     the brief's literal "2026-10-01 (Session 39)", the same at all five rider/pointer sites; i2b checked for shape, date and
     its quotation of the digest (whitespace-normalized); L1 checked against the M1a NOTE's lines 340 and 342;
  4. every anchor asserted unique (full-text line heads) and its neighbors verified.
Insertion only. Afterwards: every original line survives, in order (line 80 exactly as before once the bracket is removed);
63 '### ' headings, 10/5/21/22/5; Group I in order I.1-I.10 with I.10 the last entry before '## GROUP II'; each inserted line
once and at its expected line; +20, 745 -> 765; one trailing newline; none of the 10(g) linted phrases.

Usage:
  python3 scripts/zoo-insert-s39.py [--input PATH] [--proposed PATH] [--out PATH | --in-place]
    --input PATH     the zoo to read (default: BARRIER-ZOO.md); it must hash to fa0d7293... .
    --proposed PATH  the blocks file (default: results/zoo-s39/zoo-entries-proposed.md; another path is for testing).
    --out PATH       where to write (default: a scratch file, <system temp dir>/zoo-insert-s39-out.md); never the input or
                     BARRIER-ZOO.md.
    --in-place       write over the input file. The script NEVER writes over its input without this flag.
Modeled on scripts/zoo-insert-s37.py. Prints the result's SHA-256 (the post-insertion hash for STATUS and LOG)."""
import argparse
import hashlib
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s39" / "zoo-entries-proposed.md"
STAGED = ROOT / "results" / "novel-wave-s37" / "ZOO-LINES-STAGED.md"
DIGEST = ROOT / "results" / "novel-wave-s37" / "insights-digest.md"
FE_NOTE = ROOT / "results" / "novel-wave-s37" / "beurling-fe" / "NOTE.md"
ZOO_HASH_BEFORE = "fa0d729377df6a53566d19cf80bc0ad9bbdd22648135135467de75d3601f393e"
STAGED_HASH = "93e7e394b2dd4406b57772d6e5a33adf775674f289fe1c6fcfcc117075261f6c"
DIGEST_HASH = "e86f642a47cf4bdedad83efd61cd307b34fa55b87e60501faca2a9b3b0c6c981"
FE_NOTE_HASH = "c3e46d120337c8c30c54a6688a160de9359a3ff36f6aaeb812575bb6650989d4"
LINES_BEFORE, LINES_AFTER, ADDED = 745, 765, 20
LINT = ("clearly", "obviously", "easy to see", "well known", "well-known")
DATE_FILLS = ("2026-10-01", "2026-10-01 (Session 39)")


def die(msg: str) -> None:
    sys.exit("zoo-insert-s39: STOP -- %s Nothing written." % msg)


ap = argparse.ArgumentParser(description="zoo-s39 insertion (I.10, four riders, the V.4 pointer, the I.2(b) bracket, five rows, the count).")
ap.add_argument("--input", default=str(ZOO), help="the zoo to read (default: BARRIER-ZOO.md)")
ap.add_argument("--proposed", default=str(PROPOSED), help="the proposed-blocks file (default: results/zoo-s39/zoo-entries-proposed.md)")
mode = ap.add_mutually_exclusive_group()
mode.add_argument("--out", help="write the result here (default: a scratch file in the system temp directory)")
mode.add_argument("--in-place", action="store_true", help="write the result over the input file")
args = ap.parse_args()

inp = Path(args.input).resolve()
if args.in_place:
    out = inp
else:
    out = Path(args.out).resolve() if args.out else Path(tempfile.gettempdir()).resolve() / "zoo-insert-s39-out.md"
    if out == inp:
        die("--out names the input file; writing over the input needs --in-place.")
    if out == ZOO.resolve():
        die("--out names BARRIER-ZOO.md; writing the zoo needs --in-place (with the zoo as --input).")

# ---- Gate 1: idempotence (before the hash, so a second run says why it stops). ----
zoo_bytes = inp.read_bytes()
zoo_text = zoo_bytes.decode("utf-8")
MARKERS = ("### I.10 ", "**Entry count (dated, Session 39,", "entered at the Session-39 zoo stream", "| novel wave s37 ",
           "| tournament s36 row T24", "[CORRECTION 2026-10-01, Session 39", "[POINTER 2026-10-01, Session 38 (")
for m in MARKERS:
    if m in zoo_text:
        die("%s already carries %r -- this stream's text is in it; refusing to insert twice." % (inp.name, m))

# ---- Gate 2: hashes (full SHA-256). ----
got = hashlib.sha256(zoo_bytes).hexdigest()
if got != ZOO_HASH_BEFORE:
    die("%s SHA-256 is %s, expected %s -- someone edited the zoo; the orchestrator re-anchors." % (inp, got, ZOO_HASH_BEFORE))
for src, want in ((STAGED, STAGED_HASH), (DIGEST, DIGEST_HASH), (FE_NOTE, FE_NOTE_HASH)):
    got = hashlib.sha256(src.read_bytes()).hexdigest()
    if got != want:
        die("%s SHA-256 is %s, expected %s -- the source record changed." % (src.relative_to(ROOT), got, want))

# ---- Gate 3: the blocks against the sources. ----
prop_path = Path(args.proposed).resolve()
prop_text = prop_path.read_text(encoding="utf-8")


def block(name: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)), prop_text, re.S)
    if len(ms) != 1:
        die("block %s occurs %d times in %s (need exactly 1)." % (name, len(ms), prop_path))
    return ms[0]


NAMES = ("count", "i2b", "i2alpha", "i2thresh", "i9", "i10", "iii20", "v4", "xref")
SIZES = {"count": 1, "i2b": 1, "i2alpha": 1, "i2thresh": 1, "i9": 1, "i10": 7, "iii20": 1, "v4": 1, "xref": 5}
B = {k: block(k).split("\n") for k in NAMES}
for k, v in B.items():
    if len(v) != SIZES[k]:
        die("block %s has %d lines, expected %d." % (k, len(v), SIZES[k]))
    t = "\n".join(v)
    if not t.strip() or "\t" in t or "\r" in t:
        die("block %s is empty or carries a tab or a carriage return." % k)
    for bad in LINT:
        if bad in t.lower():
            die("block %s carries the linted phrase %r (10(g))." % (k, bad))
    if re.search(r"<(ENTRY-DATE|HASH|STREAM-FOLDER|N)>", t):
        die("block %s still carries a staging placeholder." % k)


def section(lines, head_prefix):
    """Non-empty lines of the staged section whose heading starts with head_prefix, up to the next '## ' or '---'."""
    starts = [i for i, ln in enumerate(lines) if ln.startswith(head_prefix)]
    if len(starts) != 1:
        die("staged section head %r occurs %d times." % (head_prefix, len(starts)))
    got_lines = []
    for ln in lines[starts[0] + 1:]:
        if ln.startswith("## ") or ln == "---":
            break
        if ln:
            got_lines.append(ln)
    return got_lines


def once(text: str, old: str, new: str, tag: str) -> str:
    if text.count(old) != 1:
        die("pair %s: its OLD string occurs %d times (need exactly 1): %r" % (tag, text.count(old), old[:80]))
    return text.replace(old, new)


staged = STAGED.read_text(encoding="utf-8").split("\n")
S = {"i": section(staged, "## Block (i) — NEW entry I.10"),
     "ii": section(staged, "## Block (ii) — RIDER on I.2, the (α, β) frontier"),
     "v": [ln for ln in section(staged, "## Block (v) — RIDER on I.2, threshold theorems") if ln.startswith("- **[RIDER")],
     "iii": section(staged, "## Block (iii) — RIDER on I.9"),
     "iv": [ln for ln in section(staged, "## Block (iv) — RIDER on III.20") if ln.startswith("- **[RIDER")],
     "iv′": section(staged, "## Block (iv′) — POINTER on V.4"),
     "vi": section(staged, "## Block (vi) — cross-reference rows"),
     "C": section(staged, "## Block C — the entry-count paragraph")}
for key, n in (("i", 6), ("ii", 1), ("v", 1), ("iii", 1), ("iv", 1), ("iv′", 1), ("vi", 5), ("C", 1)):
    if len(S[key]) != n:
        die("staged Block %s has %d text lines, expected %d." % (key, len(S[key]), n))

# Which <ENTRY-DATE> fill the rider/pointer heads use: read from i2alpha's head, then required at all five sites.
fills = [f for f in DATE_FILLS if B["i2alpha"][0].startswith("- **[RIDER %s, Session 38 (" % f)]
if len(fills) != 1:
    die("block i2alpha's head does not carry one of the sanctioned date fills %r." % (DATE_FILLS,))
FILL = fills[0]
OPT = {"O1": ("— NEW, Session 38 (novel wave 2", "— NEW, Session 37 (novel wave 2"),
       "O2": ("A pointer rider on V.4 is staged as block (iv′).", "A pointer rider on V.4 of this date carries the rule."),
       "O3": ("[consolidator's reading, single-check — for the stream to decide]",
              "[consolidator's reading, single-check; III.20's STATEMENT is not amended by this rider]")}
applied = []


def accept(name: str, got: str, want: str, opt: str = "") -> None:
    """got must be want, or want with the optional pair opt applied whole."""
    if got == want:
        return
    if opt and got == once(want, OPT[opt][0], OPT[opt][1], opt):
        applied.append(opt)
        return
    die("block %s is not its staged source with the sanctioned pairs%s (and nothing else)." % (name, " (+ optional %s)" % opt if opt else ""))


# i10: the heading (H2, H1 unless O1), a blank line, the five bullets (L1 on the STATEMENT).
h = once(S["i"][0], "entered <ENTRY-DATE>, Session 38)", "entered 2026-10-01, Session 39)", "H2")
h = once(h, "— NEW, Session 37 (novel wave 2", "— NEW, Session 38 (novel wave 2", "H1")
accept("i10 (heading)", B["i10"][0], h, "O1")
if B["i10"][1] != "":
    die("block i10's second line must be blank.")
bul = list(S["i"][1:])
bul[0] = once(bul[0], "**Theorem T′** (line 339–341; two systems)", "**Theorem T′** (line 340–342; two systems)", "L1")
if B["i10"][2:] != bul:
    die("block i10's bullets are not staged lines 45-49 with L1 (and nothing else).")
fe = FE_NOTE.read_text(encoding="utf-8").split("\n")
if not fe[339].startswith("THEOREM T′") or "dN₁ = dN₂ = ρΣ_{n≥1}δ_n" not in fe[341]:
    die("L1: the M1a NOTE's Theorem T′ is not at lines 340-342.")
# The four riders (D1, E1; O2 on i9, O3 on iii20) and the pointer (D1).
for key, name, opt in (("ii", "i2alpha", ""), ("v", "i2thresh", ""), ("iii", "i9", "O2"), ("iv", "iii20", "O3")):
    w = once(S[key][0], "<ENTRY-DATE>", FILL, "D1")
    w = once(w, "entered at the Session-38 zoo stream", "entered at the Session-39 zoo stream", "E1")
    accept(name, B[name][0], w, opt)
accept("v4", B["v4"][0], once(S["iv′"][0], "<ENTRY-DATE>", FILL, "D1"))
if B["xref"] != S["vi"]:
    die("block xref is not staged Block (vi) verbatim.")
C_PAIRS = (("C1", "(dated, Session 38, <ENTRY-DATE>)", "(dated, Session 39, 2026-10-01)"),
           ("C2", "745 → <N> lines", "745 → %d lines" % LINES_AFTER),
           ("C3", "`results/zoo-s38/`", "`results/zoo-s39/`"),
           ("C4", "the V.4 pointer; five cross-reference rows",
            "the V.4 pointer; the in-line correction bracket on I.2's clause (b), no line added; five cross-reference rows"),
           ("C5", "are riders, a pointer, rows and a note and move no count",
            "are riders, a pointer, a bracket, rows and a note and move no count"))
want = S["C"][0]
for tag, old, new in C_PAIRS:
    want = once(want, old, new, tag)
if B["count"] != [want]:
    die("block count is not staged Block C with the pairs C1-C5 (and nothing else).")
# i2b: new words -- shape, date, and every quotation found in the digest (whitespace-normalized).
I2B = B["i2b"][0]
if not (I2B.startswith("[CORRECTION 2026-10-01, Session 39 — ") and I2B.endswith("]") and I2B.count("[") == 1
        and I2B.count("]") == 1 and "entered at the Session-39 zoo stream" in I2B):
    die("block i2b is not one dated bracket '[CORRECTION 2026-10-01, Session 39 — … entered at the Session-39 zoo stream …]'.")
norm = lambda s: re.sub(r"\s+", " ", s).strip()
dig = norm(DIGEST.read_text(encoding="utf-8"))
quotes = re.findall(r'"([^"]+)"', I2B)
KEY_Q = "{α > ½, β < ½} is populated under RH (BDR Thm 1.3) and, non-constructively, unconditionally (Prop. 2.1)"
if KEY_Q not in quotes or any(norm(q) not in dig for q in quotes):
    die("block i2b does not quote the digest's E.2(e) words verbatim.")
zoo_lines_set = set(zoo_text.split("\n"))
for k in NAMES:
    for ln in B[k]:
        if ln and ln in zoo_lines_set:
            die("an inserted line of block %s is already a line of the zoo: %r" % (k, ln[:80]))
        if k != "i10" and ln.lstrip().startswith("#"):
            die("block %s would add a heading." % k)
if not B["i10"][0].startswith("### I.10 ") or any(ln.lstrip().startswith("#") for ln in B["i10"][1:]):
    die("block i10 must be a '### I.10' heading, a blank line and five bullets.")

# ---- Gate 4: anchors (each asserted unique as a line head; neighbors verified). ----
lines = zoo_text.split("\n")
orig = list(lines)
if lines[-1] != "" or lines[-2] == "":
    die("the input must end with exactly one newline.")
if len(orig) - 1 != LINES_BEFORE:
    die("the input has %d lines, expected %d." % (len(orig) - 1, LINES_BEFORE))
A_COUNT = "**Entry count (dated, Session 37, 2026-09-30).** IV.21 (the degree clause"
P_COUNT = "**Entry count (dated, Session 36, 2026-09-30).**"
H_I2 = "### I.2 The Beurling counterexample factory (DMV / BDR / Broucke school)"
S_I2 = "- **STATEMENT.** Beurling generalized number systems have a full Euler product"
A_I2 = "- **STATUS.** literature-verified (arXiv/Crossref pins in the sweep report; DMV on disk). **BINDS: full-RH**"
N_I3 = "### I.3 The Alternative Hypothesis world + the 256-periodic"
AT_I2B = 'β < 1/2 only under RH ("RH = Z is the extremal [1/2,0]-system")'
H_I9 = "### I.9 The rung-1 twin: the virtual curve over F₅"
A_I9 = "- **STATUS.** computationally-verified — exact integers (writer d ≤ 40; the reader's re-run:"
G_II = "## GROUP II — FORMALIZED CEILINGS"
H_III20 = "### III.20 The S6 doubled-object rule (comparative anatomy of every TRUE RH)"
A_III20 = "- **[NOTE 2026-09-29, Session 30 (G2, the Kapranov–Smirnov close, `results/g2-ks-close-s30/`;"
N_III21 = "### III.21 Substrate-blindness of positivity calculi (the Yuan–Zhang dress test)"
H_V4 = "### V.4 The negative-control rule"
A_V4 = "- **[RIDER 2026-09-24, Session 24 (digest §C.3 item 4), entered at the Session-25 zoo stream — a stop condition"
N_V5 = "### V.5 The Grossmann-condition rule"
T_XREF = "| Casualty | Verdict | Killing barriers |"
A_XREF = "| novel wave s36 N4 `tournament` (35 mechanisms at brief time) |"
P_XREF = "| novel wave s36 N3 `fingerprint`"
N_XREF = "**[READ 2026-09-10, Opus 5.]** The three Session-21 rows above were checked against their records"
ANCHORS = (A_COUNT, P_COUNT, H_I2, S_I2, A_I2, N_I3, H_I9, A_I9, G_II, H_III20, A_III20, N_III21, H_V4, A_V4, N_V5, T_XREF,
           A_XREF, P_XREF, N_XREF)
for a in ANCHORS:
    n = sum(1 for ln in lines if ln.startswith(a))
    if n != 1:
        die("the anchor string is not unique in the zoo (%d hits): %r" % (n, a[:100]))
if zoo_text.count(AT_I2B) != 1:
    die("the clause-(b) anchor occurs %d times in the zoo (need exactly 1)." % zoo_text.count(AT_I2B))


def idx(prefix: str) -> int:
    hits = [i for i, ln in enumerate(lines) if ln.startswith(prefix)]
    if len(hits) != 1:
        die("anchor %r occurs %d times (need exactly 1)." % (prefix[:80], len(hits)))
    return hits[0]


def entry_of(i: int) -> str:
    j = i
    while j >= 0 and not lines[j].startswith("### ") and not lines[j].startswith("## "):
        j -= 1
    return lines[j] if j >= 0 else ""


# Bottom-up, as the staged map orders it (each index is re-found by text, so the order is for the record only).
# 1. The rows: after the N4 row, the table's last row, before the blank line and the READ note.
i = idx(A_XREF)
if not lines[i - 1].startswith(P_XREF) or lines[i + 1] != "" or not lines[i + 2].startswith(N_XREF):
    die("the N4 row is not the table's last row between the N3 row and the blank line + READ note.")
t = i
while t >= 0 and lines[t].startswith("|"):
    t -= 1
if lines[t + 1] != T_XREF or lines[t + 2] != "|---|---|---|" or lines[t] != "" or not lines[t - 1].startswith("## Cross-reference: program casualties"):
    die("the N4 row is not in the cross-reference table under its column header.")
lines[i + 1:i + 1] = B["xref"]
# 2. The V.4 pointer: after V.4's last line, before the blank line and '### V.5'.
i = idx(A_V4)
if not entry_of(i).startswith(H_V4) or lines[i + 1] != "" or not lines[i + 2].startswith(N_V5):
    die("the Session-24 rider is not V.4's last line before the blank line and '### V.5'.")
lines[i + 1:i + 1] = B["v4"]
# 3. The III.20 rider: after III.20's last line (the Kapranov-Smirnov NOTE), before the blank line and '### III.21'.
i = idx(A_III20)
if not entry_of(i).startswith(H_III20) or lines[i + 1] != "" or lines[i + 2] != N_III21:
    die("the Kapranov-Smirnov NOTE is not III.20's last line before the blank line and '### III.21'.")
lines[i + 1:i + 1] = B["iii20"]
# 4-5. The I.9 rider, then I.10: after I.9's STATUS (its last line), before the blank line, '---' and '## GROUP II'.
i = idx(A_I9)
if not entry_of(i).startswith(H_I9) or lines[i + 1] != "" or lines[i + 2] != "---" or not lines[i + 4].startswith(G_II):
    die("I.9's STATUS is not I.9's last line before the blank line, '---' and '## GROUP II'.")
if [ln for ln in lines[:i] if ln.startswith("### I")][-1] != entry_of(i):
    die("I.9 is not the last Group-I entry in file order.")
lines[i + 1:i + 1] = B["i9"] + [""] + B["i10"]
# 6-7. The two I.2 riders, (ii) above (v): after I.2's STATUS (its last line), before the blank line and '### I.3'.
i = idx(A_I2)
if not entry_of(i).startswith(H_I2) or lines[i + 1] != "" or not lines[i + 2].startswith(N_I3):
    die("I.2's STATUS is not I.2's last line before the blank line and '### I.3'.")
lines[i + 1:i + 1] = B["i2alpha"] + B["i2thresh"]
# The in-line bracket: inside I.2's STATEMENT, one space + the bracket right after clause (b)'s last words.
i = idx(S_I2)
if not entry_of(i).startswith(H_I2) or lines[i].count(AT_I2B) != 1:
    die("the clause-(b) anchor is not inside I.2's STATEMENT.")
I2B_LINE_OLD = lines[i]
lines[i] = I2B_LINE_OLD.replace(AT_I2B, AT_I2B + " " + I2B, 1)
if not lines[i].startswith(I2B_LINE_OLD.split(AT_I2B)[0] + AT_I2B + " [CORRECTION") or not lines[i].endswith(I2B_LINE_OLD.split(AT_I2B)[1]):
    die("the bracket did not land between clause (b) and the rest of the STATEMENT.")
# 8. The count paragraph: after the Session-37 paragraph, before the blank line and '---'.
i = idx(A_COUNT)
if any(ln.startswith("### ") or ln.startswith("## ") for ln in lines[:i]):
    die("the Session-37 count paragraph is not in the header.")
if not lines[i - 2].startswith(P_COUNT) or lines[i - 1] != "" or lines[i + 1] != "" or lines[i + 2] != "---":
    die("the Session-37 count paragraph is not between the Session-36 paragraph and the blank line + '---'.")
lines[i + 1:i + 1] = ["", B["count"][0]]
new_text = "\n".join(lines)

# ---- Verification. ----
NEW80 = I2B_LINE_OLD.replace(AT_I2B, AT_I2B + " " + I2B, 1)
if lines.count(NEW80) != 1:
    die("the bracketed STATEMENT line is not present exactly once.")
cmp = [I2B_LINE_OLD if ln == NEW80 else ln for ln in lines]
it = iter(cmp)
for ln in orig:
    for cand in it:
        if cand == ln:
            break
    else:
        die("original line lost or reordered: %r" % ln[:80])
added = len(lines) - len(orig)
if added != ADDED or len(lines) - 1 != LINES_AFTER:
    die("line arithmetic: %d -> %d (+%d), expected %d -> %d (+%d)." % (len(orig) - 1, len(lines) - 1, added, LINES_BEFORE, LINES_AFTER, ADDED))
if not new_text.endswith("\n") or new_text.endswith("\n\n"):
    die("the result must end with exactly one newline.")
heads = [ln for ln in lines if ln.startswith("### ")]
tally = {g: sum(1 for ln in lines if ln.startswith("### %s." % g)) for g in ("I", "II", "III", "IV", "V")}
if len(heads) != 63 or tally != {"I": 10, "II": 5, "III": 21, "IV": 22, "V": 5}:
    die("heading tally %d %r, expected 63 {I 10, II 5, III 21, IV 22, V 5}." % (len(heads), tally))
for ln in heads:
    if not re.match(r"### (I|II|III|IV|V)\.(\d+) ", ln):
        die("heading is not a numbered entry: %r" % ln[:80])
recount = "I: %d, II: %d, III: %d, IV: %d, V: %d" % (tally["I"], tally["II"], tally["III"], tally["IV"], tally["V"])
if recount not in B["count"][0] or "**%d entries**" % len(heads) not in B["count"][0]:
    die("the count paragraph's figures are not the recount (%s; %d)." % (recount, len(heads)))
order_i = [int(re.match(r"### I\.(\d+) ", ln).group(1)) for ln in heads if ln.startswith("### I.")]
order_iv = [int(re.match(r"### IV\.(\d+) ", ln).group(1)) for ln in heads if ln.startswith("### IV.")]
if order_i != list(range(1, 11)) or order_iv != list(range(1, 16)) + [18, 16, 17, 19, 20, 21, 22]:
    die("file order: Group I %r, Group IV %r." % (order_i, order_iv))
have = set(re.match(r"### ((?:I|II|III|IV|V)\.\d+) ", ln).group(1) for ln in heads)
ins_text = "\n".join("\n".join(B[k]) for k in NAMES)
cited = set(a + "." + b for a, b in re.findall(r"(?<![\w.])(I{1,3}|IV|V)\.(\d+)(?!\d)", ins_text))
if cited - have:
    die("the new text cites entries that do not exist: %r" % sorted(cited - have))
for ln in [x for k in NAMES if k != "i2b" for x in B[k] if x]:
    if lines.count(ln) != 1:
        die("an inserted line occurs %d times: %r" % (lines.count(ln), ln[:80]))
P = lambda n: lines[n - 1]
checks = (
    (P(39).startswith(A_COUNT) and P(40) == "" and P(41) == B["count"][0] and P(42) == "" and P(43) == "---", "count at 41"),
    (P(80).startswith("### I.2 ") and P(82) == NEW80, "the I.2(b) bracket in line 82"),
    (P(86).startswith(A_I2) and P(87) == B["i2alpha"][0] and P(88) == B["i2thresh"][0] and P(89) == "" and P(90).startswith(N_I3), "I.2 riders at 87-88"),
    (P(146).startswith(A_I9) and P(147) == B["i9"][0] and P(148) == "" and P(149) == B["i10"][0], "I.9 rider 147, I.10 at 149"),
    (P(150) == "" and [P(n) for n in range(151, 156)] == B["i10"][2:] and P(156) == "" and P(157) == "---" and P(159).startswith(G_II), "I.10 bullets 151-155"),
    (P(400).startswith(A_III20) and P(401) == B["iii20"][0] and P(402) == "" and P(403) == N_III21, "III.20 rider at 401"),
    (P(676).startswith(A_V4) and P(677) == B["v4"][0] and P(678) == "" and P(679).startswith(N_V5), "V.4 pointer at 677"),
    (P(730).startswith(A_XREF) and [P(n) for n in range(731, 736)] == B["xref"] and P(736) == "" and P(737).startswith(N_XREF), "rows at 731-735"),
)
for ok, what in checks:
    if not ok:
        die("position check failed: %s." % what)

out.write_text(new_text, encoding="utf-8")
digest = hashlib.sha256(new_text.encode("utf-8")).hexdigest()
print("zoo-insert-s39: OK -- wrote %s" % out)
print("  %d -> %d lines (+%d); 62 -> %d entries, %s; date fill %r; optional pairs applied: %s"
      % (len(orig) - 1, len(lines) - 1, added, len(heads), recount, FILL, ", ".join(applied) or "none"))
print("  SHA-256 %s" % digest)
