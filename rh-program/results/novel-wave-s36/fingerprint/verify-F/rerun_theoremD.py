# Orchestrator's independent re-run of N3's decisive computation (Session 37, read-F).  mpmath only (the NOTE used Arb series).
# (1) s_m(xi) = sum_{gamma>0} gamma^{-2m} from Taylor data of log xi at s = 1/2;  (2) the S-fraction alpha_1..alpha_8 by the
# quotient-difference recursion on c_m = s_{m+1};  (3) Theorem D: s_m(xi*g_p) - s_m(xi) = lattice sum over the Euler factor's zeros,
# closed form -l^2/(4 sinh^2(l/4)) at m = 1;  (4) alpha_1(xi * g_p) < 0 for p = 2, 3, 7.
from mpmath import mp, mpf, mpc, zeta, gamma, pi, log, sinh, taylor, nsum, inf, exp
mp.dps = 60
def xi(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
# log xi(1/2 + x) = sum c'_k x^k ; even function of x ; s_m = (-1)^{m+1} m c'_{2m}
M = 10
tc = taylor(lambda x: log(xi(mpf(1)/2 + x)), 0, 2*M+1)
s = [None] + [(-1)**(m+1)*m*tc[2*m] for m in range(1, M+1)]
print("s_1 =", mp.nstr(s[1], 22), "  NOTE: 0.023104993115418970789")
print("s_2 =", mp.nstr(s[2], 20), "  NOTE: 3.7172599285269686165e-5")
print("s_3 =", mp.nstr(s[3], 19), "  NOTE: 1.441739314009732797e-7")
def sfrac(c, n):
    # F = c0/(1 - a1 w/(1 - a2 w/...)) from power series sum c_m w^m, by repeated inversion (Viskovatov)
    from mpmath import mpf
    ser = [x/c[0] for x in c]          # normalized series 1 + ...
    out = []
    for _ in range(n):
        # ser = 1/(1 - a w G)  =>  1 - 1/ser = a w G, G(0) = 1
        L = len(ser)
        inv = [mpf(1)] + [mpf(0)]*(L-1)
        for k in range(1, L):
            inv[k] = -sum(ser[j]*inv[k-j] for j in range(1, k+1))
        d = [-x for x in inv[1:]]      # (1 - 1/ser)/w
        a = d[0]; out.append(a)
        ser = [x/a for x in d]
    return out
c = [s[m+1] for m in range(0, M)]
al = sfrac(c, 8)
note = ["0.0016088556745971410", "0.0022696444618758230", "0.0012309447733972452", "0.0010732871255926878",
        "0.00072505601164270264", "0.00067059821555096551", "0.00054658061766806790", "0.00056250296730744522"]
for i, (a, b) in enumerate(zip(al, note), 1):
    print("alpha_%d = %s   NOTE %s   diff %s" % (i, mp.nstr(a, 20), b, mp.nstr(a - mpf(b), 3)))
# (3)-(4) Theorem D for the symmetrized Euler factor at p
for p in (2, 3, 7):
    l = log(p)
    def wk(k): return ((mpc(0, l/2) + 2*pi*k)/l)**2       # w_k = t_k^2, t_k = i/2 + 2 pi k / l
    lat = [None] + [(nsum(lambda k: wk(k)**(-m), [-inf, inf])).real for m in range(1, 5)]
    closed = -l**2/(4*sinh(l/4)**2)
    # direct: xi*g_p Taylor data
    g = lambda ss: -(p+1)/mp.sqrt(p) + p**(ss - mpf(1)/2) + p**(mpf(1)/2 - ss)
    tcg = taylor(lambda x: log(-g(mpf(1)/2 + x)), 0, 9)      # -g > 0 at s = 1/2 for the Euler case
    sg = [None] + [(-1)**(m+1)*m*tcg[2*m] for m in range(1, 5)]
    print("p=%d: lattice sum m=1: %s  closed form: %s  Taylor of log g: %s" % (p, mp.nstr(lat[1], 15), mp.nstr(closed, 15), mp.nstr(sg[1], 15)))
    print("      m=2: lattice %s  Taylor %s ;  s_1(xi g_p) = %s ; alpha_1(xi g_p) = s_2/s_1 = %s"
          % (mp.nstr(lat[2], 12), mp.nstr(sg[2], 12), mp.nstr(s[1] + sg[1], 10), mp.nstr((s[2] + sg[2])/(s[1] + sg[1]), 10)))
print("(sqrt(p)-1)^2 > 0: the symmetrized Euler factor has a = -(p+1), |a| - 2 sqrt(p) = (sqrt p - 1)^2")
