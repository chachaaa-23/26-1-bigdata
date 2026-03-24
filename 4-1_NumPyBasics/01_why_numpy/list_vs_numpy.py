import numpy as np

# Python lists can store numbers, but + joins the two lists together.
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("List result:", list_a + list_b)

print()

# NumPy arrays are designed for numeric calculation.
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

print("Array addition:", array_a + array_b)
print("Array multiplication:", array_a * array_b)

print()

# A single number is applied to every element in the array.
print("Array + 10:", array_a + 10)
