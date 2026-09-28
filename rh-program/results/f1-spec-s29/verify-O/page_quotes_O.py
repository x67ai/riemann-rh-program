"""F1 reader (Opus 5), Session 29: every page-level ground the SPEC's §1/§3 rows rest on,
checked by extracting the named PDF page (pdftotext -layout) and searching a normalized snippet.
Page numbers are PDF page indices unless noted; a miss is reported, never silently passed."""
import subprocess, re, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
S = "results/d2-scout-s26/sources/"
def page(pdf, p):
    return subprocess.run(["pdftotext", "-layout", "-f", str(p), "-l", str(p), os.path.join(ROOT, pdf), "-"],
                          capture_output=True, text=True).stdout
def norm(s):
    s = s.replace("ﬁ", "fi").replace("ﬀ", "ff").replace("’", "'").replace("‘", "'")
    return re.sub(r"[\s\-]+", "", s).lower()
checks = [
 # (label, pdf, page(s), snippet)
 ("Borger p7 must be defined", S+"O-arxiv-0906.3146.pdf", [7], "must be defined to be the Witt space"),
 ("Borger p7 v! left adjoint", S+"O-arxiv-0906.3146.pdf", [7], "The left adjoint v! of v"),
 ("Borger p8 absolute point", S+"O-arxiv-0906.3146.pdf", [8], "call Spec Z, viewed as a Λ-space, the absolute point"),
 ("Borger p8 extends to curves", S+"O-arxiv-0906.3146.pdf", [8], "any smooth curve over a finite field"),
 ("Borger p9 toric P^n Frobenius", S+"O-arxiv-0906.3146.pdf", [9], "projective spaces Pn do, once we choose homogeneous"),
 ("Borger p15 Teichmuller by adjunction", S+"O-arxiv-0906.3146.pdf", [15], "giving a Λ-map Z[t]"),
 ("Borger p15 a_i = [b_i]", S+"O-arxiv-0906.3146.pdf", [15], "shows that ai = [bi ]"),
 ("Borger p24 factorization", S+"O-arxiv-0906.3146.pdf", [24], "We will now construct a factorization of topos maps"),
 ("Borger p25 f essential", S+"O-arxiv-0906.3146.pdf", [25], "f is essential, meaning that f"),
 ("Borger p25 (pr,Fr^n)", S+"O-arxiv-0906.3146.pdf", [25], "the graphs of all powers of the Frobenius map on S"),
 ("Borger p25 not a monomorphism", S+"O-arxiv-0906.3146.pdf", [25], "is not a monomorphism"),
 ("Borger p27 Cor 7.6 fully faithful", S+"O-arxiv-0906.3146.pdf", [27], "separated reduced algebraic spaces over k fully faithfully"),
 ("Borger p27 7.7 uniformity (no arithmetic Spec k)", S+"O-arxiv-0906.3146.pdf", [27], "true arithmetic analogue of the base point Spec k"),
 ("Borger p28 7.8 Drinfeld: objects not descending to Sp_k", S+"O-arxiv-0906.3146.pdf", [27], "objects of SpFS1 that do not descend to Spk"),
 ("Borger p5 archimedean caveat", S+"O-arxiv-0906.3146.pdf", [5], "says nothing about the archimedean place of Q"),
 ("Borger p3 Thm 0.1 Artin-Tate", S+"O-arxiv-0906.3146.pdf", [3], "only abelian Artin–Tate motives"),
 ("0801.1691 p10 §1.10 Z ghost congruences", S+"O-arxiv-0801.1691.pdf", [10], "mod p1+ordp (j)"),
 ("0801.1691 p3 W right adjoint", S+"O-arxiv-0801.1691.pdf", [3], "right adjoint"),
 ("0801.1691 p22 §3.9 Teichmuller ghost", S+"O-arxiv-0801.1691.pdf", [22], "the image of a is"),
 ("1006.0092 p31 Krull", "results/zoo-s27/prior-art/S27-1006.0092.pdf", [31], "the Krull dimension of Wn (A) agrees with that of A[0,n]"),
 ("Milne p10 Example 1.7 adjunction", "results/e3-borger-rung1/sources/milne-1509.00797.pdf", [10], "adjunction formula"),
 ("Milne p10 number of points", "results/e3-borger-rung1/sources/milne-1509.00797.pdf", [10], "number of points on C rational over k0"),
 ("Milne p9 Thm 1.5 from Hodge index", "results/e3-borger-rung1/sources/milne-1509.00797.pdf", [9], "by the Hodge index theorem"),
 ("Le Bruyn 1304.6532 p3 P1F1 x Spec Z = P1Z", "results/zoo-s27/prior-art/S27-1304.6532.pdf", [3], "concrete proposal for Smirnov"),
 ("Le Bruyn p3 explore Smirnov maps in Borger", "results/zoo-s27/prior-art/S27-1304.6532.pdf", [3], "we will explore how Smirnov"),
 ("Le Bruyn p2 ABC", "results/zoo-s27/prior-art/S27-1304.6532.pdf", [2], "ABC-conjecture for Z provided"),
 ("Le Bruyn p30 Smirnov constants F_1^2 = {0,1,-1}", "results/zoo-s27/prior-art/S27-1304.6532.pdf", [30], "Q∩F1 = {0}∪{1, −1}"),
 ("Le Bruyn p40 Q: Smirnov covering maps in w(Z)?", "results/zoo-s27/prior-art/S27-1304.6532.pdf", [40], "can we make sense of"),
 ("Le Bruyn p41 Teichmuller 1/(1-at)", "results/zoo-s27/prior-art/S27-1304.6532.pdf", [41], "determined by a"),
 ("Lorscheid 1801.05337 p3 Smirnov map -> abc", S+"O-arxiv-1801.05337.pdf", [3], "would imply the"),
 ("Lorscheid 1801.05337 p3 KS95 content", S+"O-arxiv-1801.05337.pdf", [3], "cohomological invariants of arithmetic curves"),
 ("Durov 0704.2030 p43 Z (x)F1 Z = Z", S+"O-arxiv-0704.2030.pdf", [43], "Z ⊗F1 Z = Z"),
 ("CC 1805.10501 p2 H1 still open", S+"O-arxiv-1805.10501.pdf", [2], "still open"),
 ("CC 1805.10501 p18 N(u)", S+"O-arxiv-1805.10501.pdf", [18], "distribution N (u)"),
 ("Takagi 1203.4914 p4 Z^n not defined", S+"O-arxiv-1203.4914.pdf", [4], "not defined appropriately yet"),
 ("Banaszak-Uetake 0908.2909 p1 equiv RH", S+"S27-0908.2909.pdf", [1], "equivalent to the Riemann Hypothesis"),
 ("Scholze 1712.03708 p14 hypothetical", S+"O-arxiv-1712.03708.pdf", [14], "hypothetical"),
 ("Lorscheid 1204.3129 p11", S+"O-arxiv-1204.3129.pdf", [11], "Frobenius"),
 ("Haran 1508.04636 p51 Thm 2.9.1", S+"O-arxiv-1508.04636.pdf", [51], "2.9.1"),
 ("CCM math/0703392 p4 principal divisors", "fetched/y-07-connes-consani-marcolli-2009-weil-proof-geometry-adeles-class-space.pdf", [4], "principal divisors"),
 ("Haran 1991 p259 surface reduces to diagonal", "fetched-r3/haran1991.pdf", None, "reduces to the diagonal"),
 ("YZ 1304.3538 p3 Thm 1.1", S+"O-arxiv-1304.3538.pdf", [3], "Theorem 1.1"),
]
miss = 0
for lab, pdf, pages, snip in checks:
    found = []
    if pages is None:
        n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", os.path.join(ROOT, pdf)], capture_output=True, text=True).stdout).group(1))
        pages = list(range(1, n + 1))
    for p in pages:
        if norm(snip) in norm(page(pdf, p)): found.append(p)
    ok = bool(found)
    miss += (not ok)
    print(f"{'OK  ' if ok else 'MISS'} {lab:55s} pdf-page {found if ok else pages}")
print("misses:", miss)
