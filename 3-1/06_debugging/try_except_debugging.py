# try / except shows the error without stopping the whole loop.
values = ["10", "20", "hello", "30"]

for value in values:
    try:
        print(int(value))
    except ValueError as error:
        print("cannot convert:", value)
        print(error)
