#!/usr/bin/env python3
"""siegel_setup.py -- Session 24 item 2(c), section 0 and section 1 of siegel-world-scout.md.

The degree-2 identity (0.3) for zeta_K = zeta * L(chi_D), D = -20, in the normalization of
results/c2-r1/confinement-note.md section 0.1 (transform what(xi) = int w e^{-iu xi}; g = w/cosh(u/2); ghat(z) = int g e^{izu}):

  B_K(w) = Z_K(w) + P_K(w),
  B_K(w) = 2 what(0) + (1/2pi) int ghat(r) [Re psi(1/4 + ir/2) + Re psi(3/4 + ir/2) - 2 log pi + log|D|] dr,
  Z_K(w) = sum over zeros rho of zeta and of L(chi_D) of ghat(gamma(rho)),  gamma(rho) = (rho - 1/2)/i,
  P_K(w) = 4 sum_n Lambda_K(n) w(log n)/(n+1),  Lambda_K(p^k) = Lambda(p^k) (1 + chi_D(p)^k)  (= Lambda(p^k)(1 + chi_D(p^k))).

The chi-part is the explicit formula for L(s, chi_D), chi_D odd (D < 0), completed by (|D|/pi)^{s/2} Gamma((s+1)/2), no pole;
its archimedean bracket is Re psi(3/4 + ir/2) - log pi + log|D|. The zeta-part is the Lean literatureRHS of confinement-note section 1.1.
Checks: (1) chi_{-20} table; (2) Lambda_K >= 0 and prime-power support, n <= 2000 (m0-axiom-note section 6.2 verified n <= 200);
(3) Lambda(1/2 + it, chi) real on the line (root number +1), zeros of L(chi_{-20}) with 0 < t <= 80 by sign change + refinement;
(4) no real zero of L(sigma, chi_{-20}) on (0, 1) (positive control for section 2); (5) the identity for w_A, w_B, for zeta alone,
L(chi) alone and zeta_K, residual target 1e-6 (stop condition (a)); (6) Psi_K(s) on |s| <= 4 and the domination test (D_{0,y}).
Budget: minutes, one process.
"""
import json, sys, time
import numpy as np
import mpmath as mp
from scipy.special import digamma as sp_digamma

t0 = time.time()
mp.mp.dps = 20
D = -20; Q = 20
LOGPI = float(mp.log(mp.pi)); LOGQ = float(mp.log(Q))
out = {"D": D}

# ---------- (1) chi_{-20} as the Kronecker symbol (D/n) ----------
def kronecker(a, n):
    # Kronecker symbol (a/n) for n >= 1
    if n == 0: return 1 if abs(a) == 1 else 0
    res = 1
    # factor out 2
    while n % 2 == 0:
        n //= 2
        if a % 2 == 0: return 0
        if a % 8 in (3, 5): res = -res
    if n == 1: return res
    # Jacobi symbol (a/n), n odd
    a = a % n
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: res = -res
        a = a % n
    return res if n == 1 else 0

chi = [kronecker(D, n) for n in range(Q)]
expected = {1: 1, 3: 1, 7: 1, 9: 1, 11: -1, 13: -1, 17: -1, 19: -1}
assert all(chi[n] == v for n, v in expected.items()), chi
assert all(chi[n] == 0 for n in range(Q) if np.gcd(n, Q) != 1)
assert chi[Q - 1] == -1  # odd character
print("chi_{-20} mod 20:", chi, " (odd: chi(-1) = -1)")
out["chi_mod_20"] = chi
def chi_n(n): return chi[n % Q]

# ---------- (2) Lambda and Lambda_K by sieve ----------
NMAX = 200000
def vonmangoldt_table(N):
    lam = np.zeros(N + 1)
    spf = np.zeros(N + 1, dtype=np.int64)
    for i in range(2, N + 1):
        if spf[i] == 0:
            for j in range(i, N + 1, i):
                if spf[j] == 0: spf[j] = i
    for n in range(2, N + 1):
        p = spf[n]; m = n
        while m % p == 0: m //= p
        if m == 1: lam[n] = np.log(p)
    return lam, spf
