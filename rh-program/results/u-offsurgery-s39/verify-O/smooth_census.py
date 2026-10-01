# smooth_census.py -- per decade: 47-smooth integers, how many are irreducible (A(d)=0), how many are g-primes (read-O, S40)
import numpy as np, heapq
a = np.memmap('/private/tmp/rh-s40-u-offsurgery/r08_1e9.a16', dtype='<u2', mode='r')
gp = np.fromfile('/private/tmp/rh-s40-u-offsurgery/r08_1e9.gp', dtype=np.dtype([('n','<u4'),('m','u1')]))['n']
P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]; X = 10**9
sm = [1]
for p in P:
    new = []
    for s in sm:
        v = s*p
        while v <= X: new.append(v); v *= p
    sm += new
sm = np.array(sorted(sm), dtype=np.int64)
G = np.isin(sm, gp.astype(np.int64))
av = a[sm].astype(np.int64); A = av - G.astype(np.int64)
print('decade  #47-smooth  #irreducible(A=0)  #g-primes  frac_gp_of_smooth  frac_gp_of_irreducible')
for k in range(0, 9):
    lo, hi = 10**k, 10**(k+1)
    msk = (sm > lo) & (sm <= hi) if k else (sm >= 2) & (sm <= hi)
    ns = int(msk.sum()); ni = int(((A == 0) & msk).sum()); ng = int((G & msk).sum())
    print(f'(1e{k},1e{k+1}]  {ns:9d}  {ni:9d}  {ng:7d}  {ng/ns:.5f}  {ng/max(ni,1):.4f}')
print('47-smooth g-primes > 1e8:', [int(x) for x in sm[G & (sm > 10**8)][:12]], '...')
