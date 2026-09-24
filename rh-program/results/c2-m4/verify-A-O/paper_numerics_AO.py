#!/usr/bin/env python3
"""CHECK-O-A §10 numerics (checker's own, mpmath 40 digits): Z, ||B'||_1 = 2B(0), b1sym, the rstar_of_21L chain margin
and the exact (R*) margin at (t, L, delta) = (1050, 50, 1/2), the L* recomputation, absorb_b's closing constants, and
the clause-7 double at (t, L) = (30, 40)."""
from mpmath import mp, mpf, exp, log, sqrt, quad, cos, e, inf
mp.dps = 40
Braw = lambda v: exp(-1/(1-4*v*v)) if abs(v) < mpf(1)/2 else mpf(0)
Z = quad(Braw, [-0.5, 0, 0.5])
B = lambda v: Braw(v)/Z
dB = lambda v: Braw(v)*(-8*v)/(1-4*v*v)**2/Z if abs(v) < 0.5 else mpf(0)
L1 = quad(lambda v: abs(dB(v)), [-0.5, 0, 0.5])
print("Z                =", mp.nstr(Z, 15))
print("||B'||_1 (quad)  =", mp.nstr(L1, 15), "  2B(0) = 2e^-1/Z =", mp.nstr(2*exp(-1)/Z, 15))
b1 = (2*exp(-1)/Z)**2
print("b1sym            =", mp.nstr(b1, 15), "  (>= 4:", b1 >= 4, ")  Z <= e^-1:", Z <= exp(-1), "  Z >= 1/18:", Z >= mpf(1)/18)
print("log(b1sym/8.70)  =", mp.nstr(log(b1/mpf('8.70')), 10), "   log(10.984/8.70) =", mp.nstr(log(mpf('10.984')/mpf('8.70')), 10),
      "   log(10.99/8.70) =", mp.nstr(log(mpf('10.99')/mpf('8.70')), 10))
def Lstar(delta, t, C1, b):
    return max(25/delta, 4/delta*(log(log(3+t)) + 2*log(1/delta) + log(2*b*C1)))
a = Lstar(mpf('0.1'), mpf(10)**6, 1, mpf('8.70')); c = Lstar(mpf('0.1'), mpf(10)**6, 1, b1)
print("L*(0.1,1e6;C1=1): b1=8.70 ->", mp.nstr(a, 8), "; b1=b1sym ->", mp.nstr(c, 8), "; difference", mp.nstr(c-a, 8),
      "; 4*log(b1sym/8.70)/0.1 =", mp.nstr(4*log(b1/mpf('8.70'))/mpf('0.1'), 8))
cB = 2/sqrt(72*e); CB = e**2/Z
print("cB =", mp.nstr(cB, 12), " (>= 0.1429:", cB >= mpf('0.1429'), ")   CB =", mp.nstr(CB, 12), " (<= 18e^2 =", mp.nstr(18*e**2, 8), ")")
def rstar_margin(t, d, L):
    s = sqrt(2*t*L)
    return (2*cB*s - 2*log(1 + cB/2*s)) - (d*L/2 + log((4*t**2 + d**2)*CB**2/(mpf(27)/20*d**2)))
def chain_margin(t, d, L):
    s = sqrt(2*t*L)
    lhs = d*L/2 + 4*(s/403 + 5) + 2*(log(25) + 2)
    rhs = 2*mpf('0.1429')*s - 2*(log(25) + (1 + mpf('0.1429')/2*s)/25 - 1)
    return rhs - lhs
for (t, d, L) in [(1050, 0.5, 50), (21*50, 25/50., 50), (21*1000, 0.5, 1000), (21*100, 0.25, 100)]:
    t, d, L = mpf(t), mpf(d), mpf(L)
    print(f"(t,delta,L)=({mp.nstr(t,6)},{mp.nstr(d,4)},{mp.nstr(L,6)}): exact (R*) margin {mp.nstr(rstar_margin(t,d,L),6)} nats;"
          f" chain margin (cB -> 0.1429, dL/2 exact) {mp.nstr(chain_margin(t,d,L),6)} nats; s = {mp.nstr(sqrt(2*t*L),6)}")
# the chain in the worst case the linarith step sees: dL/2 <= L/4 <= s/25, cB s >= 0.1429 s
s = sqrt(mpf(2*1050*50))
print("linear chain value 0.230158*s - 34.955 at s=324.04:", mp.nstr((mpf('0.1429')*49/25 - mpf(1)/25 - mpf(4)/403)*s - 22 - mpf(2)/25 - 4*log(25), 8))
# absorb_b closing: need 2 b C1 <= 0.039*4*(2 b C1)^2 / ... i.e. b*C1 >= 2/0.624
print("absorb_b: threshold b*C1 >= 2/0.624 =", mp.nstr(mpf(2)/mpf('0.624'), 8), "; supplied b1sym*C1 >= 4")
# the clause-7 double at (t, L) = (30, 40): 2*(2t)^2*|Bhat(-2tL)|^2 with Bhat(eta) = int B(v) exp(-i eta v) dv (B even: cosine)
t, L = 30, 40; eta = 2*t*L
mp.dps = 60
Zh = quad(Braw, [-0.5, 0, 0.5])
n = 400
pts = [mpf(-1)/2 + mpf(k)/n for k in range(n+1)]
Bhat = quad(lambda v: Braw(v)/Zh*cos(eta*v), pts)
print("clause-7 double at (t,L)=(30,40): 2*(2t)^2*Bhat(2tL)^2 =", mp.nstr(2*(2*t)**2*Bhat**2, 8), "; note body's 16t^2 form =", mp.nstr(16*t**2*Bhat**2, 8))
