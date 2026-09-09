#!/usr/bin/env python3
"""Job 2 (Opus): the trust greps, comments stripped, with my own stripper.

Lean comments are /- ... -/ (NESTED) and -- to end of line; string literals may contain either,
so the stripper tracks strings too.  What is forbidden in the PROGRAM's Lean source (KICKSTART
10(i)): axiom, native_decide, unsafe, implemented_by, extern, opaque, sorry, admit, ofReduceBool,
Lean.trustCompiler, @[simp] on a bogus, and `decide` without `+kernel`.  A hit inside a comment
or a docstring is not a hit -- and that is exactly why the stripper has to be right.
"""
import re, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
FILES = ['lean/Zeta23/W1/FDH.lean', 'lean/Zeta23/W1/Ledger.lean', 'lean/Zeta23/W1/Soundness.lean',
         'lean/Zeta23/W1/ArgPrincipleBridge.lean', 'lean/Zeta23/W1/Format.lean',
         'lean/Zeta23/W1/Checker.lean', 'lean/Zeta23/W1/Instances.lean', 'lean/Zeta23.lean']

def strip(src):
    """remove nested block comments and line comments; keep string literals; keep line numbering."""
    out = []
    i, n, depth, instr = 0, len(src), 0, False
    while i < n:
        c = src[i]
        if instr:
            if c == '\\' and i + 1 < n:
                out.append('  '); i += 2; continue
            if c == '"':
                instr = False
            out.append(' ' if c != '\n' else '\n'); i += 1; continue
        if depth == 0 and c == '"':
            instr = True; out.append(' '); i += 1; continue
        if src.startswith('/-', i):
            depth += 1; out.append('  '); i += 2; continue
        if src.startswith('-/', i) and depth > 0:
            depth -= 1; out.append('  '); i += 2; continue
        if depth > 0:
            out.append('\n' if c == '\n' else ' '); i += 1; continue
        if src.startswith('--', i):
            j = src.find('\n', i)
            j = n if j < 0 else j
            out.append(' ' * (j - i)); i = j; continue
        out.append(c); i += 1
    return ''.join(out)

PATTERNS = [
    ('axiom',            r'(?<![A-Za-z_])axiom(?![A-Za-z_])'),
    ('native_decide',    r'native_decide'),
    ('unsafe',           r'(?<![A-Za-z_])unsafe(?![A-Za-z_])'),
    ('implemented_by',   r'implemented_by'),
    ('extern',           r'@\[extern'),
    ('opaque',           r'(?<![A-Za-z_])opaque(?![A-Za-z_])'),
    ('sorry',            r'(?<![A-Za-z_-])sorry(?![A-Za-z_-])'),
    ('admit',            r'(?<![A-Za-z_])admit(?![A-Za-z_])'),
    ('ofReduceBool',     r'ofReduceBool'),
    ('trustCompiler',    r'trustCompiler'),
    ('partial',          r'(?<![A-Za-z_])partial(?![A-Za-z_])'),
    ('macro/elab hack',  r'(?<![A-Za-z_])(?:macro_rules|elab)(?![A-Za-z_])'),
]
total = 0
print("%-46s %-8s %s" % ("file", "lines", "hits (comments and string literals stripped)"))
print("-" * 96)
decides = []
for f in FILES:
    src = open(os.path.join(ROOT, f), encoding='utf-8').read()
    code = strip(src)
    hits = []
    for name, pat in PATTERNS:
        for m in re.finditer(pat, code):
            ln = code[:m.start()].count('\n') + 1
            hits.append("%s:%d" % (name, ln))
    total += len(hits)
    print("%-46s %-8d %s" % (f, src.count('\n') + 1, ", ".join(hits) if hits else "none"))
    # every `decide` in code must be `decide +kernel` or `by decide` on a Prop the kernel does
    for m in re.finditer(r'(?<![A-Za-z_])decide(?![A-Za-z_])(\s*\+\s*kernel)?', code):
        ln = code[:m.start()].count('\n') + 1
        decides.append((f, ln, 'decide +kernel' if m.group(1) else 'decide'))

print("\n`decide` occurrences in code (a bare `decide` is fine on a small decidable Prop such as")
print("`(1 : ℤ) ≤ 1` or `m = 0`; `+kernel` is required for the big checker evaluations):")
from collections import Counter
c = Counter((f, k) for f, _, k in decides)
for (f, k), n in sorted(c.items()):
    print("   %-46s %-16s %d" % (f, k, n))

print("\nTOTAL forbidden-token hits in code: %d" % total)
print("VERDICT: %s" % ("PASS" if total == 0 else "FAIL"))
sys.exit(0 if total == 0 else 1)
