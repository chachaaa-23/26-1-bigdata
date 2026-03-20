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

    def insert_after(self, target, data):
        current_node = self.head
        while current_node:
            if current_node.data == target:
                new = Node(data)
                new.next = current_node.next
                current_node.next = new
                return True
            current_node = current_node.next
        return False

    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print('None')


if __name__ == '__main__':
    linked_list = LinkedList()

    for i in ('BusStop-A', 'BusStop-B', 'BusStop-C', 'BusStop-D', 'BusStop-E', 'BusStop-F'):
        linked_list.append(i)
    linked_list.show()

    linked_list.insert_after('BusStop-C', 'BusStop-C-2')
    linked_list.show()
