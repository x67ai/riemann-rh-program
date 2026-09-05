#!/usr/bin/env python3
"""Session 16 (2026-09-06): insert BARRIER-ZOO entries IV.11-IV.15, cross-reference rows,
the dated entry count, the protocol step-5 pointer, and formalization-queue items 8-9.

Source of every inserted line: results/c3-r/s16/zoo-entries-proposed.md (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->). Every anchor is asserted to occur exactly once;
no existing line is modified or removed except that the protocol step-5 line receives an
appended dated sentence (its original text is preserved as a prefix). The script refuses to
run twice (checks that '### IV.11' is absent) and verifies afterwards that every original
line survives in order.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "c3-r" / "s16" / "zoo-entries-proposed.md"

zoo_text = ZOO.read_text(encoding="utf-8")
prop_text = PROPOSED.read_text(encoding="utf-8")

if "### IV.11" in zoo_text:
    sys.exit("BARRIER-ZOO.md already contains IV.11 — refusing to insert twice.")


def block(name: str) -> str:
    m = re.search(
        r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)),
        prop_text,
        re.S,
    )
    if not m:
        sys.exit("block %s not found in proposed file" % name)
    return m.group(1)


blocks = {k: block(k) for k in ("count", "protocol", "entries", "xref", "queue")}

orig_lines = zoo_text.split("\n")
lines = list(orig_lines)


def unique_index(pred, label: str) -> int:
    hits = [i for i, ln in enumerate(lines) if pred(ln)]
    if len(hits) != 1:
        sys.exit("anchor %r occurs %d times (need exactly 1)" % (label, len(hits)))
    return hits[0]


# 1. Entry count: after the header's Scope-vocabulary paragraph (one line).
i = unique_index(lambda ln: ln.startswith("**Scope vocabulary**"), "scope vocabulary")
lines[i + 1 : i + 1] = ["", blocks["count"]]

# 2. Protocol step 5: append the dated pointer to the line ending "the ghost audit (IV.2)."
i = unique_index(lambda ln: ln.endswith("the ghost audit (IV.2)."), "protocol step 5")
lines[i] = lines[i] + blocks["protocol"]

# 3. Entries: before the '---' that precedes '## GROUP V'.
i = unique_index(lambda ln: ln.startswith("## GROUP V — PROCESS BARRIERS"), "GROUP V heading")
j = i - 1
while lines[j].strip() == "":
    j -= 1
if lines[j].strip() != "---":
    sys.exit("expected '---' before GROUP V, found %r" % lines[j])
lines[j:j] = blocks["entries"].split("\n") + [""]

# 4. Cross-reference rows: after the C3 row (last row of the table).
i = unique_index(lambda ln: ln.startswith("| C3 geometric-substrate (as commissioned) |"), "C3 xref row")
lines[i + 1 : i + 1] = blocks["xref"].split("\n")

# 5. Formalization queue: after item 7.
i = unique_index(lambda ln: ln.startswith("7. Converse-theorem-form DH-exclusion via Blomer–Leung"), "queue item 7")
lines[i + 1 : i + 1] = blocks["queue"].split("\n")

new_text = "\n".join(lines)

# Verification: every original line survives, in order (the step-5 line as a prefix).
it = iter(lines)
for o in orig_lines:
    for ln in it:
        if ln == o or (o.endswith("the ghost audit (IV.2).") and ln.startswith(o)):
            break
    else:
        sys.exit("verification failed: original line lost: %r" % o[:80])

n_old = len(re.findall(r"^### IV\.\d+ ", zoo_text, re.M))
n_new = len(re.findall(r"^### IV\.\d+ ", new_text, re.M))
if n_new != n_old + 5:
    sys.exit("expected %d IV entries, found %d" % (n_old + 5, n_new))
for k in range(11, 16):
    if len(re.findall(r"^### IV\.%d " % k, new_text, re.M)) != 1:
        sys.exit("IV.%d heading count != 1" % k)

ZOO.write_text(new_text, encoding="utf-8")
print("inserted: count line, protocol pointer, IV.11-IV.15 (%d -> %d Group-IV entries), 4 xref rows, queue items 8-9"
      % (n_old, n_new))
print("lines: %d -> %d" % (len(orig_lines), len(lines)))
