#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zoo-s37 writer's block builder (Opus 5.5, 2026-09-30). Fills the <!-- BLOCK:name --> ... <!-- END:name --> sections of
results/zoo-s37/zoo-entries-proposed.md FROM THE SOURCES, by code, never typed:
  iv21   results/d4-infty-s36/NOTE.md §5.1 Option A (heading -> '###' house style; five bullets byte for byte)
  iv22   results/novel-wave-s36/ZOO-LINES-STAGED.md Block (i), renumbered IV.21 -> IV.22, <ENTRY-DATE> filled
  i9     Block (iii), <ENTRY-DATE> filled
  iv9    Block (ii), <ENTRY-DATE> filled, the one-producer span -> <PRODUCER-B-VERDICT>
  iii15  Block (iv), <ENTRY-DATE> filled
  iv20   Block (v), byte for byte
  xref   the brief's d4-infty row, then Block X renumbered (IV.21 -> IV.22 in the wave rows)
  count  Block C with the adaptation pairs C0-C5 below (exact OLD -> NEW, each once)
Read-only on every source; writes only the proposed file (--write) or prints a summary (default).
The insertion script scripts/zoo-insert-s37.py re-derives every block independently and compares."""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NOTE = ROOT / "results" / "d4-infty-s36" / "NOTE.md"
STAGED = ROOT / "results" / "novel-wave-s36" / "ZOO-LINES-STAGED.md"
PROPOSED = ROOT / "results" / "zoo-s37" / "zoo-entries-proposed.md"
NOTE_HASH = "7a1dc42eb73e2f5811c84409c4564776281a71eca6edd439c6487f47f31f36ca"
STAGED_HASH = "0a26acaab4cfe2a0fd32178cab34d9817e66b3030b6a2296541c0a867af6ef5d"
ENTRY_DATE = "2026-09-30"
TOKEN = "<PRODUCER-B-VERDICT>"


def die(msg):
    sys.exit("build_blocks: STOP -- " + msg)


for p, h in ((NOTE, NOTE_HASH), (STAGED, STAGED_HASH)):
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    if got != h:
        die("%s hashes to %s, expected %s" % (p.relative_to(ROOT), got, h))

note = NOTE.read_text(encoding="utf-8").split("\n")
staged = STAGED.read_text(encoding="utf-8").split("\n")


def section(lines, head_prefix):
    """The non-empty lines of the section whose '## ' / '*Option' heading starts with head_prefix, up to the next heading or '---'."""
    starts = [i for i, ln in enumerate(lines) if ln.startswith(head_prefix)]
    if len(starts) != 1:
        die("section head %r occurs %d times" % (head_prefix, len(starts)))
    out = []
    for ln in lines[starts[0] + 1:]:
        if ln.startswith("## ") or ln == "---" or ln.startswith("*Option B"):
            break
        if ln:
            out.append(ln)
    return out


# d4-infty NOTE §5.1 Option A: the heading bullet and five bullets.
OPT_A = section(note, "*Option A — a Group-IV candidate entry, after IV.20 as staged by s35:*")
if len(OPT_A) != 6:
    die("NOTE §5.1 Option A has %d non-empty lines, expected 6" % len(OPT_A))
D4_TITLE = ("IV.21 The degree clause and the lattice-index kill (no square of Spec Z graded by ζ carries a real self-intersection "
            "of the diagonal)")
D4_TAIL_STAGED = " — NEW, Session 36 (`results/d4-infty-s36/NOTE.md` §2–§3)"
D4_TAIL_NEW = " — NEW, Session 36 (`results/d4-infty-s36/NOTE.md` §2–§3; entered 2026-09-30, Session 37)"
if OPT_A[0] != "- **" + D4_TITLE + D4_TAIL_STAGED + "**":
    die("the NOTE's Option A heading line is not the one the brief names")
for ln, pre in zip(OPT_A[1:], ("- **STATEMENT.**", "- **KILLS / RETURNS.**", "- **EXECUTABLE TEST.**", "- **SOURCE.**",
                                "- **STATUS.** program-adjudicated — dual-model (writer Opus 5.5, Session 36; the orchestrator's read")):
    if not ln.startswith(pre):
        die("Option A bullet does not begin %r" % pre)

# The wave's staged blocks, each read from its own '## Block' section.
S_I = section(staged, "## Block (i) — NEW entry IV.21")
S_II = section(staged, "## Block (ii) — RIDER on IV.9")
S_III = section(staged, "## Block (iii) — NEW entry I.9")
S_IV = section(staged, "## Block (iv) — RIDER on III.15")
S_V = section(staged, "## Block (v) — the IV.20 formalization bullet")
S_X = section(staged, "## Block X — cross-reference rows")
S_C = section(staged, "## Block C — the entry-count paragraph")
for name, sec, n in (("(i)", S_I, 6), ("(ii)", S_II, 1), ("(iii)", S_III, 6), ("(iv)", S_IV, 1), ("(v)", S_V, 1), ("X", S_X, 4)):
    if len(sec) != n:
        die("staged Block %s has %d non-empty lines, expected %d" % (name, len(sec), n))
if not S_C or not S_C[0].startswith("**Entry count (dated, Session 37, <ENTRY-DATE>).**"):
    die("staged Block C does not open with the count paragraph")
S_C = S_C[0]


def once(text, old, new, tag):
    if text.count(old) != 1:
        die("%s: OLD occurs %d times (need exactly 1): %r" % (tag, text.count(old), old[:80]))
    return text.replace(old, new)


def fill_date(text, tag):
    return once(text, "<ENTRY-DATE>", ENTRY_DATE, tag + " <ENTRY-DATE>")


B = {}
# iv21 — the d4-infty entry (Option A): the heading edit, the bullets byte for byte.
B["iv21"] = ["### " + D4_TITLE + D4_TAIL_NEW, ""] + OPT_A[1:]
# iv22 — Block (i) renumbered; <ENTRY-DATE> filled.
head = once(S_I[0], "### IV.21 Prime channels add density", "### IV.22 Prime channels add density", "(i) renumbering")
B["iv22"] = [fill_date(head, "(i)"), ""] + S_I[1:]
# i9 — Block (iii).
B["i9"] = [fill_date(S_III[0], "(iii)"), ""] + S_III[1:]
# iv9 — Block (ii): <ENTRY-DATE> filled; the one-producer span -> the token.
OLD_PRODUCER = ("from ONE producer (A, Arb) — the second producer of `results/haglund-cert-s37/BRIEF.md` §3 is owed before "
                "external use")
B["iv9"] = [once(fill_date(S_II[0], "(ii)"), OLD_PRODUCER, TOKEN, "(ii) token")]
# iii15 — Block (iv).
B["iii15"] = [fill_date(S_IV[0], "(iv)")]
# iv20 — Block (v), byte for byte.
B["iv20"] = [S_V[0]]
# xref — the brief's d4-infty row, then Block X renumbered.
D4_ROW = ("| d4-infty s36 (the (D4) residual: lattice Hodge index under the degree clause) | closed by theorem (Session 36; read "
          "at the line Session 37, dual-model) | IV.21; IV.20; III.20; IV.1; I.2 |")
rows = []
for r in S_X:
    rows.append(r.replace("IV.21", "IV.22"))
B["xref"] = [D4_ROW] + rows
# count — Block C with the adaptation pairs C0-C4 (exact OLD -> NEW, each once).
C_PAIRS = (
    ("C0", "<ENTRY-DATE>", ENTRY_DATE),
    ("C1", "** IV.21 (prime channels add density",
     "** IV.21 (the degree clause and the lattice-index kill — Proposition N: the degree clause d(φ_n) = n holds, for "
     "multiplicative degrees, exactly when the target's graded Dirichlet series is −ζ′/ζ, and it makes c injective; Theorem S: "
     "under it no real self-intersection of the diagonal is compatible with Castelnuovo–Severi and product adjunction, and no "
     "canonical class sits in an index-one space with Δ and the graphs; d4-infty s36, `results/d4-infty-s36/NOTE.md` §2–§3, "
     "writer Opus 5.5, Session 36; the orchestrator's read at the line `read-F.md` AGREES-WITH-CORRECTIONS, Option A, Session "
     "37), IV.22 (prime channels add density"),
    ("C2", "make **61 entries** — I: 9, II: 5, III: 21, IV: 21, V: 5 (recounted from this file's `###` headings at insertion: "
           "9 + 5 + 21 + 21 + 5 = 61; Group IV 20 → 21, the new entry placed after IV.20, the last Group-IV entry in file order; "
           "Group I 8 → 9, placed after I.8)",
     "make **62 entries** — I: 9, II: 5, III: 21, IV: 22, V: 5 (recounted from this file's `###` headings at insertion: "
     "9 + 5 + 21 + 22 + 5 = 62; Group IV 20 → 22, the new entries placed after IV.20, the last Group-IV entry in file order, "
     "IV.21 before IV.22; Group I 8 → 9, placed after I.8)"),
    ("C3", "four cross-reference rows \"novel wave s36\"",
     "five cross-reference rows, \"d4-infty s36\" and four \"novel wave s36\""),
    ("C4", "711 → 736 lines if entered as staged, SHA-256 at launch <HASH>, <STREAM-FOLDER>)",
     "711 → 745 lines, SHA-256 at launch 90d0ad6a…, `results/zoo-s37/`)"),
)
c = S_C
for tag, old, new in C_PAIRS:
    c = once(c, old, new, tag)
B["count"] = [c]

for k, v in B.items():
    for ln in v:
        if "\t" in ln or "\r" in ln:
            die("block %s carries a tab or a carriage return" % k)
        if re.search(r"<(ENTRY-DATE|HASH|STREAM-FOLDER)>", ln):
            die("block %s still carries a staging placeholder" % k)
ORDER = ("count", "i9", "iii15", "iv9", "iv20", "iv21", "iv22", "xref")

if __name__ == "__main__":
    if "--write" in sys.argv:
        text = PROPOSED.read_text(encoding="utf-8")
        for k in ORDER:
            pat = re.compile(r"(<!-- BLOCK:%s -->\n)(.*?)(<!-- END:%s -->)" % (k, k), re.S)
            if len(pat.findall(text)) != 1:
                die("the proposed file carries the markers of block %s %d times" % (k, len(pat.findall(text))))
            body = "\n".join(B[k]) + "\n"
            text = pat.sub(lambda m: m.group(1) + body + m.group(3), text)
        PROPOSED.write_text(text, encoding="utf-8")
        print("written:", PROPOSED)
    for k in ORDER:
        print("%-6s %d line(s), %d bytes, sha256 %s" % (k, len(B[k]), len("\n".join(B[k]).encode()),
                                                       hashlib.sha256("\n".join(B[k]).encode()).hexdigest()[:16]))
