#!/usr/bin/env python3
"""CHECK-O quote check (checker-written, Session 36): every double-quoted string of 25+ characters in FIDELITY.md,
PREDERIVATION-ERRATA.md, BUILD-NOTES.md, the challenge header and the yaml row (aa) is split at ellipses and each fragment (12+ chars)
is searched, whitespace-normalized, in NOTE.md, read-O.md, UNIT-BRIEF.md and the challenge file. Fragments found nowhere are printed."""
import re, pathlib
RP = pathlib.Path("/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program")
srcs = [RP/"results/beta-shapes-s35/NOTE.md", RP/"results/beta-shapes-s35/read-O.md", RP/"results/theoremR-lean-s36/UNIT-BRIEF.md",
        RP/"lean/comparator/Challenge/ResidueRank.lean", RP/"results/theoremR-lean-s36/typing-probe.lean"]
norm = lambda s: " ".join(s.replace("**", "").split())
corpus = [norm(p.read_text(encoding="utf-8")) for p in srcs]
targets = [RP/"results/theoremR-lean-s36/FIDELITY.md", RP/"results/theoremR-lean-s36/PREDERIVATION-ERRATA.md",
           RP/"results/theoremR-lean-s36/BUILD-NOTES.md", RP/"lean/comparator/Challenge/ResidueRank.lean"]
yaml = (RP/"lean/formalization.yaml").read_text(encoding="utf-8")
i0 = yaml.index("(aa) [Session 36"); i1 = yaml.index("\nreview:", i0)
texts = [(p.relative_to(RP), p.read_text(encoding="utf-8")) for p in targets] + [("lean/formalization.yaml row (aa)", yaml[i0:i1])]
tot = found = 0
for name, t in texts:
    nt = norm(t)
    for m in re.finditer(r"\"([^\"]*)\"", nt):   # pair quotes sequentially FIRST, then filter by length (run 1 filtered inside
        q = m.group(1)                              # the regex and so mis-paired quotes around every short quotation)
        if len(q) < 25: continue
        for frag in re.split(r"…|\.\.\.", q):
            frag = frag.strip(" ,;:.()")
            if len(frag) < 12: continue
            tot += 1
            hit = [srcs[k].name for k, c in enumerate(corpus) if frag in c]
            if hit: found += 1
            else: print(f"NOT FOUND  {name}: \"{frag[:160]}\"")
print(f"fragments checked: {tot}; found verbatim in a source: {found}; not found: {tot - found}")
