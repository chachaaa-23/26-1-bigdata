class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)


if __name__ == '__main__':
    q = Queue()

    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    print(q.items)

    q.dequeue()
    print(q.items)
