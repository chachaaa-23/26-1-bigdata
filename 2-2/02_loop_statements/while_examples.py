# A while loop repeats while a condition is true.
print("Add the numbers from 1 to 10")

total = 0
n = 1

while n <= 10:
    total += n
    n += 1

print(total)

print()

# break can stop a loop early.
n = 1

while True:
    print(n)
    n += 1

    if n == 5:
        break

print("Done")
