"""trust_greps_s36.py -- the H5/H4 trust-grep tool (results/h4-pair-lean-s33/tools/trust_greps_h4.py) with this docstring and the default file
list changed (Session 36, theoremR-lean-s36 builder): KICKSTART 10(j) trust greps, comments stripped, for the ResidueRank topic files and the
three program modules.  usage: trust_greps_s36.py <root> [files...]   (root = the Lean tree or the repository mirror `lean/`).
Strips Lean block comments `/- ... -/` (nested) and line comments `-- ...` before grepping for the nine words,
so a word in a docstring is not a hit.  Prints every remaining hit with file:line; exit 1 if any hit."""
import re, sys, os
ROOT = sys.argv[1]
FILES = sys.argv[2:] or ["Zeta23/ResidueRank/LogPrimes.lean", "Zeta23/ResidueRank/Pair.lean", "Zeta23/ResidueRank/GenusBound.lean",
    "comparator/Challenge/ResidueRank.lean", "comparator/Solution/ResidueRank.lean", "comparator/PrintAxioms/ResidueRank.lean"]
WORDS = ["axiom", "native_decide", "unsafe", "implemented_by", "extern", "opaque", "sorry", "admit", "ofReduceBool"]
def strip(src):
    out, i, n, depth = [], 0, len(src), 0
    while i < n:
        if src.startswith("/-", i):
            depth += 1; i += 2; continue
        if depth and src.startswith("-/", i):
            depth -= 1; i += 2; continue
        if depth:
            out.append("\n" if src[i] == "\n" else " "); i += 1; continue
        if src.startswith("--", i):
            while i < n and src[i] != "\n": i += 1
            continue
        out.append(src[i]); i += 1
    return "".join(out)
hits = 0; seen = 0
for f in FILES:
    p = os.path.join(ROOT, f)
    if not os.path.exists(p):
        print(f"{f}: (absent)"); continue
    seen += 1
    s = strip(open(p, encoding="utf-8").read())
    for ln, line in enumerate(s.split("\n"), 1):
        for w in WORDS:
            if re.search(r"\b" + re.escape(w) + r"\b", line):
                print(f"{f}:{ln}: [{w}] {line.strip()}")
                hits += 1
print(f"files present: {seen}; hits outside comments: {hits}")
sys.exit(1 if hits else 0)
