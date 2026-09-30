/* thin_aux.c — controls for seed M1b beurling-frontier.
 *   cramer X Y seed zeta_unused : Cramer-type random Beurling system: 2 is prime, n >= 3 is prime w.p. 1/log n (hash of n, seed);
 *        Beurling integers counted WITH multiplicity: c[n] = #multisets of P-primes with product n (DP), N(x) = sum c[n].
 *        rho from log rho = 1/2 - gamma - log log 3 + D + A + G2 (see NOTE sec. 6), A and G2 summed to Y (>= X).
 *   mean alpha X zeta2ma : deterministic mean system f(n) = prod_{p|n}(1 - p^(alpha-1)), density rho_w = 1/zeta(2-alpha)
 *        (zeta2ma = zeta(2-alpha) passed in, computed with mpmath). Counting function S(x) = sum_{n<=x} f(n).
 * Output format identical to thin.c: run,bin_lo,bin_hi,maxEplus,minEminus,sumE2,count,0
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#define BPD 20


static uint64_t splitmix64(uint64_t x) {
    x += 0x9E3779B97F4A7C15ULL;
    x = (x ^ (x >> 30)) * 0xBF58476D1CE4E5B9ULL;
    x = (x ^ (x >> 27)) * 0x94D049BB133111EBULL;
    return x ^ (x >> 31);
}
static double unif(uint64_t p, uint64_t seed, uint64_t salt) {
    uint64_t h = splitmix64(p ^ splitmix64(seed * 0xD1B54A32D192ED03ULL ^ salt));
    return (double)(h >> 11) * (1.0 / 9007199254740992.0);
}

/* odd-only prime bitset: bit i <-> number 2i+1 is prime */
static uint8_t *pbits; static uint64_t PLIM;
static int isprime(uint64_t n) {
    if (n < 2) return 0; if (n == 2) return 1; if (!(n & 1)) return 0;
    uint64_t i = n >> 1; return (pbits[i >> 3] >> (i & 7)) & 1;
}
static void sieve(uint64_t lim) {
    PLIM = lim; uint64_t nb = (lim >> 1) + 1;
    pbits = (uint8_t *)malloc((nb >> 3) + 1);
    if (!pbits) { fprintf(stderr, "alloc fail\n"); exit(1); }
    memset(pbits, 0xFF, (nb >> 3) + 1);
    pbits[0] &= ~1; /* 1 is not prime */
    for (uint64_t i = 1; ; i++) {
        uint64_t p = 2 * i + 1; if (p * p > lim) break;
        if (!((pbits[i >> 3] >> (i & 7)) & 1)) continue;
        for (uint64_t j = (p * p) >> 1; j < nb; j += p) pbits[j >> 3] &= ~(1u << (j & 7));
    }
}

/* E1(z) for z > 0 */
static double E1(double z) {
    if (z < 1.0) { /* series */
        double s = 0, t = 1; for (int k = 1; k < 200; k++) { t *= -z / k; s += -t / k; if (fabs(t / k) < 1e-18) break; }
        return -0.57721566490153286061 - log(z) + s;
    }
    /* continued fraction (Lentz) */
    double b = z + 1, c = 1e300, d = 1 / b, h = d;
    for (int i = 1; i < 500; i++) { double a = -(double)i * i; b += 2; d = 1 / (a * d + b); c = b + a / c; double del = c * d; h *= del; if (fabs(del - 1) < 1e-16) break; }
    return h * exp(-z);
}


static void emit_steps(const char *run, uint64_t X, double rho, const double *jump) {
    int K = (int)floor(BPD * log10((double)X)) + 1;
    uint64_t *lo = malloc(sizeof(uint64_t) * (K + 1));
    for (int k = 0; k <= K; k++) { double v = pow(10.0, (double)k / BPD); lo[k] = (uint64_t)ceil(v - 1e-9); }
    double S = 0, Sc = 0; int k = 0; double mx = -1e300, mn = 1e300, s2 = 0; uint64_t cnt = 0;
    for (uint64_t n = 1; n <= X; n++) {
        double y = jump[n] - Sc, t = S + y; Sc = (t - S) - y; S = t; /* Kahan */
        while (k < K && n >= lo[k + 1]) {
            if (cnt) printf("%s,%llu,%llu,%.6f,%.6f,%.6e,%llu,0\n", run, (unsigned long long)lo[k], (unsigned long long)(lo[k+1]-1), mx, mn, s2, (unsigned long long)cnt);
            k++; mx = -1e300; mn = 1e300; s2 = 0; cnt = 0;
        }
        double ep = S - rho * (double)n, em = ep - rho, ec = ep - 0.5 * rho;
        if (ep > mx) mx = ep; if (em < mn) mn = em; s2 += ec * ec; cnt++;
    }
    if (cnt) printf("%s,%llu,%llu,%.6f,%.6f,%.6e,%llu,0\n", run, (unsigned long long)lo[k], (unsigned long long)X, mx, mn, s2, (unsigned long long)cnt);
    free(lo);
}

