#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 40 zoo stream `zoo-s40` (2026-10-01): insert into BARRIER-ZOO.md the Group-I entry I.11 (Conjecture O is false at the
function-field rung: the necklace deletion), the I.10 rider (qcond-s38, with one sentence from qtwin-s39), three I.2 riders
(conj-O-s38; dz-half-s39; the withdrawal of the Session-39 candidate against Conjecture U), the I.9 and IV.1 riders
(fejer-form-s39), seven cross-reference rows and a dated count paragraph. Entries 63 -> 64 (I 11, II 5, III 21, IV 22, V 5);
765 -> 788 lines (+23).

The nine blocks are read AT RUN TIME from results/zoo-s40/zoo-entries-proposed.md (<!-- BLOCK:name --> ... <!-- END:name -->):
  count  a blank line + the paragraph after the Session-39 count paragraph (line 41), before the blank line and '---' (+2);
  i2o, i2dz, i2s5  the three I.2 riders after the Session-39 (alpha, beta)-frontier rider (line 87), before the thresholds
         rider (line 88, I.2's last line) (+3);
  i9     the rider after I.9's last line (line 147) (+1);
  i10    the rider after I.10's STATUS (line 155), I.10's last line (+1);   i11  a blank line + heading, blank, five bullets (+8);
  iv1    the rider after IV.1's last line, its Session-34 LINUX REPLAY (line 427) (+1);
  xref   seven rows after the row "| tournament s36 row T24 ..." (line 735), the table's last row (+7).

Gates, in order, before anything is written:
  1. idempotence: the input carries none of this stream's markers;
  2. full SHA-256 of the input zoo (e42d544d...) and of every source a block is re-derived from or quotes (see SOURCES);
  3. every copied block re-derived from its source with only the sanctioned pairs (D1, E1 -- or the brief's literal date fill
     with no E1, the same mode at all four copied heads -- and A1 on i10; optional O1 on i11's heading); every drafted block
     checked for shape, and every "quotation" in it found in its declared sources (whitespace-, ** - and backtick-normalized);
  4. every anchor asserted unique (full-text line heads) and its neighbors verified.
Insertion only. Afterwards: every original line survives, in order; 64 '### ' headings, 11/5/21/22/5; Group I in order
I.1-I.11 with I.11 the last entry before '## GROUP II'; each inserted line once and at its expected line; +23, 765 -> 788; one
trailing newline; none of the 10(g) linted phrases.

Usage:
  python3 scripts/zoo-insert-s40.py [--input PATH] [--proposed PATH] [--out PATH | --in-place]
    --input PATH     the zoo to read (default: BARRIER-ZOO.md); it must hash to e42d544d... .
    --proposed PATH  the blocks file (default: results/zoo-s40/zoo-entries-proposed.md; another path is for testing).
    --out PATH       where to write (default: a scratch file, <system temp dir>/zoo-insert-s40-out.md); never the input or
                     BARRIER-ZOO.md.
    --in-place       write over the input file. The script NEVER writes over its input without this flag.
Modeled on scripts/zoo-insert-s39.py. Prints the result's SHA-256 (the post-insertion hash for STATUS and LOG)."""
import argparse
import hashlib
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s40" / "zoo-entries-proposed.md"
ZOO_HASH_BEFORE = "e42d544dc144df1edb6342f00dca462738ccfa2f74ef6c9834c47a221aec4186"
R = ROOT / "results"
SOURCES = {  # name: (path, full SHA-256)
    "qcond_staged": (R / "qcond-s38" / "ZOO-LINES-STAGED.md", "61728f384770772ef9da4fcd3da82803b420868429aae666995494287434abbd"),
    "conjO_staged": (R / "conj-O-s38" / "ZOO-LINES-STAGED.md", "e75fb34759810ed6be3ccce5f3f59dfe2b48a85ef2dad688418a3022eac1bf79"),
    "fejer_note": (R / "fejer-form-s39" / "NOTE.md", "0ab5f19ed976a72ed507b271b40eb698d5b9cbfabad319214fc9eb4c406893c0"),
    "qtwin_note": (R / "qtwin-s39" / "NOTE.md", "0a7ea6be2449adf8f8a5cb5cf248e04d7c2317d6e0b9526b9fbaf2f1fa206af5"),
    "dz_note": (R / "dz-half-s39" / "NOTE.md", "51e062e9ddc3bb0edd092d1e9357e0f1c232df377c98554a826712b7d53bac3b"),
    "uoff_readF": (R / "u-offsurgery-s39" / "read-F.md", "c30a9ee3883b67b4f43dbfdcf89b37c4651473277ad964fdc49bf85c23406058"),
    "uoff_note": (R / "u-offsurgery-s39" / "NOTE.md", "ef143a4354b75580c17d619024d779de4484b0688fe886d7fce1cae9fddfc668"),
    "uoff_readO": (R / "u-offsurgery-s39" / "read-O.md", "f25749d79f2424a0daef8cf4de875d12132effbdc828fe30d5fd81a96211f4b5"),
    "s5_note": (R / "s5-multiplicity-s40" / "NOTE.md", "ced8b67448b79cddb4af13291230b550d15399ccb6fc349bf0fc7e8eaa5370ac"),
    "s5_recount": (R / "s5-multiplicity-s40" / "verify-F" / "recount_nK_F.log",
                   "8d959037a8f0a6b292ddf9543d543a7f892cdf3c29c6f8a3e4f32b071e8ee902"),
    "lemmaG_note": (R / "lemmaG-s39" / "NOTE.md", "41f195d40705ae77819b9a3805cd1323f0e5b7f3468e447c4db04b9e93b65d61"),
    "lemmaG_readF": (R / "lemmaG-s39" / "read-F.md", "1766f908ad081350bd246137f9c8b040f2d6b6aa7b1ec8353026fb7fb54f60e9"),
}
LINES_BEFORE, LINES_AFTER, ADDED = 765, 788, 23
LINT = ("clearly", "obviously", "easy to see", "well known", "well-known")
ENTRY = "entered at the Session-40 zoo stream"


def die(msg: str) -> None:
    sys.exit("zoo-insert-s40: STOP -- %s Nothing written." % msg)


ap = argparse.ArgumentParser(description="zoo-s40 insertion (I.11, the I.10 rider, three I.2 riders, I.9 and IV.1 riders, seven rows, the count).")
ap.add_argument("--input", default=str(ZOO), help="the zoo to read (default: BARRIER-ZOO.md)")
ap.add_argument("--proposed", default=str(PROPOSED), help="the proposed-blocks file (default: results/zoo-s40/zoo-entries-proposed.md)")
mode = ap.add_mutually_exclusive_group()
mode.add_argument("--out", help="write the result here (default: a scratch file in the system temp directory)")
mode.add_argument("--in-place", action="store_true", help="write the result over the input file")
args = ap.parse_args()

inp = Path(args.input).resolve()
if args.in_place:
    out = inp
else:
    out = Path(args.out).resolve() if args.out else Path(tempfile.gettempdir()).resolve() / "zoo-insert-s40-out.md"
    if out == inp:
        die("--out names the input file; writing over the input needs --in-place.")
    if out == ZOO.resolve():
        die("--out names BARRIER-ZOO.md; writing the zoo needs --in-place (with the zoo as --input).")

# ---- Gate 1: idempotence (before the hash, so a second run says why it stops). ----
zoo_bytes = inp.read_bytes()
zoo_text = zoo_bytes.decode("utf-8")
MARKERS = ("### I.11 ", "**Entry count (dated, Session 40,", ENTRY, "| unit `qcond-s38` ", "| unit `qtwin-s39` ",
           "| unit `conj-O-s38` ", "| unit `dz-half-s39` ", "| unit `u-offsurgery-s39` ", "| unit `lemmaG-s39` ",
           "| unit `fejer-form-s39` ", "Successor `results/qtwin-s39/`", "THE SESSION-39 CANDIDATE AGAINST CONJECTURE U IS WITHDRAWN",
           "(unit `dz-half-s39`:", "(unit `conj-O-s38`:", "(unit `qcond-s38`:", "(`results/fejer-form-s39/NOTE.md` §")
for m in MARKERS:
    if m in zoo_text:
        die("%s already carries %r -- this stream's text is in it; refusing to insert twice." % (inp.name, m))

# ---- Gate 2: hashes (full SHA-256). ----
got = hashlib.sha256(zoo_bytes).hexdigest()
if got != ZOO_HASH_BEFORE:
    die("%s SHA-256 is %s, expected %s -- someone edited the zoo; the orchestrator re-anchors." % (inp, got, ZOO_HASH_BEFORE))
SRC = {}
for name, (path, want) in SOURCES.items():
    if not path.is_file():
        die("source %s is missing." % path.relative_to(ROOT))
    raw = path.read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    if got != want:
        die("%s SHA-256 is %s, expected %s -- the source record changed." % (path.relative_to(ROOT), got, want))
    SRC[name] = raw.decode("utf-8")

# ---- Gate 3: the blocks against the sources. ----
prop_path = Path(args.proposed).resolve()
prop_text = prop_path.read_text(encoding="utf-8")


def block(name: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)), prop_text, re.S)
    if len(ms) != 1:
        die("block %s occurs %d times in %s (need exactly 1)." % (name, len(ms), prop_path))
    return ms[0]


