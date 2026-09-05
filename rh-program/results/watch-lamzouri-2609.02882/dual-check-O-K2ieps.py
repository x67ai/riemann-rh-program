#!/usr/bin/env python3
"""
Dual-model check (Opus 5), Session 16, 2026-09-05.
Independent re-derivation of the load-bearing numbers for the classification of
Lamzouri, arXiv:2609.02882v1, inside the program's bandwidth-one PairCeiling class.

All quantities are computed from the paper's own definitions, at 30 significant
digits with mpmath, with no reliance on any earlier session's numbers.

Fourier convention (paper eq. 2.3):   fhat(xi) = int f(u) e^{-2 pi i xi u} du,  xi in C.
Montgomery-Taylor window (paper, proof of Lemma 3.2):
    f0(x) = cos(sqrt2 x) / (sqrt2 sin(1/sqrt2))   on I = [-1/2, 1/2],  0 outside.
K = f0hat = (eta^2)hat with eta^2 = f0;  Q0 = f0 * f0;  Qhat0 = K^2.
"""
import mpmath as mp

mp.mp.dps = 40
s2 = mp.sqrt(2)
inv_s2 = 1 / s2
A = 1 / (s2 * mp.sin(inv_s2))            # normalizing constant of f0

def f0(x):
    if abs(x) > mp.mpf(1) / 2:
        return mp.mpf(0)
    return A * mp.cos(s2 * x)

# ---------------------------------------------------------------- sanity: int f0 = 1
I_f0 = mp.quad(lambda x: A * mp.cos(s2 * x), [-mp.mpf(1)/2, mp.mpf(1)/2])
print("int f0            =", mp.nstr(I_f0, 30))

# ------------------------------------------------- Q0 = f0*f0 in closed form on [0,1]
# Q0(x) = A^2 [ sin(sqrt2 (1-x))/(2 sqrt2) + (1-x) cos(sqrt2 x)/2 ],  0 <= x <= 1
def Q0(x):
    x = mp.mpf(x)
    return A**2 * (mp.sin(s2 * (1 - x)) / (2 * s2) + (1 - x) * mp.cos(s2 * x) / 2)

def Q0p(x):                                            # Q0'
    x = mp.mpf(x)
    return A**2 * (-mp.cos(s2*(1-x))/2 - mp.cos(s2*x)/2 - (s2/2)*(1-x)*mp.sin(s2*x))

def Q0pp(x):                                           # Q0''
    x = mp.mpf(x)
    return A**2 * (-(s2/2)*mp.sin(s2*(1-x)) + s2*mp.sin(s2*x) - (1-x)*mp.cos(s2*x))

# check the closed form against a direct numerical convolution
for xt in ['0', '0.25', '0.6', '0.999']:
    xt = mp.mpf(xt)
    num = mp.quad(lambda u: f0(u) * f0(xt - u), [xt - mp.mpf(1)/2, mp.mpf(1)/2])
    print("Q0(%s): closed %s  numeric %s" % (mp.nstr(xt,4), mp.nstr(Q0(xt),25), mp.nstr(num,25)))

print()
print("Q0(0)  = int f0^2  =", mp.nstr(Q0(0), 30),
      " (direct:", mp.nstr(mp.quad(lambda u: f0(u)**2, [-mp.mpf(1)/2, mp.mpf(1)/2]), 30), ")")
print("Q0(1)  =", mp.nstr(Q0(1), 30))

# ------------------------------------------------------- the Montgomery-Taylor constant
tail = 2 * mp.quad(lambda a: a * Q0(a), [0, 1])
C_MT = Q0(0) + tail
C_MT_closed = mp.mpf(1)/2 + inv_s2 / mp.tan(inv_s2)
C0_closed = mp.mpf(3)/2 - inv_s2 / mp.tan(inv_s2)
print()
print("2 int_0^1 a Q0(a) da =", mp.nstr(tail, 30))
print("C_MT = Q0(0)+2int   =", mp.nstr(C_MT, 30))
print("C_MT closed form    =", mp.nstr(C_MT_closed, 30))
print("C_MT difference     =", mp.nstr(C_MT - C_MT_closed, 10))
print("C0 = 2 - C_MT       =", mp.nstr(2 - C_MT, 30))
print("C0 closed form      =", mp.nstr(C0_closed, 30))

