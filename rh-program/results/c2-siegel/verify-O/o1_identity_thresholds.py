#!/usr/bin/env python3
"""o1_identity_thresholds.py -- Opus independent check of the Siegel-zero scout, items 1 and 2 (and the Psi_K(0) growth claim of scout section 1).

Written from the normalization of results/c2-r1/confinement-note.md section 0.1 only (the scout's scripts were not imported or copied).
  what(xi) = int w(u) e^{-iu xi} du ; g = w / cosh(u/2) ; ghat(r) = int g(u) cos(ru) du (w even)
  B_K(w) = 2 what(0) + (1/2pi) int ghat(r) [2 Re psi(1/2 + i r) - 2 log(2 pi) + log|D|] dr
     (Legendre duplication psi(z) + psi(z + 1/2) = 2 psi(2z) - 2 log 2 at z = 1/4 + ir/2 turns the scout's
      Re psi(1/4+ir/2) + Re psi(3/4+ir/2) - 2 log pi into 2 Re psi(1/2+ir) - 2 log 2pi; an algebraically different route)
  Z_K(w) = 2 sum_{tau>0} ghat(tau) over the zeros of zeta and of L(chi_D) (all taken on the line; completeness is tested by the identity)
  P_K(w) = 4 sum_n Lambda(n) (1 + chi_D(n)) w(log n) / (n + 1)
Own zeros of L(s, chi_-20): sign changes of the Hardy-type function Z_chi(t) = exp(i theta(t)) L(1/2+it), theta from loggamma,
L from Hurwitz zeta sums written out here; refined by mpmath.findroot (Illinois) to |dt| < 1e-14.
Test elements (different from the scout's w_A, w_B):  w_C(u) = exp(-u^2/2)(1 + cos 20u),  w_E(u) = exp(-u^2)(1 + cos 5u).
Thresholds: D0 (A_K(0) = 0), D1 (a_K(0) = 0) for odd characters (the scout's case) and the even-character analogues D0+, D1+.
Growth: Z_K(w_B) = B_K - P_K for large fundamental discriminants -D = p = 3 mod 4 (lower bound w(0) log|D| - C from Lambda_K <= 2 Lambda).
"""
import json, time, math
import numpy as np
import mpmath as mp
from scipy.special import digamma as sdg
from scipy.integrate import quad
import sympy

T0 = time.time()
mp.mp.dps = 25
out = {}
LOG = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); LOG.append(s)

# ---------------- Kronecker symbol for fundamental D ----------------
def kron(D, n):
    """(D/n) for n >= 1, D a discriminant (D = 0,1 mod 4)."""
    res = 1
    while n % 2 == 0:
        n //= 2
        if D % 2 == 0: return 0
        res *= 1 if D % 8 in (1, 7) else -1
    if n == 1: return res
    return res * int(sympy.jacobi_symbol(D % n, n))

D = -20; Q = 20
chi = [kron(D, n) if math.gcd(n, Q) == 1 else 0 for n in range(Q)]
say("chi_{-20}(n), n = 0..19:", chi)
assert chi[19] == -1

# ---------------- own zeros of L(s, chi_-20) on (0, 80] ----------------
def Lchi(s):
    return mp.power(Q, -s) * mp.fsum(chi[a] * mp.zeta(s, mp.mpf(a) / Q) for a in range(1, Q) if chi[a] != 0)
def theta(t):
    s = mp.mpf(0.5) + 1j * t
    return mp.im(s / 2 * mp.log(mp.mpf(Q) / mp.pi) + mp.loggamma((s + 1) / 2))
def Zchi(t):
    v = mp.exp(1j * theta(t)) * Lchi(mp.mpf(0.5) + 1j * t)
    return v
imax = 0.0
for tt in (3.3, 17.1, 41.7, 66.6, 79.2):
    v = Zchi(tt); imax = max(imax, float(abs(mp.im(v)) / max(abs(v), mp.mpf(10) ** -30)))
say("max |Im Z_chi|/|Z_chi| at five heights (realness on the line, root number +1):", "%.2e" % imax)
grid = np.arange(0.02, 80.0 + 1e-9, 0.02)
vals = [float(mp.re(Zchi(t))) for t in grid]
Lz = []
for i in range(len(grid) - 1):
    if vals[i] == 0 or vals[i] * vals[i + 1] < 0:
        r = mp.findroot(lambda t: mp.re(Zchi(t)), (grid[i], grid[i + 1]), solver="illinois", tol=1e-28)
        Lz.append(float(r))
