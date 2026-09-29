#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 32 zoo stream `zoo-s32` (2026-09-29): insert into BARRIER-ZOO.md seven lines, bookkeeping only -- the count paragraph
(block count: a blank line and the paragraph directly after the Session-31 count paragraph, before the '---'), the I.1 rider
(block i1: the witness table kernel-checked, I.1's label VERBATIM from results/i1-witness-lean-s32/FIDELITY.md's first paragraph;
a top-level bullet directly after the entry's last bullet, the Session-24 item-8 rider), the two IV.1 lines (block iv1linux, the
Linux replay of D5's topics under a real Landlock sandbox, then block iv1c2, the H5 refinement with H5's label VERBATIM from
results/h5-c2-lean-s32/BUILD-NOTES.md lines 19-21; two top-level bullets directly after the Session-30 STATUS RIDER, in that
order), the V.5 rider (block v5: the Fesenko/IUT omission re-grounded; a top-level bullet directly after the group's last bullet,
the READ line on the SOURCE line, whose head carries a typographic apostrophe), the formalization-queue item-6 sub-bullet (block
fq6: an INDENTED sub-bullet -- exactly four spaces, then "- **[" -- directly after item 6 and before item 7) and the item-10
Linux-replay sub-bullet (block fq10linux: the same indentation, directly after the FORMALIZED AND SHIPPED sub-bullet of item 10
and before item 11). No numbered entry: the entry count stays 58 (I 8, II 5, III 21, IV 19, V 5); 678 -> 686 lines (+8: six
one-line bullets and sub-bullets, the count paragraph and the blank line before it).

