#!/usr/bin/env python3
"""Session 27 zoo stream `zoo-s27` (2026-09-25): insert into BARRIER-ZOO.md four dated riders (five rider lines) and
one cross-reference row -- the D3 note's riders on I.5 and IV.4 (blocks i5, iv4: byte-identical copies of the blocks
of results/zoo-s26/zoo-entries-proposed.md), the D2 harvest's rider R-a on III.20 with a one-line pointer on IV.1
(blocks ra, ra_ptr), the D2 harvest's rider R-b' on IV.10 (block rb), and one cross-reference row (block xref).
Riders only: the entry count stays 58 (I 8, II 5, III 21, IV 19, V 5); 649 -> 655 lines.

Source of every inserted line: results/zoo-s27/zoo-entries-proposed.md, read AT RUN TIME (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->), so the orchestrator's post-reader amendments flow in. Before touching
the zoo the script asserts that BARRIER-ZOO.md has SHA-256 576dbd44... (the zoo at brief time), that every anchor
occurs exactly once, and that blocks i5 and iv4 are byte-identical to the s26 blocks. Pure insertion: no existing
line is modified or removed; each rider goes directly after its entry's last existing bullet, before the blank line
that precedes the next heading. The script refuses to run twice. Afterwards it verifies that every original line
survives, in order, as an identical line, that the '### ' count is 58 with per-group counts 8/5/21/19/5, that the
line arithmetic is exact (+6), and that the inserted text carries none of the linted phrases.

Usage: python3 scripts/zoo-insert-s27.py [--dry-run OUTPATH] [--allow-label-flip]
  --dry-run OUTPATH    write the result to OUTPATH and leave BARRIER-ZOO.md untouched (the writer's only mode).
  --allow-label-flip   relax the i5/iv4 byte-identity to identity modulo the packaging-sentence label: the
                       orchestrator flips `[novelty: single-check]` on the packaging sentence to
                       `[dual-model check, <date>: Opus reader, results/zoo-s27/zoo-entries-read-O.md]` after the
                       reader CLOSES (brief, "On completion"); the script then prints the exact difference it allowed.
Modeled on scripts/zoo-insert-s25.py.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s27" / "zoo-entries-proposed.md"
S26 = ROOT / "results" / "zoo-s26" / "zoo-entries-proposed.md"
ZOO_HASH_BEFORE = "576dbd4410ffbb3166c06c38628bf27c487a910dac83295e27cc6a76cd8f8836"
LABEL_OLD = "`[novelty: single-check]` until this stream's Opus reader has read the note."
LABEL_NEW_RE = re.compile(r"`\[dual-model check, \d{4}-\d{2}-\d{2}: Opus reader, results/zoo-s27/zoo-entries-read-O\.md\]`\.")

args = sys.argv[1:]
allow_flip = False
if "--allow-label-flip" in args:
    allow_flip = True
    args.remove("--allow-label-flip")
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
s26_text = S26.read_text(encoding="utf-8")

MARKS = ("- **[RIDER 2026-09-25, Session 26 (D3 note; `results/zoo-s26/d3-mobius-note.md` §1, §3)",
         "- **[RIDER 2026-09-25, Session 26 (D3 note; `results/zoo-s26/d3-mobius-note.md` §2.3, §3)",
         "- **[RIDER 2026-09-25, Session 27 (D2 design-axis scout pair;",
         "| D2 design-axis scout (P1–P9) |")
for m in MARKS:
    if m in zoo_text:
        sys.exit("BARRIER-ZOO.md already contains %r -- refusing to insert twice." % m[:70])


def block(text: str, name: str, where: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)), text, re.S)
    if len(ms) != 1:
        sys.exit("block %s occurs %d times in %s (need exactly 1)" % (name, len(ms), where))
    return ms[0]


NAMES = ("i5", "iv4", "ra", "ra_ptr", "rb", "xref")
blocks = {k: block(prop_text, k, "the proposed file") for k in NAMES}
for k, v in blocks.items():
    if not v.strip():
        sys.exit("block %s is empty" % k)
    for bad in ("clearly", "obviously", "easy to see", "well known", "well-known"):
        if bad in v.lower():
            sys.exit("block %s contains the linted phrase %r" % (k, bad))
    if any(ln.startswith("### ") for ln in v.split("\n")):
        sys.exit("block %s would add a '### ' heading" % k)

# i5 / iv4: byte-identical to the s26 blocks (or identical modulo the flipped packaging label, if allowed).
for k in ("i5", "iv4"):
    ref = block(s26_text, k, "the s26 proposed file")
    if blocks[k] == ref:
        continue
    if not allow_flip:
        sys.exit("block %s is not byte-identical to the s26 block (run with --allow-label-flip only after the reader CLOSES)" % k)
    # Allowed difference: exactly one occurrence of LABEL_OLD in ref replaced by a LABEL_NEW_RE match, at the same position.
    m = LABEL_NEW_RE.search(blocks[k])
    if not m or ref.count(LABEL_OLD) != 1:
        sys.exit("block %s differs from the s26 block by more than the packaging label" % k)
    rebuilt = blocks[k][:m.start()] + LABEL_OLD + blocks[k][m.end():]
    if rebuilt != ref:
        sys.exit("block %s differs from the s26 block by more than the packaging label" % k)
    print("NOTE: block %s differs from the s26 block only by the packaging label: %s -> %s" % (k, LABEL_OLD, m.group(0)))

# Shapes.
for k, head in (("i5", MARKS[0]), ("iv4", MARKS[1]), ("ra", MARKS[2]), ("ra_ptr", MARKS[2]), ("rb", MARKS[2])):
    if blocks[k].count("\n") != 0 or not blocks[k].startswith(head):
        sys.exit("block %s must be one rider line starting with %r" % (k, head[:60]))
if not blocks["ra_ptr"].startswith("- **[RIDER 2026-09-25, Session 27 (D2 design-axis scout pair; `results/d2-scout-s26/HARVEST.md` \"Proposed riders\" 1) — pointer.]**"):
    sys.exit("ra_ptr must be the one-line pointer rider")
if blocks["xref"].count("\n") != 0 or not (blocks["xref"].startswith("| ") and blocks["xref"].endswith(" |")) or blocks["xref"].count("|") != 4:
    sys.exit("xref block must be exactly one table row with three cells")
if not blocks["xref"].startswith(MARKS[3]):
    sys.exit("xref row must start with the D2 casualty cell")


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

# 1. I.5: after its STATUS line, before the blank line and '### I.6'.
i = unique_index(lines, lambda ln: ln.startswith("- **STATUS.** sweep-certified; literature-verified except the Gonek–Ng target (conjectural); the Wintner recalled-flag is **DISCHARGED 2026-08-26**"), "I.5 STATUS")
entry_of(lines, i, "### I.5 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### I.6 "):
    sys.exit("I.5's STATUS line is not the last line before '### I.6'")
lines[i + 1:i + 1] = [blocks["i5"]]

# 2. IV.4: after its STATUS line, before the blank line and '### IV.5'.
i = unique_index(lines, lambda ln: ln == "- **STATUS.** program-adjudicated. **BINDS: certificate-class.**", "IV.4 STATUS")
entry_of(lines, i, "### IV.4 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### IV.5 "):
    sys.exit("IV.4's STATUS line is not the last line before '### IV.5'")
lines[i + 1:i + 1] = [blocks["iv4"]]

# 3. III.20: after its last existing bullet (the 2026-09-16 pointer rider), before the blank line and '### III.21'.
i = unique_index(lines, lambda ln: ln.startswith("- **[RIDER 2026-09-16, Session 22 — pointer.]** The Lorentzian interface's repair takes its coefficients from a doubled object"), "III.20 pointer rider")
entry_of(lines, i, "### III.20 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### III.21 "):
    sys.exit("III.20's 2026-09-16 rider is not the last line before '### III.21'")
if not lines[i - 1].startswith("- **STATUS.** sweep-certified. **BINDS: Track-C/de-novo designs (spec-level).**"):
    sys.exit("III.20's STATUS line is not directly above its 2026-09-16 rider")
lines[i + 1:i + 1] = [blocks["ra"]]

# 4. IV.1: after its STATUS line, before the blank line and '### IV.2'.
i = unique_index(lines, lambda ln: ln == "- **STATUS.** program-adjudicated (computationally verified in C1). **BINDS: all routes.**", "IV.1 STATUS")
entry_of(lines, i, "### IV.1 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### IV.2 "):
    sys.exit("IV.1's STATUS line is not the last line before '### IV.2'")
lines[i + 1:i + 1] = [blocks["ra_ptr"]]

# 5. IV.10: after its STATUS line, before the blank line and '### IV.11'.
i = unique_index(lines, lambda ln: ln.startswith("- **STATUS.** program-adjudicated (computationally re-derived, Session 6). **BINDS: all per-prime-fiber substrate designs.**"), "IV.10 STATUS")
entry_of(lines, i, "### IV.10 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### IV.11 "):
    sys.exit("IV.10's STATUS line is not the last line before '### IV.11'")
lines[i + 1:i + 1] = [blocks["rb"]]

# 6. Cross-reference row: after the W1-26 row (the table's last row).
i = unique_index(lines, lambda ln: ln == "| W1-26 lee-yang | instrument restored, coupling map unspecified (Session 24; pair 2) | III.15, IV.1 |", "xref W1-26 row")
if lines[i + 1] != "" or not lines[i + 2].startswith("**[READ 2026-09-10, Opus 5.]**"):
    sys.exit("the W1-26 row is not the table's last row")
if not lines[i - 1].startswith("| W1-14 lorentzian |"):
    sys.exit("the W1-14 row is not directly above the W1-26 row")
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
if len(lines) - 1 != 655:
    sys.exit("line count is %d, expected 655" % (len(lines) - 1))
for m in MARKS:
    if new_text.count(m) != (3 if m == MARKS[2] else 1):
        sys.exit("marker %r occurs %d times after insertion" % (m[:50], new_text.count(m)))

out = dry if dry else ZOO
out.write_text(new_text, encoding="utf-8")
print("OK: %s written; +%d lines (649 -> %d); entries 58 (I 8, II 5, III 21, IV 19, V 5); SHA-256 after %s%s"
      % (out, added, len(lines) - 1, hashlib.sha256(new_text.encode("utf-8")).hexdigest(), " [DRY RUN -- BARRIER-ZOO.md untouched]" if dry else ""))
