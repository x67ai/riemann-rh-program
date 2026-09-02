#!/usr/bin/env python3
"""convert_gomila_log.py -- exact conversion of Gomila's sealed 883-prism barrier log
(barrier/certificates/barrier_target_closed.log at commit a74738d; SHA-256 2d010f70...05f4, identical at ea09b2f) into
(a) an exact-rational SCALAR table per prism (the mapping below, outward rounding everywhere), (b) a SPEC.md-shaped
CHAIN (manifest-level data: rectangle, t0, the 883 seams as exact rationals), and (c) an exact-arithmetic REPLAY of
the claimant's own gate (BARRIER_CERTIFICATE.md eq. (1)) from the printed numbers, plus the correspondence to the
SPEC C-B12 gate.  Everything below is exact `fractions.Fraction`; no float enters any verdict.

WHAT THE LOG CONTAINS (one line per prism; the C source prints only these summaries -- SPEC.md section 11):
  Prism(k) t=[lo,hi] winding=[mid +/- rad] min_mesh=[mid +/- rad] Dz=<int> Dt=<int> spatial=<ball or decimal>
           time=[mid +/- rad] eps=[mid +/- rad] margin=[mid +/- rad] mesh=<int> PASS
Each `[m +/- r]` is an Arb ball printed in decimal: the true value lies in [m - r, m + r] (Arb prints outward-rounded
decimal balls, arb_get_str with ARB_STR_MORE unset rounds the radius UP -- we additionally widen every printed
radius by one unit in its last printed digit, and treat a bare decimal as a ball of radius one unit in its last
digit, so the conversion is outward in every direction).

MAPPING to the SPEC vocabulary (recorded; the per-SEGMENT rows are NOT derivable from the log -- SPEC section 11):
  seam tau_k        := the exact rational lo-midpoint of prism k's t-ball  (prism 1: exactly 0; prism 883's hi is
                       exactly 129/800 up to 2e-35); for the chain we take tau_k := mid(lo ball of prism k) as
                       printed (an exact decimal = exact rational), and verify tau_{k+1} == mid(hi ball of prism k)
                       (same printed digits); Delta_k^+ := (hi_mid + hi_rad) - (lo_mid - lo_rad) is the OUTWARD
                       prism length used in the replayed gate;
  floor M_k          := min_mesh (their minimum lower modulus over the mesh POINTS -- a point floor, NOT the whole-
                       segment hull floor Fn/Fd of SPEC C-B11; the SPEC floor is smaller by the hull term);
  D_z, D_t           := printed integers (their box-uniform derivative bounds, DERIVATIVE_BOX_LEMMA.md);
  spatial_k          := D_z/(2(num-1)) with num - 1 = mesh/4 segments per edge (their eq. (1); `mesh` counts the
                       segments of the closed traversal) -- replayed here from D_z and mesh and REQUIRED to equal the
                       printed `spatial` (within its printed radius);
  time_k             := D_t * Delta_k -- replayed from D_t and the OUTWARD Delta_k^+;
  eps                := 0.00125 (their allowance for |H/B - f|; uniform_error_256.log certifies 3.5653e-4 < 0.00125);
  SPEC correspondence: C-B12 (E + D)/K < Fn/Fd with E := eps, D := time_k, Fn/Fd := M_k - spatial_k  -- i.e. their
                       (1) is exactly C-B12 with the mesh term moved into the hull floor (SPEC section 11 row 3).
  REPLAYED GATE      := M_k^- > spatial_k^+ + D_t * Delta_k^+ + eps^+   (every term in its conservative direction).

usage: convert_gomila_log.py <barrier_target_closed.log> <out-dir>
writes: gomila-scalars.json (per prism, exact strings), gomila-chain-manifest.json (SPEC manifest shape with the
seams; prism files ABSENT -- a chain-only object, honestly so), gomila-log-replay.txt (the verdict table).
"""
import json, os, re, sys
from fractions import Fraction as Fr

BALL = re.compile(r"\[(?:(-?[0-9.]+(?:e-?\d+)?) )?\+/- ([0-9.]+(?:e-?\d+)?)\]")
NUM = re.compile(r"^-?[0-9.]+(?:e-?\d+)?$")

def dec(s):
    """exact rational of a printed decimal (with optional exponent)"""
    return Fr(s)

def ulp(s):
    """one unit in the last printed digit of the mantissa of s"""
    m = re.match(r"^-?([0-9]*)\.?([0-9]*)(?:e(-?\d+))?$", s)
    frac = m.group(2) or ""; ex = int(m.group(3) or 0)
    return Fr(10) ** (ex - len(frac))

