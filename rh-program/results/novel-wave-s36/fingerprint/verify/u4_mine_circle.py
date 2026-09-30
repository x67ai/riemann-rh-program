"""
u4_mine_circle.py -- mine the circle-side table of zeta (Li coefficients, Toeplitz moments, Verblunsky alpha_n).

(1) first values; (2) sign pattern alpha_n ~ (-1)^n (1 - eps_n), law eps_n ~ W(n/2pi)^2/(32 n^2)?;
(3) Szego-Geronimus identity: the Verblunsky data of sigma are the Jacobi data of the Szego push-forward
    mu_Sz = sum 4 v delta_v, v = 1/(2|rho|^2), i.e. the S-fraction of the SHIFTED real problem
    F~(w) = sum_{gamma>0} 1/(1/4 + gamma^2 - w) (expansion of log xi at s = 1 in w = s(1-s)).
    Route A: alpha_n -> Geronimus relations -> Jacobi (B_n, A_n^2) on [-2,2].
    Route B: log xi(1+u) series (Arb) -> compose u = u(w), w = -u(1+u) -> s~_m -> S-fraction al~_n ->
             J(2cos) = 2I - 2 J_v with J_v the contraction of al~_n/2.
    Agreement of A and B = the seed's family (ii) is family (i) at the shifted point, up to Szego's map.
"""
import sys, os, json
from math import comb
import mpmath as mp
sys.path.insert(0, os.path.dirname(__file__))
from flint import arb, arb_series, ctx
import fp_core as fc
here = os.path.dirname(os.path.abspath(__file__))
tabdir = os.path.join(os.path.dirname(here), 'tables')
logf = open(os.path.join(here, 'u4_mine_circle.log'), 'w')
def say(*a):
    t = ' '.join(str(x) for x in a); print(t, flush=True); logf.write(t + '\n'); logf.flush()
mp.mp.dps = 60
C = json.load(open(os.path.join(tabdir, 'zeta_circle_P24000_S1000.json')))
lam = [None] + [mp.mpf(r['v']) for r in C['lambda'][1:]]
al = [mp.mpf(r['v']) for r in C['alpha']]
say('lambda_1..lambda_10:', [mp.nstr(x, 16) for x in lam[1:11]])
say('lambda_100, 500, 1000:', mp.nstr(lam[100], 16), mp.nstr(lam[500], 16), mp.nstr(lam[1000], 16))
say('Verblunsky alpha_0..alpha_11:', [mp.nstr(x, 16) for x in al[:12]])
sgn_ok = all((al[n] > 0) == (n % 2 == 0) for n in range(len(al)))
say('sign pattern alpha_n = (-1)^n |alpha_n| for all n <= 999:', sgn_ok)
def W(n):
    return mp.re(mp.lambertw(mp.mpf(n) / (2 * mp.pi)))
say('eps_n = 1 - |alpha_n| vs W(n/2pi)^2/(32 n^2):')
for n in (10, 50, 100, 200, 400, 600, 800, 998, 999):
    e = 1 - abs(al[n]); pred = W(n) ** 2 / (32 * n * n)
    say('  n=%d eps=%s  pred=%s  ratio=%s' % (n, mp.nstr(e, 10), mp.nstr(pred, 10), mp.nstr(e / pred, 6)))

# ---- Route A: Geronimus relations (Simon OPUC Thm 13.1.7), measure on [-2,2], x = 2 cos theta:
# b_{n+1} = (1 - a_{2n-1}) a_{2n} - (1 + a_{2n-1}) a_{2n-2}
# a_{n+1}^2 = (1 - a_{2n-1}) (1 - a_{2n}^2) (1 + a_{2n+1}),  with alpha_{-1} = -1.
def A(k):
    return mp.mpf(-1) if k == -1 else al[k]
