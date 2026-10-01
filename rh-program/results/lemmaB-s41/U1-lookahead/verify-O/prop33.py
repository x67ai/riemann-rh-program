# read-O (U1-lookahead), target (c): Prop. 3.3 (aligned bunching) reproduced at small scale, own code.
# P = greedy S8(rho), tau = 1/2, up to y0 (float64 sweep; decision margins reported). K := 2 max_{x<=y0} E_P(x)/x^theta.
# For j <= J: a_j = y0/p_j; the n_j = ceil(K a_j^theta / 4) primes of P nearest above a_j are moved to a_j (P').
# Control P'': the same primes moved by the same amount but to a_j*(1 + 0.37 j/J * 1e-2) (not aligned with y0/p_j).
# Reports (i) min_x (N_P' - N_P) >= 0, (ii) sup_{x<y0} |E_P'|/x^theta vs K, (iii) E_P'(y0) - E_P(y0) vs sum n_j,
# and the relative window widths H_j/a_j against delta0/2 (the hypothesis of (ii), not met at this scale).
import sys, math, heapq, bisect
import numpy as np
rho = eval(sys.argv[1], {"pi": math.pi}); y0 = float(sys.argv[2]); theta = float(sys.argv[3]); J = int(sys.argv[4])
t = 1/rho; tau = 0.5
def greedy_primes(X):
    P = []; past = [(1.0, -1)]; heap = []; n = 1; marg = 1.0
    while True:
        y = 1 + (n - 1 + tau)*t
        if heap: marg = min(marg, abs(heap[0][0] - y)/y)
        if heap and heap[0][0] <= y:
            v, lp = heapq.heappop(heap)
            if v > X: break
            n += 1
            for j in range(lp, len(P)):
                if P[j]*v > X: break
                heapq.heappush(heap, (P[j]*v, j))
            past.append((v, lp)); continue
        if y > X: break
        i = len(P); P.append(y)
        for (m, _) in past[1:]:
            if y*m <= X: heapq.heappush(heap, (y*m, i))
        if y*y <= X: heapq.heappush(heap, (y*y, i))
        n += 1; past.append((y, i))
    return P, marg
def gints(P, X):                          # all g-integers <= X of the multiset P (closure, with multiplicity)
    S = np.array([1.0])
    for p in sorted(P):
        parts = [S]; cur = S
        while True:
            cur = cur[cur*p <= X]*p
            if cur.size == 0: break
            parts.append(cur)
        S = np.concatenate(parts)
    return np.sort(S)
def Estats(S, X, th):
    n = np.arange(1, S.size + 1); Er = n - (rho*(S - 1) + 1); El = (n - 1) - (rho*(S - 1) + 1)
    sel = S < X; sl = sel & (S > 1)          # E(1-) = -1 is not part of the system (u >= 1)
    return Er, El, max((np.abs(Er[sel])/S[sel]**th).max(), (np.abs(El[sl])/S[sl]**th).max())
Xg = 1.02*y0
P, marg = greedy_primes(Xg)
SP = gints(P, Xg)
Er, El, _ = Estats(SP, y0, theta)
K = 2*Estats(SP, y0, theta)[2]
Pa = np.array(P); moved = []; Pnew = Pa.copy(); Pctl = Pa.copy(); Hrel = []
for j in range(1, J + 1):
    aj = y0/P[j - 1]; nj = math.ceil(K*aj**theta/4)
    k0 = bisect.bisect_left(P, aj); idx = list(range(k0, k0 + nj))
    Hrel.append((P[idx[-1]] - aj)/aj); moved.append((j, aj, nj))
    for k in idx: Pnew[k] = aj
    bj = aj*(1 + 0.5e-2*j/J); k1 = bisect.bisect_left(P, bj)      # control: same n_j, bunched at b_j (not y0/p_j)
    for k in range(k1, k1 + nj): Pctl[k] = bj
S1 = gints(list(Pnew), Xg); S2 = gints(list(Pctl), Xg)
grid = np.sort(np.concatenate([SP, S1, S2]))
NP = np.searchsorted(SP, grid, side='right'); N1 = np.searchsorted(S1, grid, side='right'); N2 = np.searchsorted(S2, grid, side='right')
E1r, E1l, r1 = Estats(S1, y0, theta); E2r, E2l, r2 = Estats(S2, y0, theta)
aJ = y0/P[J - 1]
def supr(S, a, b):
    sel = (S >= a) & (S < b); n = np.searchsorted(S, S[sel], side='right'); return ((n - (rho*(S[sel] - 1) + 1))/S[sel]**theta).max()
small = sorted(set(np.round(np.concatenate([[m*P[i] for i in range(J)] for m in SP[SP < P[J - 1]]]), 9)))
d0 = min((small[i + 1] - small[i])/small[i] for i in range(len(small) - 1))
def Eat(S, x): return np.searchsorted(S, x, side='right') - (rho*(x - 1) + 1)
def Emax(S, a, b):
    sel = (S >= a) & (S <= b); n = np.searchsorted(S, S[sel], side='right'); return (n - (rho*(S[sel] - 1) + 1)).max()
print(f"rho={rho:.6f} y0={y0:g} theta={theta} J={J}: pi(P)={len(P)} margin={marg:.2e} K={K:.4f} sum_j n_j={sum(m[2] for m in moved)}")
print(f"  bunches (j, a_j, n_j): {[(j, round(a, 2), n) for j, a, n in moved]}")
print(f"  window H_j/a_j (max) = {max(Hrel):.4f} vs delta0/2 = {d0/2:.2e}  (hypothesis of (ii) {'met' if max(Hrel) < d0/2 else 'NOT met at this scale'})")
print(f"  (i) min over grid of N_P' - N_P = {int((N1 - NP).min())}  (control: {int((N2 - NP).min())})")
print(f"  (ii) sup_(x<y0) |E|/x^theta: P {Estats(SP, y0, theta)[2]:.4f} (= K/2), P' {r1:.4f}, control {r2:.4f}; K = {K:.4f};"
      f" on [a_J, y0): P {supr(SP, aJ, y0):.4f}, P' {supr(S1, aJ, y0):.4f}, control {supr(S2, aJ, y0):.4f}")
print(f"  (iii) E(y0): P {Eat(SP, y0):.3f}, P' {Eat(S1, y0):.3f} (gain {Eat(S1, y0) - Eat(SP, y0):.0f} vs sum n_j {sum(m[2] for m in moved)}),"
      f" control {Eat(S2, y0):.3f}; max E on [y0, 1.01 y0]: P {Emax(SP, y0, 1.01*y0):.2f}, P' {Emax(S1, y0, 1.01*y0):.2f}, control {Emax(S2, y0, 1.01*y0):.2f}; K*y0^theta = {K*y0**theta:.3f}; (1/4)K y0^th sum p_j^-th = {0.25*K*y0**theta*sum(P[j]**-theta for j in range(J)):.3f}")
