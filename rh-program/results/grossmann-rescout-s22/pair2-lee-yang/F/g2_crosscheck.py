# Cross-check of my enumeration against the template log's rows (a stated check, not a source): the log keys classes by
# (p, deg, a1, a2) for MONIC f only.  Recompute that set from scratch here (monic only, both degrees) and diff.
import itertools, sys
sys.argv = ["x", "/dev/null"]
exec(open("g2_enumerate.py").read().split("classes = {}")[0])   # reuse count_points / squarefree / nonresidue only
mine = set()
for p in (3, 5, 7):
    for d in (5, 6):
        for low in itertools.product(range(p), repeat=d):
            f = list(low) + [1]
            if not squarefree(f, p): continue
            N1 = count_points(f, p, 1); N2 = count_points(f, p, 2)
            a1 = N1 - p - 1; a2 = (a1 * a1 + N2 - p * p - 1) // 2
            mine.add((p, d, a1, a2))
log = set()
for line in open("../../verify/genus2_signed_kernel.log"):
    t = line.split()
    if len(t) > 6 and t[0] in ("3", "5", "7") and t[1] in ("5", "6") and t[6] in ("True", "False"):
        log.add((int(t[0]), int(t[1]), int(t[2]), int(t[3])))
print("my monic (p,deg,a1,a2) count:", len(mine), " log rows parsed:", len(log))
print("in mine not in log:", sorted(mine - log))
print("in log not in mine:", sorted(log - mine))
print("distinct (p,a1,a2) in mine:", len({(p, a1, a2) for p, d, a1, a2 in mine}), " in log:", len({(p, a1, a2) for p, d, a1, a2 in log}))
