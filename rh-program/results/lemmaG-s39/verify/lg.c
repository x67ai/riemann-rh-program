/* lg.c — lemmaG-s39 deterministic deletion families (NOTE §4). Output: header '# run=... rho=...', bins (stdout), rn rows (stderr).
 *  sq   k X          R = {nextprime(p^k) : p prime}; rho = prod_{p<=P}(1-1/r_p) * prod_{p>P}(1-p^-k) [= 1/(zeta(k) prod_{p<=P}(1-p^-k))]
 *  nsq  k X          R = {nextprime(n^k) : n >= 1};   rho = prod_{n<=N1}(1-1/r_n) * prod_{n>N1}(1-n^-k)  (k = 2: N1/(N1+1))
 *  weyl a c X Y      R = {p <= Y : u_p < min(1, c p^(a-1))}, u_p = (p*T mod 2^64)/2^64, T = floor(frac(sqrt2) 2^64) (SHA-512 H0);
 *                    rho tail beyond Y: mean c*E1((1-a) ln Y)
 *  neck a X Nmax [spread]  necklace clusters: for N <= Nmax the M(a,N) primes > 4^N... generally e^{N lam}, lam = 2 ln a / 1 (theta=1/2):
 *                    tight = the first M(a,N) primes after a^{2N}; spread = nextprime(a^{2N} + j a^{2N}/M(a,N)), j < M(a,N)
 *  planted a c s1 g1 A X Y   greedy deletion with w_p = clip(c p^(a-1) - 2A p^(s1-1) cos(g1 ln p), 0, 1): planted pole of D_R at s1 +- i g1 */
#include "lg_core.h"
static void header(const char *run, uint64_t X, long double rho, const char *extra) {
    printf("# run=%s X=%llu rho=%.18Lf nR_le_X=%zu %s\n", run, (unsigned long long)X, rho, nR, extra); }
static int mode_sq(int argc, char **argv) {
    int k = atoi(argv[2]); uint64_t X = (uint64_t)atof(argv[3]); uint64_t P = (uint64_t)pow((double)X, 1.0 / k) + 2; if (P < 100000) P = 100000;
    sieve(P); long double lr = 0, lp = 0; char run[64]; snprintf(run, 64, "sq_k%d_%.0e", k, (double)X);
    for (uint64_t p = 2; p <= P; p++) if (isprime_s(p)) { uint64_t pk = 1; for (int j = 0; j < k; j++) pk *= p;
        uint64_t r = nextprime(pk); if (r <= X) addR(r); lr += log1pl(-1.0L / r); lp += log1pl(-powl((long double)p, -(long double)k)); }
    long double rho = expl(lr - lp) / zeta_int(k); size_t nx = nR;
    char ex[128]; snprintf(ex, 128, "P=%llu zeta_k=%.18Lf", (unsigned long long)P, zeta_int(k)); header(run, X, rho, ex);
    char dp[96]; snprintf(dp, 96, "data/R_%s.txt", run); dumpR(dp, X); build_rfree(X); emit_bins(run, X, (double)rho); emit_rn(run, X); (void)nx; return 0; }
static int mode_nsq(int argc, char **argv) {
    int k = atoi(argv[2]); uint64_t X = (uint64_t)atof(argv[3]); uint64_t N1 = 300000; long double lr = 0; uint64_t prev = 0, coll = 0;
    char run[64]; snprintf(run, 64, "nsq_k%d_%.0e", k, (double)X);
    for (uint64_t n = 1; n <= N1; n++) { uint64_t nk = 1; for (int j = 0; j < k; j++) nk *= n; uint64_t r = nextprime(nk);
        if (r == prev) { coll++; continue; } prev = r; if (r <= X) addR(r); lr += log1pl(-1.0L / r); }
    long double tail = 0; if (k == 2) tail = logl((long double)N1 / (N1 + 1)); else for (uint64_t n = N1 + 1; n <= 50 * N1; n++) tail += log1pl(-powl((long double)n, -(long double)k));
    long double rho = expl(lr + tail); char ex[96]; snprintf(ex, 96, "N1=%llu collisions=%llu", (unsigned long long)N1, (unsigned long long)coll);
    header(run, X, rho, ex); char dp[96]; snprintf(dp, 96, "data/R_%s.txt", run); dumpR(dp, X); build_rfree(X);
    emit_bins(run, X, (double)rho); emit_rn(run, X); return 0; }
static int mode_weyl(int argc, char **argv) {
    double a = atof(argv[2]), c = atof(argv[3]); uint64_t X = (uint64_t)atof(argv[4]), Y = (uint64_t)atof(argv[5]); if (Y < X) Y = X;
    const uint64_t T = 0x6A09E667F3BCC908ULL; sieve(Y); long double lr = 0; char run[80]; snprintf(run, 80, "weyl_a%.2f_c%g_%.0e", a, c, (double)X);
    for (uint64_t p = 2; p <= Y; p++) if (isprime_s(p)) { uint64_t u = p * T; long double w = c * powl((long double)p, a - 1.0L); if (w > 1) w = 1;
        if ((long double)u < w * 18446744073709551616.0L) { if (p <= X) addR(p); lr += log1pl(-1.0L / p); } }
    long double rho = expl(lr - c * E1((1.0 - a) * log((double)Y))); char ex[64]; snprintf(ex, 64, "Y=%llu", (unsigned long long)Y);
    header(run, X, rho, ex); char dp[96]; snprintf(dp, 96, "data/R_%s.txt", run); dumpR(dp, X); build_rfree(X);
    emit_bins(run, X, (double)rho); emit_rn(run, X); return 0; }