say("L(chi_-20): %d zeros on (0, 80]; first eight:" % len(Lz), ", ".join("%.9f" % z for z in Lz[:8]))
scout_first8 = [2.358934994, 4.675507750, 7.429109775, 8.804527425, 10.663300735, 12.802400811, 14.336169008, 15.493534961]
say("  max |mine - scout| over the first eight: %.2e" % max(abs(a - b) for a, b in zip(Lz, scout_first8)))
out["L_zeros"] = Lz
Zz = [float(mp.im(mp.zetazero(n))) for n in range(1, 41)]
say("zeta: 40 zeros, last %.4f" % Zz[-1])
L1 = -mp.fsum(chi[a] * mp.digamma(mp.mpf(a) / Q) for a in range(1, Q)) / Q
say("L(1, chi_-20) = -(1/20) sum chi(a) psi(a/20) = %s ; pi/sqrt5 = %s" % (mp.nstr(L1, 15), mp.nstr(mp.pi / mp.sqrt(5), 15)))
sig = np.linspace(0.005, 0.995, 199)
Ls = [float(Lchi(s)) for s in sig]
say("min L(sigma, chi_-20) on sigma in [0.005, 0.995] step 0.005: %.4f" % min(Ls))

# ---------------- von Mangoldt sieve ----------------
NM = 1_000_000
lam = np.zeros(NM + 1); spf = np.zeros(NM + 1, dtype=np.int64)
isp = np.ones(NM + 1, dtype=bool); isp[:2] = False
for p in range(2, int(NM ** 0.5) + 1):
    if isp[p]: isp[p * p::p] = False
primes = np.nonzero(isp)[0]
for p in primes:
    pk = p
    while pk <= NM:
        lam[pk] = math.log(p); pk *= p
def lamK_table(Dd):
    # Lambda_K(p^k) = log p (1 + chi(p)^k)
    lk = np.zeros(NM + 1)
    for p in primes:
        c = kron(Dd, int(p)) if Dd % p != 0 else 0
        pk = int(p); k = 1
        while pk <= NM:
            lk[pk] = math.log(p) * (1 + c ** k); pk *= int(p); k += 1
    return lk
LK20 = lamK_table(-20)
assert LK20.min() >= 0
ratio = set(np.round(LK20[lam > 0] / lam[lam > 0], 12))
say("Lambda_K/Lambda on prime powers <= 1e6 takes the values", sorted(ratio), "; min Lambda_K =", LK20.min())

# ---------------- ghat by u-quadrature ----------------
H = 0.004; U = np.arange(-16, 16 + H / 2, H)
def ghat(wfun, r):
    r = np.atleast_1d(np.asarray(r, float)); g = wfun(U) / np.cosh(U / 2)
    res = np.empty_like(r)
    for i0 in range(0, len(r), 400):
        rr = r[i0:i0 + 400]
        with np.errstate(all='ignore'):
            res[i0:i0 + 400] = (np.cos(np.outer(rr, U)) @ g) * H
    assert np.all(np.isfinite(res))
    return res
def arch_bracket(r, absD, parity="odd"):
    if parity == "odd":   # zeta (Gamma_R(s)) + odd chi (Gamma_R(s+1)): duplication form
        return 2 * np.real(sdg(0.5 + 1j * r)) - 2 * math.log(2 * math.pi) + math.log(absD)
    return 2 * np.real(sdg(0.25 + 0.5j * r)) - 2 * math.log(math.pi) + math.log(absD)
