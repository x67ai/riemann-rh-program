#!/usr/bin/env python3
"""rstar_table.py -- the weaker reflection condition (R*) of referee F (referee-F.md section 6), reproduced by the author
(Session 23 item 2, the addendum to separation-note.md).  Run from results/c2-m2/verify/.

Clause 1's explicit bound  |E_-| <= 2 (4t^2 + delta^2) e^{delta L} G(2tL)^2,  G(eta) = C_B (1 + (c_B/2) sqrt eta) e^{-c_B sqrt eta},
fed into clause 6's slack  |E_-| <= 2.7 delta^2 e^{delta L/2}  (rstar_slack_scan.py verifies that 2.7 is absorbable), gives
  (R*)   2 c_B sqrt(2tL) - 2 log(1 + (c_B/2) sqrt(2tL))  >=  delta L/2 + log((4t^2 + delta^2) C_B^2 / (1.35 delta^2)).
This script: (a) the right side is increasing in delta for delta >= 4/L (so the worst case on [25/L, 1/2] is delta = 1/2);
(b) the margin (left - right) is increasing in t for t >= 8/(c_B^2 L) (so "least t" is a threshold); (c) the least t at delta = 1/2
for L = 50, 87, 376, 403, 1000 (+ 100, 200, 1e4) and the asymptotic ratio 1/(128 c_B^2); (d) the t = 10^3 (and 10^4) lines the
campaign needs: the largest L at which t is inside (R*), and the record-point rows of CAMPAIGN.md section 5; (e) the DH control's
margin at (85.7, 87, 0.3085); (f) (R) implies (R*) on the admissible range, so t >= 21L implies (R*).
Constants are READ from the record (lemma_G_constants_out.json, b1_constant_out.json, edge_law_two_sided_out.json), not re-derived."""
import json, sys, time
import mpmath as mp
t0 = time.time(); mp.mp.dps = 30
out = {}
gj = json.load(open("lemma_G_constants_out.json")); bj = json.load(open("b1_constant_out.json")); ej = json.load(open("edge_law_two_sided_out.json"))
cB = mp.mpf(gj["c_B"]); CB = mp.mpf(gj["C_B"]); Z = mp.mpf(bj["Z"]); b1 = mp.mpf(bj["b1_certified_upper"]); kminus = mp.mpf(ej["kappa_minus"])
assert abs(cB - 2/mp.sqrt(72*mp.e)) < mp.mpf('1e-12') and abs(CB - mp.e**2/Z) < mp.mpf('1e-9'), "record constants do not match their closed forms"
print(f"constants (read from the record): c_B = {mp.nstr(cB,8)}, C_B = {mp.nstr(CB,7)}, b1 = {mp.nstr(b1,6)} (certified upper), kappa_- = {mp.nstr(kminus,7)}, Z = {mp.nstr(Z,10)}")
SLACK = mp.mpf('2.7')                      # the absorbable coefficient in |E_-| <= SLACK delta^2 e^{delta L/2}  (rstar_slack_scan.py)
def lhs(t, L):
    s = mp.sqrt(2*mp.mpf(t)*mp.mpf(L)); return 2*cB*s - 2*mp.log(1 + cB/2*s)
def rhs(t, L, d):
    t = mp.mpf(t); L = mp.mpf(L); d = mp.mpf(d); return d*L/2 + mp.log((4*t*t + d*d)*CB**2/(SLACK/2*d*d))
def margin(t, L, d): return lhs(t, L) - rhs(t, L, d)
# (a) monotonicity of the right side in delta
print("(a) d/d(delta) of the right side = L/2 + 2 delta/(4t^2 + delta^2) - 2/delta  >= L/2 - 2/delta  >= 0 for delta >= 4/L;")
worst = mp.inf
for L in (50, 87, 376, 403, 1000):
    for t in (3, 100, 1000, 1e6):
        for k in range(0, 1001):
            d = mp.mpf(25)/L + (mp.mpf(1)/2 - mp.mpf(25)/L)*k/1000
            worst = min(worst, mp.mpf(L)/2 + 2*d/(4*mp.mpf(t)**2 + d*d) - 2/d)
