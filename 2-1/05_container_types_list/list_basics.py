# Make a few simple lists.
a = []
b = [1, 2, 3]
c = ["Life", "is", "short"]
d = [1, 2, "Life"]
e = [1, 2, ["Life", "is"]]
f = list((1, 2, 3))

# Print the lists.
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print()

# Read values from a nested list.
print(e[2])
print(e[2][0])
print(e[2][1])

print()

# len() and negative indexes are useful.
print(len(b))
print(b[-1])
