/* s8gen.c -- production generator for S8(rho, theta) (free greedy system) and the rational-prime control.
   Positions in DOUBLE-DOUBLE (~106 bits): IEEE double's product rounding (~1e-7 absolute at 1e9) exceeds the
   smallest gap between distinct g-integers (~1e-9 at 1e9), so double cannot certify the event order; on arm64
   'long double' is plain double.  g-prime k sits at 1 + (k - 1 + theta) t, t = 1/rho (t given in dd).
   Composites m = P(m) * n.  If P(m) <= B = sqrt(X): small-prime cursor of P(m) walks the stored list S
   (g-integers n with n*P(n) <= X and P(n) <= B -- the only ones any cursor ever reads).  If P(m) > B: then
   n < sqrt(X), and the multiplier cursor of n walks the list of large g-primes (stored as k-deltas, ~1 byte each).
   Usage: s8gen MODE X THETA RHO_HI RHO_LO T_HI T_LO PREFIX [resume]     MODE = rule | sieve            */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#include <time.h>

typedef struct { double hi, lo; } dd;
static inline dd qts(double a, double b) { double s = a + b; dd r = { s, b - (s - a) }; return r; }
static inline dd tws(double a, double b) { double s = a + b, bb = s - a; dd r = { s, (a - (s - bb)) + (b - bb) }; return r; }
static inline dd ddmul(dd a, dd b) { double p = a.hi * b.hi, e = fma(a.hi, b.hi, -p); e += a.hi * b.lo + a.lo * b.hi; return qts(p, e); }
static inline dd ddmuld(dd a, double b) { double p = a.hi * b, e = fma(a.hi, b, -p); e += a.lo * b; return qts(p, e); }
static inline dd ddadd(dd a, dd b) { dd s = tws(a.hi, b.hi); s.lo += a.lo + b.lo; return qts(s.hi, s.lo); }
static inline dd ddsub(dd a, dd b) { dd nb = { -b.hi, -b.lo }; return ddadd(a, nb); }
static inline int ddlt(dd a, dd b) { return a.hi < b.hi || (a.hi == b.hi && a.lo < b.lo); }
static inline double ddv(dd a) { return a.hi + a.lo; }

#define NSAMP 64          /* half-decade samples */
#define HCELLS 8192       /* E histogram: cells of width 1/16 on [-1, 511) */
#define HMIN (-1.0)
#define HW (1.0 / 16.0)
#define MW 1e-4           /* block width in log n */
#define NMOM 7
#define RING 1024

typedef struct {          /* all scalar state (checkpointed as one block) */
    double X, theta; dd rho, t, Xdd, B; int sieve;
    int64_t N, C, nS, nP, nL, nM, nLD, npark, hn, pn, Kbase, Klast, nb;
    dd xprev; double Eprev, Lnext;                  /* last event (or split point), E just after it */
    double supE, supPsi, psi, psic;                 /* psi with Neumaier compensation psic */
    dd Vsup; int64_t skviol; double minEbefore;
    /* window statistics (reset at each half-decade sample) */
    double wInt, wLen, wMaxGap, wGapStart, wGapPeak, wMinGapAbs, wMinGapRel, wMinMargin, wMinEb;
    int64_t wMaxClu, wTies, wMisord, wAmbig; double wMaxE;
    dd lastPrime; double gapPeak;                   /* running peak of E since the last g-prime */
    int64_t ringH, ringT;
    int nsamp, iSamp, iProto, iFine, iSnap, nsnap; double sampX[NSAMP], snapX[32];
    double fineNext, protoNext, protoStep;
    int64_t lastRecLevel; int64_t sieveNext;        /* sieve: next candidate integer */
    double wall0, cpu_used;
} state;
static state G;
static const char *PREFIX;

/* stored list S */
static dd *Sv; static int32_t *Sl, *Sp; static int64_t capS;
/* small primes */
static dd *Pv; static int64_t *Pk, *Pc; static int64_t capP;
/* large primes: k-deltas, 1 byte (<255) or 255 + 4 bytes */
static uint8_t *LD; static int64_t capLD;
/* multiplier cursors */
typedef struct { dd n; int64_t off, k; } mcur;
static mcur *M; static int64_t capM;
static int64_t *park; static int64_t capPark;
/* heaps */
typedef struct { dd key; int64_t id; } hent;          /* id >= 0: small prime; id < 0: multiplier cursor ~id */
static int64_t capH;
typedef struct { dd pw; int64_t i; double lq; } pent;
static pent *PH; static int64_t capPH;
/* E histogram (difference arrays, cumulative from x = 1), moments, ring buffer, sieve bits */
static double *HC, *MOM; static int64_t *HS; static int64_t capMOM;   /* HS: integer counts (exact prefix sums) */
static double ring[RING];
static uint8_t *SB;
static FILE *DUMPF = 0;                             /* optional: every g-integer (dd) to $S8_DUMP, for validation */

