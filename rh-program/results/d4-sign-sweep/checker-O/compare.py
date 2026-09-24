# compare.py — Job 2 part A: |dP|, |dW| of checker-O (twsumO) against Job 1's JSONs, tolerance 1e-10 + phase line.
# Job 1's phase line is recomputed with the binding eps = 1.0267e-30 (job1_ddlog_bound.py) and also shown with Job 1's 6.392e-31.
import json, os, sys
J = "../out/"
EPS_BIND = 1.0266395604864687e-30
def j(p): return json.load(open(p))
rows = []
def add(label, mine, P1, W1, t, l1, src):
    m = j(mine); dP = abs(m["P"] - P1); dW = abs(m["W"] - W1) if W1 is not None else None
    line = EPS_BIND*t*l1; tol = 1e-10 + line
    rows.append(dict(point=label, P_job1=P1, P_checkerO=m["P"], dP=dP, W_job1=W1, W_checkerO=m["W"], dW=dW,
                     phase_line_binding=line, tolerance=tol, PASS=(dP <= tol and (dW is None or dW <= tol)),
                     n_terms_checkerO=m.get("n_terms"), l1_checkerO=m.get("l1"), job1_source=src, checkerO_json=mine))
# (85.7, 10) zeta: Job 1 values from SHARED checkpoint 1 / note sect. 4.2 (no zeta JSON at 85.7 in out/)
add("zeta (85.7, 10)", "out/zetaO_t85.69934848537759_L10.json", 0.03960850701243899, 0.003822866509676, 85.7, 1.4568633, "SHARED checkpoint 1 (printed to 16 digits)")
add("zeta (85.7, 20) [M6 record]", "out/zetaO_t85.69934848537759_L20.json", 0.004562999824717, 0.000866034231848, 85.7, 12.54, "M6 note sect. 4 table (15 digits)")
for t, L, lab in [("1000000", "10", "(1e6, 10)"), ("1000000", "20", "(1e6, 20)"), ("1000000000000", "20", "(1e12, 20)"), ("1000000000000", "28.35", "(1e12, 28.35)"), ("3000175332900", "28.35", "(3000175332900, 28.35) PT edge")]:
    p = J + "zeta_t%s_L%s.json" % (t, L)
    tt = {"1000000": "1e6", "1000000000000": "1e12", "3000175332900": "3000175332900"}[t]
    mine = "out/zetaO_t%s_L%s.json" % (tt, L)
    if os.path.exists(p) and os.path.exists(mine):
        q = j(p); add("zeta " + lab, mine, q["P_dd"], q["W"], float(t), q["l1_norm"], p)
dh = j(J + "sum_dh_t85p7_L10.json"); adh = j(J + "arch_dh_t85.69934848537759_L10.json")
Wdh = [v for k, v in adh.items() if k.upper().startswith("ARCH") and isinstance(v, float)]
add("DH (85.7, 10)", "out/dhO_t85.69934848537759_L10.json", dh["P_dd"], -0.269812074198287, 85.7, 3.29, "out/sum_dh_t85p7_L10.json; W from SHARED checkpoint 1")
if os.path.exists("out/dhO_t85.69934848537759_L20.json"):
    d2 = j(J + "sum_dh_t85p7_L20.json") if "P_dd" in j(J + "sum_dh_t85p7_L20.json") else None
    add("DH (85.7, 20)", "out/dhO_t85.69934848537759_L20.json", 0.7570041820049636, -0.748231145297333, 85.7, 30, "SHARED checkpoint 1")
json.dump(rows, open("out/compare.json", "w"), indent=1)
for r in rows:
    print("%-36s dP=%.2e dW=%s tol=%.2e %s   W_O=%.15e" % (r["point"], r["dP"], "%.2e" % r["dW"] if r["dW"] is not None else "-", r["tolerance"], "PASS" if r["PASS"] else "FAIL", r["W_checkerO"]))
