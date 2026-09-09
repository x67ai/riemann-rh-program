#!/usr/bin/env python3
"""Job 2 (Opus): re-validate lean/formalization.yaml with PyYAML + jsonschema against the UPSTREAM
schema, fetched fresh in this run (retry loop, per the network rule), and check that every new
entry names a Lean declaration that actually exists in the built mirror.
"""
import json, hashlib, os, re, sys, time, urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
BASE = "https://raw.githubusercontent.com/mathlib-initiative/formalization.yaml/main/schema/"
DISP = BASE + "formalization.schema.json"

def fetch(url, tries=60):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return r.read()
        except Exception as e:
            print("   fetch %s attempt %d failed: %r" % (url, i + 1, e))
            time.sleep(60)
    raise SystemExit("could not fetch %s after %d tries" % (url, tries))

def sha(b):
    return hashlib.sha256(b).hexdigest()

import yaml, jsonschema
print("PyYAML %s, jsonschema %s" % (yaml.__version__, jsonschema.__version__))

raw = fetch(DISP)
disp = json.loads(raw)
print("dispatcher %s  sha256 %s" % (DISP, sha(raw)))
refs = sorted({m for m in re.findall(r'"\$ref"\s*:\s*"([^"]+)"', raw.decode())})
print("dispatcher $refs: %s" % refs)
store = {DISP: disp}
for r in refs:
    if r.startswith('#'):
        continue
    u = BASE + r
    b = fetch(u)
    store[u] = json.loads(b)
    print("fetched %s sha256 %s" % (u, sha(b)))
    # compare with the on-disk copies the builder used
    for local in ('results/d1-m2a/dr8/' + r, 'results/d1-m2a/packaging/' + r):
        p = os.path.join(ROOT, local)
        if os.path.isfile(p):
            same = sha(open(p, 'rb').read()) == sha(b)
            print("   on-disk copy %s: %s" % (local, "IDENTICAL to upstream" if same else "DIFFERS from upstream"))

dsha = sha(open(os.path.join(ROOT, 'results/d1-m2a/dr8/formalization.schema.dispatcher.json'), 'rb').read())
print("dr8 dispatcher copy: %s" % ("IDENTICAL to upstream" if dsha == sha(raw) else "DIFFERS from upstream (%s)" % dsha))

doc = yaml.safe_load(open(os.path.join(ROOT, 'lean/formalization.yaml'), encoding='utf-8'))
res = jsonschema.RefResolver(base_uri=DISP, referrer=disp, store=store)
V = jsonschema.validators.validator_for(disp)
errs = sorted(V(disp, resolver=res).iter_errors(doc), key=lambda e: list(e.path))
print("\nVALIDATION errors: %d" % len(errs))
for e in errs[:20]:
    print("   %s: %s" % ('.'.join(str(x) for x in e.path), e.message[:200]))

print("top-level keys: %s" % list(doc))
mr = doc['status']['main_results']
al = doc['alignment']['statements']
print("main_results: %d   alignment.statements: %d   fidelity.divergences: %d chars"
      % (len(mr), len(al), len(doc['fidelity']['divergences'])))

# every Lean name mentioned in the yaml must exist in the mirror
src = {}
for dirpath, _, files in os.walk(os.path.join(ROOT, 'lean')):
    for fn in files:
        if fn.endswith('.lean'):
            p = os.path.join(dirpath, fn)
            src[os.path.relpath(p, os.path.join(ROOT, 'lean'))] = open(p, encoding='utf-8').read()

def declared(name):
    short = name.split('.')[-1]
    pat = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private |protected |noncomputable |nonrec )*'
                     r'(?:theorem|lemma|def|abbrev|structure|inductive|instance)\s+%s\b' % re.escape(short), re.M)
    return [f for f, t in src.items() if pat.search(t)]

names = set()
for item in mr + al:
    blob = json.dumps(item)
    for m in re.finditer(r'\b(Zeta23(?:\.[A-Za-z0-9_\']+)+)\b', blob):
        names.add(m.group(1))
    for k in ('name', 'lean_name', 'statement_id', 'id'):
        if isinstance(item, dict) and isinstance(item.get(k), str) and re.fullmatch(r'[A-Za-z_][A-Za-z0-9_.\']*', item[k]):
            names.add(item[k])
print("\nLean names referenced in status.main_results + alignment.statements: %d" % len(names))
missing = []
for n in sorted(names):
    fs = declared(n)
    print("   %-52s %s" % (n, ", ".join(fs) if fs else "NOT DECLARED IN THE MIRROR"))
    if not fs:
        missing.append(n)

print("\nVERDICT: %s" % ("PASS" if not errs and not missing else "FINDINGS: %d schema error(s), %d undeclared name(s)" % (len(errs), len(missing))))
sys.exit(0 if (not errs and not missing) else 1)
