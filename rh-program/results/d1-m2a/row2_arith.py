from fractions import Fraction as F
import math
from mpmath import mp, mpf, sqrt, pi, log, exp, floor, iv
mp.dps = 60
X = 5*10**12 + 194858
t0 = F(186,1000); y0 = F(16733,100000)
lam = t0 + y0*y0/2
print("t0 + y0^2/2 =", lam, "=", float(lam), " <= 1/5 ?", lam <= F(1,5), " slack 1/5 - lam =", F(1,5)-lam)
print("X/2 =", F(X,2), "=", float(F(X,2)))
TPT = 3000175332800
print("T_PT - X/2 =", TPT - F(X,2), "=", float(TPT - F(X,2)))
sig0 = (1+y0)/2
print("(1+y0)/2 =", sig0, "=", float(sig0), "; 58367/100000 <= sig0 ?", F(58367,100000) <= sig0, " diff", sig0 - F(58367,100000))
print("2.51e12 vs X/2:", F(251*10**10) - F(X,2))
# 1 - 2 t0, 1 - y0^2
print("1-2t0 =", 1-2*t0, " 1-y0^2 =", 1-y0*y0, " y0^2+2t0 =", y0*y0+2*t0)
# rational brackets by integer squares
def bracket_sqrt(q, den):
    # find integers a with a^2/den^2 < q <= (a+1)^2/den^2
    a = int(math.isqrt(q.numerator*den*den//q.denominator))
    while F(a*a, den*den) >= q: a -= 1
    while F((a+1)*(a+1), den*den) < q: a += 1
    assert F(a*a,den*den) < q <= F((a+1)*(a+1),den*den)
    return F(a,den), F(a+1,den)
for name,q in [("sqrt(1-y0^2)", 1-y0*y0), ("sqrt(1-2t0)", 1-2*t0), ("sqrt(y0^2+2t0)", y0*y0+2*t0)]:
    lo,hi = bracket_sqrt(q, 10**7)
    print(name, "in (", lo, ",", hi, "]  =", float(lo), float(hi))
# N0 = floor(sqrt(x/4pi + t/16)) across box
for t in [F(0), t0]:
    for x in [X, X+1]:
        v = iv.mpf(x)/(4*iv.pi) + iv.mpf(t.numerator)/(16*t.denominator)
        s = iv.sqrt(v)
        print("x=",x,"t=",t,"sqrt(x/4pi+t/16) in", s)
# x_N boundaries for N0
N0 = 630783
for t in [F(0), t0]:
    tt = iv.mpf(t.numerator)/t.denominator
    xN = 4*iv.pi*(iv.mpf(N0)**2) - iv.pi*tt/4
    xN1 = 4*iv.pi*(iv.mpf(N0+1)**2) - iv.pi*tt/4
    print("t=",t," x_N0 =", xN, " x_N0+1 =", xN1, " X in [x_N0, x_N0+1)?", (xN.b < X) and (X+1 < xN1.a))