NAMES = ("count", "i2o", "i2dz", "i2s5", "i9", "i10", "i11", "iv1", "xref")
SIZES = {"count": 1, "i2o": 1, "i2dz": 1, "i2s5": 1, "i9": 1, "i10": 1, "i11": 7, "iv1": 1, "xref": 7}
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
    if t != t.strip() or any(ln != ln.rstrip() for ln in v):
        die("block %s has leading or trailing whitespace on a line." % k)


def once(text: str, old: str, new: str, tag: str) -> str:
    if text.count(old) != 1:
        die("pair %s: its OLD string occurs %d times (need exactly 1): %r" % (tag, text.count(old), old[:80]))
    return text.replace(old, new)


def one_line(src: str, head: str, what: str) -> str:
    hits = [ln for ln in src.split("\n") if ln.startswith(head)]
    if len(hits) != 1:
        die("%s: the source line with head %r occurs %d times." % (what, head[:60], len(hits)))
    return hits[0]


def note_block(src: str, name: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (name, name), src, re.S)
    if len(ms) != 1 or "\n" in ms[0]:
        die("the fejér NOTE's BLOCK:%s is not one line." % name)
    return ms[0]


# Copied words: the two staged riders and rows, the two fejér riders.
STQ = one_line(SRC["qcond_staged"], "- **[RIDER <ENTRY-DATE>, Session 39 (unit `qcond-s38`", "qcond Block (i)")
STO = one_line(SRC["conjO_staged"], "- **[RIDER <ENTRY-DATE>, Session 39 (unit `conj-O-s38`", "conj-O Block (i)")
ROWQ = one_line(SRC["qcond_staged"], "| unit `qcond-s38` ", "qcond Block (ii)")
ROWO = one_line(SRC["conjO_staged"], "| unit `conj-O-s38` ", "conj-O Block (ii)")
FIV1 = note_block(SRC["fejer_note"], "iv1")
FI9 = note_block(SRC["fejer_note"], "i9")
E1 = {"q": ("m1–m7 applied) — the rigidity", "m1–m7 applied; %s) — the rigidity" % ENTRY),
      "o": ("m1–m12 applied) — Conjecture O", "m1–m12 applied; %s) — Conjecture O" % ENTRY),
      "iv1": ("§3, §5) — on rung 1", "§3, §5; %s) — on rung 1" % ENTRY),
      "i9": ("§4, §6, §7) — positive forms", "§4, §6, §7; %s) — positive forms" % ENTRY)}
