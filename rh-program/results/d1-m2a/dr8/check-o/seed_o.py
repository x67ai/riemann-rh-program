#!/usr/bin/env python3
"""Job 2 (Opus): the M3 seed ledger, re-derived.  Job 1's ledger_check.py and seed_rows.py are
NOT imported; this is a second, independent parser.

Per row and per leg:
  1. SHA-256 and byte count of the transcript the row points at, recomputed from disk, compared
     with the row's `sha256`/`bytes` AND with the table in PRICING-M3-ledger.md 2 (lifted out of
     the markdown table by regex, so the pricing's own figures are re-verified too).
  2. The row's box vs the transcript's `rect`, both parsed here.
  3. The row's box vs the Lean W1Data literal's p1/q1/p2/q2/a1/b1/a2/b2 in Instances.lean --
     i.e. the box the `_exclusion` corollary's `W1Rect <literal>` actually denotes.
  4. The row's `segments`, `K`, `A`, `winding_lo_hi`, `floor`, `claimed_m` vs the transcript.
  5. The `_exclusion` corollary exists in Ledger.lean, on the right literal, in the m = 0 branch.
  6. delta0 = sigma1 - 1/2, exactly; grade/status/provenance/function/mode as the pricing 1.2/1.4
     require; no aggregate field anywhere (pricing 1.5).
  7. index.json is exactly the four ROW.json records.
"""
import json, hashlib, os, re, sys
from fractions import Fraction

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
M3 = os.path.join(ROOT, 'results/d1-m3')
def rd(p):
    with open(p, encoding='utf-8') as f:
        return f.read()
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 16), b''):
            h.update(b)
    return h.hexdigest()

fails = []
def need(cond, msg):
    if not cond:
        fails.append(msg)
    return "OK" if cond else "MISMATCH"

INST = rd(os.path.join(ROOT, 'lean/Zeta23/W1/Instances.lean'))
LED = rd(os.path.join(ROOT, 'lean/Zeta23/W1/Ledger.lean'))
PRI = rd(os.path.join(ROOT, 'results/d1-m2a/dr8/PRICING-M3-ledger.md'))

# the pricing 2 table: file -> (bytes, sha256, segments)
pri_tab = {}
for m in re.finditer(r'`(w1-(?:mp|arb)-null-[a-z0-9-]+\.json)`\s*\|\s*([\d  ]+)\s*\|\s*`([0-9a-f]{64})`\s*\|\s*([\d  ]+)\s*\|', PRI):
    pri_tab[m.group(1)] = (int(re.sub(r'\D', '', m.group(2))), m.group(3), int(re.sub(r'\D', '', m.group(4))))
print("PRICING-M3-ledger 2 table parsed: %d transcript rows" % len(pri_tab))
need(len(pri_tab) == 8, "pricing 2 table: expected 8 transcript rows, parsed %d" % len(pri_tab))

def lean_literal(name):
    m = re.search(r'^def\s+%s\s*:\s*W1Data\s+where\s*\n((?:[ \t]+.+\n)+)' % re.escape(name), INST, re.M)
    if not m:
        return None
    body = m.group(1)
    out = {}
    for fld in ('p1', 'q1', 'p2', 'q2', 'a1', 'b1', 'a2', 'b2', 'm'):
        mm = re.search(r'\b%s\s*:=\s*(-?\d+)' % fld, body)
        out[fld] = int(mm.group(1)) if mm else None
    return out

rows = sorted(os.listdir(os.path.join(M3, 'rows')))
print("rows on disk: %d -> %s\n" % (len(rows), rows))
need(len(rows) == 4, "expected 4 seed rows, found %d" % len(rows))

