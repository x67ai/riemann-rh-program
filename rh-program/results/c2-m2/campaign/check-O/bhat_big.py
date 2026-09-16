"""CHECKER close 4: |Bhat(eta)| at large eta at 40+ digits, by oscillatory quadrature with breakpoints at the
extrema/zeros of cos(eta v), at enough precision to survive the cancellation (own implementation)."""
from mpmath import mp
import math, json, sys
def bhat_big(eta, dps):
    with mp.workdps(dps):
        e=mp.mpf(eta); half=mp.mpf(1)/2
        Zn=mp.quad(lambda v: mp.exp(-1/(1-4*v*v)), [-half,-mp.mpf(1)/4,0,mp.mpf(1)/4,half])
        f=lambda v: mp.exp(-1/(1-4*v*v))*mp.cos(e*v)
        # breakpoints: all multiples of pi/eta in (0,1/2) (zeros and extrema of cos(eta v)); B even -> 2*int_0^{1/2}
        n=int(mp.floor(e*half/mp.pi))
        pts=[mp.mpf(0)]+[mp.pi*j/e for j in range(1,n+1)]+[half]
        tot=mp.mpf(0)
        for i in range(len(pts)-1):
            tot+=mp.quad(f,[pts[i],pts[i+1]])
        return 2*tot/Zn
if __name__=="__main__":
    res={}
    for eta,dps in [(1000,60),(10000,80),(16384,90),(100000,110)]:
        v=bhat_big(eta,dps); v2=bhat_big(eta,dps+25)
        env=9*mp.mpf(eta)**mp.mpf(-0.75)*mp.e**(-mp.sqrt(mp.mpf(eta)/2))
        print("eta=%-8d Bhat=%s   |Bhat|=%s" % (eta, mp.nstr(v,20), mp.nstr(abs(v),12)), flush=True)
        print("          stability (dps+25): %s ; rel diff %.2e" % (mp.nstr(v2,20), float(abs(v2/v-1))))
        print("          envelope 9 eta^-3/4 e^{-sqrt(eta/2)} = %s ; |Bhat|/env = %.4f" % (mp.nstr(env,8), float(abs(v)/env)))
        print("          implied A = |Bhat| eta^{3/4} e^{sqrt(eta/2)} = %.5f ; local rate -log|Bhat|/sqrt(eta) = %.5f"
              % (float(abs(v)*mp.mpf(eta)**mp.mpf(0.75)*mp.e**mp.sqrt(mp.mpf(eta)/2)), float(-mp.log(abs(v))/mp.sqrt(mp.mpf(eta)))))
        res[eta]=dict(bhat=mp.nstr(v,25), absb=float(abs(v)), env=float(env), A=float(abs(v)*mp.mpf(eta)**mp.mpf(0.75)*mp.e**mp.sqrt(mp.mpf(eta)/2)))
    json.dump(res, open("bhat_big.json","w"), indent=1)
    print("DONE")
