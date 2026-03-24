import numpy as np

# Use one-dimensional and two-dimensional arrays for comparison.
a = np.array([10, 20, 30, 40])
b = np.array([[1, 2, 3],
              [4, 5, 6]])

# shape tells us the structure of the array.
print("a.shape:", a.shape)
print("b.shape:", b.shape)

print()

# ndim tells us how many dimensions the array has.
print("a.ndim:", a.ndim)
print("b.ndim:", b.ndim)

print()

# dtype shows the data type of the array values.
print("a.dtype:", a.dtype)
print("b.dtype:", b.dtype)

print()

# size is the total number of elements in the array.
print("a.size:", a.size)
print("b.size:", b.size)
