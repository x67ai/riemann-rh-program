"""
u1_toys.py -- Unit 1: verify every equivalence on toy cases before touching zeta.

T1  real-rooted polynomial E(w) = prod_{k<=6} (1 - w/k^2): S-fraction positive, terminates at al_12 = 0 (exact).
T2  same with the pair {16, 25} replaced by a complex pair; the failure index predicted by Heine's formula
    (sign of Hankel dets as sums over atom subsets) must match the S/J-fraction sign pattern.
T3  E(w) = sin(sqrt w)/sqrt w: S-fraction al_n = 1/((2n+1)(2n+3)) exactly (Lambert/Gauss); exact rationals,
    then Arb at fixed precision to calibrate the precision loss per index (ill-conditioning law).
C1  circle: xi-like E(s) = prod ((s-1/2)^2 + g_k^2), all zeros on the line: Toeplitz/Verblunsky |alpha| < 1,
    terminating at |alpha_{2K-1}| = 1; Levinson vs Schur algorithm (independent) must agree;
    m_n from zeros vs m_n from Taylor series of log E at s = 1 (C(z) = 2E'/E(1/(1-z))) must agree.
C2  circle: one pair moved off the line -> Toeplitz positivity fails; report the index.
"""
import sys, os, json
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(__file__))
from flint import arb, acb, ctx, arb_series, acb_series, fmpq
import fp_core as fc
import mpmath as mp

out = {}

# ---------------- exact rational S-fraction (independent of Arb) ----------------
def sfrac_exact(c, nmax):
    """Exact Viskovatov on Fractions. Returns list al (stops at an exact zero)."""
    L = len(c)
    F = [x / c[0] for x in c]
    al = []
    for n in range(1, nmax + 1):
        if len(F) < 2:
            break
        # G = 1 - 1/F ; compute 1/F series
        inv = [Fr(0)] * len(F)
        inv[0] = 1 / F[0]
        for k in range(1, len(F)):
            s = sum((F[j] * inv[k - j] for j in range(1, k + 1)), Fr(0))
            inv[k] = -s / F[0]
        G = [(1 if k == 0 else 0) - inv[k] for k in range(len(F))]
        a = G[1]
        al.append(a)
        if a == 0:
            break
        F = [x / a for x in G[1:]]
    return al

# T1
zk = [Fr(k * k) for k in range(1, 7)]
c_T1 = [sum((1 / z) ** (m + 1) for z in zk) for m in range(30)]
al_T1 = sfrac_exact(c_T1, 20)
out['T1_al_exact'] = [str(a) if a.denominator < 10**6 else float(a) for a in al_T1]
out['T1_signs'] = ''.join('+' if a > 0 else ('0' if a == 0 else '-') for a in al_T1)
out['T1_terminates_at'] = len(al_T1)
print('T1 signs', out['T1_signs'], 'length', len(al_T1))

# T2: complex pair among 6 atoms; place the pair at depth r (r real atoms above it)
def c_from_zeros(zs, M):
    """zs: list of complex zeros w_k of E (conjugate pairs), c_m = sum w_k^{-(m+1)} (real)."""
    return [sum((1 / z) ** (m + 1) for z in zs).real for m in range(M)]