Source of every inserted line: results/zoo-s32/zoo-entries-proposed.md, read AT RUN TIME (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->), so the orchestrator's post-reader amendments flow in. Before touching the zoo the
script asserts that BARRIER-ZOO.md has SHA-256 b2036ecb... (the zoo at brief time) and that the two record files carrying the
labels have 85523505... (H5 BUILD-NOTES) and 7630d497... (I.1 FIDELITY); that every anchor occurs exactly once (anchored by the
full text of the neighboring lines, never by line number alone); that the lines around each anchor are what the brief says
(blank + '---' after the count paragraph; blank + '### I.2' after I.1's rider; blank + '### IV.2' after IV.1's STATUS RIDER;
blank + '---' + blank + '## Cross-reference' after V.5's READ line; item 7 after item 6; item 11 and its first sub-bullet after
item 10's sub-bullet), so the placement is verified, not assumed; and that the two labels quoted inside blocks iv1c2 and i1
equal, character for character, the strings pulled from the two record files at run time (the wrapped lines joined with single
spaces; both strings printed on mismatch, and the script refuses). Pure insertion: no existing line is modified or removed.
The script refuses to run twice. Afterwards it verifies that every original line survives, in order, as an identical line,
that the '### ' count is 58 with per-group counts 8/5/21/19/5, that the numbered formalization-queue list still reads 1-11 in
order with the two new sub-bullets indented exactly four spaces (between 6 and 7; between item 10's sub-bullet and 11), that
the line arithmetic is exact (+8, 678 -> 686), that the file ends with exactly one newline, and that the inserted text carries
none of the linted phrases (10(g)) and none of the forbidden sentences.

Usage: python3 scripts/zoo-insert-s32.py [--dry-run OUTPATH]
  --dry-run OUTPATH    write the result to OUTPATH and leave BARRIER-ZOO.md untouched (the writer's only mode).
Modeled on scripts/zoo-insert-s31.py.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s32" / "zoo-entries-proposed.md"
BN_H5 = ROOT / "results" / "h5-c2-lean-s32" / "BUILD-NOTES.md"
FID_I1 = ROOT / "results" / "i1-witness-lean-s32" / "FIDELITY.md"
BN_I1 = ROOT / "results" / "i1-witness-lean-s32" / "BUILD-NOTES.md"
ZOO_HASH_BEFORE = "b2036ecb9b81d6584d3c0ffab12c57ffef87eb17b37aa93726ddeb156bf19991"
BN_H5_HASH = "85523505d2d934d6a50d996b10423521e0174b6b93bf4f4caff257ac2859f05a"
FID_I1_HASH = "7630d497e23a431888114731e9b069738376bb9a38927a10c2bf63ebd50f10f5"

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
for p, h in ((BN_H5, BN_H5_HASH), (FID_I1, FID_I1_HASH)):
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    if got != h:
        sys.exit("%s SHA-256 is %s, expected %s -- the label's record changed; nothing done." % (p.relative_to(ROOT), got, h))

ENTERED = "entered at the Session-32 zoo stream"
MARKS = ("**Entry count (dated, Session 32, 2026-09-29).**",
         "- **[WITNESSES KERNEL-CHECKED 2026-09-29, Session 32 (`results/i1-witness-lean-s32/`; CHECK-O 97c40eb1…; " + ENTERED + ").]**",
         "- **[LINUX REPLAY 2026-09-29, Session 32 (`results/linux-check-s30/`; `results/d5-lean-s30/CHECK-O.md` §12; " + ENTERED + ").]**",
         "- **[REFINEMENT 2026-09-29, Session 32 (H5, `results/h5-c2-lean-s32/`; CHECK-O 74b7cfb8…; " + ENTERED + ").]**",
         "- **[RIDER 2026-09-29, Session 32 (`results/fesenko-pricing-s32/PRICING.md` §2.8, §5; `read-O.md`; " + ENTERED + ") — the Fesenko/IUT omission re-grounded.]**",
         "    - **[WITNESS HALF SHIPPED 2026-09-29, Session 32 — ",
         "    - **[LINUX REPLAY 2026-09-29, Session 32 (`results/linux-check-s30/`; `results/iv17-lean-s30/CHECK-O.md` §11; " + ENTERED + ").]**")
for m in MARKS:
    if m in zoo_text:
        sys.exit("BARRIER-ZOO.md already contains %r -- refusing to insert twice." % m[:70])


def block(text: str, name: str, where: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)), text, re.S)
    if len(ms) != 1:
        sys.exit("block %s occurs %d times in %s (need exactly 1)" % (name, len(ms), where))
    return ms[0]


NAMES = ("count", "i1", "iv1linux", "iv1c2", "v5", "fq6", "fq10linux")
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
for k in ("i1", "iv1linux", "iv1c2", "v5"):
    if not blocks[k].startswith("- **["):
        sys.exit("block %s must be a top-level bullet '- **['" % k)
for k in ("fq6", "fq10linux"):
    if not blocks[k].startswith("    - **[") or blocks[k].startswith("     "):
        sys.exit("block %s must begin with exactly four spaces then '- **[' (item 11's sub-bullets are the precedent)" % k)
    if "\t" in blocks[k][:8]:
        sys.exit("block %s must be indented with spaces, not a tab" % k)

# --- The two labels: pulled from the two record files at run time (wrapped lines joined with single spaces) and compared
#     character for character with the quoted strings in blocks iv1c2 and i1 (standing order 7). ---


def pull_bold_label(path: Path, lo: int, hi: int) -> str:
    seg = " ".join(ln.strip() for ln in path.read_text(encoding="utf-8").split("\n")[lo - 1:hi])
    ms = re.findall(r'\*\*"(.*?)"\*\*', seg)
    if len(ms) != 1:
        sys.exit("%s lines %d-%d do not carry exactly one bold quoted label (found %d); the record has moved" % (path.name, lo, hi, len(ms)))
    return ms[0]


def pull_fidelity_label(path: Path) -> str:
    fl = path.read_text(encoding="utf-8").split("\n")
    starts = [k for k, ln in enumerate(fl) if ln.startswith("**First paragraph, binding")]
    if len(starts) != 1:
        sys.exit("%s does not carry exactly one '**First paragraph, binding' paragraph (found %d)" % (path.name, len(starts)))
    i = starts[0]
    j = i
    while j < len(fl) and fl[j].strip():
        j += 1
    para = " ".join(ln.strip() for ln in fl[i:j])
    ms = re.findall(r'The label the unit earns \(BRIEF §1\(4\)\), verbatim: "(.*?)"\. It is a hardening', para)
    if len(ms) != 1:
        sys.exit("%s first paragraph does not carry exactly one 'verbatim: \"...\"' label (found %d); the record has moved" % (path.name, len(ms)))
    return ms[0]


LABEL_H5 = pull_bold_label(BN_H5, 19, 21)
LABEL_I1 = pull_fidelity_label(FID_I1)
if pull_bold_label(BN_I1, 20, 24) != LABEL_I1:
    sys.exit("I.1's label differs between FIDELITY.md's first paragraph and BUILD-NOTES.md lines 20-24; the record is inconsistent. Refusing.")
for k, lab, intro, src in (("iv1c2", LABEL_H5, 'Label, as the builder and the checker assign it: "', "results/h5-c2-lean-s32/BUILD-NOTES.md lines 19-21"),
                           ("i1", LABEL_I1, 'Label as the builder and the checker assign it: "', "results/i1-witness-lean-s32/FIDELITY.md first paragraph")):
    b = blocks[k]
    if b.count(intro) != 1:
        sys.exit("block %s does not carry the label introduction %r exactly once" % (k, intro))
    quoted = b.split(intro, 1)[1]
    end = quoted.find('"')
    if end < 0:
        sys.exit("block %s: the label's closing straight quote is missing" % k)
    quoted = quoted[:end]
    if quoted != lab:
        sys.exit("block %s: the quoted label differs from the record (%s).\n  RECORD: %r\n  BLOCK:  %r\nRefusing." % (k, src, lab, quoted))
    if b.count('"' + lab + '"') != 1:
        sys.exit("block %s must carry the label in straight double quotes exactly once" % k)
for k in NAMES:
    if k not in ("iv1c2", "i1") and (LABEL_H5 in blocks[k] or LABEL_I1 in blocks[k]):
        sys.exit("block %s carries a label; only iv1c2 and i1 may" % k)
print("OK: the two labels in blocks iv1c2 and i1 equal the strings pulled from the two record files, character for character:\n   H5:  %s\n   I.1: %s" % (LABEL_H5, LABEL_I1))

# Forbidden sentences (never widen; the four units' ledgers and the V.5 pricing read).
for k in NAMES:
    b = blocks[k]
    for forb in ("IV.1's containment inside `EF_lit`", "the tilted test is C²", "DH has no Euler product", "RH-equivalent",
                 "the tilted explicit formula is formalized", "kernel-checked on Prove2Me"):
        if forb in b:
            sys.exit("block %s carries the forbidden sentence %r" % (k, forb))
    if re.search(r"(?<![A-Z])I\.1 formalized(?!-)", b):
        sys.exit("block %s carries the forbidden sentence 'I.1 formalized'" % k)

# Content sentinels per block (the brief's "What enters").
if "58 entries" not in blocks["count"] or "678 → 686" not in blocks["count"] or "b2036ecb" not in blocks["count"] or "I: 8, II: 5, III: 21, IV: 19, V: 5" not in blocks["count"]:
    sys.exit("count block does not carry the 58 count, the 678 → 686 line count and the launch hash")
if "Λ_Q(36) = −4 log 2 − 4 log 3 < 0" not in blocks["i1"] or "Λ_DH(12) = −κ(1 + κ²) log 12 < 0" not in blocks["i1"] or "`lambdaVec_rec`" not in blocks["i1"] or "97c40eb1" not in blocks["i1"]:
    sys.exit("block i1 does not carry the two witness values, lambdaVec_rec and the CHECK-O hash")
if "1 + 12 names" not in blocks["iv1linux"] or "Landlock" not in blocks["iv1linux"] or "ABI v8" not in blocks["iv1linux"] or "§12" not in blocks["iv1linux"]:
    sys.exit("block iv1linux does not carry the 1 + 12 names, the Landlock sandbox and the §12 pointer")
if "`weilContainment_c2_interpolant`" not in blocks["iv1c2"] or "74b7cfb8" not in blocks["iv1c2"] or "`weilContainment_not_contDiff`" not in blocks["iv1c2"] or "`EF_lit` not stated" not in blocks["iv1c2"]:
    sys.exit("block iv1c2 does not name the theorem, the CHECK-O hash, the (N2) instance and the EF_lit clause")
if "bracketed by RH" not in blocks["v5"] or "unswept_corners[11]" not in blocks["v5"] or "(p. 80)" not in blocks["v5"] or "(p. 81)" not in blocks["v5"] or "III.20's test returns it to IV.1" not in blocks["v5"]:
    sys.exit("block v5 does not carry the bracket, the sweep pointer, the page citations and the routing sentence")
if len(blocks["v5"].split()) > 120:
    sys.exit("block v5 is %d words by wc -w, more than the 120 the brief allows" % len(blocks["v5"].split()))
if "the exact witnesses are Lean theorems" not in blocks["fq6"] or "axiom-format statement remains unformalized" not in blocks["fq6"]:
    sys.exit("block fq6 does not carry the witness half / axiom-format half sentence")
if "16 names" not in blocks["fq10linux"] or "§11" not in blocks["fq10linux"] or "the pair channel unformalized" not in blocks["fq10linux"] or "`IntegralityGap`" not in blocks["fq10linux"]:
    sys.exit("block fq10linux does not carry the 16 names, the §11 pointer, the topic and the pair-channel sentence")


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
ANCHOR_COUNT = "**Entry count (dated, Session 31, 2026-09-29).** No entry is added. The five lines entered at this stream (the IV.1 STATUS rider"
PREV_COUNT = "**Entry count (dated, Session 30, 2026-09-28).**"
ANCHOR_I1 = "- **[RIDER 2026-09-24, Session 24 (digest §C.3 item 8), entered at the Session-25 zoo stream — Theorem M2's restricted"
PREV_I1 = "- **[RIDER 2026-09-24, Session 24 (digest §C.3 item 6), entered at the Session-25 zoo stream — the DH coefficient-support theorem"
STATUS_I1 = "- **STATUS.** computationally-verified (DH construction, witness values, off-line zero, CCM run — standing-order-5 re-verified). **BINDS: full-RH.**"
ANCHOR_IV1 = "- **[STATUS RIDER 2026-09-29, Session 30 (D5, `results/d5-lean-s30/`; entered at the Session-31 zoo stream) — formalized-in-Lean.]**"
PREV_IV1 = "- **[RIDER 2026-09-25, Session 27 (D2 design-axis scout pair; `results/d2-scout-s26/HARVEST.md` \"Proposed riders\" 1) — pointer.]**"
STATUS_IV1 = "- **STATUS.** program-adjudicated (computationally verified in C1). **BINDS: all routes.**"
ANCHOR_V5 = "- **[READ 2026-09-16, Opus 5: the SOURCE line’s split description is REPAIRED.]**"
PREV_V5 = "- **[READ 2026-09-16, Opus 5: one clause of the SIGNATURE line is REPAIRED.]**"
STATUS_V5 = "- **STATUS.** program rule (process barrier, in the vocabulary of V.1–V.4; extracted from an AUDIT finding, not from a kill)."
NEXT4_V5 = "## Cross-reference: program casualties → barriers that killed them"
ANCHOR_FQ6 = "6. DH/Epstein \"no polarized Frobenius system\" lemma (III.21 rider)"
NEXT_FQ6 = "7. Converse-theorem-form DH-exclusion via Blomer–Leung (I.1 rider)"
PREV_FQ6 = "5. \"Scalar divergent-cutoff cubic rows are unconditionally absorbed\" (IV.7)"
ANCHOR_FQ10SUB = "    - **[FORMALIZED AND SHIPPED 2026-09-29, Session 30 — Comparator topic `IntegralityGap` (`results/iv17-lean-s30/`; entered at the Session-31 zoo stream).]**"
PREV_FQ10SUB = "10. The fractional-mark integrality theorem (IV.17)"
NEXT_FQ10SUB = "11. **Theorem M2's Lemma G"
NEXT2_FQ10SUB = "    - **[PRICED 2026-09-24, Session 24"
ROUTING_III20 = "A brief with the generator acting on the un-doubled EF is returned as Weil-positivity-in-disguise (IV.1)."
for a in (ANCHOR_COUNT, ANCHOR_I1, PREV_I1, ANCHOR_IV1, PREV_IV1, ANCHOR_V5, PREV_V5, ANCHOR_FQ6, NEXT_FQ6, ANCHOR_FQ10SUB, PREV_FQ10SUB, NEXT_FQ10SUB, NEXT4_V5):
    n = sum(1 for ln in lines if ln.startswith(a))
    if n != 1:
        sys.exit("the anchor string is not unique in the zoo (%d hits): %r" % (n, a[:100]))
if sum(1 for ln in lines if ROUTING_III20 in ln) != 1:
    sys.exit("III.20's routing sentence (the one block v5 cites) does not occur exactly once")

# 1. Count header: a blank line and the paragraph after the Session-31 count paragraph, before the '---'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_COUNT), "Session-31 count paragraph")
if any(ln.startswith("### ") for ln in lines[:i]):
    sys.exit("the Session-31 count paragraph is not in the header")
if lines[i + 1] != "" or lines[i + 2] != "---":
    sys.exit("the Session-31 count paragraph is not followed by a blank line and '---'")
if not lines[i - 2].startswith(PREV_COUNT) or lines[i - 1] != "":
    sys.exit("the Session-30 count paragraph is not directly above the Session-31 paragraph")
lines[i + 1:i + 1] = ["", blocks["count"]]

# 2. I.1: the rider directly after the Session-24 item-8 rider (the entry's last bullet), before the blank and '### I.2'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_I1), "I.1 Session-24 item-8 rider")
entry_of(lines, i, "### I.1 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### I.2 "):
    sys.exit("I.1's Session-24 item-8 rider is not the last line before '### I.2'")
if not lines[i - 1].startswith(PREV_I1) or lines[i - 2] != STATUS_I1:
    sys.exit("I.1's item-6 rider and STATUS line are not the two lines above the anchor")
seg = lines[i - 7:i - 1]
if not (seg[0].startswith("- **STATEMENT.**") and seg[1].startswith("- **KILLS.**") and seg[2].startswith("- **THE CCM CASE STUDY")
        and seg[3].startswith("- **EXECUTABLE TEST.**") and seg[4].startswith("- **SOURCE.**") and seg[5] == STATUS_I1):
    sys.exit("I.1's six bullets STATEMENT / KILLS / CCM / EXECUTABLE TEST / SOURCE / STATUS are not the six lines above the two riders")
lines[i + 1:i + 1] = [blocks["i1"]]

# 3. IV.1: the Linux line, then the H5 rider, directly after the Session-30 STATUS RIDER (the entry's last bullet), before the blank and '### IV.2'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_IV1), "IV.1 Session-30 STATUS RIDER")
entry_of(lines, i, "### IV.1 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### IV.2 "):
    sys.exit("IV.1's STATUS RIDER is not the last line before '### IV.2'")
if not lines[i - 1].startswith(PREV_IV1) or lines[i - 2] != STATUS_IV1:
    sys.exit("IV.1's Session-27 pointer rider and STATUS line ('BINDS: all routes') are not the two lines above the anchor")
seg = lines[i - 6:i - 1]
if not (seg[0].startswith("- **STATEMENT.**") and seg[1].startswith("- **KILLS.**") and seg[2].startswith("- **EXECUTABLE TEST.**")
        and seg[3].startswith("- **SOURCE.**") and seg[4] == STATUS_IV1):
    sys.exit("IV.1's five bullets STATEMENT / KILLS / EXECUTABLE TEST / SOURCE / STATUS are not the five lines above the pointer rider")
lines[i + 1:i + 1] = [blocks["iv1linux"], blocks["iv1c2"]]

# 4. V.5: the rider directly after the READ line on the SOURCE line (the group's last bullet), before blank / '---' / blank / the cross-reference heading.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_V5), "V.5 READ line on the SOURCE line")
entry_of(lines, i, "### V.5 ")
if lines[i + 1] != "" or lines[i + 2] != "---" or lines[i + 3] != "" or not lines[i + 4].startswith(NEXT4_V5):
    sys.exit("V.5's READ line is not followed by blank / '---' / blank / the cross-reference heading")
if not lines[i - 1].startswith(PREV_V5) or not lines[i - 2].startswith(STATUS_V5):
    sys.exit("V.5's SIGNATURE READ line and STATUS line are not the two lines above the anchor")
seg = lines[i - 8:i - 2]
if not (seg[0].startswith("- **STATEMENT.**") and seg[1].startswith("- **THE DISTINCTION THIS RULE TURNS ON.**") and seg[2].startswith("- **THE SIGNATURE TO MATCH")
        and seg[3].startswith("- **EXECUTABLE TEST.**") and seg[4].startswith("- **WHAT THIS RULE DOES NOT SAY.**") and seg[5].startswith("- **SOURCE.**")):
    sys.exit("V.5's bullets STATEMENT / DISTINCTION / SIGNATURE / EXECUTABLE TEST / WHAT THIS RULE DOES NOT SAY / SOURCE are not the six lines above the STATUS line")
lines[i + 1:i + 1] = [blocks["v5"]]

# 5. The formalization queue: the item-6 sub-bullet directly after item 6, before item 7 (line 666 itself untouched).
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_FQ6), "formalization-queue item 6")
entry_of(lines, i, "## Formalization queue")
if not lines[i + 1].startswith(NEXT_FQ6):
    sys.exit("item 7 is not directly after item 6 -- placement not verified")
