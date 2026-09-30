# h5.py -- producer A, unit haglund-cert-s37: optional clause H5 (the seed's chain, N = 24), same winding code.
# Run: python3 h5.py > h5.log
#   xi_N(s) = 1/2 + 1/2 s(s-1) sum_{n<=N} g_n(s),  g_n(s) = X^{-s/2} Gamma(s/2, X) + X^{-(1-s)/2} Gamma((1-s)/2, X), X = pi n^2
#   (staircase NOTE section 1).  Route L: that literal sum (cancels ~855 digits at t ~ 2508; 4800 bits, exact points).
#   Route T: xi(s) - 1/2 s(s-1) sum_{n=N+1}^{M} g_n(s) - tail, xi(s) = 1/2 s(s-1) pi^{-s/2} Gamma(s/2) zeta(s), using
#   xi = 1/2 + 1/2 s(s-1) sum_{n>=1} g_n (Riemann; NOTE section 1).  Tail (CERT section 8, Lemma G):
#   for -1 <= Re s <= 2, |g_n(s)| <= 2 e^{-X}/X, and sum_{n>M} <= 2 * (2 e^{-X_{M+1}}/X_{M+1}).
import time
from flint import acb, arb, ctx
from hag_core import square_vertices, winding

def g(n, s):
    X = arb.pi() * n * n
    A, lX = acb(X), acb(X.log())
    h1, h2 = s / 2, (1 - s) / 2
    return A.gamma_upper(h1) * (-h1 * lX).exp() + A.gamma_upper(h2) * (-h2 * lX).exp()

def xiN_L(N, s):
    tot = acb(0)
    for n in range(1, N + 1):
        tot += g(n, s)
    return acb(arb(1) / 2) + s * (s - 1) / 2 * tot

def xi(s):
    return s * (s - 1) / 2 * (-(s / 2) * acb(arb.pi().log())).exp() * (s / 2).gamma() * s.zeta()

def tail_g(s, M):
    assert s.real.lower() >= -1 and s.real.upper() <= 2, "Lemma G needs -1 <= Re s <= 2"
    X = arb.pi() * (M + 1) ** 2
    return (abs(s * (s - 1)) / 2 * 2 * (2 * (-X).exp() / X)).upper()

def xiN_T(N, s, M=None):
    M = N + 4 if M is None else M
    v = xi(s)
    tot = acb(0)
    for n in range(N + 1, M + 1):
        tot += g(n, s)
    v = v - s * (s - 1) / 2 * tot
    E = tail_g(s, M)
    return v + acb(arb(0, E), arb(0, E))

N = 24
T0 = time.time()
ok_sc = True
# (H5a) sign changes of xi_24(1/2 + it) around the NOTE's on-line zeros t = 2510.20266298848152, 2510.70868403660283
for lo, hi in [("2510.2026", "2510.2027"), ("2510.7086", "2510.7087")]:
    for route, prec in [("T", 256), ("L", 4800)]:
        ctx.prec = prec
        f = (lambda s: xiN_L(N, s)) if route == "L" else (lambda s: xiN_T(N, s))
        a = f(acb(arb(1) / 2, arb(lo))).real
        b = f(acb(arb(1) / 2, arb(hi))).real
        ok = (a > 0 and b < 0) or (a < 0 and b > 0)
        ok_sc = ok_sc and ok
        print("H5a route %s prec %d: xi_24(1/2 + i%s) in %s ; xi_24(1/2 + i%s) in %s ; sign change %s" % (
            route, prec, lo, a.str(12, more=True), hi, b.str(12, more=True), ok), flush=True)
# L vs T at the NOTE's off-line zero and at the square's centre
for sr, si in [("0.8159896243043424688941", "2508.283974805324153202"), ("0.8159896243", "2508.2839748053")]:
    ctx.prec = 4800; vL = xiN_L(N, acb(arb(sr), arb(si)))
    ctx.prec = 256; vT = xiN_T(N, acb(arb(sr), arb(si)))
    print("H5 L/T at s = %s + %s i: L %s + %s i | T %s + %s i | overlap %s" % (sr, si, vL.real.str(10, more=True),
          vL.imag.str(10, more=True), vT.real.str(10, more=True), vT.imag.str(10, more=True), vL.overlaps(vT)), flush=True)
# (H5b) winding around the off-line zero, s-plane square centred at 0.8159896243 + 2508.2839748053 i
ctx.prec = 256
fT = lambda s: xiN_T(N, s)
res = {}
for tag, cx, cy, r, expect in [("H5b[r=1e-3]", "0.8159896243", "2508.2839748053", "1e-3", 1),
                               ("H5b[r=1e-10]", "0.8159896243", "2508.2839748053", "1e-10", 1),
                               ("CTL24[c+2.5e-3 i,r=1e-3]", "0.8159896243", "2508.2864748053", "1e-3", 0)]:
    k = winding(fT, square_vertices(cx, cy, r), K0=16, maxdepth=16, out=lambda s: print(s, flush=True), tag=tag)
    res[tag] = (k, expect)
    print("%s RESULT winding = %s (expected %d)" % (tag, k, expect), flush=True)
print("H5 VERDICT: sign changes %s ; windings %s ; total %.1fs" % (ok_sc, all(k == e for k, e in res.values()), time.time() - T0))
