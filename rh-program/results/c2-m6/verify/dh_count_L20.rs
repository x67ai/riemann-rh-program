// dh_count_L20.rs -- M6 rung 1 fix pass (2026-09-17, after check-O.md §2 FIX-FIRST 2a): the TRUE number of n <= X = floor(e^L)
// with Lambda_DH(n) != 0, by the structural criterion of verify/dh_true_count.py plus the f64 recursion of twisted_sum.rs:
//   S := {p^k : p == +-1 (mod 5)}  u  T,   T := {n >= 2 : every prime factor of n is == +-2 (mod 5)};
//   Lambda_DH(n) = 0 for every n outside S (proved: f_DH = L1 * F2 with L1 an Euler product over the primes == +-1 (mod 5)),
//   Lambda_DH(p^k) = chi(p)^k log p != 0 on the first part of S, and Lambda_DH = Lambda_{F2} on T.
// The f64 recursion (the same arithmetic as twisted_sum.rs `lambda_dh`, copied verbatim) then serves two purposes: its values at
// the n OUTSIDE S -- proven zeros -- measure the roundoff floor of the recursion in situ at this X; its values at the n in S
// certify nonvanishing wherever |lambda_f64(n)| > theta, a threshold placed far above that floor; the n in S with
// |lambda_f64(n)| <= theta are listed and decided EXACTLY (in Z[kappa]) by verify/dh_exact_eval.py.
// Output: counts (|S|, its two parts, the f64 `!= 0.0` count of the note), the floor, the margin, decade histograms, the list.
// usage: dh_count --L 20 [--theta 1e-6] [--out out/dh_count_L20.json] [--list out/dh_count_L20_below_theta.txt]
use std::env; use std::fs::File; use std::io::Write; use std::time::Instant;

fn kappa() -> f64 { let s5 = 5f64.sqrt(); ((10.0 - 2.0 * s5).sqrt() - 2.0) / (s5 - 1.0) }

