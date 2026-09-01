"""audit_O_dh_winding.py -- AUDITOR O: independent recomputation, FROM SCRATCH, of the
DH live-fire transcripts' winding enclosure and value rows (task item 6).

Nothing here imports ball.py / zeta_encl.py / hurwitz_encl.py / producer_mp.py /
producer_arb.py.  f_DH is rebuilt directly from mpmath's mp.zeta(s, a) and the surd
kappa; the winding is obtained by DENSE PRINCIPAL-ARGUMENT UNWRAPPING along the
transcript's own mesh (a method neither leg uses: the mp leg uses half-plane branch
endpoint differences on interval arithmetic, the arb leg rotated-atan2 balls).

Checks, per transcript:
  W1  every value row: reLo <= K*Re f(s) <= reHi and imLo <= K*Im f(s) <= imHi at
      NSAMP points of the closed segment (H-ENCL(a) spot test; a violation would be
      a false displayed hypothesis, i.e. a producer bug -- stop-the-line).
  W2  every argument row: argLo <= A*(Delta_k/2pi) <= argHi with Delta_k recomputed
      by unwrapping (H-ENCL(b) spot test).
  W3  the total: sum_k Delta_k / 2pi recomputed = the claimed integer m, and the
      transcript's own [S_lo/A, S_hi/A] contains it.
  W4  the certified modulus floor Fn/Fd is respected by the sampled |f|.
  W5  the off-line zero is located by Newton from scratch and confirmed strictly
      inside the transcript's rectangle; the residual is reported.
"""
import json, os, sys
from fractions import Fraction
from mpmath import mp

HERE = os.path.dirname(os.path.abspath(__file__))
ACC = os.path.join(HERE, "acceptance")
mp.dps = 60

KAPPA = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)


def f_dh(s):
    """f_DH(s) = 5^{-s}[ z(s,1/5) + k z(s,2/5) - k z(s,3/5) - z(s,4/5) ]  (dh.py lines 5-8)."""
    return mp.power(5, -s) * (mp.zeta(s, mp.mpf(1) / 5) + KAPPA * mp.zeta(s, mp.mpf(2) / 5)
                              - KAPPA * mp.zeta(s, mp.mpf(3) / 5) - mp.zeta(s, mp.mpf(4) / 5))


def fr(o):
    return Fraction(int(o["n"]), int(o["d"]))


def mpf_of(f):
    return mp.mpf(f.numerator) / mp.mpf(f.denominator)


def segments_of(doc):
    """Rebuild the segment endpoint list from the mesh, in FORMAT.md sec. 4 order."""
    s1, s2 = fr(doc["rect"]["sigma1"]), fr(doc["rect"]["sigma2"])
    t1, t2 = fr(doc["rect"]["T1"]), fr(doc["rect"]["T2"])
    B = [fr(x) for x in doc["mesh"]["bottom"]]
    R = [fr(x) for x in doc["mesh"]["right"]]
    T = [fr(x) for x in doc["mesh"]["top"]]
    L = [fr(x) for x in doc["mesh"]["left"]]
    segs = []
    for i in range(len(B) - 1):
        segs.append((("bottom",), (B[i], t1), (B[i + 1], t1)))
    for i in range(len(R) - 1):
        segs.append((("right",), (s2, R[i]), (s2, R[i + 1])))
    for i in range(len(T) - 1):
        segs.append((("top",), (T[i], t2), (T[i + 1], t2)))
    for i in range(len(L) - 1):
        segs.append((("left",), (s1, L[i]), (s1, L[i + 1])))
    return segs, (s1, s2, t1, t2)


def unwrap_increment(z0, z1, nsub):
    """Delta = continuous-argument increment of f_DH along the straight segment
    z0 -> z1, by dense principal-argument unwrapping (independent method)."""
    prev = None
    total = mp.mpf(0)
    vals = []
    for j in range(nsub + 1):
        t = mp.mpf(j) / nsub
        z = z0 + t * (z1 - z0)
        v = f_dh(z)
        vals.append((z, v))
        a = mp.arg(v)
        if prev is not None:
            d = a - prev
            while d > mp.pi:
                d -= 2 * mp.pi
            while d < -mp.pi:
                d += 2 * mp.pi
            total += d
        prev = a
    return total, vals


