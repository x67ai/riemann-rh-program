# Reader check (Opus 5): I.8 bullets vs scout §6 and check-O item 5(d); zoo insert integrity.
import subprocess, hashlib, re
Z = open('BARRIER-ZOO.md', encoding='utf-8').read().split('\n')
S = open('results/c2-siegel/siegel-world-scout.md', encoding='utf-8').read().split('\n')
C = open('results/c2-siegel/check-O.md', encoding='utf-8').read().split('\n')
i = next(k for k, l in enumerate(Z) if l.startswith('### I.8 '))
print('I.8 heading at line', i + 1)
zb = [l for l in Z[i+1:i+8] if l.startswith('- **')]
print('zoo bullets:', [b[:20] for b in zb])
sb = S[159:163]   # lines 160-163
print('scout 160-163 starts:', [b[:20] for b in sb])
zb4 = [b for b in zb if not b.startswith('- **SOURCE')]
print('zoo 4 bullets == scout 160-163:', zb4 == sb)
# locate same bullets in check-O
for b in sb:
    hits = [k + 1 for k, l in enumerate(C) if l == b]
    print('  in check-O at lines', hits)
# original-line survival
old = subprocess.run(['git', 'show', '97d88e0:rh-program/BARRIER-ZOO.md'], capture_output=True).stdout.decode().split('\n')
new = subprocess.run(['git', 'show', '32d6c83:rh-program/BARRIER-ZOO.md'], capture_output=True).stdout.decode().split('\n')
j = 0
for l in new:
    if j < len(old) and l == old[j]:
        j += 1
print('old lines', len(old), 'matched in order', j, 'all survive:', j == len(old))
print('new - old =', len(new) - len(old))
cur = open('BARRIER-ZOO.md', encoding='utf-8').read()
print('working == 32d6c83:', cur == '\n'.join(new))
# headings by group
heads = [l for l in Z if l.startswith('### ')]
from collections import Counter
c = Counter(re.match(r'### (I|II|III|IV|V)\.\d', h).group(1) for h in heads)
print('headings', len(heads), dict(c))
for w in ['clearly', 'obviously', 'easy to see', 'well known', 'well-known']:
    added = [l for l in new if l not in old]
    print(w, sum(w in l.lower() for l in added))
