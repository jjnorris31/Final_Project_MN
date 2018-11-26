def create_matrix(m, n, v):
    C = []
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(v)
    return C


def get_dimensions(A):
    return len(A), len(A[0])


def add_matrix(A, B):
    Am, An = get_dimensions(A)
    Bm, Bn = get_dimensions(B)
    if Am != Bm or An != Bn:
        print("Las dimensiones son diferentes")
        return []
    C = create_matrix(Am, An, 0)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] + B[i][j]
    return C


def product_matrix(A, B):
    Am, An = get_dimensions(A)
    Bm, Bn = get_dimensions(B)
    if An != Bm:
        print("Las matrices no son conformables")
        return []
    C = create_matrix(Am, Bn, 0)
    for i in range(Am):
        for j in range(Bn):
            for k in range(An):
                C[i][j] += A[i][k] * B[k][j]
    return C


def get_low_matrix(A, r, c):
    m, n = get_dimensions(A)
    C = create_matrix(m - 1, n - 1, 0)
    for i in range(m):
        if i == r:
            continue
        for j in range(n):
            if j == c:
                continue
            Ci = i
            if i > r:
                Ci = i - 1
            Cj = j
            if j > c:
                Cj = j - 1
            C[Ci][Cj] = A[i][j]
    return C


def det_matrix(A):
    m, n = get_dimensions(A)
    if m != n:
        print("La matriz no es cuadrada")
        return -1

    if m == 1:
        return m

    if m == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    det = 0

    for j in range(n):
        det += (-1) ** (j) * A[0][j] * det_matrix(get_low_matrix(A, 0, j))
    return det


def get_ady_matrix(A):
    m, n = get_dimensions(A)
    C = create_matrix(m, n, 0)
    for i in range(m):
        for j in range(n):
            C[i][j] = (-1) ** (i + j) * det_matrix(get_low_matrix(A, i, j))
    return C


def get_trans_matrix(A):
    m, n = get_dimensions(A)
    C = create_matrix(n, m, 0)
    for i in range(m):
        for j in range(n):
            C[j][i] = A[i][j]
    return C


def get_inv_matrix(A):
    detA = det_matrix(A)
    if detA == 0:
        print("La matriz no tiene inversa")
        return 0
    At = get_trans_matrix(A)
    adyAt = get_ady_matrix(At)
    m, n = get_dimensions(A)
    C = create_matrix(m, n, 0)
    for i in range(m):
        for j in range(n):
            C[i][j] = (1 / detA) * adyAt[i][j]
    return C