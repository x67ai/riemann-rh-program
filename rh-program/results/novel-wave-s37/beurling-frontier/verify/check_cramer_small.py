# Brute-force cross-check of thin_aux.c (cramer mode): N(2000) = # multisets of Cramer primes with product <= 2000 (same hash).
import math, subprocess
from functools import lru_cache
M=(1<<64)-1
def sm(x):
    x=(x+0x9E3779B97F4A7C15)&M; x=((x^(x>>30))*0xBF58476D1CE4E5B9)&M; x=((x^(x>>27))*0x94D049BB133111EB)&M; return x^(x>>31)
def unif(p,seed,salt):
    h=sm(p ^ sm(((seed*0xD1B54A32D192ED03)&M) ^ salt)); return (h>>11)*(1.0/9007199254740992.0)
X=2000; P=[n for n in range(2,X+1) if n==2 or unif(n,1,0xC7A3E5)<1/math.log(n)]
@lru_cache(None)
def cnt(n,i):
    if n==1: return 1
    s=0
    for j in range(i,len(P)):
        q=P[j]
        if q>n: break
        if n%q==0: s+=cnt(n//q,j)
    return s
print("brute-force N(2000) =", sum(cnt(n,0) for n in range(1,X+1)))
out=subprocess.run(["./thin_aux","cramer","2000","2000","1"],capture_output=True,text=True).stdout.splitlines()
rho=float(out[0].split("rho=")[1]); last=out[-1].split(",")
print("thin_aux N(2000) = %.6f (from last-bin maxE+ + rho*2000)" % (float(last[3])+rho*2000))
