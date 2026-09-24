#!/usr/bin/env python3
"""CHECK-O-B (Job 2, Opus 5) -- the checker's OWN numerics for Unit B, written without reading the builder's
cert_numbers.py or p23_diff.py.  Run from anywhere:  python3 numerics_BO.py <rh-program root>
 (i)  P2, P3, F13 transcribed here from the LEAN TEXT of comparator/ChallengeDeps/Separation5.lean, against
      r0_73_check.py lines 22-33 exec'd verbatim from the file, at L = 50, 100, 1e3, 1e4;
 (iv) the 16-cell Z enclosure (exact rationals), the constant enclosures, the certificate inequality cert_numeric
      in exact rational arithmetic, and F13(50) at the enclosure endpoints."""
import sys, os, math
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 50
root = sys.argv[1]
vdir = os.path.join(root, "results/c2-m2/verify")
# ---------- true constants at 50 digits ----------
e = mp.e
Braw = lambda v: mp.exp(-1/(1-4*v**2)) if abs(v) < mp.mpf(1)/2 else mp.mpf(0)
Z = 2*mp.quad(Braw, [0, mp.mpf(1)/4, mp.mpf(3)/8, mp.mpf(1)/2])
cB = 2/mp.sqrt(72*e); CB = e**2/Z; b1sym = (2*mp.exp(-1)/Z)**2; r73 = mp.sqrt(73)
print(f"Z = {mp.nstr(Z,20)}  cB = {mp.nstr(cB,20)}  CB = {mp.nstr(CB,20)}  b1sym = {mp.nstr(b1sym,20)}")
# ---------- (i) Lean text, transcribed by the checker ----------
def gammaPoly(n, a, s):            # sum_{j in range(n+1)} (n!:R)/(j!:R) * s^j / a^(n+1-j)
    return mp.fsum(mp.factorial(n)/mp.factorial(j)*s**j/a**(n+1-j) for j in range(n+1))
def Prelax(m, L):
    L = mp.mpf(L)
    return (1 + mp.mpf(3)/(2*(73*50-1)))**m * CB**2 * ((73*L)**m*(1 + cB/2*(r73*L))**2
        + 2/L**(m+1)*(gammaPoly(2*m+1, 2*cB, r73*L) + cB*gammaPoly(2*m+2, 2*cB, r73*L)
                      + cB**2/4*gammaPoly(2*m+3, 2*cB, r73*L)))
P2 = lambda L: Prelax(2, L); P3 = lambda L: Prelax(3, L)
def F13(L, b1):
    L = mp.mpf(L)
    return (mp.mpf(13)/8 - 2*cB*r73)*L + 2*cB/r73 + mp.log((mp.mpf(105)/100*P2(L) + P3(L))/b1)
# ---------- the script, lines 22-33 exec'd verbatim ----------
src = open(os.path.join(vdir, "r0_73_check.py")).read().splitlines()
block = "\n".join(src[21:33])
print("---- r0_73_check.py lines 22-33 (exec'd verbatim) ----"); print(block); print("----")
import json
gj = json.load(open(os.path.join(vdir, "lemma_G_constants_out.json"))); bj = json.load(open(os.path.join(vdir, "b1_constant_out.json")))
b1rec = mp.mpf(bj["b1_certified_upper"])
for label, ns_c in (("true constants (cB, CB from Z at 50 digits)", {"cB": cB, "CB": CB}),
                    ("record constants (json)", {"cB": mp.mpf(gj["c_B"]), "CB": mp.mpf(gj["C_B"])})):
    ns = {"mp": mp, "b1": b1rec}; ns.update(ns_c); exec(block, ns)
    print(f"[{label}]  record b1 = {mp.nstr(b1rec,10)}")
    save = (cB, CB)
    globals()["cB"], globals()["CB"] = ns_c["cB"], ns_c["CB"]
    worst = mp.mpf(0)
    for L in (50, 100, 1000, 10000):
        p2s, p3s = ns["P_relaxed"](2, L, 73, 50), ns["P_relaxed"](3, L, 73, 50)
        fs = ns["Ftilde"](L, 73, 50, mp.mpf(13)/8)
        p2l, p3l, fl = P2(L), P3(L), F13(L, b1rec)
        d = [abs(p2l-p2s)/abs(p2s), abs(p3l-p3s)/abs(p3s), abs(fl-fs)/abs(fs)]
        worst = max(worst, *d)
        print(f"  L={L:6d}  P2 lean {mp.nstr(p2l,16)} script {mp.nstr(p2s,16)} rel {mp.nstr(d[0],3)} | P3 rel {mp.nstr(d[1],3)} | "
              f"F13(b1 rec) lean {mp.nstr(fl,15)} script Ftilde {mp.nstr(fs,15)} rel {mp.nstr(d[2],3)} | F13(b1sym) {mp.nstr(F13(L, b1sym),10)}")
    print(f"  max relative difference: {mp.nstr(worst,3)}  -> {'AGREE' if worst < mp.mpf('1e-40') else 'DISAGREE'}")
    globals()["cB"], globals()["CB"] = save
