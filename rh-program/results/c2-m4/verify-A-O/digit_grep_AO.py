#!/usr/bin/env python3
"""Checker's digit / Z-lower-bound grep (CHECK-O-A item (i)): every hit, code AND comment, classified."""
import re, sys, os
root = sys.argv[1]
files = ["Zeta23/Separation/B1Sym.lean", "Zeta23/Separation/Assembly2.lean",
         "comparator/ChallengeDeps/Separation6b.lean", "comparator/Challenge/SeparationClause4b.lean",
         "comparator/Solution/SeparationClause4b.lean", "comparator/Challenge/Separation6b.lean",
         "comparator/Solution/Separation6b.lean", "comparator/PrintAxioms/SeparationClause4b.lean",
         "comparator/PrintAxioms/Separation6b.lean"]
pats = [r"8\.7", r"87\s*/\s*10", r"10\.99", r"1099", r"10\.98", r"0\.22", r"Z_lo", r"1\s*/\s*18", r"one_div_eighteen",
        r"eighteen", r"8\.6", r"3\.31", r"0\.23", r"\b18\b", r"exp\s*\(-4\s*/\s*3\)", r"\(Z\)|≤ Z\b|≤ Z\)|Z_pos|Z_le"]
def code_mask(text):
    # returns per-line list: True if the line has code outside comments (block /- -/ and --)
    out = []; depth = 0
    for line in text.split("\n"):
        code = []; i = 0
        while i < len(line):
            if depth == 0 and line.startswith("--", i): break
            if line.startswith("/-", i): depth += 1; i += 2; continue
            if depth > 0 and line.startswith("-/", i): depth -= 1; i += 2; continue
            if depth == 0: code.append(line[i])
            i += 1
        out.append("".join(code))
    return out
for f in files:
    text = open(os.path.join(root, f), encoding="utf-8").read()
    codes = code_mask(text); lines = text.split("\n")
    for p in pats:
        for n, (ln, cd) in enumerate(zip(lines, codes), 1):
            if re.search(p, ln):
                kind = "CODE" if re.search(p, cd) else "comment"
                print(f"{p!s:28} {kind:8} {f}:{n}: {ln.strip()[:150]}")
