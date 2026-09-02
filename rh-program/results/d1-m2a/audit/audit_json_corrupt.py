#!/usr/bin/env python3
"""AUDIT (2026-09-03): corrupt copies of the row-2 transcripts and run BOTH untrusted reference checkers on them.
Run record: audit-json-corrupt-run.txt.  usage: audit_json_corrupt.py <results/d1-m2a> <scratch-out-dir>"""
import json, sys, os, shutil, subprocess
P, OUT = sys.argv[1], sys.argv[2]
def setup(name, src_dir):
    d = os.path.join(OUT, name); shutil.rmtree(d, ignore_errors=True)
    shutil.copytree(os.path.join(P, src_dir), d, ignore=shutil.ignore_patterns("*.log","*.txt","*progress*")); return d
def run(d, manifest):
    r = subprocess.run(["python3", os.path.join(P, "checker_ref.py"), os.path.join(d, manifest), "--quiet"], capture_output=True, text=True)
    r2 = subprocess.run(["python3", os.path.join(P, "barrier_ref_checker.py"), os.path.join(d, manifest)], capture_output=True, text=True)
    last = lambda r: (r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-300:])
    return r.returncode, last(r), r2.returncode, last(r2)
def mutate(name, src, man, prism, fn):
    d = setup(name, src)
    if prism:
        f = os.path.join(d, prism); p = json.load(open(f)); fn(p); json.dump(p, open(f, "w"))
    else:
        f = os.path.join(d, man); m = json.load(open(f)); fn(m); json.dump(m, open(f, "w"))
    return run(d, man)
MP, MPM, AR, ARM = "transcripts/row2", "manifest.json", "transcripts/row2-arb", "instance02-barrier-manifest.json"
print("baseline mp:", run(setup("base", MP), MPM))
print("(a) C-B6 box straddles 0:", mutate("a", MP, MPM, "prism-0017.json", lambda p: p["segments"][7].update({"reLo": "-1", "reHi": "1", "imLo": "-1", "imHi": "1"})))
print("(b) C-B12 E := Fn:", mutate("b", MP, MPM, "prism-0017.json", lambda p: p.update({"approx_defect": p["modulus_floor"]["Fn"]})))
print("(c) C-B3 mesh not strictly monotone:", mutate("c", AR, ARM, "instance02-prism-0040.json", lambda p: p["mesh"]["bottom"].__setitem__(5, dict(p["mesh"]["bottom"][4]))))
print("(d) C-B11 floor x10:", mutate("d", AR, ARM, "instance02-prism-0040.json", lambda p: p["modulus_floor"].update({"Fn": str(10*int(p["modulus_floor"]["Fn"]))})))
print("(e) C-B13 t0 = last seam:", mutate("e", MP, MPM, None, lambda m: m.update({"t0": {"n": "3719", "d": "20000"}})))
print("(f) C-B13 first prism dropped:", mutate("f", AR, ARM, None, lambda m: m.update({"prisms": m["prisms"][1:]})))
print("(g) rows rotated by 1 (checker-blind by design, SPEC P-11):", mutate("g", MP, MPM, "prism-0017.json", lambda p: p.update({"segments": p["segments"][1:] + p["segments"][:1]})))
print("(h) prism seam != manifest seam:", mutate("h", MP, MPM, "prism-0017.json", lambda p: p.update({"seam": {"n": "1", "d": "2"}})))