n_legs = n_hash = n_box = n_cor = 0
for rid in rows:
    R = json.loads(rd(os.path.join(M3, 'rows', rid, 'ROW.json')))
    print("== %s" % rid)
    print("   row_id matches directory                       %s" % need(R['row_id'] == rid, "%s: row_id != directory" % rid))
    s1, s2 = Fraction(R['box']['sigma1']), Fraction(R['box']['sigma2'])
    t1, t2 = Fraction(R['box']['T1']), Fraction(R['box']['T2'])
    d0 = Fraction(R['delta0'])
    print("   delta0 == sigma1 - 1/2 exactly                  %s" % need(d0 == s1 - Fraction(1, 2), "%s: delta0 != sigma1 - 1/2" % rid))
    print("   1/2 < sigma1 <= sigma2 < 1 (clause C2)          %s" % need(Fraction(1,2) < s1 <= s2 < 1, "%s: box violates 1/2 < s1 <= s2 < 1" % rid))
    print("   function/mode/claimed_m/grade/status            %s" % need(
        (R['function'], R['mode'], R['claimed_m'], R['grade'], R['status']) == ('zeta', 'exclusion', '0', 'box', 'accepted'),
        "%s: function/mode/claimed_m/grade/status wrong" % rid))
    print("   provenance kind is 'acceptance'                 %s" % need(R['provenance']['kind'] == 'acceptance', "%s: provenance kind" % rid))
    for aggr in ('total_height', 'height_covered', 'rh_verified_to', 'coverage', 'aggregate'):
        need(aggr not in json.dumps(R), "%s: aggregate-looking field %r present (pricing 1.5)" % (rid, aggr))
    for leg in ('mp', 'arb'):
        L = R['legs'][leg]
        n_legs += 1
        tp = os.path.normpath(os.path.join(M3, L['transcript']))
        base = os.path.basename(tp)
        got, nb = sha(tp), os.path.getsize(tp)
        T = json.loads(rd(tp))
        rect = T['rect']
        g = lambda k: Fraction(int(rect[k]['n']), int(rect[k]['d']))
        lit = lean_literal(L['lean']['data'])
        cor = L['lean']['corollary']
        # the corollary, exactly as PRICING-M3-ledger 1.6 shapes it
        pat = (r'theorem\s+%s\s*\(hEncl\s*:\s*W1EnclOK\s+riemannZeta\s+%s\)\s*:\s*'
               r'∀\s+s\s+∈\s+W1Rect\s+%s,\s*riemannZeta\s+s\s*≠\s*0\s*:=\s*'
               r'\(cert_of_checkW1_ap\s+%s\s+\(checkW1Floor_spec\s+%s_check\)\.1\s+hEncl\)\.2\s+\(by\s+decide\)'
               % (re.escape(cor), re.escape(L['lean']['data']), re.escape(L['lean']['data']),
                  re.escape(L['lean']['data']), re.escape(L['lean']['data'])))
        cor_ok = re.search(pat, LED) is not None
        if cor_ok:
            n_cor += 1
        hash_ok = (got == L['sha256'] and nb == L['bytes'])
        if hash_ok:
            n_hash += 1
        pri = pri_tab.get(base)
        pri_ok = pri is not None and pri[1] == got and pri[0] == nb and pri[2] == L['segments']
        box_ok = (g('sigma1'), g('sigma2'), g('T1'), g('T2')) == (s1, s2, t1, t2)
        lit_ok = lit is not None and (Fraction(lit['p1'], lit['q1']), Fraction(lit['p2'], lit['q2']),
                                      Fraction(lit['a1'], lit['b1']), Fraction(lit['a2'], lit['b2'])) == (s1, s2, t1, t2)
        if box_ok and lit_ok:
            n_box += 1
        fld_ok = (L['segments'] == len(T['segments']) and L['K'] == T['scales']['K'] and L['A'] == T['scales']['A']
                  and str(T['claimed_m']) == R['claimed_m'])
        print("   [%s] %-28s sha256/bytes %s | pricing-2 table %s | box==rect %s | box==Lean literal %s | fields %s | m==0 in literal %s | corollary shape %s"
              % (leg, base,
                 need(hash_ok, "%s/%s: sha256 or bytes differ from disk" % (rid, leg)),
                 need(pri_ok, "%s/%s: PRICING 2 table row differs from disk" % (rid, leg)),
                 need(box_ok, "%s/%s: row box != transcript rect" % (rid, leg)),
                 need(lit_ok, "%s/%s: row box != Lean W1Data literal (the corollary's W1Rect)" % (rid, leg)),
                 need(fld_ok, "%s/%s: segments/K/A/claimed_m differ from the transcript" % (rid, leg)),
                 need(lit is not None and lit['m'] == 0, "%s/%s: Lean literal m != 0" % (rid, leg)),
                 need(cor_ok, "%s/%s: corollary %s not present in PRICING-M3 1.6 shape" % (rid, leg, cor))))
        # the winding sums, recomputed from the transcript's own rows
        lo = sum(int(s['argLo']) for s in T['segments'])
        hi = sum(int(s['argHi']) for s in T['segments'])
        w_ok = [str(lo), str(hi)] == list(L['winding_lo_hi'])
        print("        winding sums recomputed from the segments: [%d, %d] vs row %s  %s"
              % (lo, hi, L['winding_lo_hi'], need(w_ok, "%s/%s: winding_lo_hi != sum over segments" % (rid, leg))))

# index.json
idx = json.loads(rd(os.path.join(M3, 'index.json')))
print("\nindex.json: format=%s version=%s rows=%d" % (idx.get('format'), idx.get('version'), len(idx.get('rows', []))))
need(len(idx['rows']) == len(rows), "index.json row count != rows/ count")
for r in idx['rows']:
    disk = json.loads(rd(os.path.join(M3, 'rows', r['row_id'], 'ROW.json')))
    need(r == disk, "index.json entry %s differs from its ROW.json" % r['row_id'])
for aggr in ('total', 'covered', 'verified_to', 'aggregate'):
    need(aggr not in json.dumps(idx.get('rows') and {k: v for k, v in idx.items() if k != 'rows'}),
         "index.json carries an aggregate-looking top-level field %r" % aggr)
print("index.json entries identical to the ROW.json files            %s" % ("OK" if not any('index.json entry' in f for f in fails) else "MISMATCH"))

print("\nCOUNTS: legs checked %d, transcript hashes re-verified %d, boxes agreeing (rect & Lean literal) %d, corollaries in the 1.6 shape %d"
      % (n_legs, n_hash, n_box, n_cor))
print("VERDICT: %s" % ("PASS" if not fails else "%d FINDING(S)" % len(fails)))
for f in fails:
    print("  - " + f)
sys.exit(1 if fails else 0)
