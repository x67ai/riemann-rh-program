#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 33 zoo stream `zoo-s33` (2026-09-29): insert into BARRIER-ZOO.md five lines, bookkeeping only -- the count paragraph
(block count: a blank line and the paragraph directly after the Session-32 count paragraph, before the '---'), the III.13 pointer
(block iii13: one top-level bullet directly after the entry's STATUS line -- the entry has no rider -- before the blank and
'### III.14'; anchored by the entry's heading, unique, plus its five-bullet shape, because the STATUS text occurs six times in the
file), the IV.1 rider on Suzuki 2606.09096 v1 -> v3 (block iv1: one top-level bullet directly after the entry's last rider, the
Session-32 REFINEMENT rider, before the blank and '### IV.2'), the formalization-queue item-8 note (block fq8: an INDENTED
sub-bullet -- exactly four spaces, then "- **[" -- directly after item 8 and before item 9) and the item-10 pair-channel sub-bullet
(block fq10: the same indentation, directly after item 10's LINUX REPLAY sub-bullet and before item 11; H4's label VERBATIM as
the three record files print it). No numbered entry: the entry count stays 58 (I 8, II 5, III 21, IV 19, V 5); 686 -> 692 lines
(+6: four one-line bullets and sub-bullets, the count paragraph and the blank line before it).

Source of every inserted line: results/zoo-s33/zoo-entries-proposed.md, read AT RUN TIME (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->), so the orchestrator's post-reader amendments flow in. Before touching the zoo the
script asserts that BARRIER-ZOO.md has SHA-256 573b621e... (the zoo at brief time) and that the three record files carrying H4's
label have b1183502... (BUILD-NOTES), 2401eb9d... (ZOO-LINES-STAGED) and 578993a9... (ORCHESTRATOR-NOTES); that every anchor
occurs exactly once (anchored by the full text of the neighboring lines, never by line number alone); that the lines around each
anchor are what the brief says (blank + '---' after the count paragraph; blank + '### III.14' after III.13's STATUS; blank +
'### IV.2' after IV.1's REFINEMENT rider; item 9 after item 8; item 11 and its PRICED sub-bullet after item 10's LINUX REPLAY
sub-bullet), so the placement is verified, not assumed; and that the label quoted inside block fq10 equals, character for
character, the strings pulled from the three record files at run time (wrapped lines joined with single spaces; every string
printed on mismatch, and the script refuses). Pure insertion: no existing line is modified or removed. The script refuses to run
twice. Afterwards it verifies that every original line survives, in order, as an identical line, that the '### ' count is 58
with per-group counts 8/5/21/19/5, that the numbered formalization-queue list still reads 1-11 in order with the two new
sub-bullets indented exactly four spaces (between 8 and 9; between item 10's LINUX REPLAY sub-bullet and 11), that the line
arithmetic is exact (+6, 686 -> 692), that the file ends with exactly one newline, and that the inserted text carries none of
the linted phrases (10(g)), none of the three forbidden phrasings of the H4 unit and none of the s32 forbidden sentences.

Usage: python3 scripts/zoo-insert-s33.py [--dry-run OUTPATH]
  --dry-run OUTPATH    write the result to OUTPATH and leave BARRIER-ZOO.md untouched (the writer's only mode).
Modeled on scripts/zoo-insert-s32.py.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s33" / "zoo-entries-proposed.md"
H4 = ROOT / "results" / "h4-pair-lean-s33"
BN = H4 / "BUILD-NOTES.md"
STAGED = H4 / "ZOO-LINES-STAGED.md"
ON = H4 / "ORCHESTRATOR-NOTES.md"
ZOO_HASH_BEFORE = "573b621e1c2ec8827b9d7e80c80f592c23a2810aa4f18d19736447ab068bab7f"
BN_HASH = "b11835027397bc3e7d601c7aa80a76f2744454c4940dd9d30a14ed080f994261"
STAGED_HASH = "2401eb9dd5ab90d885620bb7861871d226a8c57c01a480107b69777502f549c8"
ON_HASH = "578993a9f80a4e5fb1fecb5b580dc23b5a9a3a60e6574809800961a6868335d1"

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
for p, h in ((BN, BN_HASH), (STAGED, STAGED_HASH), (ON, ON_HASH)):
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    if got != h:
        sys.exit("%s SHA-256 is %s, expected %s -- the label's record changed; nothing done." % (p.relative_to(ROOT), got, h))

ENTERED = "entered at the Session-33 zoo stream"
MARKS = ("**Entry count (dated, Session 33, 2026-09-29).**",
         "- **[POINTER 2026-09-29, Session 33 (the s32 digest §D J1 as read, `results/program-digest-s32.md`; " + ENTERED + ") — Suzuki 2606.09096v3.]**",
         "- **[RIDER 2026-09-29, Session 33 (the s32 digest §D J1 as read, `results/program-digest-s32.md` 565e39bf…; `ranking-read-O.md` M1, M2; " + ENTERED + ") — Suzuki 2606.09096, v1 → v3:",
         "    - **[NOTE 2026-09-29, Session 33 — rung 0 answered by grep, NOT funded; owed since the SESSION 32 QUEUE; " + ENTERED + ".]**",
         "    - **[PAIR CHANNEL COMPARATOR-CHECKED 2026-09-29, Session 33 (H4, `results/h4-pair-lean-s33/`; CHECK-O 8e59f36bf2c2bfbf…; " + ENTERED + ").]**")
for m in MARKS:
    if m in zoo_text:
        sys.exit("BARRIER-ZOO.md already contains %r -- refusing to insert twice." % m[:70])


def block(text: str, name: str, where: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)), text, re.S)
    if len(ms) != 1:
        sys.exit("block %s occurs %d times in %s (need exactly 1)" % (name, len(ms), where))
    return ms[0]


