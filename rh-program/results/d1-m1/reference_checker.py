"""reference_checker.py -- UNTRUSTED reference implementation of the W1 checker (C1-C11).

Contract: results/d1-m1/FORMAT.md (normative) + w1-schema.json (shape).
Role: producer-side prevalidation and cross-validation of worked examples.  The TRUSTED
checker is the Lean one (decide +kernel); this file exists so that producers can reject
their own bad transcripts cheaply and so that the FORMAT.md micro-example arithmetic is
machine-recomputed rather than hand-trusted.

All arithmetic is exact Python int (arbitrary precision).  No floats anywhere.
Shape validation (the w1-schema.json semantics) is hand-implemented -- no external
jsonschema dependency; a transcript that passes here is both schema-valid and
checker-accepted.

Usage:
  python3 reference_checker.py FILE.json [FILE2.json ...]   # check transcripts
  python3 reference_checker.py --selftest                   # negative controls (FORMAT.md sec. 11)

Exit code 0 iff every requested check run ACCEPTs (selftest: iff all controls fail at the
intended check).
"""
import copy
import json
import re
import sys

INT_RE = re.compile(r'^-?(0|[1-9][0-9]*)$')
NAT_RE = re.compile(r'^(0|[1-9][0-9]*)$')
POS_RE = re.compile(r'^[1-9][0-9]*$')

TRUST_LABELS = {
    'zeta': 'kernel-checked modulo displayed hypotheses H-ENCL and H-AP (producers untrusted)',
    'f_DH': 'checker-level only (D-R8): format-checked modulo H-ENCL for f_DH; no Lean-backed conclusion',
}
ROW_KEYS = ('reLo', 'reHi', 'imLo', 'imHi', 'argLo', 'argHi')
TOP_REQUIRED = ('format', 'version', 'mode', 'function', 'trust_label',
                'rect', 'scales', 'claimed_m', 'mesh', 'segments')
TOP_OPTIONAL = ('modulus_floor', 'producer', 'comment')


class Fail(Exception):
    def __init__(self, check, msg):
        super().__init__(f'{check}: {msg}')
        self.check = check


# ---------------------------------------------------------------- shape (schema semantics)
def _int(s, pat, what):
    if not isinstance(s, str) or not pat.match(s):
        raise Fail('SHAPE', f'{what}: not a valid integer string: {s!r}')
    return int(s)


def _rat(obj, what):
    if not isinstance(obj, dict) or set(obj) != {'n', 'd'}:
        raise Fail('SHAPE', f'{what}: rational must be {{"n","d"}}: {obj!r}')
    return (_int(obj['n'], INT_RE, what + '.n'), _int(obj['d'], POS_RE, what + '.d'))


