/* s8cert.c -- S8(rho) generator with every cell decision PROVED, plus block moments of n^{-sigma}.
   Written for lemmaB-s41/U6-certificate from the definition only (s40 CHARTER §1; Lindley form, s41 CHARTER §2(a)).
   Lattice x_k = 1 + (k - 1/2) t, t = 1/rho. A composite in cell k (x_{k-1} < c < x_k) counts in c_k; a g-prime is placed
   at x_k iff e_{k-1} = 0 and c_k = 0; e_k = max(e_{k-1} + c_k - 1, 0); N(x_k) = k + 1 + e_k.
   Composites are generated as P*q, q = largest g-prime factor, P a "prefix" (g-integer > 1 with P*P^+(P) <= X).
   Rigor: every value is a double with a proved relative error bound (standard model, |delta| <= u = 2^-53, no FMA
   contraction); a cell decision is accepted only if the computed distance to both lattice neighbours exceeds the
   proved error bound; otherwise it is re-decided EXACTLY in GMP integers from the lattice indices of the factors and a
   dyadic enclosure TLO/2^D <= t <= THI/2^D (params.txt, from pi_enclosure.py).
   Build: cc -O2 -ffp-contract=off -o s8cert s8cert.c -I/opt/homebrew/include -L/opt/homebrew/lib -lgmp -lm
   Usage: s8cert <params.txt> <name> <Xmax> <outprefix> [Lmax_cells]                                           */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <gmp.h>

typedef __int128 i128;
static const double U = 0x1p-53;          /* unit roundoff */
static const double SL = 0x1p-30;         /* emission slack s (>> all relative error bounds ~1e-14) */

static double TT, RHO;                    /* TT = RN(t) (|TT - t| <= u t); RHO only for guesses */
static mpz_t TLO, THI, P2;                /* TLO/2^D <= t <= THI/2^D ; P2 = 2^(D+1) */
static int DD;

static void die(const char *m) { fprintf(stderr, "FATAL: %s\n", m); printf("FATAL: %s\n", m); exit(2); }

/* lattice point / g-prime value: fl(1 + fl((k - 1/2) * TT)); relative error <= 3.0001 u (NOTE §2) */
static inline double xt(uint64_t k) { return 1.0 + ((double)k - 0.5) * TT; }

/* ---------- exact decisions in GMP ----------
   c = prod_{i<n} (1 + (k_i - 1/2) t) = prod (P2 + (2k_i - 1) T) / P2^n   (t = T / 2^D), increasing in t.
   mode 0: compare c with lattice point x_m = (P2 + (2m-1) T)/P2 (increasing in t);
   mode 1: compare c with the integer V.
   Returns +1 if c > target for every t in the enclosure, -1 if c < target for every t, 0 if undecided. */
static mpz_t gL, gH, gR, gS, gF;
static int exact_cmp(const uint32_t *ks, int n, int mode, uint64_t m_or_V) {
    mpz_set_ui(gL, 1); mpz_set_ui(gH, 1);
    for (int i = 0; i < n; i++) {
        mpz_mul_ui(gF, TLO, 2 * (unsigned long)ks[i] - 1); mpz_add(gF, gF, P2); mpz_mul(gL, gL, gF);
        mpz_mul_ui(gF, THI, 2 * (unsigned long)ks[i] - 1); mpz_add(gF, gF, P2); mpz_mul(gH, gH, gF);
    }
    int res = 0;
    if (mode == 0) {
        if (m_or_V == 0) return +1;                     /* x_0 < 1 < c */
        mpz_pow_ui(gS, P2, n - 1);
        mpz_mul_ui(gF, THI, 2 * m_or_V - 1); mpz_add(gF, gF, P2); mpz_mul(gR, gF, gS);   /* x_m(t_hi) scaled */
        if (mpz_cmp(gL, gR) > 0) res = +1;
        mpz_mul_ui(gF, TLO, 2 * m_or_V - 1); mpz_add(gF, gF, P2); mpz_mul(gR, gF, gS);   /* x_m(t_lo) scaled */
        if (mpz_cmp(gH, gR) < 0) res = (res == 0) ? -1 : 99;
    } else {
        mpz_pow_ui(gS, P2, n); mpz_mul_ui(gR, gS, m_or_V);
        if (mpz_cmp(gL, gR) > 0) res = +1;
        if (mpz_cmp(gH, gR) < 0) res = (res == 0) ? -1 : 99;
    }
    if (res == 99) die("inconsistent exact comparison");
    return res;
}

