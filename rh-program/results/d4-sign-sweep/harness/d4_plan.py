#!/usr/bin/env python3
"""d4_plan.py -- D4: the prior-art coverage windows (read at the page: prior-art/*.txt; the Odlyzko PDFs as page images -- 1992
PDF p. 4 (= p. 1), p. 8 (= p. 5) and p. 140 (Table 1.2); 2001 PDF p. 3), the tier-1 ladder t_k = 3 000 175 332 800 * 10^(k/16),
k = 0..120, as exact integer-valued doubles, the check that no ladder point falls inside a covered window, the tier-2 list and
the covered-range controls -> harness/sweep_plan.json; the GOVERNING eps_phi -> harness/eps_phi.json.
FIX PASS (Fri Sep 25 2026; CHECK-O-A.md items (b), (c); the v1 of this script is kept as d4_plan.v1.py):
  (b) eps_phi per unit t is the PROVEN a-priori bound 1.0266395604864687e-30 (checker-O/job1_ddlog_bound.py, bit-exact emulation
      of dd_log_u64: S1 error 4.250e-31 exact over all (k, idx) + the last dd add 3 * 2^-102 + the series cap 1e-32); the sampled
      maxima (6.392e-31 over 8 self-tests of 1000 n; Job 2's 6.686e-31 over 200 000 n) are kept beside it as measurements, not bounds.
      Every planned height carries its phase line eps * t * l1(L) (l1(28.35) = 146.95060754424162 exact from the (1e12, 28.35) run;
      l1(22) = the PNT estimate (2/L^2) int_0^1 e^{Lv/2} |A(v)| dv, replaced by the exact printed l1 when the first tier-1 point lands)
      and is REFUSED when the line exceeds 1e-8: t_ceil(28.35) = 6.63e19, t_ceil(22) = 4.47e20. The tier-2 point 1e20 (line 1.51e-8)
      is refused and REPLACED by ladder k = 117, t = 61609351296641974272 (line 9.30e-9); k = 118 (1.07e-8) is refused.
  (c) the coverage map has FOURTEEN windows: Odlyzko 1992 Table 1.2 (PDF p. 140; p. 5 for the reading of the entries) lists eight
      sets, of which N = 1e14, 1e16, 1e18, 1e19, 1e20, 2e20 lie in [PT, 1e20] (N = 1e6, 1e12 lie below PT); the 1e20 and 2e20 windows
      are now the page's exact zero-number ranges (the v1 windows +-176e6 / +-101e6 spacings contained them and are superseded).
Heights of the n-th zero by the Riemann-von Mangoldt main term N(t) = (t/2pi) log(t/(2 pi e)) + 7/8 (error O(log t) zeros, i.e.
a few units of t: irrelevant against windows 1e5-4e8 wide); every window padded by 100 in t on both sides."""
import json, math, subprocess, glob, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
PT = 3000175332800
EPS_PROVEN = 1.0266395604864687e-30       # checker-O/out/job1_ddlog_bound.json "eps_apriori_rigorous_per_t"
L1_2835 = 146.95060754424162              # out/sum_zeta_t1000000000000_L28.35.json l1_norm (exact, printed by the run)
ALLOW = 1e-8
def t_of_zero(n):
    T = 2*math.pi*n/math.log(n)
    for _ in range(200): T = 2*math.pi*(n - 7/8)/math.log(T/(2*math.pi*math.e))
    return T
sp = lambda T: 2*math.pi/math.log(T/(2*math.pi))
# l1(L) PNT estimate, as d4_point.py's pre-check computes it (M6 section 6)
M = 4096; w = np.arange(1, M)/M - 0.5
def braw(x):
    with np.errstate(all='ignore'): r = np.exp(-1.0/(1.0 - 4.0*x*x))
    return np.where(np.abs(x) < 0.5, np.nan_to_num(r), 0.0)
def braw_d1(x):
    with np.errstate(all='ignore'): q = 1.0 - 4.0*x*x; r = braw(x)*(-8.0*x/(q*q))
    return np.where(np.abs(x) < 0.5, np.nan_to_num(r), 0.0)
Z = braw(w).sum()/M
def A_of(v): return float(np.sum(braw_d1(w)*braw_d1(w - v))/M)/(Z*Z)
vs = np.linspace(0, 1, 2001); Av = np.array([A_of(v) for v in vs])
def l1_est(L): return float(2.0/L**2*np.trapezoid(np.exp(L*vs/2)*np.abs(Av), vs))
L1 = {22: l1_est(22.0), 28.35: L1_2835}
def line(t, L): return EPS_PROVEN*float(t)*L1[L]
win = []
gourdon = {14: (3, 2e9), 15: (0, 2e9 - 1), 16: (1, 2e9 - 1), 17: (0, 2e9), 18: (1, 2e9 - 1), 19: (0, 2e9 + 1), 20: (4, 2e9 - 1)}   # table 4.3.1, text lines 1848-1859
for n, (o1, o2) in gourdon.items():
    a = t_of_zero(10**n + o1); b = t_of_zero(10**n + o2)
    win.append(dict(t_lo=a - 100, t_hi=b + 100, zeros=f"#10^{n}+{o1} .. #10^{n}+{int(o2)}", rigor="non-rigorous (statistics run; Z(t) to ~1e-9, section 4.1)", source="Gourdon 2004 sect. 4.3.1 table (prior-art/gourdon-2004-zetazeros1e13-1e24.txt lines 1848-1859); t by the R-vM main term +-100"))
