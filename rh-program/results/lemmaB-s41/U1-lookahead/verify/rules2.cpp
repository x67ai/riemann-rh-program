// U1-lookahead (Session 41): block generator for S8-type placement rules.
// Blocks [B, p1*B): every factor of a composite in the block is < B, so the block's composites are known before its
// primes are placed (charter §2(d)).  Each composite n = q*m is emitted once, q = the factor of LARGEST INDEX.
// Bookkeeping: a prime is counted at its deficit time x* (first x with T(x) - Nbook(x) = tau); its ACTUAL position
// a in [max(B, x* - W), x*] is chosen by the rule.  Actual N >= bookkeeping N, so E(x-) >= -tau for every rule.
// Usage: rules RHO X RULE TAU [W K J H]   RULE = greedy | early (a = x* - W) | look (anti-clustering, see pick())
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
static double rho, X, tau, W = 0, H = 2.0; static int K = 1, J = 0; static char rule[16];
static vector<double> G; static vector<int> Lx;          // sorted g-integers < B, largest prime index
static vector<double> P;                                   // prime positions by index
static vector<double> fut;                                 // known g-integers in [Bh, Bh*p_J) (for look-ahead)
static long cnt(const vector<double>& v, double a, double b) {
  return lower_bound(v.begin(), v.end(), b) - lower_bound(v.begin(), v.end(), a); }
// --- rules2 additions: the Moebius-corrected template F_c(u) = sum_k mu(k) Pi_c(u^{1/k})/k (s41 NOTE §2), for open-loop rules
static vector<double> PcTab; static const double hW = 2e-5;            // Pi_c(e^w) on w = 0, hW, 2hW, ...
static double Pic(double u) { if (u <= 1) return 0; double w = log(u) / hW; size_t i = (size_t)w; if (i + 1 >= PcTab.size()) i = PcTab.size() - 2;
  double f = w - i; return PcTab[i] * (1 - f) + PcTab[i + 1] * f; }
static void tabPc(double Xmax) { size_t n = (size_t)(log(Xmax * 4) / hW) + 3; PcTab.assign(n, 0.0);
  auto g = [](double w) { return w < 1e-12 ? rho : (1 - exp(-rho * w)) * exp(w) / w; };
  for (size_t i = 1; i < n; i++) { double a = (i - 1) * hW; PcTab[i] = PcTab[i - 1] + hW / 6 * (g(a) + 4 * g(a + hW / 2) + g(a + hW)); } }
