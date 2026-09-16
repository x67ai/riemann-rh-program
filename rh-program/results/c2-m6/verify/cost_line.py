#!/usr/bin/env python3
"""cost_line.py -- M6 rung 1, the cost line (C): the sign channel's term count and wall time on THIS machine at the twelve
campaign points (L_sign(delta, t) at t and the ensemble median over centers, from results/c2-m2/campaign/summary_<tag>.json),
with the feasibility class A/B/C.

Cost model, from the MEASURED runs of twisted_sum (out/zeta_t85p7_L20_th1.json, out/zeta_t85p7_L20_sieveonly_th1.json,
out/zeta_t85p7_L20_th8.json, out/zeta_t85p7_L20_sieveonly_th8.json; X = e^20 = 4.85e8, 25 617 272 terms):
   wall(X) = [ N_terms(X) * r_term + X * r_sieve ] / S,
   r_sieve = (sieve-only single-thread time)/X,  r_term = (full single-thread time - sieve-only time)/N_terms,
   S = the measured 8-thread speed-up of the full run,  N_terms(X) = li(X) + (prime powers, li(sqrt X) + ...) ~ li(X).
The sieve cost per integer is taken constant in X (a segmented sieve's cost per integer grows like log log X; at X <= 1e17
that is a factor < 1.3 over X = 5e8 and is absorbed by rounding the classes); the per-term cost is constant by construction.
Classes (this file's definition, stated): A = wall <= 1 hour on this machine; B = 1 hour < wall <= 24 hours; C = wall > 24 hours
(beyond one slot).  Memory: a segmented sieve needs the base primes to sqrt X only (X = 1e17: 2.3e7 primes, 180 MB), so
memory is never the wall; the DH coefficient side (a full Lambda_DH array, 8 bytes per integer) is memory-bound at
X ~ 2.5e9 on 24 GiB and is NOT the object of the cost line (the cost line prices the channel on zeta).
"""
import json, math, os, datetime
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ld = lambda f: json.load(open(os.path.join(HERE, 'out', f)))
full1 = ld('zeta_t85p7_L20_th1.json'); sv1 = ld('zeta_t85p7_L20_sieveonly_th1.json')
full8 = ld('zeta_t85p7_L20_th8.json'); sv8 = ld('zeta_t85p7_L20_sieveonly_th8.json')
X0 = full1['X']; N0 = full1['n_terms']
r_sieve = sv1['time_sum_s']/X0
r_term = (full1['time_sum_s'] - sv1['time_sum_s'])/N0
S = full1['time_sum_s']/full8['time_sum_s']
print(f"[{now()}] measured at X = {X0} ({N0} terms): single-thread full {full1['time_sum_s']:.3f}s, sieve-only {sv1['time_sum_s']:.3f}s -> "
      f"r_sieve = {r_sieve*1e9:.2f} ns/integer, r_term = {r_term*1e9:.1f} ns/term; 8 threads: full {full8['time_sum_s']:.3f}s (speed-up S = {S:.2f}), sieve-only {sv8['time_sum_s']:.3f}s")
model_check = (N0*r_term + X0*r_sieve)/S
print(f"[{now()}] model check at X0: predicted 8-thread wall {model_check:.3f}s vs measured {full8['time_sum_s']:.3f}s")

def n_terms(X):   # li(X) + prime powers ~ li(sqrt X) + li(X^(1/3)) ...
    tot = float(mp.li(X))
    k = 2
    while X**(1.0/k) > 2: tot += float(mp.li(X**(1.0/k))); k += 1
    return tot
def wall(X):
    return (n_terms(X)*r_term + X*r_sieve)/S
def cls(wsec):
    return 'A' if wsec <= 3600 else ('B' if wsec <= 86400 else 'C')
def fmt(wsec):
    if wsec < 60: return f"{wsec:.1f} s"
    if wsec < 3600: return f"{wsec/60:.1f} min"
    if wsec < 86400: return f"{wsec/3600:.1f} h"
    if wsec < 86400*365: return f"{wsec/86400:.1f} d"
    return f"{wsec/86400/365:.1f} y"