print(f"5/(2cB sqrt73 - 13/8) = {mp.nstr(5/(2*cB*r73 - mp.mpf(13)/8),10)}  (A3: 6.113);  2cB sqrt73 - 13/8 = {mp.nstr(2*cB*r73-mp.mpf(13)/8,10)}")
print(f"F13(50) at record b1 = {mp.nstr(F13(50,b1rec),10)} (A3: -0.3227);  at b1sym = {mp.nstr(F13(50,b1sym),10)};  log(b1sym/b1rec) = {mp.nstr(mp.log(b1sym/b1rec),8)}")
# ---------- (iv) the certificate, exact rationals ----------
print("==== (iv) certificate, exact rational arithmetic ====")
fact = math.factorial
def expneg_upper(x):   # 1/sum_{k<8} x^k/k!
    return 1/sum(x**k/Fr(fact(k)) for k in range(8))
def T(y):              # sum_{m<8} y^m/m! + y^8*9/(8!*8)
    return sum(y**m/Fr(fact(m)) for m in range(8)) + y**8*9/Fr(fact(8)*8)
def xcell(i): return Fr(256, 256 - i*i)
def q(i): return math.ceil(xcell(i))
lo_terms, hi_terms = [], []
for i in range(16):
    x = xcell(i); qi = q(i)
    hi = expneg_upper(x)
    lo = 1/T(x/qi)**qi
    tv = mp.exp(-mp.mpf(x.numerator)/x.denominator)
    assert lo <= Fr(str(mp.nstr(tv, 45))) * (1 + Fr(1, 10**30)) and Fr(str(mp.nstr(tv,45))) <= hi * (1 + Fr(1,10**30))
    hi_terms.append(hi); lo_terms.append(lo)
    print(f"  i={i:2d} x={str(x):>9s}={float(x):.6f} q={qi} (lean qcell {1 if i==0 else 2 if i<=11 else 3 if i<=13 else 5 if i==14 else 9}) "
          f"lo={float(lo):.10e} exp(-x)={mp.nstr(tv,11)} hi={float(hi):.10e}")
    assert qi == (1 if i==0 else 2 if i<=11 else 3 if i<=13 else 5 if i==14 else 9)
