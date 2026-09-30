"""
explore_line.py -- real zeros (on Re s = 1/2) of the C1 approximants xi_N, N = 1..8, for 0 < t <= T,
against the zeros of zeta; also the value of xi_N(1/2+it) - c_N at large t (predicted -> 0).
Usage: python explore_line.py T step
"""
import sys, time
import mpmath as mp
sys.path.insert(0, '.')
import stair as st

T = mp.mpf(sys.argv[1]) if len(sys.argv) > 1 else mp.mpf(230)
h = mp.mpf(sys.argv[2]) if len(sys.argv) > 2 else mp.mpf('0.05')
mp.mp.dps = 30
Z = st.Chain('zeta')
# zeta zeros up to T
zz = []
k = 1
while True:
    g = mp.zetazero(k).imag
    if g > T:
        break
    zz.append(g)
    k += 1
print(f'zeta zeros in (0,{T}]: {len(zz)}')
for N in range(1, 9):
    t0 = time.time()
    w = st.w_trunc(N)
    fr = lambda t: Z.E_tail(mp.mpc(mp.mpf(1)/2, t), w).real
    zs, susp = st.sign_change_zeros(fr, mp.mpf('0.5'), T, h)
    # match to zeta zeros
    dev = []
    for z in zs:
        j = min(range(len(zz)), key=lambda i: abs(zz[i] - z))
        dev.append((z, zz[j], z - zz[j]))
    cN = st.c_N(N)
    tail_vals = [(tt, fr(mp.mpf(tt))) for tt in (100, 200, 400, 1000)]
    print(f'--- N = {N}: {len(zs)} real zeros in (0.5,{T}]  ({time.time()-t0:.0f}s); c_N = {mp.nstr(cN, 10)}')
    if zs:
        print('    last real zero:', mp.nstr(zs[-1], 15), ' max |t_N - gamma| =', mp.nstr(max(abs(d[2]) for d in dev), 3))
        for (z, g, d) in dev[-4:]:
            print(f'      t = {mp.nstr(z, 18)}  vs gamma = {mp.nstr(g, 18)}  diff = {mp.nstr(d, 3)}')
    print('    xi_N(1/2+it)/c_N at t = 100, 200, 400, 1000:', [mp.nstr(v/cN, 8) for (tt, v) in tail_vals])
    print('    suspicious same-sign local minima of |xi_N| (t, value, neighbor):',
          [(mp.nstr(a, 8), mp.nstr(b, 3), mp.nstr(c, 3)) for (a, b, c) in susp if abs(b) < 1e-3*abs(c)][:6])
    sys.stdout.flush()
