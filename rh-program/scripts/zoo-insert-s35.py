#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 34 zoo stream `zoo-s35` (2026-09-29): insert into BARRIER-ZOO.md six lines, bookkeeping only -- the count paragraph
(block count: a blank line and the paragraph directly after the Session-33 count paragraph, before the '---'), the I.1 LINUX REPLAY
line (block i1: one top-level bullet directly after the entry's last line, the WITNESSES KERNEL-CHECKED bullet, before the blank
and '### I.2'), the II.1 Lamzouri v2 rider (block ii1: one top-level bullet directly after the II.1 DATED NOTE, before the blank
and the DUAL-MODEL CHECK bullet), the II.4 Lamzouri v2 rider (block ii4: the same text, directly after the II.4 DATED NOTE, before
the blank and the DUAL-MODEL CHECK bullet), the IV.1 LINUX REPLAY line (block iv1: one top-level bullet directly after the entry's
last line, the Session-33 Suzuki RIDER that follows the REFINEMENT anchor, before the blank and '### IV.2') and the item-10 LINUX
REPLAY sub-bullet (block fq10: an INDENTED sub-bullet -- exactly four spaces, then "- **[" -- directly after item 10's PAIR CHANNEL
sub-bullet and before item 11). No numbered entry: the entry count stays 58 (I 8, II 5, III 21, IV 19, V 5); 692 -> 699 lines
(+7: five one-line bullets and sub-bullets, the count paragraph and the blank line before it).

Source of every inserted line: results/zoo-s35/zoo-entries-proposed.md, read AT RUN TIME (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->), so the orchestrator's post-reader amendments flow in. Before touching the zoo the
script asserts that BARRIER-ZOO.md has SHA-256 07a87152... (the zoo at brief time) and that the two STAGED files have 81bac262...
(results/linux-check-s33/ZOO-LINES-STAGED.md) and 96fbf141... (results/watch-poll-s34/ZOO-LINES-STAGED.md); that every block
equals its staged line with only the permitted substitutions (the bracket phrase "entered at the Session-34 zoo stream" the brief
requires; for the rider, optionally "(see Remark 3.4 below)" for the staged "(see Remark 3.4)" -- the record's wording at v2 line
187 -- and optionally the dual-checked label the reader may assign under standing order 7); that every anchor occurs exactly once
(anchored by the full text of the neighboring lines, never by line number alone; the two DATED NOTES share a head and are told
apart by their continuation text and their entry heading); that the lines around each anchor are what the brief says, so the
placement is verified, not assumed. Pure insertion: no existing line is modified or removed. The script refuses to run twice.
Afterwards it verifies that every original line survives, in order, as an identical line, that the '### ' count is 58 with
per-group counts 8/5/21/19/5, that the numbered formalization-queue list still reads 1-11 in order with every indented line a
four-space sub-bullet, that the line arithmetic is exact (+7, 692 -> 699), that the file ends with exactly one newline, that the
rider text occurs exactly twice and every other block once, and that the inserted text carries none of the linted phrases (10(g)),
none of the three forbidden phrasings of the H4 unit and none of the s32 forbidden sentences.

