class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, item):
        if self.full() == False:
            self.items.append(item)
        else:
            return Exception("Stack is full")

    def pop(self):
        if self.isEmpty() == True:
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return self.size() - self.items.index(target) - 1
        else:
            return -1
