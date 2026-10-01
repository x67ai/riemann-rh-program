#!/usr/bin/env python3
"""zoo-s41 insertion (Session 41): three I.2 riders (Theorem 1.6; T1-T3; S7<=2), four cross-reference rows,
the dated count paragraph. Blocks are read from results/novel-wave-s39/ZOO-LINES-STAGED.md by content;
gated on the zoo's SHA-256 at launch; insertion bottom-up at anchors verified by content. --in-place writes."""
import hashlib, io, sys
ZOO = "BARRIER-ZOO.md"; ST = "results/novel-wave-s39/ZOO-LINES-STAGED.md"; DATE = "2026-10-01"
GATE = "0a0a832d10cae4e61fae9befda358519e74181e7961a948b5c1c1a84a7df7587"
raw = io.open(ZOO, encoding="utf-8").read()
if hashlib.sha256(raw.encode("utf-8")).hexdigest() != GATE: sys.exit("zoo hash differs from the gate - stop.")
Z = raw.split("\n"); S = io.open(ST, encoding="utf-8").read().split("\n")
def one(pred, what):
    hits = [l for l in S if pred(l)]
    if len(hits) != 1: sys.exit("staged block %s: %d matches" % (what, len(hits)))
    return hits[0].replace("<ENTRY-DATE>", DATE)
b1 = one(lambda l: l.startswith("- **[RIDER") and "unit `free-greedy-s40/theory`" in l[:80], "(i)")
b2 = one(lambda l: l.startswith("- **[RIDER") and "unit `s5-multiplicity-s40`" in l[:80], "(ii)")
b3 = one(lambda l: l.startswith("- **[RIDER") and "unit `local-greedy-s40`" in l[:80], "(iii)")
rows = [l for l in S if l.startswith("| unit `") and ("-s40" in l[:40])]
if len(rows) != 4: sys.exit("rows: %d" % len(rows))
bc = one(lambda l: l.startswith("**Entry count (dated, Session 41"), "C")
# the orchestrator's one change to block (i): the zero-density clause, after the Session-41 check of the notes
old = "any brief deriving B_ρ from a zero-density bootstrap — such estimates give g-prime gaps x^{1−1/A+ε}, at best x^{½} (`read-F.md` l. 31–32, the orchestrator's pricing, single-check), while B_ρ has the strength of gaps x^θ, θ < ½ − ρ (Prop. 2.1)."
new = "any brief deriving B_ρ from a zero-density bootstrap — the passage from zero density to short intervals is not available for S8 (it needs a Littlewood-type zero-free region or a log-free density estimate: Broucke–Debruyne, Acta Arith. 207 (2023), §4), and the explicit formula's x^b error (b > θ) keeps the bootstrap exponent from falling for any density constant, while B_ρ has the strength of gaps x^θ, θ < ½ − ρ (Prop. 2.1) (`results/lemmaB-s41/ORCH-NOTES.md` O8 as corrected, `orch-notes-read-O.md` §3; dual-checked). A mean-square form suffices: Theorem 1.6 holds with ∫_X^{2X}E² ≪ X^{1+2θ₂}, and β ≤ (1 + 2β₂)/3 for every Beurling system (Lemma L), so θ₂ < (3σ₁ − 2)/4 — 0.0925 for S8(π/16), 0.1675 for S8(π/32) — refutes U (ORCH-NOTES O1, O10; dual-checked)."
if b1.count(old) != 1: sys.exit("block (i): the clause to update was not found once.")
b1 = b1.replace(old, new)
def chk(i, pred, what):
    if not pred(Z[i - 1]): sys.exit("anchor line %d is not %s" % (i, what))
chk(758, lambda l: l.startswith("| unit `fejer-form-s39`"), "the fejer row")
chk(93, lambda l: l.startswith("- **[RIDER"), "I.2's last rider")
chk(92, lambda l: l.startswith("- **[RIDER") and "u-offsurgery-s39" in l[:120], "the S5 rider")
chk(43, lambda l: l.startswith("**Entry count (dated, Session 40"), "the Session-40 count paragraph")
n0 = raw.count("\n")                      # real line count (the file ends with a newline)
final = n0 + 4 + 3 + 2
bc = bc.replace("<N>", str(final))
Z[758:758] = rows            # after line 758
Z[93:93] = [b1]              # after line 93
Z[92:92] = [b2, b3]          # after line 92: (ii) then (iii)
Z[43:43] = ["", bc]          # after line 43, one blank line before the paragraph
out = "\n".join(Z)
n_entries = sum(1 for l in Z if l.startswith("### "))
n1 = out.count("\n")
print("%d -> %d lines; entries (### headings): %d; SHA-256 %s" % (n0, n1, n_entries, hashlib.sha256(out.encode("utf-8")).hexdigest()))
if n1 != final or n_entries != 64: sys.exit("count check failed - nothing written.")
dest = ZOO if "--in-place" in sys.argv else sys.argv[sys.argv.index("--out") + 1]
io.open(dest, "w", encoding="utf-8").write(out)
