#!/usr/bin/env python3
"""Session 25 zoo stream `zoo-s25` (2026-09-24): insert into BARRIER-ZOO.md the new entry I.8 (the
Siegel-zero world; C2 Session-24 queue item 2(c), dual-checked and re-checked), the Session-25 entry-count
line, ten dated riders (IV.18 x2, IV.9 x3, V.4, V.3, I.1 x2, III.1), two cross-reference rows and one dated
sub-bullet under formalization-queue item 11. Count 57 -> 58 (I 8, II 5, III 21, IV 19, V 5).

Source of every inserted line: results/zoo-s25/zoo-entries-proposed.md (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->). The four re-checked bullets of I.8 are asserted byte-identical to
results/c2-siegel/siegel-world-scout.md section 6 (lines 160-163) AND to results/c2-siegel/check-O.md item 5(d)
(lines 147-150). Pure insertion: no existing line is modified or removed. Every anchor is asserted to occur
exactly once. The script refuses to run twice. Afterwards it verifies that every original line survives, in
order, as an identical line, that the '### ' count is 58 with the right per-group counts, that the line
arithmetic is exact, and that the inserted text carries none of the four linted phrases.

Usage: python3 scripts/zoo-insert-s25.py [--dry-run OUTPATH]   (a dry run writes the result to OUTPATH and
leaves BARRIER-ZOO.md untouched). Modeled on scripts/zoo-insert-s22b.py and scripts/zoo-insert-s23.py.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s25" / "zoo-entries-proposed.md"
SCOUT = ROOT / "results" / "c2-siegel" / "siegel-world-scout.md"
CHECKO = ROOT / "results" / "c2-siegel" / "check-O.md"

dry = None
if len(sys.argv) == 3 and sys.argv[1] == "--dry-run":
    dry = Path(sys.argv[2])
elif len(sys.argv) != 1:
    sys.exit(__doc__)

zoo_text = ZOO.read_text(encoding="utf-8")
prop_text = PROPOSED.read_text(encoding="utf-8")
scout = SCOUT.read_text(encoding="utf-8").split("\n")
checko = CHECKO.read_text(encoding="utf-8").split("\n")

MARKS = ("\n### I.8 ", "**Entry count (dated, Session 25, 2026-09-24).**",
         "- **[RIDER 2026-09-24, Session 24, entered at the Session-25 zoo stream — (i) the pole cap")
for m in MARKS:
    if m in zoo_text:
        sys.exit("BARRIER-ZOO.md already contains %r — refusing to insert twice." % m[:60])


def block(name: str) -> str:
    m = re.search(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)),
                  prop_text, re.S)
    if not m:
        sys.exit("block %s not found in proposed file" % name)
    return m.group(1)


NAMES = ("count", "i8", "iv18", "iv9", "v4", "v3", "i1", "iii1", "xref", "fq11")
blocks = {k: block(k) for k in NAMES}
for k, v in blocks.items():
    if not v.strip():
        sys.exit("block %s is empty" % k)
    for bad in ("clearly", "obviously", "easy to see", "well known", "well-known"):
        if bad in v.lower():
            sys.exit("block %s contains the linted phrase %r" % (k, bad))
    if k != "i8" and any(ln.startswith("### ") for ln in v.split("\n")):
        sys.exit("block %s would add a '### ' heading" % k)

# The I.8 block: heading, blank, STATEMENT, KILLS, EXECUTABLE TEST, SOURCE, STATUS — the four re-checked
# bullets byte-identical to the scout's section 6 and to check-O item 5(d).
i8 = blocks["i8"].split("\n")
if len(i8) != 7 or not i8[0].startswith("### I.8 The Siegel-zero world (an S1-passing GRH-false world for positive-Λ first-order instruments)") or i8[1] != "":
    sys.exit("i8 block shape is wrong")
scout_bullets = scout[159:163]
if scout_bullets != checko[146:150]:
    sys.exit("scout section 6 bullets differ from check-O item 5(d) lines 147-150")
if [i8[2], i8[3], i8[4], i8[6]] != scout_bullets:
    sys.exit("the I.8 bullets in the proposed file are not byte-identical to the scout's section 6")
if not i8[5].startswith("- **SOURCE.** `results/c2-siegel/siegel-world-scout.md`"):
    sys.exit("the I.8 SOURCE line is missing")
for ln, tag in zip((i8[2], i8[3], i8[4], i8[6]), ("STATEMENT", "KILLS", "EXECUTABLE TEST", "STATUS")):
    if not ln.startswith("- **%s.**" % tag):
        sys.exit("I.8 bullet order wrong at %s" % tag)
if "`[novelty: dual-model check 2026-09-24]`" not in i8[6]:
    sys.exit("I.8 STATUS lacks the record's novelty label")
if blocks["count"].count("\n") != 0 or not blocks["count"].startswith(MARKS[1]):
    sys.exit("count block must be one line starting with the Session-25 count marker")
if blocks["xref"].count("\n") != 1 or not all(ln.startswith("| ") and ln.endswith(" |") for ln in blocks["xref"].split("\n")):
    sys.exit("xref block must be exactly two table rows")
if blocks["fq11"].count("\n") != 0 or not blocks["fq11"].startswith("    - **[NOTE 2026-09-24, Session 25 zoo stream"):
    sys.exit("fq11 block must be one indented sub-bullet")
for k, n in (("iv18", 2), ("iv9", 3), ("v4", 1), ("v3", 1), ("i1", 2), ("iii1", 1)):
    ls = blocks[k].split("\n")
    if len(ls) != n or not all(ln.startswith("- **[RIDER 2026-09-24, Session 24") for ln in ls):
        sys.exit("block %s must be %d rider line(s) with the dated header" % (k, n))


def unique_index(lines, pred, label: str) -> int:
    hits = [i for i, ln in enumerate(lines) if pred(ln)]
    if len(hits) != 1:
        sys.exit("anchor %r occurs %d times (need exactly 1)" % (label, len(hits)))
    return hits[0]


orig = zoo_text.split("\n")
lines = list(orig)

# 1. Entry-count line: after the Session-23 count paragraph, separated by a blank line.
i = unique_index(lines, lambda ln: ln.startswith("**Entry count (dated, Session 23, 2026-09-17).**"), "S23 count")
if lines[i + 1] != "" or lines[i + 2] != "---":
    sys.exit("the Session-23 count paragraph is not followed by a blank line and '---'")
lines[i + 1:i + 1] = ["", blocks["count"]]

# 2. I.8: after I.7's STATUS line (the last line of Group I), one blank line, the entry; the blank + '---' follow.
i = unique_index(lines, lambda ln: ln.startswith("- **STATUS.** literature-verified (corpus on disk). **CALIBRATION** (binds Track-C/de-novo axiom sets)."), "I.7 STATUS")
if lines[i + 1] != "" or lines[i + 2] != "---" or not lines[i + 4].startswith("## GROUP II "):
    sys.exit("I.7's STATUS line is not followed by blank, '---', blank, '## GROUP II'")
j = i
while j >= 0 and not lines[j].startswith("### "):
    j -= 1
if not lines[j].startswith("### I.7 "):
    sys.exit("the STATUS anchor does not belong to I.7")
lines[i + 1:i + 1] = [""] + i8

# 3. IV.18: after the entry's last line (the 2026-09-16 rider (ii)); blank, blank, '---' follow.
i = unique_index(lines, lambda ln: ln.startswith("- **[RIDER 2026-09-16, Session 22 — (ii) the budget-floor lemma κ, M1's honest object — OPEN"), "IV.18 rider (ii)")
if lines[i + 1] != "" or lines[i + 2] != "" or lines[i + 3] != "---":
    sys.exit("IV.18's rider (ii) is not followed by two blank lines and '---'")
lines[i + 1:i + 1] = blocks["iv18"].split("\n")

# 4. IV.9: after the entry's last line (the 2026-09-17 addendum rider), before '### IV.10'.
i = unique_index(lines, lambda ln: ln.startswith("- **[RIDER 2026-09-17, Session 23 — from the addendum to `results/c2-m2/separation-note.md` (A1–A3;"), "IV.9 addendum rider")
if lines[i + 1] != "" or not lines[i + 2].startswith("### IV.10 "):
    sys.exit("IV.9's addendum rider is not the last line before '### IV.10'")
lines[i + 1:i + 1] = blocks["iv9"].split("\n")

# 5. V.4: after its STATUS line, before '### V.5'.
i = unique_index(lines, lambda ln: ln.startswith("- **STATUS.** program rule, extracted from a Phase-4 FINDING — not from a kill:"), "V.4 STATUS")
if lines[i + 1] != "" or not lines[i + 2].startswith("### V.5 "):
    sys.exit("V.4's STATUS line is not the last line before '### V.5'")
lines[i + 1:i + 1] = [blocks["v4"]]

# 6. V.3: after its STATUS line, before '### V.4'.
i = unique_index(lines, lambda ln: ln.startswith("- **STATUS.** sponsor standing order + program protocol. **BINDS: all briefs and all critics.**"), "V.3 STATUS")
if lines[i + 1] != "" or not lines[i + 2].startswith("### V.4 "):
    sys.exit("V.3's STATUS line is not the last line before '### V.4'")
lines[i + 1:i + 1] = [blocks["v3"]]

# 7. I.1: after its STATUS line, before '### I.2'.
i = unique_index(lines, lambda ln: ln.startswith("- **STATUS.** computationally-verified (DH construction, witness values, off-line zero, CCM run"), "I.1 STATUS")
if lines[i + 1] != "" or not lines[i + 2].startswith("### I.2 "):
    sys.exit("I.1's STATUS line is not the last line before '### I.2'")
lines[i + 1:i + 1] = blocks["i1"].split("\n")

# 8. III.1: its STATUS line is shared by other entries, so anchor on '### III.2 ' and check the two lines above.
i = unique_index(lines, lambda ln: ln.startswith("### III.2 "), "III.2 heading")
if lines[i - 1] != "" or lines[i - 2] != "- **STATUS.** literature-verified. **BINDS: full-RH.**" \
        or lines[i - 3] != "- **SOURCE.** literature.md front 3; STATUS findings log 2026-08-11; corpus y-21/y-23.":
    sys.exit("the lines before '### III.2' are not III.1's SOURCE and STATUS lines")
lines[i - 1:i - 1] = [blocks["iii1"]]

# 9. Cross-reference rows: after the C2 M6 row (the table's last row).
i = unique_index(lines, lambda ln: ln.startswith('| C2 M6 "estimate route" — certify a first-order datum\'s sign at a chosen height'), "xref M6 row")
if lines[i + 1] != "" or not lines[i + 2].startswith("**[READ 2026-09-10, Opus 5.]**"):
    sys.exit("the C2 M6 row is not the table's last row")
lines[i + 1:i + 1] = blocks["xref"].split("\n")

# 10. Formalization-queue item 11: after the 'UNIT A LANDED' sub-bullet.
i = unique_index(lines, lambda ln: ln.startswith("    - **[UNIT A LANDED 2026-09-24, Session 24 — `results/c2-m4/BUILD-NOTES-A.md`"), "item 11 UNIT A line")
if lines[i + 1] != "" or not lines[i + 2].startswith("*(File discipline:"):
    sys.exit("the UNIT A line is not followed by the blank line and the file-discipline paragraph")
if not lines[i - 1].startswith("    - **[PRICED 2026-09-24, Session 24 — `results/c2-m4/PRICING-RESIDUE.md`"):
    sys.exit("the PRICED line is not directly above the UNIT A line")
lines[i + 1:i + 1] = [blocks["fq11"]]

new_text = "\n".join(lines)

# Verification.
it = iter(lines)
for ln in orig:
    for cand in it:
        if cand == ln:
            break
    else:
        sys.exit("original line lost or reordered: %r" % ln[:80])
heads = [ln for ln in lines if ln.startswith("### ")]
if len(heads) != 58:
    sys.exit("heading count is %d, expected 58" % len(heads))
groups = {"I": 0, "II": 0, "III": 0, "IV": 0, "V": 0}
for ln in heads:
    m = re.match(r"### (I|II|III|IV|V)\.(\d+)\b", ln)
    if not m:
        sys.exit("heading is not a numbered entry: %r" % ln[:80])
    groups[m.group(1)] += 1
if groups != {"I": 8, "II": 5, "III": 21, "IV": 19, "V": 5}:
    sys.exit("group counts %r" % groups)
if new_text.count("\n### I.8 ") != 1:
    sys.exit("I.8 heading count wrong")
if not new_text.endswith("\n") or new_text.endswith("\n\n"):
    sys.exit("file must end with exactly one newline")
added = len(lines) - len(orig)
expected = 2 + (1 + len(i8)) + 2 + 3 + 1 + 1 + 2 + 1 + 2 + 1
if added != expected:
    sys.exit("line arithmetic: added %d, expected %d" % (added, expected))

out = dry if dry else ZOO
out.write_text(new_text, encoding="utf-8")
print("OK: %s written; +%d lines; entries 58 (I 8, II 5, III 21, IV 19, V 5)%s" % (out, added, " [DRY RUN]" if dry else ""))
