// s8o.cpp -- independent generator of S8(rho), Opus reader (Session 41).
// Written from CHARTER section 1 only (no code of the unit consulted).
// g-prime with count k so far sits at the lattice point L_k = 1 + (k - 1/2) t, t = 1/rho;
// the next g-integer is min(next composite, L_k) (composite first on a tie).
// Arithmetic: positions as 128-bit unsigned fixed point with F fractional bits,
// rigorous error bounds (in ulps); every composite-vs-lattice decision is certified
// (|diff| > errC + errL) or counted as a FLAG. Composites m = n * p, p = P(m) largest
// g-prime factor, n a "prefix" (g-integer with n * P(n) <= X); every prefix walks the
// g-prime list from P(n) on. Windows [a, b) with b <= a * (1 + 0.9 (q0 - 1)), so all
// factors of a window's composites are already known; window composites std::sort-ed.
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <ctime>
#include <string>
typedef unsigned __int128 u128;
typedef __int128 i128;
static const int F = 92;
static u128 ONE, TFX;              // 2^F, round(t 2^F) (|err| <= 1/2 ulp)
static double TD, RHO, ULP, XD;
static u128 XFX;

static inline u128 mulshift(u128 a, u128 b) {          // floor(a b / 2^F)
  uint64_t a0 = (uint64_t)a, a1 = (uint64_t)(a >> 64), b0 = (uint64_t)b, b1 = (uint64_t)(b >> 64);
  u128 p00 = (u128)a0 * b0, p01 = (u128)a0 * b1, p10 = (u128)a1 * b0, p11 = (u128)a1 * b1;
  u128 mid = p01 + p10; u128 midc = (mid < p01) ? ((u128)1 << 64) : 0;
  u128 lo = p00 + (mid << 64); u128 c1 = (lo < p00) ? 1 : 0;
  u128 hi = p11 + (mid >> 64) + midc + c1;
  return (hi << (128 - F)) | (lo >> F);
}
static inline double toD(u128 v) { return (double)(v >> 40) * ldexp(1.0, 40 - F); }
static inline u128 lattice(uint64_t k) { return ONE + (((u128)(2 * k - 1) * TFX) >> 1); }
static inline double lattice_err(uint64_t k) { return (2.0 * k - 1.0) * 0.25 + 1.0; }
static u128 parse_u128(const char* s) { u128 v = 0; for (; *s; ++s) v = v * 10 + (u128)(*s - '0'); return v; }

struct Prefix { u128 N, C; double eN, eC; uint32_t cur; };
static std::vector<uint32_t> PK;   // low 32 bits of the lattice index of each stored g-prime (p <= X/q0)
static std::vector<size_t> WRAP;   // PK positions where the high part of k increments (k is increasing)
static inline uint64_t getk(size_t idx) { uint64_t h = 0; for (size_t w : WRAP) h += (idx >= w); return (h << 32) | PK[idx]; }
static std::vector<Prefix> PRE;

// running state
static uint64_t cnt = 1, npr = 0;  // g-integers placed so far (1 included), g-primes so far
static double supE = 0.0, supEx = 1.0;
static double thS = 0.0, thC = 0.0; // theta_P, Neumaier-compensated
static long long flags = 0, ncmp = 0, flagsB = 0, nties = 0;
static double minratio = 1e300, minabs = 1e300, minrel = 1e300;
static FILE* dumpf = nullptr; static double dumpX = 0;
static std::vector<double> dumpbuf;
// checkpoints
static std::vector<double> CPX; static std::vector<u128> CPF; static size_t cp = 0;
struct Row { double x; uint64_t N, pi; double supE, supEx, theta; };
static std::vector<Row> rows;

