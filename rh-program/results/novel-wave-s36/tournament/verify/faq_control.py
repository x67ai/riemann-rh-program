"""faq_control.py -- verify the positive-coefficient RH-false control
F_{a,q}(s) = zeta(s) (1 + a q^{-s} + q^{1-2s}),  a > 2 sqrt(q).
Checks: (1) functional equation of the completed function; (2) off-line zeros from
1 + a u + q u^2 = 0, u = q^{-s}; (3) Dirichlet coefficients c_n >= 0; (4) Lambda_F(q^k) signs
(where the Euler-product/Ramanujan hypotheses fail)."""
import mpmath as mp
mp.mp.dps = 30

def P(s, a, q):
    return 1 + a*q**(-s) + q**(1-2*s)

def Lam(s, a, q):  # completed: pi^{-s/2} Gamma(s/2) zeta(s) * q^{s/2}... check symmetric normalization
    return q**(s/2) * q**(s/2) * mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)*P(s, a, q) / q**(mp.mpf(1)/2)

for (a, q) in [(3, 2), (5, 5), (2.9, 2), (4.5, 5)]:
    a = mp.mpf(a); q = mp.mpf(q)
    print("=== a=%s q=%s  a>2sqrt(q)? %s" % (a, q, a > 2*mp.sqrt(q)))
    # (1) FE: Lam(s) vs Lam(1-s)
    for s in [mp.mpc(0.3, 7.1), mp.mpc(0.8, 21.3), mp.mpc(-0.4, 3.3)]:
        r = abs(Lam(s, a, q) - Lam(1-s, a, q))/abs(Lam(s, a, q))
        print("  FE rel err at s=%s: %s" % (mp.nstr(s, 4), mp.nstr(r, 3)))
    # (2) zeros of 1 + a u + q u^2
    disc = a*a - 4*q
    us = [(-a + mp.sqrt(disc))/(2*q), (-a - mp.sqrt(disc))/(2*q)]
    for u in us:
        # u = q^{-s}: s = -log(u)/log q ; u<0 gives imaginary part pi/log q (mod 2pi/log q)
        s = -mp.log(mp.mpc(u))/mp.log(q)
        print("  root u=%s -> s=%s (sigma=%s); |F(s)|=%s" % (mp.nstr(u, 8), mp.nstr(s, 10), mp.nstr(s.real, 8), mp.nstr(abs(mp.zeta(s)*P(s, a, q)), 3)))
    # (3) coefficients c_n = 1 + a[q|n] + q[q^2|n] >= 0 trivially for a>0
    # (4) Lambda_F(q^k) = log q (1 - alpha^k - beta^k), alpha+beta=-a, alpha*beta=q
    al = (-a + mp.sqrt(disc))/2; be = (-a - mp.sqrt(disc))/2
    print("  alpha,beta =", mp.nstr(al, 8), mp.nstr(be, 8), " |.|/sqrt q:", mp.nstr(abs(al)/mp.sqrt(q), 6), mp.nstr(abs(be)/mp.sqrt(q), 6))
    print("  Lambda_F(q^k)/log q, k=1..6:", [mp.nstr(1 - al**k - be**k, 6) for k in range(1, 7)])
