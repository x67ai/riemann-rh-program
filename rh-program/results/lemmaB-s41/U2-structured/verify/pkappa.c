/* P_kappa(rho, r0): the power-dilated integer-supported greedy (multiplicity regime of NOTE §2, Cor. 2.3 (M)).
 * Norm points n^kappa (n >= 1). g-primes sit at norm points with multiplicity b(n) >= 0; a(n) = number of g-integers
 * (formal products, with multiplicity) at n^kappa; N_P(u) = sum_{n^kappa <= u} a(n).
 * Target: N_D(n) := sum_{m<=n} a(m) >= T(n) := ceil(rho (n+1)^kappa + r0)   (this is exactly (A): N_P(u) >= rho u + r0).
 * Greedy: c(n) = a(n) before g-primes at n are added (contributions of b(d), d<n);
 *         b(n) = max(0, T(n) - N_D(n-1) - c(n));  overshoot E_D(n) = N_D(n) - T(n) >= 0.
 * Then sup_{[n^k,(n+1)^k)} (N_P(u) - rho u) <= T(n) - rho n^kappa + E_D(n) ~ rho kappa n^(kappa-1) + r0 + E_D(n).
 * Output per dyadic range of n: max E_D/n^(kappa-1) ("queue in jump units"), argmax and its omega, fraction of busy points
 * (E_D > 0), share of g-primes placed at composite n, max c(n)/jump.  Exact integer arithmetic (__int128 accumulators).
 * Build: cc -O2 -o pkappa pkappa.c -lm      Run: ./pkappa kappa rho r0 Y
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

typedef __int128 i128;

static int omega_of(long n, const int *spf) { int w = 0; long last = 0; while (n > 1) { int p = spf[n]; if (p != last) { w++; last = p; } n /= p; } return w; }

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: %s kappa rho r0 Y\n", argv[0]); return 1; }
    double kappa = atof(argv[1]), rho = atof(argv[2]), r0 = atof(argv[3]);
    long Y = atol(argv[4]);
    int64_t *A = calloc(Y + 1, sizeof(int64_t));
    int *spf = calloc(Y + 1, sizeof(int));
    if (!A || !spf) { fprintf(stderr, "alloc\n"); return 1; }
    for (long i = 2; i <= Y; i++) if (!spf[i]) for (long j = i; j <= Y; j += i) if (!spf[j]) spf[j] = (int)i;
    A[1] = 1;
    i128 ND = 1;                          /* N_D(1) = 1 (the g-integer 1) */
    double T1 = ceil(rho * pow(2.0, kappa) + r0);
    if (T1 > 1.0) { fprintf(stderr, "infeasible at n=1: need rho*2^kappa + r0 <= 1\n"); return 1; }
    printf("# P_kappa greedy: kappa=%.4f rho=%.6f r0=%.4f Y=%ld\n", kappa, rho, r0, Y);
    printf("# range            maxE/jump   argmax  omega  busy_frac  primes_at_composite_share  max c/jump  sumb_range\n");
    long lo = 2, hi = 3; double maxEj = 0, maxcj = 0; long argmax = 0; long busy = 0, cnt = 0;
    i128 sumb = 0, sumb_comp = 0; int overflow = 0;
    double sq_sum[16] = {0}, sq_max[16] = {0}, sq_bsum[16] = {0}; long sq_cnt[16] = {0}, sq_neg[16] = {0};
    for (long n = 2; n <= Y; n++) {
        double jump = pow((double)n, kappa - 1.0);
        double Tn_d = ceil(rho * pow((double)(n + 1), kappa) + r0);
        i128 Tn = (i128)Tn_d;
        i128 c = A[n];
        i128 need = Tn - ND - c;
        long b = need > 0 ? (long)need : 0;
        if (b > 0) {
            /* multiply series by (1 - n^{-s})^{-b}: A[m] += sum_{e>=1} C(b+e-1,e) A[m/n^e], m decreasing */
            for (long m = (Y / n) * n; m >= n; m -= n) {
                i128 add = 0, coef = 1; long q = m; int e = 0;
                while (q % n == 0) { q /= n; e++; coef = coef * (b + e - 1) / e; add += coef * (i128)A[q]; }
                i128 v = (i128)A[m] + add;
                if (v > (i128)INT64_MAX) { overflow = 1; v = INT64_MAX; }
                A[m] = (int64_t)v;
            }
        }
        if (n >= Y / 2) {
            long t = n; int sqf = 1, w = 0; while (t > 1) { int p = spf[t]; t /= p; w++; if (t % p == 0) { sqf = 0; break; } }
            if (sqf && w < 16) {
                double inc = rho * (pow((double)(n + 1), kappa) - pow((double)n, kappa));   /* per-point target */
                double r = (double)c / inc;
                sq_sum[w] += r; if (r > sq_max[w]) sq_max[w] = r; sq_cnt[w]++; sq_bsum[w] += (double)b / inc;
                if (need < 0) sq_neg[w]++;
            }
        }
        ND += c + b;
        i128 E = ND - Tn;
        double Ej = (double)E / jump, cj = (double)c / jump;
        if (Ej > maxEj) { maxEj = Ej; argmax = n; }
        if (cj > maxcj) maxcj = cj;
        if (E > 0) busy++;
        cnt++;
        sumb += b; if (spf[n] != n) sumb_comp += b;
        if (n == hi - 1 || n == Y) {
            printf("[%9ld,%9ld]  %9.4f  %9ld  %5d  %9.4f  %12.4f  %12.3f  %.6g\n", lo, n, maxEj, argmax,
                   argmax ? omega_of(argmax, spf) : 0, (double)busy / cnt,
                   sumb > 0 ? (double)sumb_comp / (double)sumb : 0.0, maxcj, (double)sumb);
            fflush(stdout);
            lo = hi; hi *= 2; maxEj = 0; maxcj = 0; argmax = 0; busy = 0; cnt = 0; sumb = 0; sumb_comp = 0;
        }
    }
    printf("# squarefree n in [Y/2,Y] by omega=k: count, mean c/target_inc, max c/target_inc, mean b/target_inc, frac with forced overshoot (c > deficit)\n");
    for (int w = 1; w < 16; w++) if (sq_cnt[w]) printf("k=%2d  n=%9ld  mean_c=%.4f  max_c=%.3f  mean_b=%.4f  forced_frac=%.4f\n", w, sq_cnt[w], sq_sum[w]/sq_cnt[w], sq_max[w], sq_bsum[w]/sq_cnt[w], (double)sq_neg[w]/sq_cnt[w]);
    double Yk = pow((double)Y, kappa);
    printf("# N_D(Y)=%.6g  rho*Y^kappa=%.6g  ratio=%.6f  overflow=%d\n", (double)ND, rho * Yk, (double)ND / (rho * Yk), overflow);
    free(A); free(spf);
    return 0;
}
