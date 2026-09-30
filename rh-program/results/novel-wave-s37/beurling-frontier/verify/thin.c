/* thin.c — exact integer counting for sparse surgery on the rational primes (seed M1b beurling-frontier).
 *
 * Modes (argv[1]):
 *   bern   alpha X Y seed1 [seed2 ...]  Bernoulli thinning T_alpha: delete prime p w.p. p^(alpha-1), p <= Y.
 *   greedy alpha X Y [c]                deterministic low-discrepancy deletion: delete p iff #R(<p) < F(p), F(x)=sum_{p<=x} w_p,
 *                                       w_p = min(1, c p^(alpha-1)) (c = 1 default; c = 2 cancels the leading prime-square branch point).
 *   none   X                            control: no deletion (rational integers), rho = 1.
 * For each run: N_P(n) = #{m <= n : m has no prime factor in R}, exact, n = 1..X.
 * rho = prod_{p in R, p<=Y}(1-1/p) * exp(-E1((1-alpha) log Y))  (mean tail beyond Y; E1 = exponential integral).
 * Output (stdout, CSV): per log-spaced bin (BPD bins per decade) of integers n:
 *   run,bin_lo,bin_hi,maxEplus,minEminus,sumE2,count,psiR_ratio_at_hi
 * where Eplus(n) = N_P(n) - rho*n, Eminus(n) = N_P(n) - rho*(n+1) (the extremes of N_P(x) - rho*x on [n, n+1)),
 * sumE2 = sum over the bin of (N_P(n) - rho*(n+0.5))^2, psiR_ratio = sum_{p in R, p<=hi} log p / (hi^alpha/alpha).
 * Header lines start with '#'. Deterministic: the decision for prime p under seed s is a hash of (p, s, alpha).
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

/* run one deletion set given by flag array del (bitset over odd+2 numbers <= X), rho; emit bins */
static uint8_t *rfree; /* bitset: bit n set <-> n is R-free, n <= X */

static void emit_bins(const char *run, uint64_t X, double rho, double alpha, const double *psiR_at) {
    /* bins: [10^(k/BPD), 10^((k+1)/BPD)) over integers */
    int K = (int)floor(BPD * log10((double)X)) + 1;
    uint64_t *lo = malloc(sizeof(uint64_t) * (K + 1));
    for (int k = 0; k <= K; k++) { double v = pow(10.0, (double)k / BPD); lo[k] = (uint64_t)ceil(v - 1e-9); }
    uint64_t N = 0; int k = 0;
    double mx = -1e300, mn = 1e300, s2 = 0; uint64_t cnt = 0;
    for (uint64_t n = 1; n <= X; n++) {
        if ((rfree[n >> 3] >> (n & 7)) & 1) N++;
        while (k < K && n >= lo[k + 1]) {
            if (cnt) printf("%s,%llu,%llu,%.6f,%.6f,%.6e,%llu,%.8f\n", run, (unsigned long long)lo[k], (unsigned long long)(lo[k + 1] - 1), mx, mn, s2, (unsigned long long)cnt, psiR_at ? psiR_at[k] : 0.0);
            k++; mx = -1e300; mn = 1e300; s2 = 0; cnt = 0;
        }
        double ep = (double)N - rho * (double)n, em = ep - rho, ec = ep - 0.5 * rho;
        if (ep > mx) mx = ep; if (em < mn) mn = em; s2 += ec * ec; cnt++;
    }
    if (cnt) printf("%s,%llu,%llu,%.6f,%.6f,%.6e,%llu,%.8f\n", run, (unsigned long long)lo[k], (unsigned long long)X, mx, mn, s2, (unsigned long long)cnt, psiR_at ? psiR_at[k] : 0.0);
    free(lo);
}

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: see header\n"); return 1; }
    const char *mode = argv[1];
    if (!strcmp(mode, "none")) {
        uint64_t X = (uint64_t)atof(argv[2]);
        rfree = malloc((X >> 3) + 1); memset(rfree, 0xFF, (X >> 3) + 1);
        printf("# mode=none X=%llu rho=1\n", (unsigned long long)X);
        emit_bins("none", X, 1.0, 0.0, NULL);
        return 0;
    }
    double alpha = atof(argv[2]);
    uint64_t X = (uint64_t)atof(argv[3]), Y = (uint64_t)atof(argv[4]);
    if (Y < X) Y = X;
    sieve(Y);
    int K = (int)floor(BPD * log10((double)X)) + 1;
    double *psiR_at = calloc(K + 2, sizeof(double));
    uint64_t salt = (uint64_t)llround(alpha * 1e6);
    int nseeds = (!strcmp(mode, "greedy")) ? 1 : argc - 5;
    double cmult = (!strcmp(mode, "greedy") && argc > 5) ? atof(argv[5]) : 1.0;
    rfree = malloc((X >> 3) + 1);
    for (int si = 0; si < nseeds; si++) {
        uint64_t seed = (!strcmp(mode, "greedy")) ? 0 : (uint64_t)atoll(argv[5 + si]);
        memset(rfree, 0xFF, (X >> 3) + 1);
        double logrho = 0, logrho_c = 0, F = 0, psiR = 0; uint64_t nR = 0, nRX = 0;
        int k = 0; double nextb = pow(10.0, 1.0 / BPD);
        for (uint64_t p = 2; p <= Y; p++) {
            if (!isprime(p)) continue;
            double w = cmult * exp((alpha - 1.0) * log((double)p)); if (w > 1.0) w = 1.0;
            int d;
            if (!strcmp(mode, "greedy")) { F += w; d = ((double)nR < F); }
            else d = (unif(p, seed, salt) < w);
            if (p <= X) { /* psi_R bookkeeping at bin ends */
                while (k < K && (double)p >= nextb) { psiR_at[k] = psiR; k++; nextb = pow(10.0, (double)(k + 1) / BPD); }
            }
            if (!d) continue;
            nR++;
            double y = log1p(-1.0 / (double)p) - logrho_c; double t = logrho + y; logrho_c = (t - logrho) - y; logrho = t; /* Kahan */
            if (p <= X) {
                nRX++; psiR += log((double)p);
                for (uint64_t m = p; m <= X; m += p) rfree[m >> 3] &= ~(1u << (m & 7));
            }
        }
        while (k <= K) { psiR_at[k] = psiR; k++; }
        for (int j = 0; j <= K; j++) { double hi = pow(10.0, (double)(j + 1) / BPD); if (hi > X) hi = X; psiR_at[j] /= pow(hi, alpha) / alpha; }
        double tail = -cmult * E1((1.0 - alpha) * log((double)Y));
        double rho = exp(logrho + tail);
        char run[64]; if (cmult != 1.0) snprintf(run, sizeof run, "%s_a%.3f_s%llu_c%g", mode, alpha, (unsigned long long)seed, cmult);
        else snprintf(run, sizeof run, "%s_a%.3f_s%llu", mode, alpha, (unsigned long long)seed);
        printf("# run=%s alpha=%.4f X=%llu Y=%llu nR(Y)=%llu nR(X)=%llu logrho_Y=%.12f tail=%.12f rho=%.12f\n", run, alpha,
               (unsigned long long)X, (unsigned long long)Y, (unsigned long long)nR, (unsigned long long)nRX, logrho, tail, rho);
        fflush(stdout);
        emit_bins(run, X, rho, alpha, psiR_at);
        fflush(stdout);
    }
    return 0;
}
