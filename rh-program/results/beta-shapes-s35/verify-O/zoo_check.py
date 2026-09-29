# Reader (Opus 5): verify each zoo citation of the NOTE lies inside the named entry.
import re, os
Z = open(os.path.join(os.path.dirname(__file__), '..','..','..','BARRIER-ZOO.md'), encoding='utf-8').read()
lines = Z.split('\n')
heads = [(i, l) for i, l in enumerate(lines) if l.startswith('### ')]
def entry(tag):
    for k,(i,l) in enumerate(heads):
        if l.startswith('### '+tag+' '):
            j = heads[k+1][0] if k+1 < len(heads) else len(lines)
            return '\n'.join(lines[i:j])
    return None
def n(s): return re.sub(r'\s+',' ',s)
cites = [
 ('III.20', "Deligne's squeeze additionally needs RATIONALITY (finitely many eigenvalues of fixed weight)"),
 ('III.20', "the exact coordinate with no archimedean analog, where the transfer dies"),
 ('III.20', "Selberg has (B)-shape without (A)'s tower"),
 ('III.20', "real off-line exceptions persist"),
 ('III.20', "NEVER acts on the zeta's own explicit formula"),
 ('III.20', "a construction brief on any printed square of Spec Z must first exhibit a pairing defined independently of N(u)"),
 ('IV.13', "is Z-linearly independent (unique factorization)"),
 ('IV.13', "The kill is a dimension count"),
 ('IV.13', "is Q-linearly independent and spans an infinite-dimensional Q-subspace of R"),
 ('IV.13', "B1 (dual-check): let M be a closed 3-manifold"),
 ('IV.11', "In Deninger's dynamical system for Spec Z"),
 ('IV.11', "There are no fixed points of the flow"),
 ('IV.12', "Theorem T (Opus 5 adjudicator"),
 ('IV.12', "its entire content is the bookkeeping"),
 ('IV.14', "Hypotheses, exactly as fixed in f1-check-O.md §4.4"),
 ('IV.15', "S4′ as stated in Session 14 (ledger §15) had four clauses"),
 ('IV.16', "satisfy the contract of digest §I in its manifold case"),
 ('IV.10', "the Λ-square squares the absolute point"),
 ('IV.10', "Hom test returns the identity alone"),
 ('IV.10', "this rider claims no Z-form of Theorems 4.1(b) or 4.2"),
 ('III.21', "The positivity ENGINE being real does not make the SUBSTRATE arithmetic"),
 ('I.1', "THE CCM CASE STUDY"),
 ('I.1', "DH passes CCM's"),
 ('V.1', "The brief-time rule"),
 ('V.5', "The Grossmann-condition rule"),
 ('IV.12', "solved case"),
]
for tag, s in cites:
    e = entry(tag)
    ok = e is not None and n(s) in n(e)
    first = n(e.split('\n',1)[1])[:0] if e else ''
    print(('OK  ' if ok else 'MISS'), tag, '|', s[:80])
# first words of each STATEMENT
for tag in ['I.1','III.20','III.21','IV.10','IV.11','IV.12','IV.13','IV.14','IV.15','IV.16','V.1','V.5']:
    e = entry(tag); m = re.search(r'\*\*STATEMENT[^*]*\*\*\s*(.{0,120})', e or '')
    print('STATEMENT first words', tag, '|', n(m.group(1)) if m else '(no STATEMENT tag)')
print('IV.20 present in zoo:', '### IV.20' in Z)