# The mode is read from i2o's head and then required at all four copied heads: "house" = D1 fill "2026-10-01" + E1 everywhere;
# "literal" = the brief's fill "2026-10-01 (Session 40)" and no E1 (the fejér heads then verbatim).
MODES = {"house": "2026-10-01", "literal": "2026-10-01 (Session 40)"}
seen = [m for m, fill in MODES.items() if B["i2o"][0].startswith("- **[RIDER %s, Session 39 (unit `conj-O-s38`" % fill)]
if len(seen) != 1:
    die("block i2o's head carries neither sanctioned date fill %r." % (tuple(MODES.values()),))
MODE = seen[0]


def copied(src: str, key: str, fill_date: bool) -> str:
    w = once(src, "<ENTRY-DATE>", MODES[MODE], "D1") if fill_date else src
    return once(w, E1[key][0], E1[key][1], "E1") if MODE == "house" else w


if B["i2o"] != [copied(STO, "o", True)]:
    die("block i2o is not conj-O staged Block (i) with D1%s (and nothing else)." % (", E1" if MODE == "house" else ""))
if B["iv1"] != [copied(FIV1, "iv1", False)]:
    die("block iv1 is not the fejér NOTE's BLOCK:iv1%s (and nothing else)." % (" with E1" if MODE == "house" else ""))
