/* s8g_dfs.h — enumeration of the composites of one segment of cells [m0, m1) (read-O, U6).
 * Every composite is a multiset q_1 <= ... <= q_j (j >= 2) of stored g-primes, written once as
 * prefix g = q_1...q_{j-1} (depth d = j-1) times last factor q_j with list index >= that of q_{j-1}.
 * Pruning uses doubles with relative slack 1e-9 and is only conservative; membership in the segment is decided
 * by the exact cell. */
static u32 *P; static size_t nP, capP;            /* lattice indices of stored g-primes, increasing */
static u16 *cnt;                                  /* composites per cell of the segment */
static u64 m0, m1; static double ulo, uhi;        /* segment cells and approximate u-range */
static int dep_d; static size_t dep_idx[MAXR + 2]; static double dep_g[MAXR + 2];
static u64 dep_b[MAXR + 2]; static u128 dep_E[MAXR + 2][MAXR + 2];
static u128 dep_A[MAXR + 2], dep_B[MAXR + 2], dep_SA[MAXR + 2], dep_SB[MAXR + 2];
static u64 ncomp, nfall, nfall_cp, maxj, ftest;   /* ftest: S8G_FTEST, forces the exact path on a fraction 2^(1-ftest) */
static double minmarg = 1e300; static u64 minfac[MAXR + 2]; static int minj; static u64 mincell;
static int nact; static int act[MAXCP]; static u64 cpbelow[MAXCP];

static inline double xa(u64 n) { return 1.0 + ((double)n - 0.5) * tdbl; }

static size_t lower_bound_x(double q, size_t from) {   /* first i >= from with xa(P[i]) >= q */
  size_t lo = from, hi = nP;
  while (lo < hi) { size_t mid = lo + (hi - lo) / 2; if (xa(P[mid]) < q) lo = mid + 1; else hi = mid; }
  return lo;
}

static void set_depth(int d, size_t i, double gv) {    /* dep[d] = dep[d-1] * P[i]  (dep[0] = empty product) */
  u64 b = 2 * (u64)P[i] - 1;
  dep_idx[d] = i; dep_g[d] = gv; dep_b[d] = b;
  dep_E[d][0] = 1;
  for (int r = 1; r <= d; r++) dep_E[d][r] = (r <= d - 1 ? dep_E[d - 1][r] : 0) + (u128)b * dep_E[d - 1][r - 1];
  u128 A = 0, B = 0, SA = 0, SB = 0;
  for (int r = 2; r <= d; r++) { A += dep_E[d][r] * Kr[r]; SA += dep_E[d][r]; }
  for (int r = 2; r <= d + 1; r++) { B += dep_E[d][r - 1] * Kr[r]; SB += dep_E[d][r - 1]; }
  dep_A[d] = A; dep_B[d] = B; dep_SA[d] = SA; dep_SB[d] = SB;
}

static u64 exact_cell(int d, u64 b) {
  u64 bb[MAXR + 2], HL[NL], HH[NL];
  for (int k = 1; k <= d; k++) bb[k - 1] = dep_b[k];
  bb[d] = b;
  exact_W(bb, d + 1, HL, HH);
  if (HL[NL - 1] != HH[NL - 1]) die("UNDECIDED cell at 2^-320");
  nfall++;
  return HL[NL - 1] + 1;
}

static int exact_below_cp(int d, u64 b, int k) {       /* 1 if c < V_k, 0 if c > V_k */
  u64 bb[MAXR + 2], HL[NL], HH[NL], W1[NL];
  for (int q = 1; q <= d; q++) bb[q - 1] = dep_b[q];
  bb[d] = b;
  exact_W(bb, d + 1, HL, HH);
  nfall_cp++;
  if (ml_cmp(HH, cpWH[k]) <= 0) return 1;
  memcpy(W1, cpWH[k], sizeof W1); ml_add_u128(W1, 1, 0);
  if (ml_cmp(HL, W1) >= 0) return 0;
  die("UNDECIDED checkpoint comparison at 2^-320");
  return 0;
}

static void dfs(int d) {
  if (d + 1 > R) die("composite with more than R factors");
  double gv = dep_g[d];
  u64 E1 = (u64)dep_E[d][1]; u128 A = dep_A[d], B = dep_B[d], SA = dep_SA[d], SB = dep_SB[d];
  size_t i = lower_bound_x(ulo / gv * (1 - 1e-9), dep_idx[d]);
  for (; i < nP; i++) {
    u64 n = P[i];
    if (gv * xa(n) > 2.0 * uhi) break;               /* certainly beyond the segment; guards overflow */
    u64 b = 2 * n - 1;
    u128 Hlo = ((u128)(E1 + b + 1) << (F - 1)) + A + (u128)b * B;
    u128 Hhi = Hlo + SA + (u128)b * SB;
    u64 Mlo = (u64)(Hlo >> F), Mhi = (u64)(Hhi >> F), cell;
    u128 one = (u128)1 << F;
    u128 dl = Hlo - ((u128)Mlo << F), dh = ((u128)(Mlo + 1) << F) - Hhi;   /* margins (valid if Mlo == Mhi) */
    int forced = ftest && Mlo == Mhi && (dl < (one >> ftest) || dh < (one >> ftest));
    if (Mlo == Mhi && !forced) cell = Mlo + 1;
    else { cell = exact_cell(d, b); if (forced && cell != Mlo + 1) die("ftest: exact path disagrees"); }
    if (cell < m0) continue;
    if (cell >= m1) break;
    cnt[cell - m0]++; ncomp++;
    if (d + 1 > (int)maxj) maxj = d + 1;
    if (Mlo == Mhi) {
      double mg = (double)(dl < dh ? dl : dh) / (double)one;
      if (mg < minmarg) { minmarg = mg; minj = d + 1; mincell = cell; for (int k = 1; k <= d; k++) minfac[k - 1] = P[dep_idx[k]]; minfac[d] = n; }
    }
    for (int a = 0; a < nact; a++) {
      int k = act[a];
      if (cell != cpCell[k]) continue;
      int below;
      if (Hhi <= cpW[k]) below = 1; else if (Hlo >= cpW[k] + 1) below = 0; else below = exact_below_cp(d, b, k);
      cpbelow[k] += below;
    }
    add_point(cell, Hlo, Hhi);
  }
  for (i = dep_idx[d]; i < nP; i++) {
    double xq = xa(P[i]);
    if (gv * xq * xq > uhi * (1 + 1e-9)) break;
    set_depth(d + 1, i, gv * xq);
    dfs(d + 1);
  }
}
