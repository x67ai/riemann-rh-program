/* thin2.c — conj-O-s38 task 3. Extends the frontier NOTE's thin.c (copied verbatim as thin_fr.c; same hash, sieve, E1, bins and
 * CSV format: run,bin_lo,bin_hi,maxEplus,minEminus,sumE2,count,psiR) with three modes:
 *   finite  X p1 p2 ... pk          finite deletion R = {p_i}; rho exact; header also carries the exact one-period mean square.
 *   feedback alpha X Y K [c [corr]] NEW structured design: online error-feedback deletion (see NOTE §3.5). Target weights
 *                                   w_p = min(1, c p^(alpha-1)); discrepancy D = #R(<=p) - F(p) kept in |D| <= K p^(alpha/2);
 *                                   inside the band, delete p iff that makes |N(p) - rho_hat p| smaller. Primes in (X, Y] are
 *                                   decided greedily around the frozen offset D(X).
 *   dumpR   bern alpha X seed | greedy alpha X c   write the R-primes <= X (uint64) to $RDUMP, no counting.
 * Env RDUMP=path: also dump R-primes <= X in finite/feedback modes (for rnums.c). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#define BPD 20
static uint64_t splitmix64(uint64_t x) { x += 0x9E3779B97F4A7C15ULL; x = (x ^ (x >> 30)) * 0xBF58476D1CE4E5B9ULL;
    x = (x ^ (x >> 27)) * 0x94D049BB133111EBULL; return x ^ (x >> 31); }
static double unif(uint64_t p, uint64_t seed, uint64_t salt) {
    uint64_t h = splitmix64(p ^ splitmix64(seed * 0xD1B54A32D192ED03ULL ^ salt)); return (double)(h >> 11) * (1.0 / 9007199254740992.0); }
static uint8_t *pbits; static uint64_t PLIM;
static int isprime(uint64_t n) { if (n < 2) return 0; if (n == 2) return 1; if (!(n & 1)) return 0;
    uint64_t i = n >> 1; return (pbits[i >> 3] >> (i & 7)) & 1; }
static void sieve(uint64_t lim) { PLIM = lim; uint64_t nb = (lim >> 1) + 1; pbits = (uint8_t *)malloc((nb >> 3) + 1);
    if (!pbits) { fprintf(stderr, "alloc fail\n"); exit(1); } memset(pbits, 0xFF, (nb >> 3) + 1); pbits[0] &= ~1;
    for (uint64_t i = 1; ; i++) { uint64_t p = 2 * i + 1; if (p * p > lim) break; if (!((pbits[i >> 3] >> (i & 7)) & 1)) continue;
        for (uint64_t j = (p * p) >> 1; j < nb; j += p) pbits[j >> 3] &= ~(1u << (j & 7)); } }
static double E1(double z) { if (z < 1.0) { double s = 0, t = 1; for (int k = 1; k < 200; k++) { t *= -z / k; s += -t / k;
        if (fabs(t / k) < 1e-18) break; } return -0.57721566490153286061 - log(z) + s; }
    double b = z + 1, c = 1e300, d = 1 / b, h = d; for (int i = 1; i < 500; i++) { double a = -(double)i * i; b += 2;
        d = 1 / (a * d + b); c = b + a / c; double del = c * d; h *= del; if (fabs(del - 1) < 1e-16) break; } return h * exp(-z); }
static uint8_t *rfree;
static void emit_bins(const char *run, uint64_t X, double rho) {   /* identical statistics to thin.c (psiR column = 0) */
    int K = (int)floor(BPD * log10((double)X)) + 1; uint64_t *lo = malloc(sizeof(uint64_t) * (K + 1));
    for (int k = 0; k <= K; k++) { double v = pow(10.0, (double)k / BPD); lo[k] = (uint64_t)ceil(v - 1e-9); }
    uint64_t N = 0; int k = 0; double mx = -1e300, mn = 1e300, s2 = 0; uint64_t cnt = 0;
    for (uint64_t n = 1; n <= X; n++) { if ((rfree[n >> 3] >> (n & 7)) & 1) N++;
        while (k < K && n >= lo[k + 1]) { if (cnt) printf("%s,%llu,%llu,%.6f,%.6f,%.6e,%llu,0\n", run, (unsigned long long)lo[k],
                (unsigned long long)(lo[k + 1] - 1), mx, mn, s2, (unsigned long long)cnt);
            k++; mx = -1e300; mn = 1e300; s2 = 0; cnt = 0; }
        double ep = (double)N - rho * (double)n, em = ep - rho, ec = ep - 0.5 * rho;
        if (ep > mx) mx = ep; if (em < mn) mn = em; s2 += ec * ec; cnt++; }
    if (cnt) printf("%s,%llu,%llu,%.6f,%.6f,%.6e,%llu,0\n", run, (unsigned long long)lo[k], (unsigned long long)X, mx, mn, s2,
        (unsigned long long)cnt);
    free(lo); }
