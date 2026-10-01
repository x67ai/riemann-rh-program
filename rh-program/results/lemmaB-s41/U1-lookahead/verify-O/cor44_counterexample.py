# read-O, F1: Q' = N plus one extra g-prime q = 1 + tau/rho (tau = 1/100, rho = pi/4). Elements q^j * n (j >= 0, n in N).
# Checks inf E_rho(u-) over u <= U (E decreases between jumps, so the infimum is at left limits of jump points and on [1, q)),
# and |N(x) - x/(1-1/q)| <= O(log x) (beta(Q') = 0). Exact rationals for the rational parts; mpmath 50 digits for q^j.
import mpmath as mp
mp.mp.dps = 50
rho = mp.pi/4; tau = mp.mpf(1)/100; q = 1 + tau/rho; U = 10000
vals = []
j = 0; qj = mp.mpf(1)
while qj <= U:
    n = 1
    while qj*n <= U: vals.append(qj*n); n += 1
    j += 1; qj *= q
vals.sort()
infE = mp.mpf(10); cnt = 0; worst = None
for i, v in enumerate(vals):
    Eleft = cnt - rho*(v - 1) - 1          # E(v-) with cnt elements below v (multiplicities handled: equal values counted next)
    if i > 0 and v != vals[i-1]:          # i = 0 is the unit at u = 1 (E(1) = 0; u >= 1 only)
        if Eleft < infE: infE = Eleft; worst = v
    cnt += 1
print(f"q = {mp.nstr(q, 12)}; elements <= {U}: {len(vals)}; inf over left limits of E_rho = {mp.nstr(infE, 10)} at u = {mp.nstr(worst, 10)} (E(1)=0; on [1,q) inf = -rho(q-1) = {mp.nstr(-rho*(q-1), 10)})")
rp = 1/(1 - 1/q)
for X in [10, 100, 1000, 10000]:
    NX = sum(1 for v in vals if v <= X)
    print(f"X={X}: N={NX}  rho'X = {mp.nstr(rp*X, 10)}  N - rho'X = {mp.nstr(NX - rp*X, 6)}  log X/log q = {mp.nstr(mp.log(X)/mp.log(q), 6)}")
