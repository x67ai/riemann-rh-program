#!/usr/bin/env python3
"""lemma_G_constants.py -- Lemma G (Fourier decay of B from the LEAN derivative bounds) and every constant downstream of it:
  Lean P1 (Zeta23/Taper/Gevrey.lean, gevrey_expNegInvGlue): |g^{(k)}(x)| <= (18/e)^k k^{2k}, g(x) = exp(-1/x) (x>0), 0 (x<=0).
  B_raw(v) = exp(-1/(1-4v^2)) = g(4v+2) * g(2-4v)   (affine chain rule: factor 4^k per factor; Leibniz with
  C(k,i) i^i (k-i)^{k-i} <= k^k gives  |B_raw^{(k)}| <= (k+1) A1^k k^{2k},  A1 := 72/e;  the crude 2^k route gives A = 144/e).
  ||B_raw^{(k)}||_1 <= sup (support length 1);  |Bhat(eta)| <= ||B^{(k)}||_1/eta^k;  k = floor(sqrt(eta/A1)/e) gives
  (G1)  |Bhat(eta)| <= C_B (1 + (c_B/2) sqrt eta) exp(-c_B sqrt eta),  c_B = 2/sqrt(72 e), C_B = e^2/Z,   all eta >= 0;
  (G2)  |Bhat(eta)| <= C_B' exp(-c_B' sqrt eta),  c_B' = (7/8) c_B, C_B' = 4 e^{-3/4} C_B   (clean form).
Downstream: clause 5's R_0 (explicit, all L >= 50), clause 1's reflection condition (R) and its clean form t >= c_R L,
clause 4's L_1 (polynomial route, ||B'''||_1 from b1_constant_out.json), and the IV.9 numbers L*(delta, t).
Budget: < 10 min."""
import time, json, sys, math
import mpmath as mp
t0 = time.time(); mp.mp.dps = 30
out = {}
b1j = json.load(open("b1_constant_out.json"))
Z = mp.mpf(b1j["Z"]); b1 = mp.mpf(b1j["b1_certified_upper"]); B3 = mp.mpf(b1j["norm_B3_L1"])
def g(x):
    x = mp.mpf(x)
    return mp.e**(-1/x) if x > 0 else mp.mpf(0)
def Braw(v):
    v = mp.mpf(v)
    if abs(v) >= mp.mpf(1)/2: return mp.mpf(0)
    return mp.e**(-1/(1-4*v*v))
# (a) the factorization B_raw(v) = g(4v+2) g(2-4v)
print("(a) factorization check |B_raw(v) - g(4v+2)g(2-4v)|:", max(float(abs(Braw(v) - g(4*v+2)*g(2-4*v))) for v in [mp.mpf(x)/100 for x in range(-49, 50)]))
# (b) Lean P1 bound for g, numerically, k = 1..6 at x on a grid (sanity: the bound must hold, loosely)
A18 = 18/mp.e; A1 = 72/mp.e; Acrude = 144/mp.e
print("(b) Lean P1 |g^(k)(x)| <= (18/e)^k k^(2k), ratio max over x in (0, 1.5], k=1..6:")
for k in range(1, 7):
    r = max(abs(mp.diff(g, mp.mpf(x)/40, k))/(A18**k*mp.mpf(k)**(2*k)) for x in range(1, 61))
    print(f"    k={k}: max ratio = {mp.nstr(r, 4)}")
print("    Leibniz-transferred |B_raw^(k)(v)| <= (k+1)(72/e)^k k^(2k), ratio max over v in (-1/2,1/2), k=1..6:")
for k in range(1, 7):
    r = max(abs(mp.diff(Braw, mp.mpf(x)/100, k))/((k+1)*A1**k*mp.mpf(k)**(2*k)) for x in range(-49, 50))
    print(f"    k={k}: max ratio = {mp.nstr(r, 4)}   (||B_raw^(k)||_1 <= sup, support length 1)")
