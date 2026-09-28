#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 31 zoo stream `zoo-s31` (2026-09-29): insert into BARRIER-ZOO.md five lines, bookkeeping only -- the count
paragraph (block count: a blank line and the paragraph directly after the Session-30 count paragraph, before the '---'), the
III.20 dated note beneath the LOOKUP line (block iii20note: the lookup line's "1 undecided from disk" decided -- P9l no at the
page; the SPEC table 20/0/20/0), the IV.1 STATUS rider (block iv1: formalized-in-Lean, D5's label VERBATIM from
results/d5-lean-s30/BUILD-NOTES.md lines 16-17), the IV.17 rider (block iv17: EXECUTABLE TEST (3)'s consumed line is the named
theorem per_atom_slack; TEST (1)'s mark-4/3 law is the instance fracMark), and the formalization-queue item-10 flip (block fq10:
an INDENTED sub-bullet -- exactly four spaces, then "- **[" -- directly after item 10 and before item 11, item 11's four
sub-bullets the house precedent; IV.17's label VERBATIM from results/iv17-lean-s30/BUILD-NOTES.md lines 15-17). No numbered
entry: the entry count stays 58 (I 8, II 5, III 21, IV 19, V 5); 672 -> 678 lines (+6: four one-line riders/notes, the count
paragraph and the blank line before it).

Source of every inserted line: results/zoo-s31/zoo-entries-proposed.md, read AT RUN TIME (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->), so the orchestrator's post-reader amendments flow in. Before touching the zoo the
script asserts that BARRIER-ZOO.md has SHA-256 46b3b38f... (the zoo at brief time) and that the two BUILD-NOTES files have
335337f3... and a3c3bd69...; that every anchor occurs exactly once (anchored by the full text of the neighboring lines, never
by line number alone: the Session-30 count paragraph's head up to "(the IV.18 rider (ii′)", the LOOKUP line's head up to
"EXECUTABLE TEST (s29 digest", the Session-27 pointer rider's FULL head through "-- pointer.]**" (the shorter head also opens
III.20's Session-27 rider, so the full head is the anchor and is asserted unique), the READ line's head through "CONFIRMED at
every record it cites.]**", item 10's head "10. The fractional-mark integrality theorem (IV.17)"); that the line directly after
each anchor is what the brief says (blank after the count paragraph, the LOOKUP line, the pointer rider and the READ line;
"11. **Theorem M2's Lemma G" after item 10) and the line after that as well ('---'; '### III.21'; '### IV.2'; '### IV.19';
item 11's first sub-bullet), so the placement is verified, not assumed; and that the two labels quoted inside blocks iv1 and
fq10 equal, character for character, the strings pulled from the two BUILD-NOTES files at run time (the wrapped lines joined
with single spaces; both strings printed on mismatch, and the script refuses). Pure insertion: no existing line is modified or
removed (item 10's own line is untouched -- the flip is the sub-bullet beneath it). The script refuses to run twice. Afterwards
it verifies that every original line survives, in order, as an identical line, that the '### ' count is 58 with per-group counts
8/5/21/19/5, that the numbered formalization-queue list still reads 1-11 in order with the new sub-bullet indented exactly four
spaces between items 10 and 11, that the line arithmetic is exact (+6, 672 -> 678), that the file ends with exactly one
newline, and that the inserted text carries none of the linted phrases (10(g)).

Usage: python3 scripts/zoo-insert-s31.py [--dry-run OUTPATH]
  --dry-run OUTPATH    write the result to OUTPATH and leave BARRIER-ZOO.md untouched (the writer's only mode).
Modeled on scripts/zoo-insert-s30.py.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s31" / "zoo-entries-proposed.md"
BN_D5 = ROOT / "results" / "d5-lean-s30" / "BUILD-NOTES.md"
BN_IV17 = ROOT / "results" / "iv17-lean-s30" / "BUILD-NOTES.md"
ZOO_HASH_BEFORE = "46b3b38fbe49fc78b6466b386eeed1b6bb949c57539acf335b8768eaf6ef9a9c"
BN_D5_HASH = "335337f38b26700eaaf00b6513538dcd350329e87f7679d2f440728435c12e5d"
BN_IV17_HASH = "a3c3bd698b92f4deed1d73b39759739034ced9b906d884776efa77da613bb728"

args = sys.argv[1:]
dry = None
if len(args) == 2 and args[0] == "--dry-run":
    dry = Path(args[1])
elif args:
    sys.exit(__doc__)

zoo_bytes = ZOO.read_bytes()
zoo_hash = hashlib.sha256(zoo_bytes).hexdigest()
if zoo_hash != ZOO_HASH_BEFORE:
    sys.exit("BARRIER-ZOO.md SHA-256 is %s, expected %s -- something changed the zoo; the orchestrator re-anchors. Nothing done."
             % (zoo_hash, ZOO_HASH_BEFORE))
zoo_text = zoo_bytes.decode("utf-8")
prop_text = PROPOSED.read_text(encoding="utf-8")
for p, h in ((BN_D5, BN_D5_HASH), (BN_IV17, BN_IV17_HASH)):
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    if got != h:
        sys.exit("%s SHA-256 is %s, expected %s -- the label's record changed; nothing done." % (p.relative_to(ROOT), got, h))

MARKS = ("**Entry count (dated, Session 31, 2026-09-29).**",
         "- **[NOTE 2026-09-29, Session 30 (G2, the Kapranov–Smirnov close, `results/g2-ks-close-s30/`; entered at the Session-31 zoo stream)",
         "- **[STATUS RIDER 2026-09-29, Session 30 (D5, `results/d5-lean-s30/`; entered at the Session-31 zoo stream) — formalized-in-Lean.]**",
         "- **[RIDER 2026-09-29, Session 30 (IV.17 in Lean, `results/iv17-lean-s30/`; entered at the Session-31 zoo stream)",
         "    - **[FORMALIZED AND SHIPPED 2026-09-29, Session 30 — Comparator topic `IntegralityGap` (`results/iv17-lean-s30/`; entered at the Session-31 zoo stream).]**")
for m in MARKS:
    if m in zoo_text:
        sys.exit("BARRIER-ZOO.md already contains %r -- refusing to insert twice." % m[:70])


def block(text: str, name: str, where: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)), text, re.S)
    if len(ms) != 1:
        sys.exit("block %s occurs %d times in %s (need exactly 1)" % (name, len(ms), where))
    return ms[0]


NAMES = ("count", "iii20note", "iv1", "iv17", "fq10")
blocks = {k: block(prop_text, k, "the proposed file") for k in NAMES}
for k, v in blocks.items():
    if not v.strip():
        sys.exit("block %s is empty" % k)
    if v.count("\n") != 0:
        sys.exit("block %s must be exactly one line" % k)
    for bad in ("clearly", "obviously", "easy to see", "well known", "well-known"):
        if bad in v.lower():
            sys.exit("block %s contains the linted phrase %r" % (k, bad))
    if v.startswith("### ") or v.startswith("## ") or v.lstrip().startswith("### ") or v.lstrip().startswith("## "):
        sys.exit("block %s would add a heading" % k)
    if v in zoo_text:
        sys.exit("block %s is already in the zoo" % k)

# Shapes of the heads.
for k, head in zip(NAMES, MARKS):
    if not blocks[k].startswith(head):
        sys.exit("block %s must start with %r" % (k, head[:60]))
    if k != "count" and "]**" not in blocks[k]:
        sys.exit("block %s has no house head closing ']**'" % k)
for k in ("iii20note", "iv1", "iv17"):
    if not blocks[k].startswith("- **["):
        sys.exit("block %s must be a top-level bullet '- **['" % k)
if not blocks["fq10"].startswith("    - **[") or blocks["fq10"].startswith("     "):
    sys.exit("block fq10 must begin with exactly four spaces then '- **[' (item 11's sub-bullets are the precedent)")
if "\t" in blocks["fq10"][:8]:
    sys.exit("block fq10 must be indented with spaces, not a tab")

# --- The two labels: pulled from the two BUILD-NOTES files at run time (wrapped lines joined with single spaces) and
#     compared character for character with the quoted strings in blocks iv1 and fq10 (standing order 7). ---


def pull_label(path: Path, lo: int, hi: int) -> str:
    seg = " ".join(ln.strip() for ln in path.read_text(encoding="utf-8").split("\n")[lo - 1:hi])
    ms = re.findall(r'\*\*"(.*?)"\*\*', seg)
    if len(ms) != 1:
        sys.exit("%s lines %d-%d do not carry exactly one bold quoted label (found %d); the record has moved" % (path.name, lo, hi, len(ms)))
    return ms[0]


LABEL_D5 = pull_label(BN_D5, 16, 17)
LABEL_IV17 = pull_label(BN_IV17, 15, 17)
INTRO = 'Label, as the builder and the checker assign it: "'
for k, lab, src in (("iv1", LABEL_D5, "results/d5-lean-s30/BUILD-NOTES.md lines 16-17"),
                    ("fq10", LABEL_IV17, "results/iv17-lean-s30/BUILD-NOTES.md lines 15-17")):
    b = blocks[k]
    if b.count(INTRO) != 1:
        sys.exit("block %s does not carry the label introduction %r exactly once" % (k, INTRO))
    quoted = b.split(INTRO, 1)[1]
    end = quoted.find('"')
    if end < 0:
        sys.exit("block %s: the label's closing straight quote is missing" % k)
    quoted = quoted[:end]
    if quoted != lab:
        sys.exit("block %s: the quoted label differs from the record (%s).\n  RECORD: %r\n  BLOCK:  %r\nRefusing." % (k, src, lab, quoted))
    if b.count('"' + lab + '"') != 1:
        sys.exit("block %s must carry the label in straight double quotes exactly once" % k)
print("OK: the two labels in blocks iv1 and fq10 equal the strings pulled from the two BUILD-NOTES files, character for character:\n   D5:    %s\n   IV.17: %s" % (LABEL_D5, LABEL_IV17))

# Forbidden sentences (BUILD-NOTES, both units): "IV.17 is formalized" appears only negated inside fq10; the other nowhere.
for k in NAMES:
    if "the tilted explicit formula is formalized" in blocks[k]:
        sys.exit("block %s carries the forbidden sentence 'the tilted explicit formula is formalized'" % k)
    n = blocks[k].count("IV.17 is formalized")
    if n and not (k == "fq10" and n == 1 and blocks[k].count('Never "IV.17 is formalized"') == 1):
        sys.exit("block %s carries 'IV.17 is formalized' other than the single negated mention the brief orders in fq10" % k)
    if "kernel-checked on Prove2Me" in blocks[k]:
        sys.exit("block %s carries the forbidden phrase 'kernel-checked on Prove2Me'" % k)

# Content sentinels per block (the brief's "What enters").
if "58 entries" not in blocks["count"] or "8 + 5 + 21 + 19 + 5 = 58" not in blocks["count"] or "672 → 678" not in blocks["count"] or "46b3b38f" not in blocks["count"]:
    sys.exit("count block does not carry the 58 arithmetic, the 672 → 678 line count and the launch hash")
if "20 rows: 0 yes, 20 no with grounds at the page, 0 undecided" not in blocks["iii20note"] or "not a target of the pair" not in blocks["iii20note"] or "19 no" in blocks["iii20note"]:
    sys.exit("block iii20note does not carry the decided tally 20/0/20/0")
if "374c9e00c1df219324bb1f7d6a8a543ef175a4307bd13198b44d6ac2c1ddb32e" not in blocks["iv1"] or "BINDS: all routes" not in blocks["iv1"] or "(N6)" not in blocks["iv1"]:
    sys.exit("block iv1 does not carry the D5 CHECK-O hash, the untouched-STATUS sentence and the six not-covered items")
if "`per_atom_slack`" not in blocks["iv17"] or "`checker_mi_of_slack`" not in blocks["iv17"] or "`fracMark`" not in blocks["iv17"] or "`mi_fails_rational`" not in blocks["iv17"]:
    sys.exit("block iv17 does not name per_atom_slack, checker_mi_of_slack, fracMark and mi_fails_rational")
if "c2e8c64ed4680edc33c0ab838a07609a9999b87d3215ff00ef05cfba413d49a3" not in blocks["fq10"] or "UNFORMALIZED" not in blocks["fq10"] or "`IntegralityGap`" not in blocks["fq10"]:
    sys.exit("block fq10 does not carry the IV.17 CHECK-O hash, the pair-channel UNFORMALIZED sentence and the topic name")


def unique_index(lines, pred, label: str) -> int:
    hits = [i for i, ln in enumerate(lines) if pred(ln)]
    if len(hits) != 1:
        sys.exit("anchor %r occurs %d times (need exactly 1)" % (label, len(hits)))
    return hits[0]


def entry_of(lines, i: int, heading: str) -> None:
    j = i
    while j >= 0 and not lines[j].startswith("### ") and not lines[j].startswith("## "):
        j -= 1
    if j < 0 or not lines[j].startswith(heading):
        sys.exit("the anchor at line %d does not belong to %s" % (i + 1, heading.strip()))


orig = zoo_text.split("\n")
lines = list(orig)

# The anchors, by the full text of the neighboring lines (each asserted unique in the file).
ANCHOR_COUNT = "**Entry count (dated, Session 30, 2026-09-28).** No entry is added. The four lines entered at this stream (the IV.18 rider (ii′)"
PREV_COUNT = "**Entry count (dated, Session 29, 2026-09-28).**"
ANCHOR_III20 = "- **[LOOKUP 2026-09-28, Session 30 — the brief-time lookup for item 1 of this entry's EXECUTABLE TEST (s29 digest"
PREV_III20 = "- **[RIDER 2026-09-26, Session 28 (E3, `results/e3-borger-rung1/NOTE.md` §3–§5; entered at the Session-29 zoo stream) — (B) and R-a's sentence are theorems on rung 1.]**"
ANCHOR_IV1 = "- **[RIDER 2026-09-25, Session 27 (D2 design-axis scout pair; `results/d2-scout-s26/HARVEST.md` \"Proposed riders\" 1) — pointer.]**"
SHORT_IV1 = "- **[RIDER 2026-09-25, Session 27 (D2 design-axis scout pair; `results/d2-scout-s26/HARVEST.md` \"Proposed riders\" 1"
PREV_IV1 = "- **STATUS.** program-adjudicated (computationally verified in C1). **BINDS: all routes.**"
ANCHOR_IV17 = "- **[READ 2026-09-10, Opus 5: two scope repairs to the STATUS line above; the entry's mathematics is CONFIRMED at every record it cites.]**"
PREV_IV17_HEAD = "- **STATUS.** program-adjudicated — two blind referees on the paper (zero fatals)"
ANCHOR_FQ10 = "10. The fractional-mark integrality theorem (IV.17)"
NEXT_FQ10 = "11. **Theorem M2's Lemma G"
NEXT2_FQ10 = "    - **[PRICED 2026-09-24, Session 24"
PREV_FQ10 = "9. Theorem A (A)+(B) (IV.14)"
for a in (ANCHOR_COUNT, ANCHOR_III20, ANCHOR_IV1, ANCHOR_IV17, ANCHOR_FQ10, NEXT_FQ10):
    n = sum(1 for ln in lines if ln.startswith(a))
    if n != 1:
        sys.exit("the anchor string is not unique in the zoo (%d hits): %r" % (n, a[:100]))
if sum(1 for ln in lines if ln.startswith(SHORT_IV1)) != 2:
    sys.exit("the shorter Session-27 head is expected exactly twice (III.20 and IV.1); the record has moved")

# 1. Count header: a blank line and the paragraph after the Session-30 count paragraph, before the '---'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_COUNT), "Session-30 count paragraph")
if any(ln.startswith("### ") for ln in lines[:i]):
    sys.exit("the Session-30 count paragraph is not in the header")
if lines[i + 1] != "" or lines[i + 2] != "---":
    sys.exit("the Session-30 count paragraph is not followed by a blank line and '---'")
if not lines[i - 2].startswith(PREV_COUNT) or lines[i - 1] != "":
    sys.exit("the Session-29 count paragraph is not directly above the Session-30 paragraph")
lines[i + 1:i + 1] = ["", blocks["count"]]

# 2. III.20: the note directly after the LOOKUP line (the entry's last bullet), before the blank line and '### III.21'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_III20), "III.20 LOOKUP line")
entry_of(lines, i, "### III.20 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### III.21 "):
    sys.exit("III.20's LOOKUP line is not the last line before '### III.21'")
if not lines[i - 1].startswith(PREV_III20):
    sys.exit("III.20's E3 pointer rider is not directly above the LOOKUP line")
if "19 no with grounds at the page, 1 undecided from disk" not in lines[i]:
    sys.exit("the LOOKUP line does not carry the '19 no … 1 undecided' tally the note dates closed")
lines[i + 1:i + 1] = [blocks["iii20note"]]

# 3. IV.1: the STATUS rider directly after the Session-27 pointer rider (the entry's last bullet), before the blank and '### IV.2'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_IV1), "IV.1 Session-27 pointer rider (full head)")
entry_of(lines, i, "### IV.1 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### IV.2 "):
    sys.exit("IV.1's pointer rider is not the last line before '### IV.2'")
if lines[i - 1] != PREV_IV1:
    sys.exit("IV.1's STATUS line ('BINDS: all routes') is not directly above the pointer rider")
seg = lines[i - 5:i]
if not (seg[0].startswith("- **STATEMENT.**") and seg[1].startswith("- **KILLS.**") and seg[2].startswith("- **EXECUTABLE TEST.**")
        and seg[3].startswith("- **SOURCE.**") and seg[4] == PREV_IV1):
    sys.exit("IV.1's five bullets STATEMENT / KILLS / EXECUTABLE TEST / SOURCE / STATUS are not the five lines above the anchor")
lines[i + 1:i + 1] = [blocks["iv1"]]

# 4. IV.17: the rider directly after the READ line (the entry's last bullet), before the blank and '### IV.19'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_IV17), "IV.17 READ line")
entry_of(lines, i, "### IV.17 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### IV.19 "):
    sys.exit("IV.17's READ line is not the last line before '### IV.19'")
if not lines[i - 1].startswith(PREV_IV17_HEAD):
    sys.exit("IV.17's STATUS line is not directly above the READ line")
seg = lines[i - 5:i]
if not (seg[0].startswith("- **STATEMENT.**") and seg[1].startswith("- **KILLS.**") and seg[2].startswith("- **EXECUTABLE TEST.**")
        and seg[3].startswith("- **SOURCE.**") and seg[4].startswith("- **STATUS.**")):
    sys.exit("IV.17's five bullets are not the five lines above the READ line")
if "locate the line where integrality is consumed — the (m − 1)(m − 2) slack or the m² ≥ m floor" not in seg[2] or "F1 = Σ m² = (4/3)N, N_d = (3/4)N" not in seg[2]:
    sys.exit("IV.17's EXECUTABLE TEST does not print items (1) and (3) as the rider cites them")
lines[i + 1:i + 1] = [blocks["iv17"]]

# 5. The formalization queue: the indented sub-bullet directly after item 10, before item 11 (line 665 itself untouched).
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_FQ10), "formalization-queue item 10")
entry_of(lines, i, "## Formalization queue")
if not lines[i + 1].startswith(NEXT_FQ10):
    sys.exit("item 11 is not directly after item 10 -- placement not verified")
