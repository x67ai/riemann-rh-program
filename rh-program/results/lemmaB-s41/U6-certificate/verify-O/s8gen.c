/* s8gen.c — second-producer generator of S8(pi/D) to the lattice point x_KFIN (read-O, U6).
 * Build: cc -O2 -o s8gen s8gen.c -lm      Run: s8gen params.txt outbase [SEGLEN_LOG2]
 * Cell form: c_m = # composites in (x_{m-1}, x_m) (none sits on a lattice point: the exact test would stop);
 * N(x_m-) = N(x_{m-1}) + c_m (+1 in cell 1 for the g-integer 1); a g-prime is placed at x_m iff N(x_m-) = m. */
#include "s8g_core.h"
#include "s8g_mom.h"
#include "s8g_dfs.h"

int main(int argc, char **argv) {
  if (argc < 3) die("usage: s8gen params outbase [seglog2]");
  read_params(argv[1]);
  int seglog = argc > 3 ? atoi(argv[3]) : 27;
  u64 SEG = 1ULL << seglog;
  const char *ft = getenv("S8G_FTEST"); ftest = ft ? strtoull(ft, NULL, 10) : 0;
  mom = calloc(NBLK, sizeof(Mom)); cnt = malloc(SEG * sizeof(u16));
  capP = 1 << 20; P = malloc(capP * 4);
  if (!mom || !cnt || !P) die("alloc");
  dep_E[0][0] = 1;
  clock_t t0 = clock(); time_t w0 = time(NULL);
  printf("s8gen D=%d R=%d KFIN=%llu NCAP=%llu seg=2^%d ftest=%llu t~%.17g\n", D, R, (unsigned long long)KFIN,
         (unsigned long long)NCAP, seglog, (unsigned long long)ftest, tdbl);
  u64 nprev = 0, pic = 0, emax = 0, emax_at = 0; long double esum = 0;
  add_point(1, (u128)1 << (F - 1), (u128)1 << (F - 1));          /* the g-integer 1: W = 1/2, cell 1 */
  int nextcp = 0;
  m0 = 1;
  while (m0 <= KFIN) {
    m1 = m0 + SEG; if (m1 > 2 * m0 + 1) m1 = 2 * m0 + 1; if (m1 > KFIN + 1) m1 = KFIN + 1;
    memset(cnt, 0, (m1 - m0) * sizeof(u16));
    ulo = xa(m0 - 1) * (1 - 1e-12); if (m0 == 1) ulo = 1.0;
    uhi = xa(m1 - 1) * (1 + 1e-12);
    nact = 0;
    for (int k = 0; k < ncp; k++) if (cpCell[k] >= m0 && cpCell[k] < m1) { act[nact++] = k; cpbelow[k] = 0; }
    for (size_t i0 = 0; i0 < nP; i0++) {
      double xq = xa(P[i0]);
      if (xq * xq > uhi * (1 + 1e-9)) break;
      set_depth(1, i0, xq);
      dfs(1);
    }
    for (u64 m = m0; m < m1; m++) {
      u64 c = cnt[m - m0] + (m == 1 ? 1 : 0);
      u64 Nm = nprev + c;                                   /* N(x_m -) */
      while (nextcp < ncp && cpCell[nextcp] == m) {         /* checkpoint V in (x_{m-1}, x_m) */
        int k = nextcp++;
        u64 NV = nprev + cpbelow[k];
        printf("CHECK V=%llu cell=%llu N(V)=%llu pi(V)=%llu | lattice x_%llu: N=%llu pi=%llu e=%llu\n",
               (unsigned long long)cpV[k], (unsigned long long)m, (unsigned long long)NV, (unsigned long long)pic,
               (unsigned long long)(m - 1), (unsigned long long)nprev, (unsigned long long)pic,
               (unsigned long long)(nprev - m));
      }
      if (Nm < m) die("N(x_m-) < m: E < -1/2");
      if (Nm == m) {
        pic++; Nm++;
        if (m <= NCAP) { if (nP == capP) { capP *= 2; P = realloc(P, capP * 4); if (!P) die("alloc P"); } P[nP++] = (u32)m; }
        add_point(m, (u128)m << F, (u128)m << F);
      }
      u64 e = Nm - m - 1;
      esum += e; if (e > emax) { emax = e; emax_at = m; }
      nprev = Nm;
    }
    fprintf(stderr, "[%6.0fs] cells < %llu done: N=%llu pi=%llu stored=%zu comps=%llu fall=%llu\n",
            difftime(time(NULL), w0), (unsigned long long)m1, (unsigned long long)nprev, (unsigned long long)pic,
            nP, (unsigned long long)ncomp, (unsigned long long)nfall);
    m0 = m1;
  }
  printf("FINAL K=%llu N(x_K)=%llu pi(x_K)=%llu e_K=%llu E(x_K)=e_K+1/2\n", (unsigned long long)KFIN,
         (unsigned long long)nprev, (unsigned long long)pic, (unsigned long long)(nprev - KFIN - 1));
  printf("composites=%llu storedprimes=%zu maxfactors=%llu fallbacks_cell=%llu fallbacks_checkpoint=%llu\n",
         (unsigned long long)ncomp, nP, (unsigned long long)maxj, (unsigned long long)nfall, (unsigned long long)nfall_cp);
  printf("max e over lattice points=%llu at m=%llu (sup of E on the lattice = %llu.5); mean e=%.6Lf\n",
         (unsigned long long)emax, (unsigned long long)emax_at, (unsigned long long)emax, esum / (long double)KFIN);
  printf("closest fast-path decision: margin > %.6e in W (= %.6e in u), cell %llu, factors x(n):", minmarg,
         minmarg * tdbl, (unsigned long long)mincell);
  for (int k = 0; k < minj; k++) printf(" %llu", (unsigned long long)minfac[k]);
  printf("\nindividual=%zu cpu=%.1fs wall=%.0fs\n", nind, (double)(clock() - t0) / CLOCKS_PER_SEC, difftime(time(NULL), w0));
  write_moments(argv[2]);
  return 0;
}
