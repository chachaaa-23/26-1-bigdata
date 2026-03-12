# Sets store unique values.
a = set([1, 2, 3, 4, 5])
b = set([1, 2, 10, 11])
c = set([1, 1, 2, 2, 3])

# Compare two sets.
print(a & b) # Intersection
print(a | b) # Union
print(a - b) # Difference

print()

# Duplicates are removed in a set.
print(c)

print()

# add() and remove() change a set.
print(a)
a.add(100)
print(a)
a.remove(2)
print(a)