if not lines[i + 2].startswith(NEXT2_FQ10):
    sys.exit("item 11's first sub-bullet is not directly after item 11")
if not lines[i - 1].startswith(PREV_FQ10):
    sys.exit("item 9 is not directly above item 10")
for j in range(i + 2, i + 6):
    if not (lines[j].startswith("    - **[") and not lines[j].startswith("     ")):
        sys.exit("item 11's sub-bullet at line %d is not indented exactly four spaces -- the precedent has moved" % (j + 1))
lines[i + 1:i + 1] = [blocks["fq10"]]

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
if not new_text.endswith("\n") or new_text.endswith("\n\n"):
    sys.exit("file must end with exactly one newline")
added = len(lines) - len(orig)
if added != 6:
    sys.exit("line arithmetic: added %d, expected 6" % added)
if len(orig) - 1 != 672 or len(lines) - 1 != 678:
    sys.exit("line count is %d -> %d, expected 672 -> 678" % (len(orig) - 1, len(lines) - 1))
for m in MARKS:
    if new_text.count(m) != 1:
        sys.exit("marker %r occurs %d times after insertion" % (m[:50], new_text.count(m)))
for k in NAMES:
    if new_text.count(blocks[k]) != 1:
        sys.exit("block %s occurs %d times after insertion" % (k, new_text.count(blocks[k])))

