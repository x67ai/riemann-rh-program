#!/usr/bin/env python3
"""p9_arb.py -- Lane A producer, Arb/FLINT leg (UNTRUSTED): window rows (SPEC P-9) and the Lemma-T tail row (P-10)
for the M2a certificate of Polymath15 Table 1 row 2 (results/d1-m2a/SPEC.md sections 5, 7.2, 7.4).

TRUST STATUS.  Producer-side code outside the trust boundary (D-R3); its integers enter the trusted statement only through
the displayed hypotheses H2-A (`AsymEnclOK`) and H-TAIL (`TailOK`); the kernel checks C-A1..C-A6 only.  Never "fully
machine-checked".  Platform trust: Arb's ball contract (inclusion isotonicity; correctly rounded mid()/rad(); M1 leg D-P0)
and python-flint 0.6.0.  INDEPENDENCE: this leg imports the exact ball<->rational helpers of ITS OWN M2a producer
(results/d1-m2a/producer_arb.py: D-P1..D-P4) and nothing from the mpmath leg; the only shared input is the UNTRUSTED row plan
(rows-plan.json, data: the partition [N-, N+] and the y-pieces).  The mathematics is the SAME derivation M / M-E / M-T
(written out in p9_mp.py's docstring and PLAN.md section 2, from P15 (14)/(92), (19)-(22), (80), Lemma 10.1 p65, Lemma 8.2's
proof p43, Prop 6.6 p31, (82)-(86) p39-41, (96) p52, and SPEC 5.4) re-implemented here from the formulas, not from the code.

Conventions of this leg (as producer_arb.py): prec 320 bits; e_{C,0} by the 10.50 form of SPEC D-2.4; K = 10^12;
every emitted integer is floor(K * lo) / ceil(K * hi) on exact rationals from the ball's exact dyadic mid/rad (D-P1/D-P2).

usage:
  p9_arb.py rows --plan PLAN.json --out DIR [--resume] [--rows i,j,...] [--K 1000000000000] [--Nc 10000] [--m 2000] [--prec 320]
  p9_arb.py tail --plan PLAN.json --out DIR [--direct]     (--direct: also sum Q1/Q2 term by term and check containment)
  p9_arb.py assemble --plan PLAN.json --out DIR --name asym-arb.json
  p9_arb.py selftest
U.S. English throughout.
"""
import argparse, json, os, sys, time
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..")))
from producer_arb import ball_interval, upper, lower, floor_frac, ceil_frac, rat_ball, hull_ball, to_arb, PI  # noqa: E402
from flint import arb, ctx  # noqa: E402

T0 = Fraction(93, 500); Y0 = Fraction(16733, 100000); YA = Fraction(3962323, 5000000); N0 = 630783
TRUST_LABEL = "kernel-checked modulo the displayed hypotheses H1, H2 (H2-B, H2-A, H-TAIL) and H3 (producers untrusted)"

def frac_str(q):
    q = Fraction(q); return f"{q.numerator}/{q.denominator}"

class Tables:
    def __init__(self, Nc, t):
        self.Nc = Nc
        self.L = [None] * (Nc + 1); self.b = [None] * (Nc + 1)
        q = t / 4
        for n in range(1, Nc + 1):
            L = arb(n).log() if n > 1 else arb(0)
            self.L[n] = L
            self.b[n] = (q * L * L).exp() if n > 1 else arb(1)

