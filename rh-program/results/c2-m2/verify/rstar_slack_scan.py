#!/usr/bin/env python3
"""rstar_slack_scan.py -- the stop condition of PRICING.md section 5(e): is |E_-| <= 2.7 delta^2 e^{delta L/2} absorbable in clause 6's
chain at EVERY delta in [25/L, 1/2] for L >= 50?  Run from results/c2-m2/verify/.

Clause 6's chain (separation-note.md section 7.1, D8 with ONE noise term N, which the proof itself allows):
    W_{Z'} - W_Z >= 2 delta^2 c(delta L)^2 - |E_-| - N - 2 e^{-L},   N <= 2 b1 C1 l_R / L^2,
and the target is  >= delta^2 e^{delta L/2}.  In units of U := delta^2 e^{delta L/2}:
    2 c(delta L)^2 / e^{delta L/2} >= 2 e^{m(delta L)},  m(lambda) = lambda/2 - 2 sqrt(lambda) - (3/2) log(lambda) + 2 kappa_-   (clause 2's lower bound; m increasing, m(25) = 0.6335, e^{m(25)} = 1.884),
    N/U <= l_R delta^2 / (2 b1 C1 L^2 (log(3+t))^2)   [from the L-hypothesis: e^{delta L/2} >= (log(3+t))^2 delta^{-4} (2 b1 C1)^2, as in (7.1)'s proof]
        <= (1.1 log 6 + L) delta^2 / (2 b1 L^2 (log 6)^2)   [l_R <= 1.1 log(3+t) + L for t >= 3, L >= 50, R0 L <= e^L - 1; C1 >= 1; (1.1x + L)/x^2 decreasing in x = log(3+t) >= log 6],
    2 e^{-L}/U <= 2 e^{-L}   [U >= 1 under the L-hypothesis, D8].
So the margin in units of U is  M(delta, L) := 2 e^{m(delta L)} - 2.7 - N/U - 2 e^{-L} - 1,  and the claim is M >= 0 on the range.
Scanned on 2001-point grids plus both endpoints for L = 50, 87, 376, 403, 1000, and on a coarser grid for L up to 1e5.
The largest absorbable coefficient (2 e^{m} - 1 - N/U - 2e^{-L}, minimized) is printed too.  Constants read from the record."""
import json, sys, time
import mpmath as mp
t0 = time.time(); mp.mp.dps = 30
out = {}
gj = json.load(open("lemma_G_constants_out.json")); bj = json.load(open("b1_constant_out.json")); ej = json.load(open("edge_law_two_sided_out.json"))
b1 = mp.mpf(bj["b1_certified_upper"]); kminus = mp.mpf(ej["kappa_minus"]); R0 = mp.mpf(gj["R0"]); Z = mp.mpf(bj["Z"])
SLACK = mp.mpf('2.7'); L6 = mp.log(6)
print(f"constants (read from the record): b1 = {mp.nstr(b1,6)} (certified upper), kappa_- = {mp.nstr(kminus,7)}, R0 = {mp.nstr(R0,3)} (the larger of 81/73, conservative for l_R), coefficient tested: {SLACK}")
def m(lam): lam = mp.mpf(lam); return lam/2 - 2*mp.sqrt(lam) - mp.mpf(3)/2*mp.log(lam) + 2*kminus
def N_over_U(d, L): d = mp.mpf(d); L = mp.mpf(L); return (mp.mpf('1.1')*L6 + L)*d*d/(2*b1*L*L*L6*L6)
def M(d, L): d = mp.mpf(d); L = mp.mpf(L); return 2*mp.e**m(d*L) - SLACK - N_over_U(d, L) - 2*mp.e**(-L) - 1
def cap(d, L): d = mp.mpf(d); L = mp.mpf(L); return 2*mp.e**m(d*L) - 1 - N_over_U(d, L) - 2*mp.e**(-L)
print(f"clause 3's proved margin at lambda = 25: e^m(25) = {mp.nstr(mp.e**m(25),5)} (record: 1.884);  m'(lambda) = 1/2 - 1/sqrt(lambda) - 3/(2 lambda) >= 0.24 for lambda >= 25, so e^m is increasing and the worst delta for the SLACK is delta = 25/L (lambda = 25), not delta = 1/2")
print(f"the R0 L <= e^L - 1 condition behind l_R <= 1.1 log(3+t) + L at L = 50: {mp.nstr(R0*50,4)} <= {mp.nstr(mp.e**50 - 1,4)}: {bool(R0*50 <= mp.e**50 - 1)}")
# scan
worst_all = mp.inf; scan = {}
for L in (50, 87, 376, 403, 1000):
    dlo = mp.mpf(25)/L; dhi = mp.mpf(1)/2; n = 2000
    grid = [dlo + (dhi - dlo)*k/n for k in range(0, n+1)]
    vals = [(M(d, L), d) for d in grid]
    mn, dmin = min(vals, key=lambda p: p[0]); mx, dmax = max(vals, key=lambda p: p[0])
    e_lo = M(dlo, L); e_hi = M(dhi, L); c_lo = cap(dlo, L); c_hi = cap(dhi, L)
    nu_max = max(N_over_U(d, L) for d in grid)
    ok = mn >= 0 and e_lo >= 0 and e_hi >= 0
    worst_all = min(worst_all, mn, e_lo, e_hi)
    print(f"L = {L:5d}: delta in [{mp.nstr(dlo,5)}, 0.5], {n+1} points + endpoints: min M = {mp.nstr(mn,5)} at delta = {mp.nstr(dmin,5)};  M(25/L) = {mp.nstr(e_lo,5)}, M(1/2) = {mp.nstr(e_hi,5)};  max N/U = {mp.nstr(nu_max,3)};  absorbable cap: {mp.nstr(c_lo,5)} at 25/L, {mp.nstr(c_hi,5)} at 1/2;  HOLDS: {ok}")
    scan[L] = dict(delta_lo=float(dlo), min_M=float(mn), argmin_delta=float(dmin), M_at_lo=float(e_lo), M_at_half=float(e_hi), max_N_over_U=float(nu_max), cap_at_lo=float(c_lo), cap_at_half=float(c_hi), holds=bool(ok))
