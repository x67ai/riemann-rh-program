#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 30 zoo stream `zoo-s30` (2026-09-28): insert into BARRIER-ZOO.md four lines, bookkeeping only -- E5's rider
"(ii')" on IV.18 directly after the 2026-09-16 rider (ii) it amends (block iv18: results/e5-kappa-s29/NOTE.md section 7,
line 181, the leading "> " stripped, verbatim modulo exactly the three insertions the brief names -- (a) "(ii)" -> "(ii')"
in the head, (b) the house "entered at" clause after "reader Opus 5 `read-O.md`", (c) the prior-art label before ".]**" --
plus the house bullet marker "- "), the G7 record note directly after it (block iv18note), the III.20 lookup line after
the E3 pointer rider (block iii20), and the count paragraph (block count). No numbered entry: the entry count stays 58
(I 8, II 5, III 21, IV 19, V 5); 667 -> 672 lines (+5: three one-line riders/notes, the count paragraph and the blank
line before it).

Source of every inserted line: results/zoo-s30/zoo-entries-proposed.md, read AT RUN TIME (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->), so the orchestrator's post-reader amendments flow in. Before touching the
zoo the script asserts that BARRIER-ZOO.md has SHA-256 840f4362... (the zoo at brief time) and that NOTE.md has
e4bc9705..., that every anchor occurs exactly once (anchored by the full text of the neighboring lines, never by line
number alone: the head of the 2026-09-16 rider (ii) up to "(Session 22 queue item 4;", the head of the E3 pointer rider
up to "theorems on rung 1.]**", the Session-29 count paragraph's first words -- each asserted unique in the file), that
the line directly after the rider-(ii) anchor begins with the Session-24 rider (i) head "- **[RIDER 2026-09-24, Session
24, entered at the Session-25 zoo stream -- (i) the pole cap" (so the placement is verified, not assumed), that the iv18
body equals NOTE line 181 (stripped) modulo exactly the three named insertions and the bullet marker (the script prints
the differences it allows), and that the A8/A13/A14 NEW strings of results/e5-kappa-s29/read-O.md lines 80-86, 105-109,
111-113 are present and the OLD strings absent (block and record). Pure insertion: no existing line is modified or
removed; iv18 goes directly after the rider-(ii) line and iv18note directly after iv18 (both before the Session-24 rider
(i)); iii20 goes after III.20's last existing bullet, before the blank line that precedes '### III.21'; the count
paragraph goes after the Session-29 count paragraph, before the '---'. The script refuses to run twice. Afterwards it
verifies that every original line survives, in order, as an identical line, that the '### ' count is 58 with per-group
counts 8/5/21/19/5, that the line arithmetic is exact (+5, 667 -> 672), that the file ends with exactly one newline,
and that the inserted text carries none of the linted phrases.

Usage: python3 scripts/zoo-insert-s30.py [--dry-run OUTPATH]
  --dry-run OUTPATH    write the result to OUTPATH and leave BARRIER-ZOO.md untouched (the writer's only mode).
Modeled on scripts/zoo-insert-s29.py.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s30" / "zoo-entries-proposed.md"
NOTE = ROOT / "results" / "e5-kappa-s29" / "NOTE.md"
ZOO_HASH_BEFORE = "840f4362f21e87585b3120ede56e4064f16fd948bff633be5ed169636ba46cf7"
NOTE_HASH = "e4bc9705326a10fb7a142e5f8566377f210f60a7697b06b0322097d047ac07ee"

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
note_bytes = NOTE.read_bytes()
if hashlib.sha256(note_bytes).hexdigest() != NOTE_HASH:
    sys.exit("results/e5-kappa-s29/NOTE.md SHA-256 is not %s -- the E5 record changed; nothing done." % NOTE_HASH[:16])
note_lines = note_bytes.decode("utf-8").split("\n")

MARKS = ("- **[RIDER 2026-09-28, Session 29 — (ii′) the budget-floor constant κ: EXISTENCE CLOSED, VALUE BRACKETED",
         "- **[RECORD NOTE 2026-09-28, Session 30 — the finite-mass sentence of the 2026-09-16 rider (ii) above and Theorem F1(a)",
         "- **[LOOKUP 2026-09-28, Session 30 — the brief-time lookup for item 1 of this entry's EXECUTABLE TEST",
         "**Entry count (dated, Session 30, 2026-09-28).**")
for m in MARKS:
    if m in zoo_text:
        sys.exit("BARRIER-ZOO.md already contains %r -- refusing to insert twice." % m[:70])


def block(text: str, name: str, where: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)), text, re.S)
    if len(ms) != 1:
        sys.exit("block %s occurs %d times in %s (need exactly 1)" % (name, len(ms), where))
    return ms[0]


