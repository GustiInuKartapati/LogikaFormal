from z3 import *
from itertools import combinations

def ramsey_theorem(P, M, B):
    solver = Solver()

    # Definisi matrix segitiga atas Kp
    edges = {}
    for i in range(P):
        for j in range(i + 1, P):
            edges[(i, j)] = Bool(f"edge_{i}_{j}")

    # Fungsi untuk cek apakah semua sisi merah
    def all_red(S):
        return And([edges[(i, j)] for i, j in combinations(S, 2)])

    # Fungsi untuk cek apakah semua sisi biru
    def all_blue(S):
        return And([Not(edges[(i, j)]) for i, j in combinations(S, 2)])

    # Fungsi untuk cek apakah terdapat Km dimana semua sisi merah
    def exist_red_clique(N, M):
        for subset in combinations(N, M):
            solver.add(Not(all_red(subset)))

    # Fungsi untuk cek apakah terdapat Kb dimana semua sisi biru
    def exist_blue_clique(N, B):
        for subset in combinations(N, B):
            solver.add(Not(all_blue(subset)))

    # Membuat list Node dengan range P
    N = list(range(P))

    # Menambahkan constraint to mengecek apakah ada Kp dan Kb
    exist_red_clique(N, M)
    exist_blue_clique(N, B)

    # Cek constraint
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