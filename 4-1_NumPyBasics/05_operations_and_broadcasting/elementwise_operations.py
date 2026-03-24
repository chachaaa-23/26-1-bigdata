import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Arrays with the same shape are calculated element by element.
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)

print()

# Power also applies element by element.
print("a ** 2:", a ** 2)

print()

# A scalar value is applied to every element in the array.
scores = np.array([70, 80, 90])

print("scores + 5:", scores + 5)
print("scores * 2:", scores * 2)
print("scores / 10:", scores / 10)
