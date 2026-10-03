# control.py -- RH-false control for the theory note (orchestrator's probe; double-precision output from Arb midpoints).
# Object: f = Xi + lam (lam > 0 real): an even real entire function WITH zeros off the real axis (above the negative lobes of Xi
# whose minimum is > -lam).  Its "pencil" is (Xi_k + lam) + t Phi_{k+1} = f - L_t.  NOTE section 2/4 predict: real zeros LEAVE the
# axis (a local minimum of the real-axis quotient with value in (0,1)), and the branch then ASCENDS.
from c4probe import *
from trace import cSd
ctx.prec = 200
def real_S(k, x, lam):
    a, b = pair_T(k, acb(x))
    return float(((a + lam) / b).real.mid())
def scan(k, lam, x0, x1, h=0.005):
    xs = [x0 + i * h for i in range(int((x1 - x0) / h) + 1)]
    v = [real_S(k, x, lam) for x in xs]
    out = []
    for i in range(1, len(xs) - 1):
        if v[i] < v[i - 1] and v[i] <= v[i + 1] and 0 < v[i] < 1: out.append(("MIN", xs[i], v[i]))
        if v[i] > v[i - 1] and v[i] >= v[i + 1] and 0 < v[i] < 1: out.append(("max", xs[i], v[i]))
    return out
if __name__ == "__main__":
    k = 1
    # sizes on the first negative lobe (14.13, 21.02): the minimum of Xi and the two levels Q_1, Q_2 there
    for x in (16.0, 17.0, 17.5, 18.0, 19.0):
        z = acb(x)
        xi = float(Xi(z).real.mid()); a, b = pair_T(1, z)
        q2 = xi - float(a.real.mid()); q1 = q2 + float(b.real.mid())
        print("x=%5.2f  Xi=% .6e  Q_1=% .6e  Q_2=% .6e" % (x, xi, q1, q2))
    for lam in (0.0, 5e-5, 1e-4):
        ex = scan(k, lam, 0.5, 45.0)
        print("lam=%g: extrema of (Xi_2+lam)/Phi_2 on [0.5,45] with value in (0,1):" % lam)
        for e in ex: print("    %s x=%.3f value=%.6g" % e)