# ------------------------------------------- the certificate (c0, r) and its ceiling data
c0 = 2 - Q0(0)
r  = lambda x: -2 * Q0(x)
rp = lambda x: -2 * Q0p(x)
rpp= lambda x: -2 * Q0pp(x)
v  = c0 + mp.quad(lambda x: r(x) * x, [0, 1])
print()
print("c0 = 2 - Q0(0)      =", mp.nstr(c0, 30))
print("v  = c0 + int r x   =", mp.nstr(v, 30), "   (must equal 2 - C_MT)")
print("r(1)                =", mp.nstr(r(1), 30))
print("|r'(1)|             =", mp.nstr(abs(rp(1)), 30))
# does r'' change sign on [0,1]?
sgn = [mp.sign(rpp(mp.mpf(k)/200)) for k in range(201)]
print("sign changes of r'' on [0,1]:", sum(1 for i in range(200) if sgn[i] != sgn[i+1]))
int_abs_rpp = mp.quad(lambda x: abs(rpp(x)), [0, 1])
print("int_0^1 |r''|       =", mp.nstr(int_abs_rpp, 30))
budget = abs(rp(1)) + int_abs_rpp
print("|r'(1)| + int|r''|  =", mp.nstr(budget, 30))
ceil = mp.mpf('0.68182868746') + mp.mpf('2.5431316e-6') * budget
print("ceiling for this r  =", mp.nstr(ceil, 20))
print("headroom ceiling - v=", mp.nstr(ceil - v, 20))

# ------------------------------------------------ the flat-window (AF Theorem B) instance
lam = mp.mpf(1)
Qf  = lambda x: (lam - abs(x)) / lam**2 if abs(x) <= lam else mp.mpf(0)
c0f = 2 - Qf(0)
vf  = c0f + mp.quad(lambda x: -2 * Qf(x) * x, [0, 1])
print()
print("flat window lambda=1: c0 =", mp.nstr(c0f, 10), " r(x) = -2(1-x),  v =", mp.nstr(vf, 20))
print("0.68182868746 - 2/3 =", mp.nstr(mp.mpf('0.68182868746') - mp.mpf(2)/3, 10))
print("0.68182868746 - v   =", mp.nstr(mp.mpf('0.68182868746') - v, 10))

# ---------------------------------------------------------------- K(2 i eps) and K^2
# K(2 i eps) = int f0(u) e^{4 pi eps u} du = int f0(u) cosh(4 pi eps u) du   (f0 even)
def K2ie(eps):
    eps = mp.mpf(eps)
    c = 4 * mp.pi * eps
    return mp.quad(lambda u: A * mp.cos(s2 * u) * mp.cosh(c * u), [-mp.mpf(1)/2, mp.mpf(1)/2])

def K2ie_closed(eps):
    eps = mp.mpf(eps); b = s2; c = 4 * mp.pi * eps
    return A * 2 * (b*mp.sin(b/2)*mp.cosh(c/2) + c*mp.cos(b/2)*mp.sinh(c/2)) / (b**2 + c**2)

print()
print("eps        K(2 i eps)                          K(2 i eps)^2                     RHS = 2-2K^2")
for e in ['0', '0.001', '0.01', '0.1', '0.5']:
    K = K2ie(e); Kc = K2ie_closed(e)
    assert abs(K - Kc) < mp.mpf('1e-25'), (e, K, Kc)
    print("%-9s %-35s %-32s %s" % (e, mp.nstr(K, 25), mp.nstr(K**2, 25), mp.nstr(2 - 2*K**2, 12)))

# the two configurations, in Lamzouri's own invariants
print()
print("configuration invariants (Prop 2.1 right-hand side 2*sum_z 1 - sum_{z,s} K(z-s)^2):")
print("  on-line double at real x, m=2 :  sum_z 1 = 2, sum K^2 = m^2 K(0)^2 = 4,  RHS = 0")
for e in ['0.01', '0.1', '0.5']:
    K = K2ie(e)
    print("  off-line pair x +- i*%-5s     :  sum_z 1 = 2, sum K^2 = %s,  RHS = %s"
          % (e, mp.nstr(2 + 2*K**2, 20), mp.nstr(2 - 2*K**2, 12)))

# Gram data of the pair block (independent check that the two configs coincide as eps->0)
print()
print("pair block: a=||g||^2=(1+K)/2, ||h||^2=(K-1)/2, alpha_1=1+K, alpha_2=1-K")
for e in ['0.01', '0.1', '0.5']:
    K = K2ie(e); a = (1 + K) / 2
    g2 = mp.quad(lambda u: A*mp.cos(s2*u)*mp.cosh(2*mp.pi*mp.mpf(e)*u)**2, [-mp.mpf(1)/2, mp.mpf(1)/2])
    h2 = mp.quad(lambda u: A*mp.cos(s2*u)*mp.sinh(2*mp.pi*mp.mpf(e)*u)**2, [-mp.mpf(1)/2, mp.mpf(1)/2])
    print("  eps=%-5s ||g||^2 num %s  closed %s ; ||g||^2-||h||^2 = %s ; a1^2+a2^2 = %s"
          % (e, mp.nstr(g2, 20), mp.nstr(a, 20), mp.nstr(g2 - h2, 20),
             mp.nstr((1+K)**2 + (1-K)**2, 20)))
