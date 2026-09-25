#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 28 zoo stream `zoo-s28` (2026-09-26): insert into BARRIER-ZOO.md six lines, bookkeeping only -- the three
riders of the D1(b) FORMULATION slot in their reader-amended text (block iv7: rider 1 = Theorem F1 on IV.7 beside rider
B, with the equality-rows SCOPE sentence; block ii1: the II.1 rider; block i3: the I.3 pointer), the III.2 attribution
correction (block iii2), the IV.19 cost-line precision read (block iv19), and the count paragraph (block count).
No numbered entry: the entry count stays 58 (I 8, II 5, III 21, IV 19, V 5); 655 -> 662 lines (+7: the count
paragraph takes a blank line before it).

Source of every inserted line: results/zoo-s28/zoo-entries-proposed.md, read AT RUN TIME (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->), so the orchestrator's post-reader amendments flow in. Before touching
the zoo the script asserts that BARRIER-ZOO.md has SHA-256 ba6c7aec... (the zoo at brief time), that every anchor
occurs exactly once (anchored by the full text of the neighboring lines, never by line number alone), that the
bodies of blocks i3 and ii1 are byte-identical to the bodies of results/c2-m5b/zoo-entries-proposed.md (705caf36...)
after the head, and that the body of iv7 equals that file's body after the head with exactly the brief's scope merge
(the script prints every head difference and the scope difference it allows), and that the Z-1 ... Z-5 NEW strings
of results/c2-m5b/read-O.md section 9 are present and the OLD strings absent. Pure insertion: no existing line is
modified or removed; each rider goes directly after its entry's last existing bullet, before the blank line that
precedes the next heading; the count paragraph goes after the Session-25 count paragraph, before the '---'. The
script refuses to run twice. Afterwards it verifies that every original line survives, in order, as an identical
line, that the '### ' count is 58 with per-group counts 8/5/21/19/5, that the line arithmetic is exact (+7,
655 -> 662), that the file ends with exactly one newline, and that the inserted text carries none of the linted
phrases.

Usage: python3 scripts/zoo-insert-s28.py [--dry-run OUTPATH]
  --dry-run OUTPATH    write the result to OUTPATH and leave BARRIER-ZOO.md untouched (the writer's only mode).
Modeled on scripts/zoo-insert-s27.py.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s28" / "zoo-entries-proposed.md"
C2 = ROOT / "results" / "c2-m5b" / "zoo-entries-proposed.md"
ZOO_HASH_BEFORE = "ba6c7aec0ad63cdb703b7108318a77f227361968eb4829cad99dcd23628ef8aa"
C2_HASH = "705caf361dd42c7c65a215c364878e51d248af6944457a8f39134ef9b7277f72"

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
c2_bytes = C2.read_bytes()
if hashlib.sha256(c2_bytes).hexdigest() != C2_HASH:
    sys.exit("results/c2-m5b/zoo-entries-proposed.md SHA-256 is not %s -- the C2 record changed; nothing done." % C2_HASH[:16])
c2_text = c2_bytes.decode("utf-8")

MARKS = ("- **[RIDER 1 2026-09-25, Session 27 (D1(b) FORMULATION slot",
         "- **[RIDER 2026-09-25, Session 27 (D1(b) FORMULATION slot",
         "- **[POINTER 2026-09-25, Session 27 (D1(b) FORMULATION slot",
         "- **[RECORD CORRECTION 2026-09-26, Session 28 (",
         "- **[PRECISION READ 2026-09-26, Session 28 (",
         "**Entry count (dated, Session 28, 2026-09-26).**")
for m in MARKS:
    if m in zoo_text:
        sys.exit("BARRIER-ZOO.md already contains %r -- refusing to insert twice." % m[:70])


def block(text: str, name: str, where: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)), text, re.S)
    if len(ms) != 1:
        sys.exit("block %s occurs %d times in %s (need exactly 1)" % (name, len(ms), where))
    return ms[0]


NAMES = ("count", "i3", "ii1", "iii2", "iv7", "iv19")
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