if B["i9"] != [copied(FI9, "i9", False)]:
    die("block i9 is not the fejér NOTE's BLOCK:i9%s (and nothing else)." % (" with E1" if MODE == "house" else ""))
# i10 = qcond staged Block (i) with D1 (E1) + one space + A1, one drafted sentence.
WQ = copied(STQ, "q", True)
L10 = B["i10"][0]
if not WQ.endswith("any brief resting on a discrete RH-false Beurling system with Riemann's exact FE."):
    die("qcond staged Block (i) no longer ends where A1 is appended.")
if not L10.startswith(WQ + " Successor `results/qtwin-s39/` ("):
    die("block i10 is not qcond staged Block (i) with D1%s, then ' Successor `results/qtwin-s39/` (…'." % (", E1" if MODE == "house" else ""))
A1 = L10[len(WQ) + 1:]
if not A1.endswith("Hilberdink 2012, Acta Arith. 152, Prop. 3.4, Thms 4.3, 4.4, C.") or re.search(r"\.\s+[A-Z]", A1[:-1]):
    die("A1 is not one sentence ending '… Hilberdink 2012, Acta Arith. 152, Prop. 3.4, Thms 4.3, 4.4, C.'.")
# xref: rows 1 and 3 staged verbatim; rows 2, 4-7 drafted, each three cells, heads as listed.
if B["xref"][0] != ROWQ or B["xref"][2] != ROWO:
    die("xref rows 1 and 3 are not the staged rows verbatim.")
ROW_HEADS = {1: "| unit `qtwin-s39` (", 3: "| unit `dz-half-s39` (", 4: "| unit `u-offsurgery-s39` S5(0.8) (",
             5: "| unit `lemmaG-s39` (", 6: "| unit `fejer-form-s39` ("}
for j, row in enumerate(B["xref"]):
    if not (row.startswith("| ") and row.endswith(" |")) or len(row[2:-2].split(" | ")) != 3:
        die("xref row %d is not a three-cell table row." % (j + 1))
    if j in ROW_HEADS and not row.startswith(ROW_HEADS[j]):
        die("xref row %d does not start %r." % (j + 1, ROW_HEADS[j]))

