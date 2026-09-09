#!/usr/bin/env python3
"""ledger_check.py -- UNTRUSTED validator of the M3 exclusion ledger (results/d1-m3/).

For every rows/<row_id>/ROW.json it
  * validates the record against ledger-schema.json (Draft 2020-12, jsonschema);
  * checks row_id = directory name = the content-determined id of the box; delta0 = sigma1 - 1/2
    exactly; height = float(T1); height_span = T2 - T1; the sentence names the box;
  * for each leg: re-hashes the transcript (SHA-256 + byte count), re-reads it (function zeta,
    mode exclusion, claimed_m 0, rect = box, K, A, segment count, winding [S_lo, S_hi] = sums of the
    argument rows, modulus floor Fn/Fd, embedded trust_label), RE-RUNS both Python checkers
    (reference_checker.py, checker_ref.py) and requires ACCEPT, and confirms the Lean names exist in
    the mirror (lean/Zeta23/W1/Instances.lean: the data literal, its floor, its _check theorem;
    lean/Zeta23/W1/Ledger.lean: the _exclusion corollary with H-ENCL for that literal) and that the
    recorded build log names the _check theorem with axioms [propext] and the axioms record names the
    corollary with the three standard axioms;
  * RE-RUNS acceptance/crosscheck.py on the pair and requires CONSISTENT with the recorded pair count;
  * refuses status 'accepted' without both legs, both ACCEPTs, CONSISTENT, and a _check per leg;
    refuses any grade other than 'box' (schema) and any top-level aggregate (schema);
  * recomputes entry_sha256 (SHA-256 of the record serialized with sort_keys, separators (",", ":"),
    ensure_ascii False, entry_sha256 = "") and requires equality;
  * regenerates index.json (rows sorted by (height, delta0, row_id)) and, without --write, requires
    it to equal the on-disk index.json byte for byte; with --write, writes it.
Exit 0 iff everything holds; nonzero on any drift, with every finding printed.  Seconds.
usage: python3 ledger_check.py [--write]"""
import json, hashlib, os, re, subprocess, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))          # rh-program/
D1M1 = os.path.join(ROOT, "results", "d1-m1")
ACC = os.path.join(D1M1, "acceptance")
LEAN = os.path.join(ROOT, "lean", "Zeta23", "W1")
LABEL = "kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)"
STD_AXIOMS = "[propext, Classical.choice, Quot.sound]"

def sha256(p):
    h = hashlib.sha256(); h.update(open(p, "rb").read()); return h.hexdigest()
def frac(s):
    return Fraction(s)
def ratstr(fr):
    return str(fr.numerator) if fr.denominator == 1 else "%d/%d" % (fr.numerator, fr.denominator)
def idpart(fr):
    return str(fr.numerator) if fr.denominator == 1 else "%d-%d" % (fr.numerator, fr.denominator)
