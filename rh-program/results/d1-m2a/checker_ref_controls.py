#!/usr/bin/env python3
"""checker_ref_controls.py -- negative controls for checker_ref.py on a REAL transcript prism (row2/prism-0000 of
the mpmath leg): each mutation must be REJECTED at the named clause; two weakened-but-valid mutations must be
ACCEPTED (a checker that rejects valid weakenings would be over-strict)."""
import copy, sys
sys.path.insert(0, ".")
import checker_ref as C

b = C.load_barrier("transcripts/row2/manifest.json")
rect = b["rect"]; p0 = b["prisms"][0]
def run(label, mut, expect_ok, expect_clause=None):
    p = copy.deepcopy(p0); mut(p)
    ok, msgs = C.check_prism(rect, p)
    verdict = "ACCEPT" if ok else "REJECT at " + msgs[0]
    good = (ok == expect_ok) and (expect_ok or (expect_clause in msgs[0]))
    print(f"[{'as expected' if good else 'UNEXPECTED'}] {label}: {verdict[:90]}")
    return good
res = []
r0 = list(p0["rows"][0])
res.append(run("box straddles 0 (row 0 value box := [-1,1] x [-1,1])", lambda p: p["rows"].__setitem__(0, (-1, 1, -1, 1, r0[4], r0[5])), False, "C-B6"))
res.append(run("empty box (reLo > reHi on row 3)", lambda p: p["rows"].__setitem__(3, (p["rows"][3][1] + 1, p["rows"][3][1], *p["rows"][3][2:])), False, "C-B5"))
res.append(run("argument row inverted (argLo > argHi)", lambda p: p["rows"].__setitem__(5, (*p["rows"][5][:4], 5, -5)), False, "C-B7"))
res.append(run("argument row too wide (argHi := A)", lambda p: p["rows"].__setitem__(7, (*p["rows"][7][:4], p["rows"][7][4], p["A"])), False, "C-B7"))
res.append(run("argument sum excludes 0 (every argument row shifted by +1: S = [93, 277])", lambda p: p.__setitem__("rows", [(a, b, c, d, e + 1, f + 1) for (a, b, c, d, e, f) in p["rows"]]), False, "C-B9"))
res.append(run("argument sum too wide (row 0 argHi := A/2, all others -A/2..A/2)", lambda p: p.__setitem__("rows", [(a, b, c, d, -p["A"] // 2, p["A"] // 2) for (a, b, c, d, e, f) in p["rows"]]), False, "C-B8"))
res.append(run("row removed", lambda p: p["rows"].pop(), False, "C-B4"))
res.append(run("mesh bottom[last] != x2", lambda p: p["mesh"]["bottom"].__setitem__(-1, (p["mesh"]["bottom"][-1][0] + 1, p["mesh"]["bottom"][-1][1])), False, "C-B3"))
res.append(run("mesh right not monotone (swap two interior breakpoints)", lambda p: (p["mesh"]["right"].__setitem__(1, p["mesh"]["right"][2]), p["mesh"]["right"].__setitem__(2, p["mesh"]["right"][1])) , False, "C-B3"))
res.append(run("floor too large (Fn := 10*Fn)", lambda p: p.__setitem__("Fn", 10 * p["Fn"]), False, "C-B11"))
res.append(run("gate: D := Fn*K/Fd (E + D >= floor)", lambda p: p.__setitem__("D", p["Fn"] * p["K"] // p["Fd"]), False, "C-B12"))
res.append(run("negative E", lambda p: p.__setitem__("E", -1), False, "C-B0"))
res.append(run("seam denominator 0", lambda p: p.__setitem__("td", 0), False, "C-B0"))
res.append(run("mesh denominator 0 (bottom[1].d := 0)", lambda p: p["mesh"]["bottom"].__setitem__(1, (p["mesh"]["bottom"][1][0], 0)), False, "C-B0"))
# the producer's floor is the largest the rows support and its prism length uses theta = 1/2 of the gate, so a
# valid weakening must relax the floor together with the boxes and stay above the gate: floor x 10/11
res.append(run("WEAKENED (valid): every box widened by 1 at K, floor x 10/11", lambda p: (p.__setitem__("rows", [(a - 1, b + 1, c - 1, d + 1, e, f) for (a, b, c, d, e, f) in p["rows"]]), p.__setitem__("Fd", 11 * p["Fd"]), p.__setitem__("Fn", 10 * p["Fn"])), True))
res.append(run("WEAKENED (valid): every argument row widened by 1 on each side", lambda p: p.__setitem__("rows", [(a, b, c, d, e - 1, f + 1) for (a, b, c, d, e, f) in p["rows"]]), True))
# chain-level controls
def chain(mut, expect_clause):
    bb = copy.deepcopy(b); mut(bb); msg = C.check_barrier_chain(bb)
    good = msg is not None and expect_clause in msg
    print(f"[{'as expected' if good else 'UNEXPECTED'}] chain: {msg}")
    return good
res.append(chain(lambda bb: bb["prisms"][0].__setitem__("tn", 1), "C-B13"))
res.append(chain(lambda bb: bb.__setitem__("t0", (bb["prisms"][-1]["tn"], bb["prisms"][-1]["td"])), "C-B13"))
res.append(chain(lambda bb: (bb["prisms"].__setitem__(3, dict(bb["prisms"][3], tn=bb["prisms"][4]["tn"], td=bb["prisms"][4]["td"]))), "C-B13"))
res.append(chain(lambda bb: bb.__setitem__("rect", (bb["rect"][0], bb["rect"][0], bb["rect"][2], bb["rect"][3])), "C-B2'"))
res.append(chain(lambda bb: bb.__setitem__("rect", (bb["rect"][0], bb["rect"][1], (0, 1), bb["rect"][3])), "C-B2'"))
print(f"{sum(res)}/{len(res)} controls behaved as expected")
sys.exit(0 if all(res) else 1)
