#!/usr/bin/env python3
"""predict_det.py — the branch-point prediction for P_det (NOTE §4.3). Since pi - F_R is bounded, B(w) := sum_q q^{-w} -
int_1^oo v^{-w} f_R dv is analytic on Re w > 0, and log zeta_det(s) = sum_k P(ks)/k, P(w) = sum_q q^{-w}, gives
  (2s - 1)^{1/2} zeta_det(s) -> H := -exp( B(1/2) + B(1)/2 + sum_q [-log(1 - q^{-1/2}) - q^{-1/2} - q^{-1}/2] )  (s -> 1/2),
using s/(s-1) = -1 and 2s = 1 at s = 1/2. B(1) = lim [sum_{q<=X} 1/q - Ein(log X)], B(1/2) = lim [sum_{q<=X} q^{-1/2} -
2 Shi(log X / 2)] (tails O(1/X), O(X^{-1/2})). Transfer [heuristic, Selberg-Delange shape]: E_det(x) ~ sqrt(2/pi) H (x/log x)^{1/2}.
Compares with the measured block means E/(x/log x)^{1/2} from data/ctl_det.stats.json."""
import json, math
import numpy as np
from scipy.special import shichi
from dzcommon import Ein

meta = json.load(open("data/ctl_det.json")); X = meta["X"]
q = np.fromfile("data/ctl_det.primes.f64")
T = math.log(X)
B1 = float(np.sum(1.0 / q)) - Ein(T)
Bh = float(np.sum(q ** -0.5)) - 2.0 * float(shichi(T / 2)[0])
rest = float(np.sum(-np.log1p(-q ** -0.5) - q ** -0.5 - 0.5 / q))
H = -math.exp(Bh + 0.5 * B1 + rest)
pred = math.sqrt(2 / math.pi) * H
st = json.load(open("data/ctl_det.stats.json"))
rows = []
for b in st["blocks"]:
    s = math.sqrt(b["xm"] / math.log(b["xm"]))
    rows.append((b["j"], b["xm"], b["mean"] / s, math.sqrt(b["MS"]) / s))
out = dict(B_half=Bh, B_one=B1, rest=rest, H=H, predicted_ratio=pred, blocks=rows)
json.dump(out, open("data/ctl_det.predict.json", "w"), indent=1)
print("B(1/2)=%.6f B(1)=%.6f rest=%.6f H=%.6f  predicted E/(x/log x)^(1/2) -> %.4f" % (Bh, B1, rest, H, pred))
for j, xm, r, rr in rows:
    if j % 2 == 0:
        print("j=%2d x~%.2e  mean E/(x/log x)^(1/2) = %+.4f   rms ratio %.4f" % (j, xm, r, rr))
