import numpy as np

def MultiplyV(matrix,val):
    results=[]
    for row in matrix:
        results.append([cell*val for cell in row])
    for row in results:
        print(row)
    return results

def MultiplyVNum(matrix,val):
    results = matrix * val
    print(results)

def Multiply(matrixA,matrixB):
    results = []
    for i in range(len(matrixA)):
        row_results = []
        for j in range(len(matrixB[0])):
            dot_product = sum(matrixA[i][k] * matrixB[k][j] for k in range(len(matrixB)))
            row_results.append(dot_product)
        results.append(row_results)
    for row in results:
        print(row)
    return results

def MultiplyNum(matrixA,matrixB):
    results = matrixA.dot(matrixB)
    print(results)

def AddV(matrix,val):
    results = []
    for row in matrix:
        results.append([cell + val for cell in row])
    for row in results:
        print(row)
    return results

def AddVNum(matrix,val):
    results = matrix + val
    print(results)


def Add(matrixA,matrixB):
    results = []
    for i in range(len(matrixA)):
      row_results = [matrixA[i][j] + matrixB[i][j] for j in range(len(matrixA[0]))]
      results.append(row_results)
    for row in results:
        print (row)
    return results

def AddNum(matrixA,matrixB):
    results = matrixA + matrixB
    print(results)


def Rotate(matrix):
    results = np.rot90(matrix,-1)
    print(results)

A=np.arange(1,10).reshape(3,3)
B=np.arange(9,0,-1).reshape(3,3)
Val = 3

print("MultiplyV:")
results_multiplyV = MultiplyV(A, Val)

print("MultiplyVNum:")
results_multiplyV = MultiplyVNum(A, Val)

print("Multiply:")
results_multiply = Multiply(A, B)

print("MultiplyNum:")
results_MultiplyNum = MultiplyNum(A,B)

print("AddV:")
results_AddV = AddV(A, Val)

print("AddVNum:")
results_AddVNum = AddVNum(A, Val)

print("Add:")
results_Add = Add(A,B)

print("AddNum:")
results_AddNum = AddNum(A,B)

print("Rotate:")
results_Rotate = Rotate(A)