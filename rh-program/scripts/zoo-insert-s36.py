#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 36 zoo stream `zoo-s36` (2026-09-30): insert into BARRIER-ZOO.md the Group-IV entry IV.20 (the finite-rank target
kill; beta-shapes, results/beta-shapes-s35/NOTE.md section 2.3), the IV.10 rider (the TARGET-RANK check), one cross-reference
row and a dated count paragraph. Group IV 19 -> 20; entries 58 -> 59 (I 8, II 5, III 21, IV 20, V 5); 699 -> 711 lines (+12).

The four blocks are read AT RUN TIME from results/zoo-s36/zoo-entries-proposed.md (delimited <!-- BLOCK:name --> ...
<!-- END:name -->), so an OLD/NEW pair the orchestrator applies there flows into the insertion:
  count  one line: a blank line and this paragraph go directly after the Session-34 count paragraph (line 35), before the
         blank line 36 and the '---' at 37 (+2);
  iv10   one line: the rider goes directly after IV.10's last line, the Session-28 E3 RIDER (line 489), before the blank line
         490 and '### IV.11' at 491 (+1);
  iv20   seven lines -- the '### IV.20' heading, a blank line, the five bullets STATEMENT / KILLS / RETURNS / EXECUTABLE TEST /
         SOURCE / STATUS: a blank line and the block go directly after IV.19's last line, the PRECISION READ (line 587), the
         true end of Group IV in file order (IV.1-IV.15, IV.18, '---', IV.16, IV.17, IV.19); the existing blank line 588 then
         separates IV.20 from '## GROUP V' at 589, which has no '---' before it in this file (+8);
  xref   one line: the row goes directly after the cross-reference table's last row, the D2 design-axis scout row (line
         669), before the blank line 670 (+1).

