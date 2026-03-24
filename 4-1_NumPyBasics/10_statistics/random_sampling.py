import numpy as np

# Use a fixed seed so the random output stays the same every time.
rng = np.random.default_rng(42)

print("Seed: 42")

print()

# integers() creates random integers in a given range.
dice_rolls = rng.integers(1, 7, size=10)

print("Random dice rolls:")
print(dice_rolls)

print()

# random() creates random floats between 0 and 1.
uniform_samples = rng.random(5)

print("Uniform random samples:")
print(np.round(uniform_samples, 4))

print()

# normal() creates random values from a normal distribution.
# loc is the mean and scale is the standard deviation.
normal_scores = rng.normal(loc=75, scale=10, size=8)

print("Normal-distribution samples:")
print(np.round(normal_scores, 2))

print()

# choice() can select a random sample from existing values.
student_ids = np.arange(1, 11)
selected_students = rng.choice(student_ids, size=4, replace=False)

print("Random student sample without replacement:")
print(selected_students)

print()

# We can also take a bootstrap-style sample with replacement.
bootstrap_sample = rng.choice(normal_scores, size=10, replace=True)

print("Bootstrap-style sample with replacement:")
print(np.round(bootstrap_sample, 2))