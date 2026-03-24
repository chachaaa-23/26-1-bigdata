import numpy as np

# A comparison creates a Boolean mask.
scores = np.array([55, 72, 68, 90, 43, 81])

print("scores > 70:", scores > 70)
print("scores[scores > 70]:", scores[scores > 70])

print()

# The same idea also works with two-dimensional arrays.
sales = np.array([[120, 80, 95, 110],
                  [100, 90, 105, 115],
                  [130, 70, 100, 120]])

print("sales >= 110:")
print(sales >= 110)

print()

print("sales[sales >= 110]:", sales[sales >= 110])
print("sales[sales < 100]:", sales[sales < 100])
