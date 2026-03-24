# Put a breakpoint on the next line in VS Code.
def double(number):
    result = number * 2
    return result


def triple(number):
    result = number * 3
    return result


def make_total(a, b):
    # Use Step Into here to go inside double().
    left = double(a)

    # Use Step Over here to run triple() without entering it.
    right = triple(b)

    total = left + right
    return total


# Use Step Into on this line first.
answer = make_total(4, 5)
print(answer)

# Use Step Out while you are inside make_total().