# Drafted words: shapes, and every "quotation" found in its declared sources (normalized: whitespace, ** and backticks).
norm = lambda s: re.sub(r"\s+", " ", s.replace("**", "").replace("`", "")).strip()
NS = {k: norm(v) for k, v in SRC.items()}
QUOTE_SRC = {"i2dz": ("dz_note",), "i2s5": ("uoff_readF", "uoff_readO", "uoff_note", "s5_note", "s5_recount"),
             "i11": ("lemmaG_note", "lemmaG_readF")}
n_quotes = {}
for k, srcs in QUOTE_SRC.items():
    t = "\n".join(B[k])
    if t.count('"') % 2:
        die("block %s has an odd number of double quotes." % k)
    qs = re.findall(r'"([^"]+)"', t)
    n_quotes[k] = len(qs)
    for q in qs:
        if not any(norm(q) in NS[s] for s in srcs):
            die("block %s quotes %r, which is not in %s." % (k, q[:70], ", ".join(srcs)))
A1_KEYS = ("the masses may take infinitely many values", "bounded-frequency multiplier", "thin rational part", "(R1)–(R4)",
           "Π_ζ + log*(m) ≥ 0", "no new Group-I control is claimed", "printed core of L′/L‴ for rational finite multipliers",
           "Prop. 3.4, Thms 4.3, 4.4, C", "Hilberdink 2012, Acta Arith. 152")
for key in A1_KEYS:
    if key not in A1 or norm(key) not in NS["qtwin_note"]:
        die("A1 and the qtwin NOTE do not share the phrase %r." % key)
H_DZ = "- **[RIDER 2026-10-01, Session 40 (unit `dz-half-s39`: `results/dz-half-s39/NOTE.md` §0, §2, §5, §6;"
H_S5 = "- **[RIDER 2026-10-01, Session 40 (unit `u-offsurgery-s39`: `results/u-offsurgery-s39/read-F.md` §2–§3"
for k, head in (("i2dz", H_DZ), ("i2s5", H_S5)):
    if not B[k][0].startswith(head) or ENTRY + ") — " not in B[k][0] or B[k][0].count("]** ") != 1:
        die("block %s is not a dated rider '%s … %s) — …]** …'." % (k, head[:40], ENTRY))
S5 = B["i2s5"][0]
if (S5.count("THE SESSION-39 CANDIDATE AGAINST CONJECTURE U IS WITHDRAWN") != 1 or S5.count("[single-check; read owed]") != 1
        or S5.count("T1–T4") != 1 or re.search(r"\bT[1-4]\b", S5.replace("T1–T4", ""))):
    die("block i2s5 must name T1–T4 once, in one clause labeled '[single-check; read owed]', and nowhere else.")
O1 = ("— NEW, Session 40 (unit `lemmaG-s39`", "— NEW, Session 39 (unit `lemmaG-s39`")
I11 = B["i11"]
applied = []
if not I11[0].startswith("### I.11 Conjecture O is false at the function-field rung (the necklace deletion"):
    die("block i11's heading does not start '### I.11 Conjecture O is false at the function-field rung (the necklace deletion'.")
if I11[0].count(O1[0]) + I11[0].count(O1[1]) != 1 or not I11[0].endswith("; entered 2026-10-01, Session 40)"):
    die("block i11's heading must carry one of %r and end '; entered 2026-10-01, Session 40)'." % (O1,))
if O1[1] in I11[0]:
    applied.append("O1")
BUL = ("- **STATEMENT.** ", "- **KILLS / RETURNS.** ", "- **EXECUTABLE TEST.** ", "- **SOURCE.** ", "- **STATUS.** ")
if I11[1] != "" or any(not I11[2 + j].startswith(b) for j, b in enumerate(BUL)):
    die("block i11 must be the heading, a blank line and the five bullets %r." % (BUL,))
