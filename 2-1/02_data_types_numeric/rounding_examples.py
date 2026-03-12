import math


# Save numbers for rounding.
a = 1.5
b = 1.4
c = 1.246
d = 1.245
e = 8.5
f = 9.5

# round() makes numbers shorter.
print(round(a))
print(round(b))
print(round(c, 2))
print(round(d, 2))

print()

# .5 values can round in a surprising way. (Banker's rounding -> rounding to the nearrest even number)
print(round(e))
print(round(e, 0), type(round(e, 0)))
print(round(f))
print(round(f, 0), type(round(f, 0)))

print()

# ceil() rounds up and floor() rounds down.
print(math.ceil(b)) # round a number up to the nearest whole number
print(math.floor(a))# round a number down to the nearest whole number

print()

# format() can control how many decimal places are shown.
print(format(c, ".2f"))
