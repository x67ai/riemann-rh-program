"""
u5_function_field.py -- rung-1 (exact) control: curves over F_q.

For a curve C/F_q of genus g with L-polynomial P(T) = prod (1 - a_j T) (|a_j| = sqrt q, Weil), the completed
function Lambda_C(s) = q^{g(s-1/2)} P(q^{-s}) is entire, Lambda_C(s) = Lambda_C(1-s), real on the line:
  g = 1: Lambda(1/2+it) = 2 cos(t l) - c1/sqrt q,        l = log q, P = 1 - c1 T + q T^2 (c1 = q + 1 - N_1)
  g = 2: Lambda(1/2+it) = 2 cos(2 t l) + (2 c1/sqrt q) cos(t l) + c2/q,  P = 1 + c1 T + c2 T^2 + q c1 T^3 + q^2 T^4
Its zeros in t are PERIODIC (period 2 pi/l), so the zero measure nu_C in w = t^2 has infinitely many atoms: the
S-fraction in w does NOT terminate (erratum to the seed).  What terminates is the Frobenius-variable measure
sum_j delta_{2 sqrt q cos theta_j} (g atoms): a J-fraction of length g.
Checks: (1) genuine point counts by brute force (F_q and F_{q^2}); (2) the w-side S-fraction is certified positive
(exact Arb, RH for curves = Weil's theorem); (3) the WKB law for constant zero density D = g l/pi predicts
4 n sqrt(al_n) -> 2 g l; (4) an RH-violating 'fake curve' polynomial (Hasse bound broken) fails, with its index.
"""
import sys, os, json, itertools
sys.path.insert(0, os.path.dirname(__file__))
from flint import arb, arb_series, ctx
import fp_core as fc
here = os.path.dirname(os.path.abspath(__file__))
logf = open(os.path.join(here, 'u5_function_field.log'), 'w')
def say(*a):
    t = ' '.join(str(x) for x in a); print(t, flush=True); logf.write(t + '\n'); logf.flush()