# (c) Lemma G constants
cB = 2/mp.sqrt(72*mp.e); CB = mp.e**2/Z; cBc = 1/(6*mp.sqrt(mp.e)); CBc = CB
cB2 = mp.mpf(7)/8*cB; CB2 = 4*mp.e**(-mp.mpf(3)/4)*CB
out.update(c_B=float(cB), C_B=float(CB), c_B_crude=float(cBc), c_B_clean=float(cB2), C_B_clean=float(CB2), A1=float(A1), Z=float(Z))
print(f"(c) c_B = 2/sqrt(72e) = {mp.nstr(cB,8)};  C_B = e^2/Z = {mp.nstr(CB,8)};  crude-Leibniz c_B = 1/(6 sqrt e) = {mp.nstr(cBc,6)};  clean form c_B' = {mp.nstr(cB2,6)}, C_B' = {mp.nstr(CB2,6)};  the pricing's 0.20 = 1/(3 sqrt e) = {mp.nstr(1/(3*mp.sqrt(mp.e)),6)} is the constant for theta, not for B")
def Bhat(eta):
    eta = mp.mpf(eta)
    return mp.quad(lambda v: Braw(v)*mp.cos(eta*v)/Z, [-0.5, -0.25, 0, 0.25, 0.5])
def G1(eta): eta = mp.mpf(eta); return CB*(1 + cB/2*mp.sqrt(eta))*mp.e**(-cB*mp.sqrt(eta))
def G2(eta): eta = mp.mpf(eta); return CB2*mp.e**(-cB2*mp.sqrt(eta))
print("    (G1)/(G2) against |Bhat(eta)| (log10 of ratio bound/|Bhat| must be >= 0):")
worst1 = 99; worst2 = 99
etas = [0, 0.5, 1, 2, 4, 8, 16, 32, 64, 128, 195.7, 256, 512, 1024, 2048, 4096, 8192, 16384]
for e in etas:
    bh = abs(Bhat(e)); r1 = G1(e)/bh if bh > 0 else mp.inf; r2 = G2(e)/bh if bh > 0 else mp.inf
    worst1 = min(worst1, float(mp.log10(r1))); worst2 = min(worst2, float(mp.log10(r2)))
    if e in (0, 8, 64, 512, 4096, 16384):
        print(f"    eta={e}: |Bhat|={mp.nstr(bh,4)}  G1={mp.nstr(G1(e),4)}  G2={mp.nstr(G2(e),4)}  log10(G1/|Bhat|)={float(mp.log10(r1)):.2f}")
print(f"    min log10(G1/|Bhat|) = {worst1:.3f}, min log10(G2/|Bhat|) = {worst2:.3f} over {len(etas)} eta values")
# also the numerical decay constant for the record: fit log|Bhat| ~ -c sqrt(eta) on the envelope
env = [(e, float(mp.log(abs(Bhat(e))))) for e in (256, 512, 1024, 2048, 4096, 8192)]
cnum = -min(y/math.sqrt(e) for e, y in env); out["numerical_decay_constant_envelope"] = cnum
print(f"    numerical envelope constant (max over eta in 256..8192 of -log|Bhat|/sqrt eta, a lower bound on the true rate): {cnum:.3f}  [computed, not proved]")
out["G1_min_log10_ratio"] = worst1; out["G2_min_log10_ratio"] = worst2
# (d) clause 5: the explicit out-window sum bound and R_0
#   S <= (e^{3L/4}/b1) [ 1.05 * Sigma_2 + Sigma_3 ],  Sigma_m := sum_{k >= R-1} (k+3/2)^m G1(Lk)^2 <= (5/2)^m C_B^2 [phi_m(R-1) + int_{R-1}^inf phi_m],
#   phi_m(u) := u^m (1 + (c_B/2) sqrt(Lu))^2 e^{-2 c_B sqrt(Lu)},  int = (2/L^{m+1}) int_{s0}^inf s^{2m+1} (1 + c_B s/2)^2 e^{-2 c_B s} ds, s0 = sqrt(L(R-1))
def upper_incgamma_poly(n, a, s0):
    # int_{s0}^inf s^n e^{-a s} ds = e^{-a s0} sum_{j=0}^n n!/j! s0^j / a^{n+1-j}
    return mp.e**(-a*s0)*mp.fsum(mp.factorial(n)/mp.factorial(j)*s0**j/a**(n+1-j) for j in range(n+1))