T = 2.51327412288e15
win.append(dict(t_lo=T - 1e4, t_hi=t_of_zero(13048994265258476 + 1006374896) + 1e4, zeros="#13,048,994,265,258,476 .. +1,006,374,896", rigor="'not entirely rigorously' (p.2, of the 1e22 set; the same algorithms)", source="Odlyzko 2001, Contemp. Math. 290, p.3 (prior-art/odlyzko-2001-zeta-10to22.pdf page 3): 1,006,374,896 zeros from zero #13,048,994,265,258,476 at height ~2.51327412288e15"))
# Odlyzko 1992 Table 1.2 (PDF p. 140), read as on the page: "N | zeros | first"; p. 5: "starting with zero number N - a, ending with N + b"
odl92 = [(10**14, 1685452, 736), (10**16, 16480973, 5946), (10**18, 16671047, 8839), (10**19, 16749725, 13607), (10**20, 175587726, 30769710), (2*10**20, 101305325, 633984)]
g20 = 15202440115920747268.6290299
for N, cnt, a in odl92:
    first = N - a; last = first + cnt - 1
    lo = t_of_zero(first); hi = t_of_zero(last)
    if N == 10**20:   # anchor on the page's own value of the 1e20-th zero (p. 1) rather than the main term
        lo = g20 - a*sp(g20); hi = g20 + (cnt - 1 - a)*sp(g20)
    win.append(dict(t_lo=lo - 100, t_hi=hi + 100, zeros=f"#{N:d}-{a:,} .. #{N:d}+{cnt-1-a:,} ({cnt:,} zeros)", rigor="'not entirely rigorous due to incomplete control of roundoff errors' (Preface)",
                    source=f"Odlyzko 1992 (unpublished manuscript, author's site) Table 1.2 (PDF p. 140) and p. 5 (PDF p. 8); {'p. 1: the 1e20-th zero = 1/2 + i 15202440115920747268.6290299...; ' if N == 10**20 else ''}t by the R-vM main term +-100"))
ladder = []
for k in range(0, 121):
    td = float(round(PT * 10**(k/16))); ti = int(td); assert float(ti) == td
    hits = [w['zeros'][:24] for w in win if w['t_lo'] <= td <= w['t_hi']]
    ln = line(td, 22)
    ladder.append(dict(k=k, t_exact=str(ti), log10=round(math.log10(td), 4), in_covered_window=hits, phase_line_L22=ln, accepted=ln <= ALLOW))
inwin = [l for l in ladder if l['in_covered_window']]
refused_t1 = [l for l in ladder if not l['accepted']]
ctrl20 = "15202440115920748544"      # the double one ulp (2048) above the nearest one: +1275.4 above the 1e20-th zero (8 592 zeros above it)
assert float(int(ctrl20)) == float(ctrl20) and str(int(float(ctrl20))) == ctrl20 and float(ctrl20) - g20 > 0
k117 = ladder[117]['t_exact']; assert k117 == "61609351296641974272"
tier2 = [dict(t_exact="3000175332900", role="PT-edge point (rehearsal; landed, PASS by Job 2)"), dict(t_exact="100000000000000", role="1e14"), dict(t_exact="10000000000000000", role="1e16"),
         dict(t_exact="1000000000000000000", role="1e18"),
         dict(t_exact=ctrl20, role="covered-range control: the double 1275.4 above the 1e20-th zero (8 592 zeros above it): inside Odlyzko 1992's set #1e20-30,769,710 .. #1e20+144,818,015 (Table 1.2) and inside Gourdon 2004's window #1e20+4 .. #1e20+2e9-1"),
         dict(t_exact=k117, role="the ceiling: ladder k = 117, the largest planned height whose phase line at eps_proven is <= 1e-8 (9.30e-9); replaces 1e20 (line 1.51e-8, REFUSED; CHECK-O-A (b)); k = 118 (1.07e-8) is refused")]
for p in tier2: p['phase_line_L28.35'] = line(p['t_exact'], 28.35); p['accepted'] = p['phase_line_L28.35'] <= ALLOW
refused_t2_1e20 = {'t_exact': "100000000000000000000", 'phase_line_L28.35': line("100000000000000000000", 28.35), 'accepted': False, 'role': "REFUSED at eps_proven (was the v1 tier-2 ceiling)"}
controls_t1 = [dict(t_exact="2513274122900000", role="covered-range control, tier 1 (L = 22): inside Odlyzko 2001's window (published, Contemp. Math. 290), 2.0e4 in t (about 1.07e5 zeros) above the window's 12-digit start 2.51327412288e15"),
               dict(t_exact=ctrl20, role="covered-range control, tier 1 (L = 22): the 1e20-th zero window (Odlyzko 1992 Table 1.2; Gourdon 2004)")]
