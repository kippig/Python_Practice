from Stack import Stack


class Queue:

    def __init__(self):
        self.length = 0
        self.inStack = Stack()
        self.outStack = Stack()

    def add(self, item):
        self.inStack.push(item)
        self.length += 1

    def remove(self):
        if self.length > 0:
            if self.outStack.is_empty():
                self.flow()
            self.length -= 1
            return self.outStack.pop()
        else:
            return None

    def peek(self):
        if self.length > 0:
            if self.outStack.is_empty():
                self.flow()
            return self.outStack.peek()
        else:
            return None

    def is_empty(self):
        return self.length == 0

    def __repr__(self):
        pass

    def __len__(self):
        return self.length

    def flow(self):
        while not self.inStack.is_empty():
            self.outStack.push(self.inStack.pop())
