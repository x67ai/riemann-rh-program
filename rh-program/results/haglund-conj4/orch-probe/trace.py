# trace.py -- follow one branch of the pencil Xi_k + t Phi_{k+1} as the level curve Im S_k = 0 (S_k = Xi_{k+1}/Phi_{k+1}, u = 1 - t = S_k).
from c4probe import *

def newton_zero(k, z, target=0.0, route="T", it=40):
    """solve S_k(z) = target by Newton with a numerical derivative."""
    for _ in range(it):
        s, d = cSd(k, z, route)
        dz = (s - target) / d
        z -= dz
        if abs(dz) < 1e-13 * max(1.0, abs(z)):
            break
    return z

def trace(k, z0, ds=0.05, route="T", ymin=1e-5, maxsteps=200000, log=None):
    """from a zero z0 of Xi_k (S_k = 1) follow Im S_k = 0 with u = Re S_k decreasing, until u = 0 (a zero of Xi_{k+1})
    or the real axis (a landing).  Returns (end_type, end_z, end_u, worst), where worst = max over steps of the increase of y
    (positive means the imaginary part went UP somewhere), and the list of (u, x, y, Im S')."""
    z = complex(z0)
    path = []
    worst = -1e300
    up_events = []
    s, d = cSd(k, z, route)
    for step in range(maxsteps):
        u = s.real
        path.append((u, z.real, z.imag, d.imag))
        if d.imag > 0 and z.imag > ymin:
            up_events.append((u, z.real, z.imag, d.imag))
        h = min(ds, max(z.imag * 0.25, ymin * 0.5))
        tdir = -(1 / d) / abs(1 / d)          # direction of decreasing u
        # do not overshoot u = 0
        du_pred = h * abs(d)
        if u - du_pred < 0:
            zf = newton_zero(k, z + tdir * (u / abs(d)), 0.0, route)
            sf, df = cSd(k, zf, route)
            path.append((sf.real, zf.real, zf.imag, df.imag))
            worst = max(worst, zf.imag - z.imag)
            return "nonreal-end", zf, 0.0, worst, path, up_events
        zn = z + tdir * h
        for _ in range(3):                    # corrector: make S real, moving along the normal
            sn = cS(k, zn, route)
            zn = zn - 1j * sn.imag / d
        sn, dn = cSd(k, zn, route)
        worst = max(worst, zn.imag - z.imag)
        z, s, d = zn, sn, dn
        if z.imag < ymin:
            return "landed", z, s.real, worst, path, up_events
    return "maxsteps", z, s.real, worst, path, up_events
