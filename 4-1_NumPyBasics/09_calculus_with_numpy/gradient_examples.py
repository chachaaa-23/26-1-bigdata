import numpy as np

# gradient() estimates the rate of change at each point.
one_dimensional_data = np.array([0, 1, 4, 9, 16], dtype=float)

print("1D data:", one_dimensional_data)
print("1D gradient:", np.gradient(one_dimensional_data, 1))

print()

# In two dimensions, the first result is the row direction
# and the second result is the column direction.
surface = np.array([[1, 2, 4],
                    [2, 3, 5],
                    [4, 6, 8]], dtype=float)

row_gradient, column_gradient = np.gradient(surface, 1, 1)

print("Surface:")
print(surface)

print()

print("Gradient along rows:")
print(row_gradient)

print()

print("Gradient along columns:")
print(column_gradient)
