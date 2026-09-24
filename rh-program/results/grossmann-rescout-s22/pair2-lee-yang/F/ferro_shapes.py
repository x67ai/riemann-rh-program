# Scout F: the STRUCTURE THEOREM and the genus-2 decision at m <= 2.
# THEOREM (root at z = -1).  For a +-1 ferromagnet with couplings J_e >= 0 and support graph G = {e : J_e > 0}:
#   Z_J(-1) = sum_sigma (-1)^{#up} e^{-H} = (-1)^N Z_0 <sigma_1 ... sigma_N>_0, and (high-temperature expansion,
#   e^{J s s'} = cosh J (1 + s s' tanh J))  <sigma_A>_0 = sum_{F subset G : odd-degree set of F = A} prod_{e in F} tanh J_e /
#   sum_{F : all degrees even} prod tanh J_e, every term > 0.  Such an F exists iff |A meets C| is even for every component C.
#   Hence: an EVEN-size connected component C has Z_C(-1) != 0 (A = C); an ODD-size component has Z_C(-1) = 0 (spin flip)
#   and Z_C'(-1) = -(-1)^n Z_0/2 * sum_{i in C} <sigma_{C - i}> != 0 (|C - i| even), a SIMPLE root.  Z_J = prod_C Z_C.
#   => the multiplicity of the root -1 of Z_J equals the number of odd-size components of G.
# COROLLARY.  If Z_J(z) = c * P~(z) (1+z)^m with P~(-1) != 0 and deg P~ = 4, then G has exactly m odd components and
#   prod_C [Z_C(z)/(1+z)^{[|C| odd]}] = c P~(z), the reduced factors having degrees |C| - [|C| odd] summing to 4; so the
#   non-isolated part of G is one of {4}, {5}, {2,2}, {2,3}, {3,3} (sizes 6+ have reduced degree >= 6 > 4), and every
#   realization at any m is one of these plus m - (#odd among them) isolated sites.  Realizable at some m  <=>  at some m <= 2.
#   Shapes {2,2}, {2,3}, {3,3} are products of one-factor-per-zero-pair systems: P~ = (1 + c1 z + z^2)(1 + c2 z + z^2),
#   c_j = -2 cos theta_j; a 2-site factor needs c > 0 (J = -1/2 log(c/2)); a 3-site reduced factor needs c > -1
#   ((1+cz+z^2)(1+z) = 1 + (1+c) z + (1+c) z^2 + z^3 = the 3-site system with sum_i e^{-2 rowsum_i} = 1 + c in (0, 3]:
#   the uniform one has 3 e^{-4J} = 1 + c).  Shapes {4} (m = 0) and {5} (m = 1) are CONNECTED realizations, decided numerically.
# Part A: numerical sanity check of the theorem.  Part B: the per-class decision.  Part C: the pricing's example at m = 7.
import json, math, sys, time, itertools
import numpy as np
from ferro_core import structure, make_funcs, solve, poly_mul, JCAP, TOL
import ferro_core
t0 = time.time()
rng = np.random.default_rng(7)

def Z_coeffs(N, J, edges):
    c = np.zeros(N + 1)
    for sig in itertools.product((1, -1), repeat=N):
        e = sum(J[k] * sig[i] * sig[j] for k, (i, j) in enumerate(edges))
        c[sum(1 for s in sig if s == 1)] += math.exp(e)
    return c

def mult_minus1(c, tol=1e-9):
    """multiplicity of the root -1 of the polynomial with ascending coefficients c (by repeated exact-ish division)."""
    c = list(c / np.max(np.abs(c))); m = 0
    while True:
        if abs(sum(ci * (-1) ** i for i, ci in enumerate(c))) > tol * max(1.0, sum(abs(x) for x in c)): return m
        # divide by (1+z)
        q = [0.0] * (len(c) - 1)
        rem = c[:]
        for i in range(len(c) - 1, 0, -1):
            q[i - 1] = rem[i]; rem[i - 1] -= q[i - 1]; rem[i] = 0.0
        c = q; m += 1
        if len(c) == 0: return m

def odd_components(N, J, edges):
    parent = list(range(N))
    def find(a):
        while parent[a] != a: parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for k, (i, j) in enumerate(edges):
        if J[k] > 0: parent[find(i)] = find(j)
    sizes = {}
    for i in range(N): sizes[find(i)] = sizes.get(find(i), 0) + 1
    return sum(1 for s in sizes.values() if s % 2 == 1), sorted(sizes.values())

print("== Part A: sanity check of the root-at-(-1) theorem on random ferromagnets (N = 3..7, random support graphs) ==")
bad = 0; tot = 0
for N in range(3, 8):
    edges = list(itertools.combinations(range(N), 2))
    for trial in range(60):
        J = rng.uniform(0.05, 1.5, len(edges)) * (rng.uniform(size=len(edges)) < rng.uniform(0.1, 0.8))
        c = Z_coeffs(N, J, edges)
        mm = mult_minus1(c); od, sz = odd_components(N, J, edges)
        tot += 1
        if mm != od:
            bad += 1; print("  MISMATCH", N, sz, mm, od)