NAMES = ("count", "iii13", "iv1", "fq8", "fq10")
blocks = {k: block(prop_text, k, "the proposed file") for k in NAMES}
for k, v in blocks.items():
    if not v.strip():
        sys.exit("block %s is empty" % k)
    if v.count("\n") != 0:
        sys.exit("block %s must be exactly one line" % k)
    for bad in ("clearly", "obviously", "easy to see", "well known", "well-known"):
        if bad in v.lower():
            sys.exit("block %s contains the linted phrase %r" % (k, bad))
    if v.lstrip().startswith("### ") or v.lstrip().startswith("## "):
        sys.exit("block %s would add a heading" % k)
    if v in zoo_text:
        sys.exit("block %s is already in the zoo" % k)

# Shapes of the heads.
for k, head in zip(NAMES, MARKS):
    if not blocks[k].startswith(head):
        sys.exit("block %s must start with %r" % (k, head[:60]))
    if k != "count" and "]**" not in blocks[k]:
        sys.exit("block %s has no house head closing ']**'" % k)
    if k != "count" and ENTERED not in blocks[k].split("]**", 1)[0]:
        sys.exit("block %s does not carry %r inside its head" % (k, ENTERED))
for k in ("iii13", "iv1"):
    if not blocks[k].startswith("- **["):
        sys.exit("block %s must be a top-level bullet '- **['" % k)
for k in ("fq8", "fq10"):
    if not blocks[k].startswith("    - **[") or blocks[k].startswith("     "):
        sys.exit("block %s must begin with exactly four spaces then '- **[' (items 6, 10 and 11's sub-bullets are the precedent)" % k)
    if "\t" in blocks[k][:8]:
        sys.exit("block %s must be indented with spaces, not a tab" % k)

# --- The label: pulled from the three record files at run time and compared character for character with the quoted string
#     in block fq10 (standing order 7). ---