def Sigma_bound(m, L, R):
    L = mp.mpf(L); R = mp.mpf(R); u0 = R - 1; s0 = mp.sqrt(L*u0); a = 2*cB
    phi0 = u0**m*(1 + cB/2*s0)**2*mp.e**(-a*s0)
    integ = (2/L**(m+1))*(upper_incgamma_poly(2*m+1, a, s0) + cB*upper_incgamma_poly(2*m+2, a, s0) + cB**2/4*upper_incgamma_poly(2*m+3, a, s0))
    return (mp.mpf(5)/2)**m*CB**2*(phi0 + integ)
def logS_bound_plus_L(L, R0):
    L = mp.mpf(L); R = R0*L
    S = (mp.e**(3*L/4)/b1)*(mp.mpf('1.05')*Sigma_bound(2, L, R) + Sigma_bound(3, L, R))
    return mp.log(S) + L        # must be <= 0
# least R0 (step 0.5) with F(50) <= 0 and slope condition 2 c_B sqrt(R0) - 7/4 >= 5/50 (polynomial degree 5 in L)
R0 = mp.mpf(1)
while True:
    if logS_bound_plus_L(50, R0) <= 0 and 2*cB*mp.sqrt(R0) - mp.mpf(7)/4 >= mp.mpf(5)/50:
        break
    R0 += mp.mpf('0.5')
print(f"(d) clause 5: least R_0 (step 0.5) with F(50) := log S_bound(50, R_0 L) + L <= 0 and 2c_B sqrt(R_0) - 7/4 >= 0.1:  R_0 = {mp.nstr(R0,4)};  F(50) = {mp.nstr(logS_bound_plus_L(50, R0),5)}")
print(f"    asymptotic constants: (3/(4 c_B))^2 = {mp.nstr((3/(4*cB))**2,5)} (contract's form),  (7/(8 c_B))^2 = {mp.nstr((7/(8*cB))**2,5)} (with the density prefactor absorbed through the L-hypothesis)")
worstF = -mp.inf
for L in [50, 55, 60, 70, 80, 100, 150, 200, 300, 403, 500, 1000, 2000, 5000, 10000, 100000]:
    F = logS_bound_plus_L(L, R0); worstF = max(worstF, F)
    if L in (50, 60, 100, 403, 1000, 10000, 100000): print(f"    L={L}: F(L) = log S_bound + L = {mp.nstr(F,5)}")
print(f"    max F over the L-grid = {mp.nstr(worstF,5)} (<= 0 required; the note proves the decrease in L analytically)")
out["R0"] = float(R0); out["F50_at_R0"] = float(logS_bound_plus_L(50, R0)); out["R0_asymptotic_contract_form"] = float((3/(4*cB))**2); out["R0_asymptotic_with_prefactor"] = float((7/(8*cB))**2)
# what R_0 the NUMERICAL decay constant would give, for the record (not proved)
print(f"    for the record [computed, not proved]: with the numerical rate {cnum:.3f} the same chain would give (7/(8c))^2 = {(7/(8*cnum))**2:.2f}")
# (e) clause 1: the reflection condition.  |E_-| <= 2(4t^2+delta^2) e^{delta L} G1(2tL)^2 <= 2 delta^2 c(delta L)^2 e^{-L}
#     sufficient (using clause 2's lower bound on c and delta in [25/L, 1/2]):
#     2 c_B sqrt(2tL) - 2 log(1 + (c_B/2) sqrt(2tL)) >= L + sqrt(2L) + 1.5 log(L/2) - 2 kappa_- + log((4t^2+1/4) C_B^2 L^2/625)
kminus = mp.mpf(json.load(open("edge_law_two_sided_out.json"))["kappa_minus"])
def refl_margin(t, L):
    t = mp.mpf(t); L = mp.mpf(L); s = mp.sqrt(2*t*L)
    lhs = 2*cB*s - 2*mp.log(1 + cB/2*s)
    rhs = L + mp.sqrt(2*L) + mp.mpf(1.5)*mp.log(L/2) - 2*kminus + mp.log((4*t*t + mp.mpf(1)/4)*CB**2*L**2/625)
    return lhs - rhs