Usage: python3 scripts/zoo-insert-s35.py [--dry-run OUTPATH]
  --dry-run OUTPATH    write the result to OUTPATH and leave BARRIER-ZOO.md untouched (the writer's only mode).
Modeled on scripts/zoo-insert-s33.py.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s35" / "zoo-entries-proposed.md"
STAGED_LINUX = ROOT / "results" / "linux-check-s33" / "ZOO-LINES-STAGED.md"
STAGED_WATCH = ROOT / "results" / "watch-poll-s34" / "ZOO-LINES-STAGED.md"
ZOO_HASH_BEFORE = "07a87152e58a04d07cb472e00871682580b516a05a93cd35accecb0b01fe064b"
STAGED_LINUX_HASH = "81bac2626e14948190d5dafdac55fa18b4a2283e336a92258d6f665dd09ea2c9"
STAGED_WATCH_HASH = "96fbf1419fdc86a82e3ac7df574bb4772c7f86aac1ca1b140ff9e968af603acf"

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
for p, h in ((STAGED_LINUX, STAGED_LINUX_HASH), (STAGED_WATCH, STAGED_WATCH_HASH)):
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    if got != h:
        sys.exit("%s SHA-256 is %s, expected %s -- the staged record changed; nothing done." % (p.relative_to(ROOT), got, h))

ENTERED = "entered at the Session-34 zoo stream"
LINUX_HEAD = "- **[LINUX REPLAY 2026-09-29, Session 34 (`results/linux-check-s33/`; HARVEST-NOTE.md; " + ENTERED + ").]**"
RIDER_HEAD = "- **[RIDER 2026-09-29, Session 34 — v2 of arXiv:2609.02882 (8 Sep 2026); found by the Session 34 watch poll; "
MARKS = ("**Entry count (dated, Session 34, 2026-09-29).**",
         LINUX_HEAD + " `EpsteinWitnessSix` (rung 1) and `I1Witness` replayed",
         RIDER_HEAD,
         RIDER_HEAD,
         LINUX_HEAD + " Both H5 topics (`WeilContainmentC2One`, `WeilContainmentC2`) replayed",
         "    " + LINUX_HEAD + " `PairChannel` replayed")
for m in set(MARKS):
    if m in zoo_text:
        sys.exit("BARRIER-ZOO.md already contains %r -- refusing to insert twice." % m[:70])
if "Session 34" in zoo_text or ENTERED in zoo_text:
    sys.exit("BARRIER-ZOO.md already carries a Session-34 line -- refusing to insert twice.")


def block(text: str, name: str, where: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)), text, re.S)
    if len(ms) != 1:
        sys.exit("block %s occurs %d times in %s (need exactly 1)" % (name, len(ms), where))
    return ms[0]


NAMES = ("count", "i1", "ii1", "ii4", "iv1", "fq10")
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
for k in ("i1", "ii1", "ii4", "iv1"):
    if not blocks[k].startswith("- **["):
        sys.exit("block %s must be a top-level bullet '- **[' (the brief: at the anchor's own indentation)" % k)
if not blocks["fq10"].startswith("    - **[") or blocks["fq10"].startswith("     "):
    sys.exit("block fq10 must begin with exactly four spaces then '- **[' (items 6, 10 and 11's sub-bullets are the precedent)")
if "\t" in blocks["fq10"][:8]:
    sys.exit("block fq10 must be indented with spaces, not a tab")
if blocks["ii1"] != blocks["ii4"]:
    sys.exit("blocks ii1 and ii4 must be the same rider text (the staged file: 'identical beneath both')")

# --- The staged lines: each block equals its staged line with only the permitted substitutions. ---
linux_lines = [ln for ln in STAGED_LINUX.read_text(encoding="utf-8").split("\n") if ln.strip().startswith("- **[LINUX REPLAY 2026-09-29, Session 34")]
if len(linux_lines) != 3:
    sys.exit("results/linux-check-s33/ZOO-LINES-STAGED.md does not carry exactly three staged LINUX REPLAY lines (found %d)" % len(linux_lines))
OLD_BRACKET_LINUX = "(`results/linux-check-s33/`; HARVEST-NOTE.md).]**"
NEW_BRACKET_LINUX = "(`results/linux-check-s33/`; HARVEST-NOTE.md; " + ENTERED + ").]**"
staged_by_topic = {}
for ln in linux_lines:
    if ln.count(OLD_BRACKET_LINUX) != 1:
        sys.exit("a staged LINUX REPLAY line does not carry the bracket close %r exactly once" % OLD_BRACKET_LINUX)
    body = ln.strip().replace(OLD_BRACKET_LINUX, NEW_BRACKET_LINUX)
    for topic in ("`EpsteinWitnessSix`", "`WeilContainmentC2One`", "`PairChannel`"):
        if topic in body.split("]**", 1)[1][:60]:
            staged_by_topic[topic] = body
if sorted(staged_by_topic) != ["`EpsteinWitnessSix`", "`PairChannel`", "`WeilContainmentC2One`"]:
    sys.exit("the three staged LINUX REPLAY lines are not one each for EpsteinWitnessSix / WeilContainmentC2One / PairChannel")
