from z3 import *

# Define the polynomial coefficients here
coeffs = [1,4,1,3,2]  # Example: 2x^4 + 3x^3 + x^2 + 4x + 1

# Create the solver
s = Solver()

def find_factors(coeffs, modulus):
    degree = len(coeffs) - 1

    if degree == 4:
        # Case 1: (ax + b)(cx^3 + dx^2 + ex + f)
        a, b, c, d, e, f = Ints('a b c d e f')
        s.add(a >= 0, a < modulus, b >= 0, b < modulus,
              c >= 0, c < modulus, d >= 0, d < modulus,
              e >= 0, e < modulus, f >= 0, f < modulus)
        s.add((a * c) % modulus == coeffs[4],  # Coefficient of x^4
              (a * d + b * c) % modulus == coeffs[3],  # Coefficient of x^3
              (a * e + b * d) % modulus == coeffs[2],  # Coefficient of x^2
              (a * f + b * e) % modulus == coeffs[1],  # Coefficient of x
              (b * f) % modulus == coeffs[0])  # Constant term

        while s.check() == sat:
            model = s.model()
            factors = (f'{model[a]}x + {model[b]}', f'{model[c]}x^3 + {model[d]}x^2 + {model[e]}x + {model[f]}')
            print(f'The polynomial is reducible in Z{modulus}(x). Factors: {factors}')
            print(f'a = {model[a]}, b = {model[b]}, c = {model[c]}, d = {model[d]}, e = {model[e]}, f = {model[f]}')
            # Add constraint to exclude the current model
            s.add(Or(a != model[a], b != model[b], c != model[c], d != model[d], e != model[e], f != model[f]))
        s.reset()

        # Case 2: (ax^2 + bx + c)(dx^2 + ex + f)
        a, b, c, d, e, f = Ints('a b c d e f')
        s.add(a >= 0, a < modulus, b >= 0, b < modulus,
              c >= 0, c < modulus, d >= 0, d < modulus,
              e >= 0, e < modulus, f >= 0, f < modulus)
        s.add((a * d) % modulus == coeffs[4],  # Coefficient of x^4
              (a * e + b * d) % modulus == coeffs[3],  # Coefficient of x^3
              (a * f + b * e + c * d) % modulus == coeffs[2],  # Coefficient of x^2
              (b * f + c * e) % modulus == coeffs[1],  # Coefficient of x
              (c * f) % modulus == coeffs[0])  # Constant term

        while s.check() == sat:
            model = s.model()
            factors = (f'{model[a]}x^2 + {model[b]}x + {model[c]}', f'{model[d]}x^2 + {model[e]}x + {model[f]}')
            print(f'The polynomial is reducible in Z{modulus}(x). Factors: {factors}')
            print(f'a = {model[a]}, b = {model[b]}, c = {model[c]}, d = {model[d]}, e = {model[e]}, f = {model[f]}')
            # Add constraint to exclude the current model
            s.add(Or(a != model[a], b != model[b], c != model[c], d != model[d], e != model[e], f != model[f]))
        s.reset()

# Check if the polynomial is reducible
find_factors(coeffs, 5)
