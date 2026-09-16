"""CHECKER task (5): re-verify three of the new off-line zeros of f_DH at 30 digits and one new-height control row.
f_DH is taken from its DEFINITION (results/ccm-dh-test/dh.py docstring), re-coded here; the transform is the checker's own."""
import json, math, sys, warnings, os
warnings.filterwarnings("ignore"); import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp, numpy as np
import ind_transform as T
BASE="/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/c2-m2/campaign"
def kap():
    s5=mp.sqrt(5); return (mp.sqrt(10-2*s5)-2)/(s5-1)
def fdh(s):
    k=kap()
    return 5**(-s)*(mp.zeta(s,mp.mpf(1)/5)+k*mp.zeta(s,mp.mpf(2)/5)-k*mp.zeta(s,mp.mpf(3)/5)-mp.zeta(s,mp.mpf(4)/5))
def xidh(s): return (5/mp.pi)**((s+1)/2)*mp.gamma((s+1)/2)*fdh(s)
def Zdh(u): return mp.re(xidh(mp.mpf('0.5')+1j*u))
J=json.load(open(f"{BASE}/dh_offline_scan.json"))
strip=J['found_in_strip']
new=[r for r in strip if abs(r['t']-85.699348)>=0.01]
print("strip orbits: %d (new: %d)"%(len(strip),len(new)))
picks=[new[0], new[10], new[-1]]      # t = 114.16, 520.94 (shallowest-ish), 892.15
print("\n(A) three new off-line zeros of f_DH, re-verified at 30 digits")
for rec in picks:
    b,g=rec['rho']
    with mp.workdps(30):
        s0=mp.mpc(b,g)
        v0=fdh(s0)
        r=mp.findroot(fdh, s0, tol=mp.mpf(10)**(-40), maxsteps=50, verify=False)
        vr=fdh(r)
    print("  rho = %s + %s i" % (mp.nstr(mp.re(r),15), mp.nstr(mp.im(r),15)))
    print("     |f_DH(stored rho)| = %.3e ; |f_DH(refined)| = %.3e ; |refined - stored| = %.2e"
          %(float(abs(v0)),float(abs(vr)),float(abs(r-s0))))
    print("     beta = %.12f -> in the OPEN strip 0 < beta < 1: %s ; off the line (beta != 1/2): delta = |beta - 1/2| = %.9f (stored %.9f)"
          %(float(mp.re(r)), 0<float(mp.re(r))<1, abs(float(mp.re(r))-0.5), rec['delta']))
print("\n(B) one new-height control row, recomputed with the checker's own transform")
rec=new[0]; t=rec['t']; d=rec['delta']; Wd=30.0
g=np.array(rec['online_window'])
print("  t = %.6f, delta = %.6f, %d DH on-line zeros in [t-30, t+30] (builder's list, re-checked below)"%(t,d,len(g)))
mp.mp.dps=25
bad=max(float(abs(Zdh(mp.mpf(repr(x))))) for x in g)
print("  max |Z_DH(gamma)| over the builder's on-line list at 25 digits: %.3e"%bad)
for row in rec['control_rows']:
    L=row['L']
    u=g-t; m=np.abs(u)<=Wd; uu=u[m]
    bh=T.bhat(L*uu,16000); N=float((uu*uu*bh*bh).sum())
    c=float(T.cedge(d*L,16000)[0]); main=-2*d*d*c*c; WZ=N+main
    bnd=d*d*math.exp(d*L/2); ratio=abs(WZ-N)/bnd
    print("   L=%8.2f  W_Z chk=%.6e bld=%.6e (rel %.2e) | W_Z' chk=%.4e bld=%.4e (abs %.2e) | main rel %.2e | ratio chk=%.5g bld=%.5g"
          %(L,WZ,row['W_Z'],abs(WZ/row['W_Z']-1),N,row['W_Zprime'],abs(N-row['W_Zprime']),abs(main/row['main']-1),ratio,row['ratio']))
print("DONE")
