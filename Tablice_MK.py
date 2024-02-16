def disp_matrix(matrix):
  for row in matrix:
      print(row)

def multiply_v(matrix, val):
  result = []
  for row in matrix:
      result.append([element * val for element in row])
  disp_matrix(result)
  return result

def multiply(matrix_a, matrix_b):
  result = []
  for i in range(len(matrix_a)):
      row_result = []
      for j in range(len(matrix_b[0])):
          dot_product = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(len(matrix_b)))
          row_result.append(dot_product)
      result.append(row_result)
  disp_matrix(result)
  return result

def add_v(matrix, val):
  result = []
  for row in matrix:
      result.append([element + val for element in row])
  disp_matrix(result)
  return result

def add(matrix_a, matrix_b):
  result = []
  for i in range(len(matrix_a)):
      row_result = [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
      result.append(row_result)
  disp_matrix(result)
  return result

def rotate(matrix):
  result = [list(row)[::-1] for row in zip(*matrix)]
  disp_matrix(result)
  return result

# Przykładowe użycie funkcji
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
val = 3

print("MultiplyV:")
result_multiply_v = multiply_v(A, val)

print("\nMultiply:")
result_multiply = multiply(A, B)

print("\nAddV:")
result_add_v = add_v(A, val)

print("\nAdd:")
result_add = add(A, B)

print("\nRotate:")
result_rotate = rotate(A)
