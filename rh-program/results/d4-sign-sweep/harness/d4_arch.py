#!/usr/bin/env python3
"""d4_arch.py -- D4: the archimedean integral, the pole terms and the bracket at any height t (M6's ef_rhs_arch.py carried
above 1e6; the M6 method verbatim, plus (a) the argument r = t + eta/L formed in mpmath so that no digit of eta/L is lost
against a large t, (b) the bracket on TWO code paths at every point -- mpmath.digamma at 20 digits (M6's path) against an OWN
asymptotic-series evaluation psi(z) = log z - 1/(2z) - sum_k B_{2k}/(2k z^{2k}) after a recurrence shift to |z| >= 60,
at 30 digits (BRIEF stop line (6): agreement to 1e-12 required at every node sampled and at r = t), (c) the pole terms
ghat(i/2) + ghat(-i/2) bounded by Lemma G's strip-weighted decay at every t >= 1e3 (computed by quadrature only for t < 1e3).

  ARCH = (1/(2 pi L^3)) int eta^2 Bhat(eta)^2 bracket(t + eta/L) d eta,  bracket_zeta(r) = Re psi(1/4 + i r/2) - log pi,
  bracket_DH(r) = Re psi(3/4 + i r/2) + log(5/pi);  Bhat by the 16384-node trapezoid (own numpy), eta-trapezoid step 0.25 on
  [-3000, 3000] with the h = 0.5 and H = 2000 convergence checks (M6 section 2 item 6).

usage: d4_arch.py --kind zeta|dh --t <decimal> --L <L> [--out out/arch_<tag>.json]
"""
import json, time, sys, math, datetime, os, argparse
import numpy as np
import mpmath as mp
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument('--kind', default='zeta'); ap.add_argument('--t', required=True); ap.add_argument('--L', type=float, required=True)
ap.add_argument('--out', default=None); ap.add_argument('--h', type=float, default=0.25); ap.add_argument('--H', type=float, default=3000.0)
A = ap.parse_args()
logf = open(os.path.join(HERE, 'd4_arch_run.log'), 'a')
def out(s):
    print(s); logf.write(s + "\n"); logf.flush()
t0 = time.time()
kind, L = A.kind, A.L
t_mp = mp.mpf(A.t)                      # exact decimal of the height
t_f = float(A.t)
out(f"[{now()}] d4_arch.py start: kind={kind} t={A.t} L={L}")

# ---------------------------------------------------------------- Bhat (double, trapezoid, own implementation; as M6)
M = 16384
v = np.arange(1, M) / M - 0.5
with np.errstate(all='ignore'):
    braw = np.exp(-1.0 / (1.0 - 4.0 * v * v))
braw[~np.isfinite(braw)] = 0.0
Z = braw.sum() / M
wB = braw / braw.sum()
def bhat(eta):
    eta = np.atleast_1d(np.asarray(eta, float)); res = np.empty_like(eta); step = 2000
    with np.errstate(all='ignore'):     # numpy 2.0's matmul raises spurious fp warnings on this BLAS; the values equal M6's to all printed digits
        for i in range(0, len(eta), step): res[i:i+step] = np.cos(np.outer(eta[i:i+step], v)) @ wB
    return res
mp.mp.dps = 30
def braw_mp(x):
    x = mp.mpf(x); return mp.e**(-1/(1 - 4*x*x)) if abs(x) < mp.mpf(1)/2 else mp.mpf(0)
