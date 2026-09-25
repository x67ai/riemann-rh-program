# Reader's independent check of E1 §3.1's rung-1 pair: point counts of y^2 = f(x) over F_7 and F_49
# (F_49 = F_7[i], i^2 = -1, since -1 is a non-square mod 7), one point at infinity (deg f = 5),
# (first run counted y over F_49 for N_1 -- a reader bug, fixed: y over F_7 for N_1)
# then P(t) = 1 + c1 t + c2 t^2 + 7 c1 t^3 + 49 t^4 with S_m = q^m + 1 - N_m, c1 = -S1, c2 = (S1^2 - S2)/2.
import time; t0=time.time()
q=7
def f_eval(coeffs,x,mul,add):
    r=(0,0)
    for c in coeffs:  # Horner, coeffs from leading
        r=add(mul(r,x),(c%q,0))
    return r
def mul(a,b): return ((a[0]*b[0]-a[1]*b[1])%q,(a[0]*b[1]+a[1]*b[0])%q)
def add(a,b): return ((a[0]+b[0])%q,(a[1]+b[1])%q)
F49=[(a,b) for a in range(q) for b in range(q)]
sq49={}
for y in F49: sq49[mul(y,y)]=sq49.get(mul(y,y),0)+1
sq7={}
for y in range(q): sq7[((y*y)%q,0)]=sq7.get(((y*y)%q,0),0)+1
def count(coeffs,field,sq):
    return 1+sum(sq.get(f_eval(coeffs,x,mul,add),0) for x in field)
F7=[(a,0) for a in range(q)]
curves={'y^2=x^5+3x^3+6x^2+3':[1,0,3,6,0,3],'y^2=x^5+x^3+5x^2+5x+5':[1,0,1,5,5,5]}
def sqfree_check(c):
    # squarefree over F_7: gcd(f, f') = 1, via polynomial gcd mod 7
    def trim(a):
        while a and a[0]%q==0: a=a[1:]
        return a
    def pmod(a,b):
        a=trim([x%q for x in a]); b=trim([x%q for x in b])
        inv=pow(b[0],q-2,q)
        while len(a)>=len(b) and a:
            fct=a[0]*inv%q
            for i in range(len(b)): a[i]=(a[i]-fct*b[i])%q
            a=trim(a)
        return a
    d=len(c)-1; fp=[(c[i]*(d-i))%q for i in range(d)]
    a,b=c[:],fp
    while b: a,b=b,pmod(a,b)
    return len(trim(a))==1
for name,c in curves.items():
    N1=count(c,F7,sq7); N2=count(c,F49,sq49)
    S1=q+1-N1; S2=q*q+1-N2
    c1=-S1; c2=(S1*S1-S2)//2
    print(f"{name}: squarefree={sqfree_check(c)} N1={N1} N2={N2}  P(t)=1{c1:+d}t{c2:+d}t^2{7*c1:+d}t^3+49t^4")
print("elapsed %.2fs"%(time.time()-t0))
