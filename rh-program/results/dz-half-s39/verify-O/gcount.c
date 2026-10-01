/* read-O own enumerator of Beurling g-integers (formal products, with multiplicity).
 * mode "bins":  gcount bins primes.f64 X B out.i64      -> counts per log2-bin  [2^{i/B}, 2^{(i+1)/B})
 * mode "count": gcount count primes.f64 x lo hi          -> #{g-integers <= x using no prime in (lo, hi]}
 * primes.f64: sorted little-endian doubles. Depth-first over non-decreasing prime index. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static double *P; static long np; static double X, LO, HI; static int B;
static int64_t *cnt; static long nb; static int64_t total;

static void rec_bins(long i0, double m) {
    for (long i = i0; i < np; i++) {
        double mm = m * P[i];
        if (mm > X) break;
        long b = (long)floor(log2(mm) * B);
        if (b >= nb) b = nb - 1;
        cnt[b]++;
        rec_bins(i, mm);
    }
}
static void rec_count(long i0, double m) {
    for (long i = i0; i < np; i++) {
        double mm = m * P[i];
        if (mm > X) break;
        if (P[i] > LO && P[i] <= HI) continue;
        total++;
        rec_count(i, mm);
    }
}
int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage\n"); return 1; }
    FILE *f = fopen(argv[2], "rb"); if (!f) { perror("primes"); return 1; }
    fseek(f, 0, SEEK_END); long sz = ftell(f); fseek(f, 0, SEEK_SET);
    np = sz / 8; P = malloc(sz); if (fread(P, 8, np, f) != (size_t)np) return 1; fclose(f);
    for (long i = 1; i < np; i++) if (P[i] < P[i-1]) { fprintf(stderr, "unsorted at %ld\n", i); return 1; }
    if (!strcmp(argv[1], "bins")) {
        X = atof(argv[3]); B = atoi(argv[4]);
        nb = (long)floor(log2(X) * B) + 1;
        cnt = calloc(nb, sizeof(int64_t));
        cnt[0]++;                         /* the empty product 1 */
        rec_bins(0, 1.0);
        FILE *g = fopen(argv[5], "wb"); fwrite(cnt, sizeof(int64_t), nb, g); fclose(g);
        int64_t s = 0; for (long i = 0; i < nb; i++) s += cnt[i];
        printf("np=%ld nb=%ld N(X)=%lld\n", np, nb, (long long)s);
    } else {
        X = atof(argv[3]); LO = atof(argv[4]); HI = atof(argv[5]);
        total = 1; rec_count(0, 1.0);
        printf("%lld\n", (long long)total);
    }
    return 0;
}