/* proved lower bound for min(c - x_{k-1}, x_k - c)/c, from the same integers (statistics of the exact path) */
static double qd(mpz_t a, mpz_t b) {           /* a/b as a double, for huge a, b > 0 */
    long ea, eb; double ma = mpz_get_d_2exp(&ea, a), mb = mpz_get_d_2exp(&eb, b);
    return ldexp(ma / mb, (int)(ea - eb));
}
static double exact_margin(const uint32_t *ks, int n, uint64_t k) {
    mpz_set_ui(gL, 1); mpz_set_ui(gH, 1);
    for (int i = 0; i < n; i++) {
        mpz_mul_ui(gF, TLO, 2 * (unsigned long)ks[i] - 1); mpz_add(gF, gF, P2); mpz_mul(gL, gL, gF);
        mpz_mul_ui(gF, THI, 2 * (unsigned long)ks[i] - 1); mpz_add(gF, gF, P2); mpz_mul(gH, gH, gF);
    }
    mpz_pow_ui(gS, P2, n - 1);
    mpz_mul_ui(gF, THI, 2 * (k - 1) - 1); mpz_add(gF, gF, P2); mpz_mul(gR, gF, gS);   /* x_{k-1}(t_hi) */
    mpz_sub(gF, gL, gR); double a = qd(gF, gL);
    mpz_mul_ui(gF, TLO, 2 * k - 1); mpz_add(gF, gF, P2); mpz_mul(gR, gF, gS);         /* x_k(t_lo) */
    mpz_sub(gF, gR, gH); double b = qd(gF, gH);
    return a < b ? a : b;
}

/* ---------- storage ---------- */
typedef struct { double v; uint32_t cur; int32_t parent; uint32_t last; uint8_t om; } Pre;   /* prefix record */
static Pre *pre; static uint64_t npre, cappre;
static uint32_t *pk; static uint64_t npk, cappk;     /* lattice indices of stored g-primes (value <= Xstore) */
static uint32_t fact[80]; static int nfact;

static void build_fact(int64_t pid, uint32_t jq) {   /* factor list of pre[pid] * prime pk[jq] */
    nfact = 0; fact[nfact++] = pk[jq];
    while (pid >= 0) { if (nfact >= 79) die("fact overflow"); fact[nfact++] = pk[pre[pid].last]; pid = pre[pid].parent; }
}

/* statistics of the decisions */
static uint64_t ndec, nfb, nfbV;
static double INFL = 1.0;          /* test hook: S8C_INFLATE > 1 widens the error bounds, forcing the exact path */
static double CLOSE_THR = 1e-16;   /* exact-path decisions with relative margin below this are printed (CLOSE lines) */
static double minrel = 1e300, minrel_at;

/* ---------- cell decision ----------
   c~ = computed value of a g-integer with om prime factors: |c~ - c| <= 4.0003 om u c~ (NOTE §2, Lemma 2.1).
   Lattice values: |x~ - x| <= 3.0002 u x~.  dl = c~ - x~_{k-1}, dr = x~_k - c~ (one rounding each).
   Accepted iff dl > bnd and dr > bnd with bnd = 1.01 (4.02 om + 3.0002) u max(c~, x~_k)  =>  x_{k-1} < c < x_k. */
