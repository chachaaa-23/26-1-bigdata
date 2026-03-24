import numpy as np

# Each row is a branch and each column is a product.
sales = np.array([[120, 80, 95, 110],
                  [100, 90, 105, 115],
                  [130, 70, 100, 120]])

# This one-dimensional array stores the price for each product.
price = np.array([2000, 1500, 1200, 3500])

print("sales shape:", sales.shape)
print("price shape:", price.shape)

print()

# A single value can be added to every cell in the table.
print("sales + 10:")
print(sales + 10)

print()

# NumPy broadcasts the product prices across every row automatically.
revenue = sales * price

print("Revenue matrix:")
print(revenue)

print()

# axis=1 adds each row, so we get branch totals.
print("Total revenue:", revenue.sum())
print("Product revenue totals:", revenue.sum(axis=0))
print("Branch revenue totals:", revenue.sum(axis=1))
