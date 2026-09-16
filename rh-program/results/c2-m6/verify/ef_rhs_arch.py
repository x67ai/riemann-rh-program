#!/usr/bin/env python3
"""ef_rhs_arch.py -- M6 rung 1: the archimedean integral and the pole terms of the explicit formula's right-hand side
for the test g = f * f~, f = f_{t,L} = i (B_L)' e^{-itu} (separation-note.md section 0.1), for zeta and for DH.

Lean `Zeta23/ExplicitFormula.lean` 70-74 (`literatureRHS`, quoted verbatim in the note):
  sum_rho m_rho ghat(gamma_rho) = ghat(i/2) + ghat(-i/2) - sum_n Lambda(n) n^{-1/2} (g(log n) + g(-log n))
                                 + (1/2pi) int ghat(r) [Re psi(1/4 + ir/2) - log pi] dr,
with ghat(r) = |h_f(r)|^2 = (r - t)^2 Bhat(L(r - t))^2 for real r (identity (0.1)-(0.2)).
For DH (completed function (5/pi)^{(s+1)/2} Gamma((s+1)/2) f_DH(s), dh.py; entire, no pole terms): the bracket is
  Re psi(3/4 + ir/2) + log(5/pi)   [2 Re Gamma_f'/Gamma_f(1/2 + ir) + 2 log Q with Gamma_f(s) = Gamma((s+1)/2), Q^2 = 5/pi],
and there are no ghat(+-i/2) terms.
Substituting eta = L (r - t):  ARCH = (1/(2 pi L^3)) int eta^2 Bhat(eta)^2 bracket(t + eta/L) d eta.

Bhat by the trapezoid rule on M = 16384 nodes (own numpy code; the same rule campaign_lib.py uses, re-implemented);
checked against mpmath quadrature at three arguments.  psi by mpmath.digamma at dps 20.  The eta-integral by the
composite trapezoid rule on [-H, H]: eta^2 Bhat(eta)^2 has Fourier support in [-1, 1] (it is the transform of the
autocorrelation of (B')-type functions on [-1/2, 1/2] convolved with itself), so for step h < 2 pi the trapezoid rule is
exact on that factor up to the bracket's slow modulation; convergence is shown by halving h and by changing H.
ghat(+-i/2) at t = 85.7 by mpmath quadrature (subdivided, dps 30); at t = 1e6 by the Paley-Wiener/Lemma-G bound and a
double-precision quadrature (noise floor only).
"""
import json, time, sys, math, datetime
import numpy as np
import mpmath as mp

T85 = 85.69934848537759
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
t0 = time.time()
print(f"[{now()}] ef_rhs_arch.py start")

# ---------------------------------------------------------------- Bhat (double, trapezoid, own implementation)
M = 16384
v = np.arange(1, M) / M - 0.5
with np.errstate(all='ignore'):
    braw = np.exp(-1.0 / (1.0 - 4.0 * v * v))
braw[~np.isfinite(braw)] = 0.0
Z = braw.sum() / M
wB = braw / braw.sum()
def bhat(eta):
    eta = np.atleast_1d(np.asarray(eta, float))
    out = np.empty_like(eta)
    step = 2000
    for i in range(0, len(eta), step):
        out[i:i+step] = np.cos(np.outer(eta[i:i+step], v)) @ wB
    return out
# check against mpmath
mp.mp.dps = 30
def braw_mp(x):
    x = mp.mpf(x)
    return mp.e**(-1/(1 - 4*x*x)) if abs(x) < mp.mpf(1)/2 else mp.mpf(0)