print(f"    numerical check on delta in [25/L, 1/2] (1001 points), L in (50, 87, 376, 403, 1000), t in (3, 100, 1e3, 1e6): min derivative = {mp.nstr(worst,5)} (> 0);  worst case of (R*) on the admissible range is delta = 1/2")
out["rhs_ddelta_min"] = float(worst)
# (b) monotonicity of the margin in t
print("(b) d(margin)/dt >= c_B sqrt(L/(2t)) - 8t/(4t^2 + delta^2) >= c_B sqrt(L/(2t)) - 2/t > 0 for t > 8/(c_B^2 L)  (left side: d/ds[2c_B s - 2log(1 + c_B s/2)] >= c_B, ds/dt = sqrt(L/(2t)))")
def t_mono(L): return 8/(cB**2*mp.mpf(L))
mono_ok = True
for L in (50, 87, 376, 403, 1000):
    tm = t_mono(L); ts = [tm*mp.mpf('1.02')**k for k in range(0, 700)]
    ms = [margin(t, L, mp.mpf(1)/2) for t in ts]
    mono_ok = mono_ok and all(ms[i+1] > ms[i] for i in range(len(ms)-1))
print(f"    numerical check (delta = 1/2, geometric t-grid from 8/(c_B^2 L) to ~1e6 x that, five L): margin strictly increasing: {mono_ok};  8/(c_B^2 L) = {mp.nstr(t_mono(50),4)} at L = 50, {mp.nstr(t_mono(1000),4)} at L = 1000")
out["margin_monotone_in_t"] = bool(mono_ok)
# (c) least t at delta = 1/2
def least_t(L, d=mp.mpf(1)/2):
    lo = max(t_mono(L), mp.mpf(3)); hi = mp.mpf(10)**9
    assert margin(lo, L, d) < 0 and margin(hi, L, d) > 0
    for _ in range(200):
        mid = (lo + hi)/2
        if margin(mid, L, d) >= 0: hi = mid
        else: lo = mid
    return hi
print("(c) least t with (R*) at delta = 1/2 (bisection; margin increasing in t beyond 8/(c_B^2 L), so (R*) holds for every t >= least t):")
tab = {}
for L in (50, 87, 100, 200, 376, 403, 1000, 10000):
    tl = least_t(L); tab[L] = float(tl)
    print(f"    L = {L:5d}: least t = {mp.nstr(tl,5)}  (ceil {int(mp.ceil(tl))};  t/L = {mp.nstr(tl/L,4)})   [referee F: 167 / 151 / -- / -- / 240 / 250 / 483 / --]")
out["least_t_at_delta_half"] = tab
ratio = 1/(128*cB**2)
print(f"    asymptotic ratio: 2 c_B sqrt(2tL) >= L/4  <=>  t/L >= 1/(128 c_B^2) = {mp.nstr(ratio,5)};  least t / L at L = 1e6: {mp.nstr(least_t(10**6)/10**6,5)}, at L = 1e8: {mp.nstr(least_t(10**8)/10**8,5)}")
out["t_over_L_asymptotic_Rstar"] = float(ratio)
print(f"    for the record: at the row's own delta the balance is t/L >= delta^2/(32 c_B^2): {mp.nstr(mp.mpf('0.01')/(32*cB**2),4)} at delta = 0.1;  least t at delta = 0.1: L = 376: {mp.nstr(least_t(376, mp.mpf('0.1')),5)}, L = 1000: {mp.nstr(least_t(1000, mp.mpf('0.1')),5)}")
out["least_t_at_delta_0p1"] = {376: float(least_t(376, mp.mpf('0.1'))), 1000: float(least_t(1000, mp.mpf('0.1')))}
# (d) the campaign's lines
def largest_L(t, d=mp.mpf(1)/2):
    # margin(t, L, d) is concave-ish in L for fixed t (sqrt L against L): find the upper crossing by bisection from a point where it is positive
    lo = mp.mpf(50); assert margin(t, lo, d) > 0
    hi = mp.mpf(10)**7; assert margin(t, hi, d) < 0
    for _ in range(200):
        mid = (lo + hi)/2
        if margin(t, mid, d) >= 0: lo = mid
        else: hi = mid
    return lo
print("(d) the campaign's lines: for fixed t, the largest L at which (R*) holds (delta = 1/2, the uniform form; and at the campaign's delta):")
camp = {}
for t in (1000, 10000):
    row = {"delta_half": float(largest_L(t))}
    line = f"    t = {t}: (R*) holds for L <= {mp.nstr(largest_L(t),5)} at delta = 1/2"
    for d in ('0.05', '0.1', '0.25'):
        row[f"delta_{d}"] = float(largest_L(t, mp.mpf(d))); line += f";  L <= {mp.nstr(largest_L(t, mp.mpf(d)),5)} at delta = {d}"
    print(line + f"   [the proved 21L form: L <= {mp.nstr(mp.mpf(t)/21,4)}]"); camp[t] = row
