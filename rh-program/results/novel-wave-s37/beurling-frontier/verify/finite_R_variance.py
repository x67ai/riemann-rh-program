# Exact check of Prop 5.1: for a finite set R of primes, Q = prod R, E(x) = #{n<=x : (n,Q)=1} - rho*x (rho = phi(Q)/Q)
# is Q-periodic with mean 0 and (1/Q) int_0^Q E(x)^2 dx = rho * 2^|R| / 12.
from fractions import Fraction as Fr
from math import gcd
def check(R):
    Q=1
    for p in R: Q*=p
    rho=Fr(1)
    for p in R: rho*=Fr(p-1,p)
    # E is linear on each [n, n+1): E(x) = N(n) - rho*x ; integrate exactly
    N=0; I=Fr(0); M1=Fr(0)
    for n in range(0,Q):
        if n>=1 and gcd(n,Q)==1: N+=1
        # int_n^{n+1} (N - rho x)^2 dx and (N - rho x) dx
        a=Fr(N)-rho*n; b=Fr(N)-rho*(n+1)
        I+=(a*a+a*b+b*b)/3; M1+=(a+b)/2
    return Q, M1/Q, I/Q, rho*2**len(R)/12
for R in ([2],[3],[2,3],[2,3,5],[3,7],[2,3,5,7],[5,11,13],[2,3,5,7,11]):
    Q,mean,ms,pred=check(R)
    print(R,"Q=",Q,"mean=",mean,"meansq=",ms,"pred=",pred,"equal" if ms==pred else "DIFF")
