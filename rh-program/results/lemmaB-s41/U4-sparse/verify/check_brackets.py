#!/usr/bin/env python3
"""U4-sparse: checks of Prop. 3.3 on the dumps of run_brackets.sh (run in the scratch directory). For rho = pi/D:
idle-set inclusions i0 <= iS <= i1 (P^(1) ⊆ P ⊆ P^(2)) and i2 <= i1 (P^(3) ⊆ P^(2)), i0 <= i2 (P^(1) ⊆ P^(3)); queue brackets
e1 <= eS <= e2 <= e0 (where not saturated); first step where P^(j) differs from P, against p1^(j+2); max of each queue by decade."""
import sys, math, numpy as np
D = int(sys.argv[1]); rho = math.pi/D; t = 1/rho; p1 = 1 + t/2
i = {k: np.fromfile(f"br{D}_i{k}.u8", dtype=np.uint8).astype(bool) for k in ('0','1','2','3','S')}
e = {k: np.fromfile(f"br{D}_e{k}.u16", dtype=np.uint16).astype(np.int64) for k in ('0','1','2','3','S')}
n = min(len(v) for v in list(i.values()) + list(e.values()))
x = 1 + (np.arange(1, n+1) - 0.5)*t
print(f"## rho = pi/{D}, steps {n}, p1 = {p1:.4f}")
print("  inclusions (violations): P1⊆P", int(np.sum(i['0'][:n] & ~i['S'][:n])), " P⊆P2", int(np.sum(i['S'][:n] & ~i['1'][:n])),
      " P1⊆P3", int(np.sum(i['0'][:n] & ~i['2'][:n])), " P3⊆P2", int(np.sum(i['2'][:n] & ~i['1'][:n])))
ok = (e['0'][:n] < 65535) & (e['2'][:n] < 65535)
print("  queue brackets (violations): e1<=eS", int(np.sum(e['1'][:n] > e['S'][:n])), " eS<=e2", int(np.sum(e['S'][:n] > e['2'][:n])),
      " e2<=e0 (unsaturated)", int(np.sum((e['2'][:n] > e['0'][:n]) & ok)), " e3<=eS", int(np.sum(e['3'][:n] > e['S'][:n])))
for j, key in ((1,'0'), (2,'1'), (3,'2')):
    d = np.nonzero(i[key][:n] != i['S'][:n])[0]
    first = x[d[0]] if len(d) else float('inf')
    print(f"  P^({j}) first differs from P at x = {first:.4e}  (Prop. 3.3: not below p1^{j+2} = {p1**(j+2):.4e})")
for X in (1e5, 1e6, 1e7, 1e8, 1e9):
    m = x <= X
    if not m.any(): continue
    print(f"  x<= {X:.0e} (tau {rho*math.log(X):.3f}): max e0 {e['0'][:n][m].max()}  e1 {e['1'][:n][m].max()}  eS {e['S'][:n][m].max()}"
          f"  e2 {e['2'][:n][m].max()}  e3 {e['3'][:n][m].max()}")
