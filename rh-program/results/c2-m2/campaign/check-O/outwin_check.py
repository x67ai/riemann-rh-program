"""CHECKER close 4: independent verification of u_true(L) and of the clause-5 looseness, with the checker's own
complex-argument quadrature (oscillatory mp.quad with breakpoints at the nodes of cos(x v); NOT the Poisson-trapezoid rule)."""
from mpmath import mp
import math, json
def bhat_c(x, y, dps):
    """Bhat(x - i y) = int B(v) e^{i x v} e^{y v} dv  (B real, even, supported in [-1/2,1/2])."""
    with mp.workdps(dps):
        X=mp.mpf(x); Y=mp.mpf(y); half=mp.mpf(1)/2
        Zn=mp.quad(lambda v: mp.exp(-1/(1-4*v*v)), [-half,-mp.mpf(1)/4,0,mp.mpf(1)/4,half])
        f=lambda v: mp.exp(-1/(1-4*v*v))*mp.exp(1j*X*v)*mp.exp(Y*v)
        n=int(mp.floor(X*half/mp.pi))
        pts=[-half]+[mp.pi*j/X for j in range(-n,n+1)]+[half]
        pts=sorted(set([p for p in pts if -half<=p<=half]))
        tot=mp.mpc(0)
        for i in range(len(pts)-1): tot+=mp.quad(f,[pts[i],pts[i+1]])
        return tot/Zn
def pair(L,u,dps):
    v=bhat_c(L*u, L/2.0, dps)
    with mp.workdps(dps):
        return 2*mp.re((mp.mpc(u,-0.5))**2*v**2), v
BUILD={50:54.50484160648561, 120:130.36133764241708, 20:20.936131769113473}
print("u_true check: the pair contamination at the builder's u_true should equal e^{-L}")
for L,u in [(20,BUILD[20]),(50,BUILD[50]),(120,BUILD[120])]:
    dps = 40 + int(L/2/2.303) + 20
    w,v = pair(L,u,dps)
    tgt = math.exp(-L)
    print("  L=%-5g u_true(builder)=%.8f  |pair|=%.6e   e^{-L}=%.6e   ratio=%.5f   (|Bhat(Lu-iL/2)|=%.4e, dps=%d)"
          %(L,u,float(abs(w)),tgt,float(abs(w))/tgt,float(abs(v)),dps), flush=True)
print()
print("bound/exact looseness at the planted distances (CAMPAIGN close 4)")
CB=2/math.sqrt(72*math.e); CBIG=math.e**2/0.2219969080840397
def logG1(e):
    s=math.sqrt(max(e,0.0)); return math.log(CBIG)+math.log1p(CB/2*s)-CB*s
for (L,u,quoted) in [(20,5,10.6),(20,50,23.4),(50,5,14.3),(50,50,33.3),(120,5,19.8),(120,50,47.8)]:
    dps=40+int(L/2/2.303)+20
    w,v=pair(L,u,dps)
    lw=float(mp.log10(abs(w)))
    lb=(math.log(2*(u+0.5)**2)+L/2+2*logG1(L*u))/math.log(10)
    print("  L=%-5g u=%-5g log10(bound/|exact|) = %.2f   (CAMPAIGN quotes 10^%.1f)"%(L,u,lb-lw,quoted))
print("DONE")