static FILE *rdump_open(void) { const char *p = getenv("RDUMP"); return p ? fopen(p, "wb") : NULL; }
static void clear_multiples(uint64_t p, uint64_t X) { for (uint64_t m = p; m <= X; m += p) rfree[m >> 3] &= ~(1u << (m & 7)); }
static void kahan_add(double *s, double *c, double y0) { double y = y0 - *c; double t = *s + y; *c = (t - *s) - y; *s = t; }
static int mode_finite(int argc, char **argv) {
    uint64_t X = (uint64_t)atof(argv[2]); int k = argc - 3; uint64_t Q = 1; long double rho = 1; char run[160] = "finite";
    rfree = malloc((X >> 3) + 1); memset(rfree, 0xFF, (X >> 3) + 1); FILE *fd = rdump_open();
    for (int i = 0; i < k; i++) { uint64_t p = strtoull(argv[3 + i], 0, 10); Q *= p; rho *= (1.0L - 1.0L / p); clear_multiples(p, X);
        if (fd) fwrite(&p, 8, 1, fd); snprintf(run + strlen(run), sizeof run - strlen(run), "_%llu", (unsigned long long)p); }
    if (fd) fclose(fd);
    long double ms = -1;                    /* exact (1/Q) int_0^Q E^2: on [n, n+1), int = (N(n) - rho(n+1/2))^2 + rho^2/12 */
    if (Q <= X) { long double s = 0; uint64_t N = 0;
        for (uint64_t n = 0; n < Q; n++) { if (n >= 1 && ((rfree[n >> 3] >> (n & 7)) & 1)) N++;
            long double ec = (long double)N - rho * ((long double)n + 0.5L); s += ec * ec + rho * rho / 12.0L; } ms = s / Q; }
    printf("# run=%s X=%llu Q=%llu rho=%.15Lf period_ms=%.15Lf pred_rho_2k_over_12=%.15Lf\n", run, (unsigned long long)X,
        (unsigned long long)Q, rho, ms, rho * powl(2.0L, k) / 12.0L);
    emit_bins(run, X, (double)rho); return 0; }
