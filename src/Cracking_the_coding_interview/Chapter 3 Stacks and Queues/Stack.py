from Cons import Cons


class Stack:
    # Cons Based Stack

    def __init__(self):
        self.length = 0
        self.body = None
        self.min = Stack()

    def __len__(self):
        return self.length

    def pop(self):
        if self.length > 0:
            val, self.body, self.length = self.body.head, self.body.tail, self.length - 1
            if val == self.min.peek():
                self.min.pop()
            return val
        return None

    def push(self, value):
        self.body = Cons(value, self.body)
        self.length += 1
        if self.min.is_empty():
            self.min.push(value)
        elif self.min.peek() >= value:
            self.min.push(value)

    def peek(self):
        if self.length > 0:
            return self.body.head
        else:
            return None

    def is_empty(self):
        return self.length == 0

    def min(self):
        return self.min.peek()

    def __repr__(self):
        return '{}'.format(self.body.__repr__())

    def __str__(self):
        return '{}'.format(self.body.__repr__())