static void *xrealloc(void *p, size_t n) { void *q = realloc(p, n); if (!q) { fprintf(stderr, "out of memory (%zu)\n", n); exit(2); } return q; }
#define GROW(arr, cap, need, type) do { if ((need) > (cap)) { int64_t nc = (cap) ? (cap) : 1024; while (nc < (need)) nc *= 2; \
    arr = (type *)xrealloc(arr, (size_t)nc * sizeof(type)); cap = nc; } } while (0)

/* 4-ary min-heap, structure of arrays (Hhi, Hlo, Hid), fixed capacity, children groups 32-byte aligned.
   Order: (hi, lo) lexicographic, i.e. the exact dd order; equal dd keys (possible only for rational rho) in any order. */
static double *Hhi, *Hlo; static int64_t *Hid;
static void heap_alloc(int64_t cap) {
    void *a, *b, *c;
    if (posix_memalign(&a, 64, (cap + 8) * 8) || posix_memalign(&b, 64, (cap + 8) * 8) || posix_memalign(&c, 64, (cap + 8) * 8)) { fprintf(stderr, "heap alloc\n"); exit(2); }
    Hhi = (double *)a + 3; Hlo = (double *)b + 3; Hid = (int64_t *)c + 3; capH = cap;
}
static inline int kless(double ah, double al, double bh, double bl) { return (ah < bh) | ((ah == bh) & (al < bl)); }
static void hsift_down(int64_t k, hent e) {
    int64_t n = G.hn; double eh = e.key.hi, el = e.key.lo;
    for (;;) {
        int64_t c = 4 * k + 1;
        if (c + 3 < n) {
            int64_t m = c; double mh = Hhi[c], ml = Hlo[c];
            for (int j = 1; j < 4; j++) { double h = Hhi[c + j], l = Hlo[c + j]; int lt = kless(h, l, mh, ml);
                m = lt ? c + j : m; mh = lt ? h : mh; ml = lt ? l : ml; }
            if (!kless(mh, ml, eh, el)) break;
            Hhi[k] = mh; Hlo[k] = ml; Hid[k] = Hid[m]; k = m;
        } else {
            if (c >= n) break;
            int64_t m = c;
            for (int64_t j = c + 1; j < n; j++) if (kless(Hhi[j], Hlo[j], Hhi[m], Hlo[m])) m = j;
            if (!kless(Hhi[m], Hlo[m], eh, el)) break;
            Hhi[k] = Hhi[m]; Hlo[k] = Hlo[m]; Hid[k] = Hid[m]; k = m;
        }
    }
    Hhi[k] = eh; Hlo[k] = el; Hid[k] = e.id;
}
static void hpush(hent e) {
    if (G.hn + 1 > capH) { fprintf(stderr, "heap capacity %lld exceeded\n", (long long)capH); exit(2); }
    int64_t k = G.hn++;
    while (k > 0) { int64_t p = (k - 1) / 4; if (!kless(e.key.hi, e.key.lo, Hhi[p], Hlo[p])) break;
        Hhi[k] = Hhi[p]; Hlo[k] = Hlo[p]; Hid[k] = Hid[p]; k = p; }
    Hhi[k] = e.key.hi; Hlo[k] = e.key.lo; Hid[k] = e.id;
}
static void hreplace_top(hent e) { hsift_down(0, e); }
static void hpop_top(void) { G.hn--; if (G.hn > 0) { hent e = { { Hhi[G.hn], Hlo[G.hn] }, Hid[G.hn] }; hsift_down(0, e); } }
static inline int pless(const pent *a, const pent *b) { return ddlt(a->pw, b->pw) || (a->pw.hi == b->pw.hi && a->pw.lo == b->pw.lo && a->i < b->i); }
static void ppush(pent e) {
    GROW(PH, capPH, G.pn + 1, pent);
    int64_t k = G.pn++;
    while (k > 0) { int64_t p = (k - 1) / 2; if (!pless(&e, &PH[p])) break; PH[k] = PH[p]; k = p; }
    PH[k] = e;
}
static void ppop(void) {
    pent last = PH[--G.pn]; int64_t k = 0, n = G.pn;
    for (;;) { int64_t c = 2 * k + 1; if (c >= n) break; if (c + 1 < n && pless(&PH[c + 1], &PH[c])) c++;
               if (!pless(&PH[c], &last)) break; PH[k] = PH[c]; k = c; }
    if (n > 0) PH[k] = last;
}

