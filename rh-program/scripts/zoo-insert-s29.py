#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Session 29 zoo stream `zoo-s29` (2026-09-28): insert into BARRIER-ZOO.md four lines, bookkeeping only -- E3's rider on
IV.10 after R-b' (block iv10: results/e3-borger-rung1/NOTE.md section 8(a), line 132, verbatim plus the house "entered at"
clause and the SCOPE-over-Z sentence), E3's pointer rider on III.20 after R-a (block iii20: NOTE section 8(b), line 135,
verbatim plus the "entered at" clause), E1's rider on II.1 with the X1 pointer to IV.17 (block ii1: results/e1-m5u/
FORMULATION.md section 6, line 245, the leading "> " stripped, verbatim modulo the house head and the one X1 sentence),
and the count paragraph (block count). No numbered entry: the entry count stays 58 (I 8, II 5, III 21, IV 19, V 5);
662 -> 667 lines (+5: three one-line riders, the count paragraph and the blank line before it).

Source of every inserted line: results/zoo-s29/zoo-entries-proposed.md, read AT RUN TIME (blocks delimited by
<!-- BLOCK:name --> ... <!-- END:name -->), so the orchestrator's post-reader amendments flow in. Before touching the
zoo the script asserts that BARRIER-ZOO.md has SHA-256 1de55c2e... (the zoo at brief time), that NOTE.md has d71fb8a0...
and FORMULATION.md c4b45618..., that every anchor occurs exactly once (anchored by the full text of the neighboring
lines, never by line number alone; the three rider anchors are asserted unique in their first 120 characters), that
the iv10 and iii20 bodies equal NOTE lines 132 and 135 modulo exactly the named insertions and the ii1 body equals
FORMULATION line 245 modulo exactly the head and the X1 sentence (the script prints every difference it allows), that
the A19-A22 NEW strings of results/e1-m5u/read-O.md lines 208-214 are present and the OLD strings absent, and that
the labels are the Session-28 readers'. Pure insertion: no existing line is modified or removed; each rider goes
directly after its entry's last existing bullet, before the blank line that precedes the next heading; the count
paragraph goes after the Session-28 count paragraph, before the '---'. The script refuses to run twice. Afterwards it
verifies that every original line survives, in order, as an identical line, that the '### ' count is 58 with per-group
counts 8/5/21/19/5, that the line arithmetic is exact (+5, 662 -> 667), that the file ends with exactly one newline,
and that the inserted text carries none of the linted phrases.