static uint64_t cell_of(double c, int om, int64_t pid, uint32_t jq) {
    int64_t k = (int64_t)floor((c - 1.0) * RHO + 0.5) + 1;
    double coef = INFL * 1.01 * (4.02 * om + 3.0002) * U;
    ndec++;
    for (int it = 0; it < 6; it++) {
        double xl = xt(k - 1), xr = xt(k);
        double m = c > xr ? c : xr;
        double bnd = coef * m;
        double dl = c - xl, dr = xr - c;
        if (dl > bnd && dr > bnd) {
            double r = (dl < dr ? dl : dr) / c;
            if (r < minrel) { minrel = r; minrel_at = c; }
            return (uint64_t)k;
        }
        if (dl < -bnd) { k--; continue; }
        if (dr < -bnd) { k++; continue; }
        break;                                   /* close call: decide exactly */
    }
    build_fact(pid, jq); nfb++;
    for (int it = 0; it < 6; it++) {
        int sl = exact_cmp(fact, nfact, 0, (uint64_t)(k - 1));
        int sr = exact_cmp(fact, nfact, 0, (uint64_t)k);
        if (sl == 0 || sr == 0) die("exact cell decision undecided (enlarge D)");
        if (sl > 0 && sr < 0) {
            double r = exact_margin(fact, nfact, (uint64_t)k);
            if (r < minrel) { minrel = r; minrel_at = c; }
            if (r < CLOSE_THR) {                         /* audit trail for an independent high-precision recheck */
                printf("CLOSE k=%lld rel=%.6e c~=%.6f factors", (long long)k, r, c);
                for (int i = 0; i < nfact; i++) printf(" %u", fact[i]);
                printf("\n");
            }
            return (uint64_t)k;
        }
        if (sl < 0) k--; else k++;
    }
    die("exact cell search failed");
    return 0;
}

/* is the g-integer (value c~, om factors) <= the integer V ?  (equality impossible: t transcendental) */
static int le_V(double c, int om, double V, int64_t pid, uint32_t jq, int is_prime_k, uint64_t kprime) {
    double bnd = INFL * 1.01 * (4.02 * (om > 0 ? om : 1) + 1.0) * U * (c > V ? c : V);
    double d = c - V;
    if (d > bnd) return 0;
    if (d < -bnd) return 1;
    nfbV++;
    if (is_prime_k) { uint32_t kk = (uint32_t)kprime; int s = exact_cmp(&kk, 1, 1, (uint64_t)V); if (!s) die("V undecided"); return s < 0; }
    build_fact(pid, jq);
    int s = exact_cmp(fact, nfact, 1, (uint64_t)V);
    if (!s) die("V undecided");
    return s < 0;
}

/* ---------- block moments ----------
   Block (e,i): [a, a + W), a = 2^e (1 + i/256), W = 2^(e-8). z = (n~ - a)/W in [0,1) is EXACT.
   lo[j] <= sum z^j 2^62 <= hi[j] (j = 1..7), proved: p_j = fl(p_{j-1} z) has relative error <= gamma_{j-1} <= 6.0001 u,
   and fl(q -/+ q 2^-49) moves q = p_j 2^62 by >= 14.9 u q outward (NOTE §3). */
#define NE 40
#define JM 7
typedef struct { uint64_t cnt; int ommax; i128 lo[JM + 1], hi[JM + 1]; } Blk;
static Blk blk[NE][256];
static void mom_add(double n, int om) {
    int e = ilogb(n);
    double mm = ldexp(n, -e);
    int i = (int)((mm - 1.0) * 256.0);
    double a = ldexp(1.0 + i / 256.0, e);
    double z = ldexp(n - a, 8 - e);
    if (!(z >= 0.0 && z < 1.0) || e >= NE) die("block assignment");
    Blk *b = &blk[e][i];
    b->cnt++; if (om > b->ommax) b->ommax = om;
    double p = z, q = ldexp(p, 62);
    b->lo[1] += (int64_t)q; b->hi[1] += (int64_t)q;
    for (int j = 2; j <= JM; j++) {
        p = p * z; q = ldexp(p, 62);
        double d = ldexp(q, -49);
        double lo = q - d, hi = q + d;
        b->lo[j] += (int64_t)floor(lo); b->hi[j] += (int64_t)ceil(hi);
    }
}
static void print_i128(FILE *f, i128 x) {
    char buf[64]; int n = 0; int neg = x < 0; unsigned __int128 y = neg ? -(unsigned __int128)x : (unsigned __int128)x;
    if (y == 0) buf[n++] = '0';
    while (y) { buf[n++] = '0' + (int)(y % 10); y /= 10; }
    if (neg) fputc('-', f);
    while (n) fputc(buf[--n], f);
}

