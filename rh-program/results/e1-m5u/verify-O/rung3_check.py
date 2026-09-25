# Reader's independent check of the rung-3 cyclic cubic pair (E1 FORMULATION §3.3).
# (1) Splitting of the two LMFDB defining polynomials mod p by counting roots in F_p (a cubic
#     Galois field: 3 roots = split, 0 roots = inert, ramified primes excluded).
# (2) Character-side prediction: p splits in K1 (chi_q1*chi_q2) iff a+b = 0 mod 3, in K2 (chi_q1*conj chi_q2)
#     iff a-b = 0 mod 3, a,b the discrete logs of p mod q1,q2 reduced mod 3 (generators fixed; the labels K1/K2
#     depend on the generator choice only through swapping).
# (3) Independent search over primes q1<q2<=400, q = 1 mod 3, of p0 = first prime that is a non-cube mod both.
# (4) Discriminant and polynomial discriminant check; stratum heights.
import math, time
t0=time.time()
def primes(n):
    s=bytearray([1])*(n+1); s[0]=s[1]=0
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(n+1) if s[i]]
P=primes(2000)
polys={'.1':(1,-1,-28014,703471),'.2':(1,-1,-28014,1711987)}
def nroots(c,p):
    a,b,cc,d=c
    return sum(1 for x in range(p) if (a*x**3+b*x**2+cc*x+d)%p==0)
def disc(c):
    a,b,cc,d=c
    return b*b*cc*cc-4*a*cc**3-4*b**3*d-27*a*a*d*d+18*a*b*cc*d
for k,c in polys.items():
    D=disc(c); print(f"LMFDB {k}: poly disc = {D} = 7063225849 * {D/7063225849:.6g}")
print("p   : roots(.1) roots(.2)  -> types")
first_diff=None
for p in P:
    if p>60: break
    if p in (229,367): continue
    r1=nroots(polys['.1'],p); r2=nroots(polys['.2'],p)
    t1='split' if r1==3 else ('inert' if r1==0 else f'?{r1}')
    t2='split' if r2==3 else ('inert' if r2==0 else f'?{r2}')
    print(f"{p:3d} : {r1} {r2}  {t1:6s} {t2:6s} {'DIFFER' if t1!=t2 else ''}")
    if t1!=t2 and first_diff is None: first_diff=p
print("first prime with different splitting (poly check):", first_diff)
def dlog3(p,q):
    # index of p mod q, reduced mod 3, w.r.t. the least primitive root g of q
    for g in range(2,q):
        if all(pow(g,(q-1)//r,q)!=1 for r in set(f for f in range(2,q) if (q-1)%f==0 and all(f%j for j in range(2,int(f**.5)+1)))):
            break
    x=1
    for e in range(q-1):
        if x==p%q: return e%3
        x=x*g%q
q1,q2=229,367
print("character side (a,b) and predicted types for p<60:")
for p in P:
    if p>60: break
    a,b=dlog3(p,q1),dlog3(p,q2)
    same = (a==0 or b==0)
    print(f"  p={p:2d} a={a} b={b} same_type={same}")
# (3) search
qs=[q for q in P if q<=400 and q%3==1]
best=[]
for i,x in enumerate(qs):
    for y in qs[i+1:]:
        for p in P:
            if p in (x,y): continue
            if pow(p,(x-1)//3,x)!=1 and pow(p,(y-1)//3,y)!=1:
                best.append((p,x,y)); break
best.sort(reverse=True)
print("pairs searched:",len(best)," top p0:",best[:6])
d=7063225849
for p0 in (19,):
    print("T(alpha>=1/2) =",2*math.pi*(p0**2/d)**(1/3),"  T(alpha>=1) =",2*math.pi*(p0/d)**(1/3))
print("elapsed %.2fs"%(time.time()-t0))
