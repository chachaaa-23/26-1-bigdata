class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()


if __name__ == '__main__':
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.items)

    stack.pop()
    print(stack.items)

    stack.pop()
    print(stack.items)

    stack.push(5)
    stack.push(6)
    stack.push(7)
    print(stack.items)

    stack.pop()
    print(stack.items)
