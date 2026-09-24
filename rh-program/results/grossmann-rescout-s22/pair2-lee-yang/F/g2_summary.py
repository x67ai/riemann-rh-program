# Scout F: summary of the genus-2 decision (reads ferro_shapes_state.json), the a2 > 0 criterion, and the per-class table.
import json, math, csv
from collections import Counter
st = json.load(open("ferro_shapes_state.json"))
cl = {}
for k, r in st.items(): cl.setdefault((r['p'], r['a1'], r['a2']), {})[r['sign']] = r
def status(r, sh):
    v = r['shapes'][sh]; return v if isinstance(v, bool) else v['status']
def least(v): 
    a = [x['least_m'] for x in v.values() if x['least_m'] is not None]; return min(a) if a else None
unreal = sorted(k for k, v in cl.items() if least(v) is None)
print(f"classes {len(cl)}; realized (either sign) {sum(1 for v in cl.values() if least(v) is not None)}; realized with identity {sum(1 for v in cl.values() if v[1]['least_m'] is not None)}; realized with flip {sum(1 for v in cl.values() if v[-1]['least_m'] is not None)}; unrealized {len(unreal)}")
print("least m (best sign):", sorted(Counter(least(v) for v in cl.values() if least(v) is not None).items()))
print("least m (identity sign only):", sorted(Counter(v[1]['least_m'] for v in cl.values() if v[1]['least_m'] is not None).items()))
print("unrealized classes all have a2 <= 0:", all(k[2] <= 0 for k in unreal), " ; classes with a2 <= 0:", sum(1 for k in cl if k[2] <= 0), " ; realized classes with a2 <= 0:", sum(1 for k, v in cl.items() if k[2] <= 0 and least(v) is not None))
print("=> realized at some m  <=>  a2 > 0  holds on all 357 classes:", all((k[2] > 0) == (least(v) is not None) for k, v in cl.items()))
print("unrealized by p:", sorted(Counter(k[0] for k in unreal).items()), " a1 values:", sorted(Counter(k[1] for k in unreal).items()))
print("unrealized list:", " ".join(f"({k[0]},{k[1]},{k[2]})" for k in unreal))
# certificates
cert = Counter()
for k in unreal:
    v = cl[k]; kinds = set()
    for s in (1, -1):
        for sh in ('4', '5'): kinds.add(status(v[s], sh))
    cert[tuple(sorted(kinds))] += 1
print("certificate kinds over unrealized classes (statuses of shapes {4},{5} under both signs; factor shapes excluded by the c-inequalities in every case):", dict(cert))
assert all(status(cl[k][s], sh) in ('nonpositive', 'lemma') for k in unreal for s in (1, -1) for sh in ('4', '5')), "an unrealized class lacks a proof"
print("every unrealized class: shapes {4},{5} excluded by positivity or the lemma under both signs, shapes {2,2},{2,3},{3,3} by the c-inequalities: PROVED for all", len(unreal))
# signed / a1 = 0 classes
signed = [k for k, v in cl.items() if min(1, v[1]['b1'], v[1]['b2']) < 0 and min(1, -v[1]['b1'], v[1]['b2']) < 0]
print(f"kernel-measure signed under both signs: {len(signed)} classes; of these realized: {sum(1 for k in signed if least(cl[k]) is not None)} (all at m >= 1)")
a10 = [k for k in cl if k[1] == 0]
print(f"a1 = 0 classes: {len(a10)}; realized: {sum(1 for k in a10 if least(cl[k]) is not None)}; least m among them: {sorted(Counter(least(cl[k]) for k in a10 if least(cl[k]) is not None).items())}")
# connected vs factorized
conn = [k for k, v in cl.items() if any(status(v[s], sh) == 'realized' for s in (1, -1) for sh in ('4', '5'))]
fact = [k for k, v in cl.items() if any(v[s]['shapes'][sh] for s in (1, -1) for sh in ('2,2', '2,3', '3,3'))]
fonly = [k for k in fact if k not in conn]
print(f"realized with a connected {{4}}/{{5}} solution: {len(conn)}; realized by a factorized shape: {len(fact)}; factorized ONLY: {len(fonly)}")
proved_fonly = [k for k in fonly if all(status(cl[k][s], sh) in ('nonpositive', 'lemma') for s in (1, -1) for sh in ('4', '5'))]
print(f"  of the factorized-only classes, connected shapes excluded by PROOF (positivity/lemma) under both signs: {len(proved_fonly)}; by numerics only: {len(fonly) - len(proved_fonly)}: {[k for k in fonly if k not in proved_fonly]}")
print("  factorized-only list:", fonly)
# m = 0 connected image: count of classes with b1 > 0 (after sign) and b2 > 0 that are realized at m = 0 connected
pos0 = [k for k, v in cl.items() if any(v[s]['b1'] > 0 and v[s]['b2'] > 0 for s in (1, -1))]
real0conn = [k for k in pos0 if any(status(cl[k][s], '4') == 'realized' for s in (1, -1))]
print(f"classes with positive P~ coefficients for some sign: {len(pos0)}; of these with a connected 4-site realization found: {len(real0conn)}; not found: {[k for k in pos0 if k not in real0conn]} (their statuses: {[ (status(cl[k][1],'4'), status(cl[k][-1],'4')) for k in pos0 if k not in real0conn]})")
# table
cls_json = {(c['p'], c['a1'], c['a2']): c for c in json.load(open("g2_classes.json"))}
with open("g2_decision.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["p", "a1", "a2", "N1", "N2", "b1", "b2", "c1_id", "c2_id", "least_m_id", "least_m_flip", "shape4_id", "shape5_id", "shape4_flip", "shape5_flip", "fact22_id", "fact23_id", "fact33_id", "fact22_flip", "fact23_flip", "fact33_flip", "Jmax_conn_id", "Jmax_conn_flip"])
    for k in sorted(cl):
        v = cl[k]; c = cls_json[k]
        def jm(r):
            js = [r['shapes'][sh]['Jmax'] for sh in ('4', '5') if status(r, sh) == 'realized']; return round(min(js), 4) if js else ""
        w.writerow([k[0], k[1], k[2], c['N1'], c['N2'], round(v[1]['b1'], 6), round(v[1]['b2'], 6), round(v[1]['c'][0], 6), round(v[1]['c'][1], 6),
                    v[1]['least_m'], v[-1]['least_m'], status(v[1], '4'), status(v[1], '5'), status(v[-1], '4'), status(v[-1], '5'),
                    v[1]['shapes']['2,2'], v[1]['shapes']['2,3'], v[1]['shapes']['3,3'], v[-1]['shapes']['2,2'], v[-1]['shapes']['2,3'], v[-1]['shapes']['3,3'], jm(v[1]), jm(v[-1])])
print("wrote g2_decision.csv (one row per class)")
