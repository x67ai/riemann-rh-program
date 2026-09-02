#!/usr/bin/env python3
"""emit_gomila_scratch.py -- writes a SCRATCH Lean file (NOT a program module) with
  (a) `gomilaRect : RectData` and the CHAIN-ONLY `gomilaChain : BarrierData` whose 883 prisms carry ONLY their seams
      (exact rationals from the sealed log; all other fields dummy: empty mesh/rows, K = A = 1, floor 0/1, E = D = 0)
      and the kernel fact `gomilaChain_chain : checkBarrierChain gomilaChain = true` by `decide +kernel` -- C-B0 (global),
      C-B2', C-B13 for Gomila's seam chain [0 = tau_1 < ... < tau_883 < 129/800].  NOTHING per prism is claimed for
      these 883 dummies (checkPrism is false on them by construction: the sealed log has no rows);
  (b) for each SPOT-SAMPLE prism produced by D1's own legs on Gomila's box (gomila/spot-arb, gomila/spot-mp), the
      literal `PrismData` and `checkPrism gomilaRect <p> = true` by `decide +kernel` -- kernel facts about D1's OWN
      enclosures at Gomila's seams, the Lean-checker half of screen step 3 on the only rows that exist.
usage: emit_gomila_scratch.py <out.lean> [--mp] [--arb]
"""
import json, os, sys
from fractions import Fraction as Fr
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(here))
from emit_lean_m2a import row_lit, pair_lit, rat

def prism_defs(p, name, chunk=1000):
    rows = p["segments"]; seam = rat(p["seam"]); K, A = int(p["scales"]["K"]), int(p["scales"]["A"])
    out = []
    n = (len(rows) + chunk - 1) // chunk
    for c in range(n):
        out.append(f"def {name}_rows_{c} : List W1.W1Row := [\n" + ",\n".join("  " + row_lit(r) for r in rows[c*chunk:(c+1)*chunk]) + "]\n")
    out.append(f"def {name} : PrismData where\n  tn := {seam[0]}\n  td := {seam[1]}\n  K := {K}\n  A := {A}\n")
    for e in ("bottom", "right", "top", "left"):
        out.append(f"  {e} := [" + ", ".join(pair_lit(rat(q)) for q in p["mesh"][e]) + "]\n")
    out.append(f"  rows := {' ++ '.join(f'{name}_rows_{c}' for c in range(n))}\n  Fn := {p['modulus_floor']['Fn']}\n  Fd := {p['modulus_floor']['Fd']}\n  E := {p['approx_defect']}\n  D := {p['displacement']}\n\n")
    out.append(f"theorem {name}_check : checkPrism gomilaRect {name} = true := by decide +kernel\n\n")
    return "".join(out)

def main():
    out_path = sys.argv[1]; legs = [a[2:] for a in sys.argv[2:]] or ["arb", "mp"]
    man = json.load(open(os.path.join(here, "gomila-chain-manifest.json")))
    seams = [rat(e["seam"]) for e in man["prisms"]]
    sample = json.load(open(os.path.join(here, "spot-sample.json")))["prisms"]
    L = ["import Zeta23.DBN.BarrierCert\n\n/-! SCRATCH (results/d1-m2a/gomila/): Gomila chain-only + D1 spot-sample prisms on Gomila's box. Not a program module. -/\n",
         "namespace Zeta23.DBN.GomilaScratch\nopen Zeta23.DBN\nset_option maxRecDepth 100000\n\n",
         "/-- Gomila's barrier rectangle [X, X+1] × [1809/10000, 1], X = 6 000 000 185 827. -/\n",
         "def gomilaRect : RectData := ⟨6000000185827, 1, 6000000185828, 1, 1809, 10000, 1, 1⟩\n\n",
         "/-- seam-only dummy prism: ONLY tn/td are meaningful (checkPrism is false on it by construction). -/\n",
         "def seamOnly (tn td : ℤ) : PrismData := ⟨tn, td, 1, 1, [], [], [], [], [], 0, 1, 0, 0⟩\n\n",
         "/-- the 883 seams of the sealed log, exact (printed lower-endpoint midpoints), as a chain-only BarrierData with t₀ = 129/800. -/\n",
         "def gomilaChain : BarrierData where\n  rect := gomilaRect\n  t0n := 129\n  t0d := 800\n  prisms := [\n" + ",\n".join(f"    seamOnly {s[0]} {s[1]}" for s in seams) + "]\n\n",
         "/-- C-B0 (global), C-B2′, C-B13 on Gomila's 883-seam chain: first seam 0, strictly increasing, last < 129/800. -/\n",
         "theorem gomilaChain_chain : checkBarrierChain gomilaChain = true := by decide +kernel\n\n",
         "/-- negative control: the dummy prisms are NOT accepted per prism (no rows) — checkPrism is false on the first one. -/\n",
         "theorem gomilaChain_prism0_not : checkPrism gomilaRect (seamOnly 0 1) = false := by decide +kernel\n\n"]
    names = []
    for s in sample:
        k = s["k"]; j = k - 1
        for leg in legs:
            path = os.path.join(here, "spot-arb", f"seam-{j:04d}", "instance02-prism-0000.json") if leg == "arb" else os.path.join(here, "spot-mp", f"prism-{j:04d}.json")
            if not os.path.exists(path): continue
            p = json.load(open(path)); name = f"g{leg}{k:04d}"
            assert Fr(*rat(p["seam"])) == Fr(*rat(man["prisms"][j]["seam"]))
            L.append(f"/-- D1 {leg} leg, Gomila prism {k} (seam {rat(p['seam'])[0]}/{rat(p['seam'])[1]}), {len(p['segments'])} rows. -/\n")
            L.append(prism_defs(p, name)); names.append(name)
    L.append("#print axioms gomilaChain_chain\n" + "".join(f"#print axioms {n}_check\n" for n in names[:2]) + "\nend Zeta23.DBN.GomilaScratch\n")
    open(out_path, "w").write("".join(L))
    print(f"wrote {out_path}: 883-seam chain + {len(names)} spot prisms ({', '.join(legs)})")

if __name__ == "__main__":
    main()
