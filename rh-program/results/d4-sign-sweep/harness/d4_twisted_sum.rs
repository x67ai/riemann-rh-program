// d4_twisted_sum.rs -- D4 sign-channel sweep (results/d4-sign-sweep): the M6 twisted sum `results/c2-m6/verify/twisted_sum.rs`
// carried above the verified height.  Every change against the M6 source is marked `// D4:` and listed in
// d4-sweep-note.md section 2.  Unchanged from M6: the sieve, Lambda_DH, the double-double log, A(v), Neumaier, the JSON layout
// (new fields are appended).  Changes: (1) the height t is an integer-valued double and is printed EXACTLY (`t_exact`, the
// decimal expansion of the double; `t_bits`, its IEEE-754 bits); (2) the phase t*log n is formed as the EXACT product of t with
// the double-double log (two two_prods: four doubles, no rounding) and reduced mod 2 pi against 2 pi held as THREE doubles in
// two stages, so that the product and the reduction add nothing at the 10^-32 (t log n) scale -- the per-height self-test
// (--selftest N) measures the whole path against mpmath at 50 digits; (3) the phase line eps_phi(t) * l1 with eps_phi(t) =
// EPS_PHI_PER_T * t (BRIEF (i): 2.2e-31 * t, the M6 dd-log self-test; overridable by --eps-phi) is computed from the printed
// l1 norm and the point is flagged `refused` when it exceeds PHASE_LINE_ALLOWANCE = 1e-8; (4) --selftest N prints N
// pseudo-random n <= X with their dd log and dd reduced phase (xorshift64, --seed).
//
// M6 header follows.
// twisted_sum.rs -- M6 rung 1 (results/c2-m6): the prime-side (zeta) / coefficient-side (DH) twisted sum of the
// explicit formula for the test f_{t,L} = i (B_L)' e^{-itu}, g = f * f~ (separation-note.md section 0.1; Lean
// `Zeta23/ExplicitFormula.lean` 70-74 `literatureRHS`).
//
//   P(t, L) := sum_{n <= X} Lambda(n) n^{-1/2} (g(log n) + g(-log n)),   X = e^L,
//   g(x) = e^{-itx} a(x),  a(x) = L^{-3} A(x/L),  A(v) = int B'(w) B'(w - v) dw   (real, even, supp [-1, 1]),
//   so   P(t, L) = sum_{n <= X} Lambda(n) n^{-1/2} * 2 L^{-3} A(log n / L) * cos(t log n).
//
// B(v) = Z^{-1} exp(-1/(1 - 4 v^2)) on |v| < 1/2, Z = int exp(-1/(1-4v^2)) dv = 0.2219969080840397.
//
// Modes:  zeta  -- Lambda = von Mangoldt, from a segmented sieve of Eratosthenes (primes and prime powers);
//         dh    -- Lambda = Lambda_DH from the Dirichlet-convolution recursion a(n) log n = sum_{d|n} a(n/d) Lambda_DH(d)
//                  with a(n) = (1, kappa, -kappa, -1, 0) by n mod 5 (results/ccm-dh-test/dh.py; weilform.lambda_dh).
// Phase:  t*log n in double-double (own implementation: two-sum / two-prod with fma; log by a 257-entry table plus
//         the atanh series), reduced mod 2 pi in double-double; cos of the reduced phase.  A plain-double phase is
//         accumulated alongside so the phase-precision line of the error budget is MEASURED, not estimated.
// Summation: Neumaier-compensated per thread, threads joined by the same rule.
// A(v): tabulated on 20001 points of [0, 1] with A' (trapezoid, 4096 nodes; spectrally accurate for this
//         Gevrey-2 integrand), cubic Hermite interpolation; a `--direct` option evaluates A(log n / L) by quadrature
//         per term (small X only) to measure the interpolation error.
// No external crates (the machine's network is patchy); build:  rustc -O -C target-cpu=native twisted_sum.rs
//
// usage: d4_twisted_sum --mode zeta|dh --t <double as decimal string> --L <double> [--threads N] [--direct] [--out file.json]
//                       [--selftest N] [--seed S] [--eps-phi 2.2e-31]     (D4 additions)
use std::env;
use std::fs::File;
use std::io::Write;
use std::sync::Arc;
use std::thread;
use std::time::Instant;

// ------------------------------------------------------------------------------------------------ double-double
#[derive(Clone, Copy, Debug)]
struct DD { hi: f64, lo: f64 }

#[inline] fn two_sum(a: f64, b: f64) -> (f64, f64) { let s = a + b; let bb = s - a; (s, (a - (s - bb)) + (b - bb)) }
#[inline] fn quick_two_sum(a: f64, b: f64) -> (f64, f64) { let s = a + b; (s, b - (s - a)) }
#[inline] fn two_prod(a: f64, b: f64) -> (f64, f64) { let p = a * b; (p, a.mul_add(b, -p)) }