static int NC = 0, J = 30; static std::vector<double> CS, CT, CL;      // centers sigma, t, lambda
static std::vector<double> LR, LI, GR, GI, KR, KI;                      // local, global, compensation
static FILE* momf = nullptr;
static inline void neu(double& s, double& c, double v) { double t = s + v; if (fabs(s) >= fabs(v)) c += (s - t) + v; else c += (v - t) + s; s = t; }
static void flushmom() { for (size_t q = 0; q < LR.size(); ++q) { neu(GR[q], KR[q], LR[q]); neu(GI[q], KI[q], LI[q]); LR[q] = LI[q] = 0; } }
static inline void addmom(double ln) {
  for (int c = 0; c < NC; ++c) {
    double a = exp(-CS[c] * ln), wr = a, wi = 0, f = CL[c] * ln;
    if (CT[c] != 0) { wr = a * cos(CT[c] * ln); wi = -a * sin(CT[c] * ln); }
    double* lr = &LR[c * J]; double* li = &LI[c * J];
    for (int j = 0; j < J; ++j) { lr[j] += wr; li[j] += wi; double g = f / (j + 1); wr *= g; wi *= g; }
  }
}
static void snapmom(double x, uint64_t N) {
  if (!momf) return; flushmom();
  for (int c = 0; c < NC; ++c) for (int j = 0; j < J; ++j)
    fprintf(momf, "%.0f %llu %d %.17g %.17g %.6g %d %.17e %.17e\n", x, (unsigned long long)N, c, CS[c], CT[c], CL[c], j,
            GR[c * J + j] + KR[c * J + j], GI[c * J + j] + KI[c * J + j]);
  fflush(momf);
}
// time-weighted statistics of E per checkpoint window (x_{c-1}, x_c]: segment endpoints binned in cells of 1/16
static bool STATS = false; static const int HC = 8192; static const double HMIN = -1.0, HWID = 1.0 / 16;
static std::vector<double> hS, hSE, hE, hEE; static double wInt = 0, wLen = 0, wMax = -1e9, prevX = 1.0, prevE = 0.0;
static FILE* statf = nullptr;
static inline int cell(double e) { int c = (int)floor((e - HMIN) / HWID); return c < 0 ? 0 : (c >= HC ? HC - 1 : c); }
static inline void segment(double x0, double e0, double x1) {   // E falls linearly from e0 at x0 to e0 - rho (x1 - x0)
  double len = x1 - x0; if (len <= 0) return; double e1 = e0 - RHO * len;
  wInt += 0.5 * (e0 + e1) * len; wLen += len; if (e0 > wMax) wMax = e0;
  int a = cell(e0), b = cell(e1); hS[a] += 1; hSE[a] += e0; hE[b] += 1; hEE[b] += e1;
}
static void closewin(double x) {                                 // report the window ending at x, then reset
  if (!statf) return;
  // time with E > y (y a cell boundary): (1/rho) [sum_{starts>y} (e0 - y) - sum_{ends>y} (e1 - y)]
  std::vector<double> G(HC + 1, 0.0); double cs = 0, ss = 0, ce = 0, se = 0;
  for (int c = HC - 1; c >= 0; --c) { cs += hS[c]; ss += hSE[c]; ce += hE[c]; se += hEE[c];
    double y = HMIN + c * HWID; G[c] = ((ss - cs * y) - (se - ce * y)) / RHO / wLen; }
  auto q = [&](double p) { for (int c = 0; c < HC; ++c) if (G[c] <= 1 - p) return HMIN + c * HWID; return 999.0; };
  double sx = 0, sy = 0, sxx = 0, sxy = 0; int n = 0;            // log P(E > y) = a - lam y on 1e-1 > P > 1e-4
  for (int c = 0; c < HC; ++c) if (G[c] < 1e-1 && G[c] > 1e-4) { double y = HMIN + c * HWID, l = log(G[c]); sx += y; sy += l; sxx += y * y; sxy += y * l; n++; }
  double lam = n > 2 ? -(n * sxy - sx * sy) / (n * sxx - sx * sx) : 0;
  fprintf(statf, "%.6e len=%.6e meanE=%.4f q50=%.3f q90=%.3f q99=%.3f q999=%.3f maxE=%.3f lam=%.4f lam*log(xc)=%.3f\n",
          x, wLen, wInt / wLen, q(0.5), q(0.9), q(0.99), q(0.999), wMax, lam, lam * log(x / sqrt(sqrt(10.0))));
  fflush(statf);
  std::fill(hS.begin(), hS.end(), 0); std::fill(hSE.begin(), hSE.end(), 0); std::fill(hE.begin(), hE.end(), 0); std::fill(hEE.begin(), hEE.end(), 0);
  wInt = wLen = 0; wMax = -1e9;
}
static inline void addtheta(double v) {
  double t = thS + v;
  if (fabs(thS) >= fabs(v)) thC += (thS - t) + v; else thC += (v - t) + thS;
  thS = t;
}
static void flushdump() { if (dumpf && !dumpbuf.empty()) { fwrite(dumpbuf.data(), 8, dumpbuf.size(), dumpf); dumpbuf.clear(); } }