# The numbered formalization-queue list still reads 1-11 in order; the new sub-bullet is indented four spaces between 10 and 11.
q = unique_index(lines, lambda ln: ln.startswith("## Formalization queue"), "formalization-queue heading")
qend = q + 1
while qend < len(lines) and not lines[qend].startswith("*(File discipline"):
    qend += 1
numbered = [(j, int(re.match(r"(\d+)\. ", lines[j]).group(1))) for j in range(q, qend) if re.match(r"\d+\. ", lines[j])]
if [n for _, n in numbered] != list(range(1, 12)):
    sys.exit("the formalization queue's numbered items do not read 1-11 in order: %r" % [n for _, n in numbered])
j10 = [j for j, n in numbered if n == 10][0]
j11 = [j for j, n in numbered if n == 11][0]
if j11 != j10 + 2 or lines[j10 + 1] != blocks["fq10"] or not lines[j10 + 1].startswith("    - **[") or lines[j10 + 1].startswith("     "):
    sys.exit("the item-10 flip is not the single four-space-indented sub-bullet between items 10 and 11")
for j in range(q, qend):
    ln = lines[j]
    if ln.startswith(" ") and not (ln.startswith("    - **[") and not ln.startswith("     ")):
        sys.exit("an indented line in the formalization queue is not a four-space sub-bullet: %r" % ln[:60])