NAMES = ("count", "iv18", "iv18note", "iii20")
blocks = {k: block(prop_text, k, "the proposed file") for k in NAMES}
for k, v in blocks.items():
    if not v.strip():
        sys.exit("block %s is empty" % k)
    if v.count("\n") != 0:
        sys.exit("block %s must be exactly one line" % k)
    for bad in ("clearly", "obviously", "easy to see", "well known", "well-known"):
        if bad in v.lower():
            sys.exit("block %s contains the linted phrase %r" % (k, bad))
    if v.startswith("### ") or v.startswith("## "):
        sys.exit("block %s would add a heading" % k)
    if v in zoo_text:
        sys.exit("block %s is already in the zoo" % k)

# Shapes of the heads.
for k, head in (("iv18", MARKS[0]), ("iv18note", MARKS[1]), ("iii20", MARKS[2]), ("count", MARKS[3])):
    if not blocks[k].startswith(head):
        sys.exit("block %s must start with %r" % (k, head[:60]))
    if k != "count" and "]**" not in blocks[k]:
        sys.exit("block %s has no house head closing ']**'" % k)

# --- iv18: NOTE line 181 (the "> " stripped) modulo exactly (a), (b), (c) and the house bullet marker "- ". ---
n181 = note_lines[180]
REC_HEAD = "> **[RIDER 2026-09-28, Session 29 — (ii) the budget-floor constant κ: EXISTENCE CLOSED, VALUE BRACKETED (E5, `results/e5-kappa-s29/NOTE.md`; writer Fable 5.1, reader Opus 5 `read-O.md`).]**"
if not n181.startswith(REC_HEAD) or not n181.endswith("Nothing about where ζ's zeros are is touched."):
    sys.exit("NOTE line 181 is not the single blockquoted E5 rider with the expected head and last sentence (the record has moved)")
if len(n181) != 2798:
    sys.exit("NOTE line 181 is %d characters, expected 2798 (the record has moved)" % len(n181))
stripped = n181[2:]
A_OLD, A_NEW = "(ii) the budget-floor constant κ", "(ii′) the budget-floor constant κ"
B_OLD = "reader Opus 5 `read-O.md`)"
B_NEW = "reader Opus 5 `read-O.md`; entered at the Session-30 zoo stream, directly after the 2026-09-16 rider (ii) that it amends)"
LABEL_RE = re.compile(r"that it amends\) (`\[novelty: dual-model check 2026-09-28 — .*?\]`)\.\]\*\*")
if stripped.count(A_OLD) != 1 or stripped.count(B_OLD) != 1:
    sys.exit("NOTE line 181 does not carry the two head insertion points exactly once")
b = blocks["iv18"]
if not b.startswith("- "):
    sys.exit("block iv18 must begin with the house bullet marker '- '")
body = b[2:]
if body.count(A_NEW) != 1 or body.count(A_OLD) != 0:
    sys.exit("block iv18 does not carry the '(ii′)' head exactly once (or still carries '(ii) the budget-floor constant')")
if body.count(B_NEW) != 1 or body.count(B_OLD) != 0:
    sys.exit("block iv18 does not carry the 'entered at the Session-30 zoo stream' clause exactly once")
ms = LABEL_RE.findall(body)
if len(ms) != 1:
    sys.exit("block iv18 does not carry exactly one prior-art label between 'that it amends)' and '.]**'")
