-- CHECK-O probe (checker-written): FIDELITY (D10) — is epsteinB rejected by the compiler outside `noncomputable section`?
import Mathlib
def epsteinB' (n : ℕ) : ℚ :=
  (((Finset.Icc (-(n : ℤ)) n ×ˢ Finset.Icc (-(n : ℤ)) n).filter
      (fun xy : ℤ × ℤ => xy.1 ^ 2 + 5 * xy.2 ^ 2 = n)).card : ℚ) / 2
