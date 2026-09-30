# Brute-force cross-check of thin.c (bern mode) on a small instance: same hash, same R, recount N_P and rho.
import math
M=(1<<64)-1
def sm(x):
    x=(x+0x9E3779B97F4A7C15)&M
    x=((x^(x>>30))*0xBF58476D1CE4E5B9)&M
    x=((x^(x>>27))*0x94D049BB133111EB)&M
    return x^(x>>31)
def unif(p,seed,salt):
    h=sm(p ^ sm(((seed*0xD1B54A32D192ED03)&M) ^ salt))
    return (h>>11)*(1.0/9007199254740992.0)
alpha,X,Y,seed=0.6,10**5,10**6,1
salt=round(alpha*1e6)
sieve=bytearray([1])*(Y+1); sieve[0]=sieve[1]=0
for i in range(2,int(Y**0.5)+1):
    if sieve[i]: sieve[i*i::i]=bytearray(len(range(i*i,Y+1,i)))
R=[p for p in range(2,Y+1) if sieve[p] and unif(p,seed,salt)<math.exp((alpha-1)*math.log(p))]
logrho=sum(math.log1p(-1/p) for p in R)
# E1 via mpmath-free series/CF is in C; here use scipy-free numeric integral of u^(a-2)/log u from Y to inf
from math import exp,log
def E1(z):
    # integrate e^{-t}/t from z to inf by substitution; simple adaptive Simpson on [z, z+60]
    f=lambda t: math.exp(-t)/t
    n=200000; a=z; b=z+60; h=(b-a)/n
    s=f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n))
    return s*h/3
rho=math.exp(logrho-E1((1-alpha)*math.log(Y)))
free=bytearray([1])*(X+1)
for p in R:
    if p>X: break
    free[p::p]=bytearray(len(range(p,X+1,p)))
N=0; worst=0
for n in range(1,X+1):
    N+=free[n]
    worst=max(worst,abs(N-rho*n))
print("nR(Y)=",len(R),"rho=%.12f"%rho,"N(X)=",N,"E(X)=%.6f"%(N-rho*X),"max|E+| up to X=%.6f"%worst)
