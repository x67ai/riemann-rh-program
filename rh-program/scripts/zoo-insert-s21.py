#!/usr/bin/env python3
"""Session 21 (2026-09-10): insert into BARRIER-ZOO.md the entries IV.17 and V.4, the dated riders on
II.1, IV.3, IV.7, IV.11, IV.14 and IV.16, the Session-21 entry-count paragraph, three cross-reference
rows and formalization-queue item 10; and into results/corpus-routing.md a dated sub-bullet in caveat 22
and a new caveat 23.

Source of every inserted line: results/zoo-s21/zoo-entries-proposed.md (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->). Pure insertion: no existing line is modified or removed in
either file. Every anchor is asserted to occur exactly once. The script refuses to run twice (checks that
'### IV.17', '### V.4' and caveat 23 are absent) and verifies afterwards that every original line of both
files survives, in order, as an identical line.

Modeled on scripts/zoo-insert-s16.py.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
ROUTING = ROOT / "results" / "corpus-routing.md"
PROPOSED = ROOT / "results" / "zoo-s21" / "zoo-entries-proposed.md"

zoo_text = ZOO.read_text(encoding="utf-8")
routing_text = ROUTING.read_text(encoding="utf-8")
prop_text = PROPOSED.read_text(encoding="utf-8")

if "### IV.17" in zoo_text or "### V.4" in zoo_text:
    sys.exit("BARRIER-ZOO.md already contains IV.17 or V.4 — refusing to insert twice.")
if re.search(r"^23\. \*\*\[Added 2026-09-10, Session 21", routing_text, re.M):
    sys.exit("corpus-routing.md already contains caveat 23 — refusing to insert twice.")


def block(name: str) -> str:
    m = re.search(
        r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)),
        prop_text,
        re.S,
    )
    if not m:
        sys.exit("block %s not found in proposed file" % name)
    return m.group(1)


NAMES = ("count", "entries", "v4", "ii1", "iv3", "iv7", "iv11", "iv14", "iv16", "xref", "queue",
         "routing22", "routing23")
blocks = {k: block(k) for k in NAMES}
for k, v in blocks.items():
    if not v.strip():
        sys.exit("block %s is empty" % k)


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


# ---------------------------------------------------------------- BARRIER-ZOO.md
orig_zoo = zoo_text.split("\n")
lines = list(orig_zoo)

# 1. Entry count paragraph: after the Session-16/19 count line.
i = unique_index(lines, lambda ln: ln.startswith("**Entry count (dated, Session 16, 2026-09-06).**"), "count line")
lines[i + 1:i + 1] = ["", blocks["count"]]

# 2. II.1 pointer: directly after II.1's last block (before the blank run preceding '### II.2').
k = before_heading(lines, "### II.2 ", "II.2 heading")
lines[k:k] = blocks["ii1"].split("\n")

# 3. IV.3 rider: after IV.3's STATUS line.
i = unique_index(lines, lambda ln: ln == "- **STATUS.** program-adjudicated (computationally verified). **BINDS: all routes.**", "IV.3 STATUS")
lines[i + 1:i + 1] = blocks["iv3"].split("\n")

# 4. IV.7: the IV.17 pointer and rider B, after IV.7's last line (before the blank run preceding '### IV.8').
k = before_heading(lines, "### IV.8 ", "IV.8 heading")
lines[k:k] = blocks["iv7"].split("\n")

# 5. IV.11 riders: before the blank run preceding '### IV.12'.
k = before_heading(lines, "### IV.12 ", "IV.12 heading")
lines[k:k] = blocks["iv11"].split("\n")

# 6. IV.14 KILLS rider: before the blank run preceding '### IV.15'.
k = before_heading(lines, "### IV.15 ", "IV.15 heading")
lines[k:k] = blocks["iv14"].split("\n")

# 7. IV.16 riders: after IV.16's last line.
i = unique_index(lines, lambda ln: ln.startswith("- **[04:34 IST 2026-09-10 — rider R1 DROPPED"), "IV.16 last line")
lines[i + 1:i + 1] = blocks["iv16"].split("\n")

# 8. IV.17: after the IV.16 block, before '## GROUP V' (a blank line on each side).
i = unique_index(lines, lambda ln: ln.startswith("## GROUP V — PROCESS BARRIERS"), "GROUP V heading")
j = i - 1
while lines[j].strip() == "":
    j -= 1
lines[j + 1:j + 1] = [""] + blocks["entries"].split("\n")

# 9. V.4: after V.3's STATUS line.
i = unique_index(lines, lambda ln: ln.startswith("- **STATUS.** sponsor standing order + program protocol."), "V.3 STATUS")
lines[i + 1:i + 1] = [""] + blocks["v4"].split("\n")

# 10. Cross-reference rows: after the last row of the table.
i = unique_index(lines, lambda ln: ln.startswith("| Session-14 \"S4′ as four clauses\" statement"), "last xref row")
lines[i + 1:i + 1] = blocks["xref"].split("\n")

# 11. Formalization queue item 10: after item 9.
i = unique_index(lines, lambda ln: ln.startswith("9. Theorem A (A)+(B) (IV.14):"), "queue item 9")
lines[i + 1:i + 1] = blocks["queue"].split("\n")

new_zoo = "\n".join(lines)

# ---------------------------------------------------------------- corpus-routing.md
orig_rt = routing_text.split("\n")
rlines = list(orig_rt)
i = unique_index(rlines, lambda ln: ln.startswith("    - `r5-04` (CMH 73): printed = PDF + 305"), "caveat 22 last sub-bullet")
rlines[i + 1:i + 1] = blocks["routing22"].split("\n") + blocks["routing23"].split("\n")
new_rt = "\n".join(rlines)


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
verify_survival(orig_rt, rlines, "corpus-routing.md")

def count(pattern, text):
    return len(re.findall(pattern, text, re.M))

n4_old, n4_new = count(r"^### IV\.\d+ ", zoo_text), count(r"^### IV\.\d+ ", new_zoo)
n5_old, n5_new = count(r"^### V\.\d+ ", zoo_text), count(r"^### V\.\d+ ", new_zoo)
if n4_new != n4_old + 1 or n5_new != n5_old + 1:
    sys.exit("entry counts off: IV %d->%d, V %d->%d" % (n4_old, n4_new, n5_old, n5_new))
if count(r"^### IV\.17 ", new_zoo) != 1 or count(r"^### V\.4 ", new_zoo) != 1:
    sys.exit("IV.17 / V.4 heading count != 1")
groups = {g: count(r"^### %s\.\d+ " % g, new_zoo) for g in ("I", "II", "III", "IV", "V")}
total = sum(groups.values())
if total != 54:
    sys.exit("expected 54 entries after insertion, counted %d: %r" % (total, groups))
for k in NAMES:
    if blocks[k].split("\n")[0] not in (new_zoo if not k.startswith("routing") else new_rt):
        sys.exit("block %s not found in output" % k)

ZOO.write_text(new_zoo, encoding="utf-8")
ROUTING.write_text(new_rt, encoding="utf-8")
print("BARRIER-ZOO.md: inserted count paragraph, II.1 pointer, IV.3 rider, IV.7 pointer + rider B, IV.11 riders, "
      "IV.14 KILLS rider, IV.16 riders, IV.17, V.4, 3 xref rows, queue item 10")
print("entries: IV %d -> %d, V %d -> %d; groups %r; total %d" % (n4_old, n4_new, n5_old, n5_new, groups, total))
print("BARRIER-ZOO.md lines: %d -> %d" % (len(orig_zoo), len(lines)))
print("corpus-routing.md: caveat-22 addendum + caveat 23; lines: %d -> %d" % (len(orig_rt), len(rlines)))