for k, topic, indent in (("i1", "`EpsteinWitnessSix`", ""), ("iv1", "`WeilContainmentC2One`", ""), ("fq10", "`PairChannel`", "    ")):
    if blocks[k] != indent + staged_by_topic[topic]:
        sys.exit("block %s is not the staged %s line with the bracket phrase %r added (and nothing else changed); the block has drifted from ZOO-LINES-STAGED.md" % (k, topic, ENTERED))

rider_lines = [ln for ln in STAGED_WATCH.read_text(encoding="utf-8").split("\n") if ln.startswith("- **[RIDER 2026-09-29, Session 34")]
if len(rider_lines) != 1:
    sys.exit("results/watch-poll-s34/ZOO-LINES-STAGED.md does not carry exactly one staged rider (found %d)" % len(rider_lines))
OLD_BRACKET_RIDER = "source `results/watch-lamzouri-2609.02882/V2-DELTA-s34.md`.]**"
NEW_BRACKET_RIDER = "source `results/watch-lamzouri-2609.02882/V2-DELTA-s34.md`; " + ENTERED + ".]**"
OLD_QUOTE = "the same Montgomery–Taylor extremal problem (see Remark 3.4)"
NEW_QUOTE = "the same Montgomery–Taylor extremal problem (see Remark 3.4 below)"   # v2 extraction line 187
OLD_TAIL = "so the degeneracy recorded here is untouched."
NEW_TAIL = "so what this entry records (II.1's ceiling, II.4's degeneracy) is untouched."  # reader's P2: II.1 records a ceiling, not a degeneracy
OLD_LABEL = "single-check — orchestrator's reading"
NEW_LABEL = "dual-checked (orchestrator Fable 5.1 + Opus 5 reader, Session 34)"  # standing order 7, on the reader's AGREE
staged_rider = rider_lines[0]
for s in (OLD_BRACKET_RIDER, OLD_QUOTE, OLD_LABEL, OLD_TAIL):
    if staged_rider.count(s) != 1:
        sys.exit("the staged rider does not carry %r exactly once; the record has moved" % s)
base = staged_rider.replace(OLD_BRACKET_RIDER, NEW_BRACKET_RIDER).replace(OLD_TAIL, NEW_TAIL)
allowed = set()
for q in (base, base.replace(OLD_QUOTE, NEW_QUOTE)):
    for lab in (q, q.replace(OLD_LABEL, NEW_LABEL)):
        allowed.add(lab)
if blocks["ii1"] not in allowed:
    sys.exit("block ii1/ii4 is not the staged rider with only the permitted substitutions (the bracket phrase; optionally '(see Remark 3.4 below)'; optionally the dual-checked label); the block has drifted from results/watch-poll-s34/ZOO-LINES-STAGED.md line 7")
label_in_block = NEW_LABEL if NEW_LABEL in blocks["ii1"] else OLD_LABEL
print("OK: the rider carries the label %r (standing order 7: the reader decides; the writer carried the staged label)" % label_in_block)

# Forbidden phrasings of the H4 unit (UNIT-BRIEF §1(3); case-insensitive fixed strings) and the s32 sentences (never widen).
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
c = blocks["count"]
if "58 entries" not in c or "692 → 699" not in c or "07a87152" not in c or "I: 8, II: 5, III: 21, IV: 19, V: 5" not in c or "Group IV" not in c or "results/zoo-s35/" not in c:
    sys.exit("count block does not carry the 58 count, the 692 → 699 line count, the launch hash, the Group-IV sentence and the stream path")
