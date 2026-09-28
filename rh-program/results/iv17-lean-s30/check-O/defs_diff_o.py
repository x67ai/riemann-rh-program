"""defs_diff_o.py -- CHECKER: the seven trusted definitions of ChallengeDeps/IntegralityGap.lean against their Zeta23 originals.
Extracts `def <name>` up to the next blank line / docstring / def, compares raw bytes and whitespace-normalized text."""
import re, sys, os
root = sys.argv[1]
def get(path, name):
    s = open(os.path.join(root, path), encoding="utf-8").read()
    m = re.search(r"^def " + re.escape(name) + r"\b.*?(?=\n\s*\n|\n/--|\n/-|\ntheorem|\nlemma|\ndef |\nend)", s, re.S | re.M)
    return m.group(0) if m else None
T = "comparator/ChallengeDeps/IntegralityGap.lean"
pairs = [("chi", "Zeta23/PairCeiling/GridParseval.lean"), ("dftMark", "Zeta23/PairCeiling/GridParseval.lean"),
         ("zetaM", "Zeta23/PairCeiling/GridParseval.lean"), ("gridRow", "Zeta23/PairCeiling/GridCorner.lean"),
         ("dftMarkQ", "Zeta23/PairCeiling/GridParsevalRat.lean"), ("gridRowQ", "Zeta23/PairCeiling/GridParsevalRat.lean"),
         ("fracMark", "Zeta23/PairCeiling/GridGap.lean")]
ok = True
for n, src in pairs:
    a, b = get(T, n), get(src, n)
    raw = a == b; norm = a is not None and b is not None and " ".join(a.split()) == " ".join(b.split())
    ok &= norm
    print(f"{n:10s} vs {src}: raw {'IDENTICAL' if raw else 'differs'}; whitespace-normalized {'IDENTICAL' if norm else 'DIFFER'}")
    print("   trusted : " + (a or "NONE").replace("\n", "\n             "))
    if not raw: print("   original: " + (b or "NONE").replace("\n", "\n             "))
print("RESULT:", "PASS" if ok else "FAIL")