impl DD {
    #[inline] fn new(hi: f64, lo: f64) -> DD { DD { hi, lo } }
    #[inline] fn from(x: f64) -> DD { DD { hi: x, lo: 0.0 } }
    #[inline] fn add(self, o: DD) -> DD {
        let (s, e) = two_sum(self.hi, o.hi);
        let (t, f) = two_sum(self.lo, o.lo);
        let (s2, e2) = quick_two_sum(s, e + t);
        let (h, l) = quick_two_sum(s2, e2 + f);
        DD::new(h, l)
    }
    #[inline] fn neg(self) -> DD { DD::new(-self.hi, -self.lo) }
    #[inline] fn sub(self, o: DD) -> DD { self.add(o.neg()) }
    #[inline] fn mul(self, o: DD) -> DD {
        let (p, e) = two_prod(self.hi, o.hi);
        let e = e + (self.hi * o.lo + self.lo * o.hi);
        let (h, l) = quick_two_sum(p, e);
        DD::new(h, l)
    }
    #[inline] fn mul_f64(self, b: f64) -> DD {
        let (p, e) = two_prod(self.hi, b);
        let e = e + self.lo * b;
        let (h, l) = quick_two_sum(p, e);
        DD::new(h, l)
    }
    #[inline] fn div(self, o: DD) -> DD {
        let q1 = self.hi / o.hi;
        let r = self.sub(o.mul_f64(q1));
        let q2 = r.hi / o.hi;
        let r2 = r.sub(o.mul_f64(q2));
        let q3 = r2.hi / o.hi;
        let (h, l) = quick_two_sum(q1, q2);
        DD::new(h, l).add(DD::from(q3))
    }
    #[inline] fn to_f64(self) -> f64 { self.hi + self.lo }
}

// log(1 + r) for |r| <= 1 (used for the table and for ln 2), by 2 atanh(z), z = r/(2+r)
fn dd_log1p_series(r: DD, nterms: usize) -> DD {
    let z = r.div(DD::from(2.0).add(r));
    let z2 = z.mul(z);
    let mut term = z;           // z^{2j+1}
    let mut acc = DD::from(0.0);
    for j in 0..nterms {
        acc = acc.add(term.div(DD::from((2 * j + 1) as f64)));
        term = term.mul(z2);
    }
    acc.mul_f64(2.0)
}

struct LogTab { ln2: DD, logm0: Vec<DD>, inv_m0: Vec<DD> }

fn build_logtab() -> LogTab {
    let ln2 = dd_log1p_series(DD::from(1.0), 40);              // z = 1/3, 3^{-80} ~ 1e-38
    let mut logm0 = Vec::with_capacity(257);
    let mut inv_m0 = Vec::with_capacity(257);
    for i in 0..=256usize {
        let m0 = 1.0 + (i as f64) / 256.0;                       // exact
        logm0.push(dd_log1p_series(DD::from(m0 - 1.0), 40));     // z <= 1/3
        inv_m0.push(DD::from(1.0).div(DD::from(m0)));
    }
    LogTab { ln2, logm0, inv_m0 }
}

// natural log of a positive integer n < 2^53 in double-double
#[inline]
fn dd_log_u64(n: u64, tab: &LogTab) -> DD {
    let nf = n as f64;
    let k = 63 - n.leading_zeros() as i32;                       // 2^k <= n < 2^{k+1}
    let m = nf / f64::powi(2.0, k);                              // exact scaling, m in [1, 2)
    let idx = ((m - 1.0) * 256.0).floor() as usize;
    let idx = if idx > 256 { 256 } else { idx };
    let m0 = 1.0 + (idx as f64) / 256.0;
    let d = m - m0;                                              // exact (same binade, m0 has <= 8 fraction bits)
    let r = tab.inv_m0[idx].mul_f64(d);                          // r = (m - m0)/m0, |r| <= 1/256
    // log(1+r) = 2 atanh(z), z = r/(2+r), |z| <= 1/512: 7 terms give < 1e-33 relative
    let z = r.div(DD::from(2.0).add(r));
    let z2 = z.mul(z);
    let mut term = z;
    let mut acc = DD::from(0.0);
    for j in 0..7usize {
        acc = acc.add(term.div(DD::from((2 * j + 1) as f64)));
        term = term.mul(z2);
    }
    let log1pr = acc.mul_f64(2.0);
    tab.ln2.mul_f64(k as f64).add(tab.logm0[idx]).add(log1pr)
}