# Shapes of the heads.
for k, head in (("iv7", MARKS[0]), ("ii1", MARKS[1]), ("i3", MARKS[2]), ("iii2", MARKS[3]), ("iv19", MARKS[4]), ("count", MARKS[5])):
    if not blocks[k].startswith(head):
        sys.exit("block %s must start with %r" % (k, head[:60]))
    if k != "count" and "]**" not in blocks[k]:
        sys.exit("block %s has no house head closing ']**'" % k)


def split_head(line: str):
    i = line.index("]**") + 3
    return line[:i], line[i:]


# The three C2 blocks: bodies identical to the C2 record's bodies modulo the head (iv7: plus exactly the scope merge).
c2_lines = c2_text.split("\n")
c2_riders = [ln for ln in c2_lines if ln.startswith("- **[RIDER Fri Sep 25 21:56:57 IST 2026, Session 27 (D1(b) FORMULATION slot")
             or ln.startswith("- **[POINTER Fri Sep 25 21:56:57 IST 2026, Session 27 (D1(b) FORMULATION slot")]
if len(c2_riders) != 3:
    sys.exit("expected exactly 3 rider/pointer lines in the C2 record, found %d" % len(c2_riders))
c2_map = {}
for ln in c2_riders:
    h, b = split_head(ln)
    if "§1 Theorem F1" in h:
        c2_map["iv7"] = (h, b)
    elif "§0.3 eq. (0.5)" in h:
        c2_map["ii1"] = (h, b)
    elif "§4.3" in h:
        c2_map["i3"] = (h, b)
if sorted(c2_map) != ["i3", "ii1", "iv7"]:
    sys.exit("could not identify the three C2 riders by their heads: %r" % sorted(c2_map))

OLD_TAIL = ("Executable test: any brief proposing a finite or windowed configuration program with explicit-formula EQUALITY rows is returned by (a)–(b) before design cost; "
            "inequality (cone) rows on finite configurations are not excluded by this rider (they are IV.18's and PRICING §1.2's business). Logged numbers")
SCOPE_RE = re.compile(r"Scope, as rider B's: first-order EQUALITY rows with a free positive prime datum — .*? inequality \(cone\) rows on finite configurations are not excluded by this rider — they are IV\.18's and PRICING §1\.2's business\. ")
NEW_TEST = "Executable test: any brief proposing a finite or windowed configuration program with explicit-formula EQUALITY rows is returned by (a)–(b) before design cost. Logged numbers"

for k in ("i3", "ii1", "iv7"):
    new_head, new_body = split_head(blocks[k])
    c2_head, c2_body = c2_map[k]
    print("NOTE: block %s head differs from the C2 record's head (allowed):\n   C2: %s\n  NEW: %s" % (k, c2_head, new_head))
    if k != "iv7":
        if new_body != c2_body:
            sys.exit("block %s body is not byte-identical to the C2 record's body after the head" % k)
        continue
    # iv7: the C2 body with exactly the scope merge -- the SCOPE sentence inserted before "Executable test:" and the
    # inequality clause removed from the test sentence (carried inside the scope sentence).
    if c2_body.count(OLD_TAIL) != 1:
        sys.exit("the C2 record's rider-1 body does not contain the expected executable-test tail exactly once")
    m = SCOPE_RE.search(new_body)
    if not m or new_body.count(NEW_TEST) != 1:
        sys.exit("block iv7 does not carry the SCOPE sentence before the shortened executable test")
    scope = m.group(0)
    rebuilt = new_body.replace(scope + NEW_TEST, OLD_TAIL)
    if rebuilt != c2_body:
        sys.exit("block iv7 differs from the C2 record's body by more than the scope merge")
    print("NOTE: block iv7 body differs from the C2 record's body only by the scope merge (allowed):\n   OLD: %s\n   NEW: %s%s" % (OLD_TAIL, scope, NEW_TEST))