if not lines[i - 1].startswith(PREV_FQ6):
    sys.exit("item 5 is not directly above item 6")
if "the exact witnesses (Λ_DH(3), Λ_DH(4), Λ_DH(6), Λ_DH(12); Epstein Λ_Q(6) = 2log6, Λ_Q(36) = −4log6)" not in lines[i]:
    sys.exit("item 6 does not print the six exact witnesses the sub-bullet dates shipped")
lines[i + 1:i + 1] = [blocks["fq6"]]

# 6. The formalization queue: the item-10 Linux sub-bullet directly after the FORMALIZED AND SHIPPED sub-bullet, before item 11.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_FQ10SUB), "item 10's FORMALIZED AND SHIPPED sub-bullet")
entry_of(lines, i, "## Formalization queue")
if not lines[i - 1].startswith(PREV_FQ10SUB):
    sys.exit("item 10 is not directly above its FORMALIZED AND SHIPPED sub-bullet")
if not lines[i + 1].startswith(NEXT_FQ10SUB):
    sys.exit("item 11 is not directly after item 10's sub-bullet -- placement not verified")
if not lines[i + 2].startswith(NEXT2_FQ10SUB):
    sys.exit("item 11's first sub-bullet is not directly after item 11")
for j in range(i + 2, i + 6):
    if not (lines[j].startswith("    - **[") and not lines[j].startswith("     ")):
        sys.exit("item 11's sub-bullet at line %d is not indented exactly four spaces -- the precedent has moved" % (j + 1))