// D4: 2 pi as three doubles (c0 + c1 + c2 = 2 pi to 2.2e-49; mpmath at 60 digits, harness/_run.log) and 1/(2 pi)
const TWOPI_0: f64 = 6.283185307179586;
const TWOPI_1: f64 = 2.4492935982947064e-16;
const TWOPI_2: f64 = -5.989539619436679e-33;
const INV_TWOPI: f64 = 0.15915494309189535;
// M6 kept 2 pi in double-double and formed t*logn by DD::mul_f64 (one rounding of lo*t) then subtracted k*2pi in dd: both steps
// carry a 2^-106 (t log n) error, i.e. 3e-11 rad at t = 1e20 -- the same size as the allowance.  D4 replaces them:
const EPS_PHI_PER_T: f64 = 2.2e-31;         // D4: BRIEF (i): per-term phase error eps_phi(t) = 2.2e-31 * t (M6 dd-log self-test)
const PHASE_LINE_ALLOWANCE: f64 = 1e-8;     // D4: BRIEF (i): the phase line eps_phi * l1 must not exceed this

// D4: the reduced phase (t * logn) mod 2 pi in double-double, with the product formed EXACTLY and the reduction in two stages.
//   t * (hi + lo) = p + e + q + f exactly (two_prod twice; t and hi, lo are doubles, no rounding).
//   Stage 1: k = round(p / 2pi) (an integer-valued double, exact); k*c0 = m1 + m2 exactly (two_prod); r0 = p - m1 is exact by
//   Sterbenz (k*c0 lies within a factor 2 of p whenever k >= 1; for k = 0, m1 = 0);  then r = r0 - m2 + e + q + f - k*c1 - k*c2
//   summed in double-double from exact pieces of size <= ~2^19, so the rounding is ~2^19 * 2^-105 ~ 1e-26 rad.
//   Stage 2: k2 = round(r.hi / 2pi) (|k2| <= ~1e5, the slack of the double division in stage 1) and r -= k2 * (c0 + c1 + c2).
//   The only error left in the phase is the dd log's own (2.2e-31 absolute in M6's self-test) times t -- measured per height.
#[inline]
fn reduced_phase_dd(logn: DD, t: f64) -> DD {
    let (p, e) = two_prod(logn.hi, t);
    let (q, f) = two_prod(logn.lo, t);
    let k = (p * INV_TWOPI).round();
    let (m1, m2) = two_prod(k, TWOPI_0);
    let r0 = p - m1;
    let (n1, n2) = two_prod(k, TWOPI_1);
    let (o1, o2) = two_prod(k, TWOPI_2);
    let mut r = DD::from(r0).sub(DD::from(m2)).add(DD::from(e)).add(DD::from(q)).add(DD::from(f))
        .sub(DD::new(n1, n2)).sub(DD::new(o1, o2));
    let k2 = (r.hi * INV_TWOPI).round();
    if k2 != 0.0 {
        let (a1, a2) = two_prod(k2, TWOPI_0);
        let (b1, b2) = two_prod(k2, TWOPI_1);
        r = r.sub(DD::new(a1, a2)).sub(DD::new(b1, b2)).sub(DD::from(k2 * TWOPI_2));
    }
    r
}

// cos(t * logn) with the phase in double-double, reduced mod 2 pi   (D4: via reduced_phase_dd)
#[inline]
fn cos_phase_dd(logn: DD, t: f64) -> f64 {
    let red = reduced_phase_dd(logn, t);
    // cos(hi + lo) = cos hi - lo sin hi + O(lo^2)
    red.hi.cos() - red.lo * red.hi.sin()
}

// D4: exact decimal expansion of an integer-valued double (every sweep height is one); otherwise the shortest round-trip form
fn exact_double_str(t: f64) -> String {
    if t.fract() == 0.0 && t.abs() < 1.0e38 { format!("{}", t as i128) } else { format!("{:?}", t) }
}

// D4: xorshift64 for the self-test's pseudo-random n (deterministic; seed printed)
fn xorshift64(s: &mut u64) -> u64 { let mut x = *s; x ^= x << 13; x ^= x >> 7; x ^= x << 17; *s = x; x }