LAM, SPF = vonmangoldt_table(NMAX)
LAMK = np.zeros(NMAX + 1)
for n in range(2, NMAX + 1):
    if LAM[n] != 0:
        LAMK[n] = LAM[n] * (1 + chi_n(n))     # chi(p^k) = chi(p)^k
assert (LAMK >= 0).all()
# exact cross-check of the closed form for n <= 2000 against -zeta_K'/zeta_K via Dirichlet convolution of Lambda with chi... :
# Lambda_K = Lambda * (1 + chi) on prime powers is the log-derivative of zeta(s)L(s,chi) since -L'/L(s,chi) = sum Lambda(n) chi(n) n^{-s}.
vals = sorted(set(np.round(LAMK[2:2001] / np.where(LAM[2:2001] > 0, LAM[2:2001], 1), 12)))
print("Lambda_K(n)/Lambda(n) values for prime powers n <= 2000:", vals, "; min Lambda_K =", LAMK.min())
out["lambdaK_ratio_values_n_le_2000"] = [float(v) for v in vals]
out["lambdaK_nonneg_n_le"] = NMAX

# ---------- (3) zeros of L(s, chi_{-20}) on the critical line ----------
chi_mp = [mp.mpf(c) for c in chi]
def Lchi(s): return mp.dirichlet(s, chi_mp)
def Lambda_chi(s):  # completed, odd character
    return mp.power(mp.mpf(Q) / mp.pi, s / 2) * mp.gamma((s + 1) / 2) * Lchi(s)
def Zchi(t):  # real on the line (checked below)
    v = Lambda_chi(mp.mpc(0.5, t))
    return v
# reality check
imax = 0.0
for tt in (0.7, 3.3, 9.9, 25.0, 61.3):
    v = Zchi(tt); imax = max(imax, abs(float(mp.im(v))) / max(abs(float(mp.re(v))), 1e-30))
print(f"max relative |Im Lambda_chi(1/2+it)| at five t: {imax:.2e}")
out["lambda_chi_real_on_line_relmax"] = imax
def Zr(t): return float(mp.re(Zchi(t)))
TMAX = 80.0; h = 0.05
grid = np.arange(0.0 + h, TMAX + h / 2, h)
vals = np.array([Zr(t) for t in grid])
zeros_chi = []
for i in range(len(grid) - 1):
    if vals[i] == 0.0: zeros_chi.append(grid[i]); continue
    if vals[i] * vals[i + 1] < 0:
        a, b = grid[i], grid[i + 1]
        r = mp.findroot(lambda t: mp.re(Zchi(t)), (a, b), solver="bisect", tol=1e-18, maxsteps=80)
        zeros_chi.append(float(r))
zeros_chi = sorted(zeros_chi)
print(f"L(chi_-20): {len(zeros_chi)} sign changes of the completed function on (0, {TMAX}]; first eight: " + ", ".join(f"{z:.9f}" for z in zeros_chi[:8]))
# Riemann-von Mangoldt count for comparison (the smooth main term of N(T,chi) for 0 < t <= T, recalled shape, comparison only)
rvm = TMAX / (2 * np.pi) * np.log(Q * TMAX / (2 * np.pi * np.e))
print(f"  comparison: (T/2pi) log(qT/2pi e) at T = {TMAX}: {rvm:.2f}  (smooth main term; the identity check below is the completeness test)")
out["zeros_Lchi_0_to_80"] = zeros_chi
out["rvm_main_term_T80"] = float(rvm)

# ---------- (4) no real zero of L(sigma, chi) on (0,1) ----------
sig = np.linspace(0.005, 0.995, 199)
lv = np.array([float(mp.re(Lchi(mp.mpf(s)))) for s in sig])
print(f"L(sigma, chi_-20) on (0,1): min = {lv.min():.6f} at sigma = {sig[lv.argmin()]:.3f}, max = {lv.max():.6f}; L(1/2) = {Lchi(mp.mpf('0.5'))}; L(1) = {Lchi(mp.mpf(1))} (class number formula: 2 pi h/(w sqrt|D|) = 2*pi*2/(2*sqrt 20) = pi/sqrt 5 = {float(mp.pi/mp.sqrt(5)):.9f})")
out["L_sigma_min_on_0_1"] = float(lv.min()); out["L_1_chi"] = float(mp.re(Lchi(mp.mpf(1))))
assert lv.min() > 0

