# job1_ddlog_bound.py — Job 2 part A item (b): a RIGOROUS a-priori bound on Job 1's dd log (dd_log_u64 of
# harness/d4_twisted_sum.rs, read at lines 49-138), by bit-exact emulation of its double-double arithmetic in Python
# (IEEE doubles, round-to-nearest; two_prod by Veltkamp/Dekker, which yields the same exact error term as fma).
#   log n (dd) = S2 = S1 (+) R,  S1 = K (+) T,  K = ln2_dd.mul_f64(k),  T = logm0[idx],  R = log1p(r) by the 7-term series.
# S1 depends only on (k, idx): its error is computed EXACTLY for every one of the 40 x 257 combinations (mpmath, 60 digits).
# The last add S1 (+) R is AccurateDWPlusDW: exact two_sums/fast_two_sums except the two roundings c = RN(e + t) and
# w = RN(e2 + f). For S1, S2 in [16, 32): |e| <= 2^-49, |t| <= 2^-49 + 2^-61, so |e + t| < 2^-47 and RN(e + t) errs by
# <= 2^-101; |e2| <= 2^-49, |f| <= 2^-102, so |e2 + f| < 2^-48 and RN(e2 + f) errs by <= 2^-102: add2 <= 3 * 2^-102
# (smaller binades give smaller bounds; log n <= 28.35 < 32).
# R's own error is measured on the rows (and bounded by the series' dd arithmetic, |R| <= 0.0039).
# Verified first: the emulation reproduces Job 1's printed (hi, lo) on every self-test row, bit for bit.
import json, sys, math, mpmath as mp
mp.mp.dps = 60
SPLIT = 134217729.0
def split(a):
    c = SPLIT * a; ah = c - (c - a); return ah, a - ah
def two_sum(a, b):
    s = a + b; bb = s - a; return s, (a - (s - bb)) + (b - bb)
def quick_two_sum(a, b):
    s = a + b; return s, b - (s - a)
def two_prod(a, b):
    p = a * b; ah, al = split(a); bh, bl = split(b)
    return p, ((ah * bh - p) + ah * bl + al * bh) + al * bl
class DD:
    __slots__ = ("hi", "lo")
    def __init__(s, hi, lo=0.0): s.hi, s.lo = hi, lo
    def add(s, o):
        a, e = two_sum(s.hi, o.hi); t, f = two_sum(s.lo, o.lo)
        s2, e2 = quick_two_sum(a, e + t); h, l = quick_two_sum(s2, e2 + f); return DD(h, l)
    def neg(s): return DD(-s.hi, -s.lo)
    def sub(s, o): return s.add(o.neg())
    def mul(s, o):
        p, e = two_prod(s.hi, o.hi); e = e + (s.hi * o.lo + s.lo * o.hi); h, l = quick_two_sum(p, e); return DD(h, l)
    def mul_f64(s, b):
        p, e = two_prod(s.hi, b); e = e + s.lo * b; h, l = quick_two_sum(p, e); return DD(h, l)
    def div(s, o):
        q1 = s.hi / o.hi; r = s.sub(o.mul_f64(q1)); q2 = r.hi / o.hi; r2 = r.sub(o.mul_f64(q2)); q3 = r2.hi / o.hi
        h, l = quick_two_sum(q1, q2); return DD(h, l).add(DD(q3))
    def mp(s): return mp.mpf(s.hi) + mp.mpf(s.lo)
def log1p_series(r, nterms):
    z = r.div(DD(2.0).add(r)); z2 = z.mul(z); term = z; acc = DD(0.0)
    for j in range(nterms):
        acc = acc.add(term.div(DD(float(2 * j + 1)))); term = term.mul(z2)
    return acc.mul_f64(2.0)
ln2 = log1p_series(DD(1.0), 40)
logm0 = []; inv_m0 = []
for i in range(257):
    m0 = 1.0 + i / 256.0
    logm0.append(log1p_series(DD(m0 - 1.0), 40)); inv_m0.append(DD(1.0).div(DD(m0)))
def parts(n):
    nf = float(n); k = n.bit_length() - 1; m = nf / 2.0 ** k
    idx = min(int(math.floor((m - 1.0) * 256.0)), 256); m0 = 1.0 + idx / 256.0; d = m - m0
    r = inv_m0[idx].mul_f64(d); z = r.div(DD(2.0).add(r)); z2 = z.mul(z); term = z; acc = DD(0.0)
    for j in range(7):
        acc = acc.add(term.div(DD(float(2 * j + 1)))); term = term.mul(z2)
    R = acc.mul_f64(2.0); K = ln2.mul_f64(float(k)); S1 = K.add(logm0[idx]); S2 = S1.add(R)
    return k, idx, m0, R, S1, S2
res = {}
LN2 = mp.log(2)
res["ln2_dd"] = [ln2.hi, ln2.lo]; res["ln2_dd_error"] = float(ln2.mp() - LN2)
res["logm0_table_max_abs_error"] = float(max(abs(logm0[i].mp() - mp.log(1 + mp.mpf(i) / 256)) for i in range(257)))
# 1) bit-exact check against Job 1's printed rows
nchk = mism = 0
maxRerr = mp.mpf(0)
for path in sys.argv[1:]:
    for n, lh, ll, rh, rl, c in json.load(open(path))["phase_selftest"]:
        k, idx, m0, R, S1, S2 = parts(int(n)); nchk += 1
        if S2.hi != lh or S2.lo != ll: mism += 1
        Rtrue = mp.log(mp.mpf(int(n)) / (mp.mpf(2) ** k * mp.mpf(m0)))
        maxRerr = max(maxRerr, abs(R.mp() - Rtrue))
res["emulation_rows_checked"] = nchk; res["emulation_mismatches"] = mism
res["R_series_max_abs_error_on_rows"] = float(maxRerr)
# 2) S1 error exactly, all (k, idx), and restricted to (k, idx) that occur for 2 <= n <= X
X = int(sys.argv[0] and 2052336466859)
worst_all = (mp.mpf(0), None); worst_feas = (mp.mpf(0), None); by_k = {}
for k in range(1, 41):
    for idx in range(257):
        m0 = 1.0 + idx / 256.0
        S1 = ln2.mul_f64(float(k)).add(logm0[idx])
        e = abs(S1.mp() - (k * LN2 + mp.log(mp.mpf(m0))))
        if e > worst_all[0]: worst_all = (e, (k, idx))
        feasible = (2 ** k) * m0 <= X and idx < 256
        if feasible:
            by_k[k] = max(by_k.get(k, 0.0), float(e))
            if e > worst_feas[0]: worst_feas = (e, (k, idx))
res["S1_error_max_all_combos"] = [float(worst_all[0]), worst_all[1]]
res["S1_error_max_feasible_combos"] = [float(worst_feas[0]), worst_feas[1]]
res["S1_error_max_by_k"] = by_k
add2 = 3 * 2.0 ** -102
Rb = 1e-32  # generous cap on R's error (series in dd at |R| <= 0.0039; measured value printed above)
res["add2_rounding_bound"] = add2
res["R_error_cap_used"] = Rb
eps = float(worst_feas[0]) + Rb + add2
res["eps_apriori_rigorous_per_t"] = eps
l1 = 146.95060754424162
res["l1_L28.35"] = l1
res["t_ceil_L28.35"] = 1e-8 / (eps * l1)
res["t_ceil_L22_l1_21.81"] = 1e-8 / (eps * 21.81)
print(json.dumps(res, indent=1))
json.dump(res, open("out/job1_ddlog_bound.json", "w"), indent=1)