out["scan"] = scan
# coarser sweep in L
worstL = mp.inf; argL = None
for L in [50 + k for k in range(0, 951)] + [1000*mp.mpf('1.1')**k for k in range(0, 50)]:
    dlo = mp.mpf(25)/L
    for d in [dlo, (dlo + mp.mpf(1)/2)/2, mp.mpf(1)/2]:
        v = M(d, L)
        if v < worstL: worstL = v; argL = (float(L), float(d))
print(f"sweep over L = 50..1000 step 1 and 1000..1e5 geometric, delta in (25/L, midpoint, 1/2): min M = {mp.nstr(worstL,5)} at (L, delta) = {argL}")
worst_all = min(worst_all, worstL)
out["min_M_overall"] = float(worst_all); out["min_M_sweep_at"] = argL
# analytic minimum: delta = 25/L, N/U at delta = 1/2 (the two worst cases cannot coincide; combining them is a further overestimate)
Mana = 2*mp.e**m(25) - SLACK - N_over_U(mp.mpf(1)/2, 50) - 2*mp.e**(-50) - 1
print(f"analytic lower bound for M on the whole range (e^m at lambda = 25, N/U at delta = 1/2, L = 50, e^-L at L = 50): {mp.nstr(Mana,5)} >= 0: {bool(Mana >= 0)};  the coefficient could be as large as {mp.nstr(cap(mp.mpf(1)/2, 50) if cap(mp.mpf(1)/2,50) < cap(mp.mpf(25)/50, 50) else cap(mp.mpf(25)/50, 50),5)} (2.7 is referee F's rounding of it)")
out["M_analytic_lower_bound"] = float(Mana); out["largest_absorbable_coefficient"] = float(min(cap(mp.mpf(1)/2, 50), cap(mp.mpf(25)/50, 50)))
# sanity (computed, not part of the proof): the actual c(lambda)^2/e^{lambda/2} at lambda = 25, 50, 100 against e^{m}
def Braw(v):
    v = mp.mpf(v); return mp.e**(-1/(1-4*v*v)) if abs(v) < mp.mpf(1)/2 else mp.mpf(0)
def c(lam): return mp.quad(lambda v: Braw(v)*mp.cosh(lam*v)/Z, [-mp.mpf(1)/2, 0, mp.mpf(1)/2])
print("sanity [computed]: c(lambda)^2/e^{lambda/2} against the proved e^{m(lambda)}: " + "; ".join(f"lambda = {lam}: {mp.nstr(c(lam)**2/mp.e**(mp.mpf(lam)/2),5)} >= {mp.nstr(mp.e**m(lam),5)}" for lam in (25, 50, 100)))
verdict = "HOLDS on [25/L, 1/2] for every L >= 50 (the 'closes' branch of PRICING section 5(e))" if worst_all >= 0 else "FAILS somewhere -- see the scan"
print("VERDICT: |E_-| <= 2.7 delta^2 e^{delta L/2} is absorbable: " + verdict)
out["verdict"] = verdict; out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "rstar_slack_scan_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