CNT = B["count"][0]
for need in ("**Entry count (dated, Session 40, 2026-10-01).** I.11 (", "765 → %d lines" % LINES_AFTER, "SHA-256 at launch e42d544d…",
             "`results/zoo-s40/`", "Group I 10 → 11, the new entry placed after I.10"):
    if need not in CNT:
        die("block count lacks %r." % need)
for q in re.findall(r'"(unit `[^"]+`)"', CNT):
    if not any(row.startswith("| %s " % q) for row in B["xref"]):
        die("block count names the row %r, which xref does not carry." % q)
if len(re.findall(r'"(unit `[^"]+`)"', CNT)) != len(B["xref"]):
    die("block count does not name each of the %d rows." % len(B["xref"]))
zoo_lines_set = set(zoo_text.split("\n"))
for k in NAMES:
    for ln in B[k]:
        if ln and ln in zoo_lines_set:
            die("an inserted line of block %s is already a line of the zoo: %r" % (k, ln[:80]))
        if k != "i11" and ln.lstrip().startswith("#"):
            die("block %s would add a heading." % k)
if any(ln.lstrip().startswith("#") for ln in I11[1:]):
    die("block i11 must carry exactly one heading.")

# ---- Gate 4: anchors (each asserted unique as a line head; neighbors verified). ----
lines = zoo_text.split("\n")
orig = list(lines)
if lines[-1] != "" or lines[-2] == "":
    die("the input must end with exactly one newline.")
if len(orig) - 1 != LINES_BEFORE:
    die("the input has %d lines, expected %d." % (len(orig) - 1, LINES_BEFORE))
A_COUNT = "**Entry count (dated, Session 39, 2026-10-01).** I.10 (rigidity at conductor 1"
P_COUNT = "**Entry count (dated, Session 37, 2026-09-30).**"
H_I2 = "### I.2 The Beurling counterexample factory (DMV / BDR / Broucke school)"
A_I2F = ("- **[RIDER 2026-10-01, Session 38 (novel wave 2, seed M1b `beurling-frontier`: "
         "`results/novel-wave-s37/beurling-frontier/NOTE.md` §1–§7;")
A_I2T = ("- **[RIDER 2026-10-01, Session 38 (novel wave 2, seed M1b `beurling-frontier`: "
         "`results/novel-wave-s37/beurling-frontier/NOTE.md` §2, Corollary 2.2")
N_I3 = "### I.3 The Alternative Hypothesis world + the 256-periodic"
H_I9 = "### I.9 The rung-1 twin: the virtual curve over F₅"
A_I9 = "- **[RIDER 2026-10-01, Session 38 (novel wave 2, seed M2 `proof-mine`: `results/novel-wave-s37/proof-mine/NOTE.md` §1, §4;"
H_I10 = "### I.10 Rigidity at conductor 1: the rational primes are the only Beurling system"
A_I10 = "- **STATUS.** program-adjudicated — dual-model: writer Opus 5.5, Session 37; reader Fable 5.1 `read-F.md` AGREES, Session 38"
G_II = "## GROUP II — FORMALIZED CEILINGS"
H_IV1 = '### IV.1 The "Weil positivity in disguise" containment audit'
A_IV1 = ("- **[LINUX REPLAY 2026-09-29, Session 34 (`results/linux-check-s33/`; HARVEST-NOTE.md; entered at the Session-34 zoo "
         "stream).]** Both H5 top")
N_IV2 = "### IV.2 The tilted-EF cosh ghost"
T_XREF = "| Casualty | Verdict | Killing barriers |"
A_XREF = "| tournament s36 row T24 (Stepanov auxiliary polynomials transplanted to Z) — its G-line"
P_XREF = "| novel wave s37 M2 `proof-mine`"
N_XREF = "**[READ 2026-09-10, Opus 5.]** The three Session-21 rows above were checked against their records"
ANCHORS = (A_COUNT, P_COUNT, H_I2, A_I2F, A_I2T, N_I3, H_I9, A_I9, H_I10, A_I10, G_II, H_IV1, A_IV1, N_IV2, T_XREF, A_XREF,
           P_XREF, N_XREF)