for k, needs in (("i1", ("3 + 14 names", "sorryAx 0", "ABI v8", "7.0.0-34-generic", "4.33.0-rc2 (d8b18978)", "Mathlib 51e6992e", "12 cores, 37 GB", "Label unchanged.")),
                 ("iv1", ("1 + 1 names", "sorryAx 0", "ABI v8", "7.0.0-34-generic", "4.33.0-rc2 (d8b18978)", "Mathlib 51e6992e", "12 cores, 37 GB", "Label unchanged.")),
                 ("fq10", ("8 names", "sorryAx 0", "ABI v8", "7.0.0-34-generic", "4.33.0-rc2 (d8b18978)", "Mathlib 51e6992e", "`prop45`, `floor_holds_integer`, `floor_fails_anchor`", "Label unchanged.")),
                 ("ii1", ("C₀ = 0.67250…", "C₁ = 0.83625…", "C₂ = (1+2√2+2C₀)/(3+2√2) = 0.88762…", "1 − C₂ < 0.1124", "(2.6)", "(2.7)", "Remark 1.2",
                          "variants of a second-moment argument", "Montgomery–Taylor extremal problem (see Remark 3.4", "github.com/AxiomMath/ZetaZerosV2", "V2-DELTA-s34.md"))):
    for need in needs:
        if need not in blocks[k]:
            sys.exit("block %s does not carry %r" % (k, need))


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
ANCHOR_COUNT = "**Entry count (dated, Session 33, 2026-09-29).** No entry is added. The five lines entered at this stream (the formalization-queue item-10 pair-channel sub-bullet"
PREV_COUNT = "**Entry count (dated, Session 32, 2026-09-29).**"
ANCHOR_I1 = "- **[WITNESSES KERNEL-CHECKED 2026-09-29, Session 32 (`results/i1-witness-lean-s32/`; CHECK-O 97c40eb1…; entered at the Session-32 zoo stream).]**"
PREV_I1 = "- **[RIDER 2026-09-24, Session 24 (digest §C.3 item 8), entered at the Session-25 zoo stream"
PREV2_I1 = "- **[RIDER 2026-09-24, Session 24 (digest §C.3 item 6), entered at the Session-25 zoo stream"
STATUS_I1 = "- **STATUS.** computationally-verified (DH construction, witness values, off-line zero, CCM run — standing-order-5 re-verified). **BINDS: full-RH.**"
NOTE_HEAD = "- **DATED NOTE (2026-09-03, Session 15; single-check — orchestrator's re-derivation, dual-model verification per standing order 7 owed before external use).** "
NOTE_II1 = NOTE_HEAD + "Lamzouri, arXiv:2609.02882 (2 Sep 2026), reproves the AF constants without the matrix"
NOTE_II4 = NOTE_HEAD + "The Hilbert-space form of this degeneracy"
END_II1 = "- **[RIDER 2026-09-26, Session 28 (E1, M5-U formulation slot, `results/e1-m5u/FORMULATION.md` §2–§4; entered at the Session-29 zoo stream)"
END_II4 = "- **[RIDER 2026-09-16, Session 22 — from Theorem M2 clause 7 (`results/c2-m2/separation-note.md` §7.2"
STATUS_II1 = "- **STATUS.** formalized-in-Lean. **BINDS: certificate-class (all scopes).**"
STATUS_II4 = "- **STATUS.** formalized-in-Lean. **BINDS: certificate-class; the S3 clause binds all full-RH routes.**"
DUAL_HEAD = "- **[DUAL-MODEL CHECK 2026-09-05, Session 16 — Opus 5 re-derivation (`results/watch-lamzouri-2609.02882/dual-check-O.md`"
ANCHOR_IV1 = "- **[RIDER 2026-09-29, Session 33 (the s32 digest §D J1 as read, `results/program-digest-s32.md` 565e39bf…; `ranking-read-O.md` M1, M2; entered at the Session-33 zoo stream) — Suzuki 2606.09096, v1 → v3:"
PREV_IV1 = "- **[REFINEMENT 2026-09-29, Session 32 (H5, `results/h5-c2-lean-s32/`; CHECK-O 74b7cfb8…; entered at the Session-32 zoo stream).]**"
PREV2_IV1 = "- **[LINUX REPLAY 2026-09-29, Session 32 (`results/linux-check-s30/`; `results/d5-lean-s30/CHECK-O.md` §12; entered at the Session-32 zoo stream).]**"
PREV3_IV1 = "- **[STATUS RIDER 2026-09-29, Session 30 (D5, `results/d5-lean-s30/`; entered at the Session-31 zoo stream) — formalized-in-Lean.]**"
ANCHOR_FQ10SUB = "    - **[PAIR CHANNEL COMPARATOR-CHECKED 2026-09-29, Session 33 (H4, `results/h4-pair-lean-s33/`; CHECK-O 8e59f36bf2c2bfbf…; entered at the Session-33 zoo stream).]**"
PREV_FQ10SUB = "    - **[LINUX REPLAY 2026-09-29, Session 32 (`results/linux-check-s30/`; `results/iv17-lean-s30/CHECK-O.md` §11; entered at the Session-32 zoo stream).]**"
PREV2_FQ10SUB = "    - **[FORMALIZED AND SHIPPED 2026-09-29, Session 30 — Comparator topic `IntegralityGap`"
PREV3_FQ10SUB = "10. The fractional-mark integrality theorem (IV.17)"
NEXT_FQ10SUB = "11. **Theorem M2's Lemma G"
NEXT2_FQ10SUB = "    - **[PRICED 2026-09-24, Session 24"
# (STATUS_II1 is also II.3's STATUS line, zoo line 163, so it is a neighbor check only, not a global anchor; STATUS_II4 is checked in place too.)
for a in (ANCHOR_COUNT, PREV_COUNT, ANCHOR_I1, PREV_I1, PREV2_I1, STATUS_I1, NOTE_II1, NOTE_II4, END_II1, END_II4, ANCHOR_IV1, PREV_IV1, PREV2_IV1, PREV3_IV1,
          ANCHOR_FQ10SUB, PREV_FQ10SUB, PREV2_FQ10SUB, PREV3_FQ10SUB, NEXT_FQ10SUB):
    n = sum(1 for ln in lines if ln.startswith(a))
    if n != 1:
        sys.exit("the anchor string is not unique in the zoo (%d hits): %r" % (n, a[:100]))