def pull_buildnotes_label(path: Path) -> str:
    fl = path.read_text(encoding="utf-8").split("\n")
    starts = [k for k, ln in enumerate(fl) if ln.startswith("**Label, verbatim and binding")]
    if len(starts) != 1:
        sys.exit("%s does not carry exactly one '**Label, verbatim and binding' paragraph (found %d)" % (path.name, len(starts)))
    i = starts[0]
    j = i
    while j < len(fl) and fl[j].strip():
        j += 1
    para = " ".join(ln.strip() for ln in fl[i:j])
    ms = re.findall(r'\*\*"(.*?)"\.\*\*', para)
    if len(ms) != 1:
        sys.exit("%s label paragraph does not carry exactly one bold quoted label closed as '\".**' (found %d); the record has moved" % (path.name, len(ms)))
    return ms[0]


def pull_staged_label(path: Path) -> str:
    hits = [ln for ln in path.read_text(encoding="utf-8").split("\n") if ln.startswith("    - **[PAIR CHANNEL COMPARATOR-CHECKED 2026-09-29, Session 33")]
    if len(hits) != 1:
        sys.exit("%s does not carry exactly one staged PAIR CHANNEL sub-bullet (found %d)" % (path.name, len(hits)))
    ms = re.findall(r'Label, as the builder and the checker assign it: "(.*?)"', hits[0])
    if len(ms) != 1:
        sys.exit("%s staged line does not carry exactly one 'Label, as the builder and the checker assign it: \"...\"' (found %d)" % (path.name, len(ms)))
    return ms[0]


def pull_orchestrator_label(path: Path) -> str:
    hits = [ln for ln in path.read_text(encoding="utf-8").split("\n") if ln.startswith("**Label earned (after CHECK-O")]
    if len(hits) != 1:
        sys.exit("%s does not carry exactly one '**Label earned (after CHECK-O' line (found %d)" % (path.name, len(hits)))
    ms = re.findall(r'\*\*Label earned \(after CHECK-O, no displayed hypothesis, verbatim\):\*\* "(.*?)"', hits[0])
    if len(ms) != 1:
        sys.exit("%s §2 label line does not carry exactly one quoted label (found %d)" % (path.name, len(ms)))
    return ms[0]


LABELS = (("BUILD-NOTES.md lines 16-28", pull_buildnotes_label(BN)), ("ZOO-LINES-STAGED.md line 5", pull_staged_label(STAGED)),
          ("ORCHESTRATOR-NOTES.md §2 line 32", pull_orchestrator_label(ON)))
LABEL = LABELS[0][1]
for src, lab in LABELS[1:]:
    if lab != LABEL:
        sys.exit("H4's label differs between the record files (standing order 7).\n  BUILD-NOTES: %r\n  %s: %r\nRefusing." % (LABEL, src, lab))
intro = 'Label, as the builder and the checker assign it: "'
b = blocks["fq10"]
if b.count(intro) != 1:
    sys.exit("block fq10 does not carry the label introduction %r exactly once" % intro)
quoted = b.split(intro, 1)[1]
end = quoted.find('"')
if end < 0:
    sys.exit("block fq10: the label's closing straight quote is missing")
quoted = quoted[:end]
if quoted != LABEL:
    sys.exit("block fq10: the quoted label differs from the record (the three files agree with each other).\n  RECORD: %r\n  BLOCK:  %r\nRefusing." % (LABEL, quoted))
if b.count('"' + LABEL + '"') != 1:
    sys.exit("block fq10 must carry the label in straight double quotes exactly once")
for k in NAMES:
    if k != "fq10" and LABEL in blocks[k]:
        sys.exit("block %s carries the label; only fq10 may" % k)
print("OK: the label in block fq10 equals the string pulled from the three record files (BUILD-NOTES, ZOO-LINES-STAGED, ORCHESTRATOR-NOTES §2), character for character (%d characters):\n   %s" % (len(LABEL), LABEL))