label = ms[0]
if "no printed κ" not in label or "Odlyzko" not in label:
    sys.exit("block iv18's prior-art label is malformed (must name 'no printed κ' and Odlyzko)")
rebuilt = body.replace("that it amends) " + label + ".]**", "that it amends).]**").replace(B_NEW, B_OLD).replace(A_NEW, A_OLD)
if rebuilt != stripped:
    sys.exit("block iv18 differs from NOTE line 181 by more than the three named insertions and the bullet marker")
print("NOTE: block iv18 = NOTE line 181 (the '> ' stripped) with the house marker '- ' and exactly three insertions (allowed):\n"
      "   (a) %r -> %r\n   (b) %r -> %r\n   (c) before '.]**', the label: %s" % (A_OLD, A_NEW, B_OLD, B_NEW, label))

# The A8/A13/A14 NEW strings of results/e5-kappa-s29/read-O.md lines 80-86, 105-109, 111-113: NEW present, OLD absent.
A = {
    "A8": ("coarser grids at U = 12–32 give LP values of the same size (κ̃ ≈ 0.0103–0.0108 at ε = 10⁻³); U = 16 (hu 0.02) certifies 1.08·10⁻⁵ and U = 24 (hu 0.04) certifies only after a large repair, neither above U = 8 at the same ε",
           "coarser grids at U = 12–32 give LP values of the same size but fail the pointwise verification"),
    "A13 (head)": ("writer Fable 5.1, reader Opus 5 `read-O.md`", "writer Fable 5.1, reader Opus 5 owed)"),
    "A13 (label)": ("`[re-derived, three-model: orchestrator's pre-derivation, writer's and reader's own scripts]`",
                    "`[re-derived, dual-model: orchestrator's pre-derivation + writer's own script; reader owed]`"),
    "A14": ("with the pointwise positivity verified on disk by two independent verifiers (writer: first-derivative cells; reader: second-derivative cells, own a(τ) and zeros; validated floating point, not interval arithmetic; the reader's verifier also certifies the same certificate without repair, κ ≥ 6.649·10⁻⁵ `[single-model]`);",
            "with the pointwise positivity verified on disk;"),
}
for a, (new, old) in A.items():
    if new not in b or old in b:
        sys.exit("%s: NEW string absent from, or OLD string present in, block iv18" % a)
    if new not in n181 or old in n181:
        sys.exit("%s is not applied in NOTE line 181 itself" % a)
print("OK: A8, A13, A14 NEW strings present, OLD strings absent (block iv18 and NOTE line 181).")

# Labels per the Session-29 reader (standing order 7); the rigor clause; nothing single-check survives in the rider.
for s in ("`[re-derived, three-model: orchestrator's pre-derivation, writer's and reader's own scripts]`",
          "validated floating point, not interval arithmetic", "κ ≥ 6.649·10⁻⁵ `[single-model]`",
          "κ ∈ [6.589e-05, 9.985·10⁻⁴]", "6.3464·10⁻¹⁹", "**route (α) is closed as a competitor**",
          "Nothing about where ζ's zeros are is touched."):
    if s not in b:
        sys.exit("block iv18 lost %r" % s)
if "single-check" in b or "reader owed" in b or "Opus 5 owed" in b:
    sys.exit("block iv18 still carries a single-check / reader-owed clause")
if "58 entries" not in blocks["count"] or "8 + 5 + 21 + 19 + 5 = 58" not in blocks["count"] or "667 → 672" not in blocks["count"]:
    sys.exit("count block does not carry the 58 arithmetic and the 667 → 672 line count")
if "19 no" not in blocks["iii20"] or "1 undecided" not in blocks["iii20"] or "18 no" in blocks["iii20"]:
    sys.exit("block iii20 does not carry the corrected tally '19 no … 1 undecided' (ORCHESTRATOR-NOTES item 1)")
if "two statements" not in blocks["iv18note"] or "F1(a)" not in blocks["iv18note"] or "`results/c2-m5b/FORMULATION.md`" not in blocks["iv18note"]:
    sys.exit("block iv18note does not cite Theorem F1's own file and the two-statements reading")