lines[i + 1:i + 1] = [blocks["fq10linux"]]

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
if added != 8:
    sys.exit("line arithmetic: added %d, expected 8" % added)
if len(orig) - 1 != 678 or len(lines) - 1 != 686:
    sys.exit("line count is %d -> %d, expected 678 -> 686" % (len(orig) - 1, len(lines) - 1))
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
j6 = [j for j, n in numbered if n == 6][0]
j7 = [j for j, n in numbered if n == 7][0]
if j7 != j6 + 2 or lines[j6 + 1] != blocks["fq6"]:
    sys.exit("the item-6 sub-bullet is not the single four-space-indented line between items 6 and 7")
j10 = [j for j, n in numbered if n == 10][0]
j11 = [j for j, n in numbered if n == 11][0]
if j11 != j10 + 3 or not lines[j10 + 1].startswith(ANCHOR_FQ10SUB) or lines[j10 + 2] != blocks["fq10linux"]:
    sys.exit("item 10 is not followed by its FORMALIZED AND SHIPPED sub-bullet, then the Linux sub-bullet, then item 11")
for j in range(q, qend):
    ln = lines[j]
    if ln.startswith(" ") and not (ln.startswith("    - **[") and not ln.startswith("     ")):
        sys.exit("an indented line in the formalization queue is not a four-space sub-bullet: %r" % ln[:60])