print("(e) clause 1 reflection condition: least t = T_1(L) with margin >= 0, and the clean linear form t >= c_R L:")
T1 = {}
for L in (50, 100, 200, 403, 1000, 10000):
    t = mp.mpf(L)
    while refl_margin(t, L) < 0: t *= mp.mpf('1.01')
    T1[L] = float(t); print(f"    L={L}: T_1(L) = {mp.nstr(t,5)}  (T_1/L = {mp.nstr(t/L,4)})")
out["T1_of_L"] = T1
cR = 1
while any(refl_margin(cR*L, L) < 0 for L in [50, 55, 60, 70, 80, 100, 150, 200, 300, 500, 1000, 3000, 10000, 100000]): cR += 1
print(f"    least integer c_R with t = c_R L admissible on the L-grid: c_R = {cR};  margins at L=50,100,1000,1e5: {[float(refl_margin(cR*L, L)) for L in (50,100,1000,100000)]}")
print(f"    asymptotic threshold t/L -> 1/(8 c_B^2) = {mp.nstr(1/(8*cB**2),5)};  [computed, not proved] with the numerical rate {cnum:.3f}: 1/(8c^2) = {1/(8*cnum**2):.3f}")
out["c_R"] = cR; out["t_over_L_asymptotic"] = float(1/(8*cB**2))
# (f) clause 4: L_1 from the polynomial route, and where the Gevrey form would put it
zeta4 = mp.zeta(4)
L1 = (2*zeta4*B3**2/b1)**(mp.mpf(1)/4)
print(f"(f) clause 4: ||B'''||_1 = {mp.nstr(B3,8)};  L_1 = (2 zeta(4) ||B'''||_1^2 / b1)^(1/4) = {mp.nstr(L1,5)}  (polynomial route; L >= 50 already covers it)")
def gev_T1_ratio(L):   # 2 C_B^2 sum_{k>=1} (k+1)^2 G1(Lk)^2/C_B^2 ... i.e. Gevrey T1 bound divided by b1/L^2
    L = mp.mpf(L)
    s = mp.fsum((k+1)**2*G1(L*k)**2 for k in range(1, 4000))
    return 2*s/(b1/L**2)
Lg = 100
while gev_T1_ratio(Lg) > 1: Lg = int(Lg*1.1)
print(f"    for the record: the contract's GEVREY form of T_1 falls below b1 C1 l_R/L^2 only from L ~ {Lg} (with c_B = {mp.nstr(cB,4)})")
out["L1_poly"] = float(L1); out["L1_gevrey_form_approx"] = Lg
# (g) IV.9 numbers: L*(delta, t) = max(25/delta, 4/delta (loglog(3+t) + 2 log(1/delta) + log(2 b1 C1))), C1 = 1; balance-only value from the pricing
def Lstar(d, t, C1=1):
    d = mp.mpf(d); t = mp.mpf(t)
    return max(25/d, 4/d*(mp.log(mp.log(3+t)) + 2*mp.log(1/d) + mp.log(2*b1*C1)))
print("(g) IV.9: L* from the theorem's constants (C1 = 1):")
vis = {}
for d, t in ((0.1, 1e6), (0.1, 1e3), (0.1, 1e12), (0.05, 1e6), (0.25, 1e6), (0.3085, 85.7)):
    Ls = Lstar(d, t); vis[f"delta={d},t={t:.4g}"] = dict(L_star=float(Ls), R=float(R0*Ls), t_over_L=float(mp.mpf(t)/Ls), reflection_ok=bool(mp.mpf(t) >= cR*Ls))
    print(f"    delta={d}, t={t:.3g}: L* = {mp.nstr(Ls,5)}, window R = R_0 L* = {mp.nstr(R0*Ls,5)}, t/L* = {mp.nstr(mp.mpf(t)/Ls,4)}, reflection condition t >= {cR} L*: {bool(mp.mpf(t) >= cR*Ls)}")
out["visibility"] = vis
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "lemma_G_constants_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
