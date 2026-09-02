#!/usr/bin/env python3
"""AUDIT (independent of both producers): direct evaluation of P15's f_t (eq. (92)/(14) with the overline reading,
p6 and p46 of fetched/p3-22a4) with python-flint acb balls at 256 bits, term by term (N0 = 630783 terms per sum),
at FRESH points of the row-2 barrier boundary; containment against the transcripts' value boxes (K scale),
argument rows (A scale, via Arg(f(w)/f(z)) -- valid because C-B6 puts the segment's image in an open half-plane
missing 0) and the modulus floor.  No code from producer_arb.py / ft_mp.py / producer_mp.py is imported.

Formulas (P15 arXiv v2, PDF page = printed page):
  (9) p4   alpha(s) = 1/(2s) + 1/(s-1) + (1/2) Log(s/(2 pi))
  (7) p4   log M0(s) = Log s + Log(s-1) - (s/2) log pi + log(sqrt(2 pi)/16) + (s/2 - 1/2) Log(s/2) - s/2
  (10),(16) gamma = exp((t/4)(alpha(s-)^2 - alpha(s+)^2) + log M0(s-) - log M0(s+)),  s+ = (1+y-ix)/2, s- = (1-y+ix)/2
  (92) p46 f_t = sum_{n<=N} b_n n^{-s*} + gamma sum_{n<=N} b_n n^{-s**},  s* = s+ + (t/2)alpha(s+), s** = s- + (t/2)alpha(s-)
  (15) p6  b_n = exp((t/4) log^2 n)
"""
import json, sys, time
from fractions import Fraction as Fr
from flint import acb, arb, ctx
ctx.prec = 256
N0 = 630783
PI = arb.pi()

def alpha(s):
    return 1/(2*s) + 1/(s-1) + (s/(2*PI)).log()/2

def logM0(s):
    return s.log() + (s-1).log() - s/2*PI.log() + ((2*PI).sqrt()/16).log() + (s/2 - acb(1)/2)*(s/2).log() - s/2

def fr2arb(q):
    return arb(q.numerator)/arb(q.denominator)

LOGS = None
def prep():
    global LOGS
    t0 = time.time()
    LOGS = [None] + [arb(n).log() for n in range(1, N0+1)]
    print(f"# precomputed {N0} logs in {time.time()-t0:.1f}s", flush=True)

def f_direct(x, y, t):
    """x, y, t exact Fractions; returns (f, gamma) as acb balls."""
    z = acb(fr2arb(x), fr2arb(y)); ta = fr2arb(t)
    sp = (1 - acb(0,1)*z)/2; sm = (1 + acb(0,1)*z)/2
    sst = sp + ta/2*alpha(sp); sst2 = sm + ta/2*alpha(sm)
    gam = (ta/4*(alpha(sm)**2 - alpha(sp)**2) + logM0(sm) - logM0(sp)).exp()
    S1 = acb(0); S2 = acb(0); q = ta/4
    for n in range(2, N0+1):
        L = LOGS[n]; bt = q*L*L
        S1 += (bt - sst*L).exp()
        S2 += (bt - sst2*L).exp()
    S1 += 1; S2 += 1
    return S1 + gam*S2, gam

def segments(rect, mesh):
    x1, x2, y1, y2 = rect
    segs = []
    b, r, tp, l = mesh["bottom"], mesh["right"], mesh["top"], mesh["left"]
    for i in range(len(b)-1): segs.append(((b[i], y1), (b[i+1], y1)))
    for i in range(len(r)-1): segs.append(((x2, r[i]), (x2, r[i+1])))
    for i in range(len(tp)-1): segs.append(((tp[i], y2), (tp[i+1], y2)))
    for i in range(len(l)-1): segs.append(((x1, l[i]), (x1, l[i+1])))
    return segs

def rat(o): return Fr(int(o["n"]), int(o["d"]))

