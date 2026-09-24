#!/usr/bin/env python3
"""d4_plan.py -- D4: the prior-art coverage windows (read at the page, prior-art/*.txt and the Odlyzko PDFs' pages 1-3, 9-15, 66-67),
the tier-1 ladder t_k = 3 000 175 332 800 * 10^(k/16), k = 0..120, as exact integer-valued doubles, the check that no ladder point
falls inside a covered window, the tier-2 list and the covered-range controls -> harness/sweep_plan.json; the measured eps_phi
-> harness/eps_phi.json (from the self-test sidecars).  Heights of the n-th zero by the Riemann-von Mangoldt main term
N(t) = (t/2pi) log(t/(2 pi e)) + 7/8 (error O(log t) zeros, i.e. a few units of t: irrelevant against windows 1e7-4e8 wide)."""
import json, math, subprocess, glob, os
HERE = os.path.dirname(os.path.abspath(__file__))
PT = 3000175332800
def t_of_zero(n):
    T = 2*math.pi*n/math.log(n)
    for _ in range(200): T = 2*math.pi*(n - 7/8)/math.log(T/(2*math.pi*math.e))
    return T
sp = lambda T: 2*math.pi/math.log(T/(2*math.pi))
gourdon = {14: (3, 2e9), 15: (0, 2e9 - 1), 16: (1, 2e9 - 1), 17: (0, 2e9), 18: (1, 2e9 - 1), 19: (0, 2e9 + 1), 20: (4, 2e9 - 1)}   # table 4.3.1, text lines 1848-1859
win = []
for n, (o1, o2) in gourdon.items():
    a = t_of_zero(10**n + o1); b = t_of_zero(10**n + o2)
    win.append(dict(t_lo=a - 100, t_hi=b + 100, zeros=f"#10^{n}+{o1} .. #10^{n}+{int(o2)}", rigor="non-rigorous (statistics run; Z(t) to ~1e-9, section 4.1)", source="Gourdon 2004 sect. 4.3.1 table (prior-art/gourdon-2004-zetazeros1e13-1e24.txt lines 1848-1859); t by the R-vM main term +-100"))
T = 2.51327412288e15
win.append(dict(t_lo=T - 1e4, t_hi=t_of_zero(13048994265258476 + 1006374896) + 1e4, zeros="#13,048,994,265,258,476 .. +1,006,374,896", rigor="'not entirely rigorously' (p.2, of the 1e22 set; the same algorithms)", source="Odlyzko 2001, Contemp. Math. 290, p.3 (prior-art/odlyzko-2001-zeta-10to22.pdf page 3): 1,006,374,896 zeros from zero #13,048,994,265,258,476 at height ~2.51327412288e15"))
g20 = 15202440115920747268.6290299
win.append(dict(t_lo=g20 - 1.76e8*sp(g20), t_hi=g20 + 1.76e8*sp(g20), zeros="~176 million zeros near #1e20 (window taken as +-176e6 mean spacings around the 1e20-th zero: wider than any reading of 'near')", rigor="'not entirely rigorous due to incomplete control of roundoff errors' (Preface)", source="Odlyzko 1992 (unpublished manuscript, author's site) p.1: the 1e20-th zero = 1/2 + i 15202440115920747268.6290299..."))
T2 = t_of_zero(2*10**20)
win.append(dict(t_lo=T2 - 1.01e8*sp(T2), t_hi=T2 + 1.01e8*sp(T2), zeros="over 101 million zeros near #2e20 (+-101e6 spacings)", rigor="as above", source="Odlyzko 1992 p.1; t of zero #2e20 = %.6e by the R-vM main term" % T2))
ladder = []
for k in range(0, 121):
    td = float(round(PT * 10**(k/16))); ti = int(td); assert float(ti) == td
    hits = [w['zeros'][:24] for w in win if w['t_lo'] <= td <= w['t_hi']]
    ladder.append(dict(k=k, t_exact=str(ti), log10=round(math.log10(td), 4), in_covered_window=hits))
inwin = [l for l in ladder if l['in_covered_window']]
ctrl20 = "15202440115920748544"      # the double one ulp (2048) above the nearest one: +1275.4 above the 1e20-th zero (~8 600 zeros above it)
assert float(int(ctrl20)) == float(ctrl20) and str(int(float(ctrl20))) == ctrl20 and float(ctrl20) - g20 > 0
tier2 = [dict(t_exact="3000175332900", role="PT-edge point (rehearsal)"), dict(t_exact="100000000000000", role="1e14"), dict(t_exact="10000000000000000", role="1e16"),
         dict(t_exact="1000000000000000000", role="1e18"), dict(t_exact=ctrl20, role="covered-range control: the double 1275.4 above the 1e20-th zero (about 8 600 zeros above it): inside Odlyzko 1992's ~176-million-zero set and inside Gourdon 2004's window #1e20+4 .. #1e20+2e9-1"),
         dict(t_exact="100000000000000000000", role="the ceiling 1e20 (run only if its phase line with the measured eps is <= 1e-8; else the largest accepted ladder height replaces it)")]
controls_t1 = [dict(t_exact="2513274122900000", role="covered-range control, tier 1 (L = 22): inside Odlyzko 2001's window (published, Contemp. Math. 290)"),
               dict(t_exact=ctrl20, role="covered-range control, tier 1 (L = 22): the 1e20-th zero window (Odlyzko 1992; Gourdon 2004)")]
for p in tier2 + controls_t1: assert str(int(float(p['t_exact']))) == p['t_exact'], p
tot = sum(w['t_hi'] - w['t_lo'] for w in win)
d = subprocess.run(['date'], capture_output=True, text=True).stdout.strip()
json.dump(dict(date=d, PT_height=PT, ceiling=1e20, covered_windows=win, covered_measure_in_t=tot, covered_fraction=tot/(1e20 - PT), tier1_L=22, tier1=ladder, tier1_points_inside_covered_windows=len(inwin), tier1_controls=controls_t1, tier2_L=28.35, tier2=tier2), open(os.path.join(HERE, 'sweep_plan.json'), 'w'), indent=1)
# measured eps from the self-test sidecars
eps = {}
for f in glob.glob(os.path.join(HERE, '..', 'out', '*.selftest.json')):
    j = json.load(open(f)); eps[os.path.basename(f)] = (j['X'], j['eps_phi_per_t_measured'])
emax = max(v[1] for v in eps.values())
json.dump(dict(eps_phi_per_t=emax, per_selftest=eps, basis="maximum over the self-tests on disk of max|phase error|/t (1000 pseudo-random n <= X each, mpmath at 50 digits); the product-and-reduction path adds <= 7.3e-27 rad at 1e20 (< 1e-46 t). A priori worst case of the dd arithmetic at |log n| <= 28.35: about 3 x 2^-105 x 28.35 = 2.1e-30 (a bound, not a measurement).", date=d), open(os.path.join(HERE, 'eps_phi.json'), 'w'), indent=1)
print(f"[{d}] ladder 121 points {ladder[0]['t_exact']} .. {ladder[-1]['t_exact']}; inside a covered window: {len(inwin)}; covered measure {tot:.3e} of {1e20-PT:.3e} (fraction {tot/(1e20-PT):.1e}); eps_phi measured max = {emax:.4e} over {len(eps)} self-tests")
for w in win: print(f"  [{w['t_lo']:.6e}, {w['t_hi']:.6e}] width {w['t_hi']-w['t_lo']:.2e}  {w['zeros'][:44]}")
