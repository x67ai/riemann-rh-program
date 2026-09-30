"""
u2_prod.py -- production fingerprint tables for an L-type function, real side and circle side.

Usage:  python3 u2_prod.py FUNC SIDE PBITS SIZE [P2BITS]
  FUNC in {zeta, chi4, dh, faq:a:q, eul:p}   (see make_logxi_* below)
  SIDE = real   : S-fraction al_1..al_{SIZE-1} of F(w) = -E'/E, E(w) = Xi(sqrt w); ball arithmetic (certified).
  SIDE = circle : lambda_1..lambda_{SIZE+1} (ball), m_n, Verblunsky alpha_0..alpha_{SIZE-1} by Levinson in
                  midpoint arithmetic at PBITS and P2BITS, plus Schur (independent) at PBITS; verified digits =
                  min(agreement Levinson(P) vs Levinson(P2), agreement Levinson(P) vs Schur(P)).
Completed functions (all satisfy Lambda(s) = Lambda(1 - s), real on the critical line):
  zeta : xi(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)
  chi4 : (4/pi)^{(s+1)/2} Gamma((s+1)/2) L(s, chi_4)            (odd character; zeros = those of L)
  dh   : (5/pi)^{(s+1)/2} Gamma((s+1)/2) f_DH(s)                (results/ccm-dh-test/dh.py conventions)
  faq  : xi(s) * (a/sqrt q + q^{s-1/2} + q^{1/2-s})             (= xi(s) q^{s-1/2} (1 + a q^{-s} + q^{1-2s}))
  eul  : xi(s) * (1 - p^{-s}) (1 - p^{s-1}) = faq with a = -(p+1)   (one Euler factor removed, symmetrized)
"""
import sys, os, json, time
from math import comb
sys.path.insert(0, os.path.dirname(__file__))
from flint import arb, arb_series, acb, acb_series, ctx
import fp_core as fc

FUNC = sys.argv[1]; SIDE = sys.argv[2]; P = int(sys.argv[3]); SIZE = int(sys.argv[4])
P2 = int(sys.argv[5]) if len(sys.argv) > 5 else int(P * 4 // 3)
here = os.path.dirname(os.path.abspath(__file__))
tabdir = os.path.join(os.path.dirname(here), 'tables')
tag = '%s_%s_P%d_S%d' % (FUNC.replace(':', '-'), SIDE, P, SIZE)
logf = open(os.path.join(here, 'u2_prod_%s.log' % tag), 'w')
def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True); logf.write(s + '\n'); logf.flush()

def log_completed(s, x, deflate_at_one=False):
    """log Lambda(s) as an arb_series in x, where s = s0 + x (s passed as arb_series).
    For zeta at s0 = 1 the pole is handled by deflation: (s-1) zeta(s) = 1 + (s-1) zeta_defl(s)."""
    half = arb(1) / 2
    if FUNC == 'zeta' or FUNC.startswith('faq') or FUNC.startswith('eul'):
        logpi = arb.pi().log()
        if deflate_at_one:
            base = half.log() + s.log() - (s / 2) * logpi + (s / 2).lgamma() + (1 + x * s.zeta(deflate=True)).log()
        else:
            # at s0 = 1/2: s(s-1) < 0 and zeta < 0
            base = half.log() + (s * (1 - s)).log() - (s / 2) * logpi + (s / 2).lgamma() + (-(s.zeta())).log()
        if FUNC.startswith('faq') or FUNC.startswith('eul'):
            parts = FUNC.split(':')
            if FUNC.startswith('faq'):
                a = arb(parts[1]); q = arb(parts[2])
            else:
                q = arb(parts[1]); a = -(q + 1)
            lq = q.log()
            u = (s - half) * lq
            fac = a / q.sqrt() + u.exp() + (-u).exp()
            # fac > 0 near the base point for a > 2 sqrt q ; for the Euler case fac < 0 at s0 = 1/2
            f0 = fac.coeffs()[0]
            if f0 < 0:
                fac = -fac
            base = base + fac.log()
        return base
    if FUNC in ('chi4', 'dh'):
        q = 4 if FUNC == 'chi4' else 5
        qq = arb(q)
        pre = ((s + 1) / 2) * (qq / arb.pi()).log() + ((s + 1) / 2).lgamma()
        if FUNC == 'chi4':
            # L(s, chi4) = 4^{-s} (zeta(s, 1/4) - zeta(s, 3/4))
            L = (-(s * qq.log())).exp() * (s.zeta(arb(1) / 4) - s.zeta(arb(3) / 4))
        else:
            s5 = arb(5).sqrt()
            kap = ((10 - 2 * s5).sqrt() - 2) / (s5 - 1)
            L = (-(s * qq.log())).exp() * (s.zeta(arb(1) / 5) + kap * s.zeta(arb(2) / 5)
                                           - kap * s.zeta(arb(3) / 5) - s.zeta(arb(4) / 5))
        c0 = L.coeffs()[0]
        if c0 < 0:
            L = -L
        return pre + L.log()
    raise ValueError(FUNC)

