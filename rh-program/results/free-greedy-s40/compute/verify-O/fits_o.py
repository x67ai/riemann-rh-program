# fits_o.py -- refit sup E (S8(pi/4)) against c log^2 x, c log^k x, C x^b (least squares in log S). Opus reader.
import numpy as np
x = 10.0**np.arange(3, 12)
# 1e3..1e9 from my own run (verify-O/logs/o_pi4_1e9.log); 1e10, 1e11 from the unit's logs (NOTE l. 59, 110)
S = np.array([8.2174410257, 13.3303549454, 26.6311773813, 39.5303075943, 47.8635398026,
              95.8616048208, 95.8616048208, 113.2048, 123.618])
def fit(xx, SS, kind):
    L, LL, y = np.log(xx), np.log(np.log(xx)), np.log(SS)
    if kind == 'log2': c = np.mean(y - 2*LL); pred = c + 2*LL; par = (np.exp(c),)
    elif kind == 'logk': A = np.vstack([np.ones_like(LL), LL]).T; co = np.linalg.lstsq(A, y, rcond=None)[0]; pred = A @ co; par = (np.exp(co[0]), co[1])
    else: A = np.vstack([np.ones_like(L), L]).T; co = np.linalg.lstsq(A, y, rcond=None)[0]; pred = A @ co; par = (np.exp(co[0]), co[1])
    r = y - pred
    return par, np.sqrt(np.mean(r**2)), r[-1]
for hi in (9, 10, 11):
    m = x <= 10.0**hi
    print(f"[1e3, 1e{hi}]:", end=' ')
    for kind in ('log2', 'logk', 'pow'):
        par, rms, rend = fit(x[m], S[m], kind)
        print(f"{kind} par={tuple(round(p,4) for p in par)} rms={rms:.3f} resid_end={rend:+.3f}", end=' | ')
    print()
print("per-decade slopes:", np.round(np.diff(np.log10(S)), 3))
print("supE/log^2x:", np.round(S/np.log(x)**2, 3))
print("supE/x^0.25:", np.round(S/x**0.25, 3))
for a, b in ((6, 11), (8, 11), (7, 11)):
    i, j = a-3, b-3
    print(f"effective exponent 1e{a}->1e{b}: power {np.log10(S[j]/S[i])/(b-a):.3f}; log-power {np.log(S[j]/S[i])/np.log(np.log(x[j])/np.log(x[i])):.3f}")
# what the 9 points cannot exclude: best C for a fixed b, and its rms
for b in (0.02, 0.05, 0.10, 0.145, 0.20, 0.25):
    y = np.log(S) - b*np.log(x); c = y.mean(); r = y - c
    print(f"b={b}: C={np.exp(c):.3f} rms={np.sqrt(np.mean(r**2)):.3f} end_resid={r[-1]:+.3f}")