static const int MU[] = {0, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, -1, 1, 1, 0, -1, 0, -1, 0, 1, 1, -1, 0, 0, 1, 0, 0, -1, -1, -1, 0, 1, 1, 1, 0, -1, 1, 1, 0, -1};
static double Fc(double u) { double s = 0; for (int k = 1; k <= 40; k++) { if (!MU[k]) continue; double v = pow(u, 1.0 / k); if (v <= 1.0000001) break; s += MU[k] * Pic(v) / k; } return s; }
static double FcInv(double y, double lo, double hi) { for (int it = 0; it < 100; it++) { double m = 0.5 * (lo + hi); if (Fc(m) < y) lo = m; else hi = m; } return 0.5 * (lo + hi); }
static double lam = 1.0; static unsigned long long rs = 88172645463325252ULL;
static double urand() { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return (rs >> 11) * (1.0 / 9007199254740992.0); }
static double pick(double xs, double B) {                  // the placement rule
  double lo = max(B, xs - W);
  if (!strcmp(rule, "greedy") || W <= 0) return xs;
  if (!strcmp(rule, "early")) return lo;
  double best = xs, bc = 1e300;                            // "look": minimise known load at the dilates p_j * a
  for (int k = 0; k < K; k++) {
    double a = (K == 1) ? xs : lo + (xs - lo) * k / (K - 1);
    double c = 0;
    for (int j = 0; j < J && j < (int)P.size(); j++) {
      double y = P[j] * a; c += cnt(fut, y - H, y + H) - rho * 2 * H; }
    c += 1e-9 * (xs - a);                                  // tie-break toward the deficit time
    if (c < bc) { bc = c; best = a; }
  }
  return best;
}
int main(int argc, char** argv) {
  rho = atof(argv[1]); X = atof(argv[2]); strncpy(rule, argv[3], 15); tau = atof(argv[4]);
  if (argc > 5) W = atof(argv[5]); if (argc > 6) K = atoi(argv[6]); if (argc > 7) J = atoi(argv[7]);
  if (argc > 8) H = atof(argv[8]);
  bool openloop = !strcmp(rule, "beatty") || !strcmp(rule, "poisson");
  if (openloop) { lam = W; W = 0; tabPc(X); if (argc > 6) rs += 7919ULL * K; }   // open-loop rules: argv[5] = lambda, argv[6] = seed
  double olnext = 0;                                       // next open-loop target value of lam*F_c (in units of primes)
  if (openloop) olnext = (!strcmp(rule, "beatty")) ? 0.5 : -log(1 - urand());
  double topLo = X / sqrt(10.0), supTop = -1e9, xTop = 0;
  double t = 1.0 / rho; double Nbook = 1;                  // N counts the unit 1
  double p1 = 1.0 + tau * t;                               // first deficit time (no early placement for p1)
  G = {1.0}; Lx = {-1}; P = {p1}; Nbook = 2;
  G.push_back(p1); Lx.push_back(0);
  double B = p1, supE = 0, infEm = 1e9, maxgap = 0, lastp = p1; long ncomp = 0;
  double dec = 10; double supdec = 0;
  printf("# rule=%s rho=%.10f X=%g tau=%g W=%g K=%d J=%d H=%g p1=%.6f\n", rule, rho, X, tau, W, K, J, H, p1);
  while (B < X) {
    double Bh = min(B * p1, X);
    vector<pair<double,int>> cv;
    for (int i = 0; i < (int)P.size(); i++) {
      double q = P[i]; if (q * p1 >= Bh) continue;
      size_t lo = lower_bound(G.begin(), G.end(), B / q * (1 - 1e-12)) - G.begin(), hi = lower_bound(G.begin(), G.end(), Bh / q * (1 + 1e-12)) - G.begin();   // widened: B/q may round past a g-integer on the boundary
      for (size_t k = lo; k < hi; k++) if (Lx[k] <= i) { double v = q * G[k]; if (v >= B && v < Bh) cv.push_back({v, i}); }
    }
    sort(cv.begin(), cv.end()); ncomp += cv.size();
    if (!strcmp(rule, "look") && W > 0) {                  // known future g-integers: products of known ones, in [Bh, Bh*pJ)
      fut.clear(); double top = Bh * P[min((size_t)J, P.size()) - 1] + H + 1;
      vector<double> kn(G.begin(), G.end()); for (auto& c : cv) kn.push_back(c.first); sort(kn.begin(), kn.end());
      for (int i = 0; i < (int)P.size() && P[i] < B; i++) {
        size_t lo = lower_bound(kn.begin(), kn.end(), Bh / P[i]) - kn.begin(), hi = lower_bound(kn.begin(), kn.end(), top / P[i]) - kn.begin();
        for (size_t k = lo; k < hi; k++) if (kn[k] > 1) fut.push_back(P[i] * kn[k]);   // with multiplicity: a load proxy
      }
      sort(fut.begin(), fut.end());
    }
    vector<pair<double,int>> np; size_t j = 0;
    auto olpos = [&](double prev) {                        // solve lam*F_c(u) = olnext by Newton from prev
      double u = max(prev, B) + 1.0; for (int it = 0; it < 30; it++) { double f = lam * Fc(u) - olnext, d = lam * (Fc(u + 1e-3) - Fc(u)) / 1e-3;
        double nu = u - f / max(d, 1e-12); if (nu <= 1.0) nu = 0.5 * (u + 1.0); if (fabs(nu - u) < 1e-9 * u) { u = nu; break; } u = nu; } return u; };
    double ol = openloop ? olpos(B) : 1e300;
    while (openloop && ol < B) { olnext += (!strcmp(rule, "beatty")) ? 1.0 : -log(1 - urand()); ol = olpos(ol); }
    while (true) {
      double xs = 1.0 + (Nbook - 1.0 + tau) / rho;         // T(xs) - Nbook = tau
      double nc = (j < cv.size()) ? cv[j].first : 1e300;
      if (min(nc, ol) <= xs && min(nc, ol) < Bh) {
        if (nc <= ol) { Nbook += 1; j++; continue; }
        P.push_back(ol); np.push_back({ol, (int)P.size() - 1}); Nbook += 1;   // open-loop prime
        olnext += (!strcmp(rule, "beatty")) ? 1.0 : -log(1 - urand()); ol = olpos(ol); continue;
      }
      if (xs >= Bh) break;
      double a = pick(xs, B); P.push_back(a); np.push_back({a, (int)P.size() - 1}); Nbook += 1;
    }
    vector<pair<double,int>> ev(cv); ev.insert(ev.end(), np.begin(), np.end()); sort(ev.begin(), ev.end());
    double N = cnt(G, 0, B + 0.0) ; N = G.size();           // actual N just below B
    for (auto& e : ev) {
      double T = rho * (e.first - 1.0) + 1.0;
      infEm = min(infEm, N - T); N += 1; double E = N - T; supE = max(supE, E);
      while (e.first > dec) { printf("x=%.3g supE=%.4f supE/log2=%.5f\n", dec, supdec, supdec / pow(log(dec), 2)); dec *= 10; }
      supdec = max(supdec, E);
      if (e.first >= topLo && E > supTop) { supTop = E; xTop = e.first; }
    }
    for (auto& p : np) { if (p.first - lastp > maxgap) maxgap = p.first - lastp; lastp = max(lastp, p.first); }
    vector<double> G2; vector<int> L2; G2.reserve(G.size() + ev.size()); L2.reserve(G.size() + ev.size());
    size_t a = 0, b = 0;
    while (a < G.size() || b < ev.size()) {
      if (b >= ev.size() || (a < G.size() && G[a] <= ev[b].first)) { G2.push_back(G[a]); L2.push_back(Lx[a]); a++; }
      else { G2.push_back(ev[b].first); L2.push_back(ev[b].second); b++; }
    }
    G.swap(G2); Lx.swap(L2); B = Bh;
  }
  printf("x=%.3g supE=%.4f supE/log2=%.5f\n", X, supdec, supdec / pow(log(X), 2));
  { // diagnostics on the top half-decade [X/sqrt(10), X]: anatomy of the top excursion, and Lemma M (smoothed prime density)
    vector<double> Ps(P); sort(Ps.begin(), Ps.end()); double l2 = pow(log(X), 2);
    auto it = upper_bound(Ps.begin(), Ps.end(), xTop); double pk = (it == Ps.begin()) ? 1 : *(it - 1), pk1 = (it == Ps.end()) ? X : *it;
    printf("EXC supTop=%.4f at x=%.6g rise_from_last_prime=%.2f (%.3f log^2X) gap=%.2f (%.3f log^2X)\n", supTop, xTop, xTop - pk, (xTop - pk) / l2, pk1 - pk, (pk1 - pk) / l2);
    for (int pw = 2; pw <= 4; pw++) for (double c : {0.25, 1.0}) { double L = c * pow(log(X), pw); if (L > (X - topLo) / 8) continue;
      double mn = 1e9, sm = 0; long nw = 0;
      for (double a = topLo; a + L <= X; a += L / 2) { long q = upper_bound(Ps.begin(), Ps.end(), a + L) - upper_bound(Ps.begin(), Ps.end(), a);
        double v = q * log(a + L / 2) / L; mn = min(mn, v); sm += v; nw++; }
      printf("LEMMA_M L=%.5g (%.2f log^%d X) windows=%ld min_pi(W)log/L=%.4f mean=%.4f\n", L, c, pw, nw, mn, sm / nw); }
  }
  printf("RESULT rule=%s tau=%g W=%g K=%d J=%d N=%zu pi=%zu comp=%ld supE=%.4f supE/log2X=%.5f infE(x-)=%.6f maxgap=%.2f\n",
         rule, tau, W, K, J, G.size(), P.size(), ncomp, supE, supE / pow(log(X), 2), infEm, maxgap);
}
