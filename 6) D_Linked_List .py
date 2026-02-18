# ---------------------------------------------
# لیست دو طرفه
# ---------------------------------------------

class DNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_first(self, x):
        new_node = DNode(x)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def insert_last(self, x):
        new_node = DNode(x)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current