def ball(s):
    """printed ball or bare decimal -> (lo, hi) exact, OUTWARD by one last-digit unit of the radius/mantissa"""
    s = s.strip()
    m = BALL.match(s)
    if m:
        mid = dec(m.group(1)) if m.group(1) else Fr(0)
        rad = dec(m.group(2)) + ulp(m.group(2))
        return (mid - rad, mid + rad, mid)
    if NUM.match(s):
        v = dec(s)
        if "." not in s and "e" not in s:      # a bare integer (the exact seam t = 0 of prism 1) is exact
            return (v, v, v)
        u = ulp(s)
        return (v - u, v + u, v)
    raise ValueError(s)

def parse_line(line):
    k = int(re.match(r"Prism\((\d+)\)", line).group(1))
    tm = re.search(r" t=\[(.*?)\] winding=", line).group(1)
    # t=[lo,hi] where lo and hi are each either a ball [..] or a bare number
    parts = []
    depth = 0; cur = ""
    for ch in tm:
        if ch == "[": depth += 1
        if ch == "]": depth -= 1
        if ch == "," and depth == 0: parts.append(cur); cur = ""
        else: cur += ch
    parts.append(cur)
    assert len(parts) == 2, tm
    f = {}
    for key in ("winding", "min_mesh", "spatial", "time", "eps", "margin"):
        mm = re.search(key + r"=(\[[^\]]*\]|[0-9.e-]+)", line)
        f[key] = mm.group(1)
    Dz = re.search(r"Dz=([0-9.]+)", line).group(1); Dt = re.search(r"Dt=([0-9.]+)", line).group(1)
    mesh = int(re.search(r"mesh=(\d+)", line).group(1))
    status = line.strip().split()[-1]
    return k, parts, f, Fr(Dz), Fr(Dt), mesh, status