for p in controls_t1: p['phase_line_L22'] = line(p['t_exact'], 22); p['accepted'] = p['phase_line_L22'] <= ALLOW
for p in tier2 + controls_t1: assert str(int(float(p['t_exact']))) == p['t_exact'], p
assert all(p['accepted'] for p in tier2 + controls_t1) and not refused_t1
tot = sum(w['t_hi'] - w['t_lo'] for w in win)
d = subprocess.run(['date'], capture_output=True, text=True).stdout.strip()
t_ceil = {L: ALLOW/(EPS_PROVEN*L1[L]) for L in L1}
json.dump(dict(date=d, fix_pass="CHECK-O-A.md items (b), (c) applied; v1 plan of Fri Sep 25 01:16:00 IST 2026 superseded", PT_height=PT, ceiling_nominal=1e20,
               eps_phi_per_t_proven=EPS_PROVEN, l1_used={str(k): v for k, v in L1.items()}, t_ceil={str(k): v for k, v in t_ceil.items()}, phase_line_allowance=ALLOW,
               covered_windows=win, covered_measure_in_t=tot, covered_fraction=tot/(1e20 - PT), tier1_L=22, tier1=ladder, tier1_points_inside_covered_windows=len(inwin), tier1_refused=len(refused_t1),
               tier1_controls=controls_t1, tier2_L=28.35, tier2=tier2, tier2_refused=[refused_t2_1e20]), open(os.path.join(HERE, 'sweep_plan.json'), 'w'), indent=1)
# the governing eps: the proven bound; the sampled maxima kept beside it
eps = {}
for f in glob.glob(os.path.join(HERE, '..', 'out', '*.selftest.json')):
    j = json.load(open(f)); eps[os.path.basename(f)] = (j['X'], j['eps_phi_per_t_measured'])
emax = max(v[1] for v in eps.values())
json.dump(dict(eps_phi_per_t=EPS_PROVEN,
               basis="PROVEN a-priori bound on the dd log of harness/d4_twisted_sum.rs (dd_log_u64): checker-O/job1_ddlog_bound.py (CHECK-O-A.md section 2(b)) -- bit-exact emulation (0 mismatches on 205 000 rows); S1 = ln2_dd*k + logm0[idx] error computed exactly over all (k, idx): 4.249938815707099e-31; the last dd add <= 3*2^-102 = 5.916e-31; the log1p series capped at 1e-32 (measured 1.4e-34): total 1.0266395604864687e-30 per unit t. The product-and-reduction path adds <= 1.3e-26 rad at 1e20 (< 1e-46 t). BINDING for every phase line, refusal and Control-1 tolerance (fix (b), applied Job 1 fix pass).",
               measured_sample_max=dict(job1_1000n_x8_selftests=emax, job2_200000n_at_1e20=6.686e-31, note="sample maxima over the n sampled, NOT bounds; kept as measurements beside the proven figure"),
               per_selftest=eps, retired=dict(brief_constant=2.2e-31, v1_sampled=6.392019332313393e-31, v1_apriori_estimate=2.1e-30),
               t_ceil={str(k): v for k, v in t_ceil.items()}, l1_used={str(k): v for k, v in L1.items()}, date=d), open(os.path.join(HERE, 'eps_phi.json'), 'w'), indent=1)
print(f"[{d}] FIX PASS plan: ladder 121 points {ladder[0]['t_exact']} .. {ladder[-1]['t_exact']}; inside a covered window: {len(inwin)}; refused at eps_proven: {len(refused_t1)} (largest line {max(l['phase_line_L22'] for l in ladder):.3e}); covered measure {tot:.3e} of {1e20-PT:.3e} (fraction {tot/(1e20-PT):.1e}) over {len(win)} windows")
print(f"  eps_proven = {EPS_PROVEN:.6e}; l1(22) est = {L1[22]:.4f}, l1(28.35) = {L1[28.35]:.6f}; t_ceil(22) = {t_ceil[22]:.3e}, t_ceil(28.35) = {t_ceil[28.35]:.3e}; sampled max = {emax:.4e} over {len(eps)} self-tests")
for p in tier2 + [refused_t2_1e20]: print(f"  tier 2  t = {p['t_exact']:>22}  line {p['phase_line_L28.35']:.3e}  {'accepted' if p['accepted'] else 'REFUSED'}  {p['role'][:60]}")
for p in controls_t1: print(f"  tier 1 control t = {p['t_exact']:>22}  line {p['phase_line_L22']:.3e}  {'accepted' if p['accepted'] else 'REFUSED'}")
for w in win: print(f"  [{w['t_lo']:.6e}, {w['t_hi']:.6e}] width {w['t_hi']-w['t_lo']:.2e}  {w['zeros'][:60]}")
