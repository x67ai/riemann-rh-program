# Orchestrator's own re-run (Session 37, read-F): Haglund's Xi_N evaluated LITERALLY from his (10), (13), (14)
# (arXiv:0910.5228 p. 2-3) in Arb ball arithmetic via python-flint -- independent of the N2 agent's evaluator
# (which used Xi - tail).  Every printed value is a rigorous enclosure (ball).
import sys, time
from flint import acb, arb, ctx

def G(z, a, b):
    # G(z;a,b) = Gamma(b+iz,a)/a^(b+iz) + Gamma(b-iz,a)/a^(b-iz)      (Haglund (10))
    I = acb(0, 1)
    s1 = b + I*z
    s2 = b - I*z
    a_c = acb(a)
    # python-flint: z.gamma_upper(s) = Gamma(s, z)  (self is the lower limit z, the order s is the parameter)
    return a_c.gamma_upper(s1) * (a_c ** (-s1)) + a_c.gamma_upper(s2) * (a_c ** (-s2))

def Phi(n, z):
    # Phi_n(z) = 2 pi^2 n^4 G(z/2; n^2 pi, 9/4) - 3 pi n^2 G(z/2; n^2 pi, 5/4)   (Haglund (14))
    pi = arb.pi()
    a = pi * n * n
    return 2*pi*pi*n**4 * G(z/2, a, arb(9)/4) - 3*pi*n*n * G(z/2, a, arb(5)/4)

def XiN(N, z):
    tot = acb(0)
    for n in range(1, N+1):
        tot += Phi(n, z)
    return tot

if __name__ == "__main__":
    bits = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    ctx.prec = bits
    # validation: Haglund's table p. 4, N = 1 largest real zero 14.0454395788 (sign change)
    for t in ["14.04543957", "14.04543959"]:
        v = XiN(1, acb(arb(t)))
        print("N=1 t=", t, " Xi_1 =", v.real.str(15), " imag ball:", v.imag.str(5))
    t0 = time.time()
    v = XiN(2, acb(arb("39.5324810797"))); w = XiN(2, acb(arb("39.5324810799")))
    print("N=2 sign change around 39.5324810798:", v.real.str(10), w.real.str(10), " (%.1fs)" % (time.time()-t0))