out["largest_L_inside_Rstar"] = camp
print("    CAMPAIGN.md section 5 record points (L = L*(delta, t; C1)), flag 'inside' = (L >= L*, which holds at L = L*) and the reflection part: 21L (record) -> (R*) at delta = 1/2 (uniform) -> (R*) at the row's delta:")
rows = [(1000, '0.05', '862.48', 1), (1000, '0.05', '2590.38', 2.4e9), (1000, '0.10', '375.79', 1), (1000, '0.10', '1239.74', 2.4e9), (1000, '0.25', '120.99', 1), (1000, '0.25', '466.57', 2.4e9),
        (10000, '0.05', '885.46', 1), (10000, '0.05', '2613.36', 2.4e9), (10000, '0.10', '387.28', 1), (10000, '0.10', '1251.23', 2.4e9), (10000, '0.25', '125.59', 1), (10000, '0.25', '471.17', 2.4e9)]
rec = []
for t, d, Ls, C1 in rows:
    Lm = mp.mpf(Ls); m_half = margin(t, Lm, mp.mpf(1)/2); m_own = margin(t, Lm, mp.mpf(d))
    old = mp.mpf(t) >= 21*Lm
    print(f"    t = {t:5d}, delta = {d}, L* = {Ls:8s} (C1 = {C1:.2g}): 21L: {'inside ' if old else 'OUTSIDE'};  (R*) delta=1/2: margin {mp.nstr(m_half,4):>8s} -> {'inside ' if m_half >= 0 else 'OUTSIDE'};  (R*) own delta: margin {mp.nstr(m_own,4):>8s} -> {'inside' if m_own >= 0 else 'OUTSIDE'}")
    rec.append(dict(t=t, delta=float(d), L=float(Ls), C1=C1, inside_21L=bool(old), margin_Rstar_half=float(m_half), inside_Rstar_half=bool(m_half >= 0), margin_Rstar_own=float(m_own), inside_Rstar_own=bool(m_own >= 0)))
out["campaign_record_points"] = rec
print(f"    check: L* = 375.8 at (0.1, 1e3) is inside since least t at L = 376 is {mp.nstr(least_t(376),4)} < 1e3")
# (e) the DH control
for (t, L, d, lab) in ((mp.mpf('85.7'), mp.mpf(87), mp.mpf('0.3085'), "referee F's rounding (85.7, 87, 0.3085)"), (mp.mpf('85.6993484854'), mp.mpf('86.907'), mp.mpf('0.3085171825'), "the log's values (85.6993, 86.907, 0.3085172)")):
    m = margin(t, L, d); m2 = margin(t, L, mp.mpf(1)/2)
    print(f"(e) DH control at {lab}: (R*) margin = {mp.nstr(m,5)} nats (referee F: -2.4)  -> (R*) FAILS at DH;  uniform form (delta = 1/2): {mp.nstr(m2,5)};  least t at L = {mp.nstr(L,5)}, delta = {mp.nstr(d,4)}: {mp.nstr(least_t(L, d),5)} against t = {mp.nstr(t,5)}")
    out.setdefault("DH", {})[lab] = dict(margin=float(m), margin_uniform=float(m2), least_t_own_delta=float(least_t(L, d)))
# (f) (R) implies (R*)
print("(f) (R) of section 4 implies (R*): RHS(R) - RHS(R*) = L - delta L/2 + 2 sqrt(delta L) + (3/2) log(delta L) - 2 kappa_- + log(1.35) > 0 on delta in [25/L, 1/2], L >= 50;  hence t >= 21L => (R') => (R) => (R*):")
worstd = mp.inf
for L in (50, 87, 100, 376, 403, 1000, 10000):
    for k in range(0, 1001):
        d = mp.mpf(25)/L + (mp.mpf(1)/2 - mp.mpf(25)/L)*k/1000
        worstd = min(worstd, L - d*L/2 + 2*mp.sqrt(d*L) + mp.mpf(3)/2*mp.log(d*L) - 2*kminus + mp.log(SLACK/2))
print(f"    min of RHS(R) - RHS(R*) over the grid: {mp.nstr(worstd,5)} (> 0);  margin of (R*) at t = 21L, delta = 1/2: L = 50: {mp.nstr(margin(21*50, 50, mp.mpf(1)/2),5)}, L = 1000: {mp.nstr(margin(21000, 1000, mp.mpf(1)/2),5)}")
out["R_implies_Rstar_min_gap"] = float(worstd)
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "rstar_table_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
