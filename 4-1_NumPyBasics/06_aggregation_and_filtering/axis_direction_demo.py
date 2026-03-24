import numpy as np

# This small matrix is useful when students are confused about axis.
x = np.array([[1, 2, 3],
              [4, 5, 6]])

print("x:")
print(x)

print()

# axis=0 moves down the rows and groups each column.
print("x.sum(axis=0):", x.sum(axis=0))

# axis=1 moves across the columns and groups each row.
print("x.sum(axis=1):", x.sum(axis=1))

print()

# mean() follows the same axis rule.
print("x.mean(axis=0):", x.mean(axis=0))
print("x.mean(axis=1):", x.mean(axis=1))
