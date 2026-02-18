# ---------------------------------------------
# پیاده سازی پشته
# ---------------------------------------------

class Stack:

    def __init__(self, limit=100):
        self.stack = []
        self.limit = limit

    def push(self, x):
        if len(self.stack) >= self.limit:
            print("stack is full")
            return
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            print("stack is empty")
            return
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            print("stack is empty")
            return
        return self.stack[-1]

    def find(self, x):
        for i in range(len(self.stack)):
            if self.stack[i] == x:
                return i
        return -1

    def replace(self, x, y):
        for i in range(len(self.stack)):
            if self.stack[i] == x:
                self.stack[i] = y