for a in ANCHORS:
    n = sum(1 for ln in lines if ln.startswith(a))
    if n != 1:
        die("the anchor string is not unique in the zoo (%d hits): %r" % (n, a[:100]))


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


# Bottom-up (each index is re-found by text, so the order is for the record only).
# 1. The rows: after the T24 row, the table's last row, before the blank line and the READ note.
i = idx(A_XREF)
if not lines[i - 1].startswith(P_XREF) or lines[i + 1] != "" or not lines[i + 2].startswith(N_XREF):
    die("the T24 row is not the table's last row between the M2 row and the blank line + READ note.")
t = i
while t >= 0 and lines[t].startswith("|"):
    t -= 1
if lines[t + 1] != T_XREF or lines[t + 2] != "|---|---|---|" or lines[t] != "" or not lines[t - 1].startswith("## Cross-reference: program casualties"):
    die("the T24 row is not in the cross-reference table under its column header.")
lines[i + 1:i + 1] = B["xref"]
# 2. The IV.1 rider: after IV.1's last line (the Session-34 LINUX REPLAY), before the blank line and '### IV.2'.
i = idx(A_IV1)
if not entry_of(i).startswith(H_IV1) or lines[i + 1] != "" or not lines[i + 2].startswith(N_IV2):
    die("the Session-34 LINUX REPLAY is not IV.1's last line before the blank line and '### IV.2'.")
lines[i + 1:i + 1] = B["iv1"]
# 3-4. The I.10 rider, then I.11: after I.10's STATUS (its last line), before the blank line, '---' and '## GROUP II'.
i = idx(A_I10)
if not entry_of(i).startswith(H_I10) or lines[i + 1] != "" or lines[i + 2] != "---" or lines[i + 3] != "" or not lines[i + 4].startswith(G_II):
    die("I.10's STATUS is not I.10's last line before the blank line, '---' and '## GROUP II'.")
if [ln for ln in lines[:i] if ln.startswith("### I")][-1] != entry_of(i):
    die("I.10 is not the last Group-I entry in file order.")
lines[i + 1:i + 1] = B["i10"] + [""] + B["i11"]
# 5. The I.9 rider: after I.9's last line (its Session-38 rider), before the blank line and '### I.10'.
i = idx(A_I9)
if not entry_of(i).startswith(H_I9) or lines[i + 1] != "" or not lines[i + 2].startswith(H_I10):
    die("I.9's Session-38 rider is not I.9's last line before the blank line and '### I.10'.")
lines[i + 1:i + 1] = B["i9"]
# 6. The three I.2 riders: after the (alpha, beta)-frontier rider, before the thresholds rider (I.2's last line).
i = idx(A_I2F)
if (not entry_of(i).startswith(H_I2) or not lines[i + 1].startswith(A_I2T) or lines[i + 2] != ""
        or not lines[i + 3].startswith(N_I3)):
    die("the frontier rider is not followed by the thresholds rider, the blank line and '### I.3' inside I.2.")
lines[i + 1:i + 1] = B["i2o"] + B["i2dz"] + B["i2s5"]
# 7. The count paragraph: after the Session-39 paragraph, before the blank line and '---'.
i = idx(A_COUNT)
if any(ln.startswith("### ") or ln.startswith("## ") for ln in lines[:i]):
    die("the Session-39 count paragraph is not in the header.")
if not lines[i - 2].startswith(P_COUNT) or lines[i - 1] != "" or lines[i + 1] != "" or lines[i + 2] != "---":
    die("the Session-39 count paragraph is not between the Session-37 paragraph and the blank line + '---'.")
lines[i + 1:i + 1] = ["", B["count"][0]]
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
if len(heads) != 64 or tally != {"I": 11, "II": 5, "III": 21, "IV": 22, "V": 5}:
    die("heading tally %d %r, expected 64 {I 11, II 5, III 21, IV 22, V 5}." % (len(heads), tally))
