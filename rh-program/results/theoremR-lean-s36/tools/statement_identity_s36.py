"""statement_identity_s36.py -- the H5/H4 statement-identity tool (results/h4-pair-lean-s33/tools/statement_identity_h4.py), same extraction,
extended for the Session-36 topic `ResidueRank` (theoremR-lean-s36 builder): for each theorem name, the text from `theorem <name>` up to (not
including) the ` := ` that starts the proof, compared byte for byte
  [A] Challenge/<Topic>.lean vs Solution/<Topic>.lean, under each root given;
  [B] Challenge/<Topic>.lean vs the typing probe;
  [C] the config's theorem_names (namespace prefix stripped) against the challenge's order of theorems;
  [D] the challenge from its line `import Mathlib` to the end vs the probe from its line `import Mathlib` to the end (whole-text identity).
usage: statement_identity_s36.py <Topic> <config.json> <probe.lean> <root1> [<root2> ...] -- <names...>"""
import re, sys, os, json
args = sys.argv[1:]
sep = args.index("--")
topic, config, probe, roots, names = args[0], args[1], args[2], args[3:sep], args[sep + 1:]
def stmt_text(s, name):
    m = re.search(r"^theorem " + re.escape(name) + r"\b.*?(?=\s*:=)", s, re.S | re.M)
    return m.group(0) if m else None
def stmt(path, name):
    return stmt_text(open(path, encoding="utf-8").read(), name)
ok = True
for root in roots:
    print("[A] challenge vs solution under", root)
    for n in names:
        a = stmt(os.path.join(root, "comparator/Challenge/%s.lean" % topic), n)
        b = stmt(os.path.join(root, "comparator/Solution/%s.lean" % topic), n)
        same = a is not None and a == b
        ok &= same
        print("%-32s challenge %5s bytes, solution %5s bytes: %s" % (n, len(a) if a else "none", len(b) if b else "none", "IDENTICAL" if same else "DIFFER"))
        if same: print("    " + a.replace("\n", "\n    "))
ch_path = os.path.join(roots[0], "comparator/Challenge/%s.lean" % topic)
print("[B] challenge (%s) vs probe (%s)" % (ch_path, probe))
for n in names:
    a = stmt(ch_path, n); b = stmt(probe, n)
    same = a is not None and a == b
    ok &= same
    print("%-32s challenge %5s bytes, probe %5s bytes: %s" % (n, len(a) if a else "none", len(b) if b else "none", "IDENTICAL" if same else "DIFFER"))
print("[C] config theorem_names order vs challenge order")
cfg = json.load(open(config, encoding="utf-8"))
cfg_names = [x.split(".")[-1] for x in cfg["theorem_names"]]
ch_names = re.findall(r"^theorem (\S+)", open(ch_path, encoding="utf-8").read(), re.M)
same = cfg_names == ch_names == names
ok &= same
print("config:   ", cfg["theorem_names"]); print("challenge:", ch_names); print("ORDER", "PASS" if same else "FAIL")
print("    permitted_axioms:", cfg["permitted_axioms"], " enable_nanoda:", cfg["enable_nanoda"], " modules:", cfg["challenge_module"], cfg["solution_module"])
print("[D] whole text from `import Mathlib` to the end: challenge vs probe")
cs = open(ch_path, encoding="utf-8").read(); ps = open(probe, encoding="utf-8").read()
ct = cs[cs.index("\nimport Mathlib\n") + 1:]; pt = ps[ps.index("\nimport Mathlib\n") + 1:]
same = ct == pt
ok &= same
print("challenge tail %d bytes, probe tail %d bytes: %s" % (len(ct.encode()), len(pt.encode()), "IDENTICAL" if same else "DIFFER"))
print("RESULT:", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
