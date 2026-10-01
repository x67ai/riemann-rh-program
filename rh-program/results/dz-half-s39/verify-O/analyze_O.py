# read-O analysis of verify-O/data/dz_*.i64: E(e) = N(e-) - rho*e at log2-edges e_i = 2^{(i+1)/B}.
# Per octave j (x in (2^j, 2^{j+1}]): A_j = max|E|, running sup M_j (from x >= 16), MS_j = mean E^2 over edges.
# Slopes vs log x_j (x_j = 2^{j+1}) on full octaves inside [10^a, X]: sup, supL (M*sqrt(log x)), ms, msL (1/2 slope of MS*log x).
import json, glob, math, sys, numpy as np

def stats(tag):
    meta = json.load(open(f"data/dz_{tag}.json")); B = meta["B"]; rho = meta["rho"]; X = meta["X"]
    c = np.fromfile(f"data/dz_{tag}.i64", dtype=np.int64); N = np.cumsum(c)
    e = 2.0 ** ((np.arange(len(c)) + 1) / B); E = N - rho * e
    jmax = int(math.floor(math.log2(X))) - 1          # last full octave (2^jmax, 2^{jmax+1}] with 2^{jmax+1} <= X
    J = np.arange(4, jmax + 1); A = []; MS = []
    for j in J:
        sl = slice(j * B, (j + 1) * B)                  # edges 2^{j + 1/B} ... 2^{j+1}
        A.append(np.abs(E[sl]).max()); MS.append(np.mean(E[sl] ** 2))
    A = np.array(A); MS = np.array(MS); M = np.maximum.accumulate(A); xj = 2.0 ** (J + 1.0)
    iX = int(np.nonzero(e <= X)[0][-1])               # last edge <= X (the top bin is partial: its edge exceeds X)
    top = slice(21 * B, 23 * B)                         # octaves (2^21, 2^23]
    out = dict(tag=tag, rho=rho, has15=meta["has15"], E_X_over_s=float(E[iX] / math.sqrt(e[iX] / math.log(e[iX]))),
               frac_neg_top=float(np.mean(E[top] < 0)))
    for a in (3, 4, 5):
        m = xj / 2 >= 10 ** a
        lx = np.log(xj[m])
        sl = lambda y: float(np.polyfit(lx, y, 1)[0])
        out[f"sup{a}"] = sl(np.log(M[m])); out[f"supL{a}"] = sl(np.log(M[m] * np.sqrt(lx)))
        out[f"ms{a}"] = 0.5 * sl(np.log(MS[m])); out[f"msL{a}"] = 0.5 * sl(np.log(MS[m] * lx))
        out[f"blk{a}"] = sl(np.log(A[m]))
        out[f"nfit{a}"] = int(m.sum())
    out["amp_top_octaves"] = [round(float(A[i] / math.sqrt(xj[i] / math.log(xj[i]))), 3) for i in range(len(J) - 4, len(J))]
    return out

if __name__ == "__main__":
    tags = sys.argv[1:] or sorted(t.split("dz_")[1][:-5] for t in glob.glob("data/dz_*.json"))
    rows = [stats(t) for t in tags]
    keys = ["sup3", "sup4", "sup5", "supL3", "blk3", "ms3", "msL3", "msL4", "msL5"]
    for r in rows:
        print(r["tag"], "rho=%.4f" % r["rho"], "1.5" if r["has15"] else "  ", " ".join("%s=%.3f" % (k, r[k]) for k in keys),
              "E(X)/s=%+.2f" % r["E_X_over_s"], "neg%%=%.2f" % r["frac_neg_top"], "amp", r["amp_top_octaves"])
    for tpl in ("R", "C"):
        rr = [r for r in rows if r["tag"][0] == tpl]
        if not rr: continue
        line = []
        for k in keys:
            v = np.array([r[k] for r in rr]); line.append("%s %.3f±%.3f" % (k, v.mean(), v.std(ddof=1) / math.sqrt(len(v))))
        print("MEAN", tpl, len(rr), "seeds:", "  ".join(line))
    json.dump(rows, open("data/aggregate_O.json", "w"), indent=1)
