#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 37 zoo stream `zoo-s37` (2026-09-30): insert into BARRIER-ZOO.md the Group-IV entries IV.21 (the degree clause and
the lattice-index kill; results/d4-infty-s36/NOTE.md section 5.1 Option A) and IV.22 (prime channels add density; the wave's
staged Block (i), renumbered from IV.21), the Group-I entry I.9 (the rung-1 twin), the IV.9 and III.15 riders, the IV.20
formalization bullet, five cross-reference rows and a dated count paragraph. Entries 59 -> 62 (I 9, II 5, III 21, IV 22, V 5);
711 -> 745 lines (+34).

The eight blocks are read AT RUN TIME from results/zoo-s37/zoo-entries-proposed.md (<!-- BLOCK:name --> ... <!-- END:name -->):
  count  a blank line + the paragraph after the Session-36 count paragraph (line 37), before the blank line and '---' (+2);
  i9     a blank line + heading, blank, five bullets after I.8's last line, its STATUS (line 132) (+8);
  iii15  the rider after III.15's last line, the Session-24 RE-SCOUT RETURN (line 326) (+1);
  iv9    the rider after IV.9's last line, the READ of 2026-09-24 (line 481) (+1);
  iv20   the formalization bullet after IV.20's STATUS (line 598), inside IV.20 (+1);
  iv21   a blank line + the entry after the iv20 bullet (+8);  iv22  a blank line + the entry after IV.21 (+8);
  xref   five rows after the cross-reference table's last row, the beta-shapes s35 row (line 681) (+5).

