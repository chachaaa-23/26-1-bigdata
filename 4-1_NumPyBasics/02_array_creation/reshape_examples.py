import numpy as np

# Start with one long one-dimensional array.
numbers = np.arange(1, 13)

print("Original array:")
print(numbers)

print()

# reshape() changes the shape but keeps the same values.
print("Reshape to 3 x 4:")
print(numbers.reshape(3, 4))

print()

# The total number of elements must stay the same.
print("Reshape to 2 x 6:")
print(numbers.reshape(2, 6))

print()

print("Reshape to 4 x 3:")
print(numbers.reshape(4, 3))
