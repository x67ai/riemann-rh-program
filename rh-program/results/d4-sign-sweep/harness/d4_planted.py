#!/usr/bin/env python3
"""d4_planted.py -- D4 Control 2 (zero side): plant the orbit {+-t +- i delta} and evaluate its share of W_Z(f_{t,L}) with the
harness's OWN kernel (the 16384-node trapezoid Bhat of d4_arch.py, extended to complex argument), against the expected value
-2 delta^2 c(delta L)^2 with c(lambda) = int B(v) cosh(lambda v) dv = Bhat(+-i lambda) by mpmath quadrature at 30 digits
(separation-note.md section 0.2-0.3: the pair at +t contributes h_f(t - i delta) conj(h_f(t + i delta)) + h_f(t + i delta)
conj(h_f(t - i delta)) = -2 delta^2 c^2; the reflected pair at -t is bounded by Lemma G's strip-weighted decay at real part
-2 t L and is printed as a log10 bound, computed by quadrature only for t < 1e3).
  h_f(z) = (z - t) Bhat(L (z - t)),  Bhat(z) = int B(v) e^{i z v} dv.
Control passes when |kernel value - expected| <= 1e-12 * |expected| (the kernel's quadrature budget; the trapezoid is
spectrally accurate on this Gevrey-2 integrand and the M6 checks put Bhat at <= 5e-17 absolute).
usage: d4_planted.py --t <decimal> --L <L> --delta <delta> [--out out/planted_t<t>_L<L>.json]
"""
import json, math, time, datetime, os, argparse
import numpy as np
import mpmath as mp
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(); ap.add_argument('--t', required=True); ap.add_argument('--L', type=float, required=True); ap.add_argument('--delta', type=float, required=True); ap.add_argument('--out', default=None)
A = ap.parse_args()
logf = open(os.path.join(HERE, 'd4_planted_run.log'), 'a')
def out(s):
    print(s); logf.write(s + "\n"); logf.flush()
t0 = time.time(); L = A.L; d = A.delta; t_mp = mp.mpf(A.t); t_f = float(A.t)
out(f"[{now()}] d4_planted.py start: t={A.t} L={L} delta={d}")
# harness kernel (as d4_arch.py; complex argument)
M = 16384
v = np.arange(1, M) / M - 0.5
with np.errstate(all='ignore'):
    braw = np.exp(-1.0 / (1.0 - 4.0 * v * v))
braw[~np.isfinite(braw)] = 0.0
Z = braw.sum() / M
wB = braw / braw.sum()
def bhat_c(z):                      # Bhat(z) = sum_v w_B exp(i z v), complex z (the kernel's own trapezoid)
    z = complex(z); return complex(np.sum(wB * np.exp(1j * z * v)))
def h_f(z_minus_t):                 # h_f(z) with z - t given (so that no digit of delta is lost against a large t)
    return z_minus_t * bhat_c(L * z_minus_t)
# the pair at +t, with the kernel: gamma = t - i d and gamma = t + i d; summand h_f(gamma) conj(h_f(conj gamma))
hm = h_f(-1j*d); hp = h_f(1j*d)
s1 = hm * np.conj(hp)               # gamma = t - i d: h_f(t - i d) conj(h_f(t + i d))
s2 = hp * np.conj(hm)               # gamma = t + i d
kernel_pair = s1 + s2
c_kernel = bhat_c(-1j*d*L).real
# expected: c(dL) by mpmath quadrature at 30 digits
mp.mp.dps = 30
def braw_mp(x):
    x = mp.mpf(x); return mp.e**(-1/(1 - 4*x*x)) if abs(x) < mp.mpf(1)/2 else mp.mpf(0)
Zmp = mp.quad(braw_mp, [-0.5, -0.25, 0, 0.25, 0.5])
lam = mp.mpf(d)*L
c_mp = mp.quad(lambda x: braw_mp(x)*mp.cosh(lam*x), [-0.5, -0.25, 0, 0.25, 0.5])/Zmp
expected = -2*mp.mpf(d)**2*c_mp**2
diff = abs(mp.mpf(kernel_pair.real) - expected); rel = diff/abs(expected)
ok = (rel <= mp.mpf('1e-12')) and abs(kernel_pair.imag) <= 1e-12*abs(expected)
# reflected pair at -t: Lemma G strip-weighted bound (t >= 1e3) or quadrature (t < 1e3)
CB = math.e**2/float(Z); cB = 2/math.sqrt(72*math.e)
if t_f >= 1e3:
    x = 2*t_f*L; y = d*L
    log10_refl = (math.log(2*((2*t_f)**2 + d*d)) + 2*(y/2 + math.log(CB) + math.log1p(cB/2*math.sqrt(x)) - cB*math.sqrt(x)))/math.log(10)
    refl = dict(method='Lemma-G bound', log10_bound=log10_refl)
else:
    def bhat_mpc(z):
        z = mp.mpc(z); n = max(8, int(abs(z.real))//3 + 8); pts = [-0.5 + k/n for k in range(n+1)]
        return mp.quad(lambda xx: braw_mp(xx)*mp.e**(1j*z*xx), pts)/Zmp
    zm = mp.mpc(-2*t_mp, -d); zp = mp.mpc(-2*t_mp, d)
    hh = (zm*bhat_mpc(L*zm))*mp.conj(zp*bhat_mpc(L*zp))
    refl = dict(method='quadrature', E_minus=float(2*hh.real))
edge_law_note = 'edge-law constants (C2 Instruments line 104) apply only for lambda = delta L >= 25; not used here' if lam < 25 else 'lambda >= 25: edge law applicable'
out(f"[{now()}] planted orbit at (t = {A.t}, L = {L}, delta = {d}), lambda = delta L = {float(lam):.6f}: c(lambda) kernel = {c_kernel:.16f}, mpmath = {mp.nstr(c_mp, 18)}; "
    f"pair at +t (kernel) = {kernel_pair.real:.15e} + {kernel_pair.imag:.1e} i; expected -2 delta^2 c^2 = {mp.nstr(expected, 16)}; |diff| = {float(diff):.2e} (rel {float(rel):.2e}) -> {'PASS' if ok else 'FAIL'}; "
    f"reflected pair at -t: {refl}; {edge_law_note}")
res = dict(date=now(), t=A.t, L=L, delta=d, lambda_=float(lam), c_kernel=c_kernel, c_mpmath=float(c_mp), pair_kernel_re=kernel_pair.real, pair_kernel_im=kernel_pair.imag,
           expected=float(expected), abs_diff=float(diff), rel_diff=float(rel), pass_=bool(ok), reflected_pair=refl, Z_trap=float(Z), Z_mp=float(Zmp), seconds=time.time()-t0)
outp = A.out or os.path.join(HERE, '..', 'out', f"planted_t{A.t}_L{L:g}_d{d:g}.json")
json.dump(res, open(outp, 'w'), indent=1)
out(f"[{now()}] wrote {outp} ({time.time()-t0:.1f}s)")