Gates, in order, before anything is written:
  1. idempotence: the input carries none of this stream's markers;
  2. full SHA-256 of the input zoo (90d0ad6a...), of results/d4-infty-s36/NOTE.md (7a1dc42e...) and of
     results/novel-wave-s36/ZOO-LINES-STAGED.md (0a26acaa...);
  3. every block re-derived from those two sources with only the sanctioned edits: the IV.21 heading in the '###' house style;
     the wave's IV.21 -> IV.22 (heading and rows); <ENTRY-DATE> -> "2026-09-30" (or the brief's literal "2026-09-30 (Session
     37)", the same at all five sites); the one-producer span of the IV.9 rider -> <PRODUCER-B-VERDICT> or the orchestrator's
     one-line replacement; the count paragraph = staged Block C with the pairs C0-C4; plus any whole subset of the optional
     pairs P1 (the N2 row's "one producer so far" slot), P2 (producer-B's CERT path in the IV.9 rider head), P3 ("IV.20 as
     staged (Theorem R)" -> "IV.20 (Theorem R)"). With --in-place the token must have been replaced;
  4. every anchor asserted unique (full-text line heads) and its neighbors verified.
Pure insertion. Afterwards: every original line survives, in order; 62 '### ' headings, 9/5/21/22/5; Group I in order I.1-I.9;
Group IV in file order IV.1-IV.15, IV.18, IV.16, IV.17, IV.19, IV.20, IV.21, IV.22 with IV.22 the last entry before '## GROUP V';
each inserted line once and at its expected line; +34, 711 -> 745; one trailing newline; none of the 10(g) linted phrases.

Usage:
  python3 scripts/zoo-insert-s37.py [--input PATH] [--proposed PATH] [--out PATH | --in-place]
    --input PATH     the zoo to read (default: BARRIER-ZOO.md); it must hash to 90d0ad6a... .
    --proposed PATH  the blocks file (default: results/zoo-s37/zoo-entries-proposed.md; another path is for testing).
    --out PATH       where to write (default: a scratch file, <system temp dir>/zoo-insert-s37-out.md); never the input or
                     BARRIER-ZOO.md.
    --in-place       write over the input file. The script NEVER writes over its input without this flag.
Modeled on scripts/zoo-insert-s36.py. Prints the result's SHA-256 (the post-insertion hash for STATUS and LOG)."""
import argparse
import hashlib
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s37" / "zoo-entries-proposed.md"
NOTE = ROOT / "results" / "d4-infty-s36" / "NOTE.md"
STAGED = ROOT / "results" / "novel-wave-s36" / "ZOO-LINES-STAGED.md"
ZOO_HASH_BEFORE = "90d0ad6afa093388317a71cd89daf4c10ea755978943027fb61c5f06c237cc0c"
NOTE_HASH = "7a1dc42eb73e2f5811c84409c4564776281a71eca6edd439c6487f47f31f36ca"
STAGED_HASH = "0a26acaab4cfe2a0fd32178cab34d9817e66b3030b6a2296541c0a867af6ef5d"
LINES_BEFORE, LINES_AFTER, ADDED = 711, 745, 34
LINT = ("clearly", "obviously", "easy to see", "well known", "well-known")
TOKEN = "<PRODUCER-B-VERDICT>"
DATE_FILLS = ("2026-09-30", "2026-09-30 (Session 37)")


def die(msg: str) -> None:
    sys.exit("zoo-insert-s37: STOP -- %s Nothing written." % msg)


ap = argparse.ArgumentParser(description="zoo-s37 insertion (IV.21, IV.22, I.9, two riders, the IV.20 bullet, five rows, the count).")
ap.add_argument("--input", default=str(ZOO), help="the zoo to read (default: BARRIER-ZOO.md)")
ap.add_argument("--proposed", default=str(PROPOSED), help="the proposed-blocks file (default: results/zoo-s37/zoo-entries-proposed.md)")
mode = ap.add_mutually_exclusive_group()
mode.add_argument("--out", help="write the result here (default: a scratch file in the system temp directory)")
mode.add_argument("--in-place", action="store_true", help="write the result over the input file")
args = ap.parse_args()

inp = Path(args.input).resolve()
if args.in_place:
    out = inp
else:
    out = Path(args.out).resolve() if args.out else Path(tempfile.gettempdir()).resolve() / "zoo-insert-s37-out.md"
    if out == inp:
        die("--out names the input file; writing over the input needs --in-place.")
    if out == ZOO.resolve():
        die("--out names BARRIER-ZOO.md; writing the zoo needs --in-place (with the zoo as --input).")

# ---- Gate 1: idempotence (before the hash, so a second run says why it stops). ----
zoo_bytes = inp.read_bytes()
zoo_text = zoo_bytes.decode("utf-8")
MARKERS = ("### IV.21 ", "### IV.22 ", "### I.9 ", "**Entry count (dated, Session 37,", "Session-37 zoo stream",
           "| d4-infty s36 (", "| novel wave s36 ", "ARITHMETIC CORE COMPARATOR-CHECKED", TOKEN)
for m in MARKERS:
    if m in zoo_text:
        die("%s already carries %r -- this stream's text is in it; refusing to insert twice." % (inp.name, m))

# ---- Gate 2: hashes. ----
got = hashlib.sha256(zoo_bytes).hexdigest()
if got != ZOO_HASH_BEFORE:
    die("%s SHA-256 is %s, expected %s -- someone edited the zoo; the orchestrator re-anchors." % (inp, got, ZOO_HASH_BEFORE))
for src, want in ((NOTE, NOTE_HASH), (STAGED, STAGED_HASH)):
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


NAMES = ("count", "i9", "iii15", "iv9", "iv20", "iv21", "iv22", "xref")
SIZES = {"count": 1, "i9": 7, "iii15": 1, "iv9": 1, "iv20": 1, "iv21": 7, "iv22": 7, "xref": 5}
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
    if re.search(r"<(ENTRY-DATE|HASH|STREAM-FOLDER)>", t):
        die("block %s still carries a staging placeholder." % k)
token_left = TOKEN in B["iv9"][0]
if any(TOKEN in "\n".join(B[k]) for k in NAMES if k != "iv9"):
    die("the token %s occurs outside block iv9." % TOKEN)
if token_left and args.in_place:
    die("block iv9 still carries %s -- replace it with Producer B's verdict before --in-place." % TOKEN)


def section(lines, head_prefix):
    """Non-empty lines of the section whose heading line starts with head_prefix, up to the next '## ', '---' or '*Option B'."""
    starts = [i for i, ln in enumerate(lines) if ln.startswith(head_prefix)]
    if len(starts) != 1:
        die("source section head %r occurs %d times." % (head_prefix, len(starts)))
    got_lines = []
    for ln in lines[starts[0] + 1:]:
        if ln.startswith("## ") or ln == "---" or ln.startswith("*Option B"):
            break
        if ln:
            got_lines.append(ln)
    return got_lines


note = NOTE.read_text(encoding="utf-8").split("\n")
staged = STAGED.read_text(encoding="utf-8").split("\n")
OPT_A = section(note, "*Option A — a Group-IV candidate entry, after IV.20 as staged by s35:*")
S = {"i": section(staged, "## Block (i) — NEW entry IV.21"), "ii": section(staged, "## Block (ii) — RIDER on IV.9"),
     "iii": section(staged, "## Block (iii) — NEW entry I.9"), "iv": section(staged, "## Block (iv) — RIDER on III.15"),
     "v": section(staged, "## Block (v) — the IV.20 formalization bullet"), "X": section(staged, "## Block X — cross-reference rows"),
     "C": section(staged, "## Block C — the entry-count paragraph")}
for key, n in (("i", 6), ("ii", 1), ("iii", 6), ("iv", 1), ("v", 1), ("X", 4)):
    if len(S[key]) != n:
        die("staged Block %s has %d non-empty lines, expected %d." % (key, len(S[key]), n))
if len(OPT_A) != 6:
    die("the NOTE's section 5.1 Option A has %d non-empty lines, expected 6." % len(OPT_A))
S_C = S["C"][0]
if not S_C.startswith("**Entry count (dated, Session 37, <ENTRY-DATE>).** IV.21 (prime channels add density"):
    die("staged Block C does not open with the count paragraph.")

# The brief's IV.21 heading (item 1), and the NOTE's staged form of it.
D4_TITLE = ("IV.21 The degree clause and the lattice-index kill (no square of Spec Z graded by ζ carries a real self-intersection "
            "of the diagonal)")
if OPT_A[0] != "- **" + D4_TITLE + " — NEW, Session 36 (`results/d4-infty-s36/NOTE.md` §2–§3)**":
    die("the NOTE's Option A heading line is not the one the brief names.")
D4_HEADING = "### " + D4_TITLE + " — NEW, Session 36 (`results/d4-infty-s36/NOTE.md` §2–§3; entered 2026-09-30, Session 37)"
D4_ROW = ("| d4-infty s36 (the (D4) residual: lattice Hodge index under the degree clause) | closed by theorem (Session 36; read "
          "at the line Session 37, dual-model) | IV.21; IV.20; III.20; IV.1; I.2 |")

# Which <ENTRY-DATE> fill the blocks use: read from the count paragraph's head, then required at all five sites.
fills = [f for f in DATE_FILLS if B["count"][0].startswith("**Entry count (dated, Session 37, %s).**" % f)]
if len(fills) != 1:
    die("block count's head carries neither accepted <ENTRY-DATE> fill.")
FILL = fills[0]


def once(text: str, old: str, new: str, tag: str) -> str:
    if text.count(old) != 1:
        die("%s: OLD occurs %d times in the source (need exactly 1): %r" % (tag, text.count(old), old[:80]))
    return text.replace(old, new)


def dated(text: str, tag: str) -> str:
    return once(text, "<ENTRY-DATE>", FILL, tag + " <ENTRY-DATE>")


applied = []
# iv21: the brief's heading; a blank line; NOTE lines 191-195 byte for byte (P3 optional on STATUS).
P3_OLD, P3_NEW = "IV.20 as staged (Theorem R)", "IV.20 (Theorem R)"
st21 = OPT_A[5]
once(st21, P3_OLD, P3_OLD, "P3")
if B["iv21"][:6] != [D4_HEADING, ""] + OPT_A[1:5]:
    die("block iv21 is not the NOTE's Option A with the brief's heading (and nothing else) in its first six lines.")
if B["iv21"][6] == st21.replace(P3_OLD, P3_NEW):
    applied.append("P3")
elif B["iv21"][6] != st21:
    die("block iv21's STATUS is not the NOTE's line 195 (with P3 applied whole or not at all).")

# iv22: Block (i) renumbered IV.21 -> IV.22 (heading only), <ENTRY-DATE> filled, bullets byte for byte.
if S["i"][0].count("IV.21") != 1 or any("IV.21" in ln for ln in S["i"][1:]):
    die("staged Block (i) cites IV.21 other than in its heading; the renumbering would be incomplete.")
h22 = dated(once(S["i"][0], "### IV.21 Prime channels add density", "### IV.22 Prime channels add density", "(i)"), "(i)")
if B["iv22"] != [h22, ""] + S["i"][1:]:
    die("block iv22 is not staged Block (i) renumbered IV.21 -> IV.22 with <ENTRY-DATE> filled (and nothing else).")

# i9, iii15, iv20.
if B["i9"] != [dated(S["iii"][0], "(iii)"), ""] + S["iii"][1:]:
    die("block i9 is not staged Block (iii) with <ENTRY-DATE> filled (and nothing else).")
if B["iii15"] != [dated(S["iv"][0], "(iv)")]:
    die("block iii15 is not staged Block (iv) with <ENTRY-DATE> filled (and nothing else).")
if B["iv20"] != S["v"]:
    die("block iv20 is not staged Block (v) byte for byte.")

# iv9: Block (ii), <ENTRY-DATE> filled; the one-producer span is the slot (the token, or the orchestrator's replacement);
# P2 optional on the head.
OLD_PRODUCER = ("from ONE producer (A, Arb) — the second producer of `results/haglund-cert-s37/BRIEF.md` §3 is owed before "
                "external use")
P2_OLD = "`results/haglund-cert-s37/producer-A/CERT.md`; entered at the Session-37 zoo stream)"
P2_NEW = ("`results/haglund-cert-s37/producer-A/CERT.md`, `results/haglund-cert-s37/producer-B/CERT.md`; entered at the "
          "Session-37 zoo stream)")
base9 = dated(S["ii"][0], "(ii)")
once(base9, OLD_PRODUCER, OLD_PRODUCER, "(ii) one-producer span")
pre9, post9 = base9.split(OLD_PRODUCER)
once(pre9, P2_OLD, P2_OLD, "P2")
r9, slot9 = B["iv9"][0], None
for pv, tags in ((pre9, ()), (pre9.replace(P2_OLD, P2_NEW), ("P2",))):
    if r9.startswith(pv) and r9.endswith(post9) and len(r9) > len(pv) + len(post9):
        slot9 = r9[len(pv):len(r9) - len(post9)]
        applied += list(tags)
if slot9 is None:
    die("block iv9 is not staged Block (ii) with <ENTRY-DATE> filled and only the one-producer span replaced (P2 whole or not).")
if slot9 != TOKEN and (slot9 != slot9.strip() or "PRODUCER-B-VERDICT" in slot9 or "<" in slot9 or ">" in slot9):
    die("the replacement of the token in block iv9 is malformed: %r" % slot9[:120])

# xref: the brief's d4-infty row, then Block X renumbered IV.21 -> IV.22; the N2 row's "one producer so far" is slot P1.
rows = [r.replace("IV.21", "IV.22") for r in S["X"]]
if [S["X"][k].count("IV.21") for k in range(4)] != [1, 0, 1, 1]:
    die("staged Block X does not cite IV.21 once in each of rows N1, N3, N4 (and not in N2).")
if not rows[1].startswith("| novel wave s36 N2 `staircase`"):
    die("staged Block X's second row is not the N2 row.")
P1_OLD = "one producer so far"
once(rows[1], P1_OLD, P1_OLD, "P1")
pre_r, post_r = rows[1].split(P1_OLD)
X = B["xref"]
if X[0] != D4_ROW or [X[1], X[3], X[4]] != [rows[0], rows[2], rows[3]]:
    die("block xref is not the brief's d4-infty row followed by staged Block X renumbered (rows N1, N3, N4).")
if not (X[2].startswith(pre_r) and X[2].endswith(post_r) and len(X[2]) > len(pre_r) + len(post_r)):
    die("block xref's N2 row is not the staged row (only 'one producer so far' may be replaced, P1).")
mid = X[2][len(pre_r):len(X[2]) - len(post_r)]
if "|" in mid or mid != mid.strip():
    die("P1's replacement in the N2 row is malformed: %r" % mid[:80])
if mid != P1_OLD:
    applied.append("P1")

# count: staged Block C with the pairs C0-C4, each once.
C_PAIRS = (
    ("C0", "<ENTRY-DATE>", FILL),
    ("C1", "** IV.21 (prime channels add density",
     "** IV.21 (the degree clause and the lattice-index kill — Proposition N: the degree clause d(φ_n) = n holds, for "
     "multiplicative degrees, exactly when the target's graded Dirichlet series is −ζ′/ζ, and it makes c injective; Theorem S: "
     "under it no real self-intersection of the diagonal is compatible with Castelnuovo–Severi and product adjunction, and no "
     "canonical class sits in an index-one space with Δ and the graphs; d4-infty s36, `results/d4-infty-s36/NOTE.md` §2–§3, "
     "writer Opus 5.5, Session 36; the orchestrator's read at the line `read-F.md` AGREES-WITH-CORRECTIONS, Option A, Session "
     "37), IV.22 (prime channels add density"),
    ("C2", "make **61 entries** — I: 9, II: 5, III: 21, IV: 21, V: 5 (recounted from this file's `###` headings at insertion: "
           "9 + 5 + 21 + 21 + 5 = 61; Group IV 20 → 21, the new entry placed after IV.20, the last Group-IV entry in file order; "
           "Group I 8 → 9, placed after I.8)",
     "make **62 entries** — I: 9, II: 5, III: 21, IV: 22, V: 5 (recounted from this file's `###` headings at insertion: "
     "9 + 5 + 21 + 22 + 5 = 62; Group IV 20 → 22, the new entries placed after IV.20, the last Group-IV entry in file order, "
     "IV.21 before IV.22; Group I 8 → 9, placed after I.8)"),
    ("C3", "four cross-reference rows \"novel wave s36\"", "five cross-reference rows, \"d4-infty s36\" and four \"novel wave s36\""),
    ("C4", "711 → 736 lines if entered as staged, SHA-256 at launch <HASH>, <STREAM-FOLDER>)",
     "711 → 745 lines, SHA-256 at launch 90d0ad6a…, `results/zoo-s37/`)"),
)
want = S_C
for tag, old, new in C_PAIRS:
    want = once(want, old, new, tag)
if B["count"] != [want]:
    die("block count is not staged Block C with the pairs C0-C4 (and nothing else).")
zoo_lines_set = set(zoo_text.split("\n"))
for k in NAMES:
    for ln in B[k]:
        if ln and ln in zoo_lines_set:
            die("an inserted line of block %s is already a line of the zoo: %r" % (k, ln[:80]))
        if k not in ("i9", "iv21", "iv22") and ln.lstrip().startswith("#"):
            die("block %s would add a heading." % k)
for k in ("i9", "iv21", "iv22"):
    if not B[k][0].startswith("### ") or B[k][1] != "" or any(ln.lstrip().startswith("#") for ln in B[k][1:]):
        die("block %s must be a '###' heading, a blank line and five bullets." % k)

# ---- Gate 4: anchors (each asserted unique as a line head; neighbors verified). ----
lines = zoo_text.split("\n")
orig = list(lines)
if lines[-1] != "" or lines[-2] == "":
    die("the input must end with exactly one newline.")
if len(orig) - 1 != LINES_BEFORE:
    die("the input has %d lines, expected %d." % (len(orig) - 1, LINES_BEFORE))
A_COUNT = "**Entry count (dated, Session 36, 2026-09-30).** IV.20 (the finite-rank target kill"
P_COUNT = "**Entry count (dated, Session 34, 2026-09-29).**"
H_I8 = "### I.8 The Siegel-zero world (an S1-passing GRH-false world for positive-Λ first-order instruments)"
A_I8 = ("- **STATUS.** Instrument content under standing order 4; no bearing on RH for ζ, whose zero configuration contains no "
        "real orbit.")
G_II = "## GROUP II — FORMALIZED CEILINGS"
H_III15 = "### III.15 The Fisher-zero wall (statistical mechanics acts in the wrong variable)"
A_III15 = ("- **[RE-SCOUT RETURN 2026-09-24, Session 24 — the dark-horse exception (W1-26 lee-yang-stat-mech) priced on the "
           "function-field rung: NO, instrument RESTORED")
N_III15 = "### III.16 Lorentzian/log-concavity arithmetic-blindness"
H_IV9 = "### IV.9 Visibility pricing (the cross-cutting detection-threshold barrier — program-synthesized)"
A_IV9 = ("- **[READ 2026-09-24, Opus 5: the last sentence of the rider above outruns its records; corrected here, no number "
         "moves.]**")
N_IV9 = "### IV.10 Tate-curve products carry no correspondence calculus — NEW, Session 6 (C3 adjudication)"
H_IV20 = ("### IV.20 The finite-rank target kill (no surface over a field, and no target of finite Q-rank, can carry ζ's diagonal "
          "row)")
A_IV20 = ("- **STATUS.** program-adjudicated — dual-model: writer Fable 5.1, Session 35; Opus 5 reader `read-O.md` "
          "AGREES-WITH-CORRECTIONS 2026-09-29 (")
G_V = "## GROUP V — PROCESS BARRIERS (how briefs die for non-mathematical reasons)"
T_XREF = "| Casualty | Verdict | Killing barriers |"
A_XREF = ("| β-shapes s35 (finite-rank / Weil-form targets for the F₁-square; End_β = {id} bases) | closed by theorem (Session 35; "
          "dual-model) | IV.20; IV.10; III.20; V.5 |")
P_XREF = "| D2 design-axis scout (P1–P9) |"
N_XREF = "**[READ 2026-09-10, Opus 5.]** The three Session-21 rows above were checked against their records"
ANCHORS = (A_COUNT, P_COUNT, H_I8, A_I8, G_II, H_III15, A_III15, N_III15, H_IV9, A_IV9, N_IV9, H_IV20, A_IV20, G_V, T_XREF,
           A_XREF, P_XREF, N_XREF)
for a in ANCHORS:
    n = sum(1 for ln in lines if ln.startswith(a))
    if n != 1:
        die("the anchor string is not unique in the zoo (%d hits): %r" % (n, a[:100]))
for a in (N_IV9, G_V, T_XREF, A_XREF):
    if sum(1 for ln in lines if ln == a) != 1:
        die("the anchor line is not present exactly once as a whole line: %r" % a[:100])


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


# 1. The count paragraph: after the Session-36 paragraph, before the blank line and '---'.
i = idx(A_COUNT)
if any(ln.startswith("### ") or ln.startswith("## ") for ln in lines[:i]):
    die("the Session-36 count paragraph is not in the header.")
if not lines[i - 2].startswith(P_COUNT) or lines[i - 1] != "" or lines[i + 1] != "" or lines[i + 2] != "---":
    die("the Session-36 count paragraph is not between the Session-34 paragraph and the blank line + '---'.")
lines[i + 1:i + 1] = ["", B["count"][0]]
# 2. I.9: after I.8's last line (its STATUS), before the blank line, '---' and '## GROUP II'.
i = idx(A_I8)
if not entry_of(i).startswith(H_I8) or lines[i + 1] != "" or lines[i + 2] != "---" or not lines[i + 4].startswith(G_II):
    die("I.8's STATUS is not I.8's last line before the blank line, '---' and '## GROUP II'.")
if [ln for ln in lines[:i] if ln.startswith("### I")][-1] != entry_of(i):
    die("I.8 is not the last Group-I entry in file order.")
lines[i + 1:i + 1] = [""] + B["i9"]
# 3. The III.15 rider: after III.15's last line, before the blank line and '### III.16'.
i = idx(A_III15)
if not entry_of(i).startswith(H_III15) or lines[i + 1] != "" or not lines[i + 2].startswith(N_III15):
    die("the RE-SCOUT RETURN is not III.15's last line before the blank line and '### III.16'.")
lines[i + 1:i + 1] = B["iii15"]
# 4. The IV.9 rider: after IV.9's last line, before the blank line and '### IV.10'.
i = idx(A_IV9)
if not entry_of(i).startswith(H_IV9) or lines[i + 1] != "" or lines[i + 2] != N_IV9:
    die("the READ of 2026-09-24 is not IV.9's last line before the blank line and '### IV.10'.")
lines[i + 1:i + 1] = B["iv9"]
# 5. The IV.20 bullet, IV.21, IV.22: after IV.20's STATUS (its last line), before the blank line and '## GROUP V'.
i = idx(A_IV20)
if not entry_of(i).startswith(H_IV20) or lines[i + 1] != "" or lines[i + 2] != G_V:
    die("IV.20's STATUS is not IV.20's last line before the blank line and '## GROUP V'.")
if not [ln for ln in lines[:i] if ln.startswith("### IV.")][-1].startswith(H_IV20):
    die("IV.20 is not the last Group-IV entry in file order.")
lines[i + 1:i + 1] = B["iv20"] + [""] + B["iv21"] + [""] + B["iv22"]
# 6. The rows: after the table's last row (beta-shapes s35), before the blank line and the READ note.
i = idx(A_XREF)
if not lines[i - 1].startswith(P_XREF) or lines[i + 1] != "" or not lines[i + 2].startswith(N_XREF):
    die("the beta-shapes row is not the table's last row between the D2 row and the blank line + READ note.")
t = i
while t >= 0 and lines[t].startswith("|"):
    t -= 1
if lines[t + 1] != T_XREF or lines[t + 2] != "|---|---|---|" or lines[t] != "" or not lines[t - 1].startswith("## Cross-reference: program casualties"):
    die("the beta-shapes row is not in the cross-reference table under its column header.")
lines[i + 1:i + 1] = B["xref"]
new_text = "\n".join(lines)

# ---- Verification. ----
it = iter(lines)
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
if len(heads) != 62 or tally != {"I": 9, "II": 5, "III": 21, "IV": 22, "V": 5}:
    die("heading tally %d %r, expected 62 {I 9, II 5, III 21, IV 22, V 5}." % (len(heads), tally))
for ln in heads:
    if not re.match(r"### (I|II|III|IV|V)\.(\d+) ", ln):
        die("heading is not a numbered entry: %r" % ln[:80])
recount = "I: %d, II: %d, III: %d, IV: %d, V: %d" % (tally["I"], tally["II"], tally["III"], tally["IV"], tally["V"])
if recount not in B["count"][0] or "**%d entries**" % len(heads) not in B["count"][0]:
    die("the count paragraph's figures are not the recount (%s; %d)." % (recount, len(heads)))
order_iv = [int(re.match(r"### IV\.(\d+) ", ln).group(1)) for ln in heads if ln.startswith("### IV.")]
order_i = [int(re.match(r"### I\.(\d+) ", ln).group(1)) for ln in heads if ln.startswith("### I.")]
if order_iv != list(range(1, 16)) + [18, 16, 17, 19, 20, 21, 22] or order_i != list(range(1, 10)):
    die("file order: Group I %r, Group IV %r." % (order_i, order_iv))
ins = [x for k in NAMES for x in B[k] if x]
for ln in ins:
    if lines.count(ln) != 1:
        die("an inserted line occurs %d times: %r" % (lines.count(ln), ln[:80]))
P = lambda n: lines[n - 1]
checks = (
    (P(37).startswith(A_COUNT) and P(38) == "" and P(39) == B["count"][0] and P(40) == "" and P(41) == "---", "count at 39"),
    (P(134).startswith(A_I8) and P(135) == "" and [P(n) for n in range(136, 143)] == B["i9"] and P(143) == "" and P(144) == "---",
     "I.9 at 136-142"),
    (P(336).startswith(A_III15) and P(337) == B["iii15"][0] and P(338) == "" and P(339).startswith(N_III15), "III.15 rider at 337"),
    (P(492).startswith(A_IV9) and P(493) == B["iv9"][0] and P(494) == "" and P(495) == N_IV9, "IV.9 rider at 493"),
    (P(604).startswith(H_IV20) and P(610).startswith(A_IV20) and P(611) == B["iv20"][0] and P(612) == ""
     and [P(n) for n in range(613, 620)] == B["iv21"] and P(620) == "" and [P(n) for n in range(621, 628)] == B["iv22"]
     and P(628) == "" and P(629) == G_V, "IV.20 bullet 611, IV.21 613-619, IV.22 621-627, '## GROUP V' 629"),
    (P(710) == A_XREF and [P(n) for n in range(711, 716)] == B["xref"] and P(716) == "" and P(717).startswith(N_XREF), "rows 711-715"),
    (P(745).startswith("*(File discipline"), "file-discipline paragraph at 745"),
)
for ok, what in checks:
    if not ok:
        die("position check failed: %s." % what)
n21 = sum(1 for ln in lines if "IV.21" in ln)
n22 = sum(1 for ln in lines if "IV.22" in ln)
n9 = sum(1 for ln in lines if re.search(r"(?<![\w.])I\.9(?!\d)", ln))
if (n21, n22, n9) != (3, 5, 5):
    die("'IV.21' / 'IV.22' / 'I.9' on %d / %d / %d lines, expected 3 / 5 / 5." % (n21, n22, n9))
inserted = "\n".join(ins).lower()
for bad in LINT:
    if bad in inserted:
        die("the inserted text carries the linted phrase %r." % bad)

out_bytes = new_text.encode("utf-8")
out.write_bytes(out_bytes)
if out.read_bytes() != out_bytes:
    die("the file written does not read back byte for byte: %s." % out)
print("OK: <ENTRY-DATE> fill: %r; optional pairs applied: %s" % (FILL, ", ".join(sorted(set(applied))) if applied else "none"))
if slot9 == TOKEN:
    print("WARNING: block iv9 still carries %s -- a scratch run only; --in-place refuses until it is replaced." % TOKEN)
else:
    print("OK: the token is replaced in block iv9 by: %r" % slot9)
print("OK: %s written; %d -> %d lines (+%d); entries 62 (I 9, II 5, III 21, IV 22, V 5); blocks at 39 (count), 136-142 (I.9), "
      "337 (III.15 rider), 493 (IV.9 rider), 611 (IV.20 bullet), 613-619 (IV.21), 621-627 (IV.22), 711-715 (rows); SHA-256 %s%s"
      % (out, len(orig) - 1, len(lines) - 1, added, hashlib.sha256(out_bytes).hexdigest(),
         "" if out == ZOO.resolve() else "  [BARRIER-ZOO.md untouched]"))
