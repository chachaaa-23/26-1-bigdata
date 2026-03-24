class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()


if __name__ == '__main__':
    text = "Have a nice day"

    stack = Stack()

    for ch in text:
        stack.push(ch)

    result = ""
    for _ in range(len(stack.items)):
        result += stack.pop()

    print(result)