/* ---------- windows and buckets ---------- */
static uint64_t *KW; static double *BW; static int W;     /* window w = cells (KW[w-1], KW[w]]; BW[w] = fl(x~_{KW[w]} (1+s)) */
static uint32_t **bk; static uint64_t *bn, *bc;
static uint64_t Kfin; static double Xlim, Xstore;
static int window_of(double v) {                           /* first w with BW[w] >= v (v <= Xlim) */
    int lo = 0, hi = W - 1;
    while (lo < hi) { int mid = (lo + hi) >> 1; if (BW[mid] >= v) hi = mid; else lo = mid + 1; }
    return lo;
}
static int curw;
static void bpush(int w, uint32_t id) {
    if (w <= curw || w >= W) die("bucket target not in the future");
    if (bn[w] == bc[w]) { bc[w] = bc[w] ? 2 * bc[w] : 64; bk[w] = realloc(bk[w], bc[w] * sizeof(uint32_t)); if (!bk[w]) die("oom bucket"); }
    bk[w][bn[w]++] = id;
}
static uint32_t new_prefix(double v, uint32_t cur, int32_t parent, uint32_t last, int om) {
    if (npre == cappre) { cappre = cappre ? cappre + cappre / 2 : (1u << 20); pre = realloc(pre, cappre * sizeof(Pre)); if (!pre) die("oom pre"); }
    if (npre >= 0xFFFFFFF0u) die("too many prefixes");
    pre[npre].v = v; pre[npre].cur = cur; pre[npre].parent = parent; pre[npre].last = last; pre[npre].om = (uint8_t)om;
    return (uint32_t)npre++;
}

/* ---------- per-window composite lists ---------- */
typedef struct { double c; uint32_t k; uint8_t om, flag; } Ent;
static Ent *cur, *car; static uint64_t ncur, ncar, capcur, capcar;
static void push_ent(Ent **a, uint64_t *n, uint64_t *cap, Ent e) {
    if (*n == *cap) { *cap = *cap ? 2 * *cap : (1u << 16); *a = realloc(*a, *cap * sizeof(Ent)); if (!*a) die("oom ent"); }
    (*a)[(*n)++] = e;
}

/* checkpoints V (integers) with their cells, decided rigorously at start */
#define NCH 64
static double CV[NCH]; static uint64_t CK[NCH]; static int nch;
static int chk_index(uint64_t k) { for (int i = 0; i < nch; i++) if (CK[i] == k) return i; return -1; }
static uint64_t ncomp_emitted, nomax;

static void emit(double c, int om, int64_t pid, uint32_t jq, int w) {
    uint64_t k = cell_of(c, om, pid, jq);
    ncomp_emitted++;
    if (k > Kfin) return;                                   /* beyond X: not a g-integer <= X, and c*q > X */
    if (k <= KW[w - 1]) die("composite in a finished cell");
    Ent e; e.c = c; e.k = (uint32_t)k; e.om = (uint8_t)om; e.flag = 0;
    if ((uint64_t)om > nomax) nomax = om;
    int ci = chk_index(k);
    if (ci >= 0) e.flag = (uint8_t)le_V(c, om, CV[ci], pid, jq, 0, 0);
    if (k <= KW[w]) push_ent(&cur, &ncur, &capcur, e);
    else { if (w + 1 >= W || k > KW[w + 1]) die("carry beyond next window"); push_ent(&car, &ncar, &capcar, e); }
    double q = xt(pk[jq]);
    double nx = c * q;                                      /* first extension c * P^+(c) */
    if (nx <= Xlim) { uint32_t id = new_prefix(c, jq, (int32_t)pid, jq, om); bpush(window_of(nx), id); }
}

/* emission phase of window w: every composite with computed value <= BW[w] (Lemma 2.2: none is missed) */
static void emission(int w) {
    double Bw = BW[w];
    double xnext = xt(KW[w - 1] + 1);                      /* every unknown g-prime is >= x_{K_{w-1}+1} */
    uint64_t nb = bn[w];
    for (uint64_t i = 0; i < nb; i++) {
        uint32_t id = bk[w][i];
        double v = pre[id].v; int om = pre[id].om + 1; uint32_t j = pre[id].cur;
        for (;;) {
            if (j >= npk) {
                double lowb = v * xnext * (1.0 - 1e-12);
                if (lowb <= Xlim) bpush(window_of(lowb), id);
                break;
            }
            double c = v * xt(pk[j]);
            if (c > Bw) { if (c <= Xlim) bpush(window_of(c), id); break; }
            emit(c, om, id, j, w);
            j++;
        }
        pre[id].cur = j;
    }
    free(bk[w]); bk[w] = NULL; bn[w] = bc[w] = 0;
}

