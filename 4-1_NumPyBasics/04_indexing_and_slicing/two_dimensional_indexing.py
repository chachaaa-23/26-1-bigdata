import numpy as np

# In two dimensions, the first index is the row and the second is the column.
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Original array:")
print(arr)

print()

# Read single values from a row and column position.
print("arr[0, 0]:", arr[0, 0])
print("arr[1, 2]:", arr[1, 2])

print()

# Use : to mean "all rows" or "all columns".
print("arr[0:2, 1:3]:")
print(arr[0:2, 1:3])

print()

print("arr[:, 1]:", arr[:, 1])
print("arr[1, :]:", arr[1, :])
print("arr[:, 1].shape:", arr[:, 1].shape)
print("arr[1, :].shape:", arr[1, :].shape)