def mid(x):
    return arb(x.mid())

def rec(x, nd=60):
    return {'v': x.str(nd, radius=False), 'dig': fc.digits(x)}

ctx.prec = P
say('FUNC', FUNC, 'SIDE', SIDE, 'P', P, 'SIZE', SIZE, 'P2', P2)
t0 = time.time()
if SIDE == 'real':
    M = SIZE
    ctx.cap = 2 * M + 1
    x = arb_series([0, 1]); s = arb(1) / 2 + x
    c = log_completed(s, x).coeffs()
    say('series %.1fs; Lambda(1/2) = %s' % (time.time() - t0, c[0].exp().str(25)))
    odd_ok = all(c[k].contains(0) for k in range(1, 2 * M + 1, 2))
    say('FE check (odd coefficients contain 0):', odd_ok)
    sm = [None] + [((-1) ** (m + 1)) * m * c[2 * m] for m in range(1, M + 1)]
    say('s_1..s_3:', [v.str(25) for v in sm[1:4]])
    cm = [sm[m + 1] for m in range(0, M)]
    t1 = time.time()
    al = fc.sfrac_from_series(cm, M - 1, stop_on_zero=True)
    say('S-fraction %d coeffs in %.1fs' % (len(al), time.time() - t1))
    say('certified digits:', [(n, fc.digits(al[n - 1])) for n in (1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 999) if n <= len(al)])
    signs = ''.join('+' if a > 0 else ('-' if a < 0 else '?') for a in al)
    firstbad = next((n for n, ch in enumerate(signs, 1) if ch != '+'), None)
    say('first S-index with al_n not certified positive:', firstbad, ' sign string head:', signs[:80])
    a_j, b2_j = fc.jfrac_from_sfrac(al)
    jsg = ''.join('+' if v > 0 else ('-' if v < 0 else '?') for v in b2_j)
    say('first J-index with b_n^2 not certified positive:', next((n for n, ch in enumerate(jsg, 1) if ch != '+'), None))
    out = {'func': FUNC, 'P_bits': P, 'M': M, 'Lambda_half': rec(c[0].exp()),
           's': [None] + [rec(v) for v in sm[1:]], 'al': [rec(v) for v in al],
           'a': [rec(v) for v in a_j], 'b2': [rec(v) for v in b2_j], 'al_signs': signs, 'b2_signs': jsg}
