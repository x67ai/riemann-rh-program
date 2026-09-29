"""CHECK-O tool (Opus 5, Session 32): compare the BRIEF §0 statements and the BRIEF §1(4) label with the shipped files,
whitespace-normalized for the statements and character for character for the label.  usage: brief_identity.py <rh-program>"""
import re, sys, os
R = sys.argv[1]
brief = open(os.path.join(R, "results/h5-c2-lean-s32/BRIEF.md"), encoding="utf-8").read()
norm = lambda s: re.sub(r"\s+", " ", s).strip()
def stmt(path, name):
    s = open(os.path.join(R, path), encoding="utf-8").read()
    m = re.search(r"^theorem " + re.escape(name) + r"\s*:\s*(.*?)\s*:=", s, re.S | re.M)
    return norm(m.group(1))
for name, topic in [("weilContainment_c2_interpolant", "WeilContainmentC2"), ("weilContainment_c2_interpolant_log3", "WeilContainmentC2One")]:
    m = re.search(r"`" + re.escape(name) + r" : (.*?)`", brief, re.S)
    b = norm(m.group(1)); c = stmt("lean/comparator/Challenge/%s.lean" % topic, name)
    print(name); print("  brief    :", b); print("  challenge:", c); print("  ->", "IDENTICAL" if b == c else "DIFFER")
    if b != c:
        i = next(i for i in range(min(len(b), len(c))) if b[i] != c[i]); print("  first difference at char", i, repr(b[i-10:i+20]), "vs", repr(c[i-10:i+20]))
label = re.search(r'exactly the reader\'s A7: "(.*?)"', brief).group(1)
print("\nlabel (BRIEF §1(4)):", label)
files = ["results/h5-c2-lean-s32/BUILD-NOTES.md", "results/h5-c2-lean-s32/FIDELITY.md", "lean/README.md", "lean/formalization.yaml",
         "results/d5-lean-s30/FIDELITY.md", "lean/comparator/Challenge/WeilContainmentC2.lean", "lean/comparator/Challenge/WeilContainmentC2One.lean"]
for f in files:
    raw = open(os.path.join(R, f), encoding="utf-8").read()
    exact = raw.count(label); normed = norm(raw.replace("**", "")).count(label)
    print("  %-55s exact occurrences %d; after joining wrapped lines %d" % (f, exact, normed))
