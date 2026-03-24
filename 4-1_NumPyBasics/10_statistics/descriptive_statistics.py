import numpy as np

# Use score data to practice descriptive statistics.
scores = np.array([72, 85, 90, 68, 77, 95, 88, 91, 73, 84], dtype=float)

print("Scores:", scores)

print()

# mean() gives the average value.
print("Mean:", scores.mean())

# median() gives the center value after sorting.
print("Median:", np.median(scores))

# min() and max() show the smallest and largest values.
print("Minimum:", scores.min())
print("Maximum:", scores.max())

print()

# ptp() means peak-to-peak, which is max - min.
print("Range:", np.ptp(scores))

# var() measures how spread out the values are.
print("Variance:", scores.var())

# std() is the standard deviation.
print("Standard deviation:", scores.std())

print()

# The same functions also work on two-dimensional arrays.
class_scores = np.array([[72, 85, 90],
                         [68, 77, 95],
                         [88, 91, 73],
                         [84, 79, 87]], dtype=float)

print("Class scores:")
print(class_scores)

print()

# axis=0 gives column-based statistics.
print("Subject means:", class_scores.mean(axis=0))

# axis=1 gives row-based statistics.
print("Student means:", class_scores.mean(axis=1))
