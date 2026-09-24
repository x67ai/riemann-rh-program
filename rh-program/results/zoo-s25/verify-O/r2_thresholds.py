# Reader check (Opus 5): D1 = 16 pi^2 e^{2 gamma}, D1+ for even characters, by direct quadrature of mu_0 * A_K.
from mpmath import mp, mpf, pi, euler, exp, log, psi, re, quad, sech, findroot, mpc, inf
mp.dps = 30
D1 = 16*pi**2*exp(2*euler)
print('D1 closed form 16 pi^2 e^{2g} =', D1, ' pi^2 e^{-2 psi(1/2)} =', pi**2*exp(-2*psi(0, mpf(1)/2)))
print('D0 = 4 D1 =', 4*D1)
def aK0(logD, even):
    # a_K(0) = int mu_0(r) A_K(r) dr, mu_0 = sech(pi r), A_K = (1/2pi)[bracket]
    if even:
        br = lambda r: 2*re(psi(0, mpc(0.25, r/2))) - 2*log(pi) + logD
    else:
        br = lambda r: re(psi(0, mpc(0.25, r/2))) + re(psi(0, mpc(0.75, r/2))) - 2*log(pi) + logD
    return quad(lambda r: sech(pi*r)*br(r)/(2*pi), [-inf, 0, inf])
lo = findroot(lambda L: aK0(L, False), log(500))
print('odd  threshold by quadrature:', exp(lo))
le = findroot(lambda L: aK0(L, True), log(3700))
print('even threshold by quadrature (D1+):', exp(le))
# monotonicity of a_K in |s| for the even case (sampled)
def aK(s, logD, even):
    br = (lambda r: 2*re(psi(0, mpc(0.25, r/2)))) if even else (lambda r: re(psi(0, mpc(0.25, r/2))) + re(psi(0, mpc(0.75, r/2))))
    return quad(lambda r: sech(pi*(s-r))*(br(r) - 2*log(pi) + logD)/(2*pi), [-inf, s, inf])
vals = [aK(s, le, True) for s in [0, 0.5, 1, 2, 4, 8]]
print('even a_K(s) at D1+, s=0,.5,1,2,4,8:', [float(v) for v in vals])