# ---------- zeta zeros ----------
NZ = 40
zeros_zeta = [float(mp.im(mp.zetazero(n))) for n in range(1, NZ + 1)]
print(f"zeta: first {NZ} zeros, last = {zeros_zeta[-1]:.4f}")
out["zeros_zeta_first"] = zeros_zeta

# ---------- (5) the identity check ----------
# test elements (cone elements of Sigma_infinity: w >= 0, what >= 0, Gaussian decay)
#  w_A(u) = exp(-u^2/2) (1 + cos(12u)) ;  what_A(xi) = sqrt(2pi) [G(xi) + G(xi-12)/2 + G(xi+12)/2], G(x) = exp(-x^2/2)
#  w_B(u) = exp(-2 u^2) ;                  what_B(xi) = sqrt(pi/2) exp(-xi^2/8)
def wA(u): return np.exp(-u * u / 2) * (1 + np.cos(12 * u))
def whatA(x): return np.sqrt(2 * np.pi) * (np.exp(-x * x / 2) + 0.5 * np.exp(-(x - 12) ** 2 / 2) + 0.5 * np.exp(-(x + 12) ** 2 / 2))
def wB(u): return np.exp(-2 * u * u)
def whatB(x): return np.sqrt(np.pi / 2) * np.exp(-x * x / 8)

def mu0(x): return 1.0 / np.cosh(np.pi * x)
# ghat(r) for real r, two routes: (i) u-quadrature 2 int_0^inf w(u)/cosh(u/2) cos(ru) du; (ii) (what * mu_0)(r)
U = np.linspace(0, 12, 24001); du = U[1] - U[0]
S = np.linspace(-60, 60, 120001); ds = S[1] - S[0]
def ghat_u(w, r):
    r = np.atleast_1d(r)
    g = w(U) / np.cosh(U / 2)
    return 2 * np.trapezoid(g[None, :] * np.cos(np.outer(r, U)), dx=du, axis=1)
def ghat_conv(what, r):
    r = np.atleast_1d(r)
    return np.array([np.trapezoid(what(S) * mu0(rr - S), dx=ds) for rr in r])
# archimedean brackets on the r-grid
R = np.linspace(-60, 60, 60001); dr = R[1] - R[0]
br_zeta = np.real(sp_digamma(0.25 + 0.5j * R)) - LOGPI
br_chi = np.real(sp_digamma(0.75 + 0.5j * R)) - LOGPI + LOGQ
ns = np.arange(2, NMAX + 1)
def identity(name, w, what):
    # ghat on the r grid by convolution (fast, closed-form what) and a spot check by u-quadrature
    gr = ghat_conv(what, R)
    spot = ghat_u(w, np.array([0.0, 3.0, 12.0, 14.134725]))
    spot2 = ghat_conv(what, np.array([0.0, 3.0, 12.0, 14.134725]))
    arch_z = np.trapezoid(gr * br_zeta, dx=dr) / (2 * np.pi)
    arch_c = np.trapezoid(gr * br_chi, dx=dr) / (2 * np.pi)
    what0 = float(what(0.0))
    # zero shares: every zero is on the line (gamma real); the sum over rho and conj(rho) is 2 ghat(gamma), gamma > 0
    Zz = 2 * ghat_u(w, np.array(zeros_zeta)).sum()
    Zc = 2 * ghat_u(w, np.array(zeros_chi)).sum()
    # prime shares
    wl = w(np.log(ns))
    Pz = 4 * np.sum(LAM[2:] * wl / (ns + 1))
    Pc = 4 * np.sum(LAM[2:] * np.array([chi_n(int(n)) for n in ns]) * wl / (ns + 1))
    PK = 4 * np.sum(LAMK[2:] * wl / (ns + 1))
    Bz = 2 * what0 + arch_z; Bc = arch_c; BK = 2 * what0 + arch_z + arch_c
    res_z = Bz - Zz - Pz; res_c = Bc - Zc - Pc; res_K = BK - (Zz + Zc) - PK
    print(f"[{name}] ghat spot (u-quad vs conv) at r=0,3,12,14.13: " + ", ".join(f"{a:.9f}/{b:.9f}" for a, b in zip(spot, spot2)))
    print(f"[{name}] zeta : B = 2*{what0:.6f} + {arch_z:.9f} = {Bz:.9f};  Z = {Zz:.9f};  P = {Pz:.9f};  B - Z - P = {res_z:.3e}")
    print(f"[{name}] chi  : B = 0 + {arch_c:.9f} = {Bc:.9f};  Z = {Zc:.9f};  P = {Pc:.9f};  B - Z - P = {res_c:.3e}")
    print(f"[{name}] zeta_K: B_K = {BK:.9f};  Z_K = {Zz + Zc:.9f};  P_K = {PK:.9f} (= P_zeta + P_chi: {Pz + Pc:.9f});  B_K - Z_K - P_K = {res_K:.3e}")
    return dict(what0=what0, arch_zeta=arch_z, arch_chi=arch_c, B_zeta=Bz, Z_zeta=Zz, P_zeta=Pz, res_zeta=res_z,
                B_chi=Bc, Z_chi=Zc, P_chi=Pc, res_chi=res_c, B_K=BK, Z_K=Zz + Zc, P_K=PK, res_K=res_K,
                ghat_spot_uquad=spot.tolist(), ghat_spot_conv=spot2.tolist())
