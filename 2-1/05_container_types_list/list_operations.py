# Start with one list.
a = [1, 2, 3, 4, 5]
print(a)

# Slicing makes a smaller list.
b = a[0:2]
print(b)

# append() adds one value at the end.
b.append(10)
print(b)

# + joins two lists.
c = b + [20, 30, 40]
print(c)

# pop() removes and returns a value.
d = c.pop()
print(d)
print(c)

# del removes a value by index.
del c[1]
print(c)
