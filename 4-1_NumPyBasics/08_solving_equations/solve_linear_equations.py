import numpy as np

# Solve the system:
# 2x + y = 7
# x - y = 2
coefficients_2d = np.array([[2, 1],
                            [1, -1]], dtype=float)

constants_2d = np.array([7, 2], dtype=float)

solution_2d = np.linalg.solve(coefficients_2d, constants_2d)

print("2-variable solution [x, y]:")
print(solution_2d)

print()

# Check the result by plugging the answer back into A @ x = b.
print("Check:")
print(coefficients_2d @ solution_2d)

print()

# Solve a 3-variable system:
# x + y + z = 6
# 2x - y + z = 3
# x + 2y + 3z = 14
coefficients_3d = np.array([[1, 1, 1],
                            [2, -1, 1],
                            [1, 2, 3]], dtype=float)

constants_3d = np.array([6, 3, 14], dtype=float)

solution_3d = np.linalg.solve(coefficients_3d, constants_3d)

print("3-variable solution [x, y, z]:")
print(solution_3d)

print()

# print("Check:")
# print(coefficients_3d @ solution_3d)

# A = np.array([[1, 1],
#               [1, 1]], dtype=float)

# b = np.array([1, 2], dtype=float)

# np.linalg.solve(A, b)