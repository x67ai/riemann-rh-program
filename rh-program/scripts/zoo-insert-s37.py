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