camp = {}
for tag, t in [('t1e3', 1e3), ('t1e4', 1e4), ('t1e5', 1e5), ('t1e6', 1e6)]:
    s = json.load(open(os.path.join(HERE, '..', '..', 'c2-m2', 'campaign', f'summary_{tag}.json')))
    camp[t] = s
# the ensemble medians: CAMPAIGN.md section 2 prints them; find them in summary['ensemble']['per_delta']
def median_L_sign(s, dl):
    pd = s['ensemble']['per_delta']
    for key in (dl, str(float(dl)), f"{float(dl):g}"):
        if key in pd:
            e = pd[key]
            for k2 in ('L_sign_median', 'median_L_sign', 'L_sign'):
                if k2 in e:
                    v = e[k2]
                    return v['median'] if isinstance(v, dict) and 'median' in v else v
    return None
rows = []
print(f"[{now()}] the cost line at the twelve campaign points (L_sign at t | median over centers -> X, terms, wall on this machine, class):")
for t in (1e3, 1e4, 1e5, 1e6):
    for dl in ('0.05', '0.1', '0.25'):
        Ls = camp[t]['derived'][dl]['L_sign']; Lm = median_L_sign(camp[t], dl)
        r = dict(t=t, delta=float(dl), L_sign_at_t=Ls, L_sign_median=Lm)
        for lab, L in (('at_t', Ls), ('median', Lm)):
            if L is None: continue
            X = math.exp(L); N = n_terms(X); w = wall(X)
            r[lab] = dict(L=L, X=X, terms=N, wall_s=w, wall=fmt(w), cls=cls(w))
        rows.append(r)
        a = r['at_t']; m = r.get('median')
        print(f"   t={t:8.0e} delta={float(dl):5.2f}: L_sign at t = {Ls:5.1f} -> X = {a['X']:.2e}, terms = {a['terms']:.2e}, wall = {a['wall']:>9}, class {a['cls']}"
              + (f"   | median {Lm:5.1f} -> X = {m['X']:.2e}, wall = {m['wall']:>9}, class {m['cls']}" if m else "   | median: not found in summary"))
# reference lines: the class boundaries in L and X for this machine; the pricing's boundaries (X = 1e9, 1e13) for comparison
def L_for_wall(target):
    lo, hi = 5.0, 60.0
    for _ in range(80):
        mid = (lo + hi)/2
        if wall(math.exp(mid)) < target: lo = mid
        else: hi = mid
    return lo
LA = L_for_wall(3600); LB = L_for_wall(86400); LY = L_for_wall(86400*365)
print(f"[{now()}] class boundaries on this machine: A/B at L = {LA:.2f} (X = {math.exp(LA):.2e}, terms {n_terms(math.exp(LA)):.2e}); B/C at L = {LB:.2f} (X = {math.exp(LB):.2e}, terms {n_terms(math.exp(LB)):.2e}); one year at L = {LY:.2f} (X = {math.exp(LY):.2e})")
for X in (1e9, 1e13, 1e15):
    print(f"   pricing's reference X = {X:.0e}: terms {n_terms(X):.2e}, wall {fmt(wall(X))} (class {cls(wall(X))}) -- PRICING section 3(a) priced 'X terms at 50 ns/term'; the term count is li(X), a factor ln X smaller, and the sieve is the other cost")
out = dict(date=now(), measured=dict(X0=X0, N0=N0, full_th1_s=full1['time_sum_s'], sieve_th1_s=sv1['time_sum_s'], full_th8_s=full8['time_sum_s'], sieve_th8_s=sv8['time_sum_s'],
           r_sieve_ns=r_sieve*1e9, r_term_ns=r_term*1e9, speedup8=S, model_check_th8_s=model_check),
           classes=dict(A='wall <= 1 h', B='1 h < wall <= 24 h', C='wall > 24 h', L_AB=LA, X_AB=math.exp(LA), L_BC=LB, X_BC=math.exp(LB), L_year=LY, X_year=math.exp(LY)),
           rows=rows, pricing_refs={f"{X:.0e}": dict(terms=n_terms(X), wall_s=wall(X), cls=cls(wall(X))) for X in (1e9, 1e13, 1e15)})
json.dump(out, open(os.path.join(HERE, 'out', 'cost_line.json'), 'w'), indent=1)
print(f"[{now()}] wrote out/cost_line.json")
