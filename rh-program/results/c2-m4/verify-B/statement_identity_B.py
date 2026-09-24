"""statement_identity_B.py -- the challenge/solution statement-identity check for the Unit B topics (Session 25; byte copy of verify-A/statement_identity_A.py apart from this docstring):
for each theorem name, extract the text from `theorem <name>` up to (not including) the ` := ` that starts the proof, in
Challenge/<Topic>.lean and Solution/<Topic>.lean, and compare byte for byte.  usage: statement_identity_m4.py <root> <Topic> <names...>"""
import re, sys, os
root, topic, names = sys.argv[1], sys.argv[2], sys.argv[3:]
def stmt(path, name):
    s = open(path, encoding="utf-8").read()
    m = re.search(r"^theorem " + re.escape(name) + r"\b.*?(?=\s*:=)", s, re.S | re.M)
    return m.group(0) if m else None
ok = True
for n in names:
    a = stmt(os.path.join(root, "comparator/Challenge/%s.lean" % topic), n)
    b = stmt(os.path.join(root, "comparator/Solution/%s.lean" % topic), n)
    same = a is not None and a == b
    ok &= same
    print("%-45s challenge %5s bytes, solution %5s bytes: %s" % (n, len(a) if a else "none", len(b) if b else "none", "IDENTICAL" if same else "DIFFER"))
    if same: print("    " + a.replace("\n", "\n    "))
print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