if sum(1 for ln in lines if ln.startswith(NOTE_HEAD)) != 2 or sum(1 for ln in lines if ln.startswith(DUAL_HEAD)) != 2:
    sys.exit("the DATED NOTE head and the DUAL-MODEL CHECK head must each occur exactly twice (II.1 and II.4)")

# 1. Count header: a blank line and the paragraph after the Session-33 count paragraph, before the '---'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_COUNT), "Session-33 count paragraph")
if any(ln.startswith("### ") for ln in lines[:i]):
    sys.exit("the Session-33 count paragraph is not in the header")
if lines[i + 1] != "" or lines[i + 2] != "---":
    sys.exit("the Session-33 count paragraph is not followed by a blank line and '---'")
if not lines[i - 2].startswith(PREV_COUNT) or lines[i - 1] != "":
    sys.exit("the Session-32 count paragraph is not directly above the Session-33 paragraph")
lines[i + 1:i + 1] = ["", blocks["count"]]

# 2. I.1: the LINUX REPLAY line directly after the WITNESSES KERNEL-CHECKED bullet (the entry's last line), before the blank and '### I.2'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_I1), "I.1 WITNESSES KERNEL-CHECKED bullet")
entry_of(lines, i, "### I.1 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### I.2 "):
    sys.exit("I.1's WITNESSES bullet is not the last line before '### I.2'")
if not lines[i - 1].startswith(PREV_I1) or not lines[i - 2].startswith(PREV2_I1) or lines[i - 3] != STATUS_I1:
    sys.exit("I.1's STATUS line and its two Session-24 RIDERs are not the three lines above the anchor")
lines[i + 1:i + 1] = [blocks["i1"]]

# 3. II.1: the rider directly after the DATED NOTE (a paragraph of its own), before the blank and the DUAL-MODEL CHECK bullet.
i = unique_index(lines, lambda ln: ln.startswith(NOTE_II1), "II.1 DATED NOTE (Lamzouri)")
entry_of(lines, i, "### II.1 ")
if lines[i - 1] != "" or lines[i - 2] != STATUS_II1:
    sys.exit("II.1's DATED NOTE is not preceded by a blank line and the entry's STATUS line")
if lines[i + 1] != "" or not lines[i + 2].startswith(DUAL_HEAD):
    sys.exit("II.1's DATED NOTE is not followed by a blank line and the DUAL-MODEL CHECK bullet -- placement not verified")
e = unique_index(lines, lambda ln: ln.startswith(END_II1), "II.1's last line (the Session-28 E1 RIDER)")
entry_of(lines, e, "### II.1 ")
if not (i + 2 < e) or lines[e + 1] != "" or not lines[e + 2].startswith("### II.2 "):
    sys.exit("II.1's Session-28 E1 RIDER is not the entry's last line after the DATED NOTE, before the blank and '### II.2'")
