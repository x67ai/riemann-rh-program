/* lg_core.h — lemmaG-s39 counting core. Bins and CSV format identical to cO/verify/thin2.c (run,bin_lo,bin_hi,maxEplus,
 * minEminus,sumE2,count,psiR) so that the exact dyadic statistic (sumE2 + count*rho^2/12 per bin) applies unchanged.
 * New here: 64-bit Miller-Rabin (deterministic bases), nextprime, the W-histogram of squarefree R-numbers (DFS), long-double rho. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#define BPD 20
typedef unsigned __int128 u128;
static uint64_t mulmod(uint64_t a, uint64_t b, uint64_t m) { return (uint64_t)((u128)a * b % m); }
static uint64_t powmod(uint64_t a, uint64_t e, uint64_t m) { uint64_t r = 1; a %= m; while (e) { if (e & 1) r = mulmod(r, a, m);
    a = mulmod(a, a, m); e >>= 1; } return r; }
static int mr_isprime(uint64_t n) {            /* deterministic for n < 2^64 (bases of Jim Sinclair) */
    if (n < 2) return 0; static const uint64_t sp[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (int i = 0; i < 12; i++) { if (n == sp[i]) return 1; if (n % sp[i] == 0) return 0; }
    uint64_t d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
    static const uint64_t B[] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022};
    for (int i = 0; i < 7; i++) { uint64_t a = B[i] % n; if (a == 0) continue; uint64_t x = powmod(a, d, n);
        if (x == 1 || x == n - 1) continue; int ok = 0; for (int r = 1; r < s; r++) { x = mulmod(x, x, n); if (x == n - 1) { ok = 1; break; } }
        if (!ok) return 0; } return 1; }
static uint64_t nextprime(uint64_t n) { uint64_t m = n + 1; while (!mr_isprime(m)) m++; return m; }   /* least prime > n */
/* odd-only prime bitset up to lim */
static uint8_t *pbits; static uint64_t PLIM;
static int isprime_s(uint64_t n) { if (n < 2) return 0; if (n == 2) return 1; if (!(n & 1)) return 0; uint64_t i = n >> 1;
    return (pbits[i >> 3] >> (i & 7)) & 1; }
static void sieve(uint64_t lim) { PLIM = lim; uint64_t nb = (lim >> 1) + 1; pbits = (uint8_t *)malloc((nb >> 3) + 1);
    if (!pbits) { fprintf(stderr, "alloc fail\n"); exit(1); } memset(pbits, 0xFF, (nb >> 3) + 1); pbits[0] &= ~1;
    for (uint64_t i = 1; ; i++) { uint64_t p = 2 * i + 1; if (p * p > lim) break; if (!((pbits[i >> 3] >> (i & 7)) & 1)) continue;
        for (uint64_t j = (p * p) >> 1; j < nb; j += p) pbits[j >> 3] &= ~(1u << (j & 7)); } }
static double E1(double z) { if (z < 1.0) { double s = 0, t = 1; for (int k = 1; k < 200; k++) { t *= -z / k; s += -t / k;
        if (fabs(t / k) < 1e-18) break; } return -0.57721566490153286061 - log(z) + s; }
    double b = z + 1, c = 1e300, d = 1 / b, h = d; for (int i = 1; i < 500; i++) { double a = -(double)i * i; b += 2;
        d = 1 / (a * d + b); c = b + a / c; double del = c * d; h *= del; if (fabs(del - 1) < 1e-16) break; } return h * exp(-z); }
/* R-prime list */
static uint64_t *Rp; static size_t nR = 0, capR = 0;
static void addR(uint64_t p) { if (nR == capR) { capR = capR ? 2 * capR : 1024; Rp = realloc(Rp, capR * sizeof(uint64_t)); } Rp[nR++] = p; }
static int cmpu(const void *a, const void *b) { uint64_t x = *(const uint64_t *)a, y = *(const uint64_t *)b; return x < y ? -1 : x > y; }
static uint8_t *rfree;
static void build_rfree(uint64_t X) { rfree = malloc((X >> 3) + 1); if (!rfree) { fprintf(stderr, "alloc rfree\n"); exit(1); }
    memset(rfree, 0xFF, (X >> 3) + 1);
    for (size_t i = 0; i < nR; i++) { uint64_t p = Rp[i]; if (p > X) continue; for (uint64_t m = p; m <= X; m += p) rfree[m >> 3] &= ~(1u << (m & 7)); } }
