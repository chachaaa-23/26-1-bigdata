# Save a few numbers.
a = 10 # whole number
b = 20.5 # value has a decimal point
c = 40.5
d = 3

# Basic arithmetic.
print(a + a, type(a + a)) # additiopn
print(a - b, type(a - b)) # subtraction
print(a * c, type(a * c)) # multiplication
print(a / d, type(a / d)) # division

print()

# // gives the quotient and % gives the remainder.
print(a // d, type(a // d))
print(a % d, type(a % d))

print()

# **(double asterisk) means "to the power of".
print(b ** d, type(b ** d))

# Scientific notation is also common in Python.
print(2.1e3, type(2.1e3))

print()

# Type conversion is another important idea.
print(int(b), type(int(b)))
print(float(a), type(float(a)))
