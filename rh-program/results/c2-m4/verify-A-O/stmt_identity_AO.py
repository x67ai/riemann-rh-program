#!/usr/bin/env python3
"""Checker's own statement-identity extraction (independent of the builder's regex): for each theorem, scan from
`theorem <name>` and stop at the first `:=` that is outside every (), [], {}, ⟨⟩ pair and outside comments; compare
challenge vs solution byte for byte; also print SHA-256 of each statement."""
import sys, os, hashlib
root, topic, names = sys.argv[1], sys.argv[2], sys.argv[3:]
OPEN, CLOSE = "([{⟨", ")]}⟩"
def stmt(path, name):
    s = open(path, encoding="utf-8").read()
    key = "\ntheorem " + name
    i = s.find(key)
    if i < 0: return None
    i += 1; j = i; depth = 0
    while j < len(s):
        if s.startswith("--", j):
            while s[j] != "\n": j += 1
            continue
        c = s[j]
        if c in OPEN: depth += 1
        elif c in CLOSE: depth -= 1
        elif depth == 0 and s.startswith(":=", j): return s[i:j].rstrip()
        j += 1
    return None
ok = True
for n in names:
    a = stmt(os.path.join(root, f"comparator/Challenge/{topic}.lean"), n)
    b = stmt(os.path.join(root, f"comparator/Solution/{topic}.lean"), n)
    same = a is not None and a == b; ok &= same
    h = hashlib.sha256(a.encode()).hexdigest()[:16] if a else "-"
    print(f"{n:42} challenge {len(a.encode()) if a else 0:5} B, solution {len(b.encode()) if b else 0:5} B, sha256[:16] {h}: {'IDENTICAL' if same else 'DIFFER'}")
print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