// ------------------------------------------------------------------------------------------------ the bump and A(v)
#[inline] fn braw(w: f64) -> f64 { if w.abs() >= 0.5 { 0.0 } else { (-1.0 / (1.0 - 4.0 * w * w)).exp() } }
#[inline] fn braw_d1(w: f64) -> f64 {          // d/dw exp(phi), phi = -1/(1-4w^2), phi' = -8w/(1-4w^2)^2
    if w.abs() >= 0.5 { 0.0 } else { let q = 1.0 - 4.0 * w * w; braw(w) * (-8.0 * w / (q * q)) }
}
#[inline] fn braw_d2(w: f64) -> f64 {          // exp(phi) (phi'' + phi'^2), phi'' = -8/q^2 - 128 w^2/q^3
    if w.abs() >= 0.5 { 0.0 } else {
        let q = 1.0 - 4.0 * w * w; let p1 = -8.0 * w / (q * q); let p2 = -8.0 / (q * q) - 128.0 * w * w / (q * q * q);
        braw(w) * (p2 + p1 * p1)
    }
}

const M_NODES: usize = 4096;    // trapezoid nodes on (-1/2, 1/2)
const N_A: usize = 20000;       // A tabulated at v_i = i/N_A, i = 0..N_A

struct ATab { z: f64, a: Vec<f64>, ap: Vec<f64> }

fn z_trap() -> f64 { let mut s = 0.0; for j in 1..M_NODES { s += braw(j as f64 / M_NODES as f64 - 0.5); } s / M_NODES as f64 }

// A_raw(v) = int Braw'(w) Braw'(w - v) dw  and  A_raw'(v) = int Braw''(w) Braw'(w - v) dw, trapezoid with M nodes
fn a_raw_quad(v: f64, m: usize) -> (f64, f64) {
    let mut s = 0.0; let mut sp = 0.0;
    let h = 1.0 / m as f64;
    for j in 1..m {
        let w = j as f64 * h - 0.5;
        let b1 = braw_d1(w - v);
        if b1 != 0.0 { s += braw_d1(w) * b1; sp += braw_d2(w) * b1; }
    }
    (s * h, sp * h)
}

fn build_atab() -> ATab {
    let z = z_trap();
    let mut a = vec![0.0; N_A + 1]; let mut ap = vec![0.0; N_A + 1];
    for i in 0..=N_A {
        let v = i as f64 / N_A as f64;
        let (s, sp) = a_raw_quad(v, M_NODES);
        a[i] = s / (z * z); ap[i] = sp / (z * z);
    }
    ATab { z, a, ap }
}

#[inline]
fn a_interp(tab: &ATab, v: f64) -> f64 {        // A(v) for v in [0, 1] (0 beyond) by cubic Hermite
    let v = v.abs();
    if v >= 1.0 { return 0.0; }
    let x = v * N_A as f64;
    let i = x.floor() as usize;
    let i = if i >= N_A { N_A - 1 } else { i };
    let s = x - i as f64;
    let h = 1.0 / N_A as f64;
    let (p0, p1, m0, m1) = (tab.a[i], tab.a[i + 1], tab.ap[i] * h, tab.ap[i + 1] * h);
    let s2 = s * s; let s3 = s2 * s;
    let h00 = 2.0 * s3 - 3.0 * s2 + 1.0; let h10 = s3 - 2.0 * s2 + s; let h01 = -2.0 * s3 + 3.0 * s2; let h11 = s3 - s2;
    h00 * p0 + h10 * m0 + h01 * p1 + h11 * m1
}

// ------------------------------------------------------------------------------------------------ Neumaier sum
#[derive(Clone, Copy)]
struct Neu { s: f64, c: f64 }
impl Neu {
    fn new() -> Neu { Neu { s: 0.0, c: 0.0 } }
    #[inline] fn add(&mut self, x: f64) {
        let t = self.s + x;
        if self.s.abs() >= x.abs() { self.c += (self.s - t) + x; } else { self.c += (x - t) + self.s; }
        self.s = t;
    }
    fn get(&self) -> f64 { self.s + self.c }
    fn merge(&mut self, o: &Neu) { self.add(o.s); self.add(o.c); }
}

// ------------------------------------------------------------------------------------------------ accumulators
#[derive(Clone)]
struct Acc {
    p_dd: Neu, p_double: Neu, l1: Neu, l1_primes: Neu, l1_pp: Neu, lam_sqrt: Neu, // sum Lambda(n) n^{-1/2}
    n_terms: u64, n_primes: u64, n_pp: u64,
    neg_pos: (u64, u64),                  // DH: count of negative / positive Lambda values used
    small: Vec<(u64, u32, f64)>,          // (p, k, w_{p^k}) for p^k with p <= sqrt(X) (zeta: exact Kronecker sup)
}
impl Acc {
    fn new() -> Acc { Acc { p_dd: Neu::new(), p_double: Neu::new(), l1: Neu::new(), l1_primes: Neu::new(), l1_pp: Neu::new(),
        lam_sqrt: Neu::new(), n_terms: 0, n_primes: 0, n_pp: 0, neg_pos: (0, 0), small: Vec::new() } }
    fn merge(&mut self, o: &Acc) {
        self.p_dd.merge(&o.p_dd); self.p_double.merge(&o.p_double); self.l1.merge(&o.l1); self.l1_primes.merge(&o.l1_primes);
        self.l1_pp.merge(&o.l1_pp); self.lam_sqrt.merge(&o.lam_sqrt);
        self.n_terms += o.n_terms; self.n_primes += o.n_primes; self.n_pp += o.n_pp;
        self.neg_pos.0 += o.neg_pos.0; self.neg_pos.1 += o.neg_pos.1;
        self.small.extend_from_slice(&o.small);
    }
}

