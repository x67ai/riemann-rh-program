# Reader's independent re-derivation check of E1 FORMULATION (2.2) and clause 1 (strip positivity).
# (A) (2.2): int e^{iux} cosh(yu)/cosh(u/2) du = 2*pi*cosh(pi x)cos(pi y)/|cosh(pi(x - i y))|^2, |y|<1/2,
#     by direct quadrature (scipy.integrate.quad with weight='cos' over [0, inf) is not available for inf with
#     growing integrand, so use a truncated trapezoid on [-U, U] with U large; the integrand decays like e^{-(1/2-|y|)|u|}).
# (B) Clause 1: psi(u) = (1-u^2)^3 on (-1,1) (so k = psi*psi on (-2,2), L = 4), g = k/cosh(u/2);
#     Re ghat(x+iy) = int g(u) cos(xu) cosh(yu) du on a grid, and the convolution form (2pi)^{-1}(|psihat|^2 * P_y)(x).
#     Also the plain family: Re khat(x+iy) = int k(u) cos(xu) cosh(yu) du at y = 1/2 (expected to go negative).
import numpy as np, time
t0=time.time()
def P(x,y): return 2*np.pi*np.cosh(np.pi*x)*np.cos(np.pi*y)/np.abs(np.cosh(np.pi*(x-1j*y)))**2
print("(A) identity (2.2)")
for (x,y) in [(0.0,0.0),(1.3,0.0),(1.3,0.25),(1.3,0.45),(4.0,0.3),(-2.2,0.1)]:
    U=60.0/(0.5-abs(y)); n=int(2e6)
    u=np.linspace(-U,U,n+1); h=u[1]-u[0]
    f=np.cos(x*u)*np.cosh(y*u)/np.cosh(u/2)
    val=h*(f.sum()-0.5*(f[0]+f[-1]))
    print(f"  x={x:5.2f} y={y:4.2f}  quad={val:.12f}  formula={P(x,y):.12f}  diff={val-P(x,y):.2e}")
# (B)
N=40001
u=np.linspace(-2,2,N); du=u[1]-u[0]
s=np.linspace(-1,1,20001); ds=s[1]-s[0]
psi=lambda v: np.where(np.abs(v)<1,(1-v**2)**3,0.0)
# k(u) = int psi(s) psi(s-u) ds (psi even and real)
k=np.array([ds*np.sum(psi(s)*psi(s-uu)) for uu in u[::20]])
uk=u[::20]; duk=uk[1]-uk[0]
g=k/np.cosh(uk/2)
def ReG(x,y,fn): return duk*np.sum(fn*np.cos(x*uk)*np.cosh(y*uk))
xs=np.linspace(0,40,801)
print("(B) min over x in [0,40] of Re ghat(x+iy) (sech family) and Re khat(x+iy) (plain family)")
for y in (0.0,0.25,0.45,0.49,0.5):
    vg=np.array([ReG(x,y,g) for x in xs]); vk=np.array([ReG(x,y,k) for x in xs])
    print(f"  y={y:4.2f}: sech-family min={vg.min():+.3e} at x={xs[vg.argmin()]:.2f};  plain min={vk.min():+.3e} at x={xs[vk.argmin()]:.2f}")
# convolution-form cross-check at two points
psihat=lambda xi: np.array([ds*np.sum(psi(s)*np.cos(t*s)) for t in np.atleast_1d(xi)])
xi=np.linspace(-60,60,4801); dxi=xi[1]-xi[0]; ph2=psihat(xi)**2
for (x,y) in [(3.0,0.25),(6.5,0.45)]:
    conv=dxi*np.sum(ph2*P(x-xi,y))/(2*np.pi)
    print(f"  cross-check x={x} y={y}: direct={ReG(x,y,g):.8f}  (2pi)^-1(|psihat|^2*P_y)={conv:.8f}")
print("elapsed %.1fs"%(time.time()-t0))
