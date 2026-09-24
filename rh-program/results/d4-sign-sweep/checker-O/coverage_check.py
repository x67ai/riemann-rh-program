# coverage_check.py — Job 2 part A item (c): the coverage map re-derived from the page.
# Windows: Gourdon 2004 sect. 4.3.1 table (offsets read in prior-art/gourdon-...txt lines 1848-1859);
# Odlyzko 1992 Table 1.2 (PDF p. 140, page image) — ALL rows inside [PT, 1e20]: N = 1e14, 1e16, 1e18, 1e19, 1e20, 2e20;
# Odlyzko 2001 p. 3 (page image): 1,006,374,896 zeros from zero #13,048,994,265,258,476.
# Height of zero #n by inverting the Riemann-von Mangoldt main term N(T) = (T/2pi) log(T/2pi e) + 7/8 (error O(log T): a few
# zero spacings); every window is padded by 1000 spacings on each side, which dominates that error.
import json, mpmath as mp
mp.mp.dps = 40
def T_of(n):
    n = mp.mpf(n)
    f = lambda T: T/(2*mp.pi)*mp.log(T/(2*mp.pi*mp.e)) + mp.mpf(7)/8 - n
    T = 2*mp.pi*n/mp.log(n)
    return mp.findroot(f, T)
def sp(T): return 2*mp.pi/mp.log(T/(2*mp.pi))
W = []
for e, a, b in [(14, 3, 2*10**9), (15, 0, 2*10**9-1), (16, 1, 2*10**9-1), (17, 0, 2*10**9), (18, 1, 2*10**9-1), (19, 0, 2*10**9+1), (20, 4, 2*10**9-1)]:
    W.append(("Gourdon 2004 #1e%d" % e, 10**e + a, 10**e + b))
for N, cnt, off in [(10**14, 1685452, -736), (10**16, 16480973, -5946), (10**18, 16671047, -8839), (10**19, 16749725, -13607), (10**20, 175587726, -30769710), (2*10**20, 101305325, -633984)]:
    W.append(("Odlyzko 1992 Table 1.2 N=%g" % N, N + off, N + off + cnt - 1))
W.append(("Odlyzko 2001 p.3", 13048994265258476, 13048994265258476 + 1006374896 - 1))
PT = mp.mpf(3000175332800)
win = []
for name, n1, n2 in W:
    t1, t2 = T_of(n1), T_of(n2)
    pad = 1000*sp(t1)
    win.append(dict(src=name, n_first=n1, n_last=n2, t_lo=float(t1 - pad), t_hi=float(t2 + pad), width=float(t2 - t1)))
plan = json.load(open("../harness/sweep_plan.json"))
def inside(t):
    return [w["src"] for w in win if w["t_lo"] <= t <= w["t_hi"]]
t1hits = [(r["k"], r["t_exact"], inside(mp.mpf(r["t_exact"]))) for r in plan["tier1"]]
t1hits = [h for h in t1hits if h[2]]
t2 = [(r["t_exact"], inside(mp.mpf(r["t_exact"]))) for r in plan["tier2"]]
ctrl = [(r["t_exact"], inside(mp.mpf(r["t_exact"]))) for r in plan["tier1_controls"]]
# control 1e20 window: zero number at the control height
c = mp.mpf(15202440115920748544); z20 = mp.mpf("15202440115920747268.629029")
c2 = mp.mpf(2513274122900000); s01 = T_of(13048994265258476)
res = dict(windows=win, n_windows_in_range=sum(1 for w in win if w["t_hi"] >= PT and w["t_lo"] <= 1e20),
           tier1_heights_inside_any_window=t1hits, tier2=t2, controls=ctrl,
           control_1e20_zeros_above_zero_1e20=float((c - z20)/sp(c)),
           control_2p51e15_minus_RvM_start_t=float(c2 - s01), control_2p51e15_zeros_above_start=float((c2 - s01)/sp(c2)),
           job1_windows=[(w["t_lo"], w["t_hi"], w["zeros"][:40]) for w in plan["covered_windows"]])
json.dump(res, open("out/coverage_check.json", "w"), indent=1, default=str)
for w in win: print("%-34s t in [%.10e, %.10e] width %.3e" % (w["src"], w["t_lo"], w["t_hi"], w["width"]))
print("tier1 hits:", t1hits); print("tier2:", t2); print("controls:", ctrl)
print("control 1e20: zeros above #1e20 = %.1f" % res["control_1e20_zeros_above_zero_1e20"])
print("control 2.51e15: t - t(start) = %.4e, zeros above start %.3e" % (res["control_2p51e15_minus_RvM_start_t"], res["control_2p51e15_zeros_above_start"]))