static int mode_neck(int argc, char **argv) {
    int a = atoi(argv[2]); uint64_t X = (uint64_t)atof(argv[3]); int Nmax = atoi(argv[4]); int spread = (argc > 5 && !strcmp(argv[5], "spread"));
    long double lr = 0; char run[80]; snprintf(run, 80, "neck%s_a%d_%.0e", spread ? "spread" : "", a, (double)X);
    for (int N = 1; N <= Nmax; N++) { uint64_t base = 1; for (int j = 0; j < 2 * N; j++) base *= (uint64_t)a; uint64_t cN = necklace_num(a, N), p = base;
        for (uint64_t j = 0; j < cN; j++) { p = spread ? nextprime(base + j * (base / cN)) : nextprime(p); if (p <= X) addR(p); lr += log1pl(-1.0L / p); } }
    long double tail = 0; for (int N = Nmax + 1; N <= 40; N++) tail += (long double)necklace_num(a, N) * log1pl(-powl((long double)a, -2.0L * N) * (spread ? 0.7L : 1.0L));
    long double rho = expl(lr + tail); char ex[64]; snprintf(ex, 64, "Nmax=%d", Nmax); header(run, X, rho, ex);
    qsort(Rp, nR, sizeof(uint64_t), cmpu); for (size_t i = 1; i < nR; i++) if (Rp[i] == Rp[i - 1]) { fprintf(stderr, "DUPLICATE R-prime %llu\n", (unsigned long long)Rp[i]); return 1; }
    char dp[96]; snprintf(dp, 96, "data/R_%s.txt", run); dumpR(dp, X); build_rfree(X); emit_bins(run, X, (double)rho); emit_rn(run, X); return 0; }
static double tail_osc(double s1, double g1, double L) {   /* Re int_L^inf e^{-(1-s1)v} cos(g1 v) / v dv, Simpson */
    double b = 1.0 - s1, V = L + 60.0 / b; int n = 2000000; double h = (V - L) / n, s = 0;
    for (int i = 0; i <= n; i++) { double v = L + i * h, f = exp(-b * v) * cos(g1 * v) / v; s += (i == 0 || i == n) ? f : (i & 1 ? 4 * f : 2 * f); }
    return s * h / 3; }
static int mode_planted(int argc, char **argv) {
    double a = atof(argv[2]), c = atof(argv[3]), s1 = atof(argv[4]), g1 = atof(argv[5]), A = atof(argv[6]);
    uint64_t X = (uint64_t)atof(argv[7]), Y = (uint64_t)atof(argv[8]); if (Y < X) Y = X; sieve(Y);
    char run[96]; snprintf(run, 96, "planted_a%.2f_s%.2f_g%g_A%g_%.0e", a, s1, g1, A, (double)X);
    long double F = 0, lr = 0; uint64_t cnt = 0; double maxD = 0;
    for (uint64_t p = 2; p <= Y; p++) if (isprime_s(p)) { double lp = log((double)p);
        double w = c * exp((a - 1) * lp) - 2 * A * exp((s1 - 1) * lp) * cos(g1 * lp); if (w < 0) w = 0; if (w > 1) w = 1;
        F += w; if ((long double)cnt < F) { cnt++; if (p <= X) addR(p); lr += log1pl(-1.0L / p); }
        double D = fabs((double)((long double)cnt - F)); if (D > maxD) maxD = D; }
    double L = log((double)Y); long double tail = c * E1((1 - a) * L) - 2 * A * tail_osc(s1, g1, L);
    long double rho = expl(lr - tail); char ex[96]; snprintf(ex, 96, "Y=%llu max|pi_R-F|=%.3f tail=%.3Le", (unsigned long long)Y, maxD, tail);
    header(run, X, rho, ex); char dp[128]; snprintf(dp, 128, "data/R_%s.txt", run); dumpR(dp, X); build_rfree(X);
    emit_bins(run, X, (double)rho); emit_rn(run, X); return 0; }
int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: see header\n"); return 1; }
    if (!strcmp(argv[1], "sq")) return mode_sq(argc, argv);
    if (!strcmp(argv[1], "nsq")) return mode_nsq(argc, argv);
    if (!strcmp(argv[1], "weyl")) return mode_weyl(argc, argv);
    if (!strcmp(argv[1], "neck")) return mode_neck(argc, argv);
    if (!strcmp(argv[1], "planted")) return mode_planted(argc, argv);
    fprintf(stderr, "unknown mode\n"); return 1; }
