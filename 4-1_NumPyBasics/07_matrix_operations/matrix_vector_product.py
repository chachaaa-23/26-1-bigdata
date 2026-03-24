import numpy as np

# A matrix can multiply a vector when the inner sizes match.
matrix = np.array([[2, 1, 0],
                   [1, 3, 2]])

vector = np.array([10, 20, 30])
vector_2 = np.array([10, 20, 30]).reshape(3, 1)

print("matrix.shape:", matrix.shape)
print("vector.shape:", vector.shape)
print("vector.shape:", vector_2.shape)

print()

# The result keeps one value for each matrix row.
result = matrix @ vector
result_2 = matrix @ vector_2

print("matrix @ vector:")
print(result)
print(result.shape)

print("matrix @ vector:")
print(result_2)
print(result_2.shape)

print()

# The same rule works for a batch of samples.
samples = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

weights = np.array([[1, 0],
                    [0, 1],
                    [1, 1]])

print("samples @ weights:")
print(samples @ weights)
