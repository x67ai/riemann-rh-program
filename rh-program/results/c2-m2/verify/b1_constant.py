#!/usr/bin/env python3
"""b1_constant.py -- b1 := sup_eta |eta Bhat(eta)|^2 for the normalized bump B(v) = Z^{-1} exp(-1/(1-4v^2)) on |v|<1/2,
with a CERTIFIED upper bound (grid maximum + Lipschitz increment; tail by ||B''||_1/eta), the maximizer eta*,
and the L^1 norms ||B'||_1, ||B''||_1, ||B'''||_1 (used by clause 4's polynomial tail, tx_032 (iii)).
Convention: Bhat(eta) = int B(v) e^{i eta v} dv = int B(v) cos(eta v) dv (B even, real).
Budget: < 10 min."""
import time, json, sys
import mpmath as mp
t0 = time.time(); mp.mp.dps = 30
out = {}
def Braw(v):
    v = mp.mpf(v)
    if abs(v) >= mp.mpf(1)/2: return mp.mpf(0)
    return mp.e**(-1/(1-4*v*v))
Z = mp.quad(Braw, [-0.5, -0.25, 0, 0.25, 0.5]); out["Z"] = float(Z)
B = lambda v: Braw(v)/Z
print(f"Z = {mp.nstr(Z, 15)}")
def Bhat(eta):
    eta = mp.mpf(eta)
    return mp.quad(lambda v: B(v)*mp.cos(eta*v), [-0.5, -0.25, 0, 0.25, 0.5])
# derivatives of B on (-1/2, 1/2): phi = -1/(1-4v^2), B = e^phi / Z
def phi(v): return -1/(1-4*v*v)
def dB(v, k):
    v = mp.mpf(v)
    if abs(v) >= mp.mpf(1)/2 - mp.mpf('1e-12'): return mp.mpf(0)
    return mp.diff(lambda x: mp.e**phi(x), v, k)/Z
# L1 norms: locate sign changes of B^{(k)} on (0, 1/2) by scanning, then integrate |.| piecewise
def l1norm(k, n=400):
    xs = [mp.mpf(i)/(2*n) for i in range(0, n+1)]   # 0 .. 1/2
    vals = [dB(x, k) for x in xs]
    roots = []
    for i in range(n):
        if vals[i]*vals[i+1] < 0:
            roots.append(mp.findroot(lambda x: dB(x, k), (xs[i], xs[i+1]), solver='illinois'))
    pts = [mp.mpf(0)] + roots + [mp.mpf(1)/2]
    total = mp.mpf(0)
    for a, b in zip(pts[:-1], pts[1:]):
        total += abs(mp.quad(lambda x: dB(x, k), [a, b]))
    return 2*total, [float(r) for r in roots]   # even/odd symmetry: |B^{(k)}| is even
norms = {}
for k in (1, 2, 3):
    nk, rk = l1norm(k)
    norms[k] = float(nk); out[f"norm_B{k}_L1"] = float(nk); out[f"signchanges_B{k}_on_(0,1/2)"] = rk
    print(f"||B^({k})||_1 = {mp.nstr(nk, 12)}   sign changes on (0,1/2): {[round(r,6) for r in rk]}")
m1 = mp.quad(lambda v: abs(v)*B(v), [-0.5, 0, 0.5]); out["m1_int_abs_v_B"] = float(m1)
print(f"int |v| B(v) dv = {mp.nstr(m1, 10)}   (so |d/deta (eta Bhat)| <= 1 + eta*m1)")
# certified sup of F(eta) := |eta Bhat(eta)| on [0, 40]: coarse grid h=0.01, then refine around the max with h=1e-5
def F(eta): return abs(eta*Bhat(eta))
h = mp.mpf('0.01'); grid = [i*h for i in range(0, 4001)]
Fv = [F(e) for e in grid]
imax = max(range(len(Fv)), key=lambda i: Fv[i]); eta_c = grid[imax]
print(f"coarse grid max: F = {mp.nstr(Fv[imax], 10)} at eta = {mp.nstr(eta_c, 6)}")
# certified bound over cells: F(eta) <= max(F(a),F(b)) + (h/2)*Lip(b), Lip(x) = 1 + x*m1 (derivative bound of eta*Bhat)
cert_coarse = max(max(Fv[i], Fv[i+1]) + (h/2)*(1 + grid[i+1]*m1) for i in range(4000))
print(f"certified sup over [0,40] from the coarse grid: F <= {mp.nstr(cert_coarse, 8)}")
# refine on [eta_c - 0.02, eta_c + 0.02] with h2 = 1e-5 (4001 points) -- only needed to sharpen the certificate near the max
h2 = mp.mpf('1e-5'); g2 = [eta_c - mp.mpf('0.02') + i*h2 for i in range(0, 4001)]
F2 = [F(e) for e in g2]
j = max(range(len(F2)), key=lambda i: F2[i]); eta_star = g2[j]; Fstar = F2[j]
cert_fine = max(max(F2[i], F2[i+1]) + (h2/2)*(1 + g2[i+1]*m1) for i in range(4000))
# outside the refined interval the coarse certificate applies cell by cell
cert_out = max(max(Fv[i], Fv[i+1]) + (h/2)*(1 + grid[i+1]*m1) for i in range(4000) if grid[i+1] <= eta_c - mp.mpf('0.02') or grid[i] >= eta_c + mp.mpf('0.02'))
cert = max(cert_fine, cert_out)
# tail eta >= 40: |eta Bhat(eta)| <= ||B''||_1 / eta
tail = mp.mpf(norms[2])/40
print(f"refined: F* = {mp.nstr(Fstar, 12)} at eta* = {mp.nstr(eta_star, 8)};  certified sup on [0,40]: {mp.nstr(cert, 10)};  tail bound for eta >= 40: ||B''||_1/40 = {mp.nstr(tail, 6)}")
b1 = Fstar**2; b1_cert = max(cert, tail)**2
out["eta_star"] = float(eta_star); out["b1_computed"] = float(b1); out["b1_certified_upper"] = float(b1_cert)
out["norm_Bprime_sq"] = norms[1]**2
print(f"b1 = sup|eta Bhat|^2 = {mp.nstr(b1, 10)} (computed)   <= {mp.nstr(b1_cert, 8)} (certified)   ;  ||B'||_1^2 = {norms[1]**2:.5f} (tx_032's bound)")
# pricing cross-check: the pricing's grid (step 0.005 on [gmax-0.5, gmax+0.5]) gave 8.64612 at 4.675
print(f"pricing value 8.646123549211879 at 4.675 -- difference from this run's computed b1: {float(b1) - 8.646123549211879:.3e}")
out["runtime_s"] = time.time() - t0
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "b1_constant_out.json", "w"), indent=1)
print(f"done in {time.time()-t0:.1f}s")
