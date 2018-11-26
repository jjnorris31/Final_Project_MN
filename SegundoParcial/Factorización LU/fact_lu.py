# x1 + 2x2 + 4x3 = 11
# 4x1 + x2 -x3 = 0
# 2x1 + 5x2 + 2x3 = 3
def create_matrix(m, n, v):
    C = []
    for i in range(m):
        C.append([v]*n)
    return C

U = create_matrix(3, 3, 0)
U[0] = [5,20,5]
U[1] = [2,1,-3]
U[2] = [-2,0,1]

L = create_matrix(3, 3, 0)
L[0] = [1,0,0]
L[1] = [0,1,0]
L[2] = [0,0,1]


for i in range(3):
    a = U[i][i]
    if a == 0:
        print("La matriz no tiene LU")
        break
    for j in range(i+1,3):
        b = U[j][i]
        c = -1*b/a
        L[j][i] = -1*c
        T = create_matrix(1, 3, 0)
        for k in range(3):
            T[0][k] = c * U[i][k]
        for k in range(3):
            U[j][k] += T[0][k]
print(L)
print(U)


Z = create_matrix(3, 1, 0)
C = create_matrix(3, 1, 0)
C[0] = [210]
C[1] = [0]
C[2] = [0]
for i in range(3):
    Z[i][0] = C[i][0]
    for j in range(3):
        if i == j:
            break
        Z[i][0] -= L[i][j]*Z[j][0]
print(Z)
B = create_matrix(3, 1, 0)
for i in range(2,-1,-1):
    B[i][0] = Z[i][0]
    for j in range(2,-1,-1):
        if i == j:
            B[i][0] = B[i][0]/U[i][j]
            break
        B[i][0] -= U[i][j]*B[j][0]
print(B)