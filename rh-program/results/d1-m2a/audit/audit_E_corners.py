#!/usr/bin/env python3
"""AUDIT (2026-09-03): the Theorem 1.3 error majorant e_A + e_B + e_{C,0} re-derived from P15 Prop 6.6 (PDF p31) at POINTS
(x, y, t) of the row-2 box, with the exact Dirichlet sums (no majorant), (iv)/(v) with log^2(x/(4 pi n^2)) as printed,
and (vi) as printed, in the SPEC D-2.4 10.50 form, and with the displayed 10.44 of (24).  Independent code (python-flint
arb); no producer code imported.  The producers' E (a sup over the box) must be >= every corner value.
Run record: audit-E-corners.txt."""
import sys
from fractions import Fraction as Fr
from flint import acb, arb, ctx
ctx.prec = 200
N=630783; PI=arb.pi()
def alpha(s): return 1/(2*s) + 1/(s-1) + (s/(2*PI)).log()/2
def logM0(s): return s.log() + (s-1).log() - s/2*PI.log() + ((2*PI).sqrt()/16).log() + (s/2 - acb(1)/2)*(s/2).log() - s/2
def fa(q): return arb(q.numerator)/arb(q.denominator)
LOG=[None]+[arb(n).log() for n in range(1,N+1)]
def majorant(x, y, t):
    xa, ya, ta = fa(x), fa(y), fa(t)
    z = acb(xa, ya); sp=(1-acb(0,1)*z)/2; sm=(1+acb(0,1)*z)/2
    ap, am, amc = alpha(sp), alpha(sm), alpha(sp.conjugate())
    sst = sp + ta/2*ap; res = sst.real
    kappa = ta/2*(am - amc); ak = abs(kappa)
    gam = (ta/4*(am**2-ap**2) + logM0(sm)-logM0(sp)).exp(); ag = abs(gam)
    q = xa/(4*PI); lq = q.log()
    eA = arb(0); eB = arb(0)
    for n in range(1, N+1):
        L = LOG[n]; bt = (ta/4*L*L).exp()
        expo = ((ta*ta/16)*(lq - 2*L)**2 + arb("0.626"))/(xa - arb("6.66"))   # log(x/(4 pi n^2)) = lq - 2 log n
        term = bt * (-res*L).exp() * (expo.exp() - 1)
        eB += term
        eA += (ya*L).exp() * term
    eA = ag * N**ak * eA
    mod = abs(acb(lq, PI/2))
    br = arb("1.24")*(arb(3)**ya + arb(3)**(-ya))/(arb(N)-arb("0.125"))
    eC0_printed = q**(-(1+ya)/4) * (-(ta/16)*lq*lq + (3*mod + arb("3.58"))/(xa - arb("8.52"))).exp() * (1 + br + arb("6.92")/(xa-12))
    eC0_1050 = q**(-(1+ya)/4) * (-(ta/16)*lq*lq + (3*mod + arb("10.50"))/(xa - 12)).exp() * (1 + br)
    eC0_1044 = q**(-(1+ya)/4) * (-(ta/16)*lq*lq + (3*mod + arb("10.44"))/(xa - 12)).exp() * (1 + br)
    return eA, eB, eC0_printed, eC0_1050, eC0_1044, ag, ak, res
if __name__ == "__main__":
    X=5000000194858; y0=Fr(16733,100000); t0=Fr(93,500)
    corners = [(Fr(X), y0, Fr(0)), (Fr(X+1), y0, Fr(0)), (Fr(X), Fr(1), Fr(0)), (Fr(X), y0, t0), (Fr(X), y0, Fr(637,25000)), (Fr(X), y0, Fr(3719,20000))]
    for (x,y,t) in corners:
        eA,eB,eCp,eC1050,eC1044,ag,ak,res = majorant(x,y,t)
        tot = eA+eB+eC1050
        print(f"x={x} y={float(y):.5f} t={float(t):.5f}: e_A={eA.str(5)} e_B={eB.str(5)} e_C0(printed vi)={eCp.str(8)} e_C0(10.50)={eC1050.str(8)} e_C0(10.44 displayed)={eC1044.str(8)} |gamma|={ag.str(6)} |kappa|={ak.str(4)} Re s*={res.str(8)}  TOTAL(10.50 form)={tot.str(10)}")
