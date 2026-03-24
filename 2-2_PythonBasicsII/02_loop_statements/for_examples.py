# A for loop can add values in a list.
nums = [1, 2, 3, 4, 5]
animals = ["Tadpole", "Frog", "Catfish"]

total = 0

for n in nums:
    total = total + n

print(total)

print()

# A for loop can also read each item one by one.
i = 1

for animal in animals:
    print("Item {} is {}".format(i, animal))
    i += 1

print()

# range() is useful when you need numbers in order.
for i in range(3):
    print(i)
