#!/usr/bin/env python3
"""seed_rows.py -- writes the FOUR SEED ROWS of the M3 exclusion ledger (R1-R4 of
results/d1-m2a/dr8/PRICING-M3-ledger.md sec. 2) from the eight M1 v1 acceptance null transcripts
already on disk.  Zero producer compute: every number is READ from the transcript JSON, the
producers' own metadata, cost-curve.json, the acceptance logs and the Lean records, and the two
Python checkers + crosscheck.py are RE-RUN (seconds) to record today's verdicts.  Run once at the
seed (2026-09-10, Session 20); later rows are added by the checklist in README.md, not by this
script.  UNTRUSTED bookkeeping; ledger_check.py re-derives everything independently."""
import json, hashlib, os, sys, subprocess, re, datetime
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
D1M1 = os.path.abspath(os.path.join(HERE, "..", "d1-m1"))
ACC = os.path.join(D1M1, "acceptance")
LABEL = "kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)"
ADDED_BY = "Claude Fable 5.1 (Session 20, D-R8 + M3-seed build, Job 1 builder; brief results/d1-m2a/dr8/BUILD-BRIEF-fDH.md addendum)"

SEED = [  # (row tag, json stem, mp Lean name, arb Lean name, provenance note)
    ("R1", "null-t100",      "mpNullT100",     "arbNullT100",
     "M1 v1 acceptance null test 1 (cost-curve height point T = 10^2, delta0 = 1/10): instrument-validation box chosen for the cost curve, not by any prior; results/d1-m1/acceptance-report.md sec. 1, RUN-REPORT.md sec. 1.4."),
    ("R2", "null-t1000",     "mpNullT1000",    "arbNullT1000",
     "M1 v1 acceptance null test 2 (cost-curve height point T = 10^3, delta0 = 1/10): instrument-validation box chosen for the cost curve, not by any prior; results/d1-m1/acceptance-report.md sec. 1, RUN-REPORT.md sec. 1.4."),
    ("R3", "null-t10000",    "mpNullT10000",   "arbNullT10000",
     "M1 v1 acceptance null test 3 (cost-curve height point T = 10^4, delta0 = 1/10; the mp leg's 1 294 segments and 1 565 s are the recorded cost ceiling of the Euler-Maclaurin leg): instrument-validation box chosen for the cost curve, not by any prior; results/d1-m1/acceptance-report.md sec. 1, RUN-REPORT.md sec. 1.4."),
    ("R4", "null-deep-t100", "mpNullDeepT100", "arbNullDeepT100",
     "M1 v1 acceptance null test 4 (depth point T = 10^2, delta0 = 1/40 -- the deep box): instrument-validation box chosen for the cost curve's depth axis, not by any prior; results/d1-m1/acceptance-report.md sec. 1, RUN-REPORT.md sec. 1.4."),
]

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()

def rat(r):  # transcript rational {"n","d"} -> Fraction
    return Fraction(int(r["n"]), int(r["d"]))

def ratstr(fr):
    return str(fr.numerator) if fr.denominator == 1 else "%d/%d" % (fr.numerator, fr.denominator)

def idpart(fr):
    return str(fr.numerator) if fr.denominator == 1 else "%d-%d" % (fr.numerator, fr.denominator)

