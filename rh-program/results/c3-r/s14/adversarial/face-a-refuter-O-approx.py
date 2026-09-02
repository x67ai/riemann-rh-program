from sympy import primerange
from fractions import Fraction
import math
def M_k(p,k):
    M=1
    for l in primerange(2,k+1):
        if l!=p: M*=l**k
    return M
def find(p,cres,t,k,eps):
    M=M_k(p,k)
    if M==1: return None
    c=cres(M)
    j=1
    while Fraction(M,p**j) >= eps or p**j <= M/t: j+=1
    lo=math.ceil(t*p**j)
    m=lo+((c-lo)%M)
    r=Fraction(m,p**j)
    return M,j,m,r
print("SIMULTANEOUS APPROXIMATION  m = c mod M  AND  m*p^-j -> t   (eps = 1e-12)")
for (p,cname,cres,t) in [(2,"-1",lambda M:(-1)%M,Fraction(1,2)),
                         (2,"7", lambda M:7%M,     Fraction(3,1)),
                         (3,"-1",lambda M:(-1)%M,  Fraction(1,5)),
                         (5,"2", lambda M:2%M,     Fraction(7,11))]:
    print(f"\n p={p}, c={cname}, t={t}")
    for k in [3,4,5,6]:
        out=find(p,cres,t,k,Fraction(1,10**12))
        if out is None: continue
        M,j,m,r=out
        print(f"   k={k}: M={M}  j={j}  m={m}")
        print(f"        m mod M = {m%M}  == c mod M = {cres(M)}  -> {m%M==cres(M)}")
        print(f"        m/{p}^{j} - t = {float(r-t):.3e}   (m is a POSITIVE integer: {m>0})")
