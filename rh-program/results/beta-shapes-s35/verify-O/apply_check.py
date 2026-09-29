# Check every OLD occurs exactly the expected number of times in NOTE.md, apply all to a scratch copy,
# and verify the result: no residual "≥ 2 residue"/"at least two residue", every NEW present.
import sys, os, hashlib
sys.path.insert(0, os.path.dirname(__file__))
from amendments import A
src = os.path.join(os.path.dirname(__file__), '..', 'NOTE.md')
t = open(src, encoding='utf-8').read()
print('NOTE.md sha256', hashlib.sha256(t.encode()).hexdigest())
ok = True
for i, kind, n, old, new in A:
    c = t.count(old)
    print(f'{i:5s} {kind:5s} expected {n} found {c}', 'OK' if c == n else 'MISMATCH')
    ok &= (c == n)
u = t
for i, kind, n, old, new in A:
    u = u.replace(old, new)
for i, kind, n, old, new in A:
    if new not in u: print('NEW missing after apply:', i); ok = False
res = [s for s in ('at least two residue characteristics', '≥ 2 residue characteristics') if s in u]
print('residual wrong phrases after apply:', res)
out = sys.argv[1] if len(sys.argv) > 1 else None
if out: open(out, 'w', encoding='utf-8').write(u); print('scratch copy written:', out, hashlib.sha256(u.encode()).hexdigest())
print('ALL OK' if ok and not res else 'PROBLEMS')