print(f"  trials {tot}, mismatches {bad}  (multiplicity of -1 == number of odd components in every trial: {bad == 0})")

# LEMMA (r_2 versus r_1, any N).  s_i := prod_{j != i} w_ij in (0,1] (finite J), r_1 = sum s_i.  Each 2-subset weight is
#   W({i,j}) = prod_{k not in {i,j}} w_ik w_jk = s_i s_j / w_ij^2 >= s_i s_j, so r_2 >= e_2(s) = (r_1^2 - sum s_i^2)/2, and
#   sum s_i^2 <= n + f^2 (convex in s, maximized at a vertex (1,..,1,f,0,..,0) of {0 <= s_i <= 1, sum s_i = r_1}),
#   n = floor(r_1), f = r_1 - n.  Hence r_2 >= L(r_1) := C(n,2) + n f, with STRICT inequality at finite J when r_1 is not an
#   integer (the vertex has zero entries, i.e. infinite couplings).  Shape {4}: (r_1, r_2) = (b1, b2); shape {5}: (1 + b1, b1 + b2).
def Lbound(tau):
    n = math.floor(tau); f = tau - n
    return n * (n - 1) / 2 + n * f
print("\n== Part B: per-class decision at m <= 2, both signs (JCAP = %.1f) ==" % JCAP)
classes = json.load(open("g2_classes.json"))
out = {}
for c in classes:
    p, a1, a2 = c['p'], c['a1'], c['a2']
    for s in (1, -1):
        b1 = s * a1 / math.sqrt(p); b2 = a2 / p
        # roots x_j = 2 cos theta_j of x^2 + b1 x + (b2 - 2) = 0 ;  c_j = -x_j
        disc = b1 * b1 - 4 * (b2 - 2)
        x1 = (-b1 + math.sqrt(max(disc, 0))) / 2; x2 = (-b1 - math.sqrt(max(disc, 0))) / 2
        c1, c2 = -x1, -x2
        rec = dict(p=p, a1=a1, a2=a2, sign=s, b1=b1, b2=b2, c=[c1, c2], disc=disc, shapes={}, least_m=None, cert=None)
        # factorized shapes (exact inequalities)
        rec['shapes']['2,2'] = bool(c1 > 0 and c2 > 0)
        rec['shapes']['2,3'] = bool((c1 > 0 and c2 > -1) or (c2 > 0 and c1 > -1))
        rec['shapes']['3,3'] = bool(c1 > -1 and c2 > -1)
        P = [1.0, b1, b2, b1, 1.0]
        # connected shapes by the free-J solver (which may also return a disconnected solution; we record the support shape)
        for m, shape in ((0, '4'), (1, '5')):
            T = P
            for _ in range(m): T = poly_mul(T, [1.0, 1.0])
            N = 4 + m
            if min(T) <= 0:
                rec['shapes'][shape] = dict(status='nonpositive', mincoef=min(T)); continue
            t = [T[k] / T[0] for k in range(1, N // 2 + 1)]
            if abs(t[0] - round(t[0])) > 1e-9 and t[1] <= Lbound(t[0]) + 1e-12:
                rec['shapes'][shape] = dict(status='lemma', r1=t[0], r2=t[1], L=Lbound(t[0])); continue
            r = solve(N, t)
            edges = structure(N)[0]
            od, sz = odd_components(N, np.array(r['J']), edges) if r['ok'] else (None, None)
            if r['ok'] and abs(t[0] - round(t[0])) > 1e-9 and t[1] <= Lbound(t[0]) + 1e-12:
                print("   LEMMA CONTRADICTION on an accepted solution:", p, a1, a2, s, shape, r['Jmax']); r['ok'] = False
            rec['shapes'][shape] = dict(status='realized' if r['ok'] else ('cap' if r['at_cap'] else 'notfound'), err=r['err'],
                                        smin=r['smin'], Jmin=r['Jmin'], Jmax=r['Jmax'], support=sz, J=r['J'])
        # least m
        if rec['shapes']['2,2'] or rec['shapes']['4'].get('status') == 'realized': rec['least_m'] = 0
        elif rec['shapes']['2,3'] or rec['shapes']['5'].get('status') == 'realized': rec['least_m'] = 1
        elif rec['shapes']['3,3']: rec['least_m'] = 2
        # certificate of non-realizability (when least_m is None): what excludes each shape
        if rec['least_m'] is None:
            rec['cert'] = dict(fact=f"c=({c1:.4f},{c2:.4f}): {{2,2}} needs both > 0, {{2,3}} needs one > 0 and the other > -1, {{3,3}} needs both > -1",
                               shape4=rec['shapes']['4'].get('status'), shape5=rec['shapes']['5'].get('status'))
        out[f"{p},{a1},{a2},{'id' if s == 1 else 'flip'}"] = rec
json.dump(out, open("ferro_shapes_state.json", "w"), indent=0)

# summary
def status(rec, sh): return rec['shapes'][sh] if isinstance(rec['shapes'][sh], bool) else rec['shapes'][sh]['status']
cls = {}
for key, rec in out.items(): cls.setdefault((rec['p'], rec['a1'], rec['a2']), {})[rec['sign']] = rec
n = len(cls)
real_id = sum(1 for v in cls.values() if v[1]['least_m'] is not None)
real_any = sum(1 for v in cls.values() if v[1]['least_m'] is not None or v[-1]['least_m'] is not None)
print(f"classes: {n}; realized at some m <= 2 with the identity sign: {real_id}; with identity or flip: {real_any}; unrealized under both signs: {n - real_any}")
from collections import Counter
lm = Counter(min([v[1]['least_m'] if v[1]['least_m'] is not None else 99, v[-1]['least_m'] if v[-1]['least_m'] is not None else 99]) for v in cls.values())
print("least m over classes (best sign; 99 = unrealized):", sorted(lm.items()))
# connected-only vs factorized-only
conn = 0; fact_only = 0; both = 0
for v in cls.values():
    has_conn = any(status(v[s], sh) == 'realized' and v[s]['shapes'][sh]['support'] is not None and max(v[s]['shapes'][sh]['support']) >= 4 for s in (1, -1) for sh in ('4', '5'))
    has_fact = any(v[s]['shapes'][sh] for s in (1, -1) for sh in ('2,2', '2,3', '3,3'))
    if has_conn and has_fact: both += 1
    elif has_conn: conn += 1
    elif has_fact: fact_only += 1
print(f"realized classes with a CONNECTED realization ({{4}} or {{5}} with a connected support found): {conn + both}  (of which also factorizable: {both});  realized ONLY by a factorized (one 2- or 3-site block per zero pair) shape: {fact_only}")
big = [(k, sh, rec['shapes'][sh]['Jmax']) for k, rec in out.items() for sh in ('4', '5') if rec['shapes'][sh].get('status') == 'realized' and rec['shapes'][sh]['Jmax'] > 4.0]
print(f"accepted connected solutions with max coupling J > 4 (scrutinized: w = e^-2J < 3.4e-4): {len(big)}")
for k, sh, jm in big: print("   ", k, "shape", sh, f"Jmax={jm:.3f}")
lem = [(k, sh) for k, rec in out.items() for sh in ('4', '5') if rec['shapes'][sh].get('status') == 'lemma']
print(f"(class,sign,shape) excluded by the r_2 >= L(r_1) lemma (coefficients positive): {len(lem)}")
# suspicious: shape 4 / 5 positivity holds but solver failed
sus = [(k, sh, rec['shapes'][sh]['status'], rec['shapes'][sh]['err']) for k, rec in out.items() for sh in ('4', '5') if rec['shapes'][sh].get('status') in ('notfound', 'cap')]
print(f"(class,sign,shape) with positive coefficients where the connected solve did NOT certify a realization: {len(sus)}")
for k, sh, st, err in sus: print("   ", k, "shape", sh, st, f"err={err:.2e}", "least_m by other shapes:", out[k]['least_m'])
# per-sign counts of exclusions
print("unrealized classes (both signs), with certificates:")
for key, v in sorted(cls.items()):
    if v[1]['least_m'] is None and v[-1]['least_m'] is None:
        r = v[1]
        print(f"  ({key[0]},{key[1]},{key[2]}): b=(1,{r['b1']:.4f},{r['b2']:.4f}) c(id)=({r['c'][0]:.4f},{r['c'][1]:.4f}); shape4/5 (id): {status(r,'4')}/{status(r,'5')}; shape4/5 (flip): {status(v[-1],'4')}/{status(v[-1],'5')}")

print("\n== Part C: the pricing's example (3,0,-2) at m = 7 (N = 11), coefficients positive, free-J solve ==")
p, a1, a2 = 3, 0, -2
P = [1.0, 0.0, a2 / p, 0.0, 1.0]; T = P
for _ in range(7): T = poly_mul(T, [1.0, 1.0])
print("  coefficients of P~(z)(1+z)^7:", [round(x, 4) for x in T], " all positive:", min(T) > 0)
t = [T[k] / T[0] for k in range(1, 11 // 2 + 1)]
r = solve(11, t)
print(f"  best residual over {r['starts']} starts: {r['err']:.3e}; realized: {r['ok']}; Jmax={r['Jmax']:.3f}; at cap: {r['at_cap']}  (theorem: impossible — needs 7 odd components on 11 sites with reduced degree 4, i.e. {{3,3}}+5 or {{5}}+6 or {{2,3}}+6 or {{4}}/{{2,2}}+7; c = (-1.633, +1.633) fails {{3,3}}, and P~(1+z) has a negative coefficient)")
print(f"elapsed s: {time.time()-t0:.1f}")
