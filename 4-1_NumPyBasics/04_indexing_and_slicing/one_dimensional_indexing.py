import numpy as np

# One-dimensional indexing works like list indexing.
a = np.array([10, 20, 30, 40, 50])

print("Original array:", a)

print()

# Read single values by index.
print("a[0]:", a[0])
print("a[2]:", a[2])
print("a[-1]:", a[-1])

print()

# Slicing reads a range of values.
print("a[1:4]:", a[1:4])
print("a[:3]:", a[:3])
print("a[1:4:2]:", a[1:4:2])
print("a[::2]:", a[::2])
print("a[1::2]:", a[1::2])
print("a[:4:2]:", a[:4:2])
print("a[::-1]:", a[::-1])
print("a[3:1:-1]:", a[3:1:-1])
print("a[::-2]:", a[::-2])