def identity(name, wfun, what0, K, absD, lamK, Lzeros):
    R = np.arange(-(K + 45), K + 45 + 1e-9, 0.01)
    gR = ghat(wfun, R)
    zeta_br = np.real(sdg(0.25 + 0.5j * R)) - math.log(math.pi)
    chi_br = np.real(sdg(0.75 + 0.5j * R)) - math.log(math.pi) + math.log(absD)
    Arch_z = np.sum(gR * zeta_br) * 0.01 / (2 * math.pi)
    Arch_c = np.sum(gR * chi_br) * 0.01 / (2 * math.pi)
    Arch_dup = np.sum(gR * arch_bracket(R, absD)) * 0.01 / (2 * math.pi)
    n = np.arange(2, NM + 1); wl = wfun(np.log(n))
    P_z = 4 * np.sum(lam[2:] * wl / (n + 1)); P_K = 4 * np.sum(lamK[2:] * wl / (n + 1))
    Z_z = 2 * np.sum(ghat(wfun, np.array(Zz))); Z_c = 2 * np.sum(ghat(wfun, np.array(Lzeros)))
    B_z = 2 * what0 + Arch_z; B_c = Arch_c; B_K = 2 * what0 + Arch_dup
    say("[%s] zeta : B %.10f Z %.10f P %.10f resid %.2e" % (name, B_z, Z_z, P_z, B_z - Z_z - P_z))
    say("[%s] chi  : B %.10f Z %.10f P %.10f resid %.2e" % (name, B_c, Z_c, P_K - P_z, B_c - Z_c - (P_K - P_z)))
    say("[%s] zetaK: B %.10f Z %.10f P %.10f resid %.2e ; duplication vs two-digamma archimedean: %.2e"
        % (name, B_K, Z_z + Z_c, P_K, B_K - Z_z - Z_c - P_K, Arch_dup - Arch_z - Arch_c))
    return dict(B_K=B_K, Z_K=Z_z + Z_c, P_K=P_K, resid=B_K - Z_z - Z_c - P_K)
wC = lambda u: np.exp(-u * u / 2) * (1 + np.cos(20 * u)); wC0 = math.sqrt(2 * math.pi)   # what_C(0) = sqrt(2pi)(1 + e^{-200})
wE = lambda u: np.exp(-u * u) * (1 + np.cos(5 * u)); wE0 = math.sqrt(math.pi) * (1 + math.exp(-25 / 4))
out["id_C"] = identity("w_C", wC, wC0, 20, 20, LK20, Lz)
out["id_E"] = identity("w_E", wE, wE0, 5, 20, LK20, Lz)
# scout's w_A as a cross-check on the scout's printed B_K, Z_K, P_K
wA = lambda u: np.exp(-u * u / 2) * (1 + np.cos(12 * u)); wA0 = math.sqrt(2 * math.pi) * (1 + math.exp(-72))
out["id_A"] = identity("w_A (scout's element, my code)", wA, wA0, 12, 20, LK20, Lz)

# ---------------- Psi_K(0) at D = -20 ----------------
allz = np.array(Zz + Lz)
psi0 = np.sum(1 / np.cosh(np.pi * allz))
say("Psi_K(0) at D = -20: %.6e (first L-zero term %.6e)" % (psi0, 1 / math.cosh(math.pi * Lz[0])))

# ---------------- thresholds ----------------
g_E = float(mp.euler)
D0 = 64 * math.pi ** 2 * math.exp(2 * g_E)
D0_check = math.exp(2 * math.log(math.pi) - float(mp.digamma(0.25) + mp.digamma(0.75)))
I_odd = quad(lambda r: 2 / math.cosh(math.pi * r) * 2 * np.real(sdg(0.5 + 1j * r)), 0, 40, limit=400)[0]
D1 = math.exp(2 * math.log(2 * math.pi) - I_odd)
I_odd2 = quad(lambda r: 2 / math.cosh(math.pi * r) * (np.real(sdg(0.25 + 0.5j * r)) + np.real(sdg(0.75 + 0.5j * r))), 0, 40, limit=400)[0]
D1_check = math.exp(2 * math.log(math.pi) - I_odd2)
D0p = math.pi ** 2 * math.exp(-2 * float(mp.digamma(0.25)))
I_even = quad(lambda r: 2 / math.cosh(math.pi * r) * 2 * np.real(sdg(0.25 + 0.5j * r)), 0, 40, limit=400)[0]
D1p = math.exp(2 * math.log(math.pi) - I_even)
say("thresholds (odd chi, D < 0): D0 = 64 pi^2 e^{2 gamma} = %.4f (direct %.4f);  D1 = %.4f (two-digamma form %.4f)" % (D0, D0_check, D1, D1_check))
say("thresholds (even chi, D > 0; bracket 2 Re psi(1/4+ir/2) - 2 log pi + log D): D0+ = %.1f ; D1+ = %.2f" % (D0p, D1p))
aK0_20 = (I_odd - 2 * math.log(2 * math.pi) + math.log(20)) / (2 * math.pi)
AK0_20 = (2 * float(mp.digamma(0.5)) - 2 * math.log(2 * math.pi) + math.log(20)) / (2 * math.pi)
say("D = -20: A_K(0) = %.6f ; a_K(0) = %.6f" % (AK0_20, aK0_20))
a0_zeta = (quad(lambda r: 2 / math.cosh(math.pi * r) * np.real(sdg(0.25 + 0.5j * r)), 0, 40, limit=400)[0] - math.log(math.pi)) / (2 * math.pi)
say("control: degree-1 a(0) for zeta alone = %.6f (IV.18 rider (ii) prints -0.653847)" % a0_zeta)
out.update(D0=D0, D1=D1, D0p=D0p, D1p=D1p, aK0_20=aK0_20, AK0_20=AK0_20)
# a_K monotone in |s| on a grid (D = -20)
def aK(s, absD=20):
    f = lambda r: (1 / math.cosh(math.pi * (s - r))) * (2 * np.real(sdg(0.5 + 1j * r)) - 2 * math.log(2 * math.pi) + math.log(absD)) / (2 * math.pi)
    return quad(f, s - 30, s + 30, limit=400)[0]
