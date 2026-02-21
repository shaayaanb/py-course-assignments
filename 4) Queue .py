class Queue:

    def __init__(self, max=100):
        self.Q = [None] * max
        self.front = -1
        self.rear = -1
        self.max = max

    def insert(self ,x ):
        self.FQ_errCheck()
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.Q[self.rear] = x

    def delete(self):
        self.EQ_errCheck()
        value = self.Q[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return value

    def show(self):
        if self.front == -1 or self.front > self.rear:
            print("empty queue")
            return

        for i in range(self.front, self.rear + 1):
            print(self.Q[i], end=" ")
        print()

    def EQ_errCheck(self):
        if self.front == -1 or self.front > self.rear:
            raise IndexError("Queue is empty")

    def FQ_errCheck(self):
        if self.rear == self.max - 1:
            raise IndexError ("Queue is full")
