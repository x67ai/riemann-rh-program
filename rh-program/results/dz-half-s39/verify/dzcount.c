/* dzcount.c — exact counting of Beurling g-integers <= X for a sorted list of g-primes (float64).
   Unit dz-half-s39. Every g-integer m in (1, X] (formal product, with multiplicity) is enumerated by DFS over
   non-decreasing prime indices and binned into (e_i, e_{i+1}], e = 2^j (1 + i/K), j = 0..J-1, i = 0..K-1, so
   N(e_{i+1}) = 1 + cumulative count (the 1 is the g-integer 1).  Output: J*K int64 counts (binary) + a summary line.
   Usage: dzcount PRIMES.f64 X K J OUT.i64                                                                       */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdint.h>

static double *P; static long np; static double X; static long K; static int J;
static int64_t *cnt; static int64_t total = 0, outside = 0; static int maxdepth = 0;

static inline void record(double m) {
    int e; double fr = frexp(m, &e);           /* m = fr * 2^e, fr in [0.5, 1) */
    int j = (fr == 0.5) ? e - 2 : e - 1;         /* m in (2^j, 2^{j+1}] */
    if (j < 0 || j >= J) { outside++; return; }
    double t = (ldexp(m, -j) - 1.0) * (double)K; /* exact: power-of-two scalings, Sterbenz subtraction */
    long b = (long)ceil(t) - 1;
    if (b < 0) b = 0; if (b >= K) b = K - 1;
    cnt[(long)j * K + b]++; total++;
}

static void dfs(double m, long i, int depth) {
    if (depth > maxdepth) maxdepth = depth;
    for (long k = i; k < np; k++) {
        double v = m * P[k];
        if (v > X) break;
        record(v);
        dfs(v, k, depth + 1);
    }
}

int main(int argc, char **argv) {
    if (argc != 6) { fprintf(stderr, "usage: dzcount PRIMES.f64 X K J OUT.i64\n"); return 1; }
    FILE *f = fopen(argv[1], "rb"); if (!f) { perror("primes"); return 1; }
    fseek(f, 0, SEEK_END); long bytes = ftell(f); fseek(f, 0, SEEK_SET);
    np = bytes / 8; P = malloc(bytes);
    if (fread(P, 8, np, f) != (size_t)np) { fprintf(stderr, "read error\n"); return 1; }
    fclose(f);
    X = atof(argv[2]); K = atol(argv[3]); J = atoi(argv[4]);
    for (long k = 1; k < np; k++) if (!(P[k] > P[k-1])) { fprintf(stderr, "primes not strictly increasing at %ld\n", k); return 1; }
    if (np && !(P[0] > 1.0)) { fprintf(stderr, "first prime must exceed 1\n"); return 1; }
    cnt = calloc((size_t)J * K, sizeof(int64_t));
    dfs(1.0, 0, 1);
    FILE *o = fopen(argv[5], "wb"); fwrite(cnt, sizeof(int64_t), (size_t)J * K, o); fclose(o);
    printf("{\"n_primes\": %ld, \"n_ginteger_gt1\": %lld, \"outside_bins\": %lld, \"max_depth\": %d}\n",
           np, (long long)total, (long long)outside, maxdepth);
    return 0;
}
