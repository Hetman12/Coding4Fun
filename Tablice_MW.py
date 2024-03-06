def MultiplyV(A,val):
    rows_A, cols_A = len(A), len(A[0])
    C=[[0 for _ in range(cols_A)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_A):
            C[i][j] = A[i][j]*3
    return(C)

# def Multiply(A,B):
#     rows_A, cols_A = len(A), len(A[0])
#     C=[[0 for _ in range(cols_A)] for _ in range(rows_A)]
#     for i in range(rows_A):
#         for j in range(cols_A):
#             C[i][j] = A[i][j]*3
#     print(C)

def Multiply(A,B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("Macierze maja rozne wymiary, nie moga zostac przemnozone.")

    C = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


def AddV(A,val):
    rows_A, cols_A = len(A), len(A[0])
    C=[[0 for _ in range(cols_A)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_A):
            C[i][j] = A[i][j]+val
    return(C)

def Add(A,B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if rows_A == rows_B and cols_A==cols_B:
        C=[[0 for _ in range(cols_A)] for _ in range(rows_A)]
        for i in range(rows_A):
            for j in range(cols_A):
                C[i][j] = A[i][j] + B[i][j]
        return(C)
    else:
        print("Matrices have different shapes")

def Rotate(A):
    rows_A, cols_A = len(A), len(A[0])

    C=[[0 for _ in range(cols_A)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_A):
            C[i][j] += A[j][i]
    D=[]
    for i in range(len(C)):
        D.append(C[i][::-1])
    return(D)

    
A = [[1,2,3], [4,5,6], [7,8,9]] 
B = [[9,8,7], [6,5,4], [3,2,1]] 
val = 3


multiplyV_res = MultiplyV(A,val)
print(multiplyV_res)

print(Multiply(A,B))

AddV_res = AddV(A,val)
print(AddV_res)

Add_res = Add(A,B)
print(Add_res)

print(Rotate(A))

# print(list(zip(A)))