def parse(doc):
    """Shape-validate (w1-schema.json semantics) and translate to exact ints."""
    if not isinstance(doc, dict):
        raise Fail('SHAPE', 'top level must be an object')
    for k in TOP_REQUIRED:
        if k not in doc:
            raise Fail('SHAPE', f'missing required field {k!r}')
    for k in doc:
        if k not in TOP_REQUIRED + TOP_OPTIONAL:
            raise Fail('SHAPE', f'unknown field {k!r}')
    if doc['format'] != 'W1-rect-transcript':
        raise Fail('SHAPE', f'format must be "W1-rect-transcript": {doc["format"]!r}')
    if doc['version'] != '1.0':
        raise Fail('SHAPE', f'version must be "1.0": {doc["version"]!r}')
    if doc['mode'] not in ('refutation', 'exclusion'):
        raise Fail('SHAPE', f'bad mode {doc["mode"]!r}')
    if doc['function'] not in TRUST_LABELS:
        raise Fail('SHAPE', f'bad function {doc["function"]!r}')
    if doc['trust_label'] != TRUST_LABELS[doc['function']]:
        raise Fail('SHAPE', f'trust_label must be the fixed string for function {doc["function"]!r}')

    d = {'mode': doc['mode'], 'function': doc['function']}
    rect = doc['rect']
    if not isinstance(rect, dict) or set(rect) != {'sigma1', 'sigma2', 'T1', 'T2'}:
        raise Fail('SHAPE', 'rect must have exactly sigma1, sigma2, T1, T2')
    d['s1'] = _rat(rect['sigma1'], 'sigma1')
    d['s2'] = _rat(rect['sigma2'], 'sigma2')
    d['t1'] = _rat(rect['T1'], 'T1')
    d['t2'] = _rat(rect['T2'], 'T2')
    sc = doc['scales']
    if not isinstance(sc, dict) or set(sc) != {'K', 'A'}:
        raise Fail('SHAPE', 'scales must have exactly K, A')
    d['K'] = _int(sc['K'], POS_RE, 'K')
    d['A'] = _int(sc['A'], POS_RE, 'A')
    d['m'] = _int(doc['claimed_m'], NAT_RE, 'claimed_m')
    mesh = doc['mesh']
    if not isinstance(mesh, dict) or set(mesh) != {'bottom', 'right', 'top', 'left'}:
        raise Fail('SHAPE', 'mesh must have exactly bottom, right, top, left')
    for e in ('bottom', 'right', 'top', 'left'):
        lst = mesh[e]
        if not isinstance(lst, list) or len(lst) < 2:
            raise Fail('SHAPE', f'mesh.{e} must be a list of >= 2 rationals')
        d[e] = [_rat(x, f'mesh.{e}[{i}]') for i, x in enumerate(lst)]
    segs = doc['segments']
    if not isinstance(segs, list) or len(segs) < 4:
        raise Fail('SHAPE', 'segments must be a list of >= 4 rows')
    rows = []
    for i, r in enumerate(segs):
        if not isinstance(r, dict) or set(r) != set(ROW_KEYS):
            raise Fail('SHAPE', f'segments[{i}] must have exactly {ROW_KEYS}')
        rows.append(tuple(_int(r[k], INT_RE, f'segments[{i}].{k}') for k in ROW_KEYS))
    d['rows'] = rows
    if 'modulus_floor' in doc:
        fl = doc['modulus_floor']
        if not isinstance(fl, dict) or set(fl) != {'Fn', 'Fd'}:
            raise Fail('SHAPE', 'modulus_floor must have exactly Fn, Fd')
        d['floor'] = (_int(fl['Fn'], NAT_RE, 'Fn'), _int(fl['Fd'], POS_RE, 'Fd'))
    else:
        d['floor'] = None
    return d


# ---------------------------------------------------------------- rational comparisons (D7)
def rlt(a, b):
    return a[0] * b[1] < b[0] * a[1]


def rle(a, b):
    return a[0] * b[1] <= b[0] * a[1]


def req(a, b):
    return a[0] * b[1] == b[0] * a[1]