static inline void emit(u128 v, bool isprime) {
  while (cp < CPF.size() && v >= CPF[cp]) {
    if (STATS) { segment(prevX, prevE, CPX[cp]); prevE -= RHO * (CPX[cp] - prevX); prevX = CPX[cp]; closewin(CPX[cp]); }
    snapmom(CPX[cp], cnt); rows.push_back({CPX[cp], cnt, npr, supE, supEx, thS + thC}); cp++;
  }
  uint64_t j = cnt;                                   // 0-based index of this g-integer
  i128 diff = (i128)(ONE + (u128)j * TFX) - (i128)v;  // (1 + j t - n) 2^F
  double E = RHO * ((double)diff * ULP);              // E(n_j) = j - rho (n_j - 1)
  double vd = toD(v);
  if (E > supE) { supE = E; supEx = vd; }
  if (STATS) { segment(prevX, prevE, vd); prevX = vd; prevE = E; }
  cnt++;
  if (dumpf && vd <= dumpX) { dumpbuf.push_back(vd); if (dumpbuf.size() >= (1u << 20)) flushdump(); }
  if (NC) { addmom(log(vd)); if ((cnt & 0xFFFFF) == 0) flushmom(); }
  if (isprime) {
    npr++; addtheta(log(vd));
    uint64_t k = j;
    if (vd <= XD / (1.0 + 0.5 * TD) * 1.000001) {
      while (WRAP.size() < (k >> 32)) WRAP.push_back(PK.size());
      PK.push_back((uint32_t)k);
    }
    if (vd * vd <= XD * (1 + 1e-9)) {
      Prefix P; P.N = v; P.eN = lattice_err(k); P.C = mulshift(v, TFX);
      P.eC = (0.5 * vd + TD * P.eN + 2.0) * (1 + 1e-9); P.cur = (uint32_t)(PK.size() - 1);
      PRE.push_back(P);
    }
  }
}

