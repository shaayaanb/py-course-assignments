class CircularQueue:

    def __init__(self, max=100):
        self.Q = [None] * max
        self.front = -1
        self.rear = -1
        self.max = max

    def insertC(self, x):
        self.FQ_errCheckC()
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.max
        self.Q[self.rear] = x

    def deleteC(self):
        self.EQ_errCheckC()
        value = self.Q[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max
        return value
    
    def EQ_errCheckC(self):
        if self.front == -1:
            raise IndexError("Circular Queue is empty")

    def FQ_errCheckC(self):
        if (self.rear + 1) % self.max == self.front:
            raise IndexError("Circular Queue is full")

    def sizeC(self):
        if self.front == -1:
            return 0
        return (self.rear - self.front + self.max) % self.max + 1

    def show(self):
        if self.front == -1:
            print("empty queue")
            return

        for k in range(self.sizeC()):
            index = (self.front + k) % self.max
            print(self.Q[index], end=" ")
        print()
