"""CHECKER task (3): independent computation of ||B^{(k)}||_1 for k = 1..13, and the clause-4 truncation bound.

Derivation, done here from scratch.  B_raw(v) = exp(phi), phi = -1/w, w = 1 - 4v^2, w' = -8v, phi' = -8v/w^2.
Write B_raw^{(k)} = exp(phi) * P_k(v) / w^{2k}, P_0 = 1.  Differentiating,
   B_raw^{(k+1)} = exp(phi)[ phi' P_k + P_k' - 2k P_k w'/w ] / w^{2k}
                 = exp(phi)[ -8v P_k + P_k' w^2 + 16 k v P_k w ] / w^{2k+2},
so  P_{k+1} = -8 v P_k + P_k' w^2 + 16 k v P_k w   (exact integer coefficients).
||B^{(k)}||_1 = (1/Z) int_{-1/2}^{1/2} |exp(phi) P_k / w^{2k}| dv, Z = int exp(phi).
Roots of P_k inside (-1/2,1/2) found with mpmath.polyroots (independent of the builder's scan+bisection).
"""
from mpmath import mp
import json
mp.dps = 60
def pmul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return r
def padd(*ps):
    n=max(len(p) for p in ps); r=[0]*n
    for p in ps:
        for i,x in enumerate(p): r[i]+=x
    return r
def pder(a): return [i*a[i] for i in range(1,len(a))] or [0]
w=[1,0,-4]                       # 1 - 4 v^2 (ascending)
P=[[1]]
for k in range(13):
    p=P[-1]
    P.append(padd(pmul([0,-8],p), pmul(pder(p), pmul(w,w)), pmul([0,16*k], pmul(p,w))))
half=mp.mpf(1)/2
Z=mp.quad(lambda v: mp.exp(-1/(1-4*v*v)), [-half,-mp.mpf(1)/4,0,mp.mpf(1)/4,half])
print("Z =", mp.nstr(Z, 20))
norms={}; info={}
for k in range(1,14):
    coeffs=[mp.mpf(c) for c in reversed(P[k])]      # descending for polyroots
    while coeffs and coeffs[0]==0: coeffs=coeffs[1:]
    deg=len(coeffs)-1
    roots=[]
    if deg>0:
        rr=mp.polyroots(coeffs, maxsteps=300, extraprec=400)
        for z in rr:
            if abs(mp.im(z))<mp.mpf(10)**(-25) and -half<mp.re(z)<half:
                roots.append(mp.re(z))
    pts=sorted(set([-half,half]+[mp.mpf(r) for r in roots]))
    def Bk(v, k=k, co=coeffs):
        if abs(v)>=half: return mp.mpf(0)
        return mp.exp(-1/(1-4*v*v))*mp.polyval(co,v)/(1-4*v*v)**(2*k)/Z
    tot=mp.mpf(0); pieces=[]
    for i in range(len(pts)-1):
        val=mp.quad(Bk,[pts[i],pts[i+1]]); pieces.append(abs(val)); tot+=abs(val)
    norms[k]=tot
    info[k]=dict(deg=deg, n_roots=len(roots), roots=[mp.nstr(r,12) for r in roots])
    print("k=%2d deg=%2d roots_in=(%d) ||B^(k)||_1 = %s" % (k, deg, len(roots), mp.nstr(tot, 15)), flush=True)
rec={1:3.31427535948,2:28.7726440417,3:642.301196307,4:38779.9672465,5:4291724.35138,6:766365507.977,
     7:201117898544.0,8:7.28650765558e+13,9:3.48429007153e+16,10:2.12573067064e+19,11:1.61134800942e+22,
     12:1.48562110881e+25,13:1.63707485619e+28}
print("\n k | checker (40+ digits)        | builder DERIV_NORMS_RECORD  | rel diff")
out={}
for k in range(1,14):
    d=abs(float(norms[k])/rec[k]-1)
    out[k]=dict(checker=mp.nstr(norms[k],16), builder=rec[k], rel=d)
    print("%2d | %-27s | %-27.12g | %.3e"%(k, mp.nstr(norms[k],14), rec[k], d))
json.dump({"norms":{k:mp.nstr(v,18) for k,v in norms.items()},"cmp":{k:{"rel":v["rel"]} for k,v in out.items()},
           "Z":mp.nstr(Z,20),"info":{k:{"deg":v["deg"],"n_roots":v["n_roots"]} for k,v in info.items()}},
          open("/private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math-riemann/f0642f49-dab5-4c05-a061-651fcb3ec7a7/scratchpad/chk/deriv_norms.json","w"), indent=1)
print("DONE")
