/* s8cert.c -- S8(rho) generator with every cell decision PROVED, plus block moments of n^{-sigma}.
   Written for lemmaB-s41/U6-certificate from the definition only (s40 CHARTER §1; Lindley form, s41 CHARTER §2(a)).
   Lattice x_k = 1 + (k - 1/2) t, t = 1/rho. A composite in cell k (x_{k-1} < c < x_k) counts in c_k; a g-prime is placed
   at x_k iff e_{k-1} = 0 and c_k = 0; e_k = max(e_{k-1} + c_k - 1, 0); N(x_k) = k + 1 + e_k.
   Composites are generated as P*q, q = largest g-prime factor, P a "prefix" (g-integer > 1 with P*P^+(P) <= X).
   Rigor: every value is a double with a proved relative error bound (standard model, |delta| <= u = 2^-53, no FMA
   contraction); a cell decision is accepted only if the computed distance to both lattice neighbours exceeds the
   proved error bound; otherwise it is re-decided EXACTLY in GMP integers from the lattice indices of the factors and a
   dyadic enclosure TLO/2^D <= t <= THI/2^D (params.txt, from pi_enclosure.py).
   Build: cc -O2 -ffp-contract=off -o s8cert s8cert.c -I/opt/homebrew/include -L/opt/homebrew/lib -lgmp -lm
   Usage: s8cert <params.txt> <name> <Xmax> <outprefix> [Lmax_cells]                                           */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <gmp.h>

typedef __int128 i128;
static const double U = 0x1p-53;          /* unit roundoff */
static const double SL = 0x1p-30;         /* emission slack s (>> all relative error bounds ~1e-14) */

static double TT, RHO;                    /* TT = RN(t) (|TT - t| <= u t); RHO only for guesses */
static mpz_t TLO, THI, P2;                /* TLO/2^D <= t <= THI/2^D ; P2 = 2^(D+1) */
static int DD;

static void die(const char *m) { fprintf(stderr, "FATAL: %s\n", m); printf("FATAL: %s\n", m); exit(2); }

/* lattice point / g-prime value: fl(1 + fl((k - 1/2) * TT)); relative error <= 3.0001 u (NOTE §2) */
static inline double xt(uint64_t k) { return 1.0 + ((double)k - 0.5) * TT; }

/* ---------- exact decisions in GMP ----------
   c = prod_{i<n} (1 + (k_i - 1/2) t) = prod (P2 + (2k_i - 1) T) / P2^n   (t = T / 2^D), increasing in t.
   mode 0: compare c with lattice point x_m = (P2 + (2m-1) T)/P2 (increasing in t);
   mode 1: compare c with the integer V.
   Returns +1 if c > target for every t in the enclosure, -1 if c < target for every t, 0 if undecided. */
static mpz_t gL, gH, gR, gS, gF;
static int exact_cmp(const uint32_t *ks, int n, int mode, uint64_t m_or_V) {
    mpz_set_ui(gL, 1); mpz_set_ui(gH, 1);
    for (int i = 0; i < n; i++) {
        mpz_mul_ui(gF, TLO, 2 * (unsigned long)ks[i] - 1); mpz_add(gF, gF, P2); mpz_mul(gL, gL, gF);
        mpz_mul_ui(gF, THI, 2 * (unsigned long)ks[i] - 1); mpz_add(gF, gF, P2); mpz_mul(gH, gH, gF);
    }
    int res = 0;
    if (mode == 0) {
        if (m_or_V == 0) return +1;                     /* x_0 < 1 < c */
        mpz_pow_ui(gS, P2, n - 1);
        mpz_mul_ui(gF, THI, 2 * m_or_V - 1); mpz_add(gF, gF, P2); mpz_mul(gR, gF, gS);   /* x_m(t_hi) scaled */
        if (mpz_cmp(gL, gR) > 0) res = +1;
        mpz_mul_ui(gF, TLO, 2 * m_or_V - 1); mpz_add(gF, gF, P2); mpz_mul(gR, gF, gS);   /* x_m(t_lo) scaled */
        if (mpz_cmp(gH, gR) < 0) res = (res == 0) ? -1 : 99;
    } else {
        mpz_pow_ui(gS, P2, n); mpz_mul_ui(gR, gS, m_or_V);
        if (mpz_cmp(gL, gR) > 0) res = +1;
        if (mpz_cmp(gH, gR) < 0) res = (res == 0) ? -1 : 99;
    }
    if (res == 99) die("inconsistent exact comparison");
    return res;
}

/* ---------- storage ---------- */
typedef struct { double v; uint32_t cur; int32_t parent; uint32_t last; uint8_t om; } Pre;   /* prefix record */
static Pre *pre; static uint64_t npre, cappre;
static uint32_t *pk; static uint64_t npk, cappk;     /* lattice indices of stored g-primes (value <= Xstore) */
static uint32_t fact[80]; static int nfact;

static void build_fact(int64_t pid, uint32_t jq) {   /* factor list of pre[pid] * prime pk[jq] */
    nfact = 0; fact[nfact++] = pk[jq];
    while (pid >= 0) { if (nfact >= 79) die("fact overflow"); fact[nfact++] = pk[pre[pid].last]; pid = pre[pid].parent; }
}

/* statistics of the decisions */
static uint64_t ndec, nfb, nfbV, nrej;
static double minrel = 1e300, minrel_at;
