# Keyword arguments do not depend on order.
def youngest_child(child3, child2, child1):
    print("The youngest child is " + child3)


youngest_child(child1="Emil", child2="Tobias", child3="Linus")

print()

# A default value is used when no argument is given.
def print_country(country="Norway"):
    print("I am from " + country)


print_country("India")
print_country()

print()

# return sends a value back to the caller.
def times_five(x):
    return (5 * x, "haha") #tuple 로 결과 출력하기

aaa, bbb = times_five(3)
print(aaa, bbb)

print(times_five(3))
print(times_five(5))
print(times_five(9))
