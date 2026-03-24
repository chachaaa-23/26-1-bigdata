import numpy as np

# Build arrays directly from Python lists.
a = np.array([10, 20, 30, 40])
b = np.array([[1, 2, 3],
              [4, 5, 6]])

print("a:")
print(a)
print("b:")
print(b)

print()

# arange() creates values with a start, stop, and step.
x = np.arange(0, 10)
y = np.arange(1, 13)

print("np.arange(0, 10):", x)
print("np.arange(1, 13):", y)

print()

# linspace() creates evenly spaced values in a fixed interval.
print("np.linspace(0, 1, 5):", np.linspace(0, 1, 5))

print()

# zeros() and ones() are useful for test data or initialization.
print("np.zeros((2, 3)):")
print(np.zeros((2, 3)))
print("np.ones((2, 3)):")
print(np.ones((2, 3)))