Usage: python3 scripts/zoo-insert-s29.py [--dry-run OUTPATH]
  --dry-run OUTPATH    write the result to OUTPATH and leave BARRIER-ZOO.md untouched (the writer's only mode).
Modeled on scripts/zoo-insert-s28.py.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZOO = ROOT / "BARRIER-ZOO.md"
PROPOSED = ROOT / "results" / "zoo-s29" / "zoo-entries-proposed.md"
NOTE = ROOT / "results" / "e3-borger-rung1" / "NOTE.md"
FORM = ROOT / "results" / "e1-m5u" / "FORMULATION.md"
ZOO_HASH_BEFORE = "1de55c2ee319a7e89e724c94780ebf0626a4fa5f045968deafc66e4c7413d9ca"
NOTE_HASH = "d71fb8a0189bbcb2b910e036f4849e1b8df2487f2d1b46be1e077ff79f9330c5"
FORM_HASH = "c4b4561850209106fccb08a8b166780f5a6eb7c8cc920ec2f715e5e3b0f7ef2e"

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
    sys.exit("results/e3-borger-rung1/NOTE.md SHA-256 is not %s -- the E3 record changed; nothing done." % NOTE_HASH[:16])
form_bytes = FORM.read_bytes()
if hashlib.sha256(form_bytes).hexdigest() != FORM_HASH:
    sys.exit("results/e1-m5u/FORMULATION.md SHA-256 is not %s -- the E1 record changed; nothing done." % FORM_HASH[:16])
note_lines = note_bytes.decode("utf-8").split("\n")
form_lines = form_bytes.decode("utf-8").split("\n")

MARKS = ("- **[RIDER 2026-09-26, Session 28 (E3 Borger rung-1 step, `results/e3-borger-rung1/NOTE.md` §3–§4;",
         "- **[RIDER 2026-09-26, Session 28 (E3, `results/e3-borger-rung1/NOTE.md` §3–§5;",
         "- **[RIDER 2026-09-26, Session 28 (E1, M5-U formulation slot, `results/e1-m5u/FORMULATION.md` §2–§4;",
         "**Entry count (dated, Session 29, 2026-09-28).**")
for m in MARKS:
    if m in zoo_text:
        sys.exit("BARRIER-ZOO.md already contains %r -- refusing to insert twice." % m[:70])


def block(text: str, name: str, where: str) -> str:
    ms = re.findall(r"<!-- BLOCK:%s -->\n(.*?)\n<!-- END:%s -->" % (re.escape(name), re.escape(name)), text, re.S)
    if len(ms) != 1:
        sys.exit("block %s occurs %d times in %s (need exactly 1)" % (name, len(ms), where))
    return ms[0]


NAMES = ("count", "ii1", "iii20", "iv10")
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
for k, head in (("iv10", MARKS[0]), ("iii20", MARKS[1]), ("ii1", MARKS[2]), ("count", MARKS[3])):
    if not blocks[k].startswith(head):
        sys.exit("block %s must start with %r" % (k, head[:60]))
    if k != "count" and "]**" not in blocks[k]:
        sys.exit("block %s has no house head closing ']**'" % k)


def split_head(line: str):
    i = line.index("]**") + 3
    return line[:i], line[i:]


# --- iv10: NOTE line 132 modulo exactly (a) the "entered at" clause in the head and (b) the SCOPE sentence. ---
n132 = note_lines[131]
if not (n132.startswith("- **[RIDER 2026-09-26, Session 28 (E3 Borger rung-1 step, `results/e3-borger-rung1/NOTE.md` §3–§4; writer Fable 5.1, Opus 5 reader `read-O.md` CLOSES after amendments) — the HOST-DIMENSION check is a theorem on rung 1")
        and n132.endswith("`[novelty: dual-model check 2026-09-26]`.")):
    sys.exit("NOTE line 132 is not the E3 IV.10 rider with the expected head and label (the record has moved)")
A_OLD = "Opus 5 reader `read-O.md` CLOSES after amendments)"
A_NEW = "Opus 5 reader `read-O.md` CLOSES after amendments; entered at the Session-29 zoo stream)"
B_OLD = "`verify/witt_pairs_Z.py`). And (NOTE §4, Theorems 4.1–4.2):"
SCOPE_RE = re.compile(r"`verify/witt_pairs_Z\.py`\)\. (Scope over Z: .*?) And \(NOTE §4, Theorems 4\.1–4\.2\):")
if n132.count(A_OLD) != 1 or n132.count(B_OLD) != 1:
    sys.exit("NOTE line 132 does not carry the two insertion points exactly once")
b = blocks["iv10"]
if b.count(A_NEW) != 1:
    sys.exit("block iv10 does not carry the 'entered at the Session-29 zoo stream' clause exactly once")
ms = SCOPE_RE.findall(b)
if len(ms) != 1 or b.count(B_OLD) != 0:
    sys.exit("block iv10 does not carry exactly one SCOPE sentence between the witt_pairs_Z.py clause and 'And (NOTE §4, …'")
scope = ms[0]
if "Scope over Z:" not in scope or "widen" in scope.lower() and "never widened" not in scope.lower():
    sys.exit("block iv10's scope sentence is malformed")
rebuilt = b.replace(A_NEW, A_OLD).replace("`verify/witt_pairs_Z.py`). " + scope + " And (NOTE §4, Theorems 4.1–4.2):", B_OLD)
if rebuilt != n132:
    sys.exit("block iv10 differs from NOTE line 132 by more than the two named insertions")
print("NOTE: block iv10 = NOTE line 132 with exactly two insertions (allowed):\n   (a) %r -> %r\n   (b) after %r, the sentence: %s"
      % (A_OLD, A_NEW, "`verify/witt_pairs_Z.py`).", scope))
if not b.endswith("`[novelty: dual-model check 2026-09-26]`."):
    sys.exit("block iv10 does not end with the E3 reader's label as printed at NOTE line 132")

# --- iii20: NOTE line 135 modulo exactly the "entered at" clause. ---
n135 = note_lines[134]
if not (n135.startswith("- **[RIDER 2026-09-26, Session 28 (E3, `results/e3-borger-rung1/NOTE.md` §3–§5) — (B) and R-a's sentence are theorems on rung 1.]**")
        and n135.endswith("`[novelty: dual-model check 2026-09-26]`.")):
    sys.exit("NOTE line 135 is not the E3 III.20 pointer rider with the expected head and label (the record has moved)")
C_OLD = "`results/e3-borger-rung1/NOTE.md` §3–§5)"
C_NEW = "`results/e3-borger-rung1/NOTE.md` §3–§5; entered at the Session-29 zoo stream)"
if n135.count(C_OLD) != 1 or blocks["iii20"].count(C_NEW) != 1:
    sys.exit("the III.20 'entered at' insertion point is not exactly once in NOTE line 135 / block iii20")
if blocks["iii20"].replace(C_NEW, C_OLD) != n135:
    sys.exit("block iii20 differs from NOTE line 135 by more than the 'entered at' clause")
print("NOTE: block iii20 = NOTE line 135 with exactly one insertion (allowed): %r -> %r" % (C_OLD, C_NEW))
if "IV.10 rider of this date" not in blocks["iii20"]:
    sys.exit("block iii20 lost its internal pointer 'IV.10 rider of this date'")
d1 = re.match(r"- \*\*\[RIDER (\d{4}-\d\d-\d\d),", blocks["iv10"]).group(1)
d2 = re.match(r"- \*\*\[RIDER (\d{4}-\d\d-\d\d),", blocks["iii20"]).group(1)
if d1 != d2:
    sys.exit("the IV.10 and III.20 riders carry different dates (%s / %s); 'of this date' would be wrong" % (d1, d2))

# --- ii1: FORMULATION line 245 (the "> " stripped) modulo exactly the head and the X1 sentence. ---
f245 = form_lines[244]
OLD_HEAD = "- **[RIDER 2026-09-26, Session 28 (E1, M5-U formulation slot, `results/e1-m5u/FORMULATION.md` §2–§4; entered at the next zoo stream) — M5-U's contract and the theorem that its real-weighted relaxation is a continuum.**"
if not f245.startswith("> " + OLD_HEAD) or f245.count("\n") != 0:
    sys.exit("FORMULATION line 245 is not the blockquoted E1 rider with the expected head (the record has moved)")
old_body = f245[2 + len(OLD_HEAD):]
new_head, new_body = split_head(blocks["ii1"])
print("NOTE: block ii1 head differs from the FORMULATION record's head (allowed):\n   REC: %s\n   NEW: %s" % (OLD_HEAD, new_head))
if "`[dual-model check 2026-09-26]`" not in new_head or "entered at the next zoo stream" in blocks["ii1"] or "entered at the Session-29 zoo stream" not in new_head:
    sys.exit("block ii1 head lacks the E1 read-O line-238 label or still says 'entered at the next zoo stream'")
X_OLD = "is returned by (2)–(3) before design cost. Open, precisely:"
X_RE = re.compile(r"is returned by \(2\)–\(3\) before design cost\. (Pointer \(X1; .*?) Open, precisely:")
if old_body.count(X_OLD) != 1:
    sys.exit("FORMULATION line 245 does not carry the X1 insertion point exactly once")
ms = X_RE.findall(new_body)
if len(ms) != 1 or new_body.count(X_OLD) != 0:
    sys.exit("block ii1 does not carry exactly one X1 sentence between 'before design cost.' and 'Open, precisely:'")
x1 = ms[0]
if new_body.replace("is returned by (2)–(3) before design cost. " + x1 + " Open, precisely:", X_OLD) != old_body:
    sys.exit("block ii1 body differs from FORMULATION line 245's body by more than the X1 sentence")
print("NOTE: block ii1 body = FORMULATION line 245 body with exactly one insertion (allowed): %s" % x1)
for q in ("Any brief that relaxes marks to reals", "locate the line where integrality is consumed"):
    if q not in x1:
        sys.exit("the X1 sentence no longer quotes IV.17's first words %r" % q)

# The A19-A22 strings of results/e1-m5u/read-O.md lines 208-214: NEW present, OLD absent (block and record).
A = {
    "A19": ("real parts Re ĝ(x + iy) = (2π)⁻¹(|ψ̂|² ∗ P_y)(x) ≥ 0 on the strip (a four-point orbit contributes four times this)",
            "orbit sums (2π)⁻¹(|ψ̂|² ∗ P_y)(x) ≥ 0 on the strip"),
    "A20": ("(from G_X = ∞, Poltoratski Thm 2 + Bombieri 2000 p. 225; the mechanism is Mitkovski–Poltoratski's for finite measures, \"every non-zero measure σ with a spectral gap (−a, a) gives a rise to two a-indeterminate measures\")",
            "(from G_X = ∞, Poltoratski Thm 2 + Bombieri 2000 p. 225)"),
    "A21": ("and so is the soft-windowed datum at all but countably many heights (E1 §2.4)",
            "and so is the soft-windowed datum at every height (E1 §2.4)"),
    "A22": ("Bombieri 2000 p. 224's Example — introduced as showing that linear relations \"may occur for Dedekind zeta functions\" — is its complex-datum form.",
            "Bombieri 2000 p. 224's Example is its complex-datum form."),
}
for a, (new, old) in A.items():
    if new not in blocks["ii1"] or old in blocks["ii1"]:
        sys.exit("%s: NEW string absent from, or OLD string present in, block ii1" % a)
    if new not in f245 or old in f245:
        sys.exit("%s is not applied in FORMULATION line 245 itself" % a)
print("OK: A19 ... A22 NEW strings present, OLD strings absent (block ii1 and FORMULATION line 245).")

# Labels per the Session-28 readers; nothing single-check survives.
for k in ("iv10", "iii20", "ii1"):
    if "single-check" in blocks[k] or "Opus reader pending" in blocks[k] or "until the reader" in blocks[k]:
        sys.exit("block %s still carries a single-check / pending clause" % k)
if "58 entries" not in blocks["count"] or "8 + 5 + 21 + 19 + 5 = 58" not in blocks["count"] or "662 → 667" not in blocks["count"]:
    sys.exit("count block does not carry the 58 arithmetic and the 662 → 667 line count")


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

# The three rider anchors, by the full text of the line (first 120 characters asserted unique).
ANCHOR_II1 = "- **[RIDER 2026-09-25, Session 27 (D1(b) FORMULATION slot, `results/c2-m5b/FORMULATION.md` §0.3 eq. (0.5), §2.3, §5; entered at the Session-28 zoo stream) — the honest first-order class relative to this ceiling; M5 as a uniqueness question."
ANCHOR_III20 = "- **[RIDER 2026-09-25, Session 27 (D2 design-axis scout pair; `results/d2-scout-s26/HARVEST.md` \"Proposed riders\" 1, `scout-F.md` §4 R-a, `scout-O.md` P2, P9b, P9f) — the printed pairings on the squares of Spec Z are the explicit formula by definition.]**"
ANCHOR_IV10 = "- **[RIDER 2026-09-25, Session 27 (D2 design-axis scout pair; `results/d2-scout-s26/HARVEST.md` \"Proposed riders\" 2 and the adjudication paragraph; `scout-F.md` §4 R-b as amended, `scout-O.md` P1 and §8; the orchestrator's `verify-orch/witt_diag_degree.py`)"
for a in (ANCHOR_II1, ANCHOR_III20, ANCHOR_IV10):
    if zoo_text.count(a[:120]) != 1:
        sys.exit("the anchor's first 120 characters are not unique in the zoo: %r" % a[:120])

# The pointer targets of the X1 sentence (read, never edited): IV.17's KILLS and EXECUTABLE TEST (3) print the quoted words.
i17 = unique_index(lines, lambda ln: ln.startswith("### IV.17 "), "IV.17 heading")
seg = []
for ln in lines[i17 + 1:]:
    if ln.startswith("### ") or ln.startswith("## "):
        break
    seg.append(ln)
if not any(ln.startswith("- **KILLS.** Any brief that relaxes marks to reals") for ln in seg):
    sys.exit("IV.17's KILLS bullet does not begin 'Any brief that relaxes marks to reals'")
if not any(ln.startswith("- **EXECUTABLE TEST.**") and "(3) In every closure or baseline argument, locate the line where integrality is consumed" in ln for ln in seg):
    sys.exit("IV.17's EXECUTABLE TEST (3) does not contain 'locate the line where integrality is consumed'")

# 1. Count header: a blank line and the paragraph after the Session-28 count paragraph, before the '---'.
i = unique_index(lines, lambda ln: ln.startswith("**Entry count (dated, Session 28, 2026-09-26).** No entry is added. The six rider lines entered at the Session-27 zoo stream"), "Session-28 count paragraph")
if any(ln.startswith("### ") for ln in lines[:i]):
    sys.exit("the Session-28 count paragraph is not in the header")
if lines[i + 1] != "" or lines[i + 2] != "---":
    sys.exit("the Session-28 count paragraph is not followed by a blank line and '---'")
if not lines[i - 2].startswith("**Entry count (dated, Session 25, 2026-09-24).**") or lines[i - 1] != "":
    sys.exit("the Session-25 count paragraph is not directly above the Session-28 paragraph")
lines[i + 1:i + 1] = ["", blocks["count"]]

# 2. II.1: after its last existing bullet (the 2026-09-25 D1(b) rider), before the blank line and '### II.2'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_II1), "II.1 D1(b) rider")
entry_of(lines, i, "### II.1 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### II.2 "):
    sys.exit("II.1's D1(b) rider is not the last line before '### II.2'")
if not lines[i - 1].startswith("- **[READ 2026-09-10, Opus 5: the pointer above is CONFIRMED"):
    sys.exit("II.1's 2026-09-10 READ line is not directly above its D1(b) rider")
lines[i + 1:i + 1] = [blocks["ii1"]]

# 3. III.20: after its last existing bullet (the R-a rider), before the blank line and '### III.21'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_III20), "III.20 R-a rider")
entry_of(lines, i, "### III.20 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### III.21 "):
    sys.exit("III.20's R-a rider is not the last line before '### III.21'")
if not lines[i - 1].startswith("- **[RIDER 2026-09-16, Session 22 — pointer.]**"):
    sys.exit("III.20's 2026-09-16 pointer rider is not directly above R-a")
lines[i + 1:i + 1] = [blocks["iii20"]]

# 4. IV.10: after its last existing bullet (the R-b' rider with the HOST-DIMENSION check), before the blank line and '### IV.11'.
i = unique_index(lines, lambda ln: ln.startswith(ANCHOR_IV10), "IV.10 R-b' rider")
entry_of(lines, i, "### IV.10 ")
if lines[i + 1] != "" or not lines[i + 2].startswith("### IV.11 "):
    sys.exit("IV.10's R-b' rider is not the last line before '### IV.11'")
if "HOST-DIMENSION" not in lines[i] or "**deg(Γ₁ ∩ Γ_n) = Λ(n) for every n ≥ 2.**" not in lines[i]:
    sys.exit("IV.10's R-b' rider does not carry the HOST-DIMENSION check and deg(Γ₁ ∩ Γ_n) = Λ(n) that the new rider's scope clause points at")
if not lines[i - 1].startswith("- **STATUS.** program-adjudicated (computationally re-derived, Session 6)."):
    sys.exit("IV.10's STATUS line is not directly above R-b'")
lines[i + 1:i + 1] = [blocks["iv10"]]

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
if len(orig) - 1 != 662 or len(lines) - 1 != 667:
    sys.exit("line count is %d -> %d, expected 662 -> 667" % (len(orig) - 1, len(lines) - 1))
for m in MARKS:
    if new_text.count(m) != 1:
        sys.exit("marker %r occurs %d times after insertion" % (m[:50], new_text.count(m)))
for k in NAMES:
    if new_text.count(blocks[k]) != 1:
        sys.exit("block %s occurs %d times after insertion" % (k, new_text.count(blocks[k])))

out = dry if dry else ZOO
out.write_text(new_text, encoding="utf-8")
print("OK: %s written; +%d lines (662 -> %d); entries 58 (I 8, II 5, III 21, IV 19, V 5); SHA-256 after %s%s"
      % (out, added, len(lines) - 1, hashlib.sha256(new_text.encode("utf-8")).hexdigest(), " [DRY RUN -- BARRIER-ZOO.md untouched]" if dry else ""))
