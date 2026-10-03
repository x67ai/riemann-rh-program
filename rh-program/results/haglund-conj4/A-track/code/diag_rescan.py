# diag_rescan.py -- why does the P3 frontier rescan disagree with the main scan for pencil k? Prints the differences.
import sys, json
from a_core import ctx
from axis import scan
k = int(sys.argv[1]); ctx.prec = 96
X = 4.0 * (k + 2) ** 2 + 40; xf = 4.0 * (k + 1) ** 2 - 40
r = scan(k, 0.0, X, "T", 20.0)
r2 = scan(k, xf, X, "T", 40.0)
for name in ("zeros_Xik", "zeros_Xik1"):
    a = [z for z in r[name] if z > xf + 1e-9]; b = r2[name]
    print(name, "main", len(a), "rescan", len(b))
    for z in a:
        if all(abs(z - w) > 1e-6 for w in b): print("   only in main:", repr(z))
    for z in b:
        if all(abs(z - w) > 1e-6 for w in a): print("   only in rescan:", repr(z))
ea = [(e["x"], e["u"], e["type"]) for e in r["extrema01"] if e["x"] > xf]; eb = [(e["x"], e["u"], e["type"]) for e in r2["extrema01"]]
print("extrema main", len(ea), "rescan", len(eb))
for e in ea:
    if all(abs(e[0] - f[0]) > 1e-6 for f in eb): print("   only in main:", e)
for f in eb:
    if all(abs(e[0] - f[0]) > 1e-6 for e in ea): print("   only in rescan:", f)
for e in ea:
    for f in eb:
        if abs(e[0] - f[0]) <= 1e-6 and round(e[0], 6) != round(f[0], 6): print("   same extremum, 6th-decimal rounding differs:", e[0], f[0])