/* ---------- cell (Lindley) phase ---------- */
static uint64_t e_q, npi, lastp, maxgapk, maxgap_at, maxe;
static double supE = 0.5, supE_at = 0;
static uint32_t *off; static uint64_t capoff;
static Ent *srt; static uint64_t capsrt;
static void place_prime(uint64_t k) {
    double x = xt(k);
    npi++; mom_add(x, 1);
    if (lastp && k - lastp > maxgapk) { maxgapk = k - lastp; maxgap_at = lastp; }
    lastp = k;
    if (x <= Xstore) {
        if (npk == cappk) { cappk += cappk / 2 + 1024; pk = realloc(pk, cappk * sizeof(uint32_t)); if (!pk) die("oom pk"); }
        if (k > 0xFFFFFFFFull) die("lattice index exceeds 32 bits");
        pk[npk++] = (uint32_t)k;
        if (x * x <= Xlim) { uint32_t id = new_prefix(x, (uint32_t)(npk - 1), -1, (uint32_t)(npk - 1), 1); bpush(window_of(x * x), id); }
    }
}
static void cells(int w) {
    uint64_t K0 = w ? KW[w - 1] : 0, K1 = KW[w], L = K1 - K0;
    if (L + 2 > capoff) { capoff = L + 2; off = realloc(off, capoff * sizeof(uint32_t)); }
    if (ncur > capsrt) { capsrt = ncur; srt = realloc(srt, capsrt * sizeof(Ent)); }
    memset(off, 0, (L + 2) * sizeof(uint32_t));
    for (uint64_t i = 0; i < ncur; i++) off[cur[i].k - K0]++;        /* cell k -> slot k - K0 in 1..L */
    uint64_t acc = 0;
    for (uint64_t s = 0; s <= L + 1; s++) { uint32_t c = off[s]; off[s] = (uint32_t)acc; acc += c; }
    for (uint64_t i = 0; i < ncur; i++) srt[off[cur[i].k - K0]++] = cur[i];
    uint64_t pos = 0;
    for (uint64_t k = K0 + 1; k <= K1; k++) {
        uint64_t beg = pos, end = off[k - K0]; pos = end;
        for (uint64_t a = beg + 1; a < end; a++) {                      /* insertion sort by value (stats only) */
            Ent x = srt[a]; uint64_t b = a;
            while (b > beg && srt[b - 1].c > x.c) { srt[b] = srt[b - 1]; b--; }
            srt[b] = x;
        }
        uint64_t ck = end - beg;
        int ci = chk_index(k); uint64_t nV = 0; double supV = supE;
        double xl = xt(k - 1);
        for (uint64_t a = beg; a < end; a++) {
            mom_add(srt[a].c, srt[a].om);
            double E = (double)e_q + (double)(a - beg + 1) + 0.5 - (srt[a].c - xl) * RHO;
            if (ci >= 0 && srt[a].flag) { nV++; if (E > supV) supV = E; }
            if (E > supE) { supE = E; supE_at = srt[a].c; }
        }
        if (ci >= 0)
            printf("CHK V=%.0f N=%llu pi=%llu supE=%.10f\n", CV[ci], (unsigned long long)(k + e_q + nV),
                   (unsigned long long)npi, supV);
        if (e_q == 0 && ck == 0) place_prime(k);
        else e_q = e_q + ck - 1;
        if (e_q > maxe) maxe = e_q;
    }
}