/* ---------- primes, stored list, cursors ---------- */
static inline dd prime_value(int64_t k) { dd one = { 1.0, 0.0 }; return ddadd(one, ddmuld(G.t, (double)(k - 1) + G.theta)); }
static void S_append(dd v, int32_t l, int32_t par) {
    if (G.nS + 1 > capS) { int64_t nc = capS ? 2 * capS : 1 << 16;
        Sv = xrealloc(Sv, nc * sizeof(dd)); Sl = xrealloc(Sl, nc * 4); Sp = xrealloc(Sp, nc * 4); capS = nc; }
    Sv[G.nS] = v; Sl[G.nS] = l; Sp[G.nS] = par; G.nS++;
}
static int next_small(int64_t i, dd *out) {        /* next composite q_i * n, n in S, lpf(n) <= i */
    int64_t c = Pc[i] + 1;
    while (c < G.nS && Sl[c] > i) c++;
    if (c >= G.nS) return 0;
    Pc[i] = c;
    dd v = ddmul(Pv[i], Sv[c]);
    if (ddlt(G.Xdd, v)) return 0;
    *out = v; return 1;
}
static inline int64_t ld_read(int64_t *off) {
    uint8_t b = LD[*off];
    if (b < 255) { (*off)++; return b; }
    uint32_t v; memcpy(&v, LD + *off + 1, 4); *off += 5; return v;
}
static void ld_append(int64_t dk) {
    GROW(LD, capLD, G.nLD + 8, uint8_t);
    if (dk < 0 || dk > 4000000000LL) { fprintf(stderr, "bad k-delta %lld\n", (long long)dk); exit(3); }
    if (dk < 255) LD[G.nLD++] = (uint8_t)dk;
    else { LD[G.nLD] = 255; uint32_t v = (uint32_t)dk; memcpy(LD + G.nLD + 1, &v, 4); G.nLD += 5; }
}
static int next_mult(int64_t j, dd *out) {         /* 1 = value, 0 = exhausted, -1 = next large prime not yet known */
    mcur *c = &M[j];
    if (c->off >= G.nLD) return -1;
    c->k += ld_read(&c->off);
    dd v = ddmul(c->n, prime_value(c->k));
    if (ddlt(G.Xdd, v)) return 0;
    *out = v; return 1;
}
static void mult_step(int64_t j) {                 /* push the next product of cursor j, or park it */
    dd v; int r = next_mult(j, &v);
    if (r == 1) { hent e = { v, ~j }; hpush(e); }
    else if (r == -1) { GROW(park, capPark, G.npark + 1, int64_t); park[G.npark++] = j; }
}
static void init_mult(void) {                      /* at the first large g-prime: one cursor per g-integer n < X/B */
    for (int64_t s = 1; s < G.nS; s++) {
        if (ddv(Sv[s]) * G.B.hi > G.X) break;
        GROW(M, capM, G.nM + 1, mcur);
        int64_t j = G.nM++;
        M[j].n = Sv[s]; M[j].off = 0; M[j].k = G.Kbase;
        mult_step(j);
    }
}
static void new_prime(int64_t k, dd x) {
    if (ddv(x) <= G.B.hi) {
        if (G.nP + 1 > capP) { int64_t nc = capP ? 2 * capP : 1 << 14;
            Pv = xrealloc(Pv, nc * sizeof(dd)); Pk = xrealloc(Pk, nc * 8); Pc = xrealloc(Pc, nc * 8); capP = nc; }
        int64_t i = G.nP++;
        Pv[i] = x; Pk[i] = k; Pc[i] = 0;
        dd x2 = ddmul(x, x);
        if (!ddlt(G.Xdd, x2)) {
            S_append(x, (int32_t)i, 0);
            pent p = { x2, i, log(x.hi) + x.lo / x.hi }; ppush(p);
        }
        dd v; if (next_small(i, &v)) { hent e = { v, i }; hpush(e); }
    } else {
        if (G.nL > 0 && ddv(x) * Pv[0].hi > G.X) { G.nL++; G.npark = 0; return; }   /* q0 * q > X: never read */
        if (G.nL == 0) { G.Kbase = k; G.Klast = k; }
        ld_append(k - G.Klast); G.Klast = k; G.nL++;
        if (G.nL == 1) init_mult();
        else if (G.npark > 0) {
            int64_t np = G.npark; G.npark = 0;
            int64_t *tmp = malloc(np * sizeof(int64_t)); memcpy(tmp, park, np * sizeof(int64_t));
            for (int64_t a = 0; a < np; a++) mult_step(tmp[a]);
            free(tmp);
        }
    }
}