# In the 686-line result: the count paragraph at line 31 (29 + 2), '---' at 33; the I.1 rider at 67 (64 + 2 + 1); the IV.1 lines
# at 389-390 (385 + 3 + 1, + 1); the V.5 rider at 625 (619 + 5 + 1); the item-6 sub-bullet at 673 (666 + 6 + 1), item 7 at 674;
# the item-10 Linux sub-bullet at 679 (671 + 7 + 1), item 11 at 680; the file-discipline paragraph at 686.
if lines[30] != blocks["count"] or lines[29] != "" or not lines[28].startswith(ANCHOR_COUNT) or lines[31] != "" or lines[32] != "---":
    sys.exit("the count paragraph is not at line 31 between the Session-31 paragraph and the '---'")
if lines[66] != blocks["i1"] or not lines[65].startswith(ANCHOR_I1) or lines[67] != "" or not lines[68].startswith("### I.2 "):
    sys.exit("the I.1 rider is not at line 67 directly after the Session-24 item-8 rider")
if lines[388] != blocks["iv1linux"] or lines[389] != blocks["iv1c2"] or not lines[387].startswith(ANCHOR_IV1) or lines[390] != "" or not lines[391].startswith("### IV.2 "):
    sys.exit("the IV.1 lines are not at 389-390 directly after the Session-30 STATUS RIDER")