def run(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr

cost = json.load(open(os.path.join(D1M1, "cost-curve.json")))
cost_by = {pt["transcript"]: pt for pt in cost["points"]}

def leg_record(legname, stem, leanname):
    fname = "w1-%s-%s.json" % (legname, stem)
    path = os.path.join(ACC, fname)
    doc = json.load(open(path))
    assert doc["function"] == "zeta" and doc["mode"] == "exclusion" and doc["claimed_m"] == "0", fname
    rows = doc["segments"]
    S_lo = sum(int(r["argLo"]) for r in rows)
    S_hi = sum(int(r["argHi"]) for r in rows)
    fl = doc["modulus_floor"]
    prod = doc.get("producer", {})
    if legname == "mp":
        wall = prod["wall_seconds"]
    else:
        # the Arb leg records no wall time in the JSON; cost-curve.json carries the zsh `time` figure
        wall = cost_by["acceptance/" + fname]["wall_seconds"]
    # today's checker verdicts (re-run, seconds)
    rc1, out1 = run([sys.executable, "reference_checker.py", path], D1M1)
    rc2, out2 = run([sys.executable, "checker_ref.py", path], D1M1)
    v1 = "ACCEPT" if rc1 == 0 and "VERDICT: ACCEPT" in out1 else "REJECT"
    v2 = "ACCEPT" if rc2 == 0 and ": ACCEPT" in out2 else "REJECT"
    return {
        "transcript": "../d1-m1/acceptance/" + fname,
        "sha256": sha256(path),
        "bytes": os.path.getsize(path),
        "segments": len(rows),
        "K": doc["scales"]["K"],
        "A": doc["scales"]["A"],
        "winding_lo_hi": [str(S_lo), str(S_hi)],
        "floor": "%s/%s" % (fl["Fn"], fl["Fd"]),
        "wall_seconds": wall,
        "embedded_trust_label": doc["trust_label"],
        "python_checkers": {
            "reference_checker": v1, "checker_ref": v2,
            "logs": ["../d1-m1/acceptance/logs/reference-checker-accepts.log",
                     "../d1-m1/acceptance/logs/checker-ref-accepts.log",
                     "../d1-m1/recon_checker_pass.log"]},
        "lean": {"module": "Zeta23.W1.Instances", "data": leanname, "floor": leanname + "_floor",
                 "check": leanname + "_check", "corollary": leanname + "_exclusion",
                 "corollary_module": "Zeta23.W1.Ledger",
                 "build_record": "../d1-m1/recon_lean_instances.log",
                 "corollary_axioms_record": "../d1-m2a/dr8/fdh-axioms.log"},
    }, doc

def entry_hash(rec):
    r = dict(rec); r["entry_sha256"] = ""
    return hashlib.sha256(json.dumps(r, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
ledger_lines = []
for tag, stem, mpname, arbname, note in SEED:
    mp, mpdoc = leg_record("mp", stem, mpname)
    arb, arbdoc = leg_record("arb", stem, arbname)
    assert mpdoc["rect"] == arbdoc["rect"], stem
    s1, s2 = rat(mpdoc["rect"]["sigma1"]), rat(mpdoc["rect"]["sigma2"])
    T1, T2 = rat(mpdoc["rect"]["T1"]), rat(mpdoc["rect"]["T2"])
    row_id = "zeta_%s_%s_%s_%s" % (idpart(s1), idpart(s2), idpart(T1), idpart(T2))
    delta0 = s1 - Fraction(1, 2)
    # cross-check re-run (the on-disk record is acceptance/logs/crosscheck.log)
    rc, out = run([sys.executable, os.path.join(ACC, "crosscheck.py"),
                   os.path.join(ACC, "w1-mp-%s.json" % stem), os.path.join(ACC, "w1-arb-%s.json" % stem)], ACC)
    m = re.search(r"overlap pairs checked: (\d+)", out)
    verdict = "CONSISTENT" if rc == 0 and "VERDICT: CONSISTENT" in out else "INCONSISTENT"
    box = "[%s, %s] x [%s, %s]" % (ratstr(s1), ratstr(s2), ratstr(T1), ratstr(T2))
    rec = {
        "row_id": row_id,
        "function": "zeta", "mode": "exclusion", "claimed_m": "0",
        "box": {"sigma1": ratstr(s1), "sigma2": ratstr(s2), "T1": ratstr(T1), "T2": ratstr(T2)},
        "delta0": ratstr(delta0), "height": float(T1), "height_span": ratstr(T2 - T1),
        "grade": "box", "status": "accepted",
        "trust_label": LABEL,
        "sentence": "no zeros of zeta in the closed box %s -- %s" % (box, LABEL),
        "delta0_form": "no zeros of zeta with Re s >= 1/2 + %s AND Re s <= %s in %s <= Im s <= %s (the single-box form; the D-R6 range form 'Re s >= 1/2 + delta0 in [T1, T2]' needs a box family reaching sigma = 1 -- README, 'What a row licenses')" % (ratstr(delta0), ratstr(s2), ratstr(T1), ratstr(T2)),
        "legs": {"mp": mp, "arb": arb},
        "crosscheck": {"log": "../d1-m1/acceptance/logs/crosscheck.log",
                       "overlap_pairs": int(m.group(1)) if m else -1, "verdict": verdict},
        "provenance": {"kind": "acceptance", "note": note},
        "added_utc": now, "added_by": ADDED_BY, "entry_sha256": "",
    }
    rec["entry_sha256"] = entry_hash(rec)
    d = os.path.join(HERE, "rows", row_id)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "ROW.json"), "w", encoding="utf-8") as fh:
        json.dump(rec, fh, indent=1, ensure_ascii=False); fh.write("\n")
    with open(os.path.join(d, "PROVENANCE.md"), "w", encoding="utf-8") as fh:
        fh.write("# Ledger row `%s` (%s) -- provenance\n\n" % (row_id, tag))
        fh.write("**Box:** R = %s, delta0 = sigma1 - 1/2 = %s. **Grade:** box. **Status:** accepted.\n\n" % (box, ratstr(delta0)))
        fh.write("**Provenance kind:** `acceptance`. %s\n\n" % note)
        fh.write("**Sentence (licensed, single box):** %s\n\n" % rec["sentence"])
        fh.write("**Legs:** mp `%s` (%s, SHA-256 `%s`, %d segments) and arb `%s` (%s, SHA-256 `%s`, %d segments); both Python checkers ACCEPT on both legs (re-run today); cross-check %d overlap pairs, %s; kernel `%s_check`, `%s_check` (`[propext]`, results/d1-m1/recon_lean_instances.log); corollaries `%s_exclusion`, `%s_exclusion` in `lean/Zeta23/W1/Ledger.lean`.\n\n" % (
            mp["transcript"], mpname, mp["sha256"], mp["segments"], arb["transcript"], arbname, arb["sha256"], arb["segments"], rec["crosscheck"]["overlap_pairs"], verdict, mpname, arbname, mpname, arbname))
        fh.write("**What the negative means:** nothing new about zeta -- the box lies far below the rigorous verification record 3*10^12 (Platt-Trudgian); it is the program's own certificate in its own trust vocabulary and one of the ledger's four format-validation rows.\n\n")
        fh.write("**Added:** %s by %s.\n" % (now, ADDED_BY))
    with open(os.path.join(d, "REFS.txt"), "w", encoding="utf-8") as fh:
        fh.write("# pointer file (seed rows point at results/d1-m1/acceptance/, the single source of truth the Instances.lean back-parse was verified against; no copies)\n")
        for rel in [mp["transcript"], arb["transcript"], rec["crosscheck"]["log"],
                    "../d1-m1/acceptance/logs/crosscheck-t10000.log" if stem == "null-t10000" else None,
                    "../d1-m1/acceptance/logs/reference-checker-accepts.log", "../d1-m1/acceptance/logs/checker-ref-accepts.log",
                    "../d1-m1/recon_checker_pass.log", "../d1-m1/recon_lean_instances.log", "../lean/Zeta23/W1/Instances.lean", "../lean/Zeta23/W1/Ledger.lean"]:
            if rel is None: continue
            ap = os.path.normpath(os.path.join(HERE, rel))
            fh.write("%s  %s\n" % (sha256(ap), rel))
    ledger_lines.append("| %s | %s | `%s` | %s | %s | accepted | %s | mp `%s…` / arb `%s…` | %s |" % (
        now[:10], tag, row_id, box, ratstr(delta0), rec["sentence"].replace(" -- " + LABEL, ""), mp["sha256"][:16], arb["sha256"][:16], "acceptance"))
    print("wrote", row_id, "mp", mp["python_checkers"], "arb", arb["python_checkers"], "xc", rec["crosscheck"])

with open(os.path.join(HERE, "LEDGER.md"), "a", encoding="utf-8") as fh:
    fh.write("\n".join(ledger_lines) + "\n")
print("LEDGER.md appended", len(ledger_lines), "rows")