# The staged line: block fq10 is the staged sub-bullet with at most the one clause of the proposed file's finding 3 reworded.
staged_line = [ln for ln in STAGED.read_text(encoding="utf-8").split("\n") if ln.startswith(MARKS[4])][0]
OLD_CLAUSE = "(MI) fails over ℚ through the mark-4/3 atom column of the sub-bullet above and nowhere else on the record."
NEW_CLAUSE = "(MI)'s falsity over ℚ is the mark-4/3 atom column of the sub-bullet above and nowhere else on the record."
if b != staged_line and b != staged_line.replace(OLD_CLAUSE, NEW_CLAUSE):
    sys.exit("block fq10 is neither the staged line nor the staged line with finding 3's one clause reworded; the block has drifted from ZOO-LINES-STAGED.md line 5")

# Forbidden phrasings of the H4 unit (UNIT-BRIEF §1(3); case-insensitive fixed strings, as CHECK-O §9 greps) and the s32 sentences (never widen).
for k in NAMES:
    b = blocks[k]
    for forb in ("(mi) fails", "iv.17 is formalized", "pair channel is closed"):
        if forb in b.lower():
            sys.exit("block %s carries the forbidden phrasing %r" % (k, forb))
    for forb in ("IV.1's containment inside `EF_lit`", "the tilted test is C²", "DH has no Euler product", "RH-equivalent",
                 "the tilted explicit formula is formalized", "kernel-checked on Prove2Me"):
        if forb in b:
            sys.exit("block %s carries the forbidden sentence %r" % (k, forb))
    if re.search(r"(?<![A-Z])I\.1 formalized(?!-)", b):
        sys.exit("block %s carries the forbidden sentence 'I.1 formalized'" % k)

# Content sentinels per block (the brief's "The lines").
if "58 entries" not in blocks["count"] or "686 → 692" not in blocks["count"] or "573b621e" not in blocks["count"] or "I: 8, II: 5, III: 21, IV: 19, V: 5" not in blocks["count"] or "Group IV" not in blocks["count"]:
    sys.exit("count block does not carry the 58 count, the 686 → 692 line count, the launch hash and the Group-IV sentence")
if "NOT a reparametrization" not in blocks["iii13"] or "IV.1 rider" not in blocks["iii13"] or "expectation" not in blocks["iii13"]:
    sys.exit("block iii13 does not carry the entry's test phrase, the pointer to the IV.1 rider and the expectation qualifier")
iv1 = blocks["iv1"]
for need in ("v1 8 Jun 2026, v2 17 Aug 2026, v3 23 Sep 2026, 33 pages", "line 348", "line 367", "lines 383–386",
             "does not appear to provide a simple route to a proof of RH", "involves only finitely many primes for fixed a > 0",
             "`verdict_statement`", "(1.1)", "2511.22755", "FORMULATION.md` line 46", "NOTE.md` line 197", "ranking-read-O.md` line 18",
             "NOT funded as a unit", "III.13", "III.5", "CLOSED"):
    if need not in iv1:
        sys.exit("block iv1 does not carry %r" % need)
for need in ("51e6992e", "`Mathlib/AlgebraicTopology/SingularHomology/`", "`Mathlib/Topology/Sheaves/MayerVietoris.lean`",
             "`Mathlib/CategoryTheory/Sites/SheafCohomology/MayerVietoris.lean`", "`Mathlib/CategoryTheory/Sites/MayerVietorisSquare.lean`", "NOT funded"):
    if need not in blocks["fq8"]:
        sys.exit("block fq8 does not carry %r" % need)
