import numpy as np

# Use simple vectors to compare different kinds of products.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vector a:", a)
print("Vector b:", b)

print()

# The dot product multiplies matching positions and adds the results.
print("Dot product with np.dot(a, b):", np.dot(a, b))
print("Dot product with a @ b:", a @ b)

print()

# The outer product combines every value in a with every value in b.
print("Outer product with np.outer(a, b):")
print(np.outer(a, b)) #벡터의 곱으로 만든 행렬

print()

# The cross product returns a vector perpendicular to both inputs.
print("Cross product with np.cross(a, b):", np.cross(a, b)) #벡터의 외적 계산

print()

# inner() is the same as the dot product for one-dimensional vectors.
print("Inner product with np.inner(a, b):", np.inner(a, b))