mp.mp.dps = 60
res_T2 = {}
for r, pair in [(0, (mp.mpc(0.6, 0.3))), (2, mp.mpc(10, 3)), (4, mp.mpc(30, 4)), (4, mp.mpc(30, 0.2))]:
    reals = [mp.mpf(k * k) for k in (1, 2, 3, 4, 5, 6)][:4]
    # choose r real atoms ABOVE the pair in y = 1/w (i.e. smaller w than the pair)
    zs = reals + [pair, mp.conj(pair)]
    c = c_from_zeros(zs, 16)
    # S-fraction via exact? c are floats here: use Arb at high precision
    ctx.prec = 400
    carb = [arb(mp.nstr(x, 110)) for x in c]
    al = fc.sfrac_from_series(carb, 12, stop_on_zero=True)
    a, b2 = fc.jfrac_from_sfrac(al)
    D0 = fc.hankel_dets(carb, 7, 0)
    # Heine prediction of sign(D0_n): sum over n-subsets of atoms of prod w * prod (y_i - y_j)^2, w = y
    import itertools
    ys = [1 / z for z in zs]
    heine = []
    for n in range(1, 7):
        s = mp.mpc(0)
        for S in itertools.combinations(range(6), n):
            t = mp.mpc(1)
            for i in S:
                t *= ys[i]
            for i, j in itertools.combinations(S, 2):
                t *= (ys[i] - ys[j]) ** 2
            s += t
        heine.append(s.real)
    nreal_above = sum(1 for y in ys[:4] if abs(y) > abs(ys[4]))
    res_T2[str(pair)] = {
        'real_atoms_above_pair': nreal_above,
        'al_signs': ''.join('+' if x > 0 else ('-' if x < 0 else '?') for x in al),
        'b2_signs': ''.join('+' if x > 0 else ('-' if x < 0 else '?') for x in b2),
        'hankel_D0_signs': ''.join('+' if x > 0 else ('-' if x < 0 else '?') for x in D0),
        'heine_D0_signs': ''.join('+' if x > 0 else '-' for x in heine),
        'heine_vs_det_rel': [mp.nstr(abs(mp.mpf(fc.fmt(D0[i], 40)) - heine[i]) / abs(heine[i]), 3) for i in range(6)],
    }
    print('T2 pair', pair, res_T2[str(pair)])
out['T2'] = res_T2

# T3: sin(sqrt w)/sqrt w ; s_m = zeta(2m)/pi^{2m} = |B_{2m}| 2^{2m-1}/(2m)!
from math import factorial
def bern(n):
    return Fr(fmpq.bernoulli(n).p, fmpq.bernoulli(n).q) if hasattr(fmpq, 'bernoulli') else None
from flint import fmpq as Q
def B(n):
    q = Q.bernoulli(n)
    return Fr(int(q.p), int(q.q))
c_T3 = [abs(B(2 * (m + 1))) * 2 ** (2 * (m + 1) - 1) / factorial(2 * (m + 1)) for m in range(62)]
al_T3 = sfrac_exact(c_T3, 60)
ok = all(al_T3[n - 1] == Fr(1, (2 * n + 1) * (2 * n + 3)) for n in range(1, len(al_T3) + 1))
out['T3_exact_match_1_over_(2n+1)(2n+3)'] = ok
out['T3_n_checked'] = len(al_T3)
out['T3_c0'] = str(c_T3[0])
print('T3 exact S-fraction match:', ok, 'n =', len(al_T3))
# precision-loss law in Arb: run at prec P and record certified digits of al_n
loss = {}
for P in (200, 400, 800):
    ctx.prec = P
    carb = [arb(fmpq(x.numerator, x.denominator)) for x in c_T3]
    al = fc.sfrac_from_series(carb, 60, stop_on_zero=True)
    loss[P] = [fc.digits(x) for x in al]
    print('T3 P=%d: certified digits at n=1,10,20,30,40,50,60:' % P, [loss[P][i] for i in (0, 9, 19, 29, 39, 49, 59) if i < len(loss[P])], 'computed', len(al))
out['T3_certified_digits_by_prec'] = {str(k): v for k, v in loss.items()}

# C1 / C2: circle toys
def li_from_zeros(rhos, N):
    """lambda_n = sum_rho (1 - (1 - 1/rho)^n), rhos: full zero list (with 1-rho and conjugates)."""
    return [sum(1 - (1 - 1 / r) ** n for r in rhos).real for n in range(0, N + 1)]

def moments_from_lambda(lam):
    """m_n = lam_{n+1} - 2 lam_n + lam_{n-1}, lam_0 = 0, lam_{-1} = lam_1."""
    N = len(lam) - 2
    m = []
    for n in range(0, N + 1):
        lm1 = lam[1] if n == 0 else lam[n - 1]
        m.append(lam[n + 1] - 2 * lam[n] + lm1)
    return m

