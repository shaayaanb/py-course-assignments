# ---------------------------------------------
# صف ساده
# ---------------------------------------------

class Queue:

    def __init__(self, max_size=100):
        self.list = [None] * max_size
        self.front = -1
        self.rear = -1

    def insert(self, x):
        if self.rear >= len(self.list) - 1:
            print("Queue is Full")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.list[self.rear] = x

    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return

        value = self.list[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        return value

# ---------------------------------------------
# صف حلقوی
# ---------------------------------------------

class CircularQueue:

    def __init__(self, max_size=100):
        self.list = [None] * max_size
        self.front = -1
        self.rear = -1

    def insert(self, x):
        if (self.rear + 1) % len(self.list) == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % len(self.list)

        self.list[self.rear] = x

    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return

        value = self.list[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.list)

        return value