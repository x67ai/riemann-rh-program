#!/usr/bin/env python3
"""CHECK-O: every `OLD:` line of CHECK-O.md §11 must occur exactly once, line breaks read as spaces, in exactly one candidate file."""
import re, pathlib
RP = pathlib.Path("/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program")
chk = (RP / "results/theoremR-lean-s36/CHECK-O.md").read_text(encoding="utf-8")
sec = chk[chk.index("## 11. Verdict"):]
olds = [l[len("OLD: "):] for l in sec.splitlines() if l.startswith("OLD: ")]
news = [l[len("NEW: "):] for l in sec.splitlines() if l.startswith("NEW: ")]
cands = ["results/theoremR-lean-s36/FIDELITY.md", "results/theoremR-lean-s36/PREDERIVATION-ERRATA.md",
         "results/theoremR-lean-s36/BUILD-NOTES.md", "results/theoremR-lean-s36/SHARED.md", "lean/formalization.yaml", "lean/README.md",
         "lean/comparator/Challenge/ResidueRank.lean"]
norm = lambda s: " ".join(s.split())
T = {c: norm((RP / c).read_text(encoding="utf-8")) for c in cands}
ok = len(olds) == len(news)
print(f"OLD lines: {len(olds)}, NEW lines: {len(news)}")
for o in olds:
    counts = {c: T[c].count(norm(o)) for c in cands}
    hit = {c: n for c, n in counts.items() if n}
    good = len(hit) == 1 and list(hit.values())[0] == 1
    ok &= good
    print(("OK   " if good else "FAIL ") + f"{hit}  OLD: {o[:110]}")
print("RESULT", "PASS" if ok else "FAIL")
