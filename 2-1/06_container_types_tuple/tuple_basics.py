# A tuple uses parentheses.
a = (1, 2, 3)

# Print a tuple and its length.
print(a)
print(tuple([1, 2, 3]))

print()

print(len(a))

# A one-item tuple needs a comma.
b = ()
c = (1,)
d = (1, 2, 3)
e = 1, 2, 3
f = ("a", "b", ("ab", "cd"))

print(b)
print(c)
print(d)
print(e)
print(f)

print()

# Tuples can also be unpacked.
x, y, z = a
print(x)
print(y)
print(z)
