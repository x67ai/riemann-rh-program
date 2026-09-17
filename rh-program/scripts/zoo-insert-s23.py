#!/usr/bin/env python3
"""Session 23 (2026-09-17): insert zoo entry IV.19 (the Kronecker sharpness of the pointwise prime-sum
wall; C2 mandatory repairs 4 and 6) into BARRIER-ZOO.md, plus the IV.9 stopper rider, the dated
entry-count line and one cross-reference row. Count 56 -> 57 (I 7, II 5, III 21, IV 19, V 5).

Sources: the IV.19 block is read from results/c2-m6/zoo-IV19-proposed.md (its '### IV.19' heading
through its last '- **' line); the rider, count and cross-reference blocks from
results/zoo-s23/zoo-entries-proposed.md (<!-- BLOCK:name --> ... <!-- END:name -->). Pure insertion:
no existing line is modified or removed; every anchor is asserted to occur exactly once; the script
refuses to run twice; afterwards every original line must survive in order, the '###' count must be
57, and the inserted text must carry none of the linted phrases.

Usage: python3 scripts/zoo-insert-s23.py [--dry-run OUTPATH]   (dry run writes the result to OUTPATH
and leaves BARRIER-ZOO.md untouched). Modeled on scripts/zoo-insert-s22b.py.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
DRAFT = ROOT / "results" / "c2-m6" / "zoo-IV19-proposed.md"
PROPOSED = ROOT / "results" / "zoo-s23" / "zoo-entries-proposed.md"

dry = None
if len(sys.argv) == 3 and sys.argv[1] == "--dry-run":
    dry = Path(sys.argv[2])
elif len(sys.argv) != 1:
    sys.exit(__doc__)

zoo_text = ZOO.read_text(encoding="utf-8")
draft_text = DRAFT.read_text(encoding="utf-8")
prop_text = PROPOSED.read_text(encoding="utf-8")

if "\n### IV.19 " in zoo_text:
    sys.exit("BARRIER-ZOO.md already contains '### IV.19' — refusing to insert twice.")
if "**[RIDER 2026-09-17, Session 23 — a STOPPER" in zoo_text:
    sys.exit("BARRIER-ZOO.md already contains the IV.9 stopper rider — refusing to insert twice.")


def block(name: str) -> str:
    m = re.search(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)),
                  prop_text, re.S)
    if not m:
        sys.exit("block %s not found in proposed file" % name)
    return m.group(1)


# The IV.19 entry: from its heading to its last '- **' line (the STATUS line), inclusive.
dl = draft_text.split("\n")
heads = [i for i, ln in enumerate(dl) if ln.startswith("### ")]
if len(heads) != 1 or not dl[heads[0]].startswith("### IV.19 "):
    sys.exit("the draft must carry exactly one '### ' heading and it must be IV.19")
h = heads[0]
last = max(i for i, ln in enumerate(dl) if ln.startswith("- **"))
if last <= h:
    sys.exit("no '- **' line after the IV.19 heading")
iv19 = "\n".join(dl[h:last + 1])
if not dl[last].startswith("- **STATUS.** **program-adjudicated (dual-model)**"):
    sys.exit("the draft's last entry line is not the program-adjudicated STATUS line: %r" % dl[last][:80])
if "pending" in dl[last].lower() and "pending the Opus re-check" in dl[last]:
    sys.exit("the STATUS line still says pending the re-check")
for ln in dl[h + 1:last + 1]:
    if ln.startswith("### "):
        sys.exit("a second heading inside the IV.19 block")

blocks = {"iv19": iv19, "iv9": block("iv9"), "count": block("count"), "xref": block("xref")}
for k, v in blocks.items():
    if not v.strip():
        sys.exit("block %s is empty" % k)
    for bad in ("clearly", "obviously", "easy to see", "well known", "well-known"):
        if bad in v.lower():
            sys.exit("block %s contains the linted phrase %r" % (k, bad))
for k in ("iv9", "count", "xref"):
    if any(ln.startswith("### ") for ln in blocks[k].split("\n")):
        sys.exit("block %s would add a '### ' heading" % k)
if not blocks["xref"].startswith("| ") or blocks["xref"].count("\n") != 0:
    sys.exit("xref block must be exactly one table row")


def unique_index(lines, pred, label):
    hits = [i for i, ln in enumerate(lines) if pred(ln)]
    if len(hits) != 1:
        sys.exit("anchor %r occurs %d times (need exactly 1)" % (label, len(hits)))
    return hits[0]


orig = zoo_text.split("\n")
lines = list(orig)

# 1. Entry-count line: after the Session-22 count paragraph, separated by a blank line.
i = unique_index(lines, lambda ln: ln.startswith("**Entry count (dated, Session 22, 2026-09-16).**"), "S22 count")
if lines[i + 1].strip() != "":
    sys.exit("no blank line after the Session-22 count paragraph")
lines[i + 1:i + 1] = ["", blocks["count"]]

# 2. IV.9 stopper rider: directly after the entry's last line (the 2026-09-16 Opus READ note).
i = unique_index(lines, lambda ln: ln.startswith(
    "- **[READ 2026-09-16, Opus 5: one attribution inside the rider above corrected; no number moves"), "IV.9 READ")
if not lines[i + 1].strip() == "" or not lines[i + 2].startswith("### IV.10 "):
    sys.exit("IV.9's READ note is not the last line before '### IV.10'")
lines[i + 1:i + 1] = [blocks["iv9"]]

# 3. IV.19: after IV.18's last line, before '## GROUP V', with one blank line each side.
g = unique_index(lines, lambda ln: ln.startswith("## GROUP V — PROCESS BARRIERS"), "GROUP V heading")
j = g - 1
while j >= 0 and lines[j].strip() == "":
    j -= 1
if not lines[j].startswith("- **[READ 2026-09-10, Opus 5: two scope repairs to the STATUS line above"):
    sys.exit("line before GROUP V is not IV.18's Opus READ note: %r" % lines[j][:80])
lines[j + 1:j + 1] = [""] + blocks["iv19"].split("\n")

# 4. Cross-reference row: after the C2 Sector-I row (the table's last row).
i = unique_index(lines, lambda ln: ln.startswith(
    '| C2 Sector I\'s original numerics deliverable "V > 1 outside the classical region" (C2 line 70) |'), "xref last row")
if lines[i + 1].strip() != "":
    sys.exit("the C2 Sector-I row is not the table's last row")
lines[i + 1:i + 1] = [blocks["xref"]]

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
if len(heads) != 57:
    sys.exit("heading count is %d, expected 57" % len(heads))
groups = {"I": 0, "II": 0, "III": 0, "IV": 0, "V": 0}
for ln in heads:
    m = re.match(r"### (I|II|III|IV|V)\.(\d+)\b", ln)
    if not m:
        sys.exit("heading is not a numbered entry: %r" % ln[:80])
    groups[m.group(1)] += 1
if groups != {"I": 7, "II": 5, "III": 21, "IV": 19, "V": 5}:
    sys.exit("group counts %r" % groups)
if new_text.count("\n### IV.19 ") != 1:
    sys.exit("IV.19 heading count wrong")
added = len(lines) - len(orig)
expected = 2 + 1 + 1 + blocks["iv19"].count("\n") + 1 + 1
if added != expected:
    sys.exit("line arithmetic: added %d, expected %d" % (added, expected))

out = dry if dry else ZOO
out.write_text(new_text, encoding="utf-8")
print("OK: %s written; +%d lines; entries 57 (I 7, II 5, III 21, IV 19, V 5)%s" % (out, added, " [DRY RUN]" if dry else ""))
