#!/usr/bin/env python3
"""Session 22, second zoo stream `zoo-s22b` (2026-09-16): insert into BARRIER-ZOO.md the dated riders on
II.4, IV.9, IV.18 (two), III.16, III.6, III.15 and III.20, and into results/corpus-routing.md the
Caveat 25 paragraph. NO new numbered entry: the count stays 56 (I 7, II 5, III 21, IV 18, V 5).

Source of every inserted line: results/zoo-s22b/zoo-entries-proposed.md (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->). Pure insertion: no existing line is modified or removed.
Every anchor is asserted to occur exactly once. The script refuses to run twice (checks that the II.4
rider and Caveat 25 are absent). Afterwards it verifies that every original line of BOTH files survives,
in order, as an identical line, that the entry count is still 56, that every '### ' heading is a
numbered entry, that the line arithmetic is exact, and that the inserted text carries none of the four
linted phrases.

Modeled on scripts/zoo-insert-s22.py.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
ROUTING = ROOT / "results" / "corpus-routing.md"
PROPOSED = ROOT / "results" / "zoo-s22b" / "zoo-entries-proposed.md"

zoo_text = ZOO.read_text(encoding="utf-8")
routing_text = ROUTING.read_text(encoding="utf-8")
prop_text = PROPOSED.read_text(encoding="utf-8")

MARK_ZOO = "**[RIDER 2026-09-16, Session 22 — from Theorem M2 clause 7"
MARK_ROUTING = "**Caveat 25 ("
if MARK_ZOO in zoo_text:
    sys.exit("BARRIER-ZOO.md already contains the II.4 M2 rider — refusing to insert twice.")
if MARK_ROUTING in routing_text:
    sys.exit("results/corpus-routing.md already contains Caveat 25 — refusing to insert twice.")


def block(name: str) -> str:
    m = re.search(
        r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)),
        prop_text,
        re.S,
    )
    if not m:
        sys.exit("block %s not found in proposed file" % name)
    return m.group(1)


ZOO_NAMES = ("ii4", "iv9", "iv18", "iii16", "iii6", "iii15", "iii20")
NAMES = ZOO_NAMES + ("caveat25",)
blocks = {k: block(k) for k in NAMES}
for k, v in blocks.items():
    if not v.strip():
        sys.exit("block %s is empty" % k)
    for bad in ("clearly", "obviously", "easy to see", "well known", "well-known"):
        if bad in v.lower():
            sys.exit("block %s contains the linted phrase %r" % (k, bad))
for k in ZOO_NAMES:
    for ln in blocks[k].split("\n"):
        if ln.startswith("### "):
            sys.exit("block %s would add a '### ' heading — riders only" % k)
if MARK_ZOO not in blocks["ii4"]:
    sys.exit("the ii4 block does not carry the run-twice marker")
if not blocks["caveat25"].startswith(MARK_ROUTING):
    sys.exit("the caveat25 block does not start with the run-twice marker")


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

# 1. II.4: after the entry's last line (its Session-16 DUAL-MODEL CHECK note, whose opening is shared
#    with a II.1 line, so the anchor is the unique '### II.5 ' heading); one blank line, then the rider,
#    matching the entry's own blank-separated dated notes.
k = before_heading(lines, "### II.5 ", "II.5 heading")
prev = lines[k - 1]
if not (prev.startswith("- **[DUAL-MODEL CHECK 2026-09-05, Session 16 — Opus 5 re-derivation")
        and "Verdict CONFIRMED-WITH-CORRECTIONS" in prev
        and "All three Session-15 values confirmed to the digits quoted." in prev):
    sys.exit("line before the II.5 blank run is not II.4's dual-check note: %r" % prev[:80])
lines[k:k] = [""] + blocks["ii4"].split("\n")

# 2. IV.9: directly after its STATUS line.
i = unique_index(lines, lambda ln: ln.startswith(
    "- **STATUS.** program-adjudicated components; the synthesis is a program rule (this file). **BINDS: all routes.**"),
    "IV.9 STATUS")
lines[i + 1:i + 1] = blocks["iv9"].split("\n")

# 3. IV.18: directly after its STATUS line (the entry ends there; blank lines and '---' follow).
i = unique_index(lines, lambda ln: ln.startswith(
    "- **STATUS.** **program-adjudicated (dual-model)** — Opus 5 check `results/c2-r1/check-O.md`"),
    "IV.18 STATUS")
if "Does NOT bind: Sector II signed separations (M2)" not in lines[i]:
    sys.exit("IV.18 STATUS line does not carry the 'Does NOT bind' clause the riders answer")
lines[i + 1:i + 1] = blocks["iv18"].split("\n")

# 4. III.16: after the Opus scope note of 2026-09-16 (the entry's last line), before '### III.17'.
k = before_heading(lines, "### III.17 ", "III.17 heading")
if not lines[k - 1].startswith("- **[READ 2026-09-16, Opus 5: the scope of the SUSPENSION, recorded not amended.]**"):
    sys.exit("line before the III.17 blank run is not III.16's Opus scope note: %r" % lines[k - 1][:80])
lines[k:k] = blocks["iii16"].split("\n")

# 5. III.6: directly after its STATUS line.
i = unique_index(lines, lambda ln: ln.startswith(
    "- **STATUS.** literature-verified. **BINDS: all routes touching the dBN flow; the disproof channel is B2/D1 property.**"),
    "III.6 STATUS")
lines[i + 1:i + 1] = blocks["iii6"].split("\n")

# 6. III.15: after its STATUS line (shared by six entries, so the anchor is '### III.16 '), with the
#    SOURCE line above it checked.
k = before_heading(lines, "### III.16 ", "III.16 heading")
if lines[k - 1] != "- **STATUS.** sweep-certified. **BINDS: full-RH.**":
    sys.exit("line before the III.16 blank run is not III.15's STATUS line: %r" % lines[k - 1][:80])
if not lines[k - 2].startswith("- **SOURCE.** grossmann-sweep.json (reflection-positivity-qft dead-end 0.70; lee-yang-stat-mech instrument 0.72)"):
    sys.exit("line two above the III.16 blank run is not III.15's SOURCE line: %r" % lines[k - 2][:80])
lines[k:k] = blocks["iii15"].split("\n")

# 7. III.20: directly after its STATUS line.
i = unique_index(lines, lambda ln: ln.startswith(
    "- **STATUS.** sweep-certified. **BINDS: Track-C/de-novo designs (spec-level).**"),
    "III.20 STATUS")
lines[i + 1:i + 1] = blocks["iii20"].split("\n")

new_zoo = "\n".join(lines)

# 8. corpus-routing.md: Caveat 25 after Caveat 24 (the last line of the file), one blank line between.
orig_routing = routing_text.split("\n")
rlines = list(orig_routing)
i = unique_index(rlines, lambda ln: ln.startswith("**Caveat 24 (13:44 IST 2026-09-10, Session 21"), "Caveat 24")
rlines[i + 1:i + 1] = [""] + blocks["caveat25"].split("\n")
new_routing = "\n".join(rlines)


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
verify_survival(orig_routing, rlines, "results/corpus-routing.md")


def count(pattern, text):
    return len(re.findall(pattern, text, re.M))


groups_old = {g: count(r"^### %s\.\d+ " % g, zoo_text) for g in ("I", "II", "III", "IV", "V")}
groups = {g: count(r"^### %s\.\d+ " % g, new_zoo) for g in ("I", "II", "III", "IV", "V")}
total = sum(groups.values())
if groups != groups_old:
    sys.exit("group counts changed: %r -> %r" % (groups_old, groups))
if groups != {"I": 7, "II": 5, "III": 21, "IV": 18, "V": 5} or total != 56:
    sys.exit("expected 56 entries (7/5/21/18/5), counted %d: %r" % (total, groups))
if count(r"^### ", new_zoo) != 56 or count(r"^### ", zoo_text) != 56:
    sys.exit("'### ' heading count is not 56 before and after: %d -> %d"
             % (count(r"^### ", zoo_text), count(r"^### ", new_zoo)))
for k in ZOO_NAMES:
    for ln in blocks[k].split("\n"):
        if ln not in lines:
            sys.exit("block %s: line not found in output: %r" % (k, ln[:80]))
for ln in blocks["caveat25"].split("\n"):
    if ln not in rlines:
        sys.exit("block caveat25: line not found in output: %r" % ln[:80])
added_zoo = sum(len(blocks[k].split("\n")) for k in ZOO_NAMES) + 1  # + the blank line before the II.4 rider
if len(lines) != len(orig_zoo) + added_zoo:
    sys.exit("BARRIER-ZOO.md line arithmetic off: %d -> %d (expected +%d)" % (len(orig_zoo), len(lines), added_zoo))
added_routing = len(blocks["caveat25"].split("\n")) + 1
if len(rlines) != len(orig_routing) + added_routing:
    sys.exit("corpus-routing.md line arithmetic off: %d -> %d (expected +%d)"
             % (len(orig_routing), len(rlines), added_routing))
if new_zoo.count(MARK_ZOO) != 1 or new_routing.count(MARK_ROUTING) != 1:
    sys.exit("run-twice markers not exactly once after insertion")

ZOO.write_text(new_zoo, encoding="utf-8")
ROUTING.write_text(new_routing, encoding="utf-8")
print("BARRIER-ZOO.md: inserted riders on II.4, IV.9, IV.18 (i)+(ii), III.16, III.6, III.15, III.20 — no new entry")
print("entries: groups %r; total %d (unchanged)" % (groups, total))
print("BARRIER-ZOO.md lines (split on newline): %d -> %d" % (len(orig_zoo), len(lines)))
print("results/corpus-routing.md: inserted Caveat 25; lines %d -> %d" % (len(orig_routing), len(rlines)))
