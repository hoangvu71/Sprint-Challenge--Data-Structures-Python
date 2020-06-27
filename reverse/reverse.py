class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head == None and self.tail == None:
            self.head = node
            self.tail = node

        if self.head is not None:
            node.set_next(self.head)

        self.head = node
    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        while node != self.tail:
            prev = node
            node = node.next_node
            return self.reverse_list(node)
        print(node.value)

ll = LinkedList()
ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)
ll.add_to_head(4)
ll.add_to_head(5)
ll.add_to_head(6)
ll.add_to_head(7)
ll.add_to_head(8)
ll.add_to_head(9)
ll.add_to_head(10)


ll.reverse_list(ll.head, None)