# ---------------------------------------------------------------- the checks C1-C11
def check(d, log):
    # C1 scales and denominators (denominators already syntactically positive via POS_RE,
    # re-verified here as the Lean checker would on translated literals)
    if not (d['K'] >= 1 and d['A'] >= 1):
        raise Fail('C1', 'K, A must be >= 1')
    for key in ('s1', 's2', 't1', 't2'):
        if d[key][1] < 1:
            raise Fail('C1', f'{key} denominator < 1')
    for e in ('bottom', 'right', 'top', 'left'):
        for x in d[e]:
            if x[1] < 1:
                raise Fail('C1', f'mesh.{e} denominator < 1')
    log('C1 pass: K=%d A=%d, all denominators >= 1' % (d['K'], d['A']))

    # C2 rectangle
    (p1, q1), (p2, q2) = d['s1'], d['s2']
    (a1, b1), (a2, b2) = d['t1'], d['t2']
    if not q1 < 2 * p1:
        raise Fail('C2', 'sigma1 <= 1/2')
    if not p1 * q2 <= p2 * q1:
        raise Fail('C2', 'sigma1 > sigma2')
    if not p2 < q2:
        raise Fail('C2', 'sigma2 >= 1')
    if not a1 * b2 < a2 * b1:
        raise Fail('C2', 'T1 >= T2')
    log('C2 pass: 1/2 < sigma1 <= sigma2 < 1, T1 < T2 (cross-multiplied)')

    # C3 mesh walk
    walks = [('bottom', d['s1'], d['s2'], 'inc'), ('right', d['t1'], d['t2'], 'inc'),
             ('top', d['s2'], d['s1'], 'dec'), ('left', d['t2'], d['t1'], 'dec')]
    for e, start, end, order in walks:
        lst = d[e]
        if not req(lst[0], start):
            raise Fail('C3', f'mesh.{e}[0] != edge start corner')
        if not req(lst[-1], end):
            raise Fail('C3', f'mesh.{e}[last] != edge end corner')
        for i in range(len(lst) - 1):
            ok = rlt(lst[i], lst[i + 1]) if order == 'inc' else rlt(lst[i + 1], lst[i])
            if not ok:
                raise Fail('C3', f'mesh.{e} not strictly {order} at index {i}')
    log('C3 pass: CCW walk, corners pinned, strict monotonicity per edge')

    # C4 row count
    M = sum(len(d[e]) - 1 for e in ('bottom', 'right', 'top', 'left'))
    if len(d['rows']) != M:
        raise Fail('C4', f'|segments| = {len(d["rows"])} != M = {M}')
    log(f'C4 pass: M = {M} segments')

    # C5 box validity
    for k, (reLo, reHi, imLo, imHi, _, _) in enumerate(d['rows']):
        if not (reLo <= reHi and imLo <= imHi):
            raise Fail('C5', f'row {k}: empty box')
    log('C5 pass: all value boxes nonempty')

    # C6 nonvanishing / mesh admissibility
    for k, (reLo, reHi, imLo, imHi, _, _) in enumerate(d['rows']):
        if not (reLo > 0 or reHi < 0 or imLo > 0 or imHi < 0):
            raise Fail('C6', f'row {k}: box contains 0 (no strict coordinate sign)')
    log('C6 pass: every segment box excludes 0')

    # C7 argument rows
    A = d['A']
    for k, (_, _, _, _, aLo, aHi) in enumerate(d['rows']):
        if not aLo <= aHi:
            raise Fail('C7', f'row {k}: argLo > argHi')
        if not (-A <= 2 * aLo and 2 * aHi <= A):
            raise Fail('C7', f'row {k}: argument row exceeds the half-turn clamp')
    log('C7 pass: argument rows valid and clamped to [-A/2, A/2]')

    # C8 sum width
    S_lo = sum(r[4] for r in d['rows'])
    S_hi = sum(r[5] for r in d['rows'])
    if not 2 * (S_hi - S_lo) < A:
        raise Fail('C8', f'2*(S_hi - S_lo) = {2 * (S_hi - S_lo)} >= A = {A}')
    log(f'C8 pass: S_lo = {S_lo}, S_hi = {S_hi}, 2*width = {2 * (S_hi - S_lo)} < A = {A}')

    # C9 integer containment
    m = d['m']
    if not (S_lo <= A * m <= S_hi):
        raise Fail('C9', f'A*m = {A * m} not in [{S_lo}, {S_hi}]')
    log(f'C9 pass: S_lo = {S_lo} <= A*m = {A * m} <= S_hi = {S_hi}')

    # C10 mode
    if d['mode'] == 'refutation' and not m >= 1:
        raise Fail('C10', 'mode refutation requires m >= 1')
    if d['mode'] == 'exclusion' and m != 0:
        raise Fail('C10', 'mode exclusion requires m = 0')
    log(f'C10 pass: mode {d["mode"]}, m = {m}')

    # C11 optional modulus floor
    if d['floor'] is not None:
        Fn, Fd = d['floor']
        K = d['K']
        for k, (reLo, reHi, imLo, imHi, _, _) in enumerate(d['rows']):
            mre = 0 if reLo <= 0 <= reHi else min(abs(reLo), abs(reHi))
            mim = 0 if imLo <= 0 <= imHi else min(abs(imLo), abs(imHi))
            if not (mre * mre + mim * mim) * Fd * Fd >= Fn * Fn * K * K:
                raise Fail('C11', f'row {k}: floor fails: ({mre}^2+{mim}^2)*{Fd}^2 < {Fn}^2*{K}^2')
        log(f'C11 pass: modulus floor {Fn}/{Fd} certified on all rows')
    else:
        log('C11 skipped: no modulus_floor field')
    return True