for need in ("`PairChannel`", "`prop45`", "`floor_fails_anchor`", "8e59f36bf2c2bfbf", "Not covered: (MI) at any anchor", "Theorems 4.6–4.9", "Nothing about ζ or RH follows."):
    if need not in blocks["fq10"]:
        sys.exit("block fq10 does not carry %r" % need)


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
ANCHOR_COUNT = "**Entry count (dated, Session 32, 2026-09-29).** No entry is added. The seven lines entered at this stream (the I.1 rider"
PREV_COUNT = "**Entry count (dated, Session 31, 2026-09-29).**"
HEAD_III13 = "### III.13 Lapidus equivalence-level death certificate"
STATUS_III13 = "- **STATUS.** sweep-certified. **BINDS: full-RH.**"
TEST_III13 = "identify the one implication that is NOT a reparametrization"
ANCHOR_IV1 = "- **[REFINEMENT 2026-09-29, Session 32 (H5, `results/h5-c2-lean-s32/`; CHECK-O 74b7cfb8…; entered at the Session-32 zoo stream).]**"
PREV_IV1 = "- **[LINUX REPLAY 2026-09-29, Session 32 (`results/linux-check-s30/`; `results/d5-lean-s30/CHECK-O.md` §12; entered at the Session-32 zoo stream).]**"
PREV2_IV1 = "- **[STATUS RIDER 2026-09-29, Session 30 (D5, `results/d5-lean-s30/`; entered at the Session-31 zoo stream) — formalized-in-Lean.]**"
STATUS_IV1 = "- **STATUS.** program-adjudicated (computationally verified in C1). **BINDS: all routes.**"
ANCHOR_FQ8 = "8. The closed-3-manifold finite-rank length-group theorem (IV.13"
NEXT_FQ8 = "9. Theorem A (A)+(B) (IV.14)"
PREV_FQ8 = "7. Converse-theorem-form DH-exclusion via Blomer–Leung (I.1 rider)"
ANCHOR_FQ10SUB = "    - **[LINUX REPLAY 2026-09-29, Session 32 (`results/linux-check-s30/`; `results/iv17-lean-s30/CHECK-O.md` §11; entered at the Session-32 zoo stream).]**"
PREV_FQ10SUB = "    - **[FORMALIZED AND SHIPPED 2026-09-29, Session 30 — Comparator topic `IntegralityGap`"
PREV2_FQ10SUB = "10. The fractional-mark integrality theorem (IV.17)"
NEXT_FQ10SUB = "11. **Theorem M2's Lemma G"
NEXT2_FQ10SUB = "    - **[PRICED 2026-09-24, Session 24"
for a in (ANCHOR_COUNT, PREV_COUNT, HEAD_III13, ANCHOR_IV1, PREV_IV1, PREV2_IV1, ANCHOR_FQ8, NEXT_FQ8, PREV_FQ8, ANCHOR_FQ10SUB, PREV_FQ10SUB, PREV2_FQ10SUB, NEXT_FQ10SUB):
    n = sum(1 for ln in lines if ln.startswith(a))
    if n != 1:
        sys.exit("the anchor string is not unique in the zoo (%d hits): %r" % (n, a[:100]))

# 1. Count header: a blank line and the paragraph after the Session-32 count paragraph, before the '---'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_COUNT), "Session-32 count paragraph")
if any(ln.startswith("### ") for ln in lines[:i]):
    sys.exit("the Session-32 count paragraph is not in the header")
if lines[i + 1] != "" or lines[i + 2] != "---":
    sys.exit("the Session-32 count paragraph is not followed by a blank line and '---'")
if not lines[i - 2].startswith(PREV_COUNT) or lines[i - 1] != "":
    sys.exit("the Session-31 count paragraph is not directly above the Session-32 paragraph")
lines[i + 1:i + 1] = ["", blocks["count"]]

# 2. III.13: the pointer directly after the entry's STATUS line (its last line; no rider), before the blank and '### III.14'.
h = unique_index(lines, lambda ln: ln.startswith(HEAD_III13), "III.13 heading")
seg = lines[h:h + 9]
if not (seg[1] == "" and seg[2].startswith("- **STATEMENT.**") and seg[3].startswith("- **KILLS.**") and seg[4].startswith("- **EXECUTABLE TEST.**")
        and TEST_III13 in seg[4] and seg[5].startswith("- **SOURCE.**") and seg[6] == STATUS_III13 and seg[7] == "" and seg[8].startswith("### III.14 ")):
    sys.exit("III.13 is not heading / blank / STATEMENT / KILLS / EXECUTABLE TEST (with the reparametrization sentence) / SOURCE / STATUS / blank / '### III.14' -- placement not verified")
