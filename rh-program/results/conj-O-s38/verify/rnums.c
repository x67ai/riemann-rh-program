/* rnums.c — conj-O-s38 task 3. Reads the R-primes <= X (uint64, ascending; written by thin2 with RDUMP) and enumerates every
 * squarefree R-number b <= X by depth-first search. Output CSV per bin of the 20-per-decade grid (same edges as thin.c):
 *   bin_hi, piR(bin_hi), Q(bin_hi) = #{b in <R>, b <= bin_hi} (b = 1 included), W(bin_hi) = sum_{b <= bin_hi} prod_{p|b}(p+1)/(p-1)
 * Usage: rnums Rfile X > out.csv */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#define BPD 20
static uint64_t *P; static size_t nP; static uint64_t X; static int K; static uint64_t *edge; /* edge[k] = lo of bin k */
static double *cQ, *cW, *cPi;
static int binof(uint64_t m) { int a = 0, b = K; while (b - a > 1) { int c = (a + b) / 2; if (m >= edge[c]) a = c; else b = c; } return a; }
static void dfs(size_t i0, uint64_t m, double w) {
    for (size_t i = i0; i < nP; i++) { uint64_t p = P[i]; if (m > X / p) break; uint64_t b = m * p;
        double wb = w * (double)(p + 1) / (double)(p - 1); int k = binof(b); cQ[k] += 1; cW[k] += wb; dfs(i + 1, b, wb); } }
int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: rnums Rfile X\n"); return 1; }
    X = (uint64_t)atof(argv[2]); FILE *f = fopen(argv[1], "rb"); if (!f) { perror("Rfile"); return 1; }
    fseek(f, 0, SEEK_END); long sz = ftell(f); fseek(f, 0, SEEK_SET); nP = sz / 8; P = malloc(sz ? sz : 8);
    if (fread(P, 8, nP, f) != nP) { fprintf(stderr, "read fail\n"); return 1; } fclose(f);
    size_t m = 0; for (size_t i = 0; i < nP; i++) if (P[i] <= X) P[m++] = P[i]; nP = m;
    K = (int)floor(BPD * log10((double)X)) + 1; edge = malloc(sizeof(uint64_t) * (K + 2));
    for (int k = 0; k <= K + 1; k++) edge[k] = (uint64_t)ceil(pow(10.0, (double)k / BPD) - 1e-9);
    cQ = calloc(K + 2, sizeof(double)); cW = calloc(K + 2, sizeof(double)); cPi = calloc(K + 2, sizeof(double));
    cQ[0] += 1; cW[0] += 1;                                   /* b = 1 */
    for (size_t i = 0; i < nP; i++) cPi[binof(P[i])] += 1;
    dfs(0, 1, 1.0);
    printf("# rnums X=%llu nP=%zu\n# bin_hi,piR,Q,W\n", (unsigned long long)X, nP);
    double q = 0, w = 0, pi = 0;
    for (int k = 0; k < K; k++) { q += cQ[k]; w += cW[k]; pi += cPi[k]; uint64_t hi = edge[k + 1] - 1; if (hi > X) hi = X;
        printf("%llu,%.0f,%.0f,%.10e\n", (unsigned long long)hi, pi, q, w); if (hi == X) break; }
    return 0; }