Zmp = mp.quad(braw_mp, [-0.5, -0.25, 0, 0.25, 0.5])
def bhat_mp(eta):
    eta = mp.mpf(eta); n = max(8, int(abs(eta))//3 + 8)
    pts = [-0.5 + k/n for k in range(n+1)]
    return mp.quad(lambda x: braw_mp(x)*mp.cos(eta*x), pts)/Zmp
chk = []
for e in [0.0, 5.5, 37.25, 250.0]:
    a = float(bhat(e)[0]); b = bhat_mp(e)
    chk.append((e, a, float(b), float(a - b)))
print(f"[{now()}] Z_trap = {Z:.16f}  Z_mp = {mp.nstr(Zmp, 20)};  Bhat trapezoid vs mpmath quad (eta, trap, mp, diff): {chk}")

# ---------------------------------------------------------------- the bracket
def bracket(kind, r):
    mp.mp.dps = 20
    if kind == 'zeta':
        return float(mp.re(mp.digamma(mp.mpf(1)/4 + 1j*mp.mpf(r)/2)) - mp.log(mp.pi))
    else:
        return float(mp.re(mp.digamma(mp.mpf(3)/4 + 1j*mp.mpf(r)/2)) + mp.log(5/mp.pi))

def arch(kind, t, L, h, H):
    eta = np.arange(-H, H + h/2, h)
    F = eta*eta*bhat(eta)**2
    br = np.array([bracket(kind, t + e/L) for e in eta])
    return float(h*np.sum(F*br)/(2*np.pi*L**3)), len(eta), float(h*np.sum(F)), float(np.abs(F[0]) + np.abs(F[-1]))

results = {}
for kind, t, Ls in [('zeta', T85, (10.0, 20.0)), ('zeta', 1e6, (10.0, 20.0)), ('dh', T85, (10.0, 20.0))]:
    for L in Ls:
        key = f"{kind}_t{t:g}_L{L:g}"
        val, nn, parseval, endpt = arch(kind, t, L, 0.25, 3000.0)
        val2, _, _, _ = arch(kind, t, L, 0.5, 3000.0)
        val3, _, _, _ = arch(kind, t, L, 0.25, 2000.0)
        model = 16.62196534693389/L**3 * bracket(kind, t)      # ||B'||_2^2/L^3 x bracket(t): the 'density-model' value
        results[key] = dict(kind=kind, t=t, L=L, arch=val, arch_h0p5=val2, arch_H2000=val3, conv_h=val - val2, conv_H=val - val3,
                            nodes=nn, parseval_check=parseval, parseval_expected=2*np.pi*16.62196534693389, endpoint_F=endpt,
                            model_value=model, bracket_at_t=bracket(kind, t))
        print(f"[{now()}] ARCH {key}: {val:.15e}  (h=0.5: {val2:.15e}, H=2000: {val3:.15e}; |dh| = {abs(val-val2):.1e}, |dH| = {abs(val-val3):.1e}); "
              f"int eta^2 Bhat^2 = {parseval:.12f} vs 2pi||B'||^2 = {2*np.pi*16.62196534693389:.12f}; endpoint |F| = {endpt:.1e}; model ||B'||^2/L^3*bracket(t) = {model:.6e}")

# ---------------------------------------------------------------- ghat(+-i/2) for zeta at t = 85.7 (DH has none)
# ghat(i/2) = h_f(i/2) conj(h_f(-i/2)),  h_f(z) = (z - t) Bhat(L (z - t)),  Bhat(z) = int B(v) e^{izv} dv (complex z).
# ghat(-i/2) = conj(ghat(i/2)), so the pole term is 2 Re ghat(i/2).
mp.mp.dps = 30
def bhat_c(z):
    z = mp.mpc(z); n = max(8, int(abs(z.real))//3 + 8)
    pts = [-0.5 + k/n for k in range(n+1)]
    return mp.quad(lambda x: braw_mp(x)*mp.e**(1j*z*x), pts)/Zmp
pole = {}
for L in (10.0, 20.0):
    t = mp.mpf(T85); L = mp.mpf(L)
    zp = mp.mpc(0, 0.5); zm = mp.mpc(0, -0.5)
    hp = (zp - t)*bhat_c(L*(zp - t)); hm = (zm - t)*bhat_c(L*(zm - t))
    g = hp*mp.conj(hm)
    pole[f"zeta_t85.7_L{float(L):g}"] = dict(ghat_i2_re=float(g.real), ghat_i2_im=float(g.imag), pole_term_2Re=float(2*g.real),
                                             abs_hf_i2=float(abs(hp)), abs_bhat=float(abs(bhat_c(L*(zp - t)))))
    print(f"[{now()}] zeta t=85.7 L={float(L):g}: ghat(i/2) = {mp.nstr(g, 6)};  pole term ghat(i/2)+ghat(-i/2) = 2 Re = {mp.nstr(2*g.real, 6)};  |Bhat(L(i/2 - t))| = {mp.nstr(abs(bhat_c(L*(zp - t))), 4)}")
# t = 1e6: Lemma G complex-argument bound |Bhat(x + iy)| <= e^{|y|/2} C_B (1 + (c_B/2) sqrt|x|) e^{-c_B sqrt|x|}  (note section 2, G1 with the strip weight)
CB = math.e**2/float(Z); cB = 2/math.sqrt(72*math.e)
for L in (10.0, 20.0):
    x = 1e6*L; y = L/2
    # log10 of the bound computed analytically (the bound itself underflows double)
    log10_bound = (math.log(2*((1e6)**2 + 0.25)) + 2*(y/2 + math.log(CB) + math.log1p(cB/2*math.sqrt(x)) - cB*math.sqrt(x)))/math.log(10)
    pole[f"zeta_t1e6_L{L:g}"] = dict(log10_lemmaG_bound_on_pole_term=log10_bound)
    print(f"[{now()}] zeta t=1e6 L={L:g}: Lemma-G bound on |ghat(i/2)+ghat(-i/2)| <= 2 (t^2 + 1/4) [e^{{L/4}} G1(tL)]^2 = 10^{log10_bound:.1f}")

out = dict(date=now(), Z_trap=float(Z), Z_mp=float(Zmp), bhat_check=chk, arch=results, pole=pole, seconds=time.time() - t0)
json.dump(out, open('out/ef_rhs_arch.json', 'w'), indent=1)
print(f"[{now()}] wrote out/ef_rhs_arch.json in {time.time() - t0:.1f}s")
