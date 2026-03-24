import numpy as np

# Use a sales table to practice aggregation.
sales = np.array([[120, 80, 95, 110],
                  [100, 90, 105, 115],
                  [130, 70, 100, 120]])

# Basic aggregation reads the whole array at once.
print("sales.sum():", sales.sum())
print("sales.mean():", sales.mean())
print("sales.max():", sales.max())
print("sales.min():", sales.min())

print()

# axis=0 groups values down the rows, so the result is column based.
print("sales.sum(axis=0):", sales.sum(axis=0))

# axis=1 groups values across the columns, so the result is row based.
print("sales.sum(axis=1):", sales.sum(axis=1))
print("sales.mean(axis=1):", sales.mean(axis=1))
