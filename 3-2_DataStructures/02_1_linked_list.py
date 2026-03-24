class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data)

    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')


if __name__ == '__main__':
    linked_list = LinkedList()

    for i in (10, 15, 20, 25, 100, 5, 30, 45):
        linked_list.append(i)

    linked_list.show()
