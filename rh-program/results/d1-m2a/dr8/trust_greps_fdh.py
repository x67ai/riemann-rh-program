"""trust_greps_fdh.py -- KICKSTART 10(j) trust greps, comments stripped, on the D-R8 build's
new/changed Lean files (and the untouched W1 files for context).  Strips Lean block comments
`/- ... -/` (nested) and line comments `-- ...` before grepping for the seven words, so a word in a
docstring is not a hit.  Prints every remaining hit with file:line; exit 1 if any hit outside the
allowlist below."""
import re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "lean"))
FILES = ["Zeta23/W1/FDH.lean", "Zeta23/W1/Ledger.lean", "Zeta23/W1/Soundness.lean",
         "Zeta23/W1/ArgPrincipleBridge.lean", "Zeta23/W1/Format.lean", "Zeta23/W1/Checker.lean",
         "Zeta23/W1/Instances.lean", "Zeta23.lean"]
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
hits = 0
for f in FILES:
    p = os.path.join(ROOT, f)
    s = strip(open(p, encoding="utf-8").read())
    for ln, line in enumerate(s.split("\n"), 1):
        for w in WORDS:
            if re.search(r"\b" + re.escape(w) + r"\b", line):
                print(f"{f}:{ln}: [{w}] {line.strip()}")
                hits += 1
print(f"files: {len(FILES)}; hits outside comments: {hits}")
sys.exit(1 if hits else 0)
