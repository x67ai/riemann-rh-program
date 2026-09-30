"""
lobes.py -- the lobe law for the C1 chain on the critical line.

Theorem D (proved in NOTE.md): xi_N(1/2+it) = Xi(t) + P_N(t) with
    P_N(t) = (1/2)(1/4 + t^2) sum_{n>N} g_n(1/2+it) > 0   for all real t
(each g_n(1/2+it) is the cosine transform of a positive, decreasing, convex kernel; Polya's criterion).
Hence every real zero of xi_N lies in an open NEGATIVE lobe of Xi, and each negative lobe carries an
even number of them.  This script:
  (a) checks P_N(t) > 0 numerically on a grid (a check of the theorem, not its proof);
  (b) lists the lobes of Xi between consecutive zeta zeros up to height T, with sign and depth;
  (c) for N = 1..Nmax, computes min over each negative lobe of xi_N (golden section), predicts the number
      of real zeros of xi_N as 2 x #{negative lobes where that min is < 0}, and compares with census counts;
  (d) prints, per N, the "departure lobe" (first negative lobe with no zeros) and the depth ratio there.
Usage: python lobes.py T Nmax
"""
import sys, json, time
import mpmath as mp
sys.path.insert(0, '.')
import stair as st

T = mp.mpf(sys.argv[1]) if len(sys.argv) > 1 else mp.mpf(320)
Nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 8
mp.mp.dps = 30
Z = st.Chain('zeta')


def Xi(t):
    s = mp.mpc(mp.mpf(1)/2, t)
    return (s*(s - 1)/2 * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)).real


def xiN(t, N):
    return Z.E_tail(mp.mpc(mp.mpf(1)/2, t), st.w_trunc(N)).real


def PN(t, N):
    s = mp.mpc(mp.mpf(1)/2, t)
    acc = mp.fsum(Z.T(s, n) for n in range(N + 1, N + 12))
    return ((mp.mpf(1)/4 + t*t)/2 * acc).real


def golden_min(f, a, b, it=60):
    g = (mp.sqrt(5) - 1)/2
    c, d = b - g*(b - a), a + g*(b - a)
    fc, fd = f(c), f(d)
    for _ in range(it):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - g*(b - a); fc = f(c)
        else:
            a, c, fc = c, d, fd
            d = a + g*(b - a); fd = f(d)
    return (c, fc) if fc < fd else (d, fd)


t0 = time.time()
gam = []
k = 1
while True:
    g = mp.zetazero(k).imag
    if g > T:
        break
    gam.append(g)
    k += 1
print(f'{len(gam)} zeta zeros up to {T}  ({time.time()-t0:.0f}s)')
# (a) P_N > 0 on a grid
worst = {}
for N in range(1, Nmax + 1):
    vals = [PN(mp.mpf(t)/4, N) for t in range(0, int(T*4) + 1, 7)]
    worst[N] = min(vals)
    print(f'N={N}: min P_N on grid t in [0,{T}] step 1.75 = {mp.nstr(worst[N], 5)}  (P_N(0) = {mp.nstr(vals[0], 5)}, P_N(T) = {mp.nstr(PN(T, N), 5)}, c_N = {mp.nstr(st.c_N(N), 5)})')
sys.stdout.flush()
# (b) lobes of Xi
lobes = []
edges = [mp.mpf(0)] + gam
for j in range(len(edges) - 1):
    a, b = edges[j], edges[j + 1]
    mid = (a + b)/2
    sg = mp.sign(Xi(mid))
    tstar, v = golden_min(lambda t: sg*(-Xi(t)), a, b, it=40)   # maximize |Xi|
    lobes.append({'a': a, 'b': b, 'sign': int(sg), 'tstar': tstar, 'depth': abs(v)})
neg = [L for L in lobes if L['sign'] < 0]
print(f'{len(lobes)} lobes, {len(neg)} negative  ({time.time()-t0:.0f}s)')
# (c),(d)
out = {'T': str(T), 'N': {}}
for N in range(1, Nmax + 1):
    pred = 0
    first_fail = None
    rows = []
    for L in neg:
        tmin, vmin = golden_min(lambda t: xiN(t, N), L['a'], L['b'], it=40)
        has = vmin < 0
        ratio = L['depth'] / PN(L['tstar'], N)
        rows.append((mp.nstr(L['a'], 8), mp.nstr(L['b'], 8), mp.nstr(ratio, 4), bool(has)))
        if has:
            pred += 2
        elif first_fail is None:
            first_fail = (L, ratio)
    out['N'][N] = {'predicted_real_zeros': pred,
                   'departure_lobe': [mp.nstr(first_fail[0]['a'], 10), mp.nstr(first_fail[0]['b'], 10)] if first_fail else None,
                   'depth_over_PN_at_departure': mp.nstr(first_fail[1], 5) if first_fail else None,
                   'lobes': rows}
    msg = f'N={N}: predicted real zeros = {pred}'
    if first_fail:
        L, r = first_fail
        msg += f'; first negative lobe without zeros: ({mp.nstr(L["a"], 8)}, {mp.nstr(L["b"], 8)}), depth/P_N = {mp.nstr(r, 4)}; 4(N+1)^2 = {4*(N+1)**2}'
    print(msg + f'  ({time.time()-t0:.0f}s)'); sys.stdout.flush()
json.dump(out, open(f'lobes_T{int(T)}.json', 'w'), indent=1)
print('saved')
