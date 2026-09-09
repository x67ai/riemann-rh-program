#!/usr/bin/env python3
"""trust_greps.py -- KICKSTART 10(j) trust greps on merge, COMMENTS STRIPPED FIRST (nested block comments and line
comments removed), over the comparator DBN topic files and every module under Zeta23/DBN/.  Eight patterns:
axiom, native_decide, unsafe, implemented_by, extern, opaque, sorry, ofReduceBool (whole-word, code only).  Also reports the
raw (comments included) counts for the record.  The ONLY permitted `sorry` hits are the challenge file's placeholders,
listed by line.  Exit 0 iff no code hit other than those.   usage: trust_greps.py <lean-root>
"""
import glob, os, re, sys

ROOT = sys.argv[1]
PATTERNS = ["axiom", "native_decide", "unsafe", "implemented_by", "extern", "opaque", "sorry", "ofReduceBool"]

def strip_comments(src):
    out = []; i = 0; n = len(src); depth = 0
    while i < n:
        if src.startswith("/-", i): depth += 1; i += 2; out.append("\n" if False else ""); continue
        if depth > 0:
            if src.startswith("-/", i): depth -= 1; i += 2
            else:
                if src[i] == "\n": out.append("\n")   # keep line numbering
                i += 1
            continue
        if src.startswith("--", i):
            j = src.find("\n", i); i = n if j < 0 else j; continue
        out.append(src[i]); i += 1
    return "".join(out)

files = sorted(glob.glob(os.path.join(ROOT, "comparator", "*DBN*.lean")) + glob.glob(os.path.join(ROOT, "comparator", "*", "DBN.lean"))
               + glob.glob(os.path.join(ROOT, "comparator", "*", "DBN", "*.lean")) + [os.path.join(ROOT, "comparator", "config-dbn.json")]
               + glob.glob(os.path.join(ROOT, "Zeta23", "DBN", "*.lean")) + glob.glob(os.path.join(ROOT, "Zeta23", "DBN", "Instance02", "*.lean")))
files = sorted(set(files))
print(f"files: {len(files)} ({sum(1 for f in files if '/comparator/' in f)} comparator DBN files, {sum(1 for f in files if '/Zeta23/DBN/' in f)} Zeta23/DBN modules)")
raw = {p: 0 for p in PATTERNS}; code = {p: 0 for p in PATTERNS}; code_hits = []
for f in files:
    src = open(f, encoding="utf-8").read()
    stripped = strip_comments(src) if f.endswith(".lean") else src
    for p in PATTERNS:
        rx = re.compile(r"(?<![A-Za-z0-9_'])" + p + r"(?![A-Za-z0-9_'])")
        raw[p] += len(rx.findall(src))
        for ln, line in enumerate(stripped.split("\n"), 1):
            if rx.search(line):
                code[p] += 1; code_hits.append((p, os.path.relpath(f, ROOT), ln, line.strip()))
print("pattern           raw(all text)  code-only")
for p in PATTERNS: print(f"  {p:16s} {raw[p]:8d}     {code[p]:6d}")
print("code-only hits, by line:")
for p, f, ln, line in code_hits: print(f"  {p}: {f}:{ln}: {line}")
permitted = [h for h in code_hits if h[0] == "sorry" and h[1] == "comparator/Challenge/DBN.lean"]
other = [h for h in code_hits if h not in permitted]
print(f"permitted (challenge placeholders): {len(permitted)}; other code hits: {len(other)}")
print("RESULT:", "CLEAN" if not other else "FAIL")
sys.exit(0 if not other else 1)