i = h + 6
lines[i + 1:i + 1] = [blocks["iii13"]]

# 3. IV.1: the rider directly after the Session-32 REFINEMENT rider (the entry's last rider), before the blank and '### IV.2'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_IV1), "IV.1 Session-32 REFINEMENT rider")
entry_of(lines, i, "### IV.1 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### IV.2 "):
    sys.exit("IV.1's REFINEMENT rider is not the last line before '### IV.2'")
if not lines[i - 1].startswith(PREV_IV1) or not lines[i - 2].startswith(PREV2_IV1):
    sys.exit("IV.1's LINUX REPLAY line and STATUS RIDER are not the two lines above the anchor")
seg = lines[i - 8:i - 2]
if not (seg[0].startswith("- **STATEMENT.**") and seg[1].startswith("- **KILLS.**") and seg[2].startswith("- **EXECUTABLE TEST.**")
        and seg[3].startswith("- **SOURCE.**") and seg[4] == STATUS_IV1 and seg[5].startswith("- **[RIDER 2026-09-25, Session 27")):
    sys.exit("IV.1's five bullets and the Session-27 pointer rider are not the six lines above the STATUS RIDER")
lines[i + 1:i + 1] = [blocks["iv1"]]

# 4. The formalization queue: the item-8 note directly after item 8, before item 9 (line 675 itself untouched).
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_FQ8), "formalization-queue item 8")
entry_of(lines, i, "## Formalization queue")
if not lines[i + 1].startswith(NEXT_FQ8):
    sys.exit("item 9 is not directly after item 8 -- placement not verified")
if not lines[i - 1].startswith(PREV_FQ8):
    sys.exit("item 7 is not directly above item 8")
if "the topological half needs a Mayer–Vietoris sequence for open covers of a 3-manifold and must be checked against Mathlib's current homology coverage before commissioning" not in lines[i]:
    sys.exit("item 8 does not print the rung-0 sentence the note answers")
lines[i + 1:i + 1] = [blocks["fq8"]]

# 5. The formalization queue: the item-10 pair-channel sub-bullet directly after the LINUX REPLAY sub-bullet, before item 11.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_FQ10SUB), "item 10's LINUX REPLAY sub-bullet")
entry_of(lines, i, "## Formalization queue")
if not lines[i - 1].startswith(PREV_FQ10SUB) or not lines[i - 2].startswith(PREV2_FQ10SUB):
    sys.exit("item 10 and its FORMALIZED AND SHIPPED sub-bullet are not the two lines above the LINUX REPLAY sub-bullet")
if "the pair channel unformalized" not in lines[i]:
    sys.exit("the LINUX REPLAY sub-bullet does not print 'the pair channel unformalized' (the sentence block fq10 supersedes)")
if not lines[i + 1].startswith(NEXT_FQ10SUB):
    sys.exit("item 11 is not directly after item 10's LINUX REPLAY sub-bullet -- placement not verified")
if not lines[i + 2].startswith(NEXT2_FQ10SUB):
    sys.exit("item 11's first sub-bullet is not directly after item 11")
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
if len(orig) - 1 != 686 or len(lines) - 1 != 692:
    sys.exit("line count is %d -> %d, expected 686 -> 692" % (len(orig) - 1, len(lines) - 1))
for m in MARKS:
    if new_text.count(m) != 1:
        sys.exit("marker %r occurs %d times after insertion" % (m[:50], new_text.count(m)))
for k in NAMES:
    if new_text.count(blocks[k]) != 1:
        sys.exit("block %s occurs %d times after insertion" % (k, new_text.count(blocks[k])))

# The numbered formalization-queue list still reads 1-11 in order; the two new sub-bullets are indented four spaces at their places.
q = unique_index(lines, lambda ln: ln.startswith("## Formalization queue"), "formalization-queue heading")
qend = q + 1
while qend < len(lines) and not lines[qend].startswith("*(File discipline"):
    qend += 1
