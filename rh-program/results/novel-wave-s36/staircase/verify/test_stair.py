"""
test_stair.py -- validation of stair.py before any census rests on it.
 (1) zeta chain: E_tail vs E_direct (the latter at raised precision) for N = 1, 2, 3, 6 at complex s.
 (2) each control's full theta split (all k, weights 1) against its independently computed completed
     function (zeta; Hurwitz-zeta DH as in results/ccm-dh-test/dh.py; mpmath.dirichlet for chi_4;
     zeta times (q^s + a + q^{1-s}) for F_{a,q}); this checks the normalizations Q, kap, C and the
     modular relation of each theta series.
 (3) the F_{a,q} off-line zeros: s = 1/2 +- arccosh(a/(2 sqrt q))/ln q + i pi (2j+1)/ln q are zeros of E_full.
 (4) the functional equation E(1-s) = E(s) and reality on the line for chain members.
"""
import sys
import mpmath as mp
sys.path.insert(0, '.')
import stair as st

mp.mp.dps = 40
pts = [mp.mpc('0.5', '14.5'), mp.mpc('0.9', '33.3'), mp.mpc('3.5', '71.2'), mp.mpc('-2.2', '5.1'),
       mp.mpc('25', '140'), mp.mpc('0.5', '190.7')]

print('=== (1) zeta chain: tail vs direct ===')
Z = st.Chain('zeta')
for N in (1, 2, 3, 6):
    for s in pts:
        mp.mp.dps = 40
        et = Z.E_tail(s, st.w_trunc(N))
        with mp.workdps(160):
            ed = Z.E_direct(mp.mpc(s), st.w_trunc(N), N)
        rel = abs(et - ed)/abs(ed)
        print(f'N={N} s={mp.nstr(s, 8):>22}: E_tail={mp.nstr(et, 18):>45}  rel.diff(tail,direct@160)={mp.nstr(rel, 3)}')

print('=== (2) full theta split vs independent completed function ===')
ctrls = [('zeta', st.Chain('zeta')), ('chi4', st.Chain('chi4')), ('DH', st.Chain('DH')),
         ('F(a=3,q=2)', st.Chain('Faq', a=3, q=2)), ('F(a=2.9,q=2)', st.Chain('Faq', a='2.9', q=2)),
         ('F(a=4,q=3)', st.Chain('Faq', a=4, q=3))]
for name, C in ctrls:
    worst = mp.mpf(0)
    for s in [mp.mpc('0.5', '14.5'), mp.mpc('0.9', '33.3'), mp.mpc('3.5', '21.2'), mp.mpc('-2.2', '5.1'),
              mp.mpc('0.7', '85.6')]:
        mp.mp.dps = 50
        full = C.E_full(s)
        kmax = int(mp.sqrt(70 * C.Q / mp.pi * mp.log(10))) + 12
        with mp.workdps(120):
            ser = C.E_direct(mp.mpc(s), lambda k: 1, kmax)
        rel = abs(full - ser)/abs(full)
        worst = max(worst, rel)
        print(f'{name:>13} s={mp.nstr(s, 6):>14}: full={mp.nstr(full, 15):>40}  rel.diff(series)={mp.nstr(rel, 3)}')
    print(f'{name:>13}: worst rel.diff = {mp.nstr(worst, 3)}')

print('=== (3) F_{a,q} off-line zeros from the factor q^s + a + q^{1-s} ===')
for (a, q) in (('3', 2), ('2.9', 2), ('4', 3)):
    C = st.Chain('Faq', a=a, q=q)
    mp.mp.dps = 40
    A = mp.mpf(a)
    dlt = mp.acosh(A/(2*mp.sqrt(q)))/mp.log(q)
    for j in range(3):
        s0 = mp.mpc(mp.mpf(1)/2 + dlt, mp.pi*(2*j + 1)/mp.log(q))
        fac = mp.mpf(q)**s0 + A + mp.mpf(q)**(1 - s0)
        print(f'a={a} q={q} j={j}: s0 = {mp.nstr(s0, 20)}  |q^s+a+q^(1-s)| = {mp.nstr(abs(fac), 3)}  |E_full(s0)| = {mp.nstr(abs(C.E_full(s0)), 3)}  (Re s0 - 1/2 = {mp.nstr(dlt, 12)})')

print('=== (4) symmetry of chain members ===')
for name, C in ctrls:
    mp.mp.dps = 40
    s = mp.mpc('0.83', '17.9')
    w = st.w_trunc(3)
    e1 = C.E_tail(s, w)
    e2 = C.E_tail(1 - s, w)
    e3 = C.E_tail(mp.mpc('0.5', '17.9'), w)
    print(f'{name:>13}: |E(s)-E(1-s)|/|E(s)| = {mp.nstr(abs(e1-e2)/abs(e1), 3)} ; Im/|.| on line = {mp.nstr(abs(e3.imag)/abs(e3), 3)}')