class Leg:
    def __init__(self, Nc=10000, m=2000, prec=320):
        ctx.prec = prec
        self.prec = prec; self.Nc = Nc; self.m = m
        self.t = rat_ball(T0)
        self.tab = Tables(Nc, self.t)
        self.log2 = arb(2).log()
        self.b2 = self.tab.b[2]

    # ---- instance functions (M-1, M-6)
    def xN(self, N):
        return 4 * PI() * (arb(N * N) - self.t / 16)
    def epsN(self, N):
        return -(self.t / 4) * (1 - self.t / (16 * arb(N * N))).log() + self.t / (2 * self.xN(N) ** 2)
    def sigma_lo(self, N, y):
        s = (1 + rat_ball(y)) / 2 + (self.t / 2) * arb(N).log() - self.epsN(N)
        return lower(s)
    def rho_hi(self, N):
        return upper(1 / (1 - self.t / (16 * arb(N * N))).sqrt())
    def k_hi(self, N, y):
        return upper(self.t * rat_ball(y) / (2 * (self.xN(N) - 6)))
    def theta(self, n):
        return (-(self.t / 2) * self.log2 * rat_ball(Fraction(n, 2)).log()).exp()

    # ---- M-8: G(s', a, b)
    def term(self, n, sp):
        return self.tab.b[n] * (-sp * self.tab.L[n]).exp()
    def psi(self, u, sp):
        return ((1 - sp) * u + (self.t / 4) * u * u).exp()
    def I_upper(self, sp, u0, u1):
        m = self.m; h = (u1 - u0) / m
        tot = self.psi(u0, sp) + self.psi(u1, sp)
        for i in range(1, m):
            tot += 2 * self.psi(u0 + i * h, sp)
        return upper(tot * h / 2)
    def I_lower(self, sp, u0, u1):
        m = self.m; h = (u1 - u0) / m
        tot = arb(0)
        for i in range(m):
            tot += self.psi(u0 + (2 * i + 1) * h / 2, sp)
        return lower(tot * h)
    def G(self, sp, a, b):
        assert 0 <= a <= b
        spq = Fraction(sp); sp = rat_ball(spq)
        if a == b:
            return Fraction(0), Fraction(0)
        M = min(b, max(a, self.Nc))
        head = arb(0)
        for n in range(a + 1, M + 1):
            head += self.term(n, sp)
        lo, hi = lower(head), upper(head)
        if M < b:
            if not (upper((self.t / 2) * arb(b).log()) < spq):
                raise ValueError(f"G: summand not certified decreasing on ({M}, {b}] at s' = {float(spq)}")
            hi += self.I_upper(sp, arb(M).log(), arb(b).log())
            lo += self.I_lower(sp, arb(M + 1).log(), arb(b + 1).log())
        return lo, hi
    def G_direct(self, sp, a, b):
        sp = rat_ball(Fraction(sp)); tot = arb(0); q = self.t / 4
        for n in range(a + 1, b + 1):
            L = arb(n).log() if n > 1 else arb(0)
            tot += (q * L * L - sp * L).exp()
        return lower(tot), upper(tot)

    # ---- the sub-box floor (M-4..M-7)
    def sub_box(self, Nlo, Nhi, ya, yb):
        ya, yb = Fraction(ya), Fraction(yb)
        assert Y0 <= ya < yb <= YA and Nlo <= Nhi
        n_even = Nlo + 1 if (Nlo + 1) % 2 == 0 else Nlo + 2
        if not (upper(self.theta(n_even)) <= Fraction(1, 2)):
            raise ValueError("M-5 needs theta_n <= 1/2 for n > N-")
        sig = self.sigma_lo(Nlo, ya)
        sp = sig - ya
        b2_2s = self.b2 * (-rat_ball(sig) * self.log2).exp()
        b2_2sp = self.b2 * (-rat_ball(sp) * self.log2).exp()
        beta_hi = upper(b2_2s)
        rho = self.rho_hi(Nlo)
        c = (rat_ball(Fraction(2, 100) * yb)).exp() * rat_ball(rho)
        cN = c * (-rat_ball(ya) * arb(Nlo).log()).exp()
        k = self.k_hi(Nlo, yb)
        half = Nhi // 2
        GA_all = self.G(sig, 0, Nhi); GA_head = self.G(sig, 0, half); GA_tail = self.G(sig, half, Nhi)
        GC_all = self.G(sp, 0, Nhi); GC_head = self.G(sp, 0, half); GC_tail = self.G(sp, half, Nhi)
        LA_lo = 2 - GA_all[1] + lower(b2_2s) * GA_head[0] - upper(b2_2s) * GA_tail[1]
        two_yb = (-rat_ball(yb) * self.log2).exp()
        UC_hi = upper(cN) * (GC_all[1] - lower(two_yb * b2_2sp) * GC_head[0] + upper(b2_2s) * GC_tail[1])
        Nk = (rat_ball(k) * arb(Nhi).log()).exp() - 1
        Zbar = upper(Nk) * upper(cN) * GC_all[1]
        num = LA_lo - UC_hi
        T_lo = (num / (1 + beta_hi) - Zbar) if num >= 0 else (num - Zbar)
        return dict(Nlo=Nlo, Nhi=Nhi, ya=frac_str(ya), yb=frac_str(yb), T_lo=frac_str(T_lo), T_lo_float=float(T_lo),
                    sigma_lo=frac_str(sig), beta_hi=frac_str(beta_hi), c_hi=frac_str(upper(c)), rho_hi=frac_str(rho), k_hi=frac_str(k),
                    LA_lo=float(LA_lo), UC_hi=float(UC_hi), Zbar=float(Zbar),
                    G=dict(A_all=[float(GA_all[0]), float(GA_all[1])], A_head=[float(GA_head[0]), float(GA_head[1])], A_tail=[float(GA_tail[0]), float(GA_tail[1])],
                           C_all=[float(GC_all[0]), float(GC_all[1])], C_head=[float(GC_head[0]), float(GC_head[1])], C_tail=[float(GC_tail[0]), float(GC_tail[1])]))

    # ---- M-E: the row defect (10.50 form for e_{C,0}, this leg's convention)
    def F_majorant(self, sig, N):
        """D-F5 form re-derived (b_n <= n^{(t/4) log N} for n <= N; integral test): F <= 1 + (N^{1-rho}-1)/(1-rho), rho = sig - (t/4) log N."""
        logN = arb(N).log()
        rho = rat_ball(sig) - self.t * logN / 4
        rlo = lower(rho)
        if rlo <= 0:
            return arb(N) * (-rat_ball(rlo) * logN).exp()
        if rlo == 1:
            return 1 + logN
        r = rat_ball(rlo)
        return 1 + (((1 - r) * logN).exp() - 1) / (1 - r)
    def defect_window(self, Nlo, Nhi, ylo=Y0, yhi=YA):
        t = self.t; pi = PI()
        xb = hull_ball(lower(self.xN(Nlo)), upper(self.xN(Nhi + 1)))
        yb = hull_ball(ylo, yhi)
        q = xb / (4 * pi); lq = q.log()
        sig = self.sigma_lo(Nlo, ylo)
        F = self.F_majorant(sig, Nhi)
        delta1 = ((t * t / 16) * lq * lq + arb("0.626")) / (xb - arb("6.66"))
        kap = t * yb / (2 * (xb - 6))
        fac = 1 + (arb("0.02") * yb).exp() * rat_ball(self.rho_hi(Nlo)) * (kap * arb(Nhi).log()).exp()
        eAB = (delta1.exp() - 1) * fac * F
        modterm = (lq * lq + pi * pi / 4).sqrt()
        eC0 = (q ** (-(1 + yb) / 4)) * (-(t / 16) * lq * lq + (3 * modterm + arb(21) / 2) / (xb - 12)).exp() \
            * (1 + arb("1.24") * (arb(3) ** yb + arb(3) ** (-yb)) / (arb(Nlo) - arb(1) / 8))
        tot = eAB + eC0
        return upper(tot), dict(eAB_hi=float(upper(eAB)), eC0_hi=float(upper(eC0)), delta1_hi=float(upper(delta1)), F_hi=float(upper(F)), sigma_lo=frac_str(sig))

    # ---- M-T: the tail row
    def tail_row(self, N1, direct=False):
        t = self.t; pi = PI()
        u1 = arb(N1).log()
        eps_hi = upper(self.epsN(N1))
        sig1 = self.sigma_lo(N1, Y0)
        rho1 = self.rho_hi(N1); k1 = self.k_hi(N1, YA)
        cg = arb("0.02").exp() * rat_ball(rho1)
        a = (1 - rat_ball(Y0)) / 2 + rat_ball(eps_hi)
        a2 = (1 + rat_ball(Y0)) / 2 + rat_ball(eps_hi) + rat_ball(k1)
        e = arb(1).exp()
        kT_hi = max(upper((2 / (e * t)).sqrt()), upper(2 / (e * t * u1)))
        psi1 = a * u1 - (t / 4) * u1 * u1
        psi2 = a2 * u1 - (t / 4) * u1 * u1
        N1_y0 = (-rat_ball(Y0) * u1).exp()
        g1 = self.G(sig1, 0, N1); Q1 = g1[1]
        sig2 = sig1 - Y0 - k1
        g2 = self.G(sig2, 0, N1); Q2 = upper(cg * N1_y0) * g2[1]
        Q3 = upper(psi1.exp()) * kT_hi
        Q4 = upper(cg * N1_y0 * psi2.exp()) * kT_hi
        x1 = self.xN(N1); q = x1 / (4 * pi); lq = q.log()
        delta1 = ((t * t / 16) * lq * lq + arb("0.626")) / (x1 - arb("6.66"))
        rhoF = (1 + rat_ball(Y0)) / 2 + (t / 4) * u1 - rat_ball(eps_hi)
        if not (lower(rhoF) > 1):
            raise ValueError("M-T needs rho_F > 1")
        Fmax = 1 + 1 / (rhoF - 1)
        fac = 1 + (arb("0.02") * rat_ball(YA)).exp() * rat_ball(rho1) * (rat_ball(k1) * u1).exp()
        eAB = (delta1.exp() - 1) * fac * Fmax
        yb = hull_ball(Y0, YA)
        modterm = (lq * lq + pi * pi / 4).sqrt()
        eC0 = (q ** (-(1 + yb) / 4)) * (-(t / 16) * lq * lq + (3 * modterm + arb(21) / 2) / (x1 - 12)).exp() \
            * (1 + arb("1.24") * (arb(3) ** yb + arb(3) ** (-yb)) / (arb(N1) - arb(1) / 8))
        E1 = upper(eAB + eC0)
        side = dict(S1=bool(eps_hi < (1 + Y0) / 2), S2=bool(lower(u1) >= upper(2 * a / t)),
                    S3=bool((1 - Y0) / 2 > eps_hi + k1), S4=bool(lower(u1) >= upper(2 * a2 / t)))
        S = Q1 + Q2 + Q3 + Q4 + E1
        rec = dict(N1=N1, Q1=frac_str(Q1), Q2=frac_str(Q2), Q3=frac_str(Q3), Q4=frac_str(Q4), E1=frac_str(E1),
                   sum_float=float(S), sum_lt_2=bool(S < 2), side=side,
                   consts=dict(sigma1=frac_str(sig1), sigma2=frac_str(sig2), eps_hi=frac_str(eps_hi), k1=frac_str(k1), rho1=frac_str(rho1),
                               a_hi=frac_str(upper(a)), a2_hi=frac_str(upper(a2)), kappaT_hi=frac_str(kT_hi), rhoF_lo=frac_str(lower(rhoF)),
                               u1=[frac_str(lower(u1)), frac_str(upper(u1))]),
                   floats=dict(Q1=float(Q1), Q2=float(Q2), Q3=float(Q3), Q4=float(Q4), E1=float(E1)),
                   G_encl=dict(Q1=[float(g1[0]), float(g1[1])], Q2sum=[float(g2[0]), float(g2[1])]))
        if direct:
            t0 = time.time()
            d1 = self.G_direct(sig1, 0, N1); d2 = self.G_direct(sig2, 0, N1)
            rec["direct"] = dict(Q1sum=[frac_str(d1[0]), frac_str(d1[1])], Q2sum=[frac_str(d2[0]), frac_str(d2[1])],
                                 contained=bool(g1[0] <= d1[0] and d1[1] <= g1[1] and g2[0] <= d2[0] and d2[1] <= g2[1]),
                                 Q1sum_float=[float(d1[0]), float(d1[1])], Q2sum_float=[float(d2[0]), float(d2[1])], seconds=time.time() - t0)
        return rec