numbered = [(j, int(re.match(r"(\d+)\. ", lines[j]).group(1))) for j in range(q, qend) if re.match(r"\d+\. ", lines[j])]
if [n for _, n in numbered] != list(range(1, 12)):
    sys.exit("the formalization queue's numbered items do not read 1-11 in order: %r" % [n for _, n in numbered])
j8 = [j for j, n in numbered if n == 8][0]
j9 = [j for j, n in numbered if n == 9][0]
if j9 != j8 + 2 or lines[j8 + 1] != blocks["fq8"]:
    sys.exit("the item-8 note is not the single four-space-indented line between items 8 and 9")
j10 = [j for j, n in numbered if n == 10][0]
j11 = [j for j, n in numbered if n == 11][0]
if j11 != j10 + 4 or not lines[j10 + 1].startswith(PREV_FQ10SUB) or not lines[j10 + 2].startswith(ANCHOR_FQ10SUB) or lines[j10 + 3] != blocks["fq10"]:
    sys.exit("item 10 is not followed by its FORMALIZED AND SHIPPED sub-bullet, the LINUX REPLAY sub-bullet, the PAIR CHANNEL sub-bullet, then item 11")
for j in range(q, qend):
    ln = lines[j]
    if ln.startswith(" ") and not (ln.startswith("    - **[") and not ln.startswith("     ")):
        sys.exit("an indented line in the formalization queue is not a four-space sub-bullet: %r" % ln[:60])

# In the 692-line result: the count paragraph at line 33 (31 + 2), '---' at 35; the III.13 pointer at 300 (297 + 2 + 1); the IV.1
# rider at 394 (390 + 3 + 1); the item-8 note at 680 (675 + 4 + 1), item 9 at 681; the pair-channel sub-bullet at 685 (679 + 5 + 1),
# item 11 at 686; the file-discipline paragraph at 692.
if lines[32] != blocks["count"] or lines[31] != "" or not lines[30].startswith(ANCHOR_COUNT) or lines[33] != "" or lines[34] != "---":
    sys.exit("the count paragraph is not at line 33 between the Session-32 paragraph and the '---'")
if lines[299] != blocks["iii13"] or lines[298] != STATUS_III13 or not lines[292].startswith(HEAD_III13) or lines[300] != "" or not lines[301].startswith("### III.14 "):
    sys.exit("the III.13 pointer is not at line 300 directly after the entry's STATUS line")
if lines[393] != blocks["iv1"] or not lines[392].startswith(ANCHOR_IV1) or lines[394] != "" or not lines[395].startswith("### IV.2 "):
    sys.exit("the IV.1 rider is not at line 394 directly after the Session-32 REFINEMENT rider")
if lines[679] != blocks["fq8"] or not lines[678].startswith(ANCHOR_FQ8) or not lines[680].startswith(NEXT_FQ8):
    sys.exit("the item-8 note is not at line 680 between item 8 (679) and item 9 (681)")
if lines[684] != blocks["fq10"] or not lines[683].startswith(ANCHOR_FQ10SUB) or not lines[685].startswith(NEXT_FQ10SUB) or not lines[691].startswith("*(File discipline"):
    sys.exit("the pair-channel sub-bullet is not at line 685 between the LINUX REPLAY sub-bullet (684) and item 11 (686), with the file-discipline paragraph at 692")

out = dry if dry else ZOO
out.write_text(new_text, encoding="utf-8")
print("OK: %s written; +%d lines (686 -> %d); entries 58 (I 8, II 5, III 21, IV 19, V 5); Group IV 19 (no heading added); the five blocks at lines 33, 300, 394, 680, 685; SHA-256 after %s%s"
      % (out, added, len(lines) - 1, hashlib.sha256(new_text.encode("utf-8")).hexdigest(), " [DRY RUN -- BARRIER-ZOO.md untouched]" if dry else ""))
