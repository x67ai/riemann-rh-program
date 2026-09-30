#!/usr/bin/env python3
"""CHECK-O trust greps (checker-written, Session 36; independent of the builder's tools/trust_greps_s36.py).

For each shipped Lean file of the topic (clean clone copies, which are cmp-identical to rh-program/lean): every word-bounded hit of
the trust words, classified as IN CODE or IN COMMENT/DOCSTRING (Lean block comments /- -/ nest; line comments --), with the line.
Also: imports; declaration keywords that could add trust (axiom, opaque, instance, macro, syntax, elab, set_option, attribute,
@[, partial, unsafe, private, noncomputable); 'Challenge' anywhere in an import of the solution/program side.
"""
import re, pathlib, sys

CL = pathlib.Path.home() / "rh-lean-work/checker-clone-s36-residue"
FILES = ["Zeta23/ResidueRank/LogPrimes.lean", "Zeta23/ResidueRank/Pair.lean", "Zeta23/ResidueRank/GenusBound.lean",
         "comparator/Challenge/ResidueRank.lean", "comparator/Solution/ResidueRank.lean",
         "comparator/PrintAxioms/ResidueRank.lean", "comparator/config-residue-rank.json"]
WORDS = ["axiom", "native_decide", "unsafe", "implemented_by", "extern", "opaque", "sorry", "admit", "ofReduceBool",
         "reduceBool", "decide", "set_option", "macro", "elab", "syntax", "partial", "attribute", "instance", "private",
         "noncomputable", "Challenge", "sorryAx", "debug", "trustCompiler", "Lean.Elab", "run_cmd", "run_meta", "#eval"]

def comment_mask(text):
    """Return a list of booleans, True where the character is inside a comment (block comments nest; strings respected)."""
    mask = [False] * len(text)
    i, depth, in_str, in_line = 0, 0, False, False
    n = len(text)
    while i < n:
        c = text[i]
        if in_line:
            mask[i] = True
            if c == "\n":
                in_line = False
            i += 1
            continue
        if depth > 0:
            if text.startswith("/-", i):
                depth += 1; mask[i] = mask[i + 1] = True; i += 2; continue
            if text.startswith("-/", i):
                depth -= 1; mask[i] = mask[i + 1] = True; i += 2; continue
            mask[i] = True; i += 1; continue
        if in_str:
            if c == "\\":
                i += 2; continue
            if c == '"':
                in_str = False
            i += 1; continue
        if c == '"':
            in_str = True; i += 1; continue
        if text.startswith("--", i):
            in_line = True; mask[i] = True; i += 1; continue
        if text.startswith("/-", i):
            depth = 1; mask[i] = mask[i + 1] = True; i += 2; continue
        i += 1
    return mask

code_hits = {}
for f in FILES:
    p = CL / f
    t = p.read_text(encoding="utf-8")
    mask = comment_mask(t) if f.endswith(".lean") else [False] * len(t)
    print(f"==== {f}  ({t.count(chr(10))} lines)")
    for w in WORDS:
        pat = re.escape(w) if not w[0].isalpha() else r"(?<![A-Za-z0-9_'.])" + re.escape(w) + r"(?![A-Za-z0-9_'])"
        for m in re.finditer(pat, t):
            line = t.count("\n", 0, m.start()) + 1
            where = "COMMENT" if mask[m.start()] else "CODE"
            src = t.splitlines()[line - 1].strip()
            print(f"  {where:7s} {w:14s} l.{line}: {src[:150]}")
            if where == "CODE":
                code_hits.setdefault(f, []).append((w, line))
    if f.endswith(".lean"):
        imps = re.findall(r"^import .*$", t, re.M)
        print(f"  imports: {imps}")
        code_only = "".join(ch if not mk else (" " if ch != "\n" else "\n") for ch, mk in zip(t, mask))
        decls = re.findall(r"^\s*(?:@\[[^\]]*\]\s*)?(?:private |protected |noncomputable |unsafe |partial )*"
                           r"(def|theorem|lemma|abbrev|instance|axiom|opaque|structure|inductive|class|macro|syntax|elab|"
                           r"set_option|attribute|example|notation|infix|prefix|postfix|macro_rules|elab_rules)\b", code_only, re.M)
        from collections import Counter
        print(f"  declaration keywords in code: {dict(Counter(decls))}")

print("\n==== SUMMARY of hits IN CODE")
for f, hs in code_hits.items():
    print(f"  {f}: {hs}")
bad = [(f, w, l) for f, hs in code_hits.items() for (w, l) in hs
       if not (f == "comparator/Challenge/ResidueRank.lean" and w == "sorry")
       and not (w == "noncomputable" and f == "Zeta23/ResidueRank/LogPrimes.lean")
       and not (w == "decide" and False)]
print("  hits in code other than the challenge's `sorry`s and LogPrimes' two `noncomputable def`s:", bad if bad else "NONE")
n_sorry = len([1 for (w, l) in code_hits.get("comparator/Challenge/ResidueRank.lean", []) if w == "sorry"])
print(f"  challenge `sorry` in code: {n_sorry}")
print("RESULT", "CLEAN" if not bad and n_sorry == 8 else "SEE ABOVE")
