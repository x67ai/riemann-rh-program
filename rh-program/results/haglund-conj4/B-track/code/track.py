"""Q1/Q2: follow zeros of F_k(z,t) = Xi_k + t Phi_{k+1} = A(z) - u B(z), u = 1 - t = e^{-tau},
by Newton continuation on the fixed grid tau_j = j*dtau, j = 0..J (tau_J >= tau_max), then t = 1 (u = 0).
Per grid value: z, Im(dz/dt) = -Im(B/F'), F' = A' - u B'.  Sub-steps (not recorded) are taken when a step fails."""
import sys, json, time
sys.path.insert(0, '.')
import mpmath as mp, hb

def FdF(k, z, u):
    A, B = hb.AB(k, z)
    h = mp.mpf(2)**(-mp.mp.prec//2)*max(1, abs(z))
    A2, B2 = hb.AB(k, z + h)
    F = A - u*B
    dF = ((A2 - u*B2) - F)/h
    return F, dF, B

def newton_u(k, zp, u, maxit=6, acc=mp.mpf('1e-7')):
    """Newton at fixed u from zp; accept when a step is < acc (then the error is ~acc^2)."""
    z = zp
    for it in range(maxit):
        F, dF, B = FdF(k, z, u)
        step = F/dF
        z = z - step
        if abs(step) < acc:
            return z, dF, B, it + 1, True
    return z, dF, B, maxit, False

def landing(k, zc, uc, half=1.5, step=0.05):
    """the local max x* of S = A/B on the real axis nearest to Re zc; u* = S(x*), tau* = -ln u*;
    quadratic model: Im z ~ sqrt(2 (u - u*)/|S''(x*)|) for u slightly above u*."""
    from realaxis import SdS, bis_dS
    x0 = mp.re(zc)
    xs = [x0 - half + i*step for i in range(int(2*half/step) + 1)]
    vals = [SdS(k, x) for x in xs]
    best = None
    for i in range(len(xs) - 1):
        if vals[i][1] > 0 and vals[i + 1][1] < 0:
            xm, Vm = bis_dS(k, xs[i], xs[i + 1], vals[i], vals[i + 1])
            if best is None or abs(xm - x0) < abs(best[0] - x0):
                best = (xm, Vm)
    if best is None:
        return dict(found=False)
    xm, Vm = best
    us = Vm[0]
    hh = mp.mpf('1e-4')
    S2 = (SdS(k, xm + hh)[0] - 2*us + SdS(k, xm - hh)[0])/hh**2
    pred = mp.sqrt(2*(uc - us)/abs(S2)) if uc > us else mp.mpf(-1)
    return dict(found=True, x_star=mp.nstr(xm, 15), u_star=mp.nstr(us, 15),
                tau_star=(float(-mp.log(us)) if us > 0 else None), S2=mp.nstr(S2, 6),
                uc=mp.nstr(uc, 15), uc_gt_ustar=bool(uc > us), im_model_at_c=mp.nstr(pred, 6))

def follow(k, z0, dtau, tau_max, ylow=mp.mpf('0.02'), log=None):
    J = int(mp.ceil(tau_max/dtau))
    taus = [j*dtau for j in range(J + 1)]
    # refine the start at u = 1
    z, dF, B, it, ok = newton_u(k, mp.mpc(z0), mp.mpf(1))
    rec = [dict(tau=0.0, z=[mp.nstr(mp.re(z), 17), mp.nstr(mp.im(z), 17)],
                imdzdt=float(-mp.im(B/dF)))]
    zdot = -B/dF                          # dz/dtau at u = 1
    tc = mp.mpf(0); zc = z
    nsub = 0; status = 'running'; worst_up = None; pos = []
    for j in range(1, J + 1):
        target = mp.mpf(taus[j])
        while tc < target:
            h = target - tc
            while True:
                zp = zc + h*zdot
                u = mp.exp(-(tc + h))
                znew, dF, B, it, ok = newton_u(k, zp, u)
                corr = abs(znew - zp); move = abs(znew - zc)
                if ok and corr <= 0.1*move + mp.mpf('1e-9') and mp.im(znew) > 0:
                    break
                h = h/2; nsub += 1
                if h < dtau*mp.mpf('1e-4'):
                    status = 'stalled'; break
            if status == 'stalled':
                break
            tc = tc + h; zc = znew
            zdot = -u*B/dF
        if status == 'stalled':
            break
        imdzdt = -mp.im(B/dF)
        dy = mp.im(zc) - mp.mpf(rec[-1]['z'][1])
        if worst_up is None or dy > worst_up: worst_up = dy
        if imdzdt > 0: pos.append(float(target))
        rec.append(dict(tau=float(target), z=[mp.nstr(mp.re(zc), 17), mp.nstr(mp.im(zc), 17)],
                        imdzdt=float(imdzdt)))
        if mp.im(zc) < ylow:
            status = 'near-axis'; break
    end = None; land = None
    if status in ('stalled', 'near-axis') and mp.im(zc) < 1:
        status = 'axis-approach'
        land = landing(k, zc, mp.exp(-tc))
        land['tau_c'] = float(tc); land['z_c'] = [mp.nstr(mp.re(zc), 17), mp.nstr(mp.im(zc), 17)]
    if status == 'running':
        # t = 1: Newton on A = Xi_{k+1}
        zf, dF, B, it, ok = newton_u(k, zc, mp.mpf(0))
        end = [mp.nstr(mp.re(zf), 17), mp.nstr(mp.im(zf), 17)]
        status = 'end-t1' if ok else 'end-t1-noconv'
    return dict(start=rec[0]['z'], status=status, last=rec[-1], end_t1=end, landing=land, n_grid=len(rec),
                n_substeps=nsub, worst_increase_Im=(float(worst_up) if worst_up is not None else None),
                grid_pos_imdzdt=pos, records=rec)

if __name__ == '__main__':
    k = int(sys.argv[1]); dtau = float(sys.argv[2]); starts_file = sys.argv[3]; out = sys.argv[4]
    mp.mp.dps = int(sys.argv[5]) if len(sys.argv) > 5 else 30
    extra = float(sys.argv[6]) if len(sys.argv) > 6 else 12.0
    tau_max = float(mp.pi*(2*k + 3) + extra)
    starts = json.load(open(starts_file))
    res = []
    t0 = time.time()
    for i, s in enumerate(starts):
        z0 = mp.mpc(s[0], s[1])
        r = follow(k, z0, mp.mpf(dtau), tau_max)
        res.append(r)
        print(i, r['start'], r['status'], r['last']['tau'], r['last']['z'], r['end_t1'], 'worst dIm %.3e' % (r['worst_increase_Im'] or 0),
              'pos', len(r['grid_pos_imdzdt']), 'sub', r['n_substeps'], '%.0f s' % (time.time() - t0)); sys.stdout.flush()
        json.dump(dict(k=k, dtau=dtau, tau_max=tau_max, dps=mp.mp.dps, branches=res), open(out, 'w'))