def unique_index(lines, pred, label: str) -> int:
    hits = [i for i, ln in enumerate(lines) if pred(ln)]
    if len(hits) != 1:
        sys.exit("anchor %r occurs %d times (need exactly 1)" % (label, len(hits)))
    return hits[0]


def entry_of(lines, i: int, heading: str) -> None:
    j = i
    while j >= 0 and not lines[j].startswith("### "):
        j -= 1
    if j < 0 or not lines[j].startswith(heading):
        sys.exit("the anchor at line %d does not belong to %s" % (i + 1, heading.strip()))


orig = zoo_text.split("\n")
lines = list(orig)

# The anchors, by the full text of the neighboring lines (each asserted unique in the file).
ANCHOR_IV18 = "- **[RIDER 2026-09-16, Session 22 — (ii) the budget-floor lemma κ, M1's honest object — OPEN (Session 22 queue item 4;"
NEXT_IV18 = "- **[RIDER 2026-09-24, Session 24, entered at the Session-25 zoo stream — (i) the pole cap"
PREV_IV18 = "- **[RIDER 2026-09-16, Session 22 — (i) the Gevrey-2 edge law, PROVED in M2"
ANCHOR_III20 = "- **[RIDER 2026-09-26, Session 28 (E3, `results/e3-borger-rung1/NOTE.md` §3–§5; entered at the Session-29 zoo stream) — (B) and R-a's sentence are theorems on rung 1.]**"
PREV_III20 = "- **[RIDER 2026-09-25, Session 27 (D2 design-axis scout pair; `results/d2-scout-s26/HARVEST.md` \"Proposed riders\" 1"
ANCHOR_COUNT = "**Entry count (dated, Session 29, 2026-09-28).** No entry is added. The four lines entered at this stream (the IV.10 rider"
PREV_COUNT = "**Entry count (dated, Session 28, 2026-09-26).**"
for a in (ANCHOR_IV18, NEXT_IV18, ANCHOR_III20, ANCHOR_COUNT):
    if zoo_text.count(a) != 1:
        sys.exit("the anchor string is not unique in the zoo (%d hits): %r" % (zoo_text.count(a), a[:100]))

# The two sentences the new rider's "above" refers to must be in the anchor line (stop line (3)).
i527 = unique_index(lines, lambda ln: ln.startswith(ANCHOR_IV18), "IV.18 2026-09-16 rider (ii)")
entry_of(lines, i527, "### IV.18 ")
for s in ("with explicit κ an M1/M3-grade unit (≥ 2 slots, uncertain)",
          "**no finite-mass prime measure and no finite-variation perturbation of the mean zero density can certify any κ > 0** `[the pricing's finding, novelty: single-check]`"):
    if lines[i527].count(s) != 1:
        sys.exit("the rider-(ii) anchor line does not contain %r exactly once -- the new rider's 'above' would dangle" % s[:60])
if not lines[i527 + 1].startswith(NEXT_IV18):
    sys.exit("the line directly after the rider-(ii) anchor does not begin with the Session-24 rider (i) head -- placement not verified")
if not lines[i527 - 1].startswith(PREV_IV18):
    sys.exit("the line directly before the rider-(ii) anchor is not the 2026-09-16 rider (i)")
if not lines[i527 - 2].startswith("- **STATUS.**") or "Does NOT bind:" not in lines[i527 - 2]:
    sys.exit("IV.18's STATUS line with 'Does NOT bind:' is not two lines above the anchor")
# IV.18's STATEMENT (clauses (1)-(7)) and STATUS are read, never edited: assert they are intact in the entry.
seg = []
for ln in lines[i527 - 6:]:
    if ln.startswith("### ") or ln == "---":
        break
    seg.append(ln)
if not any(ln.startswith("- **STATEMENT.**") and "(7) Sharpness:" in ln for ln in seg):
    sys.exit("IV.18's STATEMENT bullet with clause (7) is not in the entry")