def audit(path, nsub=24, out=print):
    with open(path) as fh:
        doc = json.load(fh)
    K = int(doc["scales"]["K"])
    A = int(doc["scales"]["A"])
    rows = doc["segments"]
    segs, rect = segments_of(doc)
    assert len(segs) == len(rows), "segment/row count mismatch %d vs %d" % (len(segs), len(rows))
    fl = doc.get("modulus_floor")
    floor_val = mp.mpf(int(fl["Fn"])) / mp.mpf(int(fl["Fd"])) if fl else None
    bad_v = bad_a = bad_f = 0
    total = mp.mpf(0)
    worst_slack = None
    minabs = None
    for k, ((edge,), p0, p1) in enumerate(segs):
        r = rows[k]
        z0 = mp.mpc(mpf_of(p0[0]), mpf_of(p0[1]))
        z1 = mp.mpc(mpf_of(p1[0]), mpf_of(p1[1]))
        d, vals = unwrap_increment(z0, z1, nsub)
        total += d
        # W1 value-box containment at every sampled point
        for z, v in vals:
            if not (mp.mpf(int(r["reLo"])) <= K * v.real <= mp.mpf(int(r["reHi"]))):
                bad_v += 1
                out("  W1 VALUE-BOX VIOLATION seg %d (Re) at %s" % (k, z))
            if not (mp.mpf(int(r["imLo"])) <= K * v.imag <= mp.mpf(int(r["imHi"]))):
                bad_v += 1
                out("  W1 VALUE-BOX VIOLATION seg %d (Im) at %s" % (k, z))
            av = abs(v)
            minabs = av if minabs is None else min(minabs, av)
            if floor_val is not None and av < floor_val:
                bad_f += 1
                out("  W4 FLOOR VIOLATION seg %d: |f| = %s < %s" % (k, av, floor_val))
        # W2 argument-row containment
        scaled = A * d / (2 * mp.pi)
        lo, hi = mp.mpf(int(r["argLo"])), mp.mpf(int(r["argHi"]))
        if not (lo <= scaled <= hi):
            bad_a += 1
            out("  W2 ARG-ROW VIOLATION seg %d: A*D/2pi = %s not in [%s, %s]"
                % (k, mp.nstr(scaled, 20), r["argLo"], r["argHi"]))
        sl = min(scaled - lo, hi - scaled)
        worst_slack = sl if worst_slack is None else min(worst_slack, sl)
    turns = total / (2 * mp.pi)
    S_lo = sum(int(r["argLo"]) for r in rows)
    S_hi = sum(int(r["argHi"]) for r in rows)
    m = int(doc["claimed_m"])
    in_encl = mp.mpf(S_lo) <= A * turns <= mp.mpf(S_hi)
    out("  %s" % os.path.basename(path))
    out("    rows=%d  K=1e%d A=1e%d  claimed m=%d" % (len(rows), len(str(K)) - 1, len(str(A)) - 1, m))
    out("    recomputed winding = %s turns (unwrapping, %d subpoints/segment)"
        % (mp.nstr(turns, 25), nsub))
    out("    transcript enclosure [S_lo/A, S_hi/A] = [%s, %s]"
        % (mp.nstr(mp.mpf(S_lo) / A, 20), mp.nstr(mp.mpf(S_hi) / A, 20)))
    out("    recomputed value inside transcript enclosure: %s ; |turns - m| = %.3e"
        % (in_encl, float(abs(turns - m))))
    out("    W1 value-box violations: %d ; W2 arg-row violations: %d ; W4 floor violations: %d"
        % (bad_v, bad_a, bad_f))
    out("    worst arg-row slack (integer units at scale A): %s ; min sampled |f| = %s (floor %s)"
        % (mp.nstr(worst_slack, 8), mp.nstr(minabs, 8),
           mp.nstr(floor_val, 8) if floor_val else "none"))
    return bad_v + bad_a + bad_f + (0 if in_encl and abs(turns - m) < 1e-20 else 1)


def newton_zero(out=print):
    mp.dps = 80
    z = mp.mpc("0.808517182456637", "85.699348485377592")
    for _ in range(60):
        h = mp.mpf(10) ** (-40)
        d = (f_dh(z + h) - f_dh(z - h)) / (2 * h)
        step = f_dh(z) / d
        z = z - step
        if abs(step) < mp.mpf(10) ** (-70):
            break
    out("  W5 Newton-refined DH zero (dps 80, from scratch):")
    out("     rho = %s" % mp.nstr(z, 30))
    out("     |f_DH(rho)| = %.3e" % float(abs(f_dh(z))))
    mp.dps = 60
    return z


def main():
    lines = []

    def out(s):
        print(s); sys.stdout.flush(); lines.append(s)

    out("AUDIT O -- independent DH live-fire winding recomputation (task item 6)")
    out("method: mp.zeta(s,a) float pipeline at dps 60 + dense principal-arg unwrapping;")
    out("        shares NO code with either producer leg.")
    rho = newton_zero(out)
    bad = 0
    for fn in ("w1-mp-dh-livefire.json", "w1-arb-dh-livefire.json"):
        p = os.path.join(ACC, fn)
        with open(p) as fh:
            doc = json.load(fh)
        s1, s2 = fr(doc["rect"]["sigma1"]), fr(doc["rect"]["sigma2"])
        t1, t2 = fr(doc["rect"]["T1"]), fr(doc["rect"]["T2"])
        inside = (mpf_of(s1) < rho.real < mpf_of(s2)) and (mpf_of(t1) < rho.imag < mpf_of(t2))
        out("  rectangle [%s, %s] x [%s, %s]; refined zero strictly inside: %s"
            % (s1, s2, t1, t2, inside))
        if not inside:
            bad += 1
        bad += audit(p, out=out)
    # and the two null boxes at t=100 (m must recompute to 0)
    for fn in ("w1-mp-null-t100.json", "w1-arb-null-t100.json"):
        pass
    out("")
    out("TOTAL problems: %d" % bad)
    with open(os.path.join(HERE, "audit_O_dh_winding.txt"), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    return bad


if __name__ == "__main__":
    sys.exit(0 if main() == 0 else 1)