def main():
    log_path, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    lines = [l for l in open(log_path) if l.startswith("Prism(")]
    X = 6000000185827; t0 = Fr(129, 800); y1 = Fr(1809, 10000); eps_nominal = Fr(125, 100000)
    scalars = []; rep = []; nfail = 0; prev_hi_mid = None
    for line in lines:
        k, (tlo, thi), f, Dz, Dt, mesh, status = parse_line(line)
        lo = ball(tlo); hi = ball(thi)
        w = ball(f["winding"]); M = ball(f["min_mesh"]); sp = ball(f["spatial"]); tmv = ball(f["time"]); ep = ball(f["eps"]); mg = ball(f["margin"])
        # `mesh` counts boundary SEGMENTS: num points per edge with shared corners, 4*(num-1) = mesh (checked against
        # the printed `spatial` on every prism: prism 1 has 9600/(2*9599) = 0.5000520887..., prism 883 has 17/32)
        num = mesh // 4 + 1 if mesh % 4 == 0 else None
        # replay their eq. (1) in the conservative direction
        Delta_plus = hi[1] - lo[0]
        spatial_replay = (Dz / (2 * (num - 1))) if num else None
        time_replay = Dt * Delta_plus
        gate_lhs = M[0]                                  # M_k lower
        gate_rhs = (sp[1]) + time_replay + max(ep[1], eps_nominal)
        gate_ok = gate_lhs > gate_rhs
        # SPEC correspondence: E := eps, D := D_t*Delta, floor := M - spatial  -> C-B12: E + D < floor
        floor_spec = M[0] - sp[1]
        cb12_ok = max(ep[1], eps_nominal) + time_replay < floor_spec
        # chain continuity: this prism's lo must equal the previous prism's hi (same printed digits)
        cont = (prev_hi_mid is None and lo[2] == 0) or (prev_hi_mid is not None and lo[2] == prev_hi_mid)
        prev_hi_mid = hi[2]
        winding_ok = abs(w[0]) < Fr(1, 4) and abs(w[1]) < Fr(1, 4)
        spatial_match = (spatial_replay is not None) and (sp[0] <= spatial_replay <= sp[1])
        ok = gate_ok and cb12_ok and cont and winding_ok and status == "PASS" and num is not None and spatial_match
        if not ok: nfail += 1
        scalars.append({"k": k, "t_lo": [str(lo[0]), str(lo[1])], "t_hi": [str(hi[0]), str(hi[1])], "seam_mid": str(lo[2]), "next_mid": str(hi[2]),
                        "Delta_plus": str(Delta_plus), "winding": [str(w[0]), str(w[1])], "min_mesh": [str(M[0]), str(M[1])],
                        "Dz": str(Dz), "Dt": str(Dt), "mesh": mesh, "num_per_edge": num, "spatial_printed": [str(sp[0]), str(sp[1])],
                        "spatial_replay": str(spatial_replay), "time_printed": [str(tmv[0]), str(tmv[1])], "time_replay": str(time_replay),
                        "eps": [str(ep[0]), str(ep[1])], "margin_printed": [str(mg[0]), str(mg[1])],
                        "gate_replay_margin": str(gate_lhs - gate_rhs), "gate_replay_ok": gate_ok, "cb12_floor": str(floor_spec), "cb12_ok": cb12_ok,
                        "continuity_ok": cont, "winding_in_quarter": winding_ok, "spatial_replay_matches_printed": spatial_match, "status": status})
        rep.append(f"{k:4d} | seam {float(lo[2]):.12f} | Delta+ {float(Delta_plus):.6e} | M- {float(M[0]):.6f} | Dz {Dz} Dt {Dt} mesh {mesh} | "
                   f"spatial {float(sp[2]):.6f} (replay {float(spatial_replay) if spatial_replay else float('nan'):.6f}) | time {float(tmv[2]):.6f} (replay {float(time_replay):.6f}) | "
                   f"gate margin {float(gate_lhs - gate_rhs):+.6f} (printed {float(mg[2]):.6f}) | C-B12 floor {float(floor_spec):.6f} {'ok' if cb12_ok else 'FAIL'} | cont {'ok' if cont else 'FAIL'} | wind {'ok' if winding_ok else 'FAIL'} | {status}")
    # chain-level: first seam 0, strictly increasing (outward-consistent), last prism's hi ball contains t0 and its lower end < t0
    seams = [Fr(s["seam_mid"]) for s in scalars]
    chain_ok = seams[0] == 0 and all(a < b for a, b in zip(seams, seams[1:])) and seams[-1] < t0
    last_hi = ball(parse_line(lines[-1])[1][1])
    covers_t0 = last_hi[0] <= t0 <= last_hi[1]
    with open(os.path.join(out, "gomila-scalars.json"), "w") as fh:
        json.dump({"source": "barrier/certificates/barrier_target_closed.log @ a74738d (sha256 2d010f70902dca1627f40ddcd68f3954b37fd9596f7840787415eeafb20805f4)",
                   "X": X, "t0": str(t0), "y1": str(y1), "eps_nominal": str(eps_nominal), "prisms": scalars}, fh, indent=1)
    man = {"format": "M2a-barrier-transcript", "version": "1.0", "kind": "manifest", "lane": "barrier",
           "trust_label": "kernel-checked modulo the displayed hypotheses H1, H2 (H2-B, H2-A, H-TAIL) and H3 (producers untrusted)",
           "rect": {"x1": {"n": str(X), "d": "1"}, "x2": {"n": str(X + 1), "d": "1"}, "y1": {"n": "1809", "d": "10000"}, "y2": {"n": "1", "d": "1"}},
           "t0": {"n": "129", "d": "800"},
           "prisms": [{"index": str(i), "file": f"NOT-DERIVABLE-prism-{i:04d}.json", "seam": {"n": str(s.numerator), "d": str(s.denominator)}} for i, s in enumerate(seams)],
           "comment": "CHAIN-ONLY conversion of Gomila's sealed 883-prism log: the seams are exact (the printed lower-endpoint midpoints); the per-prism files named here DO NOT EXIST because the sealed log carries no per-segment enclosures (SPEC.md section 11). checkBarrierChain is checkable on this object; checkPrism is not."}
    with open(os.path.join(out, "gomila-chain-manifest.json"), "w") as fh:
        json.dump(man, fh, indent=1)
    with open(os.path.join(out, "gomila-log-replay.txt"), "w") as fh:
        fh.write("# exact-arithmetic replay of Gomila's printed per-prism gate (BARRIER_CERTIFICATE.md eq. (1)), outward-rounded; source log sha256 2d010f70...05f4 @ a74738d\n")
        fh.write("\n".join(rep) + "\n")
        fh.write(f"\nprisms: {len(scalars)}; per-prism replay failures: {nfail}; chain (first seam 0, strictly increasing, last seam < t0 = 129/800): {'ok' if chain_ok else 'FAIL'}; "
                 f"last prism's hi ball contains t0: {'ok' if covers_t0 else 'FAIL'}\n")
        mins = min(Fr(s["gate_replay_margin"]) for s in scalars); mins_k = min(scalars, key=lambda s: Fr(s["gate_replay_margin"]))["k"]
        fh.write(f"minimum replayed gate margin: {float(mins):.6f} at prism {mins_k}; minimum C-B12-form floor M - spatial: {float(min(Fr(s['cb12_floor']) for s in scalars)):.6f}\n")
    print(open(os.path.join(out, "gomila-log-replay.txt")).read()[-600:])

if __name__ == "__main__":
    main()