Order of the gates, before anything is written:
  1. idempotence guard: the input must carry none of this stream's markers (a second run stops here, not at the hash);
  2. hash gate on the input zoo (full SHA-256 8e66cdc0de6f13f5...; a byte-identical scratch copy passes) and on
     results/beta-shapes-s35/ZOO-LINES-STAGED.md (bc6e2411...);
  3. the blocks against the staged text: the rider is staged line 16 byte for byte; the IV.20 heading is staged line 7 with
     the brief's heading edit and nothing else; STATEMENT, KILLS / RETURNS, EXECUTABLE TEST, SOURCE are staged lines 8-11
     byte for byte; STATUS is staged line 12 with "(verdict to be entered by the zoo stream)" replaced by the reader's verdict
     the brief prints -- the two sanctioned edits. The script also accepts any subset of the FIX-FIRST pairs FF1-FF6 (the
     proposed file's finding 8), each applied whole or not at all, and prints which are applied; no other change passes;
     the xref row is the brief's three cells verbatim; the count paragraph carries the recount computed here;
  4. every anchor asserted unique in the input (full text of the neighboring lines, never a line number alone) and the lines
     around it checked, so each placement is verified, not assumed.
Pure insertion: no existing line is modified or removed. Afterwards it verifies that every original line survives, in order;
that the '### ' headings number 59 with 8/5/21/20/5; that Group IV reads IV.1-IV.15, IV.18, IV.16, IV.17, IV.19, IV.20 in
file order with IV.20 the last entry before '## GROUP V'; that each inserted line occurs exactly once and sits at its expected
line (count 37, rider 492, heading 592, bullets 594-598, '## GROUP V' 600, row 681); +12 lines, 699 -> 711; one trailing
newline; none of the 10(g) linted phrases in the inserted text.

Usage:
  python3 scripts/zoo-insert-s36.py [--input PATH] [--proposed PATH] [--out PATH | --in-place]
    --input PATH   the zoo to read (default: BARRIER-ZOO.md); it must hash to 8e66cdc0... .
    --proposed PATH  the blocks file (default: results/zoo-s36/zoo-entries-proposed.md; another path is for testing).
    --out PATH     where to write the result (default: a scratch file, <system temp dir>/zoo-insert-s36-out.md).
                   --out may not name the input file or BARRIER-ZOO.md.
    --in-place     write the result over the input file. The script NEVER writes over its input without this flag.
Modeled on scripts/zoo-insert-s35.py.
"""
import argparse
import hashlib
import itertools
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s36" / "zoo-entries-proposed.md"
STAGED = ROOT / "results" / "beta-shapes-s35" / "ZOO-LINES-STAGED.md"
ZOO_HASH_BEFORE = "8e66cdc0de6f13f598191b5fd10c4a2e7220ef6d1af7397dd8f4157a25bdfae8"
STAGED_HASH = "bc6e241120f5af37bd55c015bed107254f11205d4c09b363b1a662172df87001"
LINES_BEFORE, LINES_AFTER, ADDED = 699, 711, 12
LINT = ("clearly", "obviously", "easy to see", "well known", "well-known")


def die(msg: str) -> None:
    sys.exit("zoo-insert-s36: STOP -- %s Nothing written." % msg)


ap = argparse.ArgumentParser(description="zoo-s36 insertion (IV.20, the IV.10 rider, one cross-reference row, the count paragraph).")
ap.add_argument("--input", default=str(ZOO), help="the zoo to read (default: BARRIER-ZOO.md)")
ap.add_argument("--proposed", default=str(PROPOSED), help="the proposed-blocks file (default: results/zoo-s36/zoo-entries-proposed.md)")
mode = ap.add_mutually_exclusive_group()
mode.add_argument("--out", help="write the result here (default: a scratch file in the system temp directory)")
mode.add_argument("--in-place", action="store_true", help="write the result over the input file")
args = ap.parse_args()

inp = Path(args.input).resolve()
if args.in_place:
    out = inp
else:
    out = Path(args.out).resolve() if args.out else Path(tempfile.gettempdir()).resolve() / "zoo-insert-s36-out.md"
    if out == inp:
        die("--out names the input file; writing over the input needs --in-place.")
    if out == ZOO.resolve():
        die("--out names BARRIER-ZOO.md; writing the zoo needs --in-place (with the zoo as --input).")

# ---- Gate 1: idempotence (before the hash, so a second run says why it stops). ----
zoo_bytes = inp.read_bytes()
zoo_text = zoo_bytes.decode("utf-8")
MARKERS = ("### IV.20 ", "**Entry count (dated, Session 36, 2026-09-30).**", "- **[RIDER 2026-09-29, Session 35",
           "| β-shapes s35 (", "TARGET-RANK", "entered 2026-09-30, Session 36", "Session-36 zoo stream")
for m in MARKERS:
    if m in zoo_text:
        die("%s already carries %r -- this stream's text is in it; refusing to insert twice." % (inp.name, m))

# ---- Gate 2: hashes. ----
got = hashlib.sha256(zoo_bytes).hexdigest()
if got != ZOO_HASH_BEFORE:
    die("%s SHA-256 is %s, expected %s -- someone edited the zoo; the orchestrator re-anchors." % (inp, got, ZOO_HASH_BEFORE))
got = hashlib.sha256(STAGED.read_bytes()).hexdigest()
if got != STAGED_HASH:
    die("%s SHA-256 is %s, expected %s -- the staged record changed." % (STAGED.relative_to(ROOT), got, STAGED_HASH))

# ---- Gate 3: the blocks against the staged text. ----
prop_path = Path(args.proposed).resolve()
prop_text = prop_path.read_text(encoding="utf-8")


def block(name: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)), prop_text, re.S)
    if len(ms) != 1:
        die("block %s occurs %d times in %s (need exactly 1)." % (name, len(ms), prop_path))
    return ms[0]


B = {k: block(k) for k in ("count", "iv10", "iv20", "xref")}
for k, v in B.items():
    if not v.strip():
        die("block %s is empty." % k)
    for bad in LINT:
        if bad in v.lower():
            die("block %s carries the linted phrase %r (10(g))." % (k, bad))
    if "\t" in v or "\r" in v:
        die("block %s carries a tab or a carriage return." % k)
for k in ("count", "iv10", "xref"):
    if "\n" in B[k]:
        die("block %s must be exactly one line." % k)
iv20 = B["iv20"].split("\n")
if len(iv20) != 7:
    die("block iv20 must be seven lines (heading, blank, five bullets); it has %d." % len(iv20))

staged = STAGED.read_text(encoding="utf-8").split("\n")


def staged_line(prefix: str) -> str:
    hits = [ln for ln in staged if ln.startswith(prefix)]
    if len(hits) != 1:
        die("the staged file carries %d lines beginning %r (need exactly 1)." % (len(hits), prefix))
    return hits[0]


S_HEAD = staged_line("- **IV.20 ")
S_STATEMENT = staged_line("- **STATEMENT.**")
S_KILLS = staged_line("- **KILLS / RETURNS.**")
S_TEST = staged_line("- **EXECUTABLE TEST.**")
S_SOURCE = staged_line("- **SOURCE.**")
S_STATUS = staged_line("- **STATUS.**")
S_RIDER = staged_line("- **[RIDER 2026-09-29, Session 35")

# Sanctioned edit 1 (the brief, item 1): the heading as a '###' line in the house style, "; entered 2026-09-30, Session 36" added.
TITLE = "IV.20 The finite-rank target kill (no surface over a field, and no target of finite Q-rank, can carry ζ's diagonal row)"
TAIL_STAGED = " — NEW, Session 35 (β-shapes, `results/beta-shapes-s35/NOTE.md` §2.3)"
TAIL_BRIEF = " — NEW, Session 35 (β-shapes, `results/beta-shapes-s35/NOTE.md` §2.3; entered 2026-09-30, Session 36)"
if S_HEAD != "- **" + TITLE + TAIL_STAGED + "**":
    die("the staged heading line is not the one the brief names.")
HEADING = "### " + TITLE + TAIL_BRIEF
# Sanctioned edit 2 (the brief, item 1): the reader's verdict in place of the placeholder.
OLD_VERDICT = "(verdict to be entered by the zoo stream)"
NEW_VERDICT = ("AGREES-WITH-CORRECTIONS 2026-09-29 (Theorem R PROVED from A5 + A9 with real values and one fixed κ, Euclid and "
               "unique factorization; A7 only names the fibers; converse dim_Q G ≤ |char(B)| proved by the reader; 29 OLD/NEW pairs "
               "applied 2026-09-30 with each FIX-FIRST re-derived at the line by the orchestrator)")
if S_STATUS.count(OLD_VERDICT) != 1:
    die("the staged STATUS line does not carry %r exactly once." % OLD_VERDICT)
BASE = {"STATEMENT": S_STATEMENT, "KILLS": S_KILLS, "TEST": S_TEST, "SOURCE": S_SOURCE,
        "STATUS": S_STATUS.replace(OLD_VERDICT, NEW_VERDICT), "RIDER": S_RIDER}

# The FIX-FIRST pairs of the proposed file's finding 8. The writer applies none; the orchestrator may apply any, whole.
FIX_FIRST = (
    ("FF1", "STATEMENT",
     "with Num(Y) of infinite rank and the Hodge index available only in a regularized form (the SPEC's A8′, A11′, A13′).",
     "with Num(Y) of infinite rank (the SPEC's A11′, read as amended from 2026-09-30; the note's A8′ and A13′, the regularized "
     "adjunction and generator clauses, are HELD by the same PRECISION and not adopted)."),
    ("FF2", "RIDER",
     "- **[RIDER 2026-09-29, Session 35 — on IV.10, after the E3 rider.]**",
     "- **[RIDER 2026-09-29, Session 35 (β-shapes, `results/beta-shapes-s35/NOTE.md`, cited below as NOTE; Opus 5 reader "
     "`read-O.md` §4; entered at the Session-36 zoo stream) — on IV.10, after the E3 rider.]**"),
    ("FF3", "STATUS",
     "- **STATUS.** program-derived — writer Fable 5.1, Session 35;",
     "- **STATUS.** program-adjudicated — dual-model: writer Fable 5.1, Session 35;"),
    ("FF4", "STATUS",
     "Deninger's dictionary line \"number of residue characteristics ↔ rank of the period group\" (x-18 p. 4, an analogy)",
     "Deninger's dictionary row \"Number of residue characteristics |char(X)| of X\" ↔ \"rank of period group Λ of (X, F, φ^t)\" "
     "(x-18 p. 4, Dictionary 4, part 2; an analogy)"),
    ("FF5", "RIDER",
     "so \"this rider claims no Z-form of Theorems 4.1(b)\" may be read as \"4.1(b) holds over Z\".",
     "so in its scope sentence \"this rider claims no Z-form of Theorems 4.1(b) or 4.2\" the 4.1(b) half may be read as "
     "\"4.1(b) holds over Z\" (4.2 is unchanged)."),
    ("FF6", "KILLS",
     "\"the archimedean place\" (Borger p. 5)",
     "\"the archimedean place\" (Borger 0906.3146 p. 5)"),
)
for tag, where, old, new in FIX_FIRST:
    if BASE[where].count(old) != 1:
        die("%s: its OLD does not occur exactly once in the staged %s line; the record has moved." % (tag, where))


def variants(where: str) -> dict:
    """Every accepted form of one staged line: the base with any subset of its FIX-FIRST pairs applied, each whole."""
    pairs = [p for p in FIX_FIRST if p[1] == where]
    out_v = {}
    for r in range(len(pairs) + 1):
        for sub in itertools.combinations(pairs, r):
            t = BASE[where]
            for _, _, old, new in sub:
                t = t.replace(old, new)
            out_v[t] = tuple(p[0] for p in sub)
    return out_v


applied = []
if iv20[0] != HEADING:
    die("block iv20's heading is not the staged heading with the brief's edit (and nothing else): %r" % iv20[0][:100])
if iv20[1] != "":
    die("block iv20's second line must be blank (the house shape: heading, blank line, bullets).")
for pos, where in ((2, "STATEMENT"), (3, "KILLS"), (4, "TEST"), (5, "SOURCE"), (6, "STATUS")):
    v = variants(where)
    if iv20[pos] not in v:
        die("block iv20 line %d (%s) is not the staged line with only the sanctioned edits and whole FIX-FIRST pairs; the block "
            "has drifted from results/beta-shapes-s35/ZOO-LINES-STAGED.md." % (pos + 1, where))
    applied += v[iv20[pos]]
v = variants("RIDER")
if B["iv10"] not in v:
    die("block iv10 is not staged line 16 (with only whole FIX-FIRST pairs FF2/FF5); the block has drifted.")
applied += v[B["iv10"]]

XREF = ("| β-shapes s35 (finite-rank / Weil-form targets for the F₁-square; End_β = {id} bases) | closed by theorem (Session 35; "
        "dual-model) | IV.20; IV.10; III.20; V.5 |")
if B["xref"] != XREF:
    die("block xref is not the brief's row in the table's shape '| cell | cell | cell |'.")

c = B["count"]
COUNT_HEAD = "**Entry count (dated, Session 36, 2026-09-30).** IV.20 ("
if not c.startswith(COUNT_HEAD):
    die("block count must begin %r." % COUNT_HEAD)
for need in ("makes **59 entries**", "I: 8, II: 5, III: 21, IV: 20, V: 5", "8 + 5 + 21 + 20 + 5 = 59", "Group IV 19 → 20",
             "699 → 711 lines", "SHA-256 at launch 8e66cdc0…", "`results/zoo-s36/`", "`results/beta-shapes-s35/NOTE.md`",
             "AGREES-WITH-CORRECTIONS", "move no count"):
    if need not in c:
        die("block count does not carry %r." % need)
for k in ("count", "iv10", "xref"):
    if B[k].lstrip().startswith("#"):
        die("block %s would add a heading." % k)
for ln in iv20[1:]:
    if ln.lstrip().startswith("#"):
        die("block iv20 carries a second heading line.")
for ln in [B["count"], B["iv10"], B["xref"]] + iv20:
    if ln and ln in zoo_text.split("\n"):
        die("an inserted line is already a line of the zoo: %r" % ln[:80])

# ---- Gate 4: anchors (each asserted unique; neighbors verified). ----
lines = zoo_text.split("\n")
orig = list(lines)
if lines[-1] != "" or (len(lines) > 1 and lines[-2] == ""):
    die("the input must end with exactly one newline.")
if len(orig) - 1 != LINES_BEFORE:
    die("the input has %d lines, expected %d." % (len(orig) - 1, LINES_BEFORE))

A_COUNT = ("**Entry count (dated, Session 34, 2026-09-29).** No entry is added. The six lines entered at this stream (three LINUX "
           "REPLAY lines")
P_COUNT = "**Entry count (dated, Session 33, 2026-09-29).**"
H_IV10 = "### IV.10 Tate-curve products carry no correspondence calculus — NEW, Session 6 (C3 adjudication)"
ST_IV10 = "- **STATUS.** program-adjudicated (computationally re-derived, Session 6). **BINDS: all per-prime-fiber substrate designs.**"
P_IV10 = ("- **[RIDER 2026-09-25, Session 27 (D2 design-axis scout pair; `results/d2-scout-s26/HARVEST.md` \"Proposed riders\" 2 "
          "and the adjudication paragraph;")
A_IV10 = ("- **[RIDER 2026-09-26, Session 28 (E3 Borger rung-1 step, `results/e3-borger-rung1/NOTE.md` §3–§4; writer Fable 5.1, "
          "Opus 5 reader `read-O.md` CLOSES after amendments; entered at the Session-29 zoo stream) — the HOST-DIMENSION check is a "
          "theorem on rung 1, and the host's pairing is exactly the explicit formula's prime side.]**")
N_IV10 = "### IV.11 Packet indiscreteness and the X₀^E quasi-compact kill"
H_IV19 = "### IV.19 The Kronecker sharpness of the pointwise prime-sum wall"
ST_IV19 = "- **STATUS.** **program-adjudicated (dual-model)**, `results/c2-m6/check-O.md` 2026-09-17"
A_IV19 = ("- **[PRECISION READ 2026-09-26, Session 28 (`results/program-digest-s27/ranking-read-O.md` §2 row 3; the record lines "
          "named here read at the line).]**")
G_V = "## GROUP V — PROCESS BARRIERS (how briefs die for non-mathematical reasons)"
T_XREF = "| Casualty | Verdict | Killing barriers |"
P_XREF = "| W1-26 lee-yang | instrument restored, coupling map unspecified (Session 24; pair 2) | III.15, IV.1 |"
A_XREF = ("| D2 design-axis scout (P1–P9) | NONE at the page — no doubled object for Spec Z with log p-weighted correspondences "
          "outside K1–K4 (Session 26; blind pair, RETURNED not refuted) | III.20, IV.10, V.5 |")
N_XREF = "**[READ 2026-09-10, Opus 5.]** The three Session-21 rows above were checked against their records"
for a in (A_COUNT, P_COUNT, H_IV10, ST_IV10, P_IV10, A_IV10, N_IV10, H_IV19, ST_IV19, A_IV19, G_V, T_XREF, P_XREF, A_XREF, N_XREF):
    n = sum(1 for ln in lines if ln.startswith(a))
    if n != 1:
        die("the anchor string is not unique in the zoo (%d hits): %r" % (n, a[:100]))
for a in (H_IV10, G_V, T_XREF, P_XREF, A_XREF):
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


# 1. The count paragraph: a blank line and the paragraph after the Session-34 paragraph, before the blank line and '---'.
i = idx(A_COUNT)
if any(ln.startswith("### ") or ln.startswith("## ") for ln in lines[:i]):
    die("the Session-34 count paragraph is not in the header.")
if not lines[i - 2].startswith(P_COUNT) or lines[i - 1] != "" or lines[i + 1] != "" or lines[i + 2] != "---":
    die("the Session-34 count paragraph is not between the Session-33 paragraph and the blank line + '---'.")
lines[i + 1:i + 1] = ["", B["count"]]

# 2. The IV.10 rider: directly after IV.10's last line (the Session-28 E3 RIDER), before the blank line and '### IV.11'.
i = idx(A_IV10)
if entry_of(i) != H_IV10:
    die("the E3 rider does not belong to IV.10.")
if not lines[i - 1].startswith(P_IV10) or not lines[i - 2].startswith(ST_IV10):
    die("IV.10's STATUS line and the 2026-09-25 rider are not the two lines above the E3 rider.")
if lines[i + 1] != "" or not lines[i + 2].startswith(N_IV10):
    die("the E3 rider is not IV.10's last line before the blank line and '### IV.11'.")
lines[i + 1:i + 1] = [B["iv10"]]

# 3. IV.20: a blank line and the entry directly after IV.19's last line (the PRECISION READ), before the blank line and '## GROUP V'.
i = idx(A_IV19)
if not entry_of(i).startswith(H_IV19):
    die("the PRECISION READ does not belong to IV.19.")
if not lines[i - 1].startswith(ST_IV19):
    die("IV.19's STATUS line is not directly above the PRECISION READ.")
if lines[i + 1] != "" or lines[i + 2] != G_V:
    die("IV.19's PRECISION READ is not the last line before the blank line and '## GROUP V'.")
iv_heads = [ln for ln in lines[:i + 2] if ln.startswith("### IV.")]
if not iv_heads or not iv_heads[-1].startswith(H_IV19):
    die("IV.19 is not the last Group-IV entry in file order.")
lines[i + 1:i + 1] = [""] + iv20

# 4. The cross-reference row: directly after the table's last row (D2), before the blank line and the READ note.
i = idx(A_XREF)
if lines[i - 1] != P_XREF or lines[i + 1] != "" or not lines[i + 2].startswith(N_XREF):
    die("the D2 row is not the table's last row between the W1-26 row and the blank line + READ note.")
t = i
while t >= 0 and lines[t].startswith("|"):
    t -= 1
if lines[t + 1] != T_XREF or lines[t + 2] != "|---|---|---|" or lines[t] != "" or not lines[t - 1].startswith("## Cross-reference: program casualties"):
    die("the D2 row is not in the cross-reference table under its column header.")
lines[i + 1:i + 1] = [XREF]

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
if len(heads) != 59 or tally != {"I": 8, "II": 5, "III": 21, "IV": 20, "V": 5}:
    die("heading tally %d %r, expected 59 {I 8, II 5, III 21, IV 20, V 5}." % (len(heads), tally))
for ln in heads:
    if not re.match(r"### (I|II|III|IV|V)\.(\d+) ", ln):
        die("heading is not a numbered entry: %r" % ln[:80])
recount = "I: %d, II: %d, III: %d, IV: %d, V: %d" % (tally["I"], tally["II"], tally["III"], tally["IV"], tally["V"])
if recount not in B["count"] or "**%d entries**" % len(heads) not in B["count"]:
    die("the count paragraph's figures are not the recount (%s; %d)." % (recount, len(heads)))
order = [int(re.match(r"### IV\.(\d+) ", ln).group(1)) for ln in heads if ln.startswith("### IV.")]
if order != list(range(1, 16)) + [18, 16, 17, 19, 20]:
    die("Group IV in file order is %r." % order)
for ln in [B["count"], B["iv10"], XREF] + [x for x in iv20 if x]:
    if lines.count(ln) != 1:
        die("an inserted line occurs %d times: %r" % (lines.count(ln), ln[:80]))
# Positions in the 711-line result (1-based): count 37 ('---' 39); rider 492 ('### IV.11' 494); IV.20 heading 592, bullets
# 594-598, '## GROUP V' 600; row 681 (blank 682); the file-discipline paragraph 711.
P = lambda n: lines[n - 1]
checks = (
    (P(35).startswith(A_COUNT) and P(36) == "" and P(37) == B["count"] and P(38) == "" and P(39) == "---", "count paragraph at 37"),
    (P(491).startswith(A_IV10) and P(492) == B["iv10"] and P(493) == "" and P(494).startswith(N_IV10), "IV.10 rider at 492"),
    (P(590).startswith(A_IV19) and P(591) == "" and P(592) == HEADING and P(593) == "" and [P(n) for n in range(594, 599)] == iv20[2:]
     and P(599) == "" and P(600) == G_V, "IV.20 at 592-598 before '## GROUP V' at 600"),
    (P(680) == A_XREF and P(681) == XREF and P(682) == "" and P(683).startswith(N_XREF), "cross-reference row at 681"),
    (P(711).startswith("*(File discipline"), "file-discipline paragraph at 711"),
)
for ok, what in checks:
    if not ok:
        die("position check failed: %s." % what)
last_iv = max(k for k, ln in enumerate(lines) if ln.startswith("### IV."))
if lines[last_iv] != HEADING or lines.index(G_V) != last_iv + 8:
    die("IV.20 is not the last Group-IV entry directly before '## GROUP V'.")
if sum(1 for ln in lines if "IV.20" in ln) != 3:
    die("'IV.20' must occur on exactly three lines (heading, count paragraph, row).")
inserted = "\n".join([B["count"], B["iv10"], XREF] + iv20).lower()
for bad in LINT:
    if bad in inserted:
        die("the inserted text carries the linted phrase %r." % bad)

out_bytes = new_text.encode("utf-8")
out.write_bytes(out_bytes)
if out.read_bytes() != out_bytes:
    die("the file written does not read back byte for byte: %s." % out)
print("OK: FIX-FIRST pairs applied: %s" % (", ".join(sorted(set(applied))) if applied else "none (the staged text with the two sanctioned edits)"))
print("OK: %s written; %d -> %d lines (+%d); entries 59 (I 8, II 5, III 21, IV 20, V 5); Group IV 19 -> 20; blocks at lines 37 (count), "
      "492 (IV.10 rider), 592-598 (IV.20), 681 (row); SHA-256 %s%s"
      % (out, len(orig) - 1, len(lines) - 1, added, hashlib.sha256(out_bytes).hexdigest(),
         "" if out == ZOO.resolve() else "  [BARRIER-ZOO.md untouched]"))