def run_file(path):
    print(f'== {path}')
    with open(path) as fh:
        doc = json.load(fh)
    try:
        d = parse(doc)
        check(d, lambda s: print('   ' + s))
        # AUDIT O MINOR-1 (applied at reconciliation 2026-09-02): the banner names the
        # function's own trust label (FORMAT.md sec. 9.2, D-R8) -- an f_DH acceptance is
        # checker-level only and carries no H-AP-backed conclusion.
        if doc.get('function') == 'zeta':
            label = 'conclusion holds modulo the displayed hypotheses H-ENCL, H-AP'
        else:
            label = ('checker-level only (D-R8): format-checked modulo H-ENCL for '
                     + str(doc.get('function')) + '; no Lean-backed conclusion')
        print(f'   VERDICT: ACCEPT (all checks pass; {label})')
        return True
    except Fail as e:
        print(f'   VERDICT: REJECT at {e}')
        return False


# ---------------------------------------------------------------- negative controls
def selftest(base_path):
    """Mutations of the refutation example; each must fail at the named check."""
    with open(base_path) as fh:
        base = json.load(fh)
    controls = []

    c = copy.deepcopy(base)   # box containing 0 -> C6
    c['segments'][2]['imLo'] = '-50'
    controls.append(('box contains 0', c, 'C6'))

    c = copy.deepcopy(base)   # over-wide argument rows -> C8
    c['segments'][0]['argLo'] = '-100'
    c['segments'][0]['argHi'] = '400'
    controls.append(('over-wide argument rows', c, 'C8'))

    c = copy.deepcopy(base)   # wrong m -> C9
    c['claimed_m'] = '2'
    controls.append(('claimed_m = 2', c, 'C9'))

    c = copy.deepcopy(base)   # exclusion with m = 1 -> C10
    c['mode'] = 'exclusion'
    controls.append(('mode exclusion with m = 1', c, 'C10'))

    c = copy.deepcopy(base)   # broken mesh -> C3
    c['mesh']['bottom'][2] = {'n': '69', 'd': '100'}
    controls.append(('bottom[last] != sigma2', c, 'C3'))

    c = copy.deepcopy(base)   # sigma1 = 1/2 -> C2
    c['rect']['sigma1'] = {'n': '1', 'd': '2'}
    c['mesh']['bottom'][0] = {'n': '1', 'd': '2'}
    controls.append(('sigma1 = 1/2', c, 'C2'))

    all_ok = True
    for name, doc, expect in controls:
        try:
            d = parse(doc)
            check(d, lambda s: None)
            print(f'   control {name!r}: UNEXPECTED ACCEPT  ** SELFTEST FAILURE **')
            all_ok = False
        except Fail as e:
            ok = e.check == expect
            all_ok = all_ok and ok
            tag = 'ok' if ok else f'** WRONG CHECK (expected {expect}) **'
            print(f'   control {name!r}: rejected at {e.check} [{tag}]  ({e})')
    return all_ok


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    if args[0] == '--selftest':
        import os
        base = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'w1-example-refutation.json')
        print('== negative controls (mutations of w1-example-refutation.json)')
        sys.exit(0 if selftest(base) else 1)
    ok = all(run_file(p) for p in args)
    sys.exit(0 if ok else 1)
