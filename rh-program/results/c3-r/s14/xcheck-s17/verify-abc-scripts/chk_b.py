import numpy as np
E=np.e
def theta(t):
    t=np.asarray(t,dtype=float); out=np.zeros_like(t)
    msk=np.abs(t)<1-1e-15
    out[msk]=E*np.exp(-1.0/(1.0-t[msk]**2))
    return out
r=1.0; R=2.5   # R>2r
print("=== (b): b(iR)=c_i=(1+iR)^{m+1}; check ||b||_{K,0,0,m} blowup and (3.5) limsup ===")
for m in [-3.0,-1.0,0.0,2.5]:
    print(f" m={m}")
    for i in [1,5,20,100,1000]:
        ci=(1+i*R)**(m+1)
        s31 = ci*(1+i*R)**(-m)              # (3.1) integrand at xi=i*R e1  (weight in denominator)
        s35 = ci/((i*R)**m)                 # (3.5) integrand at xi=i*R e1
        print(f"   i={i:5d}  c_i={ci:.4e}   (3.1)-quotient={s31:.4e}   (3.5)-quotient={s35:.4e}")
print()
print("=== disjointness: supp theta(.-iR e1) = ball(iR,1). gap = R-2r =",R-2*r,">0 -> disjoint ===")
print()
print("=== non-injectivity of phi: u_j(xi)=rho(|xi|/j)(1+|xi|^2)^{m/2}, rho=0 on t<=1, 1 on t>=2 ===")
def rho(t):
    t=np.asarray(t,dtype=float); out=np.zeros_like(t)
    a=(t>1)&(t<2)
    # smooth transition using the standard bump-based partition
    s=(t[a]-1.0)
    f=np.exp(-1.0/np.clip(s,1e-300,None)); g=np.exp(-1.0/np.clip(1.0-s,1e-300,None))
    out[a]=f/(f+g)
    out[t>=2]=1.0
    return out
for m in [-2.0,0.0,1.5]:
    for j in [3,10,50]:
        xi=np.linspace(1e-6,400*max(1,j),2000001)
        u=rho(xi/j)*(1+xi**2)**(m/2)
        q=u/xi**m
        # limsup as |xi|->inf approximated by the tail
        print(f"  m={m} j={j}:  ||u_j||'_{{K,0,0,m}} (tail value) = {q[-1]:.8f}   (should ->1)")
    # difference u_j - u_i vanishes for |xi|>=2max(i,j)
    xi=np.linspace(1e-6,4000,2000001)
    d=rho(xi/10)*(1+xi**2)**(m/2)-rho(xi/50)*(1+xi**2)**(m/2)
    tail=np.max(np.abs(d[xi>120])/xi[xi>120]**m)
    print(f"  m={m}: sup over |xi|>120 of |u_10-u_50|/|xi|^m = {tail:.3e}  (0 => (3.5) seminorm of the difference is 0)")
