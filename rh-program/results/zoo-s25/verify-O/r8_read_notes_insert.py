# Reader (Opus 5), zoo-s25: insert three dated READ notes into BARRIER-ZOO.md, each as its own line directly after
# the rider line it corrects. Additions only; each anchor asserted exactly once; refuses to run twice; verifies that
# every original line survives in order and that exactly 3 lines were added; lints the notes.
import sys, hashlib
from pathlib import Path
Z = Path('BARRIER-ZOO.md')
old = Z.read_text(encoding='utf-8')
MARK = '**[READ 2026-09-24, Opus 5'
if MARK in old:
    sys.exit('READ notes of 2026-09-24 already present; refusing to insert twice.')
lines = old.split('\n')
ANCH = {
 'iv18': '- **[RIDER 2026-09-24, Session 24, entered at the Session-25 zoo stream — (i) the pole cap at t = 0 on rung 3',
 'iv9c4': '- **[RIDER 2026-09-24, Session 24 (digest §C.3 item 3), entered at the Session-25 zoo stream — the campaign\'s close 4',
 'v3': '- **[RIDER 2026-09-24, Session 24 (digest §C.3 item 5), entered at the Session-25 zoo stream — a scale-blind acceptance criterion',
}
NOTE = {
 'iv18': "- **[READ 2026-09-24, Opus 5: one hypothesis list inside the rider above completed; nothing moves.]** \"(Lemma C, from w ≥ 0 and ∫μ_y = 1 alone)\" omits the kernel's sign: the cap (ŵ ∗ μ_y)(0) = ∫ŵμ_y ≤ ŵ(0)∫μ_y uses |ŵ(ξ)| ≤ ŵ(0) (from w ≥ 0) together with μ_y ≥ 0 AND ∫μ_y = 1 — `results/c2-siegel/siegel-world-scout.md` §2.2, Lemma C's proof and \"Which hypothesis does what\" (\"the cap itself uses only w ≥ 0 … and μ_y ≥ 0 of mass one\"; Lemma P(i)–(ii)). Both kernel facts hold for every y ∈ [0, ½), so the cap, the thresholds D₁ = 500.937 and D₁⁺ = 3701.45 (re-derived by direct quadrature of μ_0 ∗ A_K for this read: 500.936739…, 3701.4497…, `results/zoo-s25/verify-O/r2_thresholds_run.log`) and the seven ŵ_B-means 0.12 … 2.78 (reproduced from (0.3_K) at the seven fundamental discriminants, `verify-O/r3_lowzero_share_run.log`) stand as printed.",
 'iv9c4': "- **[READ 2026-09-24, Opus 5: the last sentence of the rider above outruns its records; corrected here, no number moves.]** \"the gap to the true ≈ 1.1L remains a factor ≈ 66 whose whole content is the c_B gap\" — the factor 73/1.1 ≈ 66 is right, but it is not all c_B. Both records the rider cites state the close as \"the price of c_B … **plus the uniformity relaxations**\" (`results/c2-m2/campaign/CAMPAIGN.md` §4 item 4; `results/c2-followups/insights-digest.md` §C.3 item 3), and with R₀ = 73 the split is explicit: the addendum's exponent 13/8 has asymptote (13/(16c_B))² = 32.30 (`separation-note.md` addendum A3; `check-O.md` §12.8), so ≈ 73/32.30 = 2.26 of the gap is the uniformity relaxation (finite L₀ = 50, the one-point check) and ≈ (0.7071/c_B)² = 24.5 is the c_B gap against the saddle-point rate 1/√2 (the remaining ≈ 1.2 is (13/(16·0.7071))² = 1.32 against the measured ≈ 1.1). Read the sentence as \"a factor ≈ 66, of which ≈ 24.5 is the c_B gap and ≈ 2.3 the uniformity relaxations\" (arithmetic: `results/zoo-s25/verify-O/r7_r0_gap_run.log`).",
 'v3': "- **[READ 2026-09-24, Opus 5: two precisions to the rider above, both carried from its records; the verdict \"scale-blind\" is strengthened, not weakened.]** (1) The measured value 1.9·10⁻³² (1.857e-32) is printed in `results/c2-m2/SHARED.md` checkpoint (5) as \"Max |Z_DH(gamma)| over the builder's 39 on-line points at 25 digits\", beside the campaign's t = 114.16 control row, not over the M2 control's 36 points at t = 85.7; the recipe (sign changes of Z_DH refined by `findroot` on Z_DH at 15 digits) is the same in all three scripts (`results/c2-m6/check-O.md` §3, \"Which record files the correction touches\"). (2) \"≈ 10⁻²⁰ … 10⁻³³ across the window\" is carried verbatim from `check-O.md` §3; recomputed for this read over the recorded points u = 57.04 … 112.38 of the ±30 window at 85.7, e^{−πu/4} runs 3.5·10⁻²⁰ … 4.7·10⁻³⁹ and |Γ(¾ + iu/2)| runs 2.0·10⁻¹⁹ … 3.2·10⁻³⁸ (≈ 10⁻³⁰ at u ≈ 87, as `m6-rung1-note.md` §5.3 says), and over the ±30 window at 114.16 e^{−πu/4} runs 2.0·10⁻²⁹ … 6.7·10⁻⁵⁰ (`results/zoo-s25/verify-O/r4_gamma_scale_run.log`). The factor is smaller than printed at the upper end of the window, so an absolute tolerance certifies even less there.",
}
for k in ('iv18', 'iv9c4', 'v3'):
    for w in ('clearly', 'obviously', 'easy to see', 'well known', 'well-known'):
        assert w not in NOTE[k].lower(), (k, w)
idx = {}
for k, a in ANCH.items():
    hits = [i for i, l in enumerate(lines) if l.startswith(a)]
    if len(hits) != 1:
        sys.exit('anchor %s found %d times' % (k, len(hits)))
    idx[k] = hits[0]
new = list(lines)
for k in sorted(idx, key=lambda k: -idx[k]):
    new.insert(idx[k] + 1, NOTE[k])
j = 0
for l in new:
    if j < len(lines) and l == lines[j]:
        j += 1
assert j == len(lines), 'an original line did not survive'
assert len(new) - len(lines) == 3
assert sum(l.startswith('### ') for l in new) == 58
text = '\n'.join(new)
Z.write_text(text, encoding='utf-8')
for k in idx:
    print(k, 'rider at line', idx[k] + 1)
print('inserted at lines', sorted(new.index(NOTE[k]) + 1 for k in NOTE))
print('SHA-256', hashlib.sha256(text.encode('utf-8')).hexdigest())