# The Z strings of read-O section 9: NEW present, OLD absent (in the blocks and in the C2 record).
Z = {
    "Z-1": ("best-found relative residual (upper bounds on the infimum; below the count optimizer-limited — the Opus reader's fits reach 1.5·10⁻¹² and 2.1·10⁻¹² at L = 0.5 and 1)",
            "best relative residual 1.2", "iv7"),
    "Z-2": ("every transform of the configuration windowed at height T by a band-limited taper w (ŵ ∈ C_c^∞(−ε, ε), w_T(τ) = w(τ − T)) is, at |u| ≤ L − ε, EXACTLY (2π)⁻¹F_π ∗ ŵ_T",
            "the windowed transform on [T, T + W] is ĉ_{T,W}", "ii1"),
    "Z-3": ("C_X = ∞ on every closed set containing ζ's zeros (their maximal gap tends to 0, Bombieri 2000 p. 225).",
            "C_X = ∞ for supports of RvM density.", "ii1"),
    "Z-4": ("whose nearest printed neighbors are Bombieri 2000 p. 224 (two Dirichlet L-functions of the same modulus and parity: their zero sets have identical explicit-formula data for tests supported in (1/p₀, p₀) — a spectral-gap difference of two infinite zero configurations, for complex, non-positive data) and p. 225 (Bourgain: linear relations over intervals of arbitrary length, from gaps → 0); for positive integer-atomic measures nothing is printed in the sources opened.",
            "on which nothing is printed.", "ii1"),
    "Z-5": ("Its configurations are subsets of a random translate of ½ℤ in unfolded coordinates (stationary, density 1; their Theorem 4.7, p. 9): they are neither N-periodic (so IV.7 rider B does not apply to them as stated) nor of Riemann–von Mangoldt density, and whether an AH-type configuration at the true density can satisfy first-order equality rows at bandwidth L is not decided (by count it cannot be excluded at α < ½). The pointer records the data-class distinction only.",
            "A configuration on a translate of ½ℤ has a lattice comb as its transform", "i3"),
}
for z, (new, old, k) in Z.items():
    if new not in blocks[k]:
        sys.exit("%s NEW string absent from block %s" % (z, k))
    if old in blocks[k]:
        sys.exit("%s OLD string present in block %s" % (z, k))
    if new not in c2_text or old in c2_text:
        sys.exit("%s is not applied in the C2 record itself" % z)
print("OK: Z-1 ... Z-5 NEW strings present, OLD strings absent (blocks and the C2 record).")

# Labels per read-O section 12.
if "`[novelty: dual-model check 2026-09-25]`" not in split_head(blocks["iv7"])[0]:
    sys.exit("iv7 head lacks the read-O §12 label")
if "[novelty: single-check]" in blocks["iv7"] or "until the reader" in blocks["iv7"]:
    sys.exit("iv7 still carries the single-check / until-the-reader clause")
if "`[printed: Lagarias–Rodgers 2020 = `fetched/w-09`, Theorem 2.4 p. 3, §3 p. 4, Theorem 4.7 p. 9]`" not in split_head(blocks["i3"])[0]:
    sys.exit("i3 head lacks the read-O §12 row-6 label")
if "[novelty: single-check]" in blocks["ii1"] or "[novelty: single-check]" in blocks["i3"]:
    sys.exit("a single-check label survives in ii1 / i3")
if "58 entries" not in blocks["count"] or "8 + 5 + 21 + 19 + 5 = 58" not in blocks["count"]:
    sys.exit("count block does not carry the 58 arithmetic")


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

# 1. Count header: a blank line and the paragraph after the Session-25 count paragraph, before the '---'.
i = unique_index(lines, lambda ln: ln.startswith("**Entry count (dated, Session 25, 2026-09-24).** I.8 (the Siegel-zero world"), "Session-25 count paragraph")
if any(ln.startswith("### ") for ln in lines[:i]):
    sys.exit("the Session-25 count paragraph is not in the header")
if lines[i + 1] != "" or lines[i + 2] != "---":
    sys.exit("the Session-25 count paragraph is not followed by a blank line and '---'")
if not lines[i - 2].startswith("**Entry count (dated, Session 23, 2026-09-17).**") or lines[i - 1] != "":
    sys.exit("the Session-23 count paragraph is not directly above the Session-25 paragraph")
lines[i + 1:i + 1] = ["", blocks["count"]]

# 2. I.3: after its STATUS line, before the blank line and '### I.4'.
i = unique_index(lines, lambda ln: ln.startswith("- **STATUS.** formalized-in-Lean (256 law + stability bound, modulo EnclOK interval-arithmetic enclosures); literature-verified (AH)."), "I.3 STATUS")
entry_of(lines, i, "### I.3 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### I.4 "):
    sys.exit("I.3's STATUS line is not the last line before '### I.4'")
