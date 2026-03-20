class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)


if __name__ == '__main__':
    q = Queue()

    q.enqueue('Document-1')
    q.enqueue('Document-2')
    q.enqueue('Document-3')
    print(q.items)

    q.dequeue()
    print(q.items)

    q.enqueue('Document-4')
    q.dequeue()
    q.enqueue('Document-5')
    print(q.items)

    q.dequeue()
    q.dequeue()
    print(q.items)