out["identity_wA"] = identity("w_A = e^{-u^2/2}(1+cos 12u)", wA, whatA)
out["identity_wB"] = identity("w_B = e^{-2u^2}", wB, whatB)
stopA = max(abs(out["identity_wA"]["res_K"]), abs(out["identity_wB"]["res_K"]))
print(f"STOP CONDITION (a): max |B_K - Z_K - P_K| = {stopA:.3e}  -> {'FIRED' if stopA > 1e-6 else 'not fired (identity holds to 1e-6)'}")
out["stop_a_max_residual"] = stopA

# ---------- (6) Psi_K near 0 and the domination test at t = 0 ----------
def PsiK(s):
    s = np.atleast_1d(s)
    tot = np.zeros_like(s, dtype=float)
    for z in zeros_zeta + zeros_chi:
        tot += 1.0 / np.cosh(np.pi * (s - z))
    return tot
sgrid = np.linspace(-4, 4, 801)
psi = PsiK(sgrid)
print(f"Psi_K(0) = {PsiK(0.0)[0]:.6e};  max_{{|s|<=4}} Psi_K = {psi.max():.6f} at s = {sgrid[psi.argmax()]:.3f};  Psi_K(zeros_chi[0]) = {PsiK(zeros_chi[0])[0]:.4f}")
out["PsiK_0"] = float(PsiK(0.0)[0]); out["PsiK_max_abs_s_le_4"] = float(psi.max()); out["PsiK_argmax"] = float(sgrid[psi.argmax()])
out["PsiK_at_first_chi_zero"] = float(PsiK(zeros_chi[0])[0])
def mu_y(xi, y): return 2 * np.cos(np.pi * y) * np.cosh(np.pi * xi) / (np.cosh(2 * np.pi * xi) + np.cos(2 * np.pi * y))
rows = []
for delta in (0.1, 0.05, 0.02, 0.01, 0.5):
    y = 0.5 - delta
    spos = np.linspace(0, 4, 401)
    lhs = 2 * mu_y(spos, y); rhs = PsiK(spos) + PsiK(-spos)
    viol = spos[lhs > rhs]
    rows.append(dict(delta=delta, two_over_sin=2 / np.sin(np.pi * delta), PsiK0_times2=2 * float(PsiK(0.0)[0]),
                     D_holds=bool(len(viol) == 0), violation_interval=[float(viol.min()), float(viol.max())] if len(viol) else None))
    print(f"(D_{{0,y}}) at delta = {delta}: 2 mu_y(0) = 2/sin(pi delta) = {2/np.sin(np.pi*delta):.4f} vs Psi_K(0)+Psi_K(-0) = {2*PsiK(0.0)[0]:.3e}; holds: {len(viol)==0}; violated on s in [{viol.min() if len(viol) else float('nan'):.2f}, {viol.max() if len(viol) else float('nan'):.2f}]")
out["domination_t0"] = rows
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "siegel_setup_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
