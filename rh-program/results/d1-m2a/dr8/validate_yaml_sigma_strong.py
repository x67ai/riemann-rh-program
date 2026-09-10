#!/usr/bin/env python3
"""validate_yaml_sigma_strong.py -- Session 21 (2026-09-10), σ-strong sibling build: re-validate lean/formalization.yaml
with PyYAML + jsonschema against the upstream formalization.yaml schema.  The schema is taken from the on-disk copies
fetched by the D-R8 build (dr8/formalization.schema.dispatcher.json, v0.3.schema.json, v0.4.schema.json — hashes printed),
and the upstream files are re-fetched (3 attempts, 20 s each) to report whether the copies are still identical; the
validation itself never depends on the network.  Then every Zeta23.* name mentioned in status.main_results and
alignment.statements is checked to be declared in the mirror rh-program/lean (primed names handled: a name ending in an
apostrophe is matched with a lookahead, not \\b, which would miss it)."""
import json, hashlib, os, re, sys, time, urllib.request
import yaml, jsonschema
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BASE = "https://raw.githubusercontent.com/mathlib-initiative/formalization.yaml/main/schema/"
DISP = BASE + "formalization.schema.json"
def sha(b): return hashlib.sha256(b).hexdigest()
print("PyYAML %s, jsonschema %s" % (yaml.__version__, __import__("importlib.metadata").metadata.version("jsonschema")))
local = {DISP: "formalization.schema.dispatcher.json", BASE + "v0.3.schema.json": "v0.3.schema.json", BASE + "v0.4.schema.json": "v0.4.schema.json"}
store = {}
for url, fn in local.items():
    b = open(os.path.join(HERE, fn), "rb").read(); store[url] = json.loads(b)
    print("on-disk %-40s sha256 %s" % (fn, sha(b)))
    got = None
    for i in range(3):
        try:
            with urllib.request.urlopen(url, timeout=20) as r: got = r.read(); break
        except Exception as e:
            print("   upstream fetch attempt %d failed: %r" % (i + 1, e)); time.sleep(5)
    print("   upstream: %s" % ("IDENTICAL to the on-disk copy" if got is not None and sha(got) == sha(b) else ("DIFFERS (sha256 %s)" % sha(got) if got is not None else "unreachable in 3 attempts; validation uses the on-disk copy")))
disp = store[DISP]
doc = yaml.safe_load(open(os.path.join(ROOT, "lean/formalization.yaml"), encoding="utf-8"))
res = jsonschema.RefResolver(base_uri=DISP, referrer=disp, store=store)
V = jsonschema.validators.validator_for(disp)
errs = sorted(V(disp, resolver=res).iter_errors(doc), key=lambda e: list(e.path))
print("\nVALIDATION errors: %d" % len(errs))
for e in errs[:20]: print("   %s: %s" % (".".join(str(x) for x in e.path), e.message[:200]))
mr = doc["status"]["main_results"]; al = doc["alignment"]["statements"]
print("top-level keys: %s" % list(doc))
print("main_results: %d   alignment.statements: %d   fidelity.divergences: %d chars" % (len(mr), len(al), len(doc["fidelity"]["divergences"])))
src = {}
for dp, _, fs in os.walk(os.path.join(ROOT, "lean")):
    for fn in fs:
        if fn.endswith(".lean"):
            p = os.path.join(dp, fn); src[os.path.relpath(p, os.path.join(ROOT, "lean"))] = open(p, encoding="utf-8").read()
def declared(name):
    short = name.split(".")[-1]
    pat = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:private |protected |noncomputable |nonrec )*(?:theorem|lemma|def|abbrev|structure|inductive|instance)\s+%s(?![A-Za-z0-9_'])" % re.escape(short), re.M)
    return [f for f, t in src.items() if pat.search(t)]
names = set()
for item in mr + al:
    for m in re.finditer(r"\b(Zeta23(?:\.[A-Za-z0-9_']+)+)", json.dumps(item, ensure_ascii=False)): names.add(m.group(1).rstrip("."))
names = {n for n in names if "{" not in n}
missing = []
print("\nLean names referenced in status.main_results + alignment.statements: %d" % len(names))
for n in sorted(names):
    fs = declared(n); print("   %-56s %s" % (n, ", ".join(fs) if fs else "NOT DECLARED IN THE MIRROR"))
    if not fs: missing.append(n)
print("\nRESULT: %s" % ("PASS — errors: 0, undeclared names: 0" if not errs and not missing else "FINDINGS: %d schema error(s), %d undeclared name(s)" % (len(errs), len(missing))))
sys.exit(0 if (not errs and not missing) else 1)
