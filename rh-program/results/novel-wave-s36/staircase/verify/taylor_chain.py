"""
taylor_chain.py -- chain C3b: F_h(s) = X(s+h) + X(s-h), h decreasing to 0, X a completed function with
X(1-s) = X(s) (so F_h(1-s) = F_h(s), F_h real on the line: F_h(1/2+it) = 2 Re X(1/2+h+it)).
Hermite-Biehler at level h:  |X(s+h)| > |X(s-h)| on Re s > 1/2  <=>  every zero rho of X has Re rho <= 1/2 + h
(pairing computation in NOTE.md); it implies all zeros of F_h are on the line.
QUESTION: is real-rootedness of F_h (in a window) strictly weaker than the zero-free region?  Decided on the
Davenport-Heilbronn function (off-line zero 0.808517182456637 + 85.699348485377592 i, delta = 0.3085...):
for h on a grid, count zeros of F_h in the box [1/2-1, 1/2+1] x [t1, t2] (argument principle) and real zeros
(sign changes on the line); h*_DH = smallest h on the grid with all zeros in the box real.
Controls: zeta in the same kind of window (RH-true: expect all real for every h > 0).
Usage: python taylor_chain.py
"""
import sys, json, time
import mpmath as mp
sys.path.insert(0, '.')
import stair as st

mp.mp.dps = 30


def make_F(C, h):
    h = mp.mpf(h)

    def F(s):
        s = mp.mpc(s)
        return C.E_full(s + h) + C.E_full(s - h)
    return F


def real_zero_count(F, t1, t2, step=mp.mpf('0.01')):
    n = int((t2 - t1)/step)
    prev = F(mp.mpc(mp.mpf(1)/2, t1)).real
    cnt = 0
    zs = []
    for j in range(1, n + 1):
        t = t1 + (t2 - t1)*mp.mpf(j)/n
        v = F(mp.mpc(mp.mpf(1)/2, t)).real
        if mp.sign(v) != mp.sign(prev):
            cnt += 1
            zs.append(t)
        prev = v
    return cnt, zs


def box_count(F, t1, t2, w=mp.mpf(1)):
    n, mn = st.count_zeros_rect(F, mp.mpf(1)/2 - w, mp.mpf(1)/2 + w, t1, t2, n0=48, dmax=0.4)
    return n


def hb_margin(C, h, t1, t2, ns=12, nt=120):
    """min over a grid of Re s in (1/2, 1.5], t in [t1,t2] of |X(s+h)|/|X(s-h)| - 1."""
    worst = None
    arg = None
    for i in range(1, ns + 1):
        sig = mp.mpf(1)/2 + mp.mpf(i)/ns
        for j in range(nt + 1):
            t = t1 + (t2 - t1)*mp.mpf(j)/nt
            s = mp.mpc(sig, t)
            r = abs(C.E_full(s + h))/abs(C.E_full(s - h)) - 1
            if worst is None or r < worst:
                worst, arg = r, s
    return worst, arg


if __name__ == '__main__':
    t00 = time.time()
    out = {}
    hs = ['0', '0.02', '0.05', '0.1', '0.15', '0.2', '0.25', '0.28', '0.3', '0.31', '0.33', '0.35', '0.4', '0.5', '0.75', '1.0']
    cases = [('DH', st.Chain('DH'), mp.mpf('80.3'), mp.mpf('91.7')),
             ('zeta', st.Chain('zeta'), mp.mpf('80.3'), mp.mpf('91.7'))]
    for (name, C, t1, t2) in cases:
        out[name] = []
        for hstr in hs:
            F = make_F(C, hstr)
            ntot = box_count(F, t1, t2)
            nre, zs = real_zero_count(F, t1, t2)
            rec = {'h': hstr, 'box_total': mp.nstr(ntot, 8), 'real': nre,
                   'offline_pairs_in_box': (int(mp.nint(ntot.real)) - nre)/2}
            if hstr in ('0.1', '0.2', '0.3', '0.31', '0.4', '0.5'):
                m, where = hb_margin(C, mp.mpf(hstr), t1, t2)
                rec['HB_margin_min'] = mp.nstr(m, 6)
                rec['HB_margin_argmin'] = mp.nstr(where, 8)
            out[name].append(rec)
            print(name, rec, f'({time.time()-t00:.0f}s)'); sys.stdout.flush()
    json.dump(out, open('taylor_chain.json', 'w'), indent=1)
    print('saved taylor_chain.json')