struct Params { t: f64, l: f64, x: u64, direct: bool, sqrtx: u64, sieve_only: bool }

// one term: n, Lambda(n); returns nothing, accumulates
#[inline]
fn add_term(acc: &mut Acc, n: u64, lam: f64, is_prime: bool, k: u32, p: u64, pr: &Params, atab: &ATab, ltab: &LogTab) {
    if pr.sieve_only { acc.n_terms += 1; if is_prime { acc.n_primes += 1; } else { acc.n_pp += 1; } acc.lam_sqrt.add(lam / (n as f64).sqrt()); return; }
    let logn = dd_log_u64(n, ltab);
    let v = logn.to_f64() / pr.l;
    let a = if pr.direct { let (s, _) = a_raw_quad(v.abs(), M_NODES); if v.abs() >= 1.0 { 0.0 } else { s / (atab.z * atab.z) } } else { a_interp(atab, v) };
    let w = lam / (n as f64).sqrt() * 2.0 * a / (pr.l * pr.l * pr.l);   // coefficient w_n
    let c_dd = cos_phase_dd(logn, pr.t);
    let c_db = (pr.t * (n as f64).ln()).cos();
    acc.p_dd.add(w * c_dd); acc.p_double.add(w * c_db);
    acc.l1.add(w.abs()); acc.lam_sqrt.add(lam / (n as f64).sqrt());
    acc.n_terms += 1;
    if is_prime { acc.n_primes += 1; acc.l1_primes.add(w.abs()); } else { acc.n_pp += 1; acc.l1_pp.add(w.abs()); }
    if lam < 0.0 { acc.neg_pos.0 += 1; } else if lam > 0.0 { acc.neg_pos.1 += 1; }
    if p != 0 && p <= pr.sqrtx { acc.small.push((p, k, w)); }
}

// ------------------------------------------------------------------------------------------------ zeta: segmented sieve
fn base_primes(limit: u64) -> Vec<u64> {
    let n = limit as usize + 1;
    let mut s = vec![true; n]; s[0] = false; if n > 1 { s[1] = false; }
    let mut i = 2; while i * i < n { if s[i] { let mut j = i * i; while j < n { s[j] = false; j += i; } } i += 1; }
    (2..n).filter(|&i| s[i]).map(|i| i as u64).collect()
}

fn zeta_range(lo: u64, hi: u64, base: &[u64], pr: &Params, atab: &ATab, ltab: &LogTab) -> Acc {
    // primes in [lo, hi) by a segmented sieve (segment 1<<20), plus prime powers p^k in [lo, hi)
    let mut acc = Acc::new();
    const SEG: u64 = 1 << 20;
    let mut seg_lo = lo;
    let mut mark = vec![false; SEG as usize];
    while seg_lo < hi {
        let seg_hi = (seg_lo + SEG).min(hi);
        let len = (seg_hi - seg_lo) as usize;
        for m in mark.iter_mut().take(len) { *m = false; }
        for &p in base {
            if p * p >= seg_hi { break; }
            let mut j = ((seg_lo + p - 1) / p) * p; if j < p * p { j = p * p; }
            while j < seg_hi { mark[(j - seg_lo) as usize] = true; j += p; }
        }
        for i in 0..len {
            let n = seg_lo + i as u64;
            if n >= 2 && !mark[i] {
                let lp = (n as f64).ln();
                add_term(&mut acc, n, lp, true, 1, n, pr, atab, ltab);
            }
        }
        seg_lo = seg_hi;
    }
    // prime powers p^k (k >= 2) with lo <= p^k < hi: p <= sqrt(hi)
    for &p in base {
        if p * p >= hi { break; }
        let lp = (p as f64).ln();
        let mut pk = p * p; let mut k = 2u32;
        while pk < hi { if pk >= lo { add_term(&mut acc, pk, lp, false, k, p, pr, atab, ltab); } pk *= p; k += 1; }
    }
    acc
}

// ------------------------------------------------------------------------------------------------ DH: Lambda_DH
fn kappa() -> f64 { let s5 = 5f64.sqrt(); ((10.0 - 2.0 * s5).sqrt() - 2.0) / (s5 - 1.0) }