Bn = []; An2 = []
for n in range(0, 200):
    Bn.append((1 - A(2 * n - 1)) * A(2 * n) - (1 + A(2 * n - 1)) * A(2 * n - 2) if n >= 1 else None)
    An2.append((1 - A(2 * n - 1)) * (1 - A(2 * n) ** 2) * (1 + A(2 * n + 1)))
# Simon's b_{n+1} for n = 0: b_1 = alpha_0 - ... use the formula with alpha_{-2}? For n = 0: b_1 = (1 - alpha_{-1}) alpha_0 - (1 + alpha_{-1}) alpha_{-2} = 2 alpha_0.
Bn[0] = 2 * A(0)

# ---- Route B: shifted real side from log xi(1+u)
P = 12000
ctx.prec = P
Ms = 420
ctx.cap = Ms + 2
u = arb_series([0, 1])
half = arb(1) / 2; logpi = arb.pi().log()
s1 = 1 + u
logxi1 = half.log() + s1.log() - (s1 / 2) * logpi + (s1 / 2).lgamma() + (1 + u * s1.zeta(deflate=True)).log()
# u as a series in w: w = -u - u^2  ->  u = (-1 + sqrt(1 - 4w))/2
w = arb_series([0, 1])
uw = ((1 - 4 * w).sqrt() - 1) / 2
comp = logxi1(uw) if hasattr(logxi1, '__call__') else None
cw = comp.coeffs()
# log Ẽ(w) = log xi; -d/dw log Ẽ = sum s~_{m+1} w^m ; s~_{m} = -m [w^m] log Ẽ
st = [None] + [-(m) * cw[m] for m in range(1, Ms + 1)]
say('\nRoute B: s~_1 = sum 1/(1/4+gamma^2) =', st[1].str(25), ' (expect lambda_1 = 0.0230957089661...)')
alt = fc.sfrac_from_series([st[m + 1] for m in range(0, Ms)], Ms - 1)
say('shifted S-fraction: %d coeffs, certified digits at n=1, 100, 300, 400:' % len(alt), [fc.digits(alt[n - 1]) for n in (1, 100, 300, 400) if n <= len(alt)])
# J_v: contraction of alt/2 ; J(2cos) = 2 I - 2 J_v
half_al = [x / 2 for x in alt]
aJ, b2J = fc.jfrac_from_sfrac(half_al)
diffB = []; diffA = []
for n in range(1, 150):
    # Route A index n (b_n, a_n^2 in Simon: b_1..; a_1..) vs Route B: diag 2 - 2 aJ[n-1], offdiag^2 4 b2J[n-1]
    bB = 2 - 2 * mp.mpf(aJ[n - 1].str(50, radius=False))
    aB = 4 * mp.mpf(b2J[n - 1].str(50, radius=False))
    bA = Bn[n - 1]; aA = An2[n]  # try the natural alignment; report both relative diffs
    diffB.append(abs(bA - bB) / abs(bB)); diffA.append(abs(aA - aB) / abs(aB))
say('Szego-Geronimus check (n = 1..149): max rel diff diagonal = %s, off-diagonal^2 = %s'
    % (mp.nstr(max(diffB), 3), mp.nstr(max(diffA), 3)))
say('   first 3 diag A/B:', [(mp.nstr(Bn[n - 1], 12), mp.nstr(2 - 2 * mp.mpf(aJ[n - 1].str(40, radius=False)), 12)) for n in (1, 2, 3)])
say('   first 3 offd^2 A/B:', [(mp.nstr(An2[n], 12), mp.nstr(4 * mp.mpf(b2J[n - 1].str(40, radius=False)), 12)) for n in (1, 2, 3)])
json.dump({'szego_max_rel_diag': mp.nstr(max(diffB), 3), 'szego_max_rel_offd': mp.nstr(max(diffA), 3),
           'sign_pattern_ok': sgn_ok}, open(os.path.join(here, 'u4_mine_circle.json'), 'w'), indent=1)
