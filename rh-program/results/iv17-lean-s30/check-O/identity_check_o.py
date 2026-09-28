"""identity_check_o.py -- CHECKER's own statement-identity check (Opus 5, Session 30, G8/IntegralityGap).
Strips comments (nested block + line), splits each file into top-level declarations, normalizes whitespace, and compares
the statement (text before the first top-level ':=') of every challenge theorem with its solution namesake.
Also: config theorem_names == challenge theorem names in order; every challenge proof is exactly `by sorry`;
no declaration in the solution other than the challenge's theorems; imports of each file.
usage: identity_check_o.py <root> <Topic> <config>"""
import re, sys, os, json
root, topic, cfg = sys.argv[1:4]
def strip(src):
    out, i, n, depth = [], 0, len(src), 0
    while i < n:
        if src.startswith("/-", i): depth += 1; i += 2; continue
        if depth and src.startswith("-/", i): depth -= 1; i += 2; continue
        if depth: out.append("\n" if src[i] == "\n" else " "); i += 1; continue
        if src.startswith("--", i):
            while i < n and src[i] != "\n": i += 1
            continue
        out.append(src[i]); i += 1
    return "".join(out)
KW = r"^(?:theorem|lemma|def|abbrev|instance|axiom|opaque|structure|class|inductive|example|noncomputable def|private|protected|@\[)"
def decls(path):
    s = strip(open(path, encoding="utf-8").read())
    imports = re.findall(r"^import\s+(\S+)", s, re.M)
    parts = re.split(r"(?m)(?=" + KW + r")", s)
    ds = []
    for p in parts:
        m = re.match(r"(theorem|lemma|def|abbrev|instance|axiom|opaque|structure|class|inductive|example)\s+(\S+)?", p)
        if m: ds.append((m.group(1), m.group(2), p))
        elif re.match(KW, p): ds.append(("OTHER", None, p))
    return imports, ds
def stmt(text):
    i = text.find(":=")
    return " ".join(text[:i].split()), " ".join(text[i+2:].split())
ci, cd = decls(os.path.join(root, f"comparator/Challenge/{topic}.lean"))
si, sd = decls(os.path.join(root, f"comparator/Solution/{topic}.lean"))
ti, td = decls(os.path.join(root, f"comparator/ChallengeDeps/{topic}.lean"))
names = json.load(open(os.path.join(root, cfg)))["theorem_names"]
cn = [n for k, n, _ in cd if k == "theorem"]
print("imports: ChallengeDeps", ti, "| Challenge", ci, "| Solution", si)
print("challenge decl kinds:", sorted(set(k for k, _, _ in cd)), "count", len(cd))
print("solution  decl kinds:", sorted(set(k for k, _, _ in sd)), "count", len(sd))
print("trusted   decls:", [(k, n) for k, n, _ in td])
print("config names == challenge theorem names in order:", names == cn, len(names))
ok = names == cn and len(cd) == len(sd) == len(names)
sm = {n: t for k, n, t in sd}
for k, n, t in cd:
    a, pa = stmt(t); b, pb = stmt(sm.get(n, ":="))
    same = a == b
    ok &= same and pa == "by sorry"
    print(f"{n:32s} {'IDENTICAL' if same else 'DIFFER'}  challenge proof = {pa!r}  solution proof = {pb[:70]!r}")
print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
