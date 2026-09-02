# INDICATIVE (heuristic float, mpmath 50 dps) error budget at Table-1 row 2, following Polymath15
# Prop 8.1's chain (82)-(87) and the 10.50 weld of Prop 6.6(vi); NOT a certificate.
from mpmath import mp, mpf, sqrt, pi, log, exp, floor, nsum, inf
mp.dps = 50
X = mpf(5*10**12 + 194858); t0 = mpf('0.186'); y0 = mpf('0.16733'); N0 = 630783
def F_Nt(sigma, t, N):
    # sum_{n<=N} b_n^t / n^sigma, b_n^t = exp(t/4 log^2 n)
    return nsum(lambda n: exp(t/4*log(n)**2)/n**sigma, [1, N])
# (84)-(85): delta1 at x = X (monotone decreasing in x)
def delta1(x,t): return (t**2/16*log(x/(4*pi))**2 + mpf('0.626'))/(x-mpf('6.66'))
d1 = delta1(X, t0)
print("delta1(X,t0) =", d1)
# Re s* lower bound (21) at worst case x=X, y in [y0,1], t in [0,t0]: (1+y)/2 + t/4 log(x/4pi) - t/(2x^2)(...)_+
def res_lb(x,y,t): return (1+y)/2 + t/4*log(x/(4*pi)) - t/(2*x**2)*max(1-3*y+4*y*(1+y)/x**2, 0)
print("Re s* >= at (X,y0,0):", res_lb(X,y0,0), " at (X,y0,t0):", res_lb(X,y0,t0))
# e_A+e_B <= 1.023*delta1*F_{N,t}(Re s*) roughly (paper's (86)); worst t: need F_{N,t}(sigma) with sigma>= (1+y0)/2 + t/4 log(x/4pi)
for t in [mpf(0), t0]:
    sig = res_lb(X, y0, t)
    val = mpf('1.023')*delta1(X,t if t>0 else t0)*F_Nt(sig, t, N0)   # delta1 uses t<=t0 bound
    print("t=",t," sigma_lb=",sig," F_N,t(sigma)=",F_Nt(sig,t,N0)," eA+eB <~", val)
# e_C0 with the 10.50 weld at (x=X, y=y0, t=0) (worst y is y0; worst t is 0 since -t/16 log^2 term helps)
def eC0(x,y,t,N):
    return (x/(4*pi))**(-(1+y)/4)*exp(-t/16*log(x/(4*pi))**2 + mpf('1.24')*(3**y+3**(-y))/(N-mpf('0.125')) + (3*abs(log(x/(4*pi))+1j*pi/2)+mpf('10.50'))/(x-12))
print("eC0(X,y0,0,N0) =", eC0(X,y0,0,N0), " eC0(X,1,0,N0) =", eC0(X,mpf(1),0,N0), " eC0(X,y0,t0,N0) =", eC0(X,y0,t0,N0))
# for comparison the paper's row-2 lower bound 0.0376 and Gomila-type allowance 0.00125
print("ratio 0.0376 / eC0(X,y0,0,N0) =", mpf('0.0376')/eC0(X,y0,0,N0))
# asymptotic lane: eC0 at t=t0 as x grows: x_N for N = N0, 2N0, 10 N0
for N in [N0, 2*N0, 10*N0, 100*N0]:
    x = 4*pi*N**2 - pi*t0/4
    print("N=",N," x~",x," eC0(x,y0,t0,N)=",eC0(x,y0,t0,N), " |gamma|<=", exp(mpf('0.02')*y0)*(x/(4*pi))**(-y0/2))
