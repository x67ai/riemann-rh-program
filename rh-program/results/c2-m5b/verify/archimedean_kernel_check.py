#!/usr/bin/env python3
"""archimedean_kernel_check.py — FORMULATION.md (0.2)-(0.3).
(a) Verify the u-side form of the archimedean functional
      A_inf(g) := int ghat(tau) mu_inf(tau) dtau,
      mu_inf(tau) = (1/2pi) Re psi(1/4 + i tau/2) - (log pi)/(2 pi),
    against the claimed closed form for even C^2 g supported in [-1, 1]:
      A_inf(g) = - int_0^inf [g(u) e^{u/2} - g(0)] / sinh(u) du - (log 4pi + gamma_E) g(0).
    The tau-integral is done on [0, T0] with subdivision at multiples of pi (ghat oscillates with
    period 2pi for supp g = [-1,1]) plus an explicit tail bound |ghat(tau)| <= ||g''||_1 / tau^2.
(b) The dilation law: A(g_eps) - g(0) log(1/eps) -> a(g) as eps -> 0, g_eps(u) = g(u/eps),
    computed from the u-side form (exact), for the full A = pole + archimedean.
mpmath only; < 2 minutes.
"""
import mpmath as mp, time, sys
mp.mp.dps = 20
t0 = time.time()
def mu_inf(t):
    return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*t/2))/(2*mp.pi) - mp.log(mp.pi)/(2*mp.pi)
def ghat(g, tau):
    return 2*mp.quad(lambda u: g(u)*mp.cos(tau*u), [0, 0.25, 0.5, 0.75, 1])
def A_inf_direct(g, T0=200):
    n = int(T0/mp.pi) + 1
    pts = [k*mp.pi for k in range(n+1)]
    val = 2*mp.quad(lambda t: ghat(g, t)*mu_inf(t), pts)
    return val
def A_inf_uside(g):
    I = mp.quad(lambda u: (g(u)*mp.exp(u/2) - g(0))/mp.sinh(u), [0, 0.25, 0.5, 1, 3, 10, 40, mp.inf])
    return -I - (mp.log(4*mp.pi) + mp.euler)*g(0)
def A_full_uside(g, eps):
    # A(g_eps) = int g_eps 2cosh(u/2) du + A_inf(g_eps); supp g_eps = [-eps, eps]
    pole = 2*mp.quad(lambda u: g(u/eps)*2*mp.cosh(u/2), [0, eps/2, eps])
    I = mp.quad(lambda u: (g(u/eps)*mp.exp(u/2) - g(0))/mp.sinh(u), [0, eps/4, eps/2, eps, 2*eps, 1, 5, 20, mp.inf])
    return pole - I - (mp.log(4*mp.pi) + mp.euler)*g(0)
bumps = {
  "g1(u) = (1-u^2)^3 on |u|<1": (lambda u: (1-u**2)**3 if abs(u) < 1 else mp.mpf(0), 1),
  "g2(u) = cos(pi u/2)^4 on |u|<1": (lambda u: mp.cos(mp.pi*u/2)**4 if abs(u) < 1 else mp.mpf(0), 1),
}
print("(a) u-side form of A_inf against the direct tau-integral (T0 = 200; tail bound below)")
for name, (g, _) in bumps.items():
    g2n = 2*mp.quad(lambda u: abs(mp.diff(g, u, 2)), [0, 0.5, 0.999])  # ||g''||_1 (numerical)
    tail = g2n/mp.mpf(200) * (mp.log(200/(2*mp.pi))/(2*mp.pi) + 1)      # crude |int_{T0}^inf ghat mu| bound
    d = A_inf_direct(g); s = A_inf_uside(g)
    print(f"  {name}: direct = {mp.nstr(d, 12)}, u-side = {mp.nstr(s, 12)}, diff = {mp.nstr(d - s, 3)}, tail bound = {mp.nstr(tail, 3)}")
c1 = mp.quad(lambda u: (mp.exp(u/2)-1)/mp.sinh(u), [0, 1, 10, mp.inf])
print(f"  c1 = int_0^inf (e^(u/2)-1)/sinh u du = {mp.nstr(c1, 15)};  c_A = log(4pi)+gamma_E+c1 = {mp.nstr(mp.log(4*mp.pi)+mp.euler+c1, 15)}")
print("(b) dilation law: A(g_eps) - g(0) log(1/eps) for g = g1 (g(0) = 1)")
g = bumps["g1(u) = (1-u^2)^3 on |u|<1"][0]
prev = None
for eps in [mp.mpf('0.5'), mp.mpf('0.1'), mp.mpf('0.02'), mp.mpf('0.005'), mp.mpf('0.001'), mp.mpf('0.0002')]:
    v = A_full_uside(g, eps) - mp.log(1/eps)
    print(f"  eps = {mp.nstr(eps, 4)}: A(g_eps) = {mp.nstr(A_full_uside(g, eps), 10)},  A(g_eps) - log(1/eps) = {mp.nstr(v, 10)}" + (f"  (change {mp.nstr(v - prev, 3)})" if prev is not None else ""))
    prev = v
# the limit a(g) from the derivation: -1/2 * [ int_{|v|<1} (g(v)-g(0))/|v| dv - 2 g(0) * 0 ] ... computed as
# a(g) = - int_0^1 (g(v)-g(0))/v dv + g(0) * (limit constant): we print the numerical limit only.
print(f"done in {time.time()-t0:.1f} s")