fn lambda_dh(x: u64) -> Vec<f64> {
    let kap = kappa();
    let a = [0.0, 1.0, kap, -kap, -1.0];       // a(n) by n mod 5
    let n = x as usize + 1;
    let mut lam = vec![0.0f64; n];
    for m in 2..n { lam[m] = a[m % 5] * (m as f64).ln(); }
    for d in 2..n {
        let ld = lam[d];
        if ld == 0.0 { continue; }
        let mut j = 2usize; let mut m = 2 * d;
        while m < n {
            let aj = a[j % 5];
            if aj != 0.0 { lam[m] -= aj * ld; }
            j += 1; m += d;
        }
    }
    lam
}

fn dh_range(lo: u64, hi: u64, lam: &[f64], pr: &Params, atab: &ATab, ltab: &LogTab) -> Acc {
    let mut acc = Acc::new();
    for n in lo.max(2)..hi {
        let l = lam[n as usize];
        if l != 0.0 { add_term(&mut acc, n, l, false, 0, 0, pr, atab, ltab); }
    }
    acc
}

// ------------------------------------------------------------------------------------------------ main
fn main() {
    let args: Vec<String> = env::args().collect();
    let mut mode = String::from("zeta"); let mut t_str = String::from("85.69934848537759"); let mut l = 10.0f64;
    let mut threads = 8usize; let mut direct = false; let mut sieve_only = false; let mut out = String::from("out.json");
    let mut selftest = 0usize; let mut seed: u64 = 20260925; let mut eps_phi_per_t = EPS_PHI_PER_T;   // D4
    let mut i = 1;
    while i < args.len() {
        match args[i].as_str() {
            "--mode" => { mode = args[i + 1].clone(); i += 2; }
            "--t" => { t_str = args[i + 1].clone(); i += 2; }
            "--L" => { l = args[i + 1].parse().unwrap(); i += 2; }
            "--threads" => { threads = args[i + 1].parse().unwrap(); i += 2; }
            "--direct" => { direct = true; i += 1; }
            "--sieve-only" => { sieve_only = true; i += 1; }
            "--out" => { out = args[i + 1].clone(); i += 2; }
            "--selftest" => { selftest = args[i + 1].parse().unwrap(); i += 2; }        // D4
            "--seed" => { seed = args[i + 1].parse().unwrap(); i += 2; }                // D4
            "--eps-phi" => { eps_phi_per_t = args[i + 1].parse().unwrap(); i += 2; }    // D4
            _ => { eprintln!("unknown arg {}", args[i]); std::process::exit(2); }
        }
    }
    let t: f64 = t_str.parse().unwrap();
    let t_exact = exact_double_str(t);            // D4: the height as the exact decimal expansion of the double used
    let x = l.exp().floor() as u64;               // terms n <= X = floor(e^L); a(log n) = 0 for n >= e^L anyway
    let t0 = Instant::now();
    eprintln!("[{}] mode={} t={:.17e} t_exact={} t_bits={:#018x} L={} X={} threads={} direct={}", now(), mode, t, t_exact, t.to_bits(), l, x, threads, direct);

    let ltab = Arc::new(build_logtab());
    // self-test of the double-double log: print (hi, lo) of ln n for a few n; verify_dd_log.py compares them with mpmath
    let mut log_selftest: Vec<(u64, f64, f64)> = Vec::new();
    for &n in &[2u64, 3, 7, 10, 65537, 1000003, 485165195, 999999937] { let v = dd_log_u64(n, &ltab); log_selftest.push((n, v.hi, v.lo)); }
    log_selftest.push((0, ltab.ln2.hi, ltab.ln2.lo));
    eprintln!("[{}] dd-log values (n, hi, lo): {:?}", now(), log_selftest);

    let atab = Arc::new(build_atab());
    let t_atab = t0.elapsed().as_secs_f64();
    // A-table checks: A(0) = ||B'||_2^2 (record 16.62196535); A vs a finer quadrature at three points; A' vs finite differences
    let (a0_8192, _) = a_raw_quad(0.0, 8192); let a0_8192 = a0_8192 / (atab.z * atab.z);
    let mut a_check = Vec::new();
    for &v in &[0.1234567f64, 0.5, 0.87654321] {
        let (s, _) = a_raw_quad(v, 8192); let exact = s / (atab.z * atab.z);
        a_check.push((v, a_interp(&atab, v), exact, a_interp(&atab, v) - exact));
    }
    let hfd = 1e-4; let ap_fd = (a_interp(&atab, 0.3 + hfd) - a_interp(&atab, 0.3 - hfd)) / (2.0 * hfd);
    let ap_tab = { let (_, sp) = a_raw_quad(0.3, M_NODES); sp / (atab.z * atab.z) };
    eprintln!("[{}] A-table built in {:.2}s: Z = {:.16}, A(0) = {:.12} (M=8192: {:.12}); interp-vs-quad {:?}; A'(0.3) table {:.9} vs FD {:.9}",
        now(), t_atab, atab.z, atab.a[0], a0_8192, a_check, ap_tab, ap_fd);

    let sqrtx = (x as f64).sqrt().floor() as u64 + 1;
    let pr = Arc::new(Params { t, l, x, direct, sqrtx, sieve_only });
    let mut acc = Acc::new();
    let t_sieve;
    let mut lam_witness: Vec<(u64, f64)> = Vec::new();
    let t1 = Instant::now();
    if mode == "zeta" {
        let base = Arc::new(base_primes((x as f64).sqrt() as u64 + 2));
        t_sieve = 0.0;
        let chunk = (x + 1) / threads as u64 + 1;
        let mut handles = Vec::new();
        for th in 0..threads {
            let lo = 2u64.max(th as u64 * chunk); let hi = ((th as u64 + 1) * chunk).min(x + 1);
            let (base, pr, atab, ltab) = (base.clone(), pr.clone(), atab.clone(), ltab.clone());
            handles.push(thread::spawn(move || if lo < hi { zeta_range(lo, hi, &base, &pr, &atab, &ltab) } else { Acc::new() }));
        }
        for h in handles { acc.merge(&h.join().unwrap()); }
    } else {
        let ts = Instant::now();
        let lam = Arc::new(lambda_dh(x));
        t_sieve = ts.elapsed().as_secs_f64();
        for &n in &[2u64, 3, 4, 5, 6, 7, 8, 9, 10, 12, 25] { if n <= x { lam_witness.push((n, lam[n as usize])); } }
        eprintln!("[{}] Lambda_DH recursion to X = {} in {:.1}s; witnesses (n, Lambda_DH(n)): {:?}", now(), x, t_sieve, lam_witness);
        let chunk = (x + 1) / threads as u64 + 1;
        let mut handles = Vec::new();
        for th in 0..threads {
            let lo = 2u64.max(th as u64 * chunk); let hi = ((th as u64 + 1) * chunk).min(x + 1);
            let (lam, pr, atab, ltab) = (lam.clone(), pr.clone(), atab.clone(), ltab.clone());
            handles.push(thread::spawn(move || if lo < hi { dh_range(lo, hi, &lam, &pr, &atab, &ltab) } else { Acc::new() }));
        }
        for h in handles { acc.merge(&h.join().unwrap()); }
    }
    let t_sum = t1.elapsed().as_secs_f64() - t_sieve;
    let a0 = atab.a[0] / (l * l * l);
    let trivial = 4.0 * (x as f64).sqrt() * a0;
    eprintln!("[{}] done: terms={} (primes {}, prime powers {}) P_dd = {:.15e}  P_double = {:.15e}  diff = {:.3e}  l1 = {:.6e}  sum Lambda/sqrt n = {:.6e}  sum time {:.2}s ({:.1} ns/term/thread-count-{})",
        now(), acc.n_terms, acc.n_primes, acc.n_pp, acc.p_dd.get(), acc.p_double.get(), acc.p_dd.get() - acc.p_double.get(), acc.l1.get(), acc.lam_sqrt.get(), t_sum, t_sum * 1e9 / acc.n_terms.max(1) as f64, threads);
    // D4: the phase line eps_phi(t) * l1 and the refusal flag (BRIEF (i)); |cos(x + eps) - cos x| <= |eps| per term
    let eps_phi = eps_phi_per_t * t.abs();
    let phase_line = eps_phi * acc.l1.get();
    let refused = phase_line > PHASE_LINE_ALLOWANCE;
    eprintln!("[{}] phase line: eps_phi = {:.3e} rad/term (eps_phi_per_t {:.2e}), l1 = {:.6e}, line = {:.3e} against allowance {:.0e} -> {}",
        now(), eps_phi, eps_phi_per_t, acc.l1.get(), phase_line, PHASE_LINE_ALLOWANCE, if refused { "REFUSED" } else { "accepted" });
    // D4: per-height phase self-test: N pseudo-random n in [2, X]; (n, log hi, log lo, reduced-phase hi, lo, cos) for mpmath
    let mut st_rows: Vec<String> = Vec::new();
    if selftest > 0 {
        let mut s = seed | 1;
        for _ in 0..selftest {
            let r = xorshift64(&mut s);
            let n = 2 + (r % (x.max(3) - 1));
            let lg = dd_log_u64(n, &ltab);
            let red = reduced_phase_dd(lg, t);
            let c = red.hi.cos() - red.lo * red.hi.sin();
            st_rows.push(format!("[{},{:.17e},{:.17e},{:.17e},{:.17e},{:.17e}]", n, lg.hi, lg.lo, red.hi, red.lo, c));
        }
        eprintln!("[{}] self-test: {} random n <= {} written (seed {})", now(), selftest, x, seed);
    }
    acc.small.sort_by(|a, b| (a.0, a.1).cmp(&(b.0, b.1)));
    let mut f = File::create(&out).unwrap();
    let small_json: Vec<String> = acc.small.iter().map(|(p, k, w)| format!("[{},{},{:.17e}]", p, k, w)).collect();
    let wit_json: Vec<String> = lam_witness.iter().map(|(n, v)| format!("[{},{:.17e}]", n, v)).collect();
    writeln!(f, "{{\n \"mode\": \"{}\", \"t\": {:.17e}, \"t_str\": \"{}\", \"L\": {}, \"X\": {}, \"threads\": {}, \"direct\": {}, \"sieve_only\": {},", mode, t, t_str, l, x, threads, direct, sieve_only).unwrap();
    writeln!(f, " \"t_exact\": \"{}\", \"t_bits\": \"{:#018x}\", \"eps_phi_per_t\": {:.6e}, \"eps_phi\": {:.6e}, \"phase_line\": {:.6e}, \"phase_line_allowance\": {:.1e}, \"refused\": {},",
        t_exact, t.to_bits(), eps_phi_per_t, eps_phi, phase_line, PHASE_LINE_ALLOWANCE, refused).unwrap();   // D4
    writeln!(f, " \"selftest_seed\": {}, \"phase_selftest\": [{}],", seed, st_rows.join(",")).unwrap();   // D4
    writeln!(f, " \"n_terms\": {}, \"n_primes\": {}, \"n_prime_powers\": {}, \"n_lambda_negative\": {}, \"n_lambda_positive\": {},", acc.n_terms, acc.n_primes, acc.n_pp, acc.neg_pos.0, acc.neg_pos.1).unwrap();
    writeln!(f, " \"P_dd\": {:.17e}, \"P_double\": {:.17e}, \"P_dd_minus_P_double\": {:.6e},", acc.p_dd.get(), acc.p_double.get(), acc.p_dd.get() - acc.p_double.get()).unwrap();
    writeln!(f, " \"l1_norm\": {:.17e}, \"l1_primes\": {:.17e}, \"l1_prime_powers\": {:.17e}, \"sum_lambda_over_sqrt_n\": {:.17e},", acc.l1.get(), acc.l1_primes.get(), acc.l1_pp.get(), acc.lam_sqrt.get()).unwrap();
    writeln!(f, " \"a0\": {:.17e}, \"A0\": {:.17e}, \"trivial_bound_4sqrtX_a0\": {:.17e}, \"Z_trap\": {:.17e}, \"A0_M8192\": {:.17e},", a0, atab.a[0], trivial, atab.z, a0_8192).unwrap();
    let ac: Vec<String> = a_check.iter().map(|(v, ai, ex, d)| format!("[{},{:.17e},{:.17e},{:.3e}]", v, ai, ex, d)).collect();
    writeln!(f, " \"A_interp_check\": [{}], \"Aprime_check_0p3\": [{:.12e},{:.12e}],", ac.join(","), ap_tab, ap_fd).unwrap();
    let ls: Vec<String> = log_selftest.iter().map(|(n, h, l)| format!("[{},{:.17e},{:.17e}]", n, h, l)).collect();
    writeln!(f, " \"dd_log_values\": [{}],", ls.join(",")).unwrap();
    writeln!(f, " \"time_atab_s\": {:.3}, \"time_lambda_s\": {:.3}, \"time_sum_s\": {:.3}, \"ns_per_term_wall\": {:.3}, \"ns_per_term_per_thread\": {:.3},",
        t_atab, t_sieve, t_sum, t_sum * 1e9 / acc.n_terms.max(1) as f64, t_sum * 1e9 * threads as f64 / acc.n_terms.max(1) as f64).unwrap();
    writeln!(f, " \"lambda_dh_witnesses\": [{}],", wit_json.join(",")).unwrap();
    writeln!(f, " \"small_prime_powers\": [{}]\n}}", small_json.join(",")).unwrap();
    eprintln!("[{}] wrote {} ({:.1}s total)", now(), out, t0.elapsed().as_secs_f64());
}

fn now() -> String {
    let d = std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).unwrap().as_secs();
    format!("unix {}", d)
}