def run(cmd, cwd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr
def entry_hash(rec):
    r = dict(rec); r["entry_sha256"] = ""
    return hashlib.sha256(json.dumps(r, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()

def main(argv):
    write = "--write" in argv
    import jsonschema
    schema = json.load(open(os.path.join(HERE, "ledger-schema.json")))
    validator = jsonschema.Draft202012Validator(schema)
    row_schema = {"$schema": schema["$schema"], "$defs": schema["$defs"], "$ref": "#/$defs/row"}
    row_validator = jsonschema.Draft202012Validator(row_schema)
    inst_src = open(os.path.join(LEAN, "Instances.lean"), encoding="utf-8").read()
    ledger_src = open(os.path.join(LEAN, "Ledger.lean"), encoding="utf-8").read()
    findings = []
    def bad(msg): findings.append(msg); print("  DRIFT:", msg)
    rows = []
    rowdirs = sorted(d for d in os.listdir(os.path.join(HERE, "rows")) if os.path.isdir(os.path.join(HERE, "rows", d)))
    for d in rowdirs:
        p = os.path.join(HERE, "rows", d, "ROW.json")
        print("== row", d)
        if not os.path.exists(p):
            bad("%s: no ROW.json" % d); continue
        rec = json.load(open(p, encoding="utf-8"))
        for e in sorted(row_validator.iter_errors(rec), key=lambda e: list(e.path)):
            bad("%s: schema: %s at %s" % (d, e.message, "/".join(str(x) for x in e.path)))
        if rec.get("row_id") != d:
            bad("%s: row_id %r != directory" % (d, rec.get("row_id")))
        box = rec["box"]; s1, s2, T1, T2 = (frac(box[k]) for k in ("sigma1", "sigma2", "T1", "T2"))
        want_id = "zeta_%s_%s_%s_%s" % (idpart(s1), idpart(s2), idpart(T1), idpart(T2))
        if rec["row_id"] != want_id: bad("%s: row_id should be %s" % (d, want_id))
        if not (Fraction(1, 2) < s1 <= s2 < 1 and T1 < T2): bad("%s: box violates C2" % d)
        if frac(rec["delta0"]) != s1 - Fraction(1, 2): bad("%s: delta0 %s != sigma1 - 1/2" % (d, rec["delta0"]))
        if rec["height"] != float(T1): bad("%s: height %r != float(T1)" % (d, rec["height"]))
        if frac(rec["height_span"]) != T2 - T1: bad("%s: height_span" % d)
        boxstr = "[%s, %s] x [%s, %s]" % (ratstr(s1), ratstr(s2), ratstr(T1), ratstr(T2))
        if rec["sentence"] != "no zeros of zeta in the closed box %s -- %s" % (boxstr, LABEL):
            bad("%s: sentence is not the licensed box sentence" % d)
        if rec["trust_label"] != LABEL: bad("%s: trust_label" % d)
        legs_ok = {}
        for legname, leg in rec.get("legs", {}).items():
            tp = os.path.normpath(os.path.join(HERE, leg["transcript"]))
            ok = True
            if not os.path.exists(tp):
                bad("%s/%s: transcript missing %s" % (d, legname, leg["transcript"])); legs_ok[legname] = False; continue
            h = sha256(tp)
            if h != leg["sha256"]: bad("%s/%s: sha256 %s != recorded %s" % (d, legname, h, leg["sha256"])); ok = False
            if os.path.getsize(tp) != leg["bytes"]: bad("%s/%s: bytes" % (d, legname)); ok = False
            doc = json.load(open(tp, encoding="utf-8"))
            if (doc["function"], doc["mode"], doc["claimed_m"]) != ("zeta", "exclusion", "0"):
                bad("%s/%s: not a zeta exclusion m=0 transcript" % (d, legname)); ok = False
            rr = doc["rect"]
            if [Fraction(int(rr[k]["n"]), int(rr[k]["d"])) for k in ("sigma1", "sigma2", "T1", "T2")] != [s1, s2, T1, T2]:
                bad("%s/%s: rect != box" % (d, legname)); ok = False
            if doc["scales"]["K"] != leg["K"] or doc["scales"]["A"] != leg["A"]: bad("%s/%s: K/A" % (d, legname)); ok = False
            segs = doc["segments"]
            if len(segs) != leg["segments"]: bad("%s/%s: segments %d != %d" % (d, legname, len(segs), leg["segments"])); ok = False
            S = [str(sum(int(r["argLo"]) for r in segs)), str(sum(int(r["argHi"]) for r in segs))]
            if S != leg["winding_lo_hi"]: bad("%s/%s: winding %s != %s" % (d, legname, S, leg["winding_lo_hi"])); ok = False
            fl = doc.get("modulus_floor")
            if not fl or "%s/%s" % (fl["Fn"], fl["Fd"]) != leg["floor"]: bad("%s/%s: floor" % (d, legname)); ok = False
            if doc["trust_label"] != leg["embedded_trust_label"]: bad("%s/%s: embedded label" % (d, legname)); ok = False
            rc1, out1 = run([sys.executable, "reference_checker.py", tp], D1M1)
            v1 = "ACCEPT" if rc1 == 0 and "VERDICT: ACCEPT" in out1 else "REJECT"
            rc2, out2 = run([sys.executable, "checker_ref.py", tp], D1M1)
            v2 = "ACCEPT" if rc2 == 0 and ": ACCEPT" in out2 else "REJECT"
            if (v1, v2) != (leg["python_checkers"]["reference_checker"], leg["python_checkers"]["checker_ref"]) or (v1, v2) != ("ACCEPT", "ACCEPT"):
                bad("%s/%s: python checkers now %s/%s, recorded %s/%s" % (d, legname, v1, v2, leg["python_checkers"]["reference_checker"], leg["python_checkers"]["checker_ref"])); ok = False
            for rel in leg["python_checkers"]["logs"] + [leg["lean"]["build_record"], leg["lean"]["corollary_axioms_record"], rec["crosscheck"]["log"]]:
                if not os.path.exists(os.path.normpath(os.path.join(HERE, rel))): bad("%s/%s: missing record %s" % (d, legname, rel)); ok = False
            L = leg["lean"]
            if L["module"] != "Zeta23.W1.Instances" or L["corollary_module"] != "Zeta23.W1.Ledger": bad("%s/%s: lean modules" % (d, legname)); ok = False
            if not re.search(r"^def %s : W1Data where$" % re.escape(L["data"]), inst_src, re.M): bad("%s/%s: no literal %s" % (d, legname, L["data"])); ok = False
            if not re.search(r"^def %s : W1Floor where$" % re.escape(L["floor"]), inst_src, re.M): bad("%s/%s: no floor %s" % (d, legname, L["floor"])); ok = False
            if not re.search(r"^theorem %s : checkW1Floor %s %s = true := by decide \+kernel$" % tuple(re.escape(x) for x in (L["check"], L["data"], L["floor"])), inst_src, re.M):
                bad("%s/%s: no kernel theorem %s" % (d, legname, L["check"])); ok = False
            cor = r"^theorem %s \(hEncl : W1EnclOK riemannZeta %s\) :\n    ∀ s ∈ W1Rect %s, riemannZeta s ≠ 0 :=\n  \(cert_of_checkW1_ap %s \(checkW1Floor_spec %s\)\.1 hEncl\)\.2 \(by decide\)$" % tuple(re.escape(x) for x in (L["corollary"], L["data"], L["data"], L["data"], L["check"]))
            if not re.search(cor, ledger_src, re.M): bad("%s/%s: corollary %s not in Ledger.lean in the 3-line shape" % (d, legname, L["corollary"])); ok = False
            br = open(os.path.normpath(os.path.join(HERE, L["build_record"])), encoding="utf-8").read()
            if "'Zeta23.W1.%s' depends on axioms: [propext]" % L["check"] not in br: bad("%s/%s: build record does not name %s with [propext]" % (d, legname, L["check"])); ok = False
            ar = open(os.path.normpath(os.path.join(HERE, L["corollary_axioms_record"])), encoding="utf-8").read()
            if "'Zeta23.W1.%s' depends on axioms: %s" % (L["corollary"], STD_AXIOMS) not in ar: bad("%s/%s: axioms record does not name %s with %s" % (d, legname, L["corollary"], STD_AXIOMS)); ok = False
            legs_ok[legname] = ok
            print("  leg %-3s %s  sha256 ok  %d segments  S=[%s, %s]  checkers %s/%s  lean %s/%s/%s" % (legname, os.path.basename(tp), len(segs), S[0], S[1], v1, v2, L["data"], L["check"], L["corollary"]))
        xc = rec["crosscheck"]; xc_ok = False
        if set(legs_ok) == {"mp", "arb"}:
            rc, out = run([sys.executable, os.path.join(ACC, "crosscheck.py"),
                           os.path.normpath(os.path.join(HERE, rec["legs"]["mp"]["transcript"])),
                           os.path.normpath(os.path.join(HERE, rec["legs"]["arb"]["transcript"]))], ACC)
            m = re.search(r"overlap pairs checked: (\d+)", out)
            verdict = "CONSISTENT" if rc == 0 and "VERDICT: CONSISTENT" in out else "INCONSISTENT"
            pairs = int(m.group(1)) if m else -1
            xc_ok = verdict == "CONSISTENT" and verdict == xc["verdict"] and pairs == xc["overlap_pairs"]
            if not xc_ok: bad("%s: crosscheck now %s/%d pairs, recorded %s/%d" % (d, verdict, pairs, xc["verdict"], xc["overlap_pairs"]))
            print("  crosscheck %s, %d overlap pairs" % (verdict, pairs))
        if rec["status"] == "accepted" and not (set(legs_ok) == {"mp", "arb"} and all(legs_ok.values()) and xc_ok):
            bad("%s: status 'accepted' is not earned (needs both legs ACCEPTed, kernel-checked, CONSISTENT)" % d)
        eh = entry_hash(rec)
        if eh != rec["entry_sha256"]: bad("%s: entry_sha256 %s != recomputed %s" % (d, rec["entry_sha256"], eh))
        rows.append(rec)
    rows.sort(key=lambda r: (r["height"], frac(r["delta0"]), r["row_id"]))
    index = {"format": "M3-exclusion-ledger-index", "version": "0.1",
             "generated_by": "ledger_check.py (regenerated from rows/*/ROW.json; never hand-edited)", "rows": rows}
    for e in sorted(validator.iter_errors(index), key=lambda e: list(e.path)):
        bad("index: schema: %s at %s" % (e.message, "/".join(str(x) for x in e.path)))
    text = json.dumps(index, indent=1, ensure_ascii=False) + "\n"
    ip = os.path.join(HERE, "index.json")
    if write:
        open(ip, "w", encoding="utf-8").write(text); print("index.json written (%d rows)" % len(rows))
    else:
        if not os.path.exists(ip) or open(ip, encoding="utf-8").read() != text:
            bad("index.json differs from the regeneration (run with --write after adding a row)")
    print("rows: %d; findings: %d -> %s" % (len(rows), len(findings), "OK" if not findings else "FAIL"))
    return 1 if findings else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