static void snapshot(const char *outp, const char *name, uint64_t K, double secs) {
    char fn[1024]; snprintf(fn, sizeof fn, "%s_K%llu.mom", outp, (unsigned long long)K);
    FILE *f = fopen(fn, "w"); if (!f) die("cannot write moments");
    fprintf(f, "# s8cert %s K=%llu N=%llu pi=%llu eK=%llu supE=%.10f supE_at=%.6f maxgap_cells=%llu maxgap_at_k=%llu"
               " maxe=%llu omax=%llu decisions=%llu fallbacks=%llu fallbacksV=%llu minrel=%.4e at %.6e prefixes=%llu storedprimes=%llu secs=%.1f\n",
            name, (unsigned long long)K, (unsigned long long)(K + 1 + e_q), (unsigned long long)npi, (unsigned long long)e_q,
            supE, supE_at, (unsigned long long)maxgapk, (unsigned long long)maxgap_at, (unsigned long long)maxe,
            (unsigned long long)nomax, (unsigned long long)ndec, (unsigned long long)nfb, (unsigned long long)nfbV,
            minrel, minrel_at, (unsigned long long)npre, (unsigned long long)npk, secs);
    fprintf(f, "# e i cnt ommax lo1..lo%d hi1..hi%d  (sum z^j 2^62 in [lo_j, hi_j]; block [2^e(1+i/256), 2^e(1+(i+1)/256)))\n", JM, JM);
    for (int e = 0; e < NE; e++) for (int i = 0; i < 256; i++) {
        Blk *b = &blk[e][i]; if (!b->cnt) continue;
        fprintf(f, "%d %d %llu %d", e, i, (unsigned long long)b->cnt, b->ommax);
        for (int j = 1; j <= JM; j++) { fputc(' ', f); print_i128(f, b->lo[j]); }
        for (int j = 1; j <= JM; j++) { fputc(' ', f); print_i128(f, b->hi[j]); }
        fputc('\n', f);
    }
    fclose(f);
    printf("SNAP K=%llu x_K=%.6f N=%llu pi=%llu E(x_K)=%llu.5 supE=%.10f maxgap=%.6f decisions=%llu fallbacks=%llu minrel=%.3e prefixes=%llu secs=%.1f\n",
           (unsigned long long)K, xt(K), (unsigned long long)(K + 1 + e_q), (unsigned long long)npi, (unsigned long long)e_q,
           supE, maxgapk * TT, (unsigned long long)ndec, (unsigned long long)nfb, minrel, (unsigned long long)npre, secs);
    fflush(stdout);
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: s8cert params.txt name Xmax outprefix [Lmax]\n"); return 1; }
    const char *name = argv[2]; double Xmax = atof(argv[3]); const char *outp = argv[4];
    uint64_t Lmax = argc > 5 ? strtoull(argv[5], 0, 10) : (1ull << 21);
    FILE *pf = fopen(argv[1], "r"); if (!pf) die("params");
    char nm[64], ths[64], rhs[64], tl[256], th[256]; int found = 0;
    mpz_inits(TLO, THI, P2, gL, gH, gR, gS, gF, NULL);
    while (fscanf(pf, "%63s %63s %63s %d %255s %255s", nm, ths, rhs, &DD, tl, th) == 6)
        if (!strcmp(nm, name)) { found = 1; break; }
    fclose(pf); if (!found) die("name not in params");
    TT = strtod(ths, 0); RHO = strtod(rhs, 0);
    mpz_set_str(TLO, tl, 10); mpz_set_str(THI, th, 10); mpz_ui_pow_ui(P2, 2, DD + 1);
    if (getenv("S8C_INFLATE")) INFL = atof(getenv("S8C_INFLATE"));
    if (getenv("S8C_CLOSE")) CLOSE_THR = atof(getenv("S8C_CLOSE"));
    clock_t t0 = clock();
    Kfin = (uint64_t)floor((Xmax - 1.0) * RHO + 0.5);
    while (xt(Kfin) > Xmax) Kfin--;
    while (xt(Kfin + 1) <= Xmax) Kfin++;
    Xlim = xt(Kfin) * (1.0 + SL);
    double P1 = xt(1);
    Xstore = Xlim / P1 * (1.0 + 1e-6);
    /* forced boundaries: largest K with x~_K <= 10^d */
    uint64_t FK[32]; int nfk = 0;
    for (int d = 3; d <= 19; d++) {
        double V = pow(10.0, d); uint64_t K = (uint64_t)floor((V - 1.0) * RHO + 0.5);
        while (xt(K) > V) K--; while (xt(K + 1) <= V) K++;
        if (K < Kfin) FK[nfk++] = K;
    }
    FK[nfk++] = Kfin;
    /* window schedule */
    uint64_t capw = 1024; KW = malloc(capw * sizeof(uint64_t)); W = 0;
    KW[W++] = 1;
    while (KW[W - 1] < Kfin) {
        uint64_t K = KW[W - 1], Kn = K + Lmax;
        double lim = P1 * xt(K) / (1.0 + 1e-6);
        uint64_t Kr = (uint64_t)floor((lim - 1.0) * RHO + 0.5);
        while (xt(Kr) > lim) Kr--; while (xt(Kr + 1) <= lim) Kr++;
        if (Kr <= K) die("schedule stalls");
        if (Kr < Kn) Kn = Kr;
        for (int i = 0; i < nfk; i++) if (FK[i] > K && FK[i] < Kn) Kn = FK[i];
        if (Kn > Kfin) Kn = Kfin;
        if (W == (int)capw) { capw *= 2; KW = realloc(KW, capw * sizeof(uint64_t)); }
        KW[W++] = Kn;
    }
    BW = malloc(W * sizeof(double));
    for (int w = 0; w < W; w++) BW[w] = xt(KW[w]) * (1.0 + SL);
    bk = calloc(W, sizeof(uint32_t *)); bn = calloc(W, sizeof(uint64_t)); bc = calloc(W, sizeof(uint64_t));
    cappk = (uint64_t)(1.3 * Xstore / log(Xstore + 3.0)) + 4096; pk = malloc(cappk * sizeof(uint32_t));
    /* checkpoints V = floor(10^(h/2)), h >= 6, V < x_Kfin; cells decided rigorously */
    nch = 0;
    for (int h = 6; h <= 40 && nch < NCH; h++) {
        double V = floor(pow(10.0, h / 2.0)); if (h % 2 == 0) V = pow(10.0, h / 2);
        if (V >= xt(Kfin)) break;
        uint64_t k = (uint64_t)floor((V - 1.0) * RHO + 0.5) + 1;
        for (int it = 0; it < 6; it++) {
            int l = le_V(xt(k - 1), 1, V, -1, 0, 1, k - 1), r = le_V(xt(k), 1, V, -1, 0, 1, k);
            if (l && !r) break;
            if (!l) k--; else k++;
        }
        CV[nch] = V; CK[nch] = k; nch++;
    }
    printf("# s8cert %s t=%.17g rho~=%.17g Xmax=%.6g Kfin=%llu x_Kfin=%.9f windows=%d Lmax=%llu checkpoints=%d\n", name, TT, RHO,
           Xmax, (unsigned long long)Kfin, xt(Kfin), W, (unsigned long long)Lmax, nch);
    fflush(stdout);
    mom_add(1.0, 0);                                     /* the unit */
    int fi = 0;
    for (int w = 0; w < W; w++) {
        curw = w;
        ncur = 0;
        for (uint64_t i = 0; i < ncar; i++) push_ent(&cur, &ncur, &capcur, car[i]);
        ncar = 0;
        if (w > 0) emission(w);
        cells(w);
        while (fi < nfk && FK[fi] < KW[w]) fi++;
        if (fi < nfk && FK[fi] == KW[w]) snapshot(outp, name, KW[w], (double)(clock() - t0) / CLOCKS_PER_SEC);
    }
    printf("FINAL K=%llu N=%llu pi=%llu composites_emitted=%llu prefixes=%llu storedprimes=%llu decisions=%llu fallbacks=%llu fallbacksV=%llu minrel=%.4e at %.6e omax=%llu maxe=%llu secs=%.1f\n",
           (unsigned long long)Kfin, (unsigned long long)(Kfin + 1 + e_q), (unsigned long long)npi, (unsigned long long)ncomp_emitted,
           (unsigned long long)npre, (unsigned long long)npk, (unsigned long long)ndec, (unsigned long long)nfb,
           (unsigned long long)nfbV, minrel, minrel_at, (unsigned long long)nomax, (unsigned long long)maxe,
           (double)(clock() - t0) / CLOCKS_PER_SEC);
    return 0;
}
