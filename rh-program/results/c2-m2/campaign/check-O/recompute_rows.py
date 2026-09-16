"""CHECKER task (2): recompute TWO rows per height with an INDEPENDENT transform (own Gauss-Legendre quadrature).
campaign_lib.py is NOT imported.  Rows chosen: small-L (delta = 0.1, L = 20) and the record point (delta = 0.1, L*(C1 = 1))."""
import json, math, numpy as np, warnings, sys, os
warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ind_transform as T
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) if False else "/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program/results/c2-m2/campaign"
OUT  = os.path.dirname(os.path.abspath(__file__))
# record constants, read from separation-note.md / PRICING.md (not from campaign_lib)
B1 = 8.70; R0 = 81.0; LAM0 = 25.0; C0 = 4.0; BP2 = 16.62196535; ETA_SAFE = 4.0e4
def ellR(t,L): return math.log(4 + t + R0*L)
def Lstar(d,t,C1=1.0): return max(LAM0/d, C0/d*(math.log(math.log(3+t)) + 2*math.log(1/d) + math.log(2*B1*C1)))
N_GL = 16000
res = {}
for tag in ["t1e3","t1e4","t1e5","t1e6"]:
    zj = json.load(open(f"{BASE}/zeros_{tag}.json")); t = zj["t"]; U_data = zj["U_data"]
    g = np.array([z[1] for z in zj["zeros"]])
    rows_b = json.load(open(f"{BASE}/rows_{tag}.json"))
    picks = []
    for r in rows_b:
        if abs(r["delta"]-0.1) < 1e-12 and abs(r["L"]-20.0) < 1e-12: picks.append(("small-L", r))
        if abs(r["delta"]-0.1) < 1e-12 and r.get("is_record_point_C1_1"): picks.append(("record L*(C1=1)", r))
    out = []
    for kind, rb in picks:
        d = rb["delta"]; L = rb["L"]
        U_row = min(U_data, ETA_SAFE/L)
        u = g - t; m = np.abs(u) <= U_row; uu = u[m]
        bh = T.bhat(L*uu, N_GL)
        terms = uu*uu*bh*bh
        N_Z = float(terms.sum())
        # full-window value (no truncation at U_row) as a control
        bh_f = T.bhat(L*u, N_GL); N_full = float((u*u*bh_f*bh_f).sum())
        c = float(T.cedge(d*L, N_GL)[0])
        main = -2*d*d*c*c
        WZ = N_Z + main
        b6 = d*d*math.exp(d*L/2)
        sep = (2*d*d*c*c)/b6
        j = int(np.argmin(np.abs(uu)))
        out.append(dict(kind=kind, t=t, delta=d, L=L, U_row=U_row, n_used=int(m.sum()),
            chk_N_Z=N_Z, chk_N_Z_full_window=N_full, chk_c=c, chk_main=main, chk_W_Z=WZ, chk_W_Zprime=N_Z,
            chk_W_Zrep=N_Z-float(terms[j])+main, chk_clause6=b6, chk_sep_over_clause6=sep,
            chk_density_model=math.log(t/(2*math.pi))*BP2/L**3, chk_clause4=2*B1*ellR(t,L)/L**2,
            chk_near_gamma=float(t+uu[j]), chk_near_term=float(terms[j]),
            b_N_Z=rb["N_Z"], b_W_Zprime=rb["W_Zprime"], b_c=rb["c_deltaL"], b_main=rb["main_term"], b_W_Z=rb["W_Z"],
            b_W_Zrep=rb["W_Zrep"], b_clause6=rb["clause6_bound"], b_sep=rb["sep_over_clause6"],
            b_model=rb["density_model"], b_clause4=rb["clause4_bound_C1_1"], b_n_used=rb["n_zeros_used"],
            b_U_row=rb["U_row"], b_near_gamma=rb["near_gamma"], b_near_term=rb["near_term"],
            b_Lstar_C1_1=rb["Lstar_C1_1"], chk_Lstar_C1_1=Lstar(d,t,1.0), b_Lstar_C1_zeta=rb["Lstar_C1_zeta"],
            chk_Lstar_C1_zeta=Lstar(d,t,2.4e9)))
        r = out[-1]
        for k in ["N_Z","c","main","W_Z","W_Zrep","clause6"]:
            cv = r["chk_"+k] if "chk_"+k in r else None
        print(tag, kind, "N_Z  chk=%.12e bld=%.12e  rel=%.3e abs=%.3e"%(r["chk_N_Z"], r["b_N_Z"], abs(r["chk_N_Z"]/r["b_N_Z"]-1) if r["b_N_Z"] else float('nan'), abs(r["chk_N_Z"]-r["b_N_Z"])), flush=True)
        print("        ", "main chk=%.12e bld=%.12e  rel=%.3e"%(r["chk_main"], r["b_main"], abs(r["chk_main"]/r["b_main"]-1)))
        print("        ", "W_Z  chk=%.12e bld=%.12e  rel=%.3e"%(r["chk_W_Z"], r["b_W_Z"], abs(r["chk_W_Z"]/r["b_W_Z"]-1)))
        print("        ", "sep/cl6 chk=%.10g bld=%.10g rel=%.3e ; n_used chk=%d bld=%d ; U_row chk=%.6f bld=%.6f"%(
              r["chk_sep_over_clause6"], r["b_sep"], abs(r["chk_sep_over_clause6"]/r["b_sep"]-1), r["n_used"], r["b_n_used"], r["U_row"], r["b_U_row"]))
    res[tag] = out
json.dump(res, open(f"{OUT}/rows_check.json","w"), indent=1)
print("DONE")
