class Stack:

    def __init__(self, limit=100):
        self.stack = []
        self.limit = limit

    def push(self, data ):
        self.FS_errCheck()
        self.stack.append(data)

    def pop(self):
        self.ES_errCheck()
        return self.stack.pop()

    def peek(self):
        self.ES_errCheck()
        return self.stack[-1]

    def find(self ,x ):
        for i in range(self.size()):
            if self.stack[i] == x:
                return i
        return -1

    def replace_all(self ,x ,y ):
        for i in range(self.size()):
            if self.stack[i] == x:
                self.stack[i] = y

    #↑↑↑↑↑↑↑↑↑↑↑↑↑↑_Class  methods_↑↑↑↑↑↑↑↑↑↑↑↑↑↑
    #--------------------------------------------
    #↓↓↓↓↓↓↓↓↓↓↓↓↓↓_Custom methods_↓↓↓↓↓↓↓↓↓↓↓↓↓↓

    def is_empty(self):
        return self.size() == 0
    
    def is_full(self):
        return self.size() >= self.limit

    def FS_errCheck(self):
        if self.size() >= self.limit:
            raise IndexError ("stack is full")

    def ES_errCheck(self):
        if self.size() == 0:
            raise IndexError ("stack is empty")
    
    def size(self):
        return len(self.stack)

    def find_middle(self):
        self.ES_errCheck()
        return self.stack[self.size()//2]

    def clear(self):
        self.stack.clear()

    def replace_first(self ,x ,y ):
        indx = self.find(x)
        if indx != -1:
            self.stack[indx] = y
        return -1

    def show(self):
        for i in range(self.size() -1, -1 ,-1 ):
            print(self.stack[i] ,end=" " )
        
    def display(self):
        for i in range(self.size()):
            print(self.stack[i] ,end=" " )

    def rev_stack(self):

        S1 = Stack(self.limit)
        S2 = Stack(self.limit)

        while self.size() > 0 :
            S1.push(self.pop())

        while S1.size() > 0 :
            S2.push(S1.pop())

        while S2.size() > 0 :
            self.push(S2.pop())

