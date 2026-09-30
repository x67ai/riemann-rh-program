"""
u2_zeta_arb.py -- Unit 2: the fingerprint tables of zeta, in rigorous ball arithmetic (Arb via python-flint).

Usage: python3 u2_zeta_arb.py PBITS M N [tag]
  Real side:   log xi(1/2 + x) Taylor to x^{2M};  s_m = (-1)^{m+1} m c_{2m}  (m = 1..M);
               Stieltjes moments c_m = s_{m+1};  S-fraction al_n (n = 1..M-1) by Viskovatov;  J-fraction by contraction.
  Circle side: log xi(1 + w) Taylor to w^{N+1};  lambda_n = n sum_{j<=n} C(n-1,j-1) d_j  (n = 1..N+1);
               m_n = lambda_{n+1} - 2 lambda_n + lambda_{n-1};  Verblunsky alpha_n by Levinson AND by Schur (independent).
Every stored number is the midpoint to 40 digits plus its CERTIFIED digit count (from the Arb radius).
"""
import sys, os, json, time
from math import comb
sys.path.insert(0, os.path.dirname(__file__))
from flint import arb, arb_series, ctx
import fp_core as fc

P = int(sys.argv[1]); M = int(sys.argv[2]); N = int(sys.argv[3])
tag = sys.argv[4] if len(sys.argv) > 4 else 'P%d_M%d_N%d' % (P, M, N)
here = os.path.dirname(os.path.abspath(__file__))
tabdir = os.path.join(os.path.dirname(here), 'tables')
os.makedirs(tabdir, exist_ok=True)
log = open(os.path.join(here, 'u2_zeta_arb_%s.log' % tag), 'w')
def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True); log.write(s + '\n'); log.flush()

def rec(x, nd=40):
    return {'v': x.str(nd, radius=False), 'dig': fc.digits(x)}

ctx.prec = P
say('P bits', P, 'M', M, 'N', N)
half = arb(1) / 2
logpi = arb.pi().log()

# ---------------- real side ----------------
t0 = time.time()
L = 2 * M + 1
ctx.cap = L
x = arb_series([0, 1])
s = half + x
logxi = (half.log() + (arb(1) / 4 - x * x).log() - (s / 2) * logpi + (s / 2).lgamma() + (-(s.zeta())).log())
c = logxi.coeffs()
say('real side series done %.1fs' % (time.time() - t0))
xi_half = c[0].exp()
say('xi(1/2) =', xi_half.str(30), ' (expect 0.49712077818...)')
odd_ok = all(c[k].contains(0) for k in range(1, L, 2))
say('odd Taylor coefficients of log xi at 1/2 all contain 0 (FE check):', odd_ok,
    ' max odd |mid| radius-certified:', max(abs(c[k]).upper() for k in range(1, L, 2)).str(3))
sm = [None] + [((-1) ** (m + 1)) * m * c[2 * m] for m in range(1, M + 1)]
say('s_1 =', sm[1].str(30), ' s_2 =', sm[2].str(30))
cm = [sm[m + 1] for m in range(0, M)]
t1 = time.time()
al = fc.sfrac_from_series(cm, M - 1, stop_on_zero=True)
say('S-fraction: %d coefficients in %.1fs; first 6:' % (len(al), time.time() - t1), [a.str(15, radius=False) for a in al[:6]])
say('certified digits of al_n at n = 1, 50, 100, 200, ...:', [(n, fc.digits(al[n - 1])) for n in (1, 50, 100, 150, 200, 300, 400, 500, 600, 700, 800, 1000) if n <= len(al)])
nneg = [n for n, a in enumerate(al, 1) if not (a > 0)]
say('indices where al_n is NOT certified positive:', nneg[:10], '(of %d)' % len(al))
a_j, b2_j = fc.jfrac_from_sfrac(al)
realside = {
    'P_bits': P, 'M': M,
    'xi_half': rec(xi_half),
    's': [None] + [rec(v) for v in sm[1:]],
    'al': [rec(v) for v in al],
    'a': [rec(v) for v in a_j],
    'b2': [rec(v) for v in b2_j],
}
with open(os.path.join(tabdir, 'zeta_real_%s.json' % tag), 'w') as fh:
    json.dump(realside, fh)
say('saved tables/zeta_real_%s.json' % tag)

# ---------------- circle side (Li) ----------------
t0 = time.time()
Lc = N + 3
ctx.cap = Lc
w = arb_series([0, 1])
s1 = 1 + w
zdef = s1.zeta(deflate=True)
logxi1 = (half.log() + s1.log() - (s1 / 2) * logpi + (s1 / 2).lgamma() + (1 + w * zdef).log())
d = logxi1.coeffs()
say('circle side series done %.1fs' % (time.time() - t0))
lam = [arb(0)] + [n * sum((arb(comb(n - 1, j - 1)) * d[j] for j in range(1, n + 1)), arb(0)) for n in range(1, N + 2)]
lam1_closed = 1 + arb.const_euler() / 2 - (4 * arb.pi()).log() / 2
say('lambda_1 =', lam[1].str(30), ' closed form 1 + gamma/2 - log(4 pi)/2 =', lam1_closed.str(30), ' overlap:', lam[1].overlaps(lam1_closed))
say('lambda_2..5 =', [lam[n].str(20) for n in range(2, 6)])
mm = []
for n in range(0, N + 1):
    lm1 = lam[1] if n == 0 else lam[n - 1]
    mm.append(lam[n + 1] - 2 * lam[n] + lm1)
say('m_0 = 2 lambda_1 =', mm[0].str(25), '  m_1..m_4 =', [v.str(15) for v in mm[1:5]])
t1 = time.time()
alV, hV = fc.verblunsky_levinson(mm, N)
say('Levinson: %d coefficients in %.1fs' % (len(alV), time.time() - t1))
t1 = time.time()
Fco = [arb(1)] + [2 * mm[k] / mm[0] for k in range(1, N + 1)]
gS = fc.schur_parameters(Fco, N)
say('Schur: %d parameters in %.1fs' % (len(gS), time.time() - t1))
agree = [(n, alV[n].overlaps(gS[n])) for n in range(min(len(alV), len(gS)))]
say('Levinson and Schur balls overlap at every index:', all(o for _, o in agree), ' (n compared: %d)' % len(agree))
say('certified digits of Verblunsky alpha_n at n = 0, 50, 100, ...:', [(n, fc.digits(alV[n])) for n in (0, 50, 100, 150, 200, 300, 400, 500, 600, 800, 1000) if n < len(alV)])
say('first 8 alpha:', [v.str(15, radius=False) for v in alV[:8]])
bad = [n for n, v in enumerate(alV) if not (abs(v) < 1)]
say('indices where |alpha_n| < 1 is NOT certified:', bad[:10])
lneg = [n for n in range(1, N + 2) if not (lam[n] > 0)]
say('indices where lambda_n > 0 is NOT certified:', lneg[:10])
circ = {
    'P_bits': P, 'N': N,
    'lambda': [None] + [rec(v) for v in lam[1:]],
    'm': [rec(v) for v in mm],
    'alpha_levinson': [rec(v) for v in alV],
    'alpha_schur': [rec(v) for v in gS],
}
with open(os.path.join(tabdir, 'zeta_circle_%s.json' % tag), 'w') as fh:
    json.dump(circ, fh)
say('saved tables/zeta_circle_%s.json' % tag)
