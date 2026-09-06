import numpy as np
# l=1 bump: theta(t)=e*exp(-1/(1-t^2)) on |t|<1, 0 else.  theta(0)=1, supp in B(0,1) => r=1.
E=np.e
def theta(t):
    t=np.asarray(t,dtype=float); out=np.zeros_like(t)
    m=np.abs(t)<1-1e-15
    out[m]=E*np.exp(-1.0/(1.0-t[m]**2))
    return out
def dtheta(t,k,h=1e-4):
    # central finite differences of order k (k small); use high-order stencil via numpy.gradient chain on fine grid
    raise SystemExit
# Instead: exact symbolic-ish via finite differences on a very fine grid
def deriv_grid(f,x,k):
    y=f(x)
    for _ in range(k):
        y=np.gradient(y,x,edge_order=2)
    return y

r=1.0
x=np.linspace(-1.2,1.2,400001)
for beta in [1,2,3]:
    d=deriv_grid(theta,x,beta)
    supd=np.max(np.abs(d))
    for m in [0.0,0.5,-1.0,2.0]:
        if beta<=m: continue
        print(f"beta={beta} m={m}  sup|d^beta theta|={supd:.6f}")
        for N in [2,5,10,20,40,80]:
            # ||g_N||_{K,0,beta,m} = sup_eta |d^beta theta(eta)| (1+|eta+N|)^{beta-m}
            val=np.max(np.abs(d)*(1+np.abs(x+N))**(beta-m))
            lb=(1+N-r)**(beta-m)*supd
            ok = val>=lb-1e-9*max(1,abs(lb))
            # reversed convention: sup |d| (1+|eta+N|)^{m-beta}
            rev=np.max(np.abs(d)*(1+np.abs(x+N))**(m-beta))
            print(f"   N={N:3d}  printed-seminorm={val:.6e}  note-lower-bound={lb:.6e}  ok={ok}   reversed-conv={rev:.6e}")