static void emit_bins(const char *run, uint64_t X, double rho) {   /* thin2.c emit_bins statistics unchanged; + optional LG_SUME side file */
    int K = (int)floor(BPD * log10((double)X)) + 1; uint64_t *lo = malloc(sizeof(uint64_t) * (K + 1));
    for (int k = 0; k <= K; k++) { double v = pow(10.0, (double)k / BPD); lo[k] = (uint64_t)ceil(v - 1e-9); }
    uint64_t N = 0; int k = 0; double mx = -1e300, mn = 1e300, s2 = 0, s1 = 0; uint64_t cnt = 0;
    const char *sp = getenv("LG_SUME"); FILE *fs = sp ? fopen(sp, "w") : NULL;   /* optional side file: lo,hi,sum of E at midpoints */
    for (uint64_t n = 1; n <= X; n++) { if ((rfree[n >> 3] >> (n & 7)) & 1) N++;
        while (k < K && n >= lo[k + 1]) { if (cnt) printf("%s,%llu,%llu,%.6f,%.6f,%.6e,%llu,0\n", run, (unsigned long long)lo[k],
                (unsigned long long)(lo[k + 1] - 1), mx, mn, s2, (unsigned long long)cnt);
            if (cnt && fs) fprintf(fs, "%llu,%llu,%.10e\n", (unsigned long long)lo[k], (unsigned long long)(lo[k + 1] - 1), s1);
            k++; mx = -1e300; mn = 1e300; s2 = 0; s1 = 0; cnt = 0; }
        double ep = (double)N - rho * (double)n, em = ep - rho, ec = ep - 0.5 * rho;
        if (ep > mx) mx = ep; if (em < mn) mn = em; s2 += ec * ec; s1 += ec; cnt++; }
    if (fs) fclose(fs);
    if (cnt) printf("%s,%llu,%llu,%.6f,%.6f,%.6e,%llu,0\n", run, (unsigned long long)lo[k], (unsigned long long)X, mx, mn, s2,
        (unsigned long long)cnt);
    free(lo); }
/* W-histogram: Q_R(X) = #{squarefree R-numbers <= X} (1 included) and W(X) = sum_{b<=X} prod_{p|b}(p+1)/(p-1); the truncated
 * Franel diagonal is M_diag(X) = rho^2 W(X)/12 (cO §3.1). Rows: rn,<run>,<bin_hi>,<Q cumulative>,<W cumulative>. */
static uint64_t *blo; static int BK; static double *hW; static uint64_t *hQ; static uint64_t DX;
static int binof(uint64_t b) { int lo = 0, hi = BK; while (hi - lo > 1) { int m = (lo + hi) / 2; if (blo[m] <= b) lo = m; else hi = m; } return lo; }
static void dfs(size_t i, uint64_t b, double w) { int k = binof(b); hQ[k]++; hW[k] += w;
    for (size_t j = i; j < nR; j++) { uint64_t p = Rp[j]; if (p > DX / b) break; dfs(j + 1, b * p, w * (double)(p + 1) / (double)(p - 1)); } }
static void emit_rn(const char *run, uint64_t X) {
    BK = (int)floor(BPD * log10((double)X)) + 1; blo = malloc(sizeof(uint64_t) * (BK + 2));
    for (int k = 0; k <= BK; k++) { double v = pow(10.0, (double)k / BPD); blo[k] = (uint64_t)ceil(v - 1e-9); } blo[BK + 1] = UINT64_MAX;
    hW = calloc(BK + 2, sizeof(double)); hQ = calloc(BK + 2, sizeof(uint64_t)); DX = X;
    qsort(Rp, nR, sizeof(uint64_t), cmpu); dfs(0, 1, 1.0);
    double W = 0; uint64_t Q = 0;
    for (int k = 0; k < BK; k++) { W += hW[k]; Q += hQ[k]; uint64_t hi = blo[k + 1] - 1; if (hi > X) hi = X;
        fprintf(stderr, "rn,%s,%llu,%llu,%.10e\n", run, (unsigned long long)hi, (unsigned long long)Q, W); } }
static void dumpR(const char *path, uint64_t X) { FILE *f = fopen(path, "w"); if (!f) return; for (size_t i = 0; i < nR; i++) if (Rp[i] <= X)
        fprintf(f, "%llu\n", (unsigned long long)Rp[i]); fclose(f); }
static long double zeta_int(int k) { long double s = 0; for (long n = 200000; n >= 1; n--) s += powl((long double)n, -(long double)k);
    long double N = 200000.0L; return s + powl(N, 1 - k) / (k - 1) - 0.5L * powl(N, -k) ; }   /* Euler-Maclaurin tail */
static uint64_t necklace_num(int a, int N) {   /* M(a,N) = (1/N) sum_{d|N} mu(N/d) a^d, N <= 40 */
    long double s = 0; for (int d = 1; d <= N; d++) if (N % d == 0) { int m = N / d, mu = 1, mm = m;
        for (int p = 2; p * p <= mm; p++) if (mm % p == 0) { mm /= p; if (mm % p == 0) { mu = 0; break; } mu = -mu; }
        if (mu && mm > 1) mu = -mu; s += mu * powl((long double)a, d); }
    return (uint64_t)llroundl(s / N); }
