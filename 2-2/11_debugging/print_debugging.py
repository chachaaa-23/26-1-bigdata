# Print values while the code is running.
numbers = [10, 20, 30]
total = 0

for number in numbers:
    print("before:", total)
    total += number
    print("add:", number)
    print("after:", total)
    print()

print("final:", total)
