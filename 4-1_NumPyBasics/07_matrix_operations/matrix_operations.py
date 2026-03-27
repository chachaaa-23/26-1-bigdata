import numpy as np

# Two-dimensional NumPy arrays can be treated as matrices.
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[10, 20],
              [30, 40]])

C = np.array([[10, 20, 10, 20, 55, 77],
              [30, 40, 54, 63, 21, 44],
              [45, 223, 54, 45, 21, 56],
              [7, 0, 1, 63, 1, 89],
              [100, 5, 2, 6, 46, 78],
              [1, 5, 4, 78, 3, 243],])

print("Matrix A:")
print(A)

print()

print("Matrix B:")
print(B)

print()

# + and - work element by element when the shapes match.
print("A + B:")
print(A + B)

print()

print("A - B:")
print(A - B)

print()

# * is still element-wise multiplication in NumPy.
print("A * B:")
print(A * B)

print()

# @ means matrix multiplication.
print("A @ B:") #일반적인 행렬곱
print(A @ B)

print()

# np.linalg.inv() returns the inverse matrix when it exists.
inverse_C = np.linalg.inv(C)
print("inv(C):")
print(inverse_C)


inverse_A = np.linalg.inv(A)

print("inv(A):")
print(inverse_A) # 역함수 function, numpy 내장됨! (데이터 찌꺼기값 주의)

print()

# A multiplied by its inverse becomes the identity matrix.
print("A @ inv(A):")
print(A @ inverse_A)

print()

# .T changes rows into columns.
print("A.T:") #transpose matrix 계산
print(A.T)

print()

# np.eye() creates an identity matrix.
I = np.eye(2, dtype=int)

print("Identity matrix:")
print(I)

print()

# Multiplying by the identity matrix keeps the matrix unchanged.
print("A @ I:")
print(A @ I)
