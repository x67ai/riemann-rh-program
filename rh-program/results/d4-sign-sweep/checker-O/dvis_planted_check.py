# dvis_planted_check.py — Job 2 part A items (d), (e): delta_vis with log t vs log(t/2pi) at every planned height,
# and one independent evaluation of the planted-orbit expected value -2 d^2 c(dL)^2, c(l) = int B(v) cosh(l v) dv.
import json, math, mpmath as mp
plan = json.load(open("../harness/sweep_plan.json"))
def Lsign(t, var):  # campaign law, anchored L_sign(0.1, 1e6) = 22.4
    f = (lambda x: math.log(x)) if var == "log" else (lambda x: math.log(x/(2*math.pi)))
    return 22.4*(f(t)/f(1e6))**(1/3)
def dvis(t, L, var): return 0.1*(Lsign(t, var)/L)**1.5
band = 1.5**1.5
pts = [(float(r["t_exact"]), 22.0) for r in plan["tier1"]] + [(float(r["t_exact"]), 22.0) for r in plan["tier1_controls"]] \
    + [(float(r["t_exact"]), 28.35) for r in plan["tier2"]] + [(1e12, 28.35), (1e6, 10.0), (1e6, 20.0), (1e12, 20.0)]
worst = 0; rows = []
for t, L in pts:
    a, b = dvis(t, L, "log"), dvis(t, L, "log2pi")
    r = max(a/b, b/a); worst = max(worst, r)
    rows.append((t, L, a, b, r, a/band <= b <= a*band))
print("planned points:", len(pts), " max ratio of the two variants: %.4f  (band factor 1.5^1.5 = %.4f); all inside: %s" % (worst, band, all(x[5] for x in rows)))
for t, L, a, b, r, ok in rows[:1] + rows[120:121] + rows[-10:]:
    print("t=%.6e L=%.2f dvis(log t)=%.4f dvis(log t/2pi)=%.4f ratio %.4f inside %s" % (t, L, a, b, r, ok))
# planted value, independent quadrature (mpmath tanh-sinh at 30 digits)
mp.mp.dps = 30
B = lambda v: mp.e**(-1/(1-4*v*v)) if abs(v) < 0.5 else mp.mpf(0)
Z = mp.quad(B, [-0.5, 0, 0.5])
def c(l): return mp.quad(lambda v: B(v)*mp.cosh(l*v), [-0.5, 0, 0.5])/Z
for d, L, job1 in [(0.09932473853704041, 28.35, -0.026808559547114343), (0.1, 28.35, -0.02728572337348855), (0.3085171824566374, 10, -0.274612193776558)]:
    v = -2*d*d*c(d*L)**2
    print("planted d=%.6f L=%.2f: -2d^2c(dL)^2 = %s  Job1 %.17g  diff %.2e" % (d, L, mp.nstr(v, 17), job1, float(v - job1)))
print("Z =", mp.nstr(Z, 17))