Zmp = mp.quad(braw_mp, [-0.5, -0.25, 0, 0.25, 0.5])
def bhat_mp(eta):
    eta = mp.mpf(eta); n = max(8, int(abs(eta))//3 + 8); pts = [-0.5 + k/n for k in range(n+1)]
    return mp.quad(lambda x: braw_mp(x)*mp.cos(eta*x), pts)/Zmp
chk = [(e, float(bhat(e)[0]), float(bhat_mp(e)), float(bhat(e)[0] - bhat_mp(e))) for e in [0.0, 5.5, 37.25, 250.0]]
out(f"[{now()}] Z_trap = {Z:.16f}  Z_mp = {mp.nstr(Zmp, 20)};  Bhat trapezoid vs mpmath (eta, trap, mp, diff): {chk}")

# ---------------------------------------------------------------- the bracket, two code paths
def bracket_mp(kind, r):                 # path 1: mpmath.digamma at 20 digits (M6)
    mp.mp.dps = 20
    r = mp.mpf(r)
    if kind == 'zeta': val = mp.re(mp.digamma(mp.mpf(1)/4 + 1j*r/2)) - mp.log(mp.pi)
    else: val = mp.re(mp.digamma(mp.mpf(3)/4 + 1j*r/2)) + mp.log(5/mp.pi)
    mp.mp.dps = 30
    return val
def psi_asym(z, K=14, shift_to=60):      # path 2: own asymptotic series with a recurrence shift; 30 digits
    z = mp.mpc(z); s = mp.mpf(0); m = 0
    while abs(z) < shift_to: s += 1/z; z += 1; m += 1
    acc = mp.log(z) - 1/(2*z)
    z2 = z*z; zp = z2
    for k in range(1, K+1):
        acc -= mp.bernoulli(2*k)/(2*k*zp); zp *= z2
    return acc - s
def bracket_asym(kind, r):
    r = mp.mpf(r)
    if kind == 'zeta': return mp.re(psi_asym(mp.mpf(1)/4 + 1j*r/2)) - mp.log(mp.pi)
    else: return mp.re(psi_asym(mp.mpf(3)/4 + 1j*r/2)) + mp.log(5/mp.pi)

# ---------------------------------------------------------------- ARCH
def arch(kind, h, H, two_path_every=2000):
    eta = np.arange(-H, H + h/2, h)
    F = eta*eta*bhat(eta)**2
    br = np.empty_like(eta); worst2 = 0.0; n2 = 0
    for i, e in enumerate(eta):
        r = t_mp + mp.mpf(e)/L                          # exact against a large t
        b1 = bracket_mp(kind, r); br[i] = float(b1)
        if i % two_path_every == 0:
            b2 = bracket_asym(kind, r); worst2 = max(worst2, abs(float(b1 - b2))); n2 += 1
    return float(h*np.sum(F*br)/(2*np.pi*L**3)), len(eta), float(h*np.sum(F)), float(abs(F[0]) + abs(F[-1])), worst2, n2

val, nn, parseval, endpt, worst2, n2 = arch(kind, A.h, A.H)
val2 = arch(kind, 2*A.h, A.H, 10**9)[0]
val3 = arch(kind, A.h, A.H*2/3, 10**9)[0]
b_at_t_1 = bracket_mp(kind, t_mp); b_at_t_2 = bracket_asym(kind, t_mp)
two_path_at_t = abs(float(b_at_t_1 - b_at_t_2))
model = 16.62196534693389/L**3 * float(b_at_t_1)
stop6 = max(two_path_at_t, worst2) > 1e-12
out(f"[{now()}] ARCH_{kind}(t={A.t}, L={L}) = {val:.15e}  (h={2*A.h}: {val2:.15e}, H={A.H*2/3:g}: {val3:.15e}; |dh| = {abs(val-val2):.1e}, |dH| = {abs(val-val3):.1e}); "
    f"int eta^2 Bhat^2 = {parseval:.12f} vs 2pi||B'||^2 = {2*np.pi*16.62196534693389:.12f}; endpoint |F| = {endpt:.1e}; model ||B'||^2/L^3*bracket(t) = {model:.15e} (rel. diff {abs(val-model)/abs(val):.1e})")
out(f"[{now()}] bracket at r = t: mpmath.digamma(20 digits) = {mp.nstr(b_at_t_1, 20)}, own asymptotic series (30 digits) = {mp.nstr(b_at_t_2, 20)}, |diff| = {two_path_at_t:.2e}; "
    f"worst |diff| over {n2} sampled nodes = {worst2:.2e}; stop line (6) (1e-12): {'FIRES' if stop6 else 'does not fire'}")

# ---------------------------------------------------------------- pole terms (zeta only)
pole = {}
if kind == 'zeta':
    if t_f < 1e3:
        mp.mp.dps = 30
        def bhat_c(z):
            z = mp.mpc(z); n = max(8, int(abs(z.real))//3 + 8); pts = [-0.5 + k/n for k in range(n+1)]
            return mp.quad(lambda x: braw_mp(x)*mp.e**(1j*z*x), pts)/Zmp
        zp = mp.mpc(0, 0.5); zm = mp.mpc(0, -0.5)
        hp = (zp - t_mp)*bhat_c(L*(zp - t_mp)); hm = (zm - t_mp)*bhat_c(L*(zm - t_mp))
        g = hp*mp.conj(hm)
        pole = dict(method='quadrature', ghat_i2_re=float(g.real), ghat_i2_im=float(g.imag), pole_term_2Re=float(2*g.real))
        out(f"[{now()}] pole term ghat(i/2)+ghat(-i/2) = 2 Re ghat(i/2) = {float(2*g.real):.6e} (quadrature at 30 digits)")
    else:
        CB = math.e**2/float(Z); cB = 2/math.sqrt(72*math.e)
        x = t_f*L; y = L/2
        log10_bound = (math.log(2*(t_f**2 + 0.25)) + 2*(y/2 + math.log(CB) + math.log1p(cB/2*math.sqrt(x)) - cB*math.sqrt(x)))/math.log(10)
        pole = dict(method='Lemma-G bound', log10_lemmaG_bound_on_pole_term=log10_bound, pole_term_2Re=0.0)
        out(f"[{now()}] pole term: Lemma-G strip-weighted bound |ghat(i/2)+ghat(-i/2)| <= 2 (t^2 + 1/4) [e^(L/4) G1(tL)]^2 = 10^{log10_bound:.1f} (taken as 0 in W)")

res = dict(date=now(), kind=kind, t=A.t, t_float=t_f, L=L, arch=val, arch_h2=val2, arch_H2over3=val3, conv_h=val-val2, conv_H=val-val3, nodes=nn,
           parseval_check=parseval, parseval_expected=2*np.pi*16.62196534693389, endpoint_F=endpt, model_value=model,
           bracket_at_t_mpmath=float(b_at_t_1), bracket_at_t_asym=float(b_at_t_2), bracket_two_path_diff_at_t=two_path_at_t,
           bracket_two_path_worst_over_nodes=worst2, bracket_two_path_nodes=n2, stop_line_6_fires=bool(stop6),
           Z_trap=float(Z), Z_mp=float(Zmp), bhat_check=chk, pole=pole, seconds=time.time()-t0)
outp = A.out or os.path.join(HERE, '..', 'out', f"arch_{kind}_t{A.t}_L{L:g}.json")
json.dump(res, open(outp, 'w'), indent=1)
out(f"[{now()}] wrote {outp} in {time.time()-t0:.1f}s")