def check_prism(path, rect, seg_ids, label):
    p = json.load(open(path))
    K = int(p["scales"]["K"]); A = int(p["scales"]["A"]); tau = rat(p["seam"])
    mesh = {e: [rat(r) for r in p["mesh"][e]] for e in p["mesh"]}
    segs = segments(rect, mesh); rows = p["segments"]
    Fn, Fd = int(p["modulus_floor"]["Fn"]), int(p["modulus_floor"]["Fd"])
    assert len(segs) == len(rows)
    print(f"\n== {label}: seam {tau} ({float(tau):.6f}), K={K:.0e}, A={A:.0e}, floor {Fn}/{Fd} = {Fn/Fd:.6f}, {len(rows)} rows", flush=True)
    nfail = 0
    for k in seg_ids:
        (zx, zy), (wx, wy) = segs[k]; row = rows[k]
        reLo, reHi, imLo, imHi, aLo, aHi = (int(row[f]) for f in ("reLo","reHi","imLo","imHi","argLo","argHi"))
        vals = {}
        for lam in (Fr(0), Fr(37,100), Fr(1)):
            x = zx + lam*(wx-zx); y = zy + lam*(wy-zy)
            t0_ = time.time(); f, gam = f_direct(x, y, tau); dt = time.time()-t0_
            vals[lam] = f
            Kre = arb(K)*f.real; Kim = arb(K)*f.imag
            in_re = (arb(reLo) <= Kre) and (Kre <= arb(reHi)); in_im = (arb(imLo) <= Kim) and (Kim <= arb(imHi))
            fl = abs(f) >= arb(Fn)/arb(Fd)
            ok = in_re and in_im and fl
            if not ok: nfail += 1
            print(f"  seg {k:3d} lam={float(lam):.2f} z=({float(x-rect[0]):.6f}+X, {float(y):.6f}) f={f.real.str(12)}+{f.imag.str(12)}i "
                  f"|f|={abs(f).str(8)} rad={f.rad().str(3)} box_re={'OK' if in_re else 'FAIL'} box_im={'OK' if in_im else 'FAIL'} floor={'OK' if fl else 'FAIL'} ({dt:.1f}s)", flush=True)
        # argument row: A * Arg(f(w)/f(z)) / (2 pi) in [aLo, aHi]
        d = arb(A) * (vals[Fr(1)] / vals[Fr(0)]).arg() / (2*PI)
        in_arg = (arb(aLo) <= d) and (d <= arb(aHi))
        if not in_arg: nfail += 1
        print(f"  seg {k:3d} argrow [{aLo},{aHi}] direct A*dArg/2pi = {d.str(15)} -> {'OK' if in_arg else 'FAIL'}", flush=True)
    print(f"== {label}: {'ALL CONTAINED' if nfail == 0 else f'{nfail} FAILURES'}", flush=True)
    return nfail

if __name__ == "__main__":
    P = sys.argv[1]
    X = 5000000194858
    rect = (Fr(X), Fr(X+1), Fr(16733, 100000), Fr(1))
    prep()
    tot = 0
    # mp leg: mesh 51/43/51/43 -> segments bottom 0..49, right 50..91, top 92..141, left 142..183
    tot += check_prism(P+"/transcripts/row2/prism-0017.json", rect, [7, 63, 113, 172], "mp prism 17")
    # Arb leg prism 40: mesh 62/23/17/23 -> bottom 0..60, right 61..82, top 83..98, left 99..120
    tot += check_prism(P+"/transcripts/row2-arb/instance02-prism-0040.json", rect, [11, 70, 90, 110], "arb prism 40")
    tot += check_prism(P+"/transcripts/row2/prism-0000.json", rect, [23, 160], "mp prism 0")
    # Arb prism 0: mesh 201/33/17/42 -> bottom 0..199, right 200..231, top 232..247, left 248..288
    tot += check_prism(P+"/transcripts/row2-arb/instance02-prism-0000.json", rect, [137, 240], "arb prism 0")
    tot += check_prism(P+"/transcripts/row2/prism-0038.json", rect, [40, 150], "mp prism 38")
    tot += check_prism(P+"/transcripts/row2-arb/instance02-prism-0071.json", rect, [3, 50], "arb prism 71")
    print(f"\nTOTAL FAILURES: {tot}")
