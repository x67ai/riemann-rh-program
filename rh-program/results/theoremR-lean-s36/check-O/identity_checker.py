#!/usr/bin/env python3
"""CHECK-O statement identity (checker-written, Session 36; independent of the builder's tools/statement_identity_s36.py).

Extraction: for each name, the docstring immediately above `theorem <name>` plus the text from `theorem <name>` to the first
`:=` after it (no statement of this topic contains `:=`).  Comparisons:
  [A] challenge vs solution, byte for byte (docstring + statement), in the clean clone AND in rh-program/lean;
  [B] challenge vs typing probe, byte for byte;
  [C] the challenge's text from `import Mathlib` to EOF vs the probe's, byte for byte;
  [D] each statement vs the backticked text of UNIT-BRIEF.md §0, after whitespace normalization: full statements for items
      1, 2, 3, 7, 8; for items 4, 5, 6 (given in prose) every backticked fragment of the item must occur in the statement,
      and any fragment that does not occur verbatim is PRINTED with the nearest statement text;
  [E] the config's theorem_names = 'ResidueRank.' + the challenge's names in file order; permitted axioms; enable_nanoda;
  [F] clone copies cmp-identical to rh-program/lean copies.
"""
import json, re, sys, hashlib, pathlib

RP = pathlib.Path("/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program")
CL = pathlib.Path.home() / "rh-lean-work/checker-clone-s36-residue"
NAMES = ["log_primes_linearIndependent", "span_log_not_finite", "rank_span_log_le", "lemmaF_finite_fiber",
         "lemmaF_infinite_order", "theoremR", "theoremS_bound", "theoremS"]

def extract(text, name):
    m = re.search(r"(/--(?:(?!-/).)*?-/\n)?theorem " + re.escape(name) + r"\b(.*?):=", text, re.S)
    if not m:
        return None, None
    doc = m.group(1) or ""
    stmt = "theorem " + name + m.group(2)
    return doc, stmt

def norm(s):
    return " ".join(s.split())

ok_all = True
def rep(flag, msg):
    global ok_all
    print(("PASS " if flag else "FAIL ") + msg)
    if not flag:
        ok_all = False

files = {
    "chal_clone": CL / "comparator/Challenge/ResidueRank.lean",
    "sol_clone": CL / "comparator/Solution/ResidueRank.lean",
    "chal_rp": RP / "lean/comparator/Challenge/ResidueRank.lean",
    "sol_rp": RP / "lean/comparator/Solution/ResidueRank.lean",
    "probe": RP / "results/theoremR-lean-s36/typing-probe.lean",
}
T = {k: v.read_text(encoding="utf-8") for k, v in files.items()}
for k, v in files.items():
    print(f"{k}: {v}  sha256={hashlib.sha256(v.read_bytes()).hexdigest()}  bytes={len(v.read_bytes())}")

# theorem names in file order
for k in ["chal_clone", "sol_clone", "probe"]:
    order = re.findall(r"^theorem (\S+)", T[k], re.M)
    rep(order == NAMES, f"[order] {k}: theorem names in file order = {order}")

print("\n[A]/[B] per-statement byte identity (docstring + statement)")
S = {}
for k in files:
    S[k] = {n: extract(T[k], n) for n in NAMES}
for n in NAMES:
    c = S["chal_clone"][n]
    rep(c[1] is not None, f"{n}: extracted from challenge ({len(c[0]) + len(c[1])} bytes)")
    rep(S["sol_clone"][n] == c, f"[A] {n}: challenge == solution (clean clone)")
    rep(S["sol_rp"][n] == S["chal_rp"][n] == c, f"[A] {n}: challenge == solution (rh-program/lean) == clone")
    rep(S["probe"][n] == c, f"[B] {n}: challenge == typing probe")

print("\n[C] tail identity from the LINE 'import Mathlib' to EOF")
# (first run of this script used str.index("import Mathlib"), which matched the phrase "From `import Mathlib` to the end"
#  inside the challenge's header comment and so compared the wrong offsets; fixed to the line-anchored match below)
ti = re.search(r"^import Mathlib$", T["chal_clone"], re.M).start()
pi = re.search(r"^import Mathlib$", T["probe"], re.M).start()
rep(T["chal_clone"][ti:] == T["probe"][pi:], f"[C] challenge[{ti}:] == probe[{pi}:] ({len(T['probe'][pi:].encode())} bytes)")
imports = re.findall(r"^import .*$", T["chal_clone"], re.M)
rep(imports == ["import Mathlib"], f"[C] the challenge's import lines = {imports}")
rep(re.findall(r"^import .*$", T["probe"], re.M) == ["import Mathlib"], "[C] the probe's import lines = ['import Mathlib']")

print("\n[D] against UNIT-BRIEF.md §0 (whitespace-normalized)")
brief = (RP / "results/theoremR-lean-s36/UNIT-BRIEF.md").read_text(encoding="utf-8")
sec = brief[brief.index("**The statements to ship"):brief.index("Items 7–8 are SCOPED")]
items = re.split(r"\n(?=\d\. )", sec)
items = [it for it in items if re.match(r"\d\. ", it)]
rep(len(items) == 8, f"[D] brief §0 has {len(items)} numbered items")
FULL = {1, 2, 3, 7, 8}
for i, it in enumerate(items, 1):
    n = NAMES[i - 1]
    spans = re.findall(r"`([^`]+)`", it)
    stmt = norm(S["chal_clone"][n][1])
    body = stmt[len("theorem "):]
    if i in FULL:
        rep(norm(spans[0]) == body, f"[D] item {i} {n}: brief's backticked statement == challenge statement")
        if norm(spans[0]) != body:
            print("    brief :", norm(spans[0]))
            print("    lean  :", body)
    else:
        for sp in spans:
            spn = norm(sp)
            hit = spn in body
            print(("  in   " if hit else "  DIFF ") + f"item {i} {n}: `{spn}`")
            if not hit:
                print("         (not verbatim in the statement; read by eye in CHECK-O §4)")

print("\n[E] config")
cfg = json.loads((CL / "comparator/config-residue-rank.json").read_text())
rep(cfg["theorem_names"] == ["ResidueRank." + n for n in NAMES], "[E] theorem_names = ResidueRank.<challenge order>")
rep(sorted(cfg["permitted_axioms"]) == sorted(["propext", "Quot.sound", "Classical.choice"]), f"[E] permitted_axioms = {cfg['permitted_axioms']}")
rep(cfg.get("enable_nanoda") is True, "[E] enable_nanoda true")
rep(cfg["challenge_module"] == "Challenge.ResidueRank" and cfg["solution_module"] == "Solution.ResidueRank", "[E] modules")
rep(set(cfg) == {"challenge_module", "solution_module", "theorem_names", "permitted_axioms", "enable_nanoda"}, f"[E] keys {sorted(cfg)}")

print("\n[F] clone == rh-program/lean")
for f in ["Zeta23/ResidueRank/LogPrimes.lean", "Zeta23/ResidueRank/Pair.lean", "Zeta23/ResidueRank/GenusBound.lean",
          "comparator/Challenge/ResidueRank.lean", "comparator/Solution/ResidueRank.lean",
          "comparator/PrintAxioms/ResidueRank.lean", "comparator/config-residue-rank.json"]:
    rep((CL / f).read_bytes() == (RP / "lean" / f).read_bytes(), f"[F] {f}")

print("\nRESULT", "PASS" if ok_all else "FAIL")
sys.exit(0 if ok_all else 1)
