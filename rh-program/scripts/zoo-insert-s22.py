#!/usr/bin/env python3
"""Session 22 (2026-09-16): insert into BARRIER-ZOO.md the entry V.5 (the Grossmann-condition rule), the
dated rider on V.2, the dated rider + STATUS addendum on III.16, the dated sentence under §0 step 7, the
Session-22 entry-count paragraph, and the dated note under the cross-reference table.

Source of every inserted line: results/zoo-s22/zoo-entries-proposed.md (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->). Pure insertion: no existing line is modified or removed.
Every anchor is asserted to occur exactly once. The script refuses to run twice (checks that '### V.5'
is absent). Before inserting, it asserts that the two III.16 sentences the rider strikes as evidence
occur verbatim on the page (the brief's stop condition (a)); afterwards it verifies that every original
line survives, in order, as an identical line, that the entry count is 56 (I 7, II 5, III 21, IV 18,
V 5), and that the inserted text carries none of the four linted phrases.

Modeled on scripts/zoo-insert-s21.py.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s22" / "zoo-entries-proposed.md"

zoo_text = ZOO.read_text(encoding="utf-8")
prop_text = PROPOSED.read_text(encoding="utf-8")

if "### V.5" in zoo_text:
    sys.exit("BARRIER-ZOO.md already contains V.5 — refusing to insert twice.")

# Stop condition (a) of the brief: both III.16 sentences must be on the page verbatim.
S_STATEMENT = "arXiv contains literally zero papers coupling Lorentzian polynomials to RH (totalResults = 0 at sweep time)"
S_KILLS = "a multiplicative-Lorentzian bridge with prime-side coefficients — no candidate exists"
for s in (S_STATEMENT, S_KILLS):
    n = zoo_text.count(s)
    if n != 1:
        sys.exit("III.16 sentence occurs %d times (need exactly 1): %r" % (n, s))


def block(name: str) -> str:
    m = re.search(
        r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)),
        prop_text,
        re.S,
    )
    if not m:
        sys.exit("block %s not found in proposed file" % name)
    return m.group(1)


NAMES = ("count", "step7", "iii16", "v2", "v5", "xref")
blocks = {k: block(k) for k in NAMES}
for k, v in blocks.items():
    if not v.strip():
        sys.exit("block %s is empty" % k)
    for bad in ("clearly", "obviously", "easy to see", "well known"):
        if bad in v.lower():
            sys.exit("block %s contains the linted phrase %r" % (k, bad))


def unique_index(lines, pred, label: str) -> int:
    hits = [i for i, ln in enumerate(lines) if pred(ln)]
    if len(hits) != 1:
        sys.exit("anchor %r occurs %d times (need exactly 1)" % (label, len(hits)))
    return hits[0]


def before_heading(lines, heading_prefix: str, label: str) -> int:
    """Index of the first blank line of the blank run that precedes the heading (insertion point so
    that the inserted text sits directly after the previous entry's last line)."""
    i = unique_index(lines, lambda ln: ln.startswith(heading_prefix), label)
    j = i - 1
    while j >= 0 and lines[j].strip() == "":
        j -= 1
    if lines[j].strip() == "---":
        sys.exit("unexpected '---' directly before %s" % label)
    return j + 1


orig_zoo = zoo_text.split("\n")
lines = list(orig_zoo)

# 1. Entry count paragraph: after the Session-21 second-addition count line.
i = unique_index(lines, lambda ln: ln.startswith(
    "**Entry count (dated, Session 21, 14:32 IST 2026-09-10 — second addition).**"), "count line")
lines[i + 1:i + 1] = ["", blocks["count"]]

# 2. §0 step 7: one dated indented line directly after the step.
i = unique_index(lines, lambda ln: ln.startswith("7. **Process gates** (Group V)."), "step 7")
lines[i + 1:i + 1] = blocks["step7"].split("\n")

# 3. III.16: STATUS addendum + rider, directly after III.16's last line (before the blank run
#    preceding '### III.17'; the III.16 STATUS line itself is shared by six entries and is not an anchor).
k = before_heading(lines, "### III.17 ", "III.17 heading")
if not lines[k - 1].startswith("- **STATUS.** sweep-certified. **BINDS: full-RH.**"):
    sys.exit("line before the III.17 blank run is not III.16's STATUS line: %r" % lines[k - 1][:80])
lines[k:k] = blocks["iii16"].split("\n")

# 4. V.2 rider: after V.2's STATUS line.
i = unique_index(lines, lambda ln: ln == "- **STATUS.** sponsor standing order. **BINDS: all briefs.**", "V.2 STATUS")
lines[i + 1:i + 1] = blocks["v2"].split("\n")

# 5. V.5: after V.4's STATUS line (a blank line between).
i = unique_index(lines, lambda ln: ln.startswith("- **STATUS.** program rule, extracted from a Phase-4 FINDING"), "V.4 STATUS")
lines[i + 1:i + 1] = [""] + blocks["v5"].split("\n")

# 6. Note under the cross-reference table: after the Opus-read paragraph (a blank line between).
i = unique_index(lines, lambda ln: ln.startswith("**[READ 2026-09-10, Opus 5.]** The three Session-21 rows above"), "xref read paragraph")
lines[i + 1:i + 1] = ["", blocks["xref"]]

new_zoo = "\n".join(lines)


# ---------------------------------------------------------------- verification
def verify_survival(orig, new, label):
    it = iter(new)
    for o in orig:
        for ln in it:
            if ln == o:
                break
        else:
            sys.exit("%s: verification failed — original line lost or reordered: %r" % (label, o[:90]))


verify_survival(orig_zoo, lines, "BARRIER-ZOO.md")


def count(pattern, text):
    return len(re.findall(pattern, text, re.M))


n5_old, n5_new = count(r"^### V\.\d+ ", zoo_text), count(r"^### V\.\d+ ", new_zoo)
if n5_new != n5_old + 1:
    sys.exit("Group V count off: %d -> %d" % (n5_old, n5_new))
if count(r"^### V\.5 ", new_zoo) != 1:
    sys.exit("V.5 heading count != 1")
groups = {g: count(r"^### %s\.\d+ " % g, new_zoo) for g in ("I", "II", "III", "IV", "V")}
total = sum(groups.values())
if groups != {"I": 7, "II": 5, "III": 21, "IV": 18, "V": 5} or total != 56:
    sys.exit("expected 56 entries (7/5/21/18/5) after insertion, counted %d: %r" % (total, groups))
if count(r"^### ", new_zoo) != 56:
    sys.exit("a '### ' heading that is not a numbered entry appeared: %d" % count(r"^### ", new_zoo))
for k in NAMES:
    for ln in blocks[k].split("\n"):
        if ln not in lines:
            sys.exit("block %s: line not found in output: %r" % (k, ln[:80]))
if len(lines) != len(orig_zoo) + sum(len(blocks[k].split("\n")) for k in NAMES) + 3:
    sys.exit("line arithmetic off: %d -> %d" % (len(orig_zoo), len(lines)))

ZOO.write_text(new_zoo, encoding="utf-8")
print("BARRIER-ZOO.md: inserted count paragraph, §0 step-7 sentence, III.16 STATUS addendum + rider, "
      "V.2 rider, V.5, note under the cross-reference table")
print("entries: V %d -> %d; groups %r; total %d" % (n5_old, n5_new, groups, total))
print("BARRIER-ZOO.md lines (split on newline): %d -> %d" % (len(orig_zoo), len(lines)))
