from .Cons import Cons


class Stack:
    # Cons Based Stack

    def __init__(self, minimum=False, iterable=None):
        self.length = 0
        self.body = None
        if minimum:
            self.minimum = Stack()
        if iterable is not None:
            for i in iterable:
                self.push(i)

    def __len__(self):
        return self.length

    def pop(self):
        if self.length > 0:
            val, self.body, self.length = self.body.head, self.body.tail, self.length - 1
            if hasattr(self, 'minimum'):
                if val == self.minimum.peek():
                    self.minimum.pop()
            return val
        return None

    def push(self, value):
        self.body = Cons(value, self.body)
        self.length += 1
        if hasattr(self, 'minimum'):
            if self.minimum.is_empty():
                self.minimum.push(value)
            elif self.minimum.peek() >= value:
                self.minimum.push(value)

    def peek(self):
        if self.length > 0:
            return self.body.head
        else:
            return None

    def is_empty(self):
        return self.length == 0

    def min(self):
        if hasattr(self, 'minimum'):
            return self.minimum.peek()

    def __repr__(self):
        return '{}'.format(self.body.__repr__())

    def __str__(self):
        return '{}'.format(self.body.__repr__())
