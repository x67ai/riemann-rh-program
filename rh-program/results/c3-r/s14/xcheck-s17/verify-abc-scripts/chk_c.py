from mpmath import mp, mpf, exp, log
mp.dps=60
def eps(k, JMAX=5000):
    # eps_k = 1/2 inf_{j>=1 integer} e^j (1+j)^{-k}
    best=None
    for j in range(1,JMAX+1):
        v=exp(mpf(j))/ (mpf(1+j)**k)
        if best is None or v<best: best=v; arg=j
    return best/2, arg
bad=0; tot=0
for k in range(1,31):
    e_k,arg=eps(k)
    assert e_k>0
    for j in range(1,600):
        lhs=e_k*(mpf(1+j)**k); rhs=exp(mpf(j))/2
        tot+=1
        if lhs>rhs*(1+mpf('1e-40')):
            bad+=1
            print("VIOLATION k=",k,"j=",j,"lhs/rhs=",lhs/rhs)
    if k in (1,2,5,10,20,30):
        print(f"k={k:2d}  eps_k={mp.nstr(e_k,10):>18}  minimizing j={arg}  (real-arg optimum k-1={k-1})")
print(f"checked {tot} (k,j) pairs, violations = {bad}")
# also check the theoretical identity eps_k (1+j)^k <= 1/2 e^j with equality exactly at the minimizing j
for k in (1,5,10,20):
    e_k,arg=eps(k)
    print(f"k={k}: at j=arg={arg}: eps_k(1+j)^k = {mp.nstr(e_k*mpf(1+arg)**k,15)}, (1/2)e^j = {mp.nstr(exp(mpf(arg))/2,15)}")
