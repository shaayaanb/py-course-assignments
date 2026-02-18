# ---------------------------------------------
# لیست پیوندی یک طرفه
# ---------------------------------------------

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_first(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, x):
        new_node = Node(x)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert_after(self, x, y):
        current = self.head
        while current:
            if current.data == x:
                new_node = Node(y)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        print("not found")