static void emit_int(const char *run, uint64_t X, double rho, const uint32_t *c) {
    int K = (int)floor(BPD * log10((double)X)) + 1;
    uint64_t *lo = malloc(sizeof(uint64_t) * (K + 1));
    for (int k = 0; k <= K; k++) { double v = pow(10.0, (double)k / BPD); lo[k] = (uint64_t)ceil(v - 1e-9); }
    uint64_t N = 0; int k = 0; double mx = -1e300, mn = 1e300, s2 = 0; uint64_t cnt = 0;
    for (uint64_t n = 1; n <= X; n++) {
        N += c[n];
        while (k < K && n >= lo[k + 1]) {
            if (cnt) printf("%s,%llu,%llu,%.6f,%.6f,%.6e,%llu,0\n", run, (unsigned long long)lo[k], (unsigned long long)(lo[k+1]-1), mx, mn, s2, (unsigned long long)cnt);
            k++; mx = -1e300; mn = 1e300; s2 = 0; cnt = 0;
        }
        double ep = (double)N - rho * (double)n, em = ep - rho, ec = ep - 0.5 * rho;
        if (ep > mx) mx = ep; if (em < mn) mn = em; s2 += ec * ec; cnt++;
    }
    if (cnt) printf("%s,%llu,%llu,%.6f,%.6f,%.6e,%llu,0\n", run, (unsigned long long)lo[k], (unsigned long long)X, mx, mn, s2, (unsigned long long)cnt);
    free(lo);
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: see header\n"); return 1; }
    if (!strcmp(argv[1], "mean")) {
        double alpha = atof(argv[2]); uint64_t X = (uint64_t)atof(argv[3]); double z2 = atof(argv[4]);
        sieve(X);
        double *f = malloc(sizeof(double) * (X + 1));
        if (!f) { fprintf(stderr, "alloc\n"); return 1; }
        for (uint64_t n = 0; n <= X; n++) f[n] = 1.0;
        for (uint64_t p = 2; p <= X; p++) if (isprime(p)) { double g = 1.0 - exp((alpha - 1.0) * log((double)p)); for (uint64_t m = p; m <= X; m += p) f[m] *= g; }
        double rho = 1.0 / z2; char run[64]; snprintf(run, sizeof run, "mean_a%.3f", alpha);
        printf("# run=%s alpha=%.4f X=%llu rho_w=1/zeta(2-alpha)=%.15f\n", run, alpha, (unsigned long long)X, rho);
        emit_steps(run, X, rho, f); return 0;
    }
    if (!strcmp(argv[1], "cramer")) {
        uint64_t X = (uint64_t)atof(argv[2]), Y = (uint64_t)atof(argv[3]), seed = (uint64_t)atoll(argv[4]);
        if (Y < X) Y = X;
        const uint64_t salt = 0xC7A3E5ULL;
        uint32_t *c = calloc(X + 1, sizeof(uint32_t)); if (!c) { fprintf(stderr, "alloc\n"); return 1; }
        c[1] = 1;
        double A = 0, Ac = 0, G2 = 0; uint64_t np = 0;
        for (uint64_t n = 2; n <= Y; n++) {
            double ln = log((double)n);
            int isp = (n == 2) ? 1 : (unif(n, seed, salt) < 1.0 / ln);
            if (n >= 3) { double y = ((isp ? 1.0 : 0.0) - 1.0 / ln) / (double)n - Ac, t = A + y; Ac = (t - A) - y; A = t; }
            if (!isp) continue;
            np++; G2 += -log1p(-1.0 / (double)n) - 1.0 / (double)n;
            if (n <= X) for (uint64_t m = n; m <= X; m += n) c[m] += c[m / n];
        }
        /* D = lim [sum_{3<=n<=M} 1/(n log n) - (log log M - log log 3)] ; Euler-Maclaurin tail correction -f(M)/2 */
        uint64_t M = 100000000ULL; double D = 0, Dc = 0;
        for (uint64_t n = 3; n <= M; n++) { double y = 1.0 / ((double)n * log((double)n)) - Dc, t = D + y; Dc = (t - D) - y; D = t; }
        D -= (log(log((double)M)) - log(log(3.0))); D -= 0.5 / ((double)M * log((double)M));
        double logrho = 0.5 - 0.57721566490153286061 - log(log(3.0)) + D + A + G2, rho = exp(logrho);
        char run[64]; snprintf(run, sizeof run, "cramer_s%llu", (unsigned long long)seed);
        printf("# run=%s X=%llu Y=%llu nprimes(Y)=%llu A=%.12f D=%.12f G2=%.12f rho=%.12f\n", run, (unsigned long long)X,
               (unsigned long long)Y, (unsigned long long)np, A, D, G2, rho);
        emit_int(run, X, rho, c); return 0;
    }
    return 1;
}