if lines[624] != blocks["v5"] or not lines[623].startswith(ANCHOR_V5) or lines[625] != "" or lines[626] != "---" or lines[627] != "" or not lines[628].startswith(NEXT4_V5):
    sys.exit("the V.5 rider is not at line 625 directly after the READ line")
if lines[672] != blocks["fq6"] or not lines[671].startswith(ANCHOR_FQ6) or not lines[673].startswith(NEXT_FQ6):
    sys.exit("the item-6 sub-bullet is not at line 673 between item 6 (672) and item 7 (674)")
if lines[678] != blocks["fq10linux"] or not lines[677].startswith(ANCHOR_FQ10SUB) or not lines[679].startswith(NEXT_FQ10SUB) or not lines[685].startswith("*(File discipline"):
    sys.exit("the item-10 Linux sub-bullet is not at line 679 between item 10's sub-bullet (678) and item 11 (680), with the file-discipline paragraph at 686")

out = dry if dry else ZOO
out.write_text(new_text, encoding="utf-8")
print("OK: %s written; +%d lines (678 -> %d); entries 58 (I 8, II 5, III 21, IV 19, V 5); SHA-256 after %s%s"
      % (out, added, len(lines) - 1, hashlib.sha256(new_text.encode("utf-8")).hexdigest(), " [DRY RUN -- BARRIER-ZOO.md untouched]" if dry else ""))