lines[i + 1:i + 1] = [blocks["i3"]]

# 3. II.1: after its last existing bullet (the 2026-09-10 READ line), before the blank line and '### II.2'.
i = unique_index(lines, lambda ln: ln.startswith("- **[READ 2026-09-10, Opus 5: the pointer above is CONFIRMED, and its \"until the Opus reader's check\" clause is discharged.]**"), "II.1 READ line")
entry_of(lines, i, "### II.1 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### II.2 "):
    sys.exit("II.1's READ line is not the last line before '### II.2'")
if not lines[i - 1].startswith("- **[POINTER 2026-09-10, Session 21.]** Periodic configuration LPs of this ceiling's template"):
    sys.exit("II.1's 2026-09-10 pointer is not directly above its READ line")
lines[i + 1:i + 1] = [blocks["ii1"]]

# 4. III.2: after its STATUS line, before the blank line and '### III.3'.
i = unique_index(lines, lambda ln: ln == "- **STATUS.** literature-verified. **BINDS: full-RH** (and any evidence claim from small-support numerics).", "III.2 STATUS")
entry_of(lines, i, "### III.2 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### III.3 "):
    sys.exit("III.2's STATUS line is not the last line before '### III.3'")
if not lines[i - 4].startswith("- **STATEMENT.** Weil-positivity is UNCONDITIONAL for test functions of small support, and genuine negativity appears once support reaches (1/p, p) (Bombieri, Lincei 2000;"):
    sys.exit("III.2's STATEMENT (the line the correction addresses) is not four lines above its STATUS line")
lines[i + 1:i + 1] = [blocks["iii2"]]

# 5. IV.7: after its last existing bullet (the 2026-09-10 READ line on rider B), before the blank line and '### IV.8'.
i = unique_index(lines, lambda ln: ln.startswith("- **[READ 2026-09-10, Opus 5 — rider B's dual check RUN AND PASSED; the label is hereby `[novelty: dual-model check 2026-09-10]`"), "IV.7 READ line")
entry_of(lines, i, "### IV.7 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### IV.8 "):
    sys.exit("IV.7's READ line is not the last line before '### IV.8'")
if not lines[i - 1].startswith("- **[RIDER B 2026-09-10, Session 21 — from `results/c2-m5/PRICING.md` §5"):
    sys.exit("IV.7's rider B is not directly above its READ line")
lines[i + 1:i + 1] = [blocks["iv7"]]

# 6. IV.19: after its STATUS line, before the blank line and '## GROUP V'.
i = unique_index(lines, lambda ln: ln.startswith("- **STATUS.** **program-adjudicated (dual-model)**, `results/c2-m6/check-O.md` 2026-09-17"), "IV.19 STATUS")
entry_of(lines, i, "### IV.19 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("## GROUP V "):
    sys.exit("IV.19's STATUS line is not the last line before '## GROUP V'")
if not lines[i - 4].startswith("- **STATEMENT.** For the first-order datum W_Z(f_{t,L})") or "class A (≤ 1 h) for L ≤ 28.35" not in lines[i - 4]:
    sys.exit("IV.19's STATEMENT with the cost line is not four lines above its STATUS line")
lines[i + 1:i + 1] = [blocks["iv19"]]

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
if len(orig) - 1 != 655 or len(lines) - 1 != 662:
    sys.exit("line count is %d -> %d, expected 655 -> 662" % (len(orig) - 1, len(lines) - 1))
for m in MARKS:
    if new_text.count(m) != 1:
        sys.exit("marker %r occurs %d times after insertion" % (m[:50], new_text.count(m)))

out = dry if dry else ZOO
out.write_text(new_text, encoding="utf-8")
print("OK: %s written; +%d lines (655 -> %d); entries 58 (I 8, II 5, III 21, IV 19, V 5); SHA-256 after %s%s"
      % (out, added, len(lines) - 1, hashlib.sha256(new_text.encode("utf-8")).hexdigest(), " [DRY RUN -- BARRIER-ZOO.md untouched]" if dry else ""))
