"""o5_classB.py — read-O addition: an affine count functional, vanishing at genus 0, strictly positive on every
genuine curve of genus >= 1 over F_q, violated by V-type data, that is NOT a Weil test (f < 0 somewhere on the circle).
I(Z) = c0*g + (N_1 - q - 1), i.e. Theorem W(i) with c_0 = c0, c_1 = -sqrt q: f(theta) = c0 - 2 sqrt(q) cos(theta).
Weil test iff c0 >= 2 sqrt q.  Genus 1 genuine: N_1 >= q + 1 - m, m = floor(2 sqrt q), so I > 0 iff c0 > m (integrality).
Genus >= 2 genuine: N_1 >= 0 and 2 c0 > q + 1 suffice (q <= 13). Window c0 in (m, 2 sqrt q): class (B).
Exact rational c0; checks on the genuine lists of o3 (q = 5, 7) and the RH-true census data (q = 11, a superset)."""
import json
from fractions import Fraction as Fr
from math import isqrt
gen = json.load(open("o3_genuine.json")); data = json.load(open("o1_data.json"))
out = []
for q, c0 in ((5, Fr(17, 4)), (7, Fr(21, 4)), (11, Fr(25, 4))):
    m = isqrt(4 * q)                                      # floor(2 sqrt q)
    weil = c0 * c0 >= 4 * q                               # c0 >= 2 sqrt q ?
    I = lambda g, N1: c0 * g + N1 - q - 1
    g1 = [q + 1 - t for t in gen["%d_1" % q]]             # N_1 of genuine genus-1 curves
    if "%d_2" % q in gen: g2 = [q + 1 + a1 for a1, a2 in gen["%d_2" % q]]; src = "genuine (o3)"
    else: g2 = [q + 1 + r["a"][0] for r in data["%d_2" % q] if r["kind"] == "RH"]; src = "RH-true census (superset)"
    ok1 = min(I(1, n) for n in g1); ok2 = min(I(2, n) for n in g2)
    caught = {}
    for key in ("%d_1" % q, "%d_2" % q):
        g = int(key[-1]); rows = [r for r in data[key] if r["kind"] != "RH"]
        caught[key] = (sum(1 for r in rows if I(g, r["N"][0]) < 0), len(rows))
    out.append("q=%d c0=%s: Weil test? %s (f(0) = c0 - 2 sqrt q = %.4f) ; min I on genuine g=1: %s, on %s g=2: %s ; "
               "I(V-type t=q) = %s ; P^1: %s ; RH-false caught (g=1, g=2): %s"
               % (q, c0, weil, float(c0) - 2 * q ** 0.5, ok1, src, ok2, I(1, 1), I(0, q + 1), caught))
out.append("Genus >= 3 genuine curves: I >= 3 c0 - q - 1 > 0 for these (q, c0) since N_1 >= 0.")
open("o5_classB.log", "w").write("\n".join(out) + "\n")
print("\n".join(out))
