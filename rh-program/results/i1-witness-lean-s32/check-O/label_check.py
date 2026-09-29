# CHECK-O: compare the label, character for character, in every place it is quoted against BRIEF §1(4). Written by the checker.
import re, sys
RP = sys.argv[1]
brief = open(RP + "/results/i1-witness-lean-s32/BRIEF.md", encoding="utf-8").read()
m = re.search(r'\*\*\(4\) Label\*\*, only if everything lands with no displayed hypothesis: "(.*?)"\. Never', brief, re.S)
L = m.group(1); print("BRIEF label length", len(L))
norm = lambda s: re.sub(r"\s+", " ", s.replace("**", ""))
for f in ["results/i1-witness-lean-s32/BUILD-NOTES.md", "results/i1-witness-lean-s32/FIDELITY.md", "lean/README.md", "lean/formalization.yaml"]:
    t = norm(open(RP + "/" + f, encoding="utf-8").read())
    n = t.count(norm(L))
    # also count truncated quotations beginning with the label's opening words
    starts = t.count("I.1's witness table kernel-checked")
    print(f"{f}: exact(whitespace-normalized) occurrences = {n}; occurrences of the opening words = {starts}")