# ---------- finite fields F_p and F_{p^2} = F_p[i]/(i^2 - nr) ----------
def count_points(p, f, ext):
    """#C(F_{p^ext}) for y^2 = f(x) (deg f = 5 -> one point at infinity, deg 3 -> one point at infinity)."""
    # find a non-residue for F_{p^2}
    nr = next(a for a in range(2, p) if pow(a, (p - 1) // 2, p) == p - 1)
    if ext == 1:
        elems = [(a, 0) for a in range(p)]
    else:
        elems = [(a, b) for a in range(p) for b in range(p)]
    def mul(x, y):
        return ((x[0] * y[0] + nr * x[1] * y[1]) % p, (x[0] * y[1] + x[1] * y[0]) % p)
    def add(x, y):
        return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)
    def pw(x, k):
        r = (1, 0)
        for _ in range(k):
            r = mul(r, x)
        return r
    def feval(x):
        r = (0, 0)
        for k, c in enumerate(f):
            if c:
                r = add(r, mul((c % p, 0), pw(x, k)))
        return r
    squares = {}
    for y in elems:
        s = mul(y, y)
        squares[s] = squares.get(s, 0) + 1
    n = 0
    for x in elems:
        n += squares.get(feval(x), 0)
    return n + 1   # one point at infinity (odd degree)

def lpoly(p, f, g):
    N1 = count_points(p, f, 1)
    if g == 1:
        return {'N1': N1, 'c1': p + 1 - N1}
    N2 = count_points(p, f, 2)
    c1 = N1 - p - 1
    c2 = (N2 - p * p - 1 + c1 * c1) // 2
    return {'N1': N1, 'N2': N2, 'c1': c1, 'c2': c2}

def sfrac_of(logE_series_fn, M, P):
    ctx.prec = P; ctx.cap = M + 2
    w = arb_series([0, 1])
    lg = logE_series_fn(w)
    c = lg.coeffs()
    # -d/dw log E = sum s_{m+1} w^m  ->  s_{m} = -m [w^m] log E
    cm = [-(m + 1) * c[m + 1] for m in range(0, M)]
    return cm, fc.sfrac_from_series(cm, M - 1, stop_on_zero=True)

def cos_sqrt(w, a):
    """cos(a sqrt w) as a power series in w."""
    ctx_cap = ctx.cap
    coeffs = []
    term = arb(1)
    for k in range(ctx_cap):
        coeffs.append(term)
        term = -term * a * a / ((2 * k + 1) * (2 * k + 2))
    return arb_series(coeffs)

out = {}
P = 6000; M = 300
# genus 1: y^2 = x^3 + x + 1 over F_5 ; genus 2: y^2 = x^5 + x + 1 over F_5 (check squarefree by nonzero disc: brute)
for label, p, f, g in [('E: y^2=x^3+x+1 /F5', 5, [1, 1, 0, 1], 1), ('C: y^2=x^5+x+1 /F5', 5, [1, 1, 0, 0, 0, 1], 2),
                       ('C: y^2=x^5+2x+3 /F7', 7, [3, 2, 0, 0, 0, 1], 2)]:
    L = lpoly(p, f, g)
    ctx.prec = P   # constants at full precision (a first run computed log q at 53 bits and lost everything by n = 10)
    q = arb(p); l = q.log(); sq = q.sqrt()
    if g == 1:
        c1 = L['c1']
        hasse = abs(c1) <= 2 * (p ** 0.5)
        fn = lambda w, c1=c1: (2 * cos_sqrt(w, l) - arb(c1) / sq).log() if (2 - c1 / p ** 0.5) > 0 else (-(2 * cos_sqrt(w, l) - arb(c1) / sq)).log()
    else:
        c1, c2 = L['c1'], L['c2']
        # roots check: P(T) with all roots |T| = q^{-1/2}  <=>  trig poly 2cos(2x) + (2c1/sqrt q)cos x + c2/q real-rooted
        fn = lambda w, c1=c1, c2=c2: (2 * cos_sqrt(w, 2 * l) + (2 * arb(c1) / sq) * cos_sqrt(w, l) + arb(c2) / q).log()
        v0 = 2 + 2 * c1 / p ** 0.5 + c2 / p
        if v0 < 0:
            fn = lambda w, c1=c1, c2=c2: (-(2 * cos_sqrt(w, 2 * l) + (2 * arb(c1) / sq) * cos_sqrt(w, l) + arb(c2) / q)).log()
    cm, al = sfrac_of(fn, M, P)
    pos = all(a > 0 for a in al)
    A = [4 * n * al[n - 1].sqrt() for n in (50, 100, 200, 299) if n <= len(al)]
    rec = {'lpoly': L, 'n_al': len(al), 'all_certified_positive': pos,
           'first_negative': next((n for n, a in enumerate(al, 1) if a < 0), None),
           '4n sqrt(al_n) at n=50,100,200,299': [x.str(8, radius=False) for x in A],
           'WKB prediction 2 g log q': (2 * g * l).str(8, radius=False),
           'al_1..5': [a.str(10, radius=False) for a in al[:5]], 'digits_last': fc.digits(al[-1])}
    say(label, json.dumps(rec))
    out[label] = rec

# RH-violating 'fake curve' polynomial (Hasse broken): P = 1 - c1 T + q T^2 with c1 = 5 > 2 sqrt 5 = 4.47
p = 5; ctx.prec = 3000; q = arb(p); l = q.log(); sq = q.sqrt()
for c1 in (5, 6, 9):
    fn = lambda w, c1=c1: (arb(c1) / sq - 2 * cos_sqrt(w, l)).log()
    cm, al = sfrac_of(fn, 120, 3000)
    fneg = next((n for n, a in enumerate(al, 1) if a < 0), None)
    say('fake curve c1=%d (Hasse bound 2 sqrt 5 = 4.472 violated): first negative al_n at n = %s; al_1..6 = %s'
        % (c1, fneg, [a.str(6, radius=False) for a in al[:6]]))
    out['fake_c1_%d' % c1] = {'first_negative': fneg, 'al_1_6': [a.str(8, radius=False) for a in al[:6]]}
json.dump(out, open(os.path.join(here, 'u5_function_field.json'), 'w'), indent=1)
