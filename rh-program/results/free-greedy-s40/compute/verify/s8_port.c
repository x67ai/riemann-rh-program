/* s8_port.c -- line-by-line C port of proto/s8_proto.py (dress rehearsal, KICKSTART 10(l)).
   Same IEEE-double arithmetic in the same order as the Python prototype (compile with
   -ffp-contract=off so that no fused multiply-add changes a rounding), same heap order
   ((position, prime index) lexicographic, as Python tuples), same incremental deficit D0,
   same event-sampled statistics.  Output format identical to the prototype's.
   Usage: s8_port RHO X        (RHO as a decimal; e.g. 0.78539816339744830962) */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

typedef struct { double pos; long i; } hent;            /* composite heap: (position, prime index) */
typedef struct { double pw, q, lq; } pent;              /* prime-power heap: (q^k, q, log q) */
static hent *H; static long hn = 0, hcap = 0;
static pent *P; static long pn = 0, pcap = 0;
static int hless(hent a, hent b) { return a.pos < b.pos || (a.pos == b.pos && a.i < b.i); }
static int pless(pent a, pent b) { return a.pw < b.pw || (a.pw == b.pw && (a.q < b.q || (a.q == b.q && a.lq < b.lq))); }
static void hpush(hent e) {
    if (hn == hcap) { hcap = hcap ? 2 * hcap : 1024; H = realloc(H, hcap * sizeof(hent)); }
    long k = hn++; while (k > 0) { long p = (k - 1) / 2; if (!hless(e, H[p])) break; H[k] = H[p]; k = p; } H[k] = e;
}
static hent hpop(void) {
    hent top = H[0], last = H[--hn]; long k = 0;
    for (;;) { long c = 2 * k + 1; if (c >= hn) break; if (c + 1 < hn && hless(H[c + 1], H[c])) c++;
               if (!hless(H[c], last)) break; H[k] = H[c]; k = c; }
    if (hn > 0) H[k] = last; return top;
}
static void ppush(pent e) {
    if (pn == pcap) { pcap = pcap ? 2 * pcap : 1024; P = realloc(P, pcap * sizeof(pent)); }
    long k = pn++; while (k > 0) { long p = (k - 1) / 2; if (!pless(e, P[p])) break; P[k] = P[p]; k = p; } P[k] = e;
}
static pent ppop(void) {
    pent top = P[0], last = P[--pn]; long k = 0;
    for (;;) { long c = 2 * k + 1; if (c >= pn) break; if (c + 1 < pn && pless(P[c + 1], P[c])) c++;
               if (!pless(P[c], last)) break; P[k] = P[c]; k = c; }
    if (pn > 0) P[k] = last; return top;
}
static double *val; static long *lpf; static long nval = 0, vcap = 0;
static double *primes; static long *cursor; static long np = 0, pcap2 = 0;
static void vappend(double x, long l) {
    if (nval == vcap) { vcap = vcap ? 2 * vcap : 1 << 20; val = realloc(val, vcap * sizeof(double)); lpf = realloc(lpf, vcap * sizeof(long)); }
    val[nval] = x; lpf[nval] = l; nval++;
}
static void advance(long i) {
    long c = cursor[i] + 1;
    while (lpf[c] > i) c++;
    cursor[i] = c;
    hent e = { primes[i] * val[c], i }; hpush(e);
}
int main(int argc, char **argv) {
    double rho = (argc > 1 && argv[1][0] != 112) ? strtod(argv[1], 0) : M_PI / 4, X = argc > 2 ? strtod(argv[2], 0) : 1e6;
    clock_t t0 = clock();
    vappend(1.0, -1);
    long N = 1; double x0 = 1.0, D0 = 0.0, psi = 0.0, supE = 0.0, supPsi = 0.0; long maxcluster = 0;
    double nextdec = 10.0, step = pow(10.0, 0.5);
    double recs[64][7]; int nrec = 0;
    double *win = malloc(sizeof(double) * 4096); long wh = 0, wt = 0;  /* ring buffer, power-of-two size */
    for (;;) {
        double xstar = x0 + (0.5 - D0) / rho, x;
        if (hn > 0 && H[0].pos <= xstar) {
            hent e = hpop(); x = e.pos; long i = e.i;
            if (x > X) break;
            double Dbefore = D0 + rho * (x - x0);
            D0 = Dbefore - 1.0; x0 = x; N += 1;
            vappend(x, i);
            advance(i);
            double E = -D0; if (E > supE) supE = E;
        } else {
            x = xstar; if (x > X) break;
            D0 = -0.5; x0 = x; N += 1;
            if (np == pcap2) { pcap2 = pcap2 ? 2 * pcap2 : 1 << 16; primes = realloc(primes, pcap2 * sizeof(double)); cursor = realloc(cursor, pcap2 * sizeof(long)); }
            primes[np] = x; cursor[np] = 0; np++;
            vappend(x, np - 1);
            advance(np - 1);
            double lq = log(x); psi += lq;
            if (x * x <= X) { pent p = { x * x, x, lq }; ppush(p); }
        }
        while (pn > 0 && P[0].pw <= x) { pent p = ppop(); psi += p.lq; if (p.pw * p.q <= X) { pent r = { p.pw * p.q, p.q, p.lq }; ppush(r); } }
        double d = fabs(psi - x); if (d > supPsi) supPsi = d;
        win[wt & 4095] = x; wt++;
        while (win[wh & 4095] < x - 1.0) wh++;
        if (wt - wh > maxcluster) maxcluster = wt - wh;
        if (x >= nextdec) {
            double *r = recs[nrec++]; r[0] = nextdec; r[1] = N; r[2] = np; r[3] = supE; r[4] = supPsi; r[5] = maxcluster; r[6] = psi - x;
            nextdec *= step;
        }
    }
    printf("S8 rho = %.12f  X = %g  g-integers = %ld  g-primes = %ld  time = %.1fs\n", rho, X, N, np, (double)(clock() - t0) / CLOCKS_PER_SEC);
    printf("   x        N(x)      pi_P(x)   sup E   sup|psi-x|  max #g-int in a unit window   psi-x\n");
    for (int k = 0; k < nrec; k++) {
        double *r = recs[k];
        printf("%10.3g %10ld %9ld %8.2f %10.1f %5ld %12.1f", r[0], (long)r[1], (long)r[2], r[3], r[4], (long)r[5], r[6]);
        if (k > 0 && recs[k - 1][3] > 0 && recs[k - 1][4] > 0)
            printf("  slopes: E %+.3f  psi %+.3f", log(r[3] / recs[k - 1][3]) / log(r[0] / recs[k - 1][0]), log(r[4] / recs[k - 1][4]) / log(r[0] / recs[k - 1][0]));
        printf("\n");
    }
    printf("first g-primes:"); for (int k = 0; k < 14 && k < np; k++) printf(" %.4f", primes[k]); printf("\n");
    printf("# full-precision tail: N=%ld pi=%ld supE=%.17g supPsi=%.17g lastx0=%.17g D0=%.17g\n", N, np, supE, supPsi, x0, D0);
    return 0;
}