fn lambda_dh(x: u64) -> Vec<f64> {           // verbatim from twisted_sum.rs
    let kap = kappa();
    let a = [0.0, 1.0, kap, -kap, -1.0];
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

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut l = 20.0f64; let mut theta = 1e-6f64;
    let mut out = String::from("out/dh_count_L20.json"); let mut list = String::from("out/dh_count_L20_below_theta.txt");
    let mut i = 1;
    while i < args.len() {
        match args[i].as_str() {
            "--L" => { l = args[i + 1].parse().unwrap(); i += 2; }
            "--theta" => { theta = args[i + 1].parse().unwrap(); i += 2; }
            "--out" => { out = args[i + 1].clone(); i += 2; }
            "--list" => { list = args[i + 1].clone(); i += 2; }
            _ => { eprintln!("unknown arg {}", args[i]); std::process::exit(2); }
        }
    }
    let x = l.exp().floor() as u64; let n = x as usize + 1;
    let t0 = Instant::now();
    println!("dh_count: L = {}, X = {}, theta = {:e}", l, x, theta);
    // ---- primes to X
    let mut comp = vec![false; n];
    let r = (x as f64).sqrt() as usize + 1;
    for i in 2..=r { if i < n && !comp[i] { let mut j = i * i; while j < n { comp[j] = true; j += i; } } }
    let t_sieve = t0.elapsed().as_secs_f64();
    // ---- the mask of S
    let mut in_s = vec![true; n]; in_s[0] = false; in_s[1] = false;
    let mut m = 5usize; while m < n { in_s[m] = false; m += 5; }
    let (mut n_pp1, mut n_primes_pm1, mut n_primes_pm2) = (0u64, 0u64, 0u64);
    for p in 2..n {
        if comp[p] { continue; }
        match p % 5 {
            1 | 4 => { n_primes_pm1 += 1; let mut mm = p; while mm < n { in_s[mm] = false; mm += p; }
                       let mut q = p as u64; while q <= x { in_s[q as usize] = true; n_pp1 += 1; q *= p as u64; } }
            2 | 3 => { n_primes_pm2 += 1; }
            _ => {}
        }
    }
    let n_s = in_s.iter().filter(|&&b| b).count() as u64; let n_t = n_s - n_pp1;
    let n_mult5 = (x / 5) as u64; let n_zero_coprime = (x - 1) - n_mult5 - n_s;
    let t_mask = t0.elapsed().as_secs_f64();
    println!("[{:.1}s] primes <= X: {} == +-1 (5), {} == +-2 (5), plus p = 5;  |S| = {} = {} prime powers of +-1 primes + {} in T;  proven zeros: {} multiples of 5 + {} others = {}",
        t_mask, n_primes_pm1, n_primes_pm2, n_s, n_pp1, n_t, n_mult5, n_zero_coprime, n_mult5 + n_zero_coprime);
    // ---- the f64 recursion
    let lam = lambda_dh(x);
    let t_rec = t0.elapsed().as_secs_f64();
    let wit: Vec<(usize, f64)> = [2usize, 3, 4, 5, 6, 12].iter().map(|&k| (k, lam[k])).collect();
    println!("[{:.1}s] Lambda_DH recursion (f64, twisted_sum.rs arithmetic) to X in {:.1}s; witnesses {:?}", t_rec, t_rec - t_mask, wit);
    // ---- statistics
    let mut f64_nonzero = 0u64; let mut s_f64_zero = 0u64; let mut mult5_nonzero = 0u64;
    let mut min_s = (f64::INFINITY, 0usize); let mut max_z = (0.0f64, 0usize); let mut max_s = (0.0f64, 0usize);
    let mut hist_s = [0u64; 42]; let mut hist_z = [0u64; 42];   // bin 0: exactly 0.0; bin 1 + (e + 30): 10^e <= |v| < 10^(e+1), e in [-30, 9]
    let mut below: Vec<usize> = Vec::new(); let mut n_below = 0u64;
    let bin = |v: f64| -> usize { if v == 0.0 { 0 } else { let e = v.log10().floor() as i64; (1 + (e.max(-30).min(9) + 30)) as usize } };
    for m in 2..n {
        let v = lam[m].abs();
        if v != 0.0 { f64_nonzero += 1; }
        if in_s[m] {
            hist_s[bin(v)] += 1;
            if v == 0.0 { s_f64_zero += 1; }
            if v <= theta { n_below += 1; if below.len() < 5_000_000 { below.push(m); } }
            if v < min_s.0 { min_s = (v, m); }
            if v > max_s.0 { max_s = (v, m); }
        } else if m % 5 == 0 {
            if v != 0.0 { mult5_nonzero += 1; }
        } else {
            hist_z[bin(v)] += 1;
            if v > max_z.0 { max_z = (v, m); }
        }
    }
    let t_stat = t0.elapsed().as_secs_f64();
    println!("[{:.1}s] f64 `!= 0.0` count = {} (the note's term count at this L);  multiples of 5 with lambda != 0: {} (expect 0)", t_stat, f64_nonzero, mult5_nonzero);
    println!("    roundoff FLOOR, measured on the {} proven zeros coprime to 5: max |lambda_f64| = {:.3e} at n = {}", n_zero_coprime, max_z.0, max_z.1);
    println!("    on S ({} elements): min |lambda_f64| = {:.3e} at n = {};  max = {:.4} at n = {};  exactly 0.0 in f64: {};  |lambda_f64| <= theta = {:e}: {} (listed for exact evaluation)",
        n_s, min_s.0, min_s.1, max_s.0, max_s.1, s_f64_zero, theta, n_below);
    println!("    decade histogram (count of |lambda_f64| in [10^e, 10^(e+1))), e from -30 to 9; first column: exactly 0.0");
    println!("      on S          : 0.0:{}  {}", hist_s[0], (0..40).map(|k| format!("e{}:{}", k as i64 - 30, hist_s[k + 1])).filter(|s| !s.ends_with(":0")).collect::<Vec<_>>().join("  "));
    println!("      proven zeros  : 0.0:{}  {}", hist_z[0], (0..40).map(|k| format!("e{}:{}", k as i64 - 30, hist_z[k + 1])).filter(|s| !s.ends_with(":0")).collect::<Vec<_>>().join("  "));
    let mut f = File::create(&list).unwrap();
    for &m in &below { writeln!(f, "{}", m).unwrap(); }
    let mut g = File::create(&out).unwrap();
    writeln!(g, "{{\n \"L\": {}, \"X\": {}, \"theta\": {:e}, \"n_primes_pm1\": {}, \"n_primes_pm2\": {}, \"S_size\": {}, \"S_prime_powers_pm1\": {}, \"S_T\": {},",
        l, x, theta, n_primes_pm1, n_primes_pm2, n_s, n_pp1, n_t).unwrap();
    writeln!(g, " \"proven_zeros_mult5\": {}, \"proven_zeros_coprime\": {}, \"f64_nonzero_count\": {}, \"mult5_f64_nonzero\": {}, \"S_f64_exact_zero\": {}, \"S_below_theta\": {},",
        n_mult5, n_zero_coprime, f64_nonzero, mult5_nonzero, s_f64_zero, n_below).unwrap();
    writeln!(g, " \"floor_max_abs\": {:e}, \"floor_argmax\": {}, \"S_min_abs\": {:e}, \"S_argmin\": {}, \"S_max_abs\": {:e}, \"S_argmax\": {},",
        max_z.0, max_z.1, min_s.0, min_s.1, max_s.0, max_s.1).unwrap();
    writeln!(g, " \"hist_S\": {:?}, \"hist_zeros\": {:?}, \"hist_bins\": \"bin 0: exactly 0.0; bin 1+(e+30): 10^e <= |v| < 10^(e+1), e = -30..9\",", hist_s.to_vec(), hist_z.to_vec()).unwrap();
    writeln!(g, " \"witnesses\": {:?}, \"t_sieve\": {:.2}, \"t_mask\": {:.2}, \"t_recursion\": {:.2}, \"t_total\": {:.2}, \"list_file\": \"{}\"\n}}", wit, t_sieve, t_mask, t_rec, t_stat, list).unwrap();
    println!("[{:.1}s] wrote {} and {} ({} entries)", t0.elapsed().as_secs_f64(), out, list, below.len());
}