int main(int argc, char** argv) {
  if (argc < 6) { fprintf(stderr, "usage: s8o TFX_decimal t rho X W [dumpX dumpfile]\n"); return 1; }
  ONE = (u128)1 << F; ULP = ldexp(1.0, -F);
  TFX = parse_u128(argv[1]); TD = strtod(argv[2], 0); RHO = strtod(argv[3], 0);
  XD = strtod(argv[4], 0); double W = strtod(argv[5], 0);
  XFX = (u128)XD * ONE;                         // X is an integer
  if (argc >= 8) { dumpX = strtod(argv[6], 0); dumpf = fopen(argv[7], "wb"); }
  for (double d = 3; d <= log10(XD) + 1e-9; d += 0.5) {
    double x = (fmod(d, 1.0) == 0) ? pow(10, d) : floor(pow(10, d));
    CPX.push_back(x); CPF.push_back((u128)x * ONE);
  }
  if (const char* e = getenv("S8O_XCP")) {           // extra checkpoints, comma separated
    std::string str(e); size_t pos = 0;
    while (pos < str.size()) { size_t q = str.find(',', pos); if (q == std::string::npos) q = str.size();
      double x = strtod(str.substr(pos, q - pos).c_str(), 0); CPX.push_back(x); pos = q + 1; }
    std::sort(CPX.begin(), CPX.end()); CPF.clear(); for (double x : CPX) CPF.push_back((u128)x * ONE);
  }
  if (const char* e = getenv("S8O_J")) J = atoi(e);
  if (const char* e = getenv("S8O_STATS")) { STATS = true; statf = fopen(e, "w"); hS.assign(HC, 0); hSE = hS; hE = hS; hEE = hS; }
  if (const char* e = getenv("S8O_CENTERS")) {        // "sigma:t:lambda,sigma:t:lambda"
    std::string str(e); size_t pos = 0;
    while (pos < str.size()) { size_t q = str.find(',', pos); if (q == std::string::npos) q = str.size();
      double a1, a2, a3; sscanf(str.substr(pos, q - pos).c_str(), "%lf:%lf:%lf", &a1, &a2, &a3);
      CS.push_back(a1); CT.push_back(a2); CL.push_back(a3); NC++; pos = q + 1; }
    LR.assign(NC * J, 0); LI = LR; GR = LR; GI = LR; KR = LR; KI = LR;
    if (const char* f = getenv("S8O_MOM")) momf = fopen(f, "w");
    addmom(0.0);                                       // the g-integer 1
  }
  double q0 = 1.0 + 0.5 * TD, grow = 1.0 + 0.9 * (q0 - 1.0);
  { double y = XD / q0; PK.reserve((size_t)(1.6 * y / (TD * log(y)) + 1000)); }
  fprintf(stderr, "t=%.17g rho=%.17g X=%.6g q0=%.10f F=%d\n", TD, RHO, XD, q0, F);
  if (dumpf && 1.0 <= dumpX) dumpbuf.push_back(1.0);   // the g-integer 1 (cnt = 1 already)
  std::vector<u128> buf; std::vector<Prefix> newp;
  double a = 1.0; long nwin = 0; time_t t0 = time(0); double maxErrAll = 0;
  while (a < XD) {
    double bd = std::min(std::min(a * grow, a + W), XD);
    bd = floor(bd); if (bd <= a) bd = a + 1;   // integer window ends
    u128 bfx = (u128)bd * ONE;
    buf.clear(); newp.clear(); double maxErr = 0;
    for (size_t i = 0; i < PRE.size(); ++i) {
      Prefix& P = PRE[i];
      while (P.cur < PK.size()) {
        uint64_t k = getk(P.cur);
        u128 V = P.N + (((u128)(2 * k - 1) * P.C) >> 1);
        if (V >= bfx) break;
        double err = (P.eN + (k - 0.5) * P.eC + 1.0) * (1 + 1e-9);
        if (err > maxErr) maxErr = err;
        buf.push_back(V);
        double vd = toD(V), pd = 1.0 + (k - 0.5) * TD;
        if (vd * pd <= XD * (1 + 1e-9)) {
          Prefix Q; Q.N = V; Q.eN = err; Q.C = mulshift(V, TFX);
          Q.eC = (0.5 * vd + TD * err + 2.0) * (1 + 1e-9); Q.cur = P.cur; newp.push_back(Q);
        }
        P.cur++;
      }
    }
    for (auto& Q : newp) PRE.push_back(Q);
    std::sort(buf.begin(), buf.end());
    for (size_t q = 1; q < buf.size(); ++q) { u128 d = buf[q] - buf[q - 1]; if ((double)d <= 2.0 * maxErr) nties++; }
    if (maxErr > maxErrAll) maxErrAll = maxErr;
    size_t i = 0;
    while (true) {
      u128 L = lattice(cnt);
      if (i < buf.size()) {
        u128 c = buf[i];
        u128 d = c > L ? c - L : L - c;
        double dd = (double)d, bound = maxErr + lattice_err(cnt);
        ncmp++;
        if (dd <= bound) flags++;
        double r = dd / bound; if (r < minratio) minratio = r;
        double ab = dd * ULP; if (ab < minabs) minabs = ab;
        double rl = ab / toD(c); if (rl < minrel) minrel = rl;
        if (c < L) { emit(c, false); i++; continue; }
      }
      if (L >= bfx) break;
      if (i >= buf.size()) {   // implicit comparison with the next window's first composite (approx >= b)
        double dd = (double)(bfx - L), bound = 4.0 * std::max(maxErr, maxErrAll) + lattice_err(cnt);
        if (dd <= bound) flagsB++;
      }
      emit(L, true);
    }
    // drop prefixes whose next composite exceeds X
    size_t w = 0;
    for (size_t r = 0; r < PRE.size(); ++r) {
      Prefix& P = PRE[r]; bool dead = false;
      if (P.cur < PK.size()) {
        uint64_t k = getk(P.cur); u128 V = P.N + (((u128)(2 * k - 1) * P.C) >> 1);
        if (V > XFX) dead = true;
      } else if (toD(P.N) * bd > XD * 1.01) dead = true;   // every future g-prime is >= bd
      if (!dead) PRE[w++] = P;
    }
    PRE.resize(w);
    nwin++; a = bd;
    if (nwin % 50 == 0) fprintf(stderr, "win %ld a=%.6g cnt=%llu npr=%llu pre=%zu PK=%zu supE=%.4f flags=%lld t=%lds\n",
        nwin, a, (unsigned long long)cnt, (unsigned long long)npr, PRE.size(), PK.size(), supE, flags, (long)(time(0) - t0));
  }
  while (cp < CPF.size()) { snapmom(CPX[cp], cnt); rows.push_back({CPX[cp], cnt, npr, supE, supEx, thS + thC}); cp++; }
  if (momf) fclose(momf);
  flushdump(); if (dumpf) fclose(dumpf);
  // psi_P(x) = theta(x) + sum_{m>=2} theta(x^{1/m}) from the stored primes (all p <= sqrt X stored)
  printf("# s8o  t=%.17g rho=%.17g X=%.6g F=%d windows=%ld time=%lds\n", TD, RHO, XD, F, nwin, (long)(time(0) - t0));
  printf("# x  N(x)  pi_P(x)  supE(u<=x)  argsup  psi_P(x)-x\n");
  for (auto& R : rows) {
    double extra = 0, lx = log(R.x);
    for (size_t q = 0; q < PK.size(); ++q) {
      double p = 1.0 + (getk(q) - 0.5) * TD; if (p * p > R.x) break;
      double lp = log(p); extra += lp * (floor(lx / lp + 1e-12) - 1.0);
    }
    printf("%.0f %llu %llu %.10f %.6e %.6f\n", R.x, (unsigned long long)R.N, (unsigned long long)R.pi, R.supE, R.supEx, R.theta + extra - R.x);
  }
  printf("# certification: comparisons=%lld flags=%lld boundary_flags=%lld min(|diff|/errbound)=%.3e min|diff|=%.3e abs, %.3e rel; max composite err=%.3e ulps (=%.3e abs)\n",
         ncmp, flags, flagsB, minratio, minabs, minrel, maxErrAll, maxErrAll * ULP);
  printf("# composite pairs within 2x error bound (exact ties for rational t, near-ties otherwise): %lld\n", nties);
  printf("# final: N(X)=%llu pi_P(X)=%llu supE=%.10f at %.8e prefixes_left=%zu storedprimes=%zu\n",
         (unsigned long long)cnt, (unsigned long long)npr, supE, supEx, PRE.size(), PK.size());
  return 0;
}