# ---------------------------------------------------------------- driver

def now():
    return time.strftime("%Y-%m-%d %H:%M:%S %Z")

def atomic_json(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=1)
    os.replace(tmp, path)

def update_status(out_dir, leg, st):
    atomic_json(os.path.join(out_dir, f"STATUS-{leg}.json"), st)
    merged = os.path.join(out_dir, "STATUS.json")
    try:
        cur = json.load(open(merged)) if os.path.exists(merged) else {}
    except Exception:
        cur = {}
    cur[leg] = st; cur["updated"] = now()
    atomic_json(merged, cur)

def load_plan(path):
    plan = json.load(open(path))
    rows = [dict(Nlo=int(r["Nlo"]), Nhi=int(r["Nhi"]), ypieces=[(Fraction(str(a)), Fraction(str(b))) for a, b in r["ypieces"]]) for r in plan["rows"]]
    return plan, rows

def run_rows(args):
    plan, rows = load_plan(args.plan)
    os.makedirs(os.path.join(args.out, "batches"), exist_ok=True)
    sel = list(range(len(rows))) if not args.rows else [int(v) for v in args.rows.split(",")]
    K = int(args.K)
    leg = Leg(Nc=args.Nc, m=args.m, prec=args.prec)
    started = now(); t_start = time.time()
    total_windows = sum(rows[i]["Nhi"] - rows[i]["Nlo"] + 1 for i in sel)
    done_windows = 0; errors = []; times = []
    for j, i in enumerate(sel):
        r = rows[i]
        path = os.path.join(args.out, "batches", f"arb-row_{i:04d}.json")
        if args.resume and os.path.exists(path):
            done_windows += r["Nhi"] - r["Nlo"] + 1
            print(f"[resume] row {i} present, skipped", flush=True); continue
        t0 = time.time()
        pieces = []; T_lo = None
        try:
            for (ya, yb) in r["ypieces"]:
                sb = leg.sub_box(r["Nlo"], r["Nhi"], ya, yb)
                pieces.append(sb)
                v = Fraction(sb["T_lo"])
                T_lo = v if T_lo is None else min(T_lo, v)
            E_hi, E_parts = leg.defect_window(r["Nlo"], r["Nhi"])
            T_int = floor_frac(K * T_lo); E_int = ceil_frac(K * E_hi)
            ok = (T_lo > 0) and (E_int < T_int)
            rec = dict(leg="arb", row_index=i, Nlo=str(r["Nlo"]), Nhi=str(r["Nhi"]), T=str(T_int), E=str(E_int), K=str(K), ok=ok,
                       T_lo=frac_str(T_lo), T_lo_float=float(T_lo), E_hi=frac_str(E_hi), E_hi_float=float(E_hi), E_parts=E_parts,
                       pieces=pieces, seconds=time.time() - t0, prec=args.prec, Nc=args.Nc, m=args.m, stamp=now())
            if not ok:
                errors.append(f"row {i}: T_lo={float(T_lo)} E_hi={float(E_hi)} -- floor not positive or E >= T")
        except Exception as ex:
            rec = dict(leg="arb", row_index=i, Nlo=str(r["Nlo"]), Nhi=str(r["Nhi"]), ok=False, error=repr(ex), seconds=time.time() - t0, stamp=now())
            errors.append(f"row {i}: {ex!r}")
        atomic_json(path, rec)
        times.append(time.time() - t0); done_windows += r["Nhi"] - r["Nlo"] + 1
        el = time.time() - t_start; rem = len(sel) - j - 1
        eta = rem * (sum(times) / len(times)) / 3600 if times else None
        st = dict(phase="rows", leg="arb", rows_done=j + 1, rows_total=len(sel), windows_done=done_windows, windows_total=total_windows,
                  started=started, updated=now(), elapsed_s=el, eta_hours=eta, errors=errors, last_row=rec.get("row_index"),
                  last_T=rec.get("T_lo_float"), last_E=rec.get("E_hi_float"), last_seconds=rec.get("seconds"))
        update_status(args.out, "arb", st)
        print(f"row {i:3d} [{r['Nlo']},{r['Nhi']}] pieces={len(r['ypieces'])}  T_lo={rec.get('T_lo_float')}  E_hi={rec.get('E_hi_float')}  ok={rec.get('ok')}  {rec['seconds']:.1f}s", flush=True)
    st = dict(phase="rows-done", leg="arb", rows_done=len(sel), rows_total=len(sel), windows_done=done_windows, windows_total=total_windows,
              started=started, updated=now(), elapsed_s=time.time() - t_start, eta_hours=0.0, errors=errors)
    update_status(args.out, "arb", st)
    print("rows done:", json.dumps(st), flush=True)