static int mode_feedback(int argc, char **argv) {
    double alpha = atof(argv[2]); uint64_t X = (uint64_t)atof(argv[3]), Y = (uint64_t)atof(argv[4]); double Kb = atof(argv[5]);
    double cm = argc > 6 ? atof(argv[6]) : 1.0; if (Y < X) Y = X; sieve(Y);
    int corr = (argc > 7 && !strcmp(argv[7], "corr"));   /* corr: minimise |e - rho_hat*D| (future-discrepancy correction, §3.5) */
    rfree = malloc((X >> 3) + 1); memset(rfree, 0xFF, (X >> 3) + 1);
    double u0 = log(2.0), du = 1e-4; int G = (int)((log((double)Y) - u0) / du) + 3;     /* tail(u) = -c E1((1-alpha)u), u = ln p */
    double *tab = malloc(sizeof(double) * (G + 1)); for (int i = 0; i <= G; i++) tab[i] = -cm * E1((1.0 - alpha) * (u0 + i * du));
    FILE *fd = rdump_open(); double logrho = 0, lc = 0, F = 0, maxD = 0; uint64_t nR = 0, nRX = 0, N = 0, nforced = 0;
    for (uint64_t n = 1; n <= X; n++) {
        if (isprime(n)) { double p = (double)n, lp = log(p); double w = cm * exp((alpha - 1.0) * lp); if (w > 1.0) w = 1.0;
            double D = (double)nR - F, B = Kb * exp(0.5 * alpha * lp); int d;
            if (D - w < -B) { d = 1; nforced++; } else if (D + 1.0 - w > B) { d = 0; nforced++; }
            else { double x = (lp - u0) / du; int i = (int)x; double fr = x - i, tl = tab[i] * (1 - fr) + tab[i + 1] * fr;
                double rk = exp(logrho + tl), ek = (double)(N + 1) - rk * p, ed = (double)N - rk * p + rk;
                if (corr) { ek -= rk * (D - w); ed -= rk * (D + 1.0 - w); }   /* E = e - rho*D if the future D returns to 0 (§3.5) */ d = (fabs(ed) < fabs(ek)); }
            if (d) { nR++; nRX++; kahan_add(&logrho, &lc, log1p(-1.0 / p)); clear_multiples(n, X); if (fd) fwrite(&n, 8, 1, fd); }
            F += w; double r = fabs((double)nR - F) / exp(0.5 * alpha * lp); if (r > maxD && n > 1000) maxD = r; }
        if ((rfree[n >> 3] >> (n & 7)) & 1) N++; }
    if (fd) fclose(fd);
    double DX = (double)nR - F;                                   /* primes in (X, Y]: greedy around the frozen offset D(X) */
    for (uint64_t q = X + 1; q <= Y; q++) { if (!isprime(q)) continue; double w = cm * exp((alpha - 1.0) * log((double)q)); if (w > 1.0) w = 1.0;
        int d = ((double)nR - F < DX); F += w; if (d) { nR++; kahan_add(&logrho, &lc, log1p(-1.0 / (double)q)); } }
    double tail = -cm * E1((1.0 - alpha) * log((double)Y)), rho = exp(logrho + tail); char run[96];
    snprintf(run, sizeof run, "feedback_a%.3f_K%g_c%g%s", alpha, Kb, cm, corr ? "_corr" : "");
    printf("# run=%s alpha=%.4f X=%llu Y=%llu K=%g c=%g nR(Y)=%llu nR(X)=%llu D(X)=%.3f max|D|/p^(a/2)=%.3f forced=%llu logrho_Y=%.12f "
        "tail=%.12f rho=%.12f\n", run, alpha, (unsigned long long)X, (unsigned long long)Y, Kb, cm, (unsigned long long)nR,
        (unsigned long long)nRX, DX, maxD, (unsigned long long)nforced, logrho, tail, rho);
    fflush(stdout); emit_bins(run, X, rho); return 0; }
static int mode_dump(int argc, char **argv) {           /* dumpR bern alpha X seed | dumpR greedy alpha X c  (same rules as thin.c) */
    int bern = !strcmp(argv[2], "bern"); double alpha = atof(argv[3]); uint64_t X = (uint64_t)atof(argv[4]);
    double cm = bern ? 1.0 : (argc > 5 ? atof(argv[5]) : 1.0); uint64_t seed = bern ? (uint64_t)atoll(argv[5]) : 0;
    uint64_t salt = (uint64_t)llround(alpha * 1e6); FILE *fd = rdump_open(); if (!fd) { fprintf(stderr, "set RDUMP\n"); return 1; }
    sieve(X); double F = 0; uint64_t nR = 0;
    for (uint64_t p = 2; p <= X; p++) { if (!isprime(p)) continue; double w = cm * exp((alpha - 1.0) * log((double)p)); if (w > 1.0) w = 1.0;
        int d; if (!bern) { F += w; d = ((double)nR < F); } else d = (unif(p, seed, salt) < w); if (d) { nR++; fwrite(&p, 8, 1, fd); } }
    fclose(fd); fprintf(stderr, "dumped %llu R-primes <= %llu\n", (unsigned long long)nR, (unsigned long long)X); return 0; }
int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: see header\n"); return 1; }
    if (!strcmp(argv[1], "finite")) return mode_finite(argc, argv);
    if (!strcmp(argv[1], "feedback") && argc >= 6) return mode_feedback(argc, argv);
    if (!strcmp(argv[1], "dumpR") && argc >= 6) return mode_dump(argc, argv);
    fprintf(stderr, "unknown mode\n"); return 1; }
