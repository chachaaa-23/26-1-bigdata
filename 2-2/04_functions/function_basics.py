# A function runs only when it is called.
def my_function():
    print("Hello from a function")


my_function()

print()

# fname is a parameter in the function definition.
def print_full_name(fname):
    print(fname + " smith")


# "Emil" and "Tobias" are arguments in the function call.
print_full_name("Emil")
print_full_name("Tobias")
