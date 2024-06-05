from z3 import *

# Define the polynomial coefficients here
coeffs = [1, 4, 1, 3, 2]

# Create the solver
s = Solver()

def find_factors(coeffs, modulus):
    degree = len(coeffs) - 1

    # Check if the polynomial can be factored as (ax + b)(cx^3 + dx^2 + ex + f)
    a, b, c, d, e, f = Ints('a b c d e f')
    s.add(a >= 0, a < modulus, b >= 0, b < modulus, c >= 0, c < modulus, d >= 0, d < modulus, e >= 0, e < modulus, f >= 0, f < modulus)
    s.add((a * c) % modulus == coeffs[0], (a * d + b * c) % modulus == coeffs[1],
          (a * e + b * d + c * b) % modulus == coeffs[2], (a * f + b * e + c * d) % modulus == coeffs[3],
          (b * f + c * e) % modulus == coeffs[4])

    while s.check() == sat:
        model = s.model()
        factors = (f'{model[a]}x + {model[b]}', f'{model[c]}x^3 + {model[d]}x^2 + {model[e]}x + {model[f]}')
        print(f'The polynomial is reducible in Z{modulus}(x). Factors: {factors}')
        s.add(Or(a != model[a], b != model[b], c != model[c], d != model[d], e != model[e], f != model[f]))

    s.reset()

    # Check if the polynomial can be factored as (ax^2 + bx + c)(dx^2 + ex + f)
    a, b, c, d, e, f = Ints('a b c d e f')
    s.add(a >= 0, a < modulus, b >= 0, b < modulus, c >= 0, c < modulus, d >= 0, d < modulus, e >= 0, e < modulus, f >= 0, f < modulus)
    s.add((a * d) % modulus == coeffs[0], (a * e + b * d) % modulus == coeffs[1],
          (a * f + b * e + c * d) % modulus == coeffs[2], (b * f + c * e) % modulus == coeffs[3],
          (c * f) % modulus == coeffs[4])

    while s.check() == sat:
        model = s.model()
        factors = (f'{model[a]}x^2 + {model[b]}x + {model[c]}', f'{model[d]}x^2 + {model[e]}x + {model[f]}')
        print(f'The polynomial is reducible in Z{modulus}(x). Factors: {factors}')
        s.add(Or(a != model[a], b != model[b], c != model[c], d != model[d], e != model[e], f != model[f]))

    s.reset()

    # If no factorization found, polynomial is irreducible
    print(f'The polynomial is irreducible in Z{modulus}(x).')
    return False

# Check if the polynomial is reducible
find_factors(coeffs, 5)