def run_circle(rhos, N, label):
    ctx.prec = 300
    lam = li_from_zeros(rhos, N + 1)
    m = moments_from_lambda(lam)
    marb = [arb(mp.nstr(x, 80)) for x in m]
    alpha, h = fc.verblunsky_levinson(marb, N)
    Fco = [arb(1)] + [2 * marb[k] / marb[0] for k in range(1, N + 1)]
    gam = fc.schur_parameters(Fco, N)
    # direct moments from atoms: m_n = sum_rho |rho|^-2 z^n  (valid only on-line) and general formula
    zr = [1 - 1 / r for r in rhos]
    m_direct = [sum(-(1 - z) ** 2 * z ** (n - 1) for z in zr).real for n in range(0, N + 1)]
    agree_m = max(abs(m[n] - m_direct[n]) for n in range(N + 1))
    rec = {
        'alpha_levinson': [fc.fmt(a, 12) for a in alpha],
        'gamma_schur': [fc.fmt(g, 12) for g in gam],
        'max|alpha-gamma|': mp.nstr(max(abs(mp.mpf(fc.fmt(alpha[i], 50)) - mp.mpf(fc.fmt(gam[i], 50))) for i in range(min(len(alpha), len(gam)))), 3),
        'max|m(lambda) - m(atoms)|': mp.nstr(agree_m, 3),
        'first_|alpha|>=1': next((i for i, a in enumerate(alpha) if abs(a) >= 1 or (abs(a).upper() >= 1)), None),
        'lambda_1..6': [mp.nstr(x, 10) for x in lam[1:7]],
        'lambda_signs_1..%d' % N: ''.join('+' if x > 0 else '-' for x in lam[1:N + 1]),
    }
    print(label, {k: v for k, v in rec.items() if k not in ('alpha_levinson', 'gamma_schur')})
    print('   alpha:', rec['alpha_levinson'][:8])
    return rec

def full_zero_set(pts):
    """pts: list of (beta, gamma) with gamma > 0; returns the symmetric multiset {rho, 1-rho, conj}."""
    Z = []
    for b, g in pts:
        for r in {(b, g), (1 - b, g)}:
            Z.append(mp.mpc(r[0], r[1])); Z.append(mp.mpc(r[0], -r[1]))
    return Z

out['C1'] = run_circle(full_zero_set([(0.5, 3), (0.5, 5), (0.5, 8)]), 8, 'C1 on-line (3 pairs, 6 atoms)')
out['C2_shallow'] = run_circle(full_zero_set([(0.5, 3), (0.8, 5), (0.5, 8)]), 10, 'C2 pair off at gamma=5 (beta=0.8)')
out['C2_deep'] = run_circle(full_zero_set([(0.5, 3), (0.5, 5), (0.55, 8)]), 10, 'C2 pair off at gamma=8 (beta=0.55)')

# C1': m_n via Taylor series of log E(1+w) with E(s) = prod ((s-1/2)^2+g^2): lambda_n = n [z^n] log E(1/(1-z))
ctx.prec = 300
L = 12
ctx.cap = L
w = arb_series([0, 1])
s = 1 + w
logE = sum(((s - arb(1) / 2) ** 2 + g * g).log() for g in (3, 5, 8))
d = logE.coeffs()
from math import comb
lam_series = [arb(0)] + [n * sum((arb(comb(n - 1, j - 1)) * d[j] for j in range(1, n + 1)), arb(0)) for n in range(1, L)]
lam_zeros = li_from_zeros(full_zero_set([(0.5, 3), (0.5, 5), (0.5, 8)]), L - 1)
out['C1_lambda_series_vs_zeros_maxdiff'] = mp.nstr(max(abs(mp.mpf(fc.fmt(lam_series[n], 40)) - lam_zeros[n]) for n in range(1, L)), 3)
print('C1 lambda via Taylor-at-1 vs via zeros, max diff:', out['C1_lambda_series_vs_zeros_maxdiff'])

with open(os.path.join(os.path.dirname(__file__), 'u1_toys.json'), 'w') as fh:
    json.dump(out, fh, indent=1, default=str)
print('saved u1_toys.json')
