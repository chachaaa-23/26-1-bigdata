# assert stops the program when a condition is false.
def average(numbers):
    assert len(numbers) > 0, "numbers should not be empty" #false case
    return sum(numbers) / len(numbers)


print(average([10, 20, 30]))
assert average([10, 20, 30]) == 20
print("check passed")
