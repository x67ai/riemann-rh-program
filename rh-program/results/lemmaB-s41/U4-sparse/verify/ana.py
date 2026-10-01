#!/usr/bin/env python3
"""U4-sparse: per-bin analysis of an s8sp TSV (Poisson tests, queue law). Usage: ana.py file.tsv [bins_from]
Columns of s8sp: b x_lo x_hi nsteps nidle ncomp sc2 scc1 cmax se se2 emax kemax Emax om2 om3 om4 om5p viol cmpd
 | hc[16] | he[48] | (nw w1 w2) x 13."""
import sys, math
import numpy as np

def f0(tau):
    return 1.0 if tau == 0 else (1 - math.exp(-tau)) / tau

def parse(fn):
    hdr = open(fn).readline()
    kv = dict(x.split('=') for x in hdr.split() if '=' in x)
    rho = float(kv['rho']); rows = []
    for l in open(fn):
        if l.startswith('#'): continue
        parts = l.split('|'); a, hc, he, w = parts[:4]
        r_sinvp = float(parts[4]) if len(parts) > 4 else float('nan')
        a = a.split(); r = dict(b=int(a[0]), xlo=float(a[1]), xhi=float(a[2]))
        for i, k in enumerate('nsteps nidle ncomp sc2 scc1 cmax se se2 emax kemax'.split()):
            r[k] = int(a[3 + i])
        r['Emax'] = float(a[13]); r['om'] = [int(z) for z in a[14:18]]; r['viol'] = int(a[18]); r['cmpd'] = int(a[19])
        r['hc'] = np.array([int(z) for z in hc.split()]); r['he'] = np.array([int(z) for z in he.split()])
        w = [float(z) for z in w.split()]; r['win'] = [(w[3*j], w[3*j+1], w[3*j+2]) for j in range(13)]
        r['sinvp'] = r_sinvp; rows.append(r)
    return rho, kv, rows

def kappa(lam):
    """positive root of lam*(e^k - 1) = k (Cramer-Lundberg exponent, Poisson arrivals, one service per step)"""
    if lam <= 0: return float('inf')
    g = lambda k: lam * math.expm1(k) - k
    lo, hi = 1e-12, 1.0
    while g(hi) < 0: hi *= 2
    for _ in range(200):
        mid = (lo + hi) / 2
        if g(mid) < 0: lo = mid
        else: hi = mid
    return (lo + hi) / 2

def pq_stationary(lam, H=200):
    """exact stationary law of e' = max(e + c - 1, 0), c ~ Poisson(lam), by iteration"""
    from scipy.stats import poisson
    pc = poisson.pmf(np.arange(H + 2), lam)
    p = np.zeros(H); p[0] = 1.0
    for _ in range(20000):
        q = np.convolve(p, pc)[:H + 1]           # law of e + c
        nq = np.zeros(H); nq[0] = q[0] + q[1]; nq[1:H] = q[2:H + 1]
        if np.abs(nq - p).sum() < 1e-15: p = nq; break
        p = nq
    return p

def step_weighted_f0(rho, xlo, xhi, n=200):
    xs = np.linspace(xlo, xhi, n); return float(np.mean([f0(rho * math.log(x)) for x in xs]))

if __name__ == '__main__':
    fn = sys.argv[1]; b0 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    rho, kv, rows = parse(fn)
    print(f"# {fn}  rho={rho:.6g}  mode={kv['mode']}  audits={kv['audits']} flips={kv['flips']} unresolved={kv['unresolved']}")
    print("# tau_hi  nsteps  phi  f0w  lam  D1  P0/e^-l  lag1  meanE  MD1(lam)  tail  kappa  emax  supE_cum  viol/cmpd")
    supE = -1e9
    for r in rows:
        supE = max(supE, r['Emax'])
        if r['b'] < b0 or r['nsteps'] < 50: continue
        n = r['nsteps']; lam = r['ncomp'] / n; phi = r['nidle'] / n
        var = r['sc2'] / n - lam ** 2; D1 = var / lam if lam > 0 else float('nan')
        lag1 = (r['scc1'] / n - lam ** 2) / var if var > 0 else float('nan')
        P0 = r['hc'][0] / n; me = r['se'] / n; md1 = lam ** 2 / (2 * (1 - lam)) if lam < 1 else float('inf')
        he = r['he'][:-1].astype(float); tail = np.cumsum(he[::-1])[::-1] + r['he'][-1]; tail = tail / n
        hs = [h for h in range(1, 47) if tail[h] * n >= 30 and tail[h] < 0.2]
        slope = -np.polyfit(hs, np.log(tail[hs]), 1)[0] if len(hs) >= 3 else float('nan')
        print(f"{rho*math.log(r['xhi']):.4f} {n:>11d} {phi:.4f} {step_weighted_f0(rho, r['xlo'], r['xhi']):.4f} "
              f"{lam:.4f} {D1:.4f} {P0/math.exp(-lam):.4f} {lag1:+.4f} {me:.4f} {md1:.4f} {slope:.3f} {kappa(lam):.3f} "
              f"{r['emax']:>4d} {supE:8.4f} {r['viol']}/{r['cmpd']}")