lines[e + 1:e + 1] = [blocks["ii1"]]

# 4. II.4: the same rider directly after the DATED NOTE, before the blank and the DUAL-MODEL CHECK bullet.
i = unique_index(lines, lambda ln: ln.startswith(NOTE_II4), "II.4 DATED NOTE (Hilbert-space form)")
entry_of(lines, i, "### II.4 ")
if lines[i - 1] != "" or lines[i - 2] != STATUS_II4:
    sys.exit("II.4's DATED NOTE is not preceded by a blank line and the entry's STATUS line")
if lines[i + 1] != "" or not lines[i + 2].startswith(DUAL_HEAD):
    sys.exit("II.4's DATED NOTE is not followed by a blank line and the DUAL-MODEL CHECK bullet -- placement not verified")
e = unique_index(lines, lambda ln: ln.startswith(END_II4), "II.4's last line (the Session-22 RIDER)")
entry_of(lines, e, "### II.4 ")
if e != i + 4 or lines[e - 1] != "" or lines[e + 1] != "" or not lines[e + 2].startswith("### II.5 "):
    sys.exit("II.4's Session-22 RIDER is not the entry's last line (note, blank, DUAL-MODEL CHECK, blank, RIDER), before the blank and '### II.5'")
lines[e + 1:e + 1] = [blocks["ii4"]]

# 5. IV.1: the LINUX REPLAY line directly after the entry's last line, the Session-33 Suzuki RIDER (which follows the REFINEMENT anchor), before the blank and '### IV.2'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_IV1), "IV.1 Session-33 Suzuki RIDER (the entry's last line)")
entry_of(lines, i, "### IV.1 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### IV.2 "):
    sys.exit("IV.1's Session-33 RIDER is not the last line before '### IV.2'")
if not lines[i - 1].startswith(PREV_IV1) or not lines[i - 2].startswith(PREV2_IV1) or not lines[i - 3].startswith(PREV3_IV1):
    sys.exit("IV.1's REFINEMENT rider, LINUX REPLAY line and STATUS RIDER are not the three lines above the anchor")
lines[i + 1:i + 1] = [blocks["iv1"]]

# 6. The formalization queue: the item-10 LINUX REPLAY sub-bullet directly after the PAIR CHANNEL sub-bullet, before item 11.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_FQ10SUB), "item 10's PAIR CHANNEL sub-bullet")
entry_of(lines, i, "## Formalization queue")
if not lines[i - 1].startswith(PREV_FQ10SUB) or not lines[i - 2].startswith(PREV2_FQ10SUB) or not lines[i - 3].startswith(PREV3_FQ10SUB):
    sys.exit("item 10, its FORMALIZED AND SHIPPED sub-bullet and its LINUX REPLAY sub-bullet are not the three lines above the PAIR CHANNEL sub-bullet")
if not lines[i + 1].startswith(NEXT_FQ10SUB):
    sys.exit("item 11 is not directly after item 10's PAIR CHANNEL sub-bullet -- placement not verified")
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
if added != 7:
    sys.exit("line arithmetic: added %d, expected 7" % added)
if len(orig) - 1 != 692 or len(lines) - 1 != 699:
    sys.exit("line count is %d -> %d, expected 692 -> 699" % (len(orig) - 1, len(lines) - 1))
for m in set(MARKS):
    want = 2 if m == RIDER_HEAD else 1
    if new_text.count(m) != want:
        sys.exit("marker %r occurs %d times after insertion (expected %d)" % (m[:50], new_text.count(m), want))
for k in NAMES:
    want = 2 if k in ("ii1", "ii4") else 1
    if new_text.count(blocks[k]) != want:
        sys.exit("block %s occurs %d times after insertion (expected %d)" % (k, new_text.count(blocks[k]), want))
if new_text.count(ENTERED) != 5:
    sys.exit("%r must occur exactly five times after insertion (found %d)" % (ENTERED, new_text.count(ENTERED)))

# The numbered formalization-queue list still reads 1-11 in order; the new sub-bullet is indented four spaces at its place.
q = unique_index(lines, lambda ln: ln.startswith("## Formalization queue"), "formalization-queue heading")
qend = q + 1
while qend < len(lines) and not lines[qend].startswith("*(File discipline"):
    qend += 1
