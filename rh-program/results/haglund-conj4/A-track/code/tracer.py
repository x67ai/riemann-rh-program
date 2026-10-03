# tracer.py -- A-track: follow a branch of zeros of the pencil Xi_k + t Phi_{k+1} as the level curve Im S_k = 0,
# u = Re S_k decreasing from 1 (forward) or increasing to 1 (backward). Successor of orch-probe/trace.py (orchestrator):
# arc-length predictor along the tangent, chord-Newton corrector along the normal, step control by corrector size and by
# the turning angle of the tangent; S' by an Arb central difference (a_core.SdS).
import math, cmath, time
from a_core import *
from axis import crit, Sx

def newton_S(k, z, target, route="T", it=60, tol=1e-14):
    """solve S_k(z) = target (complex Newton with the Arb central-difference derivative)."""
    for _ in range(it):
        s, d = SdS(k, z, route)
        dz = (s - target) / d
        z = z - dz
        if abs(dz) < tol * max(1.0, abs(z)):
            return z, True
    return z, False

def trace(k, z0, direction=-1, h0=0.25, turnmax=0.12, route="T", ymin=1e-6, xedge=None, ytop=1e4, maxsteps=40000,
          keep_path=True):
    """direction -1: u decreasing (t increasing) from u ~ 1; +1: u increasing (backward).
    Returns a dict: end type ('u0' = reached u = 0, a zero of Xi_{k+1}; 'u1' = reached u = 1, a zero of Xi_k;
    'landed' = reached the real axis; 'exit-right'; 'exit-top'; 'maxsteps'), the end, worst step increase of Im z
    (in the direction of increasing t), smallest margin -Im S'/|S'| above ymin, steps, largest turning angle."""
    t0 = time.time()
    z = complex(z0)
    s, d = SdS(k, z, route)
    worst_dy = -float("inf")
    min_margin = float("inf")
    min_margin_at = None
    max_turn = 0.0
    path = [(s.real, z.real, z.imag)]
    h = h0
    steps = 0
    nrej = 0
    end = None
    target = 0.0 if direction < 0 else 1.0
    while steps < maxsteps:
        tau = direction * (d.conjugate() / abs(d))       # direction -1: -conj(d)/|d|  (u decreasing)
        hh = min(h, h0, 0.3 * z.imag) if z.imag > 0 else min(h, h0)
        zp = z + hh * tau
        conv = False
        corr_tot = 0.0
        dd = d
        zprev, sprev = None, None
        for _ in range(12):
            sp = Sc(k, zp, route, 60)
            if zprev is not None and zp != zprev:
                dd = (sp - sprev) / (zp - zprev)        # secant update along the correction direction
            c = -1j * sp.imag / dd
            zprev, sprev = zp, sp
            zp = zp + c
            corr_tot += abs(c)
            if abs(c) < 1e-13 * max(1.0, abs(zp)):
                conv = True
                break
        if not conv or corr_tot > 0.25 * hh:
            h = hh / 2
            nrej += 1
            if h < 1e-12:
                end = "stuck"
                break
            continue
        sn, dn = SdS(k, zp, route)
        taun = direction * (dn.conjugate() / abs(dn))
        turn = abs(cmath.phase(taun / tau))
        if turn > turnmax and hh > 1e-9:
            h = hh / 2
            nrej += 1
            continue
        # reached the target level u = 0 (forward) or u = 1 (backward)?
        if (direction < 0 and sn.real <= 0) or (direction > 0 and sn.real >= 1):
            zt, ok = newton_S(k, z + (abs(s.real - target) / abs(d)) * tau, target, route)
            st, dt = SdS(k, zt, route)
            dy = (zt.imag - z.imag) * (-direction)       # increase of Im z in the direction of increasing t
            worst_dy = max(worst_dy, dy)
            z, s, d = zt, st, dt
            path.append((s.real, z.real, z.imag))
            end = "u0" if direction < 0 else "u1"
            if not ok:
                end += "-newton-unconverged"
            steps += 1
            break
        dy = (zp.imag - z.imag) * (-direction)
        worst_dy = max(worst_dy, dy)
        max_turn = max(max_turn, turn)
        z, s, d = zp, sn, dn
        steps += 1
        if keep_path:
            path.append((s.real, z.real, z.imag))
        if z.imag > ymin:
            m = -d.imag / abs(d)
            if m < min_margin:
                min_margin, min_margin_at = m, (z.real, z.imag, s.real)
        if turn < turnmax / 4 and corr_tot < 0.02 * hh:
            h = min(h0, hh * 1.6)
        else:
            h = hh
        if z.imag < ymin:
            end = "landed"
            break
        if xedge is not None and z.real > xedge:
            end = "exit-right"
            break
        if z.imag > ytop:
            end = "exit-top"
            break
    if end is None:
        end = "maxsteps"
    res = {"k": k, "start": [z0.real, z0.imag], "direction": direction, "end": end, "z_end": [z.real, z.imag],
           "u_end": s.real, "worst_dy": worst_dy, "min_margin": min_margin, "min_margin_at": min_margin_at,
           "max_turn": max_turn, "steps": steps, "rejections": nrej, "h0": h0, "turnmax": turnmax, "route": route,
           "secs": round(time.time() - t0, 3)}
    if end == "landed":
        x = z.real
        w = max(50 * z.imag, 1e-5)
        xs = None
        for _ in range(6):
            xs = crit(k, x - w, x + w, route)
            if xs is not None:
                break
            w *= 4
        if xs is not None:
            res["x_land"] = xs
            res["u_land"] = Sx(k, xs, route)[0]
    if keep_path:
        res["path"] = path
    return res