# In the 678-line result: the count paragraph at line 29 (27 + 2), '---' at 31; the III.20 note at 363 (360 + 2 + 1); the IV.1
# rider at 385 (381 + 3 + 1); the IV.17 rider at 563 (558 + 4 + 1); the item-10 flip at 671 (665 + 5 + 1), item 11 at 672; the
# file-discipline paragraph at 678.
if lines[28] != blocks["count"] or lines[27] != "" or not lines[26].startswith(ANCHOR_COUNT) or lines[29] != "" or lines[30] != "---":
    sys.exit("the count paragraph is not at line 29 between the Session-30 paragraph and the '---'")
if lines[362] != blocks["iii20note"] or not lines[361].startswith(ANCHOR_III20) or lines[363] != "" or not lines[364].startswith("### III.21 "):
    sys.exit("the III.20 note is not at line 363 directly after the LOOKUP line")
if lines[384] != blocks["iv1"] or not lines[383].startswith(ANCHOR_IV1) or lines[385] != "" or not lines[386].startswith("### IV.2 "):
    sys.exit("the IV.1 STATUS rider is not at line 385 directly after the Session-27 pointer rider")
if lines[562] != blocks["iv17"] or not lines[561].startswith(ANCHOR_IV17) or lines[563] != "" or not lines[564].startswith("### IV.19 "):
    sys.exit("the IV.17 rider is not at line 563 directly after the READ line")
if lines[670] != blocks["fq10"] or not lines[669].startswith(ANCHOR_FQ10) or not lines[671].startswith(NEXT_FQ10) or not lines[677].startswith("*(File discipline"):
    sys.exit("the item-10 flip is not at line 671 between item 10 (670) and item 11 (672), with the file-discipline paragraph at 678")

out = dry if dry else ZOO
out.write_text(new_text, encoding="utf-8")
print("OK: %s written; +%d lines (672 -> %d); entries 58 (I 8, II 5, III 21, IV 19, V 5); SHA-256 after %s%s"
      % (out, added, len(lines) - 1, hashlib.sha256(new_text.encode("utf-8")).hexdigest(), " [DRY RUN -- BARRIER-ZOO.md untouched]" if dry else ""))