numbered = [(j, int(re.match(r"(\d+)\. ", lines[j]).group(1))) for j in range(q, qend) if re.match(r"\d+\. ", lines[j])]
if [n for _, n in numbered] != list(range(1, 12)):
    sys.exit("the formalization queue's numbered items do not read 1-11 in order: %r" % [n for _, n in numbered])
j10 = [j for j, n in numbered if n == 10][0]
j11 = [j for j, n in numbered if n == 11][0]
if j11 != j10 + 5 or not lines[j10 + 1].startswith(PREV2_FQ10SUB) or not lines[j10 + 2].startswith(PREV_FQ10SUB) or not lines[j10 + 3].startswith(ANCHOR_FQ10SUB) or lines[j10 + 4] != blocks["fq10"]:
    sys.exit("item 10 is not followed by its FORMALIZED AND SHIPPED, LINUX REPLAY (s32), PAIR CHANNEL and LINUX REPLAY (s34) sub-bullets, then item 11")
for j in range(q, qend):
    ln = lines[j]
    if ln.startswith(" ") and not (ln.startswith("    - **[") and not ln.startswith("     ")):
        sys.exit("an indented line in the formalization queue is not a four-space sub-bullet: %r" % ln[:60])

# In the 699-line result: the count paragraph at line 35 (33 + 2), '---' at 37; the I.1 line at 72 (69 + 2 + 1); the II.1 rider at
# 145 (141 + 3 + 1); the II.4 rider at 179 (174 + 4 + 1); the IV.1 line at 400 (394 + 5 + 1); the item-10 sub-bullet at 692
# (685 + 6 + 1), item 11 at 693; the file-discipline paragraph at 699.
if lines[34] != blocks["count"] or lines[33] != "" or not lines[32].startswith(ANCHOR_COUNT) or lines[35] != "" or lines[36] != "---":
    sys.exit("the count paragraph is not at line 35 between the Session-33 paragraph and the '---'")
if lines[71] != blocks["i1"] or not lines[70].startswith(ANCHOR_I1) or lines[72] != "" or not lines[73].startswith("### I.2 "):
    sys.exit("the I.1 LINUX REPLAY line is not at line 72 directly after the WITNESSES bullet")
if lines[150] != blocks["ii1"] or not lines[149].startswith(END_II1) or lines[151] != "" or not lines[152].startswith("### II.2 ") or not lines[143].startswith(NOTE_II1):
    sys.exit("the II.1 rider is not at line 151 directly after the entry's last line (the Session-28 E1 RIDER), before '### II.2'")
if lines[182] != blocks["ii4"] or not lines[181].startswith(END_II4) or lines[183] != "" or not lines[184].startswith("### II.5 ") or not lines[177].startswith(NOTE_II4):
    sys.exit("the II.4 rider is not at line 183 directly after the entry's last line (the Session-22 RIDER), before '### II.5'")
if lines[399] != blocks["iv1"] or not lines[398].startswith(ANCHOR_IV1) or lines[400] != "" or not lines[401].startswith("### IV.2 "):
    sys.exit("the IV.1 LINUX REPLAY line is not at line 400 directly after the Session-33 Suzuki RIDER")
if lines[691] != blocks["fq10"] or not lines[690].startswith(ANCHOR_FQ10SUB) or not lines[692].startswith(NEXT_FQ10SUB) or not lines[698].startswith("*(File discipline"):
    sys.exit("the item-10 LINUX REPLAY sub-bullet is not at line 692 between the PAIR CHANNEL sub-bullet (691) and item 11 (693), with the file-discipline paragraph at 699")

out = dry if dry else ZOO
out.write_text(new_text, encoding="utf-8")
print("OK: %s written; +%d lines (692 -> %d); entries 58 (I 8, II 5, III 21, IV 19, V 5); Group IV 19 (no heading added); the six blocks at lines 35, 72, 151, 183, 400, 692; SHA-256 after %s%s"
      % (out, added, len(lines) - 1, hashlib.sha256(new_text.encode("utf-8")).hexdigest(), " [DRY RUN -- BARRIER-ZOO.md untouched]" if dry else ""))