else:
    N = SIZE
    def circle_inputs(prec):
        ctx.prec = prec
        ctx.cap = N + 3
        w = arb_series([0, 1]); s1 = 1 + w
        d = log_completed(s1, w, deflate_at_one=(FUNC == 'zeta' or FUNC.startswith('faq') or FUNC.startswith('eul'))).coeffs()
        lam = [arb(0)] + [n * sum((arb(comb(n - 1, j - 1)) * d[j] for j in range(1, n + 1)), arb(0)) for n in range(1, N + 2)]
        mm = [lam[n + 1] - 2 * lam[n] + (lam[1] if n == 0 else lam[n - 1]) for n in range(0, N + 1)]
        return lam, mm
    def levinson_mid(m, nmax):
        phi = [arb(1)]; h = mid(m[0]); alpha = []
        for n in range(0, nmax):
            r = mid(sum((phi[k] * m[k + 1] for k in range(n + 1)), arb(0)))
            a = mid(r / h); alpha.append(a)
            zphi = [arb(0)] + phi; star = list(reversed(phi)) + [arb(0)]
            phi = [mid(zphi[k] - a * star[k]) for k in range(n + 2)]
            h = mid(h * (1 - a * a))
        return alpha
    def schur_mid(m, nmax):
        L = len(m)
        F = [arb(1)] + [mid(2 * m[k] / m[0]) for k in range(1, L)]
        ctx.cap = L
        Fs = arb_series(F)
        num = (Fs - 1).coeffs()
        ctx.cap = L - 1
        f = arb_series([mid(v) for v in num[1:]]) / arb_series((Fs + 1).coeffs()[:L - 1])
        gam = []; cur = L - 1
        for k in range(nmax):
            fcs = [mid(v) for v in f.coeffs()]
            g0 = fcs[0]; gam.append(g0)
            if cur < 2:
                break
            ctx.cap = cur
            fser = arb_series(fcs)
            numer = (fser - g0).coeffs(); denom = (1 - g0 * fser).coeffs()
            cur -= 1; ctx.cap = cur
            f = arb_series([mid(v) for v in numer[1:cur + 1]]) / arb_series([mid(v) for v in denom[:cur]])
        return gam
    lam, mm = circle_inputs(P)
    say('inputs %.1fs; lambda_1 = %s' % (time.time() - t0, lam[1].str(25)))
    say('lambda certified digits at n = 1, 100, 500, N:', [fc.digits(lam[n]) for n in (1, min(100, N), min(500, N), N)])
    lneg = [n for n in range(1, N + 2) if not (lam[n] > 0)]
    say('lambda_n not certified positive at:', lneg[:10])
    t1 = time.time(); ctx.prec = P
    A1 = levinson_mid([mid(v) for v in mm], N)
    say('Levinson(P) %.1fs' % (time.time() - t1))
    t1 = time.time()
    G1 = schur_mid([mid(v) for v in mm], N)
    say('Schur(P) %.1fs' % (time.time() - t1))
    t1 = time.time()
    lam2, mm2 = circle_inputs(P2)
    ctx.prec = P2
    A2 = levinson_mid([mid(v) for v in mm2], N)
    say('Levinson(P2) %.1fs' % (time.time() - t1))
    ctx.prec = P2
    def agree(a, b):
        d = abs(a - b)
        if d == 0:
            return int(P * 0.30103)
        q = d / abs(b)
        return max(0, int(-float(q.log().mid()) / 2.302585093))
    ver = [min(agree(A1[n], A2[n]), agree(A1[n], G1[n]) if n < len(G1) else 0) for n in range(len(A1))]
    say('verified digits of alpha_n at n = 0, 100, 200, ...:', [(n, ver[n]) for n in (0, 100, 200, 300, 400, 500, 600, 700, 800) if n < len(ver)])
    ctx.prec = P
    bad = [n for n in range(len(A1)) if ver[n] < 5 or not (abs(A1[n]) < 1)]
    say('indices with |alpha_n| >= 1 or < 5 verified digits:', bad[:10])
    out = {'func': FUNC, 'P_bits': P, 'P2_bits': P2, 'N': N,
           'lambda': [None] + [rec(v) for v in lam[1:]],
           'm': [rec(v) for v in mm],
           'alpha': [{'v': A1[n].str(60, radius=False), 'dig': ver[n]} for n in range(len(A1))]}
with open(os.path.join(tabdir, '%s.json' % tag), 'w') as fh:
    json.dump(out, fh)
say('saved tables/%s.json  total %.1fs' % (tag, time.time() - t0))