sg = np.arange(0, 3.001, 0.05); av = np.array([aK(s) for s in sg])
say("a_K(s), D = -20, s = 0..3 step 0.05: nondecreasing on the grid: %s ; sign change between s = %.2f and %.2f"
    % (bool(np.all(np.diff(av) >= -1e-12)), sg[np.argmax(av >= 0) - 1], sg[np.argmax(av >= 0)]))
# negative mass
from scipy.optimize import brentq
s0 = brentq(aK, 0.5, 3); negm = 2 * quad(lambda s: -aK(s), 0, s0, limit=200)[0]
say("a_K < 0 exactly on |s| < %.4f ; negative mass %.6f" % (s0, negm))

# ---------------- growth of the low-zero share with |D| (scout section 1 claim) ----------------
wB = lambda u: np.exp(-2 * u * u); wB0 = math.sqrt(math.pi / 2)
RB = np.arange(-40, 40.0001, 0.01); gB = ghat(wB, RB)
nn = np.arange(2, NM + 1); wlB = wB(np.log(nn))
say("Z_K(w_B) = B_K - P_K (w_B = e^{-2u^2}, w(0) = 1, so Lambda_K <= 2 Lambda gives Z_K >= log|D| - C):")
growth = []
for p in [20, 10007, 1000003, 100000007, 10 ** 10 + 19, 10 ** 12 + 39, 10 ** 16 + 63]:
    if p == 20:
        Dd = -20
    else:
        q = sympy.nextprime(p - 1)
        while q % 4 != 3: q = sympy.nextprime(q)
        Dd = -int(q)
    lk = LK20 if Dd == -20 else lamK_table(Dd)
    BK = 2 * wB0 + np.sum(gB * arch_bracket(RB, abs(Dd))) * 0.01 / (2 * math.pi)
    PK = 4 * np.sum(lk[2:] * wlB / (nn + 1))
    ZK = BK - PK
    # on-line part only would be 2 int what Psi_K; report the what-weighted mean Z_K/(2 int what), int what = 2 pi w(0) = 2 pi
    growth.append(dict(D=Dd, B_K=BK, P_K=PK, Z_K=ZK, mean=ZK / (4 * math.pi)))
    say("  D = %d: B_K %.4f P_K %.4f Z_K %.4f ; what-weighted mean of the zero density Z_K/(2 int what) = %.4f ; log|D|/(4 pi) = %.4f"
        % (Dd, BK, PK, ZK, ZK / (4 * math.pi), math.log(abs(Dd)) / (4 * math.pi)))
out["growth"] = growth
say("done in %.1fs" % (time.time() - T0))
json.dump(out, open(__file__.replace(".py", "_out.json"), "w"), indent=1)
open(__file__.replace(".py", "_run.log"), "w").write("\n".join(LOG) + "\n")
