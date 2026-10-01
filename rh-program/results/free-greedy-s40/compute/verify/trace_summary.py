# trace_summary.py TRACELOG RHO -- mechanism of one busy period (T rows from s8win with S8_TRACE="x0 x1"):
# composites by source (small-prime cursor q * m, or multiplier cursor n * q with q > sqrt X), the excess
# C(x) - C(x0) - rho (x - x0) along the stretch, and which multipliers n / small primes q carry the excess.
import sys, math, collections
rho = float(eval(sys.argv[2], {"pi": math.pi, "e": math.e, "sqrt": math.sqrt}))
ev = []
for ln in open(sys.argv[1]):
    if not ln.startswith("T "): continue
    p = ln.split()
    x = float(p[1])
    if p[2] == "P": ev.append((x, "P", None, None))
    elif p[3] == "small": ev.append((x, "S", float(p[4][2:]), float(p[5][2:])))
    else: ev.append((x, "M", float(p[4][2:]), float(p[5][2:])))
x0, x1 = ev[0][0], ev[-1][0]
nP = sum(1 for e in ev if e[1] == "P"); nS = sum(1 for e in ev if e[1] == "S"); nM = sum(1 for e in ev if e[1] == "M")
print(f"# trace {sys.argv[1]}: [{x0:.3f}, {x1:.3f}] length {x1 - x0:.1f}; events {len(ev)}: g-primes {nP}, small-cursor composites {nS}, multiplier composites {nM}")
print(f"#   expected composites at rate rho: {rho * (x1 - x0):.1f}; excess C - rho*L = {nS + nM - rho * (x1 - x0):+.1f}")
c = 0; best = (-1e9, x0)
for e in ev:
    if e[1] != "P": c += 1
    exc = c - rho * (e[0] - x0)
    if exc > best[0]: best = (exc, e[0])
print(f"#   max running excess {best[0]:.2f} at x = {best[1]:.3f}")
cm = collections.Counter(round(e[2], 4) for e in ev if e[1] == "M")
cs = collections.Counter(round(e[2], 4) for e in ev if e[1] == "S")
print("#   top multipliers n (multiplier cursors):", ", ".join(f"{k}:{v}" for k, v in cm.most_common(8)))
print("#   top small primes q (small cursors):    ", ", ".join(f"{k}:{v}" for k, v in cs.most_common(8)))
qs = sorted(e[3] for e in ev if e[1] == "M")
if qs:
    print(f"#   large primes used by multiplier composites: {len(qs)} uses, q from {qs[0]:.1f} to {qs[-1]:.1f}")
