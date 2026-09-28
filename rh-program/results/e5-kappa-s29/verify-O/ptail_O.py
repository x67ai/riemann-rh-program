#!/usr/bin/env python3
"""ptail_O.py -- Opus reader: size of the prime sum's tail beyond N = 1e7 for the primal element, by the PNT density
(sum_{n > N} 4 Lambda(n) w(log n)/(n+1) ~ 4 int_{log N}^inf w(u) du; heuristic size, not a bound), and the same quantity
for 1e6 < n <= 1e7 against the exact sieve difference in primal_O_run.log as a calibration."""
import numpy as np, json
J = json.load(open("../verify/target_primal_fine_best.json")); c = np.array(J["c"]); hx = J["hx"]; n = len(c); mid = (np.arange(n) + .5)*hx
def w_of(u):
    out = np.empty(len(u))
    for i in range(0, len(u), 2000):
        uu = u[i:i+2000, None]; f = (np.exp(1j*uu*mid[None, :]) @ c)*hx*np.sinc(u[i:i+2000]*hx/(2*np.pi))/(2*np.pi); out[i:i+2000] = np.abs(f)**2
    return out
def I(a, b):
    x, wg = np.polynomial.legendre.leggauss(10); e = np.arange(a, b + 1e-12, 0.02); u = (e[:-1, None] + (x + 1)/2*0.02).ravel()
    return 4*np.sum(w_of(u).reshape(-1, 10)*wg*0.01)
cal = I(np.log(1e6), np.log(1e7)); tail = I(np.log(1e7), 200.0)
far = 4*w_of(np.array([200.0]))[0]*200
print(f"PNT-density estimate on (1e6, 1e7]: {cal:.4e} (exact sieve difference 1.5120e-10); beyond 1e7 up to u = 200: {tail:.4e}; w(200)*4*200 ~ {far:.1e}")
json.dump(dict(calib=cal, tail=tail), open("ptail_O_out.json", "w"))
