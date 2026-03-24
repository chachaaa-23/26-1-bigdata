# A basic if / else example.
a = 100

if a > 50:
    print("Greater than 50")
else:
    print("50 or smaller")

# elif checks another condition.
b = 200

if b > 250:
    print("Greater than 250")
elif b >= 220:
    print("220 or greater")
else:
    print("Smaller than 220")

# and joins two conditions.
c = 400

if c > 100 and c < 500:
    print("Between 100 and 500")

# == checks whether two values are equal.
d = 10

if d == 10:
    print("Equal to 10")