/* ---------- statistics ---------- */
static dd XLAST;                                    /* last event position (not checkpoint-critical: copied into G) */
static int64_t MAXCLU_TOT = 0;
static inline void psi_add(double v) {
    double s = G.psi + v;
    if (fabs(G.psi) >= fabs(v)) G.psic += (G.psi - s) + v; else G.psic += (v - s) + G.psi;
    G.psi = s;
}
static void hist_seg(double lo, double hi) {        /* E runs linearly over [lo, hi]: time density 1/rho per unit E */
    if (!(hi > lo)) return;
    double r = 1.0 / G.rho.hi;
    double fa = (lo - HMIN) / HW, fb = (hi - HMIN) / HW;
    if (fa < 0) fa = 0;
    if (fb > HCELLS - 1e-6) fb = HCELLS - 1e-6;
    if (fa > fb) fa = fb;
    int64_t ja = (int64_t)fa, jb = (int64_t)fb;
    if (ja == jb) { HC[ja] += (fb - fa) * HW * r; return; }
    HC[ja] += ((double)(ja + 1) - fa) * HW * r;
    HS[ja + 1] += 1; HS[jb] -= 1;
    HC[jb] += (fb - (double)jb) * HW * r;
}
static inline double E_at(dd x, int64_t N) {        /* N - T(x), T(x) = rho (x - 1) + 1 */
    dd one = { 1.0, 0.0 }; dd rt = ddmul(G.rho, ddsub(x, one));
    return ((double)(N - 1) - rt.hi) - rt.lo;
}
static void mom_add(dd x) {
    double L = log(x.hi) + x.lo / x.hi;
    int64_t b = (int64_t)(L / MW);
    if (b + 1 > G.nb) {
        int64_t need = (b + 1) * NMOM;
        if (need > capMOM) { int64_t nc = capMOM ? capMOM : 1 << 16; while (nc < need) nc *= 2;
            MOM = xrealloc(MOM, nc * sizeof(double)); memset(MOM + capMOM, 0, (nc - capMOM) * sizeof(double)); capMOM = nc; }
        G.nb = b + 1;
    }
    double dl = L - ((double)b + 0.5) * MW, p = 1.0, *m = MOM + NMOM * b;
    for (int j = 0; j < NMOM; j++) { m[j] += p; p *= dl; }
}
static void flush_powers(dd x) {                    /* add log q for every prime power q^k <= x not yet added */
    while (G.pn > 0 && !ddlt(x, PH[0].pw)) {
        pent p = PH[0]; psi_add(p.lq); ppop();
        dd nx = ddmul(p.pw, Pv[p.i]);
        if (!ddlt(G.Xdd, nx)) { pent q = { nx, p.i, p.lq }; ppush(q); }
    }
}
static void window_reset(void) {
    G.wInt = 0; G.wLen = 0; G.wMaxGap = 0; G.wGapStart = 0; G.wGapPeak = 0; G.wMinGapAbs = 1e300; G.wMinGapRel = 1e300;
    G.wMinMargin = 1e300; G.wMinEb = 1e300; G.wMaxClu = 0; G.wTies = 0; G.wMisord = 0; G.wAmbig = 0; G.wMaxE = -1e300;
}
static double wall(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static void split_at(double xs) {                   /* close the running E segment at xs */
    dd xd = { xs, 0.0 };
    double Es = E_at(xd, G.N), len = ddv(ddsub(xd, G.xprev));
    if (len > 0) { hist_seg(Es, G.Eprev); G.wInt += 0.5 * (G.Eprev + Es) * len; G.wLen += len; }
    G.xprev = xd; G.Eprev = Es;
}
static void emit_sample(double xs) {
    split_at(xs); dd xd = { xs, 0.0 }; flush_powers(xd);
    int64_t pi = G.nP + G.nL;
    double psimx = (G.psi - xs) + G.psic;
    printf("S %.9e %lld %lld %lld %.6f %.6f %.6f %.6f %.6f %.6e %.6f %lld %.6e %.6e %lld %lld %.6e %lld %lld %.3f %.3f %lld %lld %lld %lld %.1f %.6f\n",
        xs, (long long)G.N, (long long)pi, (long long)G.C, G.supE, G.Eprev, G.wLen > 0 ? G.wInt / G.wLen : 0.0, G.wMinEb,
        G.wMaxGap, G.wGapStart, G.wGapPeak, (long long)G.wMaxClu, G.wMinGapAbs, G.wMinGapRel, (long long)G.wTies,
        (long long)G.wMisord, G.wMinMargin, (long long)G.wAmbig, (long long)G.skviol, G.supPsi, psimx,
        (long long)G.nS, (long long)G.nM, (long long)G.nLD, (long long)G.hn, wall() - G.wall0 + G.cpu_used, G.wMaxE);
    char fn[1024]; snprintf(fn, sizeof fn, "%s.hist", PREFIX);
    FILE *f = fopen(fn, "ab");
    if (f) { double *mass = malloc(HCELLS * sizeof(double)), cw = HW / G.rho.hi; int64_t run = 0;
        for (int j = 0; j < HCELLS; j++) { run += HS[j]; mass[j] = HC[j] + (double)run * cw; }
        fwrite(&xs, sizeof(double), 1, f); fwrite(mass, sizeof(double), HCELLS, f); fclose(f); free(mass); }
    fflush(stdout);
    window_reset();
}
static void emit_fine(double xs) {
    dd xd = { xs, 0.0 }; flush_powers(xd);
    printf("F %.9e %lld %lld %.6f %.4f %.6f %.3f\n", xs, (long long)G.N, (long long)(G.nP + G.nL), E_at(xd, G.N),
        (G.psi - xs) + G.psic, G.supE, G.supPsi);
}
static void emit_snap(double xs) {
    dd xd = { xs, 0.0 };
    char fn[1024]; snprintf(fn, sizeof fn, "%s.mom.%.6e", PREFIX, xs);
    FILE *f = fopen(fn, "wb"); if (!f) { perror(fn); return; }
    double hdr[8] = { MW, (double)G.nb, xs, (double)G.N, E_at(xd, G.N), G.rho.hi, G.rho.lo, (double)NMOM };
    fwrite(hdr, sizeof(double), 8, f); fwrite(MOM, sizeof(double), G.nb * NMOM, f); fclose(f);
    printf("M %.9e %lld %.6f %s\n", xs, (long long)G.N, E_at(xd, G.N), fn);
}

/* ---------- checkpoint ---------- */
#define WR(p, n, sz) do { if ((n) > 0 && fwrite(p, sz, n, f) != (size_t)(n)) { perror("ckpt write"); exit(4); } } while (0)
#define RD(p, n, sz) do { if ((n) > 0 && fread(p, sz, n, f) != (size_t)(n)) { perror("ckpt read"); exit(4); } } while (0)
static void ckpt_save(void) {
    char fn[1024], tmp[1100]; snprintf(fn, sizeof fn, "%s.ckpt", PREFIX); snprintf(tmp, sizeof tmp, "%s.tmp", fn);
    FILE *f = fopen(tmp, "wb"); if (!f) { perror(tmp); return; }
    double used = G.cpu_used; G.cpu_used = wall() - G.wall0 + used;
    WR(&G, 1, sizeof G); WR(&XLAST, 1, sizeof XLAST); WR(&MAXCLU_TOT, 1, 8);
    WR(Sv, G.nS, sizeof(dd)); WR(Sl, G.nS, 4); WR(Sp, G.nS, 4);
    WR(Pv, G.nP, sizeof(dd)); WR(Pk, G.nP, 8); WR(Pc, G.nP, 8);
    WR(LD, G.nLD, 1); WR(M, G.nM, sizeof(mcur)); WR(park, G.npark, 8);
    WR(Hhi, G.hn, 8); WR(Hlo, G.hn, 8); WR(Hid, G.hn, 8); WR(PH, G.pn, sizeof(pent));
    WR(HC, HCELLS, 8); WR(HS, HCELLS, 8); WR(MOM, G.nb * NMOM, 8); WR(ring, RING, 8);
    fclose(f); rename(tmp, fn); G.cpu_used = used;
    fprintf(stderr, "checkpoint written at N = %lld, x = %.6e\n", (long long)G.N, XLAST.hi);
}
static void ckpt_load(void) {
    char fn[1024]; snprintf(fn, sizeof fn, "%s.ckpt", PREFIX);
    FILE *f = fopen(fn, "rb"); if (!f) { perror(fn); exit(4); }
    RD(&G, 1, sizeof G); RD(&XLAST, 1, sizeof XLAST); RD(&MAXCLU_TOT, 1, 8);
    capS = G.nS + 1024; Sv = xrealloc(0, capS * sizeof(dd)); Sl = xrealloc(0, capS * 4); Sp = xrealloc(0, capS * 4);
    RD(Sv, G.nS, sizeof(dd)); RD(Sl, G.nS, 4); RD(Sp, G.nS, 4);
    capP = G.nP + 1024; Pv = xrealloc(0, capP * sizeof(dd)); Pk = xrealloc(0, capP * 8); Pc = xrealloc(0, capP * 8);
    RD(Pv, G.nP, sizeof(dd)); RD(Pk, G.nP, 8); RD(Pc, G.nP, 8);
    capLD = G.nLD + 4096; LD = xrealloc(0, capLD); RD(LD, G.nLD, 1);
    capM = G.nM + 16; M = xrealloc(0, capM * sizeof(mcur)); RD(M, G.nM, sizeof(mcur));
    capPark = G.npark + 16; park = xrealloc(0, capPark * 8); RD(park, G.npark, 8);
    heap_alloc((int64_t)(4.0 * sqrt(G.X)) + 65536); RD(Hhi, G.hn, 8); RD(Hlo, G.hn, 8); RD(Hid, G.hn, 8);
    capPH = G.pn + 16; PH = xrealloc(0, capPH * sizeof(pent)); RD(PH, G.pn, sizeof(pent));
    RD(HC, HCELLS, 8); RD(HS, HCELLS, 8);
    capMOM = G.nb * NMOM + (1 << 16); MOM = xrealloc(0, capMOM * 8); memset(MOM, 0, capMOM * 8); RD(MOM, G.nb * NMOM, 8);
    RD(ring, RING, 8); fclose(f);
    G.wall0 = wall();
    fprintf(stderr, "resumed at N = %lld, x = %.6e\n", (long long)G.N, XLAST.hi);
}

/* ---------- one event ---------- */
static void bookkeeping(dd x, int comp) {
    dd one = { 1.0, 0.0 };
    double Ea = E_at(x, G.N), Eb = Ea - 1.0;
    if (Eb < G.wMinEb) G.wMinEb = Eb;
    if (Eb < G.minEbefore) G.minEbefore = Eb;
    double len = ddv(ddsub(x, G.xprev));
    if (len > 0) { hist_seg(Eb, G.Eprev); G.wInt += 0.5 * (G.Eprev + Eb) * len; G.wLen += len; }
    dd gap = ddsub(x, XLAST); double gr = ddv(gap) / x.hi;
    if (gap.hi < 0) G.wMisord++;
    if (fabs(gr) < 1e-28) G.wTies++;
    if (ddv(gap) < G.wMinGapAbs) G.wMinGapAbs = ddv(gap);
    if (gr < G.wMinGapRel) G.wMinGapRel = gr;
    if (Ea > G.wMaxE) G.wMaxE = Ea;
    if (comp) { if (Ea > G.supE) G.supE = Ea; if (Ea > G.gapPeak) G.gapPeak = Ea; }
    else {
        double gl = ddv(ddsub(x, G.lastPrime));
        if (gl > G.wMaxGap) { G.wMaxGap = gl; G.wGapStart = ddv(G.lastPrime); G.wGapPeak = G.gapPeak; }
        G.lastPrime = x; G.gapPeak = Ea;
    }
    if (!G.sieve) {                                 /* Skorokhod route: pi_P = max(0, floor(sup V + 1 - theta)) */
        dd rt = ddmul(G.rho, ddsub(x, one));
        dd Vb = ddsub(rt, (dd){ (double)(G.C - (comp ? 1 : 0)), 0.0 });
        if (ddlt(G.Vsup, Vb)) G.Vsup = Vb;
        double pi = (double)(G.nP + G.nL), vs = ddv(G.Vsup);
        if (vs < pi - 1.0 + G.theta - 1e-9 || vs > pi + G.theta + 1e-9) G.skviol++;
    }
    ring[G.ringT % RING] = x.hi; G.ringT++;
    while (ring[G.ringH % RING] < x.hi - 1.0) G.ringH++;
    int64_t clu = G.ringT - G.ringH;
    if (clu > G.wMaxClu) G.wMaxClu = clu;
    if (clu > MAXCLU_TOT) MAXCLU_TOT = clu;
    if (!comp) psi_add(log(x.hi) + x.lo / x.hi);
    flush_powers(x);
    double d = fabs((G.psi - x.hi) + (G.psic - x.lo)); if (d > G.supPsi) G.supPsi = d;
    mom_add(x);
    if (DUMPF) fwrite(&x, sizeof(dd), 1, DUMPF);
    if ((int64_t)floor(Ea) > G.lastRecLevel) { G.lastRecLevel = (int64_t)floor(Ea);
        printf("R %.9e %.6f %lld %lld %.6e\n", ddv(x), Ea, (long long)G.N, (long long)(G.nP + G.nL), ddv(G.lastPrime)); }
    if (x.hi >= G.protoNext) {
        printf("P %10.3g %lld %lld %.2f %.1f %lld %.1f\n", G.protoNext, (long long)G.N, (long long)(G.nP + G.nL), G.supE, G.supPsi,
               (long long)MAXCLU_TOT, (G.psi - x.hi) + (G.psic - x.lo));
        G.protoNext *= G.protoStep;
    }
    XLAST = x; G.xprev = x; G.Eprev = Ea;
}

/* ---------- main ---------- */
static int64_t sieve_next(int64_t from, int64_t lim) {   /* smallest prime >= from, or -1 if > lim */
    for (int64_t n = from; n <= lim; n++) if (n >= 2 && !SB[n]) return n;
    return -1;
}
int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage: s8gen rule|sieve X THETA RHO_HI RHO_LO T_HI T_LO PREFIX [resume]\n"); return 1; }
    PREFIX = argv[8];
    int resume = argc > 9 && !strcmp(argv[9], "resume");
    HC = calloc(HCELLS, sizeof(double)); HS = calloc(HCELLS, sizeof(int64_t));
    if (!resume) heap_alloc((int64_t)(4.0 * sqrt(strtod(argv[2], 0))) + 65536);
    double X = strtod(argv[2], 0);
    if (resume) ckpt_load();
    else {
        memset(&G, 0, sizeof G);
        G.sieve = !strcmp(argv[1], "sieve"); G.X = X; G.theta = strtod(argv[3], 0);
        G.rho.hi = strtod(argv[4], 0); G.rho.lo = strtod(argv[5], 0); G.t.hi = strtod(argv[6], 0); G.t.lo = strtod(argv[7], 0);
        G.Xdd.hi = X; G.Xdd.lo = 0; G.B.hi = sqrt(X) * (1.0 + 1e-12); G.B.lo = 0;
        G.N = 1; G.xprev.hi = 1.0; G.Eprev = 0.0; G.lastPrime.hi = 1.0; G.gapPeak = 0.0; G.minEbefore = 1e300;
        G.Vsup.hi = 0.0; G.lastRecLevel = 0; G.sieveNext = 2;
        XLAST.hi = 1.0; XLAST.lo = 0.0;
        S_append((dd){ 1.0, 0.0 }, -1, -1);
        mom_add((dd){ 1.0, 0.0 });
        for (int j = 2; ; j++) { double s = pow(10.0, j / 2.0); if (s > X * (1 + 1e-15)) break; G.sampX[G.nsamp++] = s; }
        if (G.nsamp == 0 || fabs(G.sampX[G.nsamp - 1] - X) > 1e-9 * X) G.sampX[G.nsamp++] = X;
        for (int j = 6; ; j++) { double s = pow(10.0, j); if (s >= X / 2 * (1 - 1e-15)) break; G.snapX[G.nsnap++] = s; }
        G.snapX[G.nsnap++] = X / 4; G.snapX[G.nsnap++] = X / 2; G.snapX[G.nsnap++] = X;
        for (int a = 1; a < G.nsnap; a++) for (int b = a; b > 0 && G.snapX[b] < G.snapX[b - 1]; b--) { double t = G.snapX[b]; G.snapX[b] = G.snapX[b - 1]; G.snapX[b - 1] = t; }
        G.fineNext = 10.0; G.protoNext = 10.0; G.protoStep = pow(10.0, 0.5); G.iFine = 100;
        window_reset();
        printf("# s8gen mode=%s X=%.6e theta=%.6f rho=%.17g%+.6e t=%.17g%+.6e B=%.6f\n", argv[1], X, G.theta, G.rho.hi, G.rho.lo, G.t.hi, G.t.lo, G.B.hi);
        printf("# S cols: x N pi C supE E(x) meanE_win minEbefore_win maxPrimeGap_win gapStart gapPeakE maxClu_win minGapAbs minGapRel ties misorders minDecisionMargin_rel ambig_double skorokhodViol supPsi psi-x nS nM nLDbytes heap time wMaxE\n");
    }
    G.wall0 = wall();
    if (getenv("S8_DUMP")) { DUMPF = fopen(getenv("S8_DUMP"), "wb"); dd u = { 1.0, 0.0 }; if (DUMPF && !resume) fwrite(&u, sizeof(dd), 1, DUMPF); }
    if (G.sieve) {                                   /* rational primes, byte sieve */
        SB = calloc((size_t)X + 2, 1);
        for (int64_t p = 2; p * p <= (int64_t)X; p++) if (!SB[p]) for (int64_t q = p * p; q <= (int64_t)X; q += p) SB[q] = 1;
    }
    double lastck = wall();
    dd one = { 1.0, 0.0 }; (void)one;
    for (;;) {
        int haveC = G.hn > 0;
        dd xc = haveC ? (dd){ Hhi[0], Hlo[0] } : (dd){ INFINITY, 0.0 };
        int64_t kp; dd xp;
        if (!G.sieve) { kp = G.N; xp = prime_value(kp); }
        else { static int64_t cachedP = -2, cachedFrom = -2; if (cachedFrom != G.sieveNext) { cachedP = sieve_next(G.sieveNext, (int64_t)X); cachedFrom = G.sieveNext; } kp = cachedP; if (kp < 0) { xp.hi = INFINITY; xp.lo = 0; } else { xp.hi = (double)kp; xp.lo = 0; } }
        if (!G.sieve && haveC) {
            double m = fabs(ddv(ddsub(xc, xp))) / xp.hi;
            if (m < G.wMinMargin) G.wMinMargin = m;
            if (m < 1e-14) G.wAmbig++;
        }
        int comp = haveC && !ddlt(xp, xc);
        dd x = comp ? xc : xp;
        if (ddlt(G.Xdd, x)) break;
        while (G.iSamp < G.nsamp && (G.sampX[G.iSamp] < x.hi || (G.sampX[G.iSamp] == x.hi && x.lo > 0))) emit_sample(G.sampX[G.iSamp++]);
        while (G.fineNext < x.hi) { emit_fine(G.fineNext); G.iFine++; G.fineNext = pow(10.0, G.iFine / 100.0); }
        while (G.iSnap < G.nsnap && G.snapX[G.iSnap] < x.hi) emit_snap(G.snapX[G.iSnap++]);
        G.N++;
        if (comp) {
            hent top = { { Hhi[0], Hlo[0] }, Hid[0] }; G.C++;
            if (top.id >= 0) {
                int64_t i = top.id;
                if (!ddlt(G.Xdd, ddmul(x, Pv[i]))) S_append(x, (int32_t)i, (int32_t)Pc[i]);
                dd v; if (next_small(i, &v)) { hent e = { v, i }; hreplace_top(e); } else hpop_top();
            } else {
                int64_t j = ~top.id; dd v; int r = next_mult(j, &v);
                if (r == 1) { hent e = { v, top.id }; hreplace_top(e); }
                else { hpop_top(); if (r == -1) { GROW(park, capPark, G.npark + 1, int64_t); park[G.npark++] = j; } }
            }
        } else {
            new_prime(kp, x);
            if (G.sieve) G.sieveNext = kp + 1;
        }
        bookkeeping(x, comp);
        if ((G.N & 0xFFFFFF) == 0 && !G.sieve && wall() - lastck > 900.0) { fflush(stdout); ckpt_save(); lastck = wall(); }
    }
    while (G.iSamp < G.nsamp && G.sampX[G.iSamp] <= X) emit_sample(G.sampX[G.iSamp++]);
    while (G.fineNext <= X) { emit_fine(G.fineNext); G.iFine++; G.fineNext = pow(10.0, G.iFine / 100.0); }
    while (G.iSnap < G.nsnap && G.snapX[G.iSnap] <= X) emit_snap(G.snapX[G.iSnap++]);
    printf("# done N=%lld pi=%lld C=%lld supE=%.9f minEbefore=%.9f skviol=%lld supPsi=%.3f nS=%lld nP_small=%lld nL=%lld nM=%lld LDbytes=%lld time=%.1f\n",
        (long long)G.N, (long long)(G.nP + G.nL), (long long)G.C, G.supE, G.minEbefore, (long long)G.skviol, G.supPsi,
        (long long)G.nS, (long long)G.nP, (long long)G.nL, (long long)G.nM, (long long)G.nLD, wall() - G.wall0 + G.cpu_used);
    return 0;
}