def run_tail(args):
    plan, rows = load_plan(args.plan)
    os.makedirs(os.path.join(args.out, "batches"), exist_ok=True)
    K = int(args.K)
    leg = Leg(Nc=args.Nc, m=args.m, prec=args.prec)
    N1 = int(plan["N1"])
    t0 = time.time()
    tr = leg.tail_row(N1, direct=args.direct)
    ints = {k: str(ceil_frac(K * Fraction(tr[k]))) for k in ("Q1", "Q2", "Q3", "Q4", "E1")}
    ssum = sum(int(v) for v in ints.values())
    ok = tr["sum_lt_2"] and all(tr["side"].values()) and ssum < 2 * K and (tr["direct"]["contained"] if args.direct else True)
    rec = dict(leg="arb", N1=str(N1), K=str(K), ints=ints, sum_int=str(ssum), lt_2K=bool(ssum < 2 * K), ok=ok, seconds=time.time() - t0, stamp=now(), **tr)
    atomic_json(os.path.join(args.out, "batches", "arb-tail.json"), rec)
    update_status(args.out, "arb", dict(phase="tail-done", leg="arb", N1=N1, ok=ok, seconds=rec["seconds"], updated=now(), errors=[] if ok else ["tail row failed"]))
    print("tail:", json.dumps({k: rec[k] for k in ("N1", "ints", "sum_int", "lt_2K", "sum_float", "side", "ok", "seconds")}), flush=True)
    if args.direct:
        print("direct:", json.dumps({k: rec["direct"][k] for k in ("contained", "Q1sum_float", "Q2sum_float", "seconds")}), flush=True)