for ln in heads:
    if not re.match(r"### (I|II|III|IV|V)\.(\d+) ", ln):
        die("heading is not a numbered entry: %r" % ln[:80])
recount = "I: %d, II: %d, III: %d, IV: %d, V: %d" % (tally["I"], tally["II"], tally["III"], tally["IV"], tally["V"])
if recount not in CNT or "**%d entries**" % len(heads) not in CNT or "11 + 5 + 21 + 22 + 5 = %d" % len(heads) not in CNT:
    die("the count paragraph's figures are not the recount (%s; %d)." % (recount, len(heads)))
order_i = [int(re.match(r"### I\.(\d+) ", ln).group(1)) for ln in heads if ln.startswith("### I.")]
order_iv = [int(re.match(r"### IV\.(\d+) ", ln).group(1)) for ln in heads if ln.startswith("### IV.")]
if order_i != list(range(1, 12)) or order_iv != list(range(1, 16)) + [18, 16, 17, 19, 20, 21, 22]:
    die("file order: Group I %r, Group IV %r." % (order_i, order_iv))
have = set(re.match(r"### ((?:I|II|III|IV|V)\.\d+) ", ln).group(1) for ln in heads)
ins_text = "\n".join("\n".join(B[k]) for k in NAMES)
cited = set(a + "." + b for a, b in re.findall(r"(?<![\w.])(I{1,3}|IV|V)\.(\d+)(?!\d)", ins_text))
if cited - have:
    die("the new text cites entries that do not exist: %r" % sorted(cited - have))
for ln in [x for k in NAMES for x in B[k] if x]:
    if lines.count(ln) != 1:
        die("an inserted line occurs %d times: %r" % (lines.count(ln), ln[:80]))
P = lambda n: lines[n - 1]
checks = (
    (P(41).startswith(A_COUNT) and P(42) == "" and P(43) == CNT and P(44) == "" and P(45) == "---", "count at 43"),
    (P(89).startswith(A_I2F) and [P(90), P(91), P(92)] == B["i2o"] + B["i2dz"] + B["i2s5"] and P(93).startswith(A_I2T)
     and P(94) == "" and P(95).startswith(N_I3), "I.2 riders at 90-92"),
    (P(152).startswith(A_I9) and P(153) == B["i9"][0] and P(154) == "" and P(155).startswith(H_I10), "I.9 rider at 153"),
    (P(161).startswith(A_I10) and P(162) == B["i10"][0] and P(163) == "" and [P(n) for n in range(164, 171)] == I11
     and P(171) == "" and P(172) == "---" and P(173) == "" and P(174).startswith(G_II), "I.10 rider 162, I.11 at 164-170"),
    (P(442).startswith(A_IV1) and P(443) == B["iv1"][0] and P(444) == "" and P(445).startswith(N_IV2), "IV.1 rider at 443"),
    (P(751).startswith(A_XREF) and [P(n) for n in range(752, 759)] == B["xref"] and P(759) == "" and P(760).startswith(N_XREF),
     "rows at 752-758"),
)
for ok, what in checks:
    if not ok:
        die("position check failed: %s." % what)

out.write_text(new_text, encoding="utf-8")
digest = hashlib.sha256(new_text.encode("utf-8")).hexdigest()
print("zoo-insert-s40: OK -- wrote %s" % out)
print("  %d -> %d lines (+%d); 63 -> %d entries, %s; mode %r (date fill %r); optional pairs applied: %s"
      % (len(orig) - 1, len(lines) - 1, added, len(heads), recount, MODE, MODES[MODE], ", ".join(applied) or "none"))
print("  quotations checked: %s; A1 key phrases: %d; cited entries: %s" % (n_quotes, len(A1_KEYS), ", ".join(sorted(cited))))
print("  SHA-256 %s" % digest)