Zlo_ex = sum(lo_terms[1:]) / 16          # right-endpoint sum: cells i+1 = 1..15, plus Braw(1/2) = 0
Zhi_ex = sum(hi_terms) / 16              # left-endpoint sum: cells 0..15
print(f"  Z_lo (exact sum)/16 = {float(Zlo_ex):.10f}  Z_hi = {float(Zhi_ex):.10f}   true Z = {mp.nstr(Z,12)}")
print(f"  421/2000 <= Z_lo_sum: {Fr(421,2000) <= Zlo_ex}   Z_hi_sum <= 233651/10^6: {Zhi_ex <= Fr(233651,10**6)}")
print(f"  slack: Z_lo_sum - 421/2000 = {float(Zlo_ex - Fr(421,2000)):.3e};  233651/10^6 - Z_hi_sum = {float(Fr(233651,10**6) - Zhi_ex):.3e}")
# true Riemann sums (no exp bounds) for reference
rs_lo = mp.fsum(Braw(mp.mpf(i+1)/32) for i in range(16))/16; rs_hi = mp.fsum(Braw(mp.mpf(i)/32) for i in range(16))/16
print(f"  true Riemann sums: right {mp.nstr(rs_lo,10)} <= Z = {mp.nstr(Z,10)} <= left {mp.nstr(rs_hi,10)}")
# constant enclosures
eLo = Fr(27182818283, 10**10); eHi = Fr(13591409143, 5*10**9)
cLo = Fr(14296064739, 10**11); cHi = Fr(14296064759, 10**11)
rLo = Fr(427200187261, 5*10**10); rHi = Fr(427200187271, 5*10**10)
ZLo = Fr(421, 2000); ZHi = Fr(233651, 10**6)
tof = lambda f: mp.mpf(f.numerator)/f.denominator
print(f"  eLo<=e<=eHi: {tof(eLo) <= e <= tof(eHi)}; cLo<=cB<=cHi: {tof(cLo) <= cB <= tof(cHi)}; rLo<=sqrt73<=rHi: {tof(rLo) <= r73 <= tof(rHi)}")
# exact rational side conditions the Lean proofs use: sqrt(72e) <= 2/cLo  <=  72 eHi <= (2/cLo)^2 ; 2/cHi <= sqrt(72 e) <= (2/cHi)^2 <= 72 eLo
print(f"  72*eHi <= (2/cLo)^2: {72*eHi <= (2/cLo)**2};  (2/cHi)^2 <= 72*eLo: {(2/cHi)**2 <= 72*eLo};  rLo^2 <= 73: {rLo**2 <= 73};  73 <= rHi^2: {73 <= rHi**2}")
CBHi = eHi**2/ZLo; b1Lo = (2/(eHi*ZHi))**2
print(f"  CBHi = {float(CBHi):.8f} (true CB {mp.nstr(CB,8)});  b1Lo = {float(b1Lo):.8f} (true b1sym {mp.nstr(b1sym,8)})")
def gP(n, a, s): return sum(Fr(fact(n), fact(j))*s**j/a**(n+1-j) for j in range(n+1))
def PQ(m):
    s = rHi*50; a = 2*cLo
    return (1 + Fr(3, 2*(73*50-1)))**m * CBHi**2 * (Fr(73*50)**m*(1 + cHi/2*s)**2
        + Fr(2, 50**(m+1))*(gP(2*m+1, a, s) + cHi*gP(2*m+2, a, s) + cHi**2/4*gP(2*m+3, a, s)))
ELo = 50*(2*cLo*rLo) - Fr(13,8)*50 - 2*cHi/rLo
LHS = (Fr(105,100)*PQ(2) + PQ(3))/b1Lo
RHS = eLo**40 * sum((ELo-40)**i/Fr(fact(i)) for i in range(6))
print(f"  ELo = {float(ELo):.10f};  ELo - 40 >= 0: {ELo >= 40}")
print(f"  cert_numeric: LHS = {float(LHS):.10e}  RHS = {float(RHS):.10e}  LHS <= RHS (exact): {LHS <= RHS};  margin log(RHS/LHS) = {mp.nstr(mp.log(tof(RHS)/tof(LHS)),8)} nats")
F13_end = mp.log(tof(LHS)) - tof(ELo)
print(f"  F13(50) upper bound at the endpoints = log(Q_hi/b1_lo) - E_lo = {mp.nstr(F13_end,8)} (builder: -0.3474; pricing: -0.349)")
print(f"  true F13(50) at b1sym = {mp.nstr(F13(50,b1sym),8)} >= endpoint bound? {F13(50,b1sym) <= F13_end}  (the bound must be an UPPER bound)")
print(f"  second conjunct: 2 cLo rLo - 13/8 = {float(2*cLo*rLo - Fr(13,8)):.8f};  5/(that) = {float(5/(2*cLo*rLo-Fr(13,8))):.6f} <= 50: {5/(2*cLo*rLo-Fr(13,8)) <= 50}")
print("digits in cert_numeric's cleared numerator/denominator:", len(str(LHS.numerator)), len(str(LHS.denominator)), len(str(RHS.numerator)), len(str(RHS.denominator)))