def assemble(args):
    plan, rows = load_plan(args.plan)
    recs = []
    for i in range(len(rows)):
        p = os.path.join(args.out, "batches", f"arb-row_{i:04d}.json")
        if not os.path.exists(p):
            print(f"missing row {i}; not assembling"); sys.exit(1)
        recs.append(json.load(open(p)))
    tail = json.load(open(os.path.join(args.out, "batches", "arb-tail.json")))
    K = recs[0]["K"]
    doc = {"format": "M2a-barrier-transcript", "version": "1.0", "kind": "asymptotic", "lane": "asymptotic", "trust_label": TRUST_LABEL,
           "scales": {"K": K}, "t0": {"n": "93", "d": "500"}, "y0": {"n": "16733", "d": "100000"}, "yA": {"n": "3962323", "d": "5000000"},
           "rows": [{"Nlo": r["Nlo"], "Nhi": r["Nhi"], "T": r["T"], "E": r["E"]} for r in recs],
           "tail": {"N1": tail["N1"], **tail["ints"]},
           "producer": {"leg": "Arb/FLINT (p9_arb.py, python-flint 0.6.0)", "plan": os.path.basename(args.plan), "prec": recs[0].get("prec"), "Nc": recs[0].get("Nc"), "m": recs[0].get("m"),
                        "rows": [{k: r[k] for k in ("row_index", "T_lo", "E_hi", "E_parts", "pieces", "seconds", "ok")} for r in recs],
                        "tail": {k: tail[k] for k in ("Q1", "Q2", "Q3", "Q4", "E1", "consts", "side", "sum_float", "seconds", "ok") if k in tail},
                        "stamp": now()}}
    atomic_json(os.path.join(args.out, args.name), doc)
    print("assembled", args.name, "rows", len(recs), "all ok:", all(r["ok"] for r in recs) and tail["ok"])

