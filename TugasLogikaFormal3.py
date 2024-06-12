from z3 import *
from itertools import combinations

def ramsey_theorem(P, M, B):
    solver = Solver()

    # Mendefinisikan variabel boolean untuk sisi-sisi graf Kp
    edges = {}
    for i in range(P):
        for j in range(i + 1, P):
            edges[(i, j)] = Bool(f"edge_{i}_{j}")

    # Fungsi untuk mengecek apakah semua tepi merah
    def all_red(S):
        return And([edges[(i, j)] for i, j in combinations(S, 2)])

    # Fungsi untuk mengecek apakah semua tepi biru
    def all_blue(S):
        return And([Not(edges[(i, j)]) for i, j in combinations(S, 2)])

    # Fungsi untuk mengecek apakah terdapat clique merah Km
    def exist_red_clique(N, M):
        for subset in combinations(N, M):
            solver.add(Not(all_red(subset)))

    # Fungsi untuk mengecek apakah terdapat clique biru Kb
    def exist_blue_clique(N, B):
        for subset in combinations(N, B):
            solver.add(Not(all_blue(subset)))

    # Membuat daftar Node dengan range P
    N = list(range(P))

    # Menambahkan constraint untuk mengecek apakah ada clique merah Km dan clique biru Kb
    exist_red_clique(N, M)
    exist_blue_clique(N, B)

    # Mengecek constraint
    if solver.check() == sat:
        return "tidak"
    else:
        return "ya"

Test = [
    (3, 3, 2),
    (4, 3, 2),
    (4, 3, 3),
    (5, 3, 3),
    (6, 3, 3),
    (7, 3, 3),
]

for P, M, N in Test:
    result = ramsey_theorem(P, M, N)
    print(f"P={P}, M={M}, N={N} => {result}")