# 1. Count header: a blank line and the paragraph after the Session-29 count paragraph, before the '---'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_COUNT), "Session-29 count paragraph")
if any(ln.startswith("### ") for ln in lines[:i]):
    sys.exit("the Session-29 count paragraph is not in the header")
if lines[i + 1] != "" or lines[i + 2] != "---":
    sys.exit("the Session-29 count paragraph is not followed by a blank line and '---'")
if not lines[i - 2].startswith(PREV_COUNT) or lines[i - 1] != "":
    sys.exit("the Session-28 count paragraph is not directly above the Session-29 paragraph")
lines[i + 1:i + 1] = ["", blocks["count"]]

# 2. IV.18: the new rider directly after the 2026-09-16 rider (ii), the record note directly after the rider, both before
#    the Session-24 rider (i).
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_IV18), "IV.18 2026-09-16 rider (ii)")
entry_of(lines, i, "### IV.18 ")
if not lines[i + 1].startswith(NEXT_IV18):
    sys.exit("placement: the Session-24 rider (i) is not directly after the anchor")
lines[i + 1:i + 1] = [blocks["iv18"], blocks["iv18note"]]
if not (lines[i] .startswith(ANCHOR_IV18) and lines[i + 1] == blocks["iv18"] and lines[i + 2] == blocks["iv18note"] and lines[i + 3].startswith(NEXT_IV18)):
    sys.exit("placement check failed after insertion in IV.18")

# 3. III.20: after its last existing bullet (the E3 pointer rider), before the blank line and '### III.21'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_III20), "III.20 E3 pointer rider")
entry_of(lines, i, "### III.20 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### III.21 "):
    sys.exit("III.20's E3 pointer rider is not the last line before '### III.21'")
if not lines[i - 1].startswith(PREV_III20):
    sys.exit("III.20's R-a rider is not directly above the E3 pointer rider")
j = i
while not lines[j].startswith("### III.20 "):
    j -= 1
if not any(ln.startswith("- **EXECUTABLE TEST.**") and "exhibit the doubled object" in ln for ln in lines[j:i]):
    sys.exit("III.20's EXECUTABLE TEST with 'exhibit the doubled object' (item 1) is not in the entry")
lines[i + 1:i + 1] = [blocks["iii20"]]

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
if added != 5:
    sys.exit("line arithmetic: added %d, expected 5" % added)
if len(orig) - 1 != 667 or len(lines) - 1 != 672:
    sys.exit("line count is %d -> %d, expected 667 -> 672" % (len(orig) - 1, len(lines) - 1))
for m in MARKS:
    if new_text.count(m) != 1:
        sys.exit("marker %r occurs %d times after insertion" % (m[:50], new_text.count(m)))
for k in NAMES:
    if new_text.count(blocks[k]) != 1:
        sys.exit("block %s occurs %d times after insertion" % (k, new_text.count(blocks[k])))
# In the 672-line result the rider-(ii) anchor is at line 530 (527 + 2 for the count paragraph and its blank line + 1 for the
# III.20 line), the new rider at 531, the note at 532, the Session-24 rider (i) at 533; the III.20 anchor at 359, the lookup at 360.
if lines[530] != blocks["iv18"] or lines[531] != blocks["iv18note"] or not lines[529].startswith(ANCHOR_IV18) or not lines[532].startswith(NEXT_IV18):
    sys.exit("the new rider is not at line 531 directly after the rider-(ii) anchor (line 530) and before the Session-24 rider (i) (line 533)")
if lines[359] != blocks["iii20"] or not lines[358].startswith(ANCHOR_III20) or lines[360] != "" or not lines[361].startswith("### III.21 "):
    sys.exit("the III.20 lookup line is not at line 360 directly after the E3 pointer rider")

out = dry if dry else ZOO
out.write_text(new_text, encoding="utf-8")
print("OK: %s written; +%d lines (667 -> %d); entries 58 (I 8, II 5, III 21, IV 19, V 5); SHA-256 after %s%s"
      % (out, added, len(lines) - 1, hashlib.sha256(new_text.encode("utf-8")).hexdigest(), " [DRY RUN -- BARRIER-ZOO.md untouched]" if dry else ""))