def selftest(args):
    leg = Leg(Nc=args.Nc, m=args.m, prec=args.prec)
    for sp, a, b in ((Fraction(18257, 10000), 0, 30000), (Fraction(18257, 10000) - Y0, 0, 30000), (Fraction(19, 10), 15000, 40000)):
        lo, hi = leg.G(sp, a, b); dlo, dhi = leg.G_direct(sp, a, b)
        ok = lo <= dlo and dhi <= hi
        print(f"G({float(sp):.5f},{a},{b}) = [{float(lo):.12f}, {float(hi):.12f}]  direct [{float(dlo):.12f}, {float(dhi):.12f}]  width {float(hi-lo):.2e}  contains: {ok}")
        assert ok
    sig = leg.sigma_lo(N0, Y0)
    lo, hi = leg.G(sig, 0, N0)
    print(f"sum_{{n<=N0}} b_n n^-sigma at sigma_lo={float(sig):.6f}: [{float(lo):.6f}, {float(hi):.6f}]  (indicative 2.2789)")
    print("selftest OK")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["rows", "tail", "assemble", "selftest"])
    ap.add_argument("--plan"); ap.add_argument("--out", default=".")
    ap.add_argument("--resume", action="store_true"); ap.add_argument("--rows", default=""); ap.add_argument("--direct", action="store_true")
    ap.add_argument("--K", default=str(10 ** 12)); ap.add_argument("--Nc", type=int, default=10000); ap.add_argument("--m", type=int, default=2000)
    ap.add_argument("--prec", type=int, default=320); ap.add_argument("--name", default="asym-arb.json")
    args = ap.parse_args()
    {"rows": run_rows, "tail": run_tail, "assemble": assemble, "selftest": selftest}[args.mode](args)

if __name__ == "__main__":
    main()
