import numpy as np
import itertools


def solve_gaussian_integer_min(A, b, search_limit=40):

    A = A.astype(float)
    b = b.astype(float)
    rows, cols = A.shape

    M = np.hstack([A, b.reshape(-1, 1)])

    pivot_row = 0
    pivot_cols = []
    free_cols = []

    for col in range(cols):
        if pivot_row >= rows:
            free_cols.append(col)
            continue

        pivot_candidate = np.argmax(np.abs(M[pivot_row:, col])) + pivot_row

        if np.abs(M[pivot_candidate, col]) < 1e-10:
            free_cols.append(col)
            continue

        M[[pivot_row, pivot_candidate]] = M[[pivot_candidate, pivot_row]]

        M[pivot_row] /= M[pivot_row, col]

        for r in range(rows):
            if r != pivot_row:
                factor = M[r, col]
                M[r] -= factor * M[pivot_row]

        pivot_cols.append(col)
        pivot_row += 1

    for r in range(pivot_row, rows):
        if np.abs(M[r, -1]) > 1e-5:
            raise ValueError("System hat mathematisch KEINE Lösung.")

    if not free_cols:
        x = M[:cols, -1]
        if np.all(x >= -1e-5) and np.all(np.abs(x - np.round(x)) < 1e-5):
            return np.round(x).astype(int)
        else:
            raise ValueError("Einzige Lösung ist nicht positiv oder nicht ganzzahlig.")

    print(f"System unterbestimmt. Freie Variablen an Indices: {free_cols}")
    print(f"Teste Kombinationen im Bereich 0 bis {search_limit}...")
    best_solution = None
    min_total_presses = float('inf')

    ranges = [range(search_limit + 1) for _ in free_cols]

    for free_values in itertools.product(*ranges):
        x_candidate = np.zeros(cols)

        for i, f_idx in enumerate(free_cols):
            x_candidate[f_idx] = free_values[i]


        for i, p_idx in enumerate(pivot_cols):
            val = M[i, -1]

            for k, f_idx in enumerate(free_cols):
                coeff = M[i, f_idx]
                val -= coeff * x_candidate[f_idx]

            x_candidate[p_idx] = val

        if np.any(x_candidate < -1e-5):
            continue

        x_rounded = np.round(x_candidate)
        if not np.all(np.abs(x_candidate - x_rounded) < 1e-5):
            continue

        x_final = x_rounded.astype(int)
        total_presses = np.sum(x_final)

        if total_presses < min_total_presses:
            min_total_presses = total_presses
            best_solution = x_final

    if best_solution is None:
        raise ValueError(f"Keine positive ganzzahlige Lösung im Suchbereich (0-{search_limit}) gefunden.")

    return best_solution





with open('input.txt', 'r') as file:
    input = file.read().splitlines()

print(input)
parts = []
end_conf = []
switches = []
for i in range(len(input)):
    parts.append(input[i].split(" "))
    switches.append(parts[i][1:-1])
    end_conf.append(parts[i][-1][1:-1].split(","))
print(end_conf)
sol = 0
for j in range(len(end_conf)):
    b = [0]*len(end_conf[j])
    A = np.zeros((len(end_conf[j]), len(switches[j])))
    for i in range(len(end_conf[j])):
        b[i] = int(end_conf[j][i])
    for i in range(len(switches[j])):
        for i2 in range(len(switches[j][i])):
            if switches[j][i][i2] in "(),":
                continue
            else:
                num = int(switches[j][i][i2])
                A[num][i] = 1
    print(A, b)
    b = np.array(b)
    A = A.astype(int)
    b = b.astype(int)
    solution = solve_gaussian_integer_min(A, b, max(b))
    print("Benötigte Schalterdrücke (1 = drücken, 0 = nicht):")
    print(sum(solution))
    sol += sum(solution)


print(sol)
