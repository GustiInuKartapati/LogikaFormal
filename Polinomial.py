from z3 import *
#Menentukan apakah polinomial 2x^4+3x^3+x^2+4x+1 tereduksi di Z5(x)

#hint 1: koefisien dari polinomial dipaksa 0 s/d 4
#hint 2: definisilan koefisien dari polinomial sebagai list: [2,3,1,4,1] --> [2x^4,3x^3,x^2,4x,1]
#hint 3: operasi modulo -> x % 5 == y

# Define the polynomial coefficients here
coeffs = [ 3, 4, 1, 3, 2]

# Maximum degree of the polynomial
degree = len(coeffs) - 1

# Create the solver
s = Solver()

def find_factors(coeffs, modulus):
    degree = len(coeffs) - 1
    found_factorization = False

    # Check factorizations based on the degree
    if degree == 1:
        return False

    elif degree == 2:
        a, b, c, d = Ints('a b c d')
        s.push()
        s.add(a >= 0, a < modulus, b >= 0, b < modulus, c >= 0, c < modulus, d >= 0, d < modulus)
        s.add(a * c % modulus == coeffs[2], (a * d + b * c) % modulus == coeffs[1], b * d % modulus == coeffs[0])
        if s.check() == sat:
            model = s.model()
            factors = (f'{model[a]}x + {model[b]}', f'{model[c]}x + {model[d]}')
            print(f'The polynomial is reducible in Z{modulus}(x). Factors: {factors}')
            found_factorization = True
        s.pop()

    elif degree == 3:
        a, b, c, d, e = Ints('a b c d e')
        s.push()
        s.add(a >= 0, a < modulus, b >= 0, b < modulus, c >= 0, c < modulus, d >= 0, d < modulus, e >= 0, e < modulus)
        s.add(a * c % modulus == coeffs[3],
              (a * d + b * c) % modulus == coeffs[2],
              (a * e + b * d + c * b) % modulus == coeffs[1],
              b * e % modulus == coeffs[0])
        if s.check() == sat:
            model = s.model()
            factors = (f'{model[a]}x + {model[b]}', f'{model[c]}x^2 + {model[d]}x + {model[e]}')
            print(f'The polynomial is reducible in Z{modulus}(x). Factors: {factors}')
            found_factorization = True
        s.pop()

    elif degree == 4:
        a, b, c, d, e, f = Ints('a b c d e f')
        s.push()
        s.add(a >= 0, a < modulus, b >= 0, b < modulus, c >= 0, c < modulus, d >= 0, d < modulus, e >= 0, e < modulus, f >= 0, f < modulus)
        s.add(a * d % modulus == coeffs[4],
              (a * e + b * d) % modulus == coeffs[3],
              (a * f + b * e + c * d) % modulus == coeffs[2],
              (b * f + c * e) % modulus == coeffs[1],
              c * f % modulus == coeffs[0])
        if s.check() == sat:
            model = s.model()
            factors = (f'{model[a]}x^2 + {model[b]}x + {model[c]}', f'{model[d]}x^2 + {model[e]}x + {model[f]}')
            print(f'The polynomial is reducible in Z{modulus}(x). Factors: {factors}')
            found_factorization = True
        s.pop()

    return found_factorization

# Check if the polynomial is reducible
if not find_factors(coeffs, 5):
    print(f'The polynomial is irreducible in Z5(